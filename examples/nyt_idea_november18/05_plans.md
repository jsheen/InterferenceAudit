# Agent 5: Full experiment plans

Agent 4 selected three prototypes, and this stage plans only those:

| Plan | Prototype | Source cards |
|---|---|---|
| 1 | Prototype A: plan-coordinated upgrade | P1 + P3, with P7 as an audit arm |
| 2 | Prototype B: plan challenge and idle-seat reactivation | P4, with a P7-style audit arm |
| 3 | Prototype C: fill empty seats | U1 + P6, with optional arm M reusing P3's infrastructure |

P2 stays parked. P5 and P8 stay dropped. P6's hold/compare screen stays dropped.

---

## 0. Shared foundations (apply to all three plans)

### 0.1 Prices used in every revenue calculation

All rows are assumptions unless marked verified. Every 4-week figure assumes 13 bills per year.

| Item | Value used | Status |
|---|---|---|
| Games Family, regular | $10 per 4 weeks, $130/yr | Launch price verified as "$10 a month" (Digiday/Nieman). The 4-week billing and the 2026 price are **unverified**. |
| All Access Family, regular | $34 per 4 weeks, $442/yr. Sensitivity case: $30, $390/yr | $30 at launch is verified. $34 is **unverified** (one tracker). |
| All Access Family intro | $8 per 4 weeks for year 1 | The tracker is **unverified**. Whether existing owners qualify is **unverified**. |
| Individual All Access | $30 per 4 weeks, $390/yr | **Unverified** (tracker plus Slickdeals). |

### 0.2 Shared data foundation (build once, in Plan 1)

All of the following is inferred: NYT plausibly holds this data, but its schema is unverified.

- **`plan_roster_snapshot`**
  - Fields: plan_id, plan_type, owner account_id, member account_ids, role, joined_at, left_at, billing_channel (direct / Apple / Google), seat count, tenure.
  - Source: billing and entitlement tables.
  - It is snapshotted at entry (T0), and the snapshot is immutable.
- **`consent_snapshot`**
  - Fields per account: email marketing opt-in, push token and OS permission per device, in-app eligibility.
  - Taken at T0.
- **`assignment`**
  - Fields: experiment_id, plan_id (or account_id in audit halves), arm, stratum, salt, assigned_at.
  - Assignment is a deterministic hash of (plan_id, salt), written once and never recomputed.
- **`exposure_log`**: every touch actually delivered, with plan_id, account_id, role, channel, template, timestamp and arm.
- **Outcome tables**
  - Plan product changes, from billing.
  - Plan cancellations.
  - A plan-revenue ledger.
  - Individual-subscription events for every account linked to the plan.
  - Per-account sessions by product, paywall hits by product, and game plays.

### 0.3 Experiment layering

All three plans draw on the same scarce plan base, and their treatments interact. For example, Plan 2's engagement push could move Plan 1's upgrade rate.

- A plan_id enters **at most one** of the three plans in a given period.
- Assignment to a plan is by a separate layer hash.
- Games Family plans are split between Plans 1 and 2. All Access Family plans are split between Plans 2 and 3.
- The split proportions are set **after** the plan count is known (see the power sections).
- Plans currently in any other plan-level upsell or retention campaign are excluded.

### 0.4 Reporting conventions

- **Never report "subscribers".** A family plan counts as 2 regardless of seats (verified, Nieman).
- Report instead:
  - plan-level revenue;
  - **seats with access**;
  - the plan cancellation hazard;
  - both plan-weighted and person-weighted averages (Basse & Feller).

### 0.5 Statistical defaults

- Partial interference: no edges between plans, so plans are independent units.
- Analysis is at the plan level, which removes the member-level intra-cluster correlation (ICC) problem.
- Estimator: stratified difference in means, or OLS with stratum fixed effects plus pre-period covariates.
- Variance: HC2 robust variance at the plan level. Randomization-inference p-values are a robustness check.
- Before readout:
  - an A/A test on the assignment hash;
  - a sample-ratio-mismatch (SRM) check per stratum.

### 0.6 Email reputation (channel C6)

- Treatment arms add email volume. Mailbox providers score the sender as a whole, so control shares the reputation cost. This biases benefits **upward**.
- A dedicated sending pool per arm is preferred if infrastructure allows; feasibility is **unverified**.
- Otherwise:
  - cap incremental volume;
  - monitor complaint rate and inbox placement per arm;
  - state the bias direction in the readout.

---

## Plan 1: Plan-coordinated Games Family → All Access Family upgrade

**Pitch:** test whether nudging the *whole plan* in the same week, including giving members a one-tap way to ask the owner, produces more upgrades than nudging the owner alone, after controlling for message volume.

**Source cards:** P1 (coordinated push with saturation arms), P3 (member request to the owner), P7 (member-randomized audit).

### 1.1 Hypothesis and expected signs

Mechanism (channel C1): only the owner can buy (verified, NYT Help Center), but members hold much of the demand, through paywall hits on News, Cooking, The Athletic and Wirecutter. That demand can reach the owner only through talk outside the product, or through a request channel.

| Effect | Definition | Expected sign |
|---|---|---|
| Owner direct effect | Arm A vs arm 0 | **+** |
| Bipartite spillover onto the owner | Arm B vs arm 0: members treated, owner untreated | **+**, size unknown, limited by member paywall-hit volume (inference) |
| Spillover onto member engagement | In arm A, members are untreated but gain access if the plan upgrades | **+** |
| Total effect | Arm C vs arm 0 | **+**, the largest |
| Coordination net of dose | C vs A′ | **+** if seats are complements. This is the hypothesis under test; the null is plausible. |
| Bias of a member-randomized test | Naive estimate vs C − 0 | Naive is smaller (**understates**), because control seats share the upgrade (inference) |

### 1.2 Treatment arms

- **Window:** treatment days D1–D7 after entry T0. The request button stays live for weeks 0–8.
- **Price:** the offer price is held fixed across arms at NYT's actual policy. Prices must not vary by arm (to avoid the C8 promo-price leakage channel).

| Arm | Owner receives | Members receive |
|---|---|---|
| **0** Control | Business as usual. Suppressed from any other upsell campaign. | Business as usual |
| **A** Owner-only | 2 touches: an upgrade email on D1, plus an in-app card on the account or home page at the owner's next session in D1–7. Copy: "Unlock News, Cooking, Wirecutter and The Athletic for everyone on your plan". | Nothing |
| **A′** Owner-only, dose-matched | K touches over D1–7, mixing email, in-app and push (push only if the owner has OS permission). Same creative family as A. K is defined below. | Nothing |
| **B** Request button | Request digest (described below) | On News, Cooking, Athletic and Wirecutter paywalls, a "Request All Access for our plan" button, live weeks 0–8 |
| **C** Coordinated | Arm A's 2 touches | Each member: one in-app card in D1–7 ("Your plan could unlock Cooking, News, The Athletic. Ask the account holder", with the same request action), plus one push or email in D1–7 **only if that member consented**, plus arm B's paywall button |

**Dose matching for A′**
- At T0, compute for every plan the touches arm C *would* send: K = 2 + Σ over members of (1 + 1[member is push- or email-eligible]).
- This uses only pre-treatment data, so it can be computed for A′ plans.
- A′ delivers min(K, 7), assuming an owner cap of 1 touch per day.
- Any shortfall is logged. A sensitivity analysis drops 4-seat plans, where the cap can bind (K can reach 8).

**Request button mechanics (arms B and C)**
- **Member side**
  - When a member taps the button, the confirmation reads: "We'll let your plan's account holder know. We won't share what you were reading."
  - The flow works even if members cannot see who the owner is (unverified), because NYT routes the request.
- **Owner side**
  - Owners receive a batched digest at most once a week.
  - Content: "N requests from people on your plan this week to unlock All Access", plus the upgrade button.
  - The digest contains **only the count**: no name, product, article or recipe (Agent 4 constraint).
  - The digest is always shown in-app on the owner's account page. It also goes by email if the owner's consent covers this message class; whether it counts as transactional or marketing is a legal question and is **unverified**.
  - Owners can switch digests off.
  - Digests stop once the plan upgrades.
- Request-triggered digests are an **outcome** of treatment, not part of the dose. They are excluded from K.

**Consent rules**
- Each member's own marketing opt-in governs email and push sent to that member. The owner's consent does not cover members.
- Members without consent receive in-app surfaces only.
- The paywall button is an on-product surface, not a marketing message. This is an inference that needs legal confirmation.

### 1.3 Unit, clusters, eligibility, contamination

- **Unit:** plan_id, taken from the T0 roster snapshot and frozen.
- **Members who join after T0**
  - They inherit the plan's arm and receive the arm's member treatment.
  - The primary analysis is intention-to-treat (ITT) on the plan, so they are covered at the plan level.
  - Per-seat analyses use the T0 roster. Late joiners are reported separately, because joining is post-treatment.
- **Eligible**
  - Direct-billed Games Family plans with at least 2 seats (owner plus at least 1 member) on the T0 roster.
  - Tenure of at least 4 weeks. This is my addition, to avoid overlap with onboarding emails.
- **Excluded**
  - Third-party-billed plans. Their owners must cancel through Apple or Google before buying (verified, Help Center). Count them and report them; optionally run a separate C-vs-0 stratum if counts allow.
  - Plans with a pending cancellation or a payment failure.
  - Complimentary or employee plans.
  - Plans in another plan-level test (see 0.3).
  - Plans where any seat is also on another family plan, or is an owner elsewhere.
  - Plans with a Bonus-subscription structure (unmapped, Agent 4).
- **Strata:** seats (2 / 3 / 4) × tenure (4–12 weeks, 12–26 weeks, over 26 weeks) × owner engagement tercile (owner sessions in the 28 days before T0).
- **Contamination between clusters and how it is handled**

| Source | Handling |
|---|---|
| A person on two plans | Excluded at eligibility |
| A household spanning two plans, or members forwarding emails | Unobservable. Expected to be small (inference). Bias is toward zero. |
| Leaderboard rivalry across plans | Unverified whether it exists. Irrelevant to upgrades. |
| Plan_id changing at upgrade | Upgrade lineage (old plan_id → new plan_id) must be verified **before launch**; otherwise upgrades are lost as "cancellations". |
| Concurrent global campaigns | Suppress in all arms equally |

### 1.4 Design

- Two-stage design under partial interference (Hudgens & Halloran 2008).
- **Stage 1:** eligible plans are split 50/50 at random, within strata, into a **plan-randomized half** and an **audit half**.
- **Plan-randomized half:** plans are randomized equally to {0, A, A′, B, C} within strata.
  - If the power check in 1.7 fails, collapse to **{0, A′, C}** (Agent 4's fallback).
- **Audit half** (from P7, after Saveski et al. 2017 and LinkedIn's "A/B test of A/B tests"):
  - Each T0 seat, owner included, is independently assigned Bernoulli(0.5) to receive **its role's arm-C treatment**.
    - A treated owner gets arm A's 2 touches.
    - A treated member gets the in-app card, the push or email if consented, and the request button.
  - This reproduces what a standard user-level A/B test would do.
  - It also produces random within-plan saturation (from 0 to all seats), which supports exposure-mapping estimates (Aronow & Samii 2017). This is Bernoulli-induced saturation, not Baird et al.'s pre-set saturation levels.
  - The two halves contain disjoint, independently drawn plans, so their estimates are independent. That simplifies the variance of the comparison between them.

### 1.5 Estimands and estimators

Notation: Y_k is a plan outcome. a(k) is plan k's arm. μ_a = E[Y_k | a].

| Estimand | Formula | Notes |
|---|---|---|
| Owner direct | τ_A = μ_A − μ_0 | |
| Bipartite spillover (members → owner) | τ_B = μ_B − μ_0 | |
| Total | τ_C = μ_C − μ_0 | |
| Dose effect | τ_A′ − τ_A | |
| Coordination net of dose | Δ_coord = μ_C − μ_A′ | |
| Interaction (exploratory) | τ_C − τ_A − τ_B | Not a clean interaction: C also adds proactive member touches that B lacks |
| Indirect effect on member engagement | E[member engagement \| A] − E[\| 0], over T0 members | |
| Engagement per induced upgrade (exploratory) | Wald ratio = (member engagement effect, A vs 0) / τ_A | Exclusion restriction: owner messaging reaches members only through the upgrade. Plausible but untestable. |
| Audit: naive effect | τ_naive = mean over treated seats of 1[plan upgraded] − mean over control seats of the same | Seat-weighted. This is what a user-level dashboard would report as the effect of the C treatment. |
| Audit: bias | b = τ_C^(seat-weighted) − τ_naive | Also report the ratio τ_naive / τ_C, as LinkedIn reported 0.24 vs 0.81 |
| Audit: exposure-mapping effects | E[Y \| owner treated ∈ {0,1}, share of members treated ∈ {0, partial, all}] | Within each seat-count stratum the exposure probabilities are known (e.g. P(all members treated) = 0.5^(m−1)). Use post-stratified differences in means, which equal Horvitz-Thompson estimates within strata. |

**Estimators and variance**
- **Plan-level outcomes** (binary upgrade, revenue): stratified difference in means, with OLS with stratum fixed effects plus pre-period covariates as the precision check. HC2 robust standard errors, plans as independent units.
- **Per-seat outcomes:**
  - plan-weighted: average within the plan, then across plans;
  - person-weighted: a ratio estimator with delta-method variance, clustered by plan.
- **Audit variance**
  - The naive estimate uses plan-clustered standard errors, because seats in the same plan share Y.
  - Var(b̂) = Var(τ̂_C) + Var(τ̂_naive), since the halves are independent.
  - Report b̂ with its confidence interval. The Hausman-type z-test is secondary, because it is underpowered (see 1.7).
- **Multiplicity:** Holm adjustment over the 4 primary contrasts {τ_C, τ_A, τ_B, Δ_coord} at family-wise α = 0.05.

### 1.6 Metrics and readout

| Role | Metric | Outcome area | Readout |
|---|---|---|---|
| **Primary** | Plan upgraded to All Access Family within 8 weeks of T0 | Revenue | Week 8 after the last plan's entry. With a 2-week enrollment window, about week 10. |
| Secondary | 12-month net plan-cluster revenue, **modelled under both intro scenarios** (S1 eligible / S2 not eligible, at $34 and $30). Net revenue = owner plan billing + Σ over T0 seats of change in individual-subscription billing (members who cancel a standalone Cooking or Athletic subscription after the upgrade, and members who buy their own subscription instead). | Revenue | Model at week 10. Realized check at 6 months. |
| Secondary | Engagement on newly unlocked products per seat (sessions on News, Cooking, Athletic, Wirecutter), plan- and person-weighted | Engagement | Weeks 1–12 |
| Secondary | Requests per plan; digest-to-upgrade conversion (arms B and C) | Funnel | Week 8 |
| **Guardrail** | Plan cancellation hazard (Games Family base or upgraded plan); Cox regression stratified by stratum | Retention | Week 12, extended to 26 |
| Guardrail | Email unsubscribes, spam complaints and push opt-outs per seat; owner digest opt-outs; customer-service contacts | Engagement / brand | Weekly |
| Guardrail | Complaint rate and inbox placement per arm (C6) | Shared resource | Weekly |

**12-month revenue arithmetic per upgrading plan** (all inputs are assumptions from 0.1)

| Scenario | Calculation | Δ per upgrading plan |
|---|---|---|
| S1: intro applies | $8 × 13 − $130 | **−$26** |
| S2: regular $34 | $442 − $130 | **+$312** |
| S2′: regular $30 | $390 − $130 | **+$260** |
| S1, year 2 | $442 − $130, assuming 80% of upgraders retained into year 2 (assumption) | +$312, expected +$250 |

Under S1, the upgrade costs the owner less than staying put for a year (Agent 1). Upgrades may then be inflated by price-seekers, and year-1 revenue falls.

### 1.7 Power

**Formula** for a two-arm comparison of plan-level proportions. Upgrade is a plan event, so the design effect is 1 and no ICC term is needed.

n per arm = (z₁₋α/2 + z₁₋β)² × [p₀(1−p₀) + p₁(1−p₁)] / δ²

**Assumptions** (every input is an assumption):
- p₀ = 1.0% baseline 8-week upgrade rate.
- δ = 0.5 percentage points, so p₁ = 1.5%.
- Power 80%, so z₁₋β = 0.8416.
- Holm/Bonferroni over 4 contrasts: α per test = 0.0125, so z = 2.4977.

**Step by step, 5-arm design**
1. z sum = 2.4977 + 0.8416 = 3.3393. Squared = 11.151.
2. p₀(1−p₀) = 0.01 × 0.99 = 0.009900.
3. p₁(1−p₁) = 0.015 × 0.985 = 0.014775.
4. Sum = 0.024675.
5. 11.151 × 0.024675 = 0.27515.
6. δ² = 0.005² = 0.000025.
7. n = 0.27515 / 0.000025 = **11,006 plans per arm**.
8. Plan-randomized half = 5 × 11,006 = 55,030. With the 50% audit half, **about 110,000 eligible plans** are needed.

Agent 4 quoted about 6.4k per arm. That used 16·p₀(1−p₀)/δ², which corresponds to α = 0.05 and ignores p₁'s variance. The figures above are stricter.

**Collapsed 3-arm design {0, A′, C}** (3 contrasts, α = 0.0167, z = 2.3940)
1. z sum = 3.2356. Squared = 10.469.
2. 10.469 × 0.024675 = 0.25833.
3. 0.25833 / 0.000025 = **10,333 per arm**.
4. 31,000 plans in the plan-randomized half, **about 62,000 total**.

**If δ = 1.0 percentage point** (p₁ = 2.0%, so p₁(1−p₁) = 0.0196 and the variance sum is 0.0295)

| Design | Calculation | Per arm | Total eligible plans |
|---|---|---|---|
| 5-arm | 11.151 × 0.0295 / 0.0001 | 3,290 | **≈32,900** |
| 3-arm | 10.469 × 0.0295 / 0.0001 | 3,088 | **≈18,500** |

**The coordination contrast C vs A′ needs more plans**
- Both arms sit above baseline. Assume 2.0% vs 1.5%: variance sum = 0.0196 + 0.014775 = 0.034375.
- 11.151 × 0.034375 / 0.000025 = **15,333 per arm**.
- So the question of complementarity across seats is the weakest-powered question in this plan.

**Minimum detectable effect (MDE) for a known plan count N**
- δ ≈ (z₁₋α/2 + z₁₋β) × √(2 p̄(1−p̄) / n), where n = N / (2 × number of arms).
- Hypothetical N = 40,000, 3-arm: n = 6,667. With p̄ = 1.25%, p̄(1−p̄) = 0.012344.
- δ = 3.2356 × √(0.024688 / 6,667) = 3.2356 × 0.0019243 = **0.62 percentage points**.

**Audit half: detectable bias**
- Var(b̂) ≈ Var(τ̂_C) + Var(τ̂_naive) ≥ 2 × Var(τ̂_C).
- So the smallest detectable bias is at least about √2 = 1.41 times the MDE of τ_C. Treat the audit as estimation with a confidence interval, not as a test.

**Per-seat engagement (secondary)**
- If analysed seat-weighted with plan clustering, the design effect is 1 + (m̄ − 1)ρ.
- Assume m̄ = 2.8 seats per plan and ρ = 0.3 (both assumptions): 1 + 1.8 × 0.3 = **1.54**.
- Plan-level aggregation avoids this.

**Rule on arms (applied once the plan count is known)**

| Eligible Games Family plans available after layering | Design |
|---|---|
| ≥ 110k | Full 5-arm design with a 50% audit half |
| 62k–110k | 3-arm design {0, A′, C} with a 50% audit half |
| 19k–62k | 3-arm design. Accept an MDE of about 1 percentage point and report it. |
| < 19k | Do not run a confirmatory test. Run arm C vs 0 only, as a directional pilot, and pool across successive cohorts. |

### 1.8 MVP build plan, in order

1. **Data:** `plan_roster_snapshot`, `consent_snapshot`, and an upgrade lineage table (old plan_id → new plan_id, with timestamp and price paid). Verify that the price paid is logged, since it resolves the intro question empirically.
2. **Eligibility and stratification job:** a daily batch that writes the T0 cohort.
3. **Assignment service:** plan hash with salt, plus a seat hash for the audit half. Write-once table. Run the A/A test and SRM monitor.
4. **Exposure logging:** every touch keyed to (plan_id, account_id, arm), so that the K computation for A′ can be audited.
5. **Messaging:**
   - owner email and in-app templates;
   - member in-app card and push/email templates;
   - a dose scheduler (computes K, applies caps);
   - consent gating.
6. **Request flow:**
   - paywall variant behind a feature flag keyed on the plan's arm;
   - request event;
   - weekly aggregation;
   - owner digest (count only), with an opt-out switch;
   - suppression after upgrade.
7. **Outcome pipeline:**
   - upgrade at 8 weeks;
   - plan-cluster revenue ledger (owner plus T0 seats' individual subscriptions);
   - per-seat engagement on unlocked products;
   - cancellation events;
   - scenario revenue model (S1 / S2 / S2′).
8. **Pre-registered analysis notebook and guardrail dashboard**, written before the first plan enters.

### 1.9 Decision rule (proposed thresholds)

**Roll out arm C:**
- τ_C > 0 at Holm-adjusted significance; **and**
- the 12-month net-revenue lower 95% bound is ≥ 0 under the pricing policy NYT will actually run; **and**
- the cancellation-hazard upper 95% bound is < 1.10, **and** the implied increase in cancellation is below break-even; **and**
- Δ_coord ≥ 0, with the lower confidence bound above −0.25 percentage points.

Break-even for cancellation, under S2:
- Revenue gain per eligible plan = δ × $312 = 0.005 × 312 = $1.56.
- An extra 12-month cancellation costs about $130 × 0.5 = $65 per plan, assuming half a year of revenue is lost on average (assumption).
- So the treatment breaks even if it raises cancellation by **Δc\* = 1.56 / 65 = 2.4 percentage points**. Under S2′ ($30), Δc\* = 1.30 / 65 = 2.0 percentage points.

**Other outcomes**

| Result | Action |
|---|---|
| C ≈ A′, both > 0 | Roll out the cheaper **owner-only dose-matched (A′)** treatment. Seat coordination does not pay for its member-messaging cost. |
| τ_B > 0 | Keep the request button as a permanent paywall feature, whatever happens to the other arms |
| Lift is positive only under S2 | Roll out only if owners are made ineligible for the $8 intro on upgrade, or if a 24-month model is positive. Under S1, 2 years ≈ 0.005 × (−26 + 250) = **+$1.12 per eligible plan** (assumptions as above). |
| Audit ratio τ_naive / τ_C < 0.7 (confidence interval reported) | Move all plan-relevant tests (upsell, Games retention) to plan hashing |
| No arm's confidence interval excludes 0, and every upper bound is below the MDE | **Stop.** Coordination does not matter at this scale. Keep P2 parked. |
| Positive point estimates without significance | **Iterate:** next enrollment wave, pooling cohorts |

### 1.10 Risks

- **Underpowering.** The plan count is not disclosed (Agent 4, from the Q3 2026 8-K and earnings call).
- **Low paywall-hit volume** among members makes arm B small (inference).
- **Dose cap binds on 4-seat plans** in A′.
- **Intro-price anomaly** inflates upgrades while lowering year-1 revenue.
- **Upgrade lineage:** if the plan_id changes at upgrade and is not tracked, upgrades are misread as cancellations.
- **Members feel spammed;** the owner perceives requests as nagging.
- **Third-party exclusion** limits how far the results generalize.

### 1.11 Unverified facts to check before launch

1. The current Games Family price and its billing period.
2. The current All Access Family price ($34 or $30).
3. Whether owners qualify for the intro price on upgrade.
4. The count of direct-billed Games Family plans by seat count.
5. Member paywall hits per plan per month.
6. Whether members can see who the owner is.
7. Whether the owner digest is transactional or marketing mail (legal).
8. NYT's current randomization unit. If tests are already plan-hashed, the audit half answers a smaller question.
9. Whether the plan_id persists through an upgrade.
10. Whether a dedicated email pool per arm is feasible.

---

## Plan 2: Plan challenge and idle-seat reactivation

**Pitch:** cut whole-plan cancellation by giving every seat a synchronized weekly challenge on the existing plan leaderboard and by reactivating idle seats. The test uses a 2×2 design that separates the targeted idle-seat nudge from the full-plan treatment.

**Source cards:** P4, plus a P7-style embedded audit.

### 2.1 Hypothesis and expected signs

Mechanism (channel C3): a shared leaderboard (verified feature) makes play complementary across seats. Cancellation is a plan event decided by the owner, which becomes more likely when seats go idle (inference).

| Effect | Expected sign |
|---|---|
| Direct effect: a nudged seat plays more | **+** |
| Spillover from a reactivated idle seat to untreated active seats (arm I) | **+**, through leaderboard rivalry |
| Spillover onto the owner's cancellation decision | **−** (fewer cancellations) |
| Total effect of S+I on plan cancellation | **−**. The size is small, because the family-plan retention baseline is believed to be high (an executive belief, not data). |
| Bias of a seat-randomized test on engagement | **Understates** the effect, because control seats on the same plan see treated rivals |
| Push fatigue | **−** for engagement. Measured as a guardrail. |

### 2.2 Treatment arms: a 2×2 factorial

| Arm | Synchronized challenge (S) | Idle-seat nudge (I) |
|---|---|---|
| 0 | No | No |
| I | No | Yes |
| S | Yes | No |
| S+I | Yes | Yes |

**S: synchronized challenge**
- Runs for 12 weeks.
- Every Monday at 10:00 in each member's local time, so all seats get it on the same calendar day, every seat receives a push: "This week on your plan's leaderboard: best Connections streak". The game rotates.
- A Sunday recap push shows final standings.
- Content shows **only what the existing plan leaderboard already shows**. Which statistics the leaderboard exposes is unverified, so content must be audited against it.

**I: idle-seat nudge**
- Dynamic trigger: when a T0 seat has no session in **any** NYT product for 14 days. Using any product avoids nudging people who read News but don't play Games.
- Message: "Your plan's leaderboard is busy this week. Jump back into Wordle."
- At most 1 per 14 days per seat, and at most 3 over the test.

**Channels and caps**
- Channel priority: push if the member has OS permission, then email if the member has marketing consent, then in-app at the next open.
- In-app is logged but is weak for idle seats.
- Per-member frequency caps apply across all NYT push programmes.
- A seat with no permitted channel is untreatable but stays in the ITT analysis.

### 2.3 Unit, clusters, eligibility, contamination

- **Unit:** plan_id, from the T0 roster.
- **Eligible:**
  - Games Family **and** All Access Family plans with at least 2 seats active (any session) in the 28 days before T0;
  - direct and third-party billing alike (no purchase is involved), with billing channel as a stratum.
- **Excluded:**
  - plans allocated to Plan 1 or Plan 3 (layering);
  - pending cancellations;
  - seats on more than one plan.
- **Strata:**
  - plan type × seats (2 / 3 / 4) × tenure tercile × pre-period active seats (2 / 3 / 4);
  - whether at least 1 seat was idle at T0. This is pre-treatment, so it supports a clean subgroup analysis of arm I.
- **Contamination**
  - Leaderboard rivals outside the plan, if any such feature exists (unverified), are edges between clusters.
  - Pre-launch, compute each plan's external leaderboard edges.
  - If they exist:
    - (a) record each plan's share of external rivals in treated arms as an exposure covariate;
    - (b) run a sensitivity analysis on plans with zero external edges.
  - If they are common, randomize connected components of plans instead of single plans.
- **Late joiners:** they inherit the plan's arm. Per-seat analysis uses the T0 roster.

### 2.4 Design

- Plan-level cluster randomized trial, 2×2 factorial, with equal allocation within strata. This covers 80% of eligible plans.
- **Embedded audit:** a random **20%** of eligible plans, chosen within strata.
  - Each T0 seat is independently assigned Bernoulli(0.5) to receive S individually.
  - The size of the audit share was not set in Agent 4's brief. 20% is my choice, to protect power for the cancellation outcome.

### 2.5 Estimands and estimators

**Estimands**
- **Main effect of S** on plan cancellation: the hazard ratio (HR) for {S, S+I} vs {0, I}. The main effect of I is defined symmetrically. The S×I interaction is exploratory.
- **Spillover of I** onto untreated seats, among plans with at least 1 idle seat at T0: weekly activity of seats that were *active* at T0, arm I vs arm 0. In arm I those seats are untreated, so this is an indirect effect in Hudgens & Halloran's sense.
- **Direct effect of I** on idle seats: activity of seats idle at T0, arm I vs arm 0.
- **Total effect:** S+I vs 0, on both plan cancellation and active seats.
- **Audit:**
  - τ_naive = activity of treated seats − activity of control seats (seat-randomized);
  - compared with the per-seat activity effect of S vs 0 in the plan-randomized portion;
  - plus a spillover curve: untreated seats' activity as a function of the share of co-members treated, post-stratified by plan size.

**Estimators**

| Outcome | Estimator | Variance |
|---|---|---|
| Plan cancellation | Cox model stratified by randomization stratum, with factorial indicators plus pre-period covariates (active seats, tenure, prior-cycle activity). Restricted mean survival time (RMST) difference at 24 weeks as a robustness check. | Robust sandwich, plans independent |
| Leading metric: active seats per plan per week | Each plan's mean over weeks 1–8 (one number per plan, which avoids autocorrelation). CUPED: Y_adj = Y − θ(X − X̄), with X = mean active seats per week over the 4 weeks before T0, θ = Cov(Y, X) / Var(X). | HC2 |
| Audit | Seat-level difference in means | Clustered by plan |

### 2.6 Metrics and readout

| Role | Metric | Outcome area | Readout |
|---|---|---|---|
| **Primary** | Plan cancellation hazard | Retention | At least 12 weeks after the last entry. Pre-registered extension to 24 weeks. |
| **Leading (pre-registered surrogate)** | Active seats per plan per week, CUPED-adjusted | Engagement | Weeks 4 and 8 |
| Secondary | Game plays per seat; leaderboard views; reactivation rate of seats idle at T0 | Engagement | Weekly |
| Secondary | Realized plan revenue over 24 weeks. Prices are unchanged; this is churn-driven only. | Revenue | 24 weeks |
| **Guardrail** | Push opt-out rate per seat (proposed limit: ≤ +0.5 percentage points absolute over 12 weeks vs control) | Engagement | Weekly |
| Guardrail | Email unsubscribes (proposed limit: ≤ +0.3 percentage points); app uninstalls, if logged | Engagement | Weekly |
| Guardrail | Sessions on News and other non-Games products per seat. This checks for a **within-user** shift of attention between products, which is not interference. | Engagement | Weekly |

**Surrogate validation plan (pre-registered)**
1. In the control arm, estimate how strongly active seats per week in weeks 1–8 predict cancellation in weeks 9–24 (prognostic check).
2. Across arms, check whether (treatment effect on the surrogate) × (prognostic slope) matches the observed 24-week effect on cancellation.
3. If not, the surrogate is rejected for future plan-retention tests.

### 2.7 Power

**Formula** (Schoenfeld; events needed for a hazard ratio):

D = (z₁₋α/2 + z₁₋β)² / [π₁π₂ (ln HR)²], then N = D / P(event by the end of follow-up)

**Assumptions** (all assumptions):
- 4-week plan cancellation of 2.0%, constant hazard, both plan types pooled.
- Target HR = 0.90 for each main effect.
- α = 0.05 split across the two main effects, so 0.025 each and z = 2.2414.
- Power 80%, so z = 0.8416.
- The factorial compares halves, so π₁ = π₂ = 0.5.
- Covariate gains are ignored, which makes the estimate conservative.

**Step by step**
1. z sum = 2.2414 + 0.8416 = 3.0830. Squared = 9.505.
2. ln(0.90) = −0.10536. Squared = 0.011101.
3. π₁π₂ = 0.25.
4. D = 9.505 / (0.25 × 0.011101) = 9.505 / 0.0027753 = **3,425 events**.
5. Control cancellation over 12 weeks (3 cycles) = 1 − 0.98³ = 1 − 0.941192 = 0.05881.
6. Treated plans: 4-week survival = 0.98^0.9 = e^(0.9 × −0.020203) = 0.981982. Cubed = 0.946914, so cancellation = 0.05309.
7. Average event probability = 0.05595.
8. N = 3,425 / 0.05595 = **61,215 plans** in the factorial (about 15.3k per cell).
9. Adding the 20% audit share: 61,215 / 0.8 = **about 76,500 eligible plans**.

**With 24-week follow-up**
1. Control = 1 − 0.98⁶ = 0.11416.
2. Treated = 1 − 0.946914² = 0.10335.
3. Average = 0.10876.
4. N = 3,425 / 0.10876 = **31,490**, or **about 39,400** including the audit share.

**Interaction S×I:** its standard error is twice that of a main effect, so detecting an interaction of the same size needs about 4× the events (≈245k plans at 12 weeks). It is exploratory only.

**Leading metric (well powered)**

n per half = 2 (z₁₋α/2 + z₁₋β)² σ² (1 − ρ²) / δ²

- Assumptions:
  - mean active seats = 2.0 and σ = 0.9 (assumptions);
  - correlation between pre- and post-period ρ = 0.6, so CUPED keeps 1 − 0.36 = 0.64 of the variance;
  - δ = 0.05 seats (2.5% relative).
- Arithmetic:
  1. 2 × 9.505 = 19.01.
  2. × 0.81 = 15.398.
  3. × 0.64 = 9.855.
  4. / 0.0025 = **3,942 plans per half**, so about 7,900 plans in the factorial.

**Per-seat analysis without plan aggregation:** design effect 1 + (2.8 − 1) × 0.3 = 1.54 (assumptions as in 1.7).

**Rule**

| Eligible plans after layering | Approach |
|---|---|
| ≥ 39k | Run with cancellation as primary, 24-week readout |
| 8k–39k | Cancellation remains primary but is reported with its MDE. Decide on the validated surrogate. Lengthen follow-up to 52 weeks. |
| < 8k | Do not run the factorial. Compare S+I with 0 only. |

### 2.8 MVP build plan, in order

1. Shared data foundation (from Plan 1), plus an extract of the leaderboard data (what is shown, to whom) and a daily seat-activity table.
2. Audit of edges between plans on the leaderboard (does the feature exist; how many edges).
3. Assignment: a 2×2 plan hash, plus a seat hash for the audit share.
4. Weekly challenge generator: reads existing leaderboard statistics only, then a privacy review against the leaderboard's current visibility rules.
5. Idle-seat trigger job: daily, 14 days without activity, with the cap and channel fallback.
6. Push and email templates, integrated with the global per-member frequency-cap service.
7. Outcome pipeline: cancellation survival table, weekly active seats, opt-out and unsubscribe events.
8. Pre-registered analysis notebook, including the surrogate-validation code.

### 2.9 Decision rule (proposed thresholds)

| Result | Action |
|---|---|
| **Roll out** the arm with the best leading metric (S, I or S+I) | If (a) the cancellation HR upper 95% bound is < 1.0, **or** the surrogate is validated with HR point estimate < 1 and upper bound < 1.05; **and** (b) the guardrails hold |
| Leading metric up, cancellation inconclusive, surrogate not yet validated | **Iterate:** extend follow-up to 52 weeks, pool the next cohort |
| I's spillover onto active seats > 0 but S adds nothing | Roll out the cheaper targeted I only. Low saturation is enough. |
| Audit ratio τ_naive / τ_S < 0.7 | Games engagement tests move to plan hashing for family plans |
| Opt-out guardrail breached in S, or leading metric ≤ 0 with upper bound < +0.02 seats | **Stop S** |

### 2.10 Risks

- **Retention ceiling.** The base cancellation rate may be far below 2%, making the primary outcome unpowered.
- **Push fatigue** across NYT programmes.
- **Challenge irrelevant to non-gamers** on All Access Family plans. Shows up as heterogeneity, analysed by the plan's Games-activity stratum.
- **Cross-plan rivals** (if they exist) bias toward zero.
- **Surrogate fails validation.**

### 2.11 Unverified facts to check before launch

1. Plan count by type and seat count.
2. Baseline 4-week plan cancellation rate by plan type.
3. Exactly what the leaderboard shows and to whom; whether it has cross-plan links.
4. OS push permission rates among members.
5. Whether a member's push permission spans their devices.
6. Global frequency-cap rules.

---

## Plan 3: Fill the empty seats on All Access Family plans

**Pitch:** nudge owners of All Access Family plans that have open seats to fill them, preferably with people who don't already pay, and credit every invitee's outcome to the owner's arm. The aim is to learn whether a *nudged* fill lowers plan cancellation without losing net revenue.

**Source cards:** U1 (user idea), P6 (owner-cell accounting and non-subscriber framing). Optional arm M reuses P3's request infrastructure from Plan 1. P6's hold/compare screen is dropped.

### 3.1 Hypothesis and expected signs

Mechanism (channels C2 bipartite, C3 coupling within the plan):
- The owner is treated, but outcomes land on invitees (activation, cancelling an individual subscription) and on the plan (cancellation).
- **Seats 3–4 add $0 in price and $0 in reported subscribers.**

| Effect | Expected sign |
|---|---|
| Seats filled (owner direct effect) | **+** |
| Plan cancellation through added seats (C3) | **−** (fewer cancellations). Cotton's claim is a belief, and organic fills are selected, so this is the main unknown. |
| Net revenue | **Ambiguous**: + through retention, − through cannibalizing invitees' individual subscriptions |
| Revenue: N vs G | N **>** G, through a lower share of paying invitees |
| Bias of owner-only revenue accounting | **Overstates** net revenue |
| Bias of owner-only engagement accounting | **Understates** engagement |

### 3.2 Treatment arms

All messaging goes to the **owner**, because only the owner can invite (verified, Help Center).
- Invitations are sent by NYT only when the owner acts, by email or link (Help Center).
- NYT sends **no marketing** to invitee addresses.

| Arm | Owner receives (D1–D28) |
|---|---|
| **0** Control | Business as usual |
| **G** Generic | D1 email "You have N open seats on your All Access Family plan" with an invite button; an in-app card on the account and home page through D28; a reminder email on D14 if no seat has been filled |
| **N** Non-subscriber framing | Same timing and touches as G. Copy: "Give someone who doesn't have NYT access to News, Games, Cooking, Wirecutter and The Athletic". Includes a **share link** the owner sends through their own channels. |
| **M** (optional, second wave) | Arm N's owner touches, plus members get an in-app card "Know someone who'd use the open seat? Let the account holder know". This triggers Plan 1's count-only owner digest. **No invitee data is collected from members.** Runs only once Plan 1's request infrastructure exists. Member opt-in governs anything beyond in-app. |

### 3.3 Unit, clusters, eligibility, contamination

- **Unit of randomization:** plan_id. Owners and members are fixed at T0.
- **Analysis cluster: the ego cluster**
  - The plan, plus every account that joins that plan after T0.
  - Joining a plan is a redemption, so the membership table supplies the plan link even if invite lineage is not logged. Invite logs are still needed for invites sent but not redeemed, and for counting redemptions per link.
  - Invitees inherit the owner's arm (bipartite / ego-network ITT: Zigler & Papadogeorgou 2021; Saint-Jacques et al. 2019).
- **Eligible:**
  - direct-billed All Access Family plans with **2–3 people** (1–2 open seats);
  - held at least 4 weeks.
- **Excluded:**
  - owner-only plans;
  - plans allocated to Plan 2;
  - pending cancellations;
  - plans with Bonus subscriptions.
- **No household inference**, anywhere.
- **Strata:** people on the plan (2 / 3) × tenure tercile × owner engagement tercile.

**Invitee status before the invite**, classified at the join timestamp from the joining account's prior 90 days:

| Status | Definition |
|---|---|
| Paying direct | Active individual subscription, billed directly |
| Paying third-party | Active Apple or Google subscription linked to the account |
| Registered free | Registered account, no subscription |
| Lapsed | A subscription ended in the prior 365 days |
| Unknown / new | Account created at join |

Plus one flag I added: **"current member or owner of another family plan"**.

**Contamination between clusters**
- **Movement from another family plan.** An invitee who leaves another family plan (or cancels a Games Family plan they own) harms a different cluster. This is tracked through the flag above, and the harm is charged to the inviting cluster.
- **Public invite links.** Links posted on deal forums leak (channel C8). Flag any link with redemptions from outside the plan's usual network, or more than 2 redemptions; whether links are single-use is unverified.
- **Treated-plan invitees joining control plans.** Such a person could only be counted once, because a person can be on only one plan. Excluded at eligibility.

### 3.4 Design

- Plan-level cluster randomized trial with arms {0, G, N} in wave 1, allocated 1:1:1 within strata.
- Arm M is added in wave 2, only if Plan 1's infrastructure exists and the wave-1 base allows it.
- **Fill as an instrument (exploratory):** the effect of a *nudged* fill on cancellation can be estimated by using assignment as an instrument for fills (Wald estimator). This is the direct test of whether Cotton's observed association survives selection. The exclusion restriction (owner nudges reduce cancellation only through fills) is assumed. Its precision is poor (see 3.7).

### 3.5 Estimands and estimators

**Estimands**
- **ITT on the plan cluster:**
  - cancellation HR;
  - P(at least 1 seat filled);
  - net seats added;
  - net revenue;
  - total engagement of the cluster.
- **Contrasts:** G − 0, N − 0, N − G. Primary cancellation contrast: pooled {G, N} vs 0, allocation 2:1.

**Net revenue per cluster** over horizon H:

NetRev_k = PlanBilling_k − Σ over invitees j of k [ L_j ]

L_j is what invitee j stops paying after joining:
- the realized individual-subscription billing lost after joining (realized at 6 months);
- plus a modelled continuation to 12 months, using survival curves for comparable non-invited individual subscribers;
- plus, for the "other family plan" flag, the lost billing of that plan.

**Bounds for blind spots**
- Third-party and unknown/new invitees:
  - lower bound: each one is a $30-per-4-weeks payer who cancels;
  - upper bound: each one costs $0.
- Registered-free invitees may forgo a later purchase: bound with P(convert within 12 months | comparable registered user) × $390. This is an assumption-based bound.

**Estimators and variance**
- Difference in means of NetRev_k with HC2 variance.
- Report point estimates **and** the [lower, upper] bound interval.
- Cancellation: stratified Cox with robust standard errors; RMST as a robustness check.
- Invitee-level engagement and status mix (descriptive only): **conditioning on redemption is post-treatment, so it is not randomized**. Randomized versions use cluster-level ITT, such as "number of cannibalizing redemptions per plan".

### 3.6 Metrics and readout

| Role | Metric | Outcome area | Readout |
|---|---|---|---|
| **Primary** | Plan cancellation hazard | Retention | 24 weeks, pre-registered extension to 52 |
| Intermediate | P(at least 1 seat filled) at 4 and 8 weeks; net seats with access | Engagement / access | Weeks 4 and 8 |
| **Co-primary for the decision** | Net revenue per cluster (with bounds) | Revenue | 6 months realized; 12-month model |
| Secondary | Cannibalizing redemptions per plan, by status class | Revenue | Week 8 |
| Secondary | Total cluster engagement: sessions, game plays and reads summed over T0 seats and joiners | Engagement | Weeks 1–24 |
| Secondary | Engagement of invitees at 4 weeks (descriptive) | Engagement | Week 4 |
| **Guardrail** | Owner unsubscribes and complaints; suspected link leakage | Brand | Weekly |
| Guardrail | Cancellations of other family plans linked to invitees | Revenue / retention | Week 8 |

### 3.7 Power

**(a) Seats filled** (binary, plan level)

Formula: n = (z₁₋α/2 + z₁₋β)² [p₀(1−p₀) + p₁(1−p₁)] / δ²

Assumptions:
- p₀ = 5% filled by 8 weeks in control (assumption).
- δ = 3 percentage points (p₁ = 8%).
- 3 contrasts, so α = 0.0167, z = 2.3940. Power 80%. z sum = 3.2356, squared = 10.469.

Arithmetic:
1. p₀(1−p₀) = 0.0475. p₁(1−p₁) = 0.0736. Sum = 0.1211.
2. 10.469 × 0.1211 = 1.2678.
3. δ² = 0.0009.
4. n = 1.2678 / 0.0009 = **1,409 plans per arm** (≈4.2k total).

**(b) Cannibalizing redemptions, N vs G** (plan has at least 1 paying-invitee redemption)

Assumptions:
- G: 8% fill × 15% paying share = 1.2%.
- N: 8% × 7.5% = 0.6%.

Arithmetic:
1. Variances: 0.012 × 0.988 = 0.011856; 0.006 × 0.994 = 0.005964. Sum = 0.01782.
2. 10.469 × 0.01782 = 0.18656.
3. δ² = 0.006² = 0.000036.
4. n = 0.18656 / 0.000036 = **5,182 per arm**.

**(c) Plan cancellation (primary): honestly underpowered**

Assumptions:
- The nudge raises fill probability by Δf = 0.10 (assumption).
- A fill cuts the plan's cancellation hazard by 30%, i.e. a complier HR of 0.70. This is an assumption, and generous, since it is Cotton's unverified belief.
- So the ITT HR ≈ 1 − 0.10 × 0.30 = 0.97.
- α = 0.05, power 80%, (z)² = 7.849. Allocation 2:1, so π₁π₂ = (2/3)(1/3) = 0.2222.
- 4-week cancellation for All Access Family = 1.5% (assumption).

Arithmetic:
1. ln(0.97) = −0.030459. Squared = 0.00092776.
2. π₁π₂ × (ln HR)² = 0.2222 × 0.00092776 = 0.00020617.
3. D = 7.849 / 0.00020617 = **38,071 events**.
4. Event probability by 24 weeks = 1 − 0.985⁶ = 1 − 0.91331 = 0.0867.
5. N = 38,071 / 0.0867 = **≈439,000 plans**, almost certainly more than exist (inference; the count is undisclosed).

**Reverse calculation for a hypothetical N = 60,000**
1. D = 60,000 × 0.0867 = 5,202 events.
2. MDE |ln HR| = 2.8016 / √(0.2222 × 5,202) = 2.8016 / 34.0 = 0.0824, so the ITT HR must be at most ≈ 0.921.
3. The implied complier HR must be at most 1 − 0.079 / 0.10 ≈ **0.21**. That is implausible.

**Conclusion:** the cancellation outcome will be an estimate with a wide confidence interval, not a test. The decision will hinge on net revenue and seats with access (see 3.9).

**(d) Revenue break-even: the most decision-relevant arithmetic**

All inputs are assumptions:
- Base 12-month plan cancellation = 20%.
- A fill gives complier HR = 0.70, so cancellation becomes 1 − 0.8^0.7 = 1 − 0.8553 = 14.47%. The reduction is 5.53 percentage points.
- A cancellation loses about half a year of revenue on average.

Arithmetic:
1. Value per fill: V = 0.0553 × $442 × 0.5 = **$12.2**.
2. Loss per cannibalizing fill: L ≈ **$390** (an individual All Access subscriber kept for a year).
3. Break-even share of cannibalizing fills: s\* = V / L = 12.2 / 390 = **3.1%**.

Adding the bound for forgone conversion by registered-free invitees (assumed 2% × $390 = $7.8 per such fill) lowers V's margin further.

**Implication (inference):** a nudged fill campaign is revenue-positive only if fewer than about 3% of fills come from paying individuals. That is why arm N's framing, and the status classification, matter more than the cancellation readout.

### 3.8 MVP build plan, in order

1. Shared data foundation (from Plan 1), plus:
   - invite table: invite_id, plan_id, channel, created_at, redeemed_by, redeemed_at;
   - membership-join events.
2. Invitee status classifier: entitlement history for the prior 90 and 365 days; Apple/Google receipt linkage, if it exists; the "other family plan" flag.
3. Assignment (plan hash) and stratification.
4. Owner templates G and N; share-link generation with per-link redemption counting.
5. Net-revenue ledger: plan billing, invitees' lost billing (realized), the continuation model, and the bounds.
6. Cancellation survival table; cluster engagement aggregation.
7. Wave 2 only: arm M member card, wired to Plan 1's digest service.
8. Pre-registered notebook, including the win criteria in 3.9.

### 3.9 Decision rule (pre-specified; "win" requires both conditions)

**Win, then roll out the better of G or N:**
- (a) plan cancellation HR upper bound of the 80% two-sided confidence interval < 1.0; **and**
- (b) the **lower bound** of net revenue is ≥ 0 (i.e. third-party and unknown invitees counted as cannibalized).

**Other outcomes**

| Result | Action |
|---|---|
| Fills up, cancellation inconclusive, net revenue ≥ 0 only under the upper bound | **Iterate:** improve third-party linkage, extend to 52 weeks, pool waves. **Do not roll out.** |
| Fills up, net-revenue point estimate ≥ 0, cancellation inconclusive | Escalate to a human (Agent 4 question #8): is a seat with access that adds no revenue worth having? **No automatic rollout.** |
| Share of cannibalizing fills (with CI) clearly above the ≈3% break-even in both arms | **Stop** the revenue case. Seat filling is then a pure engagement play needing an explicit business decision. |
| N's cannibalization below G's at similar fills | Adopt N's framing in any seat-fill messaging NYT already sends |
| Cancellation HR lower bound > 1.0 | **Stop** |

### 3.10 Risks

- **Revenue sign likely negative** (see the break-even above).
- **Primary outcome is unpowered.**
- **Third-party blind spot.**
- **Public link leakage.**
- **Movement from another family plan** creates negative spillover between clusters.
- **Invitations sent through NYT:** the owner's act triggers NYT to email the invitee, a third party. The consent position needs legal review.
- **Owners find repeated "open seats" mail pushy.**

### 3.11 Unverified facts to check before launch

1. The current All Access Family price ($34 or $30).
2. Count of 2–3-person direct-billed All Access Family plans.
3. Whether invite → redemption lineage is logged.
4. Whether Apple and Google subscriptions are linked to NYT accounts.
5. Whether an App Store subscriber must cancel before joining as a member.
6. Whether invite links are single-use.
7. Baseline organic fill rate.
8. Share of joiners who already pay.
9. Whether nudged fills reduce cancellation (the question under test).
10. How Bonus subscriptions interact with family plans.

---

## Cross-plan launch gate

Answer these before any plan launches. They come from Agent 4's open questions.

1. **Plan counts by type and seat count.** These set the arm counts and the layer split.
2. **Prices:**
   - $34 or $30;
   - the current Games Family price and billing period;
   - whether owners qualify for the intro price on upgrade.
3. **NYT's current randomization unit.** This decides how much the audit arms can teach.
4. **Consent rules** for member email and push, and whether request digests and invitation emails are transactional or marketing (legal).
5. **Lineage:**
   - plan_id persistence through upgrade;
   - invite → redemption;
   - third-party receipt linkage.
6. **Leaderboard:** what it shows, and whether it links plans.
7. **Guardrail thresholds and email-pool strategy (C6).** The thresholds proposed above need business sign-off.

**Recommended sequencing (inference):**
- Build Plan 1 first. It builds the shared data foundation and the request infrastructure.
- Run Plan 2 in parallel on its layer.
- Run Plan 3 wave 1 (G and N) once the invitee classifier is validated.
- Add arm M only after Plan 1 ships.