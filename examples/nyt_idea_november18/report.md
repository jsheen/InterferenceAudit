# Interference audit

Input: `inputs/nyt.md`  
Model: `claude-opus-5-5`


# User ideas (fed to Agents 4 and 5)

# User idea: fill the empty seats on Family All Access plans

Get members of a Family All Access plan with 2 or 3 members to fill the two or one empty seats, respectively.

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

# Agent 5: Full plans for the selected prototypes

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