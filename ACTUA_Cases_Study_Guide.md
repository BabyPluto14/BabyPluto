# ACTUA Cases — Complete Study Guide
## Corporate Finance: Context, Theory, and Exam Applications

---

> **What are the ACTUA cases?**
> The ACTUA cases are real-world news stories, academic papers, and current events discussed in the course to illustrate how corporate finance theory applies in practice. They are a dedicated exam question type (Q Type 4) and can also be woven into conceptual questions elsewhere. This guide covers all four cases in full depth: what they are about, which chapters they link to, and every way they can appear on the exam — both calculation and theory.

---

## TABLE OF CONTENTS

1. ACTUA 1 — Belgian Pension Reform (2017)
2. ACTUA 2 — The Van Peteghem Bond (2023)
3. ACTUA 3 — The GameStop Short Squeeze (2021)
4. ACTUA 4 — Gu & Lev (2011): Overpriced Shares & Goodwill Impairment

---

---

# ACTUA 1 — The Belgian Pension Reform (2017)

## What is this case about?

In 2017 the Belgian government launched a pension reform plan that remains in effect. The core offer:

- **Employees can "buy off" (redeem) up to 3 years** of higher education for the state pension.
- **Cost:** €1,500 per redeemed year. With the 10% discount (available March 2017–March 2020) and a 50% marginal tax deduction, the effective real cost per year = €1,500 × 0.90 × 0.50 = **€675/year**, or a **maximum total investment of €2,025** for 3 years.
- **Benefit:** An **additional €250/year** in gross pension income for each redeemed year — a maximum of **€750/year extra** upon retirement, paid for the rest of your life.

**The question the case poses:** Is this a good financial deal? Should you do it?

---

## The Financial Logic

The scheme is a **financial trade-off involving time value of money**:

- You give up **€2,025 today** (a lump-sum cash outflow, t = 0).
- In return, you receive **€750/year** starting at retirement and continuing until death (a deferred annuity).
- The longer before retirement, the more the €2,025 could have grown elsewhere.
- The longer you live after retirement, the more pension payments you collect.

**The break-even formula (from the course):**

```
Alternative investment beats the scheme when:

  2,025 × (1 + r)^t   >   750 × [1 − (1+r)^(−z)] / r

where:
  t = years until retirement
  z = years alive after retirement
  r = annual return achievable on alternative investments
```

**Solving for the break-even r** (trial and error or financial calculator):
For t = 30 years (retire at 65, currently 35) and z = 15 years alive post-retirement:

```
Break-even r ≈ 4.67%
```

**Full sensitivity table from the course:**

| (t years to retire / z years post-retire) | z=10  | z=15  | z=20  | z=25  |
|------------------------------------------|-------|-------|-------|-------|
| t = 40 years                             | 2.93% | 3.66% | 4.10% | 4.38% |
| t = 30 years                             | 3.77% | 4.67% | 5.18% | 5.49% |
| t = 20 years                             | 5.34% | 6.45% | 7.05% | 7.40% |
| t = 10 years                             | 9.03% | 10.56%| 11.24%| 11.58%|

**Reading the table:** If you're 35 (t=30) and expect to live 20 years after retirement (z=20), the break-even is 5.18%. If you can earn more than 5.18%/year elsewhere, **don't join**. If less, **join**.

**Key insight:** The **closer you are to retirement** and the **longer you expect to live**, the more attractive the scheme becomes. Far from retirement → TVM works strongly against the plan.

**Additional caveat from the course:** The €750/year benefit is a **gross/pre-tax pension amount**, and progressive taxation on pensions makes the actual after-tax benefit even lower — making the scheme even less attractive than the numbers suggest.

---

## Which Chapters Does This Case Link To?

| Chapter | Connection |
|---------|------------|
| **CH0 / CH1 — Financial Valuation Fundamentals** | The 3 ingredients of valuation: cash flows, timing, discount rate. The pension scheme is a valuation problem. |
| **CH3 — Bonds / TVM** | Annuity formula, deferred annuity, present value of future cash flows, time value of money, opportunity cost of capital. |
| **CH5–6 — Investment Decision Tools** | NPV framework: is the pension scheme a positive-NPV "investment"? Break-even analysis (at what return is NPV = 0?). |
| **CH9 — WACC / Opportunity Cost** | The "hurdle rate" for the pension scheme is the individual's opportunity cost — what they could earn elsewhere at similar risk. |

---

## How Can This Case Appear on the Exam?

### Theory Questions (No Calculation)

**Q: Explain why time value of money is a critical factor in evaluating the pension scheme.**

> The €2,025 is paid today. By committing it to the pension scheme, you lose the ability to invest it elsewhere where it would grow exponentially. The opportunity cost of the scheme is the foregone compound return over 30+ years. A modest 5–6% alternative return can grow €2,025 into €8,000–€15,000 by retirement, far exceeding what the pension annuity is worth in PV terms. TVM limits the pension benefit substantially: future cash flows are heavily discounted.

**Q: Which uncertain factors determine whether to join? Direction of each?**

> 1. **Time to retirement (t):** longer → TVM works harder against the scheme → less attractive (−)
> 2. **Years alive after retirement (z):** longer → more pension payments collected → more attractive (+)
> 3. **Achievable alternative return (r):** higher → opportunity cost of joining is higher → less attractive (−)

**Q: The pension benefit of €750/year is a gross (pre-tax) amount. How does progressive taxation affect the decision?**

> Progressive taxation on pension income means the actual after-tax benefit received is lower than €750. If marginal pension tax rate is e.g. 30%, real benefit ≈ €525/year. This further reduces the PV of the pension stream and raises the break-even required alternative return — making the scheme even less appealing.

**Q: Conceptually, why does the attractiveness of the pension scheme increase as you approach retirement?**

> Because TVM has less time to "work against" the scheme. With only 10 years to retirement, the €2,025 cannot grow very much elsewhere. The break-even return jumps to 9–11%, which most investors cannot reliably achieve. Close to retirement, even low-risk investments beat the scheme only marginally, so the guaranteed pension benefit becomes relatively more attractive.

---

### Calculation Questions

**Q: A person aged 35 expects to retire at 65 (t=30) and live 15 years after retirement (z=15). They can earn 6% per year on alternative investments. Should they join the pension scheme?**

Step 1 — FV of alternative investment at retirement:
```
FV = 2,025 × (1.06)^30 = 2,025 × 5.7435 = €11,630.59
```

Step 2 — PV of pension annuity at retirement:
```
PV_annuity = 750 × [1 − (1.06)^(−15)] / 0.06
           = 750 × [1 − 0.4173] / 0.06
           = 750 × 9.7122
           = €7,284.15
```

Step 3 — Compare:
```
FV of alternative = €11,630.59  >  PV of pension = €7,284.15
```
→ **Do NOT join** — alternative investment delivers more value at retirement.

*(The break-even for t=30, z=15 is 4.67%. Since 6% > 4.67%, the alternative wins.)*

**TI-84 Instructions:**

FV of alternative: `2025 × 1.06^30` → 11,630.59

PV of pension annuity (at retirement): TVM Solver: N=15 | I%=6 | PMT=750 | FV=0 → PV = −7,284.15

**Q: Two-step model — calculate the price of an "inflation-linked" annuity product.**

*(See the slide example from the course — these are very similar to exam Q Type 1 MC questions.)*

An inflation-linked product pays €150/year for 4 years, then grows at 1% (inflation) forever. Nominal rate = 5%.

```
Step 1: PV of annuity (t=1 to 4):
PV₁ = 150 × [1 − (1.05)^(−4)] / 0.05 = 150 × 3.5460 = €531.89

Step 2: PV of growing perpetuity (from t=5):
PV at t=4 = 150×1.01 / (0.05−0.01) = 151.50 / 0.04 = €3,787.50
PV at t=0 = 3,787.50 / (1.05)^4 = €3,116.57

Total fair price = 531.89 + 3,116.57 = €3,648.46
```

**Buy-hold-sell:** If market price = €1,500 → massively underpriced → **BUY**.

---

### Exam Tips for ACTUA 1

- Always connect the pension scheme to the **NPV / opportunity cost framework** (the course's core logic).
- The three uncertainty factors (t, z, r) and their **direction** are almost always asked.
- The **break-even formula is the key formula**: FV of investment = PV of annuity upon retirement.
- Remember the **additional drawback**: pension income is taxed progressively — the €750/year is gross.
- This case also links to **annuity-due** vs. **ordinary annuity** distinctions if cash flows start "immediately" vs. end of period.

---

---

# ACTUA 2 — The Van Peteghem Bond (2023)

## What is this case about?

In **September 2023**, Belgian Finance Minister Vincent Van Peteghem launched a special **1-year Belgian government bond** with exceptional characteristics:

| Feature | Detail |
|---------|--------|
| Nominal rate (gross) | **3.3% per year** |
| Tax regime | **Favorable 15%** (vs. normal 30%) |
| Effective after-tax rate | 3.3% × (1 − 0.15) = **2.805%** |
| Maturity | 1 year |
| Result | **€21.9 billion** raised from ~630,000 Belgian investors — a record |

### Why was this a "master move"?

**Background — Monetary policy context:**
- 2008–2017: Near-zero interest rates due to ECB's quantitative easing (ZIRP). Banks couldn't earn on the interest rate differential → diversified into fee-based activities.
- 2020–2022: COVID + supply chain disruptions → inflation surged globally.
- 2022–2023: ECB rapidly raised interest rates to fight inflation.
- **Bank reaction:** Banks were **slow to pass higher rates on to depositors** while immediately increasing rates on loans → maximizing yield spread (profit).

**The political play:** Van Peteghem pressured banks by offering ordinary citizens a state bond at 3.3% under favorable tax — better than anything banks were offering on 1-year savings. It triggered **€21.9 billion in outflows from bank deposits**, directly hurting bank balance sheets.

### Why did the second attempt (February 2024) fail?

Three reasons:
1. **Some banks reacted**: under competitive pressure, several banks raised savings rates, making the state bond less uniquely attractive.
2. **Inverted yield curve**: Short-term government rates were now **higher than medium-term rates**. It was cheaper for the government to issue a longer-term bond at lower yield.
3. **Political backlash**: The favorable **15% tax regime was vetoed** by political opponents. The standard 30% rate applied, substantially reducing the after-tax return for investors.

---

## Key Financial Concepts

### 1. Bond Valuation

```
Bond Price = Σ [Coupon / (1+YTM)^t]  +  Par / (1+YTM)^n

For the Van Peteghem bond (1yr, 3.3% coupon, par = 1000):
Price at YTM 3.3% = 1033/1.033 = 1000 (issued at par)
```

### 2. After-Tax Yield
```
After-tax coupon = Gross coupon × (1 − tax rate)
After-tax yield  = After-tax coupon / Price
                 = 3.3% × (1 − 0.15) = 2.805%    [favorable 15% tax]
                 = 3.3% × (1 − 0.30) = 2.31%     [standard 30% tax]
```
The difference between 2.805% and 2.31% explains much of the political controversy and why the second bond failed.

### 3. Yield Curve

**Normal (upward-sloping) yield curve:**
- Long-term bonds yield more than short-term bonds.
- Signals confidence in economy; investors demand term premium for locking up money longer.

**Inverted yield curve:**
- Short-term rates > long-term rates.
- Signals recession fears; investors expect central banks to cut rates in the future.
- Short-term government bonds become more expensive for the government to issue.
- In 2024: issuing a 2–3 year bond was cheaper than a 1-year bond → less incentive to repeat the 1-year bond.

### 4. Monetary Policy & Bank Profits

```
Bank profit (simplified) = Yield spread = Lending rate − Deposit rate

Zero-rate environment (2008–2021):
  → Spread compressed → low profits → banks pivoted to fee income

Rising rate environment (2022–2024):
  → Spread expands → profits surge
  → But banks slow to raise deposit rates → extra-wide spreads
```

---

## Which Chapters Does This Case Link To?

| Chapter | Connection |
|---------|------------|
| **CH3 — Bonds** | Bond valuation, YTM, coupon, nominal vs. after-tax yield, yield curve, inverted yield curve, bond risks |
| **CH0 / CH1 — Value and opportunity cost** | NPV of saving in bank deposit vs. state bond: comparing after-tax returns |
| **CH10 — Market Efficiency** | Did the market reflect the "true" value of savings instruments? Bank slow to adjust = pricing inefficiency |
| **CH10 — Debt Policy / Capital Structure** | Government as bond issuer; impact on banking sector balance sheets |

---

## How Can This Case Appear on the Exam?

### Theory Questions (No Calculation)

**Q: Explain what the yield curve is and what an inverted yield curve signals.**

> The yield curve plots the interest rates (YTM) of government bonds of the same credit quality against maturities (from short to long). A normal curve slopes upward — investors demand higher rates for longer maturities (term premium) and it signals a healthy economy with expected long-run growth. An inverted curve occurs when short-term rates exceed long-term rates. It signals that investors expect economic slowdown and future central bank rate cuts — the market is pricing in lower future rates, pulling down the long end of the curve. Historically, an inverted yield curve is a reliable predictor of recession.

**Q: Why did the Van Peteghem bond (2023) succeed and the 2024 attempt fail?**

> In 2023: the bond succeeded because it offered 3.3% gross (2.805% after favorable 15% tax) at a time when bank savings accounts paid near zero — a dramatic mismatch. Investors rationally preferred the state bond. In 2024: (1) banks responded by raising deposit rates, reducing the attractiveness gap; (2) the yield curve had inverted, making 1-year government bonds more expensive to issue than longer-term ones; (3) the favorable 15% tax regime was politically vetoed, reverting to the standard 30%, which slashed the after-tax return to 2.31%.

**Q: Explain how monetary policy affects bank profitability. Why were banks "slow to adapt"?**

> Banks profit from the spread between lending rates and deposit rates. In the near-zero rate environment post-2008, this spread was compressed and banks pivoted to fee-based income. When the ECB raised rates from 2022, banks quickly raised lending rates (increasing interest income) but were slow to raise deposit rates (keeping interest expense low), intentionally maximizing the yield spread to compensate for a decade of low profitability. The Van Peteghem bond exposed and disrupted this strategy by offering depositors a better alternative.

**Q: What is the difference between nominal and real interest rates? How does inflation affect bond valuation?**

> Nominal rate = the stated rate including inflation compensation.
> Real rate = the purchasing-power-adjusted return.
> Fisher equation: (1 + nominal) = (1 + real) × (1 + inflation)
> When valuing inflation-linked instruments, be consistent: either use nominal rates to discount nominal cash flows, or real rates to discount real cash flows. Inflation reduces the real return to bond-holders and is one of the key bond risks.

**Q: How did the Van Peteghem bond affect the banking sector's balance sheet?**

> Directly: €21.9 billion flowed out of bank deposit accounts into state bonds. Banks suddenly faced a massive reduction in their deposit funding base, creating a liquidity squeeze.
> Indirectly: competitive pressure forced banks to raise savings rates to retain depositors, increasing their cost of funding and compressing the previously-inflated yield spread.
> The episode illustrates how government financing policy can be used as a macroprudential tool to discipline the banking sector.

---

### Calculation Questions

**Q: The Van Peteghem bond has a nominal value of €1,000, annual coupon of 3.3%, 1-year maturity, redeemed at par. An investor pays 15% tax on coupon income. If the required post-tax YTM is 2.5%, what is the fair price?**

```
After-tax coupon = 3.3% × 1,000 × (1 − 0.15) = 33 × 0.85 = €28.05
Redemption = €1,000 (at par)

Price = (28.05 + 1,000) / (1 + 0.025) = 1,028.05 / 1.025 = €1,003.00
```
Bond trades slightly above par (28.05 after-tax coupon > 25 required return → premium).

**Q: A 2-year government bond, nominal €1,000, coupon 3.3% annual, YTM = 1.5%. Calculate price, duration, and bond volatility.**

Price:
```
PV₁ = 33 / 1.015 = 32.51
PV₂ = 1,033 / 1.015² = 1,003.03 - wait let me redo

PV₂ = 1,033 / 1.030225 = 1,002.69

Price = 32.51 + 1,002.69 ... 

Hmm wait, that doesn't work for a 2yr bond. Let me redo:

1yr: 33/1.015 = 32.512
2yr: 1033/1.030225 = 1002.69 (coupon + principal together)

Price = 32.512 + 1002.69 = 1,035.20

Wait that seems high. Let me check:
1.015^2 = 1.030225
1033/1.030225 = 1002.693

Price = 32.512 + 1002.693 = 1,035.20
```

Duration:
```
Duration = (1 × 32.512 + 2 × 1002.693) / 1035.20
         = (32.512 + 2005.386) / 1035.20
         = 2037.898 / 1035.20
         = 1.9685 ≈ 1.97 years
```

Modified Duration (Volatility):
```
Volatility = Duration / (1 + YTM) = 1.9685 / 1.015 = 1.939%
```
A 1% rise in YTM reduces bond price by approximately 1.94%.

---

### Exam Tips for ACTUA 2

- Know the **yield curve** cold — normal vs. inverted, what each signals, why it matters for issuing bonds.
- The **after-tax yield formula** is key: always check whether the exam specifies a tax rate on coupon income.
- Be prepared to explain the **monetary policy timeline**: zero rates (2008–2022) → inflation → ECB rate hikes → bank profits → Van Peteghem intervention.
- The "second attempt failed" story tests understanding of **inverted yield curve** and **competitive dynamics**.
- Bond **duration and volatility** questions are directly linkable to this case: a 1-year bond has very low duration and hence low interest-rate risk — one reason it was "safe" for investors.
- The case also illustrates **interest rate risk**: if rates fall after you buy, your bond price rises (capital gain); if rates rise, your bond price falls.

---

---

# ACTUA 3 — The GameStop Short Squeeze (February 2021)

## What is this case about?

**GameStop** (ticker: GME) is a US brick-and-mortar video game retailer. By 2021 it was a struggling company — physical game stores were losing relevance due to digital streaming and online purchasing.

**The sequence of events:**

1. **Short positions accumulate:** Large institutional hedge funds (notably Melvin Capital and Citron Research) identified GameStop as fundamentally overvalued and built massive **short positions** — borrowing and selling GME shares, expecting to buy them back cheaper later. At the peak, **over 140% of GameStop's float** was in short positions (more shares were sold short than physically existed, made possible by chains of share lending).

2. **Reddit's WallStreetBets:** Members of the r/WallStreetBets community on Reddit noticed the extraordinary short interest and coordinated a mass buying campaign — not based on fundamental analysis, but specifically to cause a short squeeze. They also bought **call options**, amplifying buying pressure.

3. **The short squeeze:** As GME's price rose from ~$20 to **$360+ per share**, the hedge funds' short positions turned deeply underwater. Brokers enforced **margin requirements** — minimum collateral short-sellers must maintain. Unable to post sufficient collateral, funds were **forced to buy back shares** (cover their shorts), which pushed the price higher, triggering more forced covering — a classic feedback loop.

4. **Platform intervention:** Robinhood (a retail trading app whose business model involved selling order flow data to hedge funds — a conflict of interest) **suspended buying of GME shares** at the height of the squeeze, effectively shutting down one side of the market. This caused outrage among retail traders and accusations of market manipulation.

5. **The aftermath:** Melvin Capital suffered losses requiring a $2.75 billion bailout by Citadel and Point72. GameStop's price eventually collapsed back toward fundamental value (~$10–40), but the company used the period to raise equity capital and pivot its business.

---

## Key Financial Concepts

### 1. Short Position & Short Selling

```
Mechanics of a short sale:
  1. Borrow shares from a broker (for a fee)
  2. Sell borrowed shares at current market price P₀
  3. Wait for price to fall
  4. Buy back shares at lower price P₁ < P₀
  5. Return shares to broker
  Profit = P₀ − P₁ − borrowing fee

Maximum gain: limited to P₀ (stock cannot go below zero)
Maximum loss: UNLIMITED (stock price can rise without bound)
```

**Asymmetric risk:** This is the opposite of a long position. A long position has limited downside (you can lose at most what you paid) and unlimited upside. A short has limited upside and unlimited downside — this is why short squeezes are so devastating.

### 2. Short Squeeze Mechanics

```
Sequence:
Price rises → short-sellers face mounting losses
           → margin calls: "post more collateral or close position"
           → forced buying to cover shorts
           → buying pressure drives price even higher
           → more margin calls → more forced buying
           → self-reinforcing spiral
```

### 3. Margin Requirements

```
Margin requirement = minimum equity the short-seller must maintain as % of short position value

Example: 50% margin requirement, short 100 shares at $20 = short value $2,000
→ Must maintain $1,000 equity (collateral)

If price rises to $40: short value = $4,000
→ Must maintain $2,000 collateral
→ Must immediately post additional $1,000 or close position
```

### 4. Efficient Market Hypothesis (EMH) — Challenged by GameStop

```
Weak form EMH:    prices reflect all historical price information
Semi-strong EMH:  prices reflect all public information
Strong form EMH:  prices reflect all information including private
```

**GameStop's challenge to EMH:**
- Price surged from $20 to $480 in days — **no change in GameStop's fundamental value** occurred.
- The move was driven entirely by social media coordination, options mechanics, and short squeeze dynamics.
- This is strong evidence of **market inefficiency** — prices diverged massively from fundamental value.
- The episode supports **behavioral finance** explanations: herding, FOMO (fear of missing out), and social contagion rather than rational valuation.
- However, prices eventually reverted — consistent with weak-form efficiency in the **long run**.

---

## Which Chapters Does This Case Link To?

| Chapter | Connection |
|---------|------------|
| **CH4 — Stocks** | Stock valuation (was GME overvalued?), short selling as a "put" on overvalued stocks, market efficiency context |
| **CH10 — Market Efficiency (EMH)** | Direct challenge to all three forms of EMH; behavioral finance alternative; adaptive market hypothesis |
| **CH10 — Financial Options** | Retail traders used call options; short positions are economically similar to writing call options; asymmetric payoffs |
| **CH10 — Capita Selecta (Real Options)** | Hedge funds' exit strategy = real option to cut losses; Robinhood platform intervention |

---

## How Can This Case Appear on the Exam?

### Theory Questions (No Calculation)

**Q: Describe the GameStop story using the terms: short position, short squeeze, margin requirements.**

> GameStop was a struggling video game retailer whose shares were heavily shorted by hedge funds (borrowing shares and selling them, expecting the price to fall). Reddit's WallStreetBets community coordinated a mass buying campaign, driving the price from ~$20 to $360+. As the price surged, short-sellers faced escalating losses and were hit with margin requirements — forced by their brokers to post additional collateral or close their positions. Closing short positions required buying back shares, which further drove up the price in a self-reinforcing short squeeze. Hedge fund Melvin Capital lost billions and required a $2.75B bailout.

**Q: What is the academic/EMH implication of the GameStop story?**

> The Efficient Market Hypothesis claims that stock prices always reflect fundamental information. GameStop's price surge was entirely disconnected from any change in the company's fundamental value — it was driven by social media coordination, options mechanics, and forced covering. This is direct evidence of **temporary market inefficiency**: prices deviated massively and persistently from intrinsic value. It supports behavioral finance (herding, FOMO), the adaptive market hypothesis (markets are shaped by evolutionary forces including social media), and raises questions about the semi-strong form of EMH. However, the eventual price reversal is consistent with the long-run tendency for prices to correct mispricings.

**Q: Why is a short position fundamentally different from a long position in terms of risk/return?**

> A **long position** (buying shares) has a maximum loss equal to the amount invested (stock can fall to zero, no lower) and theoretically unlimited upside. A **short position** has the opposite: maximum gain is limited (the stock can only fall to zero, limiting profit) while the downside is theoretically **unlimited** — there is no ceiling to how high the stock can rise, meaning losses on a short position can exceed the initial investment by many multiples. The asymmetry of short positions makes them inherently riskier, which is why short squeezes are so catastrophic for the short-sellers.

**Q: Explain the role of Robinhood in the GameStop story. Does this support or challenge EMH?**

> Robinhood's business model involves selling retail investors' order-flow data to market makers and institutional clients — including the very hedge funds that were short GameStop. At the height of the squeeze, Robinhood suspended the ability to **buy** (but not sell) GME shares, claiming liquidity concerns. Critics argued this constituted market manipulation: artificially removing buying pressure to benefit the institutional clients whose order data Robinhood sold. This further challenges EMH's assumption of a level playing field — if some participants can influence market microstructure, prices cannot be fully informationally efficient.

**Q: What does the GameStop story reveal about the assumptions of the CAPM model?**

> CAPM assumes rational investors, no transaction costs, and informationally efficient markets. GameStop violated all three: retail investors acted irrationally (buying a stock with deteriorating fundamentals purely to squeeze short-sellers), transaction costs existed (margin requirements, borrowing fees), and markets were clearly inefficient (price ≠ fundamental value for extended periods). Additionally, the extreme non-normal return distribution (discontinuous jumps, fat tails) violates CAPM's assumption of normally distributed returns, making beta and expected return calculations meaningless in this context.

**Q: Explain how options (call options) were used by retail traders in GameStop and what effect this had.**

> Retail traders bought large quantities of GME **call options** (right to buy at a fixed strike price). When options are purchased, the option writer (typically a market maker) must **delta-hedge** by buying the underlying shares to remain hedged. As more calls were purchased, market makers bought more GME shares, amplifying buying pressure. Additionally, as the stock price rose above strike prices, options became deeper in-the-money, requiring market makers to buy even more shares (gamma squeeze). The options market thus created a mechanical feedback loop that turbo-charged the underlying short squeeze.

---

### Exam Tips for ACTUA 3

- **Three key terms** (short position, short squeeze, margin requirements) are always tested — know each precisely.
- **EMH link** is always there: identify which form(s) are violated and which alternative theory applies.
- The **asymmetric risk** of short vs. long positions connects to **financial options** (CH10): a short sale has a payoff similar to writing a call option.
- The **behavioral finance** angle: herding, social contagion, FOMO — connect to CH10 and the "alternative theories" to EMH.
- Robinhood's conflict of interest is a real-world example of **market manipulation** and market microstructure issues that compromise market efficiency.
- The **eventual price reversal** is important: it shows markets are not permanently inefficient — they tend to correct in the long run.

---

---

# ACTUA 4 — Gu & Lev (2011): Overpriced Shares, Ill-Advised Acquisitions, and Goodwill Impairment

## What is this case about?

This is an **academic paper** published in *The Accounting Review* (a top accounting journal) by Feng Gu (University at Buffalo) and Baruch Lev (New York University). It investigates a common pattern in corporate acquisitions using a sample of 54,218 US firm-year observations from 1990–2006.

---

## The Core Thesis

**The root cause of goodwill write-offs is the acquirer's overpriced shares at the time of acquisition.**

```
CHAIN OF EVENTS:

1. Company's shares are overpriced
       ↓
2. Managers use overpriced shares as "currency" to acquire other companies
       ↓
3. They often overpay (price > synergies) → creates goodwill on balance sheet
       ↓
4. Synergies fail to materialise (or were never real)
       ↓
5. Goodwill must be written off → massive impairment charge
       ↓
6. Shareholder lawsuits, stock price collapse, CEO turnover
```

---

## Key Concepts Defined

### 1. Share Overpricing
A firm's shares trade above their **fundamental (intrinsic) value**. The authors measure overpricing using three proxies:
- **Industry-adjusted P/E ratio**: Is the firm's P/E much higher than its industry peers?
- **Discretionary accruals**: Are earnings inflated by accounting choices?
- **Net equity issuance**: Did the firm recently issue equity (a signal it believes shares are overvalued)?

These are combined into two composite overpricing indicators (OVE1, OVE2).

### 2. Goodwill
```
Goodwill = Acquisition price − Fair value of net acquired assets

Example:
  Acquisition price paid          = €500M
  Fair value of acquired assets   = €300M
  Goodwill recorded               = €200M
```
Goodwill represents the premium paid for intangibles: brand, synergies, customer relationships. It sits on the balance sheet and must be tested annually for impairment.

### 3. Goodwill Write-Off (Impairment)
When expected synergies fail to materialise, goodwill must be **written down to its recoverable amount**. This is a large, often non-cash charge that:
- Reduces earnings dramatically
- Signals that the acquisition overpaid
- Often triggers shareholder lawsuits

**Famous examples from the course:**
- eBay–Skype ($2.6B acquisition, $1.43B goodwill write-off)
- AOL–Time Warner ($165B — biggest write-off in history)
- Daimler–Chrysler ($37B)
- HP–Autonomy ($11.7B)
- Microsoft–Nokia ($7.2B)

### 4. The Agency Problem / Managerial Incentives
Why do managers use overpriced shares to make acquisitions even if it destroys value?

```
Key managerial incentives:
  → Short-term focus: acquisitions boost reported revenues & EPS immediately
  → Hubris (Roll 1986): overconfidence in synergy estimates
  → "Empire building": managers derive private benefit from running larger firms
  → Overpriced shares are a "use it before it corrects" opportunity
  → Weak corporate governance: boards don't challenge management
```

---

## Key Empirical Findings of Gu & Lev

1. **Share overpricing → acquisition intensity:** The more overpriced the bidder, the more (and larger) acquisitions it makes.

2. **Share overpricing → goodwill:** Overpriced firms record more goodwill from their acquisitions.

3. **Share overpricing → goodwill write-offs:** The most overpriced firms (highest OVE1 and OVE2) have write-offs of 21.8% of total assets, vs. 2.6% for the least overpriced.

4. **Acquisitions worsen post-acquisition performance:** Firms with overpriced shares that also made acquisitions have measurably **worse** stock returns and accounting ROA in the 3 years after the acquisition — the acquisition makes things worse, not better.

5. **Lawsuit frequency increases with overpricing:** Up to 40% of the most overpriced bidders with write-offs faced shareholder lawsuits.

---

## Which Chapters Does This Case Link To?

| Chapter | Connection |
|---------|------------|
| **CH4 — Stocks** | Stock overvaluation, P/E ratios, PVGO, DCF valuation, why overpriced stocks arise |
| **CH5–6 — Investment Decisions (NPV)** | Acquisitions are investment decisions; NPV of acquisition = PV(synergies) − price paid; goodwill write-off = delayed NPV recognition |
| **CH10 — Market Efficiency** | If markets were fully efficient, overpriced shares wouldn't exist. The study presupposes market inefficiency. |
| **CH10 — Debt Policy / Capital Structure** | Share-financed acquisitions vs. cash; using equity as "currency"; goodwill and balance sheet implications |
| **CH10 — Real Options** | The option to abandon or write off goodwill; management's real options in acquisition decisions |
| **Psychology (CH5)** | Hubris, overconfidence, confirmation bias in making bad acquisitions |

---

## How Can This Case Appear on the Exam?

### Theory Questions (No Calculation)

**Q: Explain the main thesis of Gu & Lev (2011). Use: share overpricing, acquisition with overpriced shares, goodwill, goodwill write-off.**

> Gu & Lev argue that the **root cause** of goodwill write-offs is the acquirer's **share overpricing** at the time of acquisition. When a company's shares are overpriced — trading above fundamental value — managers face a strong incentive to exploit this by using those shares as "currency" to acquire other companies (acquisition with overpriced shares). Because they are effectively paying with inflated shares, they often **overpay**, paying more than the synergies justify. The excess of acquisition price over the fair value of acquired net assets is recorded as **goodwill** on the balance sheet. When the expected synergies fail to materialise (as they frequently do, because the acquisition was ill-advised), **goodwill must be written off** — a large impairment charge that exposes the original overpayment and signals a flawed investment strategy.

**Q: How does a goodwill write-off relate to the NPV concept from the course?**

> An acquisition can be treated as an investment project:
> NPV = PV(expected synergies) − Acquisition price paid
>
> A goodwill write-off is the accounting system's eventual recognition that this NPV was **negative** — the acquisition price exceeded the present value of synergies realised. In other words, the acquisition destroyed, not created, financial value. The write-off is not a benign accounting ritual (as managers often claim); it is evidence of an investment decision with a negative NPV, which is the most fundamental mistake in corporate finance.

**Q: Explain why managerial psychology contributes to bad acquisitions. Link to the course material on investment decisions.**

> The course identifies multiple psychological biases that cause managers to make bad investments (covered in CH5):
> - **Overconfidence / Hubris (Roll 1986):** Managers overestimate synergies and underestimate integration risks. Studies show 57% of CEOs whose acquisitions are flagged as ill-advised were replaced (Lehn & Zhao 2006).
> - **Confirmation bias:** Once committed to an acquisition idea, managers seek information that confirms it and disregard warning signs.
> - **Loss aversion:** Sunk cost fallacy — once goodwill is on the balance sheet, managers delay writing it off, prolonging the misallocation of resources.
> - **Empire building:** Managers derive private benefits from running a larger firm, creating incentive to acquire even when NPV < 0.
> - **Short-termism (Stein 1996):** Acquisitions immediately boost reported revenues and EPS, making the overpriced shares appear justified — a self-fulfilling short-term narrative.

**Q: How does PVGO connect to the concept of share overpricing in Gu & Lev?**

> From the course (CH4), a stock's price consists of:
> P₀ = EPS/r + PVGO
>
> A company with an inflated stock price often has an inflated PVGO — the market assigns excessive value to future growth opportunities that may not exist. Managers, aware of this overvaluation, use the window of opportunity to acquire other companies (paying in overpriced shares) to justify and extend the high valuation narrative — showing acquisitive "growth" to the market. When these acquisitions fail to generate the implied returns, PVGO collapses and the share price corrects. The goodwill write-off crystallises this collapse in book-value terms.

**Q: Why is it especially damaging when acquisitions are financed with overpriced shares (vs. cash)?**

> Several reasons:
> 1. **The acquirer pays more than it appears**: overpriced shares are worth less than their market price in fundamental terms, so the target's shareholders receive an implicit overpayment.
> 2. **No market discipline**: cash acquisitions require capital market access and discipline; share-for-share deals are self-financing with inflated equity.
> 3. **Target shareholders become acquirer shareholders**: they often hold on (path of least resistance), diluting the existing shareholder base and sharing in the post-acquisition underperformance.
> 4. **Goodwill is larger**: higher acquisition price (paid in overpriced shares) → more goodwill → larger potential write-off.
> 5. **Subsequent returns are worse**: Gu & Lev find that overpriced acquirers have measurably lower stock returns AND lower ROA in the 3 years post-acquisition — the deal makes things worse than not acquiring at all.

**Q: Is a goodwill write-off just a benign "accounting event"? Argue both sides.**

> **Managers' view (benign accounting event):** Goodwill write-offs simply reflect the natural correction of overvalued shares used as acquisition currency. As the acquirer's shares revert to fair value, the goodwill naturally must be reduced. It has no economic substance — no cash leaves the company. The CFO of JDS Uniphase (after a $44.8B write-off): "Had these transactions been done at times when valuations were lower, the goodwill amounts would have been considerably smaller."
>
> **Gu & Lev's view (important signal of flawed strategy):** Write-offs are NOT benign. The empirical evidence shows that firms making acquisitions with overpriced shares have substantially **worse post-acquisition performance** than they would have had without the acquisition. The write-off is not just reversing overpriced shares — it signals genuine value destruction from ill-advised acquisitions. The lawsuit frequency (up to 40%) confirms that shareholders themselves view these as costly strategic mistakes, not routine accounting adjustments.

---

### Connecting to Exam MC/Calculation Questions

**Q: Company Alpha has shares trading at €50. EPS = €2.50, cost of equity = 8%, ROE = 12%, payout ratio = 40%.**

1. Calculate the stock price using the DDM.
2. Is the stock overpriced? By how much?
3. If Alpha acquires Beta for €200M and Beta's net assets are fairly valued at €120M, what is the goodwill recorded?

```
Step 1 — DDM:
g = ROE × plowback = 12% × 60% = 7.2%
Div₁ = EPS × payout = 2.50 × 0.40 = €1.00
P_DDM = 1.00 / (0.08 − 0.072) = 1.00 / 0.008 = €125.00

Wait, that gives P=125, but market is €50. Actually market < fair value here, so stock is
underpriced. Let me adjust: if g=4%, P = 1.00/(0.08-0.04) = 25. Still below €50.

Let me adjust: g = 12% × 70% = 8.4% (payout 30%, plowback 70%)
Div1 = 2.50 × 0.30 = 0.75
P_DDM = 0.75/(0.08-0.084) → negative! g>r means formula doesn't apply.

Better example: EPS=€3, payout=50%, ROE=10%, r=9%
g = 10%×50% = 5%
Div1 = 1.50
P_DDM = 1.50/(0.09-0.05) = 1.50/0.04 = €37.50

If market price = €50 → overpriced by €50 - €37.50 = €12.50
PVGO_actual = 50 - 3/0.09 = 50 - 33.33 = €16.67 (market-implied)
PVGO_warranted = 37.50 - 33.33 = €4.17 (what growth actually justifies)
Overpricing = €12.50 (market assigns €12.50 more PVGO than justified)
```

This connects overpricing to PVGO and DDM calculation.

---

### Exam Tips for ACTUA 4

- Always trace the **full causal chain**: overpriced shares → acquisition → goodwill → write-off → value destruction.
- Know the **distinction between benign and non-benign interpretations** of goodwill write-offs — the exam often asks you to argue both sides.
- **Psychological biases** (hubris, overconfidence, empire-building, short-termism) are directly connectable to CH5 bad investment decisions content.
- **PVGO connection** is rich: overpriced stocks have inflated PVGO → managers make acquisitions to justify it → acquisitions fail → PVGO collapses.
- **NPV framing**: always state that goodwill write-off = delayed recognition of negative-NPV investment.
- **Corporate governance**: the paper shows that weaker governance amplifies the overpricing-acquisition link. Good boards restrain managers.

---

---

# CROSS-CASE CONNECTIONS & EXAM STRATEGY

## How the ACTUA Cases Connect to Each Other

| Link | ACTUA Cases | Key Concept |
|------|-------------|-------------|
| Market efficiency challenged | ACTUA 2, 3, 4 | EMH assumes prices reflect value; Van Peteghem bond shows bank pricing inefficiency; GameStop = behavioral market failure; Gu & Lev = stock overpricing is systematic |
| Time value of money | ACTUA 1, 2 | Pension reform and bond valuation both depend critically on discounting future cash flows |
| Behavioral finance | ACTUA 3, 4 | GameStop = herding/FOMO; Gu & Lev = hubris/overconfidence in M&A |
| NPV / investment decision | ACTUA 1, 4 | Pension scheme as a personal NPV problem; acquisitions as corporate NPV problems |
| Government / policy intervention | ACTUA 1, 2 | Pension reform = government as guarantor; Van Peteghem bond = government as competitor to banks |
| Asymmetric payoffs | ACTUA 3 | Short position's unlimited downside mirrors writing an option; connects to CH10 options |

---

## Summary: What to Know for Each ACTUA Case

### ACTUA 1 — Pension Reform
- **Know:** 3 uncertainty factors (t, z, r) and their direction; break-even formula; annuity + TVM logic
- **Calculate:** FV of alternative at retirement vs. PV of pension annuity; two-step annuity + growing perpetuity
- **Connect to:** CH3 (TVM), CH5–6 (NPV/break-even), CH9 (opportunity cost)

### ACTUA 2 — Van Peteghem Bond
- **Know:** The story (2023 success, 2024 failure and why); yield curve (normal vs. inverted); monetary policy timeline; after-tax yield formula
- **Calculate:** Bond price with tax-adjusted coupons; YTM; duration and volatility
- **Connect to:** CH3 (all bond topics), CH10 (market efficiency, monetary policy)

### ACTUA 3 — GameStop
- **Know:** Short selling mechanics; short squeeze; margin requirements; EMH challenge; behavioral finance; options amplification
- **Calculate:** (Usually theoretical, but may involve short-selling P&L, option payoffs)
- **Connect to:** CH4 (stock valuation), CH10 (EMH, financial options, behavioral finance)

### ACTUA 4 — Gu & Lev (2011)
- **Know:** The full causal chain; goodwill definition and write-off; distinction benign vs. non-benign; managerial incentives; psychological biases
- **Calculate:** May involve DDM/PVGO to identify overpricing; NPV of acquisition
- **Connect to:** CH4 (stocks, PVGO), CH5–6 (NPV, bad investments, psychology), CH10 (EMH, capital structure)

---

*End of ACTUA Study Guide.*
