"""
Generate an enhanced Time Series Study Guide PDF.
Uses DejaVu TrueType fonts for full Unicode / Greek-letter support.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# ---------------------------------------------------------------------------
# Register DejaVu fonts (full Unicode, including Greek)
# ---------------------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DejaVu",         FONT_DIR + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold",    FONT_DIR + "DejaVuSans-Bold.ttf"))
# Only Regular and Bold are available for DejaVuSans; use Mono-Oblique for italic
pdfmetrics.registerFont(TTFont("DejaVu-Italic",  FONT_DIR + "DejaVuSansMono-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-BoldIt",  FONT_DIR + "DejaVuSansMono-BoldOblique.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuMono",     FONT_DIR + "DejaVuSansMono.ttf"))

# ---------------------------------------------------------------------------
# Colour palette (matching the original guide)
# ---------------------------------------------------------------------------
C_TEAL      = colors.HexColor("#1B6B7B")   # TS_A chapter header
C_OLIVE     = colors.HexColor("#4A6741")   # TS_B chapter header
C_BROWN     = colors.HexColor("#7B3A10")   # TS_C chapter header
C_PURPLE    = colors.HexColor("#5C2D80")   # TS_D chapter header
C_GOLD      = colors.HexColor("#D4A017")   # KEY POINT / EXAM RECIPE label
C_GOLD_BG   = colors.HexColor("#FFF8DC")   # KEY POINT background
C_BLUE_LBL  = colors.HexColor("#2C4E8A")   # FORMULA label
C_BLUE_BG   = colors.HexColor("#E8F0FA")   # FORMULA background
C_GREEN_LBL = colors.HexColor("#3A6B35")   # INTERPRETATION label
C_GREEN_BG  = colors.HexColor("#EAF4E8")   # INTERPRETATION background
C_PURPLE_LBL= colors.HexColor("#5C2D80")   # SPSS label
C_PURPLE_BG = colors.HexColor("#F2EAFA")   # SPSS background
C_RED_LBL   = colors.HexColor("#8B0000")   # WATCH OUT label
C_RED_BG    = colors.HexColor("#FCE8E8")   # WATCH OUT background
C_INTRO_LBL = colors.HexColor("#1B4F72")   # NEW CONCEPT label
C_INTRO_BG  = colors.HexColor("#D6EAF8")   # NEW CONCEPT background
C_LGRAY     = colors.HexColor("#F5F5F5")   # table alt row
C_WHITE     = colors.white
C_BLACK     = colors.black

W, H = A4  # 595.27 x 841.89 pts

# ---------------------------------------------------------------------------
# Paragraph styles
# ---------------------------------------------------------------------------
def make_style(name, font="DejaVu", size=10, leading=14, color=C_BLACK,
               align=TA_LEFT, space_before=0, space_after=4,
               left_indent=0, right_indent=0, bold=False):
    f = "DejaVu-Bold" if bold else font
    return ParagraphStyle(
        name,
        fontName=f,
        fontSize=size,
        leading=leading,
        textColor=color,
        alignment=align,
        spaceBefore=space_before,
        spaceAfter=space_after,
        leftIndent=left_indent,
        rightIndent=right_indent,
    )

NORMAL      = make_style("normal", size=10, leading=14)
NORMAL_J    = make_style("normal_j", size=10, leading=14, align=TA_JUSTIFY)
SMALL       = make_style("small", size=8.5, leading=12)
BOLD        = make_style("bold", font="DejaVu-Bold", size=10, leading=14)
ITALIC      = make_style("italic", font="DejaVu-Italic", size=10, leading=14)
H1          = make_style("h1", font="DejaVu-Bold", size=22, leading=28,
                          color=C_WHITE, align=TA_CENTER)
H2          = make_style("h2", font="DejaVu-Bold", size=15, leading=20,
                          color=C_WHITE, align=TA_CENTER)
H3          = make_style("h3", font="DejaVu-Bold", size=13, leading=18,
                          color=C_WHITE)
SECTION     = make_style("section", font="DejaVu-Bold", size=13, leading=18,
                          color=C_TEAL, space_before=10)
SUBSECTION  = make_style("subsection", font="DejaVu-Bold", size=11, leading=16,
                          color=C_TEAL, space_before=6)
BOX_LABEL   = make_style("box_label", font="DejaVu-Bold", size=9, leading=13,
                          color=C_WHITE)
BOX_CONTENT = make_style("box_content", size=10, leading=14, left_indent=4)
BOX_ITALIC  = make_style("box_italic", font="DejaVu-Italic", size=10,
                          leading=14, left_indent=4)
BULLET      = make_style("bullet", size=10, leading=14, left_indent=14)
FORMULA_S   = make_style("formula_s", font="DejaVu-Bold", size=10.5, leading=16,
                          align=TA_CENTER)
COVER_SUB   = make_style("cover_sub", font="DejaVu-Italic", size=13, leading=18,
                          color=C_WHITE, align=TA_CENTER)
COVER_TINY  = make_style("cover_tiny", font="DejaVu-Italic", size=10, leading=14,
                          color=C_WHITE, align=TA_CENTER)
PAGE_TITLE  = make_style("page_title", font="DejaVu-Bold", size=18, leading=24,
                          color=C_WHITE, align=TA_CENTER)
TBLCELL     = make_style("tblcell", size=9.5, leading=13)
TBLHDR      = make_style("tblhdr", font="DejaVu-Bold", size=9.5, leading=13,
                          color=C_WHITE, align=TA_CENTER)
WARN        = make_style("warn", font="DejaVu-Bold", size=10, leading=14,
                          color=C_RED_LBL)
NEW_LBL     = make_style("new_lbl", font="DejaVu-Bold", size=9, leading=13,
                          color=C_WHITE)

# ---------------------------------------------------------------------------
# Helper builders
# ---------------------------------------------------------------------------
def spacer(h=6):
    return Spacer(1, h)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CCCCCC"),
                      spaceAfter=4, spaceBefore=4)

def para(text, style=NORMAL):
    return Paragraph(text, style)

def bullet(text, style=BULLET):
    return Paragraph(f"• {text}", style)

def _label_cell(text, bg, style=BOX_LABEL):
    return Table(
        [[Paragraph(text, style)]],
        colWidths=[3.2*cm],
        style=TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), bg),
            ("TOPPADDING",    (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("LEFTPADDING",   (0,0), (-1,-1), 6),
            ("RIGHTPADDING",  (0,0), (-1,-1), 4),
        ])
    )

def _content_cell(rows, bg, content_style=BOX_CONTENT):
    cells = [[Paragraph(r, content_style) if isinstance(r, str)
              else r] for r in rows]
    return Table(
        cells,
        colWidths=[13.5*cm],
        style=TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), bg),
            ("TOPPADDING",    (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("LEFTPADDING",   (0,0), (-1,-1), 8),
            ("RIGHTPADDING",  (0,0), (-1,-1), 6),
        ])
    )

def box(label, label_bg, content_rows, content_bg, content_style=BOX_CONTENT):
    """Two-column coloured box: [LABEL | CONTENT]."""
    lc = _label_cell(label, label_bg)
    cc = _content_cell(content_rows, content_bg, content_style)
    t = Table([[lc, cc]], colWidths=[3.2*cm, 13.5*cm])
    t.setStyle(TableStyle([
        ("VALIGN",  (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 0),
    ]))
    return t

def key_point(rows):
    return box("KEY POINT",      C_GOLD,       rows, C_GOLD_BG)

def formula(rows):
    return box("FORMULA",        C_BLUE_LBL,   rows, C_BLUE_BG, FORMULA_S)

def interpretation(rows):
    return box("INTERPRETATION", C_GREEN_LBL,  rows, C_GREEN_BG)

def spss_box(rows):
    return box("SPSS",           C_PURPLE_LBL, rows, C_PURPLE_BG)

def watch_out(rows):
    return box("WATCH OUT",      C_RED_LBL,    rows, C_RED_BG)

def new_concept(rows):
    return box("NEW CONCEPT",    C_INTRO_LBL,  rows, C_INTRO_BG)

def chapter_header(code, title, subtitle, bg):
    """Full-width coloured chapter banner."""
    data = [[Paragraph(code, SMALL),
             Paragraph(title, H2),
             Paragraph(subtitle, COVER_TINY)]]
    t = Table([
        [Paragraph(f"<b>CHAPTER {code}</b>", make_style("ch_code", font="DejaVu-Bold",
                    size=10, leading=14, color=C_WHITE))],
        [Paragraph(title, PAGE_TITLE)],
        [Paragraph(subtitle, COVER_TINY)],
    ], colWidths=[W - 4.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
    ]))
    return t

def section_toc(rows):
    """Section overview table at the start of each chapter."""
    header = [Paragraph("<b>Section</b>", TBLHDR),
              Paragraph("<b>Topic</b>", TBLHDR),
              Paragraph("<b>You should be able to…</b>", TBLHDR)]
    data = [header] + [[Paragraph(f"<b>{r[0]}</b>", TBLCELL),
                         Paragraph(r[1], TBLCELL),
                         Paragraph(r[2], TBLCELL)] for r in rows]
    t = Table(data, colWidths=[2*cm, 5.5*cm, 9.2*cm])
    style = [
        ("BACKGROUND",    (0,0), (-1,0),  C_TEAL),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#BBBBBB")),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [C_WHITE, C_LGRAY]),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    t.setStyle(TableStyle(style))
    return t

def two_col_table(headers, rows, col_widths, hdr_bg=C_TEAL):
    hrow = [Paragraph(f"<b>{h}</b>", TBLHDR) for h in headers]
    data = [hrow]
    for i, r in enumerate(rows):
        bg = C_WHITE if i % 2 == 0 else C_LGRAY
        data.append([Paragraph(c, TBLCELL) for c in r])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  hdr_bg),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#BBBBBB")),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [C_WHITE, C_LGRAY]),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    return t

def workflow_table(steps):
    """Coloured 3-column workflow box."""
    hrow = [Paragraph(f"<b>{s[0]}</b>", TBLHDR) for s in steps]
    brow = [Paragraph(s[1], TBLCELL) for s in steps]
    colours = [C_BROWN, C_PURPLE, C_OLIVE]
    t = Table([hrow, brow], colWidths=[5.5*cm]*3)
    style_cmds = [
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#AAAAAA")),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    for i, c in enumerate(colours):
        style_cmds.append(("BACKGROUND", (i,0), (i,0), c))
    t.setStyle(TableStyle(style_cmds))
    return t

# ===========================================================================
# DOCUMENT CONTENT
# ===========================================================================

def build_story():
    s = []  # story list

    # -----------------------------------------------------------------------
    # COVER PAGE
    # -----------------------------------------------------------------------
    cover = Table([
        [Paragraph("STATISTICS — STUDY GUIDE", make_style("cov1", font="DejaVu-Bold",
                    size=16, leading=22, color=C_WHITE, align=TA_CENTER))],
        [Paragraph("PART 2", make_style("cov2", font="DejaVu-Bold",
                    size=13, leading=18, color=C_WHITE, align=TA_CENTER))],
        [Spacer(1, 8)],
        [Paragraph("Time Series", make_style("cov3", font="DejaVu-Bold",
                    size=30, leading=38, color=C_WHITE, align=TA_CENTER))],
        [Spacer(1, 6)],
        [Paragraph("Cautions · Autocorrelation · Stationarity · Dynamic Models",
                    make_style("cov4", font="DejaVu-Italic", size=13, leading=18,
                               color=C_WHITE, align=TA_CENTER))],
        [Spacer(1, 10)],
        [Paragraph("Enhanced Edition — Beginner-Friendly with Prerequisite Foundations",
                    make_style("cov5", font="DejaVu-Italic", size=10, leading=14,
                               color=colors.HexColor("#FFD080"), align=TA_CENTER))],
    ], colWidths=[W - 4.4*cm])
    cover.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_BROWN),
        ("TOPPADDING",    (0,0), (-1,-1), 14),
        ("BOTTOMPADDING", (0,0), (-1,-1), 14),
        ("LEFTPADDING",   (0,0), (-1,-1), 20),
        ("RIGHTPADDING",  (0,0), (-1,-1), 20),
    ]))
    s.append(Spacer(1, 3*cm))
    s.append(cover)
    s.append(Spacer(1, 1*cm))

    # legend table
    legend = [
        [Paragraph("<b>KEY POINT</b>", make_style("lg", font="DejaVu-Bold", size=9,
                    color=C_WHITE)), Paragraph("Key concept or definition — must know.", TBLCELL)],
        [Paragraph("<b>FORMULA</b>", make_style("lg2", font="DejaVu-Bold", size=9,
                    color=C_WHITE)), Paragraph("Equation as it appears on the formula sheet.", TBLCELL)],
        [Paragraph("<b>INTERPRETATION</b>", make_style("lg3", font="DejaVu-Bold", size=9,
                    color=C_WHITE)), Paragraph("How to read/apply the result in plain English.", TBLCELL)],
        [Paragraph("<b>NEW CONCEPT</b>", make_style("lg4", font="DejaVu-Bold", size=9,
                    color=C_WHITE)), Paragraph("Background explanation for readers new to statistics.", TBLCELL)],
        [Paragraph("<b>SPSS</b>", make_style("lg5", font="DejaVu-Bold", size=9,
                    color=C_WHITE)), Paragraph("Menu path and what to click in SPSS.", TBLCELL)],
        [Paragraph("<b>WATCH OUT</b>", make_style("lg6", font="DejaVu-Bold", size=9,
                    color=C_WHITE)), Paragraph("Common exam pitfall or subtle distinction.", TBLCELL)],
    ]
    bgs = [C_GOLD, C_BLUE_LBL, C_GREEN_LBL, C_INTRO_LBL, C_PURPLE_LBL, C_RED_LBL]
    leg_table = Table(legend, colWidths=[3.8*cm, 12.9*cm])
    leg_style = [
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#CCCCCC")),
    ]
    for i, bg in enumerate(bgs):
        leg_style.append(("BACKGROUND", (0,i), (0,i), bg))
    leg_table.setStyle(TableStyle(leg_style))
    s.append(Paragraph("<b>How to read this guide</b>",
                        make_style("htitle", font="DejaVu-Bold", size=12, leading=16,
                                   align=TA_CENTER, space_before=6, space_after=8)))
    s.append(leg_table)
    s.append(PageBreak())

    # -----------------------------------------------------------------------
    # PREREQUISITE CHAPTER: Statistics Foundations for Beginners
    # -----------------------------------------------------------------------
    prereq_header = Table([
        [Paragraph("PREREQUISITE", make_style("prq", font="DejaVu-Bold", size=10, color=C_WHITE))],
        [Paragraph("Statistics Foundations", PAGE_TITLE)],
        [Paragraph("Everything you need before reading this guide",  COVER_TINY)],
    ], colWidths=[W - 4.4*cm])
    prereq_header.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_INTRO_LBL),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
    ]))
    s.append(prereq_header)
    s.append(spacer(10))
    s.append(para(
        "If you have never studied statistics before, read this section first. It explains every "
        "concept that the rest of the guide takes for granted — regression, hypothesis testing, "
        "Greek notation, and more. If you have already taken an introductory statistics course, "
        "you can skip ahead to Chapter TS_A.", NORMAL_J))
    s.append(spacer(10))

    # P0 – Greek letters
    s.append(para("P.0 — Greek Letters and Mathematical Notation", SECTION))
    s.append(hr())
    s.append(new_concept([
        "<b>Why Greek letters?</b> Statistics uses Greek letters to distinguish "
        "<i>population</i> quantities (the true, unknown values) from <i>sample</i> quantities "
        "(the estimates we compute from data). Here are the ones used throughout this guide:",
    ]))
    s.append(spacer(6))
    greek_rows = [
        ["Symbol", "Name", "What it usually means in this guide"],
        ["α (alpha)", "alpha", "Constant / intercept in a model; also significance level of a test"],
        ["β (beta)", "beta", "Slope coefficient — how much Y changes when X changes by 1"],
        ["γ (gamma)", "gamma", "Coefficient on a lagged Y variable in AR models"],
        ["ε (epsilon)", "epsilon", "Error term — the part of Y that the model cannot explain"],
        ["μ (mu)", "mu", "True (population) mean of a variable"],
        ["σ (sigma)", "sigma", "Standard deviation; σ² is variance"],
        ["σ² (sigma²)", "sigma squared", "Variance — average squared distance from the mean"],
        ["ρ (rho)", "rho", "Autocorrelation coefficient between errors one period apart"],
        ["λ (lambda)", "lambda", "Coefficient on a time-trend variable"],
        ["δ (delta)", "delta", "Slope of the long-run trend in certain AR models"],
        ["χ² (chi-sq.)", "chi-squared", "A distribution used in hypothesis tests (e.g. LMSC)"],
        ["Δ (Delta)", "Delta", "Difference operator: ΔX_t = X_t − X_{t−1}"],
        ["Σ (Sigma)", "Sigma", "Summation: Σβ_k means β_0 + β_1 + … + β_q"],
    ]
    greek_table = Table(
        [[Paragraph(f"<b>{r[0]}</b>" if i==0 else r[0], TBLHDR if i==0 else TBLCELL),
          Paragraph(f"<b>{r[1]}</b>" if i==0 else r[1], TBLHDR if i==0 else TBLCELL),
          Paragraph(f"<b>{r[2]}</b>" if i==0 else r[2], TBLHDR if i==0 else TBLCELL)]
         for i, r in enumerate(greek_rows)],
        colWidths=[3*cm, 2.8*cm, 10.9*cm]
    )
    greek_table.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  C_INTRO_LBL),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#BBBBBB")),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [C_WHITE, C_LGRAY]),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    s.append(greek_table)
    s.append(spacer(10))

    # P1 – What is regression?
    s.append(para("P.1 — What Is Regression?", SECTION))
    s.append(hr())
    s.append(new_concept([
        "<b>The core idea.</b> Regression is a mathematical tool that finds the best-fitting "
        "straight line (or curve) through a cloud of data points. We want to explain or predict "
        "one variable (Y, called the <i>dependent</i> or <i>response</i> variable) using one or "
        "more other variables (X, called <i>independent</i> or <i>explanatory</i> variables).",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Example.</b> Suppose we want to understand how education spending (X, in dollars per "
        "child) relates to GDP growth (Y, in %). We collect data for many years and find the line "
        "that best fits those data points. That line is our regression model.",
    ]))
    s.append(spacer(6))
    s.append(para("The simple (one X) linear regression equation is:", NORMAL))
    s.append(spacer(4))
    s.append(formula(["Y_t = β₀ + β₁ X_t + ε_t",
                       "β₀ = intercept (value of Y when X = 0)",
                       "β₁ = slope (how much Y changes for a 1-unit increase in X)",
                       "ε_t = error / residual (the part of Y not explained by X)"]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Multiple regression</b> simply adds more X variables: "
        "Y = β₀ + β₁X₁ + β₂X₂ + … + βₖXₖ + ε. "
        "Everything in this guide is a special case of multiple regression applied to data "
        "collected over time."
    ]))
    s.append(spacer(10))

    # P2 – What is OLS?
    s.append(para("P.2 — What Is OLS (Ordinary Least Squares)?", SECTION))
    s.append(hr())
    s.append(new_concept([
        "<b>OLS</b> is the most common method for estimating regression coefficients. "
        "It finds the values of β₀, β₁, … that <i>minimise</i> the sum of squared residuals — "
        "i.e. it finds the line that is as close as possible to all data points at once.",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>BLUE</b> stands for <i>Best Linear Unbiased Estimator</i>. Under the five classical "
        "assumptions (see P.4), OLS is proven to be the best possible way to estimate β — "
        "'best' meaning it has the smallest possible variance among all unbiased linear methods."
    ]))
    s.append(spacer(10))

    # P3 – Residuals
    s.append(para("P.3 — Residuals, R², and Model Fit", SECTION))
    s.append(hr())
    s.append(new_concept([
        "<b>Residual (e_t).</b> The difference between the actual observed value and the value "
        "predicted by the regression line: e_t = Y_t − Ŷ_t. "
        "A good model has residuals that look like random noise — no pattern.",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>R² (R-squared).</b> A number between 0 and 1 that tells you how much of the "
        "variation in Y is explained by your model. R² = 0.80 means the model explains 80% of "
        "the variation. A higher R² is generally better, but a high R² does not automatically "
        "mean the model is correct — especially with time-series data (see spurious regression, "
        "Section C.1).",
    ]))
    s.append(spacer(10))

    # P4 – Classical assumptions
    s.append(para("P.4 — The Five Classical Assumptions (A1–A5)", SECTION))
    s.append(hr())
    s.append(para(
        "OLS is BLUE only when these five conditions hold. The time-series part of this course "
        "focuses on what happens when A3 fails.", NORMAL_J))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>A1: E(ε_t) = 0</b> — On average the errors are zero. The model is neither "
        "systematically too high nor too low.",
    ]))
    s.append(spacer(4))
    s.append(new_concept([
        "<b>A2: Var(ε_t) = σ² (constant)</b> — Called <i>homoskedasticity</i>. The spread "
        "of errors is the same across all observations. If the spread changes (e.g. errors "
        "get bigger over time), we have <i>heteroskedasticity</i> and A2 is violated.",
    ]))
    s.append(spacer(4))
    s.append(new_concept([
        "<b>A3: cov(ε_i, ε_j) = 0 for i ≠ j</b> — Errors are uncorrelated with each other. "
        "This is the assumption most likely to fail in time-series data. If yesterday's error "
        "influences today's error, A3 is violated — we call this <i>autocorrelation</i>.",
    ]))
    s.append(spacer(4))
    s.append(new_concept([
        "<b>A4: X variables are non-random and not exact linear combinations of each other.</b> "
        "The second part means no <i>perfect multicollinearity</i> — you cannot have one X "
        "variable that is simply a multiple of another.",
    ]))
    s.append(spacer(4))
    s.append(new_concept([
        "<b>A5 (optional): ε is normally distributed.</b> Needed for exact t- and F-tests in "
        "small samples. With large samples, the Central Limit Theorem makes normality less critical.",
    ]))
    s.append(spacer(10))

    # P5 – Hypothesis testing
    s.append(para("P.5 — Hypothesis Testing: H₀, H₁, p-values, and Rejection", SECTION))
    s.append(hr())
    s.append(new_concept([
        "<b>The logic of hypothesis testing.</b> We start with a <i>null hypothesis</i> (H₀) "
        "— a default assumption we want to challenge. We then compute a test statistic from the "
        "data and ask: 'How likely is it to see a result this extreme if H₀ were actually true?'",
    ]))
    s.append(spacer(6))
    s.append(two_col_table(
        ["Term", "Plain-English meaning"],
        [
            ["H₀ (null hypothesis)", "The 'boring' baseline — e.g. 'there is no effect', 'the coefficient is zero', 'there is no autocorrelation'"],
            ["H₁ (alternative hypothesis)", "What we suspect might be true if H₀ is wrong — e.g. 'there IS an effect'"],
            ["Test statistic (t, F, LM, …)", "A number computed from data that measures how far the data are from what H₀ predicts"],
            ["p-value", "Probability of getting a test statistic this extreme if H₀ were true. Small p-value = strong evidence against H₀"],
            ["Significance level (α)", "The threshold we set in advance (commonly 0.05). If p-value < α, we reject H₀"],
            ["Reject H₀", "The data give enough evidence to conclude H₀ is false. Does NOT prove H₁ with certainty"],
            ["Fail to reject H₀", "Not enough evidence against H₀. Does NOT prove H₀ is true — the test just could not disprove it"],
            ["Critical value", "The threshold value of the test statistic beyond which we reject H₀"],
        ],
        [4.5*cm, 12.2*cm],
    ))
    s.append(spacer(6))
    s.append(watch_out([
        "<b>Rejecting H₀ is not always 'good news.'</b> In the LMSC autocorrelation test, "
        "rejecting H₀ means autocorrelation IS present — that is a problem. "
        "In the Dickey-Fuller test, rejecting H₀ means the series IS stationary — that is good news. "
        "Always read the hypotheses carefully before interpreting a result."
    ]))
    s.append(spacer(10))

    # P6 – t-test and F-test
    s.append(para("P.6 — The t-test and the F-test", SECTION))
    s.append(hr())
    s.append(new_concept([
        "<b>t-test for a single coefficient.</b> Tests whether one regression coefficient "
        "(say β₁) is significantly different from zero. "
        "H₀: β₁ = 0 (X has no effect on Y). "
        "The t-statistic = (estimated β₁) / (standard error of β₁). "
        "If |t| > critical value (roughly 2 for large samples at 5% significance), reject H₀.",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>F-test (ANOVA).</b> Tests whether the model as a whole is significant — "
        "i.e. whether at least one X variable has a non-zero effect on Y. "
        "H₀: all β coefficients are zero. A significant F-test (small p-value) means the model "
        "explains a meaningful part of Y.",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Standard error (SE).</b> A measure of how precisely we have estimated a coefficient. "
        "A smaller SE means more precision. SE depends on the sample size and the variability "
        "of the data. When autocorrelation is present, the formula for SE becomes incorrect "
        "(see Section B.3), making t- and F-tests unreliable.",
    ]))
    s.append(spacer(10))

    # P7 – Chi-squared distribution
    s.append(para("P.7 — The Chi-Squared (χ²) Distribution", SECTION))
    s.append(hr())
    s.append(new_concept([
        "The <b>chi-squared (χ²) distribution</b> is a probability distribution used in "
        "several statistical tests, including the LMSC autocorrelation test in this guide. "
        "Like the t-distribution, it has a parameter called <i>degrees of freedom</i> (df). "
        "You do not need to know how to compute χ² values by hand — the p-value from SPSS "
        "tells you directly whether to reject H₀.",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Degrees of freedom (df).</b> Roughly speaking, df = the number of independent "
        "pieces of information used by a test. In the LMSC test df = 1 for a first-order test "
        "(df increases if you test for higher-order autocorrelation). "
        "In the Dickey-Fuller test, df is large (determined by sample size).",
    ]))
    s.append(PageBreak())

    # -----------------------------------------------------------------------
    # OVERVIEW PAGE
    # -----------------------------------------------------------------------
    s.append(para("<b>Overview — the time-series workflow</b>",
                   make_style("ov_title", font="DejaVu-Bold", size=14, leading=20,
                              space_before=4, space_after=8)))
    s.append(para(
        "When you fit a regression model on time-series data, you go through the same four "
        "big steps every time. This guide is structured around them:", NORMAL_J))
    s.append(spacer(8))
    wf = workflow_table([
        ("Recognise\nTS_A — Cautions",
         "Time-series ≠ cross-section. Define lags X_{t−q} and differences ΔX_t. "
         "Beware too-few data."),
        ("Diagnose\nTS_B — Autocorrelation",
         "Classical assumption A3 violated? Detect via LMSC test. Choose a dynamic model as solution."),
        ("Stabilise\nTS_C — Stationarity",
         "Spurious regression risk. Use Dickey-Fuller. Detrend or difference if needed."),
    ])
    s.append(wf)
    s.append(spacer(4))
    model_step = Table([
        [Paragraph("<b>Model\nTS_D — Dynamic models</b>", TBLHDR)],
        [Paragraph("Fit DL(q) or AR(1). Determine optimal lag length. Interpret the total multiplier.", TBLCELL)],
    ], colWidths=[W - 4.4*cm])
    model_step.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), C_PURPLE),
        ("BACKGROUND", (0,1), (0,1), C_LGRAY),
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#AAAAAA")),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    s.append(model_step)
    s.append(spacer(10))

    exam_recipe = Table([
        [Paragraph("<b>EXAM RECIPE</b>", make_style("er_lbl", font="DejaVu-Bold", size=10,
                    color=C_WHITE))],
        [Paragraph(
            "<b>The exam steps.</b> In an exam question on time-series regression you will be "
            "told which kind of model to fit (static, DL(q), or AR(1)). You then go through:", BOX_CONTENT)],
        [Paragraph("• <b>Step 1</b> — Check stationarity of every variable: time plot + "
                   "Dickey-Fuller. If non-stationary, take differences (or model a deterministic trend).", BULLET)],
        [Paragraph("• <b>Step 2</b> — Fit the model. For DL(q): determine the optimal lag "
                   "length. Report coefficients and the total multiplier.", BULLET)],
        [Paragraph("• <b>Step 3</b> — Check assumptions, in particular autocorrelation with "
                   "the LMSC test.", BULLET)],
    ], colWidths=[W - 4.4*cm])
    exam_recipe.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), C_GOLD),
        ("BACKGROUND", (0,1), (-1,-1), C_GOLD_BG),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
    ]))
    s.append(exam_recipe)
    s.append(spacer(10))

    s.append(para("Big picture — connection with Part 1 (MR)", SECTION))
    s.append(hr())
    s.append(para(
        "Everything you learned in multiple linear regression still applies: model specification, "
        "t-test, ANOVA, R², the 5 classical assumptions, residual plots, multicollinearity, "
        "heteroskedasticity. The time-series part adds three issues on top:", NORMAL_J))
    s.append(spacer(4))
    s.append(bullet("<b>Autocorrelation</b> — assumption A3 (uncorrelated errors) can fail "
                    "because errors close in time are similar."))
    s.append(bullet("<b>Spurious regression / stationarity</b> — variables that drift over "
                    "time can look related even when they are not."))
    s.append(bullet("<b>Dynamic effects</b> — past values of X (and sometimes Y) influence "
                    "current Y. New models: DL(q), AR(1)."))
    s.append(PageBreak())

    # -----------------------------------------------------------------------
    # CHAPTER TS_A
    # -----------------------------------------------------------------------
    s.append(chapter_header("TS_A", "Cautions",
                             "Differences between cross-section and time-series data; lags and differences",
                             C_TEAL))
    s.append(spacer(10))
    s.append(section_toc([
        ("A.1", "Cross-section vs. time series",
         "Explain how time-series data differ and why we must be careful."),
        ("A.2", "Lagged variables X_{t−1}, X_{t−2}, …",
         "Build lags in SPSS; recognise LAG(x,1) notation; interpret."),
        ("A.3", "Difference variables ΔX_t",
         "Build differences in SPSS; recognise DIFF(x,1); interpret."),
        ("A.4", "The three problems",
         "Why we must be careful: data, autocorrelation, stationarity."),
    ]))
    s.append(spacer(12))

    s.append(para("A.1 — Cross-section vs. time-series data", SECTION))
    s.append(hr())
    s.append(key_point([
        "<b>Cross-section.</b> Data on many economic units at one moment in time. "
        "The order of rows does not matter; observations are interchangeable. "
        "Notation X_i, with i the individual.",
        "<b>Time-series.</b> Data on one economic unit collected over time. "
        "The order of rows carries information — shuffling destroys it. "
        "Notation X_t, with t the time index.",
        "<b>Panel data.</b> Both at once — many units over many time periods "
        "(not exam material here, but worth keeping in mind).",
    ]))
    s.append(spacer(8))
    s.append(para("<b>Example — hourly wage</b>", SUBSECTION))
    s.append(para(
        "<b>Cross-section:</b> hourly wage for a sample of Belgian employees in 2010 — "
        "one observation per person.", NORMAL))
    s.append(para(
        "<b>Time-series:</b> average hourly wage for the Belgian population in 2008, 2009, "
        "2010, … — one observation per year.", NORMAL))
    s.append(new_concept([
        "<b>Why does the order matter?</b> In a cross-section, observation 50 has nothing "
        "special to do with observation 49 — they are just two different people. "
        "In a time-series, today's value often depends on yesterday's value (e.g. today's "
        "inflation is close to last month's inflation). Ignoring this structure leads to "
        "wrong conclusions.",
    ]))
    s.append(spacer(10))

    s.append(para("A.2 — Lagged variables", SECTION))
    s.append(hr())
    s.append(para(
        "A <b>lagged variable</b> shifts the time index backwards. Notation:", NORMAL))
    s.append(spacer(4))
    s.append(formula(["X_{t−1}, X_{t−2}, …, X_{t−q}"]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>What does 'lag' mean in practice?</b> If t is quarter 3 of 1987, then X_{t−1} "
        "is the value of X in quarter 2 of 1987, and X_{t−2} is the value in quarter 1 of "
        "1987. We 'look back' one or more periods.",
    ]))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>Example.</b> If t is quarter 3 of 1987, then X_{t−1} is the value of X in "
        "quarter 2 of 1987, and X_{t−2} is the value in quarter 1 of 1987.",
    ]))
    s.append(spacer(6))
    s.append(spss_box([
        "<b>Path:</b> Transform → Create Time Series",
        "<b>Function:</b> Lag",
        "<b>Order:</b> 1, 2, 3, … (one new variable per order)",
        "<b>Internal name:</b> LAG(inf,1), LAG(inf,2), … for the variable inf.",
    ]))
    s.append(spacer(6))
    s.append(watch_out([
        "<b>You lose observations.</b> For lag q you can compute the lag only from "
        "t = q+1 onwards, so the lagged variable has <b>n−q</b> rather than n observations. "
        "This matters when n is small.",
    ]))
    s.append(spacer(10))

    s.append(para("A.3 — Difference variables", SECTION))
    s.append(hr())
    s.append(para(
        "A <b>difference variable</b> measures the change between two time points.", NORMAL))
    s.append(spacer(4))
    s.append(formula([
        "ΔX_t = X_t − X_{t−1}    (absolute first difference)",
        "Δ₁₂X_t = X_t − X_{t−12}  (difference of order 12 — useful for monthly data with yearly seasonality)",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Why 'Δ'?</b> The Greek capital letter Delta (Δ) is conventionally used in "
        "mathematics to denote 'change in'. So ΔX_t literally means 'the change in X at "
        "time t compared to the previous period'.",
    ]))
    s.append(spacer(6))
    s.append(spss_box([
        "<b>Path:</b> Transform → Create Time Series",
        "<b>Function:</b> Difference (absolute) — for the relative version use Function: Percentage change",
        "<b>Internal name:</b> DIFF(u,1), DIFF(u,2), … for the variable u.",
    ]))
    s.append(spacer(6))
    s.append(key_point([
        "<b>Why differences matter:</b>",
        "• They convert an absolute level into a change, which is what most economic theories "
        "talk about (Δ unemployment, Δ inflation, …).",
        "• If you take the difference of a log-transformed variable you obtain a log-return: "
        "Δln(X_t) = ln(X_t / X_{t−1}), often used in finance and macro.",
        "• Differencing is the standard cure for a stochastic trend (see TS_C).",
    ]))
    s.append(spacer(10))

    s.append(para("A.4 — Three problems with time-series regression", SECTION))
    s.append(hr())
    s.append(para(
        "Whenever you do regression on time-series data, three issues need attention. "
        "The rest of this guide is structured around them.", NORMAL_J))
    s.append(spacer(8))
    probs = Table([
        [Paragraph("<b>PROBLEM 1\nData</b>", TBLHDR),
         Paragraph("<b>PROBLEM 2\nAutocorrelation</b>", TBLHDR),
         Paragraph("<b>PROBLEM 3\nSpurious / Stationarity</b>", TBLHDR)],
        [Paragraph("You need many observations spanning many time periods, and the data "
                   "must be of comparable quality. Watch out for inflation when using monetary "
                   "variables — use real (deflated) values.", TBLCELL),
         Paragraph("Classical assumption A3 (uncorrelated errors) is often violated: an error "
                   "today carries some memory of yesterday's error. → Chapter TS_B.", TBLCELL),
         Paragraph("Two unrelated trending series can produce a hugely significant regression. "
                   "The underlying issue is that the series are not stationary. → Chapter TS_C.", TBLCELL)],
    ], colWidths=[5.5*cm]*3)
    probs.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (0,0), C_TEAL),
        ("BACKGROUND",    (1,0), (1,0), C_OLIVE),
        ("BACKGROUND",    (2,0), (2,0), C_BROWN),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#AAAAAA")),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    s.append(probs)
    s.append(spacer(8))
    s.append(watch_out([
        "<b>Sample size.</b> Time-series analysis needs many observations. Rules of thumb:",
        "• Prefer n > 100.",
        "• Absolute minimum: n ≈ 35 (and at least 10 observations per X-variable).",
        "• Yearly data → you may need 35 years or more of history; consider monthly or "
        "quarterly data if available.",
        "• For monetary variables, take inflation into account — use real (deflated) values, "
        "not nominal ones.",
    ]))
    s.append(PageBreak())

    # -----------------------------------------------------------------------
    # CHAPTER TS_B
    # -----------------------------------------------------------------------
    s.append(chapter_header("TS_B", "Autocorrelation",
                             "Errors that remember the past: detection with the LMSC test",
                             C_OLIVE))
    s.append(spacer(10))
    s.append(section_toc([
        ("B.1", "Which assumption fails",
         "Identify A3 (uncorrelated errors) and explain what fails."),
        ("B.2", "First-order autocorrelation ρ",
         "Define AR(1) for errors; interpret sign and magnitude of ρ."),
        ("B.3", "Consequences",
         "List effects on standard errors and (un)biasedness."),
        ("B.4", "Detection — LMSC test",
         "Carry out the LMSC test step by step with descriptive plots."),
        ("B.5", "Solutions",
         "Use a dynamic specification (DL or AR) to remove autocorrelation."),
    ]))
    s.append(spacer(12))

    s.append(para("B.1 — Which classical assumption is violated?", SECTION))
    s.append(hr())
    s.append(para(
        "Remember the assumptions under which the least-squares estimators are BLUE:", NORMAL))
    s.append(spacer(6))
    s.append(key_point([
        "<b>Classical Assumptions Recap</b>   Y_i = β₀ + β₁x₁ᵢ + … + βₖxₖᵢ + εᵢ",
        "• <b>A1:</b> E(εᵢ) = 0",
        "• <b>A2:</b> Var(εᵢ) = σ² is constant (homoskedasticity)",
        "• <b>A3:</b> cov(εᵢ, εⱼ) = 0 for any pair (i ≠ j)",
        "• <b>A4:</b> X's are non-random and not exact linear combinations of each other",
        "• <b>A5:</b> (optional) ε is normally distributed",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>What does A3 mean in plain English?</b> It says that the error you make for "
        "observation i is completely unrelated to the error you make for observation j. "
        "For cross-sectional data this is often reasonable. For time-series data it is "
        "frequently violated: if your model underestimates Y in January, it is likely to "
        "also underestimate Y in February, because economic conditions change slowly.",
    ]))
    s.append(spacer(6))
    s.append(key_point([
        "When <b>A3 is violated</b> — that is, when cov(εᵢ, εⱼ) ≠ 0 for some i ≠ j — "
        "we say the errors are <b>autocorrelated</b> (or <i>serially correlated</i>).",
        "In time-series data this is the rule rather than the exception: "
        "errors close in time tend to be similar.",
    ]))
    s.append(spacer(10))

    s.append(para("B.2 — First-order autocorrelation", SECTION))
    s.append(hr())
    s.append(para(
        "To model the relationship between two consecutive errors, we assume an "
        "<b>AR(1)</b> structure for the error term:", NORMAL))
    s.append(spacer(4))
    s.append(formula([
        "ε_t = ρ ε_{t−1} + u_t",
        "ρ is the first-order autocorrelation coefficient; u is a classical (non-autocorrelated) error.",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Reading this formula.</b> The error today (ε_t) is partly a carry-over from "
        "yesterday's error (ρ × ε_{t−1}) plus a new random shock (u_t). "
        "If ρ = 0, today's error is completely independent of yesterday's — that is A3 satisfied. "
        "If ρ ≠ 0, there is a systematic pattern in the errors — A3 violated.",
    ]))
    s.append(spacer(8))
    s.append(para("<b>Interpreting the size of ρ</b>", SUBSECTION))
    s.append(bullet("ρ = 0 → no autocorrelation: ε_t = u_t (classical error)"))
    s.append(bullet("We expect −1 < ρ < 1; otherwise the error term would explode."))
    s.append(bullet("|ρ| closer to 1 → the previous error matters more for predicting today's "
                    "error → stronger autocorrelation."))
    s.append(spacer(8))
    s.append(two_col_table(
        ["ρ > 0 (positive)", "ρ < 0 (negative)"],
        [
            ["If ε is high in one period, it tends to stay high in the next. "
             "The error series shows persistent runs above (or below) zero. "
             "Most common case in economics (shocks take time to fade).",
             "The error oscillates — the sign tends to flip every period. "
             "Rare in time-series economics; sometimes seen in over-differenced data."],
        ],
        [8.35*cm, 8.35*cm],
        hdr_bg=C_OLIVE,
    ))
    s.append(spacer(10))

    s.append(para("B.3 — Consequences", SECTION))
    s.append(hr())
    s.append(watch_out([
        "<b>What goes wrong in OLS when A3 fails?</b>",
        "• The <b>formulas for the standard errors are no longer correct</b>, so confidence "
        "intervals and t-/F-tests become misleading.",
        "• The OLS estimator is still <b>linear and unbiased</b>, but it is <b>no longer best</b> "
        "(no longer BLUE).",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>What does 'standard errors are wrong' mean in practice?</b> "
        "Your t-statistic (coefficient / SE) becomes incorrect because the denominator (SE) "
        "is based on a formula that assumes A3. With autocorrelation, the SE is typically "
        "<i>underestimated</i>, making t-statistics appear larger than they really are. "
        "This can lead you to declare a relationship significant when it is not.",
    ]))
    s.append(spacer(6))
    s.append(watch_out([
        "<b>Big exception for AR(1) models.</b> When the regression itself contains a lagged "
        "dependent variable (Y_{t−1} as regressor) and there is autocorrelation in the error "
        "term, the <b>estimated coefficients become biased</b>. This is far more serious than "
        "the general case.",
    ]))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>Practical takeaway.</b>",
        "• If autocorrelation is detected in a static or DL(q) model, your standard errors "
        "and tests are unreliable, but your coefficients are still telling you something true "
        "on average.",
        "• If autocorrelation is detected in an AR(1) model, you can no longer trust the "
        "coefficient estimates themselves — this is a stronger reason to switch model specifications.",
    ]))
    s.append(spacer(10))

    s.append(para("B.4 — Detection: the LMSC test", SECTION))
    s.append(hr())
    s.append(para("<b>Step 0 — Graphical inspection</b>", SUBSECTION))
    s.append(para(
        "Plot residuals e_t against time. A clear pattern (waves, trends, clusters above/below zero) "
        "is a strong hint that autocorrelation is present.", NORMAL))
    s.append(spacer(8))
    s.append(para("<b>The LMSC test — Lagrange Multiplier Serial Correlation</b>", SUBSECTION))
    s.append(spacer(4))
    s.append(new_concept([
        "<b>What is a Lagrange Multiplier (LM) test?</b> It is a general method for testing "
        "whether a constraint (here: ρ = 0) is satisfied. We fit an 'auxiliary' regression "
        "that deliberately tries to find autocorrelation. If it finds a lot, we reject H₀.",
    ]))
    s.append(spacer(6))
    s.append(key_point([
        "<b>Hypotheses:</b>",
        "• H₀: no autocorrelation  (equivalent to ρ = 0)",
        "• H₁: autocorrelation present  (equivalent to ρ ≠ 0)",
    ]))
    s.append(spacer(6))
    s.append(formula([
        "<b>Procedure (4 steps):</b>",
        "1. Fit the original regression model and save residuals e_t.",
        "2. Build the auxiliary regression — residuals on the original X's plus the lagged residual:",
        "   e_t = α₀ + α₁X₁_t + … + αₖXₖ_t + α_{k+1} e_{t−1} + u_t",
        "3. Get the R² of the auxiliary regression and compute:   LM = n · R²",
        "4. Under H₀, LM follows a χ² distribution with 1 degree of freedom.",
        "   Compare to a critical value or use the p-value.",
    ]))
    s.append(spacer(6))
    s.append(watch_out([
        "• In the auxiliary model the sample size is <b>n − 1</b> (you lose one observation "
        "because e_{t−1} has no value at t = 1).",
        "• Higher-order test: add e_{t−2}, e_{t−3}, … to the auxiliary regression. "
        "LM then follows a χ² with 2, 3, … df.",
        "• <b>Reject H₀</b> → there IS autocorrelation. "
        "<b>Do NOT reject</b> → assumption A3 is plausibly satisfied.",
    ]))
    s.append(spacer(10))

    s.append(para("<b>Worked example — Phillips curve, quarterly Australian data</b>",
                   SUBSECTION))
    s.append(para(
        "Original model: Y_t = β₀ + β₁X_t + ε_t,  with Y = inflation, "
        "X = change in unemployment rate, n = 90 (quarterly 1987Q1–2009Q3).", NORMAL))
    s.append(spacer(6))
    lmsc_ex = two_col_table(
        ["Auxiliary regression results", "Computation"],
        [
            ["Sample size: n = 90 − 1 = <b>89</b>\n"
             "R² of the auxiliary model: <b>0.310211</b>\n"
             "Coefficient on e_{t−1}: 0.558  (t = 6.219, sig. .000)",
             "LM = n·R² = 89 × 0.310211 = <b>27.609</b>\n"
             "p-value = P(χ²(1) ≥ 27.609) ≈ 1.5 × 10⁻⁷\n"
             "<b>Reject H₀ — autocorrelation is present.</b>"],
        ],
        [8.35*cm, 8.35*cm],
        hdr_bg=C_OLIVE,
    )
    s.append(lmsc_ex)
    s.append(spacer(8))
    s.append(para("<b>Durbin–Watson — the alternative test</b>", SUBSECTION))
    s.append(para(
        "SPSS prints the <b>Durbin–Watson statistic</b> in the regression output. "
        "Values close to 2 suggest no autocorrelation; values close to 0 suggest strong "
        "positive autocorrelation; values close to 4 suggest strong negative autocorrelation.",
        NORMAL))
    s.append(spacer(6))
    s.append(watch_out([
        "<b>Limitation.</b> Durbin–Watson is <b>not valid</b> when the model contains a "
        "lagged dependent variable (i.e. for AR models). The LMSC test is preferred because "
        "it is valid in both static and AR models.",
    ]))
    s.append(spacer(10))

    s.append(para("B.5 — Solutions", SECTION))
    s.append(hr())
    s.append(para(
        "More advanced fixes exist (Generalized Least Squares, OLS with Newey–West / HAC "
        "standard errors, …) but these are not exam material. For us, the standard route is:",
        NORMAL_J))
    s.append(spacer(6))
    s.append(key_point([
        "<b>Re-specify the model to capture the dynamic structure of the data.</b>",
        "• Add lagged X's → a <b>Distributed-Lag (DL)</b> model. See TS_D.",
        "• Add a lagged Y → an <b>Autoregressive (AR)</b> model. See TS_D.",
        "• If the auxiliary regression keeps coming back significant, you almost certainly "
        "need a dynamic specification, not a different test.",
    ]))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>DL or AR — which one?</b>",
        "• If you suspect serial correlation, <b>DL(q) is preferred</b> over AR. Why? "
        "Because AR is biased when there's residual autocorrelation, whereas DL is only inefficient.",
        "• DL is more prone to (quasi-)multicollinearity, but multicollinearity is a less "
        "severe issue than bias.",
        "• In DL the standard hypothesis tests are not strictly valid either, but corrections exist.",
    ]))
    s.append(PageBreak())

    # -----------------------------------------------------------------------
    # CHAPTER TS_C
    # -----------------------------------------------------------------------
    s.append(chapter_header("TS_C", "Stationarity",
                             "Spurious regression, the generalized AR(1), and the Dickey-Fuller test",
                             C_BROWN))
    s.append(spacer(10))
    s.append(section_toc([
        ("C.1", "Spurious regression",
         "Explain why two unrelated trending series can look correlated."),
        ("C.2", "Definition of stationarity",
         "State the formal (weak) stationarity conditions; first graphical check."),
        ("C.3", "Generalized AR(1) — 4 cases",
         "Discuss mean, variance and stationarity for each (a, λ, ρ) case."),
        ("C.4", "Trends — deterministic vs. stochastic",
         "Recognise both; choose detrending or differencing."),
        ("C.5", "Solutions for non-stationarity",
         "Apply detrending, model the trend, or take differences."),
        ("C.6", "Dickey-Fuller test",
         "Carry out the DF test (version 1 / version 2) with adapted critical values."),
    ]))
    s.append(spacer(12))

    s.append(para("C.1 — Spurious regression", SECTION))
    s.append(hr())
    s.append(watch_out([
        "<b>The problem.</b> Two time series can show a strikingly significant regression "
        "even when there is no economic relationship at all. This is called <b>spurious regression</b>.",
        "• Classic example: regress Belgian GDP per capita (1950–2004) on US population density "
        "— same period. R² is huge, the slope is significant, and yet the two have nothing to "
        "do with one another economically.",
        "• The shared cause is that both series have a <i>trend</i> over time. The regression "
        "is picking up the joint drift, not a real relationship.",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Why does trending cause this problem?</b> If both X and Y are growing over time "
        "for completely unrelated reasons (e.g. population growth, productivity gains), a "
        "regression of Y on X will find a strong positive relationship simply because both "
        "happen to be going up together. This is misleading — the relationship is an artefact "
        "of time, not a real causal connection.",
    ]))
    s.append(spacer(6))
    s.append(key_point([
        "The deeper reason spurious regression happens is that the variables are <b>not stationary</b>. "
        "Stationarity is therefore a <b>new assumption</b> added on top of the 5 classical MR "
        "assumptions whenever we work with time-series data.",
    ]))
    s.append(spacer(10))

    s.append(para("C.2 — Definition of stationarity", SECTION))
    s.append(hr())
    s.append(para(
        "Intuitively, a stationary time series does not trend or drift. If you cut it in half, "
        "the left half and the right half look roughly the same.", NORMAL_J))
    s.append(spacer(6))
    s.append(key_point([
        "<b>Formal definition (weak stationarity).</b> A time series Y_t is (weakly) "
        "stationary if for every t:",
        "• E(Y_t) = μ  (constant mean — series returns to its average)",
        "• Var(Y_t) = σ²  (constant variance)",
        "• Cov(Y_t, Y_{t−s}) = γ_s  (the covariance depends only on the lag s, not on t)",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Understanding the three conditions in plain English:</b>",
        "1. <b>Constant mean</b>: the series does not systematically move up or down over time. "
        "It fluctuates around a fixed level.",
        "2. <b>Constant variance</b>: the series does not become more or less volatile over time. "
        "The spread of fluctuations stays roughly the same.",
        "3. <b>Covariance depends only on the gap</b>: the relationship between values two periods "
        "apart is the same regardless of whether we look at 1950 or 2000.",
    ]))
    s.append(spacer(6))
    s.append(para("<b>First graphical check</b>", SUBSECTION))
    s.append(para("Plot the series against time. Two warning signs of non-stationarity:", NORMAL))
    s.append(bullet("<b>The mean changes</b> — there's a clear upward or downward trend, "
                    "or seasonal pattern."))
    s.append(bullet("<b>The variance changes</b> — the series gets noisier (or quieter) over time."))
    s.append(para(
        "If the time plot looks like flat noise oscillating around a constant level, the series "
        "is <b>plausibly stationary</b>. For a formal verdict, use the Dickey-Fuller test (C.6).",
        NORMAL_J))
    s.append(spacer(10))

    s.append(para("C.3 — The generalized AR(1) model", SECTION))
    s.append(hr())
    s.append(para(
        "In its most general form, the building block for studying stationarity is:", NORMAL))
    s.append(spacer(4))
    s.append(formula([
        "Y_t = a + λt + ρ Y_{t−1} + ε_t",
        "with ε_t white noise: independent, N(0, σ²), mean zero, no autocorrelation.",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>What is 'white noise'?</b> White noise is the ideal error term — each observation "
        "is drawn independently at random with mean zero and constant variance. "
        "It contains no pattern whatsoever. When the error in a model is white noise, "
        "all the classical assumptions are satisfied.",
    ]))
    s.append(spacer(8))
    s.append(para("Three parameters control the behaviour: the constant <i>a</i>, the trend "
                   "coefficient λ, and the autoregressive coefficient ρ. The key question is "
                   "whether |ρ| < 1 or |ρ| = 1.", NORMAL))
    s.append(spacer(8))

    cases = Table([
        [Paragraph("<b>Case 1 — Basic AR(1)</b>\n|ρ| < 1, a = 0, λ = 0", TBLHDR),
         Paragraph("<b>Case 2 — AR(1) + constant</b>\n|ρ| < 1, a ≠ 0, λ = 0", TBLHDR)],
        [Paragraph("<b>Model:</b> Y_t = ρ Y_{t−1} + ε_t\n\n"
                   "<b>Behaviour:</b> Returns to the mean 0. The further ρ is from 0, "
                   "the longer the series stays on one side before reverting.\n\n"
                   "<b>✓ STATIONARY</b>", TBLCELL),
         Paragraph("<b>Model:</b> Y_t = a + ρ Y_{t−1} + ε_t\n\n"
                   "<b>Behaviour:</b> Stationary about a non-zero mean μ = a / (1 − ρ).\n\n"
                   "<b>✓ STATIONARY</b>", TBLCELL)],
        [Paragraph("<b>Case 3 — AR(1) + linear trend</b>\n|ρ| < 1, a ≠ 0, λ ≠ 0", TBLHDR),
         Paragraph("<b>Case 4 — Random walk</b>\n|ρ| = 1", TBLHDR)],
        [Paragraph("<b>Model:</b> Y_t = a + λt + ρ Y_{t−1} + ε_t\n\n"
                   "<b>Behaviour:</b> Stationary about a deterministic trend μ + δt. "
                   "The series itself trends, but its deviation from the trend line is stationary.\n\n"
                   "<b>✗ NOT STATIONARY</b>", TBLCELL),
         Paragraph("<b>Model:</b> Y_t = a + Y_{t−1} + ε_t\n\n"
                   "<b>Behaviour:</b> Stochastic trend. With a = 0: random walk; with a ≠ 0: "
                   "random walk with drift. Variance grows with t — definitely not stationary.\n\n"
                   "<b>✗ NOT STATIONARY</b>", TBLCELL)],
    ], colWidths=[8.35*cm, 8.35*cm])
    cases.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), C_TEAL),
        ("BACKGROUND", (1,0), (1,0), C_OLIVE),
        ("BACKGROUND", (0,2), (0,2), C_BROWN),
        ("BACKGROUND", (1,2), (1,2), C_PURPLE),
        ("GRID",       (0,0), (-1,-1), 0.4, colors.HexColor("#AAAAAA")),
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    s.append(cases)
    s.append(spacer(8))
    s.append(key_point([
        "<b>Summary card.</b> AR(1) with |ρ| < 1 is the <b>stationary family</b>. "
        "AR(1) with |ρ| = 1 is the <b>random-walk family</b> — never stationary.",
        "• |ρ| < 1, λ = 0: stationary (Cases 1–2). <b>No problem</b> in regression.",
        "• |ρ| < 1, λ ≠ 0: stationary about a deterministic trend (Case 3). "
        "<b>Problem</b> — fix with detrending.",
        "• |ρ| = 1: stochastic trend / random walk (Case 4). "
        "<b>Problem</b> — fix with differencing.",
    ]))
    s.append(spacer(10))

    # Case details
    s.append(para("C.3 (details) — What each case looks like", SECTION))
    s.append(hr())
    s.append(para("<b>Case 1.</b> |ρ| < 1, a = 0, λ = 0 → basic AR(1)", SUBSECTION))
    s.append(para("Model: Y_t = ρ Y_{t−1} + ε_t.  By repeated substitution:", NORMAL))
    s.append(spacer(4))
    s.append(formula([
        "Y_t = ε_t + ρ ε_{t−1} + ρ² ε_{t−2} + … + ρᵗ Y₀",
        "E(Y_t) ≈ 0  (constant)     Var(Y_t) = σ² / (1 − ρ²)  (constant)",
        "Cov(Y_{t−s}, Y_t) = (σ² ρˢ) / (1 − ρ²)  (depends only on lag s)",
        "Correlation: r(Y_{t−s}, Y_t) = ρˢ  → autocorrelation decays exponentially",
    ]))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>Example.</b> Y_t = 0.7 Y_{t−1} + ε_t. Because ρ = 0.7 > 0, the series tends to "
        "stay a while above (or below) its mean before reverting. The closer ρ gets to 1, "
        "the slower the revert.",
    ]))
    s.append(spacer(8))
    s.append(para("<b>Case 2.</b> |ρ| < 1, a ≠ 0, λ = 0 → AR(1) with non-zero mean", SUBSECTION))
    s.append(para("Model: Y_t = a + ρ Y_{t−1} + ε_t.", NORMAL))
    s.append(spacer(4))
    s.append(formula([
        "E(Y_t) ≈ μ = a / (1 − ρ)",
        "Var(Y_t) = σ² / (1 − ρ²)",
        "Cov(Y_{t−s}, Y_t) = (σ² ρˢ) / (1 − ρ²)",
        "All three are constant in t → the series is stationary about a non-zero mean μ.",
    ]))
    s.append(spacer(8))
    s.append(para("<b>Case 3.</b> |ρ| < 1, a ≠ 0, λ ≠ 0 → stationary about a deterministic trend",
                   SUBSECTION))
    s.append(para("Model: Y_t = a + λt + ρ Y_{t−1} + ε_t.", NORMAL))
    s.append(spacer(4))
    s.append(formula([
        "δ = λ / (1 − ρ)        μ = (a − ρδ) / (1 − ρ)",
        "Y_t − μ − δt  is a stationary AR(1) about 0.",
    ]))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>Example.</b> Y_t = 1 + 0.05t + 0.7 Y_{t−1} + ε_t.",
        "• δ = 0.05 / (1 − 0.7) = 1/6",
        "• μ = (1 − 0.7 × 1/6) / (1 − 0.7) = 53/18",
        "• So Y_t − 53/18 − (1/6)t is a stationary AR(1) about 0.",
    ]))
    s.append(spacer(8))
    s.append(para("<b>Case 4.</b> |ρ| = 1 → random walk", SUBSECTION))
    s.append(key_point([
        "1. <b>Random walk</b> (a = 0, λ = 0): Y_t = Y_{t−1} + ε_t",
        "   E(Y_t) = y₀ (constant), but Var(Y_t) = tσ² → variance grows with time. ✗",
        "2. <b>Random walk with drift</b> (a ≠ 0, λ = 0): Y_t = a + Y_{t−1} + ε_t",
        "   E(Y_t) = ta + y₀ → mean drifts up (or down) over time. ✗",
        "3. <b>Random walk with drift and trend</b> (a ≠ 0, λ ≠ 0): Y_t = a + λt + Y_{t−1} + ε_t",
        "   Mean grows like ta + ½t(t+1)λ → even faster drift. ✗",
    ]))
    s.append(spacer(10))

    s.append(para("C.4 — Deterministic vs. stochastic trends", SECTION))
    s.append(hr())
    s.append(two_col_table(
        ["Deterministic trend", "Stochastic trend"],
        [
            ["Comes from a λt term → mean changes, variance stays constant.\n\n"
             "Types: linear (μ + δt); seasonal (monthly/quarterly dummies).\n\n"
             "Example: monthly unemployment figures in Flanders — same months of the year cluster together.",
             "Comes from |ρ| = 1 → random walk. Mean may or may not drift, but variance grows with time.\n\n"
             "Types: random walk; random walk with drift; random walk with drift and trend.\n\n"
             "Example: many financial prices behave roughly as random walks with drift."],
        ],
        [8.35*cm, 8.35*cm],
        hdr_bg=C_BROWN,
    ))
    s.append(spacer(6))
    s.append(watch_out([
        "<b>In practice it is often hard to tell which is which</b> just from a plot. "
        "The standard pragmatic answer: include both possibilities (<b>model 3 of the DF test</b>) "
        "when you are unsure — i.e. random walk with drift and trend.",
    ]))
    s.append(spacer(10))

    s.append(para("C.5 — Solutions for non-stationarity", SECTION))
    s.append(hr())
    s.append(para("<b>If the problem is a deterministic trend (λ ≠ 0, |ρ| < 1)</b>", SUBSECTION))
    s.append(key_point([
        "<b>Option 1 — detrending.</b> Replace the non-stationary Y_t by Y_t − μ − δt, "
        "which is stationary.",
        "<b>Option 2 — model the trend.</b> Keep Y_t but add a linear-trend term to the model:",
        "  Y_t = β₀ + β₁X_t + ε_t   becomes   Y_t = α + λt + β₁X_t + ε_t",
        "<b>Option 3 — seasonal differencing.</b> For seasonal trends (e.g. monthly data), "
        "use Δ₁₂X_t = X_t − X_{t−12} — the change vs. the same month one year earlier.",
    ]))
    s.append(spacer(8))
    s.append(para("<b>If the problem is a stochastic trend (|ρ| = 1)</b>", SUBSECTION))
    s.append(key_point([
        "<b>Take first differences.</b> Detrending does NOT work here — it is for deterministic "
        "trends only. Instead, replace each variable by its first difference:",
        "ΔY_t = Y_t − Y_{t−1},   ΔX_t = X_t − X_{t−1}",
        "• If after one round of differencing the variables are stationary, fit your regression "
        "on the differences (not the levels).",
        "• Why it works: if Y_t = Y_{t−1} + ε_t, then ΔY_t = ε_t — white noise, stationary.",
        "• If even the first differences are not stationary, try second differences "
        "Δ²Y_t = ΔY_t − ΔY_{t−1}.",
    ]))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>Worked example — GDP and Gross National Income (Belgium, 1950–2004).</b>",
        "• Both series clearly trend upward over time. A regression in levels would be spurious.",
        "• After taking first differences (or relative differences), the trends disappear. "
        "The relationship between ΔGDP and ΔGNI remains and is now economically meaningful.",
    ]))
    s.append(spacer(10))

    s.append(para("C.6 — The Dickey-Fuller test", SECTION))
    s.append(hr())
    s.append(para(
        "Until now, choosing between stationary and non-stationary was a judgement call from "
        "a time plot. The <b>Dickey-Fuller (DF) test</b> makes it formal: it is a "
        "<b>unit-root test</b> — it tests whether ρ = 1 in the generalized AR(1).", NORMAL_J))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>What is a 'unit root'?</b> The term comes from the mathematics of the AR(1) model. "
        "When ρ = 1, the model has a 'unit root' — the process does not revert to a mean and "
        "the variance grows over time. Testing for a unit root is the same as testing whether "
        "the series is a random walk (non-stationary).",
    ]))
    s.append(spacer(6))
    s.append(key_point([
        "<b>Hypotheses (re-parameterised).</b>",
        "• H₀: ρ = 1  (unit root — series is NOT stationary)",
        "• H₁: |ρ| < 1  (series is stationary, possibly about a deterministic trend)",
    ]))
    s.append(spacer(6))
    s.append(formula([
        "<b>The trick:</b> take first differences and reparameterise. Setting α₁ = ρ − 1:",
        "Version 1 — no trend:   ΔY_t = α₀ + α₁ Y_{t−1} + ε_t",
        "Version 2 — with linear trend:   ΔY_t = α₀ + λt + α₁ Y_{t−1} + ε_t",
        "Reject H₀  ⟺  α₁ < 0  (significantly).",
    ]))
    s.append(spacer(6))
    s.append(watch_out([
        "<b>Adapted critical values.</b> Under H₀ the t-statistic is <b>NOT t-distributed</b> "
        "— you cannot use the usual t-critical values. Use the table below.",
    ]))
    s.append(spacer(6))
    cv_table = Table([
        [Paragraph("<b>DF version</b>", TBLHDR),
         Paragraph("<b>1%-level</b>", TBLHDR),
         Paragraph("<b>5%-level</b>", TBLHDR),
         Paragraph("<b>10%-level</b>", TBLHDR)],
        [Paragraph("Version 1 — without trend", TBLCELL),
         Paragraph("−3.43", TBLCELL),
         Paragraph("−2.86", TBLCELL),
         Paragraph("−2.57", TBLCELL)],
        [Paragraph("Version 2 — with trend", TBLCELL),
         Paragraph("−3.96", TBLCELL),
         Paragraph("−3.41", TBLCELL),
         Paragraph("−3.13", TBLCELL)],
    ], colWidths=[6.5*cm, 3*cm, 3*cm, 3*cm])
    cv_table.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  C_BROWN),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#AAAAAA")),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [C_WHITE, C_LGRAY]),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("ALIGN",         (1,0), (-1,-1), "CENTER"),
    ]))
    s.append(cv_table)
    s.append(spacer(6))
    s.append(para(
        "<b>Decision rule.</b> If the t-stat on Y_{t−1} is <b>more negative</b> than the "
        "critical value, reject H₀ → the series is stationary.", NORMAL))
    s.append(spacer(6))
    s.append(key_point([
        "<b>Procedure (4 steps).</b>",
        "1. Plot the data versus time.",
        "2. No visible trend? Use Version 1 (no trend). Clear trend? Use Version 2 (with trend). "
        "Unsure? Use Version 2 — it's the safer default.",
        "3. Run the chosen DF regression with ΔY_t as response and Y_{t−1} as regressor "
        "(plus the time variable for Version 2).",
        "4. Read the t-statistic for the coefficient of Y_{t−1} and compare to the "
        "adapted critical values above.",
    ]))
    s.append(spacer(10))

    s.append(para("Reference — mean of a stationary AR(1)", SECTION))
    s.append(hr())
    s.append(two_col_table(
        ["Model", "Mean / behaviour"],
        [
            ["Y_t = ρ Y_{t−1} + ε_t",                   "Stationary, mean 0"],
            ["Y_t = a + ρ Y_{t−1} + ε_t",               "Stationary, mean μ = a / (1 − ρ)"],
            ["Y_t = a + λt + ρ Y_{t−1} + ε_t",
             "Stationary about a deterministic trend μ + δt,\nwith δ = λ / (1 − ρ),  μ = (a − ρδ) / (1 − ρ)"],
        ],
        [7.5*cm, 9.2*cm],
        hdr_bg=C_BROWN,
    ))
    s.append(PageBreak())

    # -----------------------------------------------------------------------
    # CHAPTER TS_D
    # -----------------------------------------------------------------------
    s.append(chapter_header("TS_D", "Dynamic models",
                             "DL(q), AR(1), total multipliers, and the time-series exam workflow",
                             C_PURPLE))
    s.append(spacer(10))
    s.append(section_toc([
        ("D.1", "Distributed lag model DL(q)",
         "Write the equation; interpret coefficients; find total multiplier."),
        ("D.2", "Optimal lag length",
         "Pick q starting from q_max by removing non-significant top lags."),
        ("D.3", "Autoregressive model AR(1)",
         "Write the equation; interpret coefficients; find total multiplier β/(1−γ)."),
        ("D.4", "Link DL(∞) ↔ AR(1)",
         "Show how AR(1) is an infinite-lag DL; derive geometric weights."),
        ("D.5", "Three-step exam workflow",
         "Combine stationarity, fit, assumption check on a real exam problem."),
    ]))
    s.append(spacer(12))

    s.append(para("D.1 — Distributed lag model DL(q)", SECTION))
    s.append(hr())
    s.append(para(
        "In a <b>static model</b>, Y depends only on the current X. But economic effects are "
        "rarely instantaneous: training today changes accident counts months later; a tax cut "
        "today affects consumption next quarter. To capture this we use a "
        "<b>distributed lag model</b>:", NORMAL_J))
    s.append(spacer(6))
    s.append(formula([
        "Y_t = α + β₀X_t + β₁X_{t−1} + β₂X_{t−2} + … + β_q X_{t−q} + ε_t",
        "Total multiplier = Σβₖ  (sum over k = 0, 1, …, q)",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Reading the DL(q) model.</b> Each β coefficient captures the effect of X at a "
        "different delay. β₀ is the immediate effect; β₁ is the effect felt one period later; "
        "β_q is the effect felt q periods later. Adding them all gives the <i>total multiplier</i> "
        "— the full long-run effect of a permanent change in X.",
    ]))
    s.append(spacer(6))
    s.append(spss_box([
        "<b>How to set up DL(q) in SPSS:</b>",
        "• Transform → Create Time Series → Function: Lag, Order: 1, 2, …, q  (to make the lagged variables)",
        "• Analyze → Regression → Linear: put Y as Dependent and X_t, X_{t−1}, …, X_{t−q} as Independents.",
        "• Sample size shrinks to n − q.",
    ]))
    s.append(spacer(8))
    s.append(para("<b>Interpreting the coefficients of DL(q)</b>", SUBSECTION))
    s.append(key_point([
        "As in any regression: β_k is the average change in Y when X_{t−k} rises by 1 unit, "
        "holding all other variables constant.",
    ]))
    s.append(spacer(6))
    s.append(two_col_table(
        ["Temporary change (X rises by 1, then returns)",
         "Maintained change (X rises by 1 and stays high)"],
        [
            ["Immediate effect: β₀\n"
             "After 1 period: β₁\n"
             "After 2 periods: β₂, and so on\n\n"
             "The effect dies out once you go beyond lag q.",
             "Immediate effect: β₀\n"
             "After 1 period: β₀ + β₁\n"
             "After 2 periods: β₀ + β₁ + β₂\n\n"
             "After q or more periods the total effect is Σβₖ = total multiplier"],
        ],
        [8.35*cm, 8.35*cm],
        hdr_bg=C_PURPLE,
    ))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>In words.</b>",
        "• The <b>total multiplier</b> is the long-run effect on Y of a permanent 1-unit rise in X.",
        "• It is the answer to the exam-style question: 'by how much will Y eventually go up "
        "if X increases by 1 unit and stays there forever?'",
    ]))
    s.append(spacer(10))

    s.append(para("D.2 — Choosing the optimal lag length q", SECTION))
    s.append(hr())
    s.append(key_point([
        "<b>Procedure (top-down).</b> Start from a maximum lag q_max (given in the exam, "
        "e.g. q_max = 3 or 4) and shrink it.",
        "1. Fit the DL(q_max) model. Look at the t-test for the highest-order lag, β_{q_max}.",
        "2. If it is <b>not significant</b>, drop that lag and refit DL(q_max−1). Repeat.",
        "3. Stop as soon as the t-test for the largest remaining lag is significant. "
        "That q is your <b>optimal lag length</b>.",
    ]))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>Worked example — safety training and accident losses.</b>",
        "• Goal: model monthly accident losses (Y, euro) as a function of monthly "
        "safety-training hours (X), with q_max = 4.",
        "• Build X_{t−1}, X_{t−2}, X_{t−3}, X_{t−4} and fit DL(4).",
        "• Suppose the t-test on β₄ is not significant — drop the lag, refit DL(3); "
        "β₃ also not significant — refit DL(2); β₂ not significant — refit DL(1); "
        "β₁ is significant. Stop: optimal lag is q = 1.",
        "• Now read off β₀ and β₁, compute the total multiplier, and interpret it.",
    ]))
    s.append(spacer(10))

    s.append(para("D.3 — Autoregressive model AR(1)", SECTION))
    s.append(hr())
    s.append(para(
        "In a DL(q) model the dynamics come from past X's. We can instead let past Y "
        "carry the memory:", NORMAL))
    s.append(spacer(4))
    s.append(formula([
        "Y_t = α + β X_t + γ Y_{t−1} + ε_t",
        "Total multiplier = β / (1 − γ)   (geometric-series formula; requires |γ| < 1)",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Why does Y_{t−1} appear?</b> Many economic variables carry their own history — "
        "GDP this quarter depends partly on GDP last quarter. Including Y_{t−1} as a regressor "
        "captures this inertia parsimoniously. Instead of needing many lag coefficients "
        "(like DL), a single γ coefficient does the work.",
    ]))
    s.append(spacer(6))
    s.append(para("<b>Interpreting AR(1)</b>", SUBSECTION))
    s.append(bullet("<b>Immediate effect</b> (temporary or maintained 1-unit rise in X): β."))
    s.append(bullet("<b>Long-run effect</b> of a maintained 1-unit rise in X: β / (1 − γ) "
                    "→ the total multiplier."))
    s.append(bullet("A temporary 1-unit rise in X gives a one-off jump of β, then a smaller "
                    "residual effect on Y in every subsequent period that fades by a factor γ."))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>Worked example — Y = 20 + 10X + 0.5 Y_{t−1}.</b>  In year 5, X temporarily rises by 1.",
        "• Year 5: Y jumps by 10 (the β coefficient).",
        "• Year 6: Y rises by 0.5 × 10 = 5 relative to its original level — even though X is "
        "back to normal — because Y₅ was elevated.",
        "• Year 7: effect is 0.5² × 10 = 2.5;  year 8: 0.5³ × 10 = 1.25, …",
        "• Total multiplier = 10 / (1 − 0.5) = 20. If X had stayed at the new level, Y "
        "would eventually rise by 20.",
    ]))
    s.append(spacer(8))
    s.append(interpretation([
        "<b>Worked example — education spending and GDP growth.</b>",
        "Yearly US data since 1910.  X = dollars invested in education per child,  Y = GDP growth (%).",
        "Fitted AR(1):   Ŷ_t = 1.01 + 0.009 X_t + 0.627 Y_{t−1}",
        "• Total multiplier = β / (1 − γ) = 0.009 / (1 − 0.627) = 0.024.",
        "• Interpretation: if the investment per child increases by 1 dollar and is maintained "
        "over the years, then GDP growth rises on average by 0.024 percentage points in the long run.",
    ]))
    s.append(spacer(10))

    s.append(para("D.4 — Link between AR(1) and DL(∞)", SECTION))
    s.append(hr())
    s.append(para(
        "Why does the AR(1) total multiplier have that specific shape β / (1 − γ)? "
        "Because AR(1) is secretly a DL model with infinitely many lags.", NORMAL_J))
    s.append(spacer(6))
    s.append(formula([
        "Y_t = α + β X_t + γ Y_{t−1} + ε_t",
        "    = α + β X_t + γ(α + β X_{t−1} + γ Y_{t−2}) + ε_t",
        "    … repeating to infinity …",
        "Y_t = α' + β X_t + βγ X_{t−1} + βγ² X_{t−2} + βγ³ X_{t−3} + … + ε'_t",
    ]))
    s.append(spacer(6))
    s.append(key_point([
        "<b>Geometric-series consequence.</b> The total multiplier of the AR(1) model is:",
        "Σβₖ = β(1 + γ + γ² + γ³ + …) = β / (1 − γ)",
        "This is exactly the geometric series 1 + q + q² + … = 1 / (1 − q), converging when |γ| < 1.",
    ]))
    s.append(spacer(6))
    s.append(new_concept([
        "<b>Geometric series refresher.</b> If |q| < 1, then "
        "1 + q + q² + q³ + … = 1 / (1 − q). "
        "Example: 1 + 0.5 + 0.25 + 0.125 + … = 1 / (1 − 0.5) = 2. "
        "The series converges because each term is a fixed fraction of the previous one, "
        "eventually becoming negligible.",
    ]))
    s.append(spacer(6))
    s.append(interpretation([
        "<b>Why does this matter?</b>",
        "• AR(1) gives you long memory with only two coefficients (β and γ), instead of many "
        "β_k's. Much less prone to (quasi-)multicollinearity than DL(q) with large q.",
        "• Drawback: AR(1) is biased when there is residual autocorrelation (see B.3). "
        "DL(q) is the safer choice when you suspect that.",
    ]))
    s.append(spacer(10))

    s.append(para("D.5 — The three-step exam workflow", SECTION))
    s.append(hr())
    s.append(para(
        "This is the procedure to follow whenever an exam question asks you to fit a static, "
        "DL(q), or AR(1) model on time-series data. The model type will be specified — "
        "you do not have to choose. You go through three steps in order.", NORMAL_J))
    s.append(spacer(8))
    wf2 = Table([
        [Paragraph("<b>STEP 1\nStationarity check</b>", TBLHDR),
         Paragraph("<b>STEP 2\nFit the model</b>", TBLHDR),
         Paragraph("<b>STEP 3\nCheck assumptions</b>", TBLHDR)],
        [Paragraph("• Time plot of every variable.\n"
                   "• Choose DF version (no-trend or with-trend).\n"
                   "• Run DF on each variable, read t-stat, compare with adapted critical values.\n"
                   "• Unit root anywhere? → take Δ of all variables, re-test on Δ.", TBLCELL),
         Paragraph("• Static / DL(q) / AR(1) — given in the question.\n"
                   "• For DL: find optimal q starting from q_max (drop top lags until significant).\n"
                   "• Report coefficients + total multiplier (Σβ or β/(1−γ)).\n"
                   "• Interpret with the right words: temporary vs. maintained, "
                   "log-return vs. unit change.", TBLCELL),
         Paragraph("• State H₀ / H₁ in plain English.\n"
                   "• Write the auxiliary regression (X's + lagged residual).\n"
                   "• Compute LM = n·R²; compare to χ²(1).\n"
                   "• Conclude — autocorrelation present or assumption satisfied.\n"
                   "• Also briefly mention the other classical assumptions.", TBLCELL)],
    ], colWidths=[5.5*cm]*3)
    wf2.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), C_BROWN),
        ("BACKGROUND", (1,0), (1,0), C_PURPLE),
        ("BACKGROUND", (2,0), (2,0), C_OLIVE),
        ("GRID",       (0,0), (-1,-1), 0.4, colors.HexColor("#AAAAAA")),
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    s.append(wf2)
    s.append(spacer(10))

    # Worked example
    s.append(para("<b>Step-by-step worked example — consumption ~ income (log-log)</b>",
                   SUBSECTION))
    s.append(interpretation([
        "<b>Setup.</b> Both income (X) and consumption (Y) are log-transformed, then we fit "
        "a DL(q) model on their differences.",
        "",
        "<b>STEP 1 — Stationarity.</b>",
        "• Time plots of Y and X show clear upward trends. Run DF on the levels — you fail to "
        "reject H₀ for both. Both variables have a unit root.",
        "• Take first differences (which are log-returns): ΔY and ΔX. "
        "Run DF Version 1 (no visible trend in the differences).",
        "• ΔY: t = −9.95, well below −2.86. Reject H₀ → stationary.",
        "• ΔX: t = −12.72, also well below −2.86. Reject H₀ → stationary.",
        "• Both variables are stationary after differencing; we proceed with the differences.",
        "",
        "<b>STEP 2 — Fit the model.</b>",
        "• Build lags of ΔX up to q_max = 3.",
        "• DL(3): β₃ not significant → drop. DL(2): β₂ not significant → drop. "
        "DL(1): β₁ is significant. Stop. Optimal lag is q = 1.",
        "• Fitted model:   ΔŶ_t = 0.004 + 0.35 ΔX_t + 0.182 ΔX_{t−1}",
        "• Total multiplier = 0.35 + 0.182 = 0.532.",
        "• Interpretation (log-returns!): if the relative change in income rises by 1 "
        "percentage point and is maintained, then the relative change in consumption rises "
        "on average by 0.532 percentage points after one quarter.",
        "",
        "<b>STEP 3 — Assumption check (LMSC test).</b>",
        "• Auxiliary regression: e_t = α₀ + α₁ΔX_t + α₂ΔX_{t−1} + α₃e_{t−1} + u_t.",
        "• Sample size n = 161 (one observation lost to the lagged residual).",
        "• R² of the auxiliary regression: 0.002618.  LM = 161 × 0.002618 = 0.4215.",
        "• p-value = P(χ²(1) ≥ 0.4215) = 0.5162.  Do not reject H₀ → no significant "
        "autocorrelation. Assumption A3 is plausibly satisfied. ✓",
    ]))
    s.append(PageBreak())

    # -----------------------------------------------------------------------
    # EXAM-DAY CHECKLIST
    # -----------------------------------------------------------------------
    checklist_banner = Table([
        [Paragraph("<b>EXAM-DAY CHECKLIST</b>", make_style("cl_title", font="DejaVu-Bold",
                    size=14, leading=20, color=C_WHITE, align=TA_CENTER))],
        [Paragraph("Time-Series Regression", make_style("cl_sub", font="DejaVu-Bold",
                    size=20, leading=26, color=C_WHITE, align=TA_CENTER))],
    ], colWidths=[W - 4.4*cm])
    checklist_banner.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_BLACK),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
    ]))
    s.append(checklist_banner)
    s.append(spacer(10))

    cl = Table([
        [Paragraph("<b>STEP 1\nSTATIONARITY\nTS_C</b>", TBLHDR),
         Paragraph("<b>STEP 2\nFIT MODEL\nTS_D</b>", TBLHDR),
         Paragraph("<b>STEP 3\nASSUMPTIONS\nTS_B</b>", TBLHDR)],
        [Paragraph("• Time plot of every variable.\n"
                   "• Choose DF version (no-trend or with-trend).\n"
                   "• Run DF on each variable, read t-stat, compare with adapted critical values.\n"
                   "• Unit root anywhere? → take Δ of all variables, re-test on Δ.", TBLCELL),
         Paragraph("• Static / DL(q) / AR(1) — given in the question.\n"
                   "• For DL: find optimal q starting from q_max (drop top lags until significant).\n"
                   "• Report coefficients + total multiplier (Σβ or β/(1−γ)).\n"
                   "• Interpret with the right words: temporary vs. maintained, "
                   "log-return vs. unit change.", TBLCELL),
         Paragraph("• State H₀ / H₁ in plain English.\n"
                   "• Write the auxiliary regression (X's + lagged residual).\n"
                   "• Compute LM = n·R²; compare to χ²(1).\n"
                   "• Conclude — autocorrelation present or assumption satisfied.", TBLCELL)],
    ], colWidths=[5.5*cm]*3)
    cl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), C_BROWN),
        ("BACKGROUND", (1,0), (1,0), C_PURPLE),
        ("BACKGROUND", (2,0), (2,0), C_OLIVE),
        ("GRID",       (0,0), (-1,-1), 0.4, colors.HexColor("#AAAAAA")),
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    s.append(cl)
    s.append(spacer(14))

    # Formula sheet
    s.append(para("Formula sheet — the four formulas you really need", SECTION))
    s.append(hr())
    s.append(formula([
        "<b>1. DL(q) model and its total multiplier:</b>",
        "Y_t = α + β₀X_t + β₁X_{t−1} + … + β_q X_{t−q} + ε_t ;   Σβₖ",
        "",
        "<b>2. AR(1) model and its total multiplier:</b>",
        "Y_t = α + β X_t + γ Y_{t−1} + ε_t ;   β / (1 − γ)",
        "",
        "<b>3. LMSC test — auxiliary regression and statistic:</b>",
        "e_t = α₀ + α₁X₁_t + … + αₖXₖ_t + α_{k+1} e_{t−1} + u_t",
        "LM = n · R²  ~  χ²(1)",
        "",
        "<b>4. Dickey-Fuller test — two versions:</b>",
        "Version 1:   ΔY_t = α₀ + α₁ Y_{t−1} + ε_t",
        "Version 2:   ΔY_t = α₀ + λt + α₁ Y_{t−1} + ε_t",
        "Critical values: 5% → −2.86 (V1), −3.41 (V2). Reject H₀ if t-stat is more negative.",
    ]))
    s.append(spacer(14))

    # Common pitfalls
    s.append(para("Common exam pitfalls", SECTION))
    s.append(hr())
    s.append(watch_out([
        "<b>1. 'Reject H₀ means stationary.'</b>  For DF, yes — Reject = Stationary. "
        "But many people confuse DF with the LMSC test, where Reject = autocorrelation present "
        "(i.e. bad news). Always re-read the hypotheses.",
        "<b>2. 'Take differences whenever in doubt.'</b>  Over-differencing creates artificial "
        "negative autocorrelation. Only difference if the DF test (or the time plot) tells you to.",
        "<b>3. 'Use Durbin–Watson for AR(1).'</b>  Durbin–Watson is not valid when a lagged "
        "dependent variable is in the model. Use LMSC.",
        "<b>4. 'Total multiplier = β₀ only.'</b>  No — for DL(q) it is the sum of all βₖ's. "
        "For AR(1) it is β / (1 − γ), not just β.",
        "<b>5. 'Interpret as units when X is logged.'</b>  If you took log-differences "
        "(log-returns), interpret as percentage-point changes, not unit changes.",
        "<b>6. 'Skip the assumption check.'</b>  The LMSC test is worth easy marks and must "
        "be reported with H₀/H₁, LM-statistic, p-value, and a conclusion sentence.",
        "<b>7. 'Use the t-distribution for the DF t-stat.'</b>  Under H₀ it is not "
        "t-distributed. Always use the adapted critical values (−2.86, −3.41, …).",
    ]))
    s.append(spacer(10))

    # One-page summary
    summary = Table([
        [Paragraph("<b>THE WHOLE GUIDE IN FOUR LINES</b>",
                    make_style("sum_hdr", font="DejaVu-Bold", size=10, color=C_BROWN))],
        [Paragraph("<b>Recognise</b> the data is time series → define lags, define differences.", BOX_CONTENT)],
        [Paragraph("<b>Diagnose</b> autocorrelation with LMSC — but think first about whether "
                   "you need a dynamic model.", BOX_CONTENT)],
        [Paragraph("<b>Stabilise</b> with detrending (deterministic trend) or differencing "
                   "(stochastic trend / unit root).", BOX_CONTENT)],
        [Paragraph("<b>Model</b> with DL(q) or AR(1) — find the optimal q, interpret the "
                   "total multiplier, run LMSC.", BOX_CONTENT)],
    ], colWidths=[W - 4.4*cm])
    summary.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), C_GOLD_BG),
        ("BACKGROUND", (0,1), (-1,-1), C_GOLD_BG),
        ("LINEBELOW",  (0,0), (0,0), 1, C_GOLD),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("BOX",        (0,0), (-1,-1), 1, C_GOLD),
    ]))
    s.append(summary)

    return s

# ---------------------------------------------------------------------------
# BUILD PDF
# ---------------------------------------------------------------------------
def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("DejaVu", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    page_num = canvas.getPageNumber()
    canvas.drawRightString(W - 2*cm, 1.2*cm, f"Page {page_num}")
    canvas.drawString(2*cm, 1.2*cm, "Statistics — Part 2 — Time Series Regression (Enhanced Edition)")
    canvas.restoreState()

OUT = "/home/user/BabyPluto/TimeSeries_StudyGuide_Enhanced.pdf"

doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=2.2*cm,
    rightMargin=2.2*cm,
    topMargin=2*cm,
    bottomMargin=2.2*cm,
    title="Statistics Part 2 — Time Series — Enhanced Edition",
    author="Enhanced Study Guide",
)

doc.build(build_story(), onFirstPage=add_page_number, onLaterPages=add_page_number)
print(f"PDF written to {OUT}")
