#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable, KeepTogether)
from reportlab.platypus.flowables import Flowable

W, H = A4
DARK_BLUE  = colors.HexColor('#1a3a5c')
MED_BLUE   = colors.HexColor('#2e6da4')
LIGHT_BLUE = colors.HexColor('#dce6f1')
LIGHT_GREY = colors.HexColor('#f2f2f2')
MED_GREY   = colors.HexColor('#cccccc')
LIGHT_RED  = colors.HexColor('#fdecea')
LIGHT_GRN  = colors.HexColor('#e8f5e9')
AMBER      = colors.HexColor('#e67e00')
GREEN      = colors.HexColor('#1a6b2a')
WHITE      = colors.white

def style(name, **kw):
    defaults = dict(fontName='Helvetica', fontSize=10, leading=14,
                    spaceAfter=6, spaceBefore=0, textColor=colors.black)
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)

S = {
    'title'  : style('title',  fontSize=20, fontName='Helvetica-Bold',
                     textColor=DARK_BLUE, alignment=TA_CENTER, spaceAfter=4),
    'sub'    : style('sub',    fontSize=13, fontName='Helvetica-Bold',
                     textColor=MED_BLUE,  alignment=TA_CENTER, spaceAfter=4),
    'tag'    : style('tag',    fontSize=10, fontName='Helvetica-Oblique',
                     textColor=colors.grey, alignment=TA_CENTER, spaceAfter=16),
    'part'   : style('part',   fontSize=13, fontName='Helvetica-Bold',
                     textColor=WHITE, backColor=DARK_BLUE,
                     borderPadding=(6,8,6,8), spaceAfter=10, spaceBefore=18),
    'chap'   : style('chap',   fontSize=12, fontName='Helvetica-Bold',
                     textColor=WHITE, backColor=MED_BLUE,
                     borderPadding=(5,6,5,6), spaceAfter=8, spaceBefore=14),
    'h2'     : style('h2',     fontSize=11, fontName='Helvetica-Bold',
                     textColor=DARK_BLUE, spaceAfter=5, spaceBefore=10),
    'h3'     : style('h3',     fontSize=10, fontName='Helvetica-Bold',
                     textColor=MED_BLUE,  spaceAfter=4, spaceBefore=7),
    'body'   : style('body',   alignment=TA_JUSTIFY),
    'bull'   : style('bull',   leftIndent=14, spaceAfter=3),
    'form'   : style('form',   fontSize=11, fontName='Helvetica-Bold',
                     alignment=TA_CENTER, backColor=LIGHT_GREY,
                     borderPadding=(8,8,8,8), spaceAfter=8, spaceBefore=6),
    'code'   : style('code',   fontSize=9, fontName='Courier',
                     backColor=LIGHT_GREY, borderPadding=(6,8,6,8),
                     leading=13, spaceAfter=6),
    'note'   : style('note',   backColor=LIGHT_BLUE,
                     borderPadding=(8,8,8,8), spaceAfter=8, spaceBefore=4),
    'warn'   : style('warn',   backColor=LIGHT_RED,
                     borderPadding=(8,8,8,8), spaceAfter=8, spaceBefore=4),
    'ok'     : style('ok',     backColor=LIGHT_GRN,
                     borderPadding=(8,8,8,8), spaceAfter=8, spaceBefore=4),
    'new'    : style('new',    fontSize=8, fontName='Helvetica-Bold',
                     textColor=WHITE, backColor=GREEN,
                     borderPadding=(2,4,2,4), spaceAfter=4),
    'fixed'  : style('fixed',  fontSize=8, fontName='Helvetica-Bold',
                     textColor=WHITE, backColor=AMBER,
                     borderPadding=(2,4,2,4), spaceAfter=4),
    'qbox'   : style('qbox',   fontName='Helvetica-Bold', textColor=DARK_BLUE,
                     backColor=LIGHT_BLUE, borderPadding=(6,8,6,8),
                     spaceAfter=4, spaceBefore=8),
    'ans'    : style('ans',    backColor=LIGHT_GRN,
                     borderPadding=(6,8,6,8), spaceAfter=6),
    'thdr'   : style('thdr',   fontSize=9, fontName='Helvetica-Bold',
                     textColor=WHITE),
    'tcell'  : style('tcell',  fontSize=9, leading=12),
}

def p(txt, s='body'): return Paragraph(txt, S[s])
def sp(h=6):          return Spacer(1, h)
def hr():             return HRFlowable(width='100%', thickness=0.5,
                                        color=MED_GREY, spaceAfter=6, spaceBefore=6)
def pb():             return PageBreak()

def tbl(data, cw=None, hrows=1):
    td = []
    for i, row in enumerate(data):
        nr = []
        for cell in row:
            st = S['thdr'] if i < hrows else S['tcell']
            nr.append(Paragraph(str(cell), st) if isinstance(cell, str) else cell)
        td.append(nr)
    t = Table(td, colWidths=cw, repeatRows=hrows)
    t.setStyle(TableStyle([
        ('BACKGROUND',  (0,0), (-1,hrows-1), DARK_BLUE),
        ('TEXTCOLOR',   (0,0), (-1,hrows-1), WHITE),
        ('GRID',        (0,0), (-1,-1), 0.4, MED_GREY),
        ('LINEBELOW',   (0,hrows-1), (-1,hrows-1), 1.2, DARK_BLUE),
        ('ROWBACKGROUNDS', (0,hrows), (-1,-1), [WHITE, colors.HexColor('#f8f9fa')]),
        ('TOPPADDING',  (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',(0,0),(-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING',(0,0), (-1,-1), 6),
        ('VALIGN',      (0,0), (-1,-1), 'TOP'),
    ]))
    return t

# ── page number footer ──────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.grey)
    canvas.drawCentredString(W/2, 1.2*cm,
        f'Statistics — Time Series Regression | Page {doc.page}')
    canvas.restoreState()

# ═══════════════════════════════════════════════════════════════════════════
# BUILD CONTENT
# ═══════════════════════════════════════════════════════════════════════════
def build():
    items = []

    # ── COVER ──────────────────────────────────────────────────────────────
    items += [sp(60),
              p('STATISTICS — COMPLETE BEGINNER\'S GUIDE', 'title'), sp(6),
              p('Time Series Regression', 'sub'),
              p('From Zero to Full Understanding', 'tag'), hr(), sp(10),
              p('<b>Who this guide is for.</b> This document assumes you have never studied '
                'statistics before. Every concept is built from the ground up with plain '
                'language and step-by-step worked examples.', 'body'), sp(6),
              p('<b>What is new in this edition.</b> Four improvements over the original:<br/>'
                '(1) <b>Confidence intervals</b> — new Section 0.4.1 explains construction and '
                'interpretation.<br/>'
                '(2) <b>Fixed ρ magnitude table</b> — the table in B.2 now shows what each '
                'range of ρ means in practice.<br/>'
                '(3) <b>Fixed Summary Card</b> — the four AR(1) cases table in C.3 now has '
                'complete Stationary? and Fix columns.<br/>'
                '(4) <b>Practice exam questions</b> — six fully worked exam-style questions '
                'added at the end.', 'note'), hr(), pb()]

    # ── NOTATION GLOSSARY ──────────────────────────────────────────────────
    items += [p('NOTATION GLOSSARY — Read This First', 'part'),
              p('Every symbol you will encounter, explained in plain English.', 'body'), sp(4),
              tbl([['Symbol','Name','Plain Meaning'],
                   ['Y','Dependent variable','The thing you are trying to predict or explain'],
                   ['X','Independent variable','The thing you use to explain Y'],
                   ['t','Time index','Which time period we are in (t = 1 means year 1)'],
                   ['i','Individual index','Which person/firm/country we are looking at'],
                   ['β (beta)','Regression coefficient','How much Y changes when X changes by 1 unit'],
                   ['α (alpha)','Intercept','The value of Y when all X\'s = 0'],
                   ['ε (epsilon)','Error / residual','The part of Y that our model fails to explain'],
                   ['ρ (rho)','Autocorrelation coeff.','How strongly this period\'s error relates to last period\'s'],
                   ['γ (gamma)','AR coeff. on lagged Y','How much last period\'s Y feeds into this period\'s Y'],
                   ['λ (lambda)','Trend slope','How much the mean of Y grows each period'],
                   ['σ²','Variance','Measure of spread / unpredictability'],
                   ['Δ (delta)','First difference','Change from one period to the next: ΔX_t = X_t − X_{t−1}'],
                   ['Σ (sigma)','Sum','Add up everything that follows'],
                   ['H₀','Null hypothesis','The "boring" default claim we try to disprove'],
                   ['H₁','Alternative hypothesis','The "interesting" claim we want to support'],
                   ['n','Sample size','Total number of observations'],
                   ['R²','R-squared','Proportion of Y\'s variation explained by the model (0 to 1)'],
                   ['SE','Standard error','How much a coefficient estimate varies across samples'],
                   ['CI','Confidence interval','A range of plausible values for the true coefficient  ★ NEW'],
                   ['LM','Lagrange Multiplier','Test statistic to check for autocorrelation'],
                   ['χ²','Chi-squared','A probability distribution used for some hypothesis tests'],
                   ['DW','Durbin-Watson','Quick autocorrelation check (limited use)']],
                  cw=[2.2*cm, 4*cm, 10.8*cm]), pb()]

    # ── PART 0 ─────────────────────────────────────────────────────────────
    items += [p('PART 0 — STATISTICS FOUNDATIONS', 'part'),
              p('Everything in this section is background knowledge that the rest of the guide '
                'builds on.', 'body')]

    items += [p('0.1 — What Is Statistics? What Is Regression?', 'h2'),
              p('<b>Statistics</b> is the science of learning from data. We observe the world, '
                'collect numbers, and try to answer questions like: Does more education cause '
                'higher wages? Does advertising increase sales?', 'body'),
              p('<b>Regression</b> is the central tool. It finds the relationship between '
                'explanatory variables (X\'s) and an outcome variable (Y).', 'body'),
              p('The Simplest Regression (One Variable)', 'h3'),
              p('Y = α + βX + ε', 'form'),
              tbl([['Term','Meaning','Example'],
                   ['Y','Outcome to explain','Hourly wage (€)'],
                   ['X','Thing that explains Y','Years of education'],
                   ['α','Baseline Y when X = 0','Wage with zero education'],
                   ['β','Slope — change in Y per 1-unit rise in X','€1.20 more per extra year'],
                   ['ε','Error — what the model misses','Luck, unobserved talent']],
                  cw=[1.8*cm, 7*cm, 8.2*cm]),
              p('<b>Example:</b> Wage = 5 + 1.2 × Education + ε. A person with 10 years of '
                'education earns an estimated 5 + 1.2 × 10 = <b>€17/hour</b>. If actual wage '
                'is €19, residual = €2.', 'body'),
              p('Multiple Regression (Several Variables)', 'h3'),
              p('Y = α + β₁X₁ + β₂X₂ + … + βₖXₖ + ε', 'form'),
              p('Each βⱼ = the <i>ceteris paribus</i> (all else equal) effect of Xⱼ on Y.', 'body')]

    items += [p('0.2 — How Regression Is Estimated: OLS', 'h2'),
              p('<b>OLS = Ordinary Least Squares.</b> Chooses α and β to minimise the sum of '
                'squared errors across all observations:', 'body'),
              p('min Σ εᵢ² = Σ (Yᵢ − α − βXᵢ)²', 'form'),
              p('<b>Why square them?</b> (1) Positive and negative errors do not cancel. '
                '(2) Large errors are penalised more than small ones.', 'body'),
              p('OLS gives coefficient estimates <b>β̂</b> ("beta hat") — the best-fitting line.<br/>'
                '<b>BLUE:</b> When classical assumptions hold, OLS is the Best Linear Unbiased '
                'Estimator — no other linear method has smaller estimation errors.', 'body')]

    items += [p('0.3 — R²: How Well Does the Model Fit?', 'h2'),
              p('R² = 1 − (Sum of Squared Errors) / (Total Variation in Y)', 'form'),
              tbl([['R² Value','Meaning'],
                   ['0.0','Model explains nothing — X tells us nothing about Y'],
                   ['0.5','Model explains 50% of Y\'s variation'],
                   ['1.0','Perfect fit — model explains everything'],
                   ['0.95','Looks great — but in time-series this can signal spurious regression ⚠']],
                  cw=[3*cm, 14*cm]),
              p('<b>Intuition:</b> Imagine Y is ocean-wave height. Total variation = how much '
                'waves differ from average. If the model explains 80%, R² = 0.80.', 'body')]

    items += [p('0.4 — Standard Errors, t-statistics, and p-values', 'h2'),
              p('<b>Standard errors (SE)</b> measure how much β̂ varies if we collected a '
                'different sample.', 'body'),
              p('t = β̂ / SE(β̂)', 'form'),
              p('A large |t| (say > 2): estimate is far from zero — likely real.<br/>'
                'A small |t| (say < 1): estimate could easily be zero by chance.', 'body'),
              tbl([['p-value','Interpretation'],
                   ['p < 0.01','Very strong evidence against H₀ (significant at 1%)'],
                   ['p < 0.05','Strong evidence against H₀ (significant at 5%) — standard threshold'],
                   ['p < 0.10','Weak evidence against H₀ (significant at 10%)'],
                   ['p > 0.10','No convincing evidence; cannot reject H₀']],
                  cw=[3*cm, 14*cm]),
              p('<b>Analogy:</b> Flip a coin 20 times and get 17 heads. The p-value asks: '
                '"If fair coin (H₀), how likely is 17+ heads?" If tiny (p < 0.05), conclude '
                'coin is probably not fair — reject H₀.', 'body'),
              p('<b>Important:</b> We never "accept H₀". We either reject it or <i>fail to '
                'reject</i> it. Failing to reject means the data do not give us enough evidence '
                '— not that H₀ is definitely true.', 'note')]

    # NEW: Confidence Intervals
    items += [p('★ NEW', 'new'),
              p('0.4.1 — Confidence Intervals', 'h2'),
              p('A <b>confidence interval (CI)</b> gives a range of plausible values for the '
                'true β. The most common is the 95% CI:', 'body'),
              p('95% CI = β̂ ± 1.96 × SE(β̂)', 'form'),
              p('<b>What this means:</b> If we repeated the study many times, 95% of the '
                'intervals constructed this way would contain the true β.', 'body'),
              p('<b>Three key rules:</b>', 'h3'),
              p('1. If the CI does <b>NOT</b> include zero → coefficient is statistically '
                'significant at 5%.', 'bull'),
              p('2. If the CI <b>DOES</b> include zero → cannot reject H₀ (consistent with '
                'no effect).', 'bull'),
              p('3. Narrower CI = more precise estimate (comes from larger n or smaller SE).', 'bull'),
              sp(4),
              tbl([['Confidence Level','Formula','Use when'],
                   ['90% CI','β̂ ± 1.645 × SE','Less strict threshold'],
                   ['95% CI','β̂ ± 1.96 × SE','Standard — most common'],
                   ['99% CI','β̂ ± 2.576 × SE','Very strict threshold']],
                  cw=[4*cm, 6*cm, 7*cm]),
              p('<b>Relationship to t-test:</b> The 95% CI excludes zero if and only if '
                '|t| > 1.96. They always agree — you cannot get a significant t-test but an '
                'insignificant CI, or vice versa.', 'body'),
              p('<b>Worked Example:</b> A wage regression gives β̂(education) = 1.20, SE = 0.35, '
                't = 3.43, p = 0.001.<br/>'
                '95% CI = 1.20 ± 1.96 × 0.35 = 1.20 ± 0.686 = <b>[0.51, 1.89]</b><br/>'
                'Interpretation: We are 95% confident that one extra year of education raises '
                'wages by between <b>€0.51 and €1.89 per hour</b>.<br/>'
                'Since CI excludes zero → significant at 5% ✓ (consistent with p = 0.001).', 'ok')]

    items += [p('0.5 — The Five Classical Assumptions', 'h2'),
              p('OLS is BLUE (Best Linear Unbiased Estimator) only when these hold:', 'body'),
              tbl([['Assumption','Formal Statement','Why It Matters'],
                   ['A1','E(ε) = 0','Errors average to zero — no systematic over/under-prediction'],
                   ['A2','Var(ε) = σ² (constant)','Homoskedasticity — equal spread of errors everywhere'],
                   ['A3','cov(εᵢ, εⱼ) = 0 for i ≠ j','Errors are uncorrelated with each other'],
                   ['A4','X\'s non-random, not perfectly collinear','We can separate each X\'s individual effect'],
                   ['A5','ε ~ Normal (optional)','Needed for exact inference in small samples']],
                  cw=[2.2*cm, 5.5*cm, 9.3*cm]),
              p('<b>Time-series warning:</b> A3 is routinely violated in time-series data '
                '(autocorrelation). A new assumption is also needed: <b>stationarity</b>.', 'warn'), pb()]

    # ── CHAPTER TS_A ───────────────────────────────────────────────────────
    items += [p('PART 1 — TIME SERIES FOUNDATIONS', 'part'),
              p('CHAPTER TS_A — Cautions', 'chap'),
              p('<i>What makes time-series data special and why ordinary regression needs '
                'modification.</i>', 'body')]

    items += [p('A.1 — Cross-Section vs. Time-Series Data', 'h2'),
              tbl([['Type','Description','Notation','Order Matters?'],
                   ['Cross-section','Many units at one point in time','X_i (i = individual)','No — rows interchangeable'],
                   ['Time-series','One unit observed repeatedly over time','X_t (t = time period)','YES — shuffling destroys information'],
                   ['Panel data','Many units over many time periods','X_{it}','Both dimensions matter']],
                  cw=[3*cm, 5.5*cm, 4.5*cm, 4*cm]),
              p('<b>Why order matters:</b> In a cross-section of 1,000 workers you could '
                'reorder rows and get the same regression result. In a time series of 40 years '
                'of GDP, row 5 must come after row 4 — the temporal structure IS the point.', 'body')]

    items += [p('A.2 — Lagged Variables', 'h2'),
              p('A <b>lag</b> is the value of a variable at an earlier time period — like '
                'looking in the rear-view mirror.', 'body'),
              tbl([['Notation','Meaning','Value refers to'],
                   ['X_t','Current value','Current period'],
                   ['X_{t−1}','One-period lag','One period ago'],
                   ['X_{t−2}','Two-period lag','Two periods ago'],
                   ['X_{t−q}','q-period lag','q periods ago']],
                  cw=[3*cm, 5*cm, 9*cm]),
              p('<b>Visual — lag in data:</b>', 'h3'),
              tbl([['t','X_t (original)','X_{t−1} (lag 1)'],
                   ['1','10','— (missing, no period 0)'],
                   ['2','14','10  ← from t=1'],
                   ['3','11','14  ← from t=2'],
                   ['4','16','11  ← from t=3'],
                   ['5','13','16  ← from t=4']],
                  cw=[3*cm, 5*cm, 9*cm]),
              p('<b>Why lags are needed:</b> Economic processes rarely respond instantaneously. '
                'Safety training in month t → behaviour change → accident reduction in t+1, t+2. '
                'Central bank rate rise → affects spending over 6–12 months.', 'body'),
              p('<b>Lost observations:</b> Lag of order q costs q observations. Starting with '
                'n = 100, a DL(3) model leaves only 97 usable rows.', 'note')]

    items += [p('A.3 — Difference Variables', 'h2'),
              p('ΔX_t = X_t − X_{t−1}', 'form'),
              p('<b>Example:</b> GDP was €100bn last year, €104bn this year → ΔGDP = +€4bn. '
                'It answers: "How much did GDP change?"', 'body'),
              tbl([['Original Variable','After Differencing','Meaning'],
                   ['GDP level (€bn)','ΔGDP','Change in GDP vs previous period'],
                   ['log(GDP)','Δlog(GDP)','Log-return ≈ percentage growth rate'],
                   ['Unemployment (%)','Δunemployment','Change in rate (percentage points)'],
                   ['log(price)','Δlog(price)','Percentage price change (return)']],
                  cw=[5*cm, 4.5*cm, 7.5*cm]),
              p('<b>Why logarithms?</b> A stock rising from €100 to €200 is +100%. Another '
                'rising from €10 to €20 is also +100%. In levels these are incomparable. '
                'Δln(X_t) ≈ percentage change — directly comparable across differently-scaled '
                'quantities.<br/><b>Example:</b> Δln(100 → 102) = ln(1.02) ≈ 2% growth. ✓', 'body'),
              p('<b>Why differences matter:</b> (1) Economic theory talks about changes. '
                '(2) They cure a stochastic trend (unit root). (3) Log-returns are scale-free.', 'body')]

    items += [p('A.4 — The Three Problems with Time-Series Regression', 'h2'),
              p('<b>Problem 1 — Data quality:</b> Time-series is data-hungry. n > 100 ideal; '
                'minimum ~35. Use <b>real (deflated)</b> monetary values — inflation creates '
                'artificial trends that produce spurious regressions.', 'body'),
              p('<b>Problem 2 — Autocorrelation:</b> A3 is routinely violated. Shocks persist '
                'over time. Covered in Chapter TS_B.', 'body'),
              p('<b>Problem 3 — Spurious regression:</b> Regress Belgian ice cream sales on '
                'sunspot activity. Both trend upward over 30 years → R² = 0.95, significant '
                'at p < 0.001 — yet completely meaningless. Solution: ensure stationarity '
                'before fitting. Covered in Chapter TS_C.', 'body'), pb()]

    # ── CHAPTER TS_B ───────────────────────────────────────────────────────
    items += [p('CHAPTER TS_B — Autocorrelation', 'chap'),
              p('<i>Errors that remember the past: detection with the LMSC test.</i>', 'body')]

    items += [p('B.1 — Which Classical Assumption Is Violated?', 'h2'),
              p('Autocorrelation violates <b>A3</b>: cov(ε_t, ε_{t−1}) ≠ 0.', 'body'),
              p('<b>Why A3 fails so commonly:</b> Think of residual ε_t as "everything that '
                'moves Y but isn\'t in my model." Omitted variables in time series tend to '
                'persist over time (business cycles, consumer confidence, institutional inertia). '
                'Today\'s omitted shock carries over into tomorrow.', 'body'),
              p('<b>Intuitive example:</b> You model consumer spending using only income. But '
                'consumer confidence (omitted) also drives spending — and confidence is '
                'persistent. Residuals form waves: positive for months (high confidence), then '
                'negative (low confidence). That is positive autocorrelation.', 'body')]

    items += [p('B.2 — First-Order Autocorrelation', 'h2'),
              p('The AR(1) error structure:', 'h3'),
              p('ε_t = ρ ε_{t−1} + u_t', 'form'),
              p('where ρ (rho) is the autocorrelation coefficient (−1 < ρ < 1) and u_t is '
                '<b>white noise</b> — pure randomness, no memory, mean zero, constant variance. '
                'This equation says: today\'s error = ρ × yesterday\'s error + a fresh shock.', 'body'),
              p('<b>Residual patterns:</b>', 'h3'),
              tbl([['Pattern','What you see','Conclusion'],
                   ['No autocorrelation (ρ = 0)','Random scatter above and below zero — no runs','A3 satisfied ✓'],
                   ['Positive autocorrelation (ρ > 0)','Long runs of same sign: + + + + − − − −  (waves)','A3 violated ✗'],
                   ['Negative autocorrelation (ρ < 0)','Alternating signs: + − + − + −  (zigzag)','A3 violated ✗']],
                  cw=[5.5*cm, 6.5*cm, 5*cm])]

    # FIXED rho table
    items += [p('★ FIXED', 'fixed'),
              p('Understanding the Size of ρ', 'h3'),
              tbl([['Value of ρ','Meaning','Pattern in Residuals'],
                   ['ρ = 0','No autocorrelation. ε_t = u_t, purely random — A3 satisfied.','Random scatter'],
                   ['0 < ρ ≤ 0.3','Mild positive autocorrelation. Small runs. Often tolerable but worth testing.','Slight clustering'],
                   ['0.3 < ρ ≤ 0.6','Moderate positive autocorrelation. Clear wave pattern. LMSC very likely to detect.','Visible waves'],
                   ['0.6 < ρ < 1','Strong positive autocorrelation. Long persistent runs. Model likely misspecified.','Long same-sign runs'],
                   ['ρ < 0','Negative autocorrelation. Alternating signs. Rare; can arise from over-differencing.','Alternating ± ± ±']],
                  cw=[3.5*cm, 8.5*cm, 5*cm]),
              p('<b>Worked analogy for ρ = 0.7:</b> If this quarter\'s residual is +10, next '
                'quarter\'s is expected to be +7 (= 0.7 × 10). Then +4.9, +3.4, +2.4 … slowly '
                'decaying toward zero. A shock takes many periods to fade.', 'body'),
              p('We require <b>−1 < ρ < 1</b> for the error process itself to be stationary '
                'and well-behaved.', 'note')]

    items += [p('B.3 — Consequences of Autocorrelation', 'h2'),
              tbl([['Property','With Autocorrelation (static or DL models)'],
                   ['OLS estimates β̂','Still unbiased — on average they hit the true β'],
                   ['OLS estimates β̂','No longer BEST — a better estimator exists'],
                   ['Standard errors','WRONG — too small when ρ > 0 (over-confident)'],
                   ['t-tests and F-tests','Invalid — built on wrong standard errors'],
                   ['Confidence intervals','Wrong width — too narrow when ρ > 0 (falsely precise)'],
                   ['R²','Unaffected but potentially misleading']],
                  cw=[5*cm, 12*cm]),
              p('<b>Key danger: false significance.</b> Positive autocorrelation inflates '
                't-statistics, making coefficients appear more significant than they really are.', 'body'),
              p('<b>Analogy:</b> Asking 10 people in one household whether they like pizza and '
                'claiming 10 independent data points. They\'re not — family members influence '
                'each other. Effective sample size is much smaller than 10. Autocorrelation '
                'does the same to time-series: consecutive observations are not truly '
                'independent.', 'body'),
              p('<b>Exception — AR(1) models:</b> When Y_{t−1} is a regressor AND '
                'autocorrelation is present, coefficient estimates themselves become '
                '<b>biased</b> — not just inefficient. Much worse. Practical rule: if '
                'autocorrelation is detected in an AR(1) model, switch to DL(q).', 'warn')]

    items += [p('B.4 — Detection: The LMSC Test', 'h2'),
              p('<b>Step 0 — Graphical inspection first.</b> Always plot residuals against '
                'time. Waves → positive AC. Zigzag → negative AC. Random scatter → A3 OK.', 'body'),
              p('<b>Hypotheses:</b> H₀: ρ = 0 (no autocorrelation, A3 satisfied) vs '
                'H₁: ρ ≠ 0 (autocorrelation present, A3 violated)', 'body'),
              p('<b>Step 1:</b> Fit the original model. Save residuals e_t.', 'bull'),
              p('<b>Step 2:</b> Auxiliary regression — regress residuals on all original '
                'predictors PLUS the lagged residual:', 'bull'),
              p('e_t = α₀ + α₁X_{1t} + … + αₖX_{kt} + α_{k+1}e_{t−1} + u_t', 'form'),
              p('<b>Why include the original X\'s?</b> Without them, some of the relationship '
                'between e_t and e_{t−1} might be caused by the X variables themselves '
                '(which also have temporal structure). Including X\'s "controls out" their '
                'influence, leaving only the pure autocorrelation signal.', 'body'),
              p('<b>Step 3:</b> LM = n × R²  where n = n_original − 1', 'bull'),
              p('<b>Step 4:</b> Under H₀, LM ~ χ²(1). Compare to <b>3.841</b> (the 5% '
                'critical value for χ²(1)).', 'bull'),
              p('Decision: LM > 3.841 → Reject H₀ → autocorrelation present.<br/>'
                'LM ≤ 3.841 → Do not reject H₀ → A3 plausibly satisfied.', 'body'),
              p('<b>Worked Example — Phillips Curve (n = 90 quarterly):</b>', 'h3'),
              tbl([['Item','Value'],
                   ['n for auxiliary regression','90 − 1 = 89'],
                   ['R² of auxiliary regression','0.310211'],
                   ['Coefficient on e_{t−1}','0.558  (t = 6.219, p < 0.001)'],
                   ['LM statistic','89 × 0.310211 = 27.609'],
                   ['Critical value (5%)','3.841'],
                   ['Conclusion','27.609 >> 3.841 → Reject H₀. Strong autocorrelation.']],
                  cw=[7*cm, 10*cm]),
              p('<b>Durbin-Watson as a quick alternative:</b>', 'h3'),
              tbl([['DW Value','Interpretation'],
                   ['Close to 2','No autocorrelation'],
                   ['Close to 0','Strong positive autocorrelation (ρ near +1)'],
                   ['Close to 4','Strong negative autocorrelation (ρ near −1)'],
                   ['Between 1.5 and 2.5','Generally acceptable (rough rule)']],
                  cw=[5*cm, 12*cm]),
              p('DW ≈ 2(1 − ρ̂).  <b>Critical limitation:</b> DW is invalid whenever '
                'Y_{t−1} appears as a regressor. Always use LMSC as the primary test.', 'warn')]

    items += [p('B.5 — Solutions for Autocorrelation', 'h2'),
              p('<b>The philosophy:</b> Autocorrelation in a static model usually indicates '
                'model misspecification — the error is carrying memory because dynamics were '
                'left out. Adding lags absorbs the dynamic structure.', 'body'),
              tbl([['Re-specification','What you add','Model type'],
                   ['Add lagged X\'s','X_{t−1}, X_{t−2}, …, X_{t−q}','DL(q) — Distributed Lag'],
                   ['Add lagged Y','Y_{t−1}','AR(1) — Autoregressive']],
                  cw=[5*cm, 6*cm, 6*cm]),
              p('<b>DL(q) vs AR(1):</b> DL is preferred when autocorrelation is present — it '
                'remains unbiased (only inefficient). AR(1) is preferred for parsimony when '
                'A3 is already satisfied. <b>Key principle: bias is worse than '
                'inefficiency.</b>', 'note'), pb()]

    # ── CHAPTER TS_C ───────────────────────────────────────────────────────
    items += [p('CHAPTER TS_C — Stationarity', 'chap'),
              p('<i>Spurious regression, the generalised AR(1), and the Dickey-Fuller '
                'test.</i>', 'body')]

    items += [p('C.1 — Spurious Regression', 'h2'),
              p('<b>The problem:</b> Regress Belgian GDP per capita (1950–2004) on US '
                'population density. Result: R² ≈ 0.96, p < 0.001 — yet no meaningful '
                'economic relationship exists. This is a <b>spurious regression</b>.', 'body'),
              p('<b>Famous example:</b> Nicolas Cage films released per year vs US swimming '
                'pool drownings (1999–2009): R² ≈ 0.67, p < 0.05. Pure coincidence. Both '
                'series happened to move similarly over that period.', 'body'),
              p('<b>Root cause:</b> Both variables are non-stationary — their means drift '
                'over time. Standard regression theory requires stationarity. When it fails, '
                't-statistics don\'t follow t-distributions and R² is meaningless.', 'body'),
              p('Stationarity is therefore a <b>required additional assumption</b> for '
                'time-series regression.', 'note')]

    items += [p('C.2 — Definition of Stationarity', 'h2'),
              p('A time series Y_t is <b>weakly stationary</b> if for every t:', 'body'),
              p('1.  E(Y_t) = μ  —  constant mean<br/>'
                '2.  Var(Y_t) = σ²  —  constant variance<br/>'
                '3.  Cov(Y_t, Y_{t−s}) = γ_s  —  covariance depends only on lag s', 'form'),
              tbl([['Series Type','Visual Pattern','Stationary?'],
                   ['Stationary','Fluctuates around a fixed level, similar spread throughout','YES ✓'],
                   ['Non-stationary (trend)','Drifts steadily upward (or downward) over time','NO ✗'],
                   ['Non-stationary (random walk)','Wanders unpredictably — goes wherever past shocks pushed it','NO ✗']],
                  cw=[5*cm, 8*cm, 4*cm]),
              p('<b>"Cut in half" test:</b> Divide the series into two halves. If both halves '
                'have similar mean, similar spread, and similar patterns → likely stationary. '
                'If the right half is systematically higher, more volatile, or different in '
                'pattern → evidence of non-stationarity.', 'body')]

    items += [p('C.3 — The Generalised AR(1) Model', 'h2'),
              p('Y_t = a + λt + ρY_{t−1} + ε_t', 'form'),
              p('Three parameters determine everything: <b>a</b> (constant), <b>λ</b> '
                '(trend slope), <b>ρ</b> (autoregressive coefficient).<br/>'
                'The critical question: is |ρ| < 1 (stationary family) or ρ = 1 (random '
                'walk)?', 'body'),
              p('The Four Cases', 'h3'),
              tbl([['Case','Model','Properties','Stationary?'],
                   ['Case 1 — Basic AR(1)\n|ρ| < 1, a=0, λ=0',
                    'Y_t = ρY_{t−1} + ε_t',
                    'Mean = 0.  Var = σ²/(1−ρ²).  Shocks decay geometrically.  Series returns to 0.',
                    'YES ✓'],
                   ['Case 2 — AR(1) + constant\n|ρ| < 1, a≠0, λ=0',
                    'Y_t = a + ρY_{t−1} + ε_t',
                    'Long-run mean μ = a/(1−ρ).  Series oscillates around μ.',
                    'YES ✓'],
                   ['Case 3 — Deterministic trend\n|ρ| < 1, a≠0, λ≠0',
                    'Y_t = a + λt + ρY_{t−1} + ε_t',
                    'Mean grows linearly.  Deviations from trend line ARE stationary.  Fix: add t as regressor.',
                    'NO ✗\n(in levels)'],
                   ['Case 4 — Random walk\nρ = 1',
                    'Y_t = a + Y_{t−1} + ε_t',
                    'Each shock is PERMANENT.  Var(Y_t) = tσ² → grows without bound.  Fix: first differences.',
                    'NO ✗']],
                  cw=[4.5*cm, 4.5*cm, 6.5*cm, 2.5*cm])]

    # FIXED Summary Card
    items += [p('★ FIXED', 'fixed'),
              p('Summary Card — The Four Cases at a Glance', 'h3'),
              tbl([['Case','ρ','λ','Stationary?','Fix'],
                   ['Basic AR(1)','|ρ| < 1','0','YES ✓','None needed — use in levels'],
                   ['AR(1) + constant','|ρ| < 1','0','YES ✓','None needed — use in levels'],
                   ['AR(1) + deterministic trend','|ρ| < 1','≠ 0','NO ✗ (in levels)','Add t as regressor in main model'],
                   ['Random walk','ρ = 1','any','NO ✗','Take first differences (ΔY_t)']],
                  cw=[4.5*cm, 1.8*cm, 1.8*cm, 3.2*cm, 5.7*cm])]

    items += [p('C.4 — Deterministic vs. Stochastic Trends', 'h2'),
              p('This distinction is crucial — the two types of non-stationarity require '
                '<b>different fixes</b>. Applying the wrong fix can make things worse.', 'body'),
              tbl([['Feature','Deterministic Trend','Stochastic Trend (Random Walk)'],
                   ['Mathematical source','λt term in the model','ρ = 1'],
                   ['Mean','Changes predictably (grows by λ per period)','May drift, but unpredictably'],
                   ['Variance','Constant','Grows with time'],
                   ['Shocks','Temporary — returns to trend after shock','Permanent — series never recovers'],
                   ['Example','GDP trend growth of 2% per year','S&P 500 stock price'],
                   ['Correct fix','Add t as regressor (or detrend)','First difference'],
                   ['Wrong fix','First-differencing → over-differences → negative AC','Detrending does not remove stochastic trend']],
                  cw=[4.5*cm, 6.5*cm, 6*cm]),
              p('<b>Key intuition — permanence of shocks:</b><br/>'
                'Deterministic: A recession pushes GDP below its trend, but in subsequent '
                'years GDP returns to the same trend. Shock is temporary.<br/>'
                'Random walk: A recession permanently lowers the level. All future values '
                'are shifted down. Shock is permanent and the series has no "memory" of '
                'where it "should" be.', 'body')]

    items += [p('C.5 — Solutions for Non-Stationarity', 'h2'),
              p('<b>Fix A — Deterministic trend (|ρ| < 1, λ ≠ 0):</b> Include t as an '
                'additional regressor:', 'body'),
              p('Y_t = β₀ + β₁X_t + λt + ε_t', 'form'),
              p('The coefficient on t absorbs the linear trend. The coefficient on X_t then '
                'measures the relationship <i>after controlling for the common time trend</i>. '
                'Seasonal: use Δ₁₂X_t = X_t − X_{t−12} to remove annual seasonality.', 'body'),
              p('<b>Fix B — Stochastic trend / unit root (ρ = 1):</b> Take first '
                'differences:', 'body'),
              p('ΔY_t = Y_t − Y_{t−1}  and  ΔX_t = X_t − X_{t−1}', 'form'),
              p('If Y_t = Y_{t−1} + ε_t, then ΔY_t = ε_t — white noise, stationary ✓. '
                'The difference operation strips away accumulated shock history.', 'body'),
              p('<b>Cointegration caveat:</b> If two non-stationary series are genuinely '
                'tied together economically, do NOT difference them. Run the regression in '
                'levels (the "cointegrating regression"). Differencing cointegrated variables '
                'throws away the most economically meaningful information.', 'note')]

    items += [p('C.6 — The Dickey-Fuller Test', 'h2'),
              p('<b>Purpose:</b> Formal unit root test — decides whether ρ = 1 (non-stationary) '
                'or |ρ| < 1 (stationary).', 'body'),
              p('<b>Hypotheses:</b> H₀: ρ = 1 (unit root — NOT stationary)  vs  '
                'H₁: |ρ| < 1 (stationary)', 'body'),
              p('<b>Reparameterisation:</b> Subtract Y_{t−1} from both sides → '
                'α₁ = ρ − 1. H₀: α₁ = 0.  H₁: α₁ < 0 (one-sided test).', 'body'),
              p('ΔY_t = a + λt + α₁Y_{t−1} + ε_t', 'form'),
              p('<b>Why the normal t-table cannot be used:</b> Under H₀, Y_t is a random '
                'walk — non-stationary, variance grows over time. Standard asymptotic theory '
                'breaks down. The DF t-distribution is shifted LEFT compared to the usual '
                't-distribution. Using ±1.96 would almost never reject H₀ even for clearly '
                'stationary series.', 'warn'),
              tbl([['DF Version','Regression','1% CV','5% CV','10% CV','Use when'],
                   ['V1 — no trend','ΔY_t = α₀ + α₁Y_{t−1} + ε_t','−3.43','−2.86','−2.57','No visible trend in time plot'],
                   ['V2 — with trend','ΔY_t = α₀ + λt + α₁Y_{t−1} + ε_t','−3.96','−3.41','−3.13','Clear trend or unsure']],
                  cw=[2.5*cm, 5.5*cm, 1.5*cm, 1.5*cm, 1.5*cm, 5.5*cm]),
              p('<b>Decision rule:</b> Reject H₀ if the t-statistic on Y_{t−1} is MORE '
                'NEGATIVE than the critical value.', 'body'),
              p('<b>Example:</b> t = −3.10.  V1 at 5%: −3.10 < −2.86 → Reject H₀ → '
                'stationary ✓.  V2 at 5%: −3.10 > −3.41 → Fail to reject → unit root ✗.  '
                'The choice of version matters!', 'ok'),
              p('<b>V2 is the safer default:</b> If a trend is present but you use V1, the '
                'test is misspecified. If no trend is present but you use V2, you merely lose '
                'one degree of freedom.', 'body'), pb()]

    # ── CHAPTER TS_D ───────────────────────────────────────────────────────
    items += [p('CHAPTER TS_D — Dynamic Models', 'chap'),
              p('<i>DL(q), AR(1), total multipliers, and the time-series exam workflow.</i>',
                'body')]

    items += [p('D.1 — Distributed Lag Model DL(q)', 'h2'),
              p('A static model assumes the entire effect of X on Y is instantaneous. But most '
                'economic effects are delayed. The DL(q) model captures this:', 'body'),
              p('Y_t = α + β₀X_t + β₁X_{t−1} + β₂X_{t−2} + … + βqX_{t−q} + ε_t', 'form'),
              p('The effect of X is <b>distributed across q+1 periods</b> — hence the name.', 'body'),
              tbl([['Type of Change','Effect at Lag k','Long-Run Total'],
                   ['Temporary (X rises by 1, then returns)',
                    'βₖ is the additional effect k periods later',
                    'Effect ends after lag q'],
                   ['Maintained (X rises by 1 permanently)',
                    'Cumulative: β₀ + β₁ + … + βₖ after k periods',
                    'Total multiplier = Σβₖ']],
                  cw=[6*cm, 6.5*cm, 4.5*cm]),
              p('<b>Total Multiplier = β₀ + β₁ + … + βq</b>', 'form'),
              p('<b>Interpretation:</b> The total multiplier is the long-run effect on Y of a '
                'permanent 1-unit increase in X. It answers: "If X goes up by 1 and stays '
                'there forever, by how much will Y eventually change?"', 'body')]

    items += [p('D.2 — Choosing the Optimal Lag Length q', 'h2'),
              p('<b>The top-down procedure:</b> Start from q_max, progressively drop the '
                'highest lag that is not significant.', 'body'),
              p('1. Fit DL(q_max). Test β_{q_max}.', 'bull'),
              p('2. If not significant: drop lag q_max, refit DL(q_max − 1).', 'bull'),
              p('3. Repeat until the highest remaining lag IS significant.', 'bull'),
              p('4. That is your optimal q.', 'bull'),
              p('<b>Important:</b> Never drop intermediate insignificant lags. If β₂ is '
                'significant but β₁ is not, keep both — you cannot have lag 2 without lag 1.', 'note'),
              p('<b>Worked Example — Safety Training (q_max = 4):</b>', 'h3'),
              tbl([['Step','Model','Result','Action'],
                   ['1','DL(4)','β₄: t = 0.83, p = 0.41','Not significant → drop lag 4'],
                   ['2','DL(3)','β₃: t = 1.21, p = 0.23','Not significant → drop lag 3'],
                   ['3','DL(2)','β₂: t = 1.56, p = 0.12','Not significant → drop lag 2'],
                   ['4','DL(1)','β₁: t = −2.87, p = 0.005','SIGNIFICANT → Stop. Optimal q = 1']],
                  cw=[1.5*cm, 2.5*cm, 6*cm, 7*cm]),
              p('Final model: Ŷ_t = α̂ + β̂₀X_t + β̂₁X_{t−1}  |  '
                'Total multiplier = β̂₀ + β̂₁', 'body')]

    items += [p('D.3 — Autoregressive Model AR(1)', 'h2'),
              p('Y_t = α + βX_t + γY_{t−1} + ε_t', 'form'),
              p('Instead of past X\'s, this model uses <b>past Y</b> to carry the memory of '
                'the system — capturing all persistence in a single coefficient γ.', 'body'),
              tbl([['Coefficient','Interpretation'],
                   ['α','Intercept (baseline)'],
                   ['β','Immediate effect: a 1-unit rise in X_t raises Y_t by β, holding Y_{t−1} fixed'],
                   ['γ','Persistence: how much of last period\'s Y carries forward. Requires |γ| < 1.'],
                   ['β/(1−γ)','Total multiplier: long-run effect of a permanent 1-unit rise in X']],
                  cw=[3*cm, 14*cm])]

    # ENHANCED gamma explanation
    items += [p('★ NEW — ENHANCED', 'new'),
              p('Why |γ| < 1 Is Required — Full Explanation', 'h3'),
              p('This condition appears in three related contexts. Here is what it means in '
                'each:', 'body'),
              p('<b>1. In the pure time-series AR(1) (Chapter C.3):</b><br/>'
                'If |ρ| ≥ 1, each shock to Y is never absorbed — it persists forever or '
                'grows. The variance of Y_t = tσ² (grows without bound). The series wanders '
                'without returning to a fixed level. This is the definition of '
                'non-stationarity.', 'body'),
              p('<b>2. In the AR(1) regression model:</b><br/>'
                'When you write Y_t = α + βX_t + γY_{t−1} + ε_t, the condition |γ| < 1 '
                'plays the same role. Each period, Y partially reverts to its long-run mean. '
                'The formula μ = a/(1−γ) only makes sense when |γ| < 1 — otherwise you '
                'divide by zero or a negative number, producing a nonsensical mean.', 'body'),
              p('<b>3. For the total multiplier β/(1−γ):</b><br/>'
                'This formula comes from summing the geometric series β + βγ + βγ² + βγ³ + … '
                'If |γ| ≥ 1, the terms do not shrink — the sum is infinite. A permanent '
                '1-unit increase in X would have an infinite long-run effect, which is '
                'economically impossible. The condition |γ| < 1 guarantees the sum converges '
                'to the finite value β/(1−γ).', 'body'),
              tbl([['γ̂ value','Implication','Action'],
                   ['|γ̂| < 1','Stationary. Total multiplier = β/(1−γ). Safe to interpret.','✓ Proceed normally'],
                   ['γ̂ = 1','Explosive / unit root in Y. AR(1) inappropriate.','Take first differences instead'],
                   ['|γ̂| > 1','Series would explode over time. Severe misspecification.','Re-specify the model']],
                  cw=[3*cm, 9*cm, 5*cm]),
              p('<b>Practical check:</b> Always verify |γ̂| < 1 after fitting an AR(1). '
                'If γ̂ ≥ 1, something has gone wrong — usually non-stationary input variables '
                'or model misspecification.', 'note'),
              p('<b>Total multiplier proof:</b> In long-run equilibrium Y* = Y_{t−1} = Y_t:<br/>'
                'Y* = α + βX* + γY*  →  Y*(1−γ) = α + βX*  →  '
                'Y* = α/(1−γ) + [β/(1−γ)]X*<br/>'
                'So a permanent 1-unit rise in X* raises Y* by <b>β/(1−γ)</b>.', 'form'),
              p('<b>Worked Example — Education Spending and GDP Growth:</b><br/>'
                'Fitted: Ŷ_t = 1.01 + 0.009X_t + 0.627Y_{t−1}', 'h3'),
              tbl([['Component','Value','Meaning'],
                   ['α̂','1.01','Baseline GDP growth when X = 0 and Y_{t−1} = 0'],
                   ['β̂','0.009','$1 rise in spending per child → +0.009pp GDP growth immediately'],
                   ['γ̂','0.627','62.7% of last year\'s GDP growth persists into this year'],
                   ['Total multiplier','0.009/(1−0.627) = 0.024','Permanent $1/child rise → +0.024pp long-run GDP growth']],
                  cw=[3.5*cm, 4*cm, 9.5*cm])]

    items += [p('D.4 — Link Between AR(1) and DL(∞)', 'h2'),
              p('By repeated substitution into the AR(1) equation, we can show it equals a '
                'DL(∞) with geometrically declining coefficients:', 'body'),
              p('Y_t = α/(1−γ) + βX_t + βγX_{t−1} + βγ²X_{t−2} + βγ³X_{t−3} + …', 'form'),
              p('<b>Total multiplier from geometric series:</b>  '
                'Σ βγᵏ = β × 1/(1−γ) = β/(1−γ)   (requires |γ| < 1)', 'form'),
              tbl([['Feature','DL(q)','AR(1)'],
                   ['Parameters needed','q+1','2'],
                   ['Multicollinearity','High for large q','Low (only one lag of Y)'],
                   ['Bias when A3 violated','None — only inefficient','Biased ✗'],
                   ['Lag flexibility','Completely free','Constrained to geometric decay'],
                   ['When to prefer','Autocorrelation suspected','A3 satisfied, parsimony needed']],
                  cw=[5*cm, 6.5*cm, 5.5*cm])]

    items += [p('D.5 — The Three-Step Exam Workflow', 'h2'),
              p('<b>Step 1 — Stationarity Check (TS_C):</b> For each variable:', 'h3'),
              p('1. Plot series against time. Does it trend? Does variance change?', 'bull'),
              p('2. Choose DF version: no trend visible → V1. Clear trend or unsure → V2.', 'bull'),
              p('3. Run DF regression, read t-stat on Y_{t−1}.', 'bull'),
              p('4. Compare to adapted critical values (−2.86 V1, −3.41 V2 at 5%). NOT ±1.96.', 'bull'),
              p('5. Reject H₀ → stationary → use in levels.', 'bull'),
              p('6. Fail to reject → unit root → take ΔY_t, re-run DF on differences.', 'bull'),
              p('<b>Step 2 — Fit the Model (TS_D):</b>', 'h3'),
              p('For DL(q): start at q_max, drop highest non-significant lag until highest '
                'is significant. Report all coefficients. Total multiplier = Σβₖ.', 'body'),
              p('For AR(1): fit directly. Report β, γ, and total multiplier = β/(1−γ). '
                'Verify |γ̂| < 1.', 'body'),
              p('<b>Step 3 — LMSC Assumption Check (TS_B):</b>', 'h3'),
              p('1. State H₀: ρ = 0 and H₁: ρ ≠ 0.', 'bull'),
              p('2. Write auxiliary regression (all X\'s + lagged residual e_{t−1}).', 'bull'),
              p('3. Compute LM = n_aux × R²_aux.', 'bull'),
              p('4. Compare to χ²(1) = 3.841.', 'bull'),
              p('5. Write a full conclusion sentence.', 'bull'),
              p('<b>Worked Example — Consumption and Income (n = 162 quarterly):</b>', 'h3'),
              p('Both ln(Y) and ln(X) show clear upward trends.', 'body'),
              tbl([['Variable','DF Version','t-statistic','Critical (5%)','Conclusion'],
                   ['ln(Y) — level','V2 (trend)','−1.82','−3.41','Fail to reject → unit root'],
                   ['ln(X) — level','V2 (trend)','−1.65','−3.41','Fail to reject → unit root'],
                   ['Δln(Y) — diff','V1 (no trend)','−9.95','−2.86','Reject → stationary ✓'],
                   ['Δln(X) — diff','V1 (no trend)','−12.72','−2.86','Reject → stationary ✓']],
                  cw=[3.5*cm, 3*cm, 2.5*cm, 3*cm, 5*cm]),
              p('Top-down DL(q), q_max = 3:', 'body'),
              tbl([['Model','Highest Lag t-stat','Significant?','Action'],
                   ['DL(3)','β₃: t = 0.91','No','Drop lag 3'],
                   ['DL(2)','β₂: t = 1.38','No','Drop lag 2'],
                   ['DL(1)','β₁: t = 2.74','YES','Stop. Optimal q = 1']],
                  cw=[3*cm, 4.5*cm, 3*cm, 6.5*cm]),
              p('Fitted: ΔŶ_t = 0.004 + 0.350ΔX_t + 0.182ΔX_{t−1}  |  '
                'Total multiplier = 0.532', 'body'),
              p('LMSC: n_aux = 161, R² = 0.002618, LM = 0.4215 < 3.841 → '
                'Fail to reject H₀. A3 plausibly satisfied. ✓', 'ok'), pb()]

    # ── FORMULA SHEET ──────────────────────────────────────────────────────
    items += [p('FORMULA SHEET — The Five Equations You Must Know', 'part')]

    for label, formula_txt in [
        ('1.  DL(q) Model',
         'Y_t = α + β₀X_t + β₁X_{t−1} + … + βqX_{t−q} + ε_t\n'
         'Total multiplier = β₀ + β₁ + … + βq  =  Σβₖ'),
        ('2.  AR(1) Model',
         'Y_t = α + βX_t + γY_{t−1} + ε_t\n'
         'Total multiplier = β/(1−γ)   [requires |γ| < 1]'),
        ('3.  LMSC Test',
         'Auxiliary: e_t = α₀ + α₁X_{1t} + … + αₖX_{kt} + α_{k+1}e_{t−1} + u_t\n'
         'LM = n × R²  ~  χ²(1)  under H₀\n'
         'H₀: ρ = 0  |  H₁: ρ ≠ 0  |  Critical value at 5%: 3.841'),
        ('4.  Dickey-Fuller Test',
         'V1 (no trend): ΔY_t = α₀ + α₁Y_{t−1} + ε_t\n'
         'V2 (with trend): ΔY_t = α₀ + λt + α₁Y_{t−1} + ε_t\n'
         'H₀: α₁ = 0 (unit root)  |  H₁: α₁ < 0 (stationary)\n'
         'Critical values at 5%:  V1 = −2.86   V2 = −3.41'),
        ('5.  Confidence Interval  ★ NEW',
         '95% CI  =  β̂  ±  1.96 × SE(β̂)\n'
         '99% CI  =  β̂  ±  2.576 × SE(β̂)\n'
         'CI excludes zero  ↔  |t| > 1.96  ↔  p < 0.05  (all equivalent at 5%)')]:
        items += [p(label, 'h3'), p(formula_txt, 'form'), sp(4)]

    items.append(pb())

    # ── EXAM-DAY CHECKLIST ─────────────────────────────────────────────────
    items += [p('EXAM-DAY CHECKLIST', 'part'),
              p('Step 1 — Stationarity (TS_C)', 'h2'),
              p('☐  Plot every variable against time', 'bull'),
              p('☐  Choose DF version (V1: no trend  /  V2: trend or unsure)', 'bull'),
              p('☐  Run DF on each variable, read t-stat on Y_{t−1}', 'bull'),
              p('☐  Compare to adapted critical values — NOT ±1.96 or ±2.58', 'bull'),
              p('☐  Unit root present? → take ΔY_t, re-test on differences', 'bull'),
              p('Step 2 — Fit the Model (TS_D)', 'h2'),
              p('☐  Model type given in question (static / DL(q) / AR(1))', 'bull'),
              p('☐  For DL: start at q_max, drop top lag while not significant', 'bull'),
              p('☐  Report all coefficients with SEs and t-stats', 'bull'),
              p('☐  Calculate total multiplier (Σβₖ  or  β/(1−γ))', 'bull'),
              p('☐  Verify |γ̂| < 1 for AR(1) models', 'bull'),
              p('☐  Interpret: temporary vs. maintained change; levels vs. log-returns', 'bull'),
              p('Step 3 — Assumption Check (TS_B)', 'h2'),
              p('☐  State H₀ and H₁ explicitly', 'bull'),
              p('☐  Write the auxiliary regression (all original X\'s + lagged residual)', 'bull'),
              p('☐  Compute LM = n_aux × R²_aux', 'bull'),
              p('☐  Compare to χ²(1) = 3.841 (or use p-value)', 'bull'),
              p('☐  Write a full conclusion sentence', 'bull'),
              p('Extra — Confidence Intervals  ★ NEW', 'h2'),
              p('☐  CI = β̂ ± 1.96 × SE', 'bull'),
              p('☐  Check whether CI excludes zero (= significant at 5%)', 'bull'),
              p('☐  Interpret in context: "We are 95% confident that …"', 'bull'), pb()]

    # ── COMMON EXAM PITFALLS ───────────────────────────────────────────────
    items += [p('COMMON EXAM PITFALLS', 'part')]
    pitfalls = [
        ('1. "Reject H₀ means non-stationary" — WRONG',
         'For the Dickey-Fuller test: Reject H₀ means the series IS stationary (H₀ is the '
         'unit root). For the LMSC test: Reject H₀ means autocorrelation IS present (H₀ is '
         'no autocorrelation). These are opposite! Know which test you are running.'),
        ('2. "Take differences whenever the series trends" — BE CAREFUL',
         'Only difference if the DF test confirms a stochastic trend (unit root, ρ = 1). '
         'If the trend is deterministic (|ρ| < 1, λ ≠ 0), add t as a regressor instead. '
         'Over-differencing creates artificial negative autocorrelation and loses information.'),
        ('3. "Use Durbin-Watson for all models" — WRONG',
         'DW is invalid whenever Y_{t−1} appears as a regressor (AR(1) models). '
         'Always use LMSC — it works for static, DL(q), and AR(1) models.'),
        ('4. "Total multiplier = β₀ only" — WRONG',
         'For DL(q): total multiplier = β₀ + β₁ + … + βq (sum of ALL lag coefficients). '
         'For AR(1): total multiplier = β/(1−γ), not just β. '
         'β₀ alone is the immediate effect only.'),
        ('5. "Unit changes when X is log-differenced" — WRONG',
         'If you differenced log(X), a 1-unit rise in Δln(X) means a 1 percentage point '
         'rise in the growth rate — not a 1-unit rise in the level. '
         'Always interpret in terms of percentage changes.'),
        ('6. "Skip the autocorrelation test to save time" — WRONG',
         'The LMSC test is worth dedicated exam marks. Always report all five elements: '
         'H₀/H₁, the auxiliary regression equation, LM = n × R², comparison to 3.841, '
         'and a conclusion sentence.'),
        ('7. "Use the regular t-table for the Dickey-Fuller t-statistic" — WRONG',
         'The DF t-statistic does NOT follow a t-distribution under H₀. Standard critical '
         'values (±1.96, ±2.58) do not apply. Always use adapted DF critical values: '
         '−2.86 (V1, 5%), −3.41 (V2, 5%).'),
        ('8. "Confidence interval includes zero = we accept H₀" — WRONG  ★ NEW',
         'We never accept H₀. If the CI includes zero, we fail to reject H₀ — meaning '
         'the data are insufficient to confirm an effect, not that there is definitely no '
         'effect. If the CI excludes zero, we reject H₀ and conclude a significant effect.'),
    ]
    for title, explanation in pitfalls:
        items += [p(f'<b>{title}</b>', 'warn'),
                  p(explanation, 'body'), sp(4)]

    items.append(pb())

    # ── PRACTICE QUESTIONS ─────────────────────────────────────────────────
    items += [p('PART 2 — PRACTICE EXAM QUESTIONS  ★ NEW', 'part'),
              p('Six fully worked exam-style questions. Attempt each question before reading '
                'the solution. Cover the answer and work through it independently — this is '
                'essential for building exam confidence.', 'body'), sp(8)]

    # Q1
    items += [p('Question 1 — Hypothesis Testing and Confidence Intervals', 'chap'),
              p('A researcher regresses monthly restaurant sales (€000s) on advertising spend '
                '(€000s) using n = 48 monthly observations. Regression output:', 'body'),
              tbl([['Coefficient','Estimate','Standard Error'],
                   ['Intercept (α̂)','42.3','8.1'],
                   ['β̂ (advertising)','6.8','2.1'],
                   ['R²','0.41','—']],
                  cw=[7*cm, 4*cm, 6*cm]),
              p('<b>(a)</b> Calculate the t-statistic for the advertising coefficient.<br/>'
                '<b>(b)</b> Is advertising statistically significant at 5%? At 1%? Justify.<br/>'
                '<b>(c)</b> Construct a 95% confidence interval for β(advertising).<br/>'
                '<b>(d)</b> Interpret the confidence interval in plain English.<br/>'
                '<b>(e)</b> What does R² = 0.41 tell us?', 'qbox'),
              p('<b>SOLUTION</b>', 'h3'),
              p('<b>(a)</b>  t = β̂ / SE = 6.8 / 2.1 = <b>3.24</b>', 'ans'),
              p('<b>(b)</b>  At 5%: |t| = 3.24 > 1.96 → significant ✓<br/>'
                'At 1%: |t| = 3.24 > 2.576 → also significant at 1% ✓', 'ans'),
              p('<b>(c)</b>  95% CI = 6.8 ± 1.96 × 2.1 = 6.8 ± 4.12 = <b>[2.68, 10.92]</b>', 'ans'),
              p('<b>(d)</b>  We are 95% confident that each additional €1,000 of advertising '
                'spend raises monthly sales by between <b>€2,680 and €10,920</b> on average. '
                'Since the entire CI is above zero, the effect is statistically significant.', 'ans'),
              p('<b>(e)</b>  Advertising spend explains <b>41%</b> of the variation in monthly '
                'sales. The remaining 59% is explained by other factors not in this model.', 'ans'), sp(10)]

    # Q2
    items += [p('Question 2 — Dickey-Fuller Test', 'chap'),
              p('You have quarterly Belgian unemployment data (n = 160). The series shows a '
                'clear upward trend. You run the Dickey-Fuller Version 2 regression and obtain: '
                'α₁ = −0.063, SE(α₁) = 0.028. You then test the first-differenced series: '
                't-statistic on ΔU_{t−1} = −11.42.', 'body'),
              p('<b>(a)</b> State H₀ and H₁ for the Dickey-Fuller test.<br/>'
                '<b>(b)</b> Calculate the t-statistic for α₁ in the level regression.<br/>'
                '<b>(c)</b> Why is Version 2 appropriate here?<br/>'
                '<b>(d)</b> Can you reject H₀ at 5%? At 1%?<br/>'
                '<b>(e)</b> What transformation should be applied? Why?<br/>'
                '<b>(f)</b> Is the transformed series stationary?', 'qbox'),
              p('<b>SOLUTION</b>', 'h3'),
              p('<b>(a)</b>  H₀: α₁ = 0 (unit root — NOT stationary)<br/>'
                'H₁: α₁ < 0 (stationary)', 'ans'),
              p('<b>(b)</b>  t = −0.063 / 0.028 = <b>−2.25</b>', 'ans'),
              p('<b>(c)</b>  The series shows a clear upward trend in the time plot. Version 2 '
                'includes t as a regressor, controlling for the deterministic trend component. '
                'Using Version 1 when a trend is present would misspecify the test.', 'ans'),
              p('<b>(d)</b>  At 5%: critical value = −3.41. t = −2.25 > −3.41 → '
                '<b>Fail to reject H₀</b>. Not significant at 5%.<br/>'
                'At 1%: critical value = −3.96. Also fail to reject.', 'ans'),
              p('<b>(e)</b>  Unemployment has a stochastic trend (unit root). Apply <b>first '
                'differences</b>: ΔU_t = U_t − U_{t−1}. This converts levels into changes in '
                'the unemployment rate (percentage points), which is stationary.', 'ans'),
              p('<b>(f)</b>  DF on ΔU_t: t = −11.42. Using Version 1 (differences show no '
                'trend): critical value = −2.86. Since −11.42 < −2.86 → <b>Reject H₀ → '
                'ΔU_t is stationary ✓</b>. Use first differences in the model.', 'ans'), sp(10)]

    # Q3
    items += [p('Question 3 — LMSC Autocorrelation Test', 'chap'),
              p('A researcher fits a DL(2) model on n = 80 monthly observations. To test for '
                'autocorrelation, they run an auxiliary regression and obtain R² = 0.143.', 'body'),
              p('<b>(a)</b> Write out the auxiliary regression equation for the LMSC test.<br/>'
                '<b>(b)</b> What is the sample size of the auxiliary regression? Why?<br/>'
                '<b>(c)</b> Compute the LM test statistic.<br/>'
                '<b>(d)</b> State H₀ and H₁.<br/>'
                '<b>(e)</b> What is the critical value at 5%?<br/>'
                '<b>(f)</b> State your conclusion. What should the researcher do next?', 'qbox'),
              p('<b>SOLUTION</b>', 'h3'),
              p('<b>(a)</b>  e_t = α₀ + α₁X_t + α₂X_{t−1} + α₃X_{t−2} + α₄e_{t−1} + u_t', 'ans'),
              p('<b>(b)</b>  n_aux = 80 − 1 = <b>79</b>. We lose one observation because '
                'e_{t−1} is undefined for the first residual (no "period zero" residual).', 'ans'),
              p('<b>(c)</b>  LM = n_aux × R² = 79 × 0.143 = <b>11.30</b>', 'ans'),
              p('<b>(d)</b>  H₀: ρ = 0 (no autocorrelation — A3 satisfied)<br/>'
                'H₁: ρ ≠ 0 (autocorrelation present — A3 violated)', 'ans'),
              p('<b>(e)</b>  χ²(1, 5%) = <b>3.841</b>. Under H₀, LM ~ χ²(1).', 'ans'),
              p('<b>(f)</b>  LM = 11.30 > 3.841 → <b>Reject H₀ at 5%</b>. Autocorrelation '
                'is significantly present; A3 is violated. The researcher should re-specify '
                'the model by adding more lagged X\'s (extend to higher DL order). DL is '
                'preferred over AR(1) when autocorrelation is detected, as AR(1) would '
                'produce biased estimates.', 'ans'), sp(10)]

    # Q4
    items += [p('Question 4 — DL(q) Lag Selection and Total Multiplier', 'chap'),
              p('A researcher models monthly workplace accidents (Y) as a function of safety '
                'training hours (X), with q_max = 3. Top-down results:', 'body'),
              tbl([['Model','Coefficient','t-statistic','p-value'],
                   ['DL(3)','β₃','0.71','0.48'],
                   ['DL(2)','β₂','1.44','0.15'],
                   ['DL(1)','β₁','−3.12','0.003']],
                  cw=[4*cm, 4*cm, 4*cm, 5*cm]),
              p('The final model gives: Ŷ_t = 52.3 − 1.8X_t − 1.2X_{t−1}', 'body'),
              p('<b>(a)</b> What is the optimal lag length q? Explain the top-down procedure.<br/>'
                '<b>(b)</b> Write out the final chosen model equation.<br/>'
                '<b>(c)</b> Interpret β̂₀ = −1.8 and β̂₁ = −1.2.<br/>'
                '<b>(d)</b> Calculate and interpret the total multiplier.<br/>'
                '<b>(e)</b> The company permanently increases training by 2 hours/month. What '
                'is the predicted long-run change in monthly accidents?', 'qbox'),
              p('<b>SOLUTION</b>', 'h3'),
              p('<b>(a)</b>  Optimal q = <b>1</b>. Top-down: Start at DL(3). β₃: t = 0.71, '
                'not significant → drop lag 3. Refit DL(2). β₂: t = 1.44, not significant → '
                'drop lag 2. Refit DL(1). β₁: t = −3.12, significant (|t| > 2) → STOP.', 'ans'),
              p('<b>(b)</b>  Ŷ_t = 52.3 − 1.8X_t − 1.2X_{t−1}', 'ans'),
              p('<b>(c)</b>  β̂₀ = −1.8: One additional training hour this month is associated '
                'with <b>1.8 fewer accidents this month</b>, holding last month\'s training '
                'constant.<br/>'
                'β̂₁ = −1.2: One additional training hour last month is associated with '
                '<b>1.2 fewer accidents this month</b>, holding this month\'s training '
                'constant.', 'ans'),
              p('<b>(d)</b>  Total multiplier = −1.8 + (−1.2) = <b>−3.0</b>. A permanent '
                '1-hour/month increase in training is associated with <b>3.0 fewer accidents '
                'per month</b> in the long run.', 'ans'),
              p('<b>(e)</b>  ΔX = +2 permanently. Long-run change = 2 × (−3.0) = '
                '<b>−6 accidents/month</b> predicted reduction.', 'ans'), sp(10)]

    # Q5
    items += [p('Question 5 — AR(1) Model Full Interpretation', 'chap'),
              p('A researcher models quarterly consumer spending (€bn) as a function of '
                'disposable income (€bn):', 'body'),
              p('Ŷ_t = 12.4 + 0.31X_t + 0.74Y_{t−1}', 'form'),
              p('<b>(a)</b> Interpret each coefficient (α̂, β̂, γ̂).<br/>'
                '<b>(b)</b> Is the stationarity condition satisfied? Why does this matter?<br/>'
                '<b>(c)</b> Calculate the total multiplier.<br/>'
                '<b>(d)</b> Income permanently increases by €5bn. What is the predicted '
                'long-run change in spending?<br/>'
                '<b>(e)</b> Instead, income temporarily rises by €5bn only in quarter t. '
                'Trace the additional effect for periods t, t+1, t+2, t+3.<br/>'
                '<b>(f)</b> The LMSC test gives LM = 8.4. What is your conclusion?', 'qbox'),
              p('<b>SOLUTION</b>', 'h3'),
              p('<b>(a)</b>  α̂ = 12.4: baseline spending level.<br/>'
                'β̂ = 0.31: A €1bn rise in income this quarter raises spending by '
                '<b>€0.31bn immediately</b>, holding last quarter\'s spending fixed.<br/>'
                'γ̂ = 0.74: <b>74% of last quarter\'s spending level persists</b> into this '
                'quarter — capturing habits, contracts, and inertia.', 'ans'),
              p('<b>(b)</b>  |γ̂| = 0.74 < 1 → stationarity condition <b>satisfied ✓</b>.<br/>'
                'This matters because: (1) the long-run mean is finite; (2) the total '
                'multiplier formula converges; (3) the model is economically interpretable. '
                'If γ̂ ≥ 1, the model implies explosive, ever-growing spending — impossible.', 'ans'),
              p('<b>(c)</b>  Total multiplier = 0.31 / (1 − 0.74) = 0.31 / 0.26 = <b>1.19</b>', 'ans'),
              p('<b>(d)</b>  Long-run ΔY = 5 × 1.19 = <b>€5.96bn</b> increase in spending.', 'ans'),
              p('<b>(e)</b>  Temporary shock ΔX = +5 in period t only:', 'ans'),
              tbl([['Period','Additional Effect on Y'],
                   ['t','5 × 0.31 = +1.55'],
                   ['t+1','0.74 × 1.55 = +1.15'],
                   ['t+2','0.74² × 1.55 = +0.85'],
                   ['t+3','0.74³ × 1.55 = +0.63'],
                   ['t+k','0.74ᵏ × 1.55 → 0  (geometric decay)']],
                  cw=[4*cm, 13*cm]),
              p('<b>(f)</b>  LM = 8.4 > 3.841 → <b>Reject H₀</b>. Autocorrelation '
                'significantly present, A3 violated. This is serious for AR(1): when '
                'autocorrelation is present, coefficient estimates become <b>biased</b>. '
                'The researcher should switch to a <b>DL(q) model</b>, which remains '
                'unbiased even with autocorrelation.', 'ans'), sp(10)]

    # Q6
    items += [p('Question 6 — Full Three-Step Workflow', 'chap'),
              p('A researcher studies Belgian real GDP growth (Y) and real government '
                'investment (X) using quarterly data (n = 104). Both series are in log form '
                'and show upward trends.', 'body'),
              p('<b>Step 1 — DF results:</b>', 'h3'),
              tbl([['Variable','DF Version','t-statistic'],
                   ['ln(Y) — level','V2','−2.01'],
                   ['Δln(Y) — diff','V1','−8.73'],
                   ['ln(X) — level','V2','−1.78'],
                   ['Δln(X) — diff','V1','−9.12']],
                  cw=[5*cm, 3.5*cm, 4.5*cm]),
              p('<b>Step 2 — Model fitting (q_max = 2):</b><br/>'
                'DL(2): β₂ t = 0.88 (p = 0.38)  →  DL(1): β₁ t = 2.51 (p = 0.014)<br/>'
                'Final: ΔŶ_t = 0.003 + 0.28Δln(X_t) + 0.19Δln(X_{t−1})', 'body'),
              p('<b>Step 3 — LMSC:</b>  Auxiliary R² = 0.018, n_aux = 101', 'body'),
              p('<b>(a)</b> Are ln(Y) and ln(X) stationary in levels? Show full reasoning.<br/>'
                '<b>(b)</b> Are the differenced series stationary?<br/>'
                '<b>(c)</b> Why is Version 1 used for the differenced series?<br/>'
                '<b>(d)</b> Why does top-down give optimal q = 1?<br/>'
                '<b>(e)</b> Interpret β̂₀ = 0.28 and β̂₁ = 0.19 in economic terms.<br/>'
                '<b>(f)</b> Calculate and interpret the total multiplier.<br/>'
                '<b>(g)</b> Conduct the full LMSC test. Is A3 satisfied?', 'qbox'),
              p('<b>SOLUTION</b>', 'h3'),
              p('<b>(a)</b>  ln(Y): t = −2.01 > −3.41 (V2, 5%) → <b>Fail to reject H₀ → '
                'unit root → NOT stationary</b>.<br/>'
                'ln(X): t = −1.78 > −3.41 → <b>Fail to reject → unit root → NOT '
                'stationary</b>.', 'ans'),
              p('<b>(b)</b>  Δln(Y): t = −8.73 < −2.86 (V1, 5%) → <b>Reject H₀ → '
                'stationary ✓</b>.<br/>'
                'Δln(X): t = −9.12 < −2.86 → <b>Reject H₀ → stationary ✓</b>.', 'ans'),
              p('<b>(c)</b>  After differencing, the trend is removed. Growth rates (Δln) '
                'fluctuate around a roughly constant mean with no visible trend. Using V2 '
                'unnecessarily would cost a degree of freedom.', 'ans'),
              p('<b>(d)</b>  DL(2): β₂ t = 0.88, not significant → drop lag 2. DL(1): '
                'β₁ t = 2.51, significant → stop. Optimal q = 1.', 'ans'),
              p('<b>(e)</b>  β̂₀ = 0.28: A 1pp rise in investment growth this quarter → '
                '<b>+0.28pp GDP growth this quarter</b>, holding last quarter\'s investment '
                'growth constant.<br/>'
                'β̂₁ = 0.19: A 1pp rise in investment growth last quarter → <b>+0.19pp '
                'GDP growth this quarter</b>, holding this quarter\'s constant.', 'ans'),
              p('<b>(f)</b>  Total multiplier = 0.28 + 0.19 = <b>0.47</b>. A permanent '
                '1pp increase in government investment growth is associated with a '
                '<b>0.47pp increase in long-run GDP growth</b>.', 'ans'),
              p('<b>(g)</b>  LMSC test:<br/>'
                'H₀: ρ = 0 (no autocorrelation)  vs  H₁: ρ ≠ 0 (autocorrelation present)<br/>'
                'Auxiliary regression: e_t = α₀ + α₁Δln(X_t) + α₂Δln(X_{t−1}) + '
                'α₃e_{t−1} + u_t<br/>'
                'LM = 101 × 0.018 = <b>1.818</b><br/>'
                '1.818 < 3.841 → <b>Fail to reject H₀</b>.<br/>'
                'Conclusion: No significant autocorrelation detected at 5%. A3 is plausibly '
                'satisfied. The DL(1) model on first-differenced log variables is well-'
                'specified. ✓', 'ans'), sp(10), pb()]

    # ── ONE-PAGE SUMMARY ───────────────────────────────────────────────────
    items += [p('ONE-PAGE SUMMARY', 'part'),
              tbl([['Stage','Key Actions'],
                   ['FOUNDATIONS',
                    'Regression: Y = α + βX + ε.  OLS finds β̂.  R² measures fit (0–1).\n'
                    't = β̂/SE tests if β ≠ 0.  p < 0.05 → significant.\n'
                    'CI: β̂ ± 1.96 × SE.  CI excludes zero ↔ significant at 5%.\n'
                    'Five classical assumptions must hold.'],
                   ['RECOGNISE',
                    'Time series: order matters.  Define lags X_{t−k} and differences ΔX_t.\n'
                    'n > 100 ideal (min ~35).  Use real (deflated) monetary values.'],
                   ['STABILISE',
                    'Time plot + Dickey-Fuller test on every variable.\n'
                    'Deterministic trend (λ≠0, |ρ|<1)? → Add t as regressor.\n'
                    'Stochastic trend / unit root (|ρ|=1)? → Take first differences.\n'
                    'DF uses special critical values: −2.86 (V1) or −3.41 (V2).  NOT ±1.96.'],
                   ['MODEL',
                    'DL(q): top-down selection.  Total multiplier = Σβₖ.\n'
                    'AR(1): total multiplier = β/(1−γ).  REQUIRES |γ| < 1.\n'
                    'Interpret: temporary vs. maintained change; levels vs. log-returns.'],
                   ['DIAGNOSE',
                    'LMSC: auxiliary regression + lagged residual.  LM = n·R² ~ χ²(1).\n'
                    'Reject H₀ → autocorrelation → re-specify (prefer DL over AR).\n'
                    'DW: quick check only — not valid for AR models.']],
                  cw=[3.5*cm, 13.5*cm])]

    return items

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════
def main():
    path = '/home/user/BabyPluto/TimeSeries_CompleteGuide_Updated.pdf'
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    doc.build(build(), onFirstPage=on_page, onLaterPages=on_page)
    print(f'PDF created: {path}')

if __name__ == '__main__':
    main()
