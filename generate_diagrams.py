"""
Clean, well-spaced macroeconomics diagrams for the try-out exam.
Font: Liberation Sans  |  Subscripts: LaTeX math mode
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os

OUT = "/home/user/BabyPluto/diagrams"
os.makedirs(OUT, exist_ok=True)

# ── Global style ─────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "Liberation Sans",
    "font.size": 13,
    "axes.linewidth": 1.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.bottom": False,
    "ytick.left": False,
    "xtick.labelbottom": False,
    "ytick.labelleft": False,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

# Palette
C0  = "#2166ac"   # blue      – Time 0 / initial
C1  = "#d6604d"   # red-orange – Time 1 / shock
C2  = "#4dac26"   # green     – Time 2 / stimulus
C3  = "#8e44ad"   # purple    – Time 3 / long-run
CLM = "#e67e22"   # orange    – LM curve
BG  = "white"

def lbl(ax, x, y, text, color, ha="left", va="center", fs=12, bold=False):
    """Label with a white backing so it never overlaps curves."""
    weight = "bold" if bold else "normal"
    ax.text(x, y, text, color=color, ha=ha, va=va, fontsize=fs,
            fontweight=weight,
            bbox=dict(boxstyle="round,pad=0.25", fc=BG, ec="none", alpha=0.85))

def dot(ax, x, y, color, size=9):
    ax.plot(x, y, "o", color=color, ms=size, zorder=6, mec="white", mew=1.2)

def save(fig, fname):
    fig.savefig(f"{OUT}/{fname}", dpi=160, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"  saved {fname}")

def axis_labels(ax, xlabel, ylabel, fontsize=13):
    ax.set_xlabel(xlabel, fontsize=fontsize, labelpad=6)
    ax.set_ylabel(ylabel, fontsize=fontsize, labelpad=6)

# ═══════════════════════════════════════════════════════════════════════════════
# FIG 1 – AD-AS  (Q 1.1 / 1.2 / 1.6.2 / 1.7)
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 8.5))
ax.set_xlim(0, 11);  ax.set_ylim(0, 11)
ax.set_title("AD – AS Diagram  (Q 1.1 · Q 1.2 · Q 1.6.2 · Q 1.7)",
             fontsize=14, fontweight="bold", pad=12)
axis_labels(ax, "Real Output  (Y)", "Price Level  (P)")

Y = np.linspace(0.3, 10.7, 400)

# ── LRAS lines ──
Ystar0, Ystar1 = 7.2, 5.0
ax.axvline(Ystar0, color=C0, lw=2.2, ls="--", zorder=2)
ax.axvline(Ystar1, color=C1, lw=2.2, ls="--", zorder=2)
lbl(ax, Ystar0+0.1, 10.2, r"$LRAS_0$", C0, fs=12, bold=True)
lbl(ax, Ystar1+0.1, 10.2, r"$LRAS_{1,2,3}$", C1, fs=12, bold=True)
lbl(ax, Ystar0,     0.4, r"$Y^*$",  C0, ha="center", fs=11)
lbl(ax, Ystar1,     0.4, r"$Y^{*'}$", C1, ha="center", fs=11)

# ── SRAS curves  y = slope*x + intercept ──
def sras(x, intercept, slope=0.55):
    return slope * x + intercept

def ad(x, intercept, slope=-0.65):
    return slope * x + intercept

def intersect_sras_ad(si, ai, ss=0.55, as_=-0.65):
    # ss*x + si = as_*x + ai  →  x = (ai-si)/(ss-as_)
    x = (ai - si) / (ss - as_)
    y = ss * x + si
    return x, y

sras0_i, sras1_i, sras2_i = 0.5, 2.8, 5.5
ad0_i,   ad2_i            = 10.0, 12.5

# SRAS₀ (Time 0)
ax.plot(Y, sras(Y, sras0_i), color=C0, lw=2.2, zorder=3)
lbl(ax, 9.8, sras(9.8, sras0_i)+0.35, r"$SRAS_0$", C0, ha="right", fs=12, bold=True)

# SRAS₁ (Time 1 – supply shock)
ax.plot(Y, sras(Y, sras1_i), color=C1, lw=2.2, zorder=3)
lbl(ax, 9.5, sras(9.5, sras1_i)+0.35, r"$SRAS_1$", C1, ha="right", fs=12, bold=True)

# SRAS₂ (Time 3 – long-run adjustment)
ax.plot(Y, sras(Y, sras2_i), color=C3, lw=2.2, ls=(0,(6,3)), zorder=3)
lbl(ax, 9.0, sras(9.0, sras2_i)+0.35, r"$SRAS_2$", C3, ha="right", fs=12, bold=True)

# AD₀ (Time 0 & 1)
ax.plot(Y, ad(Y, ad0_i), color=C0, lw=2.2, ls="-.", zorder=3)
lbl(ax, 9.8, ad(9.8, ad0_i)-0.5, r"$AD_0$", C0, ha="right", fs=12, bold=True)

# AD₂ (Time 2 – fiscal stimulus)
ax.plot(Y, ad(Y, ad2_i), color=C2, lw=2.2, ls="-.", zorder=3)
lbl(ax, 10.0, ad(10.0, ad2_i)-0.5, r"$AD_2$", C2, ha="right", fs=12, bold=True)

# ── Equilibrium points ──
# Time 0: LRAS₀ & AD₀
P0 = ad(Ystar0, ad0_i)
dot(ax, Ystar0, P0, C0)
lbl(ax, Ystar0+0.25, P0+0.3,
    r"$\mathbf{Time\ 0}$" + "\n" + r"$(P_0,\ Y^*)$",
    C0, fs=11)

# Time 1: SRAS₁ & AD₀
Y1, P1 = intersect_sras_ad(sras1_i, ad0_i)
dot(ax, Y1, P1, C1)
lbl(ax, Y1-0.3, P1+0.5,
    r"$\mathbf{Time\ 1}$" + "\n" + r"$(P_1{\uparrow},\ Y_1{\downarrow})$",
    C1, ha="right", fs=11)

# Time 2: SRAS₁ & AD₂
Y2, P2 = intersect_sras_ad(sras1_i, ad2_i)
dot(ax, Y2, P2, C2)
lbl(ax, Y2+0.25, P2-0.55,
    r"$\mathbf{Time\ 2}$" + "\n" + r"$(P_2{\uparrow\uparrow},\ Y_2{\uparrow})$",
    C2, fs=11)

# Time 3: SRAS₂ & AD₂ at new LRAS
P3 = ad(Ystar1, ad2_i)
dot(ax, Ystar1, P3, C3)
lbl(ax, Ystar1-0.3, P3+0.4,
    r"$\mathbf{Time\ 3}$" + "\n" + r"$(P_3{\uparrow\uparrow\uparrow},\ Y^{*'})$",
    C3, ha="right", fs=11)

# Price-level guide lines
for P, col in [(P0, C0), (P1, C1), (P2, C2), (P3, C3)]:
    ax.axhline(P, color=col, lw=0.6, ls=":", alpha=0.55)

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
save(fig, "fig1_adas.png")


# ═══════════════════════════════════════════════════════════════════════════════
# FIG 2 – Phillips Curve  (Q 1.4)
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9.5, 7.5))
ax.set_xlim(0, 11);  ax.set_ylim(0, 11)
ax.set_title("Phillips Curve  (Q 1.4)", fontsize=14, fontweight="bold", pad=12)
axis_labels(ax, r"Unemployment Rate  ($u$)", r"Inflation Rate  ($\pi$)")

u = np.linspace(0.3, 10.7, 400)

unat0, unat1 = 4.2, 6.0          # natural rates

# LRPC lines
ax.axvline(unat0, color=C0, lw=2.2, ls="--")
ax.axvline(unat1, color=C1, lw=2.2, ls="--")
lbl(ax, unat0+0.15, 10.3, r"$LRPC_0$", C0, fs=12, bold=True)
lbl(ax, unat1+0.15, 10.3, r"$LRPC_1$", C1, fs=12, bold=True)
lbl(ax, unat0,  0.4, r"$u^*$",  C0, ha="center", fs=11)
lbl(ax, unat1,  0.4, r"$u^{*'}$", C1, ha="center", fs=11)

# SRPC₀  π = −0.9u + 8.5
srpc0 = lambda x: -0.9*x + 8.5
ax.plot(u, srpc0(u), color=C0, lw=2.4)
lbl(ax, 1.2, srpc0(1.2)+0.4, r"$SRPC_0$  (Time 0)", C0, fs=12, bold=True)

# SRPC₁ shifted up by 2.5 (supply shock)
srpc1 = lambda x: -0.9*x + 11.0
ax.plot(u, srpc1(u), color=C1, lw=2.4)
lbl(ax, 1.2, srpc1(1.2)+0.4, r"$SRPC_1$  (Time 1, after shock)", C1, fs=12, bold=True)

# Time 0 equilibrium: LRPC₀ ∩ SRPC₀
P_eq0 = srpc0(unat0)
dot(ax, unat0, P_eq0, C0)
lbl(ax, unat0+0.3, P_eq0+0.3, "Time 0\n" + r"$(u^*,\ \pi_0)$", C0, fs=11)

# Short-run Time 1: on SRPC₁, unemployment rises moderately
u_sr1 = 5.4
pi_sr1 = srpc1(u_sr1)
dot(ax, u_sr1, pi_sr1, C1)
lbl(ax, u_sr1+0.3, pi_sr1+0.3,
    "Time 1  (SR)\n" + r"$\pi\uparrow$  and  $u\uparrow$  (stagflation)",
    C1, fs=11)
ax.annotate("", xy=(u_sr1, pi_sr1), xytext=(unat0, P_eq0),
            arrowprops=dict(arrowstyle="-|>", color="gray", lw=1.4,
                            connectionstyle="arc3,rad=-0.2"))

# Long-run Time 1: LRPC₁ ∩ SRPC₁
pi_lr1 = srpc1(unat1)
dot(ax, unat1, pi_lr1, "#d4ac0d")
lbl(ax, unat1+0.3, pi_lr1-0.7,
    "Long-run equilibrium\n" + r"$(u^{*'},\ \pi_1)$", "#d4ac0d", fs=11)

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
save(fig, "fig2_phillips.png")


# ═══════════════════════════════════════════════════════════════════════════════
# FIG 3 – Labour Market with Binding Minimum Wage  (Q 1.5)
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9.5, 7.5))
ax.set_xlim(0, 11);  ax.set_ylim(0, 11)
ax.set_title("Labour Market – Binding Minimum Wage  (Q 1.5)",
             fontsize=14, fontweight="bold", pad=12)
axis_labels(ax, "Quantity of Labour  (L)", "Nominal Wage  (W)")

L = np.linspace(0.3, 10.7, 400)

ls_fn  = lambda x:  0.75*x + 1.2          # Labour supply
ld0_fn = lambda x: -0.75*x + 9.8          # Labour demand Time 0
ld1_fn = lambda x: -0.75*x + 7.5          # Labour demand Time 1 (shift left)

ax.plot(L, ls_fn(L),  color=C0, lw=2.4, label=r"$LS$  (Labour Supply)")
ax.plot(L, ld0_fn(L), color=C2, lw=2.4, label=r"$LD_0$  (Time 0 demand)")
ax.plot(L, ld1_fn(L), color=C1, lw=2.4, label=r"$LD_1$  (Time 1 demand, after shock)")

lbl(ax, 8.8, ls_fn(8.8)+0.4,   r"$LS$",   C0, fs=12, bold=True)
lbl(ax, 8.8, ld0_fn(8.8)+0.4,  r"$LD_0$", C2, fs=12, bold=True)
lbl(ax, 8.8, ld1_fn(8.8)-0.65, r"$LD_1$", C1, fs=12, bold=True)

# Minimum wage horizontal line
W_min = 7.2
ax.axhline(W_min, color="black", lw=2.0, ls="--", zorder=4)
lbl(ax, 0.4, W_min+0.35, r"$W_{min}$  (binding minimum wage)",
    "black", fs=12, bold=True)

# Key quantities at W_min
# LD₀ at W_min: -0.75L+9.8=7.2 → L=3.47
# LD₁ at W_min: -0.75L+7.5=7.2 → L=0.4 (very small — let's adjust)
# Adjust LD₁: -0.75L+8.3=7.2 → L=1.47
ld1_fn2 = lambda x: -0.75*x + 8.3
ax.get_lines()[-2].remove()    # remove old LD1
ax.plot(L, ld1_fn2(L), color=C1, lw=2.4)
lbl(ax, 8.5, ld1_fn2(8.5)-0.65, r"$LD_1$", C1, fs=12, bold=True)

L_ld0 = (9.8 - W_min) / 0.75   # employment Time 0 ≈ 3.47
L_ld1 = (8.3 - W_min) / 0.75   # employment Time 1 ≈ 1.47
L_ls  = (W_min - 1.2) / 0.75   # labour supply at W_min ≈ 8.0

dot(ax, L_ld0, W_min, C2)
dot(ax, L_ld1, W_min, C1)
dot(ax, L_ls,  W_min, C0)

lbl(ax, L_ld0, W_min-0.7, r"$L_0$" + "\n(employed\nTime 0)", C2, ha="center", fs=11)
lbl(ax, L_ld1, W_min-0.7, r"$L_1$" + "\n(employed\nTime 1)", C1, ha="center", fs=11)
lbl(ax, L_ls,  W_min+0.4, r"$L_S$" + "\n(labour supply)", C0, ha="center", fs=11)

# Unemployment gap arrows — Time 0
y_a0 = W_min - 1.6
ax.annotate("", xy=(L_ls, y_a0), xytext=(L_ld0, y_a0),
            arrowprops=dict(arrowstyle="<->", color=C2, lw=1.7))
lbl(ax, (L_ld0+L_ls)/2, y_a0-0.45,
    "Unemployment gap\n(Time 0)", C2, ha="center", fs=10)

# Unemployment gap arrows — Time 1
y_a1 = W_min - 2.9
ax.annotate("", xy=(L_ls, y_a1), xytext=(L_ld1, y_a1),
            arrowprops=dict(arrowstyle="<->", color=C1, lw=1.7))
lbl(ax, (L_ld1+L_ls)/2, y_a1-0.45,
    "Wider unemployment gap\n(Time 1)", C1, ha="center", fs=10)

# Arrow showing demand shift
mid_L = 6.0
ax.annotate("", xy=(mid_L, ld1_fn2(mid_L)+0.15),
            xytext=(mid_L, ld0_fn(mid_L)-0.15),
            arrowprops=dict(arrowstyle="-|>", color=C1, lw=1.7))

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
save(fig, "fig3_labour.png")


# ═══════════════════════════════════════════════════════════════════════════════
# FIG 4 – IS-LM: high vs low interest sensitivity  (Q 1.6.3)
# Two separate figures to avoid congestion
# ═══════════════════════════════════════════════════════════════════════════════
for panel, (title_note, is_slope, label_eff) in enumerate([
    ("Interest Sensitivity  HIGH  →  Flat IS  →  Fiscal Policy  LESS Effective",
     -0.22, "small $\Delta Y$"),
    ("Interest Sensitivity  LOW  →  Steep IS  →  Fiscal Policy  MORE Effective",
     -1.40, "large $\Delta Y$"),
], start=1):

    fig, ax = plt.subplots(figsize=(9, 7))
    ax.set_xlim(0, 11);  ax.set_ylim(0, 11)
    ax.set_title(title_note, fontsize=13, fontweight="bold", pad=12, wrap=True)
    axis_labels(ax, "Output  (Y)", "Interest Rate  (i)")

    lm_slope, lm_int = 0.6, 1.0

    def lm(x): return lm_slope*x + lm_int
    def is0(x): return is_slope*x + 9.5
    def is1(x): return is_slope*x + 9.5 - is_slope*2.8   # shift right by 2.8

    # IS intersect LM
    def eq(fn):
        x = (lm_int - (fn(0) - is_slope*0)) / (is_slope - lm_slope) if is_slope != lm_slope else None
        # more carefully: is_slope*x + b = lm_slope*x + lm_int  → x=(lm_int-b)/(is_slope-lm_slope)
        b0 = fn(0)   # intercept of IS
        x_ = (lm_int - b0) / (is_slope - lm_slope)
        return x_, lm(x_)

    Yeq0, ieq0 = eq(is0)
    Yeq1, ieq1 = eq(is1)

    ax.plot(np.linspace(0.3,10.7,400), lm(np.linspace(0.3,10.7,400)),
            color=CLM, lw=2.4)
    ax.plot(np.linspace(0.3,10.7,400), is0(np.linspace(0.3,10.7,400)),
            color=C0, lw=2.4)
    ax.plot(np.linspace(0.3,10.7,400), is1(np.linspace(0.3,10.7,400)),
            color=C2, lw=2.4)

    # Curve end labels
    lbl(ax, 10.5, lm(10.5)+0.35, "$LM$", CLM, fs=12, bold=True)
    lbl(ax, 10.5, is0(10.5)+0.35, r"$IS_0$", C0, fs=12, bold=True)
    lbl(ax, 10.5, is1(10.5)-0.65, r"$IS_1$  (after $\uparrow G$)", C2, fs=12, bold=True)

    dot(ax, Yeq0, ieq0, C0)
    dot(ax, Yeq1, ieq1, C2)

    lbl(ax, Yeq0-0.25, ieq0+0.45, r"$E_0$", C0, ha="right", fs=12, bold=True)
    lbl(ax, Yeq1+0.25, ieq1+0.45, r"$E_1$", C2, ha="left",  fs=12, bold=True)

    # Guide lines
    for Yeq, ieq, col in [(Yeq0, ieq0, C0), (Yeq1, ieq1, C2)]:
        ax.plot([Yeq, Yeq], [0, ieq], ls=":", color=col, lw=1.1)
        ax.plot([0, Yeq],   [ieq, ieq], ls=":", color=col, lw=1.1)

    lbl(ax, Yeq0, 0.45, r"$Y_0$", C0, ha="center", fs=11)
    lbl(ax, Yeq1, 0.45, r"$Y_1$", C2, ha="center", fs=11)
    lbl(ax, 0.3, ieq0, r"$i_0$", C0, ha="right", fs=11)
    lbl(ax, 0.3, ieq1, r"$i_1$", C2, ha="right", fs=11)

    # Delta Y bracket
    y_brk = 0.95
    ax.annotate("", xy=(Yeq1, y_brk), xytext=(Yeq0, y_brk),
                arrowprops=dict(arrowstyle="<->", color="gray", lw=1.5))
    lbl(ax, (Yeq0+Yeq1)/2, y_brk+0.55, label_eff, "gray", ha="center", fs=11)

    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["left"].set_position(("data", 0))
    save(fig, f"fig4_islm_{panel}.png")


# ═══════════════════════════════════════════════════════════════════════════════
# FIG 5 – Money Market  (Q 2.1)
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 7.5))
ax.set_xlim(0, 11);  ax.set_ylim(0, 11)
ax.set_title("Money Market  (Q 2.1)", fontsize=14, fontweight="bold", pad=12)
axis_labels(ax, "Quantity of Money  (M)", "Value of Money  (1/P)")

M = np.linspace(0.3, 10.7, 400)
md_fn = lambda x: -0.75*x + 9.8

# Money demand
ax.plot(M, md_fn(M), color=C0, lw=2.4)
lbl(ax, 9.8, md_fn(9.8)-0.6, "$MD$  (Money Demand)", C0, ha="right", fs=12, bold=True)

# MS₀ initial
ms0 = 4.8
ax.axvline(ms0, color=C0, lw=2.4)
lbl(ax, ms0+0.15, 10.3, r"$MS_0$  (initial)", C0, fs=12, bold=True)

# MS₁ after QE (shifts right)
ms1 = 7.2
ax.axvline(ms1, color=C1, lw=2.4, ls="--")
lbl(ax, ms1+0.15, 10.3, r"$MS_1$  (after QE)", C1, fs=12, bold=True)

# MS₂ after cash-holding shift (shifts left from MS₁)
ms2 = 5.6
ax.axvline(ms2, color=C2, lw=2.4, ls=(0,(6,3)))
lbl(ax, ms2-0.2, 10.3, r"$MS_2$  (cash $\uparrow$, multiplier $\downarrow$)", C2,
    ha="right", fs=12, bold=True)

# Equilibrium points
A = (ms0, md_fn(ms0))   # initial eq
D = (ms1, md_fn(ms1))   # after QE
C_pt = (ms2, md_fn(ms2))# after cash shift

for pt, lbl_txt, col in [
    (A,    "A  (initial equilibrium)", C0),
    (D,    "D  (after QE)", C1),
    (C_pt, "C  (after cash shift)", C2),
]:
    dot(ax, *pt, col, size=11)
    # determine offset to avoid overlap
    if pt == A:
        dx, dy, ha_ = -0.3, 0.45, "right"
    elif pt == D:
        dx, dy, ha_ = 0.3, 0.45, "left"
    else:
        dx, dy, ha_ = -0.3, -0.65, "right"
    lbl(ax, pt[0]+dx, pt[1]+dy, lbl_txt, col, ha=ha_, fs=11, bold=True)

# Arrows between points
ax.annotate("", xy=(D[0]-0.1, D[1]+0.5),
            xytext=(A[0]+0.1, A[1]-0.25),
            arrowprops=dict(arrowstyle="-|>", color=C1, lw=1.7,
                            connectionstyle="arc3,rad=-0.3"))
lbl(ax, 6.5, 6.8, "Statement 1:\nQE  →  A to D", C1, ha="center", fs=10)

ax.annotate("", xy=(C_pt[0]+0.1, C_pt[1]+0.3),
            xytext=(D[0]-0.1,    D[1]-0.3),
            arrowprops=dict(arrowstyle="-|>", color=C2, lw=1.7,
                            connectionstyle="arc3,rad=0.35"))
lbl(ax, 5.9, 4.2, "Statement 2:\ncash↑  →  D to C", C2, ha="center", fs=10)

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
save(fig, "fig5_money.png")

print("\nAll diagrams generated successfully.")
