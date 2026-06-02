import io, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Image
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from PIL import Image as PILImage

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV",   FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DV-M", FD + "DejaVuSansMono.ttf"))
registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV", boldItalic="DV-B")

DARK_BLUE  = colors.HexColor("#1B3A6B")
MID_BLUE   = colors.HexColor("#2E6DA4")
LIGHT_BLUE = colors.HexColor("#D6E8F7")
ORANGE     = colors.HexColor("#D4500A")
GREEN      = colors.HexColor("#1A6B3A")
TEAL       = colors.HexColor("#117A65")
LIGHT_GREEN= colors.HexColor("#D6F0E0")
YELLOW_BG  = colors.HexColor("#FFF8DC")
RED_BG     = colors.HexColor("#FDE8E8")
GREY_LINE  = colors.HexColor("#CCCCCC")
WHITE      = colors.white
BLACK      = colors.black
ANSWER_BG  = colors.HexColor("#F0FFF4")
SPSS_BG    = colors.HexColor("#EBF5FB")
Q_BG       = colors.HexColor("#EBF2FA")
GUIDE_BG   = colors.HexColor("#E8F8F5")
APPR_BG    = colors.HexColor("#FFF3E0")

doc = SimpleDocTemplate(
    "/home/user/BabyPluto/Exam_Walkthrough.pdf",
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm,
)
W = A4[0] - 4*cm

def S(name, **kw):
    kw.setdefault("fontName", "DV")
    return ParagraphStyle(name, **kw)

title_s  = S("T",  fontSize=22, textColor=WHITE,      fontName="DV-B", alignment=TA_CENTER, leading=28)
sub_s    = S("Su", fontSize=10, textColor=WHITE,      fontName="DV-B", leading=14)
part_s   = S("P",  fontSize=14, textColor=WHITE,      fontName="DV-B", leading=18)
h1       = S("h1", fontSize=12, textColor=DARK_BLUE,  fontName="DV-B", spaceBefore=10, spaceAfter=4, leading=15)
body     = S("b",  fontSize=9.5,textColor=BLACK,       spaceBefore=2,  spaceAfter=3,  leading=14, alignment=TA_JUSTIFY)
mono     = S("m",  fontSize=8.5,fontName="DV-M",       spaceBefore=2,  spaceAfter=2,  leading=13, leftIndent=8, textColor=colors.HexColor("#2B2B2B"))
small    = S("sm", fontSize=8,  textColor=BLACK,       leading=12)
LIGHT_BLUE_HEX = "#D6E8F7"

def sp(h=6): return Spacer(1, h)

def banner(text, bg=DARK_BLUE):
    t = Table([[Paragraph(text, part_s)]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),bg),
        ("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),10),
        ("LEFTPADDING",(0,0),(-1,-1),14),
    ]))
    return t

def sub_q(letter, text):
    t = Table([[Paragraph(f"  {letter}   {text}", sub_s)]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),MID_BLUE),
        ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("LEFTPADDING",(0,0),(-1,-1),10),
    ]))
    return t

def q_box(text):
    t = Table([[Paragraph(f"<b>Question asks:</b>  {text}", body)]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),Q_BG),
        ("BOX",(0,0),(-1,-1),0.5,MID_BLUE),
        ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("LEFTPADDING",(0,0),(-1,-1),10),
    ]))
    return t

def guide_box(section, title, hint=""):
    rows = [[Paragraph(f"<b>Guide §{section} — {title}</b>", S("gh",fontSize=9.5,fontName="DV-B",textColor=colors.HexColor("#0A4A3A"),leading=13))]]
    if hint:
        rows.append([Paragraph(hint, S("gs",fontSize=9.5,textColor=colors.HexColor("#0A4A3A"),leading=13,alignment=TA_JUSTIFY))])
    t = Table(rows, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),GUIDE_BG),
        ("BOX",(0,0),(-1,-1),1,TEAL),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    return t

def approach_box(steps):
    hdr = S("ah",fontSize=9.5,fontName="DV-B",textColor=WHITE,leading=13)
    sty = S("as",fontSize=9.5,leading=14,textColor=BLACK)
    rows = [[Paragraph("  ✎  Approach — Which method and why", hdr)]]
    for s in steps:
        rows.append([Paragraph(f"  • {s}", sty)])
    t = Table(rows, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(0,0),ORANGE),
        ("BACKGROUND",(0,1),(-1,-1),APPR_BG),
        ("BOX",(0,0),(-1,-1),1,ORANGE),
        ("INNERGRID",(0,1),(-1,-1),0.3,GREY_LINE),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    return t

def spss_box(steps, title="SPSS Step-by-Step"):
    hdr = S("sh",fontSize=9.5,fontName="DV-B",textColor=WHITE,leading=13)
    sty = S("ss",fontSize=9,fontName="DV-M",leading=14,textColor=colors.HexColor("#1A1A2E"))
    rows = [[Paragraph(f"  ⌨  {title}", hdr)]]
    for i,s in enumerate(steps,1):
        rows.append([Paragraph(f"  {i}.  {s}", sty)])
    t = Table(rows, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(0,0),MID_BLUE),
        ("BACKGROUND",(0,1),(-1,-1),SPSS_BG),
        ("BOX",(0,0),(-1,-1),1,MID_BLUE),
        ("INNERGRID",(0,1),(-1,-1),0.3,GREY_LINE),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    return t

def ans_box(lines):
    hdr = S("ansH",fontSize=9.5,fontName="DV-B",textColor=WHITE,leading=13)
    sty = S("ansS",fontSize=9.5,leading=14,textColor=colors.HexColor("#1A3A1A"),alignment=TA_JUSTIFY)
    msty= S("ansM",fontSize=8.5,fontName="DV-M",leading=13,textColor=colors.HexColor("#1A3A1A"))
    rows = [[Paragraph("  ✓  Worked Answer", hdr)]]
    for line in lines:
        if line == "":
            rows.append([sp(3)])
        elif line.startswith(">>"):
            rows.append([Paragraph("  "+line[2:], msty)])
        else:
            rows.append([Paragraph("  "+line, sty)])
    t = Table(rows, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(0,0),GREEN),
        ("BACKGROUND",(0,1),(-1,-1),ANSWER_BG),
        ("BOX",(0,0),(-1,-1),1,GREEN),
        ("INNERGRID",(0,1),(-1,-1),0.3,GREY_LINE),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    return t

def data_tbl(header, rows, cw=None):
    if cw is None: cw=[W/len(header)]*len(header)
    th=S("dth",fontSize=8,fontName="DV-B",textColor=WHITE,leading=11)
    td=S("dtd",fontSize=8,leading=11)
    data=[[Paragraph(h,th) for h in header]]
    for r in rows:
        data.append([Paragraph(str(c),td) for c in r])
    t=Table(data,colWidths=cw)
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),DARK_BLUE),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE,colors.HexColor("#EBF2FA")]),
        ("BOX",(0,0),(-1,-1),0.5,GREY_LINE),
        ("INNERGRID",(0,0),(-1,-1),0.3,GREY_LINE),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),5),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    return t

def fig_to_image(fig, width_cm):
    buf=io.BytesIO()
    fig.savefig(buf,format="png",dpi=150,bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    w=width_cm*cm
    pil=PILImage.open(buf)
    pw,ph=pil.size
    h=w*ph/pw
    buf.seek(0)
    return Image(buf,width=w,height=h)

def fig_label(text):
    return Paragraph(f"<i>{text}</i>",
        S("fl",fontSize=8,textColor=colors.HexColor("#555555"),
          alignment=TA_CENTER,spaceBefore=2,spaceAfter=8))

# ── matplotlib charts ──────────────────────────────────────────────────────────
def plot_df_q3():
    fig, axes = plt.subplots(1, 2, figsize=(13, 3.2))

    # --- Q3a levels ---
    ax = axes[0]
    ax.set_xlim(-5, 0.5); ax.set_ylim(-0.6, 1.6); ax.axis("off")
    ax.set_title("Q3a: Levels of q and p  (DF Version 2, CV = −3.41)",
                 fontsize=9.5, color="#1B3A6B", fontweight="bold", pad=4)
    ax.annotate("", xy=(0.3,0.75), xytext=(-4.8,0.75),
                arrowprops=dict(arrowstyle="->",color="black",lw=1.5))
    for x in [-4,-3,-2,-1,0]:
        ax.text(x,0.60,str(x),ha="center",fontsize=8,color="#555")
    ax.axvspan(-5,-3.41,ymin=0.45,ymax=0.85,alpha=0.2,color="#1A6B3A")
    ax.axvspan(-3.41,0.5,ymin=0.45,ymax=0.85,alpha=0.12,color="#C0392B")
    ax.axvline(-3.41,ymin=0.3,ymax=0.9,color="#1B3A6B",lw=2,ls="--")
    ax.text(-3.41,1.42,"CV = −3.41",ha="center",fontsize=8.5,color="#1B3A6B",fontweight="bold")
    for tv,label,col,yo in [(-1.639,"q: t=−1.639\nFail to reject → non-stationary","#C0392B",0.1),
                              (-2.458,"p: t=−2.458\nFail to reject → non-stationary","#C0392B",-0.35)]:
        ax.annotate("",xy=(tv,0.75),xytext=(tv,0.2),
                    arrowprops=dict(arrowstyle="->",color=col,lw=2))
        ax.text(tv+0.05,yo,label,ha="center",fontsize=7.5,color=col,
                fontweight="bold",multialignment="center")
    ax.text(-4.5,1.42,"REJECT\n(stationary)",ha="center",fontsize=8,
            color="#1A6B3A",fontweight="bold")
    ax.text(0.1,1.42,"FAIL TO\nREJECT",ha="center",fontsize=8,
            color="#C0392B",fontweight="bold")

    # --- Q3b differences ---
    ax = axes[1]
    ax.set_xlim(-11, 0.5); ax.set_ylim(-0.6, 1.6); ax.axis("off")
    ax.set_title("Q3b: First Differences Δq and Δp  (DF Version 1, CV = −2.86)",
                 fontsize=9.5, color="#1B3A6B", fontweight="bold", pad=4)
    ax.annotate("", xy=(0.3,0.75), xytext=(-10.5,0.75),
                arrowprops=dict(arrowstyle="->",color="black",lw=1.5))
    for x in [-10,-8,-6,-4,-2,0]:
        ax.text(x,0.60,str(x),ha="center",fontsize=8,color="#555")
    ax.axvspan(-11,-2.86,ymin=0.45,ymax=0.85,alpha=0.2,color="#1A6B3A")
    ax.axvspan(-2.86,0.5,ymin=0.45,ymax=0.85,alpha=0.12,color="#C0392B")
    ax.axvline(-2.86,ymin=0.3,ymax=0.9,color="#1B3A6B",lw=2,ls="--")
    ax.text(-2.86,1.42,"CV = −2.86",ha="center",fontsize=8.5,color="#1B3A6B",fontweight="bold")
    for tv,label,yo in [(-7.2,"Δq: t=−7.200\nReject H₀ → stationary ✓",0.1),
                         (-9.431,"Δp: t=−9.431\nReject H₀ → stationary ✓",-0.35)]:
        ax.annotate("",xy=(tv,0.75),xytext=(tv,0.2),
                    arrowprops=dict(arrowstyle="->",color="#1A6B3A",lw=2))
        ax.text(tv,yo,label,ha="center",fontsize=7.5,color="#1A6B3A",
                fontweight="bold",multialignment="center")
    ax.text(-9,1.42,"REJECT\n(stationary)",ha="center",fontsize=8,
            color="#1A6B3A",fontweight="bold")
    ax.text(0.1,1.42,"FAIL TO\nREJECT",ha="center",fontsize=8,
            color="#C0392B",fontweight="bold")

    fig.tight_layout(pad=1.2)
    return fig

def plot_dl_topdown():
    steps = ["Step 1\nDL(3)\nhighest lag = 3",
             "Step 2\nDL(2)\nhighest lag = 2",
             "Step 3\nDL(1)\nhighest lag = 1",
             "Step 4\nDL(0) = Static\nfinal model"]
    pvals = [0.053, 0.064, 0.128, 0.018]
    cols  = ["#C0392B","#C0392B","#C0392B","#1A6B3A"]
    outcomes = ["p=0.053 > 0.05\n→ DROP lag 3",
                "p=0.064 > 0.05\n→ DROP lag 2",
                "p=0.128 > 0.05\n→ DROP lag 1",
                "p=0.018 < 0.05\n→ KEEP (final)"]

    fig, ax = plt.subplots(figsize=(11, 3.8))
    bars = ax.bar(steps, pvals, color=cols, edgecolor="white", linewidth=1.2, width=0.55)
    ax.axhline(0.05, color="#D4500A", lw=2.5, ls="--", label="Significance threshold α = 0.05")
    for bar, pv, oc in zip(bars, pvals, outcomes):
        ax.text(bar.get_x()+bar.get_width()/2, pv+0.004,
                f"p = {pv}\n{oc}", ha="center", va="bottom",
                fontsize=8.5, color="#1B3A6B", fontweight="bold", multialignment="center")
    ax.set_ylabel("p-value of highest lag in model", fontsize=9)
    ax.set_title("Q3f — Top-Down DL Lag Selection: Decision at Each Step",
                 color="#1B3A6B", fontsize=10, fontweight="bold")
    ax.set_ylim(0, 0.25)
    ax.legend(fontsize=9, frameon=False)
    ax.tick_params(labelsize=8.5)
    fig.tight_layout(pad=1.2)
    return fig

def plot_q2c_r2():
    models = ["Model 1\n(SUN, INHABITANTS_log)", "Model 2\n(+ POLICE added)"]
    r2s    = [0.018, 0.434]
    fig, ax = plt.subplots(figsize=(7, 3.2))
    bars = ax.bar(models, r2s, color=["#C0392B","#1A6B3A"], edgecolor="white", width=0.45)
    for bar, v in zip(bars, r2s):
        ax.text(bar.get_x()+bar.get_width()/2, v+0.01,
                f"R² = {v}", ha="center", fontsize=11, fontweight="bold",
                color="#1B3A6B")
    ax.set_ylabel("R²", fontsize=10)
    ax.set_ylim(0, 0.55)
    ax.set_title("Q2c — R² comparison: is the jump from 0.018 to 0.434 significant?",
                 color="#1B3A6B", fontsize=9.5, fontweight="bold")
    ax.annotate("", xy=(1, 0.434), xytext=(0, 0.018),
                arrowprops=dict(arrowstyle="->", color="#D4500A", lw=2.5))
    ax.text(0.5, 0.22, "ΔR² = 0.416\nTest: Joint F-test\nJ = 1",
            ha="center", fontsize=9, color="#D4500A", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF3E0", edgecolor="#D4500A"))
    fig.tight_layout(pad=1.2)
    return fig


# ════════════════════════════════════════════════════════════════════════════
# STORY
# ════════════════════════════════════════════════════════════════════════════
story = []

# ── Cover ──────────────────────────────────────────────────────────────────
cover = Table(
    [[Paragraph("Mock Exam 2026\nWorked Walkthrough", title_s)],
     [Paragraph("Every sub-question solved in order · Method chosen · SPSS steps · Full answer", S("cs",fontSize=10,textColor=LIGHT_BLUE,alignment=TA_CENTER,leading=14))],
     [sp(6)],
     [Paragraph("Q1 · Housing & Air Pollution  (pollution.sav)  —  MLR  ·  7 pts", S("cl",fontSize=9,textColor=LIGHT_BLUE,alignment=TA_CENTER,leading=13))],
     [Paragraph("Q2 · US Cities & Homicide  (output given)  —  MLR  ·  6 pts",     S("cl2",fontSize=9,textColor=LIGHT_BLUE,alignment=TA_CENTER,leading=13))],
     [Paragraph("Q3 · Chicken Demand  (chicken.sav)  —  Time Series  ·  7 pts",     S("cl3",fontSize=9,textColor=LIGHT_BLUE,alignment=TA_CENTER,leading=13))],
    ], colWidths=[W])
cover.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1),DARK_BLUE),
    ("TOPPADDING",(0,0),(-1,-1),20),("BOTTOMPADDING",(0,0),(-1,-1),14),
    ("LEFTPADDING",(0,0),(-1,-1),20),("RIGHTPADDING",(0,0),(-1,-1),20),
]))
story += [sp(20), cover, sp(14)]
story.append(Paragraph(
    "For every sub-question this document shows: which section of the exam guide applies "
    "(green box), the reasoning and approach (orange box), the exact SPSS menu steps (blue box), "
    "and the complete worked answer with the real output numbers (green answer box).", body))
story.append(PageBreak())

# ════ Q1 ══════════════════════════════════════════════════════════════════════
story += [banner("QUESTION 1 — Housing & Air Pollution   ·   pollution.sav   ·   7 points"), sp(6)]
story.append(Paragraph(
    "Goal: model median housing value (CMEDV) using all available predictors. "
    "NOx must be logged. Region is a 4-category variable requiring dummy coding. "
    "n = 506 neighbourhoods.", body))
story.append(sp(8))

# Q1a ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q1a", "Write down a theoretical equation of the model"))
story.append(sp(4))
story.append(q_box("Write down a theoretical equation of the model."))
story.append(sp(4))
story.append(guide_box("1.1 + 1.2 + 1.3",
    "Reading the Question · Dummy Variables · Log Transformations",
    "The key flags: (1) NOx must be logged → linear-log model. "
    "(2) Region has k=4 categories → create k−1 = 3 dummies, omitting one reference category. "
    "A theoretical equation lists all β coefficients, defines the dummies, and states the error term."))
story.append(sp(4))
story.append(approach_box([
    "List every predictor. Flag Region as categorical (4 levels: NE, NW, South, Center).",
    "Choose Center as reference (any category works — state which you chose).",
    "Create 3 dummies: DNE (North East), DNW (North West), DS (South).",
    "Log-transform NOx: call it lnNOx. This creates a linear-log specification for that predictor.",
    "Write the equation with β₀ … β₁₀, include ε, state the assumptions.",
]))
story.append(sp(4))
story.append(spss_box([
    "Transform → Compute Variable…  Target: LN_NOx   Expression: LN(NOx)   OK.",
    "Transform → Compute Variable…  Target: DNE   Expression: (Region = 1)   OK.",
    "Transform → Compute Variable…  Target: DNW   Expression: (Region = 2)   OK.",
    "Transform → Compute Variable…  Target: DS    Expression: (Region = 3)   OK.",
    "  (Center = 4 is the reference — do NOT create a dummy for it.)",
    "Analyze → Regression → Linear…",
    "  Dependent: CMEDV   Independent(s): CRIM, LN_NOx, RM, AGE, DIS, RAD, PTRatio, DNE, DNW, DS",
    "Click OK.",
], title="SPSS: Create Log Variable, Dummies, Run Regression"))
story.append(sp(4))
story.append(ans_box([
    "CMEDV = β₀ + β₁·CRIM + β₂·lnNOx + β₃·RM + β₄·AGE + β₅·DIS + β₆·RAD",
    "         + β₇·PTRatio + β₈·DNE + β₉·DNW + β₁₀·DS + ε",
    "",
    "Assumptions: ε ~ N(0, σ²) independent; predictors not perfectly multicollinear;",
    "ε uncorrelated with each predictor.",
    "",
    "Dummy definitions (reference category = Center):",
    "  DNE = 1 if neighbourhood is in North East, 0 otherwise",
    "  DNW = 1 if neighbourhood is in North West, 0 otherwise",
    "  DS  = 1 if neighbourhood is in South, 0 otherwise",
    "",
    "Why 3 dummies for 4 categories?  Rule: always k−1.  Including all 4 would cause",
    "perfect multicollinearity (DNE + DNW + DS + DCenter ≡ 1 for every observation).",
]))
story.append(sp(10))

# Q1b ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q1b", "Discuss the effect of pollution on housing values"))
story.append(sp(4))
story.append(q_box("Discuss the effect of pollution on the housing value based on your fitted model."))
story.append(sp(4))
story.append(guide_box("1.3 + 1.5",
    "Log Transformation Interpretation · Testing Individual Significance",
    "NOx is logged → linear-log model.  Interpretation rule: 1% increase in X → β/100 units change in Y. "
    "Also test significance: read Sig. column for lnNOx from the Coefficients table."))
story.append(sp(4))
story.append(approach_box([
    "Locate the lnNOx row in the Coefficients table. Read B (= −16.041).",
    "Apply the linear-log rule: 1% increase in NOx → −16.041/100 = −0.160 thousand dollars.",
    "Convert to dollars: −0.160 × $1000 = −$160.41 decrease in median housing value.",
    "Check significance: t = −5.572, Sig. = 0.000 < 0.05 → effect is statistically significant.",
]))
story.append(sp(4))
story.append(data_tbl(
    ["Predictor","B","Std. Error","t","Sig.","Interpretation"],
    [["lnNOx","−16.041","2.879","−5.572","0.000","Significant at 5%"]],
    cw=[2.5*cm,2*cm,2.5*cm,2*cm,2*cm,5.5*cm]))
story.append(sp(4))
story.append(ans_box([
    "Model type: Linear-Log (Y is in levels, X is logged).",
    "Rule: 1% increase in X  →  β/100 units change in Y.",
    "",
    "Interpretation: A 1% increase in NOx concentration decreases median housing value",
    "by  −16.041 / 100 = −0.160 thousand dollars = −$160.41  on average,",
    "holding all other predictors constant.",
    "",
    "Significance: t = −5.572,  p = 0.000 < 0.05.",
    "We reject H₀: β_lnNOx = 0.  The effect of pollution is statistically significant.",
    "",
    "Direction makes economic sense: higher pollution → lower desirability → lower house prices.",
]))
story.append(sp(10))

# Q1c ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q1c", "Does Region have a significant effect on CMEDV?  (one hypothesis test)"))
story.append(sp(4))
story.append(q_box("Does the variable Region have a significant effect on CMEDV? "
                   "Carry out one hypothesis test (H₀, H₁, test statistic, conclusion, assumptions)."))
story.append(sp(4))
story.append(guide_box("1.6",
    "Joint F-test — Testing a Group of Variables Together",
    "Region produces 3 dummies. Testing them individually with 3 separate t-tests inflates Type I error. "
    "The correct method is one joint F-test: H₀: β_DNE = β_DNW = β_DS = 0. "
    "Use SPSS block method to get the R²-change F-statistic automatically."))
story.append(sp(4))
story.append(approach_box([
    "J = 3 restrictions (3 dummies), k = 10 (full model), n = 506.",
    "Unrestricted model: all 10 predictors (including 3 dummies).  R²_u = 0.652.",
    "Restricted model: 7 predictors (dummies removed).  R²_r = 0.649.",
    "F = [(R²_u − R²_r)/J] / [(1 − R²_u)/(n − k − 1)].",
    "Use p-value from SPSS Change Statistics to make the decision.",
]))
story.append(sp(4))
story.append(spss_box([
    "Analyze → Regression → Linear…",
    "Block 1: Dependent CMEDV, Independent(s): CRIM LN_NOx RM AGE DIS RAD PTRatio  (no dummies).",
    "Click Next → Block 2: add DNE, DNW, DS.",
    "Click Statistics… → check R-square change → Continue.",
    "Click OK.  Read the Model Summary table: row 2, column Sig. F Change.",
], title="SPSS: Joint F-test via Block Method (R-square Change)"))
story.append(sp(4))
story.append(ans_box([
    "H₀: β_DNE = β_DNW = β_DS = 0  (Region has no effect — restricted model)",
    "H₁: At least one of β_DNE, β_DNW, β_DS ≠ 0  (Region has an effect — full model)",
    "",
    "Assumption: errors are normally distributed (for exact F-distribution).",
    "",
    "Test statistic (R²-change F):",
    ">>F = [(0.652 − 0.649) / 3] / [(1 − 0.652) / (506 − 10 − 1)] = 0.001 / 0.000703 = 1.463",
    "",
    "From SPSS Change Statistics: F Change = 1.463, df1 = 3, df2 = 495, Sig. F Change = 0.224.",
    "",
    "Decision: p = 0.224 > 0.05 → Fail to reject H₀.",
    "Conclusion: The region dummies do not jointly improve the model significantly.",
    "Region does NOT have a statistically significant effect on CMEDV at the 5% level.",
]))
story.append(sp(10))

# Q1d ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q1d", "Set up a residual plot and discuss"))
story.append(sp(4))
story.append(q_box("Set up a residual plot and discuss this."))
story.append(sp(4))
story.append(guide_box("1.7",
    "Residual Plot Analysis",
    "Plot standardized residuals (ZRESID) on Y-axis vs standardized predicted values (ZPRED) on X-axis. "
    "A good plot shows a random horizontal cloud. Look for: fan shape (heteroskedasticity), "
    "curved arc (non-linearity), isolated outliers."))
story.append(sp(4))
story.append(spss_box([
    "Analyze → Regression → Linear…  (same model as Q1a, all predictors including dummies).",
    "Click Plots… → set Y: ZRESID,  X: ZPRED  → Continue.",
    "Click Save… → check Unstandardized under Residuals and Unstandardized under Predicted Values → Continue.",
    "Click OK.  The scatter plot appears in the Output Viewer.",
    "Alternatively: Graph → Chart Builder → Scatter → drag PRE_1 to x-axis, RES_1 to y-axis → OK.",
], title="SPSS: Generate Residual Plot"))
story.append(sp(4))
story.append(ans_box([
    "What to look for: a random horizontal cloud around zero → all assumptions hold.",
    "",
    "What the actual plot shows (from official solution):",
    "  • Several neighbourhoods show outlying behaviour — isolated points far from zero.",
    "  • Some points form a 'line pattern', suggesting subgroups behave differently.",
    "  • For very low and very high predicted values, residuals tend to be positive",
    "    → mean of errors is not zero for all predictions → Assumption A1 potentially violated.",
    "  • The spread may widen for larger fitted values (possible heteroskedasticity).",
    "",
    "Conclusion: The residual plot is NOT ideal. Some regression assumptions appear violated.",
    "The 506 neighbourhoods may not be homogeneous enough for a single linear model.",
    "",
    "Key rule: describe WHAT you see and NAME the assumption violated.",
    "  Fan/cone → A2 violated (non-constant variance).",
    "  Curved arc → A1 violated (model misspecified).",
    "  Outliers → investigate individually (can distort estimates).",
]))
story.append(sp(10))

# Q1e ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q1e", "Write the auxiliary model for the White test"))
story.append(sp(4))
story.append(q_box("Write down the auxiliary model you would use to carry out the White test "
                   "(you do not have to carry out the test)."))
story.append(sp(4))
story.append(guide_box("1.8",
    "White Test for Heteroskedasticity — Auxiliary Model",
    "The auxiliary regression regresses ê² on: all original predictors, "
    "the square of each CONTINUOUS predictor, and all cross-products of pairs of predictors. "
    "Never square dummies (D² = D). Never include dummy×dummy cross-products."))
story.append(sp(4))
story.append(approach_box([
    "Continuous variables: CRIM, lnNOx, RM, AGE, DIS, RAD, PTRatio  (7 variables).",
    "Dummies: DNE, DNW, DS  — do NOT square these.",
    "Add squared terms for each continuous variable: CRIM², lnNOx², RM², AGE², DIS², RAD², PTRatio².",
    "Add cross-products for every pair of continuous variables: 7 choose 2 = 21 pairs.",
    "Add cross-products of each continuous variable with each dummy: 7 × 3 = 21 pairs.",
    "Total regressors in auxiliary model (excluding constant) = 10 + 7 + 21 + 21 = 59.",
    "Note: df for the White test statistic = 59.  W ~ χ²(59).",
]))
story.append(sp(4))
story.append(ans_box([
    "Let ê = residuals from the Q1a model.  Auxiliary regression:",
    "",
    ">>ê² = β₀ + β₁CRIM + β₂lnNOx + β₃RM + β₄AGE + β₅DIS + β₆RAD + β₇PTRatio",
    ">>     + β₈DNE + β₉DNW + β₁₀DS",
    ">>     + α₁CRIM² + α₂lnNOx² + α₃RM² + α₄AGE² + α₅DIS² + α₆RAD² + α₇PTRatio²",
    ">>     + γ₁CRIM·lnNOx + γ₂CRIM·RM + γ₃CRIM·AGE + γ₄CRIM·DIS",
    ">>       + γ₅CRIM·RAD + γ₆CRIM·PTRatio + γ₇CRIM·DNE + γ₈CRIM·DNW + γ₉CRIM·DS",
    ">>     + γ₁₀lnNOx·RM + γ₁₁lnNOx·AGE + γ₁₂lnNOx·DIS + γ₁₃lnNOx·RAD",
    ">>       + γ₁₄lnNOx·PTRatio + γ₁₅lnNOx·DNE + γ₁₆lnNOx·DNW + γ₁₇lnNOx·DS",
    ">>     + [all remaining continuous pairs: RM·AGE, RM·DIS, RM·RAD … DIS·RAD … etc.]",
    ">>     + [continuous × dummy pairs: RM·DNE, RM·DNW, RM·DS … PTRatio·DS]  + ε",
    "",
    "Key rules: (1) Never square a dummy — D² = D.  (2) Never cross dummy × dummy.",
    "(3) W = n × R²_aux  ~  χ²(df) where df = number of regressors above (excluding constant).",
    "Note: the exam note says 'the model will probably be shorter' — if fewer predictors",
    "are in the original model, the White auxiliary is much more manageable.",
]))
story.append(sp(10))

# Q1f ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q1f", "Omitted variable Indus — what does this mean for the lnNOx coefficient?"))
story.append(sp(4))
story.append(q_box("Harrison and Rubinfield indicate that Indus (proportion of non-retail business acres) "
                   "should also be included. You did not include it. What does this tell you about "
                   "the estimate for the coefficient of lnNOx?"))
story.append(sp(4))
story.append(guide_box("1.9",
    "Omitted Variable Bias",
    "sign(bias) = sign(β_Indus) × sign(r(lnNOx, Indus)). "
    "Need to determine: (1) what sign would β_Indus have in the full model? "
    "(2) are lnNOx and Indus positively or negatively correlated?"))
story.append(sp(4))
story.append(approach_box([
    "Step 1 — Sign of β_Indus: Indus measures proportion of industrial land. "
    "More industry → less desirable neighbourhood → lower house prices → β_Indus < 0 (negative).",
    "Step 2 — Sign of r(lnNOx, Indus): Industrial areas produce more NOx pollution. "
    "Therefore lnNOx and Indus are positively correlated → r > 0.",
    "Step 3 — Bias direction: sign(bias) = sign(β_Indus) × sign(r) = (−) × (+) = negative.",
    "Negative bias means our estimate for β_lnNOx is TOO LOW (more negative than the true value).",
]))
story.append(sp(4))
story.append(data_tbl(
    ["Omitted variable Z","sign(β_Z)","sign(r(lnNOx, Z))","sign(bias) = product","β_lnNOx estimate is…"],
    [["Indus","Negative (−)","Positive (+)","(−)×(+) = Negative","Too low (underestimated)"]],
    cw=[3*cm,2.5*cm,3.5*cm,4*cm,3.5*cm]))
story.append(sp(4))
story.append(ans_box([
    "Indus is an omitted variable in our model.  Omitted variables bias the coefficients",
    "of correlated included variables.",
    "",
    "sign(β_Indus) = negative  (industrial areas reduce house values).",
    "sign(r(lnNOx, Indus)) = positive  (industrial areas also have more NOx).",
    "",
    "Bias on β̂_lnNOx = (−) × (+) = negative bias.",
    "",
    "Conclusion: our estimated coefficient for lnNOx (−16.041) is UNDERESTIMATED.",
    "The true effect of pollution is more negative than −16.041 — we are understating",
    "how much pollution harms housing values.",
    "",
    "(In other words: some of the housing value reduction we attributed to pollution",
    " is actually caused by the industrial character of the area, not NOx alone.)",
]))
story.append(PageBreak())

# ════ Q2 ══════════════════════════════════════════════════════════════════════
story += [banner("QUESTION 2 — US Cities & Homicide Rates   ·   Output provided   ·   6 points"), sp(6)]
story.append(Paragraph(
    "No dataset to open — all answers are based on the SPSS output tables provided in the question. "
    "n = 100 cities. Dependent variable: HOMOCIDE. Predictors: SUN, INHABITANTS_log, POLICE, COAST.", body))
story.append(sp(8))

# Q2a ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q2a", "What do you conclude from the VIF scores?"))
story.append(sp(4))
story.append(q_box("What do you conclude from the VIF scores in the table?"))
story.append(sp(4))
story.append(guide_box("1.10",
    "VIF and Multicollinearity",
    "VIF = 1/(1 − R²_j). Threshold: VIF > 5 = concerning, VIF > 10 = severe. "
    "Read the Collinearity Statistics columns in the SPSS Coefficients table."))
story.append(sp(4))
story.append(data_tbl(
    ["Variable","Tolerance","VIF","Assessment"],
    [["SUN","0.890","1.123","Well below 5 — no problem"],
     ["INHABITANTS_log","0.919","1.088","Well below 5 — no problem"],
     ["POLICE","0.904","1.106","Well below 5 — no problem"]],
    cw=[4*cm,3*cm,2.5*cm,7*cm]))
story.append(sp(4))
story.append(ans_box([
    "All VIF scores are well below the rule-of-thumb threshold of 5.",
    "Highest VIF = 1.123 (SUN) — very close to 1, indicating almost no multicollinearity.",
    "",
    "Conclusion: There is no indication of (quasi-)multicollinearity in this model.",
    "The coefficient estimates are reliable and the standard errors are not inflated.",
]))
story.append(sp(10))

# Q2b ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q2b", "Auxiliary regression to determine Tolerance for SUN"))
story.append(sp(4))
story.append(q_box("Set up the equation of a suitable auxiliary regression model that will allow you "
                   "to determine the Tolerance score for SUN. Explain how you determine the tolerance."))
story.append(sp(4))
story.append(guide_box("1.10",
    "VIF Formula: Tolerance = 1 − R²_j",
    "Tolerance for variable j = 1 − R² from regressing X_j on all other X's. "
    "So: regress SUN on INHABITANTS_log and POLICE; read R²; Tolerance(SUN) = 1 − R²."))
story.append(sp(4))
story.append(ans_box([
    "Auxiliary regression model:",
    ">>SUN = α₀ + α₁·INHABITANTS_log + α₂·POLICE + ε",
    "",
    "Run this regression in SPSS.  Read R²_aux from the Model Summary table.",
    "",
    "Tolerance(SUN) = 1 − R²_aux",
    "VIF(SUN) = 1 / Tolerance(SUN) = 1 / (1 − R²_aux)",
    "",
    "Verification: from the table, Tolerance(SUN) = 0.890, so R²_aux ≈ 0.110.",
    "This means only 11% of the variation in SUN is explained by the other two predictors",
    "→ SUN contributes mostly independent information → low multicollinearity.",
]))
story.append(sp(10))

# Q2c ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q2c", "Is R² of Model 2 significantly larger than R² of Model 1?"))
story.append(sp(4))
story.append(q_box("Carry out a suitable hypothesis test to investigate whether the R² of Model 2 "
                   "is significantly larger than the R² of Model 1 (no need to check assumptions)."))
story.append(sp(4))
story.append(guide_box("1.6",
    "Joint F-test — Comparing Two Nested Models",
    "Model 2 adds POLICE to Model 1. So: full model = Model 2, restricted = Model 1, J = 1. "
    "This is a joint F-test (with J=1 it equals the individual t-test squared, but framing as F is cleaner)."))
story.append(sp(4))
story.append(fig_to_image(plot_q2c_r2(), 13))
story.append(fig_label("Figure Q2c — R² jumps from 0.018 to 0.434 when POLICE is added. "
                       "The joint F-test tells us whether this increase is statistically significant."))
story.append(sp(4))
story.append(approach_box([
    "Full (unrestricted) model = Model 2: HOMOCIDE = β₀ + β₁SUN + β₂INHABITANTS_log + β₃POLICE  →  R²_u = 0.434.",
    "Restricted model = Model 1: HOMOCIDE = β₀ + β₁SUN + β₂INHABITANTS_log  →  R²_r = 0.018.",
    "J = 1  (one restriction: β_POLICE = 0).  n = 100.  k = 3 (predictors in full model).",
    "F = [(R²_u − R²_r)/J] / [(1 − R²_u)/(n − k − 1)].",
]))
story.append(sp(4))
story.append(ans_box([
    "H₀: β_POLICE = 0  (adding POLICE does not improve the model — Model 1 is sufficient)",
    "H₁: β_POLICE ≠ 0  (POLICE improves the model — Model 2 is better)",
    "",
    "Calculation:",
    ">>F = [(0.434 − 0.018) / 1]  /  [(1 − 0.434) / (100 − 3 − 1)]",
    ">>  = 0.416 / (0.566 / 96)",
    ">>  = 0.416 / 0.005896",
    ">>  = 70.56",
    "",
    "p-value = P(F ≥ 70.56) = 4.01 × 10⁻¹³  ≈  0.000  (essentially zero).",
    "",
    "Decision: p << 0.05 → Reject H₀.",
    "Conclusion: The R² of Model 2 is significantly larger. Adding POLICE significantly",
    "improves the model's explanatory power.",
]))
story.append(sp(10))

# Q2d ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q2d", "Why is the INHABITANTS_log coefficient different in both models?"))
story.append(sp(4))
story.append(q_box("Explain how it is possible that the estimated effect of the number of inhabitants "
                   "is different in both models, although both models are fitted using the same sample."))
story.append(sp(4))
story.append(guide_box("1.9",
    "Omitted Variable Bias — Ceteris Paribus Interpretation",
    "When a relevant variable (POLICE) is left out of Model 1, its effect gets absorbed "
    "into the remaining coefficients. The coefficient on INHABITANTS_log in Model 1 "
    "is biased because POLICE is correlated with INHABITANTS_log."))
story.append(sp(4))
story.append(data_tbl(
    ["Model","INHABITANTS_log coefficient","POLICE included?"],
    [["Model 1  (restricted)","B = +0.105","No — POLICE omitted"],
     ["Model 2  (full)","B = −0.267","Yes — POLICE included"]],
    cw=[4.5*cm,5.5*cm,6.5*cm]))
story.append(sp(4))
story.append(ans_box([
    "In Model 2, the coefficient of INHABITANTS_log (−0.267) measures the effect of city size",
    "on homicide rate HOLDING THE NUMBER OF POLICE OFFICERS CONSTANT (ceteris paribus).",
    "",
    "In Model 1, POLICE is not in the model, so its effect is not held constant.",
    "Any variation in homicide that is actually caused by POLICE gets incorrectly",
    "attributed to INHABITANTS_log instead.",
    "",
    "This is omitted variable bias: omitting POLICE biases the INHABITANTS_log coefficient",
    "upward (from −0.267 to +0.105, a swing of +0.372) because POLICE is correlated",
    "with INHABITANTS_log and has a positive effect on homicide.",
]))
story.append(sp(10))

# Q2e ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q2e", "Positive or negative correlation between INHABITANTS_log and POLICE?"))
story.append(sp(4))
story.append(q_box("Do you expect a positive or negative correlation between INHABITANTS_log "
                   "and POLICE? Explain using the output (not based on common sense)."))
story.append(sp(4))
story.append(guide_box("1.9",
    "Omitted Variable Bias — Reverse-Engineering the Correlation Sign",
    "We know the bias direction from the output (compare coefficients across models). "
    "Bias = sign(β_POLICE) × sign(r(INHABITANTS_log, POLICE)). "
    "Solve for sign(r) given the other two known signs."))
story.append(sp(4))
story.append(approach_box([
    "Step 1: From Model 2, β_POLICE = +0.065 > 0  → POLICE has a positive effect on HOMOCIDE.",
    "Step 2: The bias on INHABITANTS_log = coefficient in Model 1 MINUS coefficient in Model 2 "
    "= +0.105 − (−0.267) = +0.372 → POSITIVE bias.",
    "Step 3: sign(bias) = sign(β_POLICE) × sign(r(INHABITANTS_log, POLICE)).",
    "   (+0.372) = (+0.065) × sign(r)  →  sign(r) = positive.",
]))
story.append(sp(4))
story.append(ans_box([
    "From Model 2: POLICE has a significant positive effect on HOMOCIDE (B = 0.065, p < 0.001).",
    "",
    "Comparing the two models, the INHABITANTS_log coefficient changed from +0.105 (Model 1)",
    "to −0.267 (Model 2) — a positive bias of +0.372 was present in Model 1.",
    "",
    "Using the bias formula: sign(bias) = sign(β_POLICE) × sign(r(INHABITANTS_log, POLICE))",
    "  positive = (+) × sign(r)  →  sign(r) must be POSITIVE.",
    "",
    "Conclusion: There is a POSITIVE correlation between INHABITANTS_log and POLICE.",
    "(Larger cities tend to have more police officers — consistent with common sense too.)",
]))
story.append(sp(10))

# Q2f ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q2f", "Discuss the effect of SUN on number of inhabitants — with interaction"))
story.append(sp(4))
story.append(q_box("Discuss the effect of the variable SUN on the number of inhabitants in a city. "
                   "Model: INHABITANTS_log = β₀ + β₁SUN + β₂COAST + β₃(SUN×COAST) + ε. "
                   "Coefficients: Constant 7.779, SUN 0.000 (p=1.000), COAST 0.150 (p=0.000), "
                   "SUN×COAST 0.020 (p=0.000)."))
story.append(sp(4))
story.append(guide_box("1.3 + 1.4",
    "Log-Linear Interpretation + Interaction Terms",
    "The dependent variable is INHABITANTS_log = ln(INHABITANTS), making this a log-linear model. "
    "Rule for log-linear: 1-unit increase in X → β × 100% change in Y. "
    "The interaction term SUN×COAST means the effect of SUN DEPENDS ON whether the city is coastal. "
    "Split into two equations: one for COAST=0, one for COAST=1."))
story.append(sp(4))
story.append(approach_box([
    "The model is: ln(INHABITANTS) = 7.779 + 0.000·SUN + 0.150·COAST + 0.020·(SUN×COAST).",
    "Split by COAST value to isolate the SUN effect in each group:",
    "  Non-coast (COAST=0): ln(INHABITANTS) = 7.779 + 0.000·SUN  →  SUN slope = 0.000.",
    "  Coast (COAST=1): ln(INHABITANTS) = (7.779+0.150) + (0.000+0.020)·SUN = 7.929 + 0.020·SUN.",
    "Since Y = ln(INHABITANTS): interpret using log-linear rule  →  β × 100% change per 1-unit X.",
    "Check significance: SUN alone p=1.000; SUN×COAST p=0.000.",
]))
story.append(sp(4))
story.append(data_tbl(
    ["City type","Equation","SUN effect","Significant?"],
    [["Non-coast (COAST=0)","ln(INHABITANTS) = 7.779 + 0.000·SUN","0.000×100% = 0%","No (p=1.000)"],
     ["Coast (COAST=1)","ln(INHABITANTS) = 7.929 + 0.020·SUN","0.020×100% = +2% per day","Yes (p=0.000)"]],
    cw=[3.5*cm,5.5*cm,3.5*cm,3*cm]))
story.append(sp(4))
story.append(ans_box([
    "The effect of SUN depends on whether the city is coastal (interaction term).",
    "",
    "Non-coast cities: SUN has NO significant effect on the number of inhabitants.",
    "  The coefficient on SUN is 0.000 (p = 1.000) — cannot reject H₀ = no effect.",
    "",
    "Coast cities: SUN has a significant POSITIVE effect.",
    "  Each extra day of sunshine → 0.020 × 100% = 2% increase in the number of inhabitants.",
    "  (Because Y = ln(INHABITANTS), the log-linear interpretation applies: β × 100%.)",
    "",
    "The intercept shift for coast cities: COAST = 0.150 → coast cities have on average",
    "e^0.150 ≈ 16% more inhabitants than non-coast cities at the same level of SUN.",
]))
story.append(PageBreak())


# ════ Q3 ══════════════════════════════════════════════════════════════════════
story += [banner("QUESTION 3 — Chicken Demand   ·   chicken.sav   ·   7 points"), sp(6)]
story.append(Paragraph(
    "Goal: find a suitable time-series model for per-capita chicken consumption (q) as a function "
    "of real price (p). Always follow the Three-Step Framework: Stationarity → Fit → LMSC check.", body))
story.append(sp(8))

# Q3a ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q3a", "Check whether p and q are stationary — Dickey-Fuller test"))
story.append(sp(4))
story.append(q_box("Check whether p and q are stationary by carrying out suitable hypothesis tests. "
                   "(H₀/H₁, test statistic, conclusion.)"))
story.append(sp(4))
story.append(guide_box("2.2 — Step 1",
    "Dickey-Fuller Test for Stationarity",
    "First plot the series. Both q and p show upward trends → use DF Version 2 (with trend variable). "
    "Critical value = −3.41 at 5%.  NEVER use the Sig. p-value from SPSS for this test — "
    "compare the t-statistic for the LAG variable directly to −3.41."))
story.append(sp(4))
story.append(approach_box([
    "Time plots of both q and p show a clear upward trend → select DF Version 2.",
    "Create DIFF_q = q − LAG(q,1) and LAG_q = LAG(q,1).",
    "Run: Dependent = DIFF_q, Independent = LAG_q AND Year (trend variable).",
    "Read t-statistic for LAG_q.  Compare to −3.41.  Ignore the Sig. column.",
    "Repeat exactly for p: DIFF_p, LAG_p, regression with LAG_p and Year.",
]))
story.append(sp(4))
story.append(spss_box([
    "Transform → Compute:  DIFF_q = q − LAG(q,1)   |   LAG_q = LAG(q,1).",
    "Transform → Compute:  DIFF_p = p − LAG(p,1)   |   LAG_p = LAG(p,1).",
    "Analyze → Regression → Linear:  Dependent=DIFF_q,  Independent=LAG_q, Year.  OK.",
    "  Read t for LAG_q.  Compare to −3.41  (NOT the Sig. column!).",
    "Analyze → Regression → Linear:  Dependent=DIFF_p,  Independent=LAG_p, Year.  OK.",
    "  Read t for LAG_p.  Compare to −3.41.",
], title="SPSS: DF Test Version 2 (with trend) for Levels"))
story.append(sp(4))
story.append(fig_to_image(plot_df_q3(), 16.5))
story.append(fig_label("Figure Q3a/b — Left: DF results for levels q and p (Version 2, CV=−3.41). "
                       "Both t-statistics are above the critical value → non-stationary. "
                       "Right: DF results for first differences (Version 1, CV=−2.86). "
                       "Both t-statistics are far below the critical value → stationary."))
story.append(sp(4))
story.append(ans_box([
    "Both series show a trend in the time plot → DF Version 2 (with trend).",
    "Critical value = −3.41  (5% level, Version 2).",
    "",
    "Is q stationary?",
    "  H₀: α₁ = 0 (unit root — non-stationary)   H₁: α₁ < 0 (stationary)",
    "  Auxiliary model: Δqₜ = α₀ + α₁ qₜ₋₁ + α₂ t + εₜ",
    "  t-statistic for LAG_q = −1.639.   −1.639 > −3.41  →  NOT more negative than CV.",
    "  Decision: Fail to reject H₀.  q is NOT stationary.",
    "",
    "Is p stationary?",
    "  H₀: α₁ = 0   H₁: α₁ < 0",
    "  Auxiliary model: Δpₜ = α₀ + α₁ pₜ₋₁ + α₂ t + εₜ",
    "  t-statistic for LAG_p = −2.458.   −2.458 > −3.41  →  NOT more negative than CV.",
    "  Decision: Fail to reject H₀.  p is NOT stationary.",
]))
story.append(sp(10))

# Q3b ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q3b", "Do the same for the first-order differences of p and q"))
story.append(sp(4))
story.append(q_box("Do the same for the first order differences of p and q."))
story.append(sp(4))
story.append(guide_box("2.2 — Step 1 continued",
    "DF Test on First Differences — Determining I(1)",
    "Plot Δq and Δp. If they show no trend → use DF Version 1 (no trend). "
    "Critical value = −2.86. If both differences are stationary, both original series are I(1)."))
story.append(sp(4))
story.append(approach_box([
    "Time plots of Δq and Δp do NOT show a clear upward trend → use DF Version 1.",
    "Create DIFF2_q = DIFF_q − LAG(DIFF_q,1) and LAG_DIFF_q = LAG(DIFF_q,1).",
    "Run: Dependent = DIFF2_q, Independent = LAG_DIFF_q only (no Year this time).",
    "Read t for LAG_DIFF_q.  Compare to −2.86.  Repeat for p.",
]))
story.append(sp(4))
story.append(spss_box([
    "Transform → Compute:  DIFF2_q = DIFF_q − LAG(DIFF_q,1)   |   LAG_DIFF_q = LAG(DIFF_q,1).",
    "Transform → Compute:  DIFF2_p = DIFF_p − LAG(DIFF_p,1)   |   LAG_DIFF_p = LAG(DIFF_p,1).",
    "Analyze → Regression → Linear:  Dependent=DIFF2_q,  Independent=LAG_DIFF_q only.  OK.",
    "  Read t for LAG_DIFF_q.  Compare to −2.86.",
    "Analyze → Regression → Linear:  Dependent=DIFF2_p,  Independent=LAG_DIFF_p only.  OK.",
    "  Read t for LAG_DIFF_p.  Compare to −2.86.",
], title="SPSS: DF Test Version 1 (no trend) for First Differences"))
story.append(sp(4))
story.append(ans_box([
    "First differences show no obvious trend → DF Version 1 (no trend).",
    "Critical value = −2.86  (5% level, Version 1).",
    "",
    "Is Δq stationary?",
    "  H₀: α₁ = 0   H₁: α₁ < 0",
    "  Auxiliary model: ΔΔqₜ = α₀ + α₁ Δqₜ₋₁ + εₜ",
    "  t-statistic for LAG_DIFF_q = −7.200.   −7.200 < −2.86  →  more negative than CV.",
    "  Decision: Reject H₀.  Δq IS stationary ✓",
    "",
    "Is Δp stationary?",
    "  H₀: α₁ = 0   H₁: α₁ < 0",
    "  Auxiliary model: ΔΔpₜ = α₀ + α₁ Δpₜ₋₁ + εₜ",
    "  t-statistic for LAG_DIFF_p = −9.431.   −9.431 < −2.86  →  more negative than CV.",
    "  Decision: Reject H₀.  Δp IS stationary ✓",
    "",
    "Conclusion: Both q and p are I(1) — they have a unit root in levels but are stationary",
    "after first differencing.  This drives the model choice in Q3c.",
]))
story.append(sp(10))

# Q3c ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q3c", "Levels or first differences for the static model?"))
story.append(sp(4))
story.append(q_box("To set up a static model for demand as a function of price, do you prefer a model "
                   "based on the original variables p and q, or on the first order differences? Explain."))
story.append(sp(4))
story.append(guide_box("2.3",
    "Choosing the Right Variables — Stationarity Rule",
    "A fundamental rule: never regress a non-stationary series on another non-stationary series "
    "without checking for cointegration. Using non-stationary series in levels risks "
    "spurious regression (high R², but relationship is meaningless). "
    "When both series are I(1) and not cointegrated, use first differences."))
story.append(sp(4))
story.append(ans_box([
    "From Q3a: both q and p are NON-STATIONARY in levels.",
    "From Q3b: both Δq and Δp ARE stationary (I(1) series).",
    "",
    "Preferred choice: use FIRST DIFFERENCES (Δq and Δp).",
    "",
    "Reason: regressing non-stationary q on non-stationary p risks SPURIOUS REGRESSION.",
    "A spurious regression produces a high R² and significant t-statistics even when",
    "the two series have no true relationship — the apparent relationship is driven by",
    "the common upward drift in both series, not by a genuine economic link.",
    "",
    "By using first differences (which are stationary), we eliminate the unit root",
    "problem and can interpret the results as a genuine causal relationship.",
]))
story.append(sp(10))

# Q3d ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q3d", "Fit the static model and test price significance"))
story.append(sp(4))
story.append(q_box("Set up the static model you preferred in part c and carry out a suitable test "
                   "to check whether the price difference has a significant effect on demand difference."))
story.append(sp(4))
story.append(guide_box("2.3 + 1.5",
    "Static Model · Individual t-test",
    "Static model: Δqₜ = β₀ + β₁Δpₜ + εₜ.  "
    "Test H₀: β₁ = 0 using the t-test p-value (Sig. column) from the SPSS Coefficients table."))
story.append(sp(4))
story.append(spss_box([
    "Analyze → Regression → Linear…",
    "  Dependent: DIFF_q   |   Independent(s): DIFF_p",
    "Click OK.  Read the Coefficients table row for DIFF_p: B, t, Sig.",
], title="SPSS: Run the Static First-Difference Model"))
story.append(sp(4))
story.append(data_tbl(
    ["","B","Std. Error","t","Sig."],
    [["(Constant)","0.678","0.129","5.264","0.000"],
     ["DIFF_p (= Δp)","−2.596","1.057","−2.456","0.018"]],
    cw=[3*cm,3*cm,3*cm,3*cm,4.5*cm]))
story.append(sp(4))
story.append(ans_box([
    "Model specification: Δqₜ = β₀ + β₁·Δpₜ + εₜ",
    "Fitted model: Δq = 0.678 − 2.596·Δp",
    "",
    "Hypothesis test for price effect:",
    "  H₀: β₁ = 0  (price change has no effect on demand change)",
    "  H₁: β₁ ≠ 0  (price change has a significant effect)",
    "",
    "Test statistic: t = −2.456",
    "p-value = 0.018 < 0.05  →  Reject H₀.",
    "",
    "Conclusion: The change in price has a statistically significant effect on the change",
    "in demand at the 5% level.",
    "",
    "Interpretation: A 1-unit increase in the price difference leads to a 2.596-unit",
    "decrease in the demand difference — as expected (higher price → lower consumption).",
]))
story.append(sp(10))

# Q3e ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q3e", "Test for autocorrelation — LMSC test on the static model"))
story.append(sp(4))
story.append(q_box("Consider the model from Q3d. Carry out a hypothesis test to check for autocorrelation. "
                   "(H₀/H₁, auxiliary model, test statistic, p-value, conclusion.)"))
story.append(sp(4))
story.append(guide_box("2.6 — Step 3",
    "LMSC Autocorrelation Test",
    "Save residuals from the Q3d model. Create LAG_RES. Run auxiliary regression: "
    "RES_1 = α₀ + α₁·DIFF_p + α₂·LAG_RES + u. "
    "LM = n × R²_aux ~ χ²(1). Critical value = 3.841. NEVER use Durbin-Watson here."))
story.append(sp(4))
story.append(spss_box([
    "In the Q3d regression dialog: click Save… → check Unstandardized Residuals → Continue → OK.",
    "  SPSS creates variable RES_1 in the dataset.",
    "Transform → Compute:  LAG_RES1 = LAG(RES_1, 1)   OK.",
    "Analyze → Regression → Linear…",
    "  Dependent: RES_1   |   Independent(s): DIFF_p  AND  LAG_RES1",
    "  Click OK.  Record R²_aux from Model Summary.",
    "  n_aux = Total df + 1 from the ANOVA table.",
    "Compute: LM = n_aux × R²_aux.  Compare to 3.841.",
], title="SPSS: LMSC Test — Auxiliary Regression on Residuals"))
story.append(sp(4))
story.append(data_tbl(
    ["Auxiliary model R²","n_aux (Total df + 1)","LM = n × R²","Critical value","Decision"],
    [["R²_aux = 0.011943","50 × 1 + 0 = 50","50 × 0.011943 = 0.597","3.841","0.597 < 3.841 → Fail to reject"]],
    cw=[4*cm,4*cm,3*cm,3*cm,2.5*cm]))
story.append(sp(4))
story.append(ans_box([
    "H₀: ρ = 0  (no autocorrelation — Assumption A3 satisfied)",
    "H₁: ρ ≠ 0  (autocorrelation present — A3 violated)",
    "",
    "Auxiliary regression: eₜ = α₀ + α₁·Δpₜ + α₂·eₜ₋₁ + uₜ",
    "",
    "R²_aux = 0.011943.  n_aux = 50 (from ANOVA Total df + 1).",
    "LM = 50 × 0.011943 = 0.597",
    "",
    "p-value = P(χ²(1) ≥ 0.597) = 0.4397 > 0.05.",
    "",
    "Decision: Fail to reject H₀.",
    "Conclusion: No significant evidence of autocorrelation.  Assumption A3 is",
    "plausibly satisfied.  The static model residuals are not serially correlated.",
]))
story.append(sp(10))

# Q3f ─────────────────────────────────────────────────────────────────────────
story.append(sub_q("Q3f", "Distributed lag model — top-down selection from DL(3)"))
story.append(sp(4))
story.append(q_box("Estimate a distributed lag model with maximum lag = 3. "
                   "How many lags will you use in the final model? Explain with intermediate results."))
story.append(sp(4))
story.append(guide_box("2.4",
    "DL(q) — Top-Down Lag Selection",
    "Start at q_max=3. At each step look at the Sig. of the HIGHEST lag in the model. "
    "If Sig. > 0.05 → drop that lag → refit at q−1. "
    "Stop when the highest remaining lag is significant (Sig. ≤ 0.05). "
    "NEVER drop an intermediate lag — structure must remain contiguous."))
story.append(sp(4))
story.append(spss_box([
    "Transform → Compute:  LAG1_DIFF_p = LAG(DIFF_p, 1)   OK.",
    "Transform → Compute:  LAG2_DIFF_p = LAG(DIFF_p, 2)   OK.",
    "Transform → Compute:  LAG3_DIFF_p = LAG(DIFF_p, 3)   OK.",
    "Step 1 — Fit DL(3): Dependent=DIFF_q, Independent=DIFF_p, LAG1, LAG2, LAG3.  Read Sig. of LAG3.",
    "Step 2 — If LAG3 not significant: remove it. Fit DL(2): Dependent=DIFF_q, IVs=DIFF_p, LAG1, LAG2.",
    "Step 3 — If LAG2 not significant: remove it. Fit DL(1): Dependent=DIFF_q, IVs=DIFF_p, LAG1.",
    "Step 4 — If LAG1 not significant: remove it. Final model = static (DIFF_p only).",
    "Stop as soon as the highest lag IS significant.",
], title="SPSS: Top-Down DL Lag Selection"))
story.append(sp(4))
story.append(fig_to_image(plot_dl_topdown(), 16))
story.append(fig_label("Figure Q3f — p-value of the highest lag at each step of top-down selection. "
                       "Red bars = not significant (p > 0.05) → lag dropped. "
                       "Green bar = final static model (p = 0.018 for DIFF_p). "
                       "All three lags are dropped → optimal q = 0."))
story.append(sp(4))

story.append(data_tbl(
    ["Step","Model","Highest lag","Sig. of highest lag","Decision"],
    [["1","DL(3): DIFF_p + LAG1 + LAG2 + LAG3","LAG3","0.053  >  0.05","Drop LAG3"],
     ["2","DL(2): DIFF_p + LAG1 + LAG2",        "LAG2","0.064  >  0.05","Drop LAG2"],
     ["3","DL(1): DIFF_p + LAG1",               "LAG1","0.128  >  0.05","Drop LAG1"],
     ["4","DL(0) = Static: DIFF_p only",        "DIFF_p","0.018  <  0.05","STOP — keep"]],
    cw=[1.2*cm,5.5*cm,2.2*cm,3.5*cm,3*cm]))
story.append(sp(4))
story.append(ans_box([
    "Step 1 — DL(3): Δq = 0.776 + (−2.214)Δp + 0.640Δpₜ₋₁ + (−1.552)Δpₜ₋₂ + 2.134Δpₜ₋₃",
    "  Sig. of LAG3 = 0.053 > 0.05 → NOT significant → drop LAG3.",
    "",
    "Step 2 — DL(2): Δq = 0.685 + (−1.750)Δp + 1.153Δpₜ₋₁ + (−2.089)Δpₜ₋₂",
    "  Sig. of LAG2 = 0.064 > 0.05 → NOT significant → drop LAG2.",
    "",
    "Step 3 — DL(1): Δq = 0.765 + (−2.090)Δp + 1.711Δpₜ₋₁",
    "  Sig. of LAG1 = 0.128 > 0.05 → NOT significant → drop LAG1.",
    "",
    "Step 4 — DL(0) = Static: Δq = 0.678 − 2.596Δp",
    "  Sig. of DIFF_p = 0.018 < 0.05 → SIGNIFICANT → STOP.",
    "",
    "Final answer: 0 lags are used in the final model.",
    "The optimal model is the static model already fitted in Q3d.",
    "The price effect is immediate only — no lagged price effects are significant.",
    "",
    "Total multiplier = β₀ = −2.596  (same as immediate effect since q = 0).",
]))
story.append(sp(14))

# ── Final tip box ─────────────────────────────────────────────────────────────
tip_hdr = S("th2",fontSize=10,fontName="DV-B",textColor=WHITE,leading=14)
tip_sty = S("ts2",fontSize=9.5,leading=14,textColor=BLACK)
tip_rows = [[Paragraph("  ★  General Exam Strategy — Key Reminders", tip_hdr)]]
for tip in [
    "Q1-type (MLR): always check for categorical variables → need k−1 dummies. "
    "If a variable is logged, use the β/100 interpretation for linear-log.",
    "Q1c-type (joint test): the phrase 'does Region have a significant effect' means ONE joint F-test, "
    "not three separate t-tests. Use SPSS block method to get the F change automatically.",
    "Q1f-type (omitted variable): apply sign(β_Z) × sign(r(X,Z)) to find bias direction. "
    "Two negatives = positive bias = overestimate.",
    "Q2c-type (model comparison): the restricted model has FEWER variables; its SSE is always LARGER.",
    "Q2e-type (reverse bias): use the known bias direction and β_omitted sign to solve for r sign.",
    "Q3-type (time series): ALWAYS check stationarity first. Non-stationary series → use differences. "
    "NEVER use p-value from SPSS for DF test — compare t directly to −2.86 or −3.41.",
    "Q3e-type (LMSC): auxiliary regression must include ALL original X variables + lagged residual. "
    "LM = n × R²_aux ~ χ²(1). Critical value = 3.841.",
    "Q3f-type (DL top-down): only drop the HIGHEST lag. If lag 2 is significant keep lag 1 even if "
    "lag 1 is not — never skip a lag in the middle.",
]:
    tip_rows.append([Paragraph(f"  • {tip}", tip_sty)])
tip_t = Table(tip_rows, colWidths=[W])
tip_t.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(0,0),colors.HexColor("#1A6B3A")),
    ("BACKGROUND",(0,1),(-1,-1),LIGHT_GREEN),
    ("BOX",(0,0),(-1,-1),1,colors.HexColor("#1A6B3A")),
    ("INNERGRID",(0,1),(-1,-1),0.3,GREY_LINE),
    ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),10),
    ("VALIGN",(0,0),(-1,-1),"TOP"),
]))
story.append(tip_t)

doc.build(story)
print("Walkthrough PDF created successfully.")

