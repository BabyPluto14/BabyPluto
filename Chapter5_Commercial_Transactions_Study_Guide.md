# Chapter 5 — Fundamental Commercial Transactions

### A Practice-Focused Study Guide & Workbook

*Course: Internal and External Financial Reporting (Part 1a — Financial Accounting)*
*Based on the lecture slides by V. Ghijselinck, Academic year 2025–2026*
*Textbook reference: “A Practical Guide to Financial Accounting”, Chapter 5 (p. 85 → p. 118)*

> **How to use this guide.** This is a *workbook*, not just notes. This chapter is almost pure **practice** — the whole thing is learning to fill in one invoice scheme and turn it into a journal entry. Keep a pen handy, cover each solution, and *do* the entry before you peek. The running example is **TELEROMEO plc**, a trader of multimedia devices (opening bank €15 000, opening cash €3 000).

---

## 📑 Table of Contents

1. [Topic Overview](#1-topic-overview)
2. [What Counts as a Commercial Transaction](#2-what-counts-as-a-commercial-transaction)
3. [How VAT Really Works (the value chain)](#3-how-vat-really-works)
4. [The Basic Purchase & Sales Invoice](#4-the-basic-purchase--sales-invoice)
5. [The VAT Declaration](#5-the-vat-declaration)
6. [⭐ The Complete Scheme of an Invoice](#6-the-complete-scheme-of-an-invoice)
7. [Commercial Discount](#7-commercial-discount)
8. [Additional Charges](#8-additional-charges)
9. [Financial Discount (the tricky one)](#9-financial-discount)
10. [Credit Notes (incoming & outgoing)](#10-credit-notes)
11. [Modes of Payment](#11-modes-of-payment)
12. [Internal Transfers of Funds](#12-internal-transfers-of-funds)
13. [Guided Practice — Worked Examples](#13-guided-practice--worked-examples-teleromeo-plc)
14. [Interactive Practice Section (Workbook)](#14-interactive-practice-section)
15. [Solutions & Explanations](#15-solutions--explanations)
16. [Quick Check / Active Recall](#16-quick-check--active-recall)
17. [Common Mistakes](#17-common-mistakes)
18. [Summary Sheet](#18-summary-sheet)

---

## 1. Topic Overview

**In one sentence:** this chapter teaches you to record the *everyday buying and selling* of a business — invoices, discounts, credit notes and payments — correctly in the journal and ledger.

Chapter 3 taught you the *machine* (debit/credit, the accounting cycle). Chapter 5 puts real fuel in it: the messy details of actual invoices. An invoice is rarely just “price + VAT”. It can carry a **trade discount**, **transport charges**, a **cash discount for quick payment**, and later a **credit note** if goods come back. Each of these hits a *specific* account.

**What you'll be able to do:**

- Explain the **VAT principle** and record a **VAT declaration**.
- Record **purchase and sales invoices** with **commercial discounts, additional charges and financial discounts**.
- Record **incoming and outgoing credit notes**.
- Record **payments** by **bank, cash and cheque**, and **internal transfers of funds**.
- State the **impact** of each on the balance sheet and income statement.

**Why it matters.** Almost every entry a real bookkeeper makes is a variation of this chapter. Master the **invoice scheme** in §6 and 90% of the work is done — everything else is a small twist on it.

---

## 2. What Counts as a Commercial Transaction

**Commercial transactions** = buying goods/services *for the trading or production process*, and selling goods/services.

> ⚠️ **Buying a fixed asset is NOT a commercial transaction** — that's an *investment* (a machine, building, van). Commercial = the stuff that flows *through* the business.

| Company type | Typically **buys** | Typically **sells** |
|---|---|---|
| Manufacturing | Raw materials & consumables | Finished goods |
| Trading | Goods for resale | Goods for resale |
| Service | Services & other goods | Services |

**Where it lands in the accounts:**

- **Purchases → an expense.**
  - Group **60** *Goods for resale, raw materials & consumables* — purchases that go **directly** into the trading/production process (e.g. `604` purchases of goods for resale).
  - Group **61** *Services and other goods* — purchases that **can't** be ascribed directly (rent, insurance, telephone, internet, office supplies).
- **Sales → a revenue** (group **70**).
- **Changes in the inventory of goods** are handled later as an **end-of-period entry** (Chapter 6) — not here. Here, purchases are simply expensed and sales booked as revenue.

---

## 3. How VAT Really Works

**VAT (value-added tax)** is an **indirect consumer tax**. The key idea: **VAT is entirely at the expense of the final consumer.** Companies merely *collect it on behalf of the tax authorities* — for a company, **VAT is never an expense and never a revenue.** (Rate assumed throughout: **21%**. A company is *not* a final consumer.)

Each company in the chain pays VAT to its supplier (reclaimable) and charges VAT to its customer (payable), then settles only the **difference** — the VAT on the *value it added*. This “netting” collects the tax quickly and fairly.

### The flat-screen-TV chain (worked illustration)

| Stage | Purchase price | VAT to reclaim | Sales price | VAT due | Value added | VAT to tax authorities |
|---|--:|--:|--:|--:|--:|--:|
| Manufacturer | — | — | 1 000,00 | 210,00 | 1 000,00 | **210,00** |
| Wholesaler | 1 000,00 | 210,00 | 1 500,00 | 315,00 | 500,00 | **105,00** |
| Retailer | 1 500,00 | 315,00 | 1 900,00 | 399,00 | 400,00 | **84,00** |
| Consumer | 1 900,00 | — | — | — | — | pays **399,00** in total |

Read the wholesaler's row: it owes the tax office `315 − 210 = 105`, which is exactly 21% of its `500` value added. Add up what every stage remits: `210 + 105 + 84 = 399` — precisely the VAT the **consumer** paid. The tax reaches the government in stages, but the **consumer bears all of it.**

> **The two VAT accounts (memorise):**
> - **411 VAT to reclaim** = VAT paid to your supplier → you'll reclaim it → an **ASSET** (debit).
> - **451 VAT due** = VAT charged to your customer → you owe the tax office → a **LIABILITY** (credit).

---

## 4. The Basic Purchase & Sales Invoice

Before any discounts, learn the two skeletons cold. (`604` purchases, `70` sales, `411`/`451` VAT, `440` suppliers, `400` trade debtors.)

**Purchase invoice** — *buy at €1 000 excl. 21% VAT:*

| No. | Account | Type | Debit | Credit |
|---|---|---|--:|--:|
| 604 | Purchases of goods for resale | **D + E** | 1 000,00 | |
| 411 | VAT to reclaim | **D + A** | 210,00 | |
| 440 | @ Suppliers | **C + L** | | 1 210,00 |

**Sales invoice** — *sell at €1 500 excl. 21% VAT:*

| No. | Account | Type | Debit | Credit |
|---|---|---|--:|--:|
| 400 | Trade debtors | **D + A** | 1 815,00 | |
| 70 | @ Sales of goods for resale | **C + R** | | 1 500,00 |
| 451 | @ VAT due | **C + L** | | 315,00 |

The little codes (**D + E** = debit, an expense increasing; **C + L** = credit, a liability increasing) are worth writing next to every line — they are your proof the entry is right.

---

## 5. The VAT Declaration

At regular intervals (monthly/quarterly) the company files a **VAT declaration** and settles with the tax office. Accounting-wise you **close the two VAT accounts against each other**:

1. Compare the balances of **411 VAT to reclaim** and **451 VAT due**.
2. **Close the account with the *smaller* balance** and transfer it to the account with the larger balance.
3. Whatever remains is the **net VAT payable (or receivable)**, which you then pay/collect.

**Example.** Say `411` has a debit balance of `210` and `451` a credit balance of `315`.

**Entry (VAT declaration, diverse document DIV):**

```
31/10  451  VAT due            210,00
       @ 411 VAT to reclaim               210,00
             (DIV 20X0/… – VAT declaration)
```

Now `451` still has a `315 − 210 = 105` credit balance → **net VAT of €105 is payable.**

**Entry (payment of VAT due):**

```
07/11  451  VAT due            105,00
       @ 5500 Bank account                  105,00
             (C/A 20X0/… – pay VAT)
```

If instead `411` were larger, you'd have a **VAT receivable** and eventually get a refund.

---

## 6. ⭐ The Complete Scheme of an Invoice

This is the **single most important thing in the chapter.** Every invoice — purchase or sale, with any mix of discounts and charges — is built from this ladder. Learn the order; it never changes.

```
    Price of the goods
  − Commercial discount        → contra account 608 (buy) / 708 (sell)
  + Additional charges         → raises the goods account (604 / 70)
  = NET amount invoice         → booked to 604 (buy) / 70 (sell)
  − Financial discount         → 757 (buy) / 657 (sell) — but ONLY at payment
  = Basis for VAT              ← VAT is ALWAYS computed on THIS line
  + VAT                        → 411 (buy) / 451 (sell)
  = TOTAL amount invoice (if quick payment)
    TOTAL amount invoice (if NO quick payment)   → 440 (buy) / 400 (sell)
```

**Three things that trip everyone up — read twice:**

1. **VAT is calculated on the “Basis for VAT”**, i.e. *after* the financial discount is deducted — **whether or not the customer actually takes that discount.** (This is a legal rule.)
2. The **financial discount is NOT booked when the invoice is recorded.** The goods account (604/70) is booked at the **NET amount**; the supplier/debtor (440/400) is booked at the **“if NO quick payment” total**. The discount (757/657) only appears **when payment happens** (and only if taken).
3. **Commercial discount** *is* booked at invoice time (contra account 608/708) and **additional charges** simply increase the net — both feed the “Basis for VAT”.

**Where each piece is classified in the income statement:**

| Item | Purchase invoice | Sales invoice | Why |
|---|---|---|---|
| **Commercial discount** | `608` Discounts received (−) → **operating** | `708` Discounts granted (−) → **operating** | Tied to normal trading activity |
| **Additional charges** | into `604` → **operating expense ↑** | into `70` → **operating revenue ↑** | Direct buying/selling cost |
| **Financial discount** | `757` Financial discounts received → **financial revenue** | `657` Financial discounts granted → **financial expense** | Tied to *payment timing* — a financing decision |

---

## 7. Commercial Discount

> **Commercial (trade) discount** — a reduction on the price itself: to boost sales, for large quantities, to promote a product, for damaged goods, or for a valued customer.

Because it relates to **normal trading activity**, it lands in the **operating** result:
- Purchase invoice → **608 Discounts received (−)** (reduces the operating *expense*).
- Sales invoice → **708 Discounts granted (−)** (reduces the operating *revenue*).

There are **two acceptable methods** (the course shows both):

**Method A — separate contra account (primary).** Book the goods at *gross* price and the discount separately.

```
01/10  604  Purchases of goods for resale   2 000,00
       411  VAT to reclaim                     399,00
       @ 608 Discounts received (−)                       100,00
       @ 440 Suppliers                                  2 299,00
             (PI 20X0/001, 10 smartphones, 5% trade disc.)
```

**Method B — netted (alternative).** Book the goods straight at the *net* price (1 900), no 608 line. Same VAT (399) and same supplier total (2 299).

Either is correct; Method A keeps the discount visible. *(VAT is 21% of the net 1 900 = 399 in both.)*

---

## 8. Additional Charges

> **Additional charges** — direct buying/selling costs added on the invoice: transport, loading/unloading, lost packaging, insurance.

Treatment: they **increase the operating result** — folded into the **net** amount:
- Purchase → **operating expense ↑** (added into `604`).
- Sale → **operating revenue ↑** (added into `70`).

They sit **above** the “Basis for VAT”, so **VAT is charged on them too.**

**Worked (purchase, entry 3):** 20 computers @ €500 = 10 000; −5% commercial = −500; +€50 transport; **net = 9 550**; VAT 21% = 2 005,50; total = 11 555,50.

```
05/10  604  Purchases of goods for resale   9 550,00
       411  VAT to reclaim                   2 005,50
       @ 440 Suppliers                                 11 555,50
             (PI 20X0/002, incl. €50 transport)
```

---

## 9. Financial Discount

> **Financial (cash) discount** — a reduction allowed **if payment is made within a certain time limit** (e.g. “3% if paid within 10 days”). Its purpose is to collect money *faster*.

Because it relates to **payment terms** (a *financing* decision, not the trade itself), it lands in the **financial** result:
- Purchase → **757 Financial discounts received** → **financial revenue** (you earned it by paying early).
- Sale → **657 Financial discounts granted** → **financial expense** (it cost you to get paid early).

### The two golden rules

1. **VAT is calculated on the amount *after* the financial discount** — even if the customer never takes it.
2. **The discount is booked only at payment time**, and only if actually taken. At invoice time you ignore it (except for computing the VAT basis).

**Worked — purchase with 3% cash discount (entry 5):** 20 computers @ €500 = 10 000 net; financial discount 3% = 300; **basis for VAT = 9 700**; VAT = 2 037; total-if-quick = 11 737; **total-if-NOT-quick = 12 037**.

*Invoice entry — book goods at net, supplier at the “no quick payment” total:*

```
09/10  604  Purchases of goods for resale  10 000,00
       411  VAT to reclaim                   2 037,00
       @ 440 Suppliers                                 12 037,00
             (PI 20X0/003, 3% disc. if paid ≤10 days)
```

*Payment within 10 days (entry 6) — now the discount appears as financial revenue:*

```
15/10  440  Suppliers                       12 037,00
       @ 5500 Bank account                              11 737,00
       @ 757  Financial discounts received                 300,00
             (C/A 20X0/001, paid within 10 days)
```

*If instead paid after 10 days:* `440` 12 037 **@ 5500** 12 037. **No VAT correction is needed** — the VAT stays as originally calculated on the 9 700 basis.

> **Symmetry for a sale:** book `70` at net, `400` at the “no quick payment” total; on collection within the period, debit **657 Financial discounts granted** for the discount.

---

## 10. Credit Notes

A **credit note** corrects an invoice — think “a mini reverse-invoice”. It does a **proportional correction** of everything the original invoice booked.

- **Incoming credit note (ICN)** — you receive it *from your supplier* (you're the buyer). Reasons: you returned purchased goods, or got an extra discount afterwards. → **reverses a purchase.**
- **Outgoing credit note (OCN)** — you draw it up yourself *as the seller*. Reasons: a customer returned goods, or you granted an extra discount afterwards. → **reverses a sale.**

**Incoming credit note (entry 9)** — return 2 damaged smartphones from PI 20X0/001 (200/unit, −5% commercial): net 380, VAT 79,80, total 459,80. Every line is the mirror of a purchase:

```
27/10  440  Suppliers                         459,80
       @ 604 Purchases of goods for resale                380,00
       @ 411 VAT to reclaim                                79,80
             (ICN 20X0/001, 2 smartphones returned)
```

**Outgoing credit note (entry 10)** — grant an extra 5% on SI 20X0/001 (sale of 2 smartphones, price 700): discount 35, VAT 7,35, total 42,35. Mirror of a sale:

```
31/10  70   Sales of goods for resale          35,00
       451  VAT due                              7,35
       @ 400 Trade debtors                                 42,35
             (OCN 20X0/001, extra 5% discount)
```

> Note: on a credit note the amounts flow *back* — the goods/VAT accounts reverse, and the supplier/debtor balance shrinks.

---

## 11. Modes of Payment

Same economic event (settling a debt/receivable), different **account** depending on the instrument. The **accounting document** tells you which.

| Instrument | Document | Collecting a sale (money in) | Paying a purchase (money out) |
|---|---|---|---|
| **Bank account** | current account extract (C/A) | `5500` **Bank** ↑ (debit) | `5500` **Bank** ↓ (credit) |
| **Cash** | cash document (CD) | `570` **Cash at hand** ↑ (debit) | `570` **Cash at hand** ↓ (credit) |
| **Cheque** | cheque | `540` **Amounts overdue & in process of collection** ↑ (debit) | `5501` **Cheques written out** ↑ (credit) |

**The cheque two-step (important).** A cheque isn't cash yet — it must clear:

- **Cheque received (sale).** ① On receipt: `540` D / `400` C. ② When the bank confirms it cleared (C/A): `5500` D / `540` C.
- **Cheque written (purchase).** ① On writing it: `440` D / `5501` C. ② When it's cashed against your account (C/A): `5501` D / `5500` C.

`540` and `5501` are **temporary bridging accounts** that hold the amount between “cheque changes hands” and “money actually moves at the bank”.

---

## 12. Internal Transfers of Funds

An **internal transfer** moves money between the company's *own* financial accounts (e.g. taking cash to the bank). The catch: the two sides happen on **different days** with **different documents** — so we use bridging account **58 Internal transfers of funds** to avoid a timing mismatch.

**Take €2 000 cash to the bank:**

*Day 1 — cash leaves the till (cash document CD, entry 23):*
```
21/11  58   Internal transfers of funds     2 000,00
       @ 570 Cash at hand                              2 000,00
```
*Day 2 — bank confirms the deposit (current account extract, entry 24):*
```
25/11  5500 Bank account                    2 000,00
       @ 58  Internal transfers of funds               2 000,00
```

After both entries, account `58` nets to zero — it existed only to bridge the two days.

---

## 13. Guided Practice — Worked Examples (TELEROMEO plc)

> Cover each solution, fill in the invoice scheme yourself, then check. VAT = 21%.

### Worked Example A — sales invoice with commercial discount

> **03/10** — SI 20X0/001: sell **2 smartphones** at €350/unit excl. VAT, **5% commercial discount**.

**Scheme:** 2 × 350 = 700 · −5% = −35 · net **665** · VAT 139,65 · total **804,65**.

```
03/10  400  Trade debtors                     804,65
       708  Discounts granted (−)              35,00
       @ 70  Sales of goods for resale                   700,00
       @ 451 VAT due                                     139,65
             (SI 20X0/001)
```
✔ Debit 804,65 + 35 = 839,65 = 700 + 139,65 credit. ✅ *(708 is a contra-revenue → debit side.)*

### Worked Example B — sales invoice with additional charges

> **07/10** — SI 20X0/002: sell **5 computers** at €750/unit excl. VAT, **+€50 installation**, **5% commercial discount**.

**Scheme:** 5 × 750 = 3 750 · −5% = −187,50 · +50 · net **3 612,50** · VAT 758,63 · total **4 371,13**.

```
07/10  400  Trade debtors                   4 371,13
       @ 70  Sales of goods for resale                 3 612,50
       @ 451 VAT due                                     758,63
             (SI 20X0/002, incl. €50 installation)
```
> Here the charge is folded straight into the net (revenue ↑). The 5% discount could be shown via 708; the slide nets it here.

### Worked Example C — sale with financial discount + its collection

> **17/10** — SI 20X0/003: sell **3 computers** at €750/unit excl. VAT, **3% cash discount if paid ≤10 days**.
> **25/10** — collected within the period.

**Scheme:** net 2 250 · financial disc. −67,50 · **basis for VAT 2 182,50** · VAT 458,33 · total-if-quick 2 640,83 · **total-if-not 2 708,33**.

*Invoice:*
```
17/10  400  Trade debtors                   2 708,33
       @ 70  Sales of goods for resale                 2 250,00
       @ 451 VAT due                                     458,33
```
*Collection within 10 days — the discount now bites as a financial expense:*
```
25/10  5500 Bank account                    2 640,83
       657  Financial discounts granted        67,50
       @ 400 Trade debtors                               2 708,33
```
> VAT was charged on 2 182,50 even though the goods were 2 250 — because the discount was *offered*. Note `70` is booked at the full net 2 250, not the VAT basis.

### Worked Example D — paying by cheque (two-step)

> **07/11** — PI 20X0/005: buy 5 smartwatches €750 excl. VAT; pay immediately **by cheque**.
> **09/11** — C/A confirms the cheque was cashed.

```
07/11  604  Purchases of goods for resale     750,00
       411  VAT to reclaim                     157,50
       @ 440 Suppliers                                    907,50      (PI 20X0/005)

07/11  440  Suppliers                          907,50
       @ 5501 Bank – Cheques written out                  907,50      (write cheque)

09/11  5501 Bank – Cheques written out         907,50
       @ 5500 Bank – Current account                      907,50      (cheque cashed)
```

### Worked Example E — incoming credit note

> **27/10** — ICN 20X0/001: return 2 smartphones from PI 20X0/001 (200/unit, 5% commercial disc.).

Net 380 · VAT 79,80 · total 459,80. Reverse of a purchase:
```
27/10  440  Suppliers                          459,80
       @ 604 Purchases of goods for resale                380,00
       @ 411 VAT to reclaim                                79,80
             (ICN 20X0/001)
```

---

## 14. Interactive Practice Section

> ✍️ Try each **before** looking at [§15 Solutions](#15-solutions--explanations). Fill in the invoice scheme, then write the full journal entry. VAT = 21%. Difficulty rises.

### Level 1 — Basic recall

**Q1.** Which account, and on which side, records: (a) a commercial discount on a **purchase**; (b) a commercial discount on a **sale**; (c) a financial discount on a **purchase**; (d) a financial discount on a **sale**?

**Q2.** True/false: “Financial discount is deducted *after* VAT is calculated.” Correct it if false.

**Q3.** Is a financial discount an **operating** or a **financial** item? What about a commercial discount? Why the difference?

**Q4.** When you pay a supplier **by cheque**, which account is credited when you *write* the cheque, and which two accounts move when it is later *cashed*?

### Level 2 — Single invoices

**Q5.** PI: buy **8 tablets** at €300/unit excl. VAT, **10% commercial discount**. Write the entry (show the 604/608 method).

**Q6.** SI: sell **4 tablets** at €480/unit excl. VAT, **no discount**. Write the entry.

**Q7.** PI: buy **15 headphones** at €40/unit excl. VAT, **+€30 transport**, no discount. Write the entry.

### Level 3 — Financial discount & VAT declaration

**Q8.** PI: buy goods, net €4 000 excl. VAT, **2% cash discount if paid within 8 days**. (a) Write the invoice entry. (b) Then write the payment entry assuming you **pay within 8 days**.

**Q9.** Same invoice as Q8, but you **pay after 8 days**. Write the payment entry. Is any VAT correction needed?

**Q10.** At quarter-end, `411 VAT to reclaim` has a debit balance of €1 260 and `451 VAT due` a credit balance of €1 890. (a) Write the VAT-declaration entry. (b) How much VAT is payable, and write the payment-by-bank entry.

### Level 4 — Credit notes, payment modes & scenarios

**Q11.** OCN: you grant a customer an extra **5% discount** on a prior sale whose goods were priced at €1 200 (excl. VAT). Write the outgoing credit note.

**Q12.** ICN: you return goods to a supplier; the original purchase net was €900 excl. VAT. Write the incoming credit note.

**Q13.** You receive a customer's cheque for a €605 receivable. Write (a) the entry on receipt and (b) the entry when the bank confirms it cleared.

**Q14.** Internal transfer: you withdraw €1 500 from the bank to top up the cash till. Write both entries (bank side and cash side) using account 58.

**Q15 (mini-cycle).** **GRASSHOPPER plc** (trader), VAT 21%:
1. 02/12 — PI: buy 10 speakers @ €150 excl. VAT, **5% commercial discount**, on credit.
2. 05/12 — SI: sell 6 speakers @ €260 excl. VAT, **+€20 delivery charge**, on credit.
3. 09/12 — pay the PI of (1) in full by bank.
4. 12/12 — the customer of (2) pays in full by bank.

Tasks: (a) journal-entry all four events; (b) what is the effect on the **operating result** so far (revenues − expenses, ignoring inventory)?

**Q16 (financial-discount scenario).** SI: sell goods net €5 000 excl. VAT, **3% cash discount if paid within 10 days**. (a) invoice entry; (b) the customer pays on day 6 — collection entry; (c) name and classify the account that carries the €150.

---

## 15. Solutions & Explanations

### Level 1

**A1.** (a) **608 Discounts received (−)**, credit side (reduces the purchase expense). (b) **708 Discounts granted (−)**, debit side (reduces sales revenue). (c) **757 Financial discounts received**, credit (financial revenue). (d) **657 Financial discounts granted**, debit (financial expense).

**A2.** **False.** Financial discount is deducted **before** VAT — VAT is calculated on the *“basis for VAT”* (net − financial discount), whether or not the discount is taken.

**A3.** Financial discount → **financial** result (it's about *payment timing*, a financing decision). Commercial discount → **operating** result (it's part of normal trading). That's why they use different account groups (65/75 vs 60/70).

**A4.** Writing the cheque: credit **5501 Bank – Cheques written out** (debit 440 Suppliers). When cashed: **5501** is debited and **5500 Bank – Current account** is credited.

### Level 2

**A5.** 8 × 300 = 2 400; −10% = −240; net 2 160; VAT 21% of 2 160 = 453,60; total 2 613,60.
```
604  Purchases of goods for resale   2 400,00
411  VAT to reclaim                    453,60
@ 608 Discounts received (−)                      240,00
@ 440 Suppliers                                 2 613,60
```

**A6.** 4 × 480 = 1 920; VAT 403,20; total 2 323,20.
```
400  Trade debtors                   2 323,20
@ 70  Sales of goods for resale                 1 920,00
@ 451 VAT due                                     403,20
```

**A7.** 15 × 40 = 600; +30 transport; net 630; VAT 132,30; total 762,30.
```
604  Purchases of goods for resale     630,00
411  VAT to reclaim                    132,30
@ 440 Suppliers                                   762,30
```

### Level 3

**A8.** Net 4 000; financial disc. 2% = 80; **basis for VAT 3 920**; VAT 823,20; total-if-quick 4 743,20; **total-if-not 4 823,20**.
(a) Invoice — goods at net, supplier at the “no quick payment” total:
```
604  Purchases of goods for resale   4 000,00
411  VAT to reclaim                    823,20
@ 440 Suppliers                                 4 823,20
```
(b) Payment within 8 days:
```
440  Suppliers                       4 823,20
@ 5500 Bank account                             4 743,20
@ 757  Financial discounts received                80,00
```

**A9.** Payment after 8 days — discount lost, pay the full supplier balance:
```
440  Suppliers                       4 823,20
@ 5500 Bank account                             4 823,20
```
**No VAT correction is needed** — VAT stays on the 3 920 basis originally recorded.

**A10.** (a) `451` (1 890) is larger, so close `411` (1 260) into it:
```
451  VAT due                         1 260,00
@ 411 VAT to reclaim                            1 260,00
```
(b) Remaining `451` = 1 890 − 1 260 = **€630 payable**:
```
451  VAT due                           630,00
@ 5500 Bank account                               630,00
```

### Level 4

**A11.** Discount 5% of 1 200 = 60; VAT 12,60; total 72,60. Outgoing credit note (reverse of sale):
```
70   Sales of goods for resale          60,00
451  VAT due                            12,60
@ 400 Trade debtors                                72,60
```

**A12.** Net 900; VAT 189; total 1 089. Incoming credit note (reverse of purchase):
```
440  Suppliers                       1 089,00
@ 604 Purchases of goods for resale               900,00
@ 411 VAT to reclaim                              189,00
```

**A13.** (a) On receipt of cheque:
```
540  Amounts overdue & in process of collection  605,00
@ 400 Trade debtors                                        605,00
```
(b) When cleared (C/A):
```
5500 Bank account                     605,00
@ 540 Amounts overdue & in process of collection          605,00
```

**A14.** Money leaves the bank first, arrives in cash after — bridge with 58:
```
58   Internal transfers of funds     1 500,00      (C/A – withdrawal)
@ 5500 Bank account                             1 500,00

570  Cash at hand                    1 500,00      (CD – cash received)
@ 58  Internal transfers of funds               1 500,00
```

**A15 — GRASSHOPPER plc.**
(1) 10 × 150 = 1 500; −5% = −75; net 1 425; VAT 299,25; total 1 724,25.
```
02/12  604  Purchases of goods for resale   1 500,00
       411  VAT to reclaim                     299,25
       @ 608 Discounts received (−)                        75,00
       @ 440 Suppliers                                  1 724,25
```
(2) 6 × 260 = 1 560; +20 delivery; net 1 580; VAT 331,80; total 1 911,80.
```
05/12  400  Trade debtors                   1 911,80
       @ 70  Sales of goods for resale                 1 580,00
       @ 451 VAT due                                     331,80
```
(3) Pay PI by bank:
```
09/12  440  Suppliers                       1 724,25
       @ 5500 Bank account                              1 724,25
```
(4) Collect SI by bank:
```
12/12  5500 Bank account                    1 911,80
       @ 400 Trade debtors                              1 911,80
```
(b) **Operating result** = revenue − expense = (Sales 1 580) − (Purchases 1 500 − Discounts received 75) = 1 580 − 1 425 = **€155**. *(VAT never touches the result; payments just move assets/liabilities.)*

**A16.** Net 5 000; financial disc. 3% = 150; **basis for VAT 4 850**; VAT 1 018,50; total-if-quick 5 868,50; total-if-not 6 018,50.
(a) Invoice:
```
400  Trade debtors                   6 018,50
@ 70  Sales of goods for resale                 5 000,00
@ 451 VAT due                                   1 018,50
```
(b) Collection on day 6 (within period):
```
5500 Bank account                    5 868,50
657  Financial discounts granted       150,00
@ 400 Trade debtors                             6 018,50
```
(c) The €150 sits in **657 Financial discounts granted** — a **financial expense** (it cost the company to be paid early).

---

## 16. Quick Check / Active Recall

Cover the answers; say each out loud.

1. VAT to reclaim (411) is a(n) → *asset* (debit). VAT due (451) is a(n) → *liability* (credit).
2. For a company, VAT is → *neither an expense nor a revenue* — it flows through.
3. Commercial discount on a purchase → *608 Discounts received (−)*; on a sale → *708 Discounts granted (−)*.
4. Financial discount on a purchase → *757 (financial revenue)*; on a sale → *657 (financial expense)*.
5. VAT is calculated on the → *“Basis for VAT”* = net **minus** financial discount.
6. The financial discount is booked → *at payment time only* (if taken).
7. Additional charges (transport) → *raise the net*, so they *are* subject to VAT.
8. Incoming credit note reverses a → *purchase*; outgoing credit note reverses a → *sale*.
9. Cheque **received** sits in → *540*; cheque **written out** sits in → *5501*; until they clear at *5500*.
10. Internal transfer bridging account → *58*.
11. Cash at hand account → *570*.
12. VAT declaration: close the account with the → *smaller* balance into the larger.

---

## 17. Common Mistakes

| ❌ Mistake | ✅ Fix / why |
|---|---|
| Calculating **VAT on the net before the financial discount** | VAT is on the **“basis for VAT”** = net **minus** financial discount, taken or not. |
| **Booking the financial discount at invoice time** | It's booked **only at payment** (757/657); at invoice the goods go in at net, the supplier/debtor at the “no quick payment” total. |
| Putting **financial discount in the operating result** | It's a **financial** item (payment timing): 757 revenue / 657 expense. |
| Putting **commercial discount in the financial result** | It's an **operating** item: 608 / 708. |
| Correcting **VAT when a cash discount is *not* taken** | **No VAT correction** — VAT stays on the original basis. |
| Treating a **cheque as immediate cash** | Use the bridge: 540 (received) / 5501 (written) until it clears at 5500. |
| Skipping account **58 on an internal transfer** | The two legs fall on different days — 58 bridges them and nets to zero. |
| Mixing up **608 (contra-expense, credit)** and **708 (contra-revenue, debit)** | Received = you're the buyer (credit 608); granted = you're the seller (debit 708). |
| Recording a **fixed-asset purchase here** | Buying a machine/van is an *investment*, not a commercial transaction. |
| Forgetting **additional charges are taxed** | They sit above the VAT basis, so VAT applies to them. |

---

## 18. Summary Sheet

**The one scheme (memorise the ladder):**
```
  Price of goods − Commercial discount + Additional charges = NET  → 604 / 70
  − Financial discount = BASIS FOR VAT                             → 757 / 657 (at payment only)
  + VAT                                                            → 411 / 451
  = TOTAL (if quick) ／ TOTAL (if not) → 440 / 400
```

**Account map:**

| Item | Buy (purchase) | Sell (sale) | Nature |
|---|---|---|---|
| Goods | **604** Purchases (D, expense) | **70** Sales (C, revenue) | operating |
| Commercial discount | **608** Discounts received (−) (C) | **708** Discounts granted (−) (D) | operating |
| Financial discount | **757** Fin. disc. received (C) | **657** Fin. disc. granted (D) | financial |
| VAT | **411** VAT to reclaim (D, asset) | **451** VAT due (C, liability) | — |
| Counterparty | **440** Suppliers (C) | **400** Trade debtors (D) | — |

**Golden rules:**
- VAT = 21% of the **basis for VAT** (after financial discount), *always*, taken or not.
- Financial discount recognised **only at payment**; no VAT correction if it's lost.
- Commercial discount + additional charges → operating & above the VAT basis.

**Payments:** bank **5500** · cash **570** · cheque received **540** then **5500** · cheque written **5501** then **5500** · internal transfer bridge **58**.

**Credit notes:** ICN reverses a purchase (440 D / 604 C / 411 C) · OCN reverses a sale (70 D / 451 D / 400 C).

**VAT declaration:** compare 411 vs 451, close the smaller into the larger, settle the net by bank.

---

### 📚 Where to read & practise more

- **Textbook:** *A Practical Guide to Financial Accounting*, **Chapter 5** (p. 85 → p. 118).
- **Exercises:** Exercise 1 *AMERICANO* (p. 119), Exercise 2 *BLUE NOTE* (p. 120), Exercise 3 *GRASSHOPPER* (p. 121).

**Keep drilling the invoice scheme** until you can fill the ladder from memory — that single skill carries the whole chapter. 💪
