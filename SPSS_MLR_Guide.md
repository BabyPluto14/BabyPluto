# Comprehensive SPSS Guide: Multiple Linear Regression
## Quantitative Research Project — Step-by-Step

---

### Your Data at a Glance

| Variable | Role | Type | Notes |
|---|---|---|---|
| `MonthlyOnlineSpend_Y` | **Y** | Quantitative (bin midpoints: 25/75/125/175/225) | Dependent variable |
| `Age` | X1 | Quantitative continuous (18–40) | — |
| `EmploymentLevel` | X2 | Qualitative ordinal (1, 2, 3) | **Needs dummy coding** |
| `MonthlyIncome` | X3 | Ordinal scale (1–5) | 5 missing values |
| `DisposableIncome` | X4 | Ordinal scale (1–4) | 11 missing values |
| `ShoppingFrequency` | X5 | Ordinal scale (1–5) | — |
| `AvgPerPurchase` | X6 | Quantitative (bin midpoints: 12/38/63/88/125) | — |
| `WhyShop_Avg` | X7 | Continuous average score (1–4.62) | Average of items |
| `Influence_Avg` | X8 | Continuous average score (1–4.50) | Average of items |
| `HoursOnline` | X9 | Ordinal scale (1–5) | — |
| `SocialMediaDiscovery` | X10 | Ordinal scale (1–5) | — |

**N = 111** (after listwise deletion for missing values: effectively ~100 for full model)

---

## STEP 0 — Import Data into SPSS

1. Open SPSS → **File > Open > Data** → select `Regression_data_.xlsx`
2. In the import wizard, confirm **Row 1 = variable names**
3. In **Variable View**, check that each variable has the correct measure type:
   - `MonthlyOnlineSpend_Y`, `Age`, `AvgPerPurchase`, `WhyShop_Avg`, `Influence_Avg` → **Scale**
   - `EmploymentLevel`, `MonthlyIncome`, `DisposableIncome`, `ShoppingFrequency`, `HoursOnline`, `SocialMediaDiscovery` → **Ordinal**
4. Add **value labels** where applicable (e.g., EmploymentLevel: 1=Student, 2=Part-time, 3=Full-time — based on your survey design)

---

## STEP 1 — Univariate Descriptive Statistics

> Goal: Understand each variable individually — distribution, mean, std dev, outliers, skewness, missing values.

### 1A. Quantitative / Continuous Variables
*(MonthlyOnlineSpend_Y, Age, AvgPerPurchase, WhyShop_Avg, Influence_Avg)*

**In SPSS:**
> **Analyze > Descriptive Statistics > Explore**

- Move variables into the **Dependent List**
- Click **Statistics** → check: Descriptives, Percentiles, Outliers
- Click **Plots** → check: Histogram, Normality plots with tests, Stem-and-leaf
- Click **OK**

**What to look for in the output:**
- Mean, Std. Deviation, Min, Max
- Skewness statistic: if |Skewness| > 1.0, the variable is notably skewed → consider ln() transformation
- Boxplot: flagged points (°) are mild outliers, stars (*) are extreme outliers
- Histogram shape: symmetric = good, right-skewed tail = consider ln()

**Additional histogram (manual, cleaner):**
> **Graphs > Legacy Dialogs > Histogram** → select variable → check "Display normal curve" → OK

---

### 1B. Ordinal / Categorical Variables
*(EmploymentLevel, MonthlyIncome, DisposableIncome, ShoppingFrequency, HoursOnline, SocialMediaDiscovery)*

**In SPSS:**
> **Analyze > Descriptive Statistics > Frequencies**

- Move all ordinal variables into the **Variable(s)** box
- Click **Statistics** → check: Mean, Std. deviation, Minimum, Maximum
- Click **Charts** → select **Bar charts**, Values = Frequencies → Continue
- Click **OK**

**What to look for:**
- Frequency table showing count and % for each category
- Are all categories represented? Any category < 5% (consider merging)?
- Is there enough variation across categories?

---

### 1C. Check and Handle Missing Values

> **Analyze > Descriptive Statistics > Frequencies** — look at the "Missing" row for each variable.

- `MonthlyIncome`: **5 missing** (4.5% of N=111) → acceptable to use listwise deletion
- `DisposableIncome`: **11 missing** (9.9%) → note this in your data section as a limitation
- In your paper: "Listwise deletion was applied, resulting in a working sample of N = [check in SPSS after running regression]."

---

### 1D. Check for Log Transformation Need (Skewness)

For **Y (MonthlyOnlineSpend_Y)** and **AvgPerPurchase** specifically, run:

> **Analyze > Descriptive Statistics > Descriptives** → move variable → Options → check Skewness → OK

**Decision rule:**
- Skewness between -1 and +1 → keep original variable
- Skewness > +1 (right skew) → create `LN_variable` and use that
- Skewness < -1 (left skew) → rarely transformed; discuss it

**To create a log-transformed variable:**
> **Transform > Compute Variable**
- Target Variable: `LN_MonthlyOnlineSpend_Y`
- Numeric Expression: `LN(MonthlyOnlineSpend_Y)`
- Click **OK**

Repeat for any X variable that shows strong right skew (e.g., AvgPerPurchase if needed).

> **Important:** If you transform Y, you must use the transformed version throughout the entire regression. Re-run the histogram on the transformed variable to confirm it is more symmetric.

---

## STEP 2 — Bivariate Descriptive Statistics (Each X vs Y)

> Goal: Show how each X variable is already correlated with / related to Y, before running the full model.

### 2A. Quantitative X variables vs Y
*(Age, AvgPerPurchase, WhyShop_Avg, Influence_Avg)*

**Scatterplot for each X vs Y:**
> **Graphs > Legacy Dialogs > Scatter/Dot > Simple Scatter**
- Y Axis: `MonthlyOnlineSpend_Y`
- X Axis: the X variable
- Click **OK**
- Double-click the chart → in Chart Editor: **Elements > Fit Line at Total** → select Linear → close

**What to look for:**
- Positive or negative relationship with Y?
- Is the relationship approximately linear, or curved? (if curved → consider ln() transformation)
- Is the spread around the line constant (homoscedastic) or fan-shaped (heteroscedastic → ln() transformation)?
- Any outliers that deviate strongly from the line?

**Pearson Correlation for each X vs Y:**
> **Analyze > Correlate > Bivariate**
- Move Y + all quantitative X variables into Variables box
- Method: Pearson, Two-tailed, Flag significant correlations
- Click **OK**

**Interpret:** Report r value and significance. E.g.: "Age shows a moderate positive correlation with monthly online spending (r = .XX, p < .05)."

---

### 2B. Ordinal/Categorical X variables vs Y

For **EmploymentLevel** (and other ordinal Xs treated as groups):

**Boxplot of Y per group:**
> **Graphs > Legacy Dialogs > Boxplot > Simple**
- Category Axis: `EmploymentLevel`
- Variable: `MonthlyOnlineSpend_Y`
- Click **OK**

**Means table:**
> **Analyze > Compare Means > Means**
- Dependent List: `MonthlyOnlineSpend_Y`
- Independent List: `EmploymentLevel` (and other ordinal variables)
- Options: Mean, N, Std. Deviation → Continue → OK

**What to report:** "Full-time employed respondents show a higher average monthly online spend (M = X, SD = X) compared to students (M = X, SD = X)."

---

### 2C. Dummy Coding for EmploymentLevel

Since `EmploymentLevel` has 3 categories, you need **2 dummy variables** (k-1 = 3-1 = 2):

> **Transform > Recode into Different Variables**

- Create `Emp_Dummy1` (1 = Part-time, 0 = otherwise):
  - Old Value 2 → New Value 1; All other values → 0
- Create `Emp_Dummy2` (1 = Full-time, 0 = otherwise):
  - Old Value 3 → New Value 1; All other values → 0
- Reference category (omitted): Level 1 (Student) — make this explicit in your paper.

---

## STEP 3 — Run the Multiple Linear Regression Model

### 3A. Set Up and Run the Model

> **Analyze > Regression > Linear**

- **Dependent**: `MonthlyOnlineSpend_Y` (or `LN_MonthlyOnlineSpend_Y` if transformed)
- **Independent(s)**: All X variables:
  - `Age`, `MonthlyIncome`, `DisposableIncome`, `ShoppingFrequency`, `AvgPerPurchase`, `WhyShop_Avg`, `Influence_Avg`, `HoursOnline`, `SocialMediaDiscovery`, `Emp_Dummy1`, `Emp_Dummy2`
- **Method**: Enter (forced entry — include all theoretically motivated variables)

**Click Statistics:**
- Check: Estimates, Confidence intervals, Model fit, **Collinearity diagnostics** (for VIF — A4)
- Check: **Casewise diagnostics** (outliers in residuals)
- Click Continue

**Click Plots:**
- Y-axis: `*ZRESID` (standardized residuals)
- X-axis: `*ZPRED` (standardized predicted values)
- Also check: **Histogram** of residuals and **Normal probability plot** (for A5)
- Click Continue

**Click Save:**
- Check: **Unstandardized Residuals** (saves as `RES_1`)
- Check: **Unstandardized Predicted Values** (saves as `PRE_1`)
- Click Continue → **OK**

---

### 3B. Interpret the Coefficients (Section B of MLR)

From the **Coefficients table** in the SPSS output:

**For each variable, report:**
1. The **B coefficient** (unstandardized): "A one-unit increase in X is associated with a [B] unit increase/decrease in Y, holding all other variables constant."
2. The **t-statistic and p-value**: "This effect is statistically significant (t = X.XX, p = .0XX)" or "not significant (t = X.XX, p = .XXX)"
3. The **expected sign**: Does it match your theoretical prediction from the literature?

**Key interpretations by variable type:**
- **Continuous X**: "A one-year increase in age is associated with a €[B] change in monthly online spend, ceteris paribus."
- **Ordinal X (treated as quantitative)**: "Moving one step up on the income scale is associated with a €[B] change in monthly spend."
- **Dummy variable**: "Full-time employed respondents spend on average €[B] more/less per month than students (reference category), holding all else equal."

**Create a results table in your paper (DO NOT use formula notation Y = B0 + B1X...):**

| Variable | B | Std. Error | t | p |
|---|---|---|---|---|
| (Constant) | | | | |
| Age | | | | |
| EmploymentLevel (Part-time) | | | | |
| EmploymentLevel (Full-time) | | | | |
| MonthlyIncome | | | | |
| DisposableIncome | | | | |
| ShoppingFrequency | | | | |
| AvgPerPurchase | | | | |
| WhyShop_Avg | | | | |
| Influence_Avg | | | | |
| HoursOnline | | | | |
| SocialMediaDiscovery | | | | |

*Note: * p < .05, ** p < .01, *** p < .001*

---

## STEP 4 — Goodness of Fit (Section C)

From the **Model Summary** table in SPSS output:

- **R**: Multiple correlation coefficient
- **R²**: Proportion of variance in Y explained by the model
- **Adjusted R²**: Penalizes for number of predictors (use this for interpretation with many X variables)
- **F-statistic and p-value** (from ANOVA table): Overall significance of the model

**In your paper (briefly):** "The model explains X% of the variance in monthly online spending (R² = .XX, Adjusted R² = .XX, F(df1, df2) = X.XX, p < .001)."

---

## STEP 5 — Check the Assumptions (Section D)

### A1 — Zero Mean of Residuals + Residual Plot (Linearity & Homoscedasticity check)

The residual vs. predicted plot you already generated (ZRESID vs ZPRED) serves this purpose.

**What to look for:**
- Residuals should scatter **randomly around the horizontal zero line**
- No systematic pattern (no curve, no fan shape)
- If you see a fan shape (residuals spread wider at higher fitted values) → **heteroscedasticity** → consider ln() transformation

> The mean of residuals from OLS is always exactly 0 by construction — so A1 (E(ε)=0) is automatically satisfied.

---

### A2 — Homoscedasticity: White's Test

SPSS does not have a built-in White's test — you run it manually via a regression on squared residuals.

**Step 1:** After running your main regression, SPSS has saved `RES_1`. Now create the squared residual:
> **Transform > Compute Variable**
- Target Variable: `RES_SQ`
- Expression: `RES_1 ** 2`
- OK

**Step 2:** Run White's test regression:
> **Analyze > Regression > Linear**
- Dependent: `RES_SQ`
- Independents: all original X variables + their squares + cross-products (simplified version: include all original Xs + their squares)

To create squared X terms:
> **Transform > Compute Variable**: e.g., `AGE_SQ = Age ** 2`, repeat for other continuous Xs

- Run this auxiliary regression
- Note the **R²_aux** from this regression

**Step 3:** Calculate the test statistic:
- **LM = N × R²_aux** (where N = sample size)
- Under H0 (homoscedasticity), LM ~ Chi-squared with degrees of freedom = number of regressors in auxiliary regression
- **If LM > critical chi-squared value** (or p < .05) → **reject H0 → heteroscedasticity present**

**Alternative (simpler):** Run the Breusch-Pagan / Koenker version:
> **Analyze > Regression > Linear** (same as above but just use original Xs as independents in auxiliary regression)
- This is the simplified White's test

**Reporting:** "White's test for heteroscedasticity yielded LM = X.XX (p = .XXX). As p [> / <] .05, the null hypothesis of homoscedasticity [cannot be rejected / is rejected]."

---

### A3 — No Autocorrelation

For cross-sectional survey data (which yours appears to be), autocorrelation is generally not a concern. However, if SPSS reports a **Durbin-Watson statistic**, mention it briefly.

To request it:
> In the Linear Regression dialog → **Statistics** → check **Durbin-Watson**

**Interpretation:** DW ≈ 2 = no autocorrelation; DW < 1.5 or > 2.5 = potential concern.

**For your paper:** "Given the cross-sectional nature of the data, autocorrelation (A3) is not expected to be a concern. The Durbin-Watson statistic of X.XX confirms the absence of serial correlation."

---

### A4 — No Multicollinearity: VIF

You already requested Collinearity diagnostics when setting up the regression. Find the **Coefficients table** → last two columns: **Tolerance** and **VIF**.

**Decision rules:**
- **VIF < 5**: No multicollinearity concern
- **VIF 5–10**: Moderate multicollinearity — mention it
- **VIF > 10**: Serious multicollinearity — consider removing one of the correlated predictors

**Note:** `MonthlyIncome` and `DisposableIncome` may show high VIF since they are conceptually related. If VIF is high, consider keeping only one of them.

**Reporting:** "Multicollinearity was assessed using Variance Inflation Factors (VIF). All VIF values were below [X], indicating no problematic multicollinearity (A4)."

---

### A5 — Normality of Residuals: Normal Q-Q Plot

The Q-Q plot of residuals was generated when you checked "Normal probability plot" in the Plots dialog.

**What to look for:**
- Residuals should fall **approximately along the diagonal reference line**
- S-shaped deviation = non-normality
- Heavy tails = outlier problem

**Kolmogorov-Smirnov / Shapiro-Wilk test (formal):**
> **Analyze > Descriptive Statistics > Explore**
- Dependent: `RES_1`
- Plots → check "Normality plots with tests"
- OK

**Interpretation:** If p > .05 on the Shapiro-Wilk test → normality is not rejected → A5 holds.

**Reporting:** "The normal Q-Q plot of the residuals shows points approximately following the diagonal line. The Shapiro-Wilk test confirms that residuals are [normally distributed / approximately normally distributed] (W = .XXX, p = .XXX), satisfying assumption A5."

> **Note:** With N ≈ 100, the Central Limit Theorem provides robustness to mild deviations from normality. Even if A5 is mildly violated, inference is still approximately valid.

---

## Summary Checklist

| Task | SPSS Path | Output to use |
|---|---|---|
| Univariate quant. stats | Analyze > Descriptives > Explore | Mean, SD, Skewness, Histogram, Boxplot |
| Univariate qual. stats | Analyze > Descriptives > Frequencies | Frequency table, Bar chart |
| Check skewness → ln() | Transform > Compute Variable | Compare histogram before/after |
| Bivariate: quant X vs Y | Graphs > Scatter + Analyze > Correlate > Bivariate | Scatterplot, Pearson r |
| Bivariate: qual X vs Y | Graphs > Boxplot + Analyze > Compare Means | Boxplot, means per group |
| Dummy code EmploymentLevel | Transform > Recode into Different Variables | 2 new dummy variables |
| Run MLR | Analyze > Regression > Linear | Full output table |
| Coefficients + significance | Coefficients table (SPSS output) | B, t, p |
| Goodness of fit | Model Summary + ANOVA table | R², Adj. R², F-test |
| A1: Residual plot | ZRESID vs ZPRED plot | Random scatter around 0 |
| A2: White's test | Manual auxiliary regression on RES_SQ | LM statistic (N × R²_aux) |
| A3: Durbin-Watson | Statistics > Durbin-Watson | DW ≈ 2 |
| A4: VIF | Statistics > Collinearity diagnostics | VIF < 5 |
| A5: Normal Q-Q plot | Plots > Normal probability plot + Explore on RES_1 | Q-Q plot + Shapiro-Wilk |

---

## Reporting Structure in Your Paper

**Data Section (Section 3):**
1. Start by describing **Y** (MonthlyOnlineSpend_Y): what it measures, how it is operationalized, descriptive stats
2. Describe each **X variable** in turn: definition, scale, source, univariate stats
3. Present a **summary descriptive statistics table** (your own — do not paste SPSS output)
4. Summarize bivariate relationships: which Xs appear positively/negatively related to Y
5. Note missing values and how handled; note any transformations applied

**Regression Section (Section 4):**
1. **A — Model setup**: Justify variable inclusion based on literature (expected signs)
2. **B — Coefficients**: Table of results; discuss each significant coefficient; link back to lit
3. **C — Goodness of fit**: One paragraph: R², Adjusted R², F-test significance
4. **D — Assumptions**: One paragraph summarizing A1–A5; full plots in appendix

**Common mistakes to avoid:**
- Do NOT write the model as a formula: Y = B0 + B1X1 + ...
- Do NOT paste SPSS output tables directly — create your own tables
- DO indicate significance with * symbols in your table
- DO discuss the sign and size of each significant coefficient (not just list them)
- DO include White's test for heteroscedasticity (it is explicitly required)
- DO put full assumption plots in the appendix; only briefly discuss in main text
