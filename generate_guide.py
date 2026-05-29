from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether, Preformatted
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import ListFlowable, ListItem

PAGE_W, PAGE_H = A4
MARGIN = 2.2 * cm

def build_styles():
    base = getSampleStyleSheet()
    styles = {}

    styles['title'] = ParagraphStyle('title', parent=base['Title'],
        fontSize=14, fontName='Helvetica-Bold', spaceAfter=4,
        alignment=TA_CENTER)

    styles['h1'] = ParagraphStyle('h1', parent=base['Heading1'],
        fontSize=12, fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=4,
        textColor=colors.HexColor('#1a1a1a'))

    styles['h2'] = ParagraphStyle('h2', parent=base['Heading2'],
        fontSize=11, fontName='Helvetica-Bold', spaceBefore=10, spaceAfter=3,
        textColor=colors.HexColor('#1a1a1a'))

    styles['h3'] = ParagraphStyle('h3', parent=base['Heading3'],
        fontSize=10, fontName='Helvetica-Bold', spaceBefore=8, spaceAfter=2)

    styles['body'] = ParagraphStyle('body', parent=base['Normal'],
        fontSize=9.5, leading=14, spaceAfter=6, alignment=TA_JUSTIFY,
        fontName='Helvetica')

    styles['body_left'] = ParagraphStyle('body_left', parent=base['Normal'],
        fontSize=9.5, leading=14, spaceAfter=6, alignment=TA_LEFT,
        fontName='Helvetica')

    styles['bold'] = ParagraphStyle('bold', parent=base['Normal'],
        fontSize=9.5, leading=14, spaceAfter=6, fontName='Helvetica-Bold')

    styles['code'] = ParagraphStyle('code', parent=base['Code'],
        fontSize=8.5, fontName='Courier', leading=12, spaceAfter=4,
        backColor=colors.HexColor('#f5f5f5'), leftIndent=10, rightIndent=10,
        borderPad=4)

    styles['note'] = ParagraphStyle('note', parent=base['Normal'],
        fontSize=9, leading=13, spaceAfter=6, fontName='Helvetica-Oblique',
        leftIndent=20, rightIndent=20,
        textColor=colors.HexColor('#333333'))

    styles['new_content'] = ParagraphStyle('new_content', parent=base['Normal'],
        fontSize=9.5, leading=14, spaceAfter=6, alignment=TA_JUSTIFY,
        fontName='Helvetica',
        backColor=colors.HexColor('#f0f7ff'),
        leftIndent=6, rightIndent=6, borderPad=4,
        borderColor=colors.HexColor('#4a90d9'), borderWidth=0.5)

    styles['checklist'] = ParagraphStyle('checklist', parent=base['Normal'],
        fontSize=9.5, leading=14, spaceAfter=3, fontName='Helvetica',
        leftIndent=20)

    styles['pitfall_head'] = ParagraphStyle('pitfall_head', parent=base['Normal'],
        fontSize=9.5, leading=14, spaceAfter=4, fontName='Helvetica-Bold',
        textColor=colors.HexColor('#cc0000'))

    return styles

S = build_styles()

def hr():
    return HRFlowable(width="80%", thickness=0.5, color=colors.grey,
                      spaceAfter=6, spaceBefore=6, hAlign='CENTER')

def sp(n=6):
    return Spacer(1, n)

def h1(t): return Paragraph(t, S['h1'])
def h2(t): return Paragraph(t, S['h2'])
def h3(t): return Paragraph(t, S['h3'])
def p(t):  return Paragraph(t, S['body'])
def pl(t): return Paragraph(t, S['body_left'])
def bold(t): return Paragraph(t, S['bold'])
def note(t): return Paragraph(t, S['note'])
def new(t): return Paragraph(t, S['new_content'])

def code_block(text):
    return Preformatted(text, S['code'])

TABLE_STYLE = TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c3e50')),
    ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
    ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0), (-1,-1), 9),
    ('ALIGN',      (0,0), (-1,-1), 'LEFT'),
    ('VALIGN',     (0,0), (-1,-1), 'TOP'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8f9fa')]),
    ('GRID',       (0,0), (-1,-1), 0.4, colors.HexColor('#cccccc')),
    ('LEFTPADDING',  (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING',   (0,0), (-1,-1), 4),
    ('BOTTOMPADDING',(0,0), (-1,-1), 4),
])

NEW_TABLE_STYLE = TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a6b9a')),
    ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
    ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0), (-1,-1), 9),
    ('ALIGN',      (0,0), (-1,-1), 'LEFT'),
    ('VALIGN',     (0,0), (-1,-1), 'TOP'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#e8f4fd'), colors.HexColor('#d0e8f5')]),
    ('GRID',       (0,0), (-1,-1), 0.6, colors.HexColor('#4a90d9')),
    ('LEFTPADDING',  (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING',   (0,0), (-1,-1), 4),
    ('BOTTOMPADDING',(0,0), (-1,-1), 4),
])

def make_table(data, col_widths=None, style=None):
    style = style or TABLE_STYLE
    rows = []
    for row in data:
        rows.append([Paragraph(str(c), ParagraphStyle('tc', fontName='Helvetica',
            fontSize=9, leading=12)) if not isinstance(c, Paragraph) else c
            for c in row])
    t = Table(rows, colWidths=col_widths, repeatRows=1)
    t.setStyle(style)
    return t

def new_tag():
    return Paragraph('<font color="#1a6b9a"><b>[NEW CONTENT]</b></font>', S['body_left'])

# ─────────────────────────────────────────────────────────────────────────────
def build_story():
    story = []
    W = PAGE_W - 2*MARGIN   # usable width

    # ── TITLE PAGE ────────────────────────────────────────────────────────────
    story += [
        sp(40),
        Paragraph("STATISTICS — COMPLETE BEGINNER'S GUIDE", S['title']),
        Paragraph("Time Series Regression", ParagraphStyle('sub', fontName='Helvetica-Bold',
            fontSize=12, alignment=TA_CENTER, spaceAfter=4)),
        Paragraph("From Zero to Full Understanding", ParagraphStyle('sub2', fontName='Helvetica-Oblique',
            fontSize=11, alignment=TA_CENTER, spaceAfter=20)),
        hr(),
        sp(10),
        note("Who this guide is for. This document assumes you have never studied statistics before. "
             "Every concept is built from the ground up with plain language, visual diagrams, and "
             "step-by-step worked examples. Nothing is skipped. If you already have some stats "
             "background, the later chapters still add valuable depth and worked examples."),
        sp(10),
        note("Note on this edition: Four gaps from the original have been filled in, marked with "
             "[NEW CONTENT] throughout: (1) the complete ρ-size reference table, "
             "(2) the completed four-case summary card, "
             "(3) a new section on confidence intervals, and "
             "(4) a full set of practice exam questions with answers."),
        hr(),
    ]

    # ── NOTATION GLOSSARY ─────────────────────────────────────────────────────
    story += [h1("NOTATION GLOSSARY — Read This First"),
              p("Before anything else, here is every symbol you will encounter, explained in plain English."),
              sp(4)]

    gloss = [
        ["Symbol","Name","Plain meaning"],
        ["Y","Dependent variable","The thing you are trying to predict or explain"],
        ["X","Independent / explanatory variable","The thing you use to explain Y"],
        ["t","Time index","Which time period we are in (e.g., t = 1 means year 1)"],
        ["i","Individual index","Which person/firm/country we are looking at"],
        ["β (beta)","Regression coefficient","How much Y changes when X changes by 1 unit"],
        ["α (alpha)","Intercept","The value of Y when all X's = 0"],
        ["ε (epsilon)","Error / residual","The part of Y that our model fails to explain"],
        ["ρ (rho)","Autocorrelation coefficient","How strongly this period's error relates to last period's error"],
        ["γ (gamma)","AR coefficient on lagged Y","How much last period's Y feeds into this period's Y"],
        ["λ (lambda)","Trend slope","How much the mean of Y grows each period"],
        ["σ²","Variance","Measure of spread / unpredictability"],
        ["Δ (delta)","First difference","Change from one period to the next: ΔX_t = X_t − X_{t−1}"],
        ["Σ (sigma)","Sum","Add up everything that follows"],
        ["H₀","Null hypothesis","The 'boring' default claim we try to disprove"],
        ["H₁","Alternative hypothesis","The 'interesting' claim we want to support"],
        ["n","Sample size","Total number of observations"],
        ["R²","R-squared","Proportion of Y's variation explained by the model (0 to 1)"],
        ["SE","Standard error","How much a coefficient estimate typically varies across samples"],
        ["CI","Confidence interval","A range of plausible values for the true β (new: see Section 0.4b)"],
        ["LM","Lagrange Multiplier","A test statistic we compute to check for autocorrelation"],
        ["χ²","Chi-squared","A probability distribution used for some hypothesis tests"],
        ["DW","Durbin-Watson","A quick test statistic for autocorrelation (limited use)"],
    ]
    story.append(make_table(gloss, [1.8*cm, 3.5*cm, W-5.3*cm]))
    story.append(sp(8))

    # ── PART 0 ────────────────────────────────────────────────────────────────
    story += [hr(), h1("PART 0 — STATISTICS FOUNDATIONS (Start Here)"),
              note("Everything in this section is background knowledge that the rest of the guide builds on.")]

    # 0.1
    story += [h2("0.1 — What Is Statistics? What Is Regression?"),
              p("<b>Statistics</b> is the science of learning from data. We observe the world, collect numbers, "
                "and try to answer questions like: Does more education cause higher wages? Does advertising "
                "increase sales? Does training reduce workplace accidents?"),
              p("The problem is: the world is messy. Wages are affected by education, <i>and</i> experience, "
                "<i>and</i> gender, <i>and</i> luck. Statistics lets us separate these influences."),
              p("<b>Regression</b> is the central tool. It finds the straight-line relationship between one or "
                "more explanatory variables (X's) and an outcome variable (Y), while controlling for noise."),
              h3("The Simplest Regression (One Variable)"),
              p("Y = α + βX + ε"),
              p("In plain English:"),
              pl("• <b>Y</b> = outcome we want to understand (e.g., hourly wage in euros)"),
              pl("• <b>X</b> = thing we think explains Y (e.g., years of education)"),
              pl("• <b>α</b> = baseline Y when X = 0 (e.g., wage with zero education)"),
              pl("• <b>β</b> = slope — how much Y changes for each 1-unit increase in X"),
              pl("• <b>ε</b> = error — everything that moves Y but isn't captured by X"),
              p("<b>Example:</b> Suppose we find: Wage = 5 + 1.2 × Education + ε"),
              p("This means: every additional year of education is associated with €1.20/hour more in wages, "
                "on average. A person with 10 years of education earns an estimated 5 + 1.2×10 = €17/hour."),
              p("The ε (error) is what remains unexplained. If the actual wage is €19/hour and our model "
                "predicts €17, the residual is ε = 19 − 17 = +2. Our model is off by €2 for that person."),
              h3("Multiple Regression (Several Variables)"),
              p("Y = α + β₁X₁ + β₂X₂ + … + βₖXₖ + ε"),
              p("Now we control for several things at once. Each β_j tells us: 'holding all other X's constant, "
                "how much does Y change when X_j increases by 1?' This is the <b>ceteris paribus</b> (all else "
                "equal) interpretation."), hr()]

    # 0.2
    story += [h2("0.2 — How Regression Is Estimated: OLS"),
              p("<b>OLS = Ordinary Least Squares.</b> It is the standard method for calculating the β values."),
              p("The idea: choose the values of α and β that make the errors ε as small as possible across "
                "all observations. Specifically, OLS minimises the <b>sum of squared errors</b>:"),
              p("min Σ εᵢ² = Σ (Yᵢ − α − βXᵢ)²"),
              p("Why square them? Two reasons: 1. Positive and negative errors don't cancel each other out. "
                "2. Large errors are penalised more than small ones (squaring amplifies big mistakes)."),
              p("OLS gives us <b>coefficient estimates</b> β̂ ('beta hat') — the best-fitting line through the data."),
              p("<b>BLUE:</b> When certain conditions hold (see Section 0.4), OLS is <b>B</b>est <b>L</b>inear "
                "<b>U</b>nbiased <b>E</b>stimator. 'Best' means no other linear method has smaller estimation "
                "errors. 'Unbiased' means on average the estimates hit the true value."), hr()]

    # 0.3
    story += [h2("0.3 — R²: How Well Does the Model Fit?"),
              p("R² = 1 − (Sum of Squared Errors) / (Total Variation in Y)"),
              p("<b>Range:</b> R² is always between 0 and 1.")]

    r2_table = [
        ["R² value","Meaning"],
        ["0.0","The model explains nothing — X tells us nothing about Y"],
        ["0.5","The model explains 50% of Y's variation"],
        ["1.0","Perfect fit — the model explains everything, zero residual"],
        ["0.95","Seems great! But in time-series data, this can be a warning sign (spurious regression)"],
    ]
    story.append(make_table(r2_table, [2.5*cm, W-2.5*cm]))
    story += [sp(4),
              p("<b>Intuition:</b> Imagine Y is the height of ocean waves. Total variation = how much waves "
                "differ from their average height. If your model explains 80% of that variation, R² = 0.80."), hr()]

    # 0.4
    story += [h2("0.4 — Standard Errors, t-statistics, and p-values"),
              p("Even if OLS gives us β̂ = 1.2, we cannot be certain the true β is 1.2. If we collected a "
                "different sample, we'd get a slightly different estimate. <b>Standard errors (SE)</b> measure "
                "how much β̂ varies across samples."),
              h3("The t-statistic"),
              p("t = β̂ / SE(β̂)"),
              p("The t-statistic asks: 'Is this estimate far enough from zero to be convincingly non-zero?'"),
              pl("• A <b>large |t|</b> (say, |t| > 2) means the estimate is large relative to its uncertainty → likely real."),
              pl("• A <b>small |t|</b> (say, |t| < 1) means the estimate could easily be zero just by chance → not convincing."),
              h3("The p-value"),
              p("The <b>p-value</b> is the probability of seeing a t-statistic this extreme (or more) if the "
                "true β were actually zero.")]

    pval_table = [
        ["p-value","Interpretation"],
        ["p < 0.01","Very strong evidence against H₀ (significant at 1%)"],
        ["p < 0.05","Strong evidence against H₀ (significant at 5%) — standard threshold"],
        ["p < 0.10","Weak evidence against H₀ (significant at 10%)"],
        ["p > 0.10","No convincing evidence; cannot reject H₀"],
    ]
    story.append(make_table(pval_table, [2.5*cm, W-2.5*cm]))
    story += [sp(4),
              p("<b>Analogy:</b> You flip a coin 20 times and get 17 heads. The p-value asks: 'If this were a "
                "fair coin (H₀), how likely is getting 17 or more heads?' If that probability is tiny (p < 0.05), "
                "you conclude the coin is probably not fair — you reject H₀."),
              p("<b>Hypothesis Testing in Regression:</b> For any coefficient β_j: H₀: β_j = 0 (X_j has no "
                "effect on Y) vs. H₁: β_j ≠ 0 (X_j does affect Y). If p < 0.05: reject H₀ → X_j is "
                "statistically significant."),
              p("<b>Important phrasing:</b> We never 'accept H₀'. We either reject it or fail to reject it. "
                "Failing to reject just means the data don't give us enough evidence — not that H₀ is "
                "definitely true."), hr()]

    # 0.4b — NEW: Confidence Intervals
    story += [
        new_tag(),
        h2("0.4b — Confidence Intervals [NEW]"),
        new("A <b>confidence interval (CI)</b> gives a range of plausible values for the true population "
            "parameter β, based on our sample estimate β̂. It is the natural complement to the t-test and "
            "p-value: while a p-value gives a yes/no decision, the CI tells you <i>how big</i> the effect "
            "plausibly is."),
        new("<b>The formula for a 95% confidence interval:</b>"),
        new("CI = β̂  ±  1.96 × SE(β̂)"),
        new("This means: we are 95% confident the true β falls somewhere in the range "
            "[β̂ − 1.96 × SE, β̂ + 1.96 × SE]."),
    ]

    ci_table = [
        ["Confidence level","Multiplier (z*)","Interpretation"],
        ["90%","1.645","10% chance the true β is outside this range"],
        ["95%","1.960","5% chance the true β is outside this range (most common)"],
        ["99%","2.576","1% chance the true β is outside this range"],
    ]
    story.append(make_table(ci_table, [3*cm, 3.5*cm, W-6.5*cm], NEW_TABLE_STYLE))
    story += [
        sp(4),
        new("<b>Worked example:</b> Suppose β̂ = 1.20 and SE(β̂) = 0.35."),
        new("  95% CI = 1.20 ± 1.96 × 0.35 = 1.20 ± 0.686 = [0.514,  1.886]"),
        new("Interpretation: We are 95% confident the true effect of one extra year of education on "
            "wages is between +€0.51/hr and +€1.89/hr."),
        new("<b>Three key rules about confidence intervals:</b>"),
        new("1. <b>Link to significance:</b> If the 95% CI does NOT contain zero, the coefficient is "
            "significant at the 5% level — this is exactly equivalent to p < 0.05."),
        new("2. <b>Width tells you precision:</b> A narrow CI means the estimate is precise. A wide CI "
            "means you have a lot of uncertainty — perhaps because the sample is small or the data "
            "are noisy."),
        new("3. <b>Width increases with SE:</b> Larger standard errors produce wider intervals. "
            "Autocorrelation inflates SE, so it makes CIs wider — another reason to test for "
            "and fix autocorrelation."),
        new("<b>In time-series models:</b> When autocorrelation is present, the reported SE values are "
            "<i>too small</i>, which makes CIs artificially narrow. Fixing autocorrelation (via DL or AR "
            "re-specification) restores correct SE values and correct CI widths."),
        hr(),
    ]

    # 0.5
    story += [h2("0.5 — The Five Classical Assumptions"),
              p("OLS is only BLUE when these five conditions hold:")]

    assump_table = [
        ["Assumption","What it says","Why it matters"],
        ["A1","E(ε) = 0","Errors average to zero — no systematic over/under-prediction"],
        ["A2","Var(ε) = σ² (constant)","Homoskedasticity — equal spread of errors everywhere"],
        ["A3","cov(εᵢ, εⱼ) = 0","Errors are uncorrelated with each other"],
        ["A4","X's are non-random, not perfectly correlated","We can separate each X's effect"],
        ["A5","ε ~ Normal (optional)","Needed for exact inference in small samples"],
    ]
    story.append(make_table(assump_table, [2*cm, 4.5*cm, W-6.5*cm]))
    story += [sp(4),
              p("When you use time-series data, <b>A3 is routinely violated</b> (autocorrelation). "
                "This is the central problem this guide addresses. A new assumption is also needed: "
                "<b>stationarity</b>."),
              hr()]

    # 0.6
    story += [h2("0.6 — Visual Intuition: What a Regression Looks Like"),
              code_block(
"Y\n"
"| *\n"
"|   *   *\n"
"|     *   *\n"
"|       *   (fitted line)\n"
"|         *   *\n"
"|             *\n"
"+---------------------- X"),
              p("Each * is a data point. OLS finds the straight line that passes as close as possible to "
                "all the points, minimising the total squared vertical distance from points to the line."),
              p("The <b>residuals</b> (errors) are the vertical distances from each point to the line. "
                "Good regression: residuals look like random noise. Bad regression: residuals show a "
                "pattern (e.g., all positive on the left, all negative on the right).")]

    story.append(PageBreak())

    # ── PART 1 ────────────────────────────────────────────────────────────────
    story += [h1("PART 1 — TIME SERIES FOUNDATIONS"),
              h1("CHAPTER TS_A — Cautions"),
              note("What makes time-series data special and why ordinary regression needs modification")]

    # A.1
    story += [h2("A.1 — Cross-Section vs. Time-Series Data"),
              h3("Definitions")]

    type_table = [
        ["Type","Description","Notation","Order matters?"],
        ["Cross-section","Many units at one point in time","X_i, subscript i = individual","No — rows are interchangeable"],
        ["Time-series","One unit observed repeatedly over time","X_t, subscript t = time period","Yes — shuffling destroys information"],
        ["Panel data","Many units over many time periods","X_{it}","Both dimensions matter"],
    ]
    story.append(make_table(type_table, [2.5*cm, 4.5*cm, 4*cm, W-11*cm]))
    story += [sp(4),
              p("<b>Why Order Matters:</b> In a cross-section of 1,000 workers you could randomly reorder "
                "the rows and your regression results would be identical. In a time series of 40 years of "
                "GDP data, row 5 (GDP in year 5) must come after row 4 and before row 6. The temporal "
                "structure is not a nuisance — it is the entire point."),
              h3("Cross-section data (each row is a different person):"),
              code_block(
"Person | Wage | Education | Age\n"
"-------|------|-----------|----\n"
"Alice  |  22  |     16    | 34\n"
"Bob    |  18  |     12    | 28\n"
"Carol  |  35  |     20    | 45\n"
"...    | ...  |    ...    | ...\n"
"You could sort Alice, Bob, Carol in any order. Same result."),
              h3("Time-series data (each row is a different time period):"),
              code_block(
"Year | Belgium GDP | Unemployment | Inflation\n"
"-----|-------------|--------------|----------\n"
"2000 |   253 bn    |     6.9%     |   2.7%\n"
"2001 |   259 bn    |     6.6%     |   2.4%\n"
"2002 |   263 bn    |     7.5%     |   1.6%\n"
"2003 |   268 bn    |     8.2%     |   1.5%\n"
"...  |    ...      |     ...      |   ...\n"
"Row 2003 MUST come after row 2002."),
              hr()]

    # A.2
    story += [h2("A.2 — Lagged Variables"),
              p("<b>What a Lag Is:</b> A lag simply refers to the value of a variable at an earlier time "
                "period. Think of it as 'looking in the rear-view mirror' — what was the value one period "
                "ago? Two periods ago?")]

    lag_table = [
        ["Notation","Meaning","Value refers to"],
        ["X_t","Current value of X","Q3 1987"],
        ["X_{t−1}","One-period lag","Q2 1987"],
        ["X_{t−2}","Two-period lag","Q1 1987"],
        ["X_{t−q}","q-period lag","q quarters before Q3 1987"],
    ]
    story.append(make_table(lag_table, [2.5*cm, 4*cm, W-6.5*cm]))
    story += [sp(4),
              code_block(
"After creating lag X_{t-1}:\n"
"  t=1: 10  |  X_{t-1}: [missing — no period 0]\n"
"  t=2: 14  |  X_{t-1}: 10  <- value from t=1\n"
"  t=3: 11  |  X_{t-1}: 14  <- value from t=2\n"
"  t=4: 16  |  X_{t-1}: 11  <- value from t=3\n"
"  t=5: 13  |  X_{t-1}: 16  <- value from t=4\n"
"Notice: first row loses its observation (no 'period 0')."),
              p("<b>Why Lags Are Needed:</b> Economic processes rarely respond instantaneously. Consider "
                "safety training: hours are delivered in month t, workers need time to absorb the training, "
                "and the reduction in accidents appears in months t+1, t+2, etc."),
              p("<b>Another example — central bank interest rates:</b> When a central bank raises interest "
                "rates today, the effect on consumer spending might take 6–12 months to fully materialise."),
              p("<b>Watch Out: Lost Observations.</b> Each lag of order q costs you q observations at the "
                "start. Lag of order 1 → lose 1 observation. Lag of order q → lose q observations."), hr()]

    # A.3
    story += [h2("A.3 — Difference Variables"),
              p("<b>Definition:</b> The first difference of X_t is the change from one period to the next: "
                "ΔX_t = X_t − X_{t−1}"),
              p("<b>Intuition:</b> If GDP was €100 billion last year and €104 billion this year, the first "
                "difference is ΔGDP = 104 − 100 = +€4 billion. It answers: 'How much did GDP change?'"),
              code_block(
"GDP level (trending upward — non-stationary):\n"
"GDP |                              *\n"
"    |                        * *\n"
"    |                    * *\n"
"    |                * *\n"
"    +-------------------------------- time\n"
"    Clearly trending -> not stationary\n\n"
"ΔGDP (first differences — fluctuates around zero):\n"
"ΔGDP |  * *      *\n"
"     |     * * * * * *\n"
"     | ─────────────────── 0\n"
"     |     * * *\n"
"     +-------------------------------- time\n"
"     Fluctuates around a constant level -> stationary"),
              p("<b>Why Logarithms?</b> When you take log(price) and then difference it: "
                "Δln(X_t) ≈ (X_t − X_{t−1})/X_{t−1}, you get the <b>percentage change</b> — "
                "directly comparable across differently-sized quantities."),
              p("<b>Why Differences Matter:</b> (1) Economic theory talks about changes. "
                "(2) They cure a stochastic trend (unit root). (3) Log-returns are scale-free."), hr()]

    # A.4
    story += [h2("A.4 — The Three Problems with Time-Series Regression"),
              p("Every time you run a regression on time-series data, you must address three specific issues."),
              bold("Problem 1 — Data Quality and Sample Size")]

    size_table = [
        ["Situation","Recommendation"],
        ["Ideal","n > 100 observations"],
        ["Minimum","n ≈ 35; at least 10 obs per X-variable in the model"],
        ["Yearly data","May need 35+ years; consider monthly or quarterly if available"],
        ["Monetary variables","Use real (deflated) values — inflation creates artificial trends"],
    ]
    story.append(make_table(size_table, [3.5*cm, W-3.5*cm]))
    story += [sp(4),
              p("<b>Why inflation matters:</b> If you regress nominal wages on nominal GDP, both series "
                "may trend upward simply because of inflation, not because of any real relationship. "
                "Always use inflation-adjusted (real) values for monetary variables."),
              bold("Problem 2 — Autocorrelation"),
              p("Classical Assumption A3 states that errors are uncorrelated: cov(εᵢ, εⱼ) = 0. In "
                "time-series data this is routinely violated. Shocks have persistence — if something "
                "unexpected happens today, its effect persists into next period, gradually fading."),
              bold("Problem 3 — Spurious Regression / Non-Stationarity"),
              p("Imagine regressing Belgian ice cream sales on annual sunspot activity. Both series happen "
                "to trend upward over a 30-year window. You would find a hugely significant regression "
                "with R² = 0.95 — even though they have absolutely nothing to do with each other."),
              p("The solution is to ensure all variables are stationary before fitting the regression.")]

    story.append(PageBreak())

    # ── CHAPTER TS_B ──────────────────────────────────────────────────────────
    story += [h1("CHAPTER TS_B — Autocorrelation"),
              note("Errors that remember the past: detection with the LMSC test")]

    story += [h2("B.1 — Which Classical Assumption is Violated?"),
              p("Autocorrelation violates <b>A3</b>. When errors are correlated over time, "
                "cov(ε_t, ε_{t-1}) ≠ 0."),
              p("<b>Why A3 Fails So Commonly in Time Series:</b> Think of the residual ε_t as "
                "'everything that moves Y but isn't in my model.' In time-series settings, omitted "
                "variables themselves tend to persist over time. Today's omitted shock tends to carry "
                "over into tomorrow."),
              p("<b>Intuitive example:</b> You model monthly consumer spending using only income. "
                "But consumer confidence, which you haven't measured, also drives spending — and "
                "consumer confidence is persistent. The residuals will therefore form waves: positive "
                "for a stretch (when confidence is high), then negative for a stretch (when confidence "
                "is low). That is positive autocorrelation."), hr()]

    # B.2
    story += [h2("B.2 — First-Order Autocorrelation"),
              p("<b>The AR(1) Error Structure:</b> ε_t = ρ ε_{t−1} + u_t"),
              p("where: ρ (rho) is the first-order autocorrelation coefficient (between −1 and 1); "
                "u_t is classical white-noise error (uncorrelated, mean zero, constant variance)."),
              p("<b>White noise</b> means pure randomness — like rolling a fair die each period. "
                "No memory, no pattern, no trend."),
              code_block(
"No autocorrelation (ρ = 0) — ideal:\n"
"  Residuals\n"
"  | * *   *   *\n"
"  |   * *   * *\n"
"0 | ─────────────────────────\n"
"  | * *   * * *\n"
"  |     * *\n"
"  Random scatter. A3 satisfied. ✓\n\n"
"Positive autocorrelation (ρ > 0) — 'waves':\n"
"  Residuals\n"
"  | * * * *\n"
"  |* *       * *\n"
"0 | ─────────────────────────\n"
"  |         * * * *\n"
"  |                   * * *\n"
"  Long runs of + then long runs of −. A3 violated. ✗\n\n"
"Negative autocorrelation (ρ < 0) — 'zigzag':\n"
"  Residuals\n"
"  | * * * * *\n"
"0 | ─────────────────────────\n"
"  |   * * * * *\n"
"  Alternates above/below every period. Rare. A3 violated. ✗"),
    ]

    # NEW: ρ size table
    story += [
        new_tag(),
        h3("Understanding the Size of ρ — Complete Reference Table [NEW]"),
        new("The magnitude of ρ tells you how severe the autocorrelation is. This table was incomplete "
            "in the original; here is the full reference:"),
    ]

    rho_table = [
        ["Value of ρ","Autocorrelation strength","Effect on residuals","Practical consequence"],
        ["ρ = 0","None","Pure white noise — ideal","A3 satisfied; OLS is BLUE"],
        ["0 < ρ ≤ 0.3","Weak positive","Short runs of same sign","Minor inflation of t-stats; often tolerable"],
        ["0.3 < ρ ≤ 0.6","Moderate positive","Noticeable wave pattern","Standard errors meaningfully wrong; fix required"],
        ["0.6 < ρ < 1","Strong positive","Long persistent waves","Severe bias in SEs; t-tests very misleading"],
        ["ρ → 1","Near unit root","Series barely returns to mean","Borders on non-stationarity; re-examine series"],
        ["−0.3 ≤ ρ < 0","Weak negative","Slight alternation","Rare in economics; minor effect"],
        ["ρ < −0.3","Strong negative","Rapid alternation + − + −","Often caused by over-differencing"],
    ]
    story.append(make_table(rho_table,
        [2*cm, 3*cm, 4*cm, W-9*cm], NEW_TABLE_STYLE))
    story += [sp(4),
              new("<b>Key boundary:</b> We require −1 < ρ < 1 for the error process to be stationary "
                  "and well-behaved."),
              new("<b>Worked analogy for ρ = 0.7:</b> If this quarter's residual is +10, next quarter's "
                  "expected residual is +7 (= 0.7 × 10). Then +4.9, then +3.4, then +2.4 — slowly "
                  "decaying toward zero. A shock takes many periods to fade."),
              hr()]

    # B.3
    story += [h2("B.3 — Consequences of Autocorrelation")]

    consq_table = [
        ["Property","With autocorrelation"],
        ["OLS estimators β̂","Still unbiased — on average they hit the true β"],
        ["Efficiency","No longer best (not BLUE) — a better estimator exists"],
        ["Standard errors","Wrong — they use the wrong formula (assumes A3)"],
        ["t-tests and F-tests","Invalid — built on wrong standard errors"],
        ["Confidence intervals","Wrong width — too narrow if ρ > 0 (falsely precise)"],
        ["R²","Unaffected but potentially misleading"],
    ]
    story.append(make_table(consq_table, [4.5*cm, W-4.5*cm]))
    story += [sp(4),
              p("The key danger is <b>false significance</b>: positive autocorrelation inflates "
                "t-statistics, making coefficients appear more significant than they really are."),
              p("<b>Analogy for wrong standard errors:</b> Imagine asking 10 people in one household "
                "whether they like pizza, and claiming those 10 opinions represent 10 independent data "
                "points. They don't — family members influence each other. Autocorrelation does the same "
                "thing: consecutive observations are not truly independent, so your effective sample size "
                "is smaller than it appears."),
              p("<b>Exception: AR(1) Models.</b> When the regression contains Y_{t−1} as a regressor "
                "AND there is autocorrelation, the coefficient estimates themselves become <b>biased</b>. "
                "<b>Practical rule:</b> If you detect autocorrelation in an AR(1) model, re-specify "
                "(switch to DL(q))."), hr()]

    # B.4
    story += [h2("B.4 — Detection: The LMSC Test"),
              p("<b>Step 0 — Graphical Inspection First.</b> Always plot the residuals against time "
                "before running any test."),
              p("<b>Hypotheses:</b> H₀: ρ = 0 (no autocorrelation — A3 satisfied) vs. "
                "H₁: ρ ≠ 0 (autocorrelation present — A3 violated)"),
              p("<b>Step 1:</b> Fit the original regression model. Save the residuals e_t."),
              p("<b>Step 2:</b> Build the auxiliary regression. Regress residuals on all original "
                "predictors X_{1t}, …, X_{kt} plus the lagged residual e_{t−1}:"),
              p("e_t = α₀ + α₁X_{1t} + … + αₖX_{kt} + α_{k+1}e_{t−1} + u_t"),
              p("<b>Step 3:</b> From the auxiliary regression, compute: LM = n × R²"),
              p("<b>Step 4:</b> Under H₀, LM ~ χ²(1). Compare LM to <b>3.841</b> "
                "(5% critical value for χ²(1))."),
              p("<b>Decision:</b> If LM > 3.841 (or p < 0.05): Reject H₀ → autocorrelation is present. "
                "If LM ≤ 3.841 (or p ≥ 0.05): Do not reject H₀ → A3 plausibly satisfied."),
              h3("Worked Example — Phillips Curve"),
              p("Original model: Y_t = β₀ + β₁X_t + ε_t — Y = inflation rate (%), "
                "X = change in unemployment rate (pp) — n = 90 quarterly observations")]

    phil_table = [
        ["Item","Value"],
        ["n for auxiliary regression","90 − 1 = 89"],
        ["R² of auxiliary regression","0.310211"],
        ["Coefficient on e_{t−1}","0.558 (t = 6.219, p < .001)"],
        ["LM statistic","89 × 0.310211 = 27.609"],
        ["Critical value (5%)","3.841"],
        ["Conclusion","Reject H₀ — strong autocorrelation present"],
    ]
    story.append(make_table(phil_table, [5*cm, W-5*cm]))
    story += [sp(4),
              h3("Durbin–Watson as an Alternative")]

    dw_table = [
        ["DW value","Interpretation"],
        ["Close to 2","No autocorrelation"],
        ["Close to 0","Strong positive autocorrelation (ρ near +1)"],
        ["Close to 4","Strong negative autocorrelation (ρ near −1)"],
        ["1.5 to 2.5","Generally acceptable (rough rule)"],
    ]
    story.append(make_table(dw_table, [3*cm, W-3*cm]))
    story += [sp(4),
              p("<b>Critical limitation:</b> Durbin–Watson is <b>invalid</b> whenever the regression "
                "contains a lagged dependent variable Y_{t−1}. Always use LMSC as your primary test."),
              p("Relationship: DW ≈ 2(1 − ρ̂). So DW = 2 when ρ̂ = 0, DW = 0 when ρ̂ = 1."), hr()]

    # B.5
    story += [h2("B.5 — Solutions for Autocorrelation")]

    sol_table = [
        ["Re-specification","What you add","Model type"],
        ["Add lagged X's","X_{t−1}, X_{t−2}, …, X_{t−q}","DL(q) — Distributed Lag"],
        ["Add lagged Y","Y_{t−1}","AR(1) — Autoregressive"],
    ]
    story.append(make_table(sol_table, [3.5*cm, 5*cm, W-8.5*cm]))
    story += [sp(4),
              p("<b>Key principle: bias is worse than inefficiency.</b> "
                "DL with autocorrelation → wrong standard errors (bad, but coefficients are still "
                "correct on average). AR with autocorrelation → wrong coefficient estimates "
                "(fundamentally misleading).")]

    story.append(PageBreak())

    # ── CHAPTER TS_C ──────────────────────────────────────────────────────────
    story += [h1("CHAPTER TS_C — Stationarity"),
              note("Spurious regression, the generalized AR(1), and the Dickey-Fuller test")]

    # C.1
    story += [h2("C.1 — Spurious Regression"),
              p("<b>The Problem:</b> Consider: regress Belgian GDP per capita (1950–2004) on US population "
                "density over the same period. You find R² ≈ 0.96 (extremely high) and slope coefficient "
                "significant at p < 0.001. Yet Belgian GDP and US population density have no meaningful "
                "economic relationship. This is a <b>spurious regression</b>."),
              p("<b>Famous real-world example:</b> The number of Nicolas Cage films released per year is "
                "significantly correlated with drowning deaths in US swimming pools between 1999 and 2009. "
                "A regression gives R² ≈ 0.67 and p < 0.05. Completely spurious."),
              p("<b>The Root Cause: Non-Stationarity.</b> Both variables are non-stationary — their "
                "means drift over time. Standard regression theory requires stationarity."), hr()]

    # C.2
    story += [h2("C.2 — Definition of Stationarity"),
              p("<b>Formal Definition (Weak/Covariance Stationarity):</b> A time series Y_t is weakly "
                "stationary if, for every t:"),
              pl("1. <b>E(Y_t) = μ</b> — The mean is constant."),
              pl("2. <b>Var(Y_t) = σ²</b> — The variance is constant."),
              pl("3. <b>Cov(Y_t, Y_{t−s}) = γ_s</b> — The covariance depends only on the gap s, not on when."),
              code_block(
"Stationary series — fluctuates around a constant level:\n"
"Y\n"
"  |     *       *   *\n"
"  |  *     * *     * *\n"
"  | ─────────────────── <- constant mean\n"
"  |  *   *       *   *\n"
"  |     *   *\n"
"  Mean is flat. Keeps returning to the same level. ✓\n\n"
"Non-stationary (trending) series — drifts upward:\n"
"Y\n"
"  |                 * *\n"
"  |             * * *\n"
"  |         * * *\n"
"  |     * * *\n"
"  | * * *\n"
"  Mean grows over time. Spurious regression risk! ✗\n\n"
"Non-stationary (random walk) — wanders unpredictably:\n"
"Y\n"
"  |   *\n"
"  | *   * * *\n"
"  |*       *   *\n"
"  |           * *\n"
"  |               * * * *\n"
"  Neither trends consistently NOR stays near a fixed level. ✗"),
              hr()]

    # C.3
    story += [h2("C.3 — The Generalized AR(1) Model"),
              p("Y_t = a + λt + ρY_{t−1} + ε_t"),
              p("The three parameters: <b>a</b> = constant; <b>λ</b> = trend slope; "
                "<b>ρ</b> = autoregressive coefficient. The critical question: |ρ| < 1 (stationary) "
                "or |ρ| = 1 (random walk)?"),
              h3("Case 1 — Basic AR(1): |ρ| < 1, a = 0, λ = 0"),
              p("Model: Y_t = ρ Y_{t-1} + ε_t. Each period, Y reverts toward zero. "
                "Properties: Mean = 0 (constant ✓); Var = σ²/(1−ρ²) (constant ✓); stationary."),
              p("<b>Example:</b> Y_t = 0.7 Y_{t−1} + ε_t. A shock of +10: t+1: +7.0, t+2: +4.9, "
                "t+3: +3.4, … → 0. Shocks fade."),
              h3("Case 2 — AR(1) with constant: |ρ| < 1, a ≠ 0, λ = 0"),
              p("Model: Y_t = a + ρ Y_{t-1} + ε_t. "
                "Long-run mean μ = a/(1−ρ). <b>Stationary</b> around non-zero mean."),
              p("<b>Example:</b> Y_t = 5 + 0.6 Y_{t−1} + ε_t. Long-run mean = 5/(1−0.6) = 12.5."),
              h3("Case 3 — AR(1) with deterministic trend: |ρ| < 1, a ≠ 0, λ ≠ 0"),
              p("Model: Y_t = a + λt + ρ Y_{t-1} + ε_t. The λt term makes the mean grow linearly. "
                "<b>Not stationary in levels</b>, but deviation from the trend line is stationary. "
                "<b>Fix:</b> Add t as a regressor."),
              h3("Case 4 — Random Walk: |ρ| = 1"),
              p("When ρ = 1, Y_t = a + Y_{t-1} + ε_t. Each shock is <b>permanent</b>. "
                "By repeated substitution: Y_t = Y_0 + ε_1 + ε_2 + … + ε_t."),
              p("Variance = tσ² → <b>grows without bound</b>. <b>Fix: Take first differences.</b>")]

    # NEW: Completed Summary Card
    story += [
        new_tag(),
        h3("Four-Case Summary Card — Completed [NEW]"),
        new("The original summary card had missing entries. Here is the complete version:"),
    ]

    card_table = [
        ["Case","ρ","λ","Stationary?","Correct Fix"],
        ["Basic AR(1)","|ρ| < 1","= 0","✓ Yes","No fix needed — use in levels"],
        ["AR(1) + constant","|ρ| < 1","= 0","✓ Yes","No fix needed — use in levels"],
        ["AR(1) + deterministic trend","|ρ| < 1","≠ 0","✗ No (in levels)\n✓ About trend line","Add t as regressor\n(Option: detrend Y first)"],
        ["Random walk\n(pure, ρ = 1, a = 0)","= 1","= 0","✗ No\n(variance grows)","Take first differences ΔY_t"],
        ["Random walk with drift\n(ρ = 1, a ≠ 0)","= 1","= 0","✗ No\n(mean drifts)","Take first differences ΔY_t"],
    ]
    story.append(make_table(card_table,
        [4*cm, 1.6*cm, 1.4*cm, 3.5*cm, W-10.5*cm], NEW_TABLE_STYLE))
    story += [sp(4),
              new("<b>Memory rule for the fix:</b>"),
              new("• Series wanders with permanently accumulating shocks (ρ = 1) → <b>First difference</b>"),
              new("• Series trends predictably but returns to trend after shocks (|ρ| < 1, λ ≠ 0) → "
                  "<b>Add t as regressor</b>"),
              new("• Series is already mean-reverting (|ρ| < 1, λ = 0) → <b>No fix needed</b>"),
              hr()]

    # C.4
    story += [h2("C.4 — Deterministic vs. Stochastic Trends"),
              p("This distinction is crucial because the two types of non-stationarity require <b>different "
                "fixes</b>. Applying the wrong fix can make things worse.")]

    trend_table = [
        ["Feature","Deterministic Trend","Stochastic Trend (Random Walk)"],
        ["Mathematical source","λt term in the model","ρ = 1 (unit root)"],
        ["Mean","Changes predictably (grows by λ per period)","May drift, but unpredictably"],
        ["Variance","Constant","Grows with time"],
        ["Shocks","Temporary — series returns to trend","Permanent — series never recovers"],
        ["Example","GDP trend growth of 2% per year","S&P 500 stock price index"],
        ["Correct fix","Detrend or add t as regressor","First difference"],
        ["Wrong fix","First-differencing → negative autocorrelation","Detrending doesn't remove stochastic trend"],
    ]
    story.append(make_table(trend_table, [3*cm, 5.5*cm, W-8.5*cm]))
    story += [sp(4), hr()]

    # C.5
    story += [h2("C.5 — Solutions for Non-Stationarity"),
              bold("Fix A — Deterministic Trend (|ρ| < 1, λ ≠ 0)"),
              p("<b>Option 2 — Model the trend explicitly (preferred):</b> Include t as an additional "
                "regressor in your main model: Y_t = β₀ + β₁X_t + λt + ε_t"),
              p("The coefficient on t absorbs the linear trend; the coefficient on X_t now measures the "
                "relationship <i>after controlling for the common time trend</i>."),
              bold("Fix B — Stochastic Trend / Unit Root (|ρ| = 1)"),
              p("Take first differences: ΔY_t = Y_t − Y_{t−1}. This is the <b>only valid fix</b> for a "
                "random walk."),
              p("<b>Why it works:</b> If Y_t = Y_{t-1} + ε_t, then ΔY_t = ε_t ← white noise, stationary. ✓"),
              p("<b>Important caveat — Cointegration:</b> There is one exception. If two non-stationary "
                "series are cointegrated — genuinely tied together by an economic relationship — you should "
                "<i>NOT</i> difference them. Instead, run the regression in levels. Differencing "
                "cointegrated variables throws away the most economically meaningful information."), hr()]

    # C.6
    story += [h2("C.6 — The Dickey-Fuller Test"),
              p("<b>Purpose:</b> The Dickey-Fuller test is a formal unit root test: it decides whether "
                "ρ = 1 (non-stationary) or |ρ| < 1 (stationary)."),
              p("<b>Hypotheses:</b>"),
              pl("• H₀: ρ = 1 — the series has a unit root, is NOT stationary"),
              pl("• H₁: |ρ| < 1 — the series IS stationary (possibly about a deterministic trend)"),
              p("<b>Note the asymmetry:</b> H₀ is the dangerous case (non-stationarity). Failing to "
                "reject H₀ means we cannot prove stationarity — assume the series needs differencing."),
              p("<b>The Reparameterisation:</b> Subtract Y_{t-1} from both sides to get: "
                "ΔY_t = a + λt + α₁Y_{t−1} + ε_t where α₁ = ρ − 1. Now H₀: α₁ = 0 and H₁: α₁ < 0."),
              p("<b>Why the Normal t-Table Cannot Be Used Here:</b> Under H₀, Y_t is a random walk "
                "— not stationary. The usual asymptotic results do not apply. The actual distribution "
                "is shifted left. If you used ±1.96, you would almost never reject H₀ for truly "
                "stationary series. Dickey and Fuller derived special critical values through simulation:")]

    df_table = [
        ["DF Version","1% critical value","5% critical value","10% critical value"],
        ["Version 1 (no trend)","−3.43","−2.86","−2.57"],
        ["Version 2 (with trend)","−3.96","−3.41","−3.13"],
    ]
    story.append(make_table(df_table, [3.5*cm, 3*cm, 3*cm, W-9.5*cm]))
    story += [sp(4),
              p("<b>Decision rule:</b> Reject H₀ (conclude stationarity) if and only if the "
                "t-statistic on Y_{t−1} is <b>more negative</b> than the critical value.")]

    ver_table = [
        ["Version","Regression","When to use"],
        ["Version 1 — no trend","ΔY_t = α₀ + α₁ Y_{t−1} + ε_t","No visible trend in time plot"],
        ["Version 2 — with trend","ΔY_t = α₀ + λt + α₁ Y_{t−1} + ε_t","Clear trend in time plot, or when unsure"],
    ]
    story.append(make_table(ver_table, [3.5*cm, 5.5*cm, W-9*cm]))
    story += [sp(4), p("<b>Version 2 is the safer default.</b>")]

    after_df = [
        ["DF result","Action"],
        ["Reject H₀ (stationary)","Use the series in levels in your model"],
        ["Fail to reject H₀ (unit root)","Take first differences, then re-run DF on ΔY_t"],
        ["DF on ΔY_t: Reject H₀","ΔY_t is stationary; use first differences in the model"],
        ["DF on ΔY_t: Still fail to reject","Rare. Consider second differences"],
    ]
    story.append(make_table(after_df, [5.5*cm, W-5.5*cm]))
    story.append(sp(6))

    story.append(PageBreak())

    # ── CHAPTER TS_D ──────────────────────────────────────────────────────────
    story += [h1("CHAPTER TS_D — Dynamic Models"),
              note("DL(q), AR(1), total multipliers, and the time-series exam workflow")]

    # D.1
    story += [h2("D.1 — Distributed Lag Model DL(q)"),
              p("A <b>static model</b> assumes the entire effect of X on Y is instantaneous: "
                "Y_t = α + β₀X_t + ε_t. But most economic effects have delayed responses."),
              p("The <b>Distributed Lag model of order q</b> captures these delays:"),
              p("Y_t = α + β₀X_t + β₁X_{t−1} + β₂X_{t−2} + … + β_qX_{t−q} + ε_t"),
              code_block(
"Visual — how DL(2) distributes the effect:\n"
"\n"
"Training hours in month t\n"
"    |\n"
"    |--- β₀ ---> Effect on accidents in month t   (immediate)\n"
"    |--- β₁ ---> Effect on accidents in month t+1 (1-period lag)\n"
"    |--- β₂ ---> Effect on accidents in month t+2 (2-period lag)\n"
"\n"
"Total effect of one training hour = β₀ + β₁ + β₂  (total multiplier)"),
              p("<b>The Total Multiplier:</b> Total multiplier = β₀ + β₁ + … + β_q = Σβ_k"),
              p("Interpretation: The long-run effect on Y of a <b>permanent</b> 1-unit increase in X. "
                "'If X goes up by 1 unit and stays there forever, by how much will Y eventually change?'"), hr()]

    # D.2
    story += [h2("D.2 — Choosing the Optimal Lag Length q"),
              p("Including too many lags creates: (1) lost observations, (2) multicollinearity, "
                "(3) overfitting."),
              p("<b>The Top-Down Procedure:</b> Start from q_max and progressively drop the highest "
                "non-significant lag:"),
              pl("1. Fit DL(q_max). Check the t-test for β_{q_max}."),
              pl("2. If β_{q_max} is not significant: drop lag q_max, refit DL(q_max − 1)."),
              pl("3. Repeat until the highest remaining lag is significant."),
              pl("4. That is your optimal lag length q."),
              p("<b>Important:</b> Do not drop intermediate insignificant lags. If β_2 is significant "
                "but β_1 is not, keep both — you cannot have lag 2 without lag 1."),
              h3("Worked Example — Safety Training")]

    dl_ex_table = [
        ["Step","Model fitted","Result","Action"],
        ["1","DL(4)","β₄: t = 0.83, p = 0.41","Not significant → Drop lag 4"],
        ["2","DL(3)","β₃: t = 1.21, p = 0.23","Not significant → Drop lag 3"],
        ["3","DL(2)","β₂: t = 1.56, p = 0.12","Not significant → Drop lag 2"],
        ["4","DL(1)","β₁: t = −2.87, p = 0.005","Significant → Stop. Optimal q = 1"],
    ]
    story.append(make_table(dl_ex_table, [1.2*cm, 2*cm, 5*cm, W-8.2*cm]))
    story.append(hr())

    # D.3
    story += [h2("D.3 — Autoregressive Model AR(1)"),
              p("Y_t = α + βX_t + γY_{t−1} + ε_t"),
              p("By including Y_{t−1}, we capture all persistence effects in a single coefficient γ.")]

    ar1_interp = [
        ["Coefficient","Interpretation"],
        ["α","Intercept"],
        ["β","Immediate effect: a 1-unit rise in X_t causes Y_t to rise by β, holding Y_{t−1} constant"],
        ["γ","Persistence coefficient: how much of last period's Y carries forward. Requires |γ| < 1"],
        ["β/(1−γ)","Total multiplier: long-run effect of a permanent 1-unit rise in X"],
    ]
    story.append(make_table(ar1_interp, [2.5*cm, W-2.5*cm]))
    story += [sp(4),
              p("<b>Proof of the total multiplier formula:</b> In long-run equilibrium, Y_t = Y_{t−1} = Y*. "
                "Then: Y* = α + βX* + γY* → Y*(1−γ) = α + βX* → Y* = α/(1−γ) + [β/(1−γ)]X*. "
                "So a 1-unit permanent increase in X* raises long-run Y* by β/(1−γ)."),
              h3("Dynamic Path After a Temporary Shock")]

    shock_table = [
        ["Period","Additional effect on Y (above baseline)"],
        ["t","β"],
        ["t+1","γ · β"],
        ["t+2","γ² · β"],
        ["t+3","γ³ · β"],
        ["t+k","γᵏ · β"],
    ]
    story.append(make_table(shock_table, [3*cm, W-3*cm]))
    story += [sp(4),
              h3("Worked Example — Education Spending and GDP Growth"),
              p("Fitted AR(1): Ŷ_t = 1.01 + 0.009 X_t + 0.627 Y_{t−1}")]

    ar1_worked = [
        ["Component","Value","Meaning"],
        ["α̂","1.01","Baseline growth when X = 0 and Y_{t−1} = 0"],
        ["β̂","0.009","A $1 increase raises GDP growth by 0.009 pp immediately"],
        ["γ̂","0.627","62.7% of last year's GDP growth persists into this year"],
        ["Total multiplier","0.009/(1−0.627) = 0.024","Permanent $1/child increase raises long-run GDP growth by 0.024 pp"],
    ]
    story.append(make_table(ar1_worked, [2.5*cm, 4.5*cm, W-7*cm]))
    story.append(hr())

    # D.4
    story += [h2("D.4 — Link Between AR(1) and DL(∞)"),
              p("AR(1) is equivalent to a DL(∞) with geometrically declining coefficients: β, βγ, βγ², βγ³, …"),
              p("Total multiplier = Σ βγᵏ = β × 1/(1−γ) = β/(1−γ)"),
              p("<b>Why does Σγᵏ = 1/(1−γ)?</b> Geometric series: S = 1 + γ + γ² + γ³ + … → "
                "S − γS = 1 → S(1−γ) = 1 → S = 1/(1−γ). Only converges when |γ| < 1.")]

    comp_table = [
        ["Feature","DL(q)","AR(1)"],
        ["Lag structure","q+1 free coefficients β₀, β₁, …, β_q","Geometric decay — only β and γ"],
        ["Parameters needed","q+1","2"],
        ["Multicollinearity","High for large q","Low (only one lag of Y needed)"],
        ["Bias when A3 violated","Unbiased (only inefficient)","Biased"],
        ["Lag structure flexibility","Completely flexible","Constrained to geometric decay"],
        ["When to prefer","Autocorrelation suspected","Parsimony matters and A3 is satisfied"],
    ]
    story.append(make_table(comp_table, [4.5*cm, 5.5*cm, W-10*cm]))
    story.append(sp(6))

    # D.5
    story += [h2("D.5 — The Three-Step Exam Workflow"),
              bold("Step 1 — Stationarity Check (Chapter TS_C)"),
              pl("1. Plot the series against time."),
              pl("2. Choose DF version (no visible trend → V1; clear trend or unsure → V2)."),
              pl("3. Run the DF regression, read the t-statistic for Y_{t−1}."),
              pl("4. Compare to −2.86 (V1 at 5%) or −3.41 (V2 at 5%)."),
              pl("5. Reject H₀ → series is stationary → use in levels."),
              pl("6. Fail to reject H₀ → unit root → take ΔY_t, re-test."),
              bold("Step 2 — Fit the Model (Chapter TS_D)"),
              pl("DL(q): Start with q = q_max. Drop highest non-significant lag. Repeat. "
                 "Report all coefficients and total multiplier = Σβ_k."),
              pl("AR(1): Fit Y_t = α + β X_t + γ Y_{t-1} + ε_t directly. "
                 "Report β, γ, and total multiplier = β/(1−γ)."),
              bold("Step 3 — Assumption Check with LMSC (Chapter TS_B)"),
              pl("1. State hypotheses: H₀: ρ = 0 vs. H₁: ρ ≠ 0."),
              pl("2. Write auxiliary regression: e_t = α₀ + α₁X_{1t} + … + α_{k+1}e_{t−1} + u_t."),
              pl("3. Compute LM = n_aux × R²_aux ~ χ²(1) under H₀."),
              pl("4. Compare to 3.841."),
              pl("5. Conclude with a full sentence.")]

    story.append(PageBreak())

    # ── FORMULA SHEET ─────────────────────────────────────────────────────────
    story += [h1("FORMULA SHEET — The Five Equations You Must Know"),
              h2("1. DL(q) Model"),
              p("Y_t = α + β₀X_t + β₁X_{t−1} + … + β_qX_{t−q} + ε_t"),
              p("Total multiplier = β₀ + β₁ + … + β_q = Σβ_k"),
              h2("2. AR(1) Model"),
              p("Y_t = α + βX_t + γY_{t−1} + ε_t"),
              p("Total multiplier = β/(1−γ) (requires |γ| < 1)"),
              h2("3. LMSC Test"),
              p("Auxiliary regression: e_t = α₀ + α₁X_{1t} + … + αₖX_{kt} + α_{k+1}e_{t−1} + u_t"),
              p("LM = n · R² ~ χ²(1) under H₀"),
              p("H₀: ρ = 0 | H₁: ρ ≠ 0 | Critical value at 5%: χ²(1) = 3.841"),
              h2("4. Dickey-Fuller Test"),
              p("Version 1 (no trend): ΔY_t = α₀ + α₁Y_{t−1} + ε_t"),
              p("Version 2 (with trend): ΔY_t = α₀ + λt + α₁Y_{t−1} + ε_t"),
              p("H₀: α₁ = 0 (unit root) | H₁: α₁ < 0 (stationary)"),
              p("Reject H₀ if t-stat is more negative than critical value (−2.86 or −3.41)."),
    ]

    story += [
        new_tag(),
        h2("5. Confidence Interval [NEW]"),
        new("95% CI for β:   β̂  ±  1.96 × SE(β̂)"),
        new("General CI:     β̂  ±  z* × SE(β̂)   where z* = 1.645 (90%), 1.960 (95%), 2.576 (99%)"),
        new("If 0 is outside the 95% CI ↔ coefficient is significant at 5% ↔ p < 0.05"),
    ]

    story.append(PageBreak())

    # ── EXAM-DAY CHECKLIST ────────────────────────────────────────────────────
    story += [h1("EXAM-DAY CHECKLIST"),
              h2("Step 1 — Stationarity (TS_C)"),
              pl("☐ Plot every variable against time"),
              pl("☐ Choose DF version (V1: no trend / V2: trend or unsure)"),
              pl("☐ Run DF on each variable, read t-stat on Y_{t−1}"),
              pl("☐ Compare to adapted critical values (NOT standard t-table)"),
              pl("☐ Unit root present? → take ΔY_t, re-test on differences"),
              h2("Step 2 — Fit the Model (TS_D)"),
              pl("☐ Model type given in question (static / DL(q) / AR(1))"),
              pl("☐ For DL: start at q_max, drop top lag while not significant"),
              pl("☐ Report all coefficients with standard errors and t-stats"),
              pl("☐ Calculate and report total multiplier (Σβ_k or β/(1−γ))"),
              pl("☐ Interpret: distinguish temporary vs. maintained; levels vs. log-returns"),
              h2("Step 3 — Assumption Check (TS_B)"),
              pl("☐ State H₀ and H₁ explicitly"),
              pl("☐ Write the auxiliary regression (all original X's + lagged residual)"),
              pl("☐ Compute LM = n_aux × R²_aux"),
              pl("☐ Compare to χ²(1) = 3.841 (or use p-value)"),
              pl("☐ Write a full conclusion sentence"),
              hr()]

    # ── COMMON EXAM PITFALLS ──────────────────────────────────────────────────
    story += [h1("COMMON EXAM PITFALLS")]

    pitfalls = [
        ('1. "Reject H₀ means non-stationary" — WRONG',
         ['For the Dickey-Fuller test: Reject H₀ means the series IS stationary (H₀ is the unit root).',
          'For the LMSC test: Reject H₀ means autocorrelation IS present (H₀ is no autocorrelation).',
          'These are opposite! Know which test you are running before concluding.']),
        ('2. "Take differences whenever the series trends" — BE CAREFUL',
         ['Only take differences if the DF test confirms a stochastic trend (unit root, |ρ| = 1).',
          'If the trend is deterministic (|ρ| < 1, λ ≠ 0), add t as a regressor instead.',
          'Over-differencing creates artificial negative autocorrelation and loses information.']),
        ('3. "Use Durbin–Watson for all models"',
         ['DW is invalid whenever Y_{t−1} appears as a regressor (AR(1) models).',
          'Always use LMSC — it works for static, DL(q), and AR(1) models.']),
        ('4. "Total multiplier = β₀ only"',
         ['For DL(q): total multiplier = β₀ + β₁ + … + β_q (sum of ALL lag coefficients).',
          'For AR(1): total multiplier = β/(1−γ), not just β.',
          'β₀ alone is the immediate effect only.']),
        ('5. "Unit changes when X is log-differenced"',
         ['If you differenced log(X), a 1-unit rise in Δln(X) means a 1 percentage point rise in '
          'the growth rate — not a 1-unit rise in the level.',
          'Interpret in terms of percentage changes.']),
        ('6. "Skip the autocorrelation test to save time"',
         ['The LMSC test is worth dedicated exam marks.',
          'Always report all five elements: H₀/H₁, the auxiliary regression, LM = n × R², '
          'comparison to 3.841, and conclusion.']),
        ('7. "Use the regular t-table for the Dickey-Fuller t-statistic"',
         ['The DF t-statistic does NOT follow a t-distribution under H₀.',
          'Standard critical values (±1.96, ±2.58) do not apply.',
          'Always use the adapted DF critical values: −2.86 (V1, 5%), −3.41 (V2, 5%).']),
        ('8. "A 95% CI that is very narrow always means a reliable result" [NEW]',
         ['If autocorrelation is present, standard errors are too small → CIs are artificially narrow.',
          'A narrow CI is only trustworthy after you have confirmed A3 is satisfied (LMSC test).',
          'Always complete Step 3 before placing confidence in your interval estimates.']),
    ]

    for head, bullets in pitfalls:
        story.append(Paragraph(head, S['pitfall_head']))
        for b in bullets:
            story.append(Paragraph(f"• {b}", S['body_left']))
        story.append(sp(6))

    story.append(PageBreak())

    # ── PRACTICE EXAM QUESTIONS — NEW ─────────────────────────────────────────
    story += [
        new_tag(),
        h1("PRACTICE EXAM QUESTIONS [NEW]"),
        new("Work through these questions yourself before checking the answers. "
            "They are structured to match common exam formats for time-series regression."),
        hr(),
    ]

    # Q1
    story += [
        h2("Question 1 — Identifying Autocorrelation"),
        new("A researcher fits the model: Y_t = α + β X_t + ε_t using 80 quarterly observations. "
            "The Durbin-Watson statistic is 0.72. She then runs the LMSC auxiliary regression and "
            "obtains R² = 0.38 with n_aux = 79."),
        new("(a) What do you conclude from the DW statistic? Why is this not sufficient?"),
        new("(b) Compute the LM statistic. What do you conclude at the 5% significance level?"),
        new("(c) What is the recommended remedy? Why is switching to an AR(1) model risky here?"),
        new("<b>Answer:</b>"),
        new("(a) DW = 0.72 is close to 0, suggesting strong positive autocorrelation (ρ ≈ 1 − 0.72/2 ≈ 0.64). "
            "However, DW alone is not sufficient as a formal test and is inappropriate if any lagged Y "
            "is included as a regressor. The LMSC test is always preferred."),
        new("(b) LM = 79 × 0.38 = 30.02. Since 30.02 > 3.841 (the 5% critical value for χ²(1)), "
            "we reject H₀ (ρ = 0). Autocorrelation is strongly present; A3 is violated."),
        new("(c) Recommended remedy: add lagged X's — switch to a DL(q) model. Switching to AR(1) "
            "is risky because if autocorrelation persists in an AR(1) model, the coefficient estimates "
            "become biased (Y_{t−1} becomes correlated with ε_t). DL with autocorrelation is only "
            "inefficient, not biased — a much lesser problem."),
        hr(),
    ]

    # Q2
    story += [
        h2("Question 2 — Stationarity and the Dickey-Fuller Test"),
        new("You have annual data on a country's inflation rate (1960–2019, n = 60 observations). "
            "The time plot shows the series fluctuating around a roughly constant level with no "
            "clear trend. You run the Dickey-Fuller test (Version 1) and obtain a t-statistic of "
            "−3.12 on the coefficient of Y_{t−1}."),
        new("(a) State the null and alternative hypotheses of the Dickey-Fuller test."),
        new("(b) Is the series stationary at the 5% significance level? At the 1% level?"),
        new("(c) Why can you NOT use the standard t-table critical value of −1.96?"),
        new("(d) Should you use Version 1 or Version 2? Is your choice here appropriate?"),
        new("<b>Answer:</b>"),
        new("(a) H₀: α₁ = 0 (series has a unit root — not stationary) vs. H₁: α₁ < 0 (series is stationary). "
            "Note: this is a one-sided test."),
        new("(b) At 5%: critical value for V1 is −2.86. Since −3.12 < −2.86, we reject H₀ → series is "
            "stationary at 5%. At 1%: critical value for V1 is −3.43. Since −3.12 > −3.43, we fail to "
            "reject H₀ → not significant at 1%. Conclusion: stationary at 5% but not at 1%."),
        new("(c) Under H₀, Y_t is a random walk — non-stationary. The standard asymptotic theory that "
            "justifies the t-distribution assumes stationarity, which fails here. The t-distribution "
            "of the DF statistic under H₀ is shifted to the left relative to the standard distribution. "
            "Using −1.96 would almost never reject H₀, even for genuinely stationary series."),
        new("(d) Version 1 (no trend) is appropriate here because the time plot showed no clear trend. "
            "If there were a visible trend, Version 2 would be required. Using Version 1 on a "
            "trending series is a misspecification; using Version 2 on a non-trending series merely "
            "loses one degree of freedom — so Version 2 is the safer default when unsure."),
        hr(),
    ]

    # Q3
    story += [
        h2("Question 3 — Distributed Lag Model and Total Multiplier"),
        new("Monthly data on advertising spend (X, €000s) and product sales (Y, units) over "
            "n = 120 months. You fit DL models with q_max = 3. Results:"),
    ]

    q3_table = [
        ["Model","Highest lag coefficient","t-statistic","p-value"],
        ["DL(3)","β₃ = −0.21","−0.88","0.381"],
        ["DL(2)","β₂ = 0.19","1.05","0.296"],
        ["DL(1)","β₁ = 0.34","2.41","0.017"],
    ]
    story.append(make_table(q3_table, [2*cm, 4*cm, 3*cm, W-9*cm], NEW_TABLE_STYLE))
    story += [
        sp(4),
        new("The final DL(1) model gives: Ŷ_t = 120 + 0.85 X_t + 0.34 X_{t−1}"),
        new("(a) Determine the optimal lag length q. Justify your answer."),
        new("(b) Interpret the coefficient β̂₀ = 0.85."),
        new("(c) Calculate the total multiplier and interpret it."),
        new("(d) Advertising spend is permanently increased by €10,000 starting in month t. "
            "What is the total long-run increase in expected monthly sales?"),
        new("<b>Answer:</b>"),
        new("(a) Optimal q = 1. Starting from q_max = 3: β₃ is not significant (p = 0.381 > 0.05) "
            "→ drop lag 3. β₂ is not significant (p = 0.296 > 0.05) → drop lag 2. β₁ is significant "
            "(p = 0.017 < 0.05) → stop. Optimal q = 1."),
        new("(b) β̂₀ = 0.85: a €1,000 increase in advertising spend in month t is associated with "
            "an immediate increase of 0.85 units in sales in month t, holding all other lagged "
            "advertising values constant (ceteris paribus)."),
        new("(c) Total multiplier = β̂₀ + β̂₁ = 0.85 + 0.34 = 1.19. Interpretation: a permanent "
            "€1,000 increase in advertising spend is associated with a long-run increase of 1.19 "
            "units in monthly sales."),
        new("(d) A permanent increase of €10,000 (= 10 × €1,000) → total long-run increase = "
            "10 × 1.19 = 11.9 units per month."),
        hr(),
    ]

    # Q4
    story += [
        h2("Question 4 — AR(1) Model"),
        new("Annual data on a firm's accident rate (Y, incidents per 1,000 workers) as a function "
            "of safety training hours (X) — n = 45 years. The LMSC test on a static model gives "
            "LM = 8.3. You switch to an AR(1) model and obtain:"),
        new("Ŷ_t = 12.4 − 0.031 X_t + 0.52 Y_{t−1}"),
        new("Standard errors: SE(β̂) = 0.010, SE(γ̂) = 0.11. "
            "LMSC on AR(1) residuals: R² = 0.021, n_aux = 44."),
        new("(a) Why did you switch from the static model to AR(1)?"),
        new("(b) Calculate the 95% confidence interval for β (the immediate effect of training)."),
        new("(c) Calculate the total multiplier. Interpret it."),
        new("(d) Run the LMSC test on the AR(1) residuals. What do you conclude?"),
        new("(e) Is the AR(1) model problematic given your answer to (d)?"),
        new("<b>Answer:</b>"),
        new("(a) The static model's LMSC gave LM = 8.3 > 3.841, rejecting H₀ — autocorrelation was "
            "detected. The static model is misspecified: the error term carries memory that should "
            "be modelled explicitly. Adding Y_{t−1} absorbs this dynamic structure."),
        new("(b) 95% CI for β: β̂ ± 1.96 × SE(β̂) = −0.031 ± 1.96 × 0.010 = −0.031 ± 0.0196 "
            "= [−0.0506, −0.0114]. Since 0 is outside this interval, the effect is significant "
            "at 5%. We are 95% confident that one additional training hour reduces the accident "
            "rate by between 0.011 and 0.051 incidents per 1,000 workers, immediately."),
        new("(c) Total multiplier = β/(1−γ) = −0.031/(1 − 0.52) = −0.031/0.48 = −0.0646. "
            "Interpretation: a permanent 1-hour increase in annual safety training reduces the "
            "long-run accident rate by approximately 0.065 incidents per 1,000 workers."),
        new("(d) LM = 44 × 0.021 = 0.924. Since 0.924 < 3.841, we fail to reject H₀. "
            "No significant autocorrelation detected in the AR(1) residuals. A3 is plausibly "
            "satisfied. ✓"),
        new("(e) No, the AR(1) model is fine here. The concern would only arise if autocorrelation "
            "were still present after adding Y_{t−1} — in that case, Y_{t−1} would be correlated "
            "with ε_t, making OLS biased. Since the LMSC test on the AR(1) residuals passes, "
            "the model is appropriately specified."),
        hr(),
    ]

    # Q5
    story += [
        h2("Question 5 — Full Three-Step Workflow"),
        new("You have quarterly Belgian data on log(real wages) [ln_W] and log(labour productivity) "
            "[ln_P], n = 80 observations. Time plots show both series trending upward. DF test results:"),
    ]

    q5_df = [
        ["Variable","DF Version","t-statistic on Y_{t−1}","Critical value (5%)","Conclusion"],
        ["ln_W — level","V2 (trend)","−2.11","−3.41","?"],
        ["ln_P — level","V2 (trend)","−1.87","−3.41","?"],
        ["Δln_W — diff","V1 (no trend)","−8.43","−2.86","?"],
        ["Δln_P — diff","V1 (no trend)","−7.91","−2.86","?"],
    ]
    story.append(make_table(q5_df,
        [3*cm, 3*cm, 4*cm, 3.5*cm, W-13.5*cm], NEW_TABLE_STYLE))
    story += [
        sp(4),
        new("After differencing and fitting DL(q) with q_max = 2, the optimal model is DL(1):"),
        new("ΔŶ_t = 0.002 + 0.61 ΔP_t + 0.22 ΔP_{t−1}"),
        new("LMSC auxiliary regression: n_aux = 78, R²_aux = 0.009"),
        new("(a) Fill in the 'Conclusion' column of the DF table above."),
        new("(b) Why do you use first differences rather than levels?"),
        new("(c) Interpret β̂₀ = 0.61 in context."),
        new("(d) Compute the total multiplier. Interpret it."),
        new("(e) Conduct the LMSC test. Conclude."),
        new("<b>Answer:</b>"),
        new("(a) ln_W level: −2.11 > −3.41 → Fail to reject H₀ → unit root. "
            "ln_P level: −1.87 > −3.41 → Fail to reject H₀ → unit root. "
            "Δln_W: −8.43 < −2.86 → Reject H₀ → stationary ✓. "
            "Δln_P: −7.91 < −2.86 → Reject H₀ → stationary ✓."),
        new("(b) Both series have unit roots (stochastic trends). Using them in levels would risk "
            "spurious regression — t-statistics and R² would not have their standard interpretations. "
            "First differencing renders both series stationary, allowing valid inference."),
        new("(c) β̂₀ = 0.61: a 1 percentage point increase in labour productivity growth this quarter "
            "is associated with a 0.61 percentage point increase in real wage growth this same quarter, "
            "holding the lagged change in productivity constant."),
        new("(d) Total multiplier = 0.61 + 0.22 = 0.83. Interpretation: a permanent 1 pp increase "
            "in quarterly productivity growth is associated with a long-run 0.83 pp increase in "
            "real wage growth per quarter."),
        new("(e) LM = 78 × 0.009 = 0.702. Since 0.702 < 3.841, we fail to reject H₀: ρ = 0. "
            "No significant autocorrelation detected. Assumption A3 is plausibly satisfied. "
            "The model is well-specified. ✓"),
    ]

    story.append(PageBreak())

    # ── ONE-PAGE SUMMARY ──────────────────────────────────────────────────────
    story += [h1("ONE-PAGE SUMMARY")]
    story.append(code_block(
"FOUNDATIONS  Regression: Y = α + βX + ε. OLS finds best-fitting β̂.\n"
"             R² measures fit (0–1). t-statistics test if β ≠ 0.\n"
"             p-value < 0.05 → significant.\n"
"             95% CI = β̂ ± 1.96×SE. If 0 not in CI → significant.\n"
"             Five classical assumptions must hold.\n\n"
"RECOGNISE    Time series: order matters. Define lags X_{t-k} and differences ΔX_t.\n"
"             Watch sample size (n > 100 ideal). Use real monetary values.\n\n"
"STABILISE    Time plot + Dickey-Fuller on every variable.\n"
"             Deterministic trend (λ≠0, |ρ|<1)? Add t as regressor.\n"
"             Stochastic trend / unit root (|ρ|=1)? Take first differences.\n"
"             DF uses special critical values (−2.86 or −3.41), NOT ±1.96.\n\n"
"             ρ SIZES: ρ=0 (none) | 0<ρ≤0.3 (weak) | 0.3<ρ≤0.6 (moderate)\n"
"                      0.6<ρ<1 (strong) | ρ→1 (near unit root).\n\n"
"MODEL        Fit DL(q) or AR(1) on stationary variables.\n"
"             DL(q): top-down selection of q; total multiplier = Σβ_k.\n"
"             AR(1): total multiplier = β/(1−γ); requires |γ| < 1.\n"
"             Interpret: temporary vs. maintained, log-returns vs. units.\n\n"
"DIAGNOSE     LMSC test: auxiliary regression with lagged residual.\n"
"             LM = n·R² ~ χ²(1). Critical value = 3.841 at 5%.\n"
"             Reject H₀ → autocorrelation → re-specify (prefer DL over AR).\n"
"             DW statistic: quick check only (NOT valid for AR models).\n\n"
"PITFALL GRID DF test: Reject H₀ = STATIONARY (H₀ is unit root).\n"
"             LMSC:    Reject H₀ = AUTOCORRELATION PRESENT (H₀ is none).\n"
"             These are OPPOSITE conclusions from rejecting H₀!"))

    story.append(hr())
    story.append(Paragraph("End of Complete Beginner's Guide to Time Series Regression — Updated Edition",
        ParagraphStyle('end', fontName='Helvetica-Oblique', fontSize=9,
                       alignment=TA_CENTER, textColor=colors.grey)))

    return story


def main():
    out = "/home/user/BabyPluto/TimeSeries_BeginnerGuide_Updated.pdf"
    doc = SimpleDocTemplate(
        out,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
        title="Statistics — Time Series Regression: Complete Beginner's Guide (Updated)",
        author="Updated Edition",
    )
    story = build_story()
    doc.build(story)
    print(f"PDF written to {out}")

if __name__ == "__main__":
    main()
