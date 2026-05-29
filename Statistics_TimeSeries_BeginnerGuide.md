# STATISTICS — COMPLETE BEGINNER'S GUIDE
## Time Series Regression
### From Zero to Full Understanding

---

> **Who this guide is for.** This document assumes you have never studied statistics before.
> Every concept is built from the ground up with plain language, visual diagrams, and
> step-by-step worked examples. Nothing is skipped. If you already have some stats background,
> the later chapters still add valuable depth and worked examples.

---

## NOTATION GLOSSARY — Read This First

Before anything else, here is every symbol you will encounter, explained in plain English.

| Symbol | Name | Plain meaning |
|--------|------|---------------|
| Y | Dependent variable | The thing you are trying to predict or explain |
| X | Independent / explanatory variable | The thing you use to explain Y |
| t | Time index | Which time period we are in (e.g., t = 1 means year 1) |
| i | Individual index | Which person/firm/country we are looking at |
| β (beta) | Regression coefficient | How much Y changes when X changes by 1 unit |
| α (alpha) | Intercept | The value of Y when all X's = 0 |
| ε (epsilon) | Error / residual | The part of Y that our model fails to explain |
| ρ (rho) | Autocorrelation coefficient | How strongly this period's error relates to last period's error |
| γ (gamma) | AR coefficient on lagged Y | How much last period's Y feeds into this period's Y |
| λ (lambda) | Trend slope | How much the mean of Y grows each period |
| σ² | Variance | Measure of spread / unpredictability |
| Δ (delta) | First difference | Change from one period to the next: ΔX_t = X_t − X_{t−1} |
| Σ (sigma) | Sum | Add up everything that follows |
| H₀ | Null hypothesis | The "boring" default claim we try to disprove |
| H₁ | Alternative hypothesis | The "interesting" claim we want to support |
| n | Sample size | Total number of observations |
| R² | R-squared | Proportion of Y's variation explained by the model (0 to 1) |
| SE | Standard error | How much a coefficient estimate typically varies across samples |
| LM | Lagrange Multiplier | A test statistic we compute to check for autocorrelation |
| χ² | Chi-squared | A probability distribution used for some hypothesis tests |
| DW | Durbin-Watson | A quick test statistic for autocorrelation (limited use) |

---

## PART 0 — STATISTICS FOUNDATIONS (Start Here)

*Everything in this section is background knowledge that the rest of the guide builds on.*

### 0.1 — What Is Statistics? What Is Regression?

**Statistics** is the science of learning from data. We observe the world, collect numbers,
and try to answer questions like:
- Does more education cause higher wages?
- Does advertising increase sales?
- Does training reduce workplace accidents?

The problem is: the world is messy. Wages are affected by education, *and* experience, *and*
gender, *and* luck. Statistics lets us separate these influences.

**Regression** is the central tool. It finds the straight-line relationship between one or more
explanatory variables (X's) and an outcome variable (Y), while controlling for noise.

#### The Simplest Regression (One Variable)

$$Y = \alpha + \beta X + \varepsilon$$

In plain English:

- **Y** = outcome we want to understand (e.g., hourly wage in euros)
- **X** = thing we think explains Y (e.g., years of education)
- **α** = baseline Y when X = 0 (e.g., wage with zero education)
- **β** = slope — how much Y changes for each 1-unit increase in X
- **ε** = error — everything that moves Y but isn't captured by X

**Example:** Suppose we find: Wage = 5 + 1.2 × Education + ε

This means: every additional year of education is associated with €1.20/hour more in wages,
on average. A person with 10 years of education earns an estimated 5 + 1.2×10 = €17/hour.

The **ε (error)** is what remains unexplained. If the actual wage is €19/hour and our model
predicts €17, the residual is ε = 19 − 17 = +2. Our model is off by €2 for that person.

#### Multiple Regression (Several Variables)

$$Y = \alpha + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_k X_k + \varepsilon$$

Now we control for several things at once. Each β_j tells us: "holding all other X's constant,
how much does Y change when X_j increases by 1?" This is the **ceteris paribus** (all else equal)
interpretation.

---

### 0.2 — How Regression Is Estimated: OLS

**OLS = Ordinary Least Squares.** It is the standard method for calculating the β values.

The idea: choose the values of α and β that make the errors ε as small as possible across
all observations. Specifically, OLS minimises the **sum of squared errors**:

$$\min_{\alpha, \beta} \sum_{i=1}^{n} \varepsilon_i^2 = \sum_{i=1}^{n} (Y_i - \alpha - \beta X_i)^2$$

Why square them? Two reasons:
1. Positive and negative errors don't cancel each other out.
2. Large errors are penalised more than small ones (squaring amplifies big mistakes).

OLS gives us **coefficient estimates** β̂ ("beta hat") — the best-fitting line through the data.

**BLUE:** When certain conditions hold (see Section 0.4), OLS is **B**est **L**inear **U**nbiased
**E**stimator. "Best" means no other linear method has smaller estimation errors. "Unbiased"
means on average the estimates hit the true value (no systematic overestimation or
underestimation).

---

### 0.3 — R² : How Well Does the Model Fit?

$$R^2 = 1 - \frac{\text{Sum of Squared Errors}}{\text{Total Variation in Y}}$$

**Range:** R² is always between 0 and 1.

| R² value | Meaning |
|---------|---------|
| 0.0 | The model explains nothing — X tells us nothing about Y |
| 0.5 | The model explains 50% of Y's variation |
| 1.0 | Perfect fit — the model explains everything, zero residual |
| 0.95 | Seems great! But in time-series data, this can be a **warning sign** (spurious regression) |

**Intuition:** Imagine Y is the height of ocean waves. Total variation = how much waves differ
from their average height. If your model explains 80% of that variation, R² = 0.80.

---

### 0.4 — Standard Errors, t-statistics, and p-values

Even if OLS gives us β̂ = 1.2, we cannot be certain the true β is 1.2. If we collected a
different sample, we'd get a slightly different estimate. **Standard errors (SE)** measure
how much β̂ varies across samples.

#### The t-statistic

$$t = \frac{\hat{\beta} - 0}{SE(\hat{\beta})} = \frac{\hat{\beta}}{SE(\hat{\beta})}$$

The t-statistic asks: "Is this estimate far enough from zero to be convincingly non-zero?"

- A **large |t|** (say, |t| > 2) means the estimate is large relative to its uncertainty → likely real.
- A **small |t|** (say, |t| < 1) means the estimate could easily be zero just by chance → not convincing.

#### The p-value

The **p-value** is the probability of seeing a t-statistic this extreme (or more) if the true β
were actually zero.

| p-value | Interpretation |
|---------|---------------|
| p < 0.01 | Very strong evidence against H₀ (significant at 1%) |
| p < 0.05 | Strong evidence against H₀ (significant at 5%) — standard threshold |
| p < 0.10 | Weak evidence against H₀ (significant at 10%) |
| p > 0.10 | No convincing evidence; cannot reject H₀ |

**Analogy:** You flip a coin 20 times and get 17 heads. The p-value asks: "If this were a fair
coin (H₀), how likely is getting 17 or more heads?" If that probability is tiny (p < 0.05), you
conclude the coin is probably not fair — you reject H₀.

#### Hypothesis Testing in Regression

For any coefficient β_j:
- **H₀: β_j = 0** — X_j has no effect on Y (null hypothesis)
- **H₁: β_j ≠ 0** — X_j does affect Y (alternative hypothesis)

If p < 0.05: reject H₀ → X_j is **statistically significant**.
If p ≥ 0.05: fail to reject H₀ → evidence insufficient to confirm an effect.

**Important phrasing:** We never "accept H₀". We either reject it or fail to reject it. Failing
to reject just means the data don't give us enough evidence — not that H₀ is definitely true.

---

### 0.5 — The Five Classical Assumptions

OLS is only BLUE when these five conditions hold:

| Assumption | What it says | Why it matters |
|-----------|-------------|---------------|
| **A1** | E(ε) = 0 | Errors average to zero — no systematic over/under-prediction |
| **A2** | Var(ε) = σ² (constant) | Homoskedasticity — equal spread of errors everywhere |
| **A3** | cov(ε_i, ε_j) = 0 | Errors are uncorrelated with each other |
| **A4** | X's are non-random, not perfectly correlated | We can separate each X's effect |
| **A5** | ε ~ Normal (optional) | Needed for exact inference in small samples |

When you use time-series data, **A3 is routinely violated** (autocorrelation). This is the
central problem this guide addresses. A new assumption is also needed: **stationarity**.

---

### 0.6 — Visual Intuition: What a Regression Looks Like

```
Y
|            *
|         *     *
|      *     *
|   *   (fitted line)
|  * *
| *
+---------------------- X
```

Each `*` is a data point. OLS finds the straight line that passes as close as possible to
all the points, minimising the total squared vertical distance from points to the line.

The **residuals** (errors) are the vertical distances from each point to the line. Good
regression: residuals look like random noise. Bad regression: residuals show a pattern
(e.g., all positive on the left, all negative on the right).

---

## PART 1 — TIME SERIES FOUNDATIONS

## CHAPTER TS_A — Cautions

*What makes time-series data special and why ordinary regression needs modification*

### A.1 — Cross-Section vs. Time-Series Data

#### Definitions

| Type | Description | Notation | Order matters? |
|------|-------------|----------|---------------|
| **Cross-section** | Many units at one point in time | X_i, subscript *i* = individual | No — rows are interchangeable |
| **Time-series** | One unit observed repeatedly over time | X_t, subscript *t* = time period | **Yes** — shuffling destroys information |
| **Panel data** | Many units over many time periods | X_{it} | Both dimensions matter |

#### Why Order Matters

In a cross-section of 1,000 workers you could randomly reorder the rows and your regression
results would be identical. In a time series of 40 years of GDP data, row 5 (GDP in year 5)
*must* come after row 4 and before row 6. The temporal structure is not a nuisance — it is
the entire point.

#### Visual: What Time-Series Data Looks Like vs. Cross-Section Data

**Cross-section data** (each row is a different person):

```
Person | Wage | Education | Age
-------|------|-----------|----
Alice  | 22   |    16     | 34
Bob    | 18   |    12     | 28
Carol  | 35   |    20     | 45
...    | ...  |    ...    | ...
```

You could sort Alice, Bob, Carol in any order. Same result.

**Time-series data** (each row is a different time period):

```
Year | Belgium GDP | Unemployment | Inflation
-----|-------------|--------------|----------
2000 |   253 bn    |     6.9%     |   2.7%
2001 |   259 bn    |     6.6%     |   2.4%
2002 |   263 bn    |     7.5%     |   1.6%
2003 |   268 bn    |     8.2%     |   1.5%
...  |    ...      |     ...      |   ...
```

Row 2003 MUST come after row 2002. Reordering destroys the story of how the economy evolved.

#### Example — Hourly Wage

- **Cross-section:** A survey of 500 Belgian employees in 2010, each row one person. You can
  sort by name, age, sector — the regression of wage on education gives the same answer.
- **Time series:** Average Belgian hourly wage in 1980, 1981, …, 2015. The rows must follow
  calendar order. Regressing wage_t on time_t captures how wages evolved; shuffling would
  produce nonsense.

---

### A.2 — Lagged Variables

#### What a Lag Is

A **lag** simply refers to the value of a variable at an earlier time period. Think of it as
"looking in the rear-view mirror" — what was the value one period ago? Two periods ago?

If the current period is quarter 3 of 1987:

| Notation | Meaning | Value refers to |
|----------|---------|-----------------|
| X_t | Current value of X | Q3 1987 |
| X_{t−1} | One-period lag | Q2 1987 |
| X_{t−2} | Two-period lag | Q1 1987 |
| X_{t−q} | q-period lag | q quarters before Q3 1987 |

#### Visual: What a Lag Looks Like in Data

```
Original series X_t:
  t=1: 10
  t=2: 14
  t=3: 11
  t=4: 16
  t=5: 13

After creating lag X_{t-1}:
  t=1: 10  | X_{t-1}: [missing — no period 0]
  t=2: 14  | X_{t-1}: 10   ← value from t=1
  t=3: 11  | X_{t-1}: 14   ← value from t=2
  t=4: 16  | X_{t-1}: 11   ← value from t=3
  t=5: 13  | X_{t-1}: 16   ← value from t=4
```

Notice: the first row loses its observation because there is no "period 0". Each lag of order q
costs you q observations.

#### Why Lags Are Needed

Economic processes rarely respond instantaneously. Consider safety training:

- Hours of safety training are delivered in month t.
- Workers need time to absorb the training and change behaviour.
- The reduction in accidents appears in months t+1, t+2, etc.

A model without lags would miss most of the effect. Lags let us model this delay explicitly.

**Another example — central bank interest rates:**
When a central bank raises interest rates today, the effect on consumer spending might take
6–12 months to fully materialise. Banks need to update loan terms, consumers need to notice
higher mortgage costs, businesses need to reassess investment plans. All of this takes time.
A model using only current interest rates would dramatically underestimate the total effect.

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
With short time series (n < 50) this can be a serious constraint — each extra lag wastes
precious degrees of freedom.

---

### A.3 — Difference Variables

#### Definition

The **first difference** of X_t is the change from one period to the next:

$$\Delta X_t = X_t - X_{t-1}$$

**Intuition:** If GDP was €100 billion last year and €104 billion this year, the first difference
is ΔGDP = 104 − 100 = +€4 billion. It answers: "How much did GDP change?"

This is an **absolute** first difference. For a **seasonal** difference of order 12 (removing
year-on-year seasonality in monthly data):

$$\Delta_{12} X_t = X_t - X_{t-12}$$

This says: "How does this January compare to last January?" — removing the seasonal pattern.

#### Visual: Original vs. Differenced Series

```
GDP level (trending upward — non-stationary):

   GDP |                            *
       |                        * *
       |                    * *
       |                * *
       |            * *
       |        * *
       |    * *
       | * *
       +-------------------------------- time
       Clearly trending → not stationary


ΔGDP (first differences — fluctuates around zero):

  ΔGDP |    *   *       *
       |  *   *   *   *   *   *
       | ─────────────────────── 0
       |        *   *       *
       +-------------------------------- time
       Fluctuates around a constant level → stationary
```

This is the visual difference between a series that needs differencing and one that doesn't.

#### Interpretation

| Original variable | After differencing | Meaning |
|------------------|--------------------|---------|
| GDP level (€ billions) | ΔGDP | Change in GDP vs. previous period |
| log(GDP) | Δlog(GDP) = log(GDP_t / GDP_{t-1}) | **Log-return** ≈ percentage growth rate |
| Monthly unemployment (%) | Δ unemployment | Change in unemployment rate (pp) |
| log(price) | Δlog(price) | Percentage price change (return) |

#### Why Logarithms? A Beginner's Explanation

If a stock price rises from €100 to €200, that is a 100% increase.
If another rises from €10 to €20, that is also a 100% increase.
But in absolute terms: one rose by €100, the other by €10. They are not comparable in levels.

When you take log(price) and then difference it:
$$\Delta \ln(X_t) = \ln(X_t) - \ln(X_{t-1}) = \ln\!\left(\frac{X_t}{X_{t-1}}\right) \approx \frac{X_t - X_{t-1}}{X_{t-1}}$$

You get the **percentage change** — which is directly comparable across differently-sized
quantities. This is why financial data is almost always analysed in log-returns.

**Example:** Δln(100 → 102) = ln(102/100) = ln(1.02) ≈ 0.0198 ≈ 2% growth. ✓

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

Every time you run a regression on time-series data, you must address three specific issues.

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
adjusted (real) values for monetary variables.

**Example of the inflation problem:**
Imagine wage = €10/hr in 2000, €20/hr in 2020 (doubled in 20 years).
GDP also doubled from €200bn to €400bn.
But if *all prices* doubled too (inflation = 100%), nothing actually got better in real terms.
The regression would show a "significant positive relationship" between wages and GDP — but
it is entirely driven by inflation, not any real economic link. **Use real values.**

#### Problem 2 — Autocorrelation

Classical Assumption A3 states that errors are uncorrelated: cov(ε_i, ε_j) = 0. In time-series
data this is routinely violated. Shocks have persistence — if something unexpected happens
today, its effect persists into next period, gradually fading.

Consequences and solutions are covered in **Chapter TS_B**.

#### Problem 3 — Spurious Regression / Non-Stationarity

Imagine regressing Belgian ice cream sales on annual sunspot activity. Both series happen to
trend upward over a 30-year window. You would find a hugely significant regression with
R² = 0.95 — even though they have absolutely nothing to do with each other.

The solution is to ensure all variables are stationary before fitting the regression. Details
are in **Chapter TS_C**.

---

## CHAPTER TS_B — Autocorrelation

*Errors that remember the past: detection with the LMSC test*

### B.1 — Which Classical Assumption is Violated?

#### The Five Classical Assumptions (Recap)

The OLS estimator is BLUE when the Gauss-Markov conditions hold:

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
technology cycles, business cycles). Today's omitted shock tends to carry over into tomorrow.

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
- u_t is a **classical white-noise error** — uncorrelated, mean zero, constant variance

**White noise** means pure randomness — like rolling a fair die each period. No memory,
no pattern, no trend. It is the ideal we want our errors to look like.

This equation says: today's error is a fraction ρ of yesterday's error, plus a new fresh shock.

#### Visual: What Autocorrelated Residuals Look Like

**No autocorrelation (ρ = 0) — ideal:**
```
Residuals
  |  *     *        *     *
  |     *     *  *     *     *
0 | ───────────────────────────
  |  *        *  *        *
  |     *  *           *
  +─────────────────────────── time
  Random scatter above and below zero. No pattern. A3 satisfied. ✓
```

**Positive autocorrelation (ρ > 0) — "waves":**
```
Residuals
  |  * * * *
  |*         * *
0 | ───────────────────────────
  |             * * * *
  |                     * * *
  +─────────────────────────── time
  Long runs of positive, then long runs of negative. Wave-like. A3 violated. ✗
```

**Negative autocorrelation (ρ < 0) — "zigzag":**
```
Residuals
  |  *   *   *   *   *
  |
0 | ───────────────────────────
  |    *   *   *   *   *
  +─────────────────────────── time
  Alternates above/below zero every period. Rare in economics. A3 violated. ✗
```

#### Understanding the Size of ρ

| Value of |ρ| | Interpretation |
|------------|---------------|
| ρ = 0 | No autocorrelation. ε_t = u_t, purely random noise — A3 satisfied. |
| 0 < |ρ| < 0.3 | Weak autocorrelation. Standard errors mildly affected. |
| 0.3 < |ρ| < 0.7 | Moderate autocorrelation. Noticeable distortion of standard errors. |
| |ρ| > 0.7 | Strong autocorrelation. Inference seriously unreliable. |
| |ρ| = 1 | Unit root in the error — errors wander without bound. Unstable model. |
| |ρ| > 1 | Explosive errors — ε_t grows without limit. Meaningless model. |

We require **−1 < ρ < 1** for the error process itself to be stationary and well-behaved.

#### Understanding the Sign of ρ

| Sign | Pattern in residuals | Typical cause in economics |
|------|---------------------|---------------------------|
| **ρ > 0** (positive) | Long runs: + + + + − − − − | Very common. Business cycles, omitted trending variables. |
| **ρ < 0** (negative) | Alternating: + − + − + − ... | Rare. Can arise from over-differencing. |

**Worked analogy for ρ = 0.7:** If this quarter's residual is +10, next quarter's residual is
expected to be +7 (= 0.7 × 10). The quarter after, +4.9. Then +3.4, then +2.4, then +1.7,
and so on — slowly decaying toward zero. A shock takes many periods to fade.

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
| Confidence intervals | **Wrong width** — too narrow if ρ > 0 (falsely precise) |
| R² | Unaffected but potentially misleading |

The key danger is **false significance**: positive autocorrelation inflates t-statistics, making
coefficients appear more significant than they really are.

**Analogy for wrong standard errors:**
Imagine asking 10 people in one household whether they like pizza, and claiming those 10 opinions
represent 10 independent data points. They don't — family members influence each other. Your
"effective" sample size is much smaller than 10. Autocorrelation does the same thing to time-
series data: consecutive observations are not truly independent, so your effective sample size
is smaller than it appears, and your standard errors are too small.

#### Exception: AR(1) Models (Lagged Dependent Variable)

When the regression contains Y_{t−1} as a regressor **and** there is autocorrelation in ε:

$$Y_t = \alpha + \beta X_t + \gamma Y_{t-1} + \varepsilon_t \quad \text{with } \text{cov}(\varepsilon_t, \varepsilon_{t-1}) \neq 0$$

The problem is now much worse: the coefficient **estimates themselves become biased**. The
reason: Y_{t−1} is a function of ε_{t−1}. If ε_t is correlated with ε_{t−1}, then Y_{t−1}
is correlated with ε_t — violating A4. When that happens, OLS is no longer even unbiased.

**Practical rule:** If you detect autocorrelation in an AR(1) model, re-specify (switch to DL(q)).

---

### B.4 — Detection: The LMSC Test

#### Step 0 — Graphical Inspection First

Always **plot the residuals against time** before running any test. Look for:
- **Waves** (long runs above or below zero) → positive autocorrelation, ρ > 0.
- **Zigzag** (alternating signs) → negative autocorrelation, ρ < 0.
- **Random scatter** (no visible pattern) → A3 plausibly satisfied.

#### The LMSC Test — Full Procedure

**What are we testing?** We want to know if there is a significant relationship between this
period's residual and last period's residual. If consecutive residuals are strongly correlated,
autocorrelation is present.

**Hypotheses:**
- H₀: ρ = 0 (no autocorrelation — A3 satisfied)
- H₁: ρ ≠ 0 (autocorrelation present — A3 violated)

**Step 1:** Fit the original regression model. Save the residuals e_t.

**Step 2:** Build the **auxiliary regression**. Regress the residuals on all the original
predictors X_{1t}, …, X_{kt} **plus** the lagged residual e_{t−1}:

$$e_t = \alpha_0 + \alpha_1 X_{1t} + \cdots + \alpha_k X_{kt} + \alpha_{k+1} e_{t-1} + u_t$$

**Why include the original X's?**
Without the X's, some of the "relationship" between e_t and e_{t-1} might actually be caused
by the X variables themselves (because X's also have temporal structure). Including X's in the
auxiliary regression "controls out" their influence, leaving only the pure autocorrelation
signal in e_{t-1}. Think of it as a partial correlation: we want the relationship between
consecutive residuals *after accounting for* the effect of the X's.

**Step 3:** From the auxiliary regression, read R² and compute:

$$LM = n \cdot R^2$$

where n is the sample size of the **auxiliary** regression (= n_original − 1).

**Why n × R²?** R² in the auxiliary regression measures how much of the variation in today's
residual is explained by yesterday's residual (and the X's). Multiplying by n scales this into
a test statistic with a known distribution.

**Step 4:** Under H₀, the LM statistic follows **χ²(1)**. Compare LM to 3.841 (the 5%
critical value for χ²(1)).

**What is χ²(1)?** The chi-squared distribution with 1 degree of freedom is a probability
distribution used for test statistics that are squared quantities. The value 3.841 is the
threshold: there is only a 5% chance of seeing LM > 3.841 if H₀ is true.

**Decision:**
- If LM > 3.841 (or p-value < 0.05): **Reject H₀** → autocorrelation is present.
- If LM ≤ 3.841 (or p-value ≥ 0.05): **Do not reject H₀** → A3 plausibly satisfied.

#### Higher-Order Tests

The procedure above tests for first-order autocorrelation only (e_{t−1} in the auxiliary
regression). To test for autocorrelation up to order p, add e_{t−1}, e_{t−2}, …, e_{t−p} to
the auxiliary regression. The LM statistic then follows χ²(p) under H₀.

**Important:** The sample size in the auxiliary regression becomes n − p.

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

**Conclusion:** LM = 27.6 >> 3.841. Reject H₀ at any reasonable significance level.
Autocorrelation is strongly present. The Phillips curve model is misspecified.

#### Durbin–Watson as an Alternative

SPSS automatically prints the **Durbin–Watson (DW)** statistic.

| DW value | Interpretation |
|----------|---------------|
| Close to **2** | No autocorrelation |
| Close to **0** | Strong positive autocorrelation (ρ near +1) |
| Close to **4** | Strong negative autocorrelation (ρ near −1) |
| Between 1.5 and 2.5 | Generally acceptable (rough rule) |

**Critical limitation:** Durbin–Watson is **invalid** whenever the regression contains a
lagged dependent variable Y_{t−1}. Always use LMSC as your primary test.

**Relationship between DW and ρ:**

$$DW \approx 2(1 - \hat{\rho})$$

So DW = 2 when ρ̂ = 0 (no autocorrelation), DW = 0 when ρ̂ = 1 (strong positive
autocorrelation), and DW = 4 when ρ̂ = −1 (strong negative autocorrelation).

---

### B.5 — Solutions for Autocorrelation

#### The Exam Approach: Re-specify the Model

The philosophy: autocorrelation in a static model usually indicates **model misspecification**.
The error term is carrying memory because dynamics were left out. Adding lags absorbs the
dynamic structure and often eliminates autocorrelation.

| Re-specification | What you add | Model type |
|-----------------|-------------|-----------|
| Add lagged X's | X_{t−1}, X_{t−2}, …, X_{t−q} | **DL(q)** — Distributed Lag |
| Add lagged Y | Y_{t−1} | **AR(1)** — Autoregressive |

#### DL(q) vs. AR(1) — Which to Choose?

| Criterion | DL(q) preferred | AR(1) preferred |
|-----------|----------------|----------------|
| Residual autocorrelation present | ✓ DL is only inefficient, not biased | ✗ AR is biased with residual autocorrelation |
| Multicollinearity concern | ✗ DL with many lags is collinear | ✓ AR uses only 2 coefficients |
| Long memory needed | ✗ Need many lags = many parameters | ✓ β/(1−γ) captures infinite lag with 2 params |
| **Bottom line** | **Safer when autocorrelation is present** | **More parsimonious when A3 satisfied** |

**Key principle: bias is worse than inefficiency.**
- DL with autocorrelation → wrong standard errors (bad, but the coefficients are still correct on average).
- AR with autocorrelation → wrong coefficient estimates (fundamentally misleading — we don't even know the direction of the effect reliably).

---

## CHAPTER TS_C — Stationarity

*Spurious regression, the generalized AR(1), and the Dickey-Fuller test*

### C.1 — Spurious Regression

#### The Problem

Consider: regress Belgian GDP per capita (1950–2004) on US population density over the
same period. You find:
- R² ≈ 0.96 (extremely high)
- Slope coefficient significant at p < 0.001

Yet Belgian GDP and US population density have **no meaningful economic relationship**. This
is a **spurious regression** — a statistically convincing result that is economically meaningless.

#### Why It Happens: Shared Trends

Both series happened to grow over the same 54-year period. The regression is picking up their
**common time trend**, not any genuine relationship.

**Famous real-world example:** The number of Nicolas Cage films released per year is
significantly correlated with drowning deaths in US swimming pools between 1999 and 2009.
Both happened to move similarly over that period — pure coincidence. A regression would give
R² ≈ 0.67 and p < 0.05. Completely spurious.

#### The Root Cause: Non-Stationarity

The mathematical reason: both variables are **non-stationary** — their means drift over time.
Standard regression theory requires stationarity. When it fails, t-statistics don't follow
t-distributions, and R² doesn't converge to a meaningful value.

**Stationarity is therefore a new assumption** required for time-series regression.

---

### C.2 — Definition of Stationarity

#### Formal Definition (Weak/Covariance Stationarity)

A time series Y_t is **weakly stationary** if, for every t:

1. **E(Y_t) = μ** — The mean is constant. The series oscillates around a fixed level.
2. **Var(Y_t) = σ²** — The variance is constant. Not more volatile over time.
3. **Cov(Y_t, Y_{t−s}) = γ_s** — The covariance depends only on the gap s, not on when.

#### Visual: Stationary vs. Non-Stationary Series

**Stationary series — fluctuates around a constant level:**
```
Y
  |     *       *   *
  |  *     * *     *   *   *
  | ──────────────────────────  ← constant mean
  |   *   *         *     *
  |       *     *
  +───────────────────────── time
  Mean is flat. Variance is constant. Keeps returning to the same level.
```

**Non-stationary (trending) series — drifts upward:**
```
Y
  |                         * *
  |                   * * *
  |             * * *
  |       * * *
  | * * *
  +───────────────────────── time
  Mean is growing over time. Does NOT return to a fixed level.
  Running a regression with this series can produce spurious results.
```

**Non-stationary (random walk) — wanders unpredictably:**
```
Y
  |   *
  |  * * *
  | *     * *
  |          * *
  |             * *
  |               * * * *
  +───────────────────────── time
  Neither trends up/down consistently NOR stays near a fixed level.
  Goes wherever past shocks have pushed it. Variance grows over time.
```

#### Intuitive Test: The "Cut in Half" Check

Plot the time series. Visually divide it into two halves. If the left half and right half:
- Have similar **average levels** → mean is constant → good sign
- Have similar **spread/volatility** → variance is constant → good sign
- Show similar **patterns** → covariance structure is similar → good sign

If the right half is systematically higher, more volatile, or shows different patterns, you
have evidence of non-stationarity.

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

The **critical question** is whether **|ρ| < 1** (stationary family) or **|ρ| = 1** (random walk).

#### The Four Cases

---

**Case 1 — Basic AR(1):** |ρ| < 1, a = 0, λ = 0

Model: Y_t = ρ Y_{t-1} + ε_t

**Intuition:** Each period, Y reverts toward zero. If Y is currently +10, next period it will
tend to be ρ×10 (closer to zero). The series has a "gravitational pull" back to zero.

By substituting the equation for Y_{t−1} back into Y_t, then Y_{t−2} back in, and so on:

$$Y_t = \varepsilon_t + \rho \varepsilon_{t-1} + \rho^2 \varepsilon_{t-2} + \cdots + \rho^t Y_0$$

This is an **infinite moving average** of all past shocks, with geometrically declining weights.
Because |ρ| < 1, the weights ρ, ρ², ρ³, … shrink toward zero — old shocks become irrelevant.

Properties:
| Property | Formula | Stationarity check |
|----------|---------|-------------------|
| Mean | E(Y_t) ≈ 0 | ✓ Constant |
| Variance | Var(Y_t) = σ²/(1−ρ²) | ✓ Constant (requires |ρ| < 1) |
| Covariance | Cov(Y_{t−s}, Y_t) = σ²ρˢ/(1−ρ²) | ✓ Depends only on lag s |
| Autocorrelation | r(Y_{t−s}, Y_t) = ρˢ | Decays exponentially to 0 |

**✓ STATIONARY**

**Example:** Y_t = 0.7 Y_{t−1} + ε_t. A shock of +10 in period t:
period t+1: +7.0, t+2: +4.9, t+3: +3.4, t+4: +2.4, …, eventually → 0.

---

**Case 2 — AR(1) with constant:** |ρ| < 1, a ≠ 0, λ = 0

Model: Y_t = a + ρ Y_{t-1} + ε_t

| Property | Formula |
|----------|---------|
| Mean | μ = a/(1−ρ) |
| Variance | σ²/(1−ρ²) |

**✓ STATIONARY** — but now around a non-zero mean μ = a/(1−ρ).

**Intuition for the mean formula:** In long-run equilibrium, Y_t = Y_{t−1} = μ (no expected
change). Substituting: μ = a + ρμ → μ(1−ρ) = a → μ = a/(1−ρ).

**Example:** Y_t = 5 + 0.6 Y_{t−1} + ε_t. Long-run mean = 5/(1−0.6) = 12.5. The series
oscillates around 12.5, never drifting away permanently.

---

**Case 3 — AR(1) with deterministic trend:** |ρ| < 1, a ≠ 0, λ ≠ 0

Model: Y_t = a + λt + ρ Y_{t-1} + ε_t

The λt term makes the mean grow linearly over time. The series **is not stationary** (the
mean changes with t). However, the **deviation from the trend line** is stationary.

**Visual:**
```
Y  |                  *  ← actual data
   |               * /
   |            * / trend line (growing by λ per period)
   |         * /
   |      * /
   |   * /
   +───────────────── time
   Deviations from the trend line (the gaps) ARE stationary.
   The trend line itself is NOT stationary.
```

**✗ NOT STATIONARY** in levels, but **✓ stationary about a deterministic trend**.

**Fix:** Add t as a regressor in the regression (see C.5, Fix A).

---

**Case 4 — Random Walk:** |ρ| = 1

When ρ = 1, Y_t = a + Y_{t-1} + ε_t.

**Crucial difference from Case 1:** Each shock is permanent. By repeated substitution:
Y_t = Y_0 + ε_1 + ε_2 + … + ε_t

The series is the accumulated sum of ALL past shocks. None of them ever fade.

| Sub-case | Model | Mean behaviour | Variance behaviour |
|----------|-------|---------------|-------------------|
| Pure random walk (a=0, λ=0) | Y_t = Y_{t-1} + ε_t | E(Y_t) = Y_0 (constant) | Var(Y_t) = tσ² → **grows without bound** |
| Random walk with drift (a≠0, λ=0) | Y_t = a + Y_{t-1} + ε_t | E(Y_t) = ta + Y_0 → **drifts** | Also grows with t |

**Why the variance explodes:**
Var(Y_t) = Var(ε_1 + ε_2 + … + ε_t) = Var(ε_1) + Var(ε_2) + … + Var(ε_t) = tσ²

Each period adds another independent shock. Unlike Case 1 where past shocks had weights ρˢ
that decay, here all past shocks carry full weight forever.

**Visual: Random walk vs. AR(1)**
```
AR(1) with ρ = 0.7 — stationary:     Random walk (ρ = 1) — non-stationary:
Y                                      Y
  |  *   *                              |              * *
  |*  * *  * *     *                    |         * * *
  |──────────────────                   |      * *
  |      *    * *  * *                  |   * *
  |           *                         | *
  +──────────────────── time            +──────────────────── time
  Keeps returning to mean = 0           Wanders freely, never returns
  Shocks fade out                       Shocks accumulate forever
```

**✗ ALL NON-STATIONARY.** Fix: Take first differences.

#### Summary Card

| Case | ρ | λ | Stationary? | Fix |
|------|---|---|-------------|-----|
| Basic AR(1) | |ρ|<1 | 0 | ✓ Yes | None needed |
| AR(1) + constant | |ρ|<1 | 0 | ✓ Yes | None needed |
| AR(1) + deterministic trend | |ρ|<1 | ≠0 | ✗ No (has trend) | Add t to regression |
| Random walk | |ρ|=1 | any | ✗ No | Take first differences |

---

### C.4 — Deterministic vs. Stochastic Trends

This distinction is crucial because the two types of non-stationarity require **different fixes**.
Applying the wrong fix can make things worse.

| Feature | Deterministic Trend | Stochastic Trend (Random Walk) |
|---------|--------------------|-----------------------------|
| Mathematical source | λt term in the model | |ρ| = 1 |
| Mean | Changes predictably (grows by λ per period) | May drift, but unpredictably |
| **Variance** | **Constant** | **Grows with time** |
| Shocks | Temporary — series returns to trend after a shock | Permanent — series never recovers |
| Example | GDP trend growth of 2% per year | S&P 500 stock price index |
| **Correct fix** | **Detrend** or add t as regressor | **First difference** |
| Wrong fix | First-differencing over-differences → negative autocorrelation | Detrending doesn't remove stochastic trend |

**Key intuition — permanence of shocks:**
- **Deterministic trend:** A recession pushes GDP below its trend line, but in subsequent years
  GDP returns to the same trend. The shock is temporary.
- **Random walk:** A recession permanently lowers the level of the series. Future values are
  all shifted down by the same amount. The shock is permanent and the series has no "memory"
  of where it "should" be.

---

### C.5 — Solutions for Non-Stationarity

#### Fix A — Deterministic Trend (|ρ| < 1, λ ≠ 0)

**Option 1 — Detrending:**
Estimate the trend (regress Y_t on t) and subtract it:
Ỹ_t = Y_t − μ̂ − δ̂t (the residuals from this auxiliary regression)
Then use Ỹ_t in place of Y_t in all subsequent analysis.

**Option 2 — Model the trend explicitly (preferred in practice):**
Include t as an additional regressor in your main model:

$$Y_t = \beta_0 + \beta_1 X_t + \lambda t + \varepsilon_t$$

This is equivalent to Option 1 but simpler — you let OLS handle the detrending simultaneously.
The coefficient on t absorbs the linear trend; the coefficient on X_t now measures the
relationship *after controlling for the common time trend*.

**Option 3 — Seasonal differencing:**
For data with seasonality (monthly, quarterly), use:
Δ₁₂X_t = X_t − X_{t−12}

This removes any pattern that repeats annually.

#### Fix B — Stochastic Trend / Unit Root (|ρ| = 1)

**Take first differences.** This is the only valid fix for a random walk.

$$\Delta Y_t = Y_t - Y_{t-1}, \quad \Delta X_t = X_t - X_{t-1}$$

**Why it works:** If Y_t = Y_{t-1} + ε_t, then:
ΔY_t = Y_t − Y_{t-1} = ε_t ← white noise, stationary ✓

The difference operation strips away the accumulated shock history, leaving only the new shock.

**How many times to difference?**
- If Y_t has one unit root → take **first differences** ΔY_t
- If ΔY_t still has a unit root → take **second differences** Δ²Y_t = ΔY_t − ΔY_{t−1}
- Most macroeconomic series need only one round of differencing.

> **Important caveat — Cointegration:**
> There is one exception to "always difference I(1) series." If two non-stationary series are
> **cointegrated** — meaning they are genuinely tied together by an economic relationship and
> their *difference* is stationary — you should NOT difference them. Instead, run the regression
> in levels (the "cointegrating regression"). This preserves the long-run relationship. If you
> difference cointegrated variables, you throw away the most economically meaningful information.
> *Detecting cointegration is beyond this course's scope, but always consider whether two
> trending series might be genuinely linked before differencing.*

---

### C.6 — The Dickey-Fuller Test

#### Purpose

The Dickey-Fuller test is a **formal unit root test**: it decides whether ρ = 1 (non-stationary)
or |ρ| < 1 (stationary). It converts a visual judgment into a rigorous hypothesis test.

#### Hypotheses

- **H₀: ρ = 1** — the series has a unit root, is NOT stationary
- **H₁: |ρ| < 1** — the series IS stationary (possibly about a deterministic trend)

**Note the asymmetry:** H₀ is the dangerous case (non-stationarity). We want to reject H₀.
**Failing to reject H₀ means we cannot prove stationarity** — assume the series needs differencing.

#### The Reparameterisation Trick

Instead of testing H₀: ρ = 1 directly, subtract Y_{t-1} from both sides:

$$\Delta Y_t = a + \lambda t + \alpha_1 Y_{t-1} + \varepsilon_t$$

where **α₁ = ρ − 1**. Now:
- H₀: ρ = 1 ⟺ **α₁ = 0**
- H₁: |ρ| < 1 ⟺ **α₁ < 0** (must be negative since ρ < 1 means ρ−1 < 0)

We test whether α₁ is significantly **negative** — a one-sided test.

**Why reparameterise?** OLS can easily test whether a coefficient equals zero. Testing
"does ρ = 1" directly is mathematically awkward. By defining α₁ = ρ − 1, we convert the
question into "does α₁ = 0?" which is standard.

#### Why the Normal t-Table Cannot Be Used Here

This is a critical point that confuses many students.

Normally, when we test whether a regression coefficient is zero, the t-statistic follows
a t-distribution (or normal distribution in large samples). We use critical values like
±1.96 (at 5%) or ±2.58 (at 1%).

**Under the null hypothesis of a unit root (H₀: ρ = 1), the standard statistical theory
completely breaks down.** Here is the intuitive reason:

The standard theory assumes the data are stationary. Under H₀, Y_t is a random walk — it is
*not* stationary. Its variance grows over time. When we use Y_{t-1} as a predictor of ΔY_t,
we are using an increasingly "large" (non-stationary) variable. The usual asymptotic results
that justify the t-distribution do not apply.

The consequence: the actual distribution of the t-statistic under H₀ is **shifted to the left**
(more negative) compared to the usual t-distribution. If you used standard critical values
(like −1.96 for 5%), you would almost never reject H₀ — even when the series is clearly
stationary. You would incorrectly conclude "unit root present" for most stationary series.

This is why Dickey and Fuller derived new, special critical values through simulation:

| DF Version | 1% critical value | 5% critical value | 10% critical value |
|-----------|-------------------|-------------------|--------------------|
| Version 1 (no trend) | −3.43 | **−2.86** | −2.57 |
| Version 2 (with trend) | −3.96 | **−3.41** | −3.13 |

These are more negative than the usual −1.96, reflecting the leftward shift of the distribution.

**Decision rule:** Reject H₀ (conclude stationarity) if and only if the t-statistic on Y_{t−1}
is **more negative** than the critical value.

**Example:** t-stat = −3.10.
- Version 1 at 5%: −3.10 < −2.86 → Reject H₀ → stationary ✓
- Version 2 at 5%: −3.10 > −3.41 → Fail to reject → unit root ✗

The choice of version matters!

#### The Two Versions

| Version | Regression | When to use |
|---------|-----------|-------------|
| **Version 1 — no trend** | ΔY_t = α₀ + α₁ Y_{t−1} + ε_t | No visible trend in time plot |
| **Version 2 — with trend** | ΔY_t = α₀ + λt + α₁ Y_{t−1} + ε_t | Clear trend in time plot, or when unsure |

Version 2 is the **safer default**: if a trend is present but you use Version 1, your test is
misspecified. If no trend is present but you use Version 2, you merely lose one degree of freedom.

#### Procedure (4 Steps)

1. **Plot Y_t against time.** Does it trend? Choose Version 1 (no trend) or Version 2 (trend or unsure).
2. **Create ΔY_t** (first difference of Y) and Y_{t−1} (one lag of Y).
3. **Run the chosen DF regression** (ΔY_t on Y_{t−1}, plus t for Version 2).
4. **Find the t-statistic for the coefficient of Y_{t−1}**. Compare to adapted critical values.

#### What to Do After the DF Test

| DF result | Action |
|-----------|--------|
| Reject H₀ (stationary) | Use the series **in levels** in your model |
| Fail to reject H₀ (unit root) | Take **first differences**, then re-run DF on ΔY_t |
| DF on ΔY_t: Reject H₀ | ΔY_t is stationary; use **first differences** in the model |
| DF on ΔY_t: Still fail to reject | Rare. Consider second differences |

---

### Reference — Mean of a Stationary AR(1)

| Model | Stationarity | Long-run mean |
|-------|-------------|---------------|
| Y_t = ρ Y_{t-1} + ε_t | ✓ Stationary | μ = 0 |
| Y_t = a + ρ Y_{t-1} + ε_t | ✓ Stationary | μ = a/(1−ρ) |
| Y_t = a + λt + ρ Y_{t-1} + ε_t | ✗ Not stationary | Stationary about μ + δt |

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

#### Visual: How a DL(q) Model Distributes the Effect Over Time

Suppose safety training reduces accidents. Here is how the DL(2) model (q=2) sees it:

```
Training hours in month t
         |
         |─── β₀ ───> Effect on accidents in month t   (immediate)
         |─── β₁ ───> Effect on accidents in month t+1 (1-period lag)
         |─── β₂ ───> Effect on accidents in month t+2 (2-period lag)

Total effect of one training hour = β₀ + β₁ + β₂  (the total multiplier)
```

The coefficients β₀, β₁, β₂ can all be different magnitudes — the effect profile is
completely flexible.

#### Interpretation of Coefficients

Each β_k is interpreted *ceteris paribus* — holding all other X variables constant.

**β_k = the average change in Y_t when X_{t−k} rises by 1 unit, all other lagged values held constant.**

The most practically useful comparison is between a **temporary** and a **maintained** change:

| Type of change | Effect at lag k | Long-run total |
|---------------|----------------|----------------|
| **Temporary** (X rises by 1, then returns) | β_k is the additional effect k periods later | Ends after lag q |
| **Maintained** (X rises by 1 permanently) | Cumulative: β₀ + β₁ + … + β_k after k periods | **Total multiplier** = Σβ_k |

#### The Total Multiplier

$$\text{Total multiplier} = \sum_{k=0}^{q} \beta_k = \beta_0 + \beta_1 + \cdots + \beta_q$$

**Interpretation:** The total multiplier is the **long-run effect on Y of a permanent 1-unit
increase in X**. It answers: "If X goes up by 1 unit and stays there forever, by how much
will Y eventually change?"

---

### D.2 — Choosing the Optimal Lag Length q

#### Why Not Just Include All Lags?

Including too many lags creates problems:
1. **Lost observations:** each lag costs one more observation.
2. **Multicollinearity:** X_t, X_{t-1}, X_{t-2} are typically very similar — their correlation
   is high. This inflates standard errors for all coefficients.
3. **Overfitting:** unnecessary lags soak up degrees of freedom without improving model quality.

#### The Top-Down Procedure

Start from a maximum lag q_max and progressively drop the highest lag that is not significant:

1. Fit DL(q_max). Check the t-test for β_{q_max}.
2. If β_{q_max} is **not significant**: drop lag q_max, refit DL(q_max − 1).
3. Repeat until the highest remaining lag is **significant**.
4. That is your **optimal lag length q**.

**Important:** Once you find the optimal q, do **not** drop intermediate insignificant lags.
If β_2 is significant but β_1 is not, you still keep both — you cannot have lag 2 without
lag 1. This would create a gap in the lag structure with no theoretical justification.

#### Worked Example — Safety Training and Accident Losses

Goal: model monthly accident losses (Y, euros) as a function of safety training hours (X),
with q_max = 4.

| Step | Model fitted | Result | Action |
|------|-------------|--------|--------|
| 1 | DL(4) | β₄: t = 0.83, p = 0.41 | Not significant → Drop lag 4 |
| 2 | DL(3) | β₃: t = 1.21, p = 0.23 | Not significant → Drop lag 3 |
| 3 | DL(2) | β₂: t = 1.56, p = 0.12 | Not significant → Drop lag 2 |
| 4 | DL(1) | β₁: t = −2.87, p = 0.005 | **Significant → Stop. Optimal q = 1** |

The final model is: Ŷ_t = α̂ + β̂₀ X_t + β̂₁ X_{t−1}

Report:
- **Immediate effect:** β̂₀
- **One-period lagged effect:** β̂₁
- **Total multiplier:** β̂₀ + β̂₁

---

### D.3 — Autoregressive Model AR(1)

#### From Distributed Lags to Autoregression

Instead of explaining today's Y by past values of X, the AR(1) model lets **past Y** carry
the memory of the system:

$$Y_t = \alpha + \beta X_t + \gamma Y_{t-1} + \varepsilon_t$$

**Why include Y_{t−1}?** Because in many economic processes, the current state of Y is the
best single predictor of the next state. Consumer spending this quarter depends heavily on
consumer spending last quarter (habits, contracts, inertia). By including Y_{t−1}, we capture
all persistence effects in a single coefficient γ.

#### Interpreting the Coefficients

| Coefficient | Interpretation |
|-------------|---------------|
| α | Intercept |
| **β** | The **immediate effect**: a 1-unit rise in X_t causes Y_t to rise by β, holding Y_{t−1} constant |
| **γ** | The **persistence coefficient**: how much of last period's Y carries forward. Requires |γ| < 1. |
| **β/(1−γ)** | The **total multiplier**: long-run effect of a permanent 1-unit rise in X |

#### The Total Multiplier Formula

$$\text{Total multiplier (AR1)} = \frac{\beta}{1 - \gamma}$$

This requires **|γ| < 1** (stationarity condition).

**Proof sketch:** In long-run equilibrium, Y_t = Y_{t−1} = Y* (steady state):
Y* = α + β X* + γ Y* → Y*(1−γ) = α + β X* → Y* = α/(1−γ) + [β/(1−γ)] X*

So a 1-unit permanent increase in X* raises long-run Y* by β/(1−γ).

#### Dynamic Path After a Temporary Shock

Suppose X rises by 1 unit only in period t, then returns to its original value:

| Period | Additional effect on Y (above baseline) |
|--------|----------------------------------------|
| t | β |
| t+1 | γ · β |
| t+2 | γ² · β |
| t+3 | γ³ · β |
| t+k | γ^k · β |

The effect decays geometrically at rate γ.

#### Worked Example — Education Spending and GDP Growth

**Data:** Yearly US data since 1910.
- X_t = education spending per child (dollars)
- Y_t = GDP growth rate (%)

**Fitted AR(1) model:**
Ŷ_t = 1.01 + 0.009 X_t + 0.627 Y_{t−1}

| Component | Value | Meaning |
|-----------|-------|---------|
| α̂ | 1.01 | Baseline growth when X = 0 and Y_{t−1} = 0 |
| β̂ | 0.009 | A $1 increase raises GDP growth by 0.009 pp immediately |
| γ̂ | 0.627 | 62.7% of last year's GDP growth persists into this year |
| **Total multiplier** | 0.009/(1−0.627) = **0.024** | A permanent $1/child increase raises long-run GDP growth by 0.024 pp |

---

### D.4 — Link Between AR(1) and DL(∞)

#### AR(1) Is Secretly an Infinite Distributed Lag

We can show that AR(1) is equivalent to a DL(∞) with geometrically declining coefficients.
Substitute Y_{t−1} into the AR(1) equation, then Y_{t−2}, and continue indefinitely:

$$Y_t = \alpha + \beta X_t + \gamma Y_{t-1} + \varepsilon_t$$

Substituting once (Y_{t-1} = α + β X_{t-1} + γ Y_{t-2} + ε_{t-1}):

$$= \alpha(1+\gamma) + \beta X_t + \beta\gamma X_{t-1} + \gamma^2 Y_{t-2} + \gamma\varepsilon_{t-1} + \varepsilon_t$$

Continuing to infinity:

$$Y_t = \frac{\alpha}{1-\gamma} + \beta X_t + \beta\gamma X_{t-1} + \beta\gamma^2 X_{t-2} + \beta\gamma^3 X_{t-3} + \cdots$$

This is a DL(∞) model with **geometrically declining lag coefficients**: β, βγ, βγ², βγ³, …

#### Total Multiplier from the Geometric Series

$$\text{Total multiplier} = \sum_{k=0}^{\infty} \beta\gamma^k = \beta \cdot \frac{1}{1-\gamma} = \frac{\beta}{1-\gamma}$$

**Why does Σγᵏ = 1/(1−γ)?**
This is the geometric series formula. Here is the intuition:

Let S = 1 + γ + γ² + γ³ + … (infinite sum, with |γ| < 1)
Then γS = γ + γ² + γ³ + γ⁴ + … (multiply both sides by γ)
Subtract: S − γS = 1 (all terms cancel except the first)
So S(1 − γ) = 1, which gives S = 1/(1−γ). ✓

This only works when |γ| < 1, so the terms shrink toward zero and the sum converges.
If |γ| ≥ 1, the terms grow (or stay the same), the sum is infinite, and the total multiplier
is undefined — which is why stationarity (|γ| < 1) is required.

#### AR(1) vs. DL(q): A Full Comparison

| Feature | DL(q) | AR(1) |
|---------|-------|-------|
| Lag structure | q+1 free coefficients β₀, β₁, …, β_q | Geometric decay — only β and γ |
| Parameters needed | q+1 | 2 |
| Multicollinearity | High for large q | Low (only one lag of Y needed) |
| Bias when A3 violated | Unbiased (only inefficient) | **Biased** |
| Lag structure flexibility | Completely flexible | Constrained to geometric decay |
| When to prefer | When autocorrelation is suspected | When parsimony matters and A3 is satisfied |

---

### D.5 — The Three-Step Exam Workflow

#### Step 1 — Stationarity Check (Chapter TS_C)

For **each** variable in the model:

1. Plot the series against time. Does it trend up/down? Does variance change?
2. Choose DF version:
   - **No trend visible** → Dickey-Fuller Version 1
   - **Clear trend** or **unsure** → Dickey-Fuller Version 2
3. Run the DF regression, read the t-statistic for the coefficient on Y_{t−1}.
4. Compare to adapted critical values (−2.86 for V1 at 5%, −3.41 for V2 at 5%).
5. **Reject H₀** → series is stationary → use in levels.
6. **Fail to reject H₀** → unit root → take first difference, then re-run DF on ΔY_t.

#### Step 2 — Fit the Model (Chapter TS_D)

**For DL(q):**
- Start with q = q_max (given in the question).
- Drop highest non-significant lag; repeat until highest lag is significant.
- Report all coefficients and the total multiplier = Σβ_k.

**For AR(1):**
- Fit Y_t = α + β X_t + γ Y_{t-1} + ε_t directly.
- Report β, γ, and total multiplier = β/(1−γ).

#### Step 3 — Assumption Check with LMSC (Chapter TS_B)

1. **State hypotheses:** H₀: ρ = 0 (no autocorrelation) vs. H₁: ρ ≠ 0.
2. **Write the auxiliary regression:**
   e_t = α₀ + α₁ X_{1t} + … + α_k X_{kt} + α_{k+1} e_{t−1} + u_t
3. **Compute:** LM = n_aux × R²_aux ~ χ²(1) under H₀
4. **Compare to** χ²(1, 5%) = 3.841.
5. **Conclude** with a full sentence.

---

### D.5 (Worked) — Consumption and Income (Log-Log Model)

**Setup:** Both income (X) and consumption (Y) are log-transformed. Fit a DL(q) on first
differences (log-returns). Data: n = 162 quarterly observations.

#### Step 1 — Stationarity

Both ln(Y) and ln(X) show clear upward trends.

| Variable | DF Version | t-statistic | Critical (5%) | Conclusion |
|----------|-----------|-------------|----------------|-----------|
| ln(Y) — level | V2 (trend) | −1.82 | −3.41 | Fail to reject → unit root |
| ln(X) — level | V2 (trend) | −1.65 | −3.41 | Fail to reject → unit root |
| Δln(Y) — difference | V1 (no trend) | **−9.95** | −2.86 | **Reject → stationary** ✓ |
| Δln(X) — difference | V1 (no trend) | **−12.72** | −2.86 | **Reject → stationary** ✓ |

Both variables need first differencing.

#### Step 2 — Fit DL(q), q_max = 3

| Model | Highest lag t-stat | Significant? | Action |
|-------|-------------------|-------------|--------|
| DL(3) | β₃: t = 0.91 | No | Drop lag 3 |
| DL(2) | β₂: t = 1.38 | No | Drop lag 2 |
| **DL(1)** | **β₁: t = 2.74** | **Yes** | **Stop. q = 1** |

**Fitted model:** ΔŶ_t = 0.004 + 0.350 ΔX_t + 0.182 ΔX_{t−1}

| Coefficient | Value | Interpretation |
|-------------|-------|---------------|
| β̂₀ | 0.350 | A 1 pp rise in income growth raises consumption growth by 0.350 pp this quarter |
| β̂₁ | 0.182 | A 1 pp rise last quarter's income growth raises this quarter's consumption by 0.182 pp |
| **Total multiplier** | **0.532** | A permanent 1 pp rise in income growth raises consumption growth by 0.532 pp long-run |

#### Step 3 — LMSC Test

Auxiliary regression: e_t = α₀ + α₁ ΔX_t + α₂ ΔX_{t−1} + α₃ e_{t−1} + u_t
n_aux = 161, R²_aux = 0.002618

LM = 161 × 0.002618 = **0.4215**
p-value = P(χ²(1) ≥ 0.4215) = **0.5162**

**Conclusion:** Fail to reject H₀. No significant autocorrelation detected. A3 plausibly satisfied. ✓

---

## FORMULA SHEET — The Four Equations You Must Know

### 1. DL(q) Model

$$Y_t = \alpha + \beta_0 X_t + \beta_1 X_{t-1} + \cdots + \beta_q X_{t-q} + \varepsilon_t$$

Total multiplier = β₀ + β₁ + … + β_q = **Σβ_k**

### 2. AR(1) Model

$$Y_t = \alpha + \beta X_t + \gamma Y_{t-1} + \varepsilon_t$$

Total multiplier = **β/(1−γ)** (requires |γ| < 1)

### 3. LMSC Test

Auxiliary regression: e_t = α₀ + α₁ X_{1t} + … + α_k X_{kt} + α_{k+1} e_{t−1} + u_t

$$LM = n \cdot R^2 \sim \chi^2(1) \text{ under } H_0$$

H₀: ρ = 0 (no autocorrelation) | H₁: ρ ≠ 0 (autocorrelation present)
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

## EXAM-DAY CHECKLIST

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
- [ ] Write a full conclusion sentence

---

## COMMON EXAM PITFALLS

### 1. "Reject H₀ means non-stationary" — WRONG
- For the **Dickey-Fuller** test: Reject H₀ means the series **IS stationary** (H₀ is the unit root).
- For the **LMSC** test: Reject H₀ means **autocorrelation IS present** (H₀ is no autocorrelation).
- These are opposite! Know which test you are running before concluding.

### 2. "Take differences whenever the series trends" — BE CAREFUL
- Only take differences if the DF test confirms a **stochastic trend** (unit root, |ρ| = 1).
- If the trend is **deterministic** (|ρ| < 1, λ ≠ 0), add t as a regressor instead.
- **Over-differencing** creates artificial negative autocorrelation and loses information.

### 3. "Use Durbin–Watson for all models"
- DW is **invalid** whenever Y_{t−1} appears as a regressor (AR(1) models).
- Always use **LMSC** — it works for static, DL(q), and AR(1) models.

### 4. "Total multiplier = β₀ only"
- For DL(q): total multiplier = **β₀ + β₁ + … + β_q** (sum of ALL lag coefficients).
- For AR(1): total multiplier = **β/(1−γ)**, not just β.
- β₀ alone is the **immediate effect** only.

### 5. "Unit changes when X is log-differenced"
- If you differenced log(X), a 1-unit rise in Δln(X) means a 1 **percentage point** rise in
  the growth rate — not a 1-unit rise in the level.
- Interpret in terms of percentage changes.

### 6. "Skip the autocorrelation test to save time"
- The LMSC test is worth dedicated exam marks. Always report all five elements:
  H₀/H₁, the auxiliary regression, LM = n × R², comparison to 3.841, and conclusion.

### 7. "Use the regular t-table for the Dickey-Fuller t-statistic"
- The DF t-statistic does NOT follow a t-distribution under H₀.
- Standard critical values (±1.96, ±2.58) do not apply.
- Always use the **adapted DF critical values**: −2.86 (V1, 5%), −3.41 (V2, 5%).

---

## ONE-PAGE SUMMARY

```
FOUNDATIONS  →  Regression: Y = α + βX + ε. OLS finds best-fitting β̂.
                R² measures fit (0–1). t-statistics test if β ≠ 0.
                p-value < 0.05 → significant. Five classical assumptions must hold.

RECOGNISE    →  Time series: order matters. Define lags X_{t-k} and differences ΔX_t.
                Watch sample size (n > 100 ideal). Use real monetary values.

STABILISE    →  Time plot + Dickey-Fuller on every variable.
                Deterministic trend (λ≠0, |ρ|<1)? Add t as regressor.
                Stochastic trend / unit root (|ρ|=1)? Take first differences.
                DF uses special critical values (−2.86 or −3.41), NOT ±1.96.

MODEL        →  Fit DL(q) or AR(1) on stationary variables.
                DL(q): top-down selection of q; total multiplier = Σβ_k.
                AR(1): total multiplier = β/(1−γ); requires |γ| < 1.
                Interpret: temporary vs. maintained, log-returns vs. units.

DIAGNOSE     →  LMSC test: auxiliary regression with lagged residual; LM = n·R² ~ χ²(1).
                Reject H₀ → autocorrelation → re-specify (prefer DL over AR).
                DW statistic: quick check only (not valid for AR models).
```

---

*End of Complete Beginner's Guide to Time Series Regression*
