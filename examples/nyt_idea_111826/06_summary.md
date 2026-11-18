## Bottom line

- **Build Plan 1 first**: the plan-coordinated Games Family → All Access Family upgrade (P1 + P3, with P7 as an audit arm). It scored highest (4.25). It also builds the shared data foundation and the member → owner request flow that Plan 3 reuses. Only the plan owner can buy (verified, Help Center), so a request button is the only in-product route from member demand to a purchase.
- **Run Plan 2** (plan retention) in parallel on its own layer. **Start Plan 3** (filling empty seats) once the invitee-status classifier is validated.
- **Biggest caveat:** NYT does not disclose how many family plans it has, so no design can yet be checked for power. Also **unverified**: whether owners get the $8 intro price when they upgrade. That decides the sign of year-1 revenue per upgrading plan: −$26 if they do, +$312 if not (assumptions).

## By outcome

### Engagement
- **Mechanisms on the plan:**
  - Plan 2: a synchronized weekly leaderboard challenge sent to every seat, plus idle-seat nudges (push, then email, then in-app).
  - Plan 1: member in-app cards and consented push or email, which drive use of newly unlocked products.
  - Plan 3: owner nudges that add seats, measured as total cluster engagement.
- **Why the plan beats individuals:** the shared leaderboard makes play complementary across seats. A seat-randomized test **understates** the effect, because control seats see treated rivals.
- **Primary or not:** no plan has engagement as its primary outcome. Plan 2 uses active seats per plan per week as a pre-registered leading surrogate. That metric is well powered: about 7,900 plans in the factorial (assumptions). In Plans 1 and 3 engagement is secondary.

### Retention
- **Mechanisms on the plan:** Plan 2's challenge and idle-seat push, and Plan 3's owner email and in-app "open seats" nudges.
- **Why the plan beats individuals:** churn is a plan event that the owner decides, so per-member retention is mis-specified.
- **Primary or not:** primary in Plans 2 and 3; a guardrail in Plan 1.
- **Measurability:**
  - Plan 2 needs about 39,400 eligible plans for a 24-week readout. This assumes 2% churn per 4 weeks and a hazard ratio of 0.90.
  - Plan 3 needs about 439,000 plans, which is likely more than exist (inference). Its result will be an estimate, not a test.
  - Cotton's "much less likely to cancel" is a belief, not data.

### Revenue
- **Mechanisms on the plan (Plan 1):**
  - Owner upsell by email and in-app, plus a dose-matched arm using push.
  - Member cards.
  - A count-only "Request All Access for our plan" button on member paywalls.
  - Offer prices are held fixed across arms.
- **Why the plan beats individuals:** the owner pays, but members hold the demand. A member-randomized test **understates** the effect, because control seats share the upgrade.
- **Primary or not:**
  - Plan 1: upgrade within 8 weeks is the primary outcome.
  - Plan 3: net revenue (invitee cannibalization netted out) is co-primary for the decision. It breaks even only if fewer than about 3.1% of fills come from people who already pay (assumptions).
  - Plan 2: churn-driven revenue is secondary.
- **Measurability (Plan 1):** about 110k plans for 5 arms, or about 62k for 3 arms, at δ = 0.5pp. At δ = 1pp, about 18.5k–32.9k. The coordination contrast (C vs A′) is the weakest-powered question, at 15,333 plans per arm.

**Levers no selected plan uses:** home-page recommendations, and personalized paywall *pricing*.

## Selected plans

| Plan | Primary outcome | Lever(s) | Cluster | Size needed | Key risk |
|---|---|---|---|---|---|
| 1. Coordinated upgrade (P1+P3+P7) | Upgrade within 8 wk (revenue) | Owner email, in-app, push; member cards; paywall request button | Games Family plan_id | ≈110k (5-arm) / ≈62k (3-arm); ≈18.5k at δ = 1pp | Plan count unknown; intro-price anomaly |
| 2. Plan challenge + idle seats (P4) | Plan cancellation hazard | Push, email, in-app | Games Family and All Access Family plan_id | ≈39.4k (24 wk) / ≈76.5k (12 wk) | Retention ceiling; push fatigue |
| 3. Fill empty seats (U1+P6) | Plan cancellation; net revenue for the decision | Owner email, in-app, share link; optional member card | All Access Family plan + invitees (ego cluster) | Fills: ≈1.4k/arm; cancellation: ≈439k | Cannibalization; third-party blind spot |

## Ranking

- P1: 4.25, kept (absorbs P3 and P7) → Plan 1
- P4: 3.80, kept → Plan 2
- **U1 (user idea): 3.55, kept, merged with P6** → Plan 3
- P6: 3.35, merged into U1
- P3: 3.25, merged into P1
- P7: 3.20, merged as audit arms
- P2: 3.05, parked
- P8: 2.40, dropped (wrong cluster, too few DMAs)
- P5: 2.35, dropped (privacy risk, negative revenue sign)

## Before building

1. **Plan counts** by type and seat count. These set the arm counts, the layer split, and whether any churn-primary design is feasible.
2. **Prices and eligibility.** Is All Access Family $34 (**unverified**) or $30? What are the current Games Family price and billing period? Do owners get the intro price on upgrade?
3. **NYT's current randomization unit.** If tests are already plan-hashed, the audit arms teach less.
4. **Consent and legal status.** Do member email and push need separate consent? Are request digests and invitation emails transactional or marketing?
5. **Lineage.** Does plan_id persist through an upgrade? Is invite → redemption logged? Can Apple and Google subscriptions be linked to accounts?