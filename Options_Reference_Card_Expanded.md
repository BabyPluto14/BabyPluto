# Options — Expanded Reference Card

> **Exam task:** Given a graph, you must (1) name the position, (2) explain the payoff logic, (3) give a corporate hedging example.

---

## What Is an Option? (Start Here)

An option is a **contract** that gives the buyer a **right** — but never an **obligation** — to buy or sell an asset at a pre-agreed price (called the **strike price, K**) on or before a future date (called **expiry**).

- The buyer of an option **pays a premium** upfront to get that right.
- The seller of an option **receives the premium** but takes on the **obligation** to fulfill the contract if the buyer decides to exercise.

Because the buyer has a right and the seller has an obligation, the two sides are **not symmetric**: the buyer's loss is capped at the premium paid, while the seller's loss can be much larger.

---

## The 4 Positions at a Glance

| Position | You… | Right / Obligation | Max Loss | Max Gain | Premium |
|---|---|---|---|---|---|
| **Long Call** | Buy call | Right to BUY at K | Premium paid | Unlimited | Pay |
| **Short Call** | Sell call | Obligation to SELL at K | Unlimited | Premium received | Receive |
| **Long Put** | Buy put | Right to SELL at K | Premium paid | K − Premium | Pay |
| **Short Put** | Sell put | Obligation to BUY at K | K − Premium | Premium received | Receive |

---

## Quick Graph Identification

| Right-side shape | Starting level (y-intercept) | Position |
|---|---|---|
| Rising (upward slope) | Below zero (−Premium) | Long Call |
| Falling (downward slope) | Above zero (+Premium) | Short Call |
| Flat right, left side rises | Below zero (−Premium) | Long Put |
| Flat right, left side falls | Above zero (+Premium) | Short Put |

**Reading a payoff graph in two steps:**
1. Look at the right side of the graph (high stock prices). Does the line go up (call) or stay flat (put)?
2. Look at where the line starts on the y-axis. Negative starting point = you paid a premium = long. Positive starting point = you received a premium = short.

---

## Position 1 — Long Call

### What It Is

You **buy** a call option by paying a premium upfront. In return, you receive the **right to buy** the underlying asset at the strike price K on the expiry date. You are not forced to buy — you only exercise the option if it benefits you.

Think of it like this: you pay a small fee today to **lock in a maximum purchase price**. If the asset gets expensive, you use your option and buy cheaply at K. If the asset stays cheap, you ignore the option and buy at the lower market price — your only loss is the premium you already paid.

### Payoff at Expiry — Three Scenarios

**Scenario A — Asset price rises well above K (S >> K):**
You exercise the option. You buy the asset at the agreed price K even though the market price is higher at S. Your profit = (S − K) − Premium. The higher S rises, the more profit you make. There is **no upper limit** on potential gain.

*Example with numbers:* K = 100, Premium = 8, S = 130.
Profit = (130 − 100) − 8 = **+22**

**Scenario B — Asset price ends just above K (S slightly > K):**
You still exercise, but your profit is small. Once S crosses the break-even point (K + Premium), you start making net profit. Below break-even but above K, you exercise but still lose a little.

*Example with numbers:* K = 100, Premium = 8, S = 104.
Profit = (104 − 100) − 8 = **−4** (you exercise but still lose a little)

**Scenario C — Asset price ends at or below K (S ≤ K):**
You do **not** exercise — why would you pay K when the market sells it for less? The option expires worthless. Your total loss = the premium you paid at the start. This is the **worst case** for a long call, and it is bounded.

*Example with numbers:* K = 100, Premium = 8, S = 75.
Loss = **−8** (premium only — nothing more)

**Summary formulas:**
- Payoff = max(S − K, 0)
- Profit = max(S − K, 0) − Premium
- Break-even: S = K + Premium

### Corporate Use — Hedging the Risk That Something You Need to BUY Gets More Expensive

**Why a company uses a long call:** A company knows it will need to purchase a commodity, currency, or input in the future. If the price of that input rises, the company's costs increase and margins shrink. A long call **caps the purchase cost**: no matter how expensive the asset becomes, the company can buy at K.

---

**Scenario 1 — Importer (FX Risk):**

A Belgian electronics company imports goods invoiced in USD. The company needs to pay $1 million in 3 months. Today, €1 = $1.10, which is acceptable. But if the dollar strengthens (say €1 = $1.00), the company will need significantly more euros — its import cost rises sharply.

**The hedge:** The company buys a call option on USD with strike K = $1.05 (per euro). It pays a small premium upfront.

- If USD strengthens and the rate moves to $1.00 = €1: the company exercises the call, buying USD at the capped rate of $1.05 per euro. It avoids the worst of the cost increase.
- If USD stays weak at $1.10 = €1: the company lets the option expire unused and buys USD at the favorable market rate. It only loses the premium paid — a small insurance cost.

**Bottom line:** The long call sets a ceiling on how much the company pays for foreign currency. It converts an open-ended FX risk into a known maximum cost.

---

**Scenario 2 — Airline (Fuel/Commodity Risk):**

An airline's single largest operating cost is jet fuel, which is priced off crude oil. The airline has already sold tickets at fixed prices for flights six months from now. If crude oil spikes from $80/barrel to $120/barrel, the airline's cost structure breaks down — it cannot pass that cost onto passengers after tickets are sold.

**The hedge:** The airline buys call options on crude oil at a strike price of, say, K = $85/barrel. It pays a premium per barrel.

- If oil rises to $120: the airline exercises its calls, effectively buying oil at $85. The $35/barrel saving (minus the premium) offsets the spike in actual fuel costs.
- If oil stays at $80: the airline lets the calls expire. It buys fuel cheaply at the market rate and only loses the option premium — much less than the potential damage from an unhedged $40/barrel spike.

**Bottom line:** The long call acts like a price ceiling on a critical input, allowing the airline to budget and price its services with confidence.

---

## Position 2 — Short Call

### What It Is

You sell a call option to someone else. They pay you a premium upfront, and in return you take on an obligation: if they decide to exercise, you must sell them the asset at K — no matter what the market price is at that point.

The key shift from a long position is that **you no longer have a choice**. The buyer has the right; you have the obligation. Your best outcome is that the price stays below K, the buyer never exercises, and you keep the premium as pure profit. Your worst outcome is that the price surges far above K and you are forced to sell cheaply.

Think of it like being the insurance company, not the customer. You collected a premium to take on someone else's risk. If nothing bad happens (from the buyer's perspective), you pocket the money. If prices spike and the buyer exercises their "claim," you have to pay out.

### Payoff at Expiry

**If the price stays below K:** The buyer has no reason to exercise — they can buy cheaper in the open market. The option expires, and you keep the full premium. This is what you are hoping for.

**If the price rises just above K:** The buyer exercises. You must sell at K even though the market is slightly higher. You give back a little of the premium in the form of a below-market sale, but you still net a small profit overall as long as S stays below K + Premium (your break-even).

**If the price rises far above K:** The buyer exercises. You are forced to sell at K while the market is much higher. The gap between K and the market price eats through your premium and keeps growing. The higher the price goes, the bigger your loss — with no ceiling. This is why short calls have unlimited downside.

With numbers: K = 100, Premium = 8.
- S = 75 → profit = +8 (buyer doesn't exercise, you keep everything)
- S = 105 → profit = +8 − 5 = +3 (buyer exercises, small net gain)
- S = 150 → profit = +8 − 50 = −42 (buyer exercises, large loss)

**Formulas:**
- Profit = Premium − max(S − K, 0)
- Break-even: S = K + Premium
- Max gain: Premium | Max loss: unlimited

### Why the Graph Looks the Way It Does

The profit line starts above zero because you collected the premium on day one — that money is yours regardless. As long as S stays below K, the line stays flat at +Premium. Once S crosses K, the buyer exercises and every extra euro the price rises costs you one euro — so the line slopes downward to the right. Once S passes K + Premium, you are in net loss territory.

### Corporate Use — Generating Income on Assets Already Owned (Covered Call)

A covered call means you already own the underlying shares and you sell a call on top of them. This is the only sensible corporate use of a short call. If the buyer exercises, you simply hand over shares you already hold — there is no cash loss, only a cap on how much you can gain.

**Scenario — Conglomerate with an idle equity stake:**

A conglomerate holds shares in a supplier, currently worth €50 per share. The shares have gone nowhere for a year. The conglomerate would be happy to sell at €60 — that is a good enough return. Instead of just waiting, they sell call options with K = €60 and collect €3 per share today.

If the stock stays below €60, the calls expire and the conglomerate keeps the €3 premium — income earned from a position that was previously doing nothing. If the stock rises to €75, the buyer exercises and the conglomerate must sell at €60. They miss the gain from €60 to €75, but they received their target exit price plus the premium, so this outcome is acceptable. The only bad scenario is if the stock crashes to €30 — they still hold the depreciating shares, and the €3 premium does almost nothing to cushion that loss. A covered call does not protect against falling prices, it only adds income when the market is flat or gently rising.

**A note on naked short calls:** If you sell a call without owning the underlying, you have no shares to deliver if the buyer exercises. You would have to go into the market, buy shares at the high market price, and sell them to the buyer at the low strike price K. The loss is the full gap between market and K, with no ceiling. This is called a naked short call — pure speculation, not hedging, and avoided by most corporate treasuries.

---

## Position 3 — Long Put

### What It Is

You **buy** a put option by paying a premium upfront. In return, you receive the **right to sell** the underlying asset at K. You will only exercise if the market price drops below K, because that lets you sell at K (better than the market).

Think of it like this: you pay insurance. If the asset you own loses value, your put option pays out to compensate. If the asset holds its value or rises, you simply don't claim on the insurance — you just lose the premium (the cost of the policy).

### Payoff at Expiry — Three Scenarios

**Scenario A — Asset price falls far below K (S << K):**
You exercise the option. You sell the asset at K even though the market only offers S < K. Your profit = (K − S) − Premium. The lower S falls, the more you make. Maximum gain occurs if S falls to zero: max gain = K − Premium.

*Example with numbers:* K = 100, Premium = 8, S = 60.
Profit = (100 − 60) − 8 = **+32**

**Scenario B — Asset price falls slightly below K (S slightly < K):**
You still exercise (market is below K so your right to sell at K is valuable), but your net profit depends on whether you've covered the premium. Between K and break-even (K − Premium), you exercise but still suffer a small net loss.

*Example with numbers:* K = 100, Premium = 8, S = 95.
Profit = (100 − 95) − 8 = **−3** (exercise, but net loss because S hasn't dropped far enough to cover the premium)

**Scenario C — Asset price stays at or above K (S ≥ K):**
You do **not** exercise — why sell at K when the market pays more? The put expires worthless. Your total loss = the premium. This is the worst case, and it is fully bounded.

*Example with numbers:* K = 100, Premium = 8, S = 120.
Loss = **−8** (premium only)

**Summary formulas:**
- Payoff = max(K − S, 0)
- Profit = max(K − S, 0) − Premium
- Break-even: S = K − Premium
- Max gain: K − Premium (achieved if S → 0)

### Corporate Use — Hedging the Risk That Something You OWN Loses Value (Portfolio Insurance)

**Why a company uses a long put:** Any time a company or investor holds an asset and fears its value could drop — shares, a currency receivable, a commodity stockpile — a long put sets a **floor** on the minimum selling price. No matter how low the market falls, the put guarantees you can sell at K.

---

**Scenario 1 — Fund Manager (Portfolio Insurance):**

A pension fund holds €500 million in equities. The fund manager is worried about a market correction in the next 6 months but does not want to sell the portfolio (it would trigger taxes and transaction costs, and the manager expects recovery after the correction). Without protection, a 20% market fall would wipe out €100 million.

**The hedge:** The fund manager buys put options on the index (or the underlying stocks) with a strike K close to today's index level. Each option is like an insurance policy on a portion of the portfolio.

- If the market falls 25%: the puts pay out. For every unit of index below K, the put delivers K − S. This offsets the portfolio losses, limiting the fund's drawdown to roughly the premium cost.
- If the market rises 10%: the puts expire worthless. The fund keeps all the upside gains and only forfeits the premium — the cost of the insurance.

**Key insight:** Unlike selling the portfolio, a long put lets you keep full **upside participation** while cutting off the downside beyond K. You pay for this asymmetry with the premium.

---

**Scenario 2 — Belgian Wheat Farmer (Commodity Price Risk):**

A farmer plants wheat in April expecting to harvest and sell in September. The current wheat price is €180/tonne — profitable. But the farmer fears that by September, a bumper global harvest could push prices down to €130/tonne, making the crop barely profitable or even loss-making.

**The hedge:** The farmer buys put options on wheat with K = €175/tonne (close to today's price) and pays a premium of €5/tonne.

- If wheat falls to €130 by September: the farmer exercises the put, effectively selling at €175 instead of €130. The €45/tonne saving (minus the €5 premium) = €40/tonne net benefit. The floor protects the business.
- If wheat rises to €200 by September: the put expires unused. The farmer sells at the high market price of €200 and only loses the €5 premium — a small cost for the security they had all season.

**Key insight:** The long put gives the farmer the **best of both worlds**: a guaranteed minimum price plus full participation in any price rally. The premium is the cost of that certainty, and it allows the farmer to plan cash flows, service loans, and budget inputs with confidence.

---

**Scenario 3 — Exporter (FX Risk):**

A Belgian IT company exports software to the US and will receive $3 million in 3 months. At today's rate of €1 = $1.10, that's roughly €2.73 million. But if the dollar weakens to $1.25 = €1, those dollars convert to only €2.40 million — a €330,000 shortfall.

**The hedge:** The exporter buys a put on USD (the right to sell USD at K = $1.12 per euro, i.e., a floor on how many euros each dollar is worth).

- If USD weakens to $1.25 = €1: the exporter exercises the put, converting at the protected rate of $1.12 = €1. The put compensates for the weaker dollar.
- If USD stays strong at $1.10 = €1: the put expires. The exporter converts at the favorable rate and only loses the small premium.

**Bottom line:** The long put locks in a **minimum revenue** in euros from foreign-currency income, eliminating the FX downside while keeping the benefit if the dollar stays strong.

---

## Position 4 — Short Put

### What It Is

You sell a put option to someone else. They pay you a premium upfront, and in return you take on an obligation: if they decide to exercise, you must buy the asset from them at K — no matter how far the market price has fallen below K.

The short put is the mirror image of the short call, but what hurts you goes in the opposite direction. With a short call, you get hurt when the price rises. With a short put, you get hurt when the price falls. In both cases, you collected a premium at the start and your best outcome is that nothing happens and you keep it.

A good way to picture a short put: you are agreeing to be a buyer of last resort at K. The person who bought the put from you has bought insurance against the price falling. You are the insurer. If the price collapses, they show up at your door and say "you promised to buy at K" — and you must honor that, even though the market is offering much less.

**Simple analogy:** You want to buy a house but think the current asking price of €400,000 is too high. Your target is €350,000. You tell the owner: "I'll pay you €5,000 today, and in return, if the price drops to €350,000, I agree to buy it at that price." The owner takes the deal. Now: if prices stay high, the owner never exercises and you keep the €5,000 with no house purchased. If prices fall to €350,000, the owner exercises and you buy the house at exactly the price you wanted — you even got paid €5,000 to wait for it. The dangerous scenario is if prices collapse to €200,000. The owner still exercises at €350,000, and you are stuck paying €150,000 above market value.

### Payoff at Expiry

**If the price stays above K:** The buyer has no reason to exercise — they can sell their asset at the higher market price instead of selling it to you at K. The option expires and you keep the full premium. This is your best case.

**If the price falls just below K:** The buyer exercises because it is now better for them to sell to you at K than at the lower market price. You buy at K, overpaying slightly relative to the market. As long as the overpayment is less than the premium you collected, you still net a small profit overall.

**If the price falls far below K:** The buyer exercises. You are forced to buy at K even though the asset is now worth much less. The further the price falls, the bigger your overpayment and the bigger your loss. The maximum loss occurs if the asset falls all the way to zero — you paid K for something worthless, minus the premium you received. Unlike the short call, losses here are capped because prices cannot go below zero.

With numbers: K = 100, Premium = 8.
- S = 120 → profit = +8 (buyer doesn't exercise, you keep everything)
- S = 95 → profit = +8 − 5 = +3 (buyer exercises, small net gain)
- S = 50 → profit = +8 − 50 = −42 (buyer exercises, large loss)
- S = 0 → profit = +8 − 100 = −92 (maximum possible loss = K − Premium)

**Formulas:**
- Profit = Premium − max(K − S, 0)
- Break-even: S = K − Premium
- Max gain: Premium | Max loss: K − Premium (when S = 0)

### Why the Graph Looks the Way It Does

The profit line starts above zero on the right side (high S) because you collected the premium upfront. As long as S stays above K, the buyer never exercises and the line stays flat at +Premium. Once S drops below K, the buyer starts exercising and each extra euro the price falls costs you one euro — the line slopes downward to the left. Once S drops below K − Premium, you are in net loss territory. The graph is the opposite shape of the short call: it is flat on the right and falls toward the left.

### Corporate Use — Committing to Buy a Desired Asset at a Lower Price

A company uses a short put when it genuinely wants to acquire something but considers the current price too high. By selling a put at its target price K, the company gets paid to wait. If the price never falls to K, the company earns the premium as income. If the price does fall to K, the company acquires exactly what it wanted at exactly the price it was prepared to pay.

**Scenario — Pharma company targeting a biotech acquisition:**

A pharmaceutical company wants to take a stake in a smaller biotech firm. The biotech currently trades at €50 per share, but the pharma company's own valuation says €40 is the right price to pay. Rather than just waiting and earning nothing, it sells put options with K = €40 and collects a €3 premium per share.

If the biotech stays above €40, the puts expire and the pharma company keeps the €3 per share — it gets paid for its willingness to buy. If the stock falls to €38, the buyer exercises: the pharma company must buy shares at €40, which was its target anyway. With the premium already received, the effective cost is only €37 per share — even better than planned. The risk is if the biotech collapses to €15 due to a failed drug trial: the pharma company is still obligated to buy at €40, taking a significant loss. This is why a short put only makes sense when the company truly wants the asset and has a clear rationale for why K is a fair price.

---

**Scenario 1 — Strategic Acquisition at Target Price:**

A large pharmaceutical company wants to acquire a 10% stake in a biotech start-up. The current share price is €50, but the pharma company's internal valuation says €40 is the right price. It does not want to overpay at €50.

**The strategy:** The pharma company sells put options with K = €40 and receives a premium of €3/share.

- If the biotech stock falls to €38: the put buyer exercises. The pharma company must buy shares at €40, which is what it wanted anyway. Effective cost = €40 − €3 premium = **€37/share net** — even better than its target price.
- If the biotech stock stays above €40 (say €52): the puts expire. The pharma company did not acquire the stake but earned the €3 premium per share as income for waiting. It can re-evaluate its strategy for the next period.

**Key insight:** The short put is a disciplined, income-generating way to pursue an acquisition. Instead of placing a limit buy order (which earns nothing while you wait), you collect premium while you wait — and you buy only if the price reaches your target.

---

**Scenario 2 — Commodity Purchasing Commitment:**

A food manufacturer knows it will eventually need to buy 10,000 tonnes of cocoa. Today's cocoa price is €2,800/tonne, which the manufacturer considers too expensive. It would be comfortable buying at €2,400/tonne.

**The strategy:** The manufacturer sells put options on cocoa with K = €2,400/tonne and receives a premium of €80/tonne.

- If cocoa falls to €2,200: the option is exercised. The manufacturer buys cocoa at €2,400 — overpaying by €200 versus the market, but this is within acceptable range, and the €80 premium reduces the net cost to €2,320/tonne.
- If cocoa stays at €2,800: the puts expire. The manufacturer collects €80/tonne in premium income, lowering the eventual cost whenever it does buy at market price.

**Key risk:** If cocoa collapses to €1,500 (perhaps due to a global supply shock), the manufacturer is locked into buying at €2,400 — a significant overpayment. The short put creates a genuine obligation to buy.

---

## Moneyness — ITM, ATM, OTM

Moneyness describes whether exercising the option right now would be profitable, based on where the market price S is relative to the strike K.

An option is **in the money (ITM)** when exercising immediately would give you a profit. For a call, that means S > K — the market is above your right-to-buy price, so exercising lets you buy cheaply. For a put, that means S < K — the market is below your right-to-sell price, so exercising lets you sell expensively.

An option is **at the money (ATM)** when S ≈ K. Exercising produces nothing — you could just as well transact in the market at the same price.

An option is **out of the money (OTM)** when exercising would make no sense. For a call, S < K means you'd be paying K for something the market sells cheaper. For a put, S > K means you'd be selling at K when the market pays more. OTM options expire worthless if they are still OTM at expiry.

### Option Value = Intrinsic Value + Time Value

**Intrinsic value** is the value if you exercised the option right now:
- Call: max(S − K, 0) — how much above the strike is the current price?
- Put: max(K − S, 0) — how much below the strike is the current price?

An OTM or ATM option has **zero intrinsic value** — exercising right now produces nothing.

**Time value** is everything else: the extra amount the market pays above intrinsic value. It reflects:
- The possibility that the asset price will move favorably before expiry.
- Uncertainty (higher volatility = higher time value, because the option has more chance of moving further ITM).
- Time remaining (more time = more chance of a favorable move = higher time value).

**Key rule:** Time value **decays toward zero** as expiry approaches (this decay accelerates in the final weeks — known as theta decay). At expiry, an option is worth exactly its intrinsic value and nothing more.

**Why ATM options have the most time value:** An ATM option is right on the fence — a small move either way determines everything. The market assigns maximum uncertainty premium here. A deeply ITM option has lots of intrinsic value but little time value (it's almost certainly going to be exercised, so there's less uncertainty). A deeply OTM option has nearly no chance of becoming profitable, so its time value is also near zero.

---

## Put–Call Parity

### The Formula

**C − P = S₀ − PV(K)**

Rearranged: **C + PV(K) = P + S₀**

Where:
- C = price of the call option
- P = price of the put option
- S₀ = current stock (spot) price
- PV(K) = K × e^(−rT) = present value of the strike price (discounted at the risk-free rate)

### What It Means (Plain Language)

Put–call parity is a **no-arbitrage rule** for European options on a non-dividend-paying stock. It says:

> "Two different portfolios that produce identical payoffs at expiry must have identical prices today. If they didn't, traders could buy the cheap one and sell the expensive one for a risk-free profit — arbitrage — until prices adjusted."

**Portfolio A (right-hand side): Fiduciary Call**
- Buy 1 call option (cost = C)
- Invest PV(K) in a risk-free bond (this grows to exactly K at expiry)
- Total cost today: C + PV(K)

**Portfolio B (left-hand side): Protective Put**
- Buy 1 share of the stock (cost = S₀)
- Buy 1 put option on that stock (cost = P)
- Total cost today: P + S₀

**Both portfolios pay the same at expiry:**
- If S > K: Portfolio A = (S − K) + K = S. Portfolio B = S + 0 = S. ✓
- If S ≤ K: Portfolio A = 0 + K = K. Portfolio B = S + (K − S) = K. ✓

Because the payoffs are identical in all scenarios, the costs must be equal: **C + PV(K) = P + S₀**

### Using Put–Call Parity on an Exam

You can rearrange the formula to solve for any one unknown given the other three:
- **Find C:** C = P + S₀ − PV(K)
- **Find P:** P = C − S₀ + PV(K)
- **Find S₀:** S₀ = C − P + PV(K)
- **Find PV(K):** PV(K) = P + S₀ − C

**Practical check:** If you are given call and put prices for the same stock, same strike, same expiry, check whether put–call parity holds. If not, there is an arbitrage opportunity — a free profit is available.

---

## Collar Strategy (Combined Position)

### What It Is

A collar combines three components. First, you already own the underlying asset, so you are exposed to its price movements. Second, you buy a put at a lower strike K_put — this sets a floor, a minimum price you can always sell at. Third, you sell a call at a higher strike K_call — this sets a ceiling, capping how much upside you can capture, but the premium you receive for selling that call offsets the cost of buying the put.

The result is a bounded range: no matter what the market does, your outcome stays between the two strikes.

### Zero-Cost Collar

If the premium received from selling the call **exactly equals** the premium paid for the put, the net cost is zero. You get downside protection for free — but you give up all upside above K_call.

Many corporates structure zero-cost collars because treasurers can tell the board: "We have full protection against price falls below K_put, and it cost us nothing." The trade-off is explicit: they permanently give up any gains above K_call.

### Collar Corporate Example — An Oil Producer

An oil company extracts crude oil at a cost of $50/barrel. Current market price is $85/barrel — very profitable. The company is worried prices might fall next year but also doesn't want to pay for expensive put options.

**The collar structure:**
- Already owns: oil inventory / future production (long the asset)
- Buys a put at K_put = $75/barrel (floor) — pays €4/barrel premium
- Sells a call at K_call = $95/barrel (cap) — receives €4/barrel premium

The premiums cancel → **zero net cost.**

- If oil falls to $55: the put is exercised. The company effectively sells at $75, saving $20/barrel versus the unprotected scenario.
- If oil stays at $85: neither option triggers. The company sells at $85 as normal.
- If oil surges to $110: the call is exercised against the company. It must sell at $95, forfeiting the $15/barrel above that. But the company is still very profitable at $95 — it simply can't capture the windfall.

**The key trade-off:** The collar converts unbounded uncertainty into a **known range** ($75–$95 in this example). This allows the company to plan capital expenditure, service debt, and pay dividends with confidence — regardless of what the oil market does.

---

## Corporate Hedging — Decision Rules

If you fear the price of something you need to **buy** will go up, use a **long call**. It caps your maximum purchase cost at K.

If you fear the price of something you **own** will fall, use a **long put**. It floors your minimum selling price at K.

If you want to generate **income on shares you already hold**, use a **short call**. You collect the premium and agree to sell at K if the price reaches it — an acceptable exit price.

If you want to **acquire an asset at a lower price** than today's market, use a **short put**. You collect premium while you wait, and you buy at K if the price falls to your target.

If you own an asset and want to **limit both downside risk and hedging cost**, use a **collar**. You buy a put (floor) and sell a call (cap). Structured correctly, the two premiums cancel out and the protection is free.

---

## Key Terminology

**Premium** — the price paid by the buyer or received by the seller at the start of the contract. It is non-refundable regardless of what happens later.

**Strike price (K)** — the pre-agreed price at which the option can be exercised. It does not change over the life of the contract.

**In the money (ITM)** — exercising right now would be profitable. For a call: S > K. For a put: S < K.

**At the money (ATM)** — S ≈ K. The option has no intrinsic value, only time value.

**Out of the money (OTM)** — exercising would not be beneficial. The option has zero intrinsic value and expires worthless if it stays OTM.

**Intrinsic value** — the value of the option if exercised right now. max(S − K, 0) for a call; max(K − S, 0) for a put.

**Time value** — everything in the option price above intrinsic value. It reflects how much time is left and how uncertain the outcome is. It decays to zero at expiry and is highest for ATM options.

**Asymmetric payoff** — because the holder has a right and not an obligation, their maximum loss is bounded (the premium), but their potential gain is not. The seller has the opposite profile.

**European option** — can only be exercised at expiry. Used in most textbook formulas including Black–Scholes.

**American option** — can be exercised at any point up to and including expiry. Always worth at least as much as an equivalent European option.

**Put–Call Parity** — C − P = S₀ − PV(K). A no-arbitrage rule stating that two portfolios producing identical payoffs must have the same price today.

**Hedging vs. speculation** — corporates use options to reduce a risk they already face. Speculation means using options to take on new risk in the hope of profit.

**Covered call** — selling a call while already owning the underlying. The obligation is "covered" by the shares held, so there is no cash loss if exercised — only a cap on upside.

**Protective put** — owning the underlying and buying a put on it. Provides a floor on losses while keeping full upside.

**Collar** — a protective put combined with a covered call. Bounds both the upside and the downside. Can be structured as zero-cost.

**Naked short call** — selling a call without owning the underlying. If exercised, you must buy at market and sell at K — an unlimited potential loss. Speculative, not a hedge.

---

## Exam Study Tips

**Tip 1 — Read graphs in two steps:**
First look at the right side (high S): is it sloping up (call) or flat (put)? Then check the y-intercept: negative = you paid premium = long; positive = you received premium = short. Those two observations uniquely identify all four positions.

**Tip 2 — Long = pay, Short = receive:**
Whenever you go long (buy) an option, you pay premium → your profit line starts below zero. Whenever you go short (sell) an option, you receive premium → your profit line starts above zero.

**Tip 3 — Map the exposure first, then pick the option:**
For corporate hedging questions, start by identifying what the company fears: "If X rises / falls, does that hurt the company?" Then choose the option that offsets it. An exporter receiving USD fears USD weakness → needs a put on USD (right to sell USD at K). An importer paying USD fears USD strength → needs a call on USD (right to buy USD at K).

**Tip 4 — Put–call parity rearranges in all directions:**
You can solve for any one of C, P, S₀, PV(K) given the other three. Practice re-arranging the formula before the exam.

**Tip 5 — Time value peaks ATM:**
ATM options have the highest time value because uncertainty about whether they'll finish ITM or OTM is at maximum. Deep ITM options are nearly certain to be exercised (low uncertainty → low time value). Deep OTM options are nearly certain to expire worthless (low uncertainty → low time value). This is key for pricing intuition questions.

**Tip 6 — The premium is always the maximum loss for a buyer:**
No matter what happens, an option buyer can never lose more than the premium paid. This is why options are useful for hedging — the downside of the hedge itself is fully known and limited from day one.
