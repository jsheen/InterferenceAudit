"""Five-agent interference-audit workflow.

Stages (each one is a Claude call; outputs are saved as Markdown):
  1. interference  - map units, levers, and interference channels; verify prices (web)
  2. research      - industry precedent and causal-inference literature per channel (web)
  3. cards         - short prototype idea cards
  4. critique      - fact/citation spot-check, critique, ranking, and selection of 2-3 winners (web)
  5. plans         - full experiment plans for the selected prototypes only

Usage:
  python -m interference_audit.pipeline inputs/nyt.md
  python -m interference_audit.pipeline inputs/nyt.md --run-dir runs/20261118-1200   # resume
  python -m interference_audit.pipeline inputs/nyt.md --ideas my_ideas.md            # add your own ideas
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import anthropic

from . import prompts

MODEL = "claude-opus-5-5"
MAX_TOKENS = 64000
EFFORT = "medium"  # low | medium | high | xhigh | max
MAX_CONTINUATIONS = 10  # resumes after pause_turn (long server-tool turns)


@dataclass
class Stage:
    key: str
    title: str
    system: str
    web_searches: int  # max web_search uses for this stage (0 = no web tools)


STAGES = [
    Stage("01_interference", "Agent 1: Interference map", prompts.AGENT1_INTERFERENCE, 6),
    Stage("02_research", "Agent 2: Industry and literature research", prompts.AGENT2_RESEARCH, 15),
    Stage("03_cards", "Agent 3: Prototype idea cards", prompts.AGENT3_PROTOTYPES, 0),
    Stage("04_critique", "Agent 4: Critique, ranking, and selection", prompts.AGENT4_CRITIC, 8),
    Stage("05_plans", "Agent 5: Full plans for the selected prototypes", prompts.AGENT5_PLANS, 0),
]


def web_tools(max_searches: int) -> list[dict]:
    if max_searches <= 0:
        return []
    return [
        {"type": "web_search_20260209", "name": "web_search", "max_uses": max_searches},
        {"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": max_searches},
    ]


def run_agent(client: anthropic.Anthropic, stage: Stage, user_content: str) -> tuple[str, list[tuple[str, str]]]:
    """Run one agent to completion. Returns (markdown text, [(title, url)] cited sources)."""
    messages: list = [{"role": "user", "content": user_content}]
    texts: list[str] = []
    sources: dict[str, str] = {}

    for _ in range(MAX_CONTINUATIONS + 1):
        with client.beta.messages.stream(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=stage.system,
            messages=messages,
            tools=web_tools(stage.web_searches),
            thinking={"type": "adaptive"},
            output_config={"effort": EFFORT},
            # Re-run on a fallback model if a safety classifier declines the request.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        ) as stream:
            response = stream.get_final_message()

        for block in response.content:
            if block.type == "text":
                texts.append(block.text)
                for c in getattr(block, "citations", None) or []:
                    url = getattr(c, "url", None)
                    if url:
                        sources.setdefault(url, getattr(c, "title", None) or url)

        if response.stop_reason == "pause_turn":
            # Long server-tool turn: send it back so the server continues where it stopped.
            messages.append({"role": "assistant", "content": response.content})
            continue
        if response.stop_reason == "refusal":
            raise RuntimeError(f"{stage.title}: request was declined ({response.stop_details}).")
        if response.stop_reason == "max_tokens":
            print(f"  warning: {stage.title} hit max_tokens; output is truncated.", file=sys.stderr)
        u = response.usage
        print(f"  tokens in={u.input_tokens} out={u.output_tokens}", file=sys.stderr)
        break
    else:
        print(f"  warning: {stage.title} still paused after {MAX_CONTINUATIONS} continuations.", file=sys.stderr)

    return "".join(texts).strip(), [(t, u) for u, t in sources.items()]


def run_agent_claude_code(stage: Stage, user_content: str) -> tuple[str, list[tuple[str, str]]]:
    """Run one agent through headless Claude Code (`claude -p`), which uses your Claude subscription."""
    tools = "WebSearch,WebFetch" if stage.web_searches > 0 else ""
    cmd = [
        "claude", "-p",
        "--model", MODEL,
        "--effort", EFFORT,
        "--system-prompt", stage.system,
        "--tools", tools,
        "--output-format", "json",
        "--no-session-persistence",
    ]
    if tools:
        cmd += ["--allowedTools", "WebSearch", "WebFetch"]
    # Drop API-key variables so Claude Code bills the logged-in subscription, not the API.
    env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")}
    proc = subprocess.run(cmd, input=user_content, capture_output=True, text=True, env=env)
    if proc.returncode != 0:
        raise RuntimeError(f"{stage.title}: claude -p failed ({proc.returncode}):\n{proc.stderr or proc.stdout}")
    data = json.loads(proc.stdout)
    if data.get("is_error"):
        raise RuntimeError(f"{stage.title}: {data.get('result')}")
    print(f"  turns={data.get('num_turns')} duration={data.get('duration_ms', 0) / 1000:.0f}s", file=sys.stderr)
    return (data.get("result") or "").strip(), []


IDEA_STAGES = ("04_critique", "05_plans")  # user ideas skip the idea generator and go straight to these


def build_input(stage: Stage, description: str, prior: dict[str, str], ideas: str | None = None) -> str:
    parts = [f"<company_description>\n{description.strip()}\n</company_description>"]
    if ideas and stage.key in IDEA_STAGES:
        parts.append(f"<user_ideas>\n{ideas.strip()}\n</user_ideas>")
    for earlier in STAGES:
        if earlier.key in prior:
            parts.append(f'<stage name="{earlier.title}">\n{prior[earlier.key]}\n</stage>')
    if stage.web_searches > 0:
        # The API backend enforces this with max_uses; Claude Code has no cap flag, so state it.
        parts.append(f"Budget: use at most {stage.web_searches} web searches and {stage.web_searches} page fetches. "
                     "Prioritize the highest-value lookups.")
    parts.append(f"Today's date is {dt.date.today().isoformat()}. Do your stage now.")
    return "\n\n".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("description", type=Path, help="Text/Markdown file describing products and levers")
    ap.add_argument("--run-dir", type=Path, help="Existing run directory to resume (finished stages are skipped)")
    ap.add_argument("--ideas", type=Path,
                    help="Text/Markdown file of your own prototype ideas, fed directly to Agents 4 and 5")
    ap.add_argument(
        "--backend", choices=["auto", "api", "claude-code"], default="auto",
        help="api = Anthropic API key (billed per token); claude-code = `claude -p` on your Claude subscription; "
             "auto = api if ANTHROPIC_API_KEY is set, else claude-code",
    )
    args = ap.parse_args()

    backend = args.backend
    if backend == "auto":
        backend = "api" if os.environ.get("ANTHROPIC_API_KEY") else "claude-code"
    if backend == "claude-code" and not shutil.which("claude"):
        sys.exit("Claude Code CLI (`claude`) not found on PATH; install it or use --backend api.")
    print(f"Backend: {backend}", file=sys.stderr)

    description = args.description.read_text()
    run_dir = args.run_dir or Path("runs") / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "00_input.md").write_text(description)
    ideas = args.ideas.read_text() if args.ideas else None
    if ideas:
        (run_dir / "00_ideas.md").write_text(ideas)

    client = anthropic.Anthropic() if backend == "api" else None
    outputs: dict[str, str] = {}

    for stage in STAGES:
        out_path = run_dir / f"{stage.key}.md"
        if out_path.exists():
            print(f"[skip] {stage.title} (found {out_path})", file=sys.stderr)
            outputs[stage.key] = out_path.read_text()
            continue
        print(f"[run]  {stage.title}", file=sys.stderr)
        prompt = build_input(stage, description, outputs, ideas)
        if backend == "api":
            text, sources = run_agent(client, stage, prompt)
        else:
            text, sources = run_agent_claude_code(stage, prompt)
        if sources:
            text += "\n\n---\n### Sources cited by web search\n" + "\n".join(f"- [{t}]({u})" for t, u in sources)
        out_path.write_text(text)
        outputs[stage.key] = text

    report = [f"# Interference audit\n\nInput: `{args.description}`  \nModel: `{MODEL}`\n"]
    if ideas:
        report.append(f"\n\n# User ideas (fed to Agents 4 and 5)\n\n{ideas.strip()}")
    report += [f"\n\n# {s.title}\n\n{outputs[s.key]}" for s in STAGES]
    (run_dir / "report.md").write_text("".join(report))
    print(f"Done. Report: {run_dir / 'report.md'}", file=sys.stderr)


if __name__ == "__main__":
    main()
