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


## Example: The New York Times

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
