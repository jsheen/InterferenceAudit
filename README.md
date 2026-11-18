# interferenceAudit

Companies using individual level data may not know areas where there may be interference, where treatments applied at the individual level will have better gains when applied at cluster level. Given free text description of the output metrics, mechanisms we have to optimize these metrics, and company subscription plans, this agentic workflow will identify and rank the best possible prototypes to build. A human in the loop is still needed in order to verify the output, maintaining proper skepticism since AI will still suggest things that don't make sense either for a production system, or even methodologically (it will frequently admit that it made something up). There is still no Lean certification for whether something "makes sense in production" (see "unverifiable tasks" by Arvind Narayanan).

Subsequently, a minimum viable product can then be built quickly with an agent.

## Workflow

Five agents run in sequence. Each one sees the original description and the output of every agent before it. They run on `claude-opus-5-5` at medium effort.

### Agent 1: Interference mapper (web search, up to 6)
- Looks up current prices for every product and plan, with a source for each, and corrects the description where it is wrong.
- Reads the company's own help center, FAQ or terms pages for how group and family plans work (who can invite, pay, upgrade or cancel), because press coverage often gets this wrong.
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
- If you pass your own ideas with `--ideas`, it critiques and scores them with the same rubric as Agent 3's cards. It always selects them for a full plan unless it judges an idea fundamentally unsound, in which case it says why.

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

### Feeding your own ideas directly into Agent 4

If you already have a prototype idea, put it in a text or Markdown file and pass it with `--ideas`. It skips Agent 3 and goes straight to Agent 4, which critiques it alongside Agent 3's cards, then to Agent 5, which writes the full plan.

```bash
.venv/bin/python -m interference_audit.pipeline inputs/nyt.md --ideas inputs/nyt_idea_111826.md
```

To try an idea without rerunning the research, start a new run directory, copy `01_interference.md`, `02_research.md` and `03_cards.md` from an earlier run into it, and pass `--run-dir`. Only Agents 4 and 5 will run, which takes about 8-10 minutes.


## Example: The New York Times

Output from a full run: [`examples/nyt/`](examples/nyt/). The final plans are in [`05_plans.md`](examples/nyt/05_plans.md), Agent 4's ranking is in [`04_critique.md`](examples/nyt/04_critique.md), and everything is combined in [`report.md`](examples/nyt/report.md). Prices and other facts in it are as the agents found them on 2026-11-18. Check what is marked unverified before relying on it.

A second run fed the user idea in [`inputs/nyt_idea_111826.md`](inputs/nyt_idea_111826.md) (fill the empty seats on Family All Access plans with 2 or 3 members) directly to Agents 4 and 5, reusing the first run's Agents 1-3: [`examples/nyt_idea_111826/`](examples/nyt_idea_111826/). Its plan for the idea is Plan 3 in [`05_plans.md`](examples/nyt_idea_111826/05_plans.md). Agents 4 and 5 took 2 min 54 s and about 8 min. Both examples predate Agent 1 reading the company's help center, so their Agents 1-3 still say any member can invite; Agent 4 corrects this.

### Run time

Measured on the NYT example, running on a Claude subscription via Claude Code, at medium effort with the search caps above:

| Agent | Time | Model turns |
|---|---|---|
| 1. Interference mapper | 2 min 58 s | 12 |
| 2. Researcher | 3 min 41 s | 31 |
| 3. Idea generator (cards) | 1 min 7 s | 1 |
| 4. Critic and selector | 3 min 8 s | 13 |
| 5. Plan writer | 5 min 10 s | 1 |
| **Total** | **about 16 min** | |

Agents 1-2 ran in one session and Agents 3-5 in a second, which reused Agents 1-2's output since their prompts had not changed. The total is the sum of the five agents; the script's own overhead between agents was a few seconds. Agent 5 is the slowest because it writes the most. Times will vary with the input and with load.

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

## Plan rules (from NYT's own help center; Agent 1 should read this page)
Source: https://thenewyorktimeshelpcenter.helpjuice.com/115002788207-Subscriptions/family-subscription (checked 2026-11-18)
- Only the primary subscriber can manage the family subscription: invites, billing, and cancellation. Other members can manage only their own account information.
- The plan gives access to up to three additional subscribers. The primary invites them by email or by sending an invitation link.
- The primary removes a member with "Revoke".
- Existing subscribers can upgrade in their account. Anyone billed through a third party (App Store, Google) must cancel there before buying a family subscription.
- Home Delivery and some All Access subscriptions can add extra people as "Bonus subscriptions", managed the same way as family subscriptions.
- The page does not say whether members must live together, or who is eligible for intro pricing.
```
