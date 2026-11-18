# Interference audit

Input: `inputs/nyt.md`  
Model: `claude-opus-5-5`


# Agent 1: Interference map

# Agent 1: Interference map for The New York Times (stage 1)

**Main findings**
- **Corrections to the description:**
  - The family plans launched in Sept 2025. At launch, Family All Access was $30 and Family Games was $10.
  - A third-party snapshot dated Oct 2026 lists All Access at **$30 and All Access Family at $34 every 4 weeks** after an intro price. That snapshot is not confirmed.
  - Members of a family plan **do not have to share a household**, so the cluster is the plan, not the household.
  - A family plan **counts as 2 subscribers** in reporting, whatever the number of seats.
- **Highest-value channel:** plan-level coupling. One person pays for an upgrade that every member benefits from, and members' engagement affects each other.
- **Biggest bias risk:** invite and seat-filling treatments can merge existing individual subscriptions into one plan. A naive test credits the upgrade and misses the cancellations.

---

## 1. Price table

I could not fetch nytimes.com/subscription ("unable to fetch"). Every row below comes from press or third-party sources. NYT bills **every 4 weeks** (13 bills a year), while the press usually writes "per month".

| Product / plan | Seats | Intro price | Regular price | Billing | Status | Source |
|---|---|---|---|---|---|---|
| All Access (News, Games, Cooking, Wirecutter, Athletic, Audio) | 1 | $4 / 4 wk for year 1 | **$30 / 4 wk** ($390/yr) | 4-weekly | Third-party snapshot dated 2026-10-20, marked "check pending". A Mar 2026 Slickdeals offer also showed $4 then $30. At the Sept 2025 launch it was **$25** (Digiday, Bloomberg); Press Gazette said "$20/month", which conflicts. | [subscriptiongauge](https://subscriptiongauge.com/service/new-york-times), [Slickdeals](https://slickdeals.net/f/19300899-1-year-digital-subscription-to-ny-times-1-week-all-access-4), [Digiday](https://digiday.com/media/how-the-new-york-times-is-betting-on-a-new-family-plan-to-grow-its-digital-subscriber-base-and-revenue/) |
| **All Access Family** | **up to 4** (owner + 3 invitees) | $8 / 4 wk for year 1 | **$34 / 4 wk** ($442/yr) | 4-weekly | Same Oct 2026 snapshot (not confirmed). **$30 at the Sept 2025 launch** (Nieman, Digiday, Axios, Press Gazette). The description's "about $30" is the launch price and may be out of date. | [subscriptiongauge](https://subscriptiongauge.com/service/new-york-times), [Nieman Lab](https://www.niemanlab.org/2025/09/the-new-york-times-launches-a-family-subscription-with-separate-wordles-for-everyone/) |
| **Games Family** | up to 4 | unverified | **$10 / mo** ($120/yr per Nieman) | press says monthly | Launch price (Sept 2025). Current 2026 price unverified. The description's "about $10" matches. | [Nieman Lab](https://www.niemanlab.org/2025/09/the-new-york-times-launches-a-family-subscription-with-separate-wordles-for-everyone/), [Bloomberg](https://www.bloomberg.com/news/articles/2025-09-08/ny-times-unveils-online-family-plans-with-little-added-expense) |
| Games (individual) | 1 | $25 for year 1 (2024 offer) | $6 / 4 wk or $50/yr | 4-weekly / annual | 2024 offer terms. Consistent with "$4 less than Games Family" (Bloomberg, Press Gazette). Current price unverified. | [Slickdeals](https://slickdeals.net/f/17550486-new-york-times-nytimes-games-subscription-limited-time-offer-save-50-25) |
| Cooking (individual) | 1 | unverified | $4.99/mo or $39.99/yr | in-app (App Store) | App Store in-app prices. The web price may differ and is unverified. | [App Store](https://apps.apple.com/MX/app/id911422904) |
| The Athletic (individual) | 1 | promos such as $1/mo (unverified, US) | ~$7.99/mo or $71.99/yr | monthly / annual | Aggregator, not an official page. Other trackers show $9.99 or $13.99. **Unverified.** | [frontdeskreview](https://frontdeskreview.com/software/news-subscriptions/the-athletic/), [Awful Announcing](https://awfulannouncing.com/athletic/the-athletic-increasing-annual-subscription-rate-71-99.html) |
| Wirecutter (individual) | 1 | — | **unverified** (no standalone price found) | — | — | — |
| News only (Basic Digital) | 1 | — | $17 / 4 wk vs $21.99 (App Store). Conflicting, **unverified.** | — | — | [subscriptionpriceguide](https://subscriptionpriceguide.com/services/nytimes/) |
| Registered free account | 1 | free | free until the paywall | — | Not priced | — |

**Verified plan mechanics:**
- Each member has a separate login with their own Wordle/Connections stats, recipe box, saved articles, newsletters and teams.
- Members can be friends; no shared household is required ("leaving it up to you to decide what you want to consider your family").
- Family members **compete on shared leaderboards**.
- New members are invited by an existing member.
- Existing subscribers can upgrade.
- Prices are "subject to promotions and experimentation".
- Early tests point to better retention on family plans. Cotton: someone sharing a plan with 3 others is "much less likely to cancel".

Sources: [Nieman](https://www.niemanlab.org/2025/09/the-new-york-times-launches-a-family-subscription-with-separate-wordles-for-everyone/), [Digiday](https://digiday.com/media/how-the-new-york-times-is-betting-on-a-new-family-plan-to-grow-its-digital-subscriber-base-and-revenue/), [Press Gazette](https://pressgazette.co.uk/paywalls/new-york-times-family-subscriptions/), [Axios](https://www.axios.com/2025/09/08/nyt-family-subscription-plans).

**Price gaps that matter for the upgrade** (my arithmetic, using the numbers above):
- **Games Family → All Access Family:** +$20/mo at 2025 launch prices. At the 2026 snapshot it is $10 → $34, or **+$24**.
- **Per seat on a full plan:** $34 / 4 = **$8.50 per seat** per 4 weeks, versus $30 for one All Access seat.
- **Individual All Access → family:** +$4 per 4 weeks (13%).
- **Intro-price anomaly (inference):** if the $8 first-year family intro is open to existing Games Family owners, the upgrade costs *less* than staying put for a year. Whether existing subscribers qualify for intro pricing is **unverified** and is a key question for Agent 2.

---

## 2. Units and graph

| Unit | Who it is | Neighbors / edges | Notes |
|---|---|---|---|
| Anonymous visitor | Cookie / device | Other devices of the same person; household members on a shared device or IP | One person on several devices is a **unit-mismatch problem, not interference** |
| Registered user | Logged-in free account | Household; people who send them gift articles or game shares; plan inviters | Main target for the paywall |
| Individual subscriber | One paid seat | Household members (substitutes); people they share with | Possible upgrade source for family plans |
| **Plan** (family) | Owner (payer) + up to 3 members | Fully connected group: shared bill, shared leaderboard, invitations | **Natural cluster.** Not the same as a household |
| Household | Co-resident people, devices, print subs | Shared devices and logins; one subscription often "enough" | Partly overlaps with plans |
| Social tie | Wordle/Connections sharers, gift-article recipients, leaderboard rivals | Sparse network beyond the household | Feature details unverified here except plan leaderboards |
| Geography | Designated market area (DMA), metro, team market (Athletic) | Local word of mouth, local news cycles | Mostly common shocks, which are **heterogeneity, not interference** |
| Shared resources | Recommendation training logs; popularity modules; email sender reputation; push/email frequency budgets; promo budget; editorial placement | All users | Algorithmic, marketplace and equilibrium channels |
| Time | Daily puzzle, news cycle | Everyone exposed on the same day | Enables switchback designs |

---

## 3. Lever × outcome matrix

Funnel stages: A = anonymous → registered, R = registered → subscriber, U = upgrade (individual or Games → bundle or family; Games Family → All Access Family), K = retention.

| Lever | Stages | Engagement | Revenue | Retention | Who is directly treated vs who absorbs the effect |
|---|---|---|---|---|---|
| Email nudges | R, U, K | + (habit, newsletters) | + (offers, upsell) | + (re-engagement); − if fatigue or unsubscribes | Sent to one inbox, but can be forwarded; plan owner vs members |
| In-app notifications | U, K | + | + (cross-sell, e.g. Games → Cooking) | + | Seen only by the logged-in member |
| Recommendations (home page) | A, R, K | ++ | + indirectly (paywall hits) | + (habit) | Shared model; popularity signals |
| Push notifications | K, R | ++ short term; risk of opt-out | + indirectly | +/− (fatigue) | Shared per-user frequency budget across teams |
| Personalized paywall | A→R, R | − for non-converters (access blocked) | ++ | ? (discount buyers churn when intro ends) | Household substitution; offers leaked to deal sites |

Within-user cross-product effects, such as Games pushes taking attention from News or a Cooking upsell taking from an Athletic upsell, are **not between-unit interference**. Model them as multi-outcome effects inside one user.

---

## 4. Interference channels

### C1. Plan-level upgrade coupling (Games Family → All Access Family). The core example.
- **Levers / products:** email, in-app and push upsells; personalized paywall shown to Games Family members who hit News, Cooking or Athletic paywalls.
- **Mechanism:**
  - Only the owner pays, but every seat gets the benefit.
  - A treated *member* j (for example, shown a "your plan could unlock Cooking" message at a recipe paywall) asks the owner i, who then upgrades.
  - The upgrade also changes the outcomes of control members k on the same plan: they gain bundle access, engage more and retain better.
  - So treating j changes i's revenue and k's engagement.
- **Graph:** the plan (2–4 people, fully connected).
- **Kind:** shared-plan coupling, with a peer element (members ask the owner).
- **Bias with member-level randomization:**
  - Control members on mixed plans get "treated" through the upgrade. That inflates the control outcome, so the test **understates** the effect.
  - Revenue credited to the treated arm cannot be attributed to a member without double counting.
  - Owner-only randomization misses the member demand that drives the upgrade, so it **understates** the value of a coordinated treatment.
- **Materiality: high.**
  - Moves all three outcomes at once.
  - +$20–24 per 4 weeks per plan converted.
  - Leadership has said family plans improve retention (verified quote, Digiday).
- **Can a cluster treatment add value? Yes (inference):**
  - **Pooled-demand evidence:** tell the owner that "members hit the Cooking/News paywall 14 times this month".
  - **Coordinated timing:** nudge all members in the same week, so members' requests reach the owner while the owner is seeing the offer.
  - **Plan-level trial:** a whole-plan trial of All Access, so that all 4 seats form habits together.
  - None of these can be built by treating one member.

### C2. Seat-filling invites and cannibalization of individual subscriptions
- **Levers / products:** email or in-app "add your family" nudges to family owners; family upsell to individual All Access or Games subscribers.
- **Mechanism:**
  - Owner i invites j.
  - If j is a **paying individual subscriber**, j cancels ($30 → $0) while i's plan rises by about $4 (+$4 total vs −$30).
  - If j is a **registered free user**, the invite converts j, but that conversion lands outside i's experiment cell.
  - If j has churned, the invite reactivates j.
- **Graph:** the owner's personal network. It need not be a household, and the invitee's cell is often unknown before the invite.
- **Kind:** social spillover plus resource substitution (cannibalization).
- **Bias:**
  - Revenue measured on the owner **overstates** the net effect: the invitee's cancellation is not counted, or counted in control.
  - Engagement and retention gains for invitees are **understated** if measured only on owners.
  - Reported subscriber counts move oddly, because each plan counts as 2 (verified).
- **Materiality: high.** It decides whether family plans add net revenue. Cotton says testing and modeling show cannibalization is "relatively small" (Digiday); this is the company's claim, not independently verified.
- **Can a cluster treatment add value?** Partly. Targeting invites at free or registered contacts rather than paying subscribers creates value. Measurement needs the **invite network** as the analysis unit, for example by randomizing owners and tracking invitees to the owner's cell.

### C3. Engagement and retention coupling within a plan (shared leaderboards and streaks)
- **Levers:** Games push and in-app notifications, streak reminders, email.
- **Mechanism:**
  - Nudging member i to play raises i's score on the shared leaderboard (verified feature).
  - That draws j and k to play: rivalry, social proof.
  - Each member's churn risk depends on whether the others are active. The plan cancels as a unit, and the owner cancels if the other seats go idle.
- **Graph:** the plan.
- **Kind:** peer spillover.
- **Bias:** positive spillover to control members, so member-level randomization **understates** engagement and retention effects. Any retention outcome measured per member is mis-specified, because churn is a plan-level event.
- **Materiality: high for retention, medium for engagement.**
- **Can a cluster treatment add value? Yes (inference).** Leaderboard play is complementary: a nudge is worth more when rivals are nudged too. Options include a synchronized "plan challenge" push and nudges aimed at idle seats to protect the payer's retention.

### C4. Substitution within a household at the paywall
- **Levers / products:** personalized paywall, meter tightness, registration walls (News, Cooking, Athletic).
- **Mechanism:**
  - A treated device or person i converts.
  - Household member j, in control, then reads through i's account, shared device or gift links, so j's chance of converting drops.
  - Conversely, a looser paywall for i lowers i's chance of subscribing, which keeps j's need alive.
- **Graph:** household and shared devices or IP. This is a household cluster, not the plan.
- **Kind:** resource substitution (one subscription meets the household's need).
- **Bias:** **overstates** the per-person conversion lift, because control is depressed by treated converts. A global rollout gets about one subscription per household, not one per person.
- **Materiality: medium–high** for revenue. Cookie- or device-level randomization is common for anonymous paywalls (general industry practice; NYT's specific practice is unverified).
- **Can a cluster treatment add value?** Yes (inference): a paywall that detects the household and offers a family plan at the second person's paywall hit. This turns substitution into a plan sale.

### C5. Recommender feedback loop
- **Levers:** home-page recommendations; "Most Popular" and trending modules (whether NYT has these modules is unverified).
- **Mechanism:**
  - Treated users' clicks under the new ranker go into the same training logs and popularity counts that rank content for control users.
  - Control users' data also trains the treatment model.
- **Graph:** all users (one shared model).
- **Kind:** algorithmic feedback loop.
- **Bias:** usually **understates** the effect, because each arm learns from the other and they converge. It can **overstate** when the treatment model uses exploration data that will not exist once it runs alone.
- **Materiality: medium–high for engagement**, lower for revenue and retention.
- **Can a cluster treatment add value?** Not mainly value. The issue is measurement: use separate data pools per arm or a switchback design.

### C6. Email deliverability and push budgets as shared resources
- **Levers:** email and push frequency.
- **Mechanism:**
  - Aggressive email in treatment raises spam complaints and unsubscribes.
  - Mailbox providers rate the *sender* (the domain or IP) as a whole, so inbox placement drops for control as well. This mechanism is general industry knowledge, not verified for NYT.
  - Within a single user, push budgets shared across News, Games and Athletic are **within-user cross-product effects, not interference**.
- **Graph:** all recipients of a sending domain or IP pool.
- **Kind:** competition for a shared resource.
- **Bias:** **overstates** the benefit, because control bears part of the reputation cost and a full rollout would bear all of it.
- **Materiality: medium.** It applies to every email lever.
- **Can a cluster treatment add value?** No. It mainly needs separate sending pools per arm.

### C7. Social sharing and gift articles (Wordle grids, gift links)
- **Levers:** push and email that raise play or reading; prompts to share.
- **Mechanism:**
  - Treated i shares a result grid or a gift article (the gift-article feature exists, but limits are unverified).
  - Recipient j engages, registers, or hits the paywall.
  - A gift link can also *substitute* for j's subscription.
- **Graph:** i's social network, sparse and mostly unobserved.
- **Kind:** peer spillover.
- **Bias:** engagement and acquisition spillover to control **understates** the effect. The revenue direction is ambiguous: acquisition vs free access.
- **Materiality: medium for engagement and acquisition, low–medium for revenue.**
- **Can a cluster treatment add value?** Somewhat (inference): "share with your plan" or "play together" features turn ties into plan invitations, which feeds C2 and C3.

### C8. Leakage of promotional prices and reference-price effects
- **Levers:** personalized paywall offers, retention or win-back offers.
- **Mechanism:**
  - Low offers shown to i get posted on deal forums (verified: NYT offers appear on [Slickdeals](https://slickdeals.net/f/19300899-1-year-digital-subscription-to-ny-times-1-week-all-access-4) and [RedFlagDeals](https://forums.redflagdeals.com/nytimes-com-new-york-times-all-access-digital-subscription-c-20-yr-2816727/)).
  - Control user j then waits or demands the offer. Users also learn that cancelling triggers retention discounts (a third-party guide exists for Athletic retention offers, [lowermysubs](https://www.lowermysubs.com/blog/the-athletic-retention-offer)).
  - Within a plan, members compare offers.
- **Graph:** deal-community network; within-plan and within-household.
- **Kind:** pricing equilibrium effect.
- **Bias:** **overstates** the revenue lift of discounts. Control is not yet anchored to the low price, but the whole market would be after a global rollout.
- **Materiality: medium.** Intro pricing (around $4 per 4 weeks for a year) is the main acquisition tool.
- **Can a cluster treatment add value?** Plan-level offers (one price for the whole plan) reduce comparison within the plan. Mostly this is a measurement issue: use geo or time-based designs.

### C9. Editorial and popularity feedback
- **Mechanism:** pushes in treatment drive traffic to story X. Editors or automated modules see the spike and promote X to everyone. The newsroom using dashboards this way is unverified.
- **Kind:** algorithmic or human feedback loop.
- **Bias:** **understates** the effect (control gains too).
- **Materiality:** low–medium.

### C10. Geography and The Athletic team markets
- Outcomes are correlated because of team performance and local events. These are **common shocks, i.e. heterogeneity, not interference**.
- Real spillover through local fan word of mouth is plausible but small (inference).
- **Materiality: low.** It mainly calls for stratified randomization. Geography is useful as a cluster for testing C8 pricing.

### Not interference (flagged)
- **Moving attention between products for the same user**, e.g. Games push pulling from News: this is a within-user cross-product effect.
- **One person with several cookies:** unit mismatch.
- **Subscriber accounting:** a family plan = 2 reported subscribers regardless of seats (verified). This is a metric artifact. Seats 3–4 add retention value but no reported subscribers, so keep "subscribers" separate from "people with access" in all evaluations.

---

## 5. Ranked shortlist

| Rank | Channel | Cluster | Naive bias | Materiality | Cluster treatment creates value? |
|---|---|---|---|---|---|
| 1 | **C1 Games Family → All Access Family upgrade coupling** | Plan | Understates the effect (control members get upgraded; member demand missed) | High | **Yes:** pooled-demand message to the owner, nudges to all seats, plan-wide trial |
| 2 | **C2 Invites and cannibalization** | Owner's invite network | Overstates net revenue; understates invitee retention | High | Partly: steer invites to non-subscribers |
| 3 | **C3 Engagement and retention coupling within a plan** | Plan | Understates the effect | High (retention) | **Yes:** synchronized challenges, reactivating idle seats |
| 4 | **C4 Household substitution at the paywall** | Household / device graph | Overstates conversions | Medium–high | **Yes:** offer a family plan at the second person's paywall hit |
| 5 | **C5 Recommender feedback loop** | Global model | Usually understates; can overstate | Medium–high (engagement) | No (fix the measurement) |
| 6 | **C8 Promo leakage and reference prices** | Deal communities, geography | Overstates discount lift | Medium | Somewhat: plan-level pricing |
| 7 | **C6 Email deliverability** | Sending pool | Overstates | Medium | No |
| 8 | **C7 Social sharing and gift links** | Social ties | Engagement understated; revenue ambiguous | Medium | Somewhat: plan-oriented sharing |

**Open questions for later stages:**
1. The live 2026 prices for every row; nytimes.com could not be fetched.
2. Whether Games Family owners qualify for the $8 intro price on All Access Family.
3. Whether every family member can see who owns the plan and request an upgrade.
4. How NYT currently randomizes: by cookie, user or plan.

**Sources**
- [Nieman Lab – NYT launches family subscription](https://www.niemanlab.org/2025/09/the-new-york-times-launches-a-family-subscription-with-separate-wordles-for-everyone/)
- [Digiday – NYT betting on family plan](https://digiday.com/media/how-the-new-york-times-is-betting-on-a-new-family-plan-to-grow-its-digital-subscriber-base-and-revenue/)
- [Press Gazette – NYT family subscriptions](https://pressgazette.co.uk/paywalls/new-york-times-family-subscriptions/)
- [Bloomberg – NYT family plans](https://www.bloomberg.com/news/articles/2025-09-08/ny-times-unveils-online-family-plans-with-little-added-expense)
- [Axios – NYT family plans](https://www.axios.com/2025/09/08/nyt-family-subscription-plans)
- [subscriptiongauge – NYT prices (Oct 2026 snapshot)](https://subscriptiongauge.com/service/new-york-times)
- [Slickdeals – All Access $4 then $30 (2026)](https://slickdeals.net/f/19300899-1-year-digital-subscription-to-ny-times-1-week-all-access-4)
- [Slickdeals – Games $25 then $50/yr (2024)](https://slickdeals.net/f/17550486-new-york-times-nytimes-games-subscription-limited-time-offer-save-50-25)
- [App Store – NYT Cooking](https://apps.apple.com/MX/app/id911422904)
- [frontdeskreview – The Athletic pricing](https://frontdeskreview.com/software/news-subscriptions/the-athletic/)
- [Awful Announcing – Athletic $71.99](https://awfulannouncing.com/athletic/the-athletic-increasing-annual-subscription-rate-71-99.html)
- [subscriptionpriceguide – NYT](https://subscriptionpriceguide.com/services/nytimes/)
- [RedFlagDeals – NYT deal thread](https://forums.redflagdeals.com/nytimes-com-new-york-times-all-access-digital-subscription-c-20-yr-2816727/)
- [lowermysubs – Athletic retention offer](https://www.lowermysubs.com/blog/the-athletic-retention-offer)
- [thepricer – NYT cost](https://www.thepricer.org/how-much-does-a-new-york-times-subscription-cost/)

# Agent 2: Industry and literature research

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

# Agent 3: Prototype idea cards

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

# Agent 4: Critique, ranking, and selection

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

# Agent 5: Full plans for the selected prototypes

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