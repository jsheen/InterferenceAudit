# Interference audit: summary

Model: `claude-opus-5-5`. Input: [`00_input.md`](00_input.md) · Your ideas: [`00_ideas.md`](00_ideas.md)

## Plan 1: Plan-coordinated Games Family → All Access Family upgrade

**Idea:** Test whether nudging the whole Games Family plan in the same week produces more upgrades to All Access Family than nudging the owner alone, after controlling for message volume. Members also get a one-tap way to ask the owner.

**Outcomes promoted:** Revenue (primary: plan upgraded within 8 weeks), engagement on newly unlocked products, and retention as a guardrail (plan cancellation hazard).

**Mechanism:**
- Owners get email, in-app and push upsells.
- Members get an in-app card, plus push or email only with their own consent.
- Members of treated plans see a "Request All Access for our plan" paywall button. It sends the owner a weekly digest containing only a count of requests.
- Cluster: plan_id, frozen at entry.

**Why cluster-level:** Only the owner can buy, but members hold much of the demand. Member-level randomization would understate the effect, because control seats also get access when the plan upgrades.

**Design:**
- Arms: control, owner-only, owner-only with the same number of messages as the coordinated arm, request button only, and coordinated all-seat treatment.
- A separate half of plans is randomized seat by seat. This measures how much a standard user-level test would understate the effect.
- Analysis is at the plan level, with Holm adjustment across contrasts.

**Size needed:** Inputs are assumptions (1.0% baseline, +0.5pp).
- 5 arms: about 110k eligible plans. 3 arms: about 62k.
- At +1pp: about 32.9k (5 arms) or 18.5k (3 arms).
- The coordination contrast needs about 15.3k plans per arm and is the weakest-powered question.
- The plan count is undisclosed. Below 19k plans the plan says to run only a directional pilot.

**Caveats:**
- Prices are unverified ($34 vs $30; current Games Family price).
- Intro-price eligibility is unverified. If owners get the $8 intro, an upgrade means −$26 in year 1.
- Member paywall-hit volume is unknown.
- Members may not be able to see who the owner is.
- Plan_id may not persist through an upgrade.
- The digest may legally count as marketing mail.

## Plan 2: Plan challenge and idle-seat reactivation

**Idea:** Reduce whole-plan cancellation with two levers: a synchronized weekly leaderboard challenge sent to every seat, and nudges to seats that have gone idle.

**Outcomes promoted:** Retention (primary: plan cancellation hazard), engagement (leading metric: active seats per plan per week), and revenue (churn-driven only).

**Mechanism:**
- Monday challenge push and Sunday recap to all seats.
- Idle-seat nudge after 14 days without activity, sent by push, then email, then in-app, subject to each member's consent and frequency caps.
- Applies to Games Family and All Access Family plans.
- Cluster: plan_id.

**Why cluster-level:** The shared leaderboard makes play complementary across seats, and cancellation is a plan event. Seat-level tests understate the effect, and measuring retention per member is mis-specified.

**Design:**
- 2×2 factorial: challenge yes/no × idle nudge yes/no.
- A 20% audit share randomized by seat.
- Cox model for cancellation; CUPED-adjusted active seats.
- Engagement is pre-registered as a surrogate for churn, with a plan to validate it.

**Size needed:** Inputs are assumptions (2% 4-week churn, HR 0.90).
- About 76.5k plans with 12-week follow-up, or about 39.4k with 24 weeks.
- The interaction needs about 245k plans and is exploratory only.
- The leading metric needs about 7.9k plans.
- The plan says the primary outcome may be unpowered if baseline churn is far below 2%. Below 8k plans, it compares the full treatment with control only.

**Caveats:**
- The high-retention baseline is an executive belief, not data.
- Push fatigue.
- Non-gamers on All Access Family plans may ignore the challenge.
- Unverified: leaderboard contents and whether it links plans, push opt-in rates, plan counts.

## Plan 3: Fill the empty seats on All Access Family plans

*From the user's idea, merged with P6.*

**Idea:** Nudge owners of 2–3-person All Access Family plans to fill their open seats, preferably with people who don't already pay. Every invitee's outcome is credited to the owner's arm.

**Outcomes promoted:**
- Retention is the primary outcome (plan cancellation hazard).
- Revenue is co-primary for the decision (net revenue per cluster).
- Engagement is secondary (seats with access, cluster engagement).

**Mechanism:**
- All messaging goes to owners, since only the owner can invite: email, an in-app card, and a reminder.
- Optional wave-2 arm: members get an in-app "suggest someone" card that reuses Plan 1's digest.
- Randomized by plan_id. The analysis cluster is the plan plus everyone who joins it.

**Why cluster-level:** The owner is treated, but outcomes land on invitees and on the plan. Owner-only accounting overstates net revenue (invitees may cancel their own subscriptions) and understates engagement.

**Design:**
- Wave 1: control, a generic "open seats" nudge, and a "for someone without NYT" framing with a share link.
- Each invitee is classified by prior status (paying, free, lapsed, unknown).
- Net revenue is reported with bounds for invitees whose status can't be seen.

**Size needed:**
- Seats filled: about 1.4k plans per arm.
- Cannibalization, framing vs generic: about 5.2k per arm.
- Cancellation: about 439k plans, "almost certainly more than exist". The plan states this outcome is honestly underpowered.
- Break-even (assumption-based): fewer than about 3.1% of fills can come from paying individuals.

**Caveats:**
- Revenue sign is likely negative.
- Third-party billing is a blind spot.
- Invite links may leak publicly.
- Invitees may leave other family plans to join.
- Cotton's retention claim is a belief.
- Unverified: $34 price, invite lineage, whether invite links are single-use.

---
**Not planned:** P2 (parked); P5, P8 and P6's hold/compare screen (dropped); P3 and P7 (merged into Plan 1); P6 (merged into Plan 3).

---

## Full outputs

- [Agent 1: Interference map](01_interference.md)
- [Agent 2: Industry and literature research](02_research.md)
- [Agent 3: Prototype idea cards](03_cards.md)
- [Agent 4: Critique, ranking, and selection](04_critique.md)
- [Agent 5: Full plans for the selected prototypes](05_plans.md)
