from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# ── Document setup ──────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    "/home/user/BabyPluto/MLR_TimeSeries_ExamGuide.pdf",
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm,
)

W = A4[0] - 4*cm   # usable width

# ── Colour palette ───────────────────────────────────────────────────────────
DARK_BLUE   = colors.HexColor("#1B3A6B")
MID_BLUE    = colors.HexColor("#2E6DA4")
LIGHT_BLUE  = colors.HexColor("#D6E8F7")
ORANGE      = colors.HexColor("#D4500A")
GREEN       = colors.HexColor("#1A6B3A")
LIGHT_GREEN = colors.HexColor("#D6F0E0")
YELLOW_BG   = colors.HexColor("#FFF8DC")
RED_BG      = colors.HexColor("#FDE8E8")
GREY_LINE   = colors.HexColor("#CCCCCC")
WHITE       = colors.white
BLACK       = colors.black

# ── Styles ───────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = S("Title",
    fontSize=22, textColor=WHITE, fontName="Helvetica-Bold",
    alignment=TA_CENTER, spaceAfter=6, leading=28)

subtitle_style = S("Subtitle",
    fontSize=12, textColor=LIGHT_BLUE, fontName="Helvetica",
    alignment=TA_CENTER, spaceAfter=4)

part_style = S("Part",
    fontSize=16, textColor=WHITE, fontName="Helvetica-Bold",
    alignment=TA_LEFT, spaceAfter=4, leading=20)

h1 = S("H1",
    fontSize=13, textColor=DARK_BLUE, fontName="Helvetica-Bold",
    spaceBefore=14, spaceAfter=4, leading=16)

h2 = S("H2",
    fontSize=11, textColor=MID_BLUE, fontName="Helvetica-Bold",
    spaceBefore=10, spaceAfter=3, leading=14)

h3 = S("H3",
    fontSize=10, textColor=ORANGE, fontName="Helvetica-Bold",
    spaceBefore=8, spaceAfter=2, leading=13)

body = S("Body",
    fontSize=9.5, textColor=BLACK, fontName="Helvetica",
    spaceBefore=2, spaceAfter=3, leading=14, alignment=TA_JUSTIFY)

bullet = S("Bullet",
    fontSize=9.5, textColor=BLACK, fontName="Helvetica",
    spaceBefore=1, spaceAfter=1, leading=13,
    leftIndent=14, firstLineIndent=-10)

code_style = S("Code",
    fontSize=8.5, textColor=colors.HexColor("#2B2B2B"),
    fontName="Courier", spaceBefore=2, spaceAfter=2,
    leading=12, leftIndent=10)

warn_style = S("Warn",
    fontSize=9.5, textColor=colors.HexColor("#7B0000"),
    fontName="Helvetica", spaceBefore=2, spaceAfter=2,
    leading=13, leftIndent=10, alignment=TA_JUSTIFY)

tip_style = S("Tip",
    fontSize=9.5, textColor=GREEN,
    fontName="Helvetica", spaceBefore=2, spaceAfter=2,
    leading=13, leftIndent=10, alignment=TA_JUSTIFY)

# ── Helper builders ──────────────────────────────────────────────────────────
def hr(): return HRFlowable(width="100%", thickness=0.5, color=GREY_LINE, spaceAfter=4)

def sp(h=6): return Spacer(1, h)

def banner(text, bg=DARK_BLUE, style=part_style):
    t = Table([[Paragraph(text, style)]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("RIGHTPADDING",  (0,0), (-1,-1), 12),
    ]))
    return t

def info_box(rows, bg=LIGHT_BLUE, label=None):
    """Coloured box with bullet rows."""
    content = []
    if label:
        content.append(Paragraph(f"<b>{label}</b>", h2))
    for r in rows:
        content.append(Paragraph(f"• {r}", body))
    t = Table([[content]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("BOX",           (0,0), (-1,-1), 0.5, GREY_LINE),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ]))
    return t

def pitfall_box(rows):
    return info_box(rows, bg=RED_BG, label="⚠  Common Pitfalls")

def tip_box(rows):
    return info_box(rows, bg=LIGHT_GREEN, label="✓  Exam Tips")

def formula_box(lines):
    content = [Paragraph(l, code_style) for l in lines]
    t = Table([content] if len(content)==1 else [[c] for c in content],
              colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), YELLOW_BG),
        ("BOX",           (0,0), (-1,-1), 1, MID_BLUE),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
    ]))
    return t

def two_col(left_items, right_items, heads=("",""), ratios=(0.5,0.5)):
    lw = W * ratios[0] - 4
    rw = W * ratios[1] - 4
    def mk(items, head):
        cell = []
        if head:
            cell.append(Paragraph(f"<b>{head}</b>", h3))
        for i in items:
            cell.append(Paragraph(f"• {i}", body))
        return cell
    row = [mk(left_items, heads[0]), mk(right_items, heads[1])]
    t = Table([row], colWidths=[lw+4, rw+4])
    t.setStyle(TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("LINEAFTER",     (0,0), (0,-1), 0.5, GREY_LINE),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    return t

def simple_table(header, rows, col_widths=None):
    if col_widths is None:
        col_widths = [W / len(header)] * len(header)
    data = [[Paragraph(f"<b>{h}</b>", S("th", fontSize=9, fontName="Helvetica-Bold",
                                         textColor=WHITE)) for h in header]]
    for r in rows:
        data.append([Paragraph(str(c), S("td", fontSize=9, fontName="Helvetica",
                                          leading=12)) for c in r])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  DARK_BLUE),
        ("BACKGROUND",    (0,1), (-1,-1), colors.HexColor("#F5F8FC")),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.white, colors.HexColor("#EBF2FA")]),
        ("BOX",           (0,0), (-1,-1), 0.5, GREY_LINE),
        ("INNERGRID",     (0,0), (-1,-1), 0.3, GREY_LINE),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ]))
    return t

# ════════════════════════════════════════════════════════════════════════════
# BUILD CONTENT
# ════════════════════════════════════════════════════════════════════════════
story = []

# ── COVER PAGE ───────────────────────────────────────────────────────────────
cover = Table(
    [[Paragraph("Statistics Exam<br/>Master Guide", title_style)],
     [Paragraph("Multiple Linear Regression &amp; Time Series", subtitle_style)],
     [Paragraph("How to read questions · Which method to use · Why it works<br/>"
                "Common pitfalls · Trick phrasings · Worked decision logic", subtitle_style)]],
    colWidths=[W]
)
cover.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), DARK_BLUE),
    ("TOPPADDING",    (0,0), (-1,-1), 28),
    ("BOTTOMPADDING", (0,0), (-1,-1), 18),
    ("LEFTPADDING",   (0,0), (-1,-1), 20),
    ("RIGHTPADDING",  (0,0), (-1,-1), 20),
    ("ROUNDEDCORNERS",(0,0), (-1,-1), 8),
]))
story += [sp(40), cover, sp(30)]

story.append(Paragraph(
    "This guide walks you through every type of question that appears in exams on "
    "Multiple Linear Regression (MLR) and Time Series Regression. For each topic you "
    "will find: <b>what the question is really asking</b>, <b>which method to choose and why</b>, "
    "<b>step-by-step decision logic</b>, <b>the correct interpretation</b>, "
    "<b>pitfalls that cost marks</b>, and <b>different phrasings that mean the same thing</b>.",
    body))
story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
# PART 1 — MLR
# ════════════════════════════════════════════════════════════════════════════
story.append(banner("PART 1 — MULTIPLE LINEAR REGRESSION (MLR)"))
story.append(sp(8))

# ── 1.1 Reading the question ─────────────────────────────────────────────────
story.append(Paragraph("1.1  How to Read an MLR Question", h1))
story.append(Paragraph(
    "Before touching SPSS, read the question twice and identify four things:", body))
story.append(simple_table(
    ["What to identify", "How it appears in the question", "What you must do"],
    [
        ["Dependent variable (Y)", '"Regress X on Y", "Y as a function of", "explain Y"',
         "Put Y in the Dependent box"],
        ["Continuous predictors", "Age, income, price — no categories mentioned",
         "Enter directly"],
        ["Categorical predictors", '"Region", "type", "group" with labels',
         "Create dummy variables manually"],
        ["Log transformation", '"ln(X)", "log(X)", "logarithm of"',
         "Variable is already logged OR use Transform → Compute"],
        ["Interaction term", '"effect of X depends on Z", "moderating effect"',
         "Create X×Z product variable"],
    ],
    col_widths=[3.5*cm, 7.5*cm, 5.5*cm]
))
story.append(sp(6))

# ── 1.2 Dummy variables ──────────────────────────────────────────────────────
story.append(Paragraph("1.2  Dummy Variables", h1))
story.append(Paragraph(
    "A dummy variable (also called indicator variable or binary variable) converts a "
    "categorical variable with k categories into k−1 binary (0/1) variables. "
    "The excluded category is the <b>reference group</b> — all interpretations are "
    "made relative to it.", body))

story.append(Paragraph("Rule: k categories → create k−1 dummies", h2))
story.append(simple_table(
    ["Categories", "Dummies to create", "Reference (omitted)"],
    [
        ["North, South, Center, East (4)", "D_North, D_South, D_East (3)", "Center"],
        ["Male, Female (2)", "D_Female (1)", "Male"],
        ["Low, Medium, High (3)", "D_Medium, D_High (2)", "Low"],
    ],
    col_widths=[5*cm, 7*cm, 4.5*cm]
))
story.append(sp(4))

story.append(Paragraph("In SPSS: Transform → Compute Variable", h2))
story.append(Paragraph("For each dummy, type an expression that equals 1 for that group:", body))
story.append(formula_box([
    "D_North  =  (Region = 1)   [if North is coded as 1]",
    "D_South  =  (Region = 2)",
    "D_East   =  (Region = 4)   [skip 3 = Center → reference]",
]))
story.append(sp(4))

story.append(Paragraph("How to write the theoretical model:", h2))
story.append(formula_box([
    "Y = β₀ + β₁X₁ + β₂D_North + β₃D_South + β₄D_East + ε",
    "",
    "Interpretation of β₂ (D_North):",
    "  On average, North regions have β₂ units MORE Y than Center regions,",
    "  holding all other variables constant.",
]))
story.append(sp(4))
story.append(pitfall_box([
    "Never create k dummies — always k−1. Including all categories causes perfect "
    "multicollinearity (the dummy trap). SPSS will drop one automatically, but you "
    "must know which one is the reference.",
    'The question may say "use Center as reference" — that just means do NOT create '
    "a dummy for Center.",
    'Different phrasings for the same thing: "baseline group", "comparison group", '
    '"omitted category", "reference category" — all mean the same thing.',
]))
story.append(sp(8))

# ── 1.3 Log transformations ──────────────────────────────────────────────────
story.append(Paragraph("1.3  Log Transformations and Interpretation", h1))
story.append(simple_table(
    ["Model type", "Equation", "Interpretation of β"],
    [
        ["Linear (standard)", "Y = α + βX + ε",
         "1-unit rise in X → β unit change in Y"],
        ["Linear-log", "Y = α + β·ln(X) + ε",
         "1% rise in X → β/100 unit change in Y"],
        ["Log-linear", "ln(Y) = α + βX + ε",
         "1-unit rise in X → β×100 % change in Y"],
        ["Log-log", "ln(Y) = α + β·ln(X) + ε",
         "1% rise in X → β% change in Y (elasticity)"],
    ],
    col_widths=[3*cm, 6*cm, 7.5*cm]
))
story.append(sp(4))
story.append(info_box([
    "The most common exam type is Linear-log: Y = α + β·ln(X) + ε.",
    "Trick: the question gives β = −16 and X is ln(NOx). Answer: 1% increase in NOx "
    "→ −16/100 = −0.16 unit change in Y (e.g., −$160 if Y is in thousands).",
    "Key phrase to watch for: 'ln(X)' or 'log(X)' in the variable name in the output.",
], bg=LIGHT_BLUE, label="Linear-Log Worked Example"))
story.append(sp(8))

# ── 1.4 Interpreting coefficients ───────────────────────────────────────────
story.append(Paragraph("1.4  Interpreting Coefficients — The Full Decision Tree", h1))
story.append(Paragraph(
    "When the question says 'interpret the coefficient of X', follow this tree:", body))
story.append(simple_table(
    ["Is X logged?", "Is Y logged?", "Interpretation"],
    [
        ["No", "No", "1 extra unit of X → β extra units of Y (ceteris paribus)"],
        ["Yes (ln X)", "No", "1% extra in X → β/100 extra units of Y"],
        ["No", "Yes (ln Y)", "1 extra unit of X → β×100 % change in Y"],
        ["Yes (ln X)", "Yes (ln Y)", "1% extra in X → β% change in Y"],
        ["Dummy (0/1)", "No", "Being in group D → β extra units of Y vs. reference"],
    ],
    col_widths=[2.5*cm, 2.5*cm, 11.5*cm]
))
story.append(sp(8))

# ── 1.5 Individual significance ─────────────────────────────────────────────
story.append(Paragraph("1.5  Testing Individual Coefficient Significance", h1))
story.append(Paragraph(
    "Every coefficient in the SPSS Coefficients table has a t-statistic and a "
    "p-value (Sig. column). Use the p-value directly:", body))
story.append(formula_box([
    "H0: β = 0  (variable has no effect)",
    "H1: β ≠ 0  (variable does have an effect)",
    "",
    "Decision:  If Sig. < 0.05  →  Reject H0  →  significant at 5%",
    "           If Sig. ≥ 0.05  →  Fail to reject H0  →  not significant",
]))
story.append(sp(4))
story.append(pitfall_box([
    '"Significant" does NOT mean "important" or "large". It means we can statistically '
    "distinguish the effect from zero.",
    'Different phrasings: "Is X relevant?", "Does X matter?", "Test whether X has an '
    'effect", "Is β significantly different from zero?" — all ask for the t-test/p-value.',
]))
story.append(sp(8))

# ── 1.6 Joint F-test ─────────────────────────────────────────────────────────
story.append(Paragraph("1.6  Joint F-test (Testing a Group of Variables Together)", h1))
story.append(Paragraph(
    "Use a joint F-test when the question asks whether a GROUP of variables "
    "(e.g., all region dummies together) is significant, not just one.", body))

story.append(Paragraph("When do you know to use a joint F-test?", h2))
story.append(info_box([
    '"Are the region dummies jointly significant?"',
    '"Do the seasonal effects together improve the model?"',
    '"Test whether including dummies D1, D2, D3 adds explanatory power."',
    '"Is the set of interaction terms significant?"',
    "Any question involving MORE THAN ONE variable being tested simultaneously.",
], bg=LIGHT_BLUE, label="Trigger phrases for joint F-test"))
story.append(sp(6))

story.append(Paragraph("How to run it in SPSS:", h2))
story.append(simple_table(
    ["Step", "What you do", "Why"],
    [
        ["1", "Run the UNRESTRICTED model — all variables included", "Get SSE_u (or R²_u)"],
        ["2", "Run the RESTRICTED model — remove the variables being tested", "Get SSE_r (or R²_r)"],
        ["3", "Count J = number of variables you removed", "J = numerator df"],
        ["4", "Get n and k from unrestricted model", "n = observations, k = predictors"],
        ["5", "Compute F using the formula", "Compare to p-value"],
    ],
    col_widths=[1*cm, 8*cm, 7.5*cm]
))
story.append(sp(4))
story.append(formula_box([
    "Option A (using SSE from ANOVA tables):",
    "  F = [(SSE_r − SSE_u) / J]  /  [SSE_u / (n − k − 1)]",
    "",
    "Option B (using R² from Model Summary):",
    "  F = [(R²_u − R²_r) / J]  /  [(1 − R²_u) / (n − k − 1)]",
    "",
    "Decision: Use the p-value from SPSS for the overall F in the ANOVA table.",
    "  If you compute F manually: compare to F-distribution critical value.",
    "  Shortcut: If both ANOVA Sig. values are available, compare them.",
]))
story.append(sp(4))
story.append(pitfall_box([
    "J is the number of RESTRICTIONS (variables removed), not the total number of variables.",
    "The restricted model has FEWER variables. Its SSE will always be LARGER (worse fit).",
    'n−k−1 uses k from the UNRESTRICTED model.',
    '"Test whether dummies are jointly significant" = run restricted model WITHOUT those dummies.',
]))
story.append(sp(8))

# ── 1.7 Residual analysis ────────────────────────────────────────────────────
story.append(Paragraph("1.7  Residual Plot Analysis", h1))
story.append(Paragraph(
    "A residual plot (residuals on Y-axis, fitted values or X on X-axis) "
    "is used to detect three violations of OLS assumptions:", body))
story.append(simple_table(
    ["Problem", "What you see in the plot", "Assumption violated"],
    [
        ["Heteroskedasticity",
         "Spread of residuals grows or shrinks — fan shape (wider on one side)",
         "A2: Var(ε) = σ² (constant variance)"],
        ["Non-linearity",
         "Residuals curve upward or downward — systematic pattern",
         "A1: Model is correctly specified (linearity)"],
        ["Outliers",
         "One or a few points far above/below the rest — isolated large residuals",
         "Distort estimates — check and report"],
    ],
    col_widths=[3.5*cm, 7*cm, 6*cm]
))
story.append(sp(4))
story.append(info_box([
    "A GOOD residual plot: random cloud of points centered around zero. "
    "No pattern, no fan, no curve.",
    "A BAD plot: any systematic shape — V-shape, cone, curve, or obvious outliers.",
    "You do NOT need to quantify — describe what you SEE and name the violation.",
], bg=LIGHT_GREEN, label="What a good vs. bad plot looks like"))
story.append(sp(4))
story.append(pitfall_box([
    "Do not say 'the residuals are not normal' from a residual vs. fitted plot — "
    "normality requires a histogram or Q-Q plot.",
    "Heteroskedasticity in residuals → standard errors are wrong → t-tests and "
    "p-values are unreliable. This is why we run the White test.",
]))
story.append(sp(8))

# ── 1.8 White test ──────────────────────────────────────────────────────────
story.append(Paragraph("1.8  The White Test for Heteroskedasticity", h1))
story.append(Paragraph(
    "The White test formally tests whether the variance of the error is constant "
    "(homoskedastic) or varies (heteroskedastic).", body))
story.append(formula_box([
    "H0: homoskedasticity (Var(ε) = σ²  — constant)",
    "H1: heteroskedasticity (variance is not constant)",
    "",
    "Step 1: Run original model. Save residuals ê.",
    "Step 2: Compute ê² (squared residuals) via Transform → Compute.",
    "Step 3: Run auxiliary regression:",
    "  ê² = α₀ + (all original X's) + (X² for each continuous X) + (Xi×Xj for each pair) + u",
    "        Note: do NOT square dummies. Do NOT create dummy × dummy terms.",
    "Step 4: W = n × R²_aux  ~  χ²(df)",
    "        df = number of regressors in auxiliary regression (excluding constant)",
    "Step 5: If W > critical value (or Sig. < 0.05)  →  Reject H0  →  heteroskedasticity present",
]))
story.append(sp(4))
story.append(pitfall_box([
    "The df for the White test is NOT 1 — it equals the number of terms in the auxiliary "
    "regression. With 2 continuous X's: original X1, X2 + squared X1², X2² + cross X1×X2 = 5 df.",
    "Dummies are never squared (D² = D for a 0/1 variable) and dummy×dummy products are "
    "excluded from the auxiliary regression.",
    "Always state df in your answer: W ~ χ²(df). Different questions have different df.",
]))
story.append(sp(8))

# ── 1.9 Omitted variable bias ────────────────────────────────────────────────
story.append(Paragraph("1.9  Omitted Variable Bias", h1))
story.append(Paragraph(
    "If a relevant variable Z is left out of the model, the estimated coefficient "
    "on the included variable X will be biased. The direction of the bias is:", body))
story.append(formula_box([
    "sign(bias on X) = sign(β_Z) × sign(r(X, Z))",
    "",
    "Where:  β_Z = the true effect of the omitted variable Z on Y",
    "        r(X, Z) = correlation between included X and omitted Z",
    "",
    "If bias > 0: estimate is TOO HIGH (upward bias)",
    "If bias < 0: estimate is TOO LOW  (downward bias)",
]))
story.append(sp(4))
story.append(simple_table(
    ["β_Z (effect of Z on Y)", "r(X, Z) (correlation)", "Bias on β_X", "Estimate is..."],
    [
        ["Positive (+)", "Positive (+)", "Positive → upward bias", "Too high"],
        ["Positive (+)", "Negative (−)", "Negative → downward bias", "Too low"],
        ["Negative (−)", "Positive (+)", "Negative → downward bias", "Too low"],
        ["Negative (−)", "Negative (−)", "Positive → upward bias", "Too high"],
    ],
    col_widths=[4.5*cm, 4.5*cm, 4*cm, 3.5*cm]
))
story.append(sp(4))
story.append(info_box([
    "Worked example: Estimating effect of NOx pollution on housing values, omitting "
    "industrial zone variable (Indus).",
    "β_Indus < 0 (more industry → lower house values). r(lnNOx, Indus) > 0 "
    "(NOx and industry are positively correlated).",
    "Bias = (−) × (+) = negative → the estimate of β_lnNOx is TOO LOW (more negative than truth).",
], bg=LIGHT_BLUE, label="Worked Example"))
story.append(sp(4))
story.append(pitfall_box([
    '"Biased downward" means the estimate is too small (too negative for a negative coefficient).',
    "The question might not give you the correlation directly — reason from common sense: "
    "do areas with high NOx also tend to have more industry? If yes, correlation is positive.",
    '"Omitted variable bias" and "specification error" mean the same thing.',
]))
story.append(sp(8))

# ── 1.10 VIF / Multicollinearity ─────────────────────────────────────────────
story.append(Paragraph("1.10  VIF and Multicollinearity", h1))
story.append(Paragraph(
    "Multicollinearity occurs when two or more predictors are highly correlated "
    "with each other. This inflates standard errors and makes individual t-tests "
    "unreliable even if the model fits well.", body))
story.append(formula_box([
    "VIF_j = 1 / (1 − R²_j)",
    "Tolerance_j = 1 − R²_j = 1 / VIF_j",
    "",
    "Where R²_j = R² from regressing X_j on all other X's (auxiliary regression)",
    "",
    "Rule of thumb:  VIF > 5 (or 10) → serious multicollinearity",
    "                Tolerance < 0.2 (or 0.1) → serious multicollinearity",
]))
story.append(sp(4))
story.append(simple_table(
    ["VIF value", "Tolerance", "Interpretation"],
    [
        ["1.0", "1.00", "No multicollinearity — X is uncorrelated with other X's"],
        ["1 – 5", "0.20 – 1.00", "Acceptable — moderate correlation, no problem"],
        ["5 – 10", "0.10 – 0.20", "Concerning — high multicollinearity, check estimates"],
        ["> 10", "< 0.10", "Severe — estimates are unreliable"],
    ],
    col_widths=[2.5*cm, 3*cm, 11*cm]
))
story.append(sp(4))
story.append(info_box([
    "In SPSS: Analyze → Regression → Linear → Statistics → tick Collinearity diagnostics.",
    "VIF and Tolerance appear in the Coefficients table.",
    "If asked to compute VIF manually: run the auxiliary regression of X_j on all "
    "other X's, read R², then VIF = 1/(1 − R²).",
], bg=LIGHT_BLUE))
story.append(sp(8))

# ── 1.11 MLR pitfalls summary ────────────────────────────────────────────────
story.append(KeepTogether([
    Paragraph("1.11  Quick Reference — Question Phrasings and Methods", h1),
    simple_table(
        ["If the question says...", "It means...", "Method"],
        [
            ['"Interpret the coefficient of ln(X)"',
             "Effect of 1% change in X", "β/100 units change in Y"],
            ['"Test if Region is significant"',
             "All region dummies jointly", "Joint F-test"],
            ['"Is β₂ significantly different from zero?"',
             "Individual significance", "p-value from Coefficients table"],
            ['"Test for heteroskedasticity"',
             "Unequal error variance", "White test (W = n×R²_aux)"],
            ['"What is the bias if Indus is omitted?"',
             "Direction of bias", "sign(β_omitted) × sign(r(X, omitted))"],
            ['"What is the reference category?"',
             "Omitted dummy group", "State which group has no dummy variable"],
            ['"VIF is 2.5 — what does this mean?"',
             "Multicollinearity assessment", "Compare to threshold of 5"],
            ['"Write the theoretical model"',
             "Symbolic equation with all variables", "Write Y = β₀ + β₁X₁ + β₂D₁ + ..."],
        ],
        col_widths=[5.5*cm, 5*cm, 6*cm]
    ),
]))

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
# PART 2 — TIME SERIES
# ════════════════════════════════════════════════════════════════════════════
story.append(banner("PART 2 — TIME SERIES REGRESSION"))
story.append(sp(8))

# ── 2.1 Overview ─────────────────────────────────────────────────────────────
story.append(Paragraph("2.1  The Three-Step Framework — Always in This Order", h1))
story.append(info_box([
    "STEP 1 — STATIONARITY: Test whether each series is stationary (Dickey-Fuller test). "
    "Non-stationary series must be differenced before use.",
    "STEP 2 — FIT THE MODEL: Choose static, DL(q), or AR(1) model depending on what "
    "the question specifies. For DL(q), use top-down lag selection.",
    "STEP 3 — CHECK AUTOCORRELATION: Run the LMSC test on the residuals of the fitted model.",
], bg=LIGHT_BLUE, label="The Three-Step Framework"))
story.append(sp(4))
story.append(pitfall_box([
    "You CANNOT skip Step 1. Using non-stationary series in regression produces spurious "
    "results — high R² and significant t-statistics that mean nothing.",
    "Steps must go in order: stationarity → fit → check. Never fit first.",
]))
story.append(sp(8))

# ── 2.2 Stationarity ─────────────────────────────────────────────────────────
story.append(Paragraph("2.2  Step 1 — Stationarity and the Dickey-Fuller Test", h1))
story.append(Paragraph(
    "A stationary series has a constant mean and variance over time. A non-stationary "
    "series drifts or wanders — its mean changes. Using non-stationary series causes "
    "spurious regression.", body))

story.append(Paragraph("How to choose DF Version 1 or Version 2:", h2))
story.append(simple_table(
    ["DF Version", "Regression run", "When to use"],
    [
        ["Version 1 — no trend",
         "∆Y_t = α₀ + α₁Y_{t-1} + ε_t",
         "Time plot shows NO visible upward or downward trend"],
        ["Version 2 — with trend",
         "∆Y_t = α₀ + λt + α₁Y_{t-1} + ε_t",
         "Time plot shows clear trend, OR when unsure (safer default)"],
    ],
    col_widths=[3.5*cm, 6.5*cm, 6.5*cm]
))
story.append(sp(4))
story.append(formula_box([
    "H0: α₁ = 0  (unit root — series is NON-STATIONARY)",
    "H1: α₁ < 0  (series IS stationary)",
    "",
    "Critical values (5% level):",
    "  Version 1 (no trend):   −2.86",
    "  Version 2 (with trend): −3.41",
    "",
    "Decision: If t-statistic on Y_{t-1} is MORE NEGATIVE than the critical value → Reject H0 → stationary",
    "          If t-statistic is LESS NEGATIVE (closer to zero) → Fail to reject H0 → unit root",
    "",
    "Example: t = −1.64, critical value = −3.41",
    "  −1.64 > −3.41  →  fail to reject H0  →  NON-STATIONARY",
    "",
    "Example: t = −4.20, critical value = −3.41",
    "  −4.20 < −3.41  →  reject H0  →  STATIONARY",
]))
story.append(sp(4))

story.append(Paragraph("What to do after the DF test:", h2))
story.append(simple_table(
    ["DF result on levels", "Action", "Then what?"],
    [
        ["Stationary (reject H0)", "Use series in levels", "Proceed to fit model"],
        ["Non-stationary (fail to reject H0)",
         "Take first differences: ∆Y = Y_t − Y_{t-1}",
         "Run DF test again on ∆Y"],
        ["∆Y is stationary (reject H0)", "Use first differences in model",
         "Series is I(1) — proceed"],
        ["∆Y still non-stationary", "Rare — take second differences",
         "Series may be I(2)"],
    ],
    col_widths=[4.5*cm, 5.5*cm, 6.5*cm]
))
story.append(sp(4))
story.append(pitfall_box([
    "The DF test has a ONE-SIDED alternative: H1 is α₁ < 0, not α₁ ≠ 0. "
    "You only reject when the t-statistic is sufficiently NEGATIVE.",
    "NEVER use the standard t-table (±1.96) for the DF test. The DF distribution "
    "is non-standard. Always use −2.86 (V1) or −3.41 (V2) at 5%.",
    "In SPSS, the p-value shown for the LAG variable uses the wrong distribution — "
    "ignore it. Compare only the t-statistic to the special critical value.",
    "Rejecting H0 in the DF test means the series IS stationary — opposite of most tests "
    "where rejecting H0 is the 'bad news'.",
]))
story.append(sp(8))

# ── 2.3 Model selection ──────────────────────────────────────────────────────
story.append(Paragraph("2.3  Step 2 — Which Model to Fit?", h1))
story.append(simple_table(
    ["Model", "Equation", "When to use"],
    [
        ["Static",
         "Y_t = α + βX_t + ε_t",
         "Question specifies it, or no significant lags found in DL"],
        ["DL(q) — Distributed Lag",
         "Y_t = α + β₀X_t + β₁X_{t-1} + … + βqX_{t-q} + ε_t",
         "Question asks for DL model; effects of X are delayed over time"],
        ["AR(1) — Autoregressive",
         "Y_t = α + βX_t + γY_{t-1} + ε_t",
         "Question specifies AR(1); or strong autocorrelation in DL residuals"],
    ],
    col_widths=[2.5*cm, 7*cm, 7*cm]
))
story.append(sp(8))

# ── 2.4 DL top-down ──────────────────────────────────────────────────────────
story.append(Paragraph("2.4  DL(q) — Top-Down Lag Selection", h1))
story.append(Paragraph(
    "The top-down procedure finds the optimal number of lags q by starting high "
    "and removing insignificant lags one at a time from the top.", body))
story.append(formula_box([
    "Start: Fit DL(q_max). In SPSS, create lag variables first:",
    "  LAG1_X = LAG(X, 1)    LAG2_X = LAG(X, 2)    etc.",
    "",
    "Top-down rule:",
    "  1. Look at the p-value of the HIGHEST lag (e.g., LAGq_X).",
    "  2. If p > 0.05: not significant → drop it → fit DL(q-1).",
    "  3. If p ≤ 0.05: significant → STOP. Optimal q is the current model.",
    "  4. Repeat until the highest remaining lag is significant.",
    "",
    "IMPORTANT: Never drop an intermediate lag.",
    "  If lag 2 is significant but lag 1 is not → keep BOTH.",
    "  You cannot have lag 2 without lag 1 in the model.",
]))
story.append(sp(4))

story.append(Paragraph("Total Multiplier for DL(q):", h2))
story.append(formula_box([
    "Total multiplier = β₀ + β₁ + β₂ + … + βq",
    "",
    "Interpretation: If X permanently increases by 1 unit and stays there forever,",
    "Y will eventually change by this total amount in the long run.",
    "",
    "Immediate effect (impact multiplier) = β₀ only.",
]))
story.append(sp(4))
story.append(pitfall_box([
    "q_max is usually given in the question. If not, a common default is 3 or 4.",
    "Each lag costs you one observation. DL(3) with n=100 gives 97 usable observations.",
    '"Optimal lag length" and "best-fitting DL model" and "chosen q" all mean the same thing.',
    'Do not confuse total multiplier (long-run effect) with β₀ (immediate effect). '
    'The question may specifically ask for one or the other.',
]))
story.append(sp(8))

# ── 2.5 AR(1) ────────────────────────────────────────────────────────────────
story.append(Paragraph("2.5  AR(1) — Autoregressive Model", h1))
story.append(formula_box([
    "Model: Y_t = α + βX_t + γY_{t-1} + ε_t",
    "",
    "Coefficients:",
    "  β = immediate effect of a 1-unit rise in X_t on Y_t",
    "  γ = persistence — how much of last period's Y carries into this period",
    "      Requires |γ| < 1 for the model to be valid (stationary errors)",
    "",
    "Total multiplier = β / (1 − γ)",
    "  Interpretation: permanent 1-unit rise in X eventually changes Y by β/(1−γ)",
    "",
    "Example: β = −0.031, γ = 0.52",
    "  Total multiplier = −0.031 / (1 − 0.52) = −0.031 / 0.48 = −0.065",
]))
story.append(sp(4))
story.append(pitfall_box([
    "In AR(1) with autocorrelation, estimates are BIASED (worse than inefficient). "
    "In DL with autocorrelation, estimates are only INEFFICIENT (standard errors wrong). "
    "This is why the LMSC test matters after fitting AR(1).",
    "γ must be strictly less than 1 in absolute value. If γ ≥ 1 the total multiplier "
    "formula breaks down (series is non-stationary).",
    '"Persistence coefficient", "AR coefficient on lagged Y", "coefficient on Y_{t-1}" '
    "— all refer to γ.",
]))
story.append(sp(8))

# ── 2.6 LMSC ─────────────────────────────────────────────────────────────────
story.append(Paragraph("2.6  Step 3 — The LMSC Autocorrelation Test", h1))
story.append(Paragraph(
    "Autocorrelation means the error in one period is correlated with the error "
    "in the previous period. It violates Assumption A3 and makes standard errors wrong.", body))
story.append(formula_box([
    "H0: ρ = 0  (no autocorrelation — A3 satisfied)",
    "H1: ρ ≠ 0  (autocorrelation present — A3 violated)",
    "",
    "Step 1: Fit original model. Save Unstandardized Residuals (RES_1).",
    "Step 2: Create LAG_RES1 = LAG(RES_1, 1) via Transform → Compute.",
    "Step 3: Run auxiliary regression:",
    "  RES_1 = α₀ + α₁X₁_t + … + αₖXₖ_t + α_{k+1}·LAG_RES1 + u_t",
    "  (Include ALL original predictors PLUS the lagged residual)",
    "Step 4: LM = n_aux × R²_aux   where n_aux = n − 1 (one obs lost to lag)",
    "Step 5: LM ~ χ²(1). Critical value at 5% = 3.841",
    "  If LM > 3.841 (or p < 0.05): Reject H0 → autocorrelation present",
    "  If LM ≤ 3.841 (or p ≥ 0.05): Fail to reject H0 → A3 plausibly satisfied",
]))
story.append(sp(4))

story.append(Paragraph("How to get n_aux:", h2))
story.append(info_box([
    "From the ANOVA table of the auxiliary regression: n_aux = Total df + 1.",
    "Or: n_aux = n − 1 (you lose one observation creating the lag).",
    "For a DL(q) model: n_aux = n − q − 1 (you lose q obs from lags plus 1 from residual lag).",
], bg=LIGHT_BLUE))
story.append(sp(4))
story.append(pitfall_box([
    "The auxiliary regression MUST include all original X predictors, not just the lagged residual.",
    "For a DL(q) model, the auxiliary regression includes: all original X's AND all "
    "lagged X's used in the DL model, plus LAG_RES.",
    '"Test for autocorrelation", "check A3", "Breusch-Godfrey test", "LMSC test" '
    "— all refer to the same procedure.",
    "DW (Durbin-Watson) is NOT valid when Y_{t-1} appears in the model (AR models). "
    "Always use LMSC.",
]))
story.append(sp(8))

# ── 2.7 Pitfall grid ─────────────────────────────────────────────────────────
story.append(Paragraph("2.7  Critical Pitfall Grid — Opposites That Confuse Everyone", h1))
story.append(simple_table(
    ["Test", "H0 means...", "Reject H0 means...", "Fail to reject means..."],
    [
        ["Dickey-Fuller",
         "Series HAS a unit root (NON-STATIONARY)",
         "Series IS stationary ✓",
         "Series is non-stationary — difference it"],
        ["LMSC",
         "NO autocorrelation (A3 satisfied)",
         "Autocorrelation IS present — fix model",
         "A3 plausibly satisfied ✓"],
        ["Individual t-test",
         "β = 0 (variable has NO effect)",
         "Variable DOES have a significant effect",
         "Cannot conclude variable matters"],
        ["Joint F-test",
         "All tested β = 0 (group has NO effect)",
         "Group of variables jointly significant",
         "Cannot conclude group matters"],
        ["White test",
         "Homoskedasticity (A2 satisfied)",
         "Heteroskedasticity present — A2 violated",
         "A2 plausibly satisfied ✓"],
    ],
    col_widths=[3*cm, 4*cm, 4.5*cm, 5*cm]
))
story.append(sp(8))

# ── 2.8 Deterministic vs stochastic ─────────────────────────────────────────
story.append(Paragraph("2.8  Deterministic vs. Stochastic Trends — Different Fix!", h1))
story.append(Paragraph(
    "Two types of non-stationarity exist and they require DIFFERENT fixes. "
    "Applying the wrong fix makes things worse.", body))
story.append(simple_table(
    ["Feature", "Deterministic trend", "Stochastic trend (unit root)"],
    [
        ["Cause", "λt term — mean grows linearly", "ρ = 1 — shocks are permanent"],
        ["Pattern in plot", "Smooth, predictable upward drift", "Erratic, wanders unpredictably"],
        ["Variance", "Constant", "Grows over time"],
        ["After a shock", "Series returns to trend line", "Series never recovers"],
        ["Correct fix", "Add t (time variable) as regressor", "Take first differences ∆Y"],
        ["Wrong fix consequence",
         "First differencing → artificial negative autocorrelation",
         "Detrending does not remove random walk"],
    ],
    col_widths=[3.5*cm, 6.5*cm, 6.5*cm]
))
story.append(sp(4))
story.append(info_box([
    "How to tell them apart: look at the DF test result.",
    "If DF rejects H0 (stationary) but the plot shows a trend → deterministic trend "
    "(|ρ| < 1, λ ≠ 0) → add t as regressor.",
    "If DF fails to reject H0 (unit root) → stochastic trend (ρ = 1) → take differences.",
], bg=LIGHT_BLUE, label="Decision rule"))
story.append(sp(8))

# ── 2.9 TS phrasings ─────────────────────────────────────────────────────────
story.append(Paragraph("2.9  Time Series — Question Phrasings Reference", h1))
story.append(simple_table(
    ["If the question says...", "It means...", "Method"],
    [
        ['"Is the series stationary?"',
         "Does it have a unit root?",
         "Dickey-Fuller test"],
        ['"Test for a unit root"',
         "Is ρ = 1?",
         "Dickey-Fuller test"],
        ['"Should we use levels or differences?"',
         "What stationarity property does it have?",
         "Run DF, then decide"],
        ['"Determine optimal lag length"',
         "What is the best q for DL(q)?",
         "Top-down procedure"],
        ['"What is the long-run effect?"',
         "Total multiplier",
         "DL: Σβk  |  AR: β/(1−γ)"],
        ['"What is the immediate effect?"',
         "Impact multiplier",
         "β₀ (the coefficient on current X only)"],
        ['"Test for autocorrelation"',
         "Is A3 violated?",
         "LMSC test (LM = n × R²_aux)"],
        ['"Is the model well-specified?"',
         "Check all assumptions",
         "LMSC + residual plot"],
        ['"Series is I(1)"',
         "Non-stationary in levels, stationary in differences",
         "Use first differences in model"],
        ['"Spurious regression risk"',
         "Non-stationary series used in levels",
         "Run DF first, then decide"],
    ],
    col_widths=[5.5*cm, 4.5*cm, 6.5*cm]
))
story.append(sp(8))

# ── 2.10 Full workflow ────────────────────────────────────────────────────────
story.append(KeepTogether([
    Paragraph("2.10  SPSS Step-by-Step Workflow — Full Exam Procedure", h1),
    simple_table(
        ["Step", "SPSS action", "What to record"],
        [
            ["1a. Plot series",
             "Graphs → Chart Builder → Line → drag variable and Time to axes",
             "Does it trend? Random walk?"],
            ["1b. DF on levels",
             "Create LAG_Y = LAG(Y,1) and DIFF_Y = Y − LAG_Y via Compute.\n"
             "Regression: DV=DIFF_Y, IV=LAG_Y (+ time variable for V2)",
             "t-stat on LAG_Y. Compare to −2.86/−3.41"],
            ["1c. If unit root: DF on differences",
             "Create LAG_DIFFY = LAG(DIFF_Y,1) and DIFF2_Y = DIFF_Y − LAG_DIFFY.\n"
             "Regression: DV=DIFF2_Y, IV=LAG_DIFFY (+ time for V2)",
             "t-stat on LAG_DIFFY. Compare to −2.86/−3.41"],
            ["2a. Create lag variables",
             "Transform → Compute: LAG1_X = LAG(X,1), LAG2_X = LAG(X,2) etc.",
             "Note observations lost"],
            ["2b. Fit model",
             "Regression with appropriate variables (static/DL/AR)",
             "All coefficients, R², n"],
            ["3a. Save residuals",
             "In regression dialog: Save → Unstandardized Residuals",
             "Variable RES_1 created"],
            ["3b. Create lagged residual",
             "Transform → Compute: LAG_RES1 = LAG(RES_1, 1)",
             "Variable LAG_RES1 created"],
            ["3c. LMSC auxiliary regression",
             "Regression: DV=RES_1, IV=all original X's + LAG_RES1",
             "R² and n from Model Summary + ANOVA"],
            ["3d. Compute LM",
             "LM = n_aux × R²_aux. Compare to 3.841",
             "State conclusion about A3"],
        ],
        col_widths=[2.2*cm, 8.3*cm, 5.5*cm]
    ),
]))
story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
# PART 3 — MASTER PITFALL LIST
# ════════════════════════════════════════════════════════════════════════════
story.append(banner("PART 3 — MASTER PITFALL & TRICK PHRASING LIST", bg=ORANGE))
story.append(sp(8))

story.append(Paragraph("3.1  The Top 15 Mistakes (and How to Avoid Them)", h1))
pitfalls = [
    ("Using p-value for DF test",
     "SPSS's p-value for the LAG variable in the DF regression uses the wrong "
     "distribution. Always compare the t-statistic directly to −2.86 (V1) or −3.41 (V2)."),
    ("Rejecting H0 in DF = non-stationary",
     "It is the OPPOSITE: rejecting H0 in the DF test means the series IS stationary. "
     "H0 is the unit root (non-stationarity)."),
    ("Creating k dummies instead of k−1",
     "For k categories, create exactly k−1 dummies. Including all k causes perfect "
     "multicollinearity (dummy trap). Always omit one reference category."),
    ("Using standard t-table for DF critical values",
     "The DF t-statistic does not follow a standard t-distribution. Standard values "
     "like ±1.96 or ±2.58 do not apply. Use −2.86 or −3.41."),
    ("Forgetting to include all X's in LMSC auxiliary regression",
     "The LMSC auxiliary regression regresses residuals on ALL original X's PLUS the "
     "lagged residual. Missing any X gives wrong R² and wrong LM statistic."),
    ("Total multiplier = β₀ only",
     "For DL(q): total multiplier = β₀ + β₁ + … + βq (sum of ALL lag coefficients). "
     "For AR(1): total multiplier = β/(1−γ). β₀ alone is only the immediate effect."),
    ("Using DW test for AR(1) models",
     "The Durbin-Watson statistic is INVALID when Y_{t−1} appears as a regressor. "
     "Always use the LMSC test."),
    ("Differencing when trend is deterministic",
     "Only difference when the DF test confirms a unit root (ρ = 1). "
     "If the series has a deterministic trend (|ρ| < 1, λ ≠ 0), add t as a regressor instead."),
    ("Dropping intermediate insignificant lags in DL",
     "In top-down selection, only drop the HIGHEST lag if insignificant. "
     "Never drop lag 1 while keeping lag 2 — the lag structure must be contiguous."),
    ("Squaring dummies in the White test",
     "D² = D for a 0/1 variable, so squaring dummies adds no information. "
     "Only square continuous variables. Also exclude dummy × dummy cross-products."),
    ("Confusing 'significant' with 'large'",
     "A coefficient can be statistically significant (p < 0.05) but economically "
     "negligible in size. Always comment on both significance AND magnitude."),
    ("Wrong sign for omitted variable bias",
     "Bias = sign(β_omitted) × sign(r(X_included, X_omitted)). "
     "Draw a sign table if needed — two negatives give a positive bias."),
    ("Ignoring the reference category when interpreting dummies",
     "The coefficient on D_North means 'compared to the reference group'. "
     "Always state what the reference category is in your interpretation."),
    ("Using levels when both series are I(1)",
     "If both Y and X are non-stationary I(1) series, always use first differences "
     "(unless cointegration is established — rare in introductory courses)."),
    ("n in LM formula is n_aux not original n",
     "The auxiliary regression loses one observation due to the lagged residual. "
     "Use n_aux = n − 1 (or read from the ANOVA table: n_aux = Total df + 1)."),
]

for i, (title, text) in enumerate(pitfalls):
    row = [[
        Paragraph(f"<b>{i+1}. {title}</b>", S(f"pt{i}", fontSize=9.5,
                  fontName="Helvetica-Bold", textColor=colors.HexColor("#7B0000"),
                  leading=13)),
        Paragraph(text, body)
    ]]
    t = Table(row, colWidths=[4.5*cm, W - 4.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), RED_BG if i % 2 == 0 else colors.HexColor("#FFF0F0")),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("BOX",           (0,0), (-1,-1), 0.3, GREY_LINE),
        ("LINEAFTER",     (0,0), (0,-1), 0.5, colors.HexColor("#E0A0A0")),
    ]))
    story.append(t)
    story.append(sp(3))

story.append(sp(8))

# ── 3.2 Trick phrasings ──────────────────────────────────────────────────────
story.append(Paragraph("3.2  Trick Phrasings — Same Question, Different Words", h1))
story.append(simple_table(
    ["What the question writes", "What it actually means"],
    [
        ['"Is X relevant to explaining Y?"', '"Is β_X significantly different from zero?" → p-value test'],
        ['"Does adding Region improve the model?"', '"Are the region dummies jointly significant?" → Joint F-test'],
        ['"Baseline group" / "comparison group"', '"Reference category" — the omitted dummy group'],
        ['"Disturbance term carries memory"', '"There is autocorrelation" → LMSC test'],
        ['"Series wanders without returning"', '"Series has a unit root" → DF test, then difference'],
        ['"Spurious correlation risk"', '"Series is non-stationary" → run DF before modelling'],
        ['"Long-run equilibrium effect"', '"Total multiplier" → Σβk or β/(1−γ)'],
        ['"Impact effect of a price shock"', '"Immediate effect" → β₀ only'],
        ['"Error variance is not constant"', '"Heteroskedasticity" → White test'],
        ['"Predictors are too correlated"', '"Multicollinearity" → VIF and Tolerance'],
        ['"Coefficient on lagged Y is 0.7"', '"γ = 0.7 in AR(1)" → total multiplier = β/(1−0.7)'],
        ['"Integrated of order one"', '"I(1) — unit root in levels, stationary in differences"'],
        ['"Misspecification bias"', '"Omitted variable bias" → sign(β_Z) × sign(r(X,Z))'],
        ['"First-order autocorrelation"', '"AR(1) error: ε_t = ρε_{t-1} + u_t" → LMSC test'],
    ],
    col_widths=[7.5*cm, 9*cm]
))
story.append(sp(8))

# ── 3.3 One-page decision guide ─────────────────────────────────────────────
story.append(banner("QUICK DECISION GUIDE — Which Method for Which Question?", bg=GREEN))
story.append(sp(6))

story.append(Paragraph("MLR Questions", h1))
story.append(simple_table(
    ["Question type", "Method", "Key formula / output"],
    [
        ["Interpret coefficient of ln(X)", "Linear-log rule", "β/100 units change in Y per 1% rise in X"],
        ["Test one coefficient", "Individual t-test", "p-value (Sig.) in Coefficients table"],
        ["Test a group of variables", "Joint F-test", "F = [(SSE_r−SSE_u)/J] / [SSE_u/(n−k−1)]"],
        ["Check equal variance", "White test", "W = n×R²_aux ~ χ²(df)"],
        ["Direction of missing-variable distortion", "Omitted variable bias", "sign(β_Z) × sign(r(X,Z))"],
        ["How correlated are predictors?", "VIF / Tolerance", "VIF = 1/(1−R²_aux), threshold = 5"],
        ["Write equation with categories", "Dummy variables", "k−1 dummies, state reference"],
    ],
    col_widths=[5*cm, 4*cm, 7.5*cm]
))
story.append(sp(8))

story.append(Paragraph("Time Series Questions", h1))
story.append(simple_table(
    ["Question type", "Method", "Key output / decision"],
    [
        ["Is series stationary?", "Dickey-Fuller test", "t < −2.86(V1) or −3.41(V2) → stationary"],
        ["Series drifts with time", "DF test → unit root?", "Yes → difference.  No → add t"],
        ["Choose number of lags", "Top-down DL selection", "Drop highest lag while p > 0.05"],
        ["Long-run effect of X on Y", "Total multiplier", "DL: Σβk   |   AR: β/(1−γ)"],
        ["Immediate effect of X on Y", "Impact multiplier", "β₀ — coefficient on current X only"],
        ["Check for autocorrelation", "LMSC test", "LM = n×R²_aux. Compare to 3.841"],
        ["Model has Y_{t-1} as regressor", "AR(1)", "Do NOT use DW. Use LMSC."],
    ],
    col_widths=[5*cm, 4*cm, 7.5*cm]
))
story.append(sp(8))

# ── Final tip ─────────────────────────────────────────────────────────────────
story.append(tip_box([
    "Always state hypotheses (H0 and H1) before every test — even when they seem obvious.",
    "Always write a conclusion sentence after every test: 'Since p = X < 0.05, we reject H0...'",
    "For DF: compare t-statistic (not p-value) to special critical value.",
    "For LMSC and White test: use p-value directly (standard chi-squared distribution).",
    "For individual t-tests and F-tests in regression: use p-value from SPSS output.",
    "When in doubt about stationarity: use DF Version 2 (with trend) — it is the safer default.",
]))

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print("PDF created successfully.")
