# Agent 2: Industry precedent and causal-inference literature for NYT interference channels

**Budget used:** 15 of 15 searches and 15 of 15 fetches.

**Main findings**
- **Plans are the clean case.** Family plans are small, disjoint groups, so interference stays inside a plan ("partial interference"). That makes two-stage and randomized-saturation designs the textbook fit (Hudgens & Halloran 2008; Baird et al. 2018; Basse & Feller). These designs lose little power at 2–4 seats per plan *(inference)*.
- **No company has published plan-level upgrade experiments.** I found no public write-up from Netflix, Spotify, Duolingo or NYT. C1 and C2 are therefore a precedent gap, and the designs below are borrowed from network and marketplace experimentation.
- **Interference can be detected cheaply.** Split the population into an individual-randomized arm and a cluster-randomized arm, then compare the two estimates (Saveski et al. 2017). LinkedIn ran this in production; one experiment showed 0.81 for the cluster arm vs 0.24 for the individual arm.
- **One open question from Agent 1 is still open.** Whether Games Family owners qualify for the $8 intro price on All Access Family remains **unverified**; the budget ran out before I could check.

---

## 1. Channel-by-channel findings

### C1. Plan-level upgrade coupling (Games Family → All Access Family). High materiality.

**Industry precedent**
- **None found** for plan-level upgrade nudges. Nobody has published on randomizing family plans as clusters for upsell. This is a gap.
- **Closest analogue: connected components as the randomization unit.**
  - Google's unofficial data-science blog argues for randomizing whole components of a collaboration network, such as everyone sharing a document. Its reasoning is that user-level randomization is biased "to the extent spillover effects exist" ([UGDS 2018](https://www.unofficialgoogledatascience.com/2018/01/designing-ab-tests-in-collaboration.html)).
  - NYT plans have the same structure: small, disjoint, observed groups.
- **Account-level bucketing is standard vendor practice.** Hightouch documents hashing on account_id so that every user on an account lands in the same variant, with a salt per experiment ([Hightouch](https://hightouch.com/playbooks/multivariate-tests-on-user-groups)). This is a vendor how-to, not a case study.

**Literature**

| Work | Contribution | Fit to C1 |
|---|---|---|
| Hudgens & Halloran 2008, *JASA* 103(482) ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548)) | Two-stage group randomization under partial interference. Defines direct, indirect, total and overall effects. | Plans are the groups. Without a cluster arm you cannot tell the indirect effect (the upgrade spilling to control members) from the direct effect of the nudge. |
| Baird, Bohren, McIntosh & Özler 2018, *REStat* 100(5) ([IDEAS](https://ideas.repec.org/a/tpr/restat/v100y2018i5p844-860.html), [WP pdf](https://economics.sas.upenn.edu/sites/default/files/filevault/SSRN%2016_025%20version%202.pdf)) | Randomized saturation: first randomize the share of a group that is treated, then randomize individuals within the group. Gives power formulas and shows the power cost of identifying spillovers. | Randomly assign how many seats get nudged (owner only, 1 member, all seats). Directly tests Agent 1's "coordinated nudge" claim that seats are complements. |
| Basse & Feller, *JASA* (accepted per arXiv) ([arXiv 1608.06805](https://arxiv.org/abs/1608.06805)) | Randomization-based analysis of two-stage experiments with households of varying size. | Plans have 2–4 seats. Shows how to weight by plan versus by person, which matters given the reporting rule "plan = 2 subscribers". |
| Aronow & Samii 2017, *AoAS* 11(4) ([Project Euclid](https://projecteuclid.org/journals/annals-of-applied-statistics/volume-11/issue-4/Estimating-average-causal-effects-under-general-interference-with-application-to/10.1214/16-AOAS1005.full)) | Exposure mappings plus inverse-probability (Horvitz-Thompson) estimators under general interference. | Define each person's exposure as (own nudge, owner nudged?, number of co-members nudged). Owner vs member is a natural exposure dimension. |
| Saveski et al. 2017, *KDD* ([paper](https://faculty.washington.edu/msaveski/assets/publications/2017_detecting_network_effects/paper.pdf)); Pouget-Abadie et al. 2019, *Biometrika* ([pdf](https://faculty.washington.edu/msaveski/assets/publications/2019_biometrika/paper.pdf)) | Run an individual-randomized arm and a cluster-randomized arm side by side and test whether their estimates differ. | Cheapest way to test whether a member-level nudge leaks across the plan. |

**Design implication (inference)**
- Make the plan the randomization unit, with upgrade as a plan-level outcome.
- Inside treated plans, randomize saturation (owner only / members only / all seats).
- Use plan-level arms to tell "pooled demand" and "coordinated timing" apart.
- With m ≤ 4 seats and plan-level outcomes, the design effect 1 + (m−1)ρ is at most about 4× for per-person engagement metrics, and roughly 1× for upgrade and cancellation, which are already plan events.

### C2. Seat-filling invites and cannibalization. High materiality.

**Industry precedent: Netflix "extra member" and paid sharing**
- **Design** ([Netflix newsroom, 8 Feb 2023](https://about.netflix.com/en/news/an-update-on-sharing)):
  - A primary household location.
  - Paid extra-member sub-accounts for people living elsewhere (CAD$7.99 / NZ$7.99 / €3.99 / €5.99).
  - Profile transfer to a new paid account, keeping history.
  - Tested in Latin America over the prior year, then launched in Canada, NZ, Portugal and Spain first.
  - The newsroom post gives **no test metrics**.
- **Rollout pattern:** country-by-country staging is effectively a **geo-cluster rollout**, which matches the cluster used for C4 and C8 *(inference: Netflix has not described it as an experiment design)*.
- **Reported outcomes (secondary sources, not the shareholder letters):**
  - Q4 2023 net additions of about 13.1M; Q1 2024 paid net additions of 9.3M vs 1.8M a year earlier ([TheWrap](https://www.thewrap.com/netflix-earnings-q4-2023/), [MarketBeat transcript](https://www.marketbeat.com/earnings/transcripts/103770)).
  - Netflix stopped reporting subscriber counts from 2025, partly because extra members don't map to a member count. This parallels NYT's "plan = 2 subscribers" artifact.
- **Mirror image of NYT:** Netflix turns free sharers into paid seats, while NYT's risk is paid individuals collapsing into cheap family seats. Netflix's profile-transfer feature is the product answer for keeping per-person history when people move between accounts.

**Literature**
- **Bipartite interference** (Zigler & Papadogeorgou 2021, *Statistical Science* 36(1), [Project Euclid](https://projecteuclid.org/euclid.ss/1608541221)): treatment is assigned to one set of units and outcomes are measured on another. Here the owner gets the invite nudge and the outcome is the invitee's cancellation or conversion. Assign invitees to the **owner's** cell (intent-to-treat on the owner's ego network).
- **Ego-cluster randomization** (Saint-Jacques, Varshney, Simpson & Xu 2019, LinkedIn, [arXiv 1903.08755](https://arxiv.org/abs/1903.08755)): treat a focal user ("ego") and measure the effect on their 1-hop neighbors ("alters"). Here the owner is the ego and invitees are alters. LinkedIn's v2 tool lowered between-cluster leakage from 30% to 20% (Su & Duan 2023, [arXiv 2308.05945](https://arxiv.org/abs/2308.05945)).
- **Netting out cannibalization (inference):** stratify invitees by their status before the invite (paying individual / registered free / churned / unknown). Report net revenue = plan Δ + Σ invitees' individual-subscription Δ.

### C3. Engagement and retention coupling within a plan (leaderboards, streaks). High for retention.

**Industry precedent: Duolingo**
- **Friend Streaks** ([Duolingo blog](https://blog.duolingo.com/product-lessons-friend-streak/)):
  - Learners with at least one Friend Streak are 22% more likely to finish their daily lesson. This is **correlational**, not an experiment.
  - Version 1 was local-only, so the other person did not know a streak existed. That made the design non-social and spillover-free, which is a cautionary example.
  - Duolingo held off on multiple shared streaks because few users have large friend groups.
- **Streak Wager A/B test** ([making.duolingo.com](https://making.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals)): day-7 retention +14%. This is an individual-level test, not a social one.
- **No published cluster test** of social streaks was found.

**Literature**
- **Randomized saturation** (Baird et al.) tests whether nudges are complements: is the effect on i bigger when j is also nudged?
- **Exposure mappings** (Aronow & Samii): exposure = share of co-members nudged.
- **Hu, Li & Wager**, "average direct and indirect effects": not verified in this session, so **dropped**.
- **Outcome definition:** retention must be the plan's cancellation hazard, not a per-member outcome.

### C4. Household substitution at the paywall. Medium–high materiality.

**Industry precedent**
- Netflix paid sharing (above) is the clearest commercial example of turning household substitution into a sale through a household or location-level product, rolled out by geography.
- No published paywall experiment design from a news publisher was found. This is a gap.

**Literature**
- **Household = cluster.** Two-stage designs (Hudgens & Halloran; Basse & Feller).
- **When the household graph is noisy** (shared IP or device, so households are inferred from network signals): graph cluster randomization (Ugander, Karrer, Backstrom & Kleinberg 2013, [arXiv 1305.6979](https://arxiv.org/abs/1305.6979)) and randomized GCR, which averages over many clusterings to cut variance (Ugander & Yin, [arXiv 2009.02297](https://arxiv.org/abs/2009.02297); later journal version unverified).
- **Cluster quality:** Meta's production framework found imbalanced Louvain clusters gave the best bias-variance trade-off, and it adds a cluster-level regression adjustment and an interference test (Karrer et al., [arXiv 2012.08591](https://arxiv.org/abs/2012.08591); [Meta blog 2021](https://research.facebook.com/blog/2021/8/testing-product-changes-with-network-effects/)). The KDD venue and year are unverified (2020 vs 2021).
- **Imperfect clusters (inference):** an IP- or device-based household is an imperfect cluster. Measure leakage the way LinkedIn reports the "loss rate" for ego clusters.

### C5. Recommender feedback loop. Medium–high for engagement.

**Industry precedent: Douyin (ByteDance)**
- Farias, Li, Peng, Ren, Zhang & Zheng, *RecSys 2023* ([arXiv 2305.02542](https://arxiv.org/abs/2305.02542)).
- Problem: experiments randomized at the creator level are biased because creators compete for the same viewers' attention. The naive bias is "on the order of the treatment effect".
- Solution: a "Differences-in-Qs" estimator whose bias is second-order in the treatment effect; it runs on the production platform.
- Reported result: 99% lower mean squared error than the alternatives (the company's own claim).

**Literature**
- **Training-loop interference.** Si 2023 ([arXiv 2310.17496](https://arxiv.org/abs/2310.17496)) uses weighted training: predict whether each log row came from treatment or control, then reweight the training loss. In the author's simulations it beats data pooling and snapshot methods, while data splitting inflates false positives in A/A tests. Fits the NYT case of one shared model trained on logs from both arms.
- **BAFF** (2026, [arXiv 2609.08725](https://arxiv.org/abs/2609.08725)): a production protocol for measuring bias from training-data interference in real-time-bidding (ad auction) A/B tests. I saw only search snippets of it, so details are unverified.
- **Switchbacks** (Bojinov, Simchi-Levi & Zhao 2023, *Management Science* 69(7), [arXiv 2009.00148](https://arxiv.org/abs/2009.00148)): optimal switchback design given a carryover order, exact randomization p-values, and a way to estimate carryover from data.
  - NYT's daily news and puzzle cycle suggests day-level periods *(inference)*.
  - Model retraining makes carryover long, so the periods must be longer than the retrain cadence.

### C6. Email deliverability and push budgets. Medium materiality.

**Industry precedent: LinkedIn**
- "Email Volume Optimization at LinkedIn", *KDD '16* ([DOI](https://unpaywall.org/10.1145%2F2939672.2939692); blog [part 1](https://engineering.linkedin.com/blog/2016/06/less-is-more--optimizing-email-volume-part-1), [part 2](https://engineering.linkedin.com/blog/2016/07/less-is-more--optimizing-email-volume-part-2-)). The author list is unverified; the blog credits Rupesh Gupta with leading the work.
- Objective: minimize volume and complaints (unsubscribes, spam reports) while maximizing sessions. Later revised to target total site-wide active users.
- Follow-on: multi-objective notification optimization across channels with offline RL ([arXiv 2207.03029](https://arxiv.org/abs/2207.03029); venue unverified).
- **None of these publications addresses sender-reputation interference** between arms. That is a gap.

**Literature and fix (inference)**
- This is a shared resource with a global equilibrium, related to Wager & Xu's *Experimenting in Equilibrium* (Management Science, [arXiv 1903.02124](https://arxiv.org/abs/1903.02124)).
- The practical fix is separate sending domains or IP pools per arm, which makes each arm its own sender-level cluster.
- Switchbacks are a poor fit: reputation decays over weeks, so carryover is long.
- **Within-user push competition between products is NOT interference.** Handle it with multi-outcome budgets.

### C7. Social sharing and gift links. Medium materiality.

**Industry precedent: LinkedIn**
- Ego clusters ([arXiv 1903.08755](https://arxiv.org/abs/1903.08755)).
- "A/B test of A/B tests" ([LinkedIn eng blog 2019](https://www.linkedin.com/blog/engineering/ab-testing-experimentation/detecting-interference-an-a-b-test-of-a-b-tests)):
  - The member graph is split into 10k clusters with reLDG (a balanced graph-partitioning method), stratified, and divided 50/50 into an individual arm and a cluster arm.
  - A Hausman-style test compares the two estimates.
  - In experiment 2 the cluster estimate was 0.81 vs 0.24 for the individual arm. The metric and p-value are not given.

**Literature**
- Graph cluster randomization (Ugander et al. 2013).
- Exposure mappings (Aronow & Samii).
- Viviano, *Experimental Design under Network Interference* ([arXiv 2003.08421](https://arxiv.org/abs/2003.08421)): two-wave designs in which a pilot estimates variance, then the design picks who to treat to minimize variance of direct and spillover effects. This suits NYT because the gift-link graph is only partly observed.

**Graph for NYT (inference):** build it from gift-link sender → recipient logs plus shared game results.

### C8. Promo-price leakage and reference prices. Medium materiality.

**Industry precedent: Airbnb pricing meta-experiment**
- Holtz, Lobel, Lobel, Liskovich & Aral, *Management Science* 71(1):390–406 (online 2024) ([pdf](https://business.columbia.edu/sites/default/files-efs/citation_file_upload/holtz-et-al-2024-reducing-interference-bias-in-online-marketplace-experiments-using-cluster-randomization-evidence-from%20%282%29.pdf); [RePEc](https://econpapers.repec.org/RePEc:inm:ormnsc:v:71:y:2025:i:1:p:390-406)).
- Design: a platform-fee test randomized two ways at once, Bernoulli (individual) and cluster.
- Result: **at least 20%** of the individual-level estimate of the total average treatment effect was interference bias. Cluster randomization removed it, at the cost of higher root-mean-square error. Suggestive evidence that the bias is worse in demand-constrained markets.
- This is the closest published analogue to "personalized price shown to i shifts j's behaviour".

**Literature**
- **Spatial or geographic clusters:** Leung, *Rate-optimal cluster-randomized designs for spatial interference* ([arXiv 2111.04219](https://arxiv.org/abs/2111.04219); journal version unverified). Gives near-optimal cluster sizes when spillover decays with distance; use for DMA-level price tests.
- **Market equilibrium:** Wager & Xu (above).
- **Two-sided bias:** Johari, Li, Liskovich & Weintraub, *Experimental Design in Two-Sided Platforms* ([arXiv 2002.05670](https://arxiv.org/abs/2002.05670); journal version unverified). Bias depends on market balance. Mostly relevant if NYT ever treats promo budget or inventory as a shared constraint.
- **Deal-forum leakage** has no geography and is not captured by geo clusters. That remains a gap.

### C9 and C10
- **C9 (editorial and popularity feedback):** Douyin-style competition and switchbacks apply. No newsroom precedent found.
- **C10 (geography and team markets):** this is heterogeneity, so stratify. No literature needed.

---

## 2. Methods toolbox

| Design / estimator | Use when (NYT channel) | Key assumptions | Cost |
|---|---|---|---|
| **Plan-level cluster randomization** | C1, C3 (plan outcomes) | No cross-plan edges (partial interference) | Small power loss: m ≤ 4, outcomes already at plan level. Low engineering effort: hash on plan_id. Plans change membership, so freeze assignment at entry. |
| **Two-stage / randomized saturation** (Hudgens & Halloran; Baird et al.; Basse & Feller) | C1 owner vs member vs all seats; C3 complementarity | Partial interference; spillover depends on the share treated | Moderate: power to detect the average effect falls as more saturation arms are added (Baird et al.). Needs many plans. |
| **Individual vs cluster arms + Hausman test** (Saveski 2017; LinkedIn) | Detecting interference in C1, C3, C4, C7 before committing to a design | Both arms drawn from the same population (stratify) | The cluster arm has high variance. Medium engineering effort. Cheap way to decide whether to switch designs. |
| **Exposure mapping + Horvitz-Thompson** (Aronow & Samii) | Mixed plans, partly observed graphs (C3, C7) | The exposure mapping is correctly specified | Inverse-probability weighting has high variance. Low engineering effort. |
| **Ego-cluster / bipartite ITT** (Saint-Jacques 2019; Zigler & Papadogeorgou 2021) | C2 invites: owner treated, invitee outcomes | Invite graph is logged; invitees are assigned to the owner's cell | Some leakage (20–30% at LinkedIn). Needs invite-to-owner lineage. |
| **Graph cluster randomization / randomized GCR / Louvain clusters** (Ugander; Ugander & Yin; Karrer) | C4 inferred households, C7 social graph | Clusters reasonably isolated | High power loss. Clustering pipeline is a large engineering effort. |
| **Geo-cluster randomization** (Leung; Holtz) | C8 pricing and reference prices, C4 rollout | Spillover decays across regions; enough regions | Very high variance (few units). Low engineering effort. |
| **Switchback** (Bojinov et al. 2023) | C5 (shared model), C9, short-carryover pricing | Bounded carryover order | Needs many periods; burn-in is wasted. Medium engineering effort. Bad fit for C6 (long carryover). |
| **Weighted training / split data pools** (Si 2023) | C5 training loop | Arm-membership propensities can be estimated | Weighted training: medium machine-learning effort. Splitting data roughly halves training data per arm and inflated A/A false positives in Si's simulations. |
| **Differences-in-Qs** (Farias et al. 2023) | C5 and C9 attention competition | Markovian state and dynamics | Medium modelling effort; high payoff per the authors. |
| **Multiple randomization designs** (Bajari et al., [arXiv 2112.13495](https://arxiv.org/abs/2112.13495); review "Experimental Design in Marketplaces", *Stat. Sci.* 2023, [Project Euclid](https://projecteuclid.org/journals/statistical-science/volume-38/issue-3/Experimental-Design-in-Marketplaces/10.1214/23-STS883.short); inference: Masoero et al. *JRSSB* 2026) | Paired item × user randomization, e.g. article/offer × reader for C5, C8 | Additive interactions between the two sides | Needs two-sided assignment. Power gains plus spillover detection, per [Imbens slides](https://www.lse.ac.uk/statistics/assets/Documents/imbens-lse.pdf). |
| **Separate sending pools per arm** (engineering fix) | C6 | Mailbox providers score reputation per domain or IP | Infrastructure cost; warm-up time. |

---

## 3. Gaps (no good precedent found)

1. **C1:** no published plan-level upsell experiment for family or household plans from Spotify, Netflix, Duolingo, Apple or NYT. The design has to be borrowed from two-stage and partial-interference work.
2. **C2:** no published method for measuring net cannibalization when individual subscribers fold into family plans. Netflix's paid-sharing results are aggregate earnings figures, not experiments.
3. **C3:** Duolingo's social-streak evidence is correlational. No published cluster test of shared leaderboards or streaks was found.
4. **C6:** no published analysis of sender-reputation interference between A/B arms.
5. **C8:** no literature on promo-code leakage through deal forums, which is a channel without geography.
6. **C9:** no newsroom or editorial feedback-loop precedent.
7. **NYT's own randomization unit** (cookie, user or plan) is still **unverified**.

---

## 4. Bibliography

**Verified via search or fetch**
- Hudgens & Halloran 2008, *JASA* — https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548
- Aronow & Samii 2017, *AoAS* — https://projecteuclid.org/journals/annals-of-applied-statistics/volume-11/issue-4/Estimating-average-causal-effects-under-general-interference-with-application-to/10.1214/16-AOAS1005.full
- Baird, Bohren, McIntosh & Özler 2018, *REStat* — https://ideas.repec.org/a/tpr/restat/v100y2018i5p844-860.html
- Basse & Feller, *JASA* (accepted; volume and pages unverified) — https://arxiv.org/abs/1608.06805
- Ugander, Karrer, Backstrom & Kleinberg 2013 — https://arxiv.org/abs/1305.6979
- Ugander & Yin 2020 — https://arxiv.org/abs/2009.02297
- Saveski et al. 2017, *KDD* — https://faculty.washington.edu/msaveski/assets/publications/2017_detecting_network_effects/paper.pdf
- Pouget-Abadie et al. 2019, *Biometrika* — https://faculty.washington.edu/msaveski/assets/publications/2019_biometrika/paper.pdf
- LinkedIn, "Detecting interference: an A/B test of A/B tests" (2019) — https://www.linkedin.com/blog/engineering/ab-testing-experimentation/detecting-interference-an-a-b-test-of-a-b-tests
- Saint-Jacques, Varshney, Simpson & Xu 2019 — https://arxiv.org/abs/1903.08755
- Su & Duan 2023 — https://arxiv.org/abs/2308.05945
- Karrer et al. (Meta) — https://arxiv.org/abs/2012.08591 ; https://research.facebook.com/blog/2021/8/testing-product-changes-with-network-effects/ (KDD year unverified)
- Holtz, Lobel, Lobel, Liskovich & Aral, *Management Science* 71(1) 2025 — https://econpapers.repec.org/RePEc:inm:ormnsc:v:71:y:2025:i:1:p:390-406
- Bojinov, Simchi-Levi & Zhao 2023, *Management Science* — https://arxiv.org/abs/2009.00148
- Si 2023 — https://arxiv.org/abs/2310.17496
- Farias et al. 2023, *RecSys* — https://arxiv.org/abs/2305.02542
- Zigler & Papadogeorgou 2021, *Statistical Science* — https://projecteuclid.org/euclid.ss/1608541221
- Bajari et al., Multiple Randomization Designs — https://arxiv.org/abs/2112.13495 ; *Stat. Sci.* 2023 review — https://projecteuclid.org/journals/statistical-science/volume-38/issue-3/Experimental-Design-in-Marketplaces/10.1214/23-STS883.short
- Johari, Li, Liskovich & Weintraub — https://arxiv.org/abs/2002.05670 (journal version unverified)
- Wager & Xu — https://arxiv.org/abs/1903.02124
- Leung — https://arxiv.org/abs/2111.04219 (journal version unverified)
- Viviano — https://arxiv.org/abs/2003.08421
- Google UGDS 2018 — https://www.unofficialgoogledatascience.com/2018/01/designing-ab-tests-in-collaboration.html
- LinkedIn email volume optimization — https://engineering.linkedin.com/blog/2016/06/less-is-more--optimizing-email-volume-part-1 ; https://engineering.linkedin.com/blog/2016/07/less-is-more--optimizing-email-volume-part-2-
- Netflix sharing update (2023) — https://about.netflix.com/en/news/an-update-on-sharing
- Duolingo Friend Streak — https://blog.duolingo.com/product-lessons-friend-streak/ ; streaks — https://making.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals
- Hightouch account-level tests — https://hightouch.com/playbooks/multivariate-tests-on-user-groups
- Imbens LSE slides — https://www.lse.ac.uk/statistics/assets/Documents/imbens-lse.pdf

**Partly verified (search snippet only)**
- BAFF 2026 — https://arxiv.org/abs/2609.08725
- LinkedIn notification offline-RL paper (venue unverified) — https://arxiv.org/abs/2207.03029
- Masoero et al., *JRSSB* 2026 (MRD inference; no URL beyond the snippet)
- Netflix subscriber figures, secondary sources only — https://www.thewrap.com/netflix-earnings-q4-2023/ ; https://www.marketbeat.com/earnings/transcripts/103770

**Dropped (could not verify)**
- Brennan, Mirrokni & Pouget-Abadie, one-sided bipartite cluster designs
- Hu, Li & Wager, direct and indirect effects under interference
- LinkedIn NOAH (KDD 2024) email paper