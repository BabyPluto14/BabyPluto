# Appendix Checklist — Online Shopping in Belgium
Based on Group15 example paper structure, adapted to your project variables.

---

## APPENDIX A: Univariate and Bivariate Statistics

The example paper includes, for EVERY variable (Y and each X):
1. Frequency table (for categorical variables) OR histogram (for continuous variables)
2. Bar chart (for categorical) OR histogram with normal curve (for continuous)
3. Descriptives table (from SPSS Explore: mean, SD, skewness, kurtosis, min, max)
4. Bivariate output vs. ln_Y2:
   - Continuous IVs → Pearson correlation + scatterplot
   - Categorical/dummy IVs → t-test (Group Statistics + Independent Samples Test) + boxplot

---

### Y: Dependent Variable

| Item | What to screenshot/paste | Where in SPSS output |
|------|--------------------------|----------------------|
| Y2 histogram (original) | Histogram of raw Y2_Monthly_Spend_EUR | Explore or Frequencies |
| ln_Y2 histogram | Histogram of ln_Y2_Monthly_Spend_EUR | Explore |
| ln_Y2 descriptives | Descriptives table (mean, SD, skewness etc.) | Explore |

---

### X1: ln_Shopping_Frequency (continuous)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Histogram | Histogram of ln_Shopping_Frequency | Explore |
| Descriptives table | Mean, SD, skewness, kurtosis | Explore |
| Scatterplot vs. ln_Y2 | Scatterplot (X = ln_ShopFreq, Y = ln_Y2) | Graphs → Chart Builder |
| Pearson correlation | Correlation table row for this variable | Correlations |

---

### X2: Y1_Per_Purchase_EUR (continuous)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Histogram | Histogram of Y1_Per_Purchase_EUR | Explore |
| Descriptives table | Mean, SD, skewness, kurtosis | Explore |
| Scatterplot vs. ln_Y2 | Scatterplot | Graphs |
| Pearson correlation | Correlation table row | Correlations |

---

### X3: Disposable_Income (continuous)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Histogram | Histogram of Disposable_Income | Explore |
| Descriptives table | Mean, SD, skewness, kurtosis | Explore |
| Scatterplot vs. ln_Y2 | Scatterplot | Graphs |
| Pearson correlation | Correlation table row | Correlations |

---

### X4: Hours_Online_Per_Week (continuous)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Histogram | Histogram | Explore |
| Descriptives table | Mean, SD, skewness, kurtosis | Explore |
| Scatterplot vs. ln_Y2 | Scatterplot | Graphs |
| Pearson correlation | Correlation table row | Correlations |

---

### X5–X8: Composite Sub-Scales (4 scales)

For each: Avg_Convenience_Motive, Avg_Hedonic_Motive, Avg_Rational_Influences, Avg_Social_Influences

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Histogram | Histogram | Explore |
| Descriptives table | Mean, SD, skewness, kurtosis | Explore |
| Scatterplot vs. ln_Y2 | Scatterplot | Graphs |
| Pearson correlation | Correlation table row | Correlations |
| Reliability output | Cronbach's alpha (for each scale) | Analyze → Scale → Reliability |

---

### X9: Employment (categorical dummy)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Frequency table | Table showing Non-working student / Student+worker / Employed counts | Frequencies |
| Bar chart | Bar chart of Employment_Code | Frequencies → Charts |
| Boxplot (Employment vs. ln_Y2) | Boxplot of ln_Y2 grouped by employment | Explore (by group) |
| T-test: Student+Worker vs. ref | Group Statistics + Independent Samples Test | Analyze → Compare Means → T-Test |
| T-test: Employed vs. ref | Group Statistics + Independent Samples Test | Same as above |

---

### X10–X11: Product Category Dummies (2 significant ones)

For Cat_Home_Items AND Cat_Beauty_Personal_Care:

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Frequency table | Count of 0 vs. 1 for each category | Frequencies |
| T-test output | Group Statistics + Independent Samples Test | T-Test |

---

## APPENDIX B: Regression Model Run

These all come from the same regression output block in SPSS.

| Item | What to screenshot/paste | Where in SPSS output |
|------|--------------------------|----------------------|
| Variables Entered table | Lists all 12 predictors entered (Enter method) | Regression output |
| Model Summary | R = .796, R² = .634, Adj R² = .581, Std. Error | Regression output |
| ANOVA table | F(12, 83) = 11.984, p < .001 | Regression output |
| Coefficients table | B, SE, Beta, t, Sig. for all 12 predictors + constant | Regression output |

---

## APPENDIX C: Reliability Statistics (Cronbach's Alpha)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Reliability: Avg_Convenience_Motive | Full Reliability output (α = .674, N of items) | Analyze → Scale → Reliability |
| Reliability: Avg_Hedonic_Motive | Full Reliability output (α = .526) | Same |
| Reliability: Avg_Rational_Influences | Full Reliability output (α = .662) | Same |
| Reliability: Avg_Social_Influences | Full Reliability output (α = .654) | Same |

---

## APPENDIX D: Assumption 1 (Zero Mean Residuals) & Assumption 2 (Homoscedasticity)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Residuals Statistics table | Min, Max, Mean (.000), SD for Residual and Predicted | Regression output → Residuals Statistics |
| Residual scatterplot | ZRESID vs. ZPRED plot (banded diagonal pattern visible) | Regression output → Scatterplot |
| White's test: Model Summary | R², F, Sig. of auxiliary regression | Separate regression: RES_SQ on PRE_1 + PRED_SQ |
| White's test: ANOVA | F = 2.272, p = .109 → homoscedasticity confirmed | Same auxiliary regression |

---

## APPENDIX E: Assumption 3 (No Autocorrelation)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Model Summary with Durbin-Watson | DW = 1.425 — shown in Model Summary table | Regression output (only appears if DW was ticked in Statistics) |

Note: If Durbin-Watson does not appear in your output, re-run the regression with Statistics → Durbin-Watson ticked.

---

## APPENDIX F: Assumption 4 (No Multicollinearity)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Full Coefficients table with VIF | Same Coefficients table but showing Collinearity Statistics columns (Tolerance + VIF) | Regression output |

Max VIF = 2.237 (ln_Shopping_Frequency) — all well below threshold of 5-10.

---

## APPENDIX G: Assumption 5 (Normality of Residuals)

| Item | What to screenshot/paste | Where |
|------|--------------------------|-------|
| Normal P-P Plot | "Normal P-P Plot of Regression Standardized Residual" | Regression output → Plots |
| Histogram of standardized residuals | Histogram with normal curve overlay | Regression output → Plots |

---

## FULL APPENDIX ORDER (suggested)

```
Appendix A  — Univariate and Bivariate Statistics
  Y: ln_Y2_Monthly_Spend_EUR
  X1: ln_Shopping_Frequency
  X2: Y1_Per_Purchase_EUR
  X3: Disposable_Income
  X4: Hours_Online_Per_Week
  X5: Avg_Convenience_Motive
  X6: Avg_Hedonic_Motive
  X7: Avg_Rational_Influences
  X8: Avg_Social_Influences
  X9: Employment (frequency + bar chart + boxplot + t-tests)
  X10: Cat_Home_Items (t-test)
  X11: Cat_Beauty_Personal_Care (t-test)

Appendix B  — Regression Model Run
  Variables Entered / Model Summary / ANOVA / Coefficients

Appendix C  — Reliability Statistics (Cronbach's Alpha for 4 scales)

Appendix D  — Assumption 1 & 2 (Residuals Statistics + Residual plot + White's test)

Appendix E  — Assumption 3 (Durbin-Watson from Model Summary)

Appendix F  — Assumption 4 (Coefficients table with VIF / Collinearity Statistics)

Appendix G  — Assumption 5 (Histogram + Normal P-P Plot of residuals)
```

---

## KEY DIFFERENCES vs. Example Paper

| Example paper (Group15) | Your project |
|------------------------|--------------|
| Used ANOVA + Tukey HSD for multi-category IVs | You use independent samples t-tests for dummy IVs (0/1 only) |
| No log transformation needed | Y2 and Shopping_Frequency were log-transformed — show BOTH original and transformed histograms |
| 9 predictors, all dummy-coded | Mix of continuous, composite scales, dummies — show all types |
| No reliability analysis (no composite scales) | 4 composite sub-scales need Cronbach's alpha appendix |
| Residual plot showed banded pattern too (same issue) | Note in text that banding is due to discrete Y2 measurement, not model failure |
