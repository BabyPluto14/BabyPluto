# STATISTICS — EXPANDED STUDY GUIDE
## Part 2: Time Series Regression
### Cautions · Autocorrelation · Stationarity · Dynamic Models

---

> **How to use this guide.** This document expands every section of the original notes with deeper
> explanations, intuition, and additional examples. Each original concept is preserved; everything
> extra is marked or woven in as extended explanation. Read it alongside your formula sheet.

---

## Overview — The Time-Series Workflow

When you apply regression to time-series data you face three challenges that simply do not exist in
cross-section analysis: **autocorrelation**, **non-stationarity**, and **dynamic effects**. The four-step
workflow below is your roadmap through all of them.

| Step | Chapter | Core question |
|------|---------|---------------|
| **Recognise** | TS_A — Cautions | Is my data time series? Do I understand lags and differences? |
| **Diagnose** | TS_B — Autocorrelation | Are errors correlated over time? |
| **Stabilise** | TS_C — Stationarity | Do my variables drift or wander? Could results be spurious? |
| **Model** | TS_D — Dynamic models | How do I capture lagged effects and interpret them? |

### The Exam Recipe (three steps in every question)

1. **Stationarity check** — time plot + Dickey-Fuller on every variable. If a unit root is found, take
   first differences.
2. **Fit the model** — the question tells you whether it is static, DL(q), or AR(1). For DL(q), find
   the optimal lag length. Report coefficients and the total multiplier.
3. **Check assumptions** — run the LMSC test on the residuals. Report H₀/H₁, the LM statistic,
   the p-value, and your conclusion.

### Why Time Series Adds Three Issues on Top of Multiple Regression

Everything from Part 1 (multiple regression) still applies: OLS, t-tests, F-test, R², the five classical
assumptions, residual diagnostics, multicollinearity, heteroskedasticity. Time series simply adds:

- **Autocorrelation** — Assumption A3 (uncorrelated errors) fails because shocks persist over time.
  Today's unexpected event still influences tomorrow's residual.
- **Spurious regression / non-stationarity** — Variables that share a common trend appear
  statistically related even when they have no genuine economic connection.
- **Dynamic effects** — In most economic processes, a change in X does not instantly produce its
  full effect on Y. The effect is spread across many periods; we need models that capture this.

---

## CHAPTER TS_A — Cautions

*Differences between cross-section and time-series data; lags and differences*

### A.1 — Cross-Section vs. Time-Series Data

#### Definitions

| Type | Description | Notation | Order matters? |
|------|-------------|----------|---------------|
| **Cross-section** | Many units at one point in time | X_i, subscript *i* = individual | No — rows are interchangeable |
| **Time-series** | One unit observed repeatedly over time | X_t, subscript *t* = time period | **Yes** — shuffling destroys information |
| **Panel data** | Many units over many time periods | X_{it} | Both dimensions matter |

#### Why Order Matters

In a cross-section of 1,000 workers you could randomly reorder the rows and your regression
results would be identical. In a time series of 40 years of GDP data, row 5 (GDP in year 5) *must*
come after row 4 and before row 6. The temporal structure is not a nuisance — it is the entire
point.

#### Example — Hourly Wage

- **Cross-section:** A survey of 500 Belgian employees in 2010, each row one person. You can sort
  by name, age, sector — the regression of wage on education gives the same answer.
- **Time series:** Average Belgian hourly wage in 1980, 1981, …, 2015. The rows must follow
  calendar order. Regressing wage_t on time_t captures how wages evolved; shuffling would
  produce nonsense.

---

### A.2 — Lagged Variables

#### What a Lag Is

A **lag** simply refers to the value of a variable at an earlier time period. If the current period is
quarter 3 of 1987:

| Notation | Meaning | Value refers to |
|----------|---------|-----------------|
| X_t | Current value of X | Q3 1987 |
| X_{t−1} | One-period lag | Q2 1987 |
| X_{t−2} | Two-period lag | Q1 1987 |
| X_{t−q} | q-period lag | q quarters before Q3 1987 |

#### Why Lags Are Needed

Economic processes rarely respond instantaneously. Consider safety training:

- Hours of safety training are delivered in month t.
- Workers need time to absorb the training and change behaviour.
- The reduction in accidents appears in months t+1, t+2, etc.

A model without lags would miss most of the effect. Lags let us model this delay explicitly.

#### SPSS Instructions

```
Transform → Create Time Series
  Function: Lag
  Order: 1  → creates X_{t-1}
  Order: 2  → creates X_{t-2}
  (one new variable per order)
Internal variable name: LAG(varname, 1), LAG(varname, 2), …
```

#### Watch Out: Lost Observations

Each lag of order q costs you **q observations** at the start of the series. The lag X_{t−1} is
undefined for the first observation (there is no "period zero"). More generally:

- Lag of order 1 → you lose **1** observation (row 1 has no X_{t−1}).
- Lag of order q → you lose **q** observations (rows 1 through q).

So if you start with n = 100 and compute a DL(3) model, your usable sample is only n − 3 = 97.
With short time series (n < 50) this can be a serious constraint — each extra lag wastes precious
degrees of freedom.

---

### A.3 — Difference Variables

#### Definition

The **first difference** of X_t is the change from one period to the next:

$$\Delta X_t = X_t - X_{t-1}$$

This is an **absolute** first difference. For a **seasonal** difference of order 12 (removing
year-on-year seasonality in monthly data):

$$\Delta_{12} X_t = X_t - X_{t-12}$$

#### Interpretation

| Original variable | After differencing | Meaning |
|------------------|--------------------|---------|
| GDP level (€ billions) | ΔGDP | Change in GDP vs. previous period |
| log(GDP) | Δlog(GDP) = log(GDP_t / GDP_{t-1}) | **Log-return** ≈ percentage growth rate |
| Monthly unemployment (%) | Δ unemployment | Change in unemployment rate (pp) |
| log(price) | Δlog(price) | Percentage price change (return) |

The log-return formula deserves special attention because it appears frequently:

$$\Delta \ln(X_t) = \ln(X_t) - \ln(X_{t-1}) = \ln\!\left(\frac{X_t}{X_{t-1}}\right) \approx \frac{X_t - X_{t-1}}{X_{t-1}}$$

So differencing log-transformed data gives you approximate percentage changes — which is why
finance uses log-returns extensively.

#### SPSS Instructions

```
Transform → Create Time Series
  Function: Difference (absolute)       → ΔX_t = X_t − X_{t-1}
  Function: Percentage change           → relative difference version
Internal name: DIFF(varname, 1), DIFF(varname, 2), …
```

#### Why Differences Matter

1. **Economic theory talks about changes.** Most macro/micro theories describe how *changes*
   in X affect *changes* in Y. Differences align your model with theory.
2. **They cure a stochastic trend (unit root).** If X_t is a random walk (X_t = X_{t-1} + ε_t),
   then ΔX_t = ε_t, which is white noise — stationary. Differencing removes the non-stationarity.
3. **Log-returns are scale-free.** The percentage change in stock price A is directly comparable
   to the percentage change in stock price B even if they are priced very differently.

---

### A.4 — The Three Problems with Time-Series Regression

Every time you run a regression on time-series data, you must address three specific issues. The
rest of this guide is organised around them.

#### Problem 1 — Data Quality and Sample Size

Time-series regression is **data-hungry**. Unlike cross-section regression where adding more
observations is easy (survey more people), adding more time-series observations means waiting
for more years to pass — or finding historical data that may not exist.

**Rules of thumb:**

| Situation | Recommendation |
|-----------|---------------|
| Ideal | n > 100 observations |
| Minimum | n ≈ 35; at least 10 obs per X-variable in the model |
| Yearly data | May need 35+ years; consider monthly or quarterly if available |
| Monetary variables | Use **real (deflated)** values — inflation creates artificial trends |

**Why inflation matters:** If you regress nominal wages on nominal GDP, both series may trend
upward simply because of inflation, not because of any real relationship. Always use inflation-
adjusted (real) values for monetary variables to avoid confusing price-level changes with genuine
economic relationships.

#### Problem 2 — Autocorrelation

Classical Assumption A3 states that errors are uncorrelated: cov(ε_i, ε_j) = 0. In time-series
data this is routinely violated. Shocks have persistence — if something unexpected happens
today (a policy surprise, a weather event, a demand shock), its effect on Y persists into next
period, and the period after, gradually fading. This means today's residual is correlated with
yesterday's residual.

Consequences and solutions are covered in **Chapter TS_B**.

#### Problem 3 — Spurious Regression / Non-Stationarity

Imagine regressing Belgian ice cream sales on annual sunspot activity. Both series happen to
trend upward over a 30-year window. You would find a hugely significant regression with R² = 0.95
— even though ice cream sales and sunspots have absolutely nothing to do with each other. The
culprit is that both series are **non-stationary**: their means drift over time.

The solution is to ensure all variables are stationary before fitting the regression. Details are in
**Chapter TS_C**.

---

## CHAPTER TS_B — Autocorrelation

*Errors that remember the past: detection with the LMSC test*

### B.1 — Which Classical Assumption is Violated?

#### The Five Classical Assumptions (Recap)

The OLS estimator is **BLUE** (Best Linear Unbiased Estimator) when the Gauss-Markov conditions
hold. Written for a time-series regression Y_t = β₀ + β₁X_{1t} + … + β_k X_{kt} + ε_t:

| Assumption | Formal statement | Plain English |
|-----------|-----------------|---------------|
| A1 | E(ε_t) = 0 | Errors average to zero |
| **A2** | Var(ε_t) = σ² (constant) | Homoskedasticity — errors have equal spread |
| **A3** | cov(ε_t, ε_s) = 0 for t ≠ s | Errors are uncorrelated with each other |
| A4 | X's non-random, not perfectly collinear | No perfect multicollinearity |
| A5 (optional) | ε ~ Normal | For exact inference in small samples |

**Autocorrelation violates A3.** When errors are correlated over time, cov(ε_t, ε_{t-1}) ≠ 0.

#### Why A3 Fails So Commonly in Time Series

Think of the residual ε_t as "everything that moves Y but isn't in my model." In time-series
settings, omitted variables themselves tend to persist over time (institutional inertia,
technology cycles, business cycles). So today's omitted shock tends to carry over into tomorrow,
making consecutive errors similar.

**Intuitive example:** You model monthly consumer spending using only income. But consumer
confidence, which you haven't measured, also drives spending — and consumer confidence is
*persistent* (it stays high for several months, then gradually declines). The residuals will
therefore form waves: positive for a stretch (when confidence is high), then negative for a
stretch (when confidence is low). That is positive autocorrelation.

---

### B.2 — First-Order Autocorrelation

#### The AR(1) Error Structure

We model the autocorrelation in the error term as a first-order autoregressive process:

$$\varepsilon_t = \rho \, \varepsilon_{t-1} + u_t$$

where:
- ρ (rho) is the **first-order autocorrelation coefficient** (a number between −1 and 1)
- u_t is a **classical white-noise error** — it is uncorrelated, has mean zero, and constant variance

This says: today's error is a fraction ρ of yesterday's error, plus a new fresh shock u_t.

#### Understanding the Size of ρ

| Value of |ρ| | Interpretation |
|------------|---------------|
| ρ = 0 | No autocorrelation. ε_t = u_t, purely random noise — A3 satisfied. |
| 0 < |ρ| < 0.3 | Weak autocorrelation. Standard errors mildly affected. |
| 0.3 < |ρ| < 0.7 | Moderate autocorrelation. Noticeable distortion of standard errors. |
| |ρ| > 0.7 | Strong autocorrelation. Inference seriously unreliable. |
| |ρ| = 1 | Unit root in the error — errors wander without bound. The entire model is unstable. |
| |ρ| > 1 | Explosive errors — ε_t grows without limit. Meaningless model. |

We require **−1 < ρ < 1** for the error process itself to be stationary and well-behaved.

#### Understanding the Sign of ρ

| Sign | Pattern in residuals | Typical cause in economics |
|------|---------------------|---------------------------|
| **ρ > 0** (positive) | Residuals form long runs: a stretch of positive values, then a stretch of negative values. Looks like "waves" in the residual plot. | Very common. Business cycles, omitted trending variables, sluggish adjustment. |
| **ρ < 0** (negative) | Residuals alternate sign every period: + − + − + − ... Looks like a "zigzag" in the residual plot. | Rare in economics. Can arise from over-differencing (taking too many differences). |

**Worked analogy for ρ = 0.7:** If this quarter's residual is +10 (meaning Y was 10 units above
prediction), next quarter's residual is expected to be +7 (= 0.7 × 10). The quarter after, +4.9. Then
+3.4, then +2.4, then +1.7, and so on — slowly decaying toward zero. A shock takes many periods
to fade.

---

### B.3 — Consequences of Autocorrelation

#### General Case (Static or DL(q) Models)

When A3 is violated in a model without lagged Y:

| Property | With autocorrelation |
|----------|---------------------|
| OLS estimators β̂ | Still **unbiased** — on average they hit the true β |
| OLS estimators β̂ | No longer **best** (not BLUE) — a better estimator exists |
| Standard errors | **Wrong** — they use the wrong formula (one that assumes A3) |
| t-tests and F-tests | **Invalid** — built on wrong standard errors |
| Confidence intervals | **Wrong width** — too narrow if ρ > 0 (falsely precise), too wide if ρ < 0 |
| R² | Unaffected but potentially misleading |

The key danger is **false significance**: positive autocorrelation inflates t-statistics, making
coefficients appear more significant than they really are. You think you have found a strong
relationship when the apparent precision is an artefact.

#### Exception: AR(1) Models (Lagged Dependent Variable)

When the regression contains Y_{t−1} as a regressor **and** there is autocorrelation in ε:

$$Y_t = \alpha + \beta X_t + \gamma Y_{t-1} + \varepsilon_t \quad \text{with } \text{cov}(\varepsilon_t, \varepsilon_{t-1}) \neq 0$$

The problem is now much worse: the coefficient **estimates themselves become biased**. The
reason is subtle but important: Y_{t−1} is a function of ε_{t−1}. If ε_t is correlated with
ε_{t−1}, then Y_{t−1} is correlated with ε_t — this violates Assumption A4 (X's must be
non-random and uncorrelated with the error). When that happens, OLS is no longer even
unbiased.

**Practical rule:** If you detect autocorrelation in an AR(1) model, you must re-specify the model
(e.g., switch to DL(q)). The estimated γ̂ and β̂ cannot be trusted.

---

### B.4 — Detection: The LMSC Test

#### Step 0 — Graphical Inspection First

Always **plot the residuals against time** before running any test. Look for:

- **Waves** (long runs above or below zero) → suggests positive autocorrelation, ρ > 0.
- **Zigzag** (alternating signs) → suggests negative autocorrelation, ρ < 0.
- **Random scatter** (no visible pattern) → A3 plausibly satisfied.

This visual check is fast and gives context to the formal test. An exam question may ask you to
describe the plot before running LMSC.

#### The LMSC Test — Full Procedure

**Hypotheses:**
- H₀: ρ = 0 (no autocorrelation — A3 satisfied)
- H₁: ρ ≠ 0 (autocorrelation present — A3 violated)

**Step 1:** Fit the original regression model (the one you are checking). Save the residuals e_t.

**Step 2:** Build the **auxiliary regression**. Regress the residuals on all the original predictors
X_{1t}, …, X_{kt} **plus** the lagged residual e_{t−1}:

$$e_t = \alpha_0 + \alpha_1 X_{1t} + \cdots + \alpha_k X_{kt} + \alpha_{k+1} e_{t-1} + u_t$$

Why include the original X's? To partial out their variation and isolate the pure autocorrelation
signal in e_{t−1}. If we omitted the X's, the test could pick up correlation arising from the X's
rather than the error process.

**Step 3:** From the auxiliary regression output, read R² and compute:

$$LM = n \cdot R^2$$

where n is the sample size of the **auxiliary** regression (= n_original − 1, because you lose
one observation for e_{t−1}).

**Step 4:** Under H₀, the LM statistic follows a **chi-squared distribution with 1 degree of
freedom**: LM ~ χ²(1). Compare LM to the critical value (χ²(1, 5%) = 3.841) or use the
reported p-value.

**Decision:**
- If LM > 3.841 (or p-value < 0.05): **Reject H₀** → autocorrelation is present.
- If LM ≤ 3.841 (or p-value ≥ 0.05): **Do not reject H₀** → A3 plausibly satisfied.

#### Higher-Order Tests

The procedure above tests for first-order autocorrelation only (e_{t−1} in the auxiliary
regression). To test for autocorrelation up to order p, add e_{t−1}, e_{t−2}, …, e_{t−p} to
the auxiliary regression. The LM statistic then follows χ²(p) under H₀.

**Important:** The sample size in the auxiliary regression becomes n − p (you lose p observations
for the p lagged residuals).

#### Worked Example — Phillips Curve (Australian Quarterly Data)

**Original model:** Y_t = β₀ + β₁X_t + ε_t
- Y = inflation rate (%), X = change in unemployment rate (pp)
- n = 90 quarterly observations (1987Q1 to 2009Q3)

**Auxiliary regression results:**

| Item | Value |
|------|-------|
| n for auxiliary regression | 90 − 1 = **89** |
| R² of auxiliary regression | **0.310211** |
| Coefficient on e_{t−1} | **0.558** (t = 6.219, p < .001) |

**Computation:**

$$LM = n \cdot R^2 = 89 \times 0.310211 = 27.609$$

$$p\text{-value} = P(\chi^2(1) \geq 27.609) \approx 1.5 \times 10^{-7}$$

**Conclusion:** Reject H₀ at any reasonable significance level. Autocorrelation is strongly
present. The Phillips curve model with only current unemployment change is misspecified — we
are missing the dynamic structure. A DL(q) or AR(1) extension is needed.

#### Durbin–Watson as an Alternative

SPSS automatically prints the **Durbin–Watson (DW)** statistic in regression output.

| DW value | Interpretation |
|----------|---------------|
| Close to **2** | No autocorrelation |
| Close to **0** | Strong positive autocorrelation (ρ near +1) |
| Close to **4** | Strong negative autocorrelation (ρ near −1) |
| Between 1.5 and 2.5 | Generally acceptable (rough rule) |

**Critical limitation:** Durbin–Watson is **invalid** whenever the regression contains a lagged
dependent variable (i.e., in any AR(1)-type model). The LMSC test does not have this limitation
and should be your default. Use DW only as a quick sanity check on static or DL(q) models, and
always confirm with LMSC.

**Relationship between DW and ρ:**

$$DW \approx 2(1 - \hat{\rho})$$

So DW = 2 when ρ̂ = 0, DW = 0 when ρ̂ = 1, and DW = 4 when ρ̂ = −1. This gives you a back-of-
the-envelope estimate of ρ from the DW statistic.

---

### B.5 — Solutions for Autocorrelation

#### Why Not Just Use a "Better" Standard Error?

More advanced fixes exist — **Generalized Least Squares (GLS)** and **Newey-West/HAC
(Heteroskedasticity and Autocorrelation Consistent) standard errors**. GLS corrects the
estimator itself; HAC corrects only the standard errors while keeping OLS coefficients. These are
valid approaches but are *not exam material* in this course.

#### The Exam Approach: Re-specify the Model

The philosophy here is that autocorrelation in a static model usually indicates **model
misspecification** — the error is carrying memory because you left out dynamics. Adding lags
directly into the model absorbs this dynamic structure:

| Re-specification | What you add | Model type |
|-----------------|-------------|-----------|
| Add lagged X's | X_{t−1}, X_{t−2}, …, X_{t−q} | **DL(q)** — Distributed Lag |
| Add lagged Y | Y_{t−1} | **AR(1)** — Autoregressive |

#### DL(q) vs. AR(1) — Which to Choose?

| Criterion | DL(q) preferred | AR(1) preferred |
|-----------|----------------|----------------|
| Residual autocorrelation present | ✓ Yes — DL is only inefficient, not biased | ✗ AR is biased with residual autocorrelation |
| Multicollinearity concern | ✗ DL with many lags is collinear (past X's are similar) | ✓ AR uses only 2 coefficients |
| Long memory needed | ✗ Need many lags = many parameters | ✓ β/(1−γ) captures infinite lag with 2 params |
| **Bottom line** | **Safer when autocorrelation is present** | **More parsimonious when A3 satisfied** |

The key principle: **bias is worse than inefficiency**. DL with autocorrelation gives wrong
standard errors (bad but fixable). AR with autocorrelation gives wrong coefficient estimates
(fundamentally misleading).

---

## CHAPTER TS_C — Stationarity

*Spurious regression, the generalized AR(1), and the Dickey-Fuller test*

### C.1 — Spurious Regression

#### The Problem

Consider this scenario: regress Belgian GDP per capita (1950–2004) on US population density
over the same period. You find:
- R² ≈ 0.96 (extremely high)
- Slope coefficient significant at p < 0.001
- Everything looks like a remarkably strong relationship

Yet Belgian GDP and US population density have **no meaningful economic relationship**. This
is a **spurious regression** — a statistically convincing result that is economically meaningless.

#### Why It Happens: Shared Trends

Both Belgian GDP and US population density happened to grow over the same 54-year period. The
regression is picking up their **common time trend**, not any genuine relationship. If two series
both go up over time — for any reason, including purely by chance — regressing one on the other
will produce high R² and significant t-statistics.

A more dramatic example: the number of Nicolas Cage films released per year is spuriously
correlated with the number of drowning deaths in swimming pools in the US (a real example from
the "spurious correlations" literature). Both happened to move similarly between 1999 and 2009.

#### The Root Cause: Non-Stationarity

The mathematical reason spurious regression occurs is that both variables are
**non-stationary**: their means and/or variances are not constant over time. Standard regression
theory requires stationarity. When it fails, the usual asymptotic results break down, t-statistics
do not follow a t-distribution, and R² does not converge to a meaningful population value.

**Stationarity is therefore a new assumption** that must be added to the five classical
assumptions whenever you work with time-series data.

---

### C.2 — Definition of Stationarity

#### Formal Definition (Weak/Covariance Stationarity)

A time series Y_t is **weakly stationary** if, for every t:

1. **E(Y_t) = μ** — The expected value (mean) is constant. The series oscillates around a fixed level and does not drift up or down.
2. **Var(Y_t) = σ²** — The variance is constant. The series does not become progressively more or less volatile.
3. **Cov(Y_t, Y_{t−s}) = γ_s** — The covariance between observations s periods apart depends only on the gap s, not on when in time you measure it.

The third condition means that the correlation structure is **time-invariant** — the relationship
between Y today and Y five periods ago is the same in 1990 as it is in 2010.

#### Intuitive Test: The "Cut in Half" Check

Plot the time series. Visually divide it into two halves. If the left half and right half:
- Have similar **average levels** → mean is constant → good sign
- Have similar **spread/volatility** → variance is constant → good sign
- Show similar **patterns of up-and-down oscillation** → covariance structure is similar → good sign

If the right half is systematically higher, more volatile, or shows different patterns, you have
evidence of non-stationarity.

#### Graphical Warning Signs

| What you see in the time plot | What it suggests |
|------------------------------|-----------------|
| Clear upward or downward trend | Non-stationary mean |
| Seasonal pattern that appears to grow or shrink | Non-stationary variance |
| Series wanders widely, rarely returning to a fixed level | Stochastic trend (random walk) |
| Variance increases over time (e.g., trumpet shape) | Heteroskedasticity / non-constant variance |
| Flat, random noise around a constant level | Likely stationary |

For a formal, objective verdict — always run the **Dickey-Fuller test** (Section C.6).

---

### C.3 — The Generalized AR(1) Model

#### The Unifying Framework

The behaviour of any univariate time series can be studied through the **generalized AR(1)**:

$$Y_t = a + \lambda t + \rho Y_{t-1} + \varepsilon_t$$

where ε_t is white noise: independent draws from N(0, σ²).

The three parameters determine everything:
- **a** — the constant (intercept)
- **λ** — the coefficient on time t (slope of deterministic trend)
- **ρ** — the autoregressive coefficient (how strongly past Y predicts current Y)

The **critical question** is whether **|ρ| < 1** (stationary family) or **|ρ| = 1** (random walk family).

#### The Four Cases

---

**Case 1 — Basic AR(1):** |ρ| < 1, a = 0, λ = 0

Model: Y_t = ρ Y_{t-1} + ε_t

By substituting the equation for Y_{t−1} back into Y_t, then Y_{t−2} back in, and so on indefinitely:

$$Y_t = \varepsilon_t + \rho \varepsilon_{t-1} + \rho^2 \varepsilon_{t-2} + \cdots + \rho^t Y_0$$

This is an **infinite moving average** of all past shocks, with geometrically declining weights.

Properties:
| Property | Formula | Stationarity check |
|----------|---------|-------------------|
| Mean | E(Y_t) ≈ 0 | ✓ Constant |
| Variance | Var(Y_t) = σ²/(1−ρ²) | ✓ Constant (requires |ρ| < 1) |
| Covariance | Cov(Y_{t−s}, Y_t) = σ²ρˢ/(1−ρ²) | ✓ Depends only on lag s |
| Autocorrelation | r(Y_{t−s}, Y_t) = ρˢ | Decays exponentially to 0 |

**✓ STATIONARY** — All three conditions satisfied.

**Example:** Y_t = 0.7 Y_{t−1} + ε_t. A shock of +10 in period t leaves a memory of 7 in period t+1,
4.9 in t+2, 3.4 in t+3, …, eventually dying out. The series constantly reverts to 0.

---

**Case 2 — AR(1) with constant:** |ρ| < 1, a ≠ 0, λ = 0

Model: Y_t = a + ρ Y_{t-1} + ε_t

Properties:
| Property | Formula |
|----------|---------|
| Mean | μ = a/(1−ρ) |
| Variance | σ²/(1−ρ²) — same as Case 1 |
| Covariance | Same structure as Case 1 |

All three are constant in t. **✓ STATIONARY** — but now around a non-zero mean μ = a/(1−ρ).

**Intuition for the mean formula:** In long-run equilibrium, Y_t = Y_{t−1} = μ (no expected change).
Substituting: μ = a + ρμ → μ(1−ρ) = a → μ = a/(1−ρ). This is just the long-run value where
the autoregression settles.

**Example:** Y_t = 5 + 0.6 Y_{t−1} + ε_t. Long-run mean = 5/(1−0.6) = 12.5. The series oscillates
around 12.5, never drifting away permanently.

---

**Case 3 — AR(1) with deterministic trend:** |ρ| < 1, a ≠ 0, λ ≠ 0

Model: Y_t = a + λt + ρ Y_{t-1} + ε_t

The λt term makes the mean grow linearly over time. By the formal definition, the series is
**not stationary** (the mean changes with t). However, the **deviation from the trend line** is
stationary.

Define the trend-adjusted series: Ỹ_t = Y_t − μ − δt, where:

$$\delta = \frac{\lambda}{1-\rho}, \qquad \mu = \frac{a - \rho\delta}{1-\rho}$$

Then Ỹ_t is a stationary AR(1) process about zero.

**✗ NOT STATIONARY** (in the level Y_t), but **✓ stationary about a deterministic trend**.

**Fix:** Add t as a regressor in the regression (see C.5, Fix A).

**Example:** Y_t = 1 + 0.05t + 0.7 Y_{t−1} + ε_t
- δ = 0.05/(1−0.7) = 1/6 ≈ 0.167 (trend growth per period)
- μ = (1 − 0.7 × 1/6)/(1−0.7) = (1 − 0.1167)/0.3 = 0.8833/0.3 ≈ 2.944

So Y_t − 2.944 − 0.167t is a stationary process. Y_t itself grows at about 0.167 units per period.

---

**Case 4 — Random Walk:** |ρ| = 1

When ρ = 1, the formula Y_t = a + ρ Y_{t-1} + ε_t becomes Y_t = a + Y_{t-1} + ε_t. There are
three sub-cases:

| Sub-case | Model | Mean behaviour | Variance behaviour |
|----------|-------|---------------|-------------------|
| Pure random walk (a=0, λ=0) | Y_t = Y_{t-1} + ε_t | E(Y_t) = Y_0 (constant) | Var(Y_t) = tσ² → **grows without bound** |
| Random walk with drift (a≠0, λ=0) | Y_t = a + Y_{t-1} + ε_t | E(Y_t) = ta + Y_0 → **drifts up/down** | Also grows with t |
| With drift and trend (a≠0, λ≠0) | Y_t = a + λt + Y_{t-1} + ε_t | Even faster drift | Even faster variance growth |

**✗ ALL NON-STATIONARY.** The variance growing without bound is the most damaging property —
standard results completely break down.

**Why the variance explodes in a random walk:**
Y_t = Y_0 + ε_1 + ε_2 + … + ε_t (by repeated substitution)
Var(Y_t) = Var(ε_1) + Var(ε_2) + … + Var(ε_t) = tσ²

Each period adds another independent shock. The series accumulates all past shocks equally —
none of them fade. This is fundamentally different from Case 1 where past shocks had weights ρˢ
that decay to zero.

**Fix:** Take first differences. If Y_t = Y_{t-1} + ε_t then ΔY_t = ε_t — white noise, stationary (see C.5, Fix B).

#### Summary Card

| Case | ρ | λ | Stationary? | Fix |
|------|---|---|-------------|-----|
| Basic AR(1) | |ρ|<1 | 0 | ✓ Yes | None needed |
| AR(1) + constant | |ρ|<1 | 0 | ✓ Yes | None needed |
| AR(1) + deterministic trend | |ρ|<1 | ≠0 | ✗ No (has trend) | Add t to regression / detrend |
| Random walk | |ρ|=1 | any | ✗ No | Take first differences |

---

### C.4 — Deterministic vs. Stochastic Trends

This distinction matters enormously because the two types of non-stationarity require
**different fixes**. Applying the wrong fix can make things worse.

| Feature | Deterministic Trend | Stochastic Trend (Random Walk) |
|---------|--------------------|-----------------------------|
| Mathematical source | λt term in the model | |ρ| = 1 |
| Mean | Changes predictably over time (grows by λ per period) | May drift, but unpredictably |
| **Variance** | **Constant** | **Grows with time** |
| Shocks | Temporary — series returns to trend after a shock | Permanent — series never fully recovers |
| Example | Belgian unemployment has seasonal peaks in winter (deterministic seasonality) | S&P 500 stock price index |
| **Correct fix** | **Detrend** (subtract trend) or add t as regressor | **First difference** |
| Wrong fix | First-differencing over-differences → creates negative autocorrelation | Detrending doesn't remove stochastic trend |

**Intuition for the permanence of shocks:**
- With a deterministic trend: a shock in period t pushes Y above the trend line, but in subsequent
  periods Y reverts back to the same trend. The shock is absorbed.
- With a random walk: a shock in period t is permanently incorporated into the level of the series.
  All future values are shifted by exactly that shock amount — forever. The series has no "memory"
  of where it "should" be.

**When in doubt:** Use the Dickey-Fuller test with a trend term (Version 2) — it accommodates
both possibilities and is the conservative choice.

---

### C.5 — Solutions for Non-Stationarity

#### Fix A — Deterministic Trend (|ρ| < 1, λ ≠ 0)

**Option 1 — Detrending:**
Estimate the trend (regress Y_t on t) and subtract it:
Ỹ_t = Y_t − μ̂ − δ̂t (the residuals from this auxiliary regression)
Then use Ỹ_t in place of Y_t in all subsequent analysis.

**Option 2 — Model the trend explicitly (preferred in practice):**
Simply include t as an additional regressor in your main model:

$$Y_t = \beta_0 + \beta_1 X_t + \lambda t + \varepsilon_t$$

This is equivalent to Option 1 but is simpler — you let OLS handle the detrending
simultaneously. The coefficient on t absorbs the linear trend; the coefficient on X_t now
measures the relationship *after controlling for the common time trend*.

**Option 3 — Seasonal differencing:**
For data with seasonality (monthly, quarterly), use:
Δ₁₂X_t = X_t − X_{t−12}

This removes any pattern that repeats annually. Example: Belgian monthly unemployment is
systematically higher in January (summer vacation workers returning) and lower in April. Seasonal
differencing removes this deterministic seasonal pattern.

#### Fix B — Stochastic Trend / Unit Root (|ρ| = 1)

**Take first differences.** This is the only valid fix for a random walk.

$$\Delta Y_t = Y_t - Y_{t-1}, \quad \Delta X_t = X_t - X_{t-1}$$

**Why it works:** If Y_t is a random walk, Y_t = Y_{t-1} + ε_t, then:
ΔY_t = Y_t − Y_{t-1} = ε_t
ε_t is white noise — it is stationary. The difference operation strips away the unit root.

**How many times to difference?**
- If Y_t has one unit root → take **first differences** ΔY_t (this is "integrated of order 1", I(1))
- If ΔY_t still has a unit root → take **second differences** Δ²Y_t = ΔY_t − ΔY_{t−1}
- Most macroeconomic series need only one round of differencing.

**Worked example — Belgian GDP and GNI (1950–2004):**
- Both series trend strongly upward. Regressing levels gives R² ≈ 0.99 — spurious.
- Dickey-Fuller on levels: fail to reject H₀ (unit root present) for both.
- Take first differences (or log-differences = growth rates).
- Dickey-Fuller on differences: strongly reject H₀ (stationary).
- Regression of ΔGDP on ΔGNI now has a sound statistical interpretation.

---

### C.6 — The Dickey-Fuller Test

#### Purpose

The Dickey-Fuller test is a **formal unit root test**: it decides whether ρ = 1 (non-stationary) or
|ρ| < 1 (stationary). It converts a visual judgment into a rigorous hypothesis test.

#### Hypotheses

- **H₀: ρ = 1** — the series has a unit root, is NOT stationary
- **H₁: |ρ| < 1** — the series IS stationary (possibly about a deterministic trend)

**Note the asymmetry:** H₀ is the dangerous case (non-stationarity). We want to reject H₀.
**Failing to reject H₀ means we cannot prove stationarity** — we assume the series needs
differencing.

#### The Reparameterisation Trick

Instead of testing H₀: ρ = 1 directly (which is awkward), subtract Y_{t-1} from both sides:

$$Y_t - Y_{t-1} = a + \lambda t + (\rho - 1) Y_{t-1} + \varepsilon_t$$
$$\Delta Y_t = a + \lambda t + \alpha_1 Y_{t-1} + \varepsilon_t$$

where **α₁ = ρ − 1**. Now:
- H₀: ρ = 1 ⟺ **α₁ = 0**
- H₁: |ρ| < 1 ⟺ **α₁ < 0** (must be negative since ρ < 1 means ρ−1 < 0)

We test whether α₁ is significantly **negative** — a one-sided test.

#### The Two Versions

| Version | Regression | When to use |
|---------|-----------|-------------|
| **Version 1 — no trend** | ΔY_t = α₀ + α₁ Y_{t−1} + ε_t | No visible trend in time plot |
| **Version 2 — with trend** | ΔY_t = α₀ + λt + α₁ Y_{t−1} + ε_t | Clear trend in time plot, or when unsure |

Version 2 is the **safer default**: if a trend is present but you use Version 1, your test is
misspecified. If no trend is present but you use Version 2, you merely lose one degree of freedom
— a minor cost.

#### Adapted Critical Values

Under H₀ the usual t-distribution **does not apply**. The distribution of the test statistic under
a unit root is non-standard (the Dickey-Fuller distribution). You **must** use the special table:

| DF Version | 1% critical value | 5% critical value | 10% critical value |
|-----------|-------------------|-------------------|--------------------|
| Version 1 (no trend) | −3.43 | **−2.86** | −2.57 |
| Version 2 (with trend) | −3.96 | **−3.41** | −3.13 |

**Decision rule:** Reject H₀ (conclude stationarity) if and only if the t-statistic on Y_{t−1} is
**more negative** than the critical value.

**Example:** t-stat = −3.10. With Version 1 at 5% level: −3.10 is more negative than −2.86 → Reject H₀
→ stationary. With Version 2 at 5% level: −3.10 is NOT more negative than −3.41 → Fail to reject → unit root.

The choice of version matters! Always look at the time plot first.

#### Procedure (4 Steps)

1. **Plot Y_t against time.** Does it trend? Choose Version 1 (no trend) or Version 2 (trend, or unsure).
2. **Create ΔY_t** (first difference of Y) and Y_{t−1} (one lag of Y).
3. **Run the chosen DF regression** (ΔY_t on Y_{t−1}, plus t for Version 2).
4. **Find the t-statistic for the coefficient of Y_{t−1}**. Compare to the adapted critical values.

#### What to Do After the DF Test

| DF result | Action |
|-----------|--------|
| Reject H₀ (stationary) | Use the series **in levels** in your model |
| Fail to reject H₀ (unit root) | Take **first differences**, then re-run DF on ΔY_t |
| DF on ΔY_t: Reject H₀ | ΔY_t is stationary; use **first differences** in the model |
| DF on ΔY_t: Still fail to reject | Rare. Consider second differences or other treatments |

---

### Reference — Mean of a Stationary AR(1) (Formula Sheet)

| Model | Stationarity | Long-run mean |
|-------|-------------|---------------|
| Y_t = ρ Y_{t-1} + ε_t | ✓ Stationary | μ = 0 |
| Y_t = a + ρ Y_{t-1} + ε_t | ✓ Stationary | μ = a/(1−ρ) |
| Y_t = a + λt + ρ Y_{t-1} + ε_t | ✗ Not stationary (has trend) | Stationary about μ + δt, where δ = λ/(1−ρ) and μ = (a−ρδ)/(1−ρ) |

---

## CHAPTER TS_D — Dynamic Models

*DL(q), AR(1), total multipliers, and the time-series exam workflow*

### D.1 — Distributed Lag Model DL(q)

#### Motivation

A **static model** assumes the entire effect of X on Y is instantaneous:

$$Y_t = \alpha + \beta_0 X_t + \varepsilon_t$$

But most economic effects have **delayed responses**:
- A tax cut today may not fully boost consumption until next quarter.
- Training employees today reduces accidents over the next several months.
- An interest rate rise starts affecting mortgage payments immediately but only slows the
  housing market after several months.

The **Distributed Lag model of order q** captures these delays by including the current and
q lagged values of X:

$$Y_t = \alpha + \beta_0 X_t + \beta_1 X_{t-1} + \beta_2 X_{t-2} + \cdots + \beta_q X_{t-q} + \varepsilon_t$$

The effect of X is **distributed across** q+1 periods — hence the name.

#### Interpretation of Coefficients

Each β_k is interpreted *ceteris paribus* — holding all other X variables constant:

**β_k = the average change in Y_t when X_{t−k} rises by 1 unit, all other lagged values of X held constant.**

But the most practically useful comparison is between a **temporary** and a **maintained** 1-unit
rise in X:

| Type of change | Interpretation | Effect at lag k |
|---------------|---------------|----------------|
| **Temporary** (X rises by 1, then returns to original level) | β_k is the additional effect k periods after the rise | Effect dies out beyond lag q |
| **Maintained** (X rises by 1 and stays there permanently) | Sum of all β₀ + β₁ + … + β_k = cumulative effect after k periods | Total effect after q or more periods = **total multiplier** = Σβ_k |

#### The Total Multiplier

$$\text{Total multiplier} = \sum_{k=0}^{q} \beta_k = \beta_0 + \beta_1 + \cdots + \beta_q$$

**Interpretation:** The total multiplier is the **long-run effect on Y of a permanent 1-unit
increase in X**. It answers: "If X goes up by 1 unit and stays there forever, by how much will Y
eventually change?"

#### SPSS Setup

```
1. Transform → Create Time Series → Lag → Order 1, 2, …, q
   (creates X_{t-1}, X_{t-2}, …, X_{t-q})

2. Analyze → Regression → Linear
   Dependent: Y_t
   Independent(s): X_t, X_{t-1}, X_{t-2}, …, X_{t-q}

3. Note: sample size is now n − q (lost observations due to lags)
```

---

### D.2 — Choosing the Optimal Lag Length q

#### Why Not Just Include All Lags?

Including too many lags creates problems:
1. **Lost observations:** each lag costs one more observation.
2. **Multicollinearity:** X_t, X_{t-1}, X_{t-2} are typically very similar to each other — their
   correlation is high. This inflates standard errors for all coefficients.
3. **Overfitting:** unnecessary lags soak up degrees of freedom without improving model quality.

#### The Top-Down Procedure

Start from a maximum lag q_max (given in the exam question, typically 3 or 4) and progressively
drop the highest lag that is not significant:

1. Fit DL(q_max). Check the t-test for β_{q_max}.
2. If β_{q_max} is **not significant**: drop lag q_max, refit DL(q_max − 1).
3. Repeat until the highest remaining lag is **significant**.
4. That is your **optimal lag length q**.

**Important:** Once you find the optimal q, do **not** drop intermediate insignificant lags. If β_2
is significant but β_1 is not, you still keep both in the model — you cannot have lag 2 without
lag 1, as this would create a gap in the lag structure with no theoretical justification.

#### Worked Example — Safety Training and Accident Losses

Goal: model monthly accident losses (Y, in euros) as a function of monthly safety training hours
(X), with q_max = 4.

| Step | Model fitted | Result | Action |
|------|-------------|--------|--------|
| 1 | DL(4) | β₄: t = 0.83, p = 0.41 (not significant) | Drop lag 4 |
| 2 | DL(3) | β₃: t = 1.21, p = 0.23 (not significant) | Drop lag 3 |
| 3 | DL(2) | β₂: t = 1.56, p = 0.12 (not significant) | Drop lag 2 |
| 4 | DL(1) | β₁: t = −2.87, p = 0.005 (significant) | **Stop. Optimal q = 1** |

The final model is: Ŷ_t = α̂ + β̂₀ X_t + β̂₁ X_{t−1}

Report:
- **Immediate effect:** β̂₀ (effect of training hours this month on losses this month)
- **One-period lagged effect:** β̂₁ (effect of training hours last month on losses this month)
- **Total multiplier:** β̂₀ + β̂₁

---

### D.3 — Autoregressive Model AR(1)

#### From Distributed Lags to Autoregression

Instead of explaining today's Y by past values of X, the AR(1) model lets **past Y** carry the
memory of the system:

$$Y_t = \alpha + \beta X_t + \gamma Y_{t-1} + \varepsilon_t$$

**Why include Y_{t−1}?** Because in many economic processes, the current state of Y is the
best single predictor of the next state. Consumer spending this quarter depends heavily on
consumer spending last quarter (habits, contracts, inertia). GDP growth this year is correlated
with GDP growth last year (momentum, investment cycles). By including Y_{t−1}, we capture
all these persistence effects in a single coefficient γ.

#### Interpreting the Coefficients

| Coefficient | Interpretation |
|-------------|---------------|
| α | Intercept (no direct economic interpretation without X) |
| **β** | The **immediate effect**: a 1-unit rise in X_t causes Y_t to rise by β, holding Y_{t−1} constant |
| **γ** | The **persistence coefficient**: how much of last period's Y carries forward. Requires |γ| < 1 for stationarity |
| **β/(1−γ)** | The **total multiplier**: long-run effect of a permanent 1-unit rise in X |

#### The Total Multiplier Formula

$$\text{Total multiplier (AR1)} = \frac{\beta}{1 - \gamma}$$

This formula requires **|γ| < 1** (stationarity condition). If |γ| ≥ 1, the model is non-stationary
and the total multiplier is undefined (or infinite).

**Proof sketch:** In long-run equilibrium, Y_t = Y_{t−1} = Y* (steady state). Then:
Y* = α + β X* + γ Y* → Y*(1−γ) = α + β X* → Y* = α/(1−γ) + [β/(1−γ)] X*

So a 1-unit permanent increase in X* raises long-run Y* by β/(1−γ).

#### Dynamic Path After a Temporary Shock

Suppose X rises by 1 unit only in period t and then returns to its original value:

| Period | Additional effect on Y (above baseline) |
|--------|----------------------------------------|
| t | β (immediate response) |
| t+1 | γ · β (Y_{t} was elevated by β, so Y_{t+1} inherits γ×β) |
| t+2 | γ² · β |
| t+3 | γ³ · β |
| … | … |
| t+k | γ^k · β |

The effect decays geometrically at rate γ. If γ = 0.8, only 20% of the shock is "absorbed" per
period — it takes a long time to fade.

#### Worked Example — Education Spending and GDP Growth

**Data:** Yearly US data since 1910.
- X_t = education spending per child (dollars)
- Y_t = GDP growth rate (%)

**Fitted AR(1) model:**
Ŷ_t = 1.01 + 0.009 X_t + 0.627 Y_{t−1}

| Component | Value | Meaning |
|-----------|-------|---------|
| α̂ | 1.01 | Baseline growth when X = 0 and Y_{t−1} = 0 |
| β̂ | 0.009 | A $1 increase in per-child spending raises GDP growth by 0.009 pp immediately |
| γ̂ | 0.627 | 62.7% of last year's GDP growth persists into this year |
| **Total multiplier** | 0.009/(1−0.627) = **0.024** | A **permanent** $1/child spending increase raises long-run GDP growth by 0.024 pp |

**Worked Dynamic Path Example:**
Suppose spending rises by $1 in year 5 only.

| Year | Additional GDP growth |
|------|----------------------|
| 5 | 0.009 |
| 6 | 0.627 × 0.009 = 0.00564 |
| 7 | 0.627² × 0.009 = 0.00354 |
| 8 | 0.627³ × 0.009 = 0.00222 |
| … | decaying to 0 |
| Sum (∞) | 0.009/(1−0.627) = **0.024** |

The cumulative effect of the temporary $1 shock is also 0.024 pp (same as the total multiplier,
which is always the case for a permanent change).

---

### D.4 — Link Between AR(1) and DL(∞)

#### Why the Total Multiplier is β/(1−γ)

We can show that AR(1) is secretly an infinite distributed lag model. Substitute Y_{t−1} into the
AR(1) equation, then Y_{t−2}, and continue indefinitely:

$$Y_t = \alpha + \beta X_t + \gamma Y_{t-1} + \varepsilon_t$$
$$= \alpha + \beta X_t + \gamma(\alpha + \beta X_{t-1} + \gamma Y_{t-2} + \varepsilon_{t-1}) + \varepsilon_t$$
$$= \alpha(1+\gamma) + \beta X_t + \beta\gamma X_{t-1} + \gamma^2 Y_{t-2} + \gamma\varepsilon_{t-1} + \varepsilon_t$$

Continuing to infinity:

$$Y_t = \frac{\alpha}{1-\gamma} + \beta X_t + \beta\gamma X_{t-1} + \beta\gamma^2 X_{t-2} + \beta\gamma^3 X_{t-3} + \cdots + \varepsilon_t'$$

This is a DL(∞) model with **geometrically declining lag coefficients**: β, βγ, βγ², βγ³, …

#### Total Multiplier from the Geometric Series

$$\text{Total multiplier} = \sum_{k=0}^{\infty} \beta\gamma^k = \beta \sum_{k=0}^{\infty} \gamma^k = \beta \cdot \frac{1}{1-\gamma} = \frac{\beta}{1-\gamma}$$

This uses the geometric series formula 1 + q + q² + … = 1/(1−q), which requires |q| < 1 — i.e.,
|γ| < 1 (the stationarity condition).

#### AR(1) vs. DL(q): A Full Comparison

| Feature | DL(q) | AR(1) |
|---------|-------|-------|
| Lag structure | q+1 free coefficients β₀, β₁, …, β_q | Geometric decay — only β and γ |
| Parameters needed | q+1 | 2 |
| Multicollinearity | High for large q (lags of X are correlated) | Low (only one lag of Y needed) |
| Bias when A3 violated | Unbiased (only inefficient) | **Biased** |
| Standard hypothesis tests | Approximately valid | Approximately valid (if A3 satisfied) |
| Lag structure flexibility | Completely flexible | Constrained to geometric decay |
| When to prefer | When autocorrelation is suspected; when flexible lag profile needed | When parsimony matters; when A3 is satisfied |

#### The ARDL(p, q) Extension

The general model with p lags of Y and q lags of X is the **Autoregressive Distributed Lag** model:

$$Y_t = \alpha + \sum_{j=1}^{p} \gamma_j Y_{t-j} + \sum_{k=0}^{q} \beta_k X_{t-k} + \varepsilon_t$$

AR(1) is the special case ARDL(1, 0). DL(q) is ARDL(0, q). ARDL is not exam material in this
course but is the workhorse of modern applied time-series econometrics.

---

### D.5 — The Three-Step Exam Workflow

This is the complete procedure for any time-series regression exam question.

#### Step 1 — Stationarity Check (Chapter TS_C)

For **each** variable in the model:

1. Plot the series against time. Does it trend up/down? Does variance change? Are there visible seasonal patterns?
2. Based on the plot, choose:
   - **No trend visible** → Dickey-Fuller Version 1
   - **Clear trend** or **unsure** → Dickey-Fuller Version 2
3. Run the DF regression, read the t-statistic for the coefficient on Y_{t−1}.
4. Compare to adapted critical values (−2.86 for V1 at 5%, −3.41 for V2 at 5%).
5. **Reject H₀** → series is stationary → use in levels.
6. **Fail to reject H₀** → unit root → take first difference, then re-run DF on ΔY_t.

#### Step 2 — Fit the Model (Chapter TS_D)

The exam question specifies the model type. Use the stationary variables (levels or differences).

**For DL(q):**
- Start with q = q_max (given in the question).
- Drop highest non-significant lag; repeat until highest lag is significant.
- Report all coefficients and the total multiplier = Σβ_k.
- Interpret: "A [temporary/maintained] 1-unit rise in X [leads to/eventually leads to] a [β₀ / total multiplier] unit change in Y."

**For AR(1):**
- Fit Y_t = α + β X_t + γ Y_{t-1} + ε_t directly.
- Report β, γ, and total multiplier = β/(1−γ).
- Interpret the total multiplier: "A permanent 1-unit rise in X raises the long-run level of Y by β/(1−γ)."

**Log-return interpretation:** If variables were log-differenced (ΔlnX, ΔlnY), interpret
coefficients as percentage-point changes, not unit changes.

#### Step 3 — Assumption Check with LMSC (Chapter TS_B)

1. **State hypotheses clearly:**
   - H₀: no autocorrelation (ρ = 0)
   - H₁: autocorrelation present (ρ ≠ 0)

2. **Write the auxiliary regression:**
   e_t = α₀ + α₁ X_{1t} + … + α_k X_{kt} + α_{k+1} e_{t−1} + u_t
   (include all original regressors plus the lagged residual)

3. **Compute:**
   LM = n_aux × R²_aux ~ χ²(1) under H₀
   (n_aux = n − 1 for first-order test)

4. **Compare to critical value:** χ²(1, 5%) = 3.841.

5. **Conclude:**
   - LM > 3.841 or p-value < 0.05: Reject H₀ → autocorrelation detected → consider re-specifying
   - LM ≤ 3.841 or p-value ≥ 0.05: Fail to reject H₀ → A3 plausibly satisfied ✓

Also briefly note the other classical assumptions: homoskedasticity (check residual vs. fitted plot),
normality of residuals (histogram/Q-Q plot), and no severe multicollinearity (check VIF if applicable).

---

### D.5 (Worked) — Consumption and Income (Log-Log Model)

**Setup:** Both income (X) and consumption (Y) are log-transformed. We fit a DL(q) on their
first differences (log-returns). Data: n = 162 quarterly observations.

#### Step 1 — Stationarity

Both ln(Y) and ln(X) show clear upward trends in the time plot.

| Variable | DF Version | t-statistic | Critical (5%) | Conclusion |
|----------|-----------|-------------|----------------|-----------|
| ln(Y) — level | V2 (trend) | −1.82 | −3.41 | Fail to reject → unit root |
| ln(X) — level | V2 (trend) | −1.65 | −3.41 | Fail to reject → unit root |
| Δln(Y) — difference | V1 (no trend) | **−9.95** | −2.86 | **Reject → stationary** ✓ |
| Δln(X) — difference | V1 (no trend) | **−12.72** | −2.86 | **Reject → stationary** ✓ |

Both variables need first differencing. Proceed with Δln(Y) and Δln(X).

#### Step 2 — Fit DL(q), q_max = 3

| Model | Highest lag t-stat | Significant? | Action |
|-------|-------------------|-------------|--------|
| DL(3) | β₃: t = 0.91 | No | Drop lag 3 |
| DL(2) | β₂: t = 1.38 | No | Drop lag 2 |
| **DL(1)** | **β₁: t = 2.74** | **Yes** | **Stop. q = 1** |

**Fitted model:**
ΔŶ_t = 0.004 + 0.350 ΔX_t + 0.182 ΔX_{t−1}

| Coefficient | Value | Interpretation |
|-------------|-------|---------------|
| β̂₀ | 0.350 | A 1 pp rise in income growth rate raises consumption growth rate by 0.350 pp this quarter |
| β̂₁ | 0.182 | A 1 pp rise in last quarter's income growth raises this quarter's consumption growth by 0.182 pp |
| **Total multiplier** | **0.532** | A permanent 1 pp rise in income growth rate raises consumption growth rate by 0.532 pp in the long run |

#### Step 3 — LMSC Test

Auxiliary regression: e_t = α₀ + α₁ ΔX_t + α₂ ΔX_{t−1} + α₃ e_{t−1} + u_t
n_aux = 161, R²_aux = 0.002618

LM = 161 × 0.002618 = **0.4215**
p-value = P(χ²(1) ≥ 0.4215) = **0.5162**

**Conclusion:** Fail to reject H₀. No significant autocorrelation detected. Assumption A3 is
plausibly satisfied. ✓

---

## Formula Sheet — The Four Equations You Must Know

### 1. DL(q) Model

$$Y_t = \alpha + \beta_0 X_t + \beta_1 X_{t-1} + \cdots + \beta_q X_{t-q} + \varepsilon_t$$

Total multiplier = β₀ + β₁ + … + β_q = **Σβ_k**

### 2. AR(1) Model

$$Y_t = \alpha + \beta X_t + \gamma Y_{t-1} + \varepsilon_t$$

Total multiplier = **β/(1−γ)** (requires |γ| < 1)

### 3. LMSC Test

Auxiliary regression: e_t = α₀ + α₁ X_{1t} + … + α_k X_{kt} + α_{k+1} e_{t−1} + u_t

$$LM = n \cdot R^2 \sim \chi^2(1) \text{ under } H_0$$

H₀: ρ = 0 (no autocorrelation)
H₁: ρ ≠ 0 (autocorrelation present)
Critical value at 5%: χ²(1) = 3.841

### 4. Dickey-Fuller Test

**Version 1 (no trend):** ΔY_t = α₀ + α₁ Y_{t−1} + ε_t

**Version 2 (with trend):** ΔY_t = α₀ + λt + α₁ Y_{t−1} + ε_t

H₀: α₁ = 0 (unit root — NOT stationary) | H₁: α₁ < 0 (stationary)

| DF version | 5% critical value |
|-----------|------------------|
| Version 1 | **−2.86** |
| Version 2 | **−3.41** |

Reject H₀ if t-stat is **more negative** than critical value.

---

## Exam-Day Checklist

### Step 1 — Stationarity (TS_C)
- [ ] Plot every variable against time
- [ ] Choose DF version (V1: no trend / V2: trend or unsure)
- [ ] Run DF on each variable, read t-stat on Y_{t−1}
- [ ] Compare to adapted critical values (NOT standard t-table)
- [ ] Unit root present? → take ΔY_t, re-test on differences

### Step 2 — Fit the Model (TS_D)
- [ ] Model type given in question (static / DL(q) / AR(1))
- [ ] For DL: start at q_max, drop top lag while not significant
- [ ] Report all coefficients with standard errors and t-stats
- [ ] Calculate and report total multiplier (Σβ_k or β/(1−γ))
- [ ] Interpret: distinguish temporary vs. maintained; levels vs. log-returns

### Step 3 — Assumption Check (TS_B)
- [ ] State H₀ and H₁ explicitly
- [ ] Write the auxiliary regression (all original X's + lagged residual)
- [ ] Compute LM = n_aux × R²_aux
- [ ] Compare to χ²(1) = 3.841 (or use p-value)
- [ ] Write a full conclusion sentence: "We [reject/fail to reject] H₀. [Autocorrelation is/is not] present."
- [ ] Briefly mention other assumptions (A1–A5)

---

## Common Exam Pitfalls (Expanded)

### 1. "Reject H₀ means non-stationary" — WRONG
- For the **Dickey-Fuller** test: Reject H₀ means the series **IS stationary** (H₀ is the unit root).
- For the **LMSC** test: Reject H₀ means **autocorrelation IS present** (H₀ is no autocorrelation).
- These are opposite! Know which test you are running and re-read its H₀ before concluding.

### 2. "Take differences whenever the series trends" — BE CAREFUL
- Only take differences if the DF test confirms a **stochastic trend** (unit root, |ρ| = 1).
- If the trend is **deterministic** (|ρ| < 1, λ ≠ 0), add t as a regressor instead.
- **Over-differencing** (differencing a series that is already stationary or has only a deterministic trend) creates artificial negative autocorrelation and loses information.

### 3. "Use Durbin–Watson for all models"
- Durbin–Watson is **invalid** whenever Y_{t−1} appears as a regressor (AR(1) models).
- Always use **LMSC** — it works for both static, DL(q), and AR(1) models.

### 4. "Total multiplier = β₀ only"
- For DL(q): total multiplier = **β₀ + β₁ + … + β_q** (sum of ALL lag coefficients, not just β₀).
- For AR(1): total multiplier = **β/(1−γ)**, not just β.
- β₀ alone is the **immediate effect** — relevant only for a temporary, instantaneous impact.

### 5. "Unit changes when X is log-differenced"
- If you differenced log(X), then X is a log-return ≈ percentage change.
- A 1-unit rise in Δln(X) means a 1 **percentage point** rise in income growth (not a 1-euro rise in income level).
- Coefficients in a log-return model must be interpreted as responses to percentage changes.

### 6. "Skip the autocorrelation test to save time"
- The LMSC test is worth dedicated exam marks. Always report:
  - H₀ and H₁ in words
  - The auxiliary regression specification
  - LM = n × R²
  - The p-value and χ²(1) comparison
  - A conclusion sentence

### 7. "Use the regular t-table for the Dickey-Fuller t-statistic"
- The DF t-statistic **does not follow a t-distribution** under H₀. Standard critical values (±1.96, ±2.58) do not apply.
- The DF distribution is shifted to the left (more negative). If you used regular critical values you would almost never reject H₀, even when the series is clearly stationary.
- Always use the **adapted DF critical values**: −2.86 (V1, 5%), −3.41 (V2, 5%), etc.

---

## One-Page Summary

```
RECOGNISE  →  Time series: order matters. Define lags X_{t-k} and differences ΔX_t.
                           Watch sample size (n > 100 ideal), use real monetary values.

STABILISE  →  Time plot + Dickey-Fuller on every variable.
                           Deterministic trend (λ≠0, |ρ|<1)? Add t as regressor.
                           Stochastic trend / unit root (|ρ|=1)? Take first differences.
                           Re-test on differences if needed.

MODEL      →  Fit DL(q) or AR(1) on stationary variables.
                           DL(q): top-down selection of q; total multiplier = Σβ_k.
                           AR(1): total multiplier = β/(1−γ); requires |γ| < 1.
                           Interpret: temporary vs. maintained, log-returns vs. units.

DIAGNOSE   →  LMSC test: auxiliary regression with lagged residual; LM = n·R² ~ χ²(1).
                           Reject H₀ → autocorrelation → re-specify (prefer DL over AR when uncertain).
                           DW statistic: quick check only (not valid for AR models).
```

---

*End of Expanded Time Series Study Guide*
