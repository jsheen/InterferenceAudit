# interferenceAudit

Companies using individual level data may not know areas where there may be interference, where treatments applied at the individual level will have better gains when applied at cluster level. Given free text description of the output metrics, mechanisms we have to optimize these metrics, and company subscription plans, this agentic workflow will identify and rank the best possible prototypes to build. A human in the loop is still needed in order to verify the output, maintaining proper skepticism since AI will still suggest things that don't make sense either for a production system, or even methodologically (it will frequently admit that it made something up). And with regards to the former, there is still no Lean certification for whether something "makes sense in production."

Subsequently, a minimum viable product can then be built quickly with an agent.

## Workflow

| Stage | Agent | Web search | Output |
|---|---|---|---|
| 1 | Interference mapper: units, levers × outcomes, interference channels, verified prices | yes | `01_interference.md` |
| 2 | Researcher: tech-industry precedent and causal-inference literature for each channel | yes | `02_research.md` |
| 3 | Prototype designer: cluster-level treatments and designs, with estimands, power sketch, and MVP plan | no | `03_prototypes.md` |
| 4 | Critic: checks citations and prices, critiques each prototype, scores and ranks them | yes | `04_critique.md` |

Each agent sees the original description and the output of every stage before it. Stages run on `claude-opus-5-5` with adaptive thinking.

## Usage

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m interference_audit.pipeline inputs/nyt.md
```

By default it runs each agent through Claude Code (`claude -p`), which uses your Claude subscription. If `ANTHROPIC_API_KEY` is set, it calls the Anthropic API directly instead (billed per token). Use `--backend claude-code` or `--backend api` to choose explicitly.

Results go to `runs/<timestamp>/` (each stage, plus `report.md` with all four). If a run stops partway, pass `--run-dir runs/<timestamp>` to resume. Stages that already finished are skipped, and you can delete a stage's file to rerun only that stage. Prompts are in `interference_audit/prompts.py`.
