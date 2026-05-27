# Corporate Finance — Mock Exam: Full Model Solutions
### With Course Formulas, Step-by-Step Calculations & TI-84 Plus Instructions

---

## QUESTION TYPE 1 — Multiple Choice

---

### MC Q1 — Van Peteghem Bond: Bond Price

**Question:** 3-year Belgian government bond, nominal €1,000, annual coupon 3.3%, redeemed at par, YTM = 1.5%. What is the fair price today?

**Answer: c. €1,052.42**

---

#### Course Formula

**Bond price = PV of all future cash flows discounted at YTM:**

    Bond Price = Σ [ Coupon / (1 + YTM)^t ]  +  Par / (1 + YTM)^n
                 t=1 to n

    where:  Coupon = coupon rate × par value
            YTM    = yield to maturity
            n      = number of periods to maturity

---

#### Step-by-Step

Annual coupon = 3.3% × €1,000 = **€33**

| Period | Cash Flow | PV = CF / (1.015)^t |
|--------|-----------|---------------------|
| t = 1  | €33       | 33 / 1.015 = **€32.51** |
| t = 2  | €33       | 33 / 1.015² = **€32.03** |
| t = 3  | €1,033    | 1,033 / 1.015³ = **€987.88** |
| **Price** | | **€1,052.42** |

    Price = 32.51 + 32.03 + 987.88 = €1,052.42  ✓

> The bond trades **above par** because coupon rate (3.3%) > YTM (1.5%) — investors are willing to pay a premium to receive the above-market coupon.

> **Van Peteghem context:** This illustrates why the 2023 Van Peteghem bond was attractive — it offered a 3.3% rate when savings accounts offered near zero, so investors were willing to pay above par in the secondary market.

#### TI-84 Plus

`APPS` → `Finance` → `TVM Solver`
N=3 | I%=1.5 | PMT=33 | FV=1000 | P/Y=1 → Solve **PV = −1,052.42**

---

### MC Q2 — Macaulay Duration

**Question:** 2-year bond, coupon = 6% annually, YTM = 4%, par = €100. Macaulay duration?

**Answer: c. 1.94 years**

---

#### Course Formula

**Macaulay Duration = weighted average time to receive cash flows in PV terms:**

    Duration = Σ [ t × PV(CF_t) ] / Bond Price

    where:  PV(CF_t) = CF_t / (1 + YTM)^t
            Bond Price = Σ PV(CF_t)

---

#### Step-by-Step

| Period | Cash Flow | PV(CF) = CF/(1.04)^t | t × PV(CF) |
|--------|-----------|----------------------|------------|
| t = 1  | €6        | 6/1.04 = **€5.769**  | 1 × 5.769 = 5.769 |
| t = 2  | €106      | 106/1.04² = **€98.003** | 2 × 98.003 = 196.006 |
| **Price** | | **€103.772** | **201.775** |

    Duration = 201.775 / 103.772 = 1.9444 ≈ 1.94 years  ✓

> Duration < Maturity (2 years): the bond pays coupons before maturity, pulling the weighted average time forward. A zero-coupon bond would have duration = 2.00 years exactly.

#### TI-84 Plus

Bond price: N=2 | I%=4 | PMT=6 | FV=100 → PV = **−103.772**

Duration:
`6 ÷ 1.04` → **5.769**
`106 ÷ 1.04^2` → **98.003**
`(1 × 5.769 + 2 × 98.003) ÷ 103.772` → **1.944 years**

---

### MC Q3 — DDM + PVGO: NextGrowth NV

**Question:** EPS₁ = €6.00, payout = 50%, ROE = 18%, cost of equity = 12%. What is the PVGO?

**Answer: c. €50.00**

---

#### Course Formulas

**Constant-growth DDM (Gordon-Shapiro):**

    P₀ = Div₁ / (r − g)

**Dividend growth rate:**

    g = ROE × Plowback ratio    where Plowback = 1 − Payout ratio

**Present Value of Growth Opportunities:**

    PVGO = P₀  −  EPS₁ / r

    where EPS₁/r = steady-state (no-growth, 100% payout) benchmark value

---

#### Step-by-Step

**Step 1 — Growth rate:**

    Plowback = 1 − 0.50 = 0.50
    g = ROE × Plowback = 18% × 50% = 9%

**Step 2 — Next dividend:**

    Div₁ = Payout × EPS₁ = 50% × €6.00 = €3.00

**Step 3 — Current share price (with growth):**

    P₀ = Div₁ / (r − g) = €3.00 / (12% − 9%) = €3.00 / 0.03 = €100.00

**Step 4 — Steady-state no-growth benchmark:**

    EPS₁ / r = €6.00 / 0.12 = €50.00

**Step 5 — PVGO:**

    PVGO = P₀ − EPS₁/r = €100.00 − €50.00 = €50.00  ✓

> Half of NextGrowth's value comes from current earning power, and half from future growth opportunities. This is only justified because ROE (18%) > cost of equity (12%) — reinvested earnings create value.

#### TI-84 Plus

`3.00 ÷ (0.12 − 0.09)` → **P₀ = 100.00**
`6.00 ÷ 0.12` → **50.00**
`100.00 − 50.00` → **PVGO = €50.00**

---

### MC Q4 — Portfolio Variance

**Question:** A (w=30%, E(R)=10%, σ=15%) + B (w=70%, E(R)=16%, σ=22%), ρ=0.3. Which best quantifies portfolio risk?

**Answer: c. Variance = 2.990%**

---

#### Course Formula

**Variance of a 2-asset portfolio:**

    σ²p = wA² × σA²  +  wB² × σB²  +  2 × wA × wB × ρ(A,B) × σA × σB

---

#### Step-by-Step

    σ²p = (0.30)² × (0.15)²  +  (0.70)² × (0.22)²  +  2 × 0.30 × 0.70 × 0.3 × 0.15 × 0.22

    Term 1: 0.0900 × 0.0225  = 0.002025
    Term 2: 0.4900 × 0.0484  = 0.023716
    Term 3: 2 × 0.30 × 0.70 × 0.3 × 0.033  = 0.004158

    σ²p = 0.002025 + 0.023716 + 0.004158 = 0.029899

    Expressed as percentage:  σ²p = 2.990%  ✓
    σp = √0.029899 = 17.29%

> Option c is the only correct answer: the standard deviation (17.29%) is not listed as an option; options a and b give wrong SD values; option d gives wrong variance. Always verify your portfolio standard deviation by squaring it back.

#### TI-84 Plus

`0.30^2 × 0.15^2 + 0.70^2 × 0.22^2 + 2 × 0.30 × 0.70 × 0.3 × 0.15 × 0.22` → **0.029899**
Multiply by 100: **2.990%**

---

### MC Q5 — WACC: Company HEX NV

**Question:** HEX NV: 4M shares × €10, €40M debt, rd=6%, t=25%, Cov=0.02, σm=10%, rf=2%, Rm=7%. WACC?

**Answer: b. 8.25%**

---

#### Course Formulas

**Beta:**

    β = Cov(Rᵢ, Rm) / Var(Rm) = Cov(Rᵢ, Rm) / σ²m

**Cost of Equity (CAPM / SML):**

    re = rf  +  β × (E(Rm) − rf)

**WACC:**

    WACC = (E / (D+E)) × re  +  (D / (D+E)) × rd × (1 − t)

---

#### Step-by-Step

**Step 1 — Beta:**

    β = 0.02 / (0.10)² = 0.02 / 0.01 = 2.0

**Step 2 — Cost of Equity:**

    re = 2% + 2.0 × (7% − 2%) = 2% + 2.0 × 5% = 2% + 10% = 12%

**Step 3 — Market value weights:**

    E = 4,000,000 × €10 = €40M
    D = €40M     →     Total = €80M
    wE = 40/80 = 50%,   wD = 40/80 = 50%

**Step 4 — WACC:**

    WACC = 0.50 × 12%  +  0.50 × 6% × (1 − 0.25)
         = 6.00%  +  0.50 × 4.50%
         = 6.00%  +  2.25%
         = 8.25%  ✓

#### TI-84 Plus

`0.02 ÷ 0.10^2` → **β = 2.0**
`2 + 2.0 × (7 − 2)` → **re = 12%**
`0.50 × 12 + 0.50 × 6 × 0.75` → **WACC = 8.25%**

---

## QUESTION TYPE 2 — Short Conceptual Questions

---

### Q2.1 — Belgian Pension Reform: Uncertain Factors

**Three key uncertain factors, each with its direction of effect:**

**1. Time to retirement (t) — negative effect on scheme attractiveness**
The longer the time horizon before retirement, the more powerfully the time value of money works against the pension plan. The €2,025 invested elsewhere has more years to grow exponentially at the opportunity rate. With 30+ years until retirement, even a modest return of 5–6% on alternative investments will easily outpace the fixed yearly pension benefit received much later. Shorter time to retirement reduces this TVM disadvantage.

**2. Years alive after retirement (z) — positive effect on scheme attractiveness**
The pension benefit (€750/year) is received every year for as long as you live after retirement. The longer you live, the more total payments you receive. A person who lives 25 years after retirement collects much more from the scheme than one who lives only 10 years. The scheme is an annuity, and longer post-retirement life means higher present value of that annuity.

**3. Alternative investment return (r) — negative effect on scheme attractiveness**
The higher the annual return you can achieve by investing the €2,025 elsewhere (in stocks, funds, etc.), the faster your money compounds and the wealthier you will be at retirement. A high achievable return makes the fixed pension benefit relatively less valuable. The break-even return is the rate at which you are indifferent between the two options.

---

### Q2.2 — Van Peteghem Bond and the Inverted Yield Curve

**(a) What is a yield curve, and what does normal vs. inverted signal?**

A **yield curve** plots the interest rates (YTM) of government bonds of the same credit quality against their maturities (from short-term to long-term). It shows at a glance the cost of borrowing at different time horizons.

- **Normal yield curve (upward-sloping):** Long-term rates are higher than short-term rates. This is the typical pattern — investors demand a higher return for committing money for longer periods (term premium). It signals **confidence in the economy**: growth and moderate inflation are expected in the long run.

- **Inverted yield curve (downward-sloping):** Short-term rates are higher than long-term rates. This is unusual and typically signals **economic uncertainty or recession fears**. Investors expect central banks to cut rates in the future (predicting a slowdown), driving long-term rates down below short-term rates.

**(b) Why did an inverted yield curve make a second 1-year bond less attractive in 2024?**

Under an inverted yield curve, the **short-term (1-year) rate is higher than medium-term rates** (e.g., 2–3 year bonds). From the Belgian government's perspective as a borrower, this means:

- A 1-year bond now carries a **higher borrowing cost** than a 2 or 3-year bond.
- It is cheaper and more rational to issue a **longer-term bond** and lock in the lower medium-term rate.
- Additionally, offering the 1-year bond without the favorable 15% tax regime (after political opposition) meant investors faced the standard 30% tax, making the after-tax yield less attractive than competing bank products that had improved.

---

### Q2.3 — Trade-Off Theory vs. Pecking Order Theory

**Trade-Off Theory:**
There is an **optimal level of debt** for every firm, determined by the trade-off between two opposing forces:
- **Tax benefit of debt (increasing with debt):** Interest payments on debt are tax-deductible → more debt = larger tax shields = more firm value. Tax shield = tc × (D × rd).
- **Costs of financial distress (increasing with debt):** As debt increases, the risk of insolvency rises, and the associated direct/indirect costs (bankruptcy costs, loss of customers, key employees, etc.) erode value.

The optimal capital structure is where the marginal tax benefit of one more unit of debt equals the marginal increase in financial distress costs.

**Pecking Order Theory:**
Firms do **not** target an optimal leverage ratio. Instead, they follow a fixed hierarchy of financing preferences driven by information asymmetry and cost of funds:

    1st preference: Internal funds (retained earnings)
    2nd preference: External debt
    3rd preference: External equity (most costly, used last)

External equity is most expensive because issuing new shares signals to the market that management believes shares are overvalued — causing a negative stock price reaction. Debt is cheaper because it avoids this signal. Internal funds are cheapest of all (opportunity cost only).

---

### Q2.4 — Real Options in Capital Budgeting

**What is a real option?**
A **real option** is the possibility for managers to **re-evaluate and adjust an investment decision** as new information becomes available over time. Unlike the standard NPV approach — which assumes all decisions are made once ("one-shot"), all information is known upfront, and managers are passive — real options acknowledge the reality of **changing business conditions and active management**.

Types include: option to delay, option to expand, option to scale down, option to abandon, option to switch.

**(a) Why do real options increase NPV?**
Standard NPV analysis treats a project as a fixed commitment and ignores the value of future flexibility. Real options add value because they allow managers to:
- **Limit downside**: if things go badly, exercise the option to abandon or scale down, avoiding further losses.
- **Capture upside**: if things go well, exercise the option to expand.

This asymmetry — avoiding losses while capturing gains — creates additional value that standard DCF misses. The real option value is always ≥ 0, so including it can only increase (or leave unchanged) the project's NPV.

**(b) Why are real options more valuable under higher uncertainty?**
Options derive their value from **uncertainty about future outcomes**. When uncertainty is high:
- The range of possible outcomes is wide → the option to avoid bad outcomes (or exploit good ones) is more valuable.
- Just as financial options are more valuable when the underlying asset's volatility is higher (Black-Scholes: σ ↑ → option value ↑), real options follow the same logic.
- In a certain world, there would be no value in waiting or flexibility — you already know the outcome.

---

### Q2.5 — Beta: Concept, Measurement, and Role in CAPM

**What is beta?**
Beta (β) measures a security's **systematic (market) risk** — its sensitivity to overall market movements. Specifically, β quantifies how much a stock's returns tend to move when the market moves by 1%.
- β = 1.5: stock tends to move 1.5% for every 1% market move (amplified).
- β = 0.5: stock moves only 0.5% for every 1% market move (dampened).
- β = 1.0: moves in line with the market.

**How is beta measured in practice?**
Beta is estimated via **regression** of the stock's historical excess returns on the market's excess returns (over the risk-free rate). The slope of this regression line is beta. Alternatively, using the covariance formula:

    β = Cov(Ri, Rm) / Var(Rm) = Cov(Ri, Rm) / σ²m

**Why use beta (not total σ) to estimate the cost of equity?**
The CAPM/SML demonstrates that investors in efficient markets will **diversify their portfolios**, eliminating all idiosyncratic (firm-specific) risk at zero cost. Therefore:
- The market does **not compensate** investors for holding diversifiable risk.
- Only **systematic risk (beta)** — risk that cannot be diversified away — commands a return premium.
- A stock's required return depends only on its beta, not on its total volatility. Two stocks with identical betas have the same required return even if their total standard deviations differ wildly.

    re = rf  +  β × (E(Rm) − rf)      [the SML / CAPM equation]

---

## QUESTION TYPE 3 — BioTech NV: Full Solution

---

### Part a — BioTech NV's Cost of Capital (WACC)

#### Course Formulas

**Beta:**

    β = Cov(R_BioTech, Rm) / Var(Rm) = Cov(R_BioTech, Rm) / σ²m

**Cost of Equity (CAPM/SML):**

    re = rf  +  β × (E(Rm) − rf)

**WACC:**

    WACC = (E / (D+E)) × re  +  (D / (D+E)) × rd × (1 − t)

---

#### Step-by-Step

**Step 1 — Beta:**

    β = Cov(BioTech, market) / σ²m
      = 0.03 / (0.15)²
      = 0.03 / 0.0225
      = 1.333

> β = 1.333: BioTech's stock moves approximately 1.33× the market. It is a moderately high-beta pharmaceutical firm — sensible given the volatile nature of biotech revenues (clinical trials, regulatory decisions).

**Step 2 — Cost of Equity (CAPM):**

    re = rf + β × (E(Rm) − rf)
       = 4% + 1.333 × (10% − 4%)
       = 4% + 1.333 × 6%
       = 4% + 8%
       = 12%

> Shareholders require a 12% annual return to compensate for the systematic risk of BioTech's equity.

**Step 3 — Market Value Weights (always use market values, not book values):**

    E = 8,000,000 shares × €9 = €72,000,000
    D = €72,000,000
    D + E = €144,000,000

    wE = 72/144 = 50%
    wD = 72/144 = 50%

**Step 4 — WACC:**

    WACC = wE × re  +  wD × rd × (1 − t)
         = 0.50 × 12%  +  0.50 × 6% × (1 − 0.25)
         = 6.00%  +  0.50 × 4.50%
         = 6.00%  +  2.25%
         = 8.25%

> **Role of WACC:** The WACC is BioTech's **hurdle rate** — the minimum annual return any investment project must generate to create value for investors. A project with NPV > 0 at 8.25% creates value; one with NPV < 0 destroys value. It reflects what all investors (shareholders at 12% and debt-holders at 6% pre-tax) collectively require.

**TI-84:** `0.03 ÷ 0.15^2` → 1.333 | `4 + 1.333 × 6` → 12% | `0.50 × 12 + 0.50 × 6 × 0.75` → **8.25%**

---

### Part b — Which Proposal? (EAA Method)

**Why EAA and not plain NPV?**
BioTech NV is a **going concern** — it will need production equipment indefinitely. The two proposals have **different economic lifespans** (5 years vs. 8 years). Simply comparing NPVs would be unfair: the 8-year project looks better partly because it lasts longer, not necessarily because it creates more value per year. The **Equivalent Annual Annuity (EAA)** method converts each NPV into an annualised figure, enabling a fair like-for-like comparison under the assumption of perpetual replacement.

---

#### Course Formulas

**After-tax Operating Cash Flow:**

    OCF = (Revenue − Costs − Depreciation) × (1 − t)  +  Depreciation
        = (Revenue − Costs) × (1 − t)  +  t × Depreciation
                                           ─────────────────
                                           Depreciation tax shield

**Straight-line depreciation:**

    Depreciation = CAPEX / Useful life (years)

**Net Present Value:**

    NPV = −CAPEX  +  OCF × Annuity factor(r, n)   [when OCF is constant]

**Annuity Factor:**

    AF(r, n) = [1 − (1 + r)^(−n)] / r

**Equivalent Annual Annuity:**

    EAA = NPV / AF(r, n)

---

#### Proposal X — CAPEX €600,000, 5-year life

**Straight-line depreciation:**

    Depreciation_X = 600,000 / 5 = €120,000 / year

**Annual after-tax cash flow:**

| Item | Calculation | Amount |
|------|-------------|--------|
| Revenue increase | given | +€240,000 |
| Operating cost increase | given | − €60,000 |
| Depreciation | − €120,000 | − €120,000 |
| **EBIT** | 240,000 − 60,000 − 120,000 | **€60,000** |
| Tax (25%) | 60,000 × 25% | − €15,000 |
| Net income | | €45,000 |
| + Add back depreciation | | + €120,000 |
| **Annual OCF** | | **€165,000** |

**Verification:**

    OCF_X = (240,000 − 60,000 − 120,000) × (1−0.25) + 120,000
           = 60,000 × 0.75 + 120,000
           = 45,000 + 120,000 = €165,000  ✓

**NPV of Proposal X:**

    AF(8.25%, 5 yr) = [1 − (1.0825)^(−5)] / 0.0825
    (1.0825)^5 = 1.4879
    AF = (1 − 1/1.4879) / 0.0825 = (1 − 0.6721) / 0.0825 = 0.3279 / 0.0825 = 3.9745

    NPV_X = −600,000 + 165,000 × 3.9745
           = −600,000 + 655,793
           = +€55,793

**EAA of Proposal X:**

    EAA_X = 55,793 / 3.9745 = €14,039 / year

---

#### Proposal Y — CAPEX €800,000, 8-year life

**Straight-line depreciation:**

    Depreciation_Y = 800,000 / 8 = €100,000 / year

**Annual after-tax cash flow:**

| Item | Calculation | Amount |
|------|-------------|--------|
| Revenue increase | given | +€260,000 |
| Operating cost increase | given | − €55,000 |
| Maintenance cost | given | − €10,000 |
| Depreciation | | − €100,000 |
| **EBIT** | 260,000 − 55,000 − 10,000 − 100,000 | **€95,000** |
| Tax (25%) | 95,000 × 25% | − €23,750 |
| Net income | | €71,250 |
| + Add back depreciation | | + €100,000 |
| **Annual OCF** | | **€171,250** |

**Verification:**

    OCF_Y = (260,000 − 55,000 − 10,000 − 100,000) × (1−0.25) + 100,000
           = 95,000 × 0.75 + 100,000
           = 71,250 + 100,000 = €171,250  ✓

**NPV of Proposal Y:**

    AF(8.25%, 8 yr) = [1 − (1.0825)^(−8)] / 0.0825
    (1.0825)^8 = 1.8878
    AF = (1 − 1/1.8878) / 0.0825 = (1 − 0.5298) / 0.0825 = 0.4702 / 0.0825 = 5.6994

    NPV_Y = −800,000 + 171,250 × 5.6994
           = −800,000 + 975,924
           = +€175,924

**EAA of Proposal Y:**

    EAA_Y = 175,924 / 5.6994 = €30,866 / year

---

#### Decision

| | NPV | EAA (annual value created) |
|---|---|---|
| Proposal X (5 yr) | €55,793 | **€14,039 / year** |
| Proposal Y (8 yr) | €175,924 | **€30,866 / year** |

**→ Proposal Y is strongly preferred.** Its EAA is more than twice that of Proposal X. Although Y requires a larger initial investment (€800k vs. €600k) and lasts longer, it generates significantly higher revenue, its cost structure is efficient, and its longer economic life more than compensates for the higher CAPEX. On an annualised basis, Y creates approximately €16,800 more value per year.

**Additional assumption:** No salvage/residual value and no additional working capital changes (beyond part c).

**TI-84 for NPV_X:**
`APPS` → Finance → `NPV(8.25, −600000, {165000,165000,165000,165000,165000})` → **€55,793**
Then: TVM Solver N=5 | I%=8.25 | PV=−55793 | FV=0 → Solve PMT → **EAA_X = €14,039**

**TI-84 for NPV_Y:**
`NPV(8.25, −800000, {171250,171250,171250,171250,171250,171250,171250,171250})` → **€175,924**
Then: TVM Solver N=8 | I%=8.25 | PV=−175924 | FV=0 → Solve PMT → **EAA_Y = €30,866**

---

### Part c — Impact of Decrease in Working Capital (−€50,000)

**Yes — the decrease in working capital INCREASES the financial value of the project.**

This is the **opposite** effect compared to a working capital increase. Here is the logic:

Working capital (inventory, receivables minus payables) is cash that is tied up in operations. A **decrease in working capital** means cash is **released** — it becomes available immediately and can be used elsewhere or returned to investors.

In NPV analysis:

    Cash flow from ΔNWC = −ΔNWC

Since ΔNWC = −€50,000 (a decrease):

    CF from NWC = −(−€50,000) = +€50,000 at t = 0

This **positive cash inflow at t = 0 adds directly to NPV**. Unlike a working capital increase where you pay now and recover later at a discounted value, here you receive cash immediately at full value — with no discounting needed.

**Conclusion:** Improved production efficiency → inventory decrease → working capital release → **cash inflow** at start → **higher NPV** → more financial value created for BioTech NV.

---

### Part d — Impact of Declining Balance Depreciation

**Yes — declining balance (degressive) depreciation would increase the financial value of the project.**

The reasoning is based on the **depreciation tax shield** formula:

    Depreciation tax shield = t × Depreciation

Key principle:
1. **Total depreciation is identical regardless of method:** over the full life of the asset, the same total CAPEX is depreciated. Total nominal tax paid is therefore the same.

2. **But timing differs critically:** declining balance front-loads depreciation (larger amounts in early years, smaller in later years). This produces:
   - **Larger tax shields early** → more taxes saved sooner (high PV)
   - **Smaller tax shields late** → less saving, but those future savings are already discounted heavily

3. **TVM effect:** Because of discounting, €1 of tax saving today is worth more than €1 of tax saving in year 8. Front-loading depreciation increases the **present value** of the total tax shield stream, even though the nominal total is unchanged.

**Conclusion:** Declining balance → front-loaded tax shields → higher PV of all tax savings → **higher NPV** → more financial value created.

> This is a core principle from the course: *"Front-loading depreciation = lower taxes in the beginning = higher financial value."*

---

## QUESTION TYPE 4 — ACTUA Cases & Capita Selecta

---

### Q4.1 — Gu & Lev (2011): Overpriced Shares and Goodwill Write-Offs

#### Part a — Main Thesis

**The root cause of goodwill write-offs, according to Gu & Lev, is the bidder's overpriced shares at the time of acquisition.**

The chain of events works as follows:

1. **Share overpricing:** A company's shares are traded at a price significantly above their fundamental (intrinsic) value — driven by market euphoria, high P/E multiples, or earnings manipulation. The paper measures share overpricing through the industry-adjusted P/E ratio, discretionary accruals, and net equity issuance.

2. **Acquisition with overpriced shares:** Managers of overpriced firms have a strong incentive to use those overpriced shares as "currency" to acquire other businesses — because each share buys more than it is really worth. This leads them to overpay for targets, often paying more than the present value of expected synergies.

3. **Goodwill creation:** The excess of the acquisition price over the fair value of the acquired net assets is recorded as **goodwill** on the balance sheet. The higher the overpayment, the higher the goodwill recorded.

4. **Goodwill write-off (impairment):** When the expected synergies fail to materialise (because the acquisition was overpriced and ill-advised to begin with), goodwill must be **written off** — a massive accounting charge recognising that the acquisition destroyed, rather than created, value.

> Empirically, Gu & Lev find a strong, monotonically increasing relationship: the more overpriced the bidder, the higher the acquisition intensity, the larger the goodwill, and the greater the subsequent goodwill write-off.

#### Part b — Link to NPV and PVGO

**Link to NPV:**
An acquisition is fundamentally an **investment decision** that should be evaluated using NPV:

    NPV_acquisition = PV(synergies from merger) − Acquisition price paid

When a firm acquires with overpriced shares:
- The **acquisition price paid** is inflated (the firm pays in shares worth less than their market price in fundamental terms).
- The **synergies** are often overestimated due to managerial overconfidence and hubris (Roll 1986).
- The result: acquisition price > PV(synergies) → **NPV < 0** → a value-destroying deal.

The goodwill write-off is the eventual accounting recognition that this NPV was, in fact, negative.

**Link to PVGO:**
The course showed that a stock's price consists of:

    P₀ = EPS/r  +  PVGO

An overpriced firm has an inflated PVGO — the market assigns high value to future growth opportunities that may not actually exist. Managers exploit this by using the overpriced shares to acquire other companies, hoping to justify the high valuation. However, if the acquisitions fail to generate the implied returns, the PVGO collapses and the stock price corrects — exactly what Gu & Lev document.

**Managerial psychology:** The course material on bad corporate investments (e.g., Daimler-Chrysler, AOL-Time Warner, HP-Autonomy) highlights psychological biases — overconfidence, hubris, confirmation bias — as accelerants of these ill-advised deals. Managers overestimate synergies and underestimate integration risks, compounding the financial damage of acquiring with overpriced shares.

---

### Q4.2 — Belgian Pension Reform: TVM and Decision

#### Part a — Why TVM is Critical

**Time value of money (TVM)** is critical because the pension scheme involves a **cash outflow now** (€2,025 today) in exchange for **cash inflows far in the future** (€750/year starting at retirement — possibly 30 years away).

The €2,025 paid today is not "free." By committing it to the pension scheme, you **forgo** the ability to invest that money elsewhere. The **opportunity cost of capital** is the return you could have earned — stocks, bonds, funds — over those 30 years. Even at a modest 5% annual return, €2,025 invested today would grow to €2,025 × (1.05)^30 ≈ €8,760 by retirement — far exceeding what the pension scheme's annuity stream is worth in PV terms.

The course formula makes this explicit. You participate in the pension scheme only if:

    FV of pension annuity  >  FV of alternative investment

    i.e. 750 × [1 − (1+r)^(−z)] / r  <  2,025 × (1+r)^t

    when: t = years to retirement, z = years of post-retirement life, r = alternative return

TVM is therefore not a minor consideration — it is the **central** factor that can make a seemingly generous pension plan financially unattractive.

#### Part b — Should This Person Participate? (r = 7%, t = 30, z = 20)

**No — at 7% annual return, this person should NOT participate in the pension scheme.**

**Reasoning:**

The break-even rate for the scenario (t=30 years to retirement, z=20 years of post-retirement life) is **5.18%** per year. This means:
- If your alternative return is **above 5.18%**, investing elsewhere beats the pension scheme.
- If your alternative return is **below 5.18%**, the pension scheme is more attractive.

This person earns **7% per year on alternative investments — well above the 5.18% break-even threshold**. Therefore:

- The €2,025 invested at 7% for 30 years grows to a much larger sum than the pension annuity's PV upon retirement.
- At 7%, the future value of €2,025 in 30 years = €2,025 × (1.07)^30 ≈ €15,420.
- The pension annuity (€750/year for 20 years at 7% discount rate) is worth approximately: 750 × [1-(1.07)^(-20)]/0.07 ≈ 750 × 10.594 = €7,946 at retirement.
- Since €15,420 > €7,946, the alternative investment clearly wins.

The higher the achievable alternative return, and the longer until retirement, the less attractive the government pension scheme becomes. This person should decline and invest the €2,025 in a diversified investment portfolio instead.

---

*End of model solutions.*
