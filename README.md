# interferenceAudit

Companies using individual level data may not know areas where there may be interference, where treatments applied at the individual level will have better gains when applied at cluster level. Given free text description of the output metrics, mechanisms we have to optimize these metrics, and company subscription plans, this agentic workflow will identify and rank the best possible prototypes to build. A human in the loop is still needed in order to verify the output, maintaining proper skepticism since AI will still suggest things that don't make sense either for a production system, or even methodologically (it will frequently admit that it made something up). And with regards to the former, there is still no Lean certification for whether something "makes sense in production."

Subsequently, a minimum viable product can then be built quickly with an agent.

## Workflow

Five agents run in sequence. Each one sees the original description and the output of every agent before it. They run on `claude-opus-5-5` at medium effort.

### Agent 1: Interference mapper (web search, up to 6)
- Looks up current prices for every product and plan, with a source for each, and corrects the description where it is wrong.
- Maps the units: free accounts, subscribers, plan members, households, sharing ties, and shared resources such as the recommendation model and email-sending reputation.
- Builds a table of which levers move which outcomes (engagement, revenue, retention).
- Lists the interference channels. For each: how one unit's treatment reaches another, the natural cluster, which way a naive individual-level A/B test is biased, how material it is, and whether treating the whole cluster could create extra value.
- Ends with a ranked shortlist of channels.

### Agent 2: Researcher (web search, up to 15)
- For each important channel, finds other tech companies that faced the same interference and what they did.
- Finds the relevant causal inference literature: cluster and graph-cluster randomization, partial interference, randomized saturation designs, bipartite interference, interference from shared models, and tests that detect interference.
- Produces a methods toolbox (design, when to use it, assumptions, cost), the gaps where it found no precedent, and a bibliography. Citations it could not verify are marked.

### Agent 3: Idea generator (no web)
- Writes 6-10 short prototype idea cards (about 150 words each): the pitch, whether it is a cluster-level treatment or a measurement design, the treatment, the cluster, why treating the cluster beats treating individuals, the outcomes moved, the main risk, and the research it rests on.
- Deliberately does not write full plans, so no effort goes into ideas that get dropped.

### Agent 4: Critic and selector (web search, up to 8)
- Spot-checks the prices, facts and citations from Agents 1-3 against sources.
- Critiques each card: is the interference real, is the method sound, are there enough clusters for power, can it be built, are there privacy or legal problems, and how much is it worth.
- Scores each card on five weighted criteria, ranks them, and says which to drop or merge.
- Selects the top 2-3 and writes a brief for each (scope, arms, required fixes, constraints, unverified facts), plus the open questions a human must answer.

### Agent 5: Plan writer (no web)
- Writes a full experiment plan for each prototype Agent 4 selected, applying Agent 4's fixes:
  - treatment arms and cluster definition
  - design, estimands and estimator
  - metrics and guardrails
  - a power calculation with the formula, every assumption and each step of the arithmetic
  - an MVP build plan
  - a decision rule
  - risks

| Agent | Output file |
|---|---|
| 1 | `01_interference.md` |
| 2 | `02_research.md` |
| 3 | `03_cards.md` |
| 4 | `04_critique.md` |
| 5 | `05_plans.md` |

## Usage

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m interference_audit.pipeline inputs/nyt.md
```

By default it runs each agent through Claude Code (`claude -p`), which uses your Claude subscription. If `ANTHROPIC_API_KEY` is set, it calls the Anthropic API directly instead (billed per token). Use `--backend claude-code` or `--backend api` to choose explicitly.

Results go to `runs/<timestamp>/` (each stage, plus `report.md` with all five). If a run stops partway, pass `--run-dir runs/<timestamp>` to resume. Stages that already finished are skipped, and you can delete a stage's file to rerun only that stage. Prompts are in `interference_audit/prompts.py`.


## Example: The New York Times

Output from a full run: [`examples/nyt/`](examples/nyt/). The final plans are in [`05_plans.md`](examples/nyt/05_plans.md), Agent 4's ranking is in [`04_critique.md`](examples/nyt/04_critique.md), and everything is combined in [`report.md`](examples/nyt/report.md). Prices and other facts in it are as the agents found them on 2026-11-18. Check what is marked unverified before relying on it.

### Raw free text

As originally written (`inputs/nyt_original.txt`). The last two paragraphs were added afterward. The three outcomes (engagement, revenue, retention) came from the task description.

> the new york times has the products of: individual account until hitting paywall, individual subscription to news, games, wirecutter, cooking, and the athletic (look up amounts), as well as a family all access plan where 4 people can be on the same plan (i think it is $30 but look up amount), a family game plan (4 people, i think $10). the mechanisms they can get people to go further down the pipeline are email nudges, notifications in the app, better algorithmic recommendations on the home page, push notifications, and personalized paywall
>
> one good example is nudging people on the games all access to become family all access
>
> it should be from family games to family all access the point being we are applying a treatment at cluster level

### Reorganized input

What the pipeline actually reads (`inputs/nyt.md`):

```markdown
# The New York Times

## Outcomes to optimize
Engagement, revenue, and retention.

## Products and plans
- Individual account (free, registered) until hitting the paywall
- Individual subscriptions: News, Games, Wirecutter, Cooking, and The Athletic (look up current prices)
- Family All Access plan: up to 4 people on one plan (believed to be about $30; look up the current price)
- Family Games plan: up to 4 people (believed to be about $10; look up the current price)

## Mechanisms to move people down the funnel
- Email nudges
- In-app notifications
- Better algorithmic recommendations on the home page
- Push notifications
- Personalized paywall

## Example of the kind of opportunity we're looking for
Nudging a Family Games plan (up to 4 members) to upgrade to Family All Access. The point is that the treatment is applied at the cluster level: the whole plan is treated together, rather than nudging members one at a time, since the upgrade decision and its payoff are shared across the plan.
```
