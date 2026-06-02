import io, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
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

# ── Fonts ────────────────────────────────────────────────────────────────────
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV",   FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DV-M", FD + "DejaVuSansMono.ttf"))
registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV", boldItalic="DV-B")

# ── Matplotlib global style ──────────────────────────────────────────────────
DARK_BLUE_HEX  = "#1B3A6B"
MID_BLUE_HEX   = "#2E6DA4"
ORANGE_HEX     = "#D4500A"
GREEN_HEX      = "#1A6B3A"
LIGHT_BLUE_HEX = "#D6E8F7"
RED_HEX        = "#C0392B"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 10,
    "axes.titleweight": "bold",
    "axes.titlecolor": DARK_BLUE_HEX,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

rng = np.random.default_rng(42)

def fig_to_image(fig, width_cm):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    w = width_cm * cm
    # preserve aspect ratio
    from PIL import Image as PILImage
    pil = PILImage.open(buf)
    pw, ph = pil.size
    h = w * ph / pw
    buf.seek(0)
    return Image(buf, width=w, height=h)

# ════════════════════════════════════════════════════════════════════════════
# PLOT GENERATORS
# ════════════════════════════════════════════════════════════════════════════

def plot_log_shapes():
    """4-panel: shapes of linear, linear-log, log-linear, log-log relationships."""
    x = np.linspace(0.5, 5, 120)
    fig, axes = plt.subplots(1, 4, figsize=(12, 2.8))
    configs = [
        ("Linear\nY = α + βX", x, 1 + 1.2*x, "X", "Y"),
        ("Linear-Log\nY = α + β·ln(X)", x, 1 + 2.5*np.log(x), "X", "Y"),
        ("Log-Linear\nln(Y) = α + βX", x, np.log(0.5 + 1.1*x), "X", "ln(Y)"),
        ("Log-Log\nln(Y) = α + β·ln(X)", x, 0.5 + 0.8*np.log(x), "ln(X)", "ln(Y)"),
    ]
    for ax, (title, xv, yv, xl, yl) in zip(axes, configs):
        ax.plot(xv, yv, color=MID_BLUE_HEX, lw=2.5)
        ax.set_title(title, fontsize=9, color=DARK_BLUE_HEX, pad=6)
        ax.set_xlabel(xl, fontsize=8)
        ax.set_ylabel(yl, fontsize=8)
        ax.tick_params(labelsize=7)
    fig.tight_layout(pad=1.2)
    return fig

def plot_residual_patterns():
    """3 residual plots: good, heteroskedastic, non-linear."""
    fitted = np.linspace(10, 60, 100)
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.2))

    # Good
    res_good = rng.normal(0, 3, 100)
    axes[0].scatter(fitted, res_good, color=MID_BLUE_HEX, s=18, alpha=0.7)
    axes[0].axhline(0, color="black", lw=1, ls="--")
    axes[0].set_title("Good Residual Plot\n(random scatter — no pattern)", color=GREEN_HEX)
    axes[0].set_xlabel("Fitted values")
    axes[0].set_ylabel("Residuals")
    axes[0].set_ylim(-12, 12)

    # Heteroskedastic (fan)
    spread = 0.12 * fitted
    res_het = rng.normal(0, 1, 100) * spread
    axes[1].scatter(fitted, res_het, color=ORANGE_HEX, s=18, alpha=0.7)
    axes[1].axhline(0, color="black", lw=1, ls="--")
    # draw fan envelope
    axes[1].plot(fitted,  2*spread, color=ORANGE_HEX, lw=1.2, ls=":", alpha=0.6)
    axes[1].plot(fitted, -2*spread, color=ORANGE_HEX, lw=1.2, ls=":", alpha=0.6)
    axes[1].set_title("Heteroskedasticity\n(fan/cone shape — variance grows)", color=ORANGE_HEX)
    axes[1].set_xlabel("Fitted values")
    axes[1].set_ylabel("Residuals")

    # Non-linear (curved)
    res_nl = -0.006*(fitted-35)**2 + 5 + rng.normal(0, 1.5, 100)
    axes[2].scatter(fitted, res_nl, color=RED_HEX, s=18, alpha=0.7)
    axes[2].axhline(0, color="black", lw=1, ls="--")
    smooth_x = np.linspace(10, 60, 300)
    smooth_y = -0.006*(smooth_x-35)**2 + 5
    axes[2].plot(smooth_x, smooth_y, color=RED_HEX, lw=2, alpha=0.6)
    axes[2].set_title("Non-Linearity\n(curved arc — model misspecified)", color=RED_HEX)
    axes[2].set_xlabel("Fitted values")
    axes[2].set_ylabel("Residuals")

    fig.tight_layout(pad=1.5)
    return fig

def plot_heteroskedasticity_white():
    """Squared residuals vs X — flat (good) and fanning (bad)."""
    x = np.linspace(1, 10, 120)
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.2))

    # Homoskedastic: ê² roughly flat
    e2_good = rng.exponential(1, 120) * 2
    axes[0].scatter(x, e2_good, color=MID_BLUE_HEX, s=16, alpha=0.7)
    axes[0].axhline(np.mean(e2_good), color=DARK_BLUE_HEX, lw=1.5, ls="--", label="mean ê²")
    axes[0].set_title("Homoskedastic\nê² does not trend with X", color=GREEN_HEX)
    axes[0].set_xlabel("X")
    axes[0].set_ylabel("ê²  (squared residuals)")
    axes[0].legend(fontsize=7)

    # Heteroskedastic: ê² grows with X
    e2_het = rng.exponential(1, 120) * (x**2) * 0.18
    axes[1].scatter(x, e2_het, color=ORANGE_HEX, s=16, alpha=0.7)
    slope = np.polyfit(x, e2_het, 1)
    axes[1].plot(x, np.polyval(slope, x), color=ORANGE_HEX, lw=2, ls="--",
                 label="rising trend in ê²")
    axes[1].set_title("Heteroskedastic\nê² grows with X  →  White test flags this", color=ORANGE_HEX)
    axes[1].set_xlabel("X")
    axes[1].set_ylabel("ê²  (squared residuals)")
    axes[1].legend(fontsize=7)

    fig.tight_layout(pad=1.5)
    return fig

def plot_omitted_variable_bias():
    """2×2 sign grid rendered as a coloured heatmap-style table."""
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.set_xlim(0, 4); ax.set_ylim(0, 2)
    ax.axis("off")

    cases = [
        (0, 1, "β_Z > 0", "r(X,Z) > 0", "UPWARD BIAS\n(estimate too high)", "#D6F0E0", GREEN_HEX),
        (1, 1, "β_Z > 0", "r(X,Z) < 0", "DOWNWARD BIAS\n(estimate too low)", "#FDE8E8", RED_HEX),
        (2, 1, "β_Z < 0", "r(X,Z) > 0", "DOWNWARD BIAS\n(estimate too low)", "#FDE8E8", RED_HEX),
        (3, 1, "β_Z < 0", "r(X,Z) < 0", "UPWARD BIAS\n(estimate too high)", "#D6F0E0", GREEN_HEX),
        (0, 0, "β_Z > 0", "r(X,Z) > 0", "(+) × (+) = +", "#D6E8F7", MID_BLUE_HEX),
        (1, 0, "β_Z > 0", "r(X,Z) < 0", "(+) × (−) = −", "#FFF8DC", ORANGE_HEX),
        (2, 0, "β_Z < 0", "r(X,Z) > 0", "(−) × (+) = −", "#FFF8DC", ORANGE_HEX),
        (3, 0, "β_Z < 0", "r(X,Z) < 0", "(−) × (−) = +", "#D6E8F7", MID_BLUE_HEX),
    ]
    for col, row, top, mid, bot, bg, fc in cases:
        rect = mpatches.FancyBboxPatch((col+0.04, row+0.04), 0.92, 0.92,
                                        boxstyle="round,pad=0.02", facecolor=bg,
                                        edgecolor="#AAAAAA", linewidth=0.8)
        ax.add_patch(rect)
        ax.text(col+0.5, row+0.78, top, ha="center", va="center",
                fontsize=7, color=DARK_BLUE_HEX, fontweight="bold")
        ax.text(col+0.5, 0.5 + row*0.5 + 0.15, bot,
                ha="center", va="center", fontsize=7.5, color=fc, fontweight="bold",
                multialignment="center")

    ax.text(2, 1.97, "sign(bias) = sign(β_Z)  ×  sign(r(X, Z))",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE_HEX, fontweight="bold")
    fig.tight_layout(pad=0.3)
    return fig

def plot_time_series_stationarity():
    """3 time-series panels: stationary, deterministic trend, random walk."""
    n = 100
    t = np.arange(n)
    rng2 = np.random.default_rng(7)

    # Stationary AR(1)
    y1 = np.zeros(n); y1[0] = 0
    e1 = rng2.normal(0, 1, n)
    for i in range(1, n):
        y1[i] = 0.45*y1[i-1] + e1[i]

    # Deterministic trend
    e2 = rng2.normal(0, 1, n)
    y2 = np.zeros(n)
    for i in range(1, n):
        y2[i] = 0.3*t[i] + 0.4*y2[i-1] + e2[i]*1.5
    trend_line = 0.3*t + np.mean(y2 - 0.3*t)

    # Random walk
    y3 = np.cumsum(rng2.normal(0, 1, n))

    fig, axes = plt.subplots(1, 3, figsize=(13, 3.5))
    cols = [GREEN_HEX, MID_BLUE_HEX, RED_HEX]
    data = [(y1, "Stationary Series\n(fluctuates around constant mean)",
             GREEN_HEX, True),
            (y2, "Deterministic Trend\n(drifts predictably — add time t as regressor)",
             MID_BLUE_HEX, False),
            (y3, "Random Walk / Unit Root\n(wanders — take first differences)",
             RED_HEX, False)]

    for ax, (y, title, col, show_mean) in zip(axes, data):
        ax.plot(t, y, color=col, lw=1.6, alpha=0.85)
        if show_mean:
            ax.axhline(np.mean(y), color=DARK_BLUE_HEX, lw=1.5, ls="--",
                       label=f"mean = {np.mean(y):.2f}")
            ax.legend(fontsize=7)
        if not show_mean and col == MID_BLUE_HEX:
            ax.plot(t, trend_line, color=DARK_BLUE_HEX, lw=1.5, ls="--",
                    label="trend line λt")
            ax.legend(fontsize=7)
        ax.set_title(title, color=col, pad=6)
        ax.set_xlabel("Time")
        ax.set_ylabel("Y")

    fig.tight_layout(pad=1.5)
    return fig

def plot_df_decision():
    """Number line showing DF t-statistics vs critical values."""
    fig, ax = plt.subplots(figsize=(10, 2.6))
    ax.set_xlim(-6, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.axis("off")

    # Number line
    ax.annotate("", xy=(1.3, 0.7), xytext=(-5.8, 0.7),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.5))
    for x in np.arange(-5, 1.5, 1):
        ax.text(x, 0.55, str(int(x)), ha="center", fontsize=8, color="#555555")

    # Reject region
    ax.axvspan(-6, -2.86, ymin=0.45, ymax=0.85, alpha=0.18, color=GREEN_HEX)
    ax.axvspan(-2.86, 1.5, ymin=0.45, ymax=0.85, alpha=0.12, color=RED_HEX)

    # Critical values
    for cv, label, offset in [(-2.86, "CV = −2.86\n(Version 1, 5%)", 0.2),
                                (-3.41, "CV = −3.41\n(Version 2, 5%)", -0.25)]:
        ax.axvline(cv, ymin=0.3, ymax=0.9, color=DARK_BLUE_HEX, lw=2, ls="--")
        ax.text(cv + offset, 1.25, label, ha="center", fontsize=8,
                color=DARK_BLUE_HEX, fontweight="bold")

    # Example statistics
    for t_val, label, col in [(-4.5, "t = −4.50\n→ Reject H₀\n(stationary ✓)", GREEN_HEX),
                               (-1.6, "t = −1.60\n→ Fail to reject\n(unit root ✗)", RED_HEX)]:
        ax.annotate("", xy=(t_val, 0.7), xytext=(t_val, 0.1),
                    arrowprops=dict(arrowstyle="->", color=col, lw=2))
        ax.text(t_val, -0.1, label, ha="center", fontsize=8, color=col,
                fontweight="bold", multialignment="center")

    ax.text(-5.5, 1.25, "REJECT H₀\n(stationary)", ha="center", fontsize=8.5,
            color=GREEN_HEX, fontweight="bold")
    ax.text(0.5, 1.25, "FAIL TO REJECT\n(unit root)", ha="center", fontsize=8.5,
            color=RED_HEX, fontweight="bold")

    fig.tight_layout(pad=0.5)
    return fig

def plot_autocorrelation_residuals():
    """Residuals vs time: no autocorrelation, positive autocorrelation."""
    n = 80
    t = np.arange(n)
    rng3 = np.random.default_rng(12)

    # No autocorrelation
    e_none = rng3.normal(0, 1.5, n)

    # Positive autocorrelation AR(1) with ρ=0.85
    e_pos = np.zeros(n)
    for i in range(1, n):
        e_pos[i] = 0.85*e_pos[i-1] + rng3.normal(0, 0.6)

    fig, axes = plt.subplots(1, 2, figsize=(11, 3.2))

    axes[0].plot(t, e_none, color=MID_BLUE_HEX, lw=1.2, alpha=0.8)
    axes[0].scatter(t, e_none, color=MID_BLUE_HEX, s=12, alpha=0.5)
    axes[0].axhline(0, color="black", lw=1, ls="--")
    axes[0].set_title("No Autocorrelation (ρ = 0)\nRandom scatter — A3 satisfied ✓", color=GREEN_HEX)
    axes[0].set_xlabel("Time period t")
    axes[0].set_ylabel("Residual eₜ")
    axes[0].set_ylim(-5, 5)

    axes[1].plot(t, e_pos, color=ORANGE_HEX, lw=1.8, alpha=0.9)
    axes[1].scatter(t, e_pos, color=ORANGE_HEX, s=12, alpha=0.5)
    axes[1].axhline(0, color="black", lw=1, ls="--")
    axes[1].fill_between(t, e_pos, 0, alpha=0.15, color=ORANGE_HEX)
    axes[1].set_title("Positive Autocorrelation (ρ ≈ 0.85)\nLong runs above/below zero — A3 violated ✗",
                      color=ORANGE_HEX)
    axes[1].set_xlabel("Time period t")
    axes[1].set_ylabel("Residual eₜ")

    fig.tight_layout(pad=1.5)
    return fig

def plot_dl_multipliers():
    """Bar chart of DL(3) coefficients + cumulative multiplier line."""
    lags = [0, 1, 2, 3]
    betas = [0.85, 0.52, 0.31, 0.09]
    cumulative = np.cumsum(betas)

    fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))

    bar_cols = [MID_BLUE_HEX if b >= 0 else RED_HEX for b in betas]
    bars = axes[0].bar(lags, betas, color=bar_cols, edgecolor="white",
                       linewidth=1.2, width=0.55)
    for bar, val in zip(bars, betas):
        axes[0].text(bar.get_x() + bar.get_width()/2, val + 0.015,
                     f"β{lags[betas.index(val)]} = {val}", ha="center",
                     fontsize=8.5, color=DARK_BLUE_HEX, fontweight="bold")
    axes[0].set_xticks(lags)
    axes[0].set_xticklabels(["Lag 0\n(current)", "Lag 1\n(1 period ago)",
                              "Lag 2\n(2 periods ago)", "Lag 3\n(3 periods ago)"], fontsize=8)
    axes[0].set_ylabel("Effect size (βₖ)", fontsize=9)
    axes[0].set_title("DL(3): Distributed Lag Coefficients\nEffect of X spreads over 4 periods",
                      color=DARK_BLUE_HEX)
    axes[0].set_ylim(0, 1.1)
    axes[0].axhline(0, color="black", lw=0.8)

    # Cumulative
    axes[1].bar(lags, cumulative, color=GREEN_HEX, alpha=0.7, edgecolor="white",
                linewidth=1.2, width=0.55)
    axes[1].plot(lags, cumulative, "o-", color=DARK_BLUE_HEX, lw=2, ms=7,
                 zorder=5)
    for lag, val in zip(lags, cumulative):
        axes[1].text(lag, val + 0.025, f"{val:.2f}", ha="center",
                     fontsize=8.5, color=DARK_BLUE_HEX, fontweight="bold")
    axes[1].axhline(cumulative[-1], color=ORANGE_HEX, lw=1.8, ls="--",
                    label=f"Total multiplier = {cumulative[-1]:.2f}")
    axes[1].set_xticks(lags)
    axes[1].set_xticklabels(["After\nlag 0", "After\nlag 1",
                              "After\nlag 2", "After\nlag 3"], fontsize=8)
    axes[1].set_ylabel("Cumulative effect", fontsize=9)
    axes[1].set_title("Cumulative Multiplier\nHow total effect builds up over time",
                      color=DARK_BLUE_HEX)
    axes[1].set_ylim(0, 2.1)
    axes[1].legend(fontsize=8.5, frameon=False)

    fig.tight_layout(pad=1.5)
    return fig

def plot_ar1_impulse():
    """AR(1) impulse response — geometric decay of a one-time shock."""
    gamma = 0.65
    beta = 1.0
    periods = 10
    t = np.arange(periods)
    effect = beta * gamma**t

    fig, ax = plt.subplots(figsize=(9, 3.4))
    ax.bar(t, effect, color=MID_BLUE_HEX, alpha=0.75, edgecolor="white",
           linewidth=1.2, width=0.6)
    ax.plot(t, effect, "o-", color=DARK_BLUE_HEX, lw=2, ms=7, zorder=5)
    for i, (ti, eff) in enumerate(zip(t, effect)):
        ax.text(ti, eff + 0.012, f"{eff:.3f}", ha="center",
                fontsize=7.5, color=DARK_BLUE_HEX, fontweight="bold")

    total = beta / (1 - gamma)
    ax.axhline(0, color="black", lw=0.8)
    ax.set_title(f"AR(1) Impulse Response  (β = {beta:.1f},  γ = {gamma})\n"
                 f"A one-time shock of 1 unit decays geometrically.  "
                 f"Total multiplier = β/(1−γ) = {total:.2f}",
                 color=DARK_BLUE_HEX, fontsize=9.5)
    ax.set_xlabel("Periods after the shock", fontsize=9)
    ax.set_ylabel("Effect on Y", fontsize=9)
    ax.set_xticks(t)

    # annotation
    ax.annotate("Each period: multiply by γ = 0.65",
                xy=(3, effect[3]), xytext=(5.5, 0.45),
                arrowprops=dict(arrowstyle="->", color=ORANGE_HEX, lw=1.5),
                fontsize=8, color=ORANGE_HEX, fontweight="bold")
    fig.tight_layout(pad=1.2)
    return fig

def plot_det_vs_stoch():
    """Side-by-side: deterministic trend vs stochastic (random walk)."""
    n = 80
    t = np.arange(n)
    rng4 = np.random.default_rng(99)

    # Deterministic: λt + stationary noise
    e1 = rng4.normal(0, 2, n)
    y_det = 0.4*t + 10 + e1
    trend = 0.4*t + 10

    # Stochastic: random walk
    y_rw = np.cumsum(rng4.normal(0, 1.5, n)) + 10

    fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))

    axes[0].plot(t, y_det, color=MID_BLUE_HEX, lw=1.6, alpha=0.8,
                 label="Series Y_t")
    axes[0].plot(t, trend, color=DARK_BLUE_HEX, lw=2, ls="--",
                 label="Trend line λt")
    axes[0].set_title("Deterministic Trend  (|ρ| < 1, λ ≠ 0)\nFix: add t as regressor",
                      color=MID_BLUE_HEX)
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("Y")
    axes[0].legend(fontsize=8, frameon=False)

    # show "returns to trend" arrows
    for idx in [30, 50, 65]:
        axes[0].annotate("", xy=(idx, trend[idx]),
                         xytext=(idx, y_det[idx]),
                         arrowprops=dict(arrowstyle="->",
                                         color=GREEN_HEX, lw=1.2, alpha=0.6))

    axes[1].plot(t, y_rw, color=RED_HEX, lw=1.8, alpha=0.85, label="Random walk Y_t")
    # No consistent trend to draw — add label for wandering
    axes[1].set_title("Stochastic Trend / Random Walk  (ρ = 1)\nFix: take first differences ΔY",
                      color=RED_HEX)
    axes[1].set_xlabel("Time")
    axes[1].set_ylabel("Y")
    axes[1].legend(fontsize=8, frameon=False)
    axes[1].text(40, np.mean(y_rw) + 5,
                 "Variance grows\nover time", fontsize=8,
                 color=RED_HEX, fontweight="bold",
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="#FDE8E8",
                           edgecolor=RED_HEX, alpha=0.8))

    fig.tight_layout(pad=1.5)
    return fig

def plot_dummy_bar():
    """Bar chart comparing mean Y across categories, highlighting reference."""
    categories = ["Center\n(reference)", "North", "South", "East"]
    means = [45, 58, 39, 51]
    cols = [DARK_BLUE_HEX, MID_BLUE_HEX, MID_BLUE_HEX, MID_BLUE_HEX]
    alphas = [1.0, 0.8, 0.8, 0.8]

    fig, ax = plt.subplots(figsize=(8, 3.5))
    bars = ax.bar(categories, means, color=cols, edgecolor="white",
                  linewidth=1.2, width=0.55)
    bars[0].set_hatch("//")
    bars[0].set_edgecolor("#AAAAAA")

    ref_line = means[0]
    ax.axhline(ref_line, color=DARK_BLUE_HEX, lw=1.5, ls="--", alpha=0.7,
               label=f"Reference mean (Center) = {ref_line}")

    for bar, val, cat in zip(bars, means, categories):
        diff = val - ref_line
        sign = "+" if diff >= 0 else ""
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.5, str(val),
                ha="center", va="bottom", fontsize=9.5, fontweight="bold",
                color=DARK_BLUE_HEX)
        if diff != 0:
            ax.text(bar.get_x() + bar.get_width()/2, ref_line + diff/2,
                    f"β = {sign}{diff}", ha="center", va="center",
                    fontsize=8.5, color="white", fontweight="bold")

    ax.set_ylabel("Mean Y (outcome)", fontsize=9)
    ax.set_title("Dummy Variable Coefficients = Difference from Reference Group",
                 color=DARK_BLUE_HEX, fontsize=10)
    ax.legend(fontsize=8.5, frameon=False)
    ax.set_ylim(0, 70)
    ax.tick_params(labelsize=9)
    fig.tight_layout(pad=1.2)
    return fig

def plot_vif_illustration():
    """Scatter plots: X1 vs X2 for low vs high multicollinearity."""
    rng5 = np.random.default_rng(55)
    x1 = rng5.normal(0, 1, 80)

    # Low collinearity
    x2_low = rng5.normal(0, 1, 80)
    # High collinearity
    x2_high = 0.95*x1 + rng5.normal(0, 0.2, 80)

    fig, axes = plt.subplots(1, 2, figsize=(10, 3.4))
    r_low = np.corrcoef(x1, x2_low)[0, 1]
    r_high = np.corrcoef(x1, x2_high)[0, 1]

    vif_low  = 1 / (1 - r_low**2)
    vif_high = 1 / (1 - r_high**2)

    for ax, x2, r, vif, title_col, label in [
        (axes[0], x2_low,  r_low,  vif_low,  GREEN_HEX,
         f"Low multicollinearity\nr = {r_low:.2f},  VIF ≈ {vif_low:.1f}"),
        (axes[1], x2_high, r_high, vif_high, RED_HEX,
         f"High multicollinearity\nr = {r_high:.2f},  VIF ≈ {vif_high:.0f}"),
    ]:
        ax.scatter(x1, x2, color=MID_BLUE_HEX, s=20, alpha=0.6)
        m, b = np.polyfit(x1, x2, 1)
        ax.plot(np.sort(x1), m*np.sort(x1)+b, color=title_col, lw=2, ls="--")
        ax.set_title(label, color=title_col, fontsize=10)
        ax.set_xlabel("X₁")
        ax.set_ylabel("X₂")

    fig.tight_layout(pad=1.5)
    return fig

def plot_lmsc_chi2():
    """χ²(1) distribution with critical value and reject region."""
    from scipy.stats import chi2
    x = np.linspace(0, 12, 400)
    y = chi2.pdf(x, df=1)

    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.plot(x, y, color=DARK_BLUE_HEX, lw=2.5)
    ax.fill_between(x, y, where=(x >= 3.841), color=ORANGE_HEX, alpha=0.35,
                    label="Reject H₀: LM > 3.841\n(autocorrelation detected)")
    ax.fill_between(x, y, where=(x < 3.841), color=MID_BLUE_HEX, alpha=0.18,
                    label="Fail to reject H₀\n(A3 plausibly satisfied)")
    ax.axvline(3.841, color=ORANGE_HEX, lw=2, ls="--")
    ax.text(3.841 + 0.15, 0.35, "Critical value\n3.841\n(5% level)", fontsize=8.5,
            color=ORANGE_HEX, fontweight="bold")
    ax.set_xlabel("LM statistic  =  n × R²_aux", fontsize=9)
    ax.set_ylabel("χ²(1) density", fontsize=9)
    ax.set_title("LMSC Test: χ²(1) Distribution\nCompare LM statistic to 3.841", color=DARK_BLUE_HEX)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 0.6)
    ax.legend(fontsize=8.5, frameon=False, loc="upper right")
    fig.tight_layout(pad=1.2)
    return fig

# ════════════════════════════════════════════════════════════════════════════
# PDF SETUP
# ════════════════════════════════════════════════════════════════════════════
doc = SimpleDocTemplate(
    "/home/user/BabyPluto/MLR_TimeSeries_ExamGuide.pdf",
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm,
)
W = A4[0] - 4*cm

# Colours
DARK_BLUE   = colors.HexColor(DARK_BLUE_HEX)
MID_BLUE    = colors.HexColor(MID_BLUE_HEX)
LIGHT_BLUE  = colors.HexColor(LIGHT_BLUE_HEX)
ORANGE      = colors.HexColor(ORANGE_HEX)
GREEN       = colors.HexColor(GREEN_HEX)
LIGHT_GREEN = colors.HexColor("#D6F0E0")
YELLOW_BG   = colors.HexColor("#FFF8DC")
RED_BG      = colors.HexColor("#FDE8E8")
GREY_LINE   = colors.HexColor("#CCCCCC")
WHITE       = colors.white
BLACK       = colors.black

def S(name, **kw):
    kw.setdefault("fontName", "DV")
    return ParagraphStyle(name, **kw)

title_style = S("Title", fontSize=21, textColor=WHITE, fontName="DV-B",
                alignment=TA_CENTER, spaceAfter=6, leading=26)
subtitle_style = S("Subtitle", fontSize=11, textColor=LIGHT_BLUE,
                   alignment=TA_CENTER, spaceAfter=4)
part_style = S("Part", fontSize=15, textColor=WHITE, fontName="DV-B",
               spaceAfter=4, leading=19)
h1 = S("H1", fontSize=12, textColor=DARK_BLUE, fontName="DV-B",
       spaceBefore=12, spaceAfter=4, leading=15)
h2 = S("H2", fontSize=10.5, textColor=MID_BLUE, fontName="DV-B",
       spaceBefore=8, spaceAfter=3, leading=13)
body = S("Body", fontSize=9.5, textColor=BLACK, spaceBefore=2, spaceAfter=3,
         leading=14, alignment=TA_JUSTIFY)
code_style = S("Code", fontSize=8.5, fontName="DV-M", spaceBefore=2, spaceAfter=2,
               leading=13, leftIndent=10, textColor=colors.HexColor("#2B2B2B"))

def sp(h=6): return Spacer(1, h)

def banner(text, bg=DARK_BLUE):
    t = Table([[Paragraph(text, part_style)]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0),(-1,-1), bg),
        ("TOPPADDING", (0,0),(-1,-1), 10),
        ("BOTTOMPADDING",(0,0),(-1,-1), 10),
        ("LEFTPADDING",(0,0),(-1,-1), 14),
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
        ("BACKGROUND",(0,0),(-1,-1), bg),
        ("BOX",(0,0),(-1,-1), 0.5, GREY_LINE),
        ("TOPPADDING",(0,0),(-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,-1), 8),
        ("LEFTPADDING",(0,0),(-1,-1), 10),
        ("VALIGN",(0,0),(-1,-1), "TOP"),
    ]))
    return t

def pitfall_box(rows): return info_box(rows, bg=RED_BG, label="⚠  Common Pitfalls")
def tip_box(rows):     return info_box(rows, bg=LIGHT_GREEN, label="✓  Exam Tips")

def formula_box(lines):
    rows = [[Paragraph(l, code_style)] for l in lines]
    t = Table(rows, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), YELLOW_BG),
        ("BOX",(0,0),(-1,-1), 1, MID_BLUE),
        ("TOPPADDING",(0,0),(-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
        ("LEFTPADDING",(0,0),(-1,-1), 10),
    ]))
    return t

def tbl(header, rows, col_widths=None):
    if col_widths is None:
        col_widths = [W/len(header)]*len(header)
    th = S("th", fontSize=9, fontName="DV-B", textColor=WHITE, leading=12)
    td = S("td", fontSize=9, leading=13)
    data = [[Paragraph(h, th) for h in header]]
    for r in rows:
        data.append([Paragraph(str(c), td) for c in r])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0), DARK_BLUE),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, colors.HexColor("#EBF2FA")]),
        ("BOX",(0,0),(-1,-1), 0.5, GREY_LINE),
        ("INNERGRID",(0,0),(-1,-1), 0.3, GREY_LINE),
        ("TOPPADDING",(0,0),(-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
        ("LEFTPADDING",(0,0),(-1,-1), 6),
        ("VALIGN",(0,0),(-1,-1), "TOP"),
    ]))
    return t

def fig_label(text):
    return Paragraph(f"<i>{text}</i>",
                     S("fl", fontSize=8, textColor=colors.HexColor("#555555"),
                       alignment=TA_CENTER, spaceBefore=2, spaceAfter=8))

SPSS_BG = colors.HexColor("#EBF5FB")

def spss_box(steps, title="SPSS Step-by-Step"):
    hdr = S("spss_h", fontSize=9.5, fontName="DV-B", textColor=WHITE, leading=13)
    sty = S("spss_s", fontSize=9, fontName="DV-M", leading=14,
            textColor=colors.HexColor("#1A1A2E"))
    rows = [[Paragraph(f"  ⌨  {title}", hdr)]]
    for i, step in enumerate(steps, 1):
        rows.append([Paragraph(f"  {i}.  {step}", sty)])
    t = Table(rows, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), MID_BLUE),
        ("BACKGROUND", (0,1), (-1,-1), SPSS_BG),
        ("BOX",        (0,0), (-1,-1), 1, MID_BLUE),
        ("INNERGRID",  (0,1), (-1,-1), 0.3, GREY_LINE),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    return t

def pitfall_row(i, title, text):
    bg = RED_BG if i%2==0 else colors.HexColor("#FFF0F0")
    ts = S(f"pt{i}", fontSize=9.5, fontName="DV-B",
           textColor=colors.HexColor("#7B0000"), leading=13)
    row = [[Paragraph(f"{i}. {title}", ts), Paragraph(text, body)]]
    t = Table(row, colWidths=[4.5*cm, W-4.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), bg),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("TOPPADDING",(0,0),(-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("LEFTPADDING",(0,0),(-1,-1), 8),
        ("BOX",(0,0),(-1,-1), 0.3, GREY_LINE),
        ("LINEAFTER",(0,0),(0,-1), 0.5, colors.HexColor("#E0A0A0")),
    ]))
    return t

# ════════════════════════════════════════════════════════════════════════════
# STORY
# ════════════════════════════════════════════════════════════════════════════
story = []

# COVER
cover = Table(
    [[Paragraph("Statistics Exam\nMaster Guide", title_style)],
     [Paragraph("Multiple Linear Regression  &  Time Series", subtitle_style)],
     [Paragraph("How to read questions · Which method to use · Why it works\n"
                "Common pitfalls · Different phrasings · Worked decision logic", subtitle_style)]],
    colWidths=[W])
cover.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1), DARK_BLUE),
    ("TOPPADDING",(0,0),(-1,-1), 28),
    ("BOTTOMPADDING",(0,0),(-1,-1), 18),
    ("LEFTPADDING",(0,0),(-1,-1), 20),
    ("RIGHTPADDING",(0,0),(-1,-1), 20),
]))
story += [sp(40), cover, sp(20)]
story.append(Paragraph(
    "This guide walks you through every type of question in exams on MLR and "
    "Time Series. Each section gives: what the question is really asking, which "
    "method to choose and why, step-by-step decision logic, the correct "
    "interpretation, actual plots to help you recognize patterns, pitfalls that "
    "cost marks, and different phrasings that mean the same thing.", body))
story.append(PageBreak())

# ════ PART 1 — MLR ═══════════════════════════════════════════════════════════
story += [banner("PART 1 — MULTIPLE LINEAR REGRESSION (MLR)"), sp(8)]

# 1.1
story.append(Paragraph("1.1  How to Read an MLR Question", h1))
story.append(Paragraph("Read the question twice and identify these four things before opening SPSS:", body))
story.append(tbl(
    ["Identify", "Appears as", "Action"],
    [
        ["Dependent variable Y", '"Regress X on Y" / "explain Y" / "Y as a function of"', "Dependent box in SPSS"],
        ["Continuous predictor", "Age, income, price — no category labels", "Enter directly as IV"],
        ["Categorical predictor", '"Region", "type" with labels like North/South', "Create k−1 dummy variables"],
        ["Log transformation", '"ln(X)", "log(X)" in the variable name', "Already logged, or Transform → Compute"],
        ["Interaction term", '"effect depends on Z" / "X×Z"', "Create product variable X×Z"],
    ],
    col_widths=[3.5*cm, 7.5*cm, 5.5*cm]))
story.append(sp(8))

# 1.2
story.append(Paragraph("1.2  Dummy Variables", h1))
story.append(Paragraph(
    "A dummy variable converts a categorical variable with k categories into k−1 "
    "binary (0/1) variables. The excluded category is the reference group — "
    "every coefficient is interpreted relative to it.", body))
story.append(tbl(
    ["Categories", "Dummies to create", "Reference (omitted)"],
    [
        ["North, South, Center, East (4)", "D_North, D_South, D_East  (3 dummies)", "Center"],
        ["Male, Female (2)", "D_Female  (1 dummy)", "Male"],
        ["Low, Medium, High (3)", "D_Medium, D_High  (2 dummies)", "Low"],
    ],
    col_widths=[5*cm, 6.5*cm, 5*cm]))
story.append(sp(4))
story.append(formula_box([
    "SPSS: Transform → Compute Variable for each category (except reference):",
    "  D_North = (Region = 1)    [if North is coded 1 in data]",
    "  D_South = (Region = 2)    [skip 3 = Center → it is the reference]",
    "  D_East  = (Region = 4)",
    "",
    "Theoretical model:",
    "  Y = β₀ + β₁X₁ + β₂·D_North + β₃·D_South + β₄·D_East + ε",
    "",
    "Interpretation of β₂:  North regions have β₂ units more Y than Center,",
    "                        holding all other variables constant.",
]))
story.append(sp(6))
story.append(fig_to_image(plot_dummy_bar(), 14))
story.append(fig_label(
    "Figure 1.2 — Each bar shows the mean Y for that region. "
    "The dummy coefficient = the bar's height minus the reference bar (Center). "
    "The reference group has no dummy and its effect is absorbed into the intercept β₀."))
story.append(spss_box([
    "Transform → Compute Variable…",
    "Target Variable: D_North   |   Numeric Expression: (Region = 1)   [use the numeric code for North]",
    "Click OK.  Repeat for each category EXCEPT the reference (e.g. Center).",
    "Analyze → Regression → Linear…",
    "Dependent: Y   |   Independent(s): X1, D_North, D_South, D_East",
    "Click OK.  Read Coefficients table: B column = estimates, Sig. column = p-values.",
], title="SPSS: Creating and Using Dummy Variables"))
story.append(sp(4))
story.append(pitfall_box([
    "Never create k dummies — always k−1. Including all k causes perfect multicollinearity (dummy trap).",
    '"Baseline group", "comparison group", "omitted category", "reference category" — all the same.',
    '"Use Center as reference" means do NOT create a dummy for Center.',
]))
story.append(sp(8))

# 1.3
story.append(Paragraph("1.3  Log Transformations and Interpretation", h1))
story.append(tbl(
    ["Model", "Equation", "β interpretation"],
    [
        ["Linear", "Y = α + βX + ε", "1-unit rise in X → β unit change in Y"],
        ["Linear-log", "Y = α + β·ln(X) + ε", "1% rise in X → β/100 unit change in Y"],
        ["Log-linear", "ln(Y) = α + βX + ε", "1-unit rise in X → β×100 % change in Y"],
        ["Log-log", "ln(Y) = α + β·ln(X) + ε", "1% rise in X → β% change in Y  (elasticity)"],
    ],
    col_widths=[3.2*cm, 5.8*cm, 7.5*cm]))
story.append(sp(6))
story.append(fig_to_image(plot_log_shapes(), 16.5))
story.append(fig_label(
    "Figure 1.3 — Shape of each model type. Linear: straight line. "
    "Linear-log: curved (diminishing returns). Log-linear: exponential. "
    "Log-log: power curve (constant elasticity). "
    "Recognise which shape fits the data to identify the correct model type."))
story.append(sp(4))
story.append(info_box([
    "Most common exam type: Linear-Log.  Y = α + β·ln(X) + ε",
    "Example: β = −16.04, X is ln(NOx).",
    "Answer: 1% increase in NOx → −16.04/100 = −0.16 units of Y.  "
    "If Y is in thousands of dollars: −$160 per 1% rise in pollution.",
], bg=LIGHT_BLUE, label="Most Tested: Linear-Log"))
story.append(sp(4))
story.append(spss_box([
    "If the variable is NOT yet logged: Transform → Compute Variable…",
    "Target Variable: LN_X   |   Numeric Expression: LN(X)   |   Click OK.",
    "If both sides need logging (log-log model): also create LN_Y = LN(Y).",
    "Analyze → Regression → Linear…",
    "Dependent: Y (or LN_Y)   |   Independent(s): LN_X (and other predictors)",
    "Click OK.  Read B column for β — apply the correct interpretation rule from the table above.",
], title="SPSS: Log Transformations"))
story.append(sp(8))

# 1.4
story.append(Paragraph("1.4  Interpreting Coefficients — Decision Table", h1))
story.append(tbl(
    ["X logged?", "Y logged?", "Interpretation of β"],
    [
        ["No", "No", "1 extra unit of X → β extra units of Y  (ceteris paribus)"],
        ["Yes (ln X)", "No", "1% extra in X → β/100 extra units of Y"],
        ["No", "Yes (ln Y)", "1 extra unit of X → β×100 % change in Y"],
        ["Yes (ln X)", "Yes (ln Y)", "1% extra in X → β% change in Y"],
        ["Dummy (0/1)", "No", "Being in group D → β extra units of Y vs. reference"],
    ],
    col_widths=[2.5*cm, 2.5*cm, 11.5*cm]))
story.append(sp(8))

# 1.5
story.append(Paragraph("1.5  Testing Individual Coefficient Significance", h1))
story.append(formula_box([
    "H₀: β = 0   (variable has no effect on Y)",
    "H₁: β ≠ 0   (variable does affect Y)",
    "",
    "Decision:  p-value (Sig. column in SPSS) < 0.05  →  Reject H₀  →  significant at 5%",
    "           p-value ≥ 0.05               →  Fail to reject H₀  →  not significant",
]))
story.append(sp(4))
story.append(spss_box([
    "Analyze → Regression → Linear…",
    "Dependent: Y   |   Independent(s): all predictor variables",
    "Click OK.  Open the Coefficients table in the output.",
    "Find the row for the variable of interest.",
    "Read the Sig. column (= p-value).  If Sig. < 0.05 → significant at 5%.",
    "Also read B (estimate) and t columns to quote in your answer.",
], title="SPSS: Testing Individual Coefficient Significance"))
story.append(sp(4))
story.append(pitfall_box([
    '"Significant" means statistically distinguishable from zero — NOT necessarily large or important.',
    '"Is X relevant?", "Does X matter?", "Test the effect of X", '
    '"Is β significantly different from zero?" — all ask for the t-test p-value.',
]))
story.append(sp(8))

# 1.6
story.append(Paragraph("1.6  Joint F-test — Testing a Group of Variables Together", h1))
story.append(info_box([
    '"Are the region dummies jointly significant?"',
    '"Do the seasonal dummies together improve the model?"',
    '"Test whether D₁, D₂, D₃ together add explanatory power."',
    "Any question testing MORE THAN ONE variable simultaneously.",
], bg=LIGHT_BLUE, label="Use joint F-test when you see these phrases"))
story.append(sp(4))
story.append(tbl(
    ["Step", "What you do", "Why"],
    [
        ["1", "Run UNRESTRICTED model — all variables included", "Gives SSE_u and R²_u"],
        ["2", "Run RESTRICTED model — remove the variables being tested", "Gives SSE_r and R²_r"],
        ["3", "J = number of variables removed", "J = numerator df"],
        ["4", "Read n (obs) and k (predictors in unrestricted model)", "For denominator df"],
        ["5", "Compute F and use p-value", "Decision"],
    ],
    col_widths=[1*cm, 8.5*cm, 7*cm]))
story.append(sp(4))
story.append(formula_box([
    "Option A  (SSE from ANOVA):",
    "  F = [ (SSE_r − SSE_u) / J ]  ÷  [ SSE_u / (n − k − 1) ]",
    "",
    "Option B  (R² from Model Summary):",
    "  F = [ (R²_u − R²_r) / J ]  ÷  [ (1 − R²_u) / (n − k − 1) ]",
    "",
    "Decision:  Use the p-value (Sig.) from the SPSS ANOVA table.",
    "  Alternatively: if your computed F > F-critical value → Reject H₀",
]))
story.append(sp(4))
story.append(spss_box([
    "Run UNRESTRICTED model: Analyze → Regression → Linear…",
    "  Dependent: Y   |   Independent(s): X1, D_North, D_South, D_East  (all variables)",
    "  Click OK.  Record: SSE_u from ANOVA table (Residual row, Sum of Squares column)",
    "  OR record R²_u from Model Summary table.",
    "Run RESTRICTED model: Analyze → Regression → Linear…",
    "  Dependent: Y   |   Independent(s): X1 only  (remove the variables being tested)",
    "  Click OK.  Record: SSE_r (Residual SS) OR R²_r from Model Summary.",
    "Count J = number of variables you removed (e.g. 3 dummies → J = 3).",
    "Compute F manually using the formula above.  Compare p-value to 0.05.",
    "TIP: n = Total df + 1 from the ANOVA table.  k = number of IVs in unrestricted model.",
], title="SPSS: Running the Joint F-test (Restricted vs Unrestricted)"))
story.append(sp(4))
story.append(pitfall_box([
    "J = number of RESTRICTIONS (variables REMOVED), not total variables.",
    "Restricted model has FEWER variables — its SSE is always LARGER.",
    "n−k−1 uses k from the UNRESTRICTED model.",
]))
story.append(sp(8))

# 1.7
story.append(Paragraph("1.7  Residual Plot Analysis", h1))
story.append(Paragraph(
    "After running a regression, always inspect the residual plot "
    "(residuals on Y-axis, fitted values on X-axis). "
    "It reveals three types of violations:", body))
story.append(tbl(
    ["What you see", "Problem", "Assumption violated"],
    [
        ["Random scatter centered on zero", "None — model is fine", "All assumptions hold ✓"],
        ["Fan/cone shape — wider spread on one side", "Heteroskedasticity", "A2: Var(ε) = σ² (constant)"],
        ["Curved arc — residuals curve up then down", "Non-linearity", "A1: model correctly specified"],
        ["One or two extreme isolated points", "Outliers", "Distort estimates — report them"],
    ],
    col_widths=[5.5*cm, 4*cm, 7*cm]))
story.append(sp(6))
story.append(fig_to_image(plot_residual_patterns(), 16.5))
story.append(fig_label(
    "Figure 1.7 — Left: good residual plot — random cloud, no pattern. "
    "Centre: heteroskedasticity — fan shape, variance grows with fitted values. "
    "Right: non-linearity — curved arc, model is missing a term (e.g. X²)."))
story.append(sp(4))
story.append(spss_box([
    "Analyze → Regression → Linear…",
    "Dependent: Y   |   Independent(s): all predictors",
    "Click Plots… button (bottom of dialog).",
    "In the Plots dialog: set Y-axis to ZRESID  (standardized residuals)",
    "  and X-axis to ZPRED  (standardized fitted values).  Click Continue.",
    "Click OK.  The scatter plot appears in the Output Viewer.",
    "Inspect the plot using the three patterns in Figure 1.7 above:",
    "  • Random cloud → good  |  Fan shape → heteroskedasticity  |  Curved arc → non-linearity",
], title="SPSS: Generating the Residual Plot"))
story.append(sp(4))
story.append(pitfall_box([
    "Do not say 'residuals are not normal' from this plot alone. "
    "Normality requires a histogram or Q-Q plot.",
    "Heteroskedasticity → standard errors are wrong → t-tests and p-values are unreliable. "
    "Follow up with the White test.",
    "You do not need to quantify — describe what you SEE and name the assumption violated.",
]))
story.append(sp(8))

# 1.8
story.append(Paragraph("1.8  The White Test for Heteroskedasticity", h1))
story.append(fig_to_image(plot_heteroskedasticity_white(), 15))
story.append(fig_label(
    "Figure 1.8 — Left: homoskedastic — squared residuals (ê²) show no trend with X. "
    "Right: heteroskedastic — ê² rises with X. The White test auxiliary regression "
    "detects this rising pattern and flags it formally."))
story.append(sp(4))
story.append(formula_box([
    "H₀: homoskedasticity  —  Var(ε) = σ²  (constant)",
    "H₁: heteroskedasticity  —  variance is NOT constant",
    "",
    "Step 1:  Run original model. Save residuals ê (Save → Unstandardized Residuals).",
    "Step 2:  Compute ê²  via Transform → Compute:  RES_SQ = RES_1 ** 2",
    "Step 3:  Auxiliary regression:",
    "         ê² = α₀ + (all original X's) + (X² for each continuous X)",
    "                  + (Xᵢ×Xⱼ for each pair of continuous X's) + u",
    "         Do NOT square dummies.  Do NOT include dummy×dummy cross-products.",
    "Step 4:  W = n × R²_aux  ~  χ²(df)",
    "         df = number of regressors in auxiliary regression (excluding constant)",
    "Step 5:  If p < 0.05  →  Reject H₀  →  heteroskedasticity present",
]))
story.append(sp(4))
story.append(spss_box([
    "Run original regression: Analyze → Regression → Linear…  (Y on all X predictors).",
    "Save residuals: click Save… → check Unstandardized (under Residuals) → Continue → OK.",
    "  SPSS creates variable RES_1 in the dataset.",
    "Compute squared residuals: Transform → Compute Variable…",
    "  Target Variable: RES_SQ   |   Expression: RES_1 ** 2   |   Click OK.",
    "Run auxiliary regression: Analyze → Regression → Linear…",
    "  Dependent: RES_SQ",
    "  Independent(s): all original X's  +  X² for each continuous X  +  Xᵢ×Xⱼ cross-products",
    "  (Do NOT square dummies.  Do NOT include dummy×dummy products.)",
    "  Click OK.  Record R²_aux from Model Summary  and  n_aux = Total df + 1 from ANOVA.",
    "Compute: W = n_aux × R²_aux.  df = number of IVs in auxiliary regression.",
    "Decision: if Sig. < 0.05 on the overall F of the auxiliary regression → reject H₀ (heteroskedasticity).",
    "  OR: if W > χ²_critical(df, 5%) → reject H₀.",
], title="SPSS: Running the White Test"))
story.append(sp(4))
story.append(pitfall_box([
    "df is NOT 1. Example: 2 continuous X's → X₁, X₂, X₁², X₂², X₁×X₂ → df = 5.",
    "D² = D for a 0/1 variable — never square dummies.",
    "Always state df explicitly in your answer: W ~ χ²(5).",
]))
story.append(sp(8))

# 1.9
story.append(Paragraph("1.9  Omitted Variable Bias", h1))
story.append(formula_box([
    "sign(bias on β̂_X)  =  sign(β_Z)  ×  sign(r(X, Z))",
    "",
    "β_Z  = true effect of the OMITTED variable Z on Y",
    "r(X,Z) = correlation between INCLUDED X and OMITTED Z",
    "",
    "Bias > 0  →  estimate is TOO HIGH  (upward bias — overestimated)",
    "Bias < 0  →  estimate is TOO LOW   (downward bias — underestimated)",
]))
story.append(sp(6))
story.append(fig_to_image(plot_omitted_variable_bias(), 13))
story.append(fig_label(
    "Figure 1.9 — Sign grid for omitted variable bias. "
    "Top row: direction of β_Z (omitted variable's true effect on Y). "
    "Left column: sign of correlation between included X and omitted Z. "
    "Green = upward bias (estimate too high). Red = downward bias (estimate too low)."))
story.append(sp(4))
story.append(tbl(
    ["β_Z (effect of Z on Y)", "r(X, Z)", "Bias on β̂_X", "Estimate is…"],
    [
        ["Positive (+)", "Positive (+)", "+ → upward bias", "Too high"],
        ["Positive (+)", "Negative (−)", "− → downward bias", "Too low"],
        ["Negative (−)", "Positive (+)", "− → downward bias", "Too low"],
        ["Negative (−)", "Negative (−)", "+ → upward bias", "Too high"],
    ],
    col_widths=[4.5*cm, 3.5*cm, 4*cm, 4.5*cm]))
story.append(sp(4))
story.append(info_box([
    "Example: estimating effect of ln(NOx) on housing values, omitting Indus (industry zone).",
    "β_Indus < 0  (more industry → lower house values).",
    "r(ln(NOx), Indus) > 0  (high-NOx areas also tend to have more industry).",
    "Bias = (−) × (+) = negative → estimate of β_lnNOx is TOO LOW (overestimates the negative effect).",
], bg=LIGHT_BLUE, label="Worked Example"))
story.append(sp(8))

# 1.10
story.append(Paragraph("1.10  VIF and Multicollinearity", h1))
story.append(formula_box([
    "VIF_j  =  1 / (1 − R²_j)          Tolerance_j  =  1 / VIF_j",
    "",
    "R²_j = R² from regressing X_j on all other X's  (auxiliary regression)",
    "",
    "Threshold:  VIF > 5  →  concerning     VIF > 10  →  severe",
]))
story.append(sp(6))
story.append(fig_to_image(plot_vif_illustration(), 14))
story.append(fig_label(
    "Figure 1.10 — Left: low multicollinearity — X₁ and X₂ are uncorrelated, VIF ≈ 1. "
    "Right: high multicollinearity — X₁ and X₂ are nearly identical (r ≈ 0.95), "
    "VIF is very large. When predictors are this correlated, SPSS cannot reliably "
    "separate their individual effects — coefficients and standard errors become unstable."))
story.append(sp(4))
story.append(tbl(
    ["VIF", "Tolerance", "Interpretation"],
    [
        ["1.0", "1.00", "No multicollinearity — X uncorrelated with all others"],
        ["1 to 5", "0.20 to 1.00", "Acceptable — moderate correlation, no real problem"],
        ["5 to 10", "0.10 to 0.20", "Concerning — inspect estimates carefully"],
        ["> 10", "< 0.10", "Severe — estimates are unreliable"],
    ],
    col_widths=[2.5*cm, 3.5*cm, 10.5*cm]))
story.append(sp(4))
story.append(spss_box([
    "Analyze → Regression → Linear…",
    "Dependent: Y   |   Independent(s): all predictor variables",
    "Click Statistics… button.",
    "Check Collinearity diagnostics.  Click Continue.",
    "Click OK.  In the Coefficients table, scroll right to find:",
    "  Tolerance column: should be close to 1.0 (low multicollinearity)",
    "  VIF column: flag any value above 5 as concerning, above 10 as severe.",
], title="SPSS: Getting VIF and Tolerance"))
story.append(sp(8))

# 1.11
story.append(KeepTogether([
    Paragraph("1.11  Quick Reference — Phrasing → Method", h1),
    tbl(
        ["If the question says…", "It means…", "Method"],
        [
            ['"Interpret the coefficient of ln(X)"', "Effect of 1% change in X", "β/100 units change in Y"],
            ['"Test if Region is significant"', "All dummies jointly", "Joint F-test"],
            ['"Is β₂ significantly different from zero?"', "Individual significance", "p-value from Coefficients table"],
            ['"Test for heteroskedasticity"', "Unequal error variance", "White test: W = n × R²_aux"],
            ['"What is the bias if Z is omitted?"', "Direction of bias", "sign(β_Z) × sign(r(X, Z))"],
            ['"VIF = 2.5 — what does this mean?"', "Multicollinearity severity", "Compare to threshold of 5"],
            ['"Write the theoretical model"', "Full symbolic equation", "Y = β₀ + β₁X₁ + β₂D₁ + …"],
        ],
        col_widths=[5.5*cm, 4.5*cm, 6.5*cm]),
]))
story.append(PageBreak())

# ════ PART 2 — TIME SERIES ════════════════════════════════════════════════════
story += [banner("PART 2 — TIME SERIES REGRESSION"), sp(8)]

# 2.1
story.append(Paragraph("2.1  The Three-Step Framework — Always in This Order", h1))
story.append(info_box([
    "STEP 1 — STATIONARITY: Dickey-Fuller test on every variable. "
    "Non-stationary series must be differenced before use.",
    "STEP 2 — FIT THE MODEL: Static, DL(q), or AR(1) depending on the question. "
    "For DL(q) use top-down lag selection.",
    "STEP 3 — CHECK AUTOCORRELATION: LMSC test on model residuals.",
], bg=LIGHT_BLUE, label="The Three-Step Framework — never skip or reorder"))
story.append(sp(8))

# 2.2
story.append(Paragraph("2.2  Step 1 — Stationarity and the Dickey-Fuller Test", h1))
story.append(Paragraph(
    "Before running any time series regression you must confirm that every variable "
    "is stationary. The three plots below show what stationary and non-stationary "
    "series look like in a time plot — this is how you choose the DF version.", body))
story.append(sp(4))
story.append(fig_to_image(plot_time_series_stationarity(), 16.5))
story.append(fig_label(
    "Figure 2.2a — Left (green): stationary series — fluctuates around a constant mean. "
    "Centre (blue): deterministic trend — drifts upward predictably, returns to trend after shocks "
    "(fix: add t as regressor). "
    "Right (red): random walk / unit root — wanders unpredictably, variance grows "
    "(fix: take first differences ΔY)."))
story.append(sp(6))
story.append(tbl(
    ["DF Version", "Regression run", "When to use"],
    [
        ["Version 1 — no trend", "ΔY_t = α₀ + α₁Y_{t−1} + ε_t",
         "Time plot shows NO visible upward or downward trend"],
        ["Version 2 — with trend", "ΔY_t = α₀ + λt + α₁Y_{t−1} + ε_t",
         "Clear trend in time plot  OR  when unsure  (safer default)"],
    ],
    col_widths=[3.5*cm, 6.5*cm, 6.5*cm]))
story.append(sp(4))
story.append(formula_box([
    "H₀: α₁ = 0   (unit root — series is NON-STATIONARY)",
    "H₁: α₁ < 0   (series IS stationary)     ← one-sided test",
    "",
    "Special critical values at 5%  —  NEVER use ±1.96 here:",
    "  Version 1  (no trend):    −2.86",
    "  Version 2  (with trend):  −3.41",
    "",
    "Decision:  t on Y_{t−1} MORE negative than CV  →  Reject H₀  →  STATIONARY",
    "           t on Y_{t−1} LESS negative (closer to 0)  →  Fail to reject  →  UNIT ROOT",
]))
story.append(sp(6))
story.append(fig_to_image(plot_df_decision(), 16))
story.append(fig_label(
    "Figure 2.2b — DF decision number line. "
    "The shaded green region is the rejection zone (t more negative than the critical value). "
    "t = −4.50 falls in the rejection zone → stationary. "
    "t = −1.60 does not → unit root, must take first differences."))
story.append(sp(4))
story.append(tbl(
    ["DF result", "Action", "Next step"],
    [
        ["Stationary (reject H₀)", "Use series in levels", "Proceed to model"],
        ["Non-stationary (fail to reject)", "Take ΔY = Y_t − Y_{t−1}", "Run DF again on ΔY"],
        ["ΔY is stationary (reject H₀)", "Series is I(1) — use first differences", "Proceed to model"],
        ["ΔY still non-stationary", "Rare — take second differences", "Series may be I(2)"],
    ],
    col_widths=[4.5*cm, 5*cm, 7*cm]))
story.append(sp(4))
story.append(spss_box([
    "CREATE FIRST DIFFERENCE:  Transform → Compute Variable…",
    "  Target Variable: DIFF_Y   |   Expression: Y - LAG(Y, 1)   |   Click OK.",
    "CREATE LAGGED LEVEL:  Transform → Compute Variable…",
    "  Target Variable: LAG_Y    |   Expression: LAG(Y, 1)        |   Click OK.",
    "RUN DF REGRESSION (Version 1 — no trend):",
    "  Analyze → Regression → Linear…",
    "  Dependent: DIFF_Y   |   Independent(s): LAG_Y",
    "  Click OK.",
    "RUN DF REGRESSION (Version 2 — with trend):",
    "  Same as above but ALSO add your time variable (e.g. TIME or t) to Independent(s).",
    "READ OUTPUT: Coefficients table → find row for LAG_Y → read the t column.",
    "  IGNORE the Sig. column!  Compare t directly to −2.86 (V1) or −3.41 (V2).",
    "  t more negative than CV → Reject H₀ → STATIONARY.",
    "  t less negative (closer to 0) → Fail to reject → UNIT ROOT → difference the series.",
    "IF UNIT ROOT: repeat steps 1–12 using DIFF_Y instead of Y (test the first difference).",
], title="SPSS: Dickey-Fuller Test (Step 1 — Stationarity)"))
story.append(sp(4))
story.append(pitfall_box([
    "NEVER use the standard t-table (±1.96) for DF. Always use −2.86 (V1) or −3.41 (V2).",
    "The Sig. (p-value) SPSS shows for the LAG variable uses the wrong distribution — ignore it.",
    "Rejecting H₀ in DF means STATIONARY — opposite of most other tests.",
    "DF is one-sided: only reject when t is sufficiently NEGATIVE.",
]))
story.append(sp(8))

# 2.3
story.append(Paragraph("2.3  Step 2 — Which Model to Fit?", h1))
story.append(tbl(
    ["Model", "Equation", "When to use"],
    [
        ["Static", "Y_t = α + βX_t + ε_t",
         "Question specifies it, or DL top-down gives q = 0"],
        ["DL(q) — Distributed Lag",
         "Y_t = α + β₀X_t + β₁X_{t−1} + … + βqX_{t−q} + ε_t",
         "Question asks for DL; delayed effects expected"],
        ["AR(1) — Autoregressive",
         "Y_t = α + βX_t + γY_{t−1} + ε_t",
         "Question specifies AR(1); or persistent autocorrelation in DL"],
    ],
    col_widths=[2.5*cm, 7*cm, 7*cm]))
story.append(sp(8))

# 2.4
story.append(Paragraph("2.4  DL(q) — Top-Down Lag Selection", h1))
story.append(formula_box([
    "Create lag variables in SPSS: Transform → Compute Variable",
    "  LAG1_X = LAG(X, 1)    LAG2_X = LAG(X, 2)    LAG3_X = LAG(X, 3)",
    "",
    "Top-down rule:",
    "  1. Fit DL(q_max). Look at p-value of the HIGHEST lag.",
    "  2. If p > 0.05: not significant → drop it → fit DL(q−1).",
    "  3. If p ≤ 0.05: significant → STOP. Current q is optimal.",
    "  4. Repeat until highest remaining lag is significant.",
    "",
    "NEVER drop an intermediate lag: if lag 2 is significant,",
    "keep lag 1 even if lag 1 is not significant — structure must be contiguous.",
    "",
    "Total multiplier = β₀ + β₁ + β₂ + … + βq   (long-run effect of permanent +1 in X)",
    "Immediate effect  = β₀ only",
]))
story.append(sp(6))
story.append(fig_to_image(plot_dl_multipliers(), 16))
story.append(fig_label(
    "Figure 2.4 — Left: DL(3) coefficients. Each bar is the effect of X on Y at that lag. "
    "Right: cumulative multiplier — how the total effect builds up over time. "
    "The dashed line is the total multiplier (sum of all β coefficients). "
    "The lag-0 bar alone is the immediate effect; the total multiplier captures all delayed effects."))
story.append(sp(4))
story.append(spss_box([
    "CREATE LAG VARIABLES (example for q_max = 3):",
    "  Transform → Compute Variable…  Target: LAG1_X  Expression: LAG(X, 1)  OK",
    "  Transform → Compute Variable…  Target: LAG2_X  Expression: LAG(X, 2)  OK",
    "  Transform → Compute Variable…  Target: LAG3_X  Expression: LAG(X, 3)  OK",
    "FIT DL(3) — Analyze → Regression → Linear…",
    "  Dependent: Y   |   Independent(s): X, LAG1_X, LAG2_X, LAG3_X   |   Click OK.",
    "  Check Coefficients table: look at Sig. for LAG3_X (highest lag).",
    "  If Sig. > 0.05 → LAG3_X not significant → drop it → fit DL(2).",
    "FIT DL(2) — repeat with Independent(s): X, LAG1_X, LAG2_X.",
    "  If Sig. of LAG2_X > 0.05 → drop → fit DL(1).",
    "FIT DL(1) — repeat with: X, LAG1_X.",
    "  If Sig. of LAG1_X > 0.05 → drop → fit DL(0) (static model with X only).",
    "STOP when the highest remaining lag is significant (Sig. ≤ 0.05).",
    "TOTAL MULTIPLIER: sum all B values (X + LAG1_X + … + LAGq_X) from the final model.",
], title="SPSS: DL(q) Top-Down Lag Selection (Step 2 — Model Fitting)"))
story.append(sp(4))
story.append(pitfall_box([
    "q_max is usually given in the question. Common default is 3 or 4.",
    "Each lag costs one observation. DL(3) with n = 100 gives 97 usable rows.",
    "Total multiplier ≠ β₀. β₀ alone is the immediate effect only.",
]))
story.append(sp(8))

# 2.5
story.append(Paragraph("2.5  AR(1) — Autoregressive Model", h1))
story.append(formula_box([
    "Model:  Y_t = α + βX_t + γY_{t−1} + ε_t",
    "",
    "β  = immediate effect: 1-unit rise in X_t changes Y_t by β, holding Y_{t−1} fixed",
    "γ  = persistence: fraction of last period's Y that carries forward  (requires |γ| < 1)",
    "",
    "Total multiplier  =  β / (1 − γ)     (long-run effect of permanent +1 in X)",
    "",
    "Example:  β = 1.0,  γ = 0.65  →  Total multiplier = 1.0 / (1 − 0.65) = 2.86",
]))
story.append(sp(6))
story.append(fig_to_image(plot_ar1_impulse(), 15))
story.append(fig_label(
    "Figure 2.5 — AR(1) impulse response: what happens to Y in each period after "
    "a one-time shock of 1 unit in X_t. The immediate effect is β = 1.0. "
    "Each subsequent period, the effect is multiplied by γ = 0.65 — it decays geometrically. "
    "The sum of all bars equals the total multiplier β/(1−γ) = 2.86."))
story.append(sp(4))
story.append(spss_box([
    "CREATE LAGGED Y:  Transform → Compute Variable…",
    "  Target Variable: LAG_Y   |   Expression: LAG(Y, 1)   |   Click OK.",
    "Analyze → Regression → Linear…",
    "  Dependent: Y   |   Independent(s): X  and  LAG_Y",
    "  Click OK.",
    "Read Coefficients table:",
    "  B for X     = β  (immediate effect of a 1-unit rise in X this period)",
    "  B for LAG_Y = γ  (persistence — must be between −1 and +1)",
    "Compute total multiplier manually: β / (1 − γ)",
    "  Example: β = 1.5, γ = 0.6  →  total multiplier = 1.5 / (1 − 0.6) = 3.75",
    "Then run the LMSC test (Section 2.6) on these residuals — autocorrelation biases AR(1) estimates.",
], title="SPSS: Fitting the AR(1) Model"))
story.append(sp(4))
story.append(pitfall_box([
    "AR(1) with remaining autocorrelation → coefficient estimates are BIASED. "
    "DL with autocorrelation → only INEFFICIENT (SE wrong, β correct). "
    "This is why always run LMSC after fitting AR(1).",
    "|γ| must be < 1 for validity. If |γ| ≥ 1 the series is non-stationary.",
    '"Persistence coefficient", "AR coefficient on lagged Y", "coefficient on Y_{t−1}" — all = γ.',
]))
story.append(sp(8))

# 2.6
story.append(Paragraph("2.6  Step 3 — LMSC Autocorrelation Test", h1))
story.append(Paragraph(
    "Autocorrelation means the model's error in one period is correlated with the "
    "error in the previous period. This violates Assumption A3 and makes standard "
    "errors wrong. The plots below show what autocorrelated residuals look like "
    "compared to residuals with no autocorrelation.", body))
story.append(sp(4))
story.append(fig_to_image(plot_autocorrelation_residuals(), 16))
story.append(fig_label(
    "Figure 2.6a — Left: no autocorrelation — residuals jump randomly above and below zero. "
    "Right: positive autocorrelation — residuals form long smooth runs above zero, "
    "then long runs below zero. This is the pattern the LMSC test detects. "
    "If you see this in your residuals, A3 is violated."))
story.append(sp(6))
story.append(fig_to_image(plot_lmsc_chi2(), 13))
story.append(fig_label(
    "Figure 2.6b — χ²(1) distribution for the LMSC test. "
    "The orange shaded region is the rejection zone (LM > 3.841). "
    "If your LM statistic falls in the orange zone, reject H₀ — autocorrelation is present."))
story.append(sp(4))
story.append(formula_box([
    "H₀: ρ = 0   (no autocorrelation — A3 satisfied)",
    "H₁: ρ ≠ 0   (autocorrelation present — A3 violated)",
    "",
    "Step 1:  Fit original model. Save residuals: Save → Unstandardized Residuals → RES_1",
    "Step 2:  Create lagged residual: Transform → Compute → LAG_RES1 = LAG(RES_1, 1)",
    "Step 3:  Auxiliary regression:  Dependent = RES_1",
    "                                 Independent = ALL original X's  +  LAG_RES1",
    "Step 4:  n_aux = Total df + 1  (from ANOVA table of auxiliary regression)",
    "         LM = n_aux × R²_aux   ~   χ²(1)   under H₀",
    "Step 5:  If p < 0.05  (or LM > 3.841)  →  Reject H₀  →  autocorrelation present",
    "         If p ≥ 0.05  (or LM ≤ 3.841)  →  Fail to reject  →  A3 plausibly satisfied",
]))
story.append(sp(4))
story.append(spss_box([
    "SAVE RESIDUALS from your original model:",
    "  Analyze → Regression → Linear…  (run your fitted model)",
    "  Click Save… → check Unstandardized under Residuals → Continue → OK.",
    "  SPSS creates variable RES_1 in the dataset.",
    "CREATE LAGGED RESIDUAL:  Transform → Compute Variable…",
    "  Target Variable: LAG_RES1   |   Expression: LAG(RES_1, 1)   |   Click OK.",
    "RUN AUXILIARY REGRESSION:  Analyze → Regression → Linear…",
    "  Dependent: RES_1",
    "  Independent(s): ALL original X variables  +  LAG_RES1",
    "  (e.g. if original model had X and LAG1_X: use X, LAG1_X, LAG_RES1 as IVs)",
    "  Click OK.",
    "READ FROM OUTPUT:",
    "  Model Summary: record R²_aux",
    "  ANOVA table: n_aux = Total df + 1  (the Total row, df column, add 1)",
    "COMPUTE: LM = n_aux × R²_aux",
    "DECISION: if LM > 3.841  OR  overall model Sig. < 0.05 → Reject H₀ → autocorrelation present.",
    "  Otherwise: Fail to reject H₀ → A3 plausibly satisfied.",
], title="SPSS: LMSC Autocorrelation Test (Step 3 — Residual Check)"))
story.append(sp(4))
story.append(pitfall_box([
    "The auxiliary regression MUST include ALL original X predictors + lagged residual.",
    "Durbin-Watson (DW) is INVALID when Y_{t−1} appears as a regressor. Always use LMSC.",
    '"Test for autocorrelation", "check A3", "Breusch-Godfrey test", "LMSC" — all the same.',
]))
story.append(sp(8))

# 2.7
story.append(Paragraph("2.7  Critical Pitfall: Rejecting H₀ Means Opposite Things!", h1))
story.append(tbl(
    ["Test", "H₀ means…", "Reject H₀ means…", "Fail to reject means…"],
    [
        ["Dickey-Fuller", "Series HAS unit root (non-stationary)",
         "Series IS stationary ✓", "Non-stationary — difference it"],
        ["LMSC", "NO autocorrelation (A3 OK)",
         "Autocorrelation present — fix model", "A3 plausibly satisfied ✓"],
        ["t-test", "β = 0 (no effect)", "Variable is significant", "Cannot conclude variable matters"],
        ["Joint F-test", "All β = 0 (group no effect)", "Group jointly significant", "Group not significant"],
        ["White test", "Homoskedasticity (A2 OK)", "Heteroskedasticity — A2 violated", "A2 plausibly satisfied ✓"],
    ],
    col_widths=[3*cm, 4*cm, 4.5*cm, 5*cm]))
story.append(sp(8))

# 2.8
story.append(Paragraph("2.8  Deterministic vs. Stochastic Trends — Different Fix!", h1))
story.append(fig_to_image(plot_det_vs_stoch(), 16))
story.append(fig_label(
    "Figure 2.8 — Left (blue): deterministic trend — the series drifts upward predictably "
    "along the dashed trend line. After a shock it returns to the trend (green arrows). "
    "Fix: add t as a regressor. "
    "Right (red): stochastic trend / random walk — the series wanders erratically, "
    "never returning to a fixed level. Variance grows over time. "
    "Fix: take first differences ΔY. Applying the wrong fix makes things worse."))
story.append(sp(4))
story.append(tbl(
    ["Feature", "Deterministic trend", "Stochastic / Random walk"],
    [
        ["Cause", "λt term (mean grows linearly)", "ρ = 1 (shocks are permanent)"],
        ["Variance", "Constant", "Grows without bound"],
        ["After a shock", "Returns to trend", "Never recovers"],
        ["Correct fix", "Add t as regressor", "Take first differences ΔY"],
        ["Wrong fix → consequence",
         "First-differencing → artificial negative autocorrelation",
         "Detrending does not remove a random walk"],
    ],
    col_widths=[3.5*cm, 6*cm, 7*cm]))
story.append(sp(8))

# 2.9 phrasings
story.append(Paragraph("2.9  Time Series — Question Phrasings Reference", h1))
story.append(tbl(
    ["If the question says…", "It means…", "Method"],
    [
        ['"Is the series stationary?"', "Does it have a unit root?", "Dickey-Fuller test"],
        ['"Test for a unit root"', "Is ρ = 1?", "Dickey-Fuller test"],
        ['"Levels or differences?"', "Stationarity property?", "Run DF, then decide"],
        ['"Determine optimal lag length"', "Best q for DL(q)?", "Top-down procedure"],
        ['"Long-run effect of X on Y"', "Total multiplier", "DL: Σβk  |  AR: β/(1−γ)"],
        ['"Immediate effect of X on Y"', "Impact multiplier", "β₀ only"],
        ['"Test for autocorrelation"', "Is A3 violated?", "LMSC: LM = n × R²_aux"],
        ['"Is the model well-specified?"', "Check all assumptions", "LMSC + residual plot"],
        ['"Series is I(1)"', "Unit root in levels, stationary in differences", "Use first differences"],
        ['"Spurious regression risk"', "Non-stationary series in levels", "Run DF first"],
        ['"Disturbance carries memory"', "Autocorrelation present", "LMSC test"],
    ],
    col_widths=[5.5*cm, 4.5*cm, 6.5*cm]))
story.append(sp(8))

# 2.10 SPSS workflow
story.append(KeepTogether([
    Paragraph("2.10  Full SPSS Workflow", h1),
    tbl(
        ["Step", "SPSS action", "Record"],
        [
            ["1a. Plot", "Graphs → Chart Builder → Line → drag Y and TIME to axes",
             "Does it trend? Wander?"],
            ["1b. DF on levels",
             "Compute DIFF_Y = Y − LAG(Y,1) and LAG_Y = LAG(Y,1).\n"
             "Regression: DV=DIFF_Y, IV=LAG_Y [+ TIME for V2]",
             "t on LAG_Y vs −2.86/−3.41"],
            ["1c. DF on differences",
             "Compute DIFF2_Y = DIFF_Y − LAG(DIFF_Y,1) and LAG_DY = LAG(DIFF_Y,1).\n"
             "Regression: DV=DIFF2_Y, IV=LAG_DY [+ TIME]",
             "t on LAG_DY vs −2.86/−3.41"],
            ["2a. Lag variables", "Transform → Compute: LAG1_X = LAG(X,1), LAG2_X = LAG(X,2)…",
             "Obs lost = q"],
            ["2b. Fit model", "Regression with chosen variables", "All β, R², n"],
            ["3a. Save residuals", "Regression → Save → Unstandardized Residuals", "RES_1 created"],
            ["3b. Lag residual", "Transform → Compute: LAG_RES1 = LAG(RES_1, 1)", "LAG_RES1 created"],
            ["3c. Auxiliary reg.", "Regression: DV=RES_1, IV=all original X's + LAG_RES1",
             "R² and n from output"],
            ["3d. LMSC", "LM = n_aux × R²_aux.  n_aux = Total df + 1 from ANOVA",
             "Compare to 3.841"],
        ],
        col_widths=[2.2*cm, 9*cm, 5.3*cm]),
]))
story.append(PageBreak())

# ════ PART 3 — PITFALLS ══════════════════════════════════════════════════════
story += [banner("PART 3 — MASTER PITFALL & TRICK PHRASING LIST", bg=ORANGE), sp(8)]

story.append(Paragraph("3.1  The Top 15 Mistakes — and How to Avoid Them", h1))
pitfalls = [
    ("Using p-value for DF test",
     "SPSS's Sig. for the LAG variable uses the wrong distribution. "
     "Always compare the t-statistic directly to −2.86 (V1) or −3.41 (V2)."),
    ("Reject H₀ in DF = non-stationary",
     "OPPOSITE: rejecting H₀ in the DF test means the series IS stationary. "
     "H₀ is the unit root (non-stationarity)."),
    ("Creating k dummies instead of k−1",
     "For k categories, create k−1 dummies. Including all k causes the dummy trap "
     "(perfect multicollinearity). Always omit one reference category."),
    ("Using standard t-table for DF",
     "The DF t-statistic does not follow a standard t-distribution. "
     "±1.96 does not apply. Use −2.86 or −3.41 only."),
    ("Missing X's in LMSC auxiliary regression",
     "The auxiliary regression regresses residuals on ALL original X's PLUS the "
     "lagged residual. Missing any original X gives the wrong R² and wrong LM."),
    ("Total multiplier = β₀ only",
     "DL(q): total multiplier = β₀ + β₁ + … + βq  (ALL lag coefficients summed). "
     "AR(1): total multiplier = β/(1−γ). β₀ alone is only the immediate effect."),
    ("Using DW for AR(1) models",
     "Durbin-Watson is INVALID when Y_{t−1} appears as a regressor. Always use LMSC."),
    ("Differencing when trend is deterministic",
     "Only difference when DF confirms a unit root. If trend is deterministic "
     "(|ρ|<1, λ≠0), add t as regressor instead. Wrong fix creates artificial autocorrelation."),
    ("Dropping intermediate insignificant lags",
     "Top-down: only drop the HIGHEST lag while insignificant. "
     "Never drop lag 1 while keeping lag 2 — lag structure must be contiguous."),
    ("Squaring dummies in the White test",
     "D² = D for a 0/1 variable — squaring adds nothing. "
     "Only square continuous variables. Exclude dummy×dummy cross-products."),
    ("Confusing significant with large",
     "A coefficient can be statistically significant (p < 0.05) but economically negligible. "
     "Always comment on both significance AND the size/direction of the effect."),
    ("Wrong sign for omitted variable bias",
     "Bias = sign(β_Z) × sign(r(X,Z)). "
     "Two negatives = positive bias. Use the sign grid if in doubt."),
    ("Ignoring reference category in interpretation",
     'Coefficient on D_North means "compared to the reference group". '
     "Always state the reference category explicitly."),
    ("Using levels when both series are I(1)",
     "If both Y and X have unit roots, always use first differences "
     "(unless cointegration is established — rare at introductory level)."),
    ("Wrong n in LM formula",
     "The auxiliary regression loses one observation for the lagged residual. "
     "Use n_aux = Total df + 1 from the ANOVA table (not the original n)."),
]
for i, (title, text) in enumerate(pitfalls, 1):
    story.append(pitfall_row(i, title, text))
    story.append(sp(3))

story.append(sp(8))
story.append(Paragraph("3.2  Trick Phrasings — Same Question, Different Words", h1))
story.append(tbl(
    ["What the question writes", "What it actually means"],
    [
        ['"Is X relevant to explaining Y?"', '"Is β_X significantly different from zero?"  →  p-value test'],
        ['"Does adding Region improve the model?"', '"Are the region dummies jointly significant?"  →  joint F-test'],
        ['"Baseline group" / "comparison group"', '"Reference category" — the omitted dummy group'],
        ['"The disturbance carries memory"', '"Autocorrelation is present"  →  LMSC test'],
        ['"Series wanders without returning"', '"Series has a unit root"  →  DF test, then difference'],
        ['"Spurious correlation risk"', '"Series is non-stationary"  →  run DF before modelling'],
        ['"Long-run equilibrium effect"', '"Total multiplier"  →  Σβk  or  β/(1−γ)'],
        ['"Impact effect of a price shock"', '"Immediate effect"  →  β₀ only'],
        ['"Error variance is not constant"', '"Heteroskedasticity"  →  White test'],
        ['"Predictors are too correlated"', '"Multicollinearity"  →  VIF and Tolerance'],
        ['"Coefficient on lagged Y is 0.7"', '"γ = 0.7 in AR(1)"  →  total multiplier = β/(1−0.7)'],
        ['"Series is integrated of order one"', '"I(1) — unit root in levels, stationary in differences"'],
        ['"Misspecification bias"', '"Omitted variable bias"  →  sign(β_Z) × sign(r(X,Z))'],
        ['"First-order autocorrelation"', '"ε_t = ρε_{t−1} + u_t"  →  run LMSC test'],
    ],
    col_widths=[7.5*cm, 9*cm]))
story.append(sp(8))

# Quick decision guide
story += [banner("QUICK DECISION GUIDE", bg=GREEN), sp(8)]
story.append(Paragraph("MLR — Method Selector", h1))
story.append(tbl(
    ["Question type", "Method", "Key formula / output"],
    [
        ["Interpret coeff. of ln(X)", "Linear-log rule", "β/100 units per 1% rise in X"],
        ["Test one coefficient", "Individual t-test", "p-value (Sig.) in Coefficients table"],
        ["Test a group of variables", "Joint F-test", "F = [(SSE_r−SSE_u)/J] / [SSE_u/(n−k−1)]"],
        ["Check equal error variance", "White test", "W = n×R²_aux  ~  χ²(df)"],
        ["Direction of missing-variable distortion", "Omitted variable bias", "sign(β_Z)×sign(r(X,Z))"],
        ["Predictor correlation severity", "VIF / Tolerance", "VIF=1/(1−R²_aux), threshold=5"],
        ["Write equation with categories", "Dummy variables", "k−1 dummies, state reference"],
    ],
    col_widths=[5*cm, 4*cm, 7.5*cm]))
story.append(sp(8))
story.append(Paragraph("Time Series — Method Selector", h1))
story.append(tbl(
    ["Question type", "Method", "Key output / decision"],
    [
        ["Is series stationary?", "Dickey-Fuller test", "t < −2.86 (V1) or −3.41 (V2)  →  stationary"],
        ["Series drifts with time", "DF test → unit root?", "Unit root → difference. Deterministic → add t"],
        ["Choose number of lags", "Top-down DL", "Drop highest lag while p > 0.05"],
        ["Long-run effect of X on Y", "Total multiplier", "DL: Σβk        AR: β/(1−γ)"],
        ["Immediate effect of X on Y", "Impact multiplier", "β₀ only"],
        ["Check for autocorrelation", "LMSC test", "LM = n×R²_aux. Compare to 3.841"],
        ["Model contains Y_{t−1}", "Use LMSC, not DW", "DW invalid for AR models"],
    ],
    col_widths=[5*cm, 4*cm, 7.5*cm]))
story.append(sp(10))
story.append(tip_box([
    "Always state H₀ and H₁ before every test.",
    "Always write a full conclusion sentence: 'Since p = X < 0.05, we reject H₀ and conclude…'",
    "For DF: compare t-statistic (NOT p-value) to −2.86 or −3.41.",
    "For LMSC and White test: use p-value directly (standard χ² distribution applies).",
    "For individual t-tests and F-tests: use p-value from SPSS output.",
    "When unsure about stationarity: always use DF Version 2 (safer default).",
    "Total multiplier = LONG-RUN effect of a PERMANENT change in X.",
]))

doc.build(story)
print("PDF created successfully.")
