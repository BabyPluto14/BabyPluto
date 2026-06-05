# Corporate Finance — Illustrated Exam: Full Model Answers
### With Course Formulas & TI-84 Plus Instructions

---

## QUESTION TYPE 1 — Multiple Choice

---

### MC Q1 — Inflation-Linked Financial Product

**Question:** A product pays €50 at the **beginning of each quarter** for 3 years (first payment immediately). Afterwards, payments grow at **0.5%/quarter** (inflation). Real annual interest rate = 10%. What is the price today?

**Answer: d. €2,550.93**

---

#### Course Formulas Used

**Converting annual rate to periodic rate (compounding):**

    (1 + r_annual) = (1 + r_periodic)^m
    →  r_quarterly = (1 + r_annual)^(1/m) − 1

**Present Value of an Annuity-Due** (payments at beginning of period):

    PV_annuity-due = PMT × [1 − (1 + r)^(−n)] / r  ×  (1 + r)

**Present Value of a Growing Perpetuity** (first payment C₁ at t=1):

    PV = C₁ / (r − g)

---

#### Step-by-Step Solution

**Step 1 — Real quarterly discount rate:**

    r_quarterly = (1.10)^(1/4) − 1 = 1.02411 − 1 = 2.411%

> Shortcut: (1.02411)^4 = 1.10, so (1.02411)^12 = (1.10)^3 = 1.331

**Step 2 — Phase 1: PV of annuity-due (12 payments of €50):**

    PV₁ = 50 × [1 − (1.02411)^(−12)] / 0.02411  ×  (1.02411)
        = 50 × [1 − 1/1.331] / 0.02411  ×  1.02411
        = 50 × [0.2487 / 0.02411]  ×  1.02411
        = 50 × 10.313 × 1.02411
        = €528.09

**Step 3 — Phase 2: PV of growing perpetuity (starting t = 12)**

The first growing payment at t=12 is C₁₂ = 50 × 1.005 = €50.25.
The growing perpetuity formula gives PV one period before the first payment, i.e. at t = 11:

    PV at t=11 = C₁₂ / (r − g)
               = (50 × 1.005) / (0.02411 − 0.005)
               = 50.25 / 0.01911
               = €2,629.01

Discount back 11 quarters to t = 0:

    PV₂ = 2,629.01 / (1.02411)^11
        = 2,629.01 / (1.331 / 1.02411)
        = 2,629.01 / 1.3001
        = €2,022.84

**Step 4 — Total price:**

    Price = PV₁ + PV₂ = 528.09 + 2,022.84 = €2,550.93  ✓

---

#### TI-84 Plus

**Phase 1 (annuity-due):** `2nd` → `FINANCE` → `TVM Solver`
Set: N=12 | I%=2.411 | PMT=50 | FV=0 | P/Y=1
Switch to BEGIN mode: `2nd` → `BGN` → `2nd` → `SET`
Cursor to PV → `ALPHA` → `SOLVE` → **PV = 528.09**

**Phase 2:** Enter directly:
`50 × 1.005 ÷ (0.02411 − 0.005)` → store result
Then `÷ 1.02411^11` → **2022.84**
Add: `528.09 + 2022.84` → **€2,550.93**

---

### MC Q2 — Macaulay Duration

**Question:** 2-year bond, YTM = 3%, coupon = 5% annually, redeemed at par. Macaulay duration?

**Answer: d. 1.95 years**

---

#### Course Formula Used

**Macaulay Duration** — weighted average time to receive the bond's cash flows (in PV terms):

    Duration = Σ [ t × PV(CF_t) ] / Bond Price

where:

    PV(CF_t) = CF_t / (1 + YTM)^t

    Bond Price = Σ PV(CF_t) = Σ CF_t / (1 + YTM)^t

---

#### Step-by-Step Solution

Assume par value = €100.

**Bond cash flows:**

    t = 1:  CF₁ = coupon = €5
    t = 2:  CF₂ = coupon + par = 5 + 100 = €105

**Step 1 — PV of each cash flow:**

    PV(CF₁) = 5 / (1.03)¹ = 5 / 1.03       = €4.854
    PV(CF₂) = 105 / (1.03)² = 105 / 1.0609  = €98.973

**Step 2 — Bond Price:**

    Bond Price = 4.854 + 98.973 = €103.827

> The bond trades above par (coupon 5% > YTM 3%) — makes sense.

**Step 3 — Macaulay Duration:**

    Duration = (1 × 4.854  +  2 × 98.973) / 103.827
             = (4.854 + 197.946) / 103.827
             = 202.800 / 103.827
             = 1.953 ≈ 1.95 years  ✓

> Duration < Maturity (2 years) because the bond pays coupons before maturity, pulling the weighted average time forward.

---

#### TI-84 Plus

**Bond price:** TVM Solver: N=2 | I%=3 | PMT=5 | FV=100 → Solve PV → **103.827**

**Duration:**
`5 ÷ 1.03` → 4.854
`105 ÷ 1.03^2` → 98.973
`(1 × 4.854 + 2 × 98.973) ÷ 103.827` → **1.953 years**

---

### MC Q3 — DDM — Company Z

**Question:** 2M shares, net profit = €3.6M, payout = 35%, ROE = 12%, cost of equity = 10%. Expected share value?

**Answer: b. €31.50**

---

#### Course Formulas Used

**Earnings Per Share:**

    EPS = Net Profit / Number of Shares

**Dividend growth rate (Gordon-Shapiro):**

    g = ROE × Plowback ratio
    Plowback ratio = 1 − Payout ratio

**Constant Growth DDM (Gordon-Shapiro model):**

    P₀ = Div₁ / (r − g)

where Div₁ is the next dividend and r is the cost of equity.

---

#### Step-by-Step Solution

**Step 1 — EPS:**

    EPS = €3,600,000 / 2,000,000 shares = €1.80

**Step 2 — Dividend (Div₁):**

    Div₁ = Payout ratio × EPS = 35% × €1.80 = €0.63

**Step 3 — Growth rate:**

    Plowback ratio = 1 − 0.35 = 0.65
    g = ROE × Plowback = 12% × 65% = 7.8% ≈ 8%

> The exam rounds g to 8% — a standard simplification used in the course.

**Step 4 — Share price:**

    P₀ = Div₁ / (r − g)
       = 0.63 / (0.10 − 0.08)
       = 0.63 / 0.02
       = €31.50  ✓

---

#### TI-84 Plus

`0.63 ÷ (0.10 − 0.08)` → **€31.50**

---

### MC Q4 — Sharpe Ratio of Portfolio

**Question:** Portfolio A (w=35%, E(R)=12%, σ=15%) + B (w=65%, E(R)=15%, σ=20%), ρ=0.6, rf=0.25%. Sharpe ratio?

**Answer: b. 0.82**

---

#### Course Formulas Used

**Expected return of a portfolio:**

    E(Rp) = Σ wᵢ × E(Rᵢ)  =  wA × E(RA) + wB × E(RB)

**Variance of a 2-asset portfolio:**

    σ²p = wA² × σA²  +  wB² × σB²  +  2 × wA × wB × ρ(A,B) × σA × σB

**Standard deviation of portfolio:**

    σp = √σ²p

**Sharpe Ratio:**

    Sharpe = [E(Rp) − rf] / σp

---

#### Step-by-Step Solution

**Step 1 — Expected portfolio return:**

    E(Rp) = 0.35 × 12% + 0.65 × 15%
           = 4.20% + 9.75%
           = 13.95%

**Step 2 — Portfolio variance:**

    σ²p = (0.35)² × (0.15)²  +  (0.65)² × (0.20)²  +  2 × 0.35 × 0.65 × 0.6 × 0.15 × 0.20

    Term 1: 0.1225 × 0.0225  = 0.002756
    Term 2: 0.4225 × 0.0400  = 0.016900
    Term 3: 2 × 0.35 × 0.65 × 0.6 × 0.03  = 0.008190

    σ²p = 0.002756 + 0.016900 + 0.008190 = 0.027846

**Step 3 — Portfolio standard deviation:**

    σp = √0.027846 = 16.687%

**Step 4 — Sharpe ratio:**

    Sharpe = (13.95% − 0.25%) / 16.687%
           = 13.70% / 16.687%
           = 0.821 ≈ 0.82  ✓

---

#### TI-84 Plus

`0.35^2 × 0.15^2 + 0.65^2 × 0.20^2 + 2 × 0.35 × 0.65 × 0.6 × 0.15 × 0.20` → 0.027846
`2nd` → `√` → `0.027846` → **0.16687**
`(0.1395 − 0.0025) ÷ 0.16687` → **0.821**

---

### MC Q5 — Portfolio Risk (Variance)

**Question:** Portfolio A (w=35%, E(R)=15%, σ=20%) + B (w=65%, E(R)=18%, σ=22%), ρ=0.7. Which best quantifies portfolio risk?

**Answer: c. variance = 3.936%**

---

#### Course Formula Used

**Variance of a 2-asset portfolio:**

    σ²p = wA² × σA²  +  wB² × σB²  +  2 × wA × wB × ρ(A,B) × σA × σB

---

#### Step-by-Step Solution

    σ²p = (0.35)² × (0.20)²  +  (0.65)² × (0.22)²  +  2 × 0.35 × 0.65 × 0.7 × 0.20 × 0.22

    Term 1: 0.1225 × 0.0400  = 0.004900
    Term 2: 0.4225 × 0.0484  = 0.020449
    Term 3: 2 × 0.35 × 0.65 × 0.7 × 0.044  = 0.014014

    σ²p = 0.004900 + 0.020449 + 0.014014 = 0.039363

    Expressed as percentage: 0.039363 × 100 = 3.936%  ✓
    σp = √0.039363 = 19.84%

> The exam expresses variance in percentage terms. Options a/b give wrong standard deviation values; option d gives wrong variance. Only option c is correct.

---

#### TI-84 Plus

`0.35^2 × 0.20^2 + 0.65^2 × 0.22^2 + 2 × 0.35 × 0.65 × 0.7 × 0.20 × 0.22` → **0.039363 = 3.936%**

---

## QUESTION TYPE 2 — Short Conceptual Questions

---

### Q2.1 — Itsme Acquiring NextAuth: Financial Valuation

**How should the acquisition price be determined?**

The acquisition should be framed as a **financial valuation problem**, and CH0 of the course gives a precise framework for approaching any such problem through three questions: *who is valuing, what cash flows will they receive, and at what discount rate?*

**Who is valuing?** Itsme, as the acquirer, must estimate the maximum price it would rationally be willing to pay — not what NextAuth is worth to its current owners, but what it is worth *to Itsme*.

**Which cash flows?** The course defines financial value as the **sum of discounted future cash flows**. Itsme must forecast all **Free Cash Flows (FCF)** NextAuth will generate over an explicit horizon, plus a **terminal (going-concern) value** beyond that horizon — estimated as a growing perpetuity:

    TV = FCF_(n+1) / (WACC − g_long-run)

Critically, Itsme must also quantify **synergies** — the additional cash flows that only arise *because* Itsme owns NextAuth (cost savings, combined technology, new revenue streams). These are part of the value Itsme captures but NextAuth cannot create alone. The maximum rational acquisition price therefore equals:

    Max price = Standalone DCF value of NextAuth + PV of synergies

**At what discount rate?** The cash flows must be discounted at NextAuth's **WACC** — reflecting *NextAuth's* risk profile, not Itsme's. A riskier target implies a higher discount rate, which mechanically reduces its present value.

The deeper insight from CH0 is that **financial value ≠ price**. The final negotiated price depends on investor disagreement — what Itsme believes NextAuth is worth versus what NextAuth's owners believe. If Itsme pays less than its estimated value, the acquisition creates value. If it overpays — even for a fundamentally strong company — it destroys shareholder value.

---

### Q2.2 — Present Value of Growth Opportunities (PVGO)

**What is PVGO, why does it arise, how to estimate it?**

The deepest insight here is that a stock price is not one thing — it is the sum of **two fundamentally different claims** that investors are buying simultaneously:

    P₀ = EPS / r  +  PVGO
         ─────────    ──────
         Value as a   Value of future
         zero-growth  reinvestment
         perpetuity   opportunities

The first term, EPS/r, is what the company would be worth if it paid out *all* earnings as dividends forever and never grew. It is a bond-like perpetuity based on current earnings power. The second term, **PVGO**, is what investors pay *on top of that* because they expect the company to reinvest earnings profitably in the future — it is essentially a **real option on future investment**.

**Why PVGOs arise — the critical condition:**
PVGO is only positive when the firm can invest retained earnings at a **return on equity (ROE) that exceeds the cost of equity (r)**. This is the condition `ROE > r`. When this holds, each euro retained and reinvested creates *more* than one euro of value, so retaining earnings is preferable to paying them out. When `ROE = r`, retention adds no value (PVGO = 0). When `ROE < r`, the firm is destroying value by retaining — a negative PVGO — and shareholders would be better off receiving the earnings as dividends to reinvest themselves elsewhere.

This means PVGO is fundamentally a signal of **managerial reinvestment quality**: high PVGO firms are those the market believes will continue finding projects that beat the cost of capital.

**How to estimate:**

    PVGO = P₀  −  EPS / r

where P₀ is the market price (observed or via Gordon-Shapiro DDM), EPS/r is the no-growth benchmark, and r is the cost of equity.

---

### Q2.3 — Three Main Drivers of Bond Volatility

**Bond volatility (modified duration)** = the percentage change in bond price for a 1 percentage-point change in YTM:

    Volatility (%) = Modified Duration = Macaulay Duration / (1 + YTM)

All three drivers reduce to **one unifying mechanism**: they all change how *back-loaded* a bond's cash flows are — i.e., how much of the bond's total value is concentrated in distant future payments. The further cash flows lie in the future, the more sensitive they are to interest rate changes, because they are divided by (1+r)^t where t is large. A small change in r gets amplified by compounding over many periods.

**1. Coupon Rate → inverse relationship with volatility**
A lower coupon bond is more back-loaded: less cash arrives early (via coupons), so proportionally more of the bond's value comes from the final principal repayment far in the future. That distant cash flow is highly rate-sensitive. Extreme case: a **zero-coupon bond** has *all* its cash at maturity — maximum back-loading, maximum volatility for a given maturity.

**2. Time to Maturity → positive relationship with volatility**
A longer maturity pushes all cash flows — especially the principal — further into the future. The compounding effect in (1+r)^t grows with t, so rate changes have an exponentially larger effect on distant flows than near-term ones. Longer bonds are therefore inherently more rate-sensitive.

**3. YTM Level → inverse relationship with volatility**
At lower yield levels, the discount factors (1+r)^t are smaller, giving distant cash flows a relatively larger weight in the bond's price. A given change in YTM then moves those heavily-weighted distant flows more in PV terms, producing a bigger overall price swing. This is also why bond price-yield relationship is **convex**: at low yields, the same rate change causes a larger price impact than at high yields.

---

### Q2.4 — Capital Market Line (CML) vs. Securities Market Line (SML)

The two equations from the course:

    CML:  E(Rp) = rf  +  [(E(Rm) − rf) / σm]  ×  σp

    SML:  E(Ri) = rf  +  βᵢ  ×  [E(Rm) − rf]

**The essence of both lines is the same fundamental principle: you are only compensated for risk you cannot avoid.**

Both the CML and SML express expected return as the **risk-free rate** (r_f) plus a **risk premium** — a reward for bearing risk. The critical question both equations answer is: *which risk deserves a premium?*

**The essence of the CML** — for fully diversified portfolios under **Modern Portfolio Theory**: an investor who holds the **market portfolio** (the optimal risky portfolio) has already eliminated all **unsystematic (idiosyncratic) risk** through diversification. What remains is total risk (σ), which at this point is entirely systematic. The slope of the CML — (E(Rm)−rf)/σm — is the **market Sharpe ratio**, the going rate of compensation per unit of total portfolio risk. Any rational investor should position themselves *on* this line, not below it.

**The essence of the SML** — the core insight of **CAPM**: when extended to individual securities, total risk is no longer the right measure, because part of it (idiosyncratic risk) can be diversified away for free. The market therefore only prices the part that *cannot* be avoided — **beta (β)**, the measure of an asset's **systematic risk** relative to the market. The term β_i(E(Rm)−rf) is the **equity risk premium**, scaled by the asset's sensitivity to market-wide movements. Investors receive no compensation for firm-specific risk because rational, diversified investors have already eliminated it.

**The connection:** The CML is a special case of the SML — valid only for efficient, fully diversified portfolios where total risk equals systematic risk. The SML is universal, applying to any asset by isolating the only component of risk that survives in a rational investor's portfolio. A security plotting above the SML offers a return *above* what its beta justifies — it is underpriced (**buy**); below the SML, it is overpriced (**sell**).

---

### Q2.5 — Diversification

**The core insight: diversification is a free lunch — you reduce risk without sacrificing expected return.**

When you combine assets in a portfolio, expected returns add up linearly (they are additive by weight), but risks *partially cancel out* rather than adding up. This is because firm-specific shocks are uncorrelated across companies — when one firm has a bad quarter due to a management scandal, another firm's product launch is unaffected. These events wash out in a large portfolio. The variance formula makes this visible:

    σ²p = wA² × σA²  +  wB² × σB²  +  2 × wA × wB × ρ(A,B) × σA × σB

When ρ < 1, the cross-term shrinks, making portfolio risk strictly lower than the weighted average of individual risks — without any reduction in expected return. The lower the correlation, the more powerful the diversification effect. At the theoretical extreme of ρ = −1, all risk can be eliminated.

**What can and cannot be eliminated:**

Diversification eliminates **unsystematic (idiosyncratic / firm-specific) risk** — shocks unique to a company (product recalls, lawsuits, management changes). These are uncorrelated across firms, so they cancel out as the portfolio grows.

What *cannot* be eliminated is **systematic (market / non-diversifiable) risk** — shocks that affect *all* assets simultaneously: recessions, interest rate changes, inflation, geopolitical crises. There is no second asset to offset these with, because everything moves in the same direction. No matter how many stocks you hold, you cannot diversify away a global recession.

This is why **beta, not total standard deviation, is the correct measure of risk for pricing purposes** (per the SML): it captures only the irreducible, non-diversifiable component of risk — the only part that rational investors are actually exposed to and must therefore be compensated for.

---

## QUESTION TYPE 3 — Large Quantitative Exercise (SRB)

**Financial data given:**

| Item | Value |
|------|-------|
| Outstanding shares | 5,000,000 |
| Book value / share | €7 |
| Market value / share | €8 |
| Market value of debt | €60,000,000 |
| Cost of debt (rd) | 7% |
| Tax rate (t) | 30% |
| Cov(SRB returns, market returns) | 0.04 |
| Expected market return (Rm) | 9% |
| Std dev of market return (σm) | 14% |
| Risk-free rate — ST gov. bond (rf) | 5% |

---

### Part a — Estimate SRB's Cost of Capital (WACC)

WACC is SRB's **opportunity cost of capital** — the minimum return the company must earn on any investment to create value for its investors. It is the correct discount rate for evaluating investment projects.

---

#### Course Formulas Used

**Beta (systematic risk of SRB's equity):**

    β = Cov(Rᵢ, Rm) / Var(Rm) = Cov(Rᵢ, Rm) / σ²m

**Cost of Equity via CAPM / Securities Market Line:**

    COE = re = rf  +  β × (E(Rm) − rf)

**WACC (Weighted Average Cost of Capital):**

    WACC = (E / (D+E)) × re  +  (D / (D+E)) × rd × (1 − t)

> Always use **market values** for weights, not book values.

---

#### Step-by-Step Solution

**Step 1 — Beta:**

    β = Cov(SRB, market) / σ²m
      = 0.04 / (0.14)²
      = 0.04 / 0.0196
      = 2.041

> β = 2.041 means SRB's returns move approximately twice as much as the market — a high-risk, highly sensitive stock.

**Step 2 — Cost of Equity (COE) via CAPM:**

    re = rf + β × (E(Rm) − rf)
       = 5% + 2.041 × (9% − 5%)
       = 5% + 2.041 × 4%
       = 5% + 8.163%
       = 13.163%

> Shareholders of SRB require a 13.16% annual return to be compensated for the systematic risk they bear. This is the return demanded per the SML.

**Step 3 — Market Value Weights:**

    E = 5,000,000 shares × €8 = €40,000,000
    D = €60,000,000
    D + E = €100,000,000

    wE = 40 / 100 = 40%
    wD = 60 / 100 = 60%

**Step 4 — WACC:**

    WACC = wE × re  +  wD × rd × (1 − t)
         = 0.40 × 13.163%  +  0.60 × 7% × (1 − 0.30)
         = 5.265%  +  0.60 × 7% × 0.70
         = 5.265%  +  2.940%
         = 8.205%  ≈  8.21%

> The after-tax cost of debt is 7% × 0.70 = 4.90%, because interest payments are tax-deductible, reducing the effective cost of debt to the firm.

> **Role of WACC in investment analysis:** WACC is the hurdle rate for projects. Any project with NPV > 0 when discounted at 8.21% creates financial value for SRB's investors. It reflects what all investors (shareholders and debt-holders) minimally require.

---

#### TI-84 Plus

`0.04 ÷ 0.14^2` → **β = 2.041**
`5 + 2.041 × (9 − 5)` → **COE = 13.163%**
`0.40 × 13.163 + 0.60 × 7 × 0.70` → **WACC = 8.205%**

---

### Part b — Which Proposal? (EAA Method)

**Why EAA and not simply NPV?**

SRB is a **going-concern** company, meaning it will need machinery indefinitely. The two proposals have **different lifespans** (4 vs. 6 years). Comparing NPVs directly would be unfair because the 6-year project simply lasts longer — not because it is necessarily more efficient.

The correct method is the **Equivalent Annual Annuity (EAA)**, which converts each project's NPV into a constant annual value, making both options directly comparable over the same time horizon (assuming identical replacement cycles forever).

---

#### Course Formulas Used

**After-tax Operating Cash Flow (OCF):**

    OCF = (Revenue − Costs − Depreciation) × (1 − t)  +  Depreciation

This can be rewritten to highlight the depreciation tax shield:

    OCF = (Revenue − Costs) × (1 − t)  +  t × Depreciation
                                            ────────────────
                                            Depreciation tax shield

**Straight-line Depreciation:**

    Depreciation = CAPEX / Useful life (years)

**Net Present Value:**

    NPV = −C₀  +  Σ [ OCFt / (1 + r)^t ]
        = −C₀  +  OCF × Annuity factor(r, n)    [when OCF is constant]

**Annuity Factor:**

    Annuity factor(r, n) = [1 − (1 + r)^(−n)] / r

**Equivalent Annual Annuity:**

    EAA = NPV / Annuity factor(r, n)

---

#### Proposal A — CAPEX €400,000, 4-year life

**Depreciation (straight-line):**

    Depreciation = 400,000 / 4 = €100,000 / year

**Annual incremental income statement:**

    Revenue increase              = +€175,000
    Operating cost increase       = − €40,000
    Depreciation                  = −€100,000
    ─────────────────────────────────────────
    EBIT (pre-tax profit)         =  +€35,000
    Tax (30%)                     =  − €10,500
    Net income                    =  +€24,500
    + Add back depreciation       =  +€100,000
    ─────────────────────────────────────────
    Annual after-tax OCF          =  +€124,500

**Verification via formula:**

    OCF = (175,000 − 40,000 − 100,000) × (1 − 0.30) + 100,000
        = 35,000 × 0.70 + 100,000
        = 24,500 + 100,000
        = €124,500  ✓

**NPV of Proposal A:**

    Annuity factor (8.21%, 4 yr) = [1 − (1.0821)^(−4)] / 0.0821 = 3.297

    NPV_A = −400,000 + 124,500 × 3.297
          = −400,000 + 410,487
          = +€10,487

**EAA of Proposal A:**

    EAA_A = NPV_A / Annuity factor = 10,487 / 3.297 = €3,181 / year

---

#### Proposal B — CAPEX €500,000, 6-year life

**Depreciation (straight-line):**

    Depreciation = 500,000 / 6 = €83,333 / year

**Annual incremental income statement:**

    Revenue increase              = +€190,000
    Operating cost increase       = − €40,000
    Maintenance cost              = −  €5,000
    Depreciation                  = − €83,333
    ─────────────────────────────────────────
    EBIT (pre-tax profit)         =  +€61,667
    Tax (30%)                     = − €18,500
    Net income                    =  +€43,167
    + Add back depreciation       =  +€83,333
    ─────────────────────────────────────────
    Annual after-tax OCF          = +€126,500

**Verification via formula:**

    OCF = (190,000 − 40,000 − 5,000 − 83,333) × (1 − 0.30) + 83,333
        = 61,667 × 0.70 + 83,333
        = 43,167 + 83,333
        = €126,500  ✓

**NPV of Proposal B:**

    Annuity factor (8.21%, 6 yr) = [1 − (1.0821)^(−6)] / 0.0821 = 4.594

    NPV_B = −500,000 + 126,500 × 4.594
          = −500,000 + 581,141
          = +€81,141

**EAA of Proposal B:**

    EAA_B = NPV_B / Annuity factor = 81,141 / 4.594 = €17,661 / year

---

#### Decision

| | NPV | EAA (annual value created) |
|---|---|---|
| Proposal A (4 yr) | €10,487 | **€3,181 / year** |
| Proposal B (6 yr) | €81,141 | **€17,661 / year** |

**→ Proposal B is clearly preferred.** Its EAA is ~5.5× higher. Even though Proposal B requires a larger upfront investment, its stronger revenue profile and manageable depreciation produce far more after-tax cash flow per year. On a like-for-like annual basis, Proposal B creates nearly €14,500 more value per year.

---

#### TI-84 Plus

**NPV_A:** `APPS` → `Finance` → `NPV(`
Enter: `NPV(8.21, −400000, {124500, 124500, 124500, 124500})` → **€10,487**

**EAA_A:** TVM Solver: N=4 | I%=8.21 | PV=−10487 | FV=0 → Solve PMT → **€3,181**

**NPV_B:** `NPV(8.21, −500000, {126500, 126500, 126500, 126500, 126500, 126500})` → **€81,141**

**EAA_B:** TVM Solver: N=6 | I%=8.21 | PV=−81141 | FV=0 → Solve PMT → **€17,661**

---

### Part c — Impact of Higher Inventory on Financial Value

**Yes — holding more inventory reduces the financial value generated by the project.**

The key insight is not that money is *lost* — it is that money is *locked up in time*. Higher inventory requires cash to be committed upfront (to purchase and hold stock), which is an **increase in Net Working Capital (NWC)**. In NPV analysis this appears as an immediate cash outflow:

    Cash flow from ΔNWC = −ΔNWC  (increase in NWC = cash outflow)

At the end of the project, that inventory is typically liquidated and the NWC is recovered — so the cash does come back. But this is precisely where **time value of money** creates the damage: the outflow happens at t = 0 (full weight), while the recovery happens at t = n (discounted heavily). The PV of the future recovery is always less than the present outflow. The net effect is a permanent reduction in NPV — not because cash disappears, but because holding it idle in inventory has an **opportunity cost**: that capital could have been earning returns elsewhere.

**Conclusion:** More inventory → higher NWC → additional cash outflow at t = 0 → recovery only at project end → **lower NPV** due to time value of money.

---

### Part d — Impact of Declining Balance vs. Straight-Line Depreciation

**Yes — switching to declining balance (degressive) depreciation would increase the financial value of the project.**

The essential insight is that **the total amount depreciated is identical under both methods** — you write off the same CAPEX down to zero either way. So the total nominal tax saved over the project's life is also the same. What changes is purely the *timing* of those tax savings, and timing is everything in a discounted cash flow world.

The **depreciation tax shield** each year equals:

    Depreciation tax shield = t × Depreciation

Under straight-line depreciation, this shield is spread evenly across all years. Under declining balance, larger depreciation charges arrive in early years, front-loading the tax shields:

- **Early years:** larger deduction → larger tax shield → tax saved *now* (full PV)
- **Later years:** smaller deduction → smaller tax shield → tax saved *in the future* (discounted)

Because of **time value of money**, a euro of tax saved in year 1 is worth more than a euro saved in year 5. By pulling the tax savings forward in time, declining balance depreciation increases the **present value of the total tax shield stream** — even though the sum of all shields is unchanged in nominal terms.

**Conclusion:** Declining balance → front-loaded tax deductions → higher PV of depreciation tax shields → **higher NPV**. This is a pure time-value-of-money effect: same cash, earlier timing, higher value.

---

## QUESTION TYPE 4 — Capita Selecta / ACTUA

---

### Q4.1 — The GameStop Story (Feb 2021)

#### Part a — The Story (Short Position, Short Squeeze, Margin Requirements)

GameStop was a struggling brick-and-mortar video game retailer. Large hedge funds believed its stock was overvalued and took **short positions**: they borrowed GameStop shares, sold them immediately, and planned to buy them back later at a lower price — pocketing the difference.

Retail investors on Reddit's r/WallStreetBets noticed the extremely high short interest and began coordinated mass buying of GameStop shares. This drove the price sharply upward.

As the price rose, the short-sellers faced growing losses. Brokers enforcing **margin requirements** — minimum collateral that short-sellers must maintain at all times — forced the funds to either post more collateral or buy back ("cover") their short positions. This forced buying pushed the price even higher, triggering more forced buying in a self-reinforcing feedback loop known as a **short squeeze**.

GameStop's stock surged from ~$20 to nearly $500 within weeks, causing billions in losses for hedge funds.

#### Part b — EMH Implications

**What EMH means:** The **Efficient Market Hypothesis (EMH)** states that asset prices at all times reflect all available information, so no investor can consistently earn abnormal (risk-adjusted) returns. It exists in three forms: **weak** (prices reflect all historical trading data), **semi-strong** (prices reflect all publicly available information), and **strong** (prices reflect all information including private). The deeper implication of EMH — connecting back to CH0 — is that in an efficient market, **price equals fundamental value** at all times.

**How GameStop challenges EMH — the arbitrage mechanism:**
The most important academic insight from GameStop is not simply that the price was "wrong" — it is that the *mechanism that normally corrects mispricings was disabled*.

Under EMH, **short-sellers are the market's self-correction mechanism**: when a stock is overpriced, sophisticated investors short it, creating selling pressure that drives the price back toward fundamental value. In GameStop, this mechanism was inverted. As the coordinated retail buying drove the price up, margin requirements forced short-sellers to *buy* rather than sell, adding *upward* pressure rather than corrective downward pressure. The very action that should have corrected the overpricing instead amplified it — a **short squeeze** turned the EMH correction mechanism against itself.

This is a challenge to the **semi-strong form** of EMH: for weeks, the market price reflected irrational social media coordination rather than publicly available fundamental information about GameStop's cash flows. It is strong evidence for **behavioral finance** — specifically herding, momentum chasing, and FOMO — over rational price formation.

The eventual collapse of the price back toward fundamental value is partially consistent with the long-run corrective tendency of semi-strong EMH, suggesting markets may be inefficient in the **short run** but tend toward efficiency over time — closer to the **Adaptive Market Hypothesis** than strict EMH.

---

### Q4.2 — Long-Call Option Position

#### Part a — What is a Long-Call and Why is the Profit/Loss Asymmetric?

A **long-call position** = **buying a call option**.

By paying a **premium** (the option price) today, the buyer acquires the **right — but not the obligation** — to purchase the underlying asset at the agreed **strike price (K)** on or before the **expiry date**.

The profit/loss profile is asymmetric because of the optionality embedded in the contract:

**If stock price (S) at expiry < K (out of the money):**

    The buyer does NOT exercise (why buy at K when market price is lower?).
    Option expires worthless.
    Loss = premium paid   ← this is the maximum possible loss (fixed and known upfront)

**If stock price (S) at expiry > K (in the money):**

    The buyer exercises: buys the asset at K, worth S in the market.
    Profit = (S − K) − premium paid   ← grows linearly and is theoretically unlimited

This creates the **asymmetric "hockey stick" shape**: flat at (−premium) for all S < K, then upward-sloping once S exceeds K. The defining feature of options: **limited downside, unlimited upside**.

#### Part b — What Risk Does a Long-Call Hedge? Example.

**Risk hedged:** A long-call hedges against the risk of a **future price increase** in an asset the company needs to **buy** (an input, a commodity, or a foreign currency).

**Specific example:**

An **airline company (e.g., Ryanair)** has large, predictable future purchases of jet fuel. If oil prices spike, its operating costs surge and margins collapse. By buying **call options on crude oil (or jet fuel)**:

- The airline **caps its maximum fuel cost** at: Strike Price K + premium paid — regardless of how high oil goes.
- The airline **still benefits** if fuel prices fall: it lets the option expire worthless and buys fuel at the lower market price (unlike a forward contract, which locks in the price in both directions).

This gives the airline cost certainty and protects its profit margin against the most significant input cost risk it faces — at the limited cost of the option premium.

---

*End of model answers.*
