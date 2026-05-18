# Step-by-Step SPSS Guide — Multiple Linear Regression
### Project: Determinants of Monthly Online Spending (Online Shopping Belgium survey, n = 111)

This guide is written specifically for **`Regression_data_.xlsx`** (11 columns) and follows
the structure required by **QRP 3 (Data)**, **QRP 4 (Regression analysis)** and the
lecturer's notes ("DUE MAY 20TH"). Every SPSS menu path is given as
`Menu → Submenu → Dialog`. Numbers shown are pre-computed so you can **verify your own
SPSS output matches** — if a number is far off, something is set up wrong.

> Golden rules from the notes, applied throughout:
> - **Never paste raw SPSS output** in the text — build your own tables. Full output → appendix.
> - **Do NOT write the model as** `Y = β0 + β1x1 + …`. Report a **table** of variables + coefficients + significance.
> - Univariate **must include Y**. Start the Data section text by **explaining Y first**.
> - Assumptions in the text = **one short paragraph** (residual plot, White/heteroscedasticity, multicollinearity/VIF, QQ plot). Full checks → appendix.
> - Always report each effect with its significance: *"… this effect is significant (t = …, p = …)"*.

---

## 0. The variables (define every one — the notes require this)

| Role | Variable | Meaning | How measured / units | Type for SPSS |
|---|---|---|---|---|
| **Y** | `MonthlyOnlineSpend_Y` | Monthly online spend | € (bin midpoints: 25 / 75 / 125 / 175 / 225) | Scale (quantitative) |
| X | `Age` | Respondent age | Years | Scale |
| X | `EmploymentLevel` | Employment status | 1, 2, 3 (categories) | **Nominal → use dummies** |
| X | `MonthlyIncome` | Gross monthly income band | 1=€0–999 … 5=€4000+ (5 missing) | Ordinal |
| X | `DisposableIncome` | Income after expenses | 1=€0–499 … 4=€1500+ (11 missing) | Ordinal |
| X | `ShoppingFrequency` | How often shops online | 1=<1/mo … 5=>10/mo | Ordinal |
| X | `AvgPerPurchase` | Spend per purchase | € (midpoints 12 … 125) | Scale |
| X | `WhyShop_Avg` | Motivation composite | Mean of Likert items, 1–5 | Scale |
| X | `Influence_Avg` | Purchase-influence composite | Mean of Likert items, 1–5 | Scale |
| X | `HoursOnline` | Daily hours online | 1=<2h … 5=>10h | Ordinal |
| X | `SocialMediaDiscovery` | Discovers products via social media | 1–5 | Ordinal |

**Note on income:** `MonthlyIncome` and `DisposableIncome` both measure income and are
correlated → keep **only one** in the model (recommended: `DisposableIncome`) to avoid
quasi-multicollinearity (QRP 3, "do not mix"; QRP 4, assumption A4).

**Note on `AvgPerPurchase`:** spend-per-purchase is mechanically linked to monthly spend.
Including it answers "do bigger baskets mean more spend"; be ready to justify it
theoretically (QRP 4: *"use theoretical framework, don't merely sum up"*).

---

## 1. Prepare the data in SPSS (do this first)

1. **Import:** `File → Import Data → Excel…` → select `Regression_data_.xlsx` →
   tick *Read variable names from first row* → OK.
2. **Variable View** (bottom tab): for each variable set the **Measure** column:
   - `Scale` → Y, Age, AvgPerPurchase, WhyShop_Avg, Influence_Avg
   - `Ordinal` → MonthlyIncome, DisposableIncome, ShoppingFrequency, HoursOnline, SocialMediaDiscovery
   - `Nominal` → EmploymentLevel
3. **Missing values:** the 5 + 11 blank income cells are already system-missing (empty).
   Leave as is. SPSS regression uses **listwise deletion** → effective **n ≈ 100**.
   You will mention this in the *Data* section as a limitation (QRP 3: "missing values").
4. **Create the employment dummies** (`EmploymentLevel` has 3 categories → **2 dummies**,
   one reference category):
   `Transform → Compute Variable`
   - Target `Emp2` → Numeric Expression: `EmploymentLevel = 2`
   - Target `Emp3` → Numeric Expression: `EmploymentLevel = 3`
   (Category 1 is the **reference** — interpret Emp2/Emp3 *relative to category 1*.)

---

## 2. Univariate descriptive statistics + a graph for every variable

> Goal (QRP 3): for **quantitative** variables report min, max, mean, SD, skewness +
> **histogram**; for **qualitative** (`EmploymentLevel`) report a **frequency table** +
> bar chart. **Include Y.**

### 2a. Quantitative variables (Y + all scale/ordinal X)
`Analyze → Descriptive Statistics → Frequencies`
- Move in: Y, Age, MonthlyIncome, DisposableIncome, ShoppingFrequency,
  AvgPerPurchase, WhyShop_Avg, Influence_Avg, HoursOnline, SocialMediaDiscovery
- **Statistics** button → tick: Mean, Std. deviation, Minimum, Maximum, **Skewness**, Kurtosis
- **Charts** button → *Histograms* + tick *Show normal curve on histogram*
- Untick *Display frequency tables* (too long for scale vars) → OK

**Expected values to verify against (n = 111 unless noted):**

| Variable | Mean | SD | Min | Max | Skew | Comment |
|---|---|---|---|---|---|---|
| **MonthlyOnlineSpend_Y** | 62.84 | 46.82 | 25 | 225 | **+1.37** | right-skewed → log candidate |
| Age | 23.87 | 3.26 | 18 | 40 | **+1.59** | right-skewed, narrow (students) |
| MonthlyIncome | 1.81 | 1.08 | 1 | 5 | +1.25 | 5 missing |
| DisposableIncome | 1.77 | 1.07 | 1 | 4 | +1.06 | 11 missing |
| ShoppingFrequency | 1.71 | 0.81 | 1 | 5 | +1.08 | most shop 1–2×/mo |
| AvgPerPurchase | 44.39 | 26.57 | 12 | 125 | +0.80 | mild right skew |
| WhyShop_Avg | 3.25 | 0.62 | 1 | 4.62 | −0.59 | roughly symmetric |
| Influence_Avg | 3.46 | 0.61 | 1 | 4.50 | **−1.55** | **left**-skewed |
| HoursOnline | 2.50 | 1.09 | 1 | 5 | +0.51 | ~symmetric |
| SocialMediaDiscovery | 3.01 | 0.93 | 1 | 5 | −0.15 | ~symmetric |

### 2b. Qualitative variable — `EmploymentLevel`
`Analyze → Descriptive Statistics → Frequencies` → add `EmploymentLevel` →
keep *Display frequency tables* on → **Charts → Bar chart** → OK.

Expected frequencies: **1 → 33 (29.7%) · 2 → 50 (45.0%) · 3 → 28 (25.2%)**.
All categories occur with enough cases → keep all (2 dummies).

### 2c. Boxplots (outliers — QRP 3)
`Analyze → Descriptive Statistics → Explore` → Dependent List = Y (and any scale X) →
Plots → tick *Boxplot* → OK. Note any flagged points; **do not delete blindly** (QRP 3:
"never just remove observations") — they will be re-examined in the residual plot.

> **Build your own summary table** in the report (like 2a above). Put the SPSS
> histograms/frequency output in the **appendix** and summarise in 1 short paragraph.

---

## 3. Bivariate descriptive statistics (each X vs Y)

> Goal (QRP 3): quantitative X → **scatterplot + Pearson correlation**;
> qualitative X → **boxplot / mean of Y per group**.

### 3a. Quantitative X vs Y — correlations
`Analyze → Correlate → Bivariate` → move in Y + all scale/ordinal X →
Pearson → Flag significant correlations → OK.

**Expected correlation of each X with Y (verify):**

| X vs Y | Pearson r | p | Strength |
|---|---|---|---|
| ShoppingFrequency | **+0.62** | <0.001 | strong + |
| AvgPerPurchase | **+0.54** | <0.001 | moderate + |
| DisposableIncome | +0.45 | <0.001 | moderate + |
| MonthlyIncome | +0.40 | <0.001 | moderate + |
| EmploymentLevel | +0.25 | 0.009 | weak + |
| WhyShop_Avg | +0.19 | 0.050 | weak (borderline) |
| Age | +0.04 | 0.65 | none |
| Influence_Avg | −0.01 | 0.90 | none |
| HoursOnline | −0.02 | 0.81 | none |
| SocialMediaDiscovery | −0.06 | 0.53 | none |

### 3b. Scatterplots
`Graphs → Chart Builder → Scatter/Dot → Simple Scatter` → Y on Y-axis, X on X-axis → OK.
Double-click chart → *Add Fit Line at Total* (linear) to see direction/strength and
spot **non-linearity / heteroscedasticity / outliers** (QRP 3). Do this at least for the
strong predictors (ShoppingFrequency, AvgPerPurchase, DisposableIncome).

### 3c. Qualitative X (`EmploymentLevel`) vs Y
- `Analyze → Compare Means → Means`: Dependent = Y, Independent = EmploymentLevel.
  Expected mean Y: **cat 1 ≈ 49.2 · cat 2 ≈ 62.0 · cat 3 ≈ 80.4** → spend rises with
  employment level.
- `Graphs → Chart Builder → Boxplot` of Y by EmploymentLevel for the appendix.

---

## 4. Skewness — when and how to use the `ln` transformation

**Rule (QRP 3):** `ln` only fixes **right-skewed**, strictly positive variables
(typical for "size"/"price"/"spend"). It does **not** fix left skew.

| Variable | Raw skew | ln skew | Action |
|---|---|---|---|
| **MonthlyOnlineSpend_Y** | +1.37 | **+0.35** | **Transform Y → `ln(Y)`** ✔ (big improvement) |
| AvgPerPurchase | +0.80 | −0.49 | Optional; ln slightly over-corrects → keep raw or test both |
| Age | +1.59 | +0.89 | ln helps little; keep raw (range is narrow anyway) |
| Influence_Avg | −1.55 | worse | **left-skewed → do NOT log** |
| WhyShop_Avg, HoursOnline, SocialMediaDiscovery | small | — | leave raw |
| MonthlyIncome / DisposableIncome / ShoppingFrequency | ~+1 | mild | ordinal codes — leave raw, treat as ordinal |

**Create ln(Y):** `Transform → Compute Variable` → Target `lnY` →
Numeric Expression: `LN(MonthlyOnlineSpend_Y)` → OK.
Re-run the histogram on `lnY` to confirm it looks ~symmetric (skew ≈ +0.35).

**Why this matters here:** with raw Y the residuals are **non-normal**
(Shapiro p ≈ 0.03 → A5 fails). With **ln(Y)** the residuals become normal
(Shapiro p ≈ 0.60), White's test is fine, and coefficients gain a clean **%
interpretation** ("a one-unit rise in X changes spend by ≈100·β %"). **Use the ln(Y)
model as your main model** and mention you tested both (QRP 4: sensitivity analysis).

---

## 5. Data section — what to write (text)

Order required by the notes:
1. **Start by explaining Y** — what monthly online spend is, the € midpoint coding, its
   distribution (right-skewed → log-transformed), why it is a valid continuous response.
2. **Then summarise** the univariate findings (1 short paragraph + your own table) and
   the bivariate findings (which X correlate strongly with Y: ShoppingFrequency,
   AvgPerPurchase, DisposableIncome positively; Employment level groups differ).
3. **Describe each variable** (meaning, units, expected relation to Y), citing your
   literature review ("we expect higher disposable income → higher spend, in line with …").
4. State **limitations**: convenience sample, students-heavy (narrow Age), bin-coded Y/spend,
   16 missing income cases → listwise n ≈ 100, possible income multicollinearity.
5. All SPSS output → **appendix**; text references it briefly.

---

## 6. Regression analysis (QRP 4 structure: A → B → C → D)

### A. Set up the linear model
- **Dependent:** `lnY` (log of monthly spend — see §4).
- **Predictors:** `Emp2`, `Emp3` (employment dummies), `DisposableIncome`,
  `ShoppingFrequency`, `AvgPerPurchase`, `WhyShop_Avg`, `Influence_Avg`,
  `SocialMediaDiscovery`. *(Drop `MonthlyIncome` — collinear with DisposableIncome;
  `Age`/`HoursOnline` may be dropped, they are insignificant and theoretically weak —
  test both as sensitivity analysis. ~10 params / n≈100 ≈ 10 obs per parameter,
  satisfies QRP 3.)*

### B. Fit the model
`Analyze → Regression → Linear`
- **Dependent:** `lnY`  · **Independent(s):** the predictors above · **Method:** Enter
- **Statistics** button → tick: Estimates, Confidence intervals, **Model fit**,
  **R squared change**, **Collinearity diagnostics**, **Durbin-Watson**,
  Casewise diagnostics (outliers outside 3 SD)
- **Plots** button → Y = `*ZRESID`, X = `*ZPRED` (residual plot, A1/A2);
  tick **Histogram** and **Normal probability plot** (A5)
- **Save** button → Residuals: *Unstandardized* & *Studentized*; Distances: *Cook's*,
  *Leverage* (for outlier discussion)
- OK.

**Report as a TABLE (NOT a formula).** Expected ln(Y) results (verify; n ≈ 100,
R² ≈ 0.62, adj R² ≈ 0.58, F highly significant):

| Variable | B | t | p | Sig.? |
|---|---|---|---|---|
| (Constant) | +1.95 | 5.78 | <0.001 | — |
| ShoppingFrequency | **+0.42** | 6.98 | <0.001 | *** |
| AvgPerPurchase | **+0.010** | 5.28 | <0.001 | *** |
| DisposableIncome | **+0.17** | 2.88 | 0.005 | ** |
| SocialMediaDiscovery | **−0.11** | −2.04 | 0.044 | * |
| Influence_Avg | +0.12 | 1.51 | 0.13 | ns |
| WhyShop_Avg | +0.10 | 1.08 | 0.28 | ns |
| Emp2 (cat 2 vs 1) | +0.10 | 0.90 | 0.37 | ns |
| Emp3 (cat 3 vs 1) | +0.03 | 0.19 | 0.85 | ns |

**Discuss coefficients** (sign, plausible size, significance vs literature), e.g.:
*"Shopping frequency has a strong positive effect on online spend; each step up the
frequency scale raises expected monthly spend by ≈ 42%. This effect is significant
(t = 6.98, p < 0.001) and is in line with [literature], as we expected."* Do the same
for AvgPerPurchase (+) and DisposableIncome (+, supports income–consumption theory),
and note SocialMediaDiscovery is **negative and significant** — discuss whether this
was expected. State which expected effects were **not** found (employment, motivation,
influence: not significant).

### C. Goodness of fit (keep short — QRP 4)
From the **Model Summary** and **ANOVA** tables:
> *"The model explains about **62%** of the variation in (log) monthly online spend
> (R² ≈ 0.62, adjusted R² ≈ 0.58). The overall model is significant
> (F-test, p < 0.001), so the predictors jointly explain online spending well."*

### D. Check the assumptions A1–A5 (one short paragraph in text; full output in appendix)

| # | Assumption | How to check in SPSS | Expected result here |
|---|---|---|---|
| **A1** | E(ε)=0 / correct functional form | **Residual plot** `*ZRESID` vs `*ZPRED` | Cloud centred on 0, no curve → OK |
| **A2** | Var(ε)=σ² constant (homoscedastic) | Same residual plot (no funnel) **+ White's test** | No funnel; White p ≈ 0.13 (>0.05) → **no heteroscedasticity** |
| **A3** | cov(εᵢ,εⱼ)=0 (no autocorrelation) | **Durbin–Watson** in Model Summary | DW ≈ 1.36 (≈2 ideal); cross-sectional survey, no time order → acceptable, note it |
| **A4** | X not exact linear combos (no multicollinearity) | **Tolerance / VIF** (Collinearity diagnostics) | All VIF < 3 (well below 10) → OK *(this is why MonthlyIncome was dropped)* |
| **A5** | ε normally distributed (optional) | **Normal P-P / Q-Q plot** of residuals + histogram | Points on the line (ln model) → OK *(raw-Y model fails this — justifies the log)* |

**White's test in SPSS** (not a one-click menu): use
`Analyze → Regression → Linear`, click **Save → Unstandardized residuals**, then
`Transform → Compute` `res_sq = RES_1**2`; regress `res_sq` on the predictors **and**
their squares/cross-products; the test statistic is **n·R²** of that auxiliary
regression, compared to χ² (df = #regressors). Report: *"White's test does not reject
homoscedasticity (p ≈ 0.13)."* (Alternatively, SPSS 27+ offers heteroscedasticity
options under the Linear Regression *Bootstrap*/*HC* settings — the manual White test
above is what QRP 4 asks for.)

**Text paragraph template (one paragraph, per the notes):**
> *"All five assumptions were checked (full output in appendix). The residual plot shows
> a random scatter around zero with no systematic pattern, supporting A1 and constant
> variance; White's test confirms no heteroscedasticity (p ≈ 0.13, A2). The
> Durbin–Watson statistic (≈1.4) gives no strong evidence of autocorrelation, and since
> the data are cross-sectional A3 is reasonable. All VIF values are below 3, so
> multicollinearity is not a concern (A4). The normal Q-Q plot of the residuals lies
> close to the diagonal, so the normality assumption A5 holds for the log-transformed
> model. Overall the model is valid."*

If an assumption had **failed**, QRP 4 requires you to adapt the model (transform a
variable, drop a collinear predictor, handle an outlier) **or** discuss the consequences
of the violation. (You already did this: logging Y fixed A5; dropping MonthlyIncome
protected A4.)

---

## 7. Reporting checklist (from the lecturer's notes)

- [ ] Intro: 1 page, structured **to the RQ**; **RQ stated in the intro**; last paragraph
      lists the goal of each section. (Don't open with "Introduction".)
- [ ] Literature review **used**, not summarised — tie each article to the RQ/variables.
- [ ] Data section: starts with Y; own tables (no pasted SPSS); limitations.
- [ ] Regression: variables + coefficients in a **table**, significance flagged; **no
      `Y = β0+…` formula**; each effect reported with (t, p); R² short.
- [ ] Assumptions: one short paragraph (residual plot, White/heteroscedasticity, VIF,
      QQ plot); full analysis in appendix; **don't forget the White test**.
- [ ] You **state conclusions** from results (e.g. "this is a positive, significant effect").
- [ ] Conclusion: standalone, contains an **answer** to the RQ, consequences/use of
      results, limitations again, future research.
- [ ] Appendix: all univariate, bivariate and assumption output.

---

### Quick reference — recommended final model
**ln(MonthlyOnlineSpend) on** ShoppingFrequency, AvgPerPurchase, DisposableIncome,
SocialMediaDiscovery, WhyShop_Avg, Influence_Avg, Emp2, Emp3 — n ≈ 100, R² ≈ 0.62,
all five assumptions satisfied. Significant drivers: **shopping frequency (+)**,
**average spend per purchase (+)**, **disposable income (+)**, **social-media discovery (−)**.
