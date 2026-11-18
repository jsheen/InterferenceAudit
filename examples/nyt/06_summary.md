## Bottom line

- **Build Plan A (owner offer + member "Request All Access" button) and Plan B (plan challenge + interference detector) first, in parallel.** Randomize them independently. Run Plan C (whole-plan trial) only after A's 8-week read.
- **Why these:** in each one the plan is the unit that pays, uses and cancels. A goes after the +$20–24 per 4 weeks per upgraded plan (prices unverified; $34 comes from a single unconfirmed source). B tests directly whether NYT's member-level tests are biased.
- **First, the pre-launch checklist** (prices, intro eligibility, base size, randomization unit). It blocks all three plans.
- **Biggest caveat:** no one knows how many Games Family plans exist. A needs about 51k eligible plans and B about 82.7k family plans. Both figures rest on assumed baselines. Also, if owners get the $8 intro price, year-1 revenue from upgrades turns **negative**.

## By outcome

### Engagement
- **Levers:** push, in-app cards and idle-seat email (B); member in-app cards and push (A); time-boxed entitlement trials with in-app notes (C). No selected plan uses home-page recommendations.
- **Cluster:** plan_id in all three.
- **Why cluster beats individual:**
  - Shared leaderboards make play complementary across seats.
  - An upgrade unlocks products for members who were never messaged.
  - Member-level randomization therefore leaks positive spillover into control and **understates** the effect.
- **Role in the plans:** no plan has engagement as its primary outcome. It is B's leading and detector metric, and a secondary in A and C (C uses post-trial engagement only).
- **Measurable:** yes. B's MDE is about 0.054 plays/week per seat, and a detectable bias is about 0.068 plays/week (σ, ρ and seats per plan are assumptions).

### Retention
- **Levers:** synchronized weekly push and in-app challenge, plus idle-seat nudges (B).
- **Cluster:** plan_id.
- **Why cluster beats individual:** churn is a plan event. The owner may cancel when other seats go idle, so per-member retention is mis-specified.
- **Role in the plans:**
  - B: primary outcome, 26-week plan cancellation hazard.
  - A: secondary and guardrail.
  - C: co-primary non-inferiority test for the drop in access when the trial ends.
- **Measurable, but expensive:** about 18.6k plans per arm (Schoenfeld). This assumes 8% baseline churn and a −0.8 pp effect. High baseline retention may compress the effect.

### Revenue
- **Levers:**
  - A: owner email and in-app offer, a member paywall request button, and a capped request digest to the owner.
  - C: plan-wide trial followed by an owner offer.
- **Cluster:** plan_id. Net revenue R_p counts every person in the plan cluster across all billing channels (the P6 rule).
- **Why cluster beats individual:**
  - The member who wants the product is not the owner who pays.
  - Member-level tests upgrade control members, and owner-only tests miss member demand. Both **understate** the effect.
  - Revenue measured on the owner alone **overstates** net gains, because it misses cancelled standalone or invitee subscriptions.
- **Role in the plans:** the primary outcome in A and C is plan upgrade. Net R_p is a secondary and a condition in the decision rule.
- **Measurable:** the upgrade outcome, at roughly 17k plans per arm for A (p₀ = 2% assumed) and about 6k per arm for C.
  - Revenue at that scale is small: about $22k–27k/yr per 17k plans at regular price, or −$1.4k to −$2.2k in year 1 under the intro price (inference).

## Selected plans

| Plan | Primary outcome | Lever(s) | Cluster | Size needed | Key risk |
|---|---|---|---|---|---|
| A: Owner offer × member request (P1+P3) | Plan upgrade, 8 wk | Email, in-app, push (opt-in), paywall request button | Games Family plan_id (≥2 seats) | 17k/arm: 51k (3 arms), 68k (4 arms); fallbacks below 27.6k | Intro-price eligibility flips year-1 revenue; base size unknown |
| B: Plan challenge + idle-seat + detector (P4+P7) | Plan cancellation hazard, 26 wk | Push, in-app card, email (separate sending pool) | All family plan_ids; half randomized by plan, half by member | 18.6k/arm; 41.3k plan half + 41.3k member half = 82.7k | High baseline retention; low push opt-in; within-plan user hashing unverified |
| C: Whole-plan trial (P2), second wave | Upgrade 28 days post-trial; co-primary: cancellation non-inferiority | Temporary All Access entitlement, in-app notes, owner offer | Games Family plan_id | 6,024/arm, about 18.1k total | Churn when access ends; reuse of A's holdout |

## Ranking

No user-proposed ideas (U1, U2, …) appear in the critique. P1 builds on the company's own example (Games Family → All Access Family).

- P1 Coordinated upgrade push: 3.75, **merged → A**
- P7 Interference detector: 3.65, **merged → B**
- P4 Plan challenge / idle seats: 3.55, **merged → B**
- P2 Whole-plan trial: 3.45, **kept → C (second wave)**
- P3 "Ask the plan owner": 3.35, **merged → A**
- P6 Steer invites: 3.25, **dropped as a treatment** (its accounting rule is kept in all plans)
- P5 Household second-person offer: 2.05, **dropped** (privacy, likely negative net revenue, high build cost)
- P8 Geo family offer: 1.95, **dropped** (wrong cluster, too few DMAs)

## Before building

1. **Live prices and billing cycle:** is All Access Family $30 or $34, and is Games Family billed monthly or every 4 weeks? Can existing Games Family owners get the $8 intro? Together these set the sign of year-1 revenue.
2. **Base size and baselines:** number of Games Family and All Access Family plans, seat distribution, 8-week upgrade rate, and 26-week cancellation rate. All current sizing figures are assumptions.
3. **Experimentation platform:** what unit does NYT randomize on today, and can it hash on plan_id and on user_id within a plan? If tests are already plan-hashed, B's detector shrinks to a pilot.
4. **Feasibility:**
   - Is there an upgrade path for owners billed through Apple or Google?
   - What happens to members' standalone subscriptions when they upgrade?
   - Can a person be on two plans?
   - Do Games Family plans have leaderboards?
5. **Sign-off:**
   - Counsel on member-to-owner requests, minors and consent.
   - Leadership agreement to judge results on seats with access and net R_p rather than reported subscribers (a plan counts as 2 regardless of seats).