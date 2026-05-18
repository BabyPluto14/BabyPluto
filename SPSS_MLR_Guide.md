# Comprehensive SPSS Step-by-Step Guide: MLR on Online Shopping (Belgium)

---

## YOUR DATASET AT A GLANCE

| Role | Variable | Description | Values |
|------|----------|-------------|--------|
| **Y** | `Y_Monthly_Spend_EUR` | Monthly online spend (midpoints) | 25, 75, 125, 175, 225 |
| X – Dummy | `Emp_M_StudentWorking` | Student working (vs. student non-working = ref) | 0 / 1 |
| X – Dummy | `Emp_M_Employed` | Employed PT/FT (vs. student non-working = ref) | 0 / 1 |
| X – Ordinal | `Disposable_Income` | Income after expenses | 1(€0-499) to 4(€1500+) |
| X – Ordinal | `Shopping_Frequency` | How often shops online | 1(<1x/mo) to 5(>10x/mo) |
| X – Ordinal | `Hours_Online_Daily` | Daily hours online | 1(<2h) to 5(>10h) |
| X – Scale | `Avg_Convenience_Motive` | Avg. of 4 convenience Likert items | 1–5 |
| X – Scale | `Avg_Hedonic_Motive` | Avg. of 4 hedonic Likert items | 1–5 |
| X – Scale | `Avg_Rational_Influences` | Avg. of price/quality/reviews items | 1–5 |
| X – Scale | `Avg_Social_Influences` | Avg. of social media/ads/brand items | 1–5 |

**Filter variable**: `Include_In_Regression = 1` → gives **n = 106** (excludes 5 self-employed/unemployed/stay-at-home)

**Reference group for employment dummies**: Student non-working (n = 29)

---

## STEP 0 — SET UP & FILTER DATA

**Before anything else, apply the filter so all analyses use only the 106 valid cases.**

1. Go to **Data → Select Cases**
2. Select **"If condition is satisfied"** → click **If...**
3. Type: `Include_In_Regression = 1`
4. Click **Continue** → **OK**
5. SPSS will show diagonal lines through the excluded rows — you'll see n=106 in the output

> Keep this filter active for ALL subsequent steps.

---

## STEP 1 — UNIVARIATE DESCRIPTIVE STATISTICS

### 1A. Y Variable: `Y_Monthly_Spend_EUR`

**Expected output**: Mean ≈ €60.85, SD ≈ large (check), Min = 25, Max = 225

**Descriptive statistics + histogram:**

1. **Analyze → Descriptive Statistics → Frequencies**
2. Move `Y_Monthly_Spend_EUR` into the **Variable(s)** box
3. Click **Statistics** → check:
   - Mean, Median, Mode
   - Std. Deviation, Variance
   - Skewness, Kurtosis
   - Minimum, Maximum
4. Click **Charts** → select **Histograms** → check **"Show normal curve on histogram"**
5. Click **Continue → OK**

**What to look for:**
- Distribution shape: right-skewed? (Most responses cluster at €25–€75 = categories 1–2)
- Skewness statistic: if > +1.0, the distribution is meaningfully right-skewed → apply ln transformation (see Step 1F)

---

### 1B. Continuous/Ordinal X Variables

Run the same **Frequencies** procedure for all of these at once:

- `Disposable_Income`
- `Shopping_Frequency`
- `Hours_Online_Daily`
- `Avg_Convenience_Motive`
- `Avg_Hedonic_Motive`
- `Avg_Rational_Influences`
- `Avg_Social_Influences`

1. **Analyze → Descriptive Statistics → Frequencies**
2. Move all 7 variables into the **Variable(s)** box
3. Click **Statistics** → check Mean, SD, Min, Max, Skewness, Kurtosis
4. Click **Charts** → **Histograms** → **Show normal curve**
5. Click **Continue → OK**

**Expected patterns:**
- `Avg_Convenience_Motive` mean ≈ 3.64 — tends toward agreement (convenience matters)
- `Avg_Hedonic_Motive` mean ≈ 2.81 — more neutral/mixed
- `Avg_Rational_Influences` mean ≈ 4.18 — strong rational factors (price, quality, reviews)
- `Avg_Social_Influences` mean ≈ 2.99 — moderate social influence
- `Shopping_Frequency` mean ≈ 1.70 — most shop 1–2x/month or less
- `Disposable_Income` mean ≈ 1.76 — majority have low disposable income (€0–€999)

---

### 1C. Dummy/Binary X Variables

For `Emp_M_StudentWorking` and `Emp_M_Employed`:

1. **Analyze → Descriptive Statistics → Frequencies**
2. Move both variables into the **Variable(s)** box
3. Click **Statistics** → check **Frequencies** (the percentage table is enough for dummies)
4. Do NOT request a histogram (bar chart is more appropriate for binary)
5. Click **Charts** → **Bar charts**
6. Click **Continue → OK**

**Expected output:**
- `Emp_M_StudentWorking`: 44 coded 1 (41.5%), 62 coded 0 (58.5%)
- `Emp_M_Employed`: 33 coded 1 (31.1%), 73 coded 0 (68.9%)
- Reference group: 29 students non-working (27.4%)

---

### 1F. CHECK SKEWNESS & APPLY LN TRANSFORMATION

**Check your Y histogram and skewness statistic:**

- If **Skewness > 1.0** for `Y_Monthly_Spend_EUR` → create `LN_Y`:
  1. **Transform → Compute Variable**
  2. Target Variable: `LN_Y_Monthly_Spend`
  3. Numeric Expression: `LN(Y_Monthly_Spend_EUR)`
  4. Click **OK**
  5. Re-run the Frequencies procedure on `LN_Y_Monthly_Spend` to confirm it looks more normal

- Same logic for `Disposable_Income` if right-skewed (less likely since it only has 4 categories)

> **Note on ln for Likert averages (Avg_*):** Likert scales are bounded 1–5 so they cannot be 0. LN transformation is technically valid, but usually not needed unless strongly skewed. Check the histogram first.

---

## STEP 2 — BIVARIATE DESCRIPTIVE STATISTICS (Each X vs. Y)

### 2A. Scatterplots: Quantitative X vs. Y

For each continuous/ordinal X, create a scatterplot against Y:

1. **Graphs → Chart Builder**
2. In Gallery, select **Scatter/Dot** → drag the **Simple Scatter** thumbnail to the chart area
3. Drag `Y_Monthly_Spend_EUR` (or `LN_Y_Monthly_Spend`) to the **Y-Axis** box
4. Drag one X variable to the **X-Axis** box
5. Click **OK**
6. Repeat for each X variable

**Variables to scatterplot vs. Y:**
- `Disposable_Income` vs. Y
- `Shopping_Frequency` vs. Y
- `Hours_Online_Daily` vs. Y
- `Avg_Convenience_Motive` vs. Y
- `Avg_Hedonic_Motive` vs. Y
- `Avg_Rational_Influences` vs. Y
- `Avg_Social_Influences` vs. Y

**What to look for in each:**
- Positive or negative linear trend?
- Any nonlinearity (curved pattern)?
- Heteroscedasticity (fan shape = variance increases with X)?
- Obvious outliers?

---

### 2B. Correlation Matrix: All Quantitative Variables with Y

1. **Analyze → Correlate → Bivariate**
2. Move into the **Variables** box:
   - `Y_Monthly_Spend_EUR` (or LN version)
   - `Disposable_Income`
   - `Shopping_Frequency`
   - `Hours_Online_Daily`
   - `Avg_Convenience_Motive`
   - `Avg_Hedonic_Motive`
   - `Avg_Rational_Influences`
   - `Avg_Social_Influences`
3. Correlation Coefficients: **Pearson** (checked by default)
4. Test of Significance: **Two-tailed**
5. Check **"Flag significant correlations"**
6. Click **OK**

**What to look for:**
- Which X variables have significant correlation with Y? (p < 0.05)
- Are any X variables very highly correlated with each other? (r > 0.8 = potential multicollinearity concern)

---

### 2C. Boxplots: Dummy X Variables vs. Y

For employment dummies:

1. **Graphs → Chart Builder**
2. Select **Boxplot** → drag **Simple Boxplot** to chart area
3. Drag `Y_Monthly_Spend_EUR` to the **Y-Axis**
4. Drag `Emp_M_StudentWorking` to the **X-Axis**
5. Click **OK** → repeat for `Emp_M_Employed`

**Alternative — Means by Group:**
1. **Analyze → Compare Means → Means**
2. Dependent: `Y_Monthly_Spend_EUR`
3. Independent Layer 1: `Emp_M_StudentWorking`
4. Click **Next** → Independent Layer 2: `Emp_M_Employed`
5. Click **Options** → add Mean, N, Std. Deviation
6. Click **OK**

**What to look for:** Does mean Y differ between employed and non-employed groups?

---

### 2D. Summary Table to Include in Your Report

Build a table like this from the outputs above (do NOT copy-paste SPSS tables):

| Variable | Mean (or %) | SD | Correlation with Y (r) | p-value |
|----------|-------------|-----|------------------------|---------|
| Y_Monthly_Spend_EUR | 60.85 | — | — | — |
| Disposable_Income | 1.76 | — | r = ? | ? |
| Shopping_Frequency | 1.70 | — | r = ? | ? |
| Hours_Online_Daily | 2.46 | — | r = ? | ? |
| Avg_Convenience_Motive | 3.64 | 0.71 | r = ? | ? |
| Avg_Hedonic_Motive | 2.81 | 0.74 | r = ? | ? |
| Avg_Rational_Influences | 4.18 | 0.75 | r = ? | ? |
| Avg_Social_Influences | 2.99 | 0.72 | r = ? | ? |
| Emp_M_StudentWorking (%) | 41.5% | — | — | — |
| Emp_M_Employed (%) | 31.1% | — | — | — |

---

## STEP 3 — RUN THE MLR MODEL IN SPSS

### 3A. Navigate to Linear Regression

1. **Analyze → Regression → Linear**

### 3B. Define Variables

- **Dependent**: `Y_Monthly_Spend_EUR` (or `LN_Y_Monthly_Spend` if transformed)
- **Independent(s)** — move all of these:
  - `Emp_M_StudentWorking`
  - `Emp_M_Employed`
  - `Disposable_Income`
  - `Shopping_Frequency`
  - `Hours_Online_Daily`
  - `Avg_Convenience_Motive`
  - `Avg_Hedonic_Motive`
  - `Avg_Rational_Influences`
  - `Avg_Social_Influences`
- **Method**: **Enter** (forced entry — include all variables simultaneously)

### 3C. Click "Statistics"

Check ALL of the following:
- ✅ Estimates (regression coefficients)
- ✅ Confidence intervals (95%)
- ✅ Model fit (R², F-test)
- ✅ Descriptives
- ✅ Part and partial correlations
- ✅ **Collinearity diagnostics** ← for A4 (VIF/Tolerance)
- ✅ **Durbin-Watson** ← for A3
- Click **Continue**

### 3D. Click "Plots"

- Move `*ZRESID` to the Y-axis box
- Move `*ZPRED` to the X-axis box → this creates the **residual plot (A1 + A3)**
- Also check: ✅ **Normal probability plot** ← for A5 (Normal Q-Q plot)
- Click **Continue**

### 3E. Click "Save"

Check:
- ✅ Standardized residuals
- ✅ Cook's Distance (identifies influential observations)
- Click **Continue**

### 3F. Click OK

SPSS will produce multiple output tables. You need: **Model Summary**, **ANOVA**, **Coefficients**, **Collinearity Diagnostics**, **Residuals Statistics**, and the two plots.

---

## STEP 4 — INTERPRET RESULTS

### 4A. Model Summary Table

| Output | What it tells you |
|--------|-------------------|
| R | Multiple correlation coefficient |
| **R²** | % of variation in Y explained by all X together |
| Adjusted R² | R² corrected for number of predictors (use this for comparison) |
| F-statistic + sig. | Whether the model as a whole is significant |
| Durbin-Watson | Autocorrelation check (relevant for A3) |

**How to report (example):** *"The model explains R² = [X]% of the variance in monthly online spending (F([df1], [df2]) = [F], p < 0.001)."*

---

### 4B. Coefficients Table — Create Your Own Table

**DO NOT** write: Y = β₀ + β₁x₁ + ...

**DO** create a table like this:

| Variable | B | SE | β (Std.) | t | p | 95% CI |
|----------|---|----|----------|---|---|--------|
| Constant | | | — | | | |
| Emp_M_StudentWorking | | | | | | |
| Emp_M_Employed | | | | | | |
| Disposable_Income | | | | | | |
| Shopping_Frequency | | | | | | |
| Hours_Online_Daily | | | | | | |
| Avg_Convenience_Motive | | | | | | |
| Avg_Hedonic_Motive | | | | | | |
| Avg_Rational_Influences | | | | | | |
| Avg_Social_Influences | | | | | | |

Mark significant coefficients with * (p<0.05), ** (p<0.01), *** (p<0.001)

**How to interpret each coefficient (B):**
- Continuous/ordinal X: *"A one-unit increase in [X] is associated with a [B] euro increase/decrease in monthly spending, holding all other variables constant (t = [t], p = [p])."*
- Dummy variable: *"Students who are working spend on average [B] euros more/less per month than non-working students (t = [t], p = [p])."*
- If Y is log-transformed: multiply coefficient by 100 to interpret as approximate % change

---

### 4C. Goodness of Fit (R²)

Short section in your report. Example text:
> *"The model achieves an R² of [X]%, indicating that [X]% of the variation in monthly online spending among Belgian students and employees is explained by the nine predictors. The adjusted R² of [X]% accounts for the number of predictors included."*

---

## STEP 4.2 — ASSUMPTION CHECKS (A1–A5)

### A1: E(ε) = 0 — Residual Plot

**Output**: The ZRESID vs. ZPRED scatterplot produced automatically in Step 3D.

**What to look for:**
- Points should be randomly scattered around zero (horizontal band)
- No curved/nonlinear pattern → if there is, E(ε) ≠ 0 (systematic bias)
- No fan/funnel shape → that would indicate A2 violation (heteroscedasticity)

**How to report (briefly, full plot goes in appendix):**
> *"The residual plot shows no systematic pattern, suggesting E(ε) = 0 is satisfied."*

---

### A2: Var(ε) = σ² Constant — White's Test for Heteroscedasticity

**IMPORTANT: You MUST run White's test explicitly.**

SPSS does not have a built-in White's test button, so use this syntax approach:

**Step 1 — Get squared residuals and cross-products:**
After running the regression (Step 3), SPSS saved standardized residuals as `ZRE_1`. You need the unstandardized residuals. Go back to Step 3, click **Save** → check **Unstandardized residuals** → run again. This saves them as `RES_1`.

**Step 2 — Create squared residuals:**
1. **Transform → Compute Variable**
2. Target: `RES_SQ`
3. Expression: `RES_1 ** 2`
4. Click **OK**

**Step 3 — Create squared X variables and cross-products (for White's test):**
Create squares of each continuous X:
- `DISP_SQ` = `Disposable_Income ** 2`
- `FREQ_SQ` = `Shopping_Frequency ** 2`
- `HRS_SQ` = `Hours_Online_Daily ** 2`
- `CONV_SQ` = `Avg_Convenience_Motive ** 2`
- `HED_SQ` = `Avg_Hedonic_Motive ** 2`
- `RAT_SQ` = `Avg_Rational_Influences ** 2`
- `SOC_SQ` = `Avg_Social_Influences ** 2`

**Step 4 — Run auxiliary regression (White's test):**
1. **Analyze → Regression → Linear**
2. Dependent: `RES_SQ`
3. Independent: ALL original X variables + all squared X variables created above
4. Click **Statistics** → check **Model fit**
5. Click **OK**

**Step 5 — Calculate White's test statistic:**
- White's test statistic = **n × R²** from the auxiliary regression
- This follows a chi-square distribution with degrees of freedom = number of regressors in auxiliary regression
- Compare to chi-square critical value or check p-value

**Interpretation:**
- If p > 0.05 → **Fail to reject H0** → homoscedasticity holds ✅
- If p < 0.05 → **Reject H0** → heteroscedasticity present ❌ → discuss in your report

---

### A3: No Autocorrelation — Durbin-Watson

**Output**: In the **Model Summary** table from Step 3 (Durbin-Watson statistic).

**Interpretation:**
- Value near **2.0** → no autocorrelation ✅
- Value near 0 → positive autocorrelation
- Value near 4 → negative autocorrelation
- Acceptable range: roughly 1.5–2.5

**Note**: Cross-sectional survey data (like yours) rarely has autocorrelation. Report the value and note it is close to 2.

**How to report:**
> *"The Durbin-Watson statistic of [DW] indicates no evidence of autocorrelation in the residuals."*

Also check the **residual plot** (A1 plot) — random scatter with no wave pattern confirms A3.

---

### A4: No Multicollinearity — Tolerance & VIF

**Output**: In the **Coefficients** table, scroll right to **Collinearity Statistics** columns (Tolerance, VIF).

**Interpretation thresholds:**
| VIF value | Conclusion |
|-----------|------------|
| < 5 | No multicollinearity ✅ |
| 5–10 | Moderate concern, investigate |
| > 10 | Severe multicollinearity ❌ |

| Tolerance | Conclusion |
|-----------|------------|
| > 0.2 | No multicollinearity ✅ |
| < 0.1 | Severe multicollinearity ❌ |

**Likely concern**: `Avg_Convenience_Motive` and `Avg_Hedonic_Motive` were created from different sub-items so should be fine. Employment dummies are constructed to be non-collinear. Check anyway.

**How to report:**
> *"VIF values range from [min] to [max], all well below the threshold of 10, indicating no multicollinearity concern (Tolerance values all > 0.2)."*

---

### A5: Normality of Residuals — Normal Q-Q Plot

**Output**: The Normal P-P Plot of Regression Standardized Residuals (produced automatically in Step 3D).

**What to look for:**
- Points should fall **closely along the diagonal reference line**
- Moderate deviations at tails are acceptable with n > 100
- S-curve deviation → skewed residuals
- Heavy tails → kurtosis issue

**How to produce a Q-Q plot explicitly (if requested):**
After regression, you have unstandardized residuals `RES_1` saved:
1. **Analyze → Descriptive Statistics → Q-Q Plots**
2. Move `RES_1` to the **Variables** box
3. Test Distribution: **Normal**
4. Click **OK**

**How to report:**
> *"The normal Q-Q plot shows residuals approximately following the diagonal, suggesting the normality assumption is reasonably satisfied."*

---

## STEP 5 — FINAL REPORTING CHECKLIST

### In the main text of Section 4 (Regression Analysis):

- [ ] Describe the model (which variables included and why)
- [ ] Table: Coefficients with B, SE, β, t, p, significance stars
- [ ] Discuss each significant coefficient: direction, magnitude, theoretical expectation
- [ ] Discuss R² (goodness of fit — short paragraph)
- [ ] Brief paragraph on assumptions: *"All five classical assumptions were tested. The residual plot confirms E(ε) ≈ 0 and no autocorrelation. White's test [does/does not] reject homoscedasticity (p = [?]). VIF values confirm no multicollinearity. The Q-Q plot supports normality of residuals."*

### In the Appendix:

- [ ] Histogram of Y (and LN_Y if transformed)
- [ ] Histograms of all X variables
- [ ] Scatterplots (bivariate: each X vs. Y)
- [ ] Correlation matrix
- [ ] Residual plot (ZRESID vs. ZPRED)
- [ ] White's test auxiliary regression output
- [ ] VIF/Tolerance table
- [ ] Normal Q-Q plot of residuals

---

## QUICK REFERENCE — SPSS MENU PATHS

| Task | SPSS Path |
|------|-----------|
| Filter data | Data → Select Cases → If → `Include_In_Regression = 1` |
| Descriptive stats + histograms | Analyze → Descriptive Statistics → Frequencies |
| Correlation matrix | Analyze → Correlate → Bivariate |
| Scatterplot | Graphs → Chart Builder → Scatter/Dot |
| Boxplot by group | Graphs → Chart Builder → Boxplot |
| Means by group | Analyze → Compare Means → Means |
| Log transformation | Transform → Compute Variable → `LN(variable)` |
| Run regression | Analyze → Regression → Linear |
| Save residuals | (inside Regression dialog) → Save → Unstandardized residuals |
| Q-Q plot | Analyze → Descriptive Statistics → Q-Q Plots |
| White's test | Manually: create RES_SQ + squared X's → Analyze → Regression → Linear |
