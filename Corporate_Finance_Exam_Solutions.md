# Corporate Finance — Illustrated Exam: Full Model Answers

> **Note:** All calculations shown step-by-step. TI-84 Plus keystrokes are included for every numerical question.

---

## QUESTION TYPE 1 — Multiple Choice

---

### MC Q1 — Inflation-Linked Financial Product

**Question:** An inflation-linked product pays €50 at the **beginning of each quarter** for 3 years (first payment immediately). Afterwards, payments grow at **0.5% per quarter** (= inflation). Real annual interest rate = 10%. What is today's price?

**Answer: d. €2,550.93**

#### Concept
This is a two-part valuation:
- **Phase 1:** Annuity-due (payments at beginning of period) for 12 quarters at €50 fixed.
- **Phase 2:** Growing perpetuity starting after 3 years, growing at 0.5%/quarter.

The product is inflation-linked, so we use the **real** interest rate to discount (the growing payments compensate for inflation; using the real rate avoids double-counting inflation).

#### Step-by-Step

**Step 1 – Convert real annual rate to quarterly rate:**

```
r_quarterly = (1 + r_annual)^(1/4) - 1
            = (1.10)^(1/4) - 1
            = 1.02411 - 1
            = 2.411% per quarter
```

> Key shortcut: (1.02411)^4 = 1.10, so (1.02411)^**12** = (1.10)^**3** = **1.331** — you will use this repeatedly.

---

**Step 2 – Phase 1: PV of annuity-due (12 payments of €50)**

For an annuity-**due** (payments at beginning of period), multiply the ordinary annuity formula by (1 + r):

```
PV₁ = 50 × [1 - (1.02411)^(-12)] / 0.02411 × (1.02411)

    = 50 × [1 - 1/1.331] / 0.02411 × 1.02411

    = 50 × [1 - 0.7513] / 0.02411 × 1.02411

    = 50 × 0.2487 / 0.02411 × 1.02411

    = 50 × 10.313 × 1.02411

    = €528.09
```

---

**Step 3 – Phase 2: PV of growing perpetuity (starting at t = 12)**

After 3 years, the next payment at t = 12 is €50 × 1.005 = €50.25, then grows at 0.5%/quarter forever.

The growing perpetuity formula gives PV **one period before** the first payment, i.e., at t = 11:

```
PV at t=11 = C₁₂ / (r - g) = (50 × 1.005) / (0.02411 - 0.005)
           = 50.25 / 0.01911
           = €2,629.01
```

Discount this back 11 quarters to today (t = 0):

```
PV₂ = 2,629.01 / (1.02411)^11
    = 2,629.01 / (1.331 / 1.02411)
    = 2,629.01 / 1.3001
    = €2,022.84
```

---

**Step 4 – Total price:**

```
Price = PV₁ + PV₂ = €528.09 + €2,022.84 = €2,550.93  ✓
```

#### TI-84 Plus Instructions

**Phase 1 (annuity-due):**
1. Press `2nd` → `FINANCE` (or `APPS` → `Finance`) → `TVM Solver`
2. Set: `N=12`, `I%=2.411`, `PMT=50`, `FV=0`, `P/Y=1`, `C/Y=1`
3. Set payment to **BEGIN**: press `2nd` → `BGN` → `2nd` → `SET` (screen shows "BEGIN")
4. Move cursor to `PV`, press `ALPHA` → `SOLVE` → reads **PV = -528.09**

**Phase 2 (manual, enter directly):**
- `50 × 1.005 ÷ (0.02411 - 0.005)` → store as A
- `A ÷ (1.02411 ^ 11)` → reads **2022.84**
- Add: `528.09 + 2022.84 = 2550.93`

---

### MC Q2 — Macaulay Duration

**Question:** 2-year corporate bond, YTM = 3%, coupon rate = 5% annually, redeemed at par. What is the Macaulay duration?

**Answer: d. 1.95 years**

#### Concept
Macaulay duration = **weighted average time** to receive the bond's cash flows, where weights = PV(cash flow) / Bond Price. It measures how long it takes to "recover" the bond price in present value terms.

#### Step-by-Step

Assume par value = €100.

| Period | Cash Flow | PV = CF / (1.03)^t | Weight = PV / Price | t × Weight |
|--------|-----------|---------------------|----------------------|------------|
| t = 1  | €5        | 5/1.03 = **4.854**  | 4.854/103.827 = 0.0468 | 0.0468 |
| t = 2  | €105      | 105/1.06² = **98.973** | 98.973/103.827 = 0.9532 | 1.9065 |
| **Price** | | **€103.827** | 1.0000 | **1.9533 years** |

```
Duration = 0.0468 × 1 + 0.9532 × 2 = 1.9533 ≈ 1.95 years  ✓
```

> The bond trades **above par** (coupon 5% > YTM 3%), so duration < maturity (2 years), which makes sense.

#### TI-84 Plus Instructions

**Find bond price first:**
1. `TVM Solver`: `N=2`, `I%=3`, `PMT=5`, `FV=100`, `P/Y=1`, `C/Y=1`
2. Solve for `PV` → **103.827**

**Calculate duration manually:**
- `5 ÷ 1.03` → **4.854** (PV of coupon at t=1)
- `105 ÷ 1.03^2` → **98.973** (PV of coupon+par at t=2)
- `(1 × 4.854 + 2 × 98.973) ÷ 103.827` → **1.9533 ≈ 1.95 years**

---

### MC Q3 — DDM — Company Z

**Question:** Company Z: 2M shares, net profit = €3.6M, payout = 35%, ROE = 12%, cost of equity = 10%. Expected share value per DDM?

**Answer: b. €31.5**

#### Concept
Use the **Gordon-Shapiro constant growth DDM**: P₀ = Div₁ / (r - g)

#### Step-by-Step

**Step 1 – EPS:**
```
EPS = €3.6M / 2M shares = €1.80 per share
```

**Step 2 – Dividend (Div₁ = dividend to be paid, treated as next period's dividend):**
```
Div₁ = payout ratio × EPS = 35% × €1.80 = €0.63
```

**Step 3 – Growth rate g:**
```
Plowback ratio = 1 - payout ratio = 1 - 35% = 65%
g = ROE × plowback = 12% × 65% = 7.8% ≈ 8%
```

> The exam rounds g to **8%** (a common simplification in problems).

**Step 4 – Share price:**
```
P₀ = Div₁ / (r - g) = €0.63 / (10% - 8%) = €0.63 / 0.02 = €31.50  ✓
```

#### TI-84 Plus Instructions
Direct calculation: `0.63 ÷ (0.10 - 0.08)` → **31.50**

---

### MC Q4 — Sharpe Ratio of Portfolio

**Question:** Portfolio: Asset A (w=35%, E(R)=12%, σ=15%) + Asset B (w=65%, E(R)=15%, σ=20%), ρ=0.6, rf=0.25%. What is the Sharpe ratio?

**Answer: b. 0.82**

#### Concept
Sharpe ratio = excess return per unit of **total** portfolio risk.
```
Sharpe = [E(Rp) - rf] / σp
```

#### Step-by-Step

**Step 1 – Expected portfolio return:**
```
E(Rp) = 0.35 × 12% + 0.65 × 15% = 4.20% + 9.75% = 13.95%
```

**Step 2 – Portfolio variance:**
```
σ²p = wA² × σA² + wB² × σB² + 2 × wA × wB × ρ × σA × σB

    = (0.35)² × (0.15)² + (0.65)² × (0.20)² + 2 × 0.35 × 0.65 × 0.6 × 0.15 × 0.20

    = 0.001225 × 0.1225 ... [computed term by term:]
      Term 1: 0.1225 × 0.0225 = 0.002756
      Term 2: 0.4225 × 0.0400 = 0.016900
      Term 3: 2 × 0.2275 × 0.6 × 0.03 = 0.008190

    σ²p = 0.002756 + 0.016900 + 0.008190 = 0.027846
```

**Step 3 – Portfolio standard deviation:**
```
σp = √0.027846 = 16.687%
```

**Step 4 – Sharpe ratio:**
```
Sharpe = (13.95% - 0.25%) / 16.687% = 13.70% / 16.687% = 0.821 ≈ 0.82  ✓
```

#### TI-84 Plus Instructions
Enter directly:
- `0.35^2 × 0.15^2 + 0.65^2 × 0.20^2 + 2 × 0.35 × 0.65 × 0.6 × 0.15 × 0.20` → **0.027846**
- `√(0.027846)` → **0.16687** (use `2nd` → `√`)
- `(0.1395 - 0.0025) ÷ 0.16687` → **0.8210**

---

### MC Q5 — Portfolio Risk (Variance)

**Question:** Portfolio: Asset A (w=35%, E(R)=15%, σ=20%) + Asset B (w=65%, E(R)=18%, σ=22%), ρ=0.7. Best estimate of portfolio risk?

**Answer: c. variance = 3.936%**

#### Step-by-Step

```
σ²p = (0.35)² × (0.20)² + (0.65)² × (0.22)² + 2 × 0.35 × 0.65 × 0.7 × 0.20 × 0.22

      Term 1: 0.1225 × 0.0400 = 0.004900
      Term 2: 0.4225 × 0.0484 = 0.020449
      Term 3: 2 × 0.35 × 0.65 × 0.7 × 0.044 = 0.014014

    σ²p = 0.004900 + 0.020449 + 0.014014 = 0.039363

Expressed as a percentage: 0.039363 = 3.936%   ✓
σp = √0.039363 = 19.84%
```

> The exam asks which answer "best quantifies the risk." Option c. expresses the **variance** correctly (in percentage terms). Option a/b state incorrect standard deviation values; option d. is wrong variance.

#### TI-84 Plus Instructions
- `0.35^2 × 0.20^2 + 0.65^2 × 0.22^2 + 2 × 0.35 × 0.65 × 0.7 × 0.20 × 0.22` → **0.039363**
- Expressed as %: × 100 = **3.936%**

---

## QUESTION TYPE 2 — Short Conceptual Questions

---

### Q2.1 — Itsme Acquiring NextAuth: Financial Valuation

**How should the acquisition price be determined?**

Determining an acquisition price is fundamentally a **financial valuation** exercise. The goal is to estimate the **intrinsic value** of NextAuth — i.e., what its future cash flows are worth today.

The elements of financial value to consider are:

1. **Future Free Cash Flows (FCF):** Estimate the cash flows NextAuth will generate from its core operations over the forecast horizon. This requires forecasting revenues, costs, and capital expenditure.

2. **Terminal (going-concern) value:** Beyond the explicit forecast period, NextAuth will continue generating cash flows. A terminal value is estimated (e.g., using a perpetuity with a long-run growth rate) to capture this.

3. **Appropriate discount rate (opportunity cost of capital):** The discount rate must reflect the **risk** of NextAuth's cash flows — specifically the cost of capital appropriate for an authentication/fintech company, **not** necessarily Itsme's own WACC. A higher risk profile means a higher discount rate and lower valuation.

4. **Synergies:** The acquisition may create additional value (cost savings, new revenue streams). Itsme should estimate synergies separately from the stand-alone value — they represent the maximum premium above intrinsic value it makes sense to pay.

5. **Maximum vs. minimum price:** The maximum Itsme should pay = stand-alone value + synergies. The minimum acceptable to NextAuth's owners = what they can get elsewhere (outside options).

> The recommended method is a **DCF model** (discounting projected free cash flows) or a **multiples approach** (P/E, EV/EBITDA of comparable authentication companies) as a cross-check.

---

### Q2.2 — Present Value of Growth Opportunities (PVGO)

**What is PVGO, why does it arise, and how is it estimated?**

**What it means:**
PVGO is the part of a stock's price that is **not** explained by its current earnings (assuming zero growth and full payout), but rather by the market's expectation of **future profitable growth**. It represents the present value of all future investment opportunities that generate returns above the cost of equity.

```
P₀ = EPS/r  +  PVGO
     ↑              ↑
  steady-state   value of
  (no-growth)    future growth
```

**Why PVGOs arise:**
PVGOs arise when a firm **retains earnings (plowback > 0)** AND reinvests them at a **return on equity (ROE) above the cost of equity (r)**:
- If ROE > r → reinvesting creates more value than paying out, so the market assigns extra value to future growth.
- If ROE = r → retaining vs. paying out makes no difference; PVGO = 0.
- If ROE < r → retaining destroys value; PVGO is negative (firm should pay out everything).

The dividend growth rate g = ROE × plowback ratio captures this mechanism.

**How to estimate PVGO:**
```
PVGO = P₀  −  EPS/r

where:
  P₀    = current share price (constant-growth DDM: Div₁/(r-g))
  EPS/r = benchmark value with zero growth and 100% payout ratio
  r     = cost of equity
```

---

### Q2.3 — Three Main Drivers of Bond Volatility (Modified Duration)

Bond volatility (%) = modified duration = **percentage change in bond price for a 1 percentage point change in YTM**. Three main drivers:

**1. Coupon rate (inverse relationship)**
- Higher coupon → **lower** duration → **lower** volatility.
- *Why:* A high-coupon bond returns more cash **sooner** (front-loaded), so its price is less sensitive to changes in the discount rate. In the extreme, a zero-coupon bond has the highest possible duration (= its maturity) because **all** cash is received at the very end.

**2. Time to maturity (positive relationship)**
- Longer maturity → **higher** duration → **higher** volatility.
- *Why:* A longer-maturity bond exposes the investor to interest rate changes for a longer period. Cash flows further in the future are affected more dramatically by a change in YTM because the discount factor (1+r)^t grows with t. Longer bonds thus have more "interest rate risk."

**3. YTM level (inverse relationship)**
- Lower YTM → **higher** volatility.
- *Why:* When yields are low, future cash flows are discounted less heavily, so they represent a larger share of the bond's current price. A small change in the (already-low) YTM therefore has a disproportionately large effect on price. Also: at low yield levels, rates are more likely to rise, amplifying the price risk further.

---

### Q2.4 — Capital Market Line (CML) vs. Securities Market Line (SML)

**CML:** `E(Rportfolio) = rf + [(E(Rm) - rf) / σm] × σportfolio`

**SML:** `E(Ri) = rf + βi × [E(Rm) - rf]`

**The essence of each:**

**CML — for efficient portfolios:**
The CML tells us the **minimum required expected return for a portfolio**, given its total risk (σ). Any rational investor should sit *on* this line — choosing a portfolio **below** the CML is irrational because you are not being compensated for the risk you carry. The slope of the CML is the **Sharpe ratio of the market portfolio** (return per unit of total risk), which is the best trade-off available. You always require at least the risk-free rate plus a premium for the extra risk you take on.

**SML — for individual securities:**
The SML tells us the **minimum required expected return for an individual security**, based on its **beta (systematic risk)** alone. This is the crucial insight of CAPM: for individual securities, **only systematic (market) risk is priced** because idiosyncratic risk can be diversified away for free. Investors are not compensated for carrying avoidable risk. A security plotting *above* the SML is underpriced (offers more return than required for its risk) — buy it. A security *below* the SML is overpriced — avoid or sell it.

**Key difference:** CML uses **total risk** (σ) and applies to **portfolios**. SML uses **systematic risk** (β) and applies to **individual securities**.

---

### Q2.5 — Diversification

**How diversification works:**
Diversification exploits the **imperfect correlation** between asset returns. When assets are not perfectly positively correlated (ρ < 1), combining them into a portfolio causes the positive deviations of one asset to be partially offset by the negative deviations of another. The portfolio variance formula shows this clearly:

```
σ²p = wA²σA² + wB²σB² + 2·wA·wB·ρ·σA·σB
```

When ρ < 1, the cross-term is reduced relative to the case ρ = 1 (perfect correlation), making portfolio risk **lower** than the weighted average of individual risks. The lower the correlation, the more powerful the diversification effect. In theory, if ρ = −1, all risk can be eliminated.

**What type of risk is eliminated:**
- ✅ **Idiosyncratic / unique / non-systematic risk** — firm-specific risk (e.g., a product recall, a management scandal) can be diversified away, because such events are uncorrelated across firms.
- ❌ **Systematic / market / non-diversifiable risk** — economy-wide shocks (recessions, interest rate changes, inflation) affect all firms simultaneously and cannot be diversified away. This remaining risk is captured by **beta** and is the only risk for which investors are compensated (per SML).

---

## QUESTION TYPE 3 — Large Quantitative Exercise (SRB)

**Financial data:**

| Item | Value |
|------|-------|
| Outstanding shares | 5,000,000 |
| Book value / share | €7 |
| **Market value / share** | **€8** |
| Market value of debt | €60,000,000 |
| Cost of debt (rd) | 7% |
| Tax rate | 30% |
| Cov(SRB returns, market returns) | 0.04 |
| Expected market return (Rm) | 9% |
| Std dev of market return (σm) | 14% |
| Risk-free rate (ST gov. bond) | 5% |

---

### Part a — Estimate SRB's Cost of Capital (WACC)

WACC is the company's **opportunity cost of capital** — the minimum return SRB must earn on any investment to create (rather than destroy) financial value for its investors. It is the appropriate discount rate for investment projects.

---

**Step 1 — Compute Beta (β)**

Beta measures SRB's systematic risk (sensitivity to market movements):

```
β = Cov(SRB, market) / Var(market)
  = 0.04 / (0.14)²
  = 0.04 / 0.0196
  = 2.041
```

> β = 2.041 means SRB's returns move ~2× as much as the market. This is a **high-risk stock** (e.g., a highly cyclical or leveraged company).

**TI-84:** `0.04 ÷ 0.14^2` → **2.041**

---

**Step 2 — Compute Cost of Equity (COE) via CAPM/SML**

```
COE = rf + β × (Rm − rf)
    = 5% + 2.041 × (9% − 5%)
    = 5% + 2.041 × 4%
    = 5% + 8.163%
    = 13.163%
```

> Shareholders of SRB require a **13.16% annual return** to compensate for the systematic risk they bear. This is derived from the SML — the minimum return justified by SRB's beta.

**TI-84:** `5 + 2.041 × (9 - 5)` → **13.163%**

---

**Step 3 — Compute Market Value Weights**

> Always use **market values** (not book values) for WACC weights, since WACC reflects what investors currently require.

```
Market value of equity (E) = 5,000,000 shares × €8 = €40,000,000
Market value of debt    (D) = €60,000,000
Total (D + E)               = €100,000,000

Weight equity: wE = 40/100 = 40%
Weight debt:   wD = 60/100 = 60%
```

---

**Step 4 — Compute WACC**

Debt interest is tax-deductible, so the effective cost of debt to the firm is rd × (1 − t):

```
WACC = wE × re + wD × rd × (1 − t)
     = 0.40 × 13.163% + 0.60 × 7% × (1 − 0.30)
     = 5.265% + 2.940%
     = 8.205%  ≈  8.21%
```

> **Interpretation:** SRB must earn at least **8.21%** on any investment project to satisfy both its shareholders (who require 13.16%) and its debt-holders (who require 7%, costing the firm only 4.90% after tax). Any project with NPV > 0 at this 8.21% discount rate creates value for SRB's investors.

**TI-84:** `0.40 × 13.163 + 0.60 × 7 × 0.70` → **8.205%**

---

### Part b — Which Proposal? (EAC Method)

**Why the Equivalent Annual Annuity (EAA) method?**

The two proposals have **different lifespans** (4 vs. 6 years). Since SRB is a **going concern**, it will need to replace the machinery repeatedly. A simple NPV comparison would favour the 6-year project merely because it lasts longer — that's not a fair comparison. The **EAA method** converts each project's NPV into an annual value, making the lifespans directly comparable. The EAA represents the annual value created, assuming perpetual replacement cycles.

**Formula:** `EAA = NPV / Annuity factor(r, n)`

**Additional assumption:** No salvage value or working capital changes (not mentioned; assume zero).

---

**Proposal A — CAPEX €400,000, 4-year life**

| Item | Calculation | Value |
|------|-------------|-------|
| Annual depreciation | 400,000 / 4 years | €100,000 |
| Revenue increase | given | +€175,000 |
| Operating cost increase | given | −€40,000 |
| Depreciation (non-cash) | | −€100,000 |
| **EBIT** | 175,000 − 40,000 − 100,000 | **€35,000** |
| Tax (30%) | 35,000 × 30% | −€10,500 |
| Net income | | €24,500 |
| + Add back depreciation | | +€100,000 |
| **Annual after-tax OCF** | | **€124,500** |

> Shortcut formula: `OCF = (ΔRevenue − ΔCosts − Depreciation) × (1−t) + Depreciation`
> = (175,000 − 40,000 − 100,000) × 0.70 + 100,000 = €124,500 ✓

```
Annuity factor (8.21%, 4 yr) = [1 − (1.0821)^(−4)] / 0.0821 = 3.297

NPV_A = −400,000 + 124,500 × 3.297 = −400,000 + 410,475 = €10,475

EAA_A = 10,475 / 3.297 = €3,177/year
```

**TI-84 for NPV_A:**
1. `APPS` → `Finance` → `NPV(`
2. Enter: `NPV(8.21, -400000, {124500,124500,124500,124500})` → **€10,475**

**TI-84 for EAA_A (solve for PMT given NPV as PV):**
1. `TVM Solver`: `N=4`, `I%=8.21`, `PV=-10475`, `FV=0`
2. Solve for `PMT` → **€3,177/year**

---

**Proposal B — CAPEX €500,000, 6-year life**

| Item | Calculation | Value |
|------|-------------|-------|
| Annual depreciation | 500,000 / 6 years | €83,333 |
| Revenue increase | given | +€190,000 |
| Operating cost increase | given | −€40,000 |
| Maintenance cost | given | −€5,000 |
| Depreciation (non-cash) | | −€83,333 |
| **EBIT** | 190,000 − 40,000 − 5,000 − 83,333 | **€61,667** |
| Tax (30%) | 61,667 × 30% | −€18,500 |
| Net income | | €43,167 |
| + Add back depreciation | | +€83,333 |
| **Annual after-tax OCF** | | **€126,500** |

```
Annuity factor (8.21%, 6 yr) = [1 − (1.0821)^(−6)] / 0.0821 = 4.594

NPV_B = −500,000 + 126,500 × 4.594 = −500,000 + 581,136 = €81,136

EAA_B = 81,136 / 4.594 = €17,660/year
```

**TI-84 for NPV_B:**
1. `NPV(8.21, -500000, {126500,126500,126500,126500,126500,126500})` → **€81,136**

**TI-84 for EAA_B:**
1. `TVM Solver`: `N=6`, `I%=8.21`, `PV=-81136`, `FV=0` → solve PMT → **€17,660/year**

---

**Decision:**

| | NPV | EAA |
|---|---|---|
| Proposal A (4 yr) | €10,475 | **€3,177/yr** |
| Proposal B (6 yr) | €81,136 | **€17,660/yr** |

**→ Proposal B is clearly preferred.** Its EAA is ~5.5× higher than Proposal A. Proposal B creates substantially more financial value per year of operation. Even though Proposal B requires a higher upfront investment (€500k vs. €400k) and lasts longer, its incremental revenues and lower relative depreciation burden make it far more profitable on an annualised basis.

---

### Part c — Impact of Higher Inventory on Financial Value

**Yes, holding more inventory will reduce the financial value generated by the project.**

Higher inventory = **increase in net working capital (NWC)**. Working capital is cash tied up in the business (inventory, receivables) that is not available for other uses. An increase in NWC is a **cash outflow** — it must be funded upfront.

In NPV analysis, an increase in working capital at the start of the project reduces the initial (t=0) cash flow, directly reducing NPV. If NWC continues to grow over the project's life, there are additional cash outflows in subsequent years. Working capital is typically recovered at the **end** of the project (when inventory is liquidated), which partly offsets the initial cost — but because of the **time value of money**, the present value of the recovery is less than the initial outflow.

**Conclusion:** More inventory → increase in working capital → additional cash outflow (not captured in operating cash flows) → **lower NPV** → less financial value created.

---

### Part d — Impact of Declining Balance Depreciation vs. Straight-Line

**Yes, switching to declining balance depreciation would increase the financial value generated by the project.**

Here is the key reasoning:

1. **Total depreciation is identical:** Regardless of the method, the total amount depreciated over the project's life equals the CAPEX. The total tax paid is also the same in nominal terms.

2. **But timing matters — time value of money:** Declining balance (degressive) depreciation **front-loads** the depreciation — larger depreciation amounts are charged in the early years. This means:
   - **Larger tax shields (= tax × depreciation) in early years** → more tax savings sooner
   - **Smaller tax shields in later years** → less saving, but those are further in the future

3. **Present value effect:** Because early cash flows are discounted less, the present value of front-loaded tax shields is **higher** than the present value of back-loaded (straight-line) tax shields.

**Conclusion:** Declining balance depreciation → front-loaded tax deductions → higher PV of tax shields → **higher NPV** → more financial value created. This is consistent with the course principle: *"Front-loading depreciation = lower taxes in the beginning = higher financial value."*

---

## QUESTION TYPE 4 — Capita Selecta / ACTUA

---

### Q4.1 — The GameStop Story (Feb 2021)

#### Part a — Story with Key Terms

GameStop was a struggling brick-and-mortar video game retailer. Large institutional investors (hedge funds) believed its stock was overvalued and took **short positions**: they borrowed GameStop shares and sold them, with the plan to buy them back later at a lower price and pocket the difference.

A group of retail investors, coordinated via the Reddit community r/WallStreetBets, noticed the extremely high short interest in GameStop and began buying shares aggressively (and call options). This drove the share price sharply upward.

As the price rose, the hedge funds' short positions began generating massive losses. Brokers enforcing **margin requirements** — minimum collateral that short-sellers must maintain — forced the hedge funds to either post more collateral or **close (cover)** their short positions by buying back GameStop shares. This buying pressure pushed the price even higher, which in turn forced other short-sellers to cover, creating a self-reinforcing feedback loop known as a **short squeeze**.

GameStop's stock went from ~$20 to nearly $500 within weeks, causing billions in losses for institutional short-sellers.

#### Part b — EMH Implications

**What EMH means:** The Efficient Market Hypothesis (EMH) states that stock prices at all times **reflect all available information**, so no investor can consistently earn abnormal returns. In its semi-strong form, prices reflect all publicly available information; in its strong form, even private information is already priced in.

**The GameStop story challenges EMH** on several levels:
- The dramatic price surge was **not driven by any change in GameStop's fundamental value** (the company was still struggling). The price move was entirely driven by coordinated speculative buying and the mechanics of a short squeeze.
- This is evidence of **market inefficiency**: prices deviated massively from fundamental value for weeks — a prolonged deviation that EMH would say should not persist.
- The event supports **behavioral finance** explanations: herding behavior, retail FOMO (fear of missing out), and irrational exuberance drove prices far beyond what fundamentals justify.
- However, consistent with a weaker form of EMH, prices eventually collapsed back toward fundamental value, suggesting that in the **long run**, markets do tend to correct mispricings.

**Academic conclusion:** The GameStop episode is a real-world illustration that markets can be temporarily inefficient, with prices driven by behavioral and mechanical forces rather than information about fundamental value.

---

### Q4.2 — Long-Call Option Position

#### Part a — What is a Long-Call and Why is the Profit/Loss Asymmetric?

A **long-call position** means **buying a call option**. By paying a premium (the option price) today, the buyer acquires the **right — but not the obligation** — to purchase the underlying asset at the agreed **strike price (K)** on or before the **expiry date**.

The profit/loss profile is **asymmetric** because of the optionality:

- **If stock price (S) at expiry < K:** The option is "out of the money." The buyer has no reason to exercise (why buy at K when you can buy cheaper in the market?). The option expires worthless. **Loss = premium paid** (this is the maximum possible loss — it is limited and known upfront).

- **If stock price (S) at expiry > K:** The option is "in the money." The buyer exercises: buys at K, immediately has an asset worth S. **Profit = (S − K) − premium**. This profit grows linearly and is theoretically unlimited as S rises.

This creates the characteristic **asymmetric "hockey stick" shape**: a flat section at (−premium) for S < K, then an upward-sloping line once S > K. The asymmetry is the core value proposition of options — **limited downside, unlimited upside**.

#### Part b — What Risk Does a Long-Call Hedge? Example.

**Risk hedged:** A long-call hedges against the risk of a **future price increase** in an asset that the company **needs to buy** (an input, commodity, or currency).

**Specific example:**

An **airline company (e.g., Ryanair or Lufthansa)** has large and predictable future fuel (jet kerosene) purchases. If oil prices spike, operating costs surge and profits collapse. By buying **call options on crude oil (or jet fuel)**, the airline:
- **Caps its maximum fuel cost** at the strike price + premium paid, no matter how high oil goes.
- **Still benefits** if fuel prices fall (unlike a forward contract): it simply lets the option expire and buys fuel at the (lower) market price.

This gives the airline certainty in budgeting and protects its profit margin against the key input cost risk it faces.

---

*End of model answers.*
