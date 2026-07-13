# Chapter 8 — Inventories

### A Practice-Focused Study Guide & Workbook

*Course: Internal and External Financial Reporting (Part 1a — Financial Accounting)*
*Based on the lecture slides by V. Ghijselinck, Academic year 2025–2026*
*Textbook reference: “A Practical Guide to Financial Accounting”, Chapter 8 (p. 177 → p. 218)*

> **How to use this guide.** This is a *workbook*, not just notes. Chapter 8 is the first heavily **numerical** chapter — the skill is *calculating* the value of closing inventory three different ways, then turning the result into one end-of-period journal entry. Keep a pen and a calculator next to you, cover each solution, and *do* the numbers before you peek. The running example is **OMEGA KAPPA plc**.

---

## 📑 Table of Contents

1. [Topic Overview](#1-topic-overview)
2. [The Core Mechanism — Why Inventory Only Moves at Year-End](#2-the-core-mechanism)
3. [Cost of Acquisition vs Market Value](#3-cost-of-acquisition-vs-market-value)
4. [The Case Study (OMEGA KAPPA plc)](#4-the-case-study)
5. [⭐ FIFO](#5-fifo--first-in-first-out)
6. [⭐ LIFO](#6-lifo--last-in-first-out)
7. [⭐ Weighted Average Price (overall & moving)](#7-weighted-average-price)
8. [Comparing the Methods](#8-comparing-the-methods)
9. [The Market Test (lower of cost or market)](#9-the-market-test)
10. [Write-offs on Inventory](#10-write-offs-on-inventory)
11. [Manufactured Inventories & Contracts in Progress](#11-manufactured-inventories--contracts-in-progress)
12. [Guided Practice — Worked Example (SPRITZ plc)](#12-guided-practice--worked-example-spritz-plc)
13. [Interactive Practice Section (Workbook)](#13-interactive-practice-section)
14. [Solutions & Explanations](#14-solutions--explanations)
15. [Quick Check / Active Recall](#15-quick-check--active-recall)
16. [Common Mistakes](#16-common-mistakes)
17. [Summary Sheet](#17-summary-sheet)

---

## 1. Topic Overview

**In one sentence:** this chapter is about putting the *right value* on the goods still sitting in the warehouse at year-end — and recording the change so both the balance sheet and the income statement tell the truth.

The problem: during the year you buy stock at *different prices*. When only *some* of it is left at year-end, **which prices do the leftover units carry?** That single question has three accepted answers — **FIFO, LIFO, and weighted average** — and they give *different profits from identical facts*. That's why this matters: the valuation method is a real accounting *choice* with a real effect on reported profit and on tax.

**What you'll be able to do:**

- Explain the valuation choices for **purchased inventories**.
- Compute closing inventory under **FIFO, LIFO and weighted-average** (overall *and* moving).
- Record the **change in inventory** as an end-of-period entry in the ledger and journal.
- Apply the **market test** (lower of cost or market).
- Record **write-offs** on inventory.
- Outline the valuation of **manufactured inventories & contracts in progress** (direct/full costing, %-of-completion / completed-contract).
- State the **impact** on the balance sheet and income statement.

---

## 2. The Core Mechanism

Here is the idea the whole chapter hangs on. **During the accounting period:**

- Every **purchase** is booked to an **expense** account (`604` Purchases of goods for resale).
- Every **sale** is booked to a **revenue** account (`70` Sales of goods for resale).
- The **inventory account (`340`) is *not touched*** — it just keeps its opening balance all year.

**Only at year-end** (an *end-of-period entry*, after a physical stock-take) do we:

- Record the **change in inventories** so `340` shows the **correct closing value** (an asset on the balance sheet), and
- so the income statement shows the **correct cost of goods sold** (COGS).

### The cost-of-goods-sold identity

$$\text{COGS} = \text{Opening inventory} + \text{Purchases} - \text{Closing inventory}$$

And the **change in inventory** = Closing − Opening. Everything in this chapter is really just: *value the closing inventory, then book the change.*

### The one journal entry (inventory increased)

When closing > opening, inventory went **up**:

```
31/12  340   Inventory of goods for resale – Cost of acquisition   [change]
       @ 6094 Changes in inventories of goods for resale                     [change]
             (DIV 20X0/… – change in inventory)
```

- `340` is an **asset** → **debit** to increase it.
- `6094` *Changes in inventories* is an **operating expense account**, but here it is **credited** — an increase in stock **reduces** the net cost of goods sold (it appears as a *negative* on the expense side, line `609`).

> If inventory instead **decreased**, you flip the entry: `6094` D / `340` C.

---

## 3. Cost of Acquisition vs Market Value

Two values compete for every item; you'll always compare them (§9).

- **Cost of acquisition** = purchase cost **+ other/additional costs** (transport, etc.), *excluding refundable taxes* like VAT. This is what the four valuation methods estimate.
  - Methods to pin it down: **specific identification**, **FIFO**, **LIFO**, **weighted average**.
- **Market value (net realisable value)** = estimated selling price **−** estimated costs of completion **−** estimated costs of sale.

The **lower of the two always prevails** (§9) — a consequence of the **prudence principle**.

---

## 4. The Case Study

All of §5–§9 use **OMEGA KAPPA plc**, one item of *goods for resale*:

| Date | Movement | Units | Price/unit | Total |
|---|---|--:|--:|--:|
| 01/01/20X0 | Opening inventory | 100 | 10,00 | 1 000,00 |
| 15/02/20X0 | Sale | 60 | 16,00 | 960,00 |
| 29/03/20X0 | **Purchase** | 80 | 15,00 | 1 200,00 |
| 23/08/20X0 | Sale | 60 | 21,00 | 1 260,00 |
| 05/09/20X0 | **Purchase** | 100 | 20,00 | 2 000,00 |
| 21/12/20X0 | Sale | 80 | 24,00 | 1 920,00 |

**Facts that are the same under every method:**

- **Closing units** = 100 opening + (80 + 100) purchased − (60 + 60 + 80) sold = **80 units**.
- **Purchases** (cost, on `604`) = 1 200 + 2 000 = **3 200,00**.
- **Sales** (revenue, on `70`) = 960 + 1 260 + 1 920 = **4 140,00**.
- **Opening inventory** (on `340`) = **1 000,00**.

The *only* thing that differs between methods is **how you value those 80 leftover units** — which then drives the change, COGS and profit.

---

## 5. FIFO — First In, First Out

> **Assumption:** the goods bought **first** are sold **first**. Therefore the goods **left in stock** are assumed to come from the **most recent** purchases.

**Value the 80 closing units from the newest purchases first:**
- 80 units all fit inside the last purchase (05/09, 100 units @ 20,00) → 80 × 20,00 = **€1 600,00**.

**Change in inventory** = 1 600 − 1 000 = **+600,00**.

```
340   Inventory of GFR – Cost of acquisition   600,00
@ 6094 Changes in inventories of GFR                       600,00
```

- **Closing inventory (BS)** = **1 600,00**.
- **COGS (IS)** = 1 000 + 3 200 − 1 600 = **2 600,00**.
- **Operating profit** = Sales 4 140 − COGS 2 600 = **1 540,00**.

> In a period of *rising* prices, FIFO leaves the *newest, dearest* units in stock → **highest closing inventory, lowest COGS, highest profit.**

---

## 6. LIFO — Last In, First Out

> **Assumption:** the goods bought **last** are sold **first**. Therefore the goods **left in stock** are assumed to come from the **earliest** purchases.

⚠️ **You must work step-by-step**, checking what's in stock at *each sale* — you can't just grab the oldest layers at the end, because a layer might already have been sold.

| After… | Stock layers |
|---|---|
| Opening | 100 @ 10 |
| Sale 60 (15/02) | sell newest = 60 @ 10 → **40 @ 10** |
| Purchase 80 @ 15 | 40 @ 10 + 80 @ 15 |
| Sale 60 (23/08) | sell newest = 60 @ 15 → 40 @ 10 + **20 @ 15** |
| Purchase 100 @ 20 | 40 @ 10 + 20 @ 15 + 100 @ 20 |
| Sale 80 (21/12) | sell newest = 80 @ 20 → 40 @ 10 + 20 @ 15 + **20 @ 20** |

**Closing (80 units)** = 40 × 10 + 20 × 15 + 20 × 20 = 400 + 300 + 400 = **€1 100,00**.

**Change** = 1 100 − 1 000 = **+100,00**.

```
340   Inventory of GFR – Cost of acquisition   100,00
@ 6094 Changes in inventories of GFR                       100,00
```

- **Closing inventory (BS)** = **1 100,00** · **COGS** = 1 000 + 3 200 − 1 100 = **3 100,00** · **Operating profit** = 4 140 − 3 100 = **1 040,00**.

> With *rising* prices, LIFO leaves the *oldest, cheapest* units in stock → **lowest closing inventory, highest COGS, lowest profit.**

---

## 7. Weighted Average Price

Two flavours. Both value the 80 closing units at an *average* purchase price, but computed differently.

### 7a. Overall (periodic) weighted average

Average over **opening + all purchases of the whole period**:

| | Units | Total |
|---|--:|--:|
| Opening | 100 | 1 000,00 |
| Purchases | 180 | 3 200,00 |
| **Total available** | **280** | **4 200,00** |

**Weighted average price** = 4 200 / 280 = **€15,00/unit**.
**Closing** = 80 × 15,00 = **€1 200,00**. **Change** = +200,00.

```
340   Inventory of GFR – Cost of acquisition   200,00
@ 6094 Changes in inventories of GFR                       200,00
```

COGS = 1 000 + 3 200 − 1 200 = **3 000,00** · Operating profit = 4 140 − 3 000 = **1 140,00**.

### 7b. Moving weighted average

Recompute the average **after each purchase** (round to the cent). At each sale, units leave at the *current* average.

| Date | Movement | Units | Avg price | Balance value |
|---|---|--:|--:|--:|
| 01/01 | Opening | 100 | 10,00 | 1 000,00 |
| 15/02 | Sale 60 | 40 | 10,00 | 400,00 |
| 29/03 | Purchase 80 @ 15 | 120 | **13,33** | 1 600,00 |
| 23/08 | Sale 60 | 60 | 13,33 | 800,00 |
| 05/09 | Purchase 100 @ 20 | 160 | **17,50** | 2 800,00 |
| 21/12 | Sale 80 | 80 | 17,50 | 1 400,00 |

**Closing** = **€1 400,00**. **Change** = +400,00.

```
340   Inventory of GFR – Cost of acquisition   400,00
@ 6094 Changes in inventories of GFR                       400,00
```

COGS = 1 000 + 3 200 − 1 400 = **2 800,00** · Operating profit = 4 140 − 2 800 = **1 340,00**.

> *New average after a purchase* = (old value + purchase value) / (old units + purchased units). E.g. after 29/03: (400 + 1 200) / (40 + 80) = 1 600 / 120 = 13,33.

---

## 8. Comparing the Methods

Same transactions, four different profits — this is the punchline of the chapter:

| | FIFO | Moving WAP | Overall WAP | LIFO |
|---|--:|--:|--:|--:|
| Sales | 4 140,00 | 4 140,00 | 4 140,00 | 4 140,00 |
| Purchases | 3 200,00 | 3 200,00 | 3 200,00 | 3 200,00 |
| Change in inventory | −600,00 | −400,00 | −200,00 | −100,00 |
| **Cost of goods sold** | **2 600,00** | **2 800,00** | **3 000,00** | **3 100,00** |
| **Operating profit** | **1 540,00** | **1 340,00** | **1 140,00** | **1 040,00** |
| **Closing inventory (BS)** | **1 600,00** | **1 400,00** | **1 200,00** | **1 100,00** |

*(The “change in inventory” is shown as a negative because it **reduces** the expense side — line `609` Inventories: decrease (increase).)*

**Two rules to remember:**
- A company must **choose a method and apply it consistently**.
- The chosen method **need not match the actual physical flow** of goods (LIFO is an accounting fiction, not a warehouse rule).
- In *rising* prices: **FIFO → highest profit, LIFO → lowest profit**, weighted averages in between.

---

## 9. The Market Test

> **The lower-of-cost-or-market rule.** If the **market value** of closing inventory falls **below** its **cost of acquisition** (per the method chosen), value it at **market value**. Driven by the **prudence principle** — never overstate an asset.

**Always compare** closing-inventory-at-cost vs market value; **the lowest prevails.**

**Continuing OMEGA KAPPA (FIFO chosen).** FIFO cost of closing = 1 600. But at year-end market price is only **14,00/unit** → 80 × 14 = **1 120,00**. Market (1 120) < cost (1 600) → **use 1 120**.

- Change in inventory now = 1 120 − 1 000 = **+120,00** (not +600).

```
31/12  340   Inventory of GFR – Cost of acquisition   120,00
       @ 6094 Changes in inventories of GFR                        120,00
             (DIV 20X0/… – change in inventory)
```

- Closing inventory (BS) = **1 120,00** · COGS (IS) = 1 000 + 3 200 − 1 120 = **3 080,00**.

> The market test doesn't need a special account — you simply record the change using the **lower** closing value.

---

## 10. Write-offs on Inventory

A **write-off** is a *further* value reduction for causes like **obsolescence** or **physical deterioration** (or an expected future price fall). Unlike the market test, it uses a **separate contra-asset account** so the gross cost and the reduction both stay visible.

- Value of inventory **↓** → **`349` Inventory of GFR – Amounts written off (−)** (a **contra-asset**, credit).
- Operating expenses **↑** → **`6310` Amounts written off inventories – Increase** (an **expense**, debit).

**Worked — VICTORIA plc (31/12/20X0), goods for resale (WAP method):**
Opening inventory 150 000; closing at cost 200 000; **market value 185 000**; a *further* decline to 160 000 is expected.

**Step 1 — record the change in inventory, applying the market test** (market 185 000 < cost 200 000 → use 185 000). Change = 185 000 − 150 000 = **+35 000**:

```
31/12  340   Inventory of GFR – Cost of acquisition   35 000,00
       @ 6094 Changes in inventories of GFR                        35 000,00
```

**Step 2 — record the write-off** for the expected further decline to 160 000, i.e. 185 000 − 160 000 = **25 000**:

```
31/12  6310  Amounts written off inventories – Increase   25 000,00
       @ 349  Inventory of GFR – Amounts written off (−)                25 000,00
```

After both entries the **net book value** of inventory = 185 000 − 25 000 = **160 000,00**.

> **Market test vs write-off:** the market test sets the *cost* value on `340` to the lower of cost/market; a **write-off** is an *extra* prudence reduction parked in `349`, keeping the gross `340` figure intact.

---

## 11. Manufactured Inventories & Contracts in Progress

For a company that *makes* things (not just resells), closing inventory is valued at **manufacturing price** (or market if lower). *(Concrete numeric examples: textbook p. 205–213.)*

**Work in progress & finished goods — how much cost goes in?**

| Method | What's included in the manufacturing price |
|---|---|
| **Direct costing** | Only **direct** production costs |
| **Full costing** | **Direct + indirect** production costs |

**Contracts in progress — when is profit recognised?** (manufacturing price **+ gained profit**)

| Method | Profit recognition |
|---|---|
| **Percentage-of-completion** | Profit recognised **as work progresses**, proportional to completion |
| **Completed-contract** | Profit recognised **only at the end** (on delivery) |

**Relevant accounts** (each pairs a `3x` asset with a `7xx` “changes” account):

| Asset | “Changes” account |
|---|---|
| `320` Work in progress | `712` Changes in inventories of WIP |
| `330` Finished goods | `713` Changes in inventories of finished goods |
| `370` Contracts in progress – cost of acquisition | `7170` Changes … CIP – cost of acquisition |
| `371` Contracts in progress – attributed profit | `7171` Changes … CIP – attributed profit |

---

## 12. Guided Practice — Worked Example (SPRITZ plc)

> A **new** dataset so you actually practise. Work each method, then check. (`340`/`6094`, goods for resale, VAT ignored — inventory is recorded excl. VAT.)

**SPRITZ plc — one item of goods for resale:**

| Date | Movement | Units | Price/unit | Total |
|---|---|--:|--:|--:|
| 01/01 | Opening inventory | 50 | 8,00 | 400,00 |
| 10/03 | **Purchase** | 100 | 10,00 | 1 000,00 |
| 15/05 | Sale | 80 | 18,00 | — |
| 12/09 | **Purchase** | 50 | 12,00 | 600,00 |
| 20/11 | Sale | 40 | 22,00 | — |

**Same under every method:** closing units = 50 + 150 − 120 = **80** · Purchases = **1 600** · Sales revenue = 80×18 + 40×22 = **2 320** · Opening = **400**.

### FIFO

Closing 80 units from newest: 50 @ 12 (600) + 30 @ 10 (300) = **€900**. Change = 900 − 400 = **+500**.
```
340   Inventory of GFR – Cost of acquisition   500,00
@ 6094 Changes in inventories of GFR                       500,00
```
COGS = 400 + 1 600 − 900 = **1 100** · Operating profit = 2 320 − 1 100 = **1 220**.

### LIFO (step by step)

| After… | Stock |
|---|---|
| Opening | 50 @ 8 |
| Purchase 100 @ 10 | 50 @ 8 + 100 @ 10 |
| Sale 80 | sell newest 80 @ 10 → 50 @ 8 + **20 @ 10** |
| Purchase 50 @ 12 | 50 @ 8 + 20 @ 10 + 50 @ 12 |
| Sale 40 | sell newest 40 @ 12 → 50 @ 8 + 20 @ 10 + **10 @ 12** |

Closing = 50×8 + 20×10 + 10×12 = 400 + 200 + 120 = **€720**. Change = **+320**.
```
340   Inventory of GFR – Cost of acquisition   320,00
@ 6094 Changes in inventories of GFR                       320,00
```
COGS = 400 + 1 600 − 720 = **1 280** · Operating profit = 2 320 − 1 280 = **1 040**.

### Overall weighted average

Total available = (50 + 150) units = 200; value 400 + 1 600 = 2 000 → WAP = **€10,00/unit**.
Closing = 80 × 10 = **€800**. Change = **+400**.
```
340   Inventory of GFR – Cost of acquisition   400,00
@ 6094 Changes in inventories of GFR                       400,00
```
COGS = 400 + 1 600 − 800 = **1 200** · Operating profit = 2 320 − 1 200 = **1 120**.

**SPRITZ summary:** FIFO profit 1 220 > WAP 1 120 > LIFO 1 040 — the familiar rising-price pattern.

---

## 13. Interactive Practice Section

> ✍️ Try each **before** looking at [§14 Solutions](#14-solutions--explanations). Show your working: closing value → change → journal entry. Difficulty rises.

### Level 1 — Basic recall

**Q1.** During the year, where are (a) purchases and (b) sales recorded? (c) What happens to the inventory account `340` during the year?

**Q2.** Write the cost-of-goods-sold identity in terms of opening inventory, purchases and closing inventory.

**Q3.** In a period of **rising** prices, which method gives the **highest** profit and which the **lowest**? Why?

**Q4.** What is the difference between the **market test** and a **write-off** — which accounts does each use?

### Level 2 — Single-method calculations

Use this dataset for Q5–Q8 — **NEGRONI plc**, one item of goods for resale:

| Date | Movement | Units | Price/unit |
|---|---|--:|--:|
| 01/01 | Opening | 40 | 5,00 |
| 01/04 | Purchase | 60 | 7,00 |
| 01/07 | Sale | 70 | — |
| 01/10 | Purchase | 50 | 9,00 |
| 01/12 | Sale | 30 | — |

**Q5.** How many units are in **closing inventory**? What are total **purchases** (cost)?

**Q6.** Value closing inventory under **FIFO**. Then write the change-in-inventory entry.

**Q7.** Value closing inventory under **LIFO** (show the step-by-step layers). Then write the entry.

**Q8.** Value closing inventory under the **overall weighted average** method. Then write the entry.

### Level 3 — Change, COGS and the market test

**Q9.** For NEGRONI under **FIFO**, compute the **cost of goods sold** (opening = 40 × 5 = 200).

**Q10.** NEGRONI has chosen **FIFO** (closing at cost from Q6). At year-end the market value is **€8,00/unit**. Apply the **market test**: what closing value goes on the balance sheet, and write the change-in-inventory entry.

**Q11.** A company's closing inventory at cost (WAP) is **€60 000**; market value is **€66 000**. Which value is used, and why? (No entry needed — just state the rule.)

### Level 4 — Write-offs & scenarios

**Q12.** At 31/12, MARTINI plc (goods for resale, WAP): opening inventory **€80 000**, closing at cost **€110 000**, market value **€100 000**. (a) Write the change-in-inventory entry (apply the market test). (b) A further decline to **€92 000** is expected — write the write-off entry. (c) What is the net book value of inventory afterwards?

**Q13.** Explain, for manufactured goods, the difference between **direct costing** and **full costing**; and for contracts in progress, between **percentage-of-completion** and **completed-contract**.

**Q14 (full method comparison).** Using **NEGRONI plc** (Q5 data), and given sales revenue of **70 × 12 + 30 × 15 = €1 290**, build the comparison table (Sales, COGS, Operating profit, Closing inventory) for **FIFO, LIFO and overall WAP**. Which method reports the most profit, and does that reflect a real difference in performance?

---

## 14. Solutions & Explanations

### Level 1

**A1.** (a) Purchases → **expense** account `604`. (b) Sales → **revenue** account `70`. (c) `340` is **left unchanged** during the year — it keeps its opening balance until the year-end change-in-inventory entry.

**A2.** **COGS = Opening inventory + Purchases − Closing inventory.**

**A3.** **FIFO** highest profit, **LIFO** lowest. With rising prices, FIFO leaves the newest (dearest) units in stock (high closing inventory → low COGS → high profit); LIFO leaves the oldest (cheapest) units in stock (low closing inventory → high COGS → low profit).

**A4.** The **market test** values closing inventory at the **lower of cost or market** and records it through the normal change entry on `340`/`6094` (no special account). A **write-off** is an *additional* prudence reduction (obsolescence, deterioration, expected decline) booked to `6310` (expense, debit) against `349` (contra-asset, credit), leaving the gross `340` intact.

### Level 2 — NEGRONI plc

**A5.** Closing units = 40 + (60 + 50) − (70 + 30) = **50 units**. Purchases (cost) = 60 × 7 + 50 × 9 = 420 + 450 = **€870**.

**A6. FIFO.** Closing 50 units from newest: 50 @ 9 = **€450**. Opening = 40 × 5 = 200 → change = 450 − 200 = **+250**.
```
340   Inventory of GFR – Cost of acquisition   250,00
@ 6094 Changes in inventories of GFR                       250,00
```

**A7. LIFO** (step by step):
| After… | Stock |
|---|---|
| Opening | 40 @ 5 |
| Purchase 60 @ 7 | 40 @ 5 + 60 @ 7 |
| Sale 70 | sell newest 60 @ 7 + 10 @ 5 → **30 @ 5** |
| Purchase 50 @ 9 | 30 @ 5 + 50 @ 9 |
| Sale 30 | sell newest 30 @ 9 → 30 @ 5 + **20 @ 9** |

Closing = 30 × 5 + 20 × 9 = 150 + 180 = **€330**. Change = 330 − 200 = **+130**.
```
340   Inventory of GFR – Cost of acquisition   130,00
@ 6094 Changes in inventories of GFR                       130,00
```

**A8. Overall WAP.** Available = 40 + 110 = 150 units; value 200 + 870 = 1 070 → WAP = 1 070 / 150 = **€7,1333/unit** (≈ 7,13). Closing = 50 × 7,1333 = **€356,67**. Change = 356,67 − 200 = **+156,67**.
```
340   Inventory of GFR – Cost of acquisition   156,67
@ 6094 Changes in inventories of GFR                       156,67
```
*(Round to the cent, as the course does.)*

### Level 3

**A9.** FIFO COGS = Opening 200 + Purchases 870 − Closing 450 = **€620**.

**A10.** FIFO cost of closing = 450; market = 50 × 8 = **400**. Market < cost → use **€400**. Change = 400 − 200 = **+200**.
```
340   Inventory of GFR – Cost of acquisition   200,00
@ 6094 Changes in inventories of GFR                       200,00
```

**A11.** Use **€60 000** (the cost). Market (66 000) is *higher* than cost, so the lower-of-cost-or-market rule keeps the asset at cost — prudence forbids writing an asset *up* above cost here.

### Level 4

**A12 — MARTINI plc.**
(a) Market test: market 100 000 < cost 110 000 → closing = **100 000**. Change = 100 000 − 80 000 = **+20 000**.
```
340   Inventory of GFR – Cost of acquisition   20 000,00
@ 6094 Changes in inventories of GFR                       20 000,00
```
(b) Write-off for expected decline to 92 000: 100 000 − 92 000 = **8 000**.
```
6310  Amounts written off inventories – Increase   8 000,00
@ 349  Inventory of GFR – Amounts written off (−)              8 000,00
```
(c) Net book value = 100 000 − 8 000 = **€92 000**.

**A13.** **Direct costing** includes only *direct* production costs in the manufacturing price; **full costing** includes *both direct and indirect* production costs (so full costing gives a higher inventory value). For contracts in progress, **percentage-of-completion** recognises profit *gradually as the work progresses*; **completed-contract** recognises profit *only at delivery/completion*.

**A14 — NEGRONI comparison.** Opening = 200; Purchases = 870; Sales = 1 290. COGS = 200 + 870 − closing.

| | FIFO | Overall WAP | LIFO |
|---|--:|--:|--:|
| Sales | 1 290,00 | 1 290,00 | 1 290,00 |
| Closing inventory | 450,00 | 356,67 | 330,00 |
| COGS (200 + 870 − closing) | 620,00 | 713,33 | 740,00 |
| **Operating profit** | **670,00** | **576,67** | **550,00** |

**FIFO** reports the most profit — but this is **not** a real difference in performance. The company sold identical goods for identical cash; only the *accounting assumption* about which units remain differs. FIFO's higher profit comes from leaving the dearer, newer units in stock (a bookkeeping choice), not from trading better.

---

## 15. Quick Check / Active Recall

Cover the answers; say each out loud.

1. During the year, the inventory account `340` is → *left unchanged*; the change is booked → *at year-end*.
2. COGS = → *Opening + Purchases − Closing*.
3. Change-in-inventory entry when stock **rises** → *340 D / 6094 C*.
4. FIFO: closing stock is valued from the → *most recent* purchases.
5. LIFO: closing stock is valued from the → *earliest* purchases (work step by step!).
6. Overall WAP price = → *(opening value + all purchases) ÷ (opening + all units)*.
7. Moving WAP: recompute the average → *after each purchase*.
8. Rising prices: highest profit → *FIFO*; lowest profit → *LIFO*.
9. Market test: use the → *lower* of cost or market (prudence).
10. Write-off accounts → *6310 (expense, D) / 349 (contra-asset, C)*.
11. Full costing includes → *direct + indirect* production costs; direct costing → *direct only*.
12. Contracts in progress, profit as work proceeds → *percentage-of-completion*.

---

## 16. Common Mistakes

| ❌ Mistake | ✅ Fix / why |
|---|---|
| Touching `340` **during** the year on each sale/purchase | `340` moves **only at year-end**; purchases → `604`, sales → `70` all year. |
| **LIFO grabbed straight from the end** without step-by-step layers | Trace stock **at every sale** — an early layer may already be gone. |
| Valuing closing stock at the **selling price** | Inventory is valued at **cost of acquisition** (or lower market), never at sales price. |
| Forgetting the **market test** | Always compare closing-at-cost vs market; **the lower prevails** (prudence). |
| Confusing **market test** and **write-off** | Market test → value on `340` at lower of cost/market. Write-off → extra reduction via `6310`/`349`. |
| Booking the **change** on the wrong side | Stock **up** → `340` D / `6094` C. Stock **down** → `6094` D / `340` C. |
| Thinking the method must match the **real** flow of goods | It need **not** — LIFO/FIFO are accounting fictions; only *consistency* is required. |
| Overall vs moving WAP mixed up | Overall = one average for the whole period; moving = new average **after each purchase**. |
| Writing an asset **up** above cost when market is higher | Not allowed — the rule is lower-of-cost-or-market, only *downward*. |
| Forgetting VAT is **excluded** from inventory cost | Cost of acquisition excludes **refundable** taxes (VAT). |

---

## 17. Summary Sheet

**The mechanism:** all year — purchases → `604` (expense), sales → `70` (revenue), `340` untouched. **At year-end**, book the change so `340` shows correct closing value and the IS shows correct COGS.

$$\text{COGS} = \text{Opening} + \text{Purchases} - \text{Closing} \qquad \text{Change} = \text{Closing} - \text{Opening}$$

**The one entry (stock up):** `340` D / `6094` C (an increase in stock **reduces** net expense, line `609`). Stock down → reverse.

**Valuing the closing units:**

| Method | Closing units valued from… |
|---|---|
| **FIFO** | most recent purchases |
| **LIFO** | earliest purchases (step by step at each sale) |
| **Overall WAP** | one average = (opening + all purchases value) ÷ total units |
| **Moving WAP** | average recomputed after each purchase |

**Rising prices:** FIFO → highest profit & closing inventory; LIFO → lowest; averages in between. Choose one method, apply **consistently**; it need not match the physical flow.

**Market test:** value at **lower of cost or market** (net realisable value = selling price − completion costs − selling costs). Prudence: only downward.

**Write-off:** obsolescence/deterioration/expected decline → `6310` Amounts written off (expense, D) / `349` Amounts written off (−) (contra-asset, C).

**Manufactured inventory:** direct vs full costing (indirect costs in or out). **Contracts in progress:** percentage-of-completion (profit as you go) vs completed-contract (profit at the end). Accounts: `320`/`712` WIP, `330`/`713` finished goods, `370`/`7170` & `371`/`7171` CIP.

---

### 📚 Where to read & practise more

- **Textbook:** *A Practical Guide to Financial Accounting*, **Chapter 8** (p. 177 → p. 218).
- **Exercises:** 1 *PINA COLADA* (p. 219), 2 *MARGARITA* (p. 220), 3 *BELLINI* (p. 221), 4 *COSMOPOLITAN* (p. 222).

**Drill the three valuations until they're automatic** — compute FIFO, LIFO and weighted average on the same data and watch the profit move. That comparison *is* the chapter. 💪
