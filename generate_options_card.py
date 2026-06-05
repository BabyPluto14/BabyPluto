"""
Generate an improved Options Reference Card PDF with proper matplotlib charts
and additional missing content.
"""

import io
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, Image, KeepTogether, PageBreak
)
from reportlab.platypus.flowables import Flowable

# ── Colour palette ──────────────────────────────────────────────────────────
DARK_BLUE   = colors.HexColor('#1B3A6B')
MID_BLUE    = colors.HexColor('#2E5FA3')
LIGHT_BLUE  = colors.HexColor('#D6E4F7')
ACCENT_RED  = colors.HexColor('#C0392B')
ACCENT_GRN  = colors.HexColor('#1A7A4A')
GOLD        = colors.HexColor('#E8A020')
PALE_GREY   = colors.HexColor('#F4F6F8')
MID_GREY    = colors.HexColor('#BDC3C7')
TEXT_DARK   = colors.HexColor('#1C1C1C')
BOX_BORDER  = colors.HexColor('#2E5FA3')

# ── Matplotlib colours ───────────────────────────────────────────────────────
MPL_BLUE  = '#2E5FA3'
MPL_RED   = '#C0392B'
MPL_GREEN = '#1A7A4A'
MPL_GREY  = '#7F8C8D'
MPL_GOLD  = '#E8A020'

PAGE_W, PAGE_H = A4
MARGIN = 1.8 * cm

# ── Styles ───────────────────────────────────────────────────────────────────
def make_styles():
    base = getSampleStyleSheet()
    def s(name, parent='Normal', **kw):
        return ParagraphStyle(name, parent=base[parent], **kw)

    title   = s('MyTitle',  fontSize=22, textColor=DARK_BLUE,
                fontName='Helvetica-Bold', spaceAfter=4, leading=26)
    h1      = s('MyH1',     fontSize=14, textColor=DARK_BLUE,
                fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=4,
                leading=18)
    h2      = s('MyH2',     fontSize=11, textColor=MID_BLUE,
                fontName='Helvetica-Bold', spaceBefore=8, spaceAfter=2,
                leading=14)
    body    = s('MyBody',   fontSize=9.5, textColor=TEXT_DARK,
                leading=14, spaceAfter=4, alignment=TA_JUSTIFY)
    body_c  = s('MyBodyC',  fontSize=9.5, textColor=TEXT_DARK,
                leading=14, spaceAfter=4, alignment=TA_CENTER)
    small   = s('MySmall',  fontSize=8.5, textColor=TEXT_DARK,
                leading=12, spaceAfter=2)
    code    = s('MyCode',   fontSize=8.5, fontName='Courier',
                textColor=colors.HexColor('#2C3E50'),
                backColor=colors.HexColor('#EEF2F7'),
                leading=13, spaceAfter=2,
                leftIndent=8, rightIndent=8)
    label_b = s('LabelBold', fontSize=9, fontName='Helvetica-Bold',
                textColor=DARK_BLUE)
    tip     = s('Tip', fontSize=9, textColor=colors.HexColor('#5D4037'),
                fontName='Helvetica-Oblique', leading=13,
                leftIndent=6, rightIndent=6)
    return dict(title=title, h1=h1, h2=h2, body=body, body_c=body_c,
                small=small, code=code, label_b=label_b, tip=tip)

ST = make_styles()

# ── Helper flowables ─────────────────────────────────────────────────────────
def rule(color=MID_BLUE, thickness=1):
    return HRFlowable(width='100%', thickness=thickness, color=color,
                      spaceAfter=6, spaceBefore=2)

def spacer(h=0.3):
    return Spacer(1, h * cm)

def box_para(text, bg=LIGHT_BLUE, border=BOX_BORDER, style=None, pad=8):
    """Paragraph inside a single-cell coloured table."""
    st = style or ST['body']
    tbl = Table([[Paragraph(text, st)]],
                colWidths=[PAGE_W - 2 * MARGIN])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('BOX',        (0,0), (-1,-1), 0.8, border),
        ('TOPPADDING',    (0,0), (-1,-1), pad),
        ('BOTTOMPADDING', (0,0), (-1,-1), pad),
        ('LEFTPADDING',   (0,0), (-1,-1), 12),
        ('RIGHTPADDING',  (0,0), (-1,-1), 12),
    ]))
    return tbl

# ── Chart helpers ─────────────────────────────────────────────────────────────
def fig_to_image(fig, width_cm=15):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight',
                facecolor='white')
    plt.close(fig)
    buf.seek(0)
    img = Image(buf, width=width_cm * cm, height=width_cm * cm * 0.55)
    return img

def _base_ax(ax, title=''):
    ax.set_facecolor('#FAFBFC')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#AAAAAA')
    ax.spines['bottom'].set_color('#AAAAAA')
    ax.tick_params(labelsize=8, color='#888888')
    ax.yaxis.set_tick_params(labelcolor='#555555')
    ax.xaxis.set_tick_params(labelcolor='#555555')
    ax.set_xlabel('Stock Price at Maturity (S)', fontsize=9, color='#444444')
    ax.set_ylabel('Profit / Loss', fontsize=9, color='#444444')
    if title:
        ax.set_title(title, fontsize=10, fontweight='bold',
                     color='#1B3A6B', pad=8)
    ax.axhline(0, color='#888888', linewidth=0.8, linestyle='--')

def make_long_call_chart():
    K, P = 100, 8
    S = np.linspace(60, 160, 400)
    profit = np.where(S > K, S - K - P, -P)

    fig, ax = plt.subplots(figsize=(7, 3.8))
    _base_ax(ax, 'Position 1 — Long Call')

    ax.fill_between(S, profit, 0,
                    where=(profit > 0), alpha=0.15, color=MPL_GREEN)
    ax.fill_between(S, profit, 0,
                    where=(profit < 0), alpha=0.15, color=MPL_RED)
    ax.plot(S, profit, color=MPL_BLUE, linewidth=2.2)

    ax.axvline(K, color=MPL_GREY, linewidth=1, linestyle=':')
    ax.axvline(K + P, color=MPL_GREEN, linewidth=1, linestyle='--', alpha=0.8)

    ax.annotate('Strike K', xy=(K, ax.get_ylim()[0]), xytext=(K - 18, -22),
                textcoords='offset points', fontsize=7.5, color=MPL_GREY,
                arrowprops=dict(arrowstyle='->', color=MPL_GREY, lw=0.8))
    ax.annotate('Break-even\nK + Premium', xy=(K+P, 0),
                xytext=(10, 12), textcoords='offset points',
                fontsize=7.5, color=MPL_GREEN,
                arrowprops=dict(arrowstyle='->', color=MPL_GREEN, lw=0.8))
    ax.annotate(f'Max Loss = −{P}\n(premium paid)',
                xy=(70, -P), fontsize=7.5, color=MPL_RED,
                ha='center', va='bottom')
    ax.annotate('Unlimited\nupside', xy=(155, profit[-1]),
                xytext=(-30, 8), textcoords='offset points',
                fontsize=7.5, color=MPL_GREEN,
                arrowprops=dict(arrowstyle='->', color=MPL_GREEN, lw=0.8))

    ax.set_xlim(60, 160)
    ax.set_xticks([60, 80, K, K+P, 140, 160])
    ax.set_xticklabels(['60', '80', 'K=100', f'{K+P}', '140', '160'],
                       fontsize=7.5)
    fig.tight_layout()
    return fig_to_image(fig)

def make_short_call_chart():
    K, P = 100, 8
    S = np.linspace(60, 160, 400)
    profit = np.where(S > K, -(S - K) + P, P)

    fig, ax = plt.subplots(figsize=(7, 3.8))
    _base_ax(ax, 'Position 2 — Short Call')

    ax.fill_between(S, profit, 0,
                    where=(profit > 0), alpha=0.15, color=MPL_GREEN)
    ax.fill_between(S, profit, 0,
                    where=(profit < 0), alpha=0.15, color=MPL_RED)
    ax.plot(S, profit, color=MPL_RED, linewidth=2.2)

    ax.axvline(K, color=MPL_GREY, linewidth=1, linestyle=':')
    ax.axvline(K + P, color=MPL_RED, linewidth=1, linestyle='--', alpha=0.8)

    ax.annotate('Strike K', xy=(K, ax.get_ylim()[0]),
                xytext=(K - 20, -22), textcoords='offset points',
                fontsize=7.5, color=MPL_GREY,
                arrowprops=dict(arrowstyle='->', color=MPL_GREY, lw=0.8))
    ax.annotate(f'Max Gain = +{P}\n(premium received)',
                xy=(75, P), fontsize=7.5, color=MPL_GREEN,
                ha='center', va='bottom')
    ax.annotate('Unlimited\ndownside', xy=(155, profit[-1]),
                xytext=(-40, -20), textcoords='offset points',
                fontsize=7.5, color=MPL_RED,
                arrowprops=dict(arrowstyle='->', color=MPL_RED, lw=0.8))

    ax.set_xlim(60, 160)
    ax.set_xticks([60, 80, K, K+P, 140, 160])
    ax.set_xticklabels(['60', '80', 'K=100', f'{K+P}', '140', '160'],
                       fontsize=7.5)
    fig.tight_layout()
    return fig_to_image(fig)

def make_long_put_chart():
    K, P = 100, 8
    S = np.linspace(40, 160, 400)
    profit = np.where(S < K, K - S - P, -P)

    fig, ax = plt.subplots(figsize=(7, 3.8))
    _base_ax(ax, 'Position 3 — Long Put')

    ax.fill_between(S, profit, 0,
                    where=(profit > 0), alpha=0.15, color=MPL_GREEN)
    ax.fill_between(S, profit, 0,
                    where=(profit < 0), alpha=0.15, color=MPL_RED)
    ax.plot(S, profit, color=MPL_BLUE, linewidth=2.2)

    ax.axvline(K, color=MPL_GREY, linewidth=1, linestyle=':')
    ax.axvline(K - P, color=MPL_GREEN, linewidth=1, linestyle='--', alpha=0.8)

    ax.annotate('Strike K', xy=(K, ax.get_ylim()[0]),
                xytext=(4, -22), textcoords='offset points',
                fontsize=7.5, color=MPL_GREY,
                arrowprops=dict(arrowstyle='->', color=MPL_GREY, lw=0.8))
    ax.annotate('Break-even\nK − Premium', xy=(K-P, 0),
                xytext=(-60, 12), textcoords='offset points',
                fontsize=7.5, color=MPL_GREEN,
                arrowprops=dict(arrowstyle='->', color=MPL_GREEN, lw=0.8))
    ax.annotate(f'Max Loss = −{P}\n(premium paid)',
                xy=(130, -P), fontsize=7.5, color=MPL_RED,
                ha='center', va='bottom')
    ax.annotate(f'Max Gain = K − Premium\n= {K-P}',
                xy=(50, profit[50]), xytext=(10, 8),
                textcoords='offset points',
                fontsize=7.5, color=MPL_GREEN,
                arrowprops=dict(arrowstyle='->', color=MPL_GREEN, lw=0.8))

    ax.set_xlim(40, 160)
    ax.set_xticks([40, K-P, 80, K, 130, 160])
    ax.set_xticklabels(['40', f'{K-P}', '80', 'K=100', '130', '160'],
                       fontsize=7.5)
    fig.tight_layout()
    return fig_to_image(fig)

def make_short_put_chart():
    K, P = 100, 8
    S = np.linspace(40, 160, 400)
    profit = np.where(S < K, -(K - S) + P, P)

    fig, ax = plt.subplots(figsize=(7, 3.8))
    _base_ax(ax, 'Position 4 — Short Put')

    ax.fill_between(S, profit, 0,
                    where=(profit > 0), alpha=0.15, color=MPL_GREEN)
    ax.fill_between(S, profit, 0,
                    where=(profit < 0), alpha=0.15, color=MPL_RED)
    ax.plot(S, profit, color=MPL_RED, linewidth=2.2)

    ax.axvline(K, color=MPL_GREY, linewidth=1, linestyle=':')
    ax.axvline(K - P, color=MPL_RED, linewidth=1, linestyle='--', alpha=0.8)

    ax.annotate('Strike K', xy=(K, ax.get_ylim()[0]),
                xytext=(4, -22), textcoords='offset points',
                fontsize=7.5, color=MPL_GREY,
                arrowprops=dict(arrowstyle='->', color=MPL_GREY, lw=0.8))
    ax.annotate(f'Max Gain = +{P}\n(premium received)',
                xy=(140, P), fontsize=7.5, color=MPL_GREEN,
                ha='center', va='bottom')
    ax.annotate(f'Max Loss = K − Premium\n= {K-P}  (if S→0)',
                xy=(55, profit[30]), xytext=(10, -20),
                textcoords='offset points',
                fontsize=7.5, color=MPL_RED,
                arrowprops=dict(arrowstyle='->', color=MPL_RED, lw=0.8))

    ax.set_xlim(40, 160)
    ax.set_xticks([40, K-P, 80, K, 130, 160])
    ax.set_xticklabels(['40', f'{K-P}', '80', 'K=100', '130', '160'],
                       fontsize=7.5)
    fig.tight_layout()
    return fig_to_image(fig)

def make_pcp_chart():
    """Illustrate put-call parity: Long Stock + Long Put = Long Call + Cash (PV of K)."""
    K, P_put, P_call = 100, 8, 12
    S = np.linspace(50, 160, 400)

    stock_profit   = S - 100           # bought stock at 100
    long_put       = np.maximum(K - S, 0) - P_put
    portfolio_lhs  = stock_profit + long_put   # protective put

    long_call      = np.maximum(S - K, 0) - P_call
    cash_pv        = P_call - P_put            # bond (simplified)
    portfolio_rhs  = long_call + cash_pv       # fiduciary call

    fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
    for ax, profit, label, color, title in [
        (axes[0], portfolio_lhs, 'Stock + Long Put\n(Protective Put)', MPL_BLUE,
         'LHS: Stock + Long Put'),
        (axes[1], portfolio_rhs, 'Long Call + Cash (PV of K)\n(Fiduciary Call)', MPL_GREEN,
         'RHS: Long Call + Bond'),
    ]:
        _base_ax(ax, title)
        ax.fill_between(S, profit, 0, where=(profit>=0), alpha=0.15, color=MPL_GREEN)
        ax.fill_between(S, profit, 0, where=(profit<0),  alpha=0.15, color=MPL_RED)
        ax.plot(S, profit, color=color, linewidth=2.2, label=label)
        ax.axvline(K, color=MPL_GREY, linewidth=1, linestyle=':')
        ax.set_xlim(50, 160)

    fig.suptitle('Put–Call Parity:  C − P = S₀ − PV(K)',
                 fontsize=10, fontweight='bold', color='#1B3A6B', y=1.02)
    fig.tight_layout()
    return fig_to_image(fig, width_cm=17)

def make_collar_chart():
    K_put, K_call, P_put, P_call = 90, 110, 6, 6
    S = np.linspace(50, 160, 400)

    # Already hold stock at S0=100
    stock = S - 100
    long_put  = np.maximum(K_put - S, 0) - P_put
    short_call = -(np.maximum(S - K_call, 0)) + P_call
    collar = stock + long_put + short_call

    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    _base_ax(ax, 'Collar: Long Stock + Long Put + Short Call')

    ax.plot(S, stock,   color=MPL_GREY,  linewidth=1.4, linestyle='--', label='Unhedged stock', alpha=0.7)
    ax.plot(S, collar,  color=MPL_BLUE,  linewidth=2.2, label='Collar (net)')
    ax.fill_between(S, collar, 0, where=(collar>=0), alpha=0.12, color=MPL_GREEN)
    ax.fill_between(S, collar, 0, where=(collar<0),  alpha=0.12, color=MPL_RED)

    ax.axvline(K_put,  color=MPL_RED,  linewidth=1, linestyle=':', alpha=0.8)
    ax.axvline(K_call, color=MPL_GREEN, linewidth=1, linestyle=':', alpha=0.8)

    ax.annotate(f'Floor\n(Put K={K_put})', xy=(K_put, min(collar)),
                xytext=(-35, -20), textcoords='offset points',
                fontsize=7.5, color=MPL_RED,
                arrowprops=dict(arrowstyle='->', color=MPL_RED, lw=0.8))
    ax.annotate(f'Cap\n(Call K={K_call})', xy=(K_call, max(collar)),
                xytext=(5, 8), textcoords='offset points',
                fontsize=7.5, color=MPL_GREEN,
                arrowprops=dict(arrowstyle='->', color=MPL_GREEN, lw=0.8))

    ax.legend(fontsize=8, loc='upper left', framealpha=0.85)
    ax.set_xlim(50, 160)
    fig.tight_layout()
    return fig_to_image(fig, width_cm=15)

def make_moneyness_chart():
    """Bar chart comparing ITM / ATM / OTM intrinsic values."""
    labels = ['Deep\nOTM', 'OTM', 'ATM', 'ITM', 'Deep\nITM']
    intrinsic_call = [0, 0, 0, 10, 30]
    intrinsic_put  = [30, 10, 0, 0, 0]

    x = np.arange(len(labels))
    w = 0.35

    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.set_facecolor('#FAFBFC')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    b1 = ax.bar(x - w/2, intrinsic_call, w, label='Call intrinsic value',
                color=MPL_BLUE, alpha=0.8)
    b2 = ax.bar(x + w/2, intrinsic_put,  w, label='Put intrinsic value',
                color=MPL_GREEN, alpha=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel('Intrinsic Value', fontsize=9)
    ax.set_title('Moneyness & Intrinsic Value  (K = 100, S varies)',
                 fontsize=10, fontweight='bold', color='#1B3A6B')
    ax.legend(fontsize=8.5)
    ax.bar_label(b1, padding=2, fontsize=8)
    ax.bar_label(b2, padding=2, fontsize=8)
    fig.tight_layout()
    return fig_to_image(fig, width_cm=13)

# ── Document build ─────────────────────────────────────────────────────────
def build_pdf(path):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN,  bottomMargin=MARGIN,
        title='Options — Exam Reference Card',
        author='Corporate Finance Reference'
    )
    story = []

    # ── PAGE 1 — Title + Overview table ───────────────────────────────────
    story.append(Paragraph('Options — Exam Reference Card', ST['title']))
    story.append(rule(DARK_BLUE, 2))
    story.append(spacer(0.2))

    story.append(box_para(
        '<b>Exam task:</b> Given a graph, you must (1) name the position, '
        '(2) explain the payoff logic, (3) give a corporate hedging example.',
        bg=LIGHT_BLUE, border=MID_BLUE
    ))
    story.append(spacer(0.4))

    story.append(Paragraph('The 4 Positions at a Glance', ST['h1']))
    story.append(rule())

    overview_data = [
        [Paragraph('<b>Position</b>', ST['label_b']),
         Paragraph('<b>You…</b>', ST['label_b']),
         Paragraph('<b>Right / Obligation</b>', ST['label_b']),
         Paragraph('<b>Max Loss</b>', ST['label_b']),
         Paragraph('<b>Max Gain</b>', ST['label_b']),
         Paragraph('<b>Premium</b>', ST['label_b'])],
        ['Long Call',  'Buy call',  'Right to BUY at K',
         'Premium paid', 'Unlimited', 'Pay'],
        ['Short Call', 'Sell call', 'Obligation to SELL at K',
         'Unlimited', 'Premium received', 'Receive'],
        ['Long Put',   'Buy put',   'Right to SELL at K',
         'Premium paid', 'K − Premium', 'Pay'],
        ['Short Put',  'Sell put',  'Obligation to BUY at K',
         'K − Premium', 'Premium received', 'Receive'],
    ]
    col_w = [2.6*cm, 2.2*cm, 4.4*cm, 2.8*cm, 3.0*cm, 2.0*cm]
    ov_tbl = Table(overview_data, colWidths=col_w, repeatRows=1)
    ov_tbl.setStyle(TableStyle([
        ('BACKGROUND',   (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR',    (0,0), (-1,0), colors.white),
        ('FONTNAME',     (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',     (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [PALE_GREY, colors.white]),
        ('BOX',          (0,0), (-1,-1), 0.5, MID_BLUE),
        ('INNERGRID',    (0,0), (-1,-1), 0.3, MID_GREY),
        ('ALIGN',        (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',       (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',   (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',(0,0), (-1,-1), 5),
        # colour-code position names
        ('TEXTCOLOR', (0,1), (0,1), MID_BLUE),
        ('TEXTCOLOR', (0,2), (0,2), ACCENT_RED),
        ('TEXTCOLOR', (0,3), (0,3), MID_BLUE),
        ('TEXTCOLOR', (0,4), (0,4), ACCENT_RED),
        ('FONTNAME',  (0,1), (0,-1), 'Helvetica-Bold'),
    ]))
    story.append(ov_tbl)
    story.append(spacer(0.5))

    # Quick-identify table
    story.append(Paragraph('Quick Graph Identification', ST['h2']))
    qi_data = [
        [Paragraph('<b>Right side shape</b>', ST['label_b']),
         Paragraph('<b>Starting level (y-intercept)</b>', ST['label_b']),
         Paragraph('<b>Position</b>', ST['label_b'])],
        ['Rising (upward slope)',  'Below zero (−Premium)', 'Long Call'],
        ['Falling (downward slope)', 'Above zero (+Premium)', 'Short Call'],
        ['Flat, left side rises',  'Below zero (−Premium)', 'Long Put'],
        ['Flat, left side falls',  'Above zero (+Premium)', 'Short Put'],
    ]
    qi_col = [(PAGE_W - 2*MARGIN - 1*cm) / 3] * 3
    qi_tbl = Table(qi_data, colWidths=qi_col, repeatRows=1)
    qi_tbl.setStyle(TableStyle([
        ('BACKGROUND',     (0,0), (-1,0), MID_BLUE),
        ('TEXTCOLOR',      (0,0), (-1,0), colors.white),
        ('FONTNAME',       (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',       (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, PALE_GREY]),
        ('BOX',            (0,0), (-1,-1), 0.5, MID_BLUE),
        ('INNERGRID',      (0,0), (-1,-1), 0.3, MID_GREY),
        ('ALIGN',          (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',         (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',     (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',  (0,0), (-1,-1), 5),
        ('FONTNAME',       (0,1), (0,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR',      (0,1), (0,1), MID_BLUE),
        ('TEXTCOLOR',      (0,2), (0,2), ACCENT_RED),
        ('TEXTCOLOR',      (0,3), (0,3), MID_BLUE),
        ('TEXTCOLOR',      (0,4), (0,4), ACCENT_RED),
    ]))
    story.append(qi_tbl)

    story.append(PageBreak())

    # ── POSITIONS 1 & 2 ───────────────────────────────────────────────────
    for pos_num, pos_name, color_hex, chart_fn, payoff_lines, corp_title, corp_body in [
        (
            1, 'Long Call', '#2E5FA3', make_long_call_chart,
            [
                'If S &gt; K:  <b>Exercise.</b>  Payoff = S − K  |  Profit = (S − K) − Premium',
                'If S ≤ K:  <b>Do not exercise.</b>  Loss = Premium  (maximum possible loss)',
                'Break-even: S = K + Premium',
            ],
            'Corporate use — hedges the risk of <b>buying something that gets more expensive</b>',
            [
                '<b>Importer (FX risk):</b> A Belgian company buying goods priced in USD fears the '
                'EUR/USD rate will move against them, making imports costlier. They buy a call on USD — '
                'capping their effective exchange rate. If USD stays cheap they let the option expire; '
                'if USD spikes the call compensates.',
                '<b>Airline (fuel risk):</b> An airline buying jet fuel buys a call on crude oil — '
                'capping fuel costs regardless of how high oil prices go.',
            ]
        ),
        (
            2, 'Short Call', '#C0392B', make_short_call_chart,
            [
                'If S ≤ K:  <b>Buyer does not exercise.</b>  Profit = Premium received',
                'If S &gt; K:  <b>Buyer exercises.</b>  You must sell at K &lt; market price.  Loss = (S − K) − Premium',
                'Break-even: S = K + Premium',
            ],
            'Corporate use — income generation on assets already owned (<b>covered call</b>)',
            [
                '<b>Covered call:</b> A company holding shares in another firm sells call options on those '
                'shares to earn extra income (the premium). They agree to sell at K if the price rises that '
                'far. Risk: if the stock surges far above K, they miss the upside.',
                '<b>Important — naked short call:</b> Selling a call without owning the underlying is highly '
                'speculative (unlimited downside) and is rarely used for corporate hedging.',
            ]
        ),
    ]:
        story.append(Paragraph(f'Position {pos_num} — {pos_name}', ST['h1']))
        story.append(rule(colors.HexColor(color_hex)))
        story.append(spacer(0.1))

        story.append(Paragraph(
            f'<b>What it is:</b> You {"buy" if "Long" in pos_name else "sell"} a '
            f'{"call" if "Call" in pos_name else "put"} option. '
            + ('You pay a premium upfront for the <b>right to BUY</b> the asset at strike price K.'
               if pos_num == 1 else
               'You receive the premium upfront but take on the <b>obligation to SELL</b> the asset at K if exercised.'),
            ST['body']
        ))
        story.append(spacer(0.2))

        story.append(Paragraph('<b>Payoff at expiry:</b>', ST['h2']))
        for ln in payoff_lines:
            story.append(Paragraph('• ' + ln, ST['body']))
        story.append(spacer(0.2))

        story.append(chart_fn())
        story.append(spacer(0.2))

        story.append(Paragraph(corp_title, ST['h2']))
        lines_para = []
        for line in corp_body:
            lines_para.append(Paragraph(line, ST['body']))

        tbl = Table([[lines_para[i]] for i in range(len(lines_para))],
                    colWidths=[PAGE_W - 2*MARGIN])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), LIGHT_BLUE),
            ('BOX',        (0,0), (-1,-1), 0.7, BOX_BORDER),
            ('TOPPADDING',    (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING',   (0,0), (-1,-1), 10),
            ('RIGHTPADDING',  (0,0), (-1,-1), 10),
        ]))
        story.append(tbl)
        story.append(spacer(0.5))

    story.append(PageBreak())

    # ── POSITIONS 3 & 4 ───────────────────────────────────────────────────
    for pos_num, pos_name, color_hex, chart_fn, payoff_lines, corp_title, corp_body in [
        (
            3, 'Long Put', '#2E5FA3', make_long_put_chart,
            [
                'If S &lt; K:  <b>Exercise.</b>  Payoff = K − S  |  Profit = (K − S) − Premium',
                'If S ≥ K:  <b>Do not exercise.</b>  Loss = Premium  (maximum possible loss)',
                'Break-even: S = K − Premium  |  Max Gain = K − Premium  (if S → 0)',
            ],
            'Corporate use — hedges the risk of <b>owning something that loses value</b> (portfolio insurance)',
            [
                '<b>Fund manager:</b> Holds a large equity position and buys put options on it. '
                'If the stock crashes, the put pays out, offsetting the loss — classic portfolio insurance.',
                '<b>Belgian farmer:</b> Growing wheat fears prices will fall before harvest. They buy a put '
                'on wheat — guaranteeing a minimum selling price (K), while still benefiting if prices rise '
                '(they simply do not exercise the put).',
                '<b>Exporter (FX risk):</b> A company receiving USD in 3 months buys a put on USD — '
                'locking in a minimum EUR conversion rate. If USD weakens the put compensates.',
            ]
        ),
        (
            4, 'Short Put', '#C0392B', make_short_put_chart,
            [
                'If S ≥ K:  <b>Buyer does not exercise.</b>  Profit = Premium received',
                'If S &lt; K:  <b>Buyer exercises.</b>  You must buy at K &gt; market price.  Loss = (K − S) − Premium',
                'Break-even: S = K − Premium  |  Max Loss = K − Premium  (if S → 0)',
            ],
            'Corporate use — willingness to <b>acquire shares at a lower price</b>',
            [
                '<b>Acquisition strategy:</b> A company wants to buy shares in a target firm but believes '
                'the current price is too high. They sell put options at their desired purchase price K. '
                'If the stock falls to K, the put is exercised and they acquire the shares at K — exactly '
                'the price they wanted. They also pocket the premium as compensation for waiting.',
            ]
        ),
    ]:
        story.append(Paragraph(f'Position {pos_num} — {pos_name}', ST['h1']))
        story.append(rule(colors.HexColor(color_hex)))
        story.append(spacer(0.1))

        story.append(Paragraph(
            f'<b>What it is:</b> You {"buy" if "Long" in pos_name else "sell"} a '
            f'{"put" if "Put" in pos_name else "call"} option. '
            + ('You pay a premium upfront for the <b>right to SELL</b> the asset at strike price K.'
               if pos_num == 3 else
               'You receive the premium upfront but take on the <b>obligation to BUY</b> the asset at K if exercised.'),
            ST['body']
        ))
        story.append(spacer(0.2))

        story.append(Paragraph('<b>Payoff at expiry:</b>', ST['h2']))
        for ln in payoff_lines:
            story.append(Paragraph('• ' + ln, ST['body']))
        story.append(spacer(0.2))

        story.append(chart_fn())
        story.append(spacer(0.2))

        story.append(Paragraph(corp_title, ST['h2']))
        lines_para = []
        for line in corp_body:
            lines_para.append(Paragraph(line, ST['body']))
        tbl = Table([[lines_para[i]] for i in range(len(lines_para))],
                    colWidths=[PAGE_W - 2*MARGIN])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), LIGHT_BLUE),
            ('BOX',        (0,0), (-1,-1), 0.7, BOX_BORDER),
            ('TOPPADDING',    (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING',   (0,0), (-1,-1), 10),
            ('RIGHTPADDING',  (0,0), (-1,-1), 10),
        ]))
        story.append(tbl)
        story.append(spacer(0.5))

    story.append(PageBreak())

    # ── PAGE 4 — Moneyness + Put–Call Parity ──────────────────────────────
    story.append(Paragraph('Moneyness — ITM, ATM, OTM', ST['h1']))
    story.append(rule())
    story.append(spacer(0.1))

    story.append(Paragraph(
        'Moneyness describes the relationship between the current stock price S and the strike price K. '
        'It determines whether immediate exercise would be profitable.',
        ST['body']
    ))
    story.append(spacer(0.2))

    mono_data = [
        [Paragraph('<b>State</b>', ST['label_b']),
         Paragraph('<b>Call (right to buy)</b>', ST['label_b']),
         Paragraph('<b>Put (right to sell)</b>', ST['label_b']),
         Paragraph('<b>Intrinsic Value</b>', ST['label_b'])],
        ['In the Money (ITM)',   'S > K  (exercise is profitable)', 'S < K  (exercise is profitable)',  'max(S−K,0) or max(K−S,0) > 0'],
        ['At the Money (ATM)',   'S = K  (indifferent)',             'S = K  (indifferent)',              '0'],
        ['Out of the Money (OTM)', 'S < K  (would not exercise)',   'S > K  (would not exercise)',       '0  (expires worthless)'],
    ]
    mono_col = [2.8*cm, 4.5*cm, 4.5*cm, 5.2*cm]
    mono_tbl = Table(mono_data, colWidths=mono_col, repeatRows=1)
    mono_tbl.setStyle(TableStyle([
        ('BACKGROUND',     (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR',      (0,0), (-1,0), colors.white),
        ('FONTNAME',       (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',       (0,0), (-1,-1), 8.2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1),
         [colors.HexColor('#E8F5E9'), colors.HexColor('#FFF8E1'), colors.HexColor('#FFEBEE')]),
        ('BOX',            (0,0), (-1,-1), 0.5, DARK_BLUE),
        ('INNERGRID',      (0,0), (-1,-1), 0.3, MID_GREY),
        ('ALIGN',          (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',         (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',     (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',  (0,0), (-1,-1), 5),
        ('FONTNAME',       (0,1), (0,-1), 'Helvetica-Bold'),
    ]))
    story.append(mono_tbl)
    story.append(spacer(0.3))
    story.append(make_moneyness_chart())
    story.append(spacer(0.3))

    # Option value decomposition
    story.append(Paragraph('Option Value = Intrinsic Value + Time Value', ST['h2']))
    story.append(Paragraph(
        '• <b>Intrinsic value</b> — the immediate exercise value: max(S − K, 0) for a call; max(K − S, 0) for a put.<br/>'
        '• <b>Time value</b> — the extra amount the market pays above intrinsic value, reflecting uncertainty '
        'and the possibility that the option moves further in the money before expiry. '
        'Time value decays to zero at expiration (theta decay).',
        ST['body']
    ))
    story.append(spacer(0.5))

    # Put–Call Parity
    story.append(Paragraph('Put–Call Parity', ST['h1']))
    story.append(rule())
    story.append(spacer(0.1))

    story.append(box_para(
        '<b>Formula:</b>  C − P = S₀ − PV(K)  &nbsp;&nbsp;→&nbsp;&nbsp;  '
        'C + PV(K) = P + S₀<br/>'
        'Where: C = call price, P = put price, S₀ = current stock price, '
        'PV(K) = K · e<super>−rT</super> (present value of strike).',
        bg=colors.HexColor('#EEF7F0'), border=ACCENT_GRN
    ))
    story.append(spacer(0.25))
    story.append(Paragraph(
        'Put–call parity is a <b>no-arbitrage relationship</b> for European options with the same strike K '
        'and expiry T on a non-dividend-paying asset. It says two portfolios with identical payoffs must '
        'have the same price today:',
        ST['body']
    ))
    story.append(spacer(0.1))

    pcp_data = [
        [Paragraph('<b>LHS portfolio</b>', ST['label_b']),
         Paragraph('<b>RHS portfolio</b>', ST['label_b'])],
        [Paragraph('Long Call  +  Cash (PV of K)\n<i>(fiduciary call)</i>', ST['body']),
         Paragraph('Long Stock  +  Long Put\n<i>(protective put)</i>', ST['body'])],
        [Paragraph('Payoff at expiry:\nS &gt; K: (S−K) + K = S\nS ≤ K: 0 + K = K', ST['code']),
         Paragraph('Payoff at expiry:\nS &gt; K: S + 0 = S\nS ≤ K: S + (K−S) = K', ST['code'])],
    ]
    pcp_col = [(PAGE_W - 2*MARGIN) / 2] * 2
    pcp_tbl = Table(pcp_data, colWidths=pcp_col)
    pcp_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), MID_BLUE),
        ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
        ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, PALE_GREY]),
        ('BOX',        (0,0), (-1,-1), 0.5, MID_BLUE),
        ('INNERGRID',  (0,0), (-1,-1), 0.4, MID_GREY),
        ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(pcp_tbl)
    story.append(spacer(0.25))
    story.append(make_pcp_chart())

    story.append(PageBreak())

    # ── PAGE 5 — Collar strategy ──────────────────────────────────────────
    story.append(Paragraph('Collar Strategy (Combined Position)', ST['h1']))
    story.append(rule())
    story.append(spacer(0.1))

    story.append(Paragraph(
        'A <b>collar</b> is the most common corporate hedging structure. It combines <b>three legs</b>:',
        ST['body']
    ))

    collar_legs = [
        [Paragraph('<b>Leg</b>', ST['label_b']),
         Paragraph('<b>Position</b>', ST['label_b']),
         Paragraph('<b>Effect</b>', ST['label_b'])],
        ['1', 'Already own the underlying asset', 'Exposed to price movements'],
        ['2', 'Buy a put (strike K_put, lower)', 'Sets a floor — limits downside'],
        ['3', 'Sell a call (strike K_call, higher)', 'Sets a cap — limits upside; premium offsets cost of put'],
    ]
    c_col = [1.2*cm, 6.0*cm, (PAGE_W-2*MARGIN-7.2*cm)]
    c_tbl = Table(collar_legs, colWidths=c_col)
    c_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR',     (0,0), (-1,0), colors.white),
        ('FONTNAME',      (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [PALE_GREY, colors.white, LIGHT_BLUE]),
        ('BOX',           (0,0), (-1,-1), 0.5, DARK_BLUE),
        ('INNERGRID',     (0,0), (-1,-1), 0.3, MID_GREY),
        ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(c_tbl)
    story.append(spacer(0.3))
    story.append(make_collar_chart())
    story.append(spacer(0.3))

    story.append(box_para(
        '<b>Zero-cost collar:</b> The premium received from selling the call exactly offsets the premium paid '
        'for the put → net cost = 0. The company trades away upside for free downside protection.',
        bg=colors.HexColor('#FFF8E1'), border=GOLD
    ))
    story.append(spacer(0.4))

    # ── One-line hedging rules ─────────────────────────────────────────────
    story.append(Paragraph('Corporate Hedging — One-Line Rules', ST['h1']))
    story.append(rule())
    hedge_data = [
        [Paragraph('<b>You fear…</b>', ST['label_b']),
         Paragraph('<b>You use…</b>', ST['label_b']),
         Paragraph('<b>Because…</b>', ST['label_b'])],
        ['Price of something you BUY goes UP',
         Paragraph('<b>Long Call</b>', ST['body']),
         'Caps your maximum purchase cost'],
        ['Price of something you OWN goes DOWN',
         Paragraph('<b>Long Put</b>', ST['body']),
         'Floors your minimum selling price'],
        ['You want income on shares you hold',
         Paragraph('<b>Short Call</b>', ST['body']),
         'Collect premium; agree to sell at K'],
        ['You want to buy shares at a lower price',
         Paragraph('<b>Short Put</b>', ST['body']),
         'Collect premium; agree to buy at K'],
        ['You own an asset and want to limit both risk and cost',
         Paragraph('<b>Collar</b>', ST['body']),
         'Buy put (floor) + sell call (cap); can be zero-cost'],
    ]
    h_col = [5.2*cm, 2.6*cm, (PAGE_W-2*MARGIN-7.8*cm)]
    h_tbl = Table(hedge_data, colWidths=h_col, repeatRows=1)
    h_tbl.setStyle(TableStyle([
        ('BACKGROUND',     (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR',      (0,0), (-1,0), colors.white),
        ('FONTNAME',       (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',       (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, PALE_GREY]),
        ('BOX',            (0,0), (-1,-1), 0.5, DARK_BLUE),
        ('INNERGRID',      (0,0), (-1,-1), 0.3, MID_GREY),
        ('ALIGN',          (0,0), (-1,-1), 'LEFT'),
        ('VALIGN',         (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',     (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',  (0,0), (-1,-1), 5),
        ('LEFTPADDING',    (0,0), (-1,-1), 8),
    ]))
    story.append(h_tbl)

    story.append(PageBreak())

    # ── PAGE 6 — Key Terminology ───────────────────────────────────────────
    story.append(Paragraph('Key Terminology the Exam Expects', ST['h1']))
    story.append(rule())
    story.append(spacer(0.2))

    terms = [
        ('Premium', 'The price paid (buyer) or received (seller) for the option contract. '
                    'It is determined at inception and is non-refundable.'),
        ('Strike price (K)', 'The pre-agreed price at which the option can be exercised.'),
        ('In the money (ITM)', 'Exercising would be immediately profitable: S > K for a call; S < K for a put.'),
        ('At the money (ATM)', 'S ≈ K. Intrinsic value is zero; the option has only time value.'),
        ('Out of the money (OTM)', 'Exercising would not be beneficial; the option expires worthless if still OTM at expiry.'),
        ('Intrinsic value', 'max(S − K, 0) for a call; max(K − S, 0) for a put. The value if exercised right now.'),
        ('Time value', 'Option price − intrinsic value. Reflects uncertainty and time remaining. '
                       'Decays to zero at expiry (theta decay).'),
        ('Asymmetric payoff', 'The option holder has a right, not an obligation → bounded maximum loss '
                              '(the premium), but asymmetric upside/downside.'),
        ('European option', 'Can only be exercised at expiry. Used in most textbook formulas '
                            '(e.g. Black–Scholes).'),
        ('American option', 'Can be exercised at any time up to and including expiry. '
                            'Worth at least as much as a European option.'),
        ('Put–Call Parity', 'C − P = S₀ − PV(K). A no-arbitrage relationship between call price, '
                            'put price, spot price, and present value of the strike (European options only).'),
        ('Hedging vs. speculation', 'Corporates use options to REDUCE a pre-existing risk exposure '
                                    '(hedging), not to create new exposure (speculation).'),
        ('Covered call', 'Selling a call while already owning the underlying — limits upside '
                         'but the unlimited loss risk is covered by the shares held.'),
        ('Protective put', 'Owning the underlying + buying a put — provides downside insurance '
                           'while keeping unlimited upside.'),
        ('Collar', 'Protective put + covered call on the same underlying — bounds both upside '
                   'and downside. Can be structured as zero-cost.'),
    ]

    for term, defn in terms:
        row = Table(
            [[Paragraph(f'<b>{term}</b>', ST['label_b']),
              Paragraph(defn, ST['body'])]],
            colWidths=[4.2*cm, PAGE_W - 2*MARGIN - 4.2*cm]
        )
        row.setStyle(TableStyle([
            ('VALIGN',        (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING',    (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING',   (0,0), (-1,-1), 4),
            ('LINEBELOW',     (0,0), (-1,-1), 0.3, MID_GREY),
        ]))
        story.append(row)

    story.append(spacer(0.6))

    # Study tips
    story.append(Paragraph('Exam Study Tips', ST['h1']))
    story.append(rule())
    tips = [
        'Identify graph shape first (flat vs. sloping on each side), then read the sign of the '
        'y-intercept. Those two observations uniquely determine all 4 basic positions.',
        'Remember: <b>Long = pay premium, Short = receive premium.</b>  '
        'The starting level of the profit line tells you which side of the trade you are on.',
        'For corporate examples: map the company\'s UNDERLYING EXPOSURE first, then choose the '
        'option that offsets it. An importer has a natural "long USD cost" position → needs a '
        'long call on USD to hedge.',
        'Put–call parity can be used to derive any one of C, P, S₀, PV(K) if the other three are known.',
        'Time value is highest for ATM options and for options with long time to expiry — '
        'important for pricing intuition.',
    ]
    for i, tip in enumerate(tips, 1):
        story.append(box_para(
            f'<b>Tip {i}:</b> {tip}',
            bg=colors.HexColor('#FFFDE7'),
            border=GOLD,
            style=ST['body'],
            pad=6
        ))
        story.append(spacer(0.15))

    doc.build(story)
    print(f'PDF written to {path}')

if __name__ == '__main__':
    build_pdf('/home/user/BabyPluto/Options_Reference_Card_v2.pdf')
