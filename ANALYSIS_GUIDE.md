# Online Shopping Belgium — Complete Analysis Guide
*Updated with actual data results — due 20 May 23:59*

---

## One-page quick reference: what changed vs the previous session

| Topic | Previous session (predicted) | Actual (verified on data) |
|---|---|---|
| VIF for influence variables | ~2–3 | 6.1 & 5.8 → PROBLEM |
| Fix | Use `Avg_PurchaseInfluences` + `Avg_Social_Influences` | Replace with **`Avg_Rational_Influences`** + `Avg_Social_Influences` |
| `SocialMediaDiscovery` effect | Negative, significant (−0.11, p=0.044) | Positive, just significant (+0.14, p=0.049) |
| Employment in data | 3 categories (1/2/3) | 7 codes; 3 collapsed → Student / Student+Working / Employed |
| Effective n | ~100 | **96** (10 missing Disposable_Income) |
| lnY in SPSS file | Not included | **Now included** — open the xlsx directly |

---

## Variable dictionary (what to call each variable in your report)

| Variable in file | Name in report | Type | Measure in SPSS |
|---|---|---|---|
| `Y2_Monthly_Spend_EUR` | Monthly online spend (Y) | Scale | midpoint-coded EUR |
| `lnY` | ln(monthly online spend) | Scale | natural log of Y |
| `Y1_Per_Purchase_EUR` | Average spend per purchase (EUR) | Scale | midpoint-coded EUR |
| `Disposable_Income` | Disposable income | Ordinal (treat as scale) | 4-category ordinal |
| `Monthly_Income` | Monthly income | Ordinal | 5-category ordinal — NOT in model |
| `Shopping_Frequency` | Shopping frequency | Ordinal (treat as scale) | 5-category ordinal |
| `Hours_Online_Daily` | Daily hours online | Ordinal (treat as scale) | 5-category ordinal |
| `Avg_WhyShopOnline` | Shopping motives (avg) | Scale | mean of 8 items (1–5) |
| `Avg_Rational_Influences` | Rational purchase influences | Scale | mean of Price, Quality, Reviews |
| `Avg_Social_Influences` | Social purchase influences | Scale | mean of SocialMedia, Ads, Recommendations |
| `Emp_M_StudentWorking` | Student+working dummy (Emp2) | Nominal | 1 = student+working, 0 = other |
| `Emp_M_Employed` | Employed dummy (Emp3) | Nominal | 1 = employed, 0 = other |
| `Include_In_Regression` | — | — | Use as filter (=1): removes 5 edge cases |

**Reference category for employment:** *Student only* (Emp_M_StudentWorking=0, Emp_M_Employed=0), n=29

---

## Phase 0 — The four design decisions (recap)

1. **Log-transform Y.** Y is right-skewed (+1.33 in regression subset). lnY skew = +0.37. Logging fixes normality of residuals (A5: Shapiro p=0.17 ✓) and gives coefficients a "% change" interpretation.
2. **Employment → 2 dummies.** Employment code is nominal (not a quantity). Reference = student only. Emp2 = student+working. Emp3 = employed.
3. **Drop Monthly_Income, keep Disposable_Income.** Both measure income; correlation is high. Disposable income is more theoretically relevant for discretionary spending.
4. **Do NOT log Avg_PurchaseInfluences or Avg_Social_Influences.** Left-skewed (−1.55, −0.68). Logging left-skewed data makes it worse. Leave raw.
5. **NEW: Use Avg_Rational_Influences + Avg_Social_Influences, NOT Avg_PurchaseInfluences.** Avg_PurchaseInfluences is the average of all 8 influence items. Avg_Social_Influences is a 3-item subset of those same 8 items → correlation = 0.90 → VIF > 6 if both included. Splitting into rational and social sub-scales drops all VIF below 2.2.

---

## Phase 1 — Univariate descriptive statistics

### SPSS steps
1. Analyze → Descriptive Statistics → Frequencies
2. Add: `lnY, Y1_Per_Purchase_EUR, Disposable_Income, Shopping_Frequency, Hours_Online_Daily, Avg_WhyShopOnline, Avg_Rational_Influences, Avg_Social_Influences`
3. Statistics tab: Mean, Std deviation, Minimum, Maximum, Skewness
4. Charts tab: Histogram + Show normal curve; untick "Display frequency tables"
5. For Y: also run Analyze → Descriptive Statistics → Explore → Boxplot to check outliers

For employment: Analyze → Descriptive Statistics → Frequencies → `Employment_Code` → tick Display frequency tables → Charts → Bar chart.

### Table to put in your report text (build it yourself — do not paste SPSS output)

**Table 1. Univariate descriptive statistics — regression subset (n=96–106)**

| Variable | n | Mean | SD | Min | Max | Skewness |
|---|---|---|---|---|---|---|
| Monthly online spend — Y (EUR) | 106 | 60.85 | 44.59 | 25.00 | 225.00 | +1.33 |
| ln(Monthly online spend) | 106 | 3.87 | 0.69 | 3.22 | 5.42 | +0.37 |
| Avg spend per purchase (EUR) | 106 | 43.29 | 25.18 | 12.50 | 125.00 | +0.80 |
| Disposable income (1–4) | 96 | 1.76 | 1.06 | 1.00 | 4.00 | +1.09 |
| Shopping frequency (1–5) | 106 | 1.70 | 0.81 | 1.00 | 5.00 | +1.16 |
| Daily hours online (1–5) | 106 | 2.46 | 1.05 | 1.00 | 5.00 | +0.48 |
| Shopping motives avg (1–5) | 106 | 3.23 | 0.62 | 1.00 | 4.62 | −0.59 |
| Rational influences avg (1–5) | 106 | 3.58 | 0.80 | 1.00 | 5.00 | −0.75 |
| Social influences avg (1–5) | 106 | 2.99 | 0.72 | 1.00 | 4.20 | −0.68 |

**Table 2. Employment group frequencies**

| Group | n | % |
|---|---|---|
| Student only (reference) | 29 | 27.4 |
| Student + working | 44 | 41.5 |
| Employed | 33 | 31.1 |
| **Total** | **106** | **100.0** |

### Text paragraph template
> Monthly online spend (Y) ranges from €25 to €225, with a mean of €60.85 (SD=44.59). The distribution is right-skewed (+1.33), which violates the normality assumption for residuals; a natural log transformation reduces the skewness to +0.37 and is used throughout the regression analysis. Shopping frequency and disposable income are also right-skewed but are retained in raw form as mild skewness does not compromise the regression assumptions at this scale. Shopping motives and social influences are slightly left-skewed and are similarly kept raw. The sample is predominantly student-affiliated: 27.4% are students only, 41.5% are student-working, and 31.1% are employed. Ten respondents did not report disposable income, reducing the effective regression sample to n=96 (see Section 3 for limitations).

---

## Phase 2 — Bivariate descriptive statistics

### SPSS steps
- **Correlations:** Analyze → Correlate → Bivariate → add Y + all scale/ordinal X → Pearson → Flag significant at 0.05
- **Scatterplots:** Graphs → Chart Builder → Simple Scatter (Y-axis = lnY, X-axis = each X with r>0.3) → Add Fit Line
- **Employment vs Y:** Analyze → Compare Means → Means → Dependent: `Y2_Monthly_Spend_EUR`, Layer: `Employment_Code`

### Correlation results (verified on actual data)

**Table 3. Pearson correlations with lnY (n varies 96–106)**

| Variable | r with lnY | p | Interpretation |
|---|---|---|---|
| Shopping frequency | +0.599 | <0.001 | Strong positive |
| Avg spend per purchase | +0.486 | <0.001 | Moderate positive |
| Disposable income | +0.404 | <0.001 | Moderate positive |
| Monthly income | +0.313 | 0.001 | Weak positive |
| Shopping motives avg | +0.207 | 0.033 | Weak positive |
| Social influences avg | +0.053 | 0.591 | None |
| Rational influences avg | −0.119 | 0.224 | None |
| Daily hours online | −0.083 | 0.400 | None |

**Employment group means (Y, raw EUR):**
- Student only: €45.69
- Student + working: €61.36
- Employed: €73.48
→ Mean spend rises monotonically with employment level, as expected from theory.

### Text paragraph template
> Shopping frequency shows the strongest bivariate association with log monthly spend (r=+0.60, p<0.001), followed by average spend per purchase (r=+0.49, p<0.001) and disposable income (r=+0.40, p<0.001). Shopping motives are weakly positively correlated (r=+0.21, p=0.033). The remaining variables — social and rational influences, and daily hours online — show no significant linear relationship with lnY at the bivariate level. Regarding employment, mean monthly spend increases from €45.69 (students) to €61.36 (student+working) to €73.48 (employed), suggesting that income-earning status is associated with higher spending.

---

## Phase 3 — Log transformation (already done)

`lnY` is now in the SPSS file. In SPSS, after loading the xlsx, you do **not** need to run Transform → Compute for lnY — it is already there.

If you want to verify in SPSS: Analyze → Descriptive Statistics → Frequencies → `lnY` → Statistics: Skewness → expect +0.37.

---

## Phase 4 — Data section (writing guide)

Write in this order:

**1. Start with Y (required by notes)**
Explain what monthly online spend measures (total EUR spent on online shopping per month), how it is coded (respondents selected a spending range; midpoint values used: €25, €75, €125, €175, €225), and why it is a valid continuous outcome. Note the right-skewed distribution and the log transformation.

**2. Summarise univariate findings (one paragraph + Table 1 + Table 2)**
Refer readers to the full SPSS output in the appendix.

**3. Summarise bivariate findings (one paragraph + Table 3)**
Highlight the three strong predictors. Note that employment group means suggest a positive gradient. Refer to appendix for scatterplots and boxplots.

**4. Variable-by-variable description (briefly, in a list or short paragraphs)**
For each predictor, state: what it measures, how it is coded/scaled, and the expected theoretical direction of effect on Y (tie to your literature review).

**5. Limitations**
- Convenience sample; predominantly students → narrow age range, potentially not representative of the Belgian adult population.
- Spend variable is bin-coded → midpoint approximation, not exact EUR amount.
- Disposable income: 10 missing values → listwise deletion reduces regression n from 106 to 96.
- Monthly income excluded due to high correlation with Disposable Income (multicollinearity; see Section 4).

---

## Phase 5 — Regression analysis

### Primary model

**Dependent variable:** lnY = ln(Monthly online spend)

**Predictors:** Avg per purchase, Shopping frequency, Disposable income, Shopping motives avg, Rational influences avg, Social influences avg, Student+working dummy, Employed dummy

### SPSS steps
1. Analyze → Regression → Linear
2. Dependent: `lnY`
3. Independents: `Y1_Per_Purchase_EUR`, `Shopping_Frequency`, `Disposable_Income`, `Avg_WhyShopOnline`, `Avg_Rational_Influences`, `Avg_Social_Influences`, `Emp_M_StudentWorking`, `Emp_M_Employed`
4. Method: Enter
5. **Statistics:** Estimates, Confidence intervals, Model fit, R² change, Collinearity diagnostics, Durbin-Watson, Casewise diagnostics
6. **Plots:** Y=`*ZRESID`, X=`*ZPRED` → tick Histogram + Normal probability plot
7. **Save:** Unstandardized residuals, Studentized residuals, Cook's distance, Leverage

### Table 4. Regression results — include this in the text (NOT the raw SPSS output)

**Table 4. OLS regression: determinants of ln(monthly online spend), n=96**

| Variable | B | SE | t | p | Significance |
|---|---|---|---|---|---|
| Constant | 2.090 | 0.359 | 5.83 | <0.001 | *** |
| Avg spend per purchase (EUR) | 0.011 | 0.002 | 5.77 | <0.001 | *** |
| Shopping frequency | 0.422 | 0.062 | 6.81 | <0.001 | *** |
| Disposable income | 0.138 | 0.057 | 2.43 | 0.017 | * |
| Shopping motives avg | 0.033 | 0.091 | 0.37 | 0.715 | — |
| Rational influences avg | −0.071 | 0.067 | −1.05 | 0.295 | — |
| Social influences avg | 0.143 | 0.072 | 1.99 | 0.049 | * |
| Student+working (vs student) | 0.134 | 0.119 | 1.13 | 0.262 | — |
| Employed (vs student) | 0.126 | 0.141 | 0.89 | 0.377 | — |

*Note: *** p<0.001, * p<0.05, — not significant. R²=0.608, Adjusted R²=0.572, F(8,87)=16.88, p<0.001.*

### How to discuss each coefficient (write one sentence each)

**Avg spend per purchase:** Each additional €1 in average spend per purchase is associated with a 1.1% increase in expected monthly spend (B=0.011, t=5.77, p<0.001). This effect is highly significant and consistent with [your lit review on basket size / spending habits].

**Shopping frequency:** Each step up the frequency scale is associated with a 42.2% increase in expected monthly spend (B=0.422, t=6.81, p<0.001). This is the strongest driver and aligns with [your lit review on purchase frequency].

**Disposable income:** Each income category higher is associated with a 13.8% increase in expected monthly spend (B=0.138, t=2.43, p=0.017). This positive and significant effect confirms that discretionary income drives online spending [cite lit review].

**Social influences avg:** Higher perceived influence of social media, online advertising, and peer recommendations is associated with a 14.3% higher expected spend (B=0.143, t=1.99, p=0.049). The effect is marginally significant, suggesting a weak but present social/marketing channel effect.

**Shopping motives, rational influences, employment dummies:** None are statistically significant (all p>0.25). This means that after controlling for actual spending behaviour (frequency, basket size) and income, the *reasons* for shopping online and employment status do not independently explain variation in monthly spend. Mention whether this is surprising relative to your literature review.

### Section C — Goodness of fit (keep to 2–3 sentences)

> The model explains 60.8% of the variance in log monthly online spending (R²=0.608). After adjusting for the number of predictors, the model retains substantial explanatory power (Adjusted R²=0.572). The overall model is highly significant (F(8,87)=16.88, p<0.001).

### Section D — Assumptions A1–A5

#### Table 5. Assumption checks (put this in your text; full output in appendix)

| # | Assumption | Test | Result | Verdict |
|---|---|---|---|---|
| A1 | E(ε)=0, linear form | Standardised residual plot (*ZRESID vs *ZPRED) | Random scatter around zero; no curve | ✓ |
| A2 | Homoscedasticity | White's test | χ²=42.06, p=0.425 | ✓ |
| A3 | No autocorrelation | Durbin-Watson | DW=1.42; cross-sectional data | ✓ acceptable |
| A4 | No multicollinearity | VIF | All VIF<2.2 (max=2.16) | ✓ |
| A5 | Normal residuals | Shapiro-Wilk + Q-Q plot | W=0.981, p=0.170 | ✓ |

**White's test in SPSS** (no menu button — do it manually):
1. After regression, go to Save → untick/save Unstandardized Residuals (RES_1 appears in data)
2. Transform → Compute → `res_sq = RES_1 ** 2`
3. Analyze → Regression → Linear: Dependent=`res_sq`, Independents = all original predictors + their squares + cross-products
4. Note n × R² of that auxiliary regression → compare to χ²(df = number of regressors in auxiliary). Here: n=96, R²≈0.438, statistic≈42.1, df≈36, p≈0.43 → do not reject homoscedasticity.

**One-paragraph template for text:**
> All five OLS assumptions were verified (full output in appendix). The standardised residual plot shows random scatter around zero with no discernible pattern or funnel shape (A1, A2). White's test confirms homoscedasticity (χ²=42.06, p=0.425, A2). Durbin-Watson equals 1.42; as the data are a cross-sectional survey, no temporal autocorrelation is expected (A3). All VIF values are below 2.2, confirming the absence of multicollinearity (A4); note that Monthly Income was excluded precisely to keep VIF low, as it is highly correlated with Disposable Income. The Shapiro-Wilk test on standardised residuals yields p=0.170, and the normal Q-Q plot aligns closely with the diagonal, confirming residual normality (A5). The log transformation of Y was necessary to satisfy A5 — residuals from the raw Y model are non-normal (Shapiro p<0.05). The model assumptions hold.

### Sensitivity check (robustness)

Run the same model without `Y1_Per_Purchase_EUR`. Results (n=96):

| Variable | B | t | p | Sig |
|---|---|---|---|---|
| Constant | 2.497 | 6.07 | <0.001 | *** |
| Shopping frequency | 0.390 | 5.40 | <0.001 | *** |
| Disposable income | 0.182 | 2.77 | 0.007 | ** |
| Shopping motives avg | 0.129 | 1.23 | 0.221 | — |
| Rational influences avg | −0.123 | −1.58 | 0.117 | — |
| Social influences avg | 0.114 | 1.37 | 0.175 | — |
| Student+working | 0.221 | 1.61 | 0.112 | — |
| Employed | 0.166 | 1.01 | 0.316 | — |

R²=0.459, Adj R²=0.415. R² drops by 0.150 when average spend per purchase is removed.

**What to write:** "As a robustness check, the model was re-estimated without average spend per purchase, since this variable reflects individual transaction size and could be considered partially mechanical relative to total monthly spend. Shopping frequency and disposable income remain significant and positive in both specifications (Table 5 vs Table 4), confirming the core findings are not driven by the inclusion of this variable. The R² reduction of 15 percentage points confirms that average basket size is a substantive predictor but not the only one."

---

## SPSS variable setup checklist (open Online_Shopping_Belgium_SPSS.xlsx)

In Variable View, set Measure column as follows:

| Variable | Measure | Role |
|---|---|---|
| `Y2_Monthly_Spend_EUR` | Scale | Dependent |
| `lnY` | Scale | Dependent (use this in regression) |
| `Y1_Per_Purchase_EUR` | Scale | Independent |
| `Disposable_Income` | Scale | Independent |
| `Shopping_Frequency` | Scale | Independent |
| `Hours_Online_Daily` | Scale | Independent |
| `Avg_WhyShopOnline` | Scale | Independent |
| `Avg_Rational_Influences` | Scale | Independent |
| `Avg_Social_Influences` | Scale | Independent |
| `Emp_M_StudentWorking` | Nominal | Independent (dummy) |
| `Emp_M_Employed` | Nominal | Independent (dummy) |
| `Employment_Code` | Nominal | For frequency table only |
| `Include_In_Regression` | Nominal | Use as Select Cases filter |

**Apply filter:** Data → Select Cases → `Include_In_Regression = 1` → keep this ON for all analyses (removes 5 edge cases).

---

## Common mistakes to avoid (from your notes)

- Do NOT write Y = β₀ + β₁x₁ + ... in the text. Present coefficients in Table 4 only.
- Do NOT paste SPSS output tables into the report. Build your own tables (Tables 1–5 above are ready to use).
- Make sure every variable has a unit/measurement description.
- Include the Research Question in the introduction AND the conclusion must answer it.
- The conclusion must be self-contained (readable without the rest of the paper).
- Explicitly state the log transformation and the reason (right-skewed Y → needed for A5).
- Employment dummies: explain that the reference category is "student only" and that "employed" means employed or self-employed (not in education).
- Note the 10 missing values in Disposable Income and the resulting n=96 for the regression.
