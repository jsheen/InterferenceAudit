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