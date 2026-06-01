# STATISTICS — STUDY GUIDE · PART 2
## Time Series Regression
### Cautions · Autocorrelation · Stationarity · Dynamic Models

---

> **How to read this guide**
>
> | Tag | Meaning |
> |-----|---------|
> | **KEY POINT** | Key concept or definition — must know |
> | **FORMULA** | The equation you need |
> | **INTERPRETATION** | How to read/apply the result in plain English |
> | **SPSS** | Menu path and what to click in SPSS |
> | **WATCH OUT** | Common exam pitfall or subtle distinction |
> | **BEGINNER BOX** | Plain-language foundation — read this if a term is unfamiliar |

---

## FOUNDATIONS — Read This First

*This section did not exist in the original guide. It covers the vocabulary and concepts from basic statistics that the rest of this guide assumes you already know. If you have studied regression before, you can skip ahead to Chapter TS_A.*

---

### F.1 — What is regression?

Regression is a mathematical technique for describing the relationship between variables.

- The variable you are trying to **explain or predict** is called **Y** (the dependent variable, or response).
- The variable(s) you use to **explain** Y are called **X** (the independent variable, or predictor).

A **simple linear regression** says:

```
Y = β₀ + β₁ X + ε
```

In plain English: "Y is approximately equal to a baseline value (β₀) plus some multiple of X (β₁ × X), with some leftover error (ε)."

**Example.** If Y = exam score and X = hours studied, the regression might say:
> Score = 40 + 5 × Hours_studied + ε
>
> → A student who studied 10 hours is predicted to score 40 + 5×10 = 90.

A **multiple regression** simply adds more X-variables:
```
Y = β₀ + β₁ X₁ + β₂ X₂ + … + βₖ Xₖ + ε
```

---

### F.2 — What are coefficients (β values)?

The **β (beta) values** are the numbers the regression estimates from your data. They tell you:

> "If X increases by 1 unit, Y changes by β units on average, *holding everything else constant*."

- β₀ is the **intercept** — the predicted value of Y when all X's equal zero.
- β₁, β₂, … are the **slopes** — how much Y changes per 1-unit increase in that X.

---

### F.3 — What are residuals (errors)?

After fitting a regression, your model predicts a value of Y for each observation. The **residual** (also called the **error**, written ε or *e*) is the gap between the actual Y and the model's prediction:

```
residual (e) = Actual Y − Predicted Y
```

Residuals are important because they tell you how well the model fits. A good model has residuals that look like random noise — no patterns, no trends.

---

### F.4 — What is OLS?

**OLS** stands for **Ordinary Least Squares** — it is the standard method for fitting a regression line. OLS finds the β values that make the sum of the *squared* residuals as small as possible. Under good conditions (the classical assumptions, see F.7), OLS gives the best possible estimates.

---

### F.5 — What is a hypothesis test?

A **hypothesis test** is a formal procedure for deciding whether a pattern in your data is real or just random chance.

Every test has two competing statements:

- **H₀ (null hypothesis):** "There is nothing going on" — the default position.
- **H₁ (alternative hypothesis):** "There IS something going on" — what you are trying to show.

You compute a **test statistic** from your data. If that statistic is extreme enough (far from what you'd expect by chance), you **reject H₀** and conclude there is evidence for H₁.

**The p-value** is the probability of seeing a result this extreme if H₀ were actually true.
- Small p-value (e.g., < 0.05) → the result is unlikely to be random chance → **reject H₀**.
- Large p-value → the result could easily be random → **do not reject H₀**.

**The t-test** is a common test for individual regression coefficients. It asks: "Is βₖ significantly different from zero?" A large absolute t-statistic (typically |t| > 2) and a small p-value means the coefficient is statistically significant.

---

### F.6 — What is R²?

**R² (R-squared)** measures how much of the variation in Y is explained by your model. It ranges from 0 to 1:

- R² = 0 → the model explains nothing.
- R² = 1 → the model explains everything perfectly.
- R² = 0.75 → the model explains 75% of the variation in Y.

A higher R² is generally better, but a high R² does not guarantee the model is correct — especially in time series (see the spurious regression warning in TS_C).

---

### F.7 — What are the classical assumptions?

OLS gives reliable results only when five conditions (the **classical assumptions**) hold:

| # | Assumption | Plain English |
|---|-----------|---------------|
| A1 | E(ε) = 0 | Errors average out to zero — the model is not systematically wrong |
| A2 | Var(ε) = σ² (constant) | Errors have the same spread everywhere (homoskedasticity) |
| A3 | cov(εᵢ, εⱼ) = 0 | Errors are not related to each other (uncorrelated errors) |
| A4 | X's are non-random and not exact combinations of each other | No perfect multicollinearity |
| A5 | ε is normally distributed | (Optional — needed for small samples) |

When these hold, OLS is **BLUE** — the **B**est **L**inear **U**nbiased **E**stimator. "Best" means minimum variance among all linear unbiased estimators. "Unbiased" means that on average the estimates are correct.

When an assumption fails, something goes wrong — either the estimates themselves are wrong (biased), or the standard errors and tests are unreliable, or both.

**Time series data frequently violates A3** — errors close in time tend to be similar to each other. That is the central problem this guide addresses.

---

### F.8 — What is a standard error?

A **standard error** measures the uncertainty in an estimated coefficient. A smaller standard error means you are more confident about the estimate. Standard errors are used to compute t-statistics and confidence intervals. If the standard errors are wrong (because an assumption fails), then all your t-tests and confidence intervals are also wrong — even if the coefficient estimates themselves are fine.

---

### F.9 — What is the chi-squared (χ²) distribution?

The **chi-squared distribution** is a probability distribution used in many statistical tests. You do not need to understand its mathematics — you just need to know:

- It has a parameter called **degrees of freedom (df)**.
- You look up a **critical value** from a table (or use software) for a given df and significance level.
- Your test statistic is compared to this critical value: if the statistic exceeds the critical value, you reject H₀.

In this guide, the chi-squared distribution appears in the **LMSC test** for autocorrelation (TS_B). The test statistic is LM = n × R², and under H₀ it follows a χ²(1) distribution — meaning a chi-squared with 1 degree of freedom.

---

### F.10 — What is white noise?

**White noise** is the name for a perfectly well-behaved random error sequence:
- Mean of zero — no systematic direction.
- Constant variance — equally spread around zero at all times.
- No correlation across time — knowing today's error tells you nothing about tomorrow's.

White noise is what we *want* the residuals of a time-series model to look like. If residuals are not white noise — if they show patterns over time — that is evidence of **autocorrelation**, which violates assumption A3.

---

### F.11 — Quick Greek notation guide

| Symbol | Name | What it usually means in this guide |
|--------|------|--------------------------------------|
| β (beta) | beta | Regression coefficient |
| ε (epsilon) | epsilon | Error / residual term |
| ρ (rho) | rho | Autocorrelation coefficient |
| σ² (sigma squared) | sigma squared | Variance of the errors |
| μ (mu) | mu | Mean (average) |
| λ (lambda) | lambda | Trend coefficient |
| α (alpha) | alpha | Intercept in auxiliary regressions |
| γ (gamma) | gamma | Coefficient on lagged Y in AR(1) |
| δ (delta) | delta | Long-run trend slope |
| Δ (Delta, capital) | Delta | "Change in" — e.g., ΔY = Y_t − Y_{t-1} |
| χ² (chi-squared) | chi-squared | A probability distribution used in tests |

---

---

## Overview — The Time-Series Workflow

When you fit a regression model on time-series data, you go through the same four big steps every time:

| Recognise | Diagnose | Stabilise | Model |
|-----------|----------|-----------|-------|
| **TS_A — Cautions** | **TS_B — Autocorrelation** | **TS_C — Stationarity** | **TS_D — Dynamic models** |
| Time-series ≠ cross-section. Define lags X_{t−q} and differences ΔX_t. Beware too-few data. | Classical assumption A3 violated? Detect via LMSC test. Choose a dynamic model as solution. | Spurious regression risk. Use Dickey-Fuller. Detrend or difference if needed. | Fit DL(q) or AR(1). Determine optimal lag length. Interpret the total multiplier. |

---

> **EXAM RECIPE**
>
> In an exam question on time-series regression you will be told which kind of model to fit (static, DL(q), or AR(1)). You then go through:
> - **Step 1** — Check stationarity of every variable: time plot + Dickey-Fuller. If non-stationary, take differences (or model a deterministic trend).
> - **Step 2** — Fit the model. For DL(q): determine the optimal lag length. Report coefficients and the total multiplier.
> - **Step 3** — Check assumptions, in particular autocorrelation with the LMSC test.

---

### Big picture — connection with Part 1 (Multiple Regression)

Everything from multiple linear regression still applies: model specification, t-test, F-test, R², the 5 classical assumptions, residual plots, multicollinearity, heteroskedasticity. Time series adds three new issues on top:

- **Autocorrelation** — assumption A3 (uncorrelated errors) can fail because errors close in time are similar.
- **Spurious regression / stationarity** — variables that drift over time can look related even when they are not.
- **Dynamic effects** — past values of X (and sometimes Y) influence current Y. New models: DL(q), AR(1).

---

---

## CHAPTER TS_A — Cautions
### *Differences between cross-section and time-series data; lags and differences*

| Section | Topic | You should be able to… |
|---------|-------|------------------------|
| A.1 | Cross-section vs. time series | Explain how time-series data differ and why we must be careful |
| A.2 | Lagged variables X_{t−1}, X_{t−2}, … | Build lags in SPSS; recognise LAG(x,1) notation; interpret |
| A.3 | Difference variables ΔX_t | Build differences in SPSS; recognise DIFF(x,1); interpret |
| A.4 | The three problems | Why we must be careful: data, autocorrelation, stationarity |

---

### A.1 — Cross-section vs. time-series data

> **KEY POINT — Definitions**
>
> **Cross-section.** Data on *many units* at *one moment in time*. The order of rows does not matter; observations are interchangeable. Notation: X_i, with *i* the individual.
>
> **Time-series.** Data on *one unit* collected *over time*. The order of rows carries information — shuffling destroys it. Notation: X_t, with *t* the time index.
>
> **Panel data.** Both at once — many units over many time periods (not exam material here).

**Example — hourly wage**

- *Cross-section:* hourly wage for a sample of Belgian employees in 2010 — one observation per person.
- *Time-series:* average hourly wage for the Belgian population in 2008, 2009, 2010, … — one observation per year.

> **BEGINNER BOX — Why does order matter?**
>
> In a cross-section, swapping two rows (e.g., swapping person 5 and person 12) changes nothing — each person is independent. In a time series, swapping two rows destroys the chronological order and the analysis becomes meaningless. Tuesday's data cannot be placed before Monday's.

---

### A.2 — Lagged variables

A **lagged variable** shifts the time index backwards — it is simply the *past value* of a variable.

> **FORMULA — Lag notation**
>
> X_{t-1} , X_{t-2} , … , X_{t-q}

If *t* is Quarter 3 of 1987, then X_{t-1} is the value of X in Quarter 2 of 1987, and X_{t-2} is the value in Quarter 1 of 1987.

> **BEGINNER BOX — Intuition for lags**
>
> Imagine you are studying whether today's advertising spend affects sales. But maybe it takes a month for the ads to sink in. Then *last month's* advertising spend (X_{t-1}) might be what actually drives *this month's* sales (Y_t). A lagged variable lets you capture this delayed effect.

> **SPSS**
>
> Path: Transform → Create Time Series
> Function: Lag
> Order: 1, 2, 3, … (one new variable per order)
> Internal name: LAG(inf,1), LAG(inf,2), … for the variable *inf*

> **WATCH OUT — You lose observations.**
> For lag *q* you can compute the lag only from t = q+1 onwards, so the lagged variable has **n−q** rather than n observations. This matters when n is small.

---

### A.3 — Difference variables

A **difference variable** measures the *change* between two time points.

> **FORMULA**
>
> ΔX_t = X_t − X_{t-1}   *(absolute first difference)*
>
> Δ₁₂X_t = X_t − X_{t-12}   *(difference of order 12 — for monthly data with yearly seasonality)*

> **BEGINNER BOX — Intuition for differences**
>
> Instead of asking "what is the unemployment rate this month?", differencing asks "how much did the unemployment rate *change* compared to last month?" This shift from *levels* to *changes* is very common in economics because most economic theories talk about changes, not absolute levels.

> **SPSS**
>
> Path: Transform → Create Time Series
> Function: Difference (absolute) — for the relative version use Function: Percentage change
> Internal name: DIFF(u,1), DIFF(u,2), … for the variable *u*

> **INTERPRETATION — Why differences matter**
>
> - They convert an absolute level into a change, which is what most economic theories actually talk about (Δ unemployment, Δ inflation, …).
> - If you take the difference of a log-transformed variable you obtain a **log-return**: Δln(X_t) = ln(X_t / X_{t-1}), often used in finance and macro.
> - Differencing is the standard cure for a stochastic trend (see TS_C).

---

### A.4 — Three problems with time-series regression

Whenever you do regression on time-series data, three issues need attention. The rest of this guide is structured around them.

| PROBLEM 1 — Data | PROBLEM 2 — Autocorrelation | PROBLEM 3 — Spurious / Stationarity |
|-----------------|----------------------------|--------------------------------------|
| You need many observations spanning many time periods, and the data must be of comparable quality. Watch out for inflation when using monetary variables — use real (deflated) values. | Classical assumption A3 (uncorrelated errors) is often violated: an error today carries some memory of yesterday's error. → Chapter TS_B | Two unrelated trending series can produce a hugely significant regression. The underlying issue is that the series are not stationary. → Chapter TS_C |

> **WATCH OUT — Sample size**
>
> Time-series analysis needs many observations. Rules of thumb:
> - Prefer **n > 100**.
> - Absolute minimum: **n ≈ 35** (and at least 10 observations per X-variable).
> - Yearly data → you may need 35 years or more of history; consider monthly or quarterly data if available.
> - For monetary variables, take inflation into account — use real (deflated) values, not nominal ones.

---

---

## CHAPTER TS_B — Autocorrelation
### *Errors that remember the past: detection with the LMSC test*

| Section | Topic | You should be able to… |
|---------|-------|------------------------|
| B.1 | Which assumption fails | Identify A3 (uncorrelated errors) and explain what fails |
| B.2 | First-order autocorrelation ρ | Define AR(1) for errors; interpret sign and magnitude of ρ |
| B.3 | Consequences | List effects on standard errors and (un)biasedness |
| B.4 | Detection — LMSC test | Carry out the LMSC test step by step with descriptive plots |
| B.5 | Solutions | Use a dynamic specification (DL or AR) to remove autocorrelation |

---

### B.1 — Which classical assumption is violated?

> **BEGINNER BOX — Recap of the classical assumptions**
>
> As explained in F.7, OLS is reliable when five conditions hold. The key one for time series is **A3**:
> - A1: E(ε) = 0
> - A2: Var(ε) = σ² is constant (homoskedasticity)
> - **A3: cov(εᵢ, εⱼ) = 0** for any pair (εᵢ, εⱼ)
> - A4: X's are non-random and not exact linear combinations of each other
> - A5: (optional) ε is normally distributed

> **KEY POINT**
>
> When **A3 is violated** — that is, when cov(ε_i, ε_j) ≠ 0 for some i ≠ j — we say the errors are **autocorrelated** (or **serially correlated**).
>
> In time-series data this is the rule rather than the exception: **errors close in time tend to be similar**.

> **BEGINNER BOX — What does "cov(εᵢ, εⱼ) = 0" mean?**
>
> **Covariance** measures whether two things tend to move together. If cov(εᵢ, εⱼ) = 0, knowing the error at one time point tells you nothing about the error at another — they are independent.
>
> Autocorrelation means this is violated: if the error is unusually large *this* period, it tends to also be large *next* period. Imagine a factory that is consistently over-producing for three months — the errors in those months will all be in the same direction, violating A3.

---

### B.2 — First-order autocorrelation

To model the relationship between two consecutive errors, we assume an **AR(1) structure** for the error term:

> **AR(1) STRUCTURE FOR THE ERROR**
>
> ε_t = ρ ε_{t-1} + u_t
>
> ρ is the **first-order autocorrelation coefficient**; u is a classical (non-autocorrelated) error.

> **BEGINNER BOX — What does this equation mean?**
>
> This says: today's error (ε_t) is partly explained by yesterday's error (ε_{t-1}), scaled by ρ, plus a fresh random shock (u_t). The parameter ρ (rho) controls how strongly the past error carries over.

**Interpreting the size of ρ**

- ρ = 0 → no autocorrelation: ε_t = u_t (classical error, A3 satisfied)
- We expect −1 < ρ < 1; otherwise the error term would explode over time.
- |ρ| closer to 1 → the previous error matters more for predicting today's error → stronger autocorrelation.

**Interpreting the sign of ρ**

| ρ > 0 (positive) | ρ < 0 (negative) |
|-----------------|-----------------|
| If ε is high in one period, it tends to stay high in the next | The error oscillates — the sign tends to flip every period |
| The error series shows persistent runs above (or below) zero | Rare in time-series economics; sometimes seen in over-differenced data |
| *Most common case in economics (shocks take time to fade)* | |

---

### B.3 — Consequences

> **CONSEQUENCES — General case**
>
> What goes wrong in OLS when A3 fails?
> - The **formulas for the standard errors are no longer correct**, so confidence intervals and t-/F-tests become misleading.
> - The OLS estimator is **still linear and unbiased**, but it is **no longer best** (no longer BLUE).

> **BEGINNER BOX — Why do wrong standard errors matter?**
>
> Even if your coefficient (e.g., β₁ = 3.5) is correct on average, if the standard error is wrong, then your t-statistic is wrong, your p-value is wrong, and your conclusion about significance is wrong. You might declare a relationship "significant" when it is not, or miss a real relationship. This is why autocorrelation is a serious problem even when it does not bias the coefficients.

> **EXCEPTION — AR(1) MODELS**
>
> **Big exception for autoregressive (AR) models.** When the regression itself contains a lagged dependent variable (Y_{t-1} as regressor) and there is autocorrelation in the error term, the **estimated coefficients become biased**. This is far more serious than the general case.

> **INTERPRETATION — Practical takeaway**
>
> - If autocorrelation is detected in a **static or DL(q) model**, your standard errors and tests are unreliable, but your coefficients are still telling you something true on average.
> - If autocorrelation is detected in an **AR(1) model**, you can no longer trust the coefficient estimates themselves — this is a stronger reason to switch model specifications.

---

### B.4 — Detection: the LMSC test

**Step 0 — Graphical inspection**

Plot residuals *e_t* against time. A clear pattern (waves, trends, clusters above/below zero) is a strong hint that autocorrelation is present.

> **BEGINNER BOX — What does a residual plot look like with autocorrelation?**
>
> - *No autocorrelation:* residuals bounce randomly around zero — sometimes positive, sometimes negative, no pattern.
> - *Positive autocorrelation (ρ > 0):* residuals drift — you see long stretches where they stay positive, then long stretches where they stay negative. Like a slow wave.
> - *Negative autocorrelation (ρ < 0):* residuals rapidly oscillate — +, −, +, −, … like a zigzag.

**The LMSC test — Lagrange Multiplier Serial Correlation**

> **HYPOTHESES**
>
> - H₀: no autocorrelation (equivalent to ρ = 0)
> - H₁: autocorrelation present (equivalent to ρ ≠ 0)

> **LMSC PROCEDURE — 4 steps**
>
> 1. Fit the original regression model and save residuals e_t.
> 2. Build the **auxiliary regression** — regress the residuals on the original X's *plus the lagged residual*:
>    ```
>    e_t = α₀ + α₁ X_{1t} + … + αₖ X_{kt} + α_{k+1} e_{t-1} + u_t
>    ```
> 3. Get the R² of the auxiliary regression and compute:
>    ```
>    LM = n · R²
>    ```
> 4. Under H₀, LM follows a **χ²(1)** distribution. Compare to a critical value or use the p-value.

> **BEGINNER BOX — Why does this test work?**
>
> The auxiliary regression in step 2 asks: "Can yesterday's residual (e_{t-1}) help predict today's residual (e_t)?" If yes (i.e., α_{k+1} is significantly different from zero), then the errors are correlated across time — autocorrelation is present. The LM statistic summarises how much explanatory power the lagged residual adds.

> **WATCH OUT**
>
> - In the auxiliary model the sample size is **n − 1** (you lose one observation because e_{t-1} has no value at t = 1).
> - Higher-order test: add e_{t-2}, e_{t-3}, … to the auxiliary regression. LM then follows a χ² with 2, 3, … df.
> - **Reject H₀ → there IS autocorrelation.** Do NOT reject → assumption A3 is plausibly satisfied.

---

**Worked example — Phillips curve, quarterly Australian data**

Original model: Y_t = β₀ + β₁ X_t + ε_t, with Y = inflation, X = change in unemployment rate, n = 90 (quarterly 1987Q1–2009Q3).

| Auxiliary regression results | Computation |
|------------------------------|-------------|
| Sample size: n = 90 − 1 = **89** | LM = n·R² = 89 × 0.310211 = **27.609** |
| R² of the auxiliary model: **0.310211** | p-value = P(χ²(1) ≥ 27.609) ≈ **1.5 × 10⁻⁷** |
| Coefficient on e_{t-1}: 0.558 (t = 6.219, sig. .000) | **Reject H₀** — autocorrelation is present |

---

**Durbin–Watson — the alternative test**

SPSS prints the **Durbin–Watson statistic** in the regression output. Values close to 2 suggest no autocorrelation; values close to 0 suggest strong positive autocorrelation; values close to 4 suggest strong negative autocorrelation.

> **WATCH OUT — Limitation.**
> Durbin–Watson is **not valid** when the model contains a lagged dependent variable (i.e. for AR models). The LMSC test is preferred because it is valid in both static and AR models.

---

### B.5 — Solutions

More advanced fixes exist (Generalized Least Squares, OLS with Newey–West / HAC standard errors, …) but these are not exam material. The standard route is:

> **SOLUTION STRATEGY**
>
> Re-specify the model to capture the dynamic structure of the data.
> - Add lagged X's → a **Distributed-Lag (DL) model**. See TS_D.
> - Add a lagged Y → an **Autoregressive (AR) model**. See TS_D.
> - If the auxiliary regression keeps coming back significant, you almost certainly need a dynamic specification, not a different test.

> **RULE OF THUMB — DL or AR?**
>
> - If you suspect serial correlation, **DL(q) is preferred** over AR. Why? Because AR is biased when there's residual autocorrelation, whereas DL is only inefficient.
> - DL is more prone to (quasi-)multicollinearity, but multicollinearity is a less severe issue than bias.
> - In DL the standard hypothesis tests are not strictly valid either, but corrections exist.

---

---

## CHAPTER TS_C — Stationarity
### *Spurious regression, the generalized AR(1), and the Dickey-Fuller test*

| Section | Topic | You should be able to… |
|---------|-------|------------------------|
| C.1 | Spurious regression | Explain why two unrelated trending series can look correlated |
| C.2 | Definition of stationarity | State the formal (weak) stationarity conditions; first graphical check |
| C.3 | Generalized AR(1) — 4 cases | Discuss mean, variance and stationarity for each (a, λ, ρ) case |
| C.4 | Trends — deterministic vs. stochastic | Recognise both; choose detrending or differencing |
| C.5 | Solutions for non-stationarity | Apply detrending, model the trend, or take differences |
| C.6 | Dickey-Fuller test | Carry out the DF test (version 1 / version 2) with adapted critical values |

---

### C.1 — Spurious regression

> **PROBLEM 3 — SPURIOUS REGRESSION**
>
> **The problem.** Two time series can show a strikingly significant regression even when there is no economic relationship at all. This is called **spurious regression**.
>
> - Classic example: regress Belgian GDP per capita (1950–2004) on US population density — same period. R² is huge, the slope is significant, and yet the two have nothing to do with one another economically.
> - The shared cause is that **both series have a trend over time**. The regression is picking up the joint drift, not a real relationship.

> **BEGINNER BOX — Why does this happen?**
>
> Imagine two completely unrelated variables that both happen to grow over time — say, the number of TVs sold in Belgium and the average height of NBA players. Both trend upward, so regressing one on the other gives a significant positive coefficient. But TVs do not cause NBA players to grow taller. The trend is a **confounding factor**, creating a fake statistical relationship. This is the essence of spurious regression.

> **LINK TO STATIONARITY**
>
> The deeper reason spurious regression happens is that the variables are **not stationary**. Stationarity is therefore a new assumption added on top of the 5 classical MR assumptions whenever we work with time-series data.

---

### C.2 — Definition of stationarity

Intuitively, a **stationary** time series does not trend or drift. If you cut it in half, the left half and the right half look roughly the same.

> **DEFINITION — Weak stationarity**
>
> A time series Y_t is (weakly) stationary if for every t:
> - **E(Y_t) = μ** — constant mean — series returns to its average
> - **Var(Y_t) = σ²** — constant variance
> - **Cov(Y_t, Y_{t-s}) = γ_s** — the covariance depends only on the lag s, not on t

> **BEGINNER BOX — In plain words**
>
> A stationary series:
> - Oscillates around a fixed average level (no upward or downward drift).
> - Has roughly the same "wobbliness" throughout — it does not get more or less noisy over time.
> - Its relationship with its own past values depends only on how far back, not on *when* you are looking.
>
> A non-stationary series might, for example, keep climbing upward (like GDP) or have variance that grows over time (like stock prices).

**First graphical check**

Plot the series against time. Two warning signs of non-stationarity:
- **The mean changes** — there's a clear upward or downward trend, or seasonal pattern.
- **The variance changes** — the series gets noisier (or quieter) over time.

If the time plot looks like flat noise oscillating around a constant level, the series is plausibly stationary. For a formal verdict, use the Dickey-Fuller test (C.6).

---

### C.3 — The generalized AR(1) model

In its most general form, the building block for studying stationarity is:

> **GENERALIZED AR(1)**
>
> Y_t = a + λ t + ρ Y_{t-1} + ε_t
>
> with ε_t **white noise**: independent, N(0, σ²), mean zero, no autocorrelation.

Three parameters control the behaviour: the constant *a*, the trend coefficient *λ*, and the autoregressive coefficient *ρ*. The **key question** is whether |ρ| < 1 or |ρ| = 1.

> **BEGINNER BOX — What does this equation do?**
>
> This equation says that Y at time t depends on:
> - A baseline level (*a*)
> - A time trend (*λ t*) — if λ > 0, Y naturally drifts upward over time
> - Its own past value (*ρ Y_{t-1}*) — if ρ is close to 1, the past strongly determines the present
> - A random shock (*ε_t*)
>
> By choosing different values of a, λ, and ρ, we can describe many different kinds of time series behaviour.

**The four cases — overview**

| Case 1 — Basic AR(1) | Case 2 — AR(1) + constant |
|----------------------|--------------------------|
| \|ρ\| < 1, a = 0, λ = 0 | \|ρ\| < 1, a ≠ 0, λ = 0 |
| Y_t = ρ Y_{t-1} + ε_t | Y_t = a + ρ Y_{t-1} + ε_t |
| Returns to mean 0. The further ρ is from 0, the longer it stays on one side before reverting. | Stationary about a non-zero mean μ = a / (1 − ρ) |
| ✓ **STATIONARY** | ✓ **STATIONARY** |

| Case 3 — AR(1) + linear trend | Case 4 — Random walk |
|------------------------------|----------------------|
| \|ρ\| < 1, a ≠ 0, λ ≠ 0 | \|ρ\| = 1 |
| Y_t = a + λ t + ρ Y_{t-1} + ε_t | Y_t = a + Y_{t-1} + ε_t |
| Stationary *about* a deterministic trend. The series itself trends, but its deviation from the trend line is stationary. | Stochastic trend. With a = 0: random walk; with a ≠ 0: random walk with drift. Variance grows with t. |
| ✗ **NOT STATIONARY** | ✗ **NOT STATIONARY** |

---

### C.3 (details) — What each case looks like

**Case 1. |ρ| < 1, a = 0, λ = 0 → basic AR(1)**

Model: Y_t = ρ Y_{t-1} + ε_t.

> **FORMULA**
>
> Y_t = ε_t + ρ ε_{t-1} + ρ² ε_{t-2} + … + ρ^t Y₀

- E(Y_t) ≈ 0 (constant)
- Var(Y_t) = σ² / (1 − ρ²) (constant)
- Cov(Y_{t-s}, Y_t) = (σ² ρˢ) / (1 − ρ²) (depends only on lag s)
- Correlation: r(Y_{t-s}, Y_t) = ρˢ → autocorrelation **decays exponentially**. First-order autocorrelation = ρ.

> **INTERPRETATION**
>
> Example. Y_t = 0.7 Y_{t-1} + ε_t. Because ρ = 0.7 > 0, the series tends to stay a while above (or below) its mean before reverting. The closer ρ gets to 1, the slower the revert.

---

**Case 2. |ρ| < 1, a ≠ 0, λ = 0 → AR(1) with non-zero mean**

Model: Y_t = a + ρ Y_{t-1} + ε_t.

> **MEAN, VARIANCE, COVARIANCE**
>
> E(Y_t) ≈ μ = a / (1 − ρ)
> Var(Y_t) = σ² / (1 − ρ²)
> Cov(Y_{t-s}, Y_t) = (σ² ρˢ) / (1 − ρ²)

All three are constant in t, so the series is stationary, this time around a non-zero mean μ.

---

**Case 3. |ρ| < 1, a ≠ 0, λ ≠ 0 → stationary about a deterministic trend**

Model: Y_t = a + λ t + ρ Y_{t-1} + ε_t.

The series itself trends because of the λt term, so by the formal definition it is **not stationary**. But the deviation Y_t − μ − δt is stationary.

> **FORMULA — Stationary trend parameters**
>
> δ = λ / (1 − ρ)
>
> μ = (a − ρδ) / (1 − ρ)

> **INTERPRETATION**
>
> Example. Y_t = 1 + 0.05 t + 0.7 Y_{t-1} + ε_t.
> - δ = 0.05 / (1 − 0.7) = 1/6
> - μ = (1 − 0.7 · 1/6) / (1 − 0.7) = 53/18
> - So Y_t − 53/18 − (1/6)t is a stationary AR(1) about 0.

---

**Case 4. |ρ| = 1 → random walk(s)**

When ρ = 1 the AR(1) becomes a **random walk**. Three sub-cases matter:

> **THE THREE RANDOM-WALK CASES**
>
> 1. **Random walk** (a = 0, λ = 0): Y_t = Y_{t-1} + ε_t
>    - E(Y_t) = y₀ (constant), but Var(Y_t) = t σ² → variance grows with time. ✗ not stationary.
>
> 2. **Random walk with drift** (a ≠ 0, λ = 0): Y_t = a + Y_{t-1} + ε_t
>    - E(Y_t) = ta + y₀ → mean drifts up (or down) over time. ✗ definitely not stationary.
>
> 3. **Random walk with drift and trend** (a ≠ 0, λ ≠ 0): Y_t = a + λt + Y_{t-1} + ε_t
>    - Mean grows like ta + ½ t(t+1) λ → even faster drift. ✗ not stationary.

> **BEGINNER BOX — What is a random walk?**
>
> Imagine flipping a coin each day. Heads = take one step right, tails = take one step left. Your position after many days is a random walk. You have no idea where you will end up — the variance of your position grows over time. Many financial prices behave approximately like random walks: today's price is yesterday's price plus a random surprise.

> **KEY POINT — Summary card**
>
> - |ρ| < 1, λ = 0: **stationary** (Cases 1–2). No problem in regression.
> - |ρ| < 1, λ ≠ 0: **stationary about a deterministic trend** (Case 3). Problem — fix with detrending.
> - |ρ| = 1: **stochastic trend / random walk** (Case 4). Problem — fix with differencing.

---

### C.4 — Deterministic vs. stochastic trends

| Deterministic trend | Stochastic trend |
|--------------------|-----------------|
| Comes from a λt term → mean changes, variance stays constant | Comes from |ρ| = 1 → random walk. Mean may or may not drift, but **variance grows with time** |
| Types: linear (μ + δt); seasonal (monthly / quarterly dummies) | Types: random walk; random walk with drift; random walk with drift and trend |
| Example: monthly unemployment figures in Flanders — same months cluster together | Example: many financial prices behave roughly as random walks with drift |

> **BEGINNER BOX — Deterministic vs. stochastic in plain terms**
>
> - A **deterministic trend** is predictable and fixed: e.g., "on average, GDP grows by exactly 2% per year." Remove it by subtracting the trend line.
> - A **stochastic trend** is random and cumulative: each period the series takes a random step, and those steps accumulate unpredictably. You cannot remove it by subtracting a trend line — you must take differences instead.

> **WATCH OUT**
>
> In practice it is often hard to tell which is which just from a plot. The standard pragmatic answer: include both possibilities (**model 3 of the DF test**) when you are unsure — i.e. random walk with drift and trend.

---

### C.5 — Solutions for non-stationarity

**If the problem is a deterministic trend (λ ≠ 0, |ρ| < 1)**

> **FIX A — DETERMINISTIC TREND**
>
> - **Option 1 — detrending.** Replace the non-stationary Y_t by Y_t − μ − δt, which is stationary.
> - **Option 2 — model the trend.** Equivalent to Option 1: keep Y_t but add a linear-trend term to the regression model:
>   ```
>   Y_t = β₀ + β₁ X_t + εt    becomes    Y_t = α + λ t + β₁ X_t + εt
>   ```
> - **Option 3 — seasonal differencing.** For seasonal trends (e.g. monthly data), use Δ₁₂ X_t = X_t − X_{t-12} — the change vs. the same month one year earlier.

**If the problem is a stochastic trend (|ρ| = 1)**

> **FIX B — STOCHASTIC TREND**
>
> **Take first differences.** Detrending does not work — that fix is for deterministic trends only. Instead, replace each variable by its first difference:
> ```
> ΔY_t = Y_t − Y_{t-1},   ΔX_t = X_t − X_{t-1}
> ```
> - If after one round of differencing the variables are now stationary, fit your regression on the differences.
> - Why it works: if Y_t = Y_{t-1} + ε_t, then ΔY_t = ε_t, which is white noise — stationary.
> - If even the first differences are not stationary, try **second differences** Δ²Y_t = ΔY_t − ΔY_{t-1}.

> **INTERPRETATION — Worked example**
>
> GDP and Gross National Income (Belgium, 1950–2004):
> - Both series clearly trend upward over time. A regression in levels would be spurious.
> - After taking first differences (or relative differences), the trends disappear. The relationship between ΔGDP and ΔGNI remains and is now economically meaningful.

---

### C.6 — The Dickey-Fuller test

Until now, choosing between stationary and non-stationary was a judgement call from a time plot. The **Dickey-Fuller (DF) test** makes it formal: it is a **unit-root test** — it tests whether ρ = 1 in the generalized AR(1).

> **BEGINNER BOX — What is a "unit root"?**
>
> A "unit root" simply means ρ = 1 in the AR(1) model — i.e., the series is a random walk and therefore non-stationary. The name comes from the mathematics of the equation, but all you need to remember is: **unit root = non-stationary = problem**.

> **HYPOTHESES**
>
> - **H₀:** ρ = 1 (unit root — series is **NOT** stationary)
> - **H₁:** |ρ| < 1 (series **IS** stationary, possibly about a deterministic trend)

> **DICKEY-FULLER REGRESSIONS**
>
> The trick: take first differences and reparameterise. Setting α₁ = ρ − 1, we get:
>
> **Version 1 — no trend:**
> ΔY_t = α₀ + α₁ Y_{t-1} + ε_t
>
> **Version 2 — with linear trend:**
> ΔY_t = α₀ + λ t + α₁ Y_{t-1} + ε_t
>
> Reject H₀ ⟺ α₁ < 0 (significantly).

> **WATCH OUT — Adapted critical values**
>
> Under H₀ the t-statistic is **NOT t-distributed** — you cannot use the usual t-critical values. Use the adapted table below.
>
> *Why not? When ρ = 1, the series is non-stationary, and the usual statistical theory that gives the t-distribution breaks down. Dickey and Fuller derived the correct distribution for this situation, and it requires more negative critical values than the standard t-distribution.*

**Critical values for the DF t-statistic**

| DF version | 1%-level | 5%-level | 10%-level |
|------------|----------|----------|-----------|
| Version 1 — without trend | −3.43 | **−2.86** | −2.57 |
| Version 2 — with trend | −3.96 | **−3.41** | −3.13 |

**Decision rule.** If the t-stat on Y_{t-1} is **more negative** than the critical value, **reject H₀** → the series is stationary.

> **HOW TO RUN THE DF TEST — 4 steps**
>
> 1. Plot the data versus time.
> 2. No visible trend? Use Version 1 (no trend). Clear trend? Use Version 2 (with trend). Unsure? Use Version 2 — it's the safer default.
> 3. Run the chosen DF regression with ΔY_t as response and Y_{t-1} as regressor (plus the time variable for Version 2).
> 4. Read the t-statistic for the coefficient of Y_{t-1} and compare to the adapted critical values above.

---

**Reference — mean of a stationary AR(1)**

| Model | Mean / behaviour |
|-------|-----------------|
| Y_t = ρ Y_{t-1} + ε_t | stationary, mean 0 |
| Y_t = a + ρ Y_{t-1} + ε_t | stationary, mean μ = a / (1 − ρ) |
| Y_t = a + λ t + ρ Y_{t-1} + ε_t | stationary about a deterministic trend μ + δt, with δ = λ / (1 − ρ), μ = (a − ρδ) / (1 − ρ) |

---

---

## CHAPTER TS_D — Dynamic models
### *DL(q), AR(1), total multipliers, and the time-series exam workflow*

| Section | Topic | You should be able to… |
|---------|-------|------------------------|
| D.1 | Distributed lag model DL(q) | Write the equation; interpret coefficients; find total multiplier |
| D.2 | Optimal lag length | Pick q starting from qmax by removing non-significant top lags |
| D.3 | Autoregressive model AR(1) | Write the equation; interpret coefficients; find total multiplier β/(1−γ) |
| D.4 | Link DL(∞) ↔ AR(1) | Show how AR(1) is an infinite-lag DL; derive geometric weights |
| D.5 | Three-step exam workflow | Combine stationarity, fit, assumption check on a real exam problem |

---

### D.1 — Distributed lag model DL(q)

In a static model, Y depends only on the current X. But economic effects are rarely instantaneous: training today changes accident counts months later; a tax cut today affects consumption next quarter. To capture this we use a **distributed lag model**:

> **DL(q) MODEL**
>
> Y_t = α + β₀ X_t + β₁ X_{t-1} + β₂ X_{t-2} + … + β_q X_{t-q} + ε_t
>
> **Total multiplier = Σ β_k** (sum over k = 0, 1, …, q)

> **BEGINNER BOX — What does DL(q) mean?**
>
> The DL(q) model simply includes *q* past values of X as additional predictors. The subscript "q" is the number of lags included. For example, DL(2) would include X_t, X_{t-1}, and X_{t-2}. Each β_k captures how much Y changes due to X from *k* periods ago.

> **SPSS — How to set up DL(q)**
>
> - Transform → Create Time Series → Function: Lag, Order: 1, 2, …, q to make the lagged variables.
> - Analyze → Regression → Linear: put Y as Dependent and X_t, X_{t-1}, …, X_{t-q} as Independents.
> - Sample size shrinks to **n − q**.

---

**Interpreting the coefficients of DL(q)**

> **KEY POINT**
>
> As in any regression: β_k is the average change in Y when X_{t-k} rises by 1 unit, holding all other variables constant.

| Temporary change *(X rises by 1, then returns)* | Maintained change *(X rises by 1 and stays high)* |
|--------------------------------------------------|---------------------------------------------------|
| Immediate effect: β₀ | Immediate effect: β₀ |
| After 1 period: β₁ | After 1 period: β₀ + β₁ |
| After 2 periods: β₂, and so on | After 2 periods: β₀ + β₁ + β₂ |
| The effect dies out once you go beyond lag q | After q or more periods the total effect is **Σ β_k = total multiplier** |

> **INTERPRETATION**
>
> - The **total multiplier** is the long-run effect on Y of a permanent 1-unit rise in X.
> - It answers the exam question: "by how much will Y eventually go up if X increases by 1 unit and stays there forever?"

---

### D.2 — Choosing the optimal lag length q

> **OPTIMAL LAG LENGTH — Procedure (top-down)**
>
> Start from a maximum lag q_max (given in the exam, e.g. q_max = 3 or 4) and shrink it:
> 1. Fit the DL(q_max) model. Look at the t-test for the **highest-order lag**, β_{q_max}.
> 2. If it is **not significant**, drop that lag and refit DL(q_max−1). Repeat.
> 3. Stop as soon as the t-test for the largest remaining lag **is significant**. That q is your optimal lag length.

> **INTERPRETATION — Worked example: safety training and accident losses**
>
> - Goal: model monthly accident losses (Y, euro) as a function of monthly safety-training hours (X), with q_max = 4.
> - Build X_{t-1}, X_{t-2}, X_{t-3}, X_{t-4} and fit DL(4).
> - The t-test on β₄ is not significant → drop the lag, refit DL(3); β₃ also not significant → refit DL(2); β₂ not significant → refit DL(1); β₁ is significant. **Stop: optimal lag is q = 1.**
> - Now read off β₀ and β₁, compute the total multiplier, and interpret it.

---

### D.3 — Autoregressive model AR(1)

In a DL(q) model the dynamics come from past X's. We can instead let **past Y** carry the memory:

> **AR(1) MODEL**
>
> Y_t = α + β X_t + γ Y_{t-1} + ε_t
>
> **Total multiplier = β / (1 − γ)**
> (geometric-series formula; requires |γ| < 1)

> **BEGINNER BOX — Why use past Y?**
>
> Sometimes Y is self-reinforcing: high GDP growth this year tends to cause high GDP growth next year (confidence, investment cycles, etc.). Including Y_{t-1} as a predictor directly captures this "inertia" without needing to add many lags of X. It is a more parsimonious (efficient) model when the persistence in Y is the main dynamic.

**Interpreting AR(1)**

- **Immediate effect** (temporary or maintained 1-unit rise in X): β.
- **Long-run effect** of a maintained 1-unit rise in X: β / (1 − γ) → the total multiplier.
- A **temporary** 1-unit rise in X gives a one-off jump of β, then a smaller residual effect on Y in every subsequent period that fades by a factor γ.

> **INTERPRETATION — Worked example**
>
> Y = 20 + 10 X + 0.5 Y_{t-1}. In year 5, X temporarily rises by 1.
> - Year 5: Y jumps by **10** (the β coefficient).
> - Year 6: Y rises by 0.5 × 10 = **5** relative to its original level — even though X is back to normal — because Y₅ was elevated.
> - Year 7: effect is 0.5² × 10 = 2.5; year 8: 0.5³ × 10 = 1.25, …
> - Total multiplier = 10 / (1 − 0.5) = **20**. If X had stayed at the new level, Y would eventually rise by 20.

---

**Worked example — education spending and GDP growth**

Setup. Yearly US data since 1910. X = dollars invested in education per child, Y = GDP growth (%). Fit an AR(1):

```
Ŷ_t = 1.01 + 0.009 X_t + 0.627 Y_{t-1}
```

- Total multiplier = β / (1 − γ) = 0.009 / (1 − 0.627) = **0.024**
- Interpretation: if the investment per child increases by 1 dollar and is maintained over the years, then GDP growth rises on average by **0.024 percentage points** in the long run.

---

### D.4 — Link between AR(1) and DL(∞)

Why does the AR(1) total multiplier have the specific shape β / (1 − γ)? Because **AR(1) is secretly a DL model with infinitely many lags**.

> **AR(1) UNROLLED → DL(∞)**
>
> Y_t = α + β X_t + γ Y_{t-1} + ε_t
>      = α + β X_t + γ(α + β X_{t-1} + γ Y_{t-2}) + ε_t
>      … repeating to infinity …
>      = α' + β X_t + βγ X_{t-1} + βγ² X_{t-2} + βγ³ X_{t-3} + … + ε'_t

> **KEY POINT — Geometric-series consequence**
>
> The total multiplier of the AR(1) model is the infinite sum:
>
> Σ β_k = β(1 + γ + γ² + γ³ + …) = **β / (1 − γ)**
>
> This is the geometric series 1 + q + q² + … = 1/(1−q) from the formula sheet, converging when |γ| < 1.

> **BEGINNER BOX — What is a geometric series?**
>
> A geometric series is a sum where each term is a fixed multiple of the previous one: 1 + 0.5 + 0.25 + 0.125 + … When the multiplier is between −1 and 1, this infinite sum converges to a finite number: 1/(1 − 0.5) = 2. That is exactly the formula β/(1−γ) in the AR(1) total multiplier.

> **INTERPRETATION — Why does this matter?**
>
> - AR(1) gives you **long memory with only two coefficients** (β and γ), instead of many β_k's. Much less prone to (quasi-)multicollinearity than DL(q) with large q.
> - **Drawback:** AR(1) is biased when there is residual autocorrelation (see B.3). DL(q) is the safer choice when you suspect that.
> - The model with more lags of both X and Y is the ARDL(p, q) model. The AR(1) is the special case ARDL(1, 0). ARDL is not exam material.

---

### D.5 — The three-step exam workflow

This is the procedure to follow whenever an exam question asks you to fit a static, DL(q), or AR(1) model on time-series data. The model type will be specified — you do not have to choose. You go through three steps in order.

| STEP 1 — Stationarity *(TS_C)* | STEP 2 — Fit the model *(TS_D)* | STEP 3 — Check assumptions *(TS_B)* |
|-------------------------------|--------------------------------|-------------------------------------|
| Time plot of every variable. Decide DF version (no-trend or with-trend). Run the DF test on each variable, read t-stat, compare with adapted critical values. Unit root anywhere? → take Δ of all variables, re-test on Δ. | Use the variables you have ended up with (levels or differences). For DL(q), determine the optimal lag length. Report all coefficients and the total multiplier. | Run the LMSC test on the fitted model's residuals. Report H₀/H₁, the auxiliary regression, LM = n·R², the p-value, and the conclusion. Also briefly mention the other classical assumptions. |

---

**Step-by-step worked example — consumption ~ income (log-log)**

Setup. Both income (X) and consumption (Y) are log-transformed, then we fit a DL(q) model on their differences.

**STEP 1 — Stationarity**
- Time plots of Y and X show clear upward trends. Run DF on the levels — fail to reject H₀ for both. Both variables have a unit root.
- Take first differences (which are log-returns): ΔY and ΔX. Run DF Version 1 (no visible trend in the differences).
- ΔY: t = −9.95, well below −2.86. **Reject H₀** → stationary.
- ΔX: t = −12.72, also well below −2.86. **Reject H₀** → stationary.
- Both variables are stationary after differencing; we proceed with the differences.

**STEP 2 — Fit the model**
- Build lags of ΔX up to q_max = 3.
- Start with DL(3): β₃ not significant → drop. DL(2): β₂ not significant → drop. DL(1): β₁ is significant. Stop. **Optimal lag is q = 1.**
- Fitted model: ΔŶ_t = 0.004 + 0.35 ΔX_t + 0.182 ΔX_{t-1}
- Total multiplier = 0.35 + 0.182 = **0.532**
- Interpretation (log-returns!): if the relative change in income rises by 1 percentage point and is maintained, then the relative change in consumption rises on average by **0.532 percentage points** after one quarter.

**STEP 3 — Assumption check (LMSC test)**
- Auxiliary regression: e_t = α₀ + α₁ ΔX_t + α₂ ΔX_{t-1} + α₃ e_{t-1} + u_t
- Sample size n = 161 (one observation lost to the lagged residual).
- R² of the auxiliary regression: 0.002618. LM = 161 × 0.002618 = **0.4215**
- p-value = P(χ²(1) ≥ 0.4215) = 0.5162. **Do not reject H₀** → no significant autocorrelation. Assumption A3 is plausibly satisfied. ✓

---

---

## EXAM-DAY CHECKLIST — Time-Series Regression

| STEP 1 — STATIONARITY | STEP 2 — FIT MODEL | STEP 3 — ASSUMPTIONS |
|-----------------------|--------------------|-----------------------|
| Time plot of every variable | Static / DL(q) / AR(1) — given in the question | State H₀ / H₁ in plain English |
| Choose DF version (no-trend or with-trend) | For DL: find optimal q starting from q_max (drop top lags until significant) | Write the auxiliary regression (X's + lagged residual) |
| Run DF on each variable, read t-stat, compare with adapted critical values | Report coefficients + total multiplier (Σβ or β/(1−γ)) | Compute LM = n·R²; compare to χ²(1) |
| Unit root anywhere? → take Δ of all variables, re-test on Δ | Interpret with the right words: temporary vs. maintained, log-return vs. unit change | Conclude — autocorrelation present or assumption satisfied |

---

## Formula Sheet — The Four Equations You Really Need

> **THE FOUR EQUATIONS**
>
> **1. DL(q) model and its total multiplier:**
> ```
> Y_t = α + β₀ X_t + β₁ X_{t-1} + … + β_q X_{t-q} + ε_t  ;  Σ β_k
> ```
>
> **2. AR(1) model and its total multiplier:**
> ```
> Y_t = α + β X_t + γ Y_{t-1} + ε_t  ;  β / (1 − γ)
> ```
>
> **3. LMSC test — auxiliary regression and statistic:**
> ```
> e_t = α₀ + α₁ X_{1t} + … + αₖ X_{kt} + α_{k+1} e_{t-1} + u_t
> LM = n · R²  ~  χ²(1)
> ```
>
> **4. Dickey-Fuller test — two versions:**
> ```
> Version 1:  ΔY_t = α₀ + α₁ Y_{t-1} + ε_t
> Version 2:  ΔY_t = α₀ + λ t + α₁ Y_{t-1} + ε_t
> ```
> Critical values: 5% → **−2.86** (V1), **−3.41** (V2). Reject H₀ if t-stat is more negative.

---

## Common Exam Pitfalls — Seven to Remember

> **SEVEN PITFALLS**
>
> 1. **"Reject H₀ means stationary."** For DF, yes — Reject = Stationary. But many people confuse DF with the LMSC test, where Reject = autocorrelation present (bad news). Always re-read the hypotheses.
>
> 2. **"Take differences whenever in doubt."** Over-differencing creates artificial negative autocorrelation. Only difference if the DF test (or the time plot) tells you to.
>
> 3. **"Use Durbin–Watson for AR(1)."** Durbin–Watson is **not valid** when a lagged dependent variable is in the model. Use LMSC.
>
> 4. **"Total multiplier = β₀ only."** No — for DL(q) it is the **sum of all β_k's**. For AR(1) it is β / (1 − γ), not just β.
>
> 5. **"Interpret as units when X is logged."** If you took log-differences (log-returns), interpret as **percentage-point changes**, not unit changes.
>
> 6. **"Skip the assumption check."** The LMSC test is worth easy marks and must be reported with H₀/H₁, LM-statistic, p-value, and a conclusion sentence.
>
> 7. **"Use the t-distribution for the DF t-stat."** Under H₀ it is **not t-distributed**. Always use the adapted critical values (−2.86, −3.41, …).

---

## One-Page Summary — The Whole Guide in Four Lines

> **Recognise** the data is time series → define lags, define differences.
>
> **Diagnose** autocorrelation with LMSC — but think first about whether you need a dynamic model.
>
> **Stabilise** with detrending (deterministic trend) or differencing (stochastic trend / unit root).
>
> **Model** with DL(q) or AR(1) — find the optimal q, interpret the total multiplier, run LMSC.
