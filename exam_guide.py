from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Register DejaVu fonts (full Unicode support) ─────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV",    FONT_DIR + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B",  FONT_DIR + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DV-M",  FONT_DIR + "DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("DV-MB", FONT_DIR + "DejaVuSansMono-Bold.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV", boldItalic="DV-B")

# ── Document ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    "/home/user/BabyPluto/MLR_TimeSeries_ExamGuide.pdf",
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm,
)
W = A4[0] - 4*cm

# ── Colours ──────────────────────────────────────────────────────────────────
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
def S(name, **kw):
    kw.setdefault("fontName", "DV")
    return ParagraphStyle(name, **kw)

title_style = S("Title",
    fontSize=21, textColor=WHITE, fontName="DV-B",
    alignment=TA_CENTER, spaceAfter=6, leading=26)

subtitle_style = S("Subtitle",
    fontSize=11, textColor=LIGHT_BLUE, fontName="DV",
    alignment=TA_CENTER, spaceAfter=4)

part_style = S("Part",
    fontSize=15, textColor=WHITE, fontName="DV-B",
    alignment=TA_LEFT, spaceAfter=4, leading=19)

h1 = S("H1", fontSize=12, textColor=DARK_BLUE, fontName="DV-B",
       spaceBefore=12, spaceAfter=4, leading=15)

h2 = S("H2", fontSize=10.5, textColor=MID_BLUE, fontName="DV-B",
       spaceBefore=8, spaceAfter=3, leading=13)

h3 = S("H3", fontSize=10, textColor=ORANGE, fontName="DV-B",
       spaceBefore=6, spaceAfter=2, leading=13)

body = S("Body", fontSize=9.5, textColor=BLACK, fontName="DV",
         spaceBefore=2, spaceAfter=3, leading=14, alignment=TA_JUSTIFY)

code_style = S("Code", fontSize=8.5, textColor=colors.HexColor("#2B2B2B"),
               fontName="DV-M", spaceBefore=2, spaceAfter=2,
               leading=13, leftIndent=10)

# ── Helpers ──────────────────────────────────────────────────────────────────
def sp(h=6): return Spacer(1, h)

def banner(text, bg=DARK_BLUE):
    t = Table([[Paragraph(text, part_style)]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
    ]))
    return t

def info_box(rows, bg=LIGHT_BLUE, label=None):
    content = []
    if label:
        content.append(Paragraph(label, h2))
    for r in rows:
        content.append(Paragraph("• " + r, body))
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
    rows = [[Paragraph(l, code_style)] for l in lines]
    t = Table(rows, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), YELLOW_BG),
        ("BOX",           (0,0), (-1,-1), 1, MID_BLUE),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
    ]))
    return t

def tbl(header, rows, col_widths=None):
    if col_widths is None:
        col_widths = [W / len(header)] * len(header)
    th_style = S("th", fontSize=9, fontName="DV-B", textColor=WHITE, leading=12)
    td_style = S("td", fontSize=9, fontName="DV", leading=13)
    data = [[Paragraph(h, th_style) for h in header]]
    for r in rows:
        data.append([Paragraph(str(c), td_style) for c in r])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  DARK_BLUE),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [WHITE, colors.HexColor("#EBF2FA")]),
        ("BOX",           (0,0), (-1,-1), 0.5, GREY_LINE),
        ("INNERGRID",     (0,0), (-1,-1), 0.3, GREY_LINE),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ]))
    return t

def pitfall_row(i, title, text):
    bg = RED_BG if i % 2 == 0 else colors.HexColor("#FFF0F0")
    title_s = S(f"pt{i}", fontSize=9.5, fontName="DV-B",
                textColor=colors.HexColor("#7B0000"), leading=13)
    row = [[Paragraph(f"{i}. {title}", title_s), Paragraph(text, body)]]
    t = Table(row, colWidths=[4.5*cm, W - 4.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("BOX",           (0,0), (-1,-1), 0.3, GREY_LINE),
        ("LINEAFTER",     (0,0), (0,-1), 0.5, colors.HexColor("#E0A0A0")),
    ]))
    return t

# ════════════════════════════════════════════════════════════════════════════
# CONTENT
# ════════════════════════════════════════════════════════════════════════════
story = []

# ── COVER ────────────────────────────────────────────────────────────────────
cover = Table(
    [[Paragraph("Statistics Exam\nMaster Guide", title_style)],
     [Paragraph("Multiple Linear Regression  &  Time Series", subtitle_style)],
     [Paragraph(
         "How to read questions · Which method to use · Why it works\n"
         "Common pitfalls · Different phrasings · Worked decision logic",
         subtitle_style)]],
    colWidths=[W]
)
cover.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), DARK_BLUE),
    ("TOPPADDING",    (0,0), (-1,-1), 28),
    ("BOTTOMPADDING", (0,0), (-1,-1), 18),
    ("LEFTPADDING",   (0,0), (-1,-1), 20),
    ("RIGHTPADDING",  (0,0), (-1,-1), 20),
]))
story += [sp(40), cover, sp(20)]
story.append(Paragraph(
    "This guide walks you through every type of question that appears in exams on "
    "Multiple Linear Regression (MLR) and Time Series. For each topic you will find: "
    "what the question is really asking, which method to choose and why, step-by-step "
    "decision logic, the correct interpretation, pitfalls that cost marks, and different "
    "phrasings that mean the same thing.",
    body))
story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
# PART 1 — MLR
# ════════════════════════════════════════════════════════════════════════════
story += [banner("PART 1 — MULTIPLE LINEAR REGRESSION (MLR)"), sp(8)]

# 1.1 Reading the question
story.append(Paragraph("1.1  How to Read an MLR Question", h1))
story.append(Paragraph("Before touching SPSS, read the question twice and identify:", body))
story.append(tbl(
    ["What to identify", "How it appears", "What you do"],
    [
        ["Dependent variable Y", '"Regress X on Y" / "explain Y" / "Y as a function of"', "Put in Dependent box"],
        ["Continuous predictors", "Age, income, price — no category labels", "Enter directly"],
        ["Categorical predictor", '"Region", "type", "group" with labels like North/South', "Create dummy variables (k−1)"],
        ["Log transformation", '"ln(X)", "log(X)" in variable name', "Variable already logged, or use Transform → Compute"],
        ["Interaction term", '"effect depends on Z", "moderating", "X×Z"', "Create product variable X×Z"],
    ],
    col_widths=[3.5*cm, 7.5*cm, 5.5*cm]
))
story.append(sp(8))

# 1.2 Dummy variables
story.append(Paragraph("1.2  Dummy Variables", h1))
story.append(Paragraph(
    "A dummy (indicator) variable is 0/1 and converts a categorical variable with "
    "k categories into k−1 binary variables. The omitted category is the reference group — "
    "all coefficient interpretations are made relative to it.", body))
story.append(Paragraph("Rule:  k categories  →  create k−1 dummies", h2))
story.append(tbl(
    ["Categories", "Dummies to create", "Reference (omitted)"],
    [
        ["North, South, Center, East (4 groups)", "D_North, D_South, D_East  (3 dummies)", "Center"],
        ["Male, Female (2 groups)", "D_Female  (1 dummy)", "Male"],
        ["Low, Medium, High (3 groups)", "D_Medium, D_High  (2 dummies)", "Low"],
    ],
    col_widths=[5*cm, 6.5*cm, 5*cm]
))
story.append(sp(4))
story.append(Paragraph("In SPSS:  Transform → Compute Variable", h2))
story.append(formula_box([
    "D_North = (Region = 1)    [if North is coded 1 in the data]",
    "D_South = (Region = 2)",
    "D_East  = (Region = 4)    [skip 3 = Center → it is the reference]",
    "",
    "Theoretical model:",
    "Y = β₀ + β₁X₁ + β₂·D_North + β₃·D_South + β₄·D_East + ε",
    "",
    "Interpretation of β₂:  On average, North regions have β₂ units MORE Y",
    "                        than Center regions, holding all else constant.",
]))
story.append(sp(4))
story.append(pitfall_box([
    "Never create k dummies — always k−1. Including all k causes perfect multicollinearity "
    "(dummy trap). Always omit one reference category.",
    '"Baseline group", "comparison group", "omitted category", "reference category" — '
    "all mean the same thing.",
    'The question may say "use Center as reference" — that means do NOT create a dummy for Center.',
]))
story.append(sp(8))

# 1.3 Log transformations
story.append(Paragraph("1.3  Log Transformations and Interpretation", h1))
story.append(tbl(
    ["Model type", "Equation", "Interpretation of β"],
    [
        ["Linear (standard)", "Y = α + βX + ε", "1-unit rise in X  →  β unit change in Y"],
        ["Linear-log", "Y = α + β·ln(X) + ε", "1% rise in X  →  β/100 unit change in Y"],
        ["Log-linear", "ln(Y) = α + βX + ε", "1-unit rise in X  →  β×100 % change in Y"],
        ["Log-log (elasticity)", "ln(Y) = α + β·ln(X) + ε", "1% rise in X  →  β% change in Y"],
    ],
    col_widths=[3.5*cm, 6*cm, 7*cm]
))
story.append(sp(4))
story.append(info_box([
    "Most common exam type: Linear-log.  Y = α + β·ln(X) + ε",
    "Example: β = −16.04, X is ln(NOx).",
    "Answer: 1% increase in NOx → −16.04/100 = −0.16 unit change in Y.",
    "If Y is measured in thousands of dollars: −$160 per 1% increase in NOx.",
    "Watch for 'ln(X)' or 'log(X)' in the variable name in SPSS output.",
], bg=LIGHT_BLUE, label="Linear-Log: Most Tested Type"))
story.append(sp(8))

# 1.4 Coefficient interpretation tree
story.append(Paragraph("1.4  Interpreting Coefficients — Decision Table", h1))
story.append(tbl(
    ["Is X logged?", "Is Y logged?", "Interpretation of β"],
    [
        ["No", "No", "1 extra unit of X → β extra units of Y  (ceteris paribus)"],
        ["Yes — ln(X)", "No", "1% extra in X → β/100 extra units of Y"],
        ["No", "Yes — ln(Y)", "1 extra unit of X → β×100 % change in Y"],
        ["Yes — ln(X)", "Yes — ln(Y)", "1% extra in X → β% change in Y  (elasticity)"],
        ["Dummy (0/1)", "No", "Being in group D → β extra units of Y vs. reference group"],
    ],
    col_widths=[2.5*cm, 2.5*cm, 11.5*cm]
))
story.append(sp(8))

# 1.5 Individual significance
story.append(Paragraph("1.5  Testing Individual Coefficient Significance", h1))
story.append(formula_box([
    "H₀: β = 0   (variable has no effect on Y)",
    "H₁: β ≠ 0   (variable does affect Y)",
    "",
    "Decision:  p-value (Sig. column) < 0.05  →  Reject H₀  →  significant at 5%",
    "           p-value ≥ 0.05               →  Fail to reject H₀  →  not significant",
]))
story.append(sp(4))
story.append(pitfall_box([
    '"Significant" means statistically distinguishable from zero — not necessarily large or important.',
    '"Is X relevant?", "Does X matter?", "Is β significantly different from zero?", '
    '"Test the effect of X" — all ask for the t-test and p-value.',
]))
story.append(sp(8))

# 1.6 Joint F-test
story.append(Paragraph("1.6  Joint F-test — Testing a Group of Variables Together", h1))
story.append(Paragraph(
    "Use the joint F-test when the question asks whether a GROUP of variables "
    "is significant together, not just one at a time.", body))
story.append(info_box([
    '"Are the region dummies jointly significant?"',
    '"Do the seasonal dummies together improve the model?"',
    '"Test whether D₁, D₂, D₃ together add explanatory power."',
    '"Is the set of interaction terms significant?"',
    "Any question testing MORE THAN ONE variable simultaneously.",
], bg=LIGHT_BLUE, label="Trigger phrases — use joint F-test when you see these"))
story.append(sp(4))
story.append(tbl(
    ["Step", "What you do", "Why"],
    [
        ["1", "Run UNRESTRICTED model — all variables included", "Gives SSE_u and R²_u"],
        ["2", "Run RESTRICTED model — remove the variables being tested", "Gives SSE_r and R²_r"],
        ["3", "J = number of variables removed", "J = numerator degrees of freedom"],
        ["4", "Read n (observations) and k (predictors in unrestricted model)", "For denominator df"],
        ["5", "Compute F and compare to p-value", "Decision"],
    ],
    col_widths=[1*cm, 8.5*cm, 7*cm]
))
story.append(sp(4))
story.append(formula_box([
    "Option A  (using SSE from ANOVA tables):",
    "  F = [ (SSE_r − SSE_u) / J ]  ÷  [ SSE_u / (n − k − 1) ]",
    "",
    "Option B  (using R² from Model Summary):",
    "  F = [ (R²_u − R²_r) / J ]  ÷  [ (1 − R²_u) / (n − k − 1) ]",
    "",
    "Decision:  Use the p-value (Sig.) from SPSS ANOVA table if available.",
    "           Or compare your computed F to the critical value from the F-table.",
]))
story.append(sp(4))
story.append(pitfall_box([
    "J = number of RESTRICTIONS (variables removed), not total variables in model.",
    "Restricted model has FEWER variables — its SSE is always LARGER.",
    "n−k−1 uses k from the UNRESTRICTED model.",
    '"Test if dummies are jointly significant" = run restricted model WITHOUT those dummies.',
]))
story.append(sp(8))

# 1.7 Residual analysis
story.append(Paragraph("1.7  Residual Plot Analysis", h1))
story.append(tbl(
    ["Problem", "What you see in the plot", "Assumption violated"],
    [
        ["Heteroskedasticity",
         "Spread of residuals grows or shrinks — fan shape (wider on one side)",
         "A2: Var(ε) = σ²  (constant variance)"],
        ["Non-linearity",
         "Residuals curve upward or downward — systematic arc pattern",
         "A1: model correctly specified (linearity)"],
        ["Outliers",
         "One or a few points far above/below the rest",
         "Distort estimates — identify and report"],
    ],
    col_widths=[3.5*cm, 7*cm, 6*cm]
))
story.append(sp(4))
story.append(info_box([
    "Good residual plot: random cloud of points centred near zero. No pattern, no fan, no curve.",
    "Bad residual plot: any systematic shape — V-shape, cone/fan, curve, or large isolated points.",
    "You do NOT need to quantify — describe what you SEE and name the assumption violated.",
], bg=LIGHT_GREEN, label="Good vs. Bad Residual Plot"))
story.append(sp(4))
story.append(pitfall_box([
    "Do not say 'residuals are not normal' from a residual-vs-fitted plot alone. "
    "Normality requires a histogram or Q-Q plot.",
    "Heteroskedasticity → standard errors are wrong → t-tests and p-values are unreliable. "
    "This is why we follow up with the White test.",
]))
story.append(sp(8))

# 1.8 White test
story.append(Paragraph("1.8  The White Test for Heteroskedasticity", h1))
story.append(formula_box([
    "H₀: homoskedasticity  —  Var(ε) = σ²  (constant)",
    "H₁: heteroskedasticity  —  variance is NOT constant",
    "",
    "Step 1:  Run original model. Save residuals ê  (Save → Unstandardized Residuals).",
    "Step 2:  Create ê²  via Transform → Compute Variable: RES_SQ = RES_1 ** 2",
    "Step 3:  Run auxiliary regression:",
    "         ê² = α₀ + (all original X's) + (X² for each continuous X)",
    "                  + (Xᵢ × Xⱼ for each pair of continuous X's) + u",
    "         Do NOT square dummies.  Do NOT include dummy × dummy terms.",
    "Step 4:  W = n × R²_aux  ~  χ²(df)",
    "         df = number of regressors in auxiliary regression (excluding constant)",
    "Step 5:  If W > critical value  OR  p < 0.05  →  Reject H₀  →  heteroskedasticity",
]))
story.append(sp(4))
story.append(pitfall_box([
    "The df for the White test is NOT 1. Count all terms in the auxiliary regression: "
    "original X's + squared continuous X's + cross-products.",
    "Example with 2 continuous X's: X₁, X₂, X₁², X₂², X₁×X₂ → df = 5.",
    "Dummies: D² = D for a 0/1 variable, so squaring adds nothing. Exclude them.",
    "Always state df in your answer: W ~ χ²(5). Different questions have different df.",
]))
story.append(sp(8))

# 1.9 Omitted variable bias
story.append(Paragraph("1.9  Omitted Variable Bias", h1))
story.append(Paragraph(
    "If a relevant variable Z is left out of the model, the estimated coefficient "
    "on the included variable X will be biased. The direction of the bias:", body))
story.append(formula_box([
    "sign(bias on β̂_X)  =  sign(β_Z)  ×  sign(r(X, Z))",
    "",
    "β_Z  = true effect of omitted variable Z on Y",
    "r(X, Z) = correlation between included X and omitted Z",
    "",
    "Bias > 0  →  estimate is TOO HIGH  (upward bias)",
    "Bias < 0  →  estimate is TOO LOW   (downward bias)",
]))
story.append(sp(4))
story.append(tbl(
    ["β_Z (effect of Z on Y)", "r(X, Z) (correlation with X)", "Bias on β̂_X", "Estimate is..."],
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
    "Worked example: estimating effect of ln(NOx) on housing values, omitting Indus (industry).",
    "β_Indus < 0  (more industry → lower house values).",
    "r(ln(NOx), Indus) > 0  (areas with high NOx also tend to have more industry).",
    "Bias = (−) × (+) = negative → estimate of β_lnNOx is TOO LOW (overestimates the negative effect).",
], bg=LIGHT_BLUE, label="Worked Example"))
story.append(sp(4))
story.append(pitfall_box([
    '"Biased downward" means the estimate is too small (too negative for a negative coefficient).',
    "If the correlation is not given directly, reason from context: "
    "do areas with high NOx tend to also have more industry? If yes, correlation is positive.",
    '"Omitted variable bias" and "specification error" mean the same thing.',
]))
story.append(sp(8))

# 1.10 VIF
story.append(Paragraph("1.10  VIF and Multicollinearity", h1))
story.append(formula_box([
    "VIF_j  =  1 / (1 − R²_j)",
    "Tolerance_j  =  1 − R²_j  =  1 / VIF_j",
    "",
    "R²_j = R² from regressing X_j on all other X's  (auxiliary regression)",
    "",
    "Rule of thumb:  VIF > 5   →  concerning multicollinearity",
    "                VIF > 10  →  severe multicollinearity",
    "                Tolerance < 0.20  →  concerning",
]))
story.append(sp(4))
story.append(tbl(
    ["VIF", "Tolerance", "Interpretation"],
    [
        ["1.0", "1.00", "No multicollinearity — X is uncorrelated with all other X's"],
        ["1 to 5", "0.20 to 1.00", "Acceptable — moderate correlation, no real problem"],
        ["5 to 10", "0.10 to 0.20", "Concerning — check estimates carefully"],
        ["> 10", "< 0.10", "Severe — coefficient estimates are unreliable"],
    ],
    col_widths=[2.5*cm, 3.5*cm, 10.5*cm]
))
story.append(sp(4))
story.append(info_box([
    "In SPSS: Analyze → Regression → Linear → Statistics → tick Collinearity diagnostics.",
    "VIF and Tolerance appear in the Coefficients table.",
    "If asked to compute VIF manually: run auxiliary regression of X_j on all other X's, "
    "read R², compute VIF = 1/(1 − R²).",
], bg=LIGHT_BLUE))
story.append(sp(8))

# 1.11 Quick reference
story.append(KeepTogether([
    Paragraph("1.11  Quick Reference — Question Phrasing → Method", h1),
    tbl(
        ["If the question says…", "It means…", "Method"],
        [
            ['"Interpret the coefficient of ln(X)"', "Effect of 1% change in X", "β/100 units change in Y"],
            ['"Test if Region is significant"', "All region dummies jointly", "Joint F-test"],
            ['"Is β₂ significantly different from zero?"', "Individual significance", "p-value from Coefficients table"],
            ['"Test for heteroskedasticity"', "Unequal error variance", "White test: W = n × R²_aux"],
            ['"What is the bias if Z is omitted?"', "Direction of bias", "sign(β_Z) × sign(r(X, Z))"],
            ['"What is the reference category?"', "Omitted dummy group", "State which group has no dummy"],
            ['"VIF = 2.5 — what does this mean?"', "Multicollinearity severity", "Compare to threshold of 5"],
            ['"Write the theoretical model"', "Full symbolic equation", "Y = β₀ + β₁X₁ + β₂D₁ + …"],
        ],
        col_widths=[5.5*cm, 4.5*cm, 6.5*cm]
    ),
]))
story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
# PART 2 — TIME SERIES
# ════════════════════════════════════════════════════════════════════════════
story += [banner("PART 2 — TIME SERIES REGRESSION"), sp(8)]

# 2.1 Framework
story.append(Paragraph("2.1  The Three-Step Framework — Always in This Order", h1))
story.append(info_box([
    "STEP 1 — STATIONARITY: Run the Dickey-Fuller test on every variable. "
    "Non-stationary series must be differenced before use.",
    "STEP 2 — FIT THE MODEL: Choose static, DL(q), or AR(1). "
    "For DL(q) use top-down lag selection.",
    "STEP 3 — CHECK AUTOCORRELATION: Run the LMSC test on the model residuals.",
], bg=LIGHT_BLUE, label="The Three-Step Framework — never skip or reorder these"))
story.append(sp(4))
story.append(pitfall_box([
    "You cannot skip Step 1. Using non-stationary series produces spurious results: "
    "high R² and significant t-values that have no real meaning.",
    "Steps must go in order: stationarity → fit → check. Never fit first.",
]))
story.append(sp(8))

# 2.2 Dickey-Fuller
story.append(Paragraph("2.2  Step 1 — Stationarity: The Dickey-Fuller Test", h1))
story.append(Paragraph(
    "A stationary series has a constant mean and variance. "
    "A non-stationary series drifts — its mean changes over time. "
    "The Dickey-Fuller (DF) test formally tests whether a unit root is present.", body))
story.append(Paragraph("Choose DF Version 1 or Version 2:", h2))
story.append(tbl(
    ["Version", "Regression run", "When to use"],
    [
        ["Version 1 — no trend",
         "ΔY_t = α₀ + α₁Y_{t−1} + ε_t",
         "Time plot shows NO visible upward or downward trend"],
        ["Version 2 — with trend",
         "ΔY_t = α₀ + λt + α₁Y_{t−1} + ε_t",
         "Time plot shows a clear trend  OR  when unsure  (safer default)"],
    ],
    col_widths=[3.5*cm, 6.5*cm, 6.5*cm]
))
story.append(sp(4))
story.append(formula_box([
    "H₀: α₁ = 0   (unit root — series is NON-STATIONARY)",
    "H₁: α₁ < 0   (series IS stationary)        ← one-sided test",
    "",
    "Special critical values at 5%  (NOT the standard t-table):",
    "  Version 1  (no trend):    −2.86",
    "  Version 2  (with trend):  −3.41",
    "",
    "Decision:  t on Y_{t−1} more negative than critical value  →  Reject H₀  →  STATIONARY",
    "           t on Y_{t−1} less negative (closer to 0)        →  Fail to reject  →  UNIT ROOT",
    "",
    "Example A:  t = −1.64,  critical = −3.41",
    "  −1.64 > −3.41  →  fail to reject H₀  →  NON-STATIONARY  →  take first differences",
    "",
    "Example B:  t = −4.20,  critical = −3.41",
    "  −4.20 < −3.41  →  reject H₀  →  STATIONARY  →  use in levels",
]))
story.append(sp(4))
story.append(tbl(
    ["DF result", "Action", "Next step"],
    [
        ["Stationary  (reject H₀)", "Use series in levels", "Proceed to fit model"],
        ["Non-stationary  (fail to reject)", "Take ΔY = Y_t − Y_{t−1}", "Run DF again on ΔY"],
        ["ΔY is stationary  (reject H₀)", "Series is I(1) — use first differences", "Proceed to fit model"],
        ["ΔY still non-stationary", "Rare — take second differences", "Series may be I(2)"],
    ],
    col_widths=[4.5*cm, 5*cm, 7*cm]
))
story.append(sp(4))
story.append(pitfall_box([
    "NEVER use the standard t-table (±1.96) for the DF test. The DF distribution is "
    "non-standard. Always use −2.86 (V1) or −3.41 (V2) at 5%.",
    "The p-value SPSS shows for the LAG variable uses the wrong distribution — ignore it. "
    "Compare the t-statistic directly to the special critical value.",
    "Rejecting H₀ in the DF test means the series IS stationary — opposite of most tests.",
    "The DF test is one-sided: you only reject when the t-statistic is sufficiently NEGATIVE.",
]))
story.append(sp(8))

# 2.3 Model selection
story.append(Paragraph("2.3  Step 2 — Which Model to Fit?", h1))
story.append(tbl(
    ["Model", "Equation", "When to use"],
    [
        ["Static", "Y_t = α + βX_t + ε_t",
         "Question specifies it, or top-down DL gives q = 0"],
        ["DL(q) — Distributed Lag",
         "Y_t = α + β₀X_t + β₁X_{t−1} + … + βqX_{t−q} + ε_t",
         "Question asks for DL; effects of X are delayed"],
        ["AR(1) — Autoregressive",
         "Y_t = α + βX_t + γY_{t−1} + ε_t",
         "Question specifies AR(1); autocorrelation found in DL residuals"],
    ],
    col_widths=[2.5*cm, 7*cm, 7*cm]
))
story.append(sp(8))

# 2.4 DL top-down
story.append(Paragraph("2.4  DL(q) — Top-Down Lag Selection", h1))
story.append(formula_box([
    "Setup in SPSS — create lag variables via Transform → Compute Variable:",
    "  LAG1_X = LAG(X, 1)    LAG2_X = LAG(X, 2)    LAG3_X = LAG(X, 3)",
    "",
    "Top-down procedure:",
    "  1. Fit DL(q_max).  Look at p-value of the HIGHEST lag (LAgq_X).",
    "  2. If p > 0.05:  not significant  →  drop it  →  fit DL(q−1).",
    "  3. If p ≤ 0.05:  significant  →  STOP.  Current q is optimal.",
    "  4. Repeat until highest remaining lag is significant.",
    "",
    "IMPORTANT:  Never drop an intermediate lag.",
    "  If lag 2 is significant but lag 1 is not  →  keep BOTH.",
    "  You cannot have lag 2 without lag 1 in the model.",
    "",
    "Total multiplier  =  β₀ + β₁ + β₂ + … + βq",
    "  = long-run effect of a permanent 1-unit increase in X",
    "",
    "Immediate effect (impact multiplier)  =  β₀  only",
]))
story.append(sp(4))
story.append(pitfall_box([
    "q_max is usually given in the question. If not, 3 or 4 is a common default.",
    "Each lag costs one observation. DL(3) with n = 100 gives only 97 usable rows.",
    '"Optimal lag length", "best DL model", "chosen q" — all mean the same thing.',
    "Do not confuse total multiplier (long-run, sum of all β) with β₀ (immediate effect only).",
]))
story.append(sp(8))

# 2.5 AR(1)
story.append(Paragraph("2.5  AR(1) — Autoregressive Model", h1))
story.append(formula_box([
    "Model:  Y_t = α + βX_t + γY_{t−1} + ε_t",
    "",
    "β  =  immediate effect: 1-unit rise in X_t raises Y_t by β, holding Y_{t−1} fixed",
    "γ  =  persistence: how much of last period's Y carries into this period",
    "      Requires |γ| < 1 for the model to be valid",
    "",
    "Total multiplier  =  β / (1 − γ)",
    "  = long-run effect of a permanent 1-unit increase in X",
    "",
    "Example:  β = −0.031,  γ = 0.52",
    "  Total multiplier = −0.031 / (1 − 0.52) = −0.031 / 0.48 = −0.065",
]))
story.append(sp(4))
story.append(pitfall_box([
    "AR(1) with remaining autocorrelation → coefficient estimates are BIASED. "
    "DL with autocorrelation → only INEFFICIENT (standard errors wrong, but β's still correct). "
    "This is why always run LMSC after fitting AR(1).",
    "γ must be strictly between −1 and +1. If |γ| ≥ 1 the series is non-stationary.",
    '"Persistence coefficient", "coefficient on lagged Y", "AR coefficient" — all refer to γ.',
]))
story.append(sp(8))

# 2.6 LMSC
story.append(Paragraph("2.6  Step 3 — LMSC Autocorrelation Test", h1))
story.append(formula_box([
    "H₀: ρ = 0   (no autocorrelation — A3 satisfied)",
    "H₁: ρ ≠ 0   (autocorrelation present — A3 violated)",
    "",
    "Step 1:  Fit original model. Save residuals: Save → Unstandardized Residuals → RES_1",
    "Step 2:  Create lagged residual: Transform → Compute → LAG_RES1 = LAG(RES_1, 1)",
    "Step 3:  Run auxiliary regression:",
    "         Dependent = RES_1",
    "         Independent = ALL original X's  +  LAG_RES1",
    "Step 4:  From Model Summary: read R²_aux",
    "         From ANOVA table:  n_aux = Total df + 1",
    "Step 5:  LM = n_aux × R²_aux   ~   χ²(1)   under H₀",
    "         Critical value at 5%:  3.841",
    "         If LM > 3.841  (or p < 0.05)  →  Reject H₀  →  autocorrelation present",
    "         If LM ≤ 3.841  (or p ≥ 0.05)  →  Fail to reject  →  A3 plausibly satisfied",
]))
story.append(sp(4))
story.append(pitfall_box([
    "The auxiliary regression MUST include ALL original X predictors, not just the lagged residual.",
    "For DL(q): auxiliary regression includes all original X's AND all lagged X's from the DL model, "
    "plus LAG_RES1.",
    '"Test for autocorrelation", "check A3", "Breusch-Godfrey test", "LMSC test" — all the same.',
    "Durbin-Watson (DW) is INVALID when Y_{t−1} appears in the model. Always use LMSC.",
]))
story.append(sp(8))

# 2.7 Opposites grid
story.append(Paragraph("2.7  Critical Pitfall Grid — Rejecting H₀ Means Opposite Things!", h1))
story.append(tbl(
    ["Test", "H₀ means…", "Reject H₀ means…", "Fail to reject means…"],
    [
        ["Dickey-Fuller",
         "Series HAS unit root  (NON-STATIONARY)",
         "Series IS stationary ✓",
         "Non-stationary — difference it"],
        ["LMSC",
         "NO autocorrelation  (A3 satisfied)",
         "Autocorrelation IS present — fix model",
         "A3 plausibly satisfied ✓"],
        ["Individual t-test",
         "β = 0  (variable has NO effect)",
         "Variable DOES have a significant effect",
         "Cannot conclude variable matters"],
        ["Joint F-test",
         "All tested β = 0  (group has NO effect)",
         "Group jointly significant",
         "Cannot conclude group matters"],
        ["White test",
         "Homoskedasticity  (A2 satisfied)",
         "Heteroskedasticity present — A2 violated",
         "A2 plausibly satisfied ✓"],
    ],
    col_widths=[3*cm, 4*cm, 4.5*cm, 5*cm]
))
story.append(sp(8))

# 2.8 Deterministic vs stochastic
story.append(Paragraph("2.8  Deterministic vs. Stochastic Trends — Different Fix!", h1))
story.append(tbl(
    ["Feature", "Deterministic trend", "Stochastic trend (unit root)"],
    [
        ["Mathematical source", "λt term — mean grows linearly", "ρ = 1 — each shock is permanent"],
        ["Pattern in time plot", "Smooth, predictable upward drift", "Erratic, wanders unpredictably"],
        ["Variance over time", "Constant", "Grows without bound"],
        ["After a shock", "Series returns to the trend line", "Series NEVER recovers"],
        ["Correct fix", "Add t (time) as regressor", "Take first differences ΔY"],
        ["Wrong fix → consequence",
         "First-differencing creates artificial negative autocorrelation",
         "Detrending does not remove a random walk"],
    ],
    col_widths=[3.5*cm, 6*cm, 7*cm]
))
story.append(sp(4))
story.append(info_box([
    "How to distinguish: look at the DF test result.",
    "DF fails to reject H₀ (unit root confirmed)  →  stochastic trend  →  take differences.",
    "DF rejects H₀ (stationary) but time plot still shows a trend  →  deterministic trend  →  add t.",
], bg=LIGHT_BLUE, label="Decision rule: deterministic vs. stochastic"))
story.append(sp(8))

# 2.9 Phrasings
story.append(Paragraph("2.9  Time Series — Question Phrasings Reference", h1))
story.append(tbl(
    ["If the question says…", "It means…", "Method"],
    [
        ['"Is the series stationary?"', "Does it have a unit root?", "Dickey-Fuller test"],
        ['"Test for a unit root"', "Is ρ = 1?", "Dickey-Fuller test"],
        ['"Levels or differences?"', "What is the stationarity property?", "Run DF, then decide"],
        ['"Determine optimal lag length"', "What is the best q for DL(q)?", "Top-down procedure"],
        ['"Long-run effect of X on Y"', "Total multiplier", "DL: Σβk  |  AR: β/(1−γ)"],
        ['"Immediate effect of X on Y"', "Impact multiplier (current period only)", "β₀ — coefficient on X_t only"],
        ['"Test for autocorrelation"', "Is A3 violated?", "LMSC test:  LM = n × R²_aux"],
        ['"Is the model well-specified?"', "Check all assumptions including A3", "LMSC + residual plot"],
        ['"Series is I(1)"', "Non-stationary in levels, stationary in differences", "Use first differences"],
        ['"Spurious regression risk"', "Non-stationary series used in levels", "Run DF first, then decide"],
        ['"Disturbance term carries memory"', "Autocorrelation is present", "LMSC test"],
    ],
    col_widths=[5.5*cm, 4.5*cm, 6.5*cm]
))
story.append(sp(8))

# 2.10 SPSS workflow
story.append(KeepTogether([
    Paragraph("2.10  SPSS Step-by-Step Workflow", h1),
    tbl(
        ["Step", "SPSS action", "Record"],
        [
            ["1a. Plot", "Graphs → Chart Builder → Line → drag variable and TIME to axes",
             "Does it trend? Wander?"],
            ["1b. DF on levels",
             "Compute DIFF_Y = Y − LAG(Y,1) and LAG_Y = LAG(Y,1).\n"
             "Regression: DV = DIFF_Y,  IV = LAG_Y  [+ TIME for Version 2]",
             "t on LAG_Y. Compare to −2.86/−3.41"],
            ["1c. DF on differences  (if unit root found)",
             "Compute DIFF2_Y = DIFF_Y − LAG(DIFF_Y,1) and LAG_DIFFY = LAG(DIFF_Y,1).\n"
             "Regression: DV = DIFF2_Y,  IV = LAG_DIFFY  [+ TIME for V2]",
             "t on LAG_DIFFY. Compare to −2.86/−3.41"],
            ["2a. Lag variables",
             "Transform → Compute:  LAG1_X = LAG(X,1),  LAG2_X = LAG(X,2), etc.",
             "Note observations lost"],
            ["2b. Fit model", "Regression with chosen variables (static / DL / AR)",
             "All β, R², n"],
            ["3a. Save residuals", "Regression dialog → Save → Unstandardized Residuals",
             "Variable RES_1 created"],
            ["3b. Lag residual", "Transform → Compute:  LAG_RES1 = LAG(RES_1, 1)",
             "Variable LAG_RES1 created"],
            ["3c. Auxiliary regression",
             "Regression: DV = RES_1,  IV = all original X's + LAG_RES1",
             "R² and n from Model Summary + ANOVA"],
            ["3d. LMSC",
             "LM = n_aux × R²_aux.  n_aux = Total df + 1 from ANOVA",
             "Compare to 3.841. State conclusion."],
        ],
        col_widths=[2.2*cm, 9*cm, 5.3*cm]
    ),
]))
story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
# PART 3 — MASTER PITFALL LIST
# ════════════════════════════════════════════════════════════════════════════
story += [banner("PART 3 — MASTER PITFALL & TRICK PHRASING LIST", bg=ORANGE), sp(8)]

story.append(Paragraph("3.1  The Top 15 Mistakes — and How to Avoid Them", h1))
pitfalls = [
    ("Using p-value for DF test",
     "SPSS's Sig. for the LAG variable uses the wrong distribution. "
     "Always compare the t-statistic directly to −2.86 (V1) or −3.41 (V2). Never use the p-value."),
    ("Reject H₀ in DF = non-stationary",
     "It is the OPPOSITE: rejecting H₀ in the DF test means the series IS stationary. "
     "H₀ is the unit root (non-stationarity)."),
    ("Creating k dummies instead of k−1",
     "For k categories, create exactly k−1 dummies. Including all k causes the dummy trap "
     "(perfect multicollinearity). Always omit one reference category."),
    ("Using standard t-table for DF",
     "The DF t-statistic does not follow a standard t-distribution. "
     "Values like ±1.96 do not apply. Use −2.86 or −3.41 only."),
    ("Missing X's in LMSC auxiliary regression",
     "The LMSC auxiliary regression regresses residuals on ALL original X's PLUS the "
     "lagged residual. Missing any original X gives the wrong R² and wrong LM."),
    ("Total multiplier = β₀ only",
     "DL(q): total multiplier = β₀ + β₁ + … + βq (ALL lag coefficients). "
     "AR(1): total multiplier = β/(1−γ). β₀ alone is only the immediate effect."),
    ("Using DW for AR(1) models",
     "Durbin-Watson is INVALID when Y_{t−1} appears as a regressor. "
     "Always use the LMSC test."),
    ("Differencing when trend is deterministic",
     "Only difference when DF confirms a unit root (ρ = 1). "
     "If the trend is deterministic (|ρ| < 1, λ ≠ 0), add t as a regressor instead. "
     "Differencing a deterministic trend creates artificial negative autocorrelation."),
    ("Dropping intermediate insignificant lags",
     "In top-down selection, only drop the HIGHEST lag while insignificant. "
     "Never drop lag 1 while keeping lag 2 — the lag structure must be contiguous."),
    ("Squaring dummies in the White test",
     "D² = D for a 0/1 variable, so squaring dummies adds nothing. "
     "Only square continuous variables. Exclude dummy × dummy cross-products too."),
    ("Confusing significant with large",
     "A coefficient can be statistically significant (p < 0.05) but economically negligible. "
     "Always comment on both significance AND the size/direction of the effect."),
    ("Wrong sign for omitted variable bias",
     "Bias = sign(β_Z) × sign(r(X, Z)). "
     "Two negatives give positive bias (upward). Draw a sign table if in doubt."),
    ("Ignoring reference category in interpretation",
     'The coefficient on D_North means "compared to the reference group". '
     "Always state the reference category explicitly in your interpretation."),
    ("Using levels when both series are I(1)",
     "If both Y and X are non-stationary I(1) series, use first differences "
     "(unless cointegration is established — not typically covered at introductory level)."),
    ("Wrong n in LM formula",
     "The auxiliary regression loses one observation for the lagged residual. "
     "Use n_aux = n − 1, or read from the ANOVA table: n_aux = Total df + 1."),
]
for i, (title, text) in enumerate(pitfalls, 1):
    story.append(pitfall_row(i, title, text))
    story.append(sp(3))

story.append(sp(10))

# 3.2 Trick phrasings
story.append(Paragraph("3.2  Trick Phrasings — Same Question, Different Words", h1))
story.append(tbl(
    ["What the question writes", "What it actually means"],
    [
        ['"Is X relevant to explaining Y?"',
         '"Is β_X significantly different from zero?"  →  p-value test'],
        ['"Does adding Region improve the model?"',
         '"Are the region dummies jointly significant?"  →  joint F-test'],
        ['"Baseline group" / "comparison group"',
         '"Reference category" — the omitted dummy group'],
        ['"The disturbance term carries memory"',
         '"There is autocorrelation"  →  LMSC test'],
        ['"Series wanders without returning to its mean"',
         '"Series has a unit root"  →  DF test, then first differences'],
        ['"Spurious correlation risk"',
         '"Series is non-stationary"  →  run DF before modelling'],
        ['"Long-run equilibrium effect"',
         '"Total multiplier"  →  Σβk  or  β/(1−γ)'],
        ['"Impact effect of a price shock"',
         '"Immediate effect"  →  β₀ only  (coefficient on current X)'],
        ['"Error variance is not constant"',
         '"Heteroskedasticity"  →  White test'],
        ['"Predictors are too correlated"',
         '"Multicollinearity"  →  VIF and Tolerance'],
        ['"Coefficient on lagged Y is 0.7"',
         '"γ = 0.7 in AR(1)"  →  total multiplier = β/(1−0.7) = β/0.3'],
        ['"Series is integrated of order one"',
         '"I(1) — unit root in levels, stationary in first differences"'],
        ['"Misspecification bias"',
         '"Omitted variable bias"  →  sign(β_Z) × sign(r(X, Z))'],
        ['"First-order autocorrelation"',
         '"ε_t = ρε_{t−1} + u_t"  →  run LMSC test'],
    ],
    col_widths=[7.5*cm, 9*cm]
))
story.append(sp(10))

# Quick decision guide
story += [banner("QUICK DECISION GUIDE", bg=GREEN), sp(8)]

story.append(Paragraph("MLR — Method Selector", h1))
story.append(tbl(
    ["Question type", "Method", "Key formula / output"],
    [
        ["Interpret coeff. of ln(X)", "Linear-log rule", "β/100 units per 1% rise in X"],
        ["Test one coefficient", "Individual t-test", "p-value (Sig.) in Coefficients table"],
        ["Test a group of variables", "Joint F-test", "F = [(SSE_r−SSE_u)/J] / [SSE_u/(n−k−1)]"],
        ["Check equal error variance", "White test", "W = n × R²_aux  ~  χ²(df)"],
        ["Direction of missing-variable distortion", "Omitted variable bias", "sign(β_Z) × sign(r(X,Z))"],
        ["Predictor correlation severity", "VIF / Tolerance", "VIF = 1/(1−R²_aux),  threshold = 5"],
        ["Write equation with categories", "Dummy variables", "k−1 dummies, state reference group"],
    ],
    col_widths=[5*cm, 4*cm, 7.5*cm]
))
story.append(sp(8))

story.append(Paragraph("Time Series — Method Selector", h1))
story.append(tbl(
    ["Question type", "Method", "Key output / decision"],
    [
        ["Is series stationary?", "Dickey-Fuller test", "t < −2.86 (V1) or −3.41 (V2)  →  stationary"],
        ["Series drifts with time", "DF test → unit root?", "Unit root confirmed  →  difference it.  No unit root  →  add t"],
        ["Choose number of lags", "Top-down DL selection", "Drop highest lag while p > 0.05"],
        ["Long-run effect of X on Y", "Total multiplier", "DL: Σβk        AR: β/(1−γ)"],
        ["Immediate effect of X on Y", "Impact multiplier", "β₀ — coefficient on current X_t only"],
        ["Check for autocorrelation", "LMSC test", "LM = n × R²_aux.  Compare to 3.841"],
        ["Model contains Y_{t−1}", "Use LMSC, not DW", "DW is invalid for AR models"],
    ],
    col_widths=[5*cm, 4*cm, 7.5*cm]
))
story.append(sp(10))

story.append(tip_box([
    "Always state H₀ and H₁ before every test — even when they seem obvious.",
    "Always write a full conclusion sentence: 'Since p = X < 0.05, we reject H₀ and conclude…'",
    "For DF: compare t-statistic (NOT p-value) to special critical value −2.86 or −3.41.",
    "For LMSC and White test: use p-value directly (standard χ² distribution applies).",
    "For individual t-tests and F-tests in regression: use p-value from SPSS output.",
    "When unsure about stationarity: use DF Version 2 (with trend) — it is the safer default.",
    "Total multiplier always refers to the LONG-RUN effect after a PERMANENT change in X.",
]))

doc.build(story)
print("PDF created successfully.")
