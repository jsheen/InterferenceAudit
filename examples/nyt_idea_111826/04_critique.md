I've finished the spot-checks and written up the audit, scores, ranking and briefs below.

# Agent 4: Critique, scoring, ranking and briefs

**Bottom line**
- **Select three prototypes:**
  - **A** = P1 + P3, with P7 folded in as an audit arm (the Games Family → All Access Family upgrade).
  - **B** = P4 (plan-level retention).
  - **C** = U1 + P6 (filling empty seats on All Access Family plans, with invitees credited to the owner's arm).
- **Drop** P5 (privacy and brand risk) and P8 (DMAs are the wrong cluster for plans that span households). **Park** P2.
- **The biggest error carried through every stage:** Agent 1 says "new members are invited by an existing member". NYT's help center says **only the primary subscriber** can manage invites, billing and cancellation. That breaks part of P6 and part of the user idea as written, and it makes P3's "request" button more valuable.
- **What decides the business case:** NYT does not publish how many family plans it has, so we can't judge power for any plan-level design. Whether existing Games Family owners get the $8 intro price on an upgrade is still unverified.

---

## 1. Audit of Agents 1–3

| Claim | Stage | Verdict | Evidence |
|---|---|---|---|
| All Access Family $30 at launch; Games Family $10 | A1 | **Verified**. Digiday: "$30, $5 more than an All Access subscription"; Games Family "$10 a month, $4 more than an individual Games subscription". | [Digiday](https://digiday.com/media/how-the-new-york-times-is-betting-on-a-new-family-plan-to-grow-its-digital-subscriber-base-and-revenue/), [Nieman](https://www.niemanlab.org/2025/09/the-new-york-times-launches-a-family-subscription-with-separate-wordles-for-everyone/) |
| All Access Family now $8 intro, then **$34** / 4 wk | A1, A3 | **Unverified.** It still rests on one third-party tracker. Senior Daily's "$2 a week" only supports the $8 intro, not the $34. A July 2026 price history still lists $30. Agent 3's "+$24 upgrade" figure depends on this number. | [subscriptiongauge](https://subscriptiongauge.com/service/new-york-times), [subbuddy](https://subbuddy.io/en/services/new-york-times), [Senior Daily](https://www.seniordaily.com/nytimes-subscription-deals/) |
| Games Family 2026 price | A1 | Unverified. I found no reliable report of any change. Some aggregator sites mix it up with All Access Family. | search, no reliable source |
| A family plan counts as 2 subscribers | A1 | **Verified** in Nieman. Digiday does *not* say this, even though Agent 1 cited it there too. | [Nieman](https://www.niemanlab.org/2025/09/the-new-york-times-launches-a-family-subscription-with-separate-wordles-for-everyone/) |
| Members need not share a household; shared leaderboards | A1 | Verified | Nieman, Digiday |
| "Much less likely to cancel" | A1, A3 | The quote is real, but it is **a belief, not data**: "*We think* that a subscriber who has three other people…". Nieman separately quotes "early testing suggests… higher retention". Neither is causal evidence that *added* seats cut churn. U1 and P4 depend on that causal link. | Digiday, Nieman |
| Cannibalization "relatively small" | A1 | Quote verified. It is the company's own claim, with no method disclosed. | Digiday |
| "New members are invited by an existing member" | A1 | **Wrong or imprecise.** "Only the primary Subscriber can manage the Family Subscription", including invites by email or link. Members cannot invite. | [NYT Help Center](https://thenewyorktimeshelpcenter.helpjuice.com/115002788207-Subscriptions/family-subscription) |
| Existing subscribers can upgrade | A1 | Verified: direct-billed subscribers upgrade in Account settings. **Missed by all three stages:** people billed through a third party (App Store or Google) must "cancel your subscription via the third-party before purchasing". This creates friction and a measurement hole in the cannibalization accounting. | Help Center |
| Plan structures that were missed | — | The help center says Home Delivery and some All Access subscriptions manage extra people under **"Bonus subscriptions"**. That is a second, pre-existing seat cluster that no stage mapped. | Help Center |
| Number of family plans | — | **Not disclosed.** Q3 2026: about 13.76M total subscribers, digital-only ARPU $9.93, and the CEO says there is "a big TAM to penetrate family plan". No plan count is given. | [SEC 8-K Q3 2026](https://www.sec.gov/Archives/edgar/data/0000071691/000007169126000039/pressrelease9302026.htm), [Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/11/04/ny-times-nyt-q3-2026-earnings-call-transcript/) |
| LinkedIn 0.81 vs 0.24; 10k reLDG clusters | A2 | Verified. The metric is not named in the post. | [LinkedIn eng](https://www.linkedin.com/blog/engineering/ab-testing-experimentation/detecting-interference-an-a-b-test-of-a-b-tests) |
| Holtz et al.: at least 20% interference bias | A2 | Verified, and it is a lower bound | [RePEc](https://econpapers.repec.org/RePEc:inm:ormnsc:v:71:y:2025:i:1:p:390-406) |
| BAFF, arXiv 2609.08725 | A2 | Verified to exist: Oh, Choi, Youn & Kim, about filters for training-data interference in real-time-bidding A/B tests. Agent 2's description is accurate. | [arXiv](https://arxiv.org/abs/2609.08725) |
| Netflix stopped reporting subscribers "partly because of extra members" | A2 | Not spot-checked. The causal "partly because" is an inference. | — |
| Intro-price anomaly ($8 < $10) | A1 | The arithmetic is right *if* owners qualify for the intro price. Eligibility is **unverified** and the help center says nothing about it. | — |

**Internal errors in Agent 3's cards**
- P6 labels two arms "(B)".
- P3 is tagged C4 (household substitution), but it has nothing to do with households. It is C1 only.
- P2's comparison arm ("trial for the most active seat") is not an individual-randomized counterpart. It is a different, endogenously chosen treatment: picking the most active seat is selection on outcomes.
- P1's arm C (all seats) differs from arm A (owner only) in **dose** (number of messages) as well as **saturation** (how many seats are treated). Without a dose-matched arm, "complementarity" cannot be separated from "more messages".

---

## 2. Card critiques

**P1. Coordinated plan-wide upgrade push**
- **Interference is real.** The payer and the beneficiaries are different people, and the upgrade is a plan event.
- **Identification is clean:** randomize by plan_id, under partial interference.
- **Design fixes needed:**
  - Add a dose-matched arm, where the owner gets as many touches as arm C sends in total.
  - Treat upgrade and cancellation as plan-level outcomes, so there is no member-level ICC problem.
- **Power** depends on the Games Family base, which is unknown. *Illustrative only:* detecting a 1% → 1.5% upgrade rate needs about 6.4k plans per arm (≈16·p(1−p)/δ²). Four arms means about 26k plans.
- **Consent:** marketing email or push to *members* needs each member's own opt-in. The owner's consent does not cover members.
- **Value:** +$20–24 per 4 weeks per conversion at list price, but **negative in year 1** if the $8 intro applies to owners.

**P2. Whole-plan All Access trial**
- **Interference is real** (C1, C3).
- **Weaknesses:**
  - The comparison arm is flawed (see above).
  - Expensive: it needs entitlement engineering, and Athletic or rights constraints are unverified.
  - The deprivation risk when the trial ends needs a long readout, at least 8–12 weeks after the trial.
- **Value is plausible**, but it is a heavier build than P1 for the same question. Park it until P1 shows whether coordination matters.

**P3. "Ask the plan owner" at the member paywall**
- **Stronger than Agent 3 realized:** members *cannot* manage the plan (help center), so a request channel is the only route from member demand to purchase.
- **Weaknesses:**
  - Paywall hits by Games Family members on News, Cooking or Athletic per plan are probably low (inference). The volume is unknown.
  - A request button triggers a message to the owner. That message is closer to transactional, user-initiated mail, which eases consent, but it reveals the member's interest to the owner.
- **Best used as P1 arm B**, not as a standalone test.

**P4. Plan challenge and idle-seat reactivation**
- **Interference is real** (leaderboards are verified).
- **Clean plan randomization.** Saturation arms (idle seat only vs all seats) identify spillover.
- **Weaknesses:**
  - Churn baseline is low and readouts are long. *Illustrative:* moving a 2% 4-week churn rate down by 10% relative needs about 78k plans per arm.
  - That number may exceed the plan base, so use engagement as a pre-registered leading metric.
- **Covers both plan types**, which widens the base.
- **Brand risk:** low to medium (push fatigue).

**P5. Second person in a household → family offer**
- **Drop.**
- **Privacy:** inferring co-residence from IP or device and then telling a subscriber that someone in their home hits the paywall reveals another person's reading behaviour. That is a serious privacy and brand problem for a news publisher (legal analysis unverified).
- **Bad clusters:** IP clustering is noisy (carrier-grade NAT, offices).
- **Revenue sign likely negative:** it converts a potential $30 individual sale into +$4.

**P6. Steer invites toward non-subscribers, with owner-cell accounting**
- **The accounting is the real contribution:** credit invitee outcomes to the owner's cell (bipartite / ego-network ITT).
- **The "hold/compare screen" for paying subscribers has problems:**
  - Dark-pattern risk.
  - Third-party-billed subscribers can't be stopped from cancelling elsewhere.
  - Email matching misses App Store payers.
- **Merge into U1.**

**P7. Interference detector (member-randomized vs plan-randomized halves)**
- **High learning value at low cost**, but the Hausman-style test is underpowered when clusters are this small.
- **Moot if NYT already hashes by plan** (unverified).
- **Do not run it standalone.** Embed a member-randomized arm inside A and B.

**P8. Geo-randomized family intro offer**
- **Drop.**
- **Wrong cluster:** family plans explicitly span households and states ("a grandparent in another state"), so spillover crosses DMA boundaries.
- **Not enough clusters:** about 210 DMAs, with the audience concentrated in a few.
- **Leakage has no geography:** deal forums ignore DMAs.

**U1. Fill the empty seats on All Access Family plans (user idea)**
- **Restated as a card:** target All Access Family plans with 2–3 people on them, so 1–2 empty seats, with nudges that get the seats filled. The cluster is the plan plus whoever redeems its invites.
- **Interference is real but bipartite:**
  - The owner is treated.
  - Outcomes land on invitees: activation, and cancelling an existing individual sub (cannibalization).
  - Outcomes also land on the plan: cancellation hazard through C3 coupling.
- **What does not make sense as stated:**
  1. **Seats 3–4 add $0 revenue and $0 reported subscribers.** The price is flat and the plan counts as 2. The whole payoff is (a) lower plan churn on a $34 × 13 ≈ $442/yr stream (price unverified) and (b) engagement or habit for new people. It can be **negative** if invitees were paying individuals or would have become paying subscribers.
  2. **"Get members to fill seats" is not a feature that exists.** Only the primary can invite. Member-side treatments need a new "suggest someone to the owner" feature, which is the P3 pattern.
  3. **Selection bias in Cotton's retention belief:** plans that fill organically are different from plans that fill because of a nudge. The causal effect of a *nudged* fill on churn is exactly what's unknown. This is the experiment's main learning value.
- **Power:** the primary outcome is plan churn, so P4's numbers apply. Seats filled is a well-powered intermediate metric.
- **Feasibility:** good. The owner channel exists and invite logs presumably exist (lineage unverified).

---

## 3. Scores

Weights: materiality 0.25, methodological soundness 0.25, feasibility 0.2, business value 0.2, learning value 0.1.

| Card | Materiality | Method | Feasibility | Value | Learning | **Weighted** |
|---|---|---|---|---|---|---|
| P1 | 5 | 4 | 4 | 4 | 4 | **4.25** |
| P4 | 4 | 4 | 4 | 3 | 4 | **3.80** |
| U1 | 4 | 3 | 4 | 3 | 4 | **3.55** |
| P6 | 4 | 3 | 3 | 3 | 4 | **3.35** |
| P3 | 4 | 3 | 3 | 3 | 3 | **3.25** |
| P7 | 3 | 3 | 4 | 2 | 5 | **3.20** |
| P2 | 4 | 3 | 2 | 3 | 3 | **3.05** |
| P8 | 3 | 1 | 3 | 3 | 2 | **2.40** |
| P5 | 3 | 2 | 1 | 3 | 3 | **2.35** |

## 4. Ranking

1. **P1:** the highest-value, cleanest test of the cluster thesis. **Merge P3 in** as the member-side arm and **P7 in** as an audit arm.
2. **P4:** retention coupling is real, and it can use both plan types for power.
3. **U1:** a real question, but the payoff is retention only and could be negative on revenue. **Merge with P6**, which supplies the owner-cell accounting and the non-subscriber framing.
4. **P6:** merged into U1.
5. **P3:** merged into P1.
6. **P7:** merged as an embedded arm.
7. **P2:** parked until P1 shows that coordination matters.
8. **P8:** dropped (wrong cluster, too few clusters).
9. **P5:** dropped (privacy and brand risk, negative revenue sign).

---

## 5. Briefs for Agent 5

### Prototype A: Plan-coordinated Games Family → All Access Family upgrade (P1 + P3, with a P7 audit arm)
- **Scope:** direct-billed Games Family plans with 2 or more seats. Exclude third-party-billed plans or analyse them as a separate stratum.
- **Unit:** plan_id, frozen when the plan enters the experiment. Stratify by seats (2/3/4), tenure and owner engagement.
- **Arms:**
  - 0: control.
  - A: owner-only upsell.
  - A′: owner-only, **dose-matched** to arm C.
  - B: member paywall "Request All Access for our plan" button, which sends a request count to the owner.
  - C: all seats in the same 7-day window, plus B.
  - Audit (P7): a *member*-randomized arm drawn from a separate random half of plans.
- **Outcomes:**
  - Primary: plan upgrade within 8 weeks.
  - Then: net plan revenue over 12 months, **modelled under both intro-eligibility scenarios**.
  - Plan cancellation hazard, as a guardrail.
  - Engagement on unlocked products per seat.
- **Fixes required:**
  - Plan-level analysis (no member-level ICC).
  - Report the direct, spillover and total effects (Hudgens & Halloran).
  - Run a power calculation against the *actual* plan count.
  - Collapse to 3 arms if the base is too small (for example 0 / A′ / C).
- **Constraints:**
  - Each member's marketing opt-in governs messages sent to that member.
  - Request messages contain no member reading or content details.
  - Only the owner can buy.
- **Unverified:** the $34 price, the 2026 Games Family price, intro eligibility, member paywall-hit volume, whether members see who the owner is, and NYT's current randomization unit.

### Prototype B: Plan challenge and idle-seat reactivation (P4)
- **Scope:** Games Family and All Access Family plans with at least 2 active seats.
- **Unit:** plan_id. Stratify by plan type, seats and tenure.
- **Arms:**
  - 0: control.
  - I: idle-seat-only nudge.
  - S: synchronized weekly challenge to all seats.
  - S + I.
  - Plus an embedded member-randomized audit arm.
- **Outcomes:**
  - Primary: plan cancellation hazard (survival analysis, 12+ weeks).
  - Leading metric: active seats per plan per week.
  - Guardrails: push opt-out rate and unsubscribes.
- **Fixes required:**
  - Pre-register engagement as a surrogate metric, with a plan to validate it against churn.
  - Use a CUPED-style adjustment on pre-period plan activity.
  - Treat leaderboard rivals outside the plan (if such links exist) as possible cross-cluster edges.
- **Constraints:** OS push permission per member; per-member frequency caps; no exposure of activity beyond what the existing leaderboard already shows.
- **Unverified:** the plan count, baseline plan churn, whether leaderboard mechanics work across plans, and the push opt-in rate among members.

### Prototype C: Fill the empty seats on All Access Family plans (U1 + P6), selected as a user idea
- **Scope:** All Access Family plans with 2–3 people, held for at least 4 weeks, owner direct-billed. The owner gets all messaging, because only the owner can invite.
- **Unit:** the owner's plan plus every invitee who redeems an invite from that plan. Invitees inherit the owner's arm (bipartite / ego-network ITT).
- **Arms:**
  - 0: control.
  - G: generic "you have N open seats" owner nudge.
  - N: the same nudge with "for someone without NYT" framing and a share link.
  - M (optional, needs a build): members get a "suggest someone to the owner" request, which reuses the Prototype A request infrastructure.
- **Outcomes:**
  - Primary: plan cancellation hazard.
  - Intermediate: seats filled at 4 and 8 weeks.
  - **Net revenue**: plan revenue minus invitees' lost individual-subscription revenue.
    - Classify each invitee before the invite as paying direct, paying third-party, registered free, lapsed or unknown.
    - Third-party payers are an explicit blind spot to bound.
  - Invitee engagement.
- **Fixes required:**
  - Drop P6's hold/compare screen (dark-pattern risk).
  - Do not report "subscribers".
  - Pre-specify that a "win" requires lower plan churn *and* net revenue ≥ 0.
- **Constraints:**
  - Invite emails go out from the owner's action. NYT must not email invitees' addresses for marketing without consent.
  - No household inference.
- **Unverified:** the $34 price, whether invite-redemption lineage is logged, the share of invitees who are already paying, and whether *nudged* fills cut churn as much as organic ones (Cotton's claim is a belief).

---

## 6. Open questions for a human

1. How many Games Family and All Access Family plans are there, by seat count? This decides the number of arms and whether any churn-primary design is feasible.
2. Do existing Games Family owners (and individual subscribers who upgrade) get the $8 first-year family intro price? Is the current regular price $34 or $30?
3. What is NYT's randomization unit today: cookie, user or plan? If it is already plan-hashed, P7 is moot.
4. Can members see who the owner is? Can NYT build a member → owner request flow under the current terms of service and privacy policy?
5. What consent do members have for marketing email and push, given that it is separate from the owner's consent?
6. Is invite → redemption lineage logged, and can invitees' prior subscriptions, including App Store and Google ones, be linked?
7. How do "Bonus subscriptions" (Home Delivery and some All Access plans) fit in? Are they a third seat cluster to include or exclude?
8. Company priority: is a filled seat that adds no revenue but may cut churn worth more than holding individual price points? That trade-off decides U1.
9. What are the guardrail thresholds for push and email fatigue, and how will the sender-reputation spillover across arms (C6) be handled?

**Sources:** [Digiday](https://digiday.com/media/how-the-new-york-times-is-betting-on-a-new-family-plan-to-grow-its-digital-subscriber-base-and-revenue/) · [Nieman Lab](https://www.niemanlab.org/2025/09/the-new-york-times-launches-a-family-subscription-with-separate-wordles-for-everyone/) · [NYT Help Center: Family Subscription](https://thenewyorktimeshelpcenter.helpjuice.com/115002788207-Subscriptions/family-subscription) · [subscriptiongauge](https://subscriptiongauge.com/service/new-york-times) · [subbuddy](https://subbuddy.io/en/services/new-york-times) · [Senior Daily](https://www.seniordaily.com/nytimes-subscription-deals/) · [Bloomberg](https://www.bloomberg.com/news/articles/2025-09-08/ny-times-unveils-online-family-plans-with-little-added-expense) · [Axios](https://www.axios.com/2025/09/08/nyt-family-subscription-plans) · [LinkedIn A/B test of A/B tests](https://www.linkedin.com/blog/engineering/ab-testing-experimentation/detecting-interference-an-a-b-test-of-a-b-tests) · [Holtz et al. (RePEc)](https://econpapers.repec.org/RePEc:inm:ormnsc:v:71:y:2025:i:1:p:390-406) · [Holtz et al. pdf](https://business.columbia.edu/sites/default/files-efs/citation_file_upload/holtz-et-al-2024-reducing-interference-bias-in-online-marketplace-experiments-using-cluster-randomization-evidence-from%20%282%29.pdf) · [BAFF arXiv](https://arxiv.org/abs/2609.08725) · [NYT Q3 2026 8-K](https://www.sec.gov/Archives/edgar/data/0000071691/000007169126000039/pressrelease9302026.htm) · [Q3 2026 call transcript (Fool)](https://www.fool.com/earnings/call-transcripts/2026/11/04/ny-times-nyt-q3-2026-earnings-call-transcript/)