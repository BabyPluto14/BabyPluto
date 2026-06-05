# Options — Exam Reference Card
### All 4 Positions: Identify the Graph, Payoff, and When a Company Uses It

> **The exam gives you a graph. You must: (1) name the position, (2) explain the payoff logic, (3) give a corporate hedging example.**

---

## The 4 Positions at a Glance

| Position | You... | Max Loss | Max Gain | Pay/Receive premium? |
|---|---|---|---|---|
| Long Call | Buy a call | Premium paid | Unlimited | Pay |
| Short Call | Sell a call | Unlimited | Premium received | Receive |
| Long Put | Buy a put | Premium paid | Strike price − premium | Pay |
| Short Put | Sell a put | Strike price − premium | Premium received | Receive |

---

## POSITION 1 — Long Call

**What it is:** You buy the RIGHT to purchase an asset at strike price K. You pay a premium upfront.

**Payoff at expiry:**

```
If S > K:  Exercise. Payoff = S − K.  Profit = (S − K) − Premium
If S ≤ K:  Don't exercise. Loss = Premium (maximum possible loss)
```

**Graph shape:** Flat at −Premium below K. Then rises linearly above K. Breaks even at S = K + Premium.

```
Profit
  |                        /
  |                       /
  |                      /
--+----------[K]---------/------→ Stock price at maturity
  |          |          /
  |__________|_________/   ← flat at −Premium
             K
```

**Corporate use — hedges: risk of BUYING something that gets MORE EXPENSIVE**

> An **importer** (e.g. Belgian company buying goods priced in USD) fears the EUR/USD rate will move against them, making imports costlier. They buy a call on USD — capping their effective exchange rate. If USD stays cheap, they let the option expire and buy at market. If USD spikes, the call compensates.

> An **airline** buying jet fuel buys a call on crude oil — capping fuel costs regardless of how high oil goes.

---

## POSITION 2 — Short Call

**What it is:** You SELL a call option. You collect the premium upfront, but take on the obligation to sell the asset at K if the buyer exercises.

**Payoff at expiry:**

```
If S ≤ K:  Buyer doesn't exercise. You keep the premium. Profit = Premium
If S > K:  Buyer exercises. You must sell at K < market price. Loss = (S − K) − Premium
```

**Graph shape:** Flat at +Premium above K. Then falls linearly below K (mirror image of long call).

```
Profit
  |__________ ← flat at +Premium
  |          |
--+----------[K]----→ Stock price at maturity
              \
               \
                \  ← unlimited loss potential
```

**Corporate use — income generation on assets already owned (covered call)**

> A company that **already holds shares** in another firm sells call options on those shares to earn extra income (the premium). They are willing to sell the shares at K if the price rises that far. Risk: if the stock surges far above K, they miss the upside.

> **Important:** naked short calls (without owning the underlying) are very risky and rarely used for hedging — more of a speculative position.

---

## POSITION 3 — Long Put

**What it is:** You buy the RIGHT to SELL an asset at strike price K. You pay a premium upfront.

**Payoff at expiry:**

```
If S < K:  Exercise. Payoff = K − S.  Profit = (K − S) − Premium
If S ≥ K:  Don't exercise. Loss = Premium (maximum possible loss)
```

**Graph shape:** Rises linearly as stock falls below K. Flat at −Premium above K. Mirror image of long call, but on the left side.

```
Profit
  \
   \
    \
-----[K]----------+-------→ Stock price at maturity
                  |________  ← flat at −Premium
```

**Corporate use — hedges: risk of OWNING something that LOSES VALUE (insurance)**

> A **fund manager** holding a large position in a stock buys put options on it — if the stock crashes, the put pays out, offsetting the loss. This is portfolio insurance.

> A **Belgian farmer** growing wheat fears prices will fall before harvest. They buy a put on wheat — guaranteeing a minimum selling price (K), while still benefiting if prices rise (they just don't exercise the put).

> An **exporter** receiving USD in 3 months buys a put on USD — locking in a minimum EUR conversion rate. If USD weakens, the put compensates.

---

## POSITION 4 — Short Put

**What it is:** You SELL a put option. You collect the premium, but take on the obligation to BUY the asset at K if the buyer exercises.

**Payoff at expiry:**

```
If S ≥ K:  Buyer doesn't exercise. You keep premium. Profit = Premium
If S < K:  Buyer exercises. You must buy at K > market price. Loss = (K − S) − Premium
```

**Graph shape:** Flat at +Premium above K. Then falls as stock drops below K.

```
Profit
  |__________  ← flat at +Premium
             |
-------------[K]-----→ Stock price at maturity
            /
           /  ← loss grows as price falls
```

**Corporate use — willingness to acquire at a lower price**

> A company that **wants to buy shares** in a target (but thinks the current price is too high) sells put options at their desired purchase price K. If the stock falls to K, the put is exercised and they acquire the shares at K — the price they wanted anyway. They also pocket the premium as compensation for waiting.

---

## How to Identify the Graph in the Exam

**Step 1 — Look at what happens on the RIGHT side (high stock price):**
- Rising line → involves a CALL (benefit from price going UP)
- Flat line → involves a PUT (don't benefit from price going up)

**Step 2 — Look at the starting level:**
- Starts BELOW zero (at −Premium) → you BOUGHT the option (Long)
- Starts ABOVE zero (at +Premium) → you SOLD the option (Short)

**Quick identification table:**

| Right side | Starting level | Position |
|---|---|---|
| Rising (upward slope) | Below zero (−Premium) | **Long Call** |
| Falling (downward slope) | Above zero (+Premium) | **Short Call** |
| Flat (at +Premium level) with left side rising | Below zero (−Premium) | **Long Put** |
| Flat (at +Premium level) with left side falling | Above zero (+Premium) | **Short Put** |

---

## Corporate Hedging — One-Line Rules

| You fear... | You use... | Because... |
|---|---|---|
| Price of something you BUY goes UP | **Long Call** | Caps your maximum purchase cost |
| Price of something you OWN goes DOWN | **Long Put** | Floors your minimum selling price |
| You want income on shares you hold | **Short Call** | Collect premium, agree to sell at K |
| You want to buy shares cheaper | **Short Put** | Collect premium, agree to buy at K |

---

## Key Terminology the Exam Expects

- **Premium** — the price paid/received for the option contract
- **Strike price (K)** — the pre-agreed exercise price
- **In the money** — exercising would be profitable (S > K for call; S < K for put)
- **Out of the money** — exercising would not be beneficial; option expires worthless
- **Asymmetric payoff** — the option holder has a right, not an obligation → bounded loss, asymmetric upside/downside
- **Intrinsic value** — max(S − K, 0) for a call; max(K − S, 0) for a put
- **Hedging vs. speculation** — corporates use options to REDUCE risk exposure, not create it

---

*Study tip: For the exam graph question — identify the shape first (flat vs. sloping on each side), then read the sign of the starting intercept. Those two observations uniquely determine all 4 positions.*
