# Agent 5: Full experiment plans

**What this covers.** Full plans for Agent 4's three selections only:
- **A** (P1+P3): plan-level upgrade, owner offer × member request
- **B** (P4+P7): plan challenge, idle-seat reactivation and interference detector
- **C** (P2): whole-plan trial, second wave

P5 and P8 are not revived. P6 survives only as the accounting rule below.

**Conventions shared by all three plans**

- **Prices are unverified.** I did no new verification at this stage. The upgrade gap is a range throughout:

| Scenario | Games Family | All Access Family | Δ per 4 wk | Δ per year |
|---|---|---|---|---|
| GF billed 4-weekly, AAF $30 | $10 × 13 = $130/yr | $390/yr | +$20 | +$260 |
| GF billed 4-weekly, AAF $34 | $130/yr | $442/yr | +$24 | +$312 |
| GF billed monthly ($120/yr), AAF $30 | $9.23 per 4 wk | $390/yr | +$20.77 | +$270 |
| GF billed monthly, AAF $34 | $9.23 per 4 wk | $442/yr | +$24.77 | +$322 |
| **Owner gets $8 intro on upgrade** | $120–130/yr | $8 × 13 = $104 in year 1 | −$1.23 to −$2 | **−$16 to −$26 in year 1** |

  - Prices and billing cycle come from Agents 1 and 4, single-source or launch prices.
  - Year-1 revenue changes sign under intro pricing. That is why every revenue decision rule below depends on the verified price policy.

- **Net-revenue accounting (the P6 rule, applied everywhere).** For each plan p, define the *plan cluster* as everyone who was a seat at randomization plus anyone who joins later.
  - R_p = plan billing + all standalone NYT subscription revenue of every person in the cluster, across every billing channel, net of app-store fees, from randomization to the horizon.
  - The estimand is E[R_p | arm] − E[R_p | control].
  - This equals the brief's formula (plan Δ − members' cancelled standalone subscriptions − invitee cancellations), with no double counting.
- **Metric conventions.**
  - Report **seats with access** and **net plan revenue**, never raw "subscribers". A family plan counts as 2 billed/additional subscribers whatever its seats ([SEC 8-K Q3 2026](https://www.sec.gov/Archives/edgar/data/0000071691/000007169126000039/pressrelease9302026.htm)).
  - Subscriber counts appear only as a finance translation.
  - Retention is always a **plan** event: the cancellation hazard of the plan_id.
- **Statistical constants.** Two-sided α = 0.05 gives z = 1.960. Power 80% gives z = 0.8416. (z_α + z_β)² = 2.8016² = **7.849**.
- **Method references.** Lin (2013) regression adjustment and Schoenfeld's events formula are standard methods, named but not re-verified at this stage. All other design citations come from Agent 2's verified list.

---

## Plan A: Plan-level upgrade, owner offer × member request

**Pitch.** Move Games Family plans to All Access Family by pairing an owner offer with a consented, member-initiated "Request All Access for our plan" button. The whole plan is treated in one 7-day window, and the plan is the unit.
**From cards:** P1 + P3, with the P6 accounting rule.

### Hypothesis and expected signs

| Effect | Path | Expected sign |
|---|---|---|
| Direct | Owner offer → owner upgrades | **+** |
| Spillover, member → owner (bipartite) | Member request → owner upgrades | **+** (core hypothesis) |
| Spillover, owner → members | Upgrade → untreated members use News, Cooking and Athletic | **+** on unlocked products; ≈0 on Games |
| Negative spillover | Owner annoyed by requests → removes members or cancels Games Family | **−** (guardrail) |
| Total, arm C vs holdout | | **+** on upgrades. Revenue: **+** at regular price, **−** in year 1 if the $8 intro applies |

### Treatment arms

| Arm | Owner receives | Members receive |
|---|---|---|
| **0 Holdout** | Business as usual (BAU); no upgrade messaging from this test | BAU paywall |
| **A Owner offer** (k = 3 touches) | Day 0 email; in-app card on first session in days 0–7; day 5 reminder email. Each deep-links to the upgrade flow at the price policy verified before launch | BAU (untreated) |
| **A′ Dose-matched owner** (optional, only if power allows, see below) | Same 3 touches, plus additional owner touches equal to the plan's expected member touches in C (one per member, in days 0–7) | BAU |
| **C Coordinated** | Same 3 touches as A, plus **request digests** (below) | Day 0 push (opt-in only) and an in-app card in days 0–7: "Your plan could include Cooking, News and The Athletic. Ask the person who manages your plan." The paywall (News, Cooking, Athletic) shows a **"Request All Access for our plan"** button for 8 weeks |

**Request-button rules (required fixes):**
- **Member-initiated only.** Nothing about members' reading or play is reported passively.
- Before sending, the member sees a preview of exactly what the owner will see: a request count, the product category the member chose, and optionally the member's name (opt-in).
- Copy says "the person who manages your plan", so no member needs to identify the owner. Whether members can see the owner is unverified, and this wording makes it irrelevant.
- **Owner cap:** at most 1 digest per 7 days and at most 3 in the experiment. Requests are batched.
- Member messaging only goes to members with email/push consent. Members flagged as minors, or of unknown age, get no messaging if counsel requires it (age data availability is unverified).
- **Dropped:** the members-only arm without the button, and A1's passive "pooled-demand" counts.

### Unit, clusters, eligibility, contamination

- **Unit:** plan_id. Assignment = hash(plan_id ‖ salt_A), stratified, then **frozen** in an assignment table at entry.
- **Cluster source:** billing and entitlement tables (owner_id, plan_id) joined to the invite-redemption table (member user_ids, join dates).
- **Eligibility:**
  - Active Games Family plan, ≥2 seats filled at the snapshot.
  - Not past due, not in the cancellation flow, and ≥1 paid billing cycle completed.
  - Not in another pricing or plan test.
- **Strata:** seats filled (2/3/4) × tenure (<6 mo / ≥6 mo) × billing channel (web / Apple / Google) × prior-28-day member paywall hits (0 / 1–4 / 5+). That gives 3 × 2 × 3 × 3 = 54 cells; merge cells with fewer than 200 plans.
- **App-store owners.**
  - If verification shows no supported upgrade path for Apple- or Google-billed owners (Help Center: they must cancel through the store first), exclude them **before** randomization. You cannot test an outcome the unit cannot reach.
  - Otherwise include them, route them to a guided web flow, and pre-register heterogeneity by channel.
- **Contamination across clusters:**
  - **Person on 2+ plans** (unverified whether possible): build the plan–person bipartite graph and take its connected components. Either exclude multi-plan components (preferred if under 2%) or assign the whole component one arm.
  - **Membership churn after randomization (ITT):**
    - New invitees inherit the plan's arm.
    - Departing members stay in the plan cluster for revenue accounting.
    - An owner who transfers or recreates the plan is tracked through owner_id lineage.
  - **Offer leakage** (members forward offer emails; deal forums) is not interference between arms if the offer price equals the public price. Ensure it does.

### Design
- Stratified plan-level cluster RCT with 3 arms (4 if A′ runs).
- Saturation is a fixed policy per arm: owner-only vs all seats. It is not a within-plan randomized saturation, because the upgrade is a plan-level outcome. Plan B tests within-plan saturation.
- Run an A/A pre-period balance check and a sample-ratio-mismatch (SRM) test at launch.

### Estimands and estimators

| Estimand | Definition (plan-level unless noted) | Interpretation |
|---|---|---|
| τ_A | E[Y_p(A)] − E[Y_p(0)] | Total effect of the owner-only policy (direct effect on the payer) |
| τ_C | E[Y_p(C)] − E[Y_p(0)] | Total effect of the coordinated policy |
| τ_C − τ_A | | Value of member channel plus coordination, **including extra dose**: a policy comparison |
| τ_C − τ_A′ | | Member-request channel net of plan-level message volume (only if A′ runs) |
| Owner→member spillover | Member-seat outcome in A minus member-seat outcome in 0 | Members are untreated in A, so this is a **pure indirect effect** of treating the owner |
| Bipartite exposure | Owner received ≥1 request (within C) | Post-treatment and **not randomized**. Descriptive only |

- **Estimator.** Stratified difference in means, Σ_s w_s(Ȳ_s,arm − Ȳ_s,0) with w_s = stratum share. Report also the Lin regression-adjusted estimate (treatment × centred pre-period covariates).
- **Variance.**
  - Neyman stratified variance, Σ_s w_s²(s²_s,1/n_s,1 + s²_s,0/n_s,0), equivalently HC2 at the plan level.
  - The plan is the unit, so no further clustering is needed.
  - Robustness: Fisher randomization test (10,000 re-randomizations within strata).
- **Member-seat secondaries:** CR2 standard errors clustered on plan_id. Report both seat-weighted and plan-weighted averages (Basse & Feller weighting).
- **Multiplicity:** fixed sequence at α = 0.05, in order (1) τ_C > 0, (2) τ_A > 0, (3) τ_C > τ_A. A step is tested only if the previous step rejected.

### Metrics and read-out

| Tier | Metric | Window |
|---|---|---|
| **Primary** | Plan upgraded to All Access Family (binary) | 8 weeks from day 0 |
| Secondary: revenue | Net R_p (P6 rule) | 8 and 26 weeks |
| Secondary: engagement | Weekly active days per seat in News, Cooking and Athletic (ITT, all seats) | Weeks 1–8; 26 |
| Secondary: retention | Plan cancellation hazard (any downgrade or exit) | 26 weeks |
| Secondary: access | Seats with access to any bundle product; seats filled | 8, 26 weeks |
| Mechanism | Request rate per member, digests sent, share of upgrades preceded by a request | 8 weeks |
| **Guardrails** | Games Family cancellation (non-inferiority margin 0.5 pp at 8 wk); email unsubscribes and push opt-outs per seat; member removals by owner; standalone subscription cancellations within the cluster; support tickets and app-store refunds; Games plays per seat (no decrease beyond 5%) | Weekly monitoring; O'Brien–Fleming boundaries for harm only |

**Read-outs:** primary at week 8 plus 2 weeks of data lag; long-run read at week 26.

### Power

- **Formula** (two proportions, plan = unit, so design effect = 1):
  n per arm = (z_α + z_β)² · [p₀(1−p₀) + p₁(1−p₁)] / (p₁ − p₀)²
- **Assumptions:**
  - p₀ = 2.0% 8-week upgrade rate in the holdout (assumption, from Agent 4; no public data).
  - MDE = +0.5 pp, i.e. 25% relative (assumption).
  - ICC is irrelevant for the primary because the outcome is one per plan, so m = 1.

**Step 1: C vs 0** (p₀ = 0.020, p₁ = 0.025)
- 0.020 × 0.980 = 0.019600
- 0.025 × 0.975 = 0.024375
- Sum = 0.043975
- Δ² = 0.005² = 0.000025
- 0.043975 / 0.000025 = 1,759
- × 7.849 = **13,806 plans per arm**

**Step 2: C vs A**, assuming τ_A = 0.5 pp and τ_C = 1.0 pp (both assumptions), so p_A = 0.025 and p_C = 0.030
- 0.024375 + (0.030 × 0.970 = 0.029100) = 0.053475
- / 0.000025 = 2,139
- × 7.849 = **16,790 per arm**
- **Size every arm at 17,000.**

**Total plans needed**

| Arms | Plans |
|---|---|
| 3 arms (0, A, C) | 3 × 17,000 = **51,000** eligible plans |
| 4 arms (with A′) | **68,000** |

**Fallbacks by eligible base E** (E is unverified, so pre-register this table):

| E | Design |
|---|---|
| ≥ 68k | 0 / A / A′ / C |
| 51k – 68k | 0 / A / C |
| 41.4k – 51k | 0 / A / C. C vs 0 is confirmatory; C vs A is underpowered (report its MDE) |
| 27.6k – 41.4k | Rolling weekly enrolment of newly eligible plans over 12 weeks. If still short, run 0 vs C only |
| < 27.6k | Don't run as a randomized controlled trial (RCT). Extend the window to 12 weeks (raises p₀, assumed) and re-compute |

- **MDE at a given n:** Δ ≈ 2.8016 · √(2p̄(1−p̄)/n). Example: n = 10,000 at p̄ ≈ 0.02 gives √(2 × 0.0196 / 10,000) = 0.00198, and × 2.8016 = **0.55 pp**.
- **Member-engagement secondaries:**
  - Design effect DE = 1 + (m̄ − 1)ρ.
  - With m̄ = 3 seats (assumption) and ρ = 0.3 (assumption): DE = 1 + 2 × 0.3 = 1.6.
- **Revenue scale check** (inference):
  - 0.5 pp × 17,000 plans = 85 extra upgrades.
  - At regular price that is 85 × $260–$322 ≈ **$22k–$27k per year** per 17k plans.
  - Under the $8 intro, year 1 is 85 × (−$16 to −$26) ≈ **−$1.4k to −$2.2k**.
  - The build is justified only at portfolio scale or by the retention secondary.

### MVP build plan (in order)
1. **Verify facts first** (see checklist): prices, intro eligibility, app-store path, base size, multi-plan membership, randomization unit.
2. **Data**
   - Daily plan-roster snapshot: plan_id, owner_id, member_ids, join and leave dates, billing channel, tenure.
   - Person-to-standalone-subscription map across web, Apple and Google entitlements (needed for R_p).
   - Member paywall-hit events joined to plan_id.
3. **Assignment**
   - Eligibility and strata job; plan–person component check.
   - Hash plan_id with salt_A; frozen assignment table; inheritance rule for new invitees.
   - A/A balance report.
4. **Owner messaging**
   - Email and in-app templates, deep-linked to the upgrade flow.
   - Register them in the global frequency cap.
5. **Member channel**
   - Feature-flag the paywall button by plan arm; preview screen; request event log.
   - Digest batcher enforcing the 1-per-7-days and 3-total caps; consent and age filters.
6. **Upgrade flow** for the app-store-billed path, if in scope.
7. **Outcome pipeline:** plan-level table with upgrade, R_p, seats with access, cancellation; guardrail dashboard.
8. **Analysis:** pre-registered notebook and fixed-sequence tests, filed before launch.

### Decision rule (pre-registered)
- **Roll out C** if all of the following hold:
  - τ_C > 0 at the primary read;
  - 26-week net R_p effect is positive, with the 90% CI lower bound > 0 *under the verified price policy*;
  - the Games Family cancellation guardrail is non-inferior (upper CI bound < +0.5 pp);
  - opt-out and removal guardrails pass.
- **Roll out A instead** if τ_A > 0 and the C − A CI includes 0 with an upper bound below the cost of running the member channel (owned by product).
- **Iterate** if upgrades rise but net revenue is ≤ 0 (intro pricing or cannibalization). Next test: regular-price upgrade offer, or a 3-month intro.
- **Stop** if the τ_C CI upper bound is < 0.25 pp, or any harm boundary is crossed.

### Risks and unverified facts
- **Base size and p₀ are unknown.** They decide the number of arms.
- **Intro-price eligibility** decides the sign of year-1 revenue.
- **App-store upgrade friction:** cancel-then-rebuy may *cause* churn. That is a guardrail and possibly an exclusion.
- **Paywall-hit volume per member** may be too low for the button to matter; the mechanism metric tracks this.
- **Owner nagging:** member removals are a negative spillover; watch them.
- **Minors and consent;** counsel sign-off is required for member-to-owner messaging.
- **Within-cluster cannibalization** of standalone Cooking or Athletic subscriptions; R_p captures it.
- **Overlap with B:** see B's contamination section.

---

## Plan B: Plan challenge and idle-seat reactivation, with built-in interference detector

**Pitch.** A weekly, synchronized plan challenge plus idle-seat nudges to cut whole-plan cancellation. Half the plans are randomized by member and half by plan, which tests whether member-level tests of in-plan engagement nudges are biased.
**From cards:** P4 + P7, with the P6 accounting rule.

### Hypothesis and expected signs

| Effect | Definition | Sign |
|---|---|---|
| Direct | Nudged seat's own plays (co-members untreated) | **+** |
| Spillover | Untreated seat's plays rise because treated co-members appear on the leaderboard | **+** (small to moderate) |
| Complementarity | Nudged idle seat plays more when co-members are also nudged | **+** (hypothesis) |
| Total | All seats nudged vs control, per seat and per plan cancellation | **+** engagement, **−** cancellation hazard |
| Negative channels | Push fatigue → opt-outs; email sender reputation (C6) | **−** (guardrails) |
| Detector | Plan-randomized estimate vs member-randomized estimate | PR > MR if spillover is positive |

### Treatment arms (exactly what a "treated seat" receives)
- **Weekly push**, same calendar day and 6 pm recipient-local time (assumption): "This week's plan challenge: [puzzle]. See where you rank on your plan."
- **In-app card** linking to the **existing** plan leaderboard. The leaderboard itself is unchanged for everyone, so untreated seats can still see it. That visibility is the spillover channel.
- **If the seat has had no Games activity for ≥14 days:** one extra "Your plan is playing this week" nudge.
  - Push if opted in.
  - Otherwise email from a **dedicated experiment sending subdomain/IP pool** (C6 fix).
- **Frequency:** at most 2 experiment messages per seat per week, counted inside the global NYT cap and applied identically across arms.
- **Duration:** 26 weeks.

| Half | Arm | Who is treated |
|---|---|---|
| **PR (plan-randomized)**, stratum I (≥1 idle seat) | Control | Nobody |
| | Idle-only | Idle seats only |
| | All seats | Every seat |
| **PR**, stratum N (no idle seat) | Control | Nobody |
| | All seats | Every seat |
| **MR (member-randomized)** | Bernoulli(0.5) per seat | Each seat independently; plans end up mixed |

### Unit, clusters, eligibility, contamination
- **Population:** all family plans (Games Family and All Access Family) with ≥2 seats active in the prior 28 days.
- **Idle:** a seat (owner or member) with no Games activity for ≥14 days. Stratum I = plans with ≥1 idle seat.
- **Stage 1:** stratify by product × seats (2/3/4) × stratum I/N × tenure. Then hash(plan_id ‖ salt_B1) gives a 50/50 split into PR and MR.
- **Stage 2:**
  - PR: hash(plan_id ‖ salt_B2) assigns the arm, 1:1:1 in I and 1:1 in N.
  - MR: hash(user_id ‖ salt_B3) gives Bernoulli(0.5); store each plan's realized saturation.
- Assignment is frozen. Seats joining later are not treated in PR control; they inherit the arm in PR-treated plans and get a fresh Bernoulli draw in MR.
- **Leaderboard check (required).**
  - If Games Family plans have no leaderboard (unverified), restrict B to All Access Family plans, or drop the "rank" copy for Games Family and stratify by product.
- **Contamination**
  - **Across plans:** leaderboards are within plans, so cross-plan spillover runs only through people on 2+ plans (handled with the same component rule as A) or social ties outside the plan (assumed negligible; not interference *between arms* unless the ties are dense).
  - **Overlap with A** (Games Family plans in both):
    - Randomize **orthogonally** (independent salts) and stratify B's analysis by A arm.
    - Pre-register the A×B interaction as exploratory.
    - Push messages from A arm C and from B share the frequency cap. Monitor cap-binding rates by A×B cell.
  - **Sender pool:** experiment email goes through its own subdomain/IP pool. Track inbox placement for that pool against the main pool.

### Design
- Two-stage randomized saturation inside PR (Hudgens & Halloran; Baird et al.).
- PR vs MR split with a Hausman-style test (Saveski et al. 2017; LinkedIn 2019).
- The MR half also gives a natural Bernoulli saturation for exposure-mapping estimates (Aronow & Samii).
- If NYT already randomizes by account or plan (unverified), the MR half becomes a member-level pilot and needs an engineering change to hash on user_id inside plans.

### Estimands and estimators

| Estimand | Definition | Data |
|---|---|---|
| Direct (DE) | E[Y_idle-seat ∣ idle-only] − E[Y_idle-seat ∣ control] | PR stratum I |
| Spillover (IE) | E[Y_active-seat ∣ idle-only] − E[Y_active-seat ∣ control] (active seats are untreated) | PR stratum I |
| Complementarity | E[Y_idle-seat ∣ all] − E[Y_idle-seat ∣ idle-only] | PR stratum I |
| Total, per seat (τ_PR) | E[Y_seat ∣ all] − E[Y_seat ∣ control] | PR, both strata |
| Plan retention | Hazard ratio (HR) and 26-week cancellation difference, all vs control; idle-only vs control | PR (plan = unit) |
| Naive individual (τ_MR) | Mean of treated seats − mean of control seats | MR |
| MR spillover curve | E[Y_i(0, k)] − E[Y_i(0, 0)], with k = number of treated co-members | MR, Horvitz-Thompson (HT) weights π_i(z, k) = 0.5 · Binom(k; m_i−1, 0.5) |

- **Engagement:** seat-level regression with stratum fixed effects and pre-period plays as a covariate, CR2 standard errors clustered on plan_id. Report seat-weighted and plan-weighted versions.
- **Retention:** Cox model stratified by design strata, plan as unit, robust sandwich SE. Report also the 26-week restricted mean survival time (RMST) difference and the cancellation-proportion difference with Neyman variance.
  - **Retention is never estimated per member.**
  - In MR, plan cancellation is regressed on realized saturation as an exploratory analysis only.
- **Detector:** H = (τ̂_PR − τ̂_MR)² / (V̂_PR + V̂_MR) ~ χ²₁. The halves are independent, so there is no covariance term.
  - Pair it with an equivalence test (TOST) at a ±0.07 plays/week bound. Failing to reject is not evidence of no bias.

### Metrics and read-out

| Tier | Metric | Window |
|---|---|---|
| **Primary** | Plan cancellation hazard (PR: all vs control) | 26 weeks |
| Leading / detector | Games plays per seat per week, all seats including untreated seats on treated plans | Weeks 1–4, read at week 5 |
| Secondary: engagement | Seat reactivation (idle seat plays ≥1 in 14 days); active seats per plan | Weeks 1–4, 13, 26 |
| Secondary: revenue | Net R_p (P6 rule); downgrades from AAF to individual | 26 weeks |
| Secondary: access | Seats filled; seats with access | 26 weeks |
| **Guardrails** | Push opt-out per seat (≤ +1 pp, assumption); email unsubscribes or complaints and inbox placement of the experiment pool; non-Games engagement (no drop beyond 3%); frequency-cap binding rate | Weekly; harm-only O'Brien–Fleming |

**Read-outs:** detector and engagement at week 5; guardrail interim at week 13; retention at week 26.

### Power

**Primary: plan cancellation, PR all vs control**
- **Assumptions:**
  - 26-week plan cancellation p₀ = 8% (assumption, Agent 4).
  - MDE = −0.8 pp (10% relative), p₁ = 7.2% (assumption).
- **Two-proportion calculation:**
  - 0.08 × 0.92 = 0.073600
  - 0.072 × 0.928 = 0.066816
  - Sum = 0.140416
  - / 0.008² (0.000064) = 2,194
  - × 7.849 = **17,221 plans per arm**
- **Check with the Schoenfeld events formula** (1:1 allocation):
  - d = 4(z_α + z_β)² / (ln HR)², with HR = 0.9 and ln 0.9 = −0.10536, squared = 0.011101.
  - d = 4 × 7.849 / 0.011101 = 31.396 / 0.011101 = **2,828 events**.
  - Mean event probability (0.080 + 0.072)/2 = 0.076, so 2,828 / 0.076 = 37,211 plans = **18,606 per arm**.
  - **Use 18.6k, the conservative figure.**

**PR half size**
- Assumed idle-plan share q = 30% (assumption).
- The control arm gets q/3 + (1−q)/2 of the half = 0.10 + 0.35 = 0.45P. The all-seats arm is the same.
- 0.45P ≥ 18,606 gives **P ≥ 41,347**, so use P = 41.3k.
- The idle-only arm is q/3 × P = 0.10 × 41.3k = **4.1k plans**. Report its MDE; it is not confirmatory.

**MR half:** the same 41.3k under the 50/50 brief. **Total: 82.7k family plans with ≥2 active seats.** The base is unverified.

**Engagement (leading)**
- **Assumptions:**
  - σ = 2.5 plays/week per seat (4-week average).
  - m̄ = 2.8 seats.
  - ρ = 0.3.
- DE = 1 + 1.8 × 0.3 = **1.54**.
- **PR per arm:** 0.45 × 41,300 × 2.8 = 52,038 seats. V_PR = 2σ²·DE / n = 2 × 6.25 × 1.54 / 52,038 = 19.25 / 52,038 = 3.699e-4.
  - MDE = 2.8016 × √3.699e-4 = 2.8016 × 0.01923 = **0.054 plays/week** (easily powered).
- **MR half:** 41,300 × 2.8 = 115,640 seats. V_MR ≈ 4σ² / N = 25 / 115,640 = 2.162e-4. This is conservative because within-plan randomization removes some plan-level variance.

**Detectable bias**
- 2.8016 × √(3.699e-4 + 2.162e-4) = 2.8016 × √5.861e-4 = 2.8016 × 0.02421 = **0.068 plays/week**.
- Example: if the true total effect is 0.30 plays/week (assumption), a 23% understatement by the individual design is detectable. That is in the range Holtz et al. found (≥20%).

**Fallback if the base is below 82.7k** (a deviation from the 50/50 brief that needs sign-off)
- Keep PR at 41.3k and give MR the remainder.
- With a 10k-plan MR half: V_MR = 25 / 28,000 = 8.93e-4. The sum with V_PR is 1.263e-3, √ = 0.0355, and × 2.8016 gives a detectable bias of **≈0.10 plays/week**.
- If PR itself cannot reach 41.3k:
  - extend the horizon to 39 weeks (more events), or
  - accept MDE = 2.8016 × √(2p̄(1−p̄)/n) at the achievable n.

### MVP build plan (in order)
1. **Verify:**
   - leaderboards on Games Family;
   - current randomization unit and whether the platform can hash on user_id within a plan;
   - push opt-in rates;
   - base size and churn.
2. **Data**
   - Per-seat daily Games activity.
   - Plan roster snapshot shared with A.
   - Idle flag job.
   - Plan cancellation events with reason codes.
   - Standalone-subscription map for R_p.
3. **Assignment:** two-stage hashing (salt_B1, salt_B2, salt_B3); store realized MR saturation; A/A and SRM checks.
4. **Content:** weekly challenge selection (an existing daily puzzle, so no new puzzle production); push and in-app card templates; local-time scheduler.
5. **Idle-seat nudge** and the dedicated email subdomain/IP pool, warmed up before launch (warm-up time unverified).
6. **Frequency-cap integration;** cap-binding logs per A×B cell.
7. **Outcome pipeline:** plays per seat (including untreated seats on treated plans), plan cancellation hazard, R_p.
8. **Analysis:** pre-registered detector test, saturation estimands, HT exposure estimator.

### Decision rule
- **Roll out all-seats** if the HR upper 95% bound is < 1 (or the 26-week cancellation reduction CI excludes 0), net R_p ≥ 0, and the guardrails pass.
- **Roll out idle-only** (cheaper, less fatigue) if it is within 80% of all-seats on retention and better on opt-outs. This is descriptive, given its MDE.
- **Iterate** if engagement rises but retention is null at 26 weeks. Test a lower-frequency version and extend follow-up.
- **Stop** if engagement is null at week 5 (CI upper bound < 0.05 plays/week) or a harm boundary is crossed.
- **Detector outcome sets company policy:**
  - **H rejects with PR > MR:** in-plan engagement nudges must be plan-randomized.
  - **H does not reject and TOST passes (difference < ±0.07):** member-level randomization is acceptable for this lever class.
  - **Otherwise:** inconclusive. Default to plan randomization, since its power cost at 2–4 seats is small.

### Risks and unverified facts
- **High baseline retention** (Cotton's quote, which is about family vs individual and gives no number) may compress the effect. The 8% churn baseline is an assumption.
- **Push opt-in may be low,** so the in-app card carries the treatment. ITT is diluted.
- **Interaction with A** on Games Family plans; cap crowding.
- **The MR half requires within-plan user hashing** (feasibility unverified).
- **Sender-pool warm-up** cost and timing.
- **Minors on plans** need consent rules for pushes.

---

## Plan C: Whole-plan All Access trial (second wave)

**Pitch.** Unlock All Access for every seat of a Games Family plan for 21 days, then offer the owner the upgrade. Compare against a trial for the most active seat only, and against no trial.
**From card:** P2, with the P6 accounting rule. It launches **after A's primary read** and is mutually exclusive with A.

### Hypothesis and expected signs

| Effect | Sign |
|---|---|
| Direct (trial seat's own post-trial engagement) | **+** |
| Within-plan spillover (one-seat arm: non-trial seats, via shared links and leaderboard visibility) | Small **+**, possibly ≈0 |
| Cluster increment (all seats vs one seat: shared habit, visible demand) | **+** (core hypothesis) |
| Deprivation at trial end (loss of access → base plan cancellation) | **−** (co-primary non-inferiority) |
| Total revenue | **+** at regular price; depends on intro policy |

### Treatment arms

| Arm | Days 0–21 | Day 21 |
|---|---|---|
| **N No trial** | BAU | Owner offer, identical to A's arm A (3 touches over 7 days) |
| **S Most-active seat** | All Access entitlement for the seat with the most Games sessions in the prior 28 days (tie-break: owner). Day 0 and day 14 in-app notes | Same owner offer |
| **W All seats** | All Access entitlement for every seat, with the same notes to each seat | Same owner offer |

- Trial length of 21 days is an assumption chosen within P2's 14–28-day range.
- No billing change; the entitlement auto-expires.
- Members' own requests (A's button) are **not** used, keeping C mutually exclusive with A's mechanism.

### Unit, clusters, eligibility, contamination
- **Unit:** plan_id, with the same roster, component rule and strata as A, plus "most-active seat is the owner" (yes/no) as a stratum. In S, if the most-active seat is usually the owner, arm S is effectively an owner-only trial; report that.
- **Population (applying Agent 4's "reuse A's holdout")**
  - After A's 8-week primary read, a pre-registered **30% of A's holdout is reserved** and never enters C. A's 26-week revenue and retention comparisons use it.
  - The other 70% plus newly eligible Games Family plans (never in A) form C's pool.
  - **Alternative:** wait until A's week-26 read and use the whole holdout. That costs about 18 weeks.
- **Exclusions:** plans that upgraded; plans whose members hold standalone All Access (the trial would change nothing for them; flag it).
- **Contamination:** the one-seat arm's trial seat may share gift links with co-members. This is a measured within-plan spillover, not between plans. Cross-plan contamination follows A's component rule.

### Estimands and estimators
- τ_W = E[Y(W)] − E[Y(N)] and τ_S = E[Y(S)] − E[Y(N)]: total effects of each trial policy, plan-level.
- **τ_W − τ_S:** the cluster increment. It inherently includes dose (more seats trialled); that is the policy question.
- **Spillover in S:** non-trial seats in S vs matched seat positions in N. Post-trial engagement, CR2 on plan_id.
- **Estimators:** stratified difference in means with Neyman variance (HC2 at plan level); Fisher randomization test as robustness. Cancellation: Cox, stratified, plan-level.
- **Multiplicity:** fixed sequence (1) τ_W > 0, (2) τ_W > τ_S, (3) τ_S > 0. Cancellation non-inferiority is tested separately at one-sided α = 0.05.

### Metrics and read-out

| Tier | Metric | Window |
|---|---|---|
| **Primary** | Plan upgrade to All Access Family | 28 days after trial end |
| **Co-primary (non-inferiority)** | Plan cancellation (Games Family exit), margin +1 pp | 60 days after trial end |
| Secondary | Post-trial engagement per seat in News, Cooking and Athletic (**trial-period engagement excluded**, as it is mechanically inflated); net R_p; seats with access | Weeks 4–12 from start; 26 weeks |
| Guardrails | Standalone Cooking or Athletic cancellations during the trial; support tickets; marginal trial cost (audio and third-party rights unverified) | Weekly |

### Power

**τ_W vs τ_S** (the hard comparison)
- **Assumptions:** S conversion 3.5%, W conversion 4.5% (MDE +1.0 pp); N conversion 2.5%.
- 0.035 × 0.965 = 0.033775
- 0.045 × 0.955 = 0.042975
- Sum = 0.076750
- / 0.01² (0.0001) = 767.5
- × 7.849 = **6,024 plans per arm**, so **18.1k plans total**.

**MDE for τ_W vs N at n = 4,000** (if the pool is short)
- √(0.024375 + 0.035631) = 0.2450
- / √4000 (= 63.25) = 0.003873
- × 2.8016 = 0.0109
- So MDE ≈ **1.1 pp**. Trial lifts of this size are plausible but unverified.

**Cancellation non-inferiority**
- **Assumptions:** 60-day cancellation 3%; margin 1 pp.
- n = (1.645 + 0.8416)² × 2 × 0.03 × 0.97 / 0.01²
- = 6.183 × 0.0582 / 0.0001 = **3,598 per arm**, so 6k per arm is sufficient.

**Supply**
- 70% of A's 17k holdout ≈ 11.9k plans.
- About 6.2k newly eligible plans are needed. The growth rate of the Games Family base is unverified.
- If supply is short, enrol on a rolling basis for up to 12 weeks, or pre-register τ_W vs N as the only confirmatory test.

### MVP build plan (in order)
1. **Verify:**
   - whether a trial changes intro-price eligibility;
   - audio and third-party rights;
   - the entitlement system's support for temporary per-seat and per-plan grants with no billing record.
2. **Entitlement service:** time-boxed All Access grant at plan or seat level; auto-expiry; audit log.
3. **Most-active-seat selector** and stratum flag.
4. **Assignment** from A's released holdout plus new plans; A/A check.
5. **Messaging:** trial-start and day-14 notes; reuse A's arm-A owner-offer templates at day 21.
6. **Outcome pipeline:** post-trial engagement, conversion, 60-day cancellation, R_p.
7. **Pre-registered analysis.**

### Decision rule
- **Roll out W** if τ_W > 0, τ_W > τ_S, cancellation is non-inferior (upper bound < +1 pp), and net R_p at 26 weeks is > 0 under the verified price policy.
- **Roll out S** if τ_S > 0 and τ_W ≈ τ_S (the difference CI includes 0) while W costs more.
- **Iterate** if conversion rises but deprivation churn breaches the margin. Test a soft landing, e.g. a step-down offer at trial end.
- **Stop** if neither trial beats N by more than the cost of the trial.

### Risks and unverified facts
- **Deprivation churn** at trial end.
- **Intro-eligibility interaction** with trials.
- **Rights cost** for non-owned content.
- **Holdout reuse** weakens A's long-run read (mitigated by the 30% reserve).
- **Owner-dominant plans** make S ≈ owner-only.

---

## Pre-launch verification checklist (blocks all three plans)

| # | Fact | Blocks | How to check (internal) |
|---|---|---|---|
| 1 | Live prices: AAF $30 or $34; GF billed monthly or every 4 weeks | A, C revenue | Pricing service, live checkout |
| 2 | Are existing GF owners eligible for the $8 AAF intro? | A, C sign of year-1 revenue | Offer eligibility rules |
| 3 | Counts of GF and AAF plans; seat distribution; idle share; 8-week upgrade rate; 26-week and 60-day cancellation | Power for all three | Billing warehouse |
| 4 | Current randomization unit; can the platform hash on plan_id and on user_id within plan? | A, B detector | Experimentation platform |
| 5 | Upgrade path for app-store-billed owners; what happens to members' or invitees' standalone subscriptions on join or upgrade | A eligibility, R_p | Billing / Help Center owners |
| 6 | Can a person be on 2+ plans? Can members see the owner? | Contamination; A copy | Product spec |
| 7 | Do Games Family plans have leaderboards? | B scope | Games product |
| 8 | Push opt-in rates; email consent per member; age data and minors | A, B | Messaging and identity teams |
| 9 | Counsel sign-off: member-to-owner requests, minors, frequency of messaging | A, B | Legal |
| 10 | Leadership accepts seats with access and net R_p as decision metrics | All | Finance / exec |

**Sequencing.** Steps 1–4 first. If step 3 gives fewer than 27.6k eligible Games Family plans, A and C collapse to two-arm or rolling designs per the fallback tables. B runs on the larger all-family base and can launch in parallel with A, orthogonally randomized.