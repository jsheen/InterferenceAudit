# interferenceAudit

Companies using individual level data may not know areas where there may be interference, where treatments applied at the individual level will have better gains when applied at cluster level. Given free text description of the output metrics, mechanisms we have to optimize these metrics, and company subscription plans, this agentic workflow will identify and rank the best possible prototypes to build. A human in the loop is still needed in order to verify the output, maintaining proper skepticism since AI will still suggest things that don't make sense either for a production system, or even methodologically (it will frequently admit that it made something up). And with regards to the former, there is still no Lean certification for whether something "makes sense in production."

Subsequently, a minimum viable product can then be built quickly with an agent.

## Workflow

Five agents run in sequence on `claude-opus-5-5` (medium effort), each seeing the description and every earlier agent's output. A short summary comes last.

| Step | Web searches | What it does | Output |
|---|---|---|---|
| 1. Interference mapper | up to 6 | Checks prices and the company's own plan rules (who can invite, pay, cancel); maps units, levers × outcomes, and interference channels, with the bias each causes in an individual-level A/B test | `01_interference.md` |
| 2. Researcher | up to 15 | Finds how other tech companies handled each channel, and the relevant causal inference literature; flags unverified citations | `02_research.md` |
| 3. Idea generator | none | Writes 6-10 short prototype cards (cluster-level treatments or measurement designs) | `03_cards.md` |
| 4. Critic and selector | up to 8 | Spot-checks facts and citations, critiques and scores each card, ranks them, and picks the top 2-3 with a brief for each | `04_critique.md` |
| 5. Plan writer | none | Full plans for the picks only: arms, cluster, design, estimands, metrics, power math shown step by step, build plan, decision rule | `05_plans.md` |
| Summary | none | Summarizes each planned prototype without ranking or recommending: the idea, which outcomes it promotes (engagement, retention, revenue), levers and cluster, why cluster-level, design, size needed, caveats | `report.md` |

## Usage

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m interference_audit.pipeline inputs/nyt.md
```

- **Billing:** runs through Claude Code (`claude -p`) on your Claude subscription by default, or the Anthropic API if `ANTHROPIC_API_KEY` is set (`--backend` to choose).
- **Output:** `runs/<timestamp>/`. Read `report.md` first.
- **Resume:** `--run-dir runs/<timestamp>` skips finished steps and reuses that run's recorded input. Delete a step's file to rerun just that step.
- **Your own ideas:** `--ideas my_ideas.md` sends them straight to Agents 4 and 5. Agent 4 scores them like any card and plans them unless they are unsound. To skip the research, copy `01`-`03` from an earlier run into a new `--run-dir`; Agents 4-5 then take about 8-10 minutes.
- **Prompts:** `interference_audit/prompts.py`.

## Example: The New York Times

- [`examples/nyt/`](examples/nyt/): full run.
- [`examples/nyt_idea_111826/`](examples/nyt_idea_111826/): same research plus the user idea in [`inputs/nyt_idea_111826.md`](inputs/nyt_idea_111826.md) (fill the empty seats on Family All Access plans with 2-3 members); see Plan 3.

Start with each folder's `report.md`. Facts are as found on 2026-11-18; check anything marked unverified. Both runs predate Agent 1 reading NYT's help center, so their Agents 1-3 wrongly say any member can invite (Agent 4 corrects this).

**Run time** (subscription, medium effort): Agent 1 3 min, Agent 2 3.7 min, Agent 3 1.1 min, Agent 4 3.1 min, Agent 5 5.2 min, summary under 1 min, so **about 16 min** in total.

### Raw free text

From `inputs/nyt_original.txt`. The last two paragraphs were added later; the three outcomes came from the task description.

> the new york times has the products of: individual account until hitting paywall, individual subscription to news, games, wirecutter, cooking, and the athletic (look up amounts), as well as a family all access plan where 4 people can be on the same plan (i think it is $30 but look up amount), a family game plan (4 people, i think $10). the mechanisms they can get people to go further down the pipeline are email nudges, notifications in the app, better algorithmic recommendations on the home page, push notifications, and personalized paywall
>
> one good example is nudging people on the games all access to become family all access
>
> it should be from family games to family all access the point being we are applying a treatment at cluster level

### Reorganized input

What the pipeline reads (`inputs/nyt.md`):

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
