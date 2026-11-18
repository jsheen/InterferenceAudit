# Agent 4: Critique and ranking

**Budget used:** 6 of 8 searches, 7 of 8 fetches.

**Main findings**
- **The prize is real, but the main cards fix the unit more than they fix interference.** For P1–P4, interference only exists if you measure members one at a time. Make the plan the unit and the problem largely goes away. What these cards really test is how to design a cluster treatment (who gets nudged, when, and how many seats), not how to remove bias. That is still worth doing, but the "naive tests understate" framing overstates how novel this is.
- **Statistical power is the main unknown, and nobody can answer it from public data.** NYT does not report family plans separately. The Q3 2026 8-K groups them with group subscriptions in a footnote. So the number of Games Family plans, which caps P1, P2 and P3, is **unverified**.
- **Drop P5 and P8. Merge P1 with P3, and P4 with P7. Fold P6's accounting into every card.** Select **A (P1+P3)**, **B (P4+P7)** and **C (P2, second wave)**.

---

## 1. Audit of Agents 1–3

| Claim | Stage | Status | Note |
|---|---|---|---|
| A family plan counts as 2 subscribers | A1, A3 | **True, but miscited** | Not in Digiday (fetched). The source is NYT's Q3 2026 8-K: each family subscription "is counted as one billed subscriber and one additional subscriber" ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000071691/000007169126000039/pressrelease9302026.htm)). Cite that instead. |
| All Access Family $34, intro $8 (Oct 2026) | A1, A3 | **Unverified, single source** | Only [subscriptiongauge](https://subscriptiongauge.com/service/new-york-times) gives $34. Other 2026 trackers still show $30, and no source reports a price increase. **A3 using +$24 as the base case is aggressive.** Use the range +$20 to +$24 per plan per 4 weeks. |
| Games Family $10 "per month" | A1 | **Launch price verified, billing cycle not** | Nieman gives both "$10/month" and "$120/year" ([Nieman](https://www.niemanlab.org/2025/09/the-new-york-times-launches-a-family-subscription-with-separate-wordles-for-everyone/)). NYT normally bills every 4 weeks; $10 every 4 weeks would be $130 a year. Whether the cycle is 4-weekly or monthly is unverified, so the size of the upgrade gap is not exact. |
| Family plan = All Access + $5 at launch | A1 | Verified | Digiday: $30 vs $25. Press Gazette's "$20" is still a conflict. |
| Cotton: someone "sharing a plan with 3 others" is "much less likely to cancel" | A1 | **Paraphrase drift** | The actual quote is "much less likely to cancel than someone who's subscribed just for themselves" ([Digiday](https://digiday.com/media/how-the-new-york-times-is-betting-on-a-new-family-plan-to-grow-its-digital-subscriber-base-and-revenue/)). It says nothing about 3 others. |
| Cannibalization is "relatively small" | A1–A3 | Verified as the company's own claim | Based on "tests and modeling", with no numbers. |
| Prices are "subject to promotions and experimentation" | A1 | **Not in Nieman** | Axios says "depending on promotional pricing". Treat the exact phrase as unverified. |
| Shared leaderboards; "up to you to decide … your family" | A1 | Verified | Nieman. It does not say whether Games Family has leaderboards, as opposed to only All Access Family. |
| Members can see the owner / request an upgrade | A1 Q3, A3 P3 | **Unverified** | The [Help Center](https://thenewyorktimeshelpcenter.helpjuice.com/115002788207-Subscriptions/family-subscription) says only the primary subscriber manages invites and billing. Invites go out by email or a shareable link, so link invitees may not know who the owner is. |
| App-store-billed users must cancel through Apple or Google before buying a family plan | new | Verified (Help Center) | **A feasibility constraint A1–A3 missed.** Games Family owners billed through an app store may not be able to upgrade in one click. Stratify on billing channel. |
| Search snippet: "invitees often already have a subscription" | — | **Not on the fetched page** | Discarded. What happens to an invitee's existing subscription (auto-cancel, proration) is unverified. |
| Holtz et al.: ≥20% interference bias | A2 | Verified | It is a lower bound. 25% of clusters were Bernoulli-randomized and 75% cluster-randomized. The authors say the meta-experiment is underpowered. |
| LinkedIn 0.81 vs 0.24, 10k clusters | A2 | Verified | The metric is not named and no p-value is given. Don't cite it as a measured size of bias. |
| BAFF, arXiv 2609.08725 | A2 | Verified it exists | Oh, Choi, Youn, Kim. It is about RTB filters and only loosely relevant to C5. |
| Basse & Feller "JASA accepted" | A2 | Unverified (not checked) | Minor. |
| Context: Q3 2026 has 13.22M digital-only subscribers, ARPU $9.93, retention described as "strong" | new | Verified ([8-K](https://www.sec.gov/Archives/edgar/data/0000071691/000007169126000039/pressrelease9302026.htm), [Q3 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/ny-times-nyt-q3-2026-earnings-call-transcript/)) | Management is "really excited" about family plans but gave no numbers. |

**Errors of reasoning in the earlier stages**
- **A1's "pooled-demand" message is a privacy problem.** A1 suggested telling the owner "members hit the paywall 14 times". That shows a member's reading behaviour to the person who pays, without the member's consent. Family plans can include teenagers or adult children, and age limits are unverified. Drop it. P3's explicit, member-initiated request is the consent-safe version.
- **A2's "≤4× design effect" is right as a bound but beside the point.** Upgrade and cancellation happen once per plan, so the plan is the n. With 2–4 seats per plan, the cluster arm in P7 is **not** high-variance the way LinkedIn's was. A3's P7 risk statement is too pessimistic about that.
- **Intro-price sign flip.** If owners get the $8 intro, the upgrade *reduces* year-1 revenue versus staying at $10, by about $2 per 4 weeks per plan. That makes the sign of P1–P3 depend on an unverified policy.
- **Missing cannibalization inside the plan.** Members of a Games Family plan may already pay for standalone Cooking or Athletic. An upgrade to All Access Family can cancel those subscriptions. None of the cards net this out.

---

## 2. Card-by-card critique

**P1. Coordinated plan-wide upgrade push**
- **Interference:** real, but it lives inside the plan, and plan randomization handles it.
- **The design flaw is dose:** arm C (all seats) delivers more total messages than arm A (owner only). So C > A could be volume, not coordination or complementarity.
  - Fix: add a dose-matched owner arm (same number of touches), or call the comparison a policy comparison rather than a complementarity test.
- **Arm B makes no sense alone:** members can't buy the upgrade. It needs P3's request mechanism to have any path to the outcome.
- **Power (inference):** suppose an 8-week baseline upgrade rate of about 2%, and you want to detect a +25% relative lift (0.5 pp) at α=.05 and 80% power. That needs about 14k plans per arm, or about 55k plans for 4 arms, before correcting for multiple comparisons. If Games Family has only tens of thousands of plans, cut to 3 arms or pool over time.
- **Feasibility:** low build effort. Constraints are app-store billing and each member's email/push consent.
- **Value:** +$20–24 per plan per 4 weeks, less the intro discount and the standalone subscriptions it cannibalizes.

**P2. Whole-plan All Access trial**
- **Interference:** plausible (habit-building across seats, plus visible demand).
- **The comparison is good:** "most active seat only" is the right individual counterfactual. Also add a no-trial control.
- **Engagement measured during the trial is mechanically inflated.** Use engagement after the trial, the plan cancellation hazard, and conversion.
- **Risk of losing access when the trial ends:** real and testable.
- **Athletic "licensing limits" are probably a non-issue,** since NYT owns The Athletic. Rights for audio or third-party content are unverified.
- **It competes with P1 for the same Games Family plans.** Run it sequentially or with mutually exclusive allocation.

**P3. "Ask the plan owner" button**
- **The strongest mechanism idea:** an explicit, consented demand signal sent from a member to the owner. The bipartite framing is correct.
- **Volume:** paywall hits per Games Family member per month are unknown. If they are rare, effects will be small and noisy.
- **Unverified:** whether members can identify the owner, especially invitees who joined by link.
- **Merge into P1** as the member channel.

**P4. Plan challenge and idle-seat reactivation**
- **Mechanism:** the most direct test of complementarity. The saturation arms (idle seat only vs all seats) cleanly identify spillover.
- **Bigger base:** it can include All Access Family plans.
- **Retention power is the problem (inference):** with an assumed 6-month plan cancellation of about 8% and a target reduction of 0.8 pp, it needs about 18k plans per arm. Use engagement as the leading indicator and cancellation hazard as the primary metric with a long horizon.
- **Constraints:** push opt-in rates and fatigue (C6 sender reputation applies if email is used).
- **Learning value is high,** because member-level randomization of engagement nudges is technically possible here. That makes it the natural host for P7.

**P5. Second person in a household → family offer**
- **Cluster:** the inferred household is noisy (CGNAT, offices).
- **Privacy:** messaging subscriber X because *another person's* device read behind the paywall at X's IP reveals one person's behaviour to another. Inferring households also raises state-privacy-law questions; legal analysis not done, flag for counsel.
- **Revenue:** the net sign is likely negative (a $30 sale collapses to +$4).
- **Feasibility:** high engineering cost.
- **Verdict: drop.** Revisit only as a passive, opt-in "add someone to your plan" prompt.

**P6. Steer invites to non-subscribers**
- **The accounting is essential** and belongs in every card: credit invitee outcomes to the owner's arm and report net revenue.
- **The "hold/compare screen" adds friction** for a paying subscriber leaving one product for another. That is a brand risk and potentially a cancellation-law risk; I did not check the state auto-renewal laws, so flag for counsel.
- **Invite volume is likely low.**
- **Email matching misses** subscribers billed through an app store.
- **Verdict:** fold the accounting rule into A and B. Park the steering treatment.

**P7. Interference detector**
- **Cheap and highly informative:** with clusters of 2–4, the cluster arm loses little power.
- **But it only applies where member-level randomization is meaningful,** i.e. engagement nudges, not owner-paid upgrades.
- **Moot if NYT already buckets by account or plan** (unverified).
- **Verdict:** merge into P4.

**P8. Geo (DMA) family offer**
- **Wrong cluster for the channels it targets.** Household substitution is within the household. Deal-forum leakage has no geography (A2 gap #5).
- **Power:** about 210 DMAs with a highly concentrated audience gives very high variance.
- **Legal:** geographic and personalized price variation needs review. I believe New York's algorithmic-pricing disclosure law may apply to personalized offers, but I did not verify this; flag for counsel.
- **Verdict: drop.**

---

## 3. Scores

Weights: materiality 0.25, method 0.25, feasibility 0.2, value 0.2, learning 0.1.

| Card | Material | Method | Feasible | Value | Learning | **Weighted** |
|---|---|---|---|---|---|---|
| P1 | 4 | 3 | 4 | 4 | 4 | **3.75** |
| P7 | 3 | 4 | 5 | 2 | 5 | **3.65** |
| P4 | 3 | 4 | 4 | 3 | 4 | **3.55** |
| P2 | 4 | 3 | 3 | 4 | 3 | **3.45** |
| P3 | 4 | 3 | 3 | 3 | 4 | **3.35** |
| P6 | 4 | 3 | 3 | 3 | 3 | **3.25** |
| P5 | 3 | 2 | 1 | 2 | 2 | **2.05** |
| P8 | 2 | 1 | 3 | 2 | 2 | **1.95** |

## 4. Ranking and justification

1. **P1+P3 (merged → A):** highest value. The member request is what makes the member arm meaningful, and the plan is the natural unit.
2. **P4+P7 (merged → B):** clean saturation test of complementarity. It is the only place the member-vs-plan detector is meaningful, and it covers the larger All Access Family base.
3. **P2 (→ C, second wave):** a strong mechanism, but it shares A's population and carries the risk of losing access after the trial.
4. **P6:** keep the accounting and **drop the treatment as a standalone card.**
5. **P5: drop.** Privacy risk, likely negative net revenue, and high engineering cost.
6. **P8: drop.** Wrong cluster for its channels, and too few units.

## 5. Briefs for Agent 5

### A. Plan-level upgrade: owner offer × member request (P1+P3)
- **Scope:** Games Family plans with 2 or more seats filled. Stratify by seats, tenure, billing channel (web vs Apple/Google) and prior paywall hits by members.
- **Unit:** plan_id, hashed and frozen at entry. The outcome is plan-level.
- **Arms (keep to 3–4):**
  - (0) holdout;
  - (A) owner offer, k touches;
  - (A′) owner offer, dose-matched to arm C (optional, only if power allows);
  - (C) owner offer plus a member "Request All Access for our plan" button at the paywall, sent to all seats in the same 7-day window.
- **Required fixes:**
  - Drop the members-only arm unless it includes the request button.
  - No passive reporting of members' behaviour to the owner. The owner sees only the requests members chose to send.
  - Net revenue = plan Δ − members' cancelled standalone subscriptions − invitee cancellations (the P6 rule).
  - Pre-register the analysis: plan-level comparison, with heterogeneity by billing channel.
- **Constraints:**
  - Email and push consent per member.
  - The app-store upgrade path for owners billed through Apple or Google.
  - Possible minors on plans.
  - A cap on how often an owner can receive requests, so they don't feel nagged.
- **Still unverified:** current prices; billing cadence; whether owners are eligible for the intro price; size of the Games Family base and its baseline upgrade rate; whether members can identify the owner; whether a person can belong to more than one plan.

### B. Plan challenge and idle-seat reactivation with built-in interference detector (P4+P7)
- **Scope:** all family plans (Games Family and All Access Family) with 2 or more active seats, plus a slice where an idle seat exists.
- **Design:**
  - First, split plans 50/50 into a member-randomized half and a plan-randomized half, after stratifying.
  - Inside the plan-randomized half, run the saturation arms: idle seat only / all seats / control.
  - Hausman-style test of whether the two halves' estimates differ.
- **Outcomes:**
  - Primary: plan cancellation hazard over 6 months or more.
  - Leading: plays per seat in weeks 1–4.
  - Measure on all seats, including control members on treated plans.
- **Required fixes:**
  - Measure retention per plan, never per member.
  - Separate push or email sending pools, or cap frequency, to limit the C6 sender-reputation channel.
  - Check that Games Family plans actually have leaderboards.
- **Unverified:** baseline plan churn; push opt-in rates; NYT's current randomization unit (if tests are already plan-hashed, the detector shrinks to a "member-level" pilot).

### C. Whole-plan All Access trial (P2), second wave after A
- **Arms:** no trial / most-active seat only / all seats, each followed by an owner offer at the end of the trial.
- **Primary metrics:** conversion; plan cancellation hazard over the 60 days after the trial (to catch the effect of losing access); engagement after the trial only.
- **Allocation:** mutually exclusive with A. Reuse A's holdout plans.
- **Unverified:** content rights for any non-owned content; trial cost; whether a trial changes eligibility for intro pricing.

## 6. Open questions for a human

1. **Live prices and billing cycle:** All Access Family ($30 or $34), Games Family ($10 per month or per 4 weeks), and the size of the upgrade gap.
2. **Intro-price eligibility:** can existing Games Family owners get the $8 intro on an upgrade? This decides the sign of year-1 revenue for A and C.
3. **Base size:** how many Games Family and All Access Family plans exist, the distribution of seats, the baseline 8-week upgrade rate and the 6-month plan cancellation rate. These decide power and the number of arms.
4. **NYT's current randomization unit** (cookie, user, account or plan) and whether the platform can hash on plan_id.
5. **Upgrade path for app-store-billed owners,** and what happens to an invitee's or member's existing standalone subscription when they join or upgrade.
6. **Visibility:** can members see who the owner is, and can a person be on two plans (cross-plan contamination)?
7. **Privacy and legal sign-off:** member-to-owner messaging, age limits and minors on plans, consent per member, cancellation-flow rules for any P6-style friction, and pricing-law review for any personalized or geographic pricing.
8. **Reporting:** will leadership accept "seats with access" and net plan revenue as decision metrics, given that reported subscribers count a plan as 2 regardless of seats?

---

**Sources**
- [NYT Q3 2026 8-K press release (SEC)](https://www.sec.gov/Archives/edgar/data/0000071691/000007169126000039/pressrelease9302026.htm)
- [NYT Q3 2026 earnings call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/11/04/ny-times-nyt-q3-2026-earnings-call-transcript/)
- [Digiday – NYT family plan](https://digiday.com/media/how-the-new-york-times-is-betting-on-a-new-family-plan-to-grow-its-digital-subscriber-base-and-revenue/)
- [Nieman Lab – NYT family subscription](https://www.niemanlab.org/2025/09/the-new-york-times-launches-a-family-subscription-with-separate-wordles-for-everyone/)
- [NYT Help Center – Family Subscription](https://thenewyorktimeshelpcenter.helpjuice.com/115002788207-Subscriptions/family-subscription)
- [subscriptiongauge – NYT prices](https://subscriptiongauge.com/service/new-york-times)
- [Axios – NYT family plans](https://www.axios.com/2025/09/08/nyt-family-subscription-plans)
- [Press Gazette – NYT family subscriptions](https://pressgazette.co.uk/paywalls/new-york-times-family-subscriptions/)
- [Holtz et al., Management Science (RePEc)](https://econpapers.repec.org/RePEc:inm:ormnsc:v:71:y:2025:i:1:p:390-406)
- [Holtz et al. (pdf)](https://business.columbia.edu/sites/default/files-efs/citation_file_upload/holtz-et-al-2024-reducing-interference-bias-in-online-marketplace-experiments-using-cluster-randomization-evidence-from%20%282%29.pdf)
- [LinkedIn – A/B test of A/B tests](https://www.linkedin.com/blog/engineering/ab-testing-experimentation/detecting-interference-an-a-b-test-of-a-b-tests)
- [BAFF, arXiv 2609.08725](https://arxiv.org/abs/2609.08725)