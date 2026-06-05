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

You **sell** (write) a call option. You receive the premium upfront immediately. In return, you accept the **obligation to sell** the underlying asset at K if the buyer decides to exercise. You no longer have a choice — if the buyer wants to buy at K, you must sell at K, even if the market price is much higher.

Think of it like this: you accept a payment today in exchange for **capping your upside**. If the asset stays cheap, great — you keep the premium for free. If the asset surges, you are forced to sell cheaply and miss all the gains above K.

### Payoff at Expiry — Three Scenarios

**Scenario A — Asset price stays at or below K (S ≤ K):**
The buyer has no incentive to exercise (why pay K when the market is cheaper?). The option expires. You keep the full premium with no further obligation. This is the **best case** for the short call writer.

*Example with numbers:* K = 100, Premium = 8, S = 85.
Profit = **+8** (full premium kept)

**Scenario B — Asset price rises above K but below break-even (K < S < K + Premium):**
The buyer exercises. You must sell at K while the market is at S > K. You lose (S − K) on the transaction, but this loss is less than the premium you received, so you still have a small net profit.

*Example with numbers:* K = 100, Premium = 8, S = 105.
Profit = 8 − (105 − 100) = **+3** (still positive but shrinking)

**Scenario C — Asset price rises far above K (S >> K):**
The buyer exercises. You must sell at K, forfeiting all the upside above K. Your loss grows without bound as S increases. This is the **naked short call** — theoretically unlimited loss.

*Example with numbers:* K = 100, Premium = 8, S = 150.
Profit = 8 − (150 − 100) = **−42** (large loss)

**Summary formulas:**
- Payoff to seller = −max(S − K, 0)
- Profit = Premium − max(S − K, 0)
- Break-even: S = K + Premium

### Corporate Use — Generating Income on Assets Already Owned (Covered Call)

**Why a company uses a short call:** When a company already owns the underlying asset, selling a call is not as dangerous as it sounds. If the stock is called away (buyer exercises), the company simply delivers shares it already holds. The risk of the stock "surging past K and causing losses" is offset by the fact that those shares gain value — so the company doesn't actually lose money; it just misses out on gains above K.

---

**Scenario 1 — Covered Call on an Equity Stake:**

A large industrial conglomerate holds a 5% equity stake in a supplier company worth €50 per share. The conglomerate does not plan to sell in the short term, but it would be happy to sell at €60/share — that would represent a good return. The stock has been trading sideways, generating no income.

**The strategy:** The conglomerate sells call options on those shares with K = €60. It receives a premium of €3/share.

- If the stock stays below €60: the calls expire, the conglomerate keeps its shares AND the €3 premium — extra income on an idle asset.
- If the stock surges to €75: the buyer exercises; the conglomerate must sell at €60. It misses the gain from €60 to €75, but it already achieved its target exit price and collected the premium. This is acceptable.
- Downside: If the stock crashes to €30, the conglomerate still loses on the share value. The premium received (€3) provides only a small cushion against that fall — a covered call is **not** downside protection.

**Bottom line:** The short call converts a static equity position into one that generates regular income, at the cost of capping the upside.

---

**Scenario 2 — Exporter Locking in a Favorable Exchange Rate (Capped Upside):**

A German exporter will receive $2 million in 6 months. The current rate is €1 = $1.08. The company would be very happy converting at $1.05 (they'd get more euros per dollar). They are willing to accept that rate and give up any further euro appreciation.

**The strategy:** The exporter sells a call on EUR/USD (effectively selling a call on EUR from the dollar's perspective) at K = $1.05. They receive a premium.

- If EUR stays weak (rate = $1.10): the buyer does not exercise, and the exporter converts at the favorable market rate and keeps the premium.
- If EUR strengthens significantly: the call is exercised; the exporter converts at $1.05 as agreed — still acceptable to them.

**Important note on naked short calls:** Selling a call **without** owning the underlying is called a **naked short call**. Because losses are theoretically unlimited, this is a speculative bet, not a hedge, and is rarely appropriate for corporate risk management. It requires significant capital reserves and is heavily regulated.

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

You **sell** (write) a put option. You receive the premium upfront immediately. In return, you accept the **obligation to buy** the underlying asset at K if the buyer decides to exercise. The buyer will only exercise if the market falls below K — meaning you are forced to pay K for something worth less than K.

Think of it like this: you agree to be a buyer of last resort at K. You collect a fee (premium) for making this commitment. If the asset never falls to K, you keep the fee and nothing happens. If the asset does fall below K, you must buy it at the above-market price K.

### Payoff at Expiry — Three Scenarios

**Scenario A — Asset price stays at or above K (S ≥ K):**
The buyer has no reason to exercise (market value ≥ K, so they can sell at market for at least as much). Option expires worthless. You keep the premium. Best case for the short put writer.

*Example with numbers:* K = 100, Premium = 8, S = 115.
Profit = **+8** (full premium kept)

**Scenario B — Asset price falls just below K (K − Premium < S < K):**
The buyer exercises. You buy at K, overpaying relative to market. Your loss (K − S) is smaller than the premium you received, so you still net a small profit.

*Example with numbers:* K = 100, Premium = 8, S = 95.
Profit = 8 − (100 − 95) = **+3** (still positive, but shrinking)

**Scenario C — Asset price falls far below K (S << K):**
The buyer exercises. You are forced to buy at K — a large overpayment relative to current market value. Your loss grows as S falls. Maximum loss = K − Premium (if S → 0 the asset is worthless but you paid K for it).

*Example with numbers:* K = 100, Premium = 8, S = 50.
Profit = 8 − (100 − 50) = **−42**

**Summary formulas:**
- Payoff to seller = −max(K − S, 0)
- Profit = Premium − max(K − S, 0)
- Break-even: S = K − Premium
- Max loss: K − Premium (if S → 0)

### Corporate Use — Committing to Buy a Desired Asset at a Lower Price

**Why a company uses a short put:** A company that genuinely wants to acquire an asset (shares, land, equipment) but thinks the current price is too high can sell a put at its target acquisition price K. If the price never falls to K, the company keeps the premium as compensation for being willing to buy. If the price does fall to K, the company gets what it wanted at exactly the price it was prepared to pay.

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

Moneyness describes the relationship between the current stock price S and the strike price K. It tells you whether exercising right now would be profitable.

| State | Call (right to buy) | Put (right to sell) | Intrinsic Value |
|---|---|---|---|
| **In the Money (ITM)** | S > K — exercising is profitable | S < K — exercising is profitable | > 0 |
| **At the Money (ATM)** | S = K — indifferent | S = K — indifferent | 0 |
| **Out of the Money (OTM)** | S < K — would not exercise | S > K — would not exercise | 0 (expires worthless if still OTM) |

### Why Moneyness Matters — Intuitive Explanation

**For a call:** You have the right to BUY at K. That right is only useful if the market price S is **above K** — otherwise you'd just buy cheaper in the market. So a call is ITM when S > K.

**For a put:** You have the right to SELL at K. That right is only useful if the market price S is **below K** — otherwise you'd just sell at the higher market price. So a put is ITM when S < K.

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

A collar combines three components:
1. **Own the underlying asset** (e.g., shares in a company, a currency receivable, a commodity stockpile)
2. **Buy a put** at a lower strike K_put — this creates a floor: your minimum selling price
3. **Sell a call** at a higher strike K_call — this creates a ceiling: your maximum selling price, but you collect premium that offsets the put's cost

The result is a **bounded range**: you can neither benefit if the price rises above K_call, nor suffer if it falls below K_put.

| Leg | Position | Effect on You |
|---|---|---|
| 1 | Already own the underlying asset | Exposed to price movements |
| 2 | Buy a put (strike K_put, lower) | Sets a floor — limits downside loss |
| 3 | Sell a call (strike K_call, higher) | Sets a cap — limits upside gain; premium received offsets cost of put |

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

## Corporate Hedging — One-Line Rules

| You fear… | You use… | Why it works |
|---|---|---|
| Price of something you **BUY** goes UP | **Long Call** | Caps your maximum purchase cost at K |
| Price of something you **OWN** goes DOWN | **Long Put** | Floors your minimum selling price at K |
| You want **income** on shares you hold | **Short Call** | Collect premium; agree to sell at K (acceptable exit price) |
| You want to **buy shares at a lower price** | **Short Put** | Collect premium; acquire at K if price falls to target |
| You own an asset and want to **limit both risk and cost** | **Collar** | Buy put (floor) + sell call (cap); can be structured as zero-cost |

---

## Key Terminology

| Term | Definition |
|---|---|
| **Premium** | The price paid (buyer) or received (seller) for the option contract at inception. Non-refundable. |
| **Strike price (K)** | The pre-agreed price at which the option can be exercised. Fixed throughout the option's life. |
| **In the money (ITM)** | Exercising right now would be profitable: S > K for a call; S < K for a put. |
| **At the money (ATM)** | S ≈ K. Intrinsic value is zero; only time value remains. |
| **Out of the money (OTM)** | Exercising would not be beneficial. The option has zero intrinsic value. Expires worthless if still OTM at expiry. |
| **Intrinsic value** | max(S − K, 0) for a call; max(K − S, 0) for a put. The value if exercised right now. |
| **Time value** | Option price − intrinsic value. Reflects uncertainty and time remaining. Decays to zero at expiry (theta decay). Highest for ATM options. |
| **Asymmetric payoff** | Option holder has a right, not an obligation → bounded maximum loss (the premium) but uncapped upside (for buyers). |
| **European option** | Can only be exercised at expiry. Used in most textbook formulas (e.g., Black–Scholes). |
| **American option** | Can be exercised at any time up to and including expiry. Always worth at least as much as an equivalent European option. |
| **Put–Call Parity** | C − P = S₀ − PV(K). A no-arbitrage relationship for European options: two portfolios with identical payoffs must cost the same today. |
| **Hedging vs. speculation** | Corporates use options to REDUCE an existing risk exposure (hedging). Speculation means taking on new risk to profit from price moves. |
| **Covered call** | Short call + own the underlying. Limits upside but the obligation is covered by shares held — not as dangerous as a naked short call. |
| **Protective put** | Own the underlying + long put. Provides downside insurance while keeping unlimited upside. |
| **Collar** | Protective put + covered call on the same underlying. Bounds both upside and downside. Can be zero-cost. |
| **Naked short call** | Selling a call without owning the underlying. Theoretically unlimited loss. Speculative, not a hedge. |

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
