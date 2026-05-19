# CH2: Financial Algebra — KU Leuven Study Guide

---

## 0. The Big Picture

Every topic in this chapter is a variation of one core idea:

> **A euro today is worth more than a euro in the future** — because money invested today earns interest.

All formulas are just ways to move cash flows forward or backward in time.

---

## 1. Compound vs. Simple Interest

### 1.1 Compound Interest

**Formula:**
```
FV = PV × (1 + r)^t
```
- `PV` = Present Value (money you have today)
- `FV` = Future Value (money you'll have at time t)
- `r` = annual interest rate (as a decimal, e.g. 5% → 0.05)
- `t` = number of years

**Why this formula?**
Each year your balance grows by factor `(1+r)`. After t years you have multiplied by `(1+r)` exactly t times:
- End of year 1: PV × (1+r)
- End of year 2: PV × (1+r) × (1+r) = PV × (1+r)²
- End of year t: PV × (1+r)^t

**Real example (10% on €100):**

| Year | Start | Interest earned | End |
|------|-------|-----------------|-----|
| 1    | 100   | 10              | 110 |
| 2    | 110   | 11 (interest ON interest!) | 121 |
| 3    | 121   | 12.1            | 133.1 |
| 10   | 236   | 24              | 259 |
| 100  | 1,252,783 | 125,278      | 1,378,061 |
| 200  | 17.3 trillion | ... | 19 trillion |

**Key insight:** Growth is *exponential*. The longer the horizon, the more dramatic the effect.

### 1.2 Simple Interest

**Formula:**
```
FV = PV × (1 + r × t)
```

Interest is earned only on the original principal — it is **not reinvested**.

**Same example (10% on €100):**

| Year | Start | Interest | End |
|------|-------|----------|-----|
| 1    | 100   | 10       | 110 |
| 2    | 110   | 10 (always on original 100) | 120 |
| 10   | 190   | 10       | 200 |
| 100  | 1,090 | 10       | 1,100 |

**Growth is linear.** At year 200: only €2,100 vs €19 trillion with compounding!

### Common mistakes here:
- **Using simple interest when compound is required.** In finance, almost everything uses compound interest unless explicitly stated otherwise.
- **Forgetting to convert % to decimal:** `r = 5%` means use `0.05`, not `5`.
- **Off-by-one on t:** If you invest today and want the value after 3 full years, `t = 3`. Do not use `t = 4`.

---

## 2. Time Value of Money (TVM)

### Core concepts

| Term | Definition | Formula |
|------|-----------|---------|
| **Future Value (FV)** | How much a current amount grows to | `FV = PV × (1+r)^t` |
| **Present Value (PV)** | Today's worth of a future cash flow | `PV = FV / (1+r)^t` |
| **Discount Rate (r)** | Rate used to bring future cash flows back to today | given |
| **Discount Factor (DF)** | PV of €1 received at time t | `DF = 1 / (1+r)^t` |

### The PV formula explained

```
PV = FV / (1+r)^t   =   FV × [1/(1+r)^t]   =   FV × DF_t
```

You are asking: *"How much do I need to invest today at rate r to have FV in t years?"*

**Intuition:** Dividing by `(1+r)^t` "un-grows" the money back to today.

### Worked examples:
```
FV of €100 at 7% for 2 years:
FV = 100 × (1.07)² = 100 × 1.1449 = €114.49

PV of €300 received in 6 years at 4%:
PV = 300 / (1.04)⁶ = 300 / 1.2653 = €237.10
```

### Common mistakes here:
- **Mixing up PV and FV:** PV is always the earlier (smaller) value; FV is the later (larger) value.
- **Wrong sign convention:** Investments are outflows (negative), receipts are inflows (positive).
- **Forgetting opportunity cost:** The discount rate represents what you *could* earn elsewhere at similar risk — not just a bank rate.

---

## 3. Periodicity of Interest Rates

### The Problem

A "6% annual rate compounded monthly" is NOT the same as 6% effective annually.

### Key Terms

| Term | Meaning |
|------|---------|
| **APR** (Annual Percentage Rate / nominal rate) | Stated annual rate — does NOT account for compounding within year |
| **Periodic rate** | Rate per compounding period = APR / m |
| **EAR** (Effective Annual Rate = real rate) | The actual yearly rate after accounting for within-year compounding |
| **m** | Number of compounding periods per year |

### Formula: APR → EAR

```
EAR = (1 + APR/m)^m  - 1
```

**Why?** If you apply the periodic rate `APR/m` exactly `m` times in a year, you compound up by `(1 + APR/m)^m`. Subtract 1 to get just the interest portion.

**Examples:**
```
6% APR compounded monthly (m=12):
EAR = (1 + 0.06/12)^12 - 1 = (1.005)^12 - 1 = 0.0617 = 6.17%

6% APR compounded daily (m=365):
EAR = (1 + 0.06/365)^365 - 1 ≈ 6.18%
```
→ More frequent compounding = higher effective rate.

### Formula: EAR → Periodic rate

```
Periodic rate = (1 + EAR)^(1/m) - 1
```

**Example:**
```
EAR = 5.5%, find the semi-annual rate (m=2):
Semi-annual rate = (1.055)^(1/2) - 1 = (1.055)^0.5 - 1 ≈ 2.703%

EAR = 5.5%, find the monthly rate (m=12):
Monthly rate = (1.055)^(1/12) - 1 ≈ 0.447%
```

### Multi-year rates (same logic!)

The same formula works across years, not just within a year:
```
5-year return given 3% annual:
(1.03)^5 - 1 = 15.93%

Required annual rate to achieve 10% over 5 years:
(1.10)^(1/5) - 1 = 1.923% per year
```

### FV/PV with sub-annual compounding

When compounding m times per year, the general formula becomes:
```
FV = PV × (1 + APR/m)^(m×t)
```

**Example:** €400,000 at 5% APR compounded semi-annually (m=2) for 3 years:
```
FV = 400,000 × (1 + 0.05/2)^(2×3)
   = 400,000 × (1.025)^6
   = 400,000 × 1.1597
   = €463,880
```

### Common mistakes here:
- **Using APR directly as the interest rate when compounding is sub-annual.** Always check the compounding frequency.
- **Confusing m and t:** `m` is periods per year, `t` is years. The total number of periods is `m × t`.
- **Assuming APR = EAR:** Banks advertise APR (lower-looking number). The real return/cost is EAR.
- **Dividing instead of raising to power:** To go from EAR to monthly rate, you take the **12th root** `(1+EAR)^(1/12)`, NOT divide by 12.

---

## 4. Present Value of Cash Flow Streams

### The Principle

Sum the present values of each individual cash flow:

```
PV = CF₁/(1+r)¹ + CF₂/(1+r)² + CF₃/(1+r)³ + ... + CFₙ/(1+r)ⁿ
```

Each cash flow is discounted at the rate appropriate for its timing.

### Net Present Value (NPV)

```
NPV = -Initial Investment + PV of all future cash flows
```

**Decision rule:** Accept a project if `NPV > 0`.

**Why NPV > 0 means "yes"?**
It means the project creates more value than investing the same money at rate r elsewhere.

### Rate of Return (ROR) Rule — equivalent to NPV rule

```
ROR = (Profit) / (Investment cost)
```
Accept if `ROR > r` (opportunity cost).

**Example:**
```
Invest €370,000 today, receive €420,000 next year, r = 5%:

NPV = -370,000 + 420,000/1.05 = -370,000 + 400,000 = +30,000 > 0 → ACCEPT

ROR = (420,000 - 370,000) / 370,000 = 50,000/370,000 = 13.5% > 5% → ACCEPT
```
Both rules give the same answer.

### Changing discount rates

Technically possible but rarely used. **Critical constraint:** Discount factors must always decrease over time:
```
DF₁ > DF₂ > DF₃ > ...
i.e., 1/(1+r₁) > 1/(1+r₂)² > ...
```
If violated, a lower discount rate for a far-future period than a near-future one creates **arbitrage opportunities** (risk-free profit), which is economically inconsistent.

**Example of violation:**
```
r₁ = 20%: DF₁ = 1/1.20 = 0.83
r₂ = 7%:  DF₂ = 1/(1.07)² = 0.87
0.83 < 0.87 → VIOLATION → arbitrage possible
```
The arbitrage: invest at 20% to get €1 at t=1, borrow against a €1 liability at t=2 discounted at 7% → pocket the difference risk-free today.

### Common mistakes here:
- **Forgetting the minus sign on the initial investment in NPV.**
- **Discounting the year-0 cash flow:** Cash flows at t=0 are already at today's value. Never discount them.
- **Using a lower discount rate for risky projects:** Higher risk → higher r → lower NPV. Never justify a project by lowering the discount rate.

---

## 5. Annuities

### What is an annuity?

A **fixed payment C** made (or received) at **regular intervals** for a **finite number of periods t**.

- Post-numerando (ordinary annuity): first payment at end of year 1 ← **default assumption**
- Pre-numerando (annuity due): first payment today (beginning of year 1)

### PV of an Annuity (post-numerando)

```
PV = C × [1/r - 1/(r × (1+r)^t)]
   = C × [(1 - 1/(1+r)^t) / r]
```

This is called the **annuity factor**.

**Why this formula?** It's the geometric sum of t discount factors:
```
PV = C/(1+r) + C/(1+r)² + ... + C/(1+r)^t
```
Applying the formula for a geometric series gives the compact formula above.

**Example:**
```
€100/year for 5 years, r = 5%:
PV = 100 × [(1 - 1/(1.05)^5) / 0.05]
   = 100 × [(1 - 0.7835) / 0.05]
   = 100 × [0.2165 / 0.05]
   = 100 × 4.329
   = €432.90
```

### FV of an Annuity (post-numerando)

```
FV = C × [(1+r)^t - 1) / r]
```

Relation to PV: `FV = PV × (1+r)^t` — just compound the PV forward.

**Example:**
```
$20,000/year for 5 years, r = 8%:
FV = 20,000 × [(1.08)^5 - 1) / 0.08]
   = 20,000 × [0.4693 / 0.08]
   = 20,000 × 5.867
   = $117,340
```

### Solving for C (the payment)

Rearrange PV formula:
```
C = PV × r / (1 - 1/(1+r)^t)
```

**Use case:** "How much must I save each year to accumulate €50,000 in 30 years at 3%?"
```
C = FV × r / ((1+r)^t - 1)
C = 50,000 × 0.03 / ((1.03)^30 - 1)
C = 1,500 / 1.4268
= €1,051 per year
```

### Pre-numerando (Annuity Due)

Two equivalent approaches:

**Method 1 — Multiply by (1+r):**
```
PV_pre = PV_post × (1+r)
```
The first payment is now instead of in 1 year, so everything is worth one period more.

**Method 2 — Decompose:**
Take the immediate cash flow out, then price the remaining (t-1) payments as a regular annuity:
```
PV_pre = C + C × [(1 - 1/(1+r)^(t-1)) / r]
```

**Example: Lottery with payments starting now (annuity due):**
```
25 payments of €20,000, r = 6%, first payment today:
PV_post = 20,000 × [(1 - 1/(1.06)^25) / 0.06] = €255,667
PV_pre  = 255,667 × 1.06 = €271,007
```

### Common mistakes with annuities:
- **Assuming post-numerando when the problem says "starting today" or "beginning of year."** Always read carefully.
- **Using the annuity formula when cash flows are unequal.** The annuity formula requires all C to be identical. If amounts differ, discount each separately.
- **Forgetting to check what r represents.** If payments are monthly and r is annual, convert to monthly rate first: `r_monthly = (1+r_annual)^(1/12) - 1`.
- **Using APR directly for monthly payments.** Use `r_monthly = APR/12` only if the problem specifies APR compounded monthly; otherwise use the EAR-based conversion.

---

## 6. Perpetuities

### Perpetuity

A **fixed payment C forever** (infinite annuity).

```
PV = C / r
```

**Why?** The geometric sum `C/(1+r) + C/(1+r)² + ...` with infinitely many terms converges to `C/r` (valid because `|1/(1+r)| < 1`).

**Example:** $1,000/year forever at 10%:
```
PV = 1,000 / 0.10 = $10,000
```

### Growing Perpetuity

Cash flows grow at constant rate g each year:
- Year 1: C
- Year 2: C(1+g)
- Year 3: C(1+g)²
- ...

```
PV = C / (r - g)        [requires r > g]
```

**Example:** €100 at end of year 1, growing at 2% forever, r = 10%:
```
PV = 100 / (0.10 - 0.02) = 100 / 0.08 = €1,250
```

**Why r > g must hold:** If g ≥ r, the series diverges to infinity (an asset that grows faster than your discount rate would be worth an infinite amount, which is economically impossible for real assets).

### Common mistakes with perpetuities:
- **Using g > r:** Always verify r > g before applying the growing perpetuity formula.
- **Using r% and g% without converting to decimals:** e.g., r=10, g=4 gives 10-4=6, but you need (0.10 - 0.04) = 0.06.
- **Forgetting the first cash flow is at END of year 1** (post-numerando assumption). If it starts now, multiply by (1+r).
- **Confusing growth rate g with interest rate r:** g describes how the cash flows change; r is your required return.

---

## 7. Two-Step Models

### When to use

When you have a finite annuity period followed by a perpetuity (or growing perpetuity) that starts afterward.

**Structure:**
```
Years 1–t:  Fixed cash flow C  (ordinary annuity)
Year t+1 onwards: Cash flows grow at g forever (growing perpetuity)
```

**Steps:**

1. **Price the annuity** for years 1 to t using the annuity PV formula.

2. **Price the growing perpetuity** at time t (i.e., one period before the first growing cash flow):
```
PV_at_t = C_{t+1} / (r - g)
```

3. **Discount that perpetuity value back** to today:
```
PV_today_of_perpetuity = PV_at_t / (1+r)^t
```

4. **Add both parts:**
```
Total PV = Annuity PV + PV_today_of_perpetuity
```

**Example:**
€150/year for 4 years, then growing at 1% forever, r = 5%:

```
Step 1: PV of annuity (years 1–4)
  = 150 × [(1 - 1/(1.05)^4) / 0.05] = 150 × 3.546 = €531.90

Step 2: PV of growing perpetuity AT t=4
  First cash flow at t=5 = 150 × (1.01) = €151.50
  PV₄ = 151.50 / (0.05 - 0.01) = 151.50 / 0.04 = €3,787.50

Step 3: Discount PV₄ back to today
  PV₀ = 3,787.50 / (1.05)^4 = 3,787.50 / 1.2155 = €3,116.33

Step 4: Total PV = 531.90 + 3,116.33 = €3,648.23
```

### Buy/Hold/Sell decision:
- Market price < PV → **Buy** (undervalued)
- Market price = PV → **Hold**
- Market price > PV → **Sell** (overvalued)

### Common mistakes with two-step models:
- **Timing the perpetuity wrong.** The formula `C/(r-g)` gives PV *one period before* the first cash flow. If the first growing cash flow is at t=5, the formula gives the value at t=4 — then discount back 4 more periods.
- **Using year-t cash flow instead of year-(t+1).** The perpetuity formula uses the *next* payment after t.
- **Forgetting to add both parts together.**

---

## 8. Summary of All Formulas

| Concept | Formula |
|---------|---------|
| Compound FV | `FV = PV × (1+r)^t` |
| Compound PV | `PV = FV / (1+r)^t` |
| Simple interest | `FV = PV × (1 + r×t)` |
| Discount Factor | `DF = 1/(1+r)^t` |
| APR → EAR | `EAR = (1 + APR/m)^m - 1` |
| EAR → periodic | `r_periodic = (1 + EAR)^(1/m) - 1` |
| FV with m periods/yr | `FV = PV × (1 + APR/m)^(m×t)` |
| PV of annuity | `PV = C × [(1 - 1/(1+r)^t) / r]` |
| FV of annuity | `FV = C × [(1+r)^t - 1) / r]` |
| Annuity due (pre-num.) | `PV_pre = PV_post × (1+r)` |
| Perpetuity | `PV = C / r` |
| Growing perpetuity | `PV = C / (r - g)` |
| NPV | `NPV = -Cost + Σ CFₜ/(1+r)^t` |

---

## 9. Master List of Easy Mistakes to Avoid

| # | Mistake | Correct approach |
|---|---------|-----------------|
| 1 | Using % instead of decimal | 5% → 0.05 |
| 2 | Discounting t=0 cash flows | Never discount year-0; it's already "today" |
| 3 | APR = EAR | Only equal when m=1 (annual compounding) |
| 4 | Dividing by m instead of taking mth root | EAR → monthly: `(1+EAR)^(1/12) - 1`, not EAR/12 |
| 5 | Wrong t in FV = PV(1+r)^t | Count full periods, not calendar years ambiguously |
| 6 | Pre vs. post-numerando confusion | "Starting end of year" = post; "starting today/now" = pre |
| 7 | Annuity formula with unequal cash flows | Must discount each separately |
| 8 | Growing perpetuity with g ≥ r | Formula breaks down; r must exceed g |
| 9 | Two-step: wrong timing for perpetuity PV | `C/(r-g)` is at t before first growing CF |
| 10 | Positive NPV but ROR < r | Impossible — check arithmetic; they must agree |
| 11 | Mixing annual r with monthly payments | Convert r to match payment frequency |
| 12 | Simple vs. compound interest | Finance uses compound unless stated otherwise |
| 13 | Changing discount rates violating DF₁>DF₂ | Check that discount factors decrease monotonically |
| 14 | Ignoring risk in discount rate | Higher risk → higher r → lower PV |

---

## 10. Intuition Cheat Sheet

- **Higher r** → lower PV (future money worth less today)
- **Longer t** → lower PV of a single future cash flow
- **More frequent compounding** → higher EAR for same APR
- **Annuity PV** < t × C (you'd rather have all money now)
- **Perpetuity** = annuity with t → ∞; annuity factor → 1/r
- **Growing perpetuity**: denominator shrinks as g → r → PV explodes
- **NPV > 0** = the project earns more than your opportunity cost
- **Pre-numerando** is always worth more than post-numerando (same cash flows, just earlier)
