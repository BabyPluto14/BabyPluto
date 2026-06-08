import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np
import os

OUT = "/home/user/BabyPluto/diagrams"
os.makedirs(OUT, exist_ok=True)

STYLE = {
    "font.family": "serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 1.4,
    "font.size": 12,
}
plt.rcParams.update(STYLE)

def arrow(ax, x0, y0, x1, y1, color="black", lw=1.5):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw))

def finish(ax, xlabel, ylabel, title, fname):
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([]); ax.set_yticks([])
    plt.tight_layout()
    plt.savefig(f"{OUT}/{fname}", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved {fname}")

# ── 1.1 / 1.2 / 1.6.2 / 1.7  AD-AS diagram ──────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 6))

# LRAS curves
ax.axvline(x=6.2, color="#1f77b4", lw=2, ls="--", label="LRAS₀ (Time 0)")
ax.axvline(x=4.5, color="#d62728", lw=2, ls="--", label="LRAS₁ / LRAS₂ (Time 1+)")

# SRAS curves
x = np.linspace(0.5, 9.5, 200)
# SRAS₀
sras0 = 0.6 * x + 1.0
ax.plot(x, sras0, color="#1f77b4", lw=2, label="SRAS₀ (Time 0)")
# SRAS₁ (supply shock shifts left)
sras1 = 0.6 * x + 3.2
ax.plot(x, sras1, color="#d62728", lw=2, label="SRAS₁ (Time 1)")
# SRAS₂ (long-run adj., shifts further left — Time 3 label on same curve for clarity)
sras2 = 0.6 * x + 5.0
ax.plot(x, sras2, color="#9467bd", lw=2, ls=(0,(5,3)), label="SRAS₂ (Time 3)")

# AD curves
ad0 = -0.6 * x + 9.5
ax.plot(x, ad0, color="#1f77b4", lw=2, ls="-.", label="AD₀ (Time 0)")
ad2 = -0.6 * x + 11.5   # government stimulus shifts AD right
ax.plot(x, ad2, color="#2ca02c", lw=2, ls="-.", label="AD₂ (Time 2)")

# ── Equilibrium points ─────────────────────────────────────────────────────
# Time 0: LRAS₀ x=6.2, AD₀ at x=6.2 → y = -0.6*6.2+9.5 = 5.78; sras0 at x=6.2 → 0.6*6.2+1=4.72 → intersection SRAS₀ & AD₀
# Actual crossing SRAS₀ & AD₀: 0.6x+1 = -0.6x+9.5 → 1.2x=8.5 → x=7.08; y=5.25
x0_eq, y0_eq = 7.08, 5.25   # but we place it at LRAS₀ for LR-eq
# For long-run eq at LRAS₀=6.2 we need AD₀ to pass through (6.2, sras0(6.2)):
# Let's just mark the intersections visually
# Time 0 LR eq: LRAS₀ & AD₀: y_AD0(6.2)=-0.6*6.2+9.5=5.78; we say equilibrium=(6.2,5.78)
p0, y0 = 5.78, 6.2
ax.plot(y0, p0, 'o', color="#1f77b4", ms=9, zorder=5)
ax.text(y0+0.1, p0+0.2, "Time 0\n(P₀, Y*)", color="#1f77b4", fontsize=10)

# Time 1 SR eq: SRAS₁ & AD₀: 0.6x+3.2=-0.6x+9.5 → 1.2x=6.3 → x=5.25; y=6.35
p1, y1 = 6.35, 5.25
ax.plot(y1, p1, 'o', color="#d62728", ms=9, zorder=5)
ax.text(y1-1.6, p1+0.15, "Time 1 (P₁↑, Y₁↓)", color="#d62728", fontsize=10)

# Time 2 SR eq: SRAS₁ & AD₂: 0.6x+3.2=-0.6x+11.5 → 1.2x=8.3 → x=6.92; y=7.35
p2, y2 = 7.35, 6.92
ax.plot(y2, p2, 'o', color="#2ca02c", ms=9, zorder=5)
ax.text(y2+0.1, p2+0.1, "Time 2\n(P₂↑↑, Y₂↑)", color="#2ca02c", fontsize=10)

# Time 3 LR eq: new LRAS₁=4.5, AD₂: y_AD2(4.5)=-0.6*4.5+11.5=8.8
p3, y3 = 8.8, 4.5
ax.plot(y3, p3, 'o', color="#9467bd", ms=9, zorder=5)
ax.text(y3-2.2, p3+0.1, "Time 3 (P₃↑↑↑, Y*'↓)", color="#9467bd", fontsize=10)

# Vertical dashed lines at Y* and Y*'
ax.plot([y0, y0], [0, p0], ls=":", color="#1f77b4", lw=1)
ax.plot([4.5, 4.5], [0, p3], ls=":", color="#d62728", lw=1)
ax.text(y0-0.05, 0.2, "Y*", color="#1f77b4", fontsize=11, ha="center")
ax.text(4.5-0.05, 0.2, "Y*'", color="#d62728", fontsize=11, ha="center")

# Horizontal dashed lines at price levels
for p, label, col in [(p0,"P₀","#1f77b4"),(p1,"P₁","#d62728"),
                       (p2,"P₂","#2ca02c"),(p3,"P₃","#9467bd")]:
    ax.plot([0, max(y0,y1,y2,y3)], [p, p], ls=":", color=col, lw=1, alpha=0.5)
    ax.text(0.15, p+0.1, label, color=col, fontsize=10)

ax.legend(loc="upper right", fontsize=9, framealpha=0.9)
finish(ax, "Real Output (Y)", "Price Level (P)",
       "AD–AS Diagram (Q1.1 / 1.2 / 1.6.2 / 1.7)", "fig1_adas.png")

# ── 1.4  Phillips Curve ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6.5, 5.5))

u = np.linspace(0.5, 9.5, 200)

# Long-run Phillips curves
ax.axvline(x=4.5, color="#1f77b4", lw=2, ls="--", label="LRPC₀ (u* initial)")
ax.axvline(x=6.0, color="#d62728", lw=2, ls="--", label="LRPC₁ (u*' after shock)")

# SRPC₀
srpc0 = -0.8*u + 7.5
ax.plot(u, srpc0, color="#1f77b4", lw=2.2, label="SRPC₀ (Time 0)")

# SRPC₁ shifted up (supply shock)
srpc1 = -0.8*u + 10.0
ax.plot(u, srpc1, color="#d62728", lw=2.2, label="SRPC₁ (Time 1, after shock)")

# Equilibrium points
# Time 0: LRPC₀ x=4.5 → srpc0: y=-0.8*4.5+7.5=3.9
ax.plot(4.5, 3.9, 'o', color="#1f77b4", ms=9, zorder=5)
ax.text(4.6, 3.7, "Time 0\n(u*, π₀)", color="#1f77b4", fontsize=10)

# Time 1: on SRPC₁, at u*'=6.0 → y=-0.8*6.0+10.0=5.2
# short-run: on SRPC₁, moving from previous u*=4.5 → unemployment rises AND inflation rises
# Short run: still at old u expectation → on SRPC₁ at u~5.5 (between old and new)
ax.plot(5.6, 5.52, 'o', color="#d62728", ms=9, zorder=5)
ax.text(5.7, 5.6, "Time 1 (SR)", color="#d62728", fontsize=10)
ax.annotate("", xy=(5.6,5.52), xytext=(4.5,3.9),
            arrowprops=dict(arrowstyle="-|>", color="gray", lw=1.4))

# Long-run after shock: on LRPC₁ and SRPC₁
ax.plot(6.0, 5.2, 'o', color="#ff7f0e", ms=9, zorder=5)
ax.text(6.1, 5.3, "LR after shock\n(u*', π₁)", color="#ff7f0e", fontsize=10)

ax.plot([4.5,4.5],[0,3.9], ls=":", color="#1f77b4", lw=1)
ax.plot([6.0,6.0],[0,5.2], ls=":", color="#d62728", lw=1)
ax.text(4.5, 0.2, "u*", color="#1f77b4", fontsize=11, ha="center")
ax.text(6.0, 0.2, "u*'", color="#d62728", fontsize=11, ha="center")

ax.legend(loc="upper right", fontsize=9, framealpha=0.9)
finish(ax, "Unemployment Rate (u)", "Inflation Rate (π)",
       "Phillips Curve (Q1.4)", "fig2_phillips.png")

# ── 1.5  Labour Market with Binding Minimum Wage ─────────────────────────────
fig, ax = plt.subplots(figsize=(6.5, 5.5))

L = np.linspace(0.5, 9.5, 200)

# Labour supply (upward sloping)
ls = 0.7*L + 1.0
ax.plot(L, ls, color="#1f77b4", lw=2.2, label="Labour Supply (LS)")

# Labour demand Time 0
ld0 = -0.7*L + 9.0
ax.plot(L, ld0, color="#2ca02c", lw=2.2, label="Labour Demand (LD₀)")

# Labour demand Time 1 (shifts left)
ld1 = -0.7*L + 6.5
ax.plot(L, ld1, color="#d62728", lw=2.2, label="Labour Demand (LD₁, after shock)")

# Equilibrium wages (where LS meets LD)
# LS=LD₀: 0.7L+1=-0.7L+9 → 1.4L=8 → L=5.71, W=5.0
L_eq0, W_eq0 = 5.71, 5.0

# Minimum wage line — above W_eq0
W_min = 6.8
ax.axhline(y=W_min, color="black", lw=2, ls="--", label=f"W_min (binding)")
ax.text(0.6, W_min+0.15, "W_min", fontsize=11, fontweight="bold")

# Employment at W_min under LD₀: LD₀=W_min → -0.7L+9=6.8 → L=3.14
# Employment at W_min under LD₁: LD₁=W_min → -0.7L+6.5=6.8 → L=−0.43 (neg, so = 0 or use L=0.5)
# Let me adjust LD₁ so it makes sense
# LD₁ = -0.7L + 8.0 → at W_min=6.8 → L=(8-6.8)/0.7 = 1.71
ld1b = -0.7*L + 8.0
ax.get_lines()[-1].remove()
ax.plot(L, ld1b, color="#d62728", lw=2.2, label="Labour Demand (LD₁, after shock)")

L_emp0 = (9.0 - W_min) / 0.7   # ~3.14
L_emp1 = (8.0 - W_min) / 0.7   # ~1.71
# Labour supply at W_min: LS=W_min → 0.7L+1=6.8 → L=8.29/0.7=8.29
L_sup = (W_min - 1.0) / 0.7    # ~8.29

# Mark Time 0 employment and unemployment
ax.plot(L_emp0, W_min, 'o', color="#2ca02c", ms=9, zorder=5)
ax.text(L_emp0+0.1, W_min+0.2, f"L₀\n(Time 0\nemployment)", color="#2ca02c", fontsize=9)

# Mark Time 1 employment
ax.plot(L_emp1, W_min, 'o', color="#d62728", ms=9, zorder=5)
ax.text(L_emp1-0.1, W_min+0.2, f"L₁\n(Time 1)", color="#d62728", fontsize=9, ha="right")

# Labour supply at W_min
ax.plot(L_sup, W_min, 'o', color="#1f77b4", ms=9, zorder=5)
ax.text(L_sup+0.1, W_min+0.2, "L_S", color="#1f77b4", fontsize=10)

# Unemployment gap arrows
ax.annotate("", xy=(L_sup, W_min-0.35), xytext=(L_emp0, W_min-0.35),
            arrowprops=dict(arrowstyle="<->", color="#2ca02c", lw=1.5))
ax.text((L_emp0+L_sup)/2, W_min-0.7, "Unemployment\n(Time 0)", color="#2ca02c",
        fontsize=9, ha="center")

ax.annotate("", xy=(L_sup, W_min-1.3), xytext=(L_emp1, W_min-1.3),
            arrowprops=dict(arrowstyle="<->", color="#d62728", lw=1.5))
ax.text((L_emp1+L_sup)/2, W_min-1.7, "Unemployment\n(Time 1, wider)", color="#d62728",
        fontsize=9, ha="center")

# Arrow showing LD shift
ax.annotate("", xy=(4.5, ld1b[np.argmin(np.abs(L-4.5))]),
            xytext=(4.5, ld0[np.argmin(np.abs(L-4.5))]),
            arrowprops=dict(arrowstyle="-|>", color="#d62728", lw=1.5))

ax.legend(loc="lower right", fontsize=9, framealpha=0.9)
finish(ax, "Quantity of Labour (L)", "Nominal Wage (W)",
       "Labour Market with Binding Minimum Wage (Q1.5)", "fig3_labour.png")

# ── 1.6.3  IS-LM: Interest Sensitivity of Investment ─────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

for ax, title, is_flat, fname_suffix in [
    (ax1, "Interest Sensitivity HIGH\n(Flat IS curve – fiscal policy LESS effective)", True, "A"),
    (ax2, "Interest Sensitivity LOW\n(Steep IS curve – fiscal policy MORE effective)", False, "B"),
]:
    Y = np.linspace(0.5, 9.5, 200)

    # LM curve (upward sloping, same in both)
    lm = 0.55*Y + 1.5
    ax.plot(Y, lm, color="#1f77b4", lw=2.2, label="LM")

    # IS slope: flat vs steep
    if is_flat:
        slope_is = -0.25
    else:
        slope_is = -1.2

    # IS₀
    intercept0 = 8.0
    is0 = slope_is*Y + intercept0
    ax.plot(Y, is0, color="#2ca02c", lw=2.2, label="IS₀")

    # IS₁ (fiscal policy shifts IS right by same horizontal amount)
    shift = 2.5  # same horizontal shift for both diagrams
    intercept1 = intercept0 - slope_is*shift  # shift IS right
    is1 = slope_is*Y + intercept1
    ax.plot(Y, is1, color="#d62728", lw=2.2, label="IS₁ (after fiscal policy ↑G)")

    # Find intersections IS0 & LM: slope_is*Y+int0 = 0.55*Y+1.5 → (slope_is-0.55)*Y = 1.5-int0
    Y_eq0 = (1.5 - intercept0) / (slope_is - 0.55)
    i_eq0 = 0.55*Y_eq0 + 1.5

    Y_eq1 = (1.5 - intercept1) / (slope_is - 0.55)
    i_eq1 = 0.55*Y_eq1 + 1.5

    ax.plot(Y_eq0, i_eq0, 'o', color="#2ca02c", ms=9, zorder=5)
    ax.plot(Y_eq1, i_eq1, 'o', color="#d62728", ms=9, zorder=5)

    ax.annotate("", xy=(Y_eq1, i_eq1+0.2), xytext=(Y_eq0, i_eq0+0.2),
                arrowprops=dict(arrowstyle="-|>", color="gray", lw=1.4))

    ax.text(Y_eq0-0.1, i_eq0-0.5, "E₀", fontsize=11, color="#2ca02c", ha="right")
    ax.text(Y_eq1+0.1, i_eq1-0.5, "E₁", fontsize=11, color="#d62728")

    delta_Y = Y_eq1 - Y_eq0
    delta_i = i_eq1 - i_eq0

    ax.plot([Y_eq0, Y_eq0], [0, i_eq0], ls=":", color="#2ca02c", lw=1)
    ax.plot([Y_eq1, Y_eq1], [0, i_eq1], ls=":", color="#d62728", lw=1)
    ax.plot([0, Y_eq0], [i_eq0, i_eq0], ls=":", color="#2ca02c", lw=1)
    ax.plot([0, Y_eq1], [i_eq1, i_eq1], ls=":", color="#d62728", lw=1)

    ax.text(Y_eq0, 0.2, "Y₀", color="#2ca02c", fontsize=10, ha="center")
    ax.text(Y_eq1, 0.2, "Y₁", color="#d62728", fontsize=10, ha="center")
    ax.text(0.2, i_eq0, f"i₀", color="#2ca02c", fontsize=10, va="center")
    ax.text(0.2, i_eq1, f"i₁", color="#d62728", fontsize=10, va="center")

    dy_label = f"ΔY ≈ {delta_Y:.1f}"
    ax.text((Y_eq0+Y_eq1)/2, 0.6, dy_label, ha="center", fontsize=10, color="gray",
            bbox=dict(boxstyle="round,pad=0.2", fc="lightyellow", ec="gray"))

    ax.set_title(title, fontsize=11, fontweight="bold", pad=8)
    ax.set_xlabel("Output (Y)", fontsize=11)
    ax.set_ylabel("Interest Rate (i)", fontsize=11)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_xticks([]); ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.9)

plt.suptitle("IS-LM: Effectiveness of Fiscal Policy by Interest Sensitivity of Investment (Q1.6.3)",
             fontsize=12, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig(f"{OUT}/fig4_islm.png", dpi=150, bbox_inches="tight")
plt.close()
print("  saved fig4_islm.png")

# ── 2.1  Money Market ─────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6.5, 5.5))

M = np.linspace(0.5, 9.5, 200)

# Money demand (downward sloping)
md = -0.7*M + 9.0
ax.plot(M, md, color="#1f77b4", lw=2.2, label="Money Demand (MD)")

# MS₀ (initial, vertical)
ax.axvline(x=5.0, color="#2ca02c", lw=2.2, label="MS₀ (initial)")
# MS₁ after QE (shifts right)
ax.axvline(x=7.0, color="#d62728", lw=2, ls="--", label="MS₁ (after QE)")
# MS₂ after increased cash holding (shifts left from MS₁)
ax.axvline(x=5.5, color="#ff7f0e", lw=2, ls="-.", label="MS₂ (cash↑→ multiplier↓)")

# Point A: initial equilibrium MS₀ & MD: M=5 → V=−0.7*5+9=5.5
A = (5.0, 5.5)
# Point D: equilibrium after QE on MS₁: M=7 → V=−0.7*7+9=4.1
D = (7.0, 4.1)
# Point C: equilibrium on MS₂: M=5.5 → V=−0.7*5.5+9=5.15
C = (5.5, 5.15)
# Point B: some reference point (upper area)
B = (5.0, 7.5)

for pt, lbl, col in [(A,"A","#2ca02c"),(D,"D","#d62728"),(C,"C","#ff7f0e"),(B,"B","#9467bd")]:
    ax.plot(*pt, 'o', ms=10, color=col, zorder=6)
    offset = (0.2, 0.2) if lbl in ("A","D") else (-0.5, 0.2)
    ax.text(pt[0]+offset[0], pt[1]+offset[1], lbl, fontsize=13, fontweight="bold", color=col)

# Arrows
ax.annotate("", xy=D, xytext=A,
            arrowprops=dict(arrowstyle="-|>", color="#d62728", lw=1.5,
                            connectionstyle="arc3,rad=-0.25"))
ax.text(6.1, 5.2, "Stmt 1:\nQE → A→D", color="#d62728", fontsize=9)

ax.annotate("", xy=C, xytext=D,
            arrowprops=dict(arrowstyle="-|>", color="#ff7f0e", lw=1.5,
                            connectionstyle="arc3,rad=0.3"))
ax.text(6.2, 4.5, "Stmt 2:\nD→C", color="#ff7f0e", fontsize=9)

ax.legend(loc="upper right", fontsize=9, framealpha=0.9)
finish(ax, "Quantity of Money (M)", "Value of Money (1/P)",
       "Money Market (Q2.1)", "fig5_money.png")

print("\nAll diagrams generated successfully.")
