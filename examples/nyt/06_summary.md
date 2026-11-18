## Plan 1: Plan-level upgrade, owner offer × member request

- **Idea:** Move Games Family plans to All Access Family by pairing an offer to the owner with a "Request All Access for our plan" button that members choose to use. The whole plan is treated in one 7-day window. This merges cards P1 and P3.
- **Outcomes promoted:** Revenue, engagement and retention.
  - **Primary outcome: revenue.** It is measured as the 8-week plan upgrade.
  - Engagement on unlocked products and the plan cancellation hazard are secondary.
- **Mechanism:**
  - Owners get email and in-app offers (3 touches).
  - Members get an opt-in push, an in-app card, and a paywall request button that runs for 8 weeks.
  - Owners receive request digests, capped at 1 per week and 3 in total.
  - Nothing about members' behaviour is reported passively.
  - **Cluster randomized:** plan_id, hashed and frozen at entry.
- **Why cluster-level:**
  - The member who wants the product and the owner who pays are different people.
  - An upgrade spills onto every seat, so member-level tests would understate the effect.
- **Design:**
  - Stratified arms: holdout, owner-only offer, coordinated (owner plus members), and an optional dose-matched owner arm.
  - Each policy's effect is compared with the holdout at the plan level.
  - Net revenue counts all standalone subscriptions in the cluster (the P6 rule).
- **Size needed:**
  - 17,000 plans per arm: 51k for 3 arms, 68k for 4.
  - This rests on an **assumed** 2% baseline upgrade rate and an **assumed** +0.5 pp minimum detectable effect.
  - The plan does not say the size is realistic. The eligible base is **unverified**, so it pre-registers fallbacks down to two arms or rolling enrolment.
  - It notes the build is justified only at portfolio scale or through the retention secondary.
- **Caveats:**
  - Prices and billing cycle are **unverified**. If owners get the $8 intro price, year-1 revenue turns negative.
  - Owners billed through Apple or Google face upgrade friction.
  - Paywall-hit volume per member is unknown, owners may feel nagged, and minors and consent need counsel sign-off.
  - Members' existing standalone subscriptions may be cannibalized.

## Plan 2: Plan challenge and idle-seat reactivation, with built-in interference detector

- **Idea:** A weekly synchronized "plan challenge" plus nudges to idle seats, to reduce whole-plan cancellation. Half the plans are randomized by member, which tests whether member-level tests are biased. This merges cards P4 and P7.
- **Outcomes promoted:** Retention, engagement and revenue.
  - **Primary outcome: retention**, measured as the plan cancellation hazard over 26 weeks.
  - Engagement is the leading metric and net revenue is secondary.
- **Mechanism:**
  - A weekly push and an in-app card link every treated seat to the existing plan leaderboard.
  - Seats idle for 14 days or more get an extra push or email, sent from a dedicated sending pool.
  - Covers all family plans (Games Family and All Access Family).
  - **Randomized:** plan_id in one half, user_id in the other.
- **Why cluster-level:**
  - Leaderboard rivalry makes play complementary across seats.
  - Churn is a plan event, so per-member retention is mis-specified.
- **Design:**
  - Plans are split into a plan-randomized half and a member-randomized half.
  - The plan-randomized half has three saturation arms: control, idle seat only, all seats.
  - A Hausman-style test compares the two halves' estimates.
- **Size needed:**
  - 18.6k plans per arm, about 82.7k plans in total.
  - The idle-only arm (about 4.1k) is not confirmatory.
  - The baseline churn (8%) and idle share are **assumptions**, and the base is **unverified**.
  - Engagement is "easily powered". Fallbacks need sign-off.
- **Caveats:**
  - High baseline retention may compress the effect.
  - Push opt-in may be low, and the plan interacts with Plan 1 on shared frequency caps.
  - Leaderboards on Games Family are **unverified**.
  - Within-plan user hashing is **unverified**.

## Plan 3: Whole-plan All Access trial (second wave)

- **Idea:** Unlock All Access for every seat of a Games Family plan for 21 days (an **assumed** length), then offer the owner the upgrade. This comes from card P2.
- **Outcomes promoted:** Revenue, retention and engagement.
  - **Primary outcome: revenue**, measured as upgrade within 28 days after the trial.
  - Cancellation non-inferiority is co-primary, and post-trial engagement is secondary.
- **Mechanism:**
  - A temporary entitlement grant with in-app notes to seats.
  - The owner offer from Plan 1 follows at day 21.
  - **Randomized:** plan_id. It is mutually exclusive with Plan 1 and launches after Plan 1's primary read.
- **Why cluster-level:**
  - The owner pays based on what the whole plan uses.
  - A trial for one seat builds habit in someone who may not be the payer.
- **Design:**
  - Three arms: no trial, most-active seat only, all seats.
  - The comparison of all seats against one seat gives the cluster increment.
- **Size needed:**
  - About 6,024 plans per arm (18.1k in total), based on **assumed** conversion rates.
  - Supply is 70% of Plan 1's holdout (about 11.9k) plus about 6.2k new plans. Growth of the base is **unverified**.
  - The fallback is rolling enrolment, or testing all seats against no trial only.
- **Caveats:**
  - Losing access when the trial ends may raise cancellation.
  - The interaction with intro-price eligibility is **unverified**.
  - Rights for non-owned content are **unverified**.
  - Reusing Plan 1's holdout weakens Plan 1's long-run read.
  - If the owner dominates usage, the one-seat arm is effectively an owner-only trial.

**Not planned:** P5 (household paywall → family offer, dropped); P8 (geo family offer, dropped); P6 (invite steering, parked, with its accounting rule folded into all plans).