# Agent 3: Prototype idea cards

**Notes for Agent 4 and Agent 5**
- **Cluster definition.** "Plan" means family plan_id: owner plus up to 3 invitees, not necessarily one household (verified, Agent 1). "Household" means an *inferred* IP or device cluster.
- **Prices are unconfirmed.** Upgrade economics use the unconfirmed Oct 2026 snapshot: Games Family $10, All Access Family $34 per 4 weeks, so **+$24 per plan**. Launch prices were $10 → $30 (+$20).
- **Intro-price eligibility is unknown.** Whether existing owners get the $8 intro price is **unverified**. This sign-flips the near-term revenue of P1–P3.
- **Metrics for every card.** Report plan-level revenue, **seats with access**, and the plan cancellation hazard. Do not report "subscribers": a plan counts as 2 regardless of seats, which is a metric artifact.
- **Ordering.** Cards follow the stated focus on whole-plan and household treatment. Two measurement cards (P7, P8) protect the estimates.

---

### P1. Coordinated plan-wide upgrade push, saturation-randomized
- **Pitch:** Nudge every seat on a Games Family plan toward All Access Family in the same week, and test that against nudging the owner alone.
- **Type:** cluster-level treatment, with a measurement design built in.
- **Channel(s):** C1.
- **Treatment:** Games Family plans are randomized to one of four arms:
  - (0) no nudge;
  - (A) owner-only email and in-app upsell;
  - (B) members-only in-app "your plan could unlock Cooking/News/Athletic";
  - (C) all seats in the same 7-day window.
- **Cluster / unit of randomization:** plan_id, hashed and frozen at entry. Membership comes from billing and invite tables.
- **Why cluster beats individual:**
  - Direct effect (owner offer → owner upgrades): positive.
  - Spillover (member nudge → member asks owner → upgrade): positive.
  - Total effect in arm C > arm A if seats are complements. This is an inference that the design tests directly.
  - Member-level randomization **understates** the effect, because control members are upgraded too.
- **Outcomes moved:** revenue (+$24 per 4 weeks per conversion), engagement on unlocked products, retention.
- **Main risk:** the Games Family base may be too small for 4 arms. If the $8 intro applies to existing owners, year-1 revenue is roughly flat.
- **Grounding:**
  - Two-stage design: Hudgens & Halloran 2008.
  - Randomized saturation: Baird et al. 2018.
  - Component-level randomization: UGDS 2018.
  - No direct industry precedent (Agent 2 gap #1).

### P2. Whole-plan All Access trial
- **Pitch:** Unlock All Access for all seats of a Games Family plan for 14–28 days, then offer the owner the upgrade.
- **Type:** cluster-level treatment.
- **Channel(s):** C1, C3.
- **Treatment:** All seats on treated plans get bundle access, with an end-of-trial upgrade offer to the owner. The comparison arm gives the trial only to the *most active seat*, which is the individual-level counterpart.
- **Cluster / unit of randomization:** plan_id.
- **Why cluster beats individual:**
  - The owner pays based on what the *plan* uses. A single-seat trial builds habit in one member, who may not be the payer.
  - Direct effect: positive.
  - Spillover: positive. Co-members' use becomes visible demand, and shared leaderboards already link the seats.
  - Total effect: positive and larger than the one-seat trial (inference).
- **Outcomes moved:** engagement during the trial, revenue (conversion), retention.
- **Main risk:**
  - Losing access when the trial ends may *raise* cancellation of the base Games Family plan. This is a deprivation effect, so the primary metric must be the plan cancellation hazard.
  - Licensing or cost limits on Athletic trials are unverified.
- **Grounding:**
  - Hudgens & Halloran (plan as the group).
  - No published plan-trial precedent was found.

### P3. "Ask the plan owner" at the member paywall
- **Pitch:** When a Games Family member hits a News, Cooking or Athletic paywall, give them a one-tap request that sends the owner a pre-filled upgrade offer.
- **Type:** cluster-level treatment (bipartite: treatment on members, outcome on the owner).
- **Channel(s):** C1, C4.
- **Treatment:**
  - The paywall shown to members of treated plans adds a "Request All Access for our plan" button.
  - The owner receives an email or push carrying the *count* of requests.
  - Content details are excluded, to protect privacy.
- **Cluster / unit of randomization:** plan_id. Any per-member randomization would contaminate the owner.
- **Why cluster beats individual:**
  - The person who wants the product (member) and the person who pays (owner) are different people.
  - An individual paywall test credits nothing to the member and misses the owner's conversion.
  - Direct effect on the member: small.
  - Spillover onto the owner: large and positive.
- **Outcomes moved:** revenue, engagement.
- **Main risk:**
  - Whether members can see who owns the plan is unverified (Agent 1 open question #3).
  - Owners may perceive requests as nagging. Low paywall-hit volume per plan.
- **Grounding:**
  - Bipartite interference: Zigler & Papadogeorgou 2021.
  - Exposure mappings: Aronow & Samii 2017.

### P4. Plan challenge and idle-seat reactivation (retention)
- **Pitch:** Send all seats a synchronized weekly "plan challenge" push, and target seats that have gone idle, to cut whole-plan cancellation.
- **Type:** cluster-level treatment.
- **Channel(s):** C3.
- **Treatment:**
  - Treated plans get a shared weekly Games challenge on the existing plan leaderboard (verified feature), pushed to every seat at the same time.
  - Seats with no activity for 14 or more days get a "your plan is playing" nudge.
  - Saturation arms: idle seat only vs. all seats.
- **Cluster / unit of randomization:** plan_id. Stratify by seats filled (2/3/4) and plan tenure.
- **Why cluster beats individual:**
  - Rivalry makes play complementary across seats.
  - Direct effect: positive. Spillover onto co-members: positive. Total effect > sum of individual nudges (inference).
  - Churn is a plan event, so per-member retention is mis-specified.
  - Naive testing **understates** the effect.
- **Outcomes moved:** engagement, retention (also covers All Access Family plans).
- **Main risk:**
  - The family-plan retention base is already high (Cotton quote), so the measurable lift may be small.
  - Push fatigue and opt-outs.
- **Grounding:**
  - Baird et al. (complementarity across seats).
  - Duolingo Friend Streaks: correlational only, +22% lesson completion.

### P5. Second-person-in-household paywall → family offer
- **Pitch:** When a second registered user in an inferred household with an existing individual subscriber hits the paywall, offer the subscriber a family upgrade instead of selling the second person a full subscription.
- **Type:** cluster-level treatment.
- **Channel(s):** C4, C2.
- **Treatment:**
  - The subscriber gets an "add [household] for +$4" email or in-app message.
  - The second person sees a "join a family plan" paywall variant.
- **Cluster / unit of randomization:** inferred household. Built from shared residential IP, device IDs and billing address, using Louvain-style clusters.
- **Why cluster beats individual:**
  - One subscription meets the household's need, so a device-level paywall test **overstates** per-person conversion.
  - Converting the substitute reader into a seat captures revenue that otherwise leaks to account sharing.
  - Direct effect: positive. Spillover under device-level randomization: negative.
- **Outcomes moved:** revenue, retention (the plan effect), engagement of the second person.
- **Main risk:**
  - The second person might have bought $30 individual All Access; the offer collapses that sale to +$4. This makes net revenue the sign-deciding metric.
  - Noisy IP households (CGNAT, offices).
  - Privacy risk in implying a co-resident subscribes.
- **Grounding:**
  - Graph cluster randomization: Ugander et al. 2013.
  - Clustering at Meta: Karrer et al.
  - Commercial precedent: Netflix paid sharing.

### P6. Steer seat-fill invites toward non-subscribers, with owner-cell accounting
- **Pitch:** Nudge owners of plans with empty seats to invite people who *don't* already pay, and credit every invitee's outcome to the owner's arm.
- **Type:** cluster-level treatment plus measurement design.
- **Channel(s):** C2, C7.
- **Treatment:** Arms for owners of All Access Family and Games Family plans with open seats:
  - (0) none;
  - (A) generic "add your family" nudge;
  - (B) nudge plus a share link carrying "for someone without NYT" framing;
  - (B) also includes a check when the invitee redeems: if the email matches a paying individual subscriber, they see a hold/compare screen.
- **Cluster / unit of randomization:** the owner's ego network (owner plus everyone who redeems their invites), with lineage taken from invite logs.
- **Why cluster beats individual:**
  - Owner-only revenue **overstates** the net effect (Agent 1 C2; example: an invitee cancels $30 while the plan gains only about $4).
  - Arm B raises seats with access while protecting individual-subscription revenue.
- **Outcomes moved:** revenue (net), retention, engagement of invitees.
- **Main risk:**
  - Few owners invite at all.
  - Email matching misses invitees who pay through Apple or Google.
  - Cotton says cannibalization is "relatively small"; this is the company's claim and is unverified.
- **Grounding:**
  - Ego clusters: Saint-Jacques et al. 2019.
  - Bipartite ITT: Zigler & Papadogeorgou 2021.
  - Profile transfer as a product answer: Netflix.

### P7. Interference detector: plan-randomized vs. member-randomized arms side by side
- **Pitch:** Run the next existing Games or upsell notification test in two halves, one randomized by member and one by plan, and test whether the estimates differ.
- **Type:** measurement design.
- **Channel(s):** C1, C3 (and C4 if household IDs exist).
- **Treatment:** No new product; reuse a queued test.
- **Cluster / unit of randomization:**
  - Stratify plans by size and product, then split them 50/50 into a member-randomized arm and a plan-randomized arm.
  - Compare the two arms' estimates with a Hausman-style test.
- **Why it matters:**
  - Expected sign: the plan-arm estimate > the member-arm estimate for upgrade and retention, because spillover to control is positive (inference).
  - If the gap is null, NYT can keep individual tests for these levers.
  - It gives a cheap go/no-go on P1–P4 before building them.
- **Outcomes moved:** indirect; it corrects estimates for all three outcomes.
- **Main risk:**
  - The cluster arm has high variance, so a modest bias may go undetected.
  - NYT's current randomization unit is unverified. If tests are already plan-hashed, this card is moot.
- **Grounding:**
  - Saveski et al. 2017.
  - LinkedIn "A/B test of A/B tests": 0.81 vs 0.24.
  - Holtz et al. 2025: ≥20% interference bias in a pricing test.

### P8. Geo-randomized family intro offer, to measure net cannibalization
- **Pitch:** Randomize the prominence of the family intro offer ($8 → $34) on the paywall by DMA, to measure the true net effect on individual All Access intro sales.
- **Type:** measurement design.
- **Channel(s):** C8, C2, C4.
- **Treatment:** In treated DMAs the personalized paywall leads with the family intro; control DMAs lead with the individual intro ($4 → $30, per the unconfirmed snapshot).
- **Cluster / unit of randomization:** DMA. Stratify by baseline subscription penetration, and exclude NYC from treatment or use it as its own stratum.
- **Why cluster beats individual:**
  - A user-level test **overstates** the lift. Control households are depressed by treated co-residents (C4).
  - Reference prices also spread locally within households and friend groups (C8).
  - A DMA-level test captures the rollout equilibrium: revenue per household and seats with access.
- **Outcomes moved:** revenue (net), retention (the plan effect), engagement.
- **Main risk:**
  - Only about 210 DMAs, and the national audience is concentrated in a few metros, so variance is very high.
  - Deal-forum leakage has no geography (Agent 2 gap #5).
- **Grounding:**
  - Cluster-randomized pricing test: Holtz et al. 2025.
  - Spatial cluster sizes: Leung (arXiv 2111.04219).
  - Geo-staged rollout: Netflix paid sharing.

---

**Quick index for Agent 4**

| Card | Type | Cluster | Build effort (inference) | Biggest unknown |
|---|---|---|---|---|
| P1 | Treatment + design | Plan | Low (messaging + plan hash) | Size of the Games Family base; intro-price eligibility |
| P2 | Treatment | Plan | Medium (entitlements) | Retention hit when the trial ends |
| P3 | Treatment | Plan (bipartite) | Medium (paywall UI + owner notification) | Members' visibility of the owner |
| P4 | Treatment | Plan | Low–medium | Retention ceiling |
| P5 | Treatment | Inferred household | High (household graph) | Net revenue sign |
| P6 | Treatment + design | Owner ego network | Medium (invite lineage) | Invite volume |
| P7 | Design | Plan vs member | Low | Current randomization unit |
| P8 | Design | DMA | Low build, high variance | Statistical power |