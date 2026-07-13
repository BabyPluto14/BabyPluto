# Chapter 3 — The Accounting Process

### A Practice-Focused Study Guide & Workbook

*Course: Internal and External Financial Reporting (Part 1a — Financial Accounting)*
*Based on the lecture slides by V. Ghijselinck, Academic year 2025–2026*
*Textbook reference: “A Practical Guide to Financial Accounting”, Chapter 3 (p. 41 → p. 70)*

> **How to use this guide.** This is a *workbook*, not just notes. Read a section, then **do** the practice before peeking at the solutions. Accounting is a skill — like riding a bike, you only learn it by falling off a few times. Keep a pen and paper (or a spreadsheet) next to you and actually write the journal entries out.

---

## 📑 Table of Contents

1. [Topic Overview](#1-topic-overview)
2. [The Big Picture — The Accounting Cycle](#2-the-big-picture--the-accounting-cycle)
3. [The Balance Sheet](#3-the-balance-sheet)
4. [Balance Sheet Accounts (T-accounts & debit/credit rules)](#4-balance-sheet-accounts)
5. [The Income Statement & Its Accounts](#5-the-income-statement--its-accounts)
6. [VAT — The One Thing Students Trip Over](#6-vat--the-one-thing-students-trip-over)
7. [The Chart of Accounts](#7-the-chart-of-accounts)
8. [The General Ledger and the Journal](#8-the-general-ledger-and-the-journal)
9. [The Trial Balance](#9-the-trial-balance)
10. [From Opening to Closing Balance Sheet (the result)](#10-from-opening-to-closing-balance-sheet)
11. [Guided Practice — Full Worked Example (TELECONNECT plc)](#11-guided-practice--the-teleconnect-plc-story)
12. [Interactive Practice Section (Workbook)](#12-interactive-practice-section)
13. [Solutions & Explanations](#13-solutions--explanations)
14. [Quick Check / Active Recall](#14-quick-check--active-recall)
15. [Common Mistakes](#15-common-mistakes)
16. [Summary Sheet](#16-summary-sheet)

---

## 1. Topic Overview

**In one sentence:** the *accounting process* is the step-by-step machine that turns everyday business events (buying furniture, selling phones, paying a bill) into two final reports — the **balance sheet** and the **income statement**.

**What you'll be able to do after this chapter:**

- Read and structure a **balance sheet** (what the company *owns* vs. how it is *financed*).
- Read and structure an **income statement** (what the company *earned* vs. what it *spent*).
- Know **when to debit and when to credit** any account.
- Record real transactions as **T-accounts** and as **journal entries** (this is the core skill — most of your exam marks live here).
- Assign the correct **account numbers** from the chart of accounts.
- Build a **trial balance** and use it to check your work.
- Show how a “balanced” balance sheet is produced at year-end, and where **profit or loss** comes from.

**Why it matters (real-world relevance).** Every company on earth — from a corner sandwich shop to Apple — runs this exact cycle. If you can do the accounting process, you can:

- Understand whether a business is actually making money.
- Spot when the books *don't balance* (a sign of an error or fraud).
- Speak the “language of business” to bankers, tax authorities and investors.

Think of the whole chapter as following **one company (TELECONNECT plc)** through **one year**, from the day it opens its doors to the day it prepares its year-end accounts. Everything else is detail hanging off that story.

---

## 2. The Big Picture — The Accounting Cycle

Before any detail, memorise this flow. Every section below is just *one box* in this diagram.

```
   OPENING BALANCE SHEET
   (open the accounts in the journal + general ledger)
              │
              ▼
   RECORD ALL TRANSACTIONS during the year
   (in the journal and the general ledger)
              │
              ▼
   1st PROVISIONAL TRIAL BALANCE   ← a check: does debit = credit?
              │
              ▼
   INVENTORY  (count reality) → END-OF-PERIOD ENTRIES   [mostly Chapter 6+]
              │
              ▼
   2nd PROVISIONAL TRIAL BALANCE   (determine result BEFORE tax)
              │
              ▼
   TAXES  →  FINAL TRIAL BALANCE
              │
              ▼
   FINANCIAL STATEMENTS
   (Balance sheet + Income statement + Notes)
              │
              ▼
   DISTRIBUTION OF PROFIT AFTER TAX
```

> **Study tip:** In this chapter we mostly stay in the top half (open → record → trial balance → result). The “inventory / end-of-period entries” and “taxes” boxes are developed in later chapters, so here the result we compute is a **profit *before* end-of-period adjustments and tax**.

---

## 3. The Balance Sheet

### 3.1 The core idea

> **A balance sheet is a snapshot (a “photo”) of a company's financial position at *one specific moment* in time.**

It always has two sides that are **equal**:

| **ASSETS** (left) | **EQUITY + LIABILITIES** (right) |
|---|---|
| *Operating resources* — what the company **uses** | *Financing resources* — where the money **came from** |
| “**Use** of funds” | “**Origin** of funds” |

**The fundamental accounting equation:**

$$\boxed{\text{ASSETS} = \text{EQUITY} + \text{LIABILITIES}}$$

Every euro of resource the company controls (an asset) had to be financed by *someone* — either the owner (equity) or a third party the company owes (a liability). That's why the two sides *must* be equal. If they aren't, you made an error.

### 3.2 The sandwich-shop intuition

Imagine you want to open **a sandwich shop**. What do you need?

- A **building**, a **refrigerated counter**, an **oven**, a **van** → big, long-lasting things → **fixed assets** (long-term).
- A **stock of bread**, money in the **bank**, some **cash** in the till → things that turn over quickly → **current assets** (short-term).

That's the **ASSETS** side. Now — *how do you pay for all this?*

- Your **own savings** you put in → **Equity** (permanent; you don't have to pay yourself back on a deadline).
- A **bank loan** → **Liability** (you must repay it).
- Suppliers letting you **pay later** → **Liability** (you owe them).

That's the **EQUITY + LIABILITIES** side. Same total, viewed two ways.

### 3.3 The ordering rule (important for the template we use)

- **Assets** are listed by **increasing degree of liquidity** (how quickly they turn into cash).
  - Least liquid first: *Fixed assets* (building, machines) → *Current assets* (inventory → receivables → bank → **cash last**, because cash is *already* liquid).
- **Equity + Liabilities** are listed by **increasing degree of callability** (how soon you must repay).
  - *Equity* first (never “called” — permanent) → *Liabilities > 1 year* → *Liabilities ≤ 1 year*.

### 3.4 The template balance sheet (with chart-of-account groups)

| **ASSETS** | code | **EQUITY + LIABILITIES** | code |
|---|---|---|---|
| **FIXED ASSETS** | | **EQUITY** | |
| Intangible fixed assets | 21 | Contributions / Capital | 10/11 |
| Tangible fixed assets | 22/27 | Revaluation surpluses | 12 |
| Financial fixed assets | 28 | Reserves | 13 |
| Amounts receivable > 1 year | 29 | Retained profits (losses) | 14 |
| **CURRENT ASSETS** | | **LIABILITIES** | |
| Inventories & contracts in progress | 3 | Provisions for liabilities & expenses | 16 |
| Amounts receivable ≤ 1 year | 40/41 | Amounts payable > 1 year | 17 |
| Current investments | 50/53 | Amounts payable ≤ 1 year | 42/48 |
| Cash at bank and in hand | 54/58 | Accruals and deferrals | 492/3 |
| Accruals and deferrals | 490/1 | | |

Don't memorise every number yet — just notice the **shape**: assets on the left going from “sticky” to “liquid”, financing on the right going from “permanent” to “due soon”.

### 3.5 The golden property: it *stays* balanced

After **every single transaction**, the balance sheet remains balanced:

$$\Delta \text{Assets} = \Delta \text{Equity} + \Delta \text{Liabilities}$$

There are only **four** ways a transaction can move the balance sheet:

| Case | What happens | Example |
|---|---|---|
| ① | Asset ↑ **and** (E+L) ↑ | Buy furniture on credit (furniture ↑, supplier debt ↑) |
| ② | Asset ↓ **and** (E+L) ↓ | Pay a supplier from the bank (bank ↓, supplier debt ↓) |
| ③ | One asset ↑ **and** another asset ↓ | Customer pays you: bank ↑, receivable ↓ |
| ④ | One (E+L) ↑ **and** another (E+L) ↓ | Convert a short-term debt into a long-term loan |

In every case, total assets still equal total equity + liabilities. **This is your #1 self-check.**

---

## 4. Balance Sheet Accounts

We can't redraw the whole balance sheet after every transaction — that would be insane for a company with thousands of transactions. Instead, **each balance sheet item gets its own account**, drawn as a **T-account**.

### 4.1 Anatomy of a T-account

```
      C   Account name   D          ← (in these slides the layout is Credit | Debit,
     ─────────────┬─────────────       but the universal convention is Debit left,
                  │                     Credit right — see the note below)
```

**Universal convention (use this):**

```
        D  |  Account name  |  C
      ─────┼────────────────┼─────
   Left side│                │Right side
   = DEBIT  │                │= CREDIT
```

- **Left side = DEBIT** (abbreviated **D** or **Dr**)
- **Right side = CREDIT** (abbreviated **C** or **Cr**)
- The **collection of all accounts** = the **general ledger**.

> ⚠️ **Notation warning.** The lecture slides sometimes print the T-account header as “**C … D**” (credit on the left of the label, debit on the right). Ignore the visual order of the letters in the header — what matters is the *universal rule*: **debit = left, credit = right**. When you draw your own, always put **debit on the left**.

### 4.2 The debit/credit rules for balance sheet accounts

This is the heart of everything. Learn it cold.

| Account type | Opening balance sits on… | Increase (+) → | Decrease (−) → |
|---|---|---|---|
| **ASSET** account (left side of B/S) | **DEBIT** side | **DEBIT** | **CREDIT** |
| **LIABILITY / EQUITY** account (right side of B/S) | **CREDIT** side | **CREDIT** | **DEBIT** |

**Mnemonic:** *the account “lives” on the same side it appears in the balance sheet.*
- Assets are on the **left** of the balance sheet → assets **increase on the left (debit)**.
- Equity + Liabilities are on the **right** of the balance sheet → they **increase on the right (credit)**.

**The iron law (for every transaction):**

$$\boxed{\text{total DEBIT} = \text{total CREDIT}}$$

This is called **double-entry bookkeeping**. Every entry hits at least two accounts, and the debits always equal the credits. If they don't, stop — you've made a mistake.

### 4.3 The 4-question decision procedure

For **any** transaction, ask these four questions in order. Do this *out loud* until it becomes automatic:

1. **Which accounting document?** (invoice, bank statement…) — this proves the transaction happened.
2. **Which account(s) are affected?** (asset? liability? — later also expense/revenue)
3. **What is the change?** (increase or decrease)
4. **Debit or credit?** (apply the rule from §4.2)

> 💡 Transactions are **numbered** (entry 1, entry 2, …) so you can trace each amount in a T-account back to the event that caused it.

### 4.4 Opening and closing accounts

- **Opening the accounts:** at the start of the period, each account receives its **opening balance (OB)** on its “home” side (assets: debit; E+L: credit). These come straight from the opening balance sheet.
- **Closing / balancing an account:** at the end, you compute the account's **balance** = the difference between the total debit side and the total credit side.
  - Total **debit > credit** → **debit balance (DB)**.
  - Total **credit > debit** → **credit balance (CB)**.
  - **Asset accounts** end with a **debit balance (D > C)**.
  - **Liability / equity accounts** end with a **credit balance (C > D)**.

To *close* an account you insert the balancing figure on the **smaller** side so both sides total to the same amount, then carry that balance to the closing balance sheet.

---

## 5. The Income Statement & Its Accounts

### 5.1 Why we need it

The balance sheet is a *photo* at one moment. But owners want to know: **did we make money over the period?** That's a *film*, not a photo — it's the **income statement** (also called the profit & loss account, P&L).

$$\text{Revenues} - \text{Expenses} = \text{Result (Profit or Loss)}$$

- **Revenues > Expenses → PROFIT**
- **Revenues < Expenses → LOSS**

### 5.2 The categories

A company's activities split into **commercial (operating)** and **financial**, and each into **recurring** and **non-recurring**:

| | Revenues (class 7) | Expenses (class 6) |
|---|---|---|
| **Operating – recurring** | Sales of goods for resale, supply of services | Purchases of goods for resale, electricity/water, wages |
| **Operating – non-recurring** | Gain on disposal of (in)tangible fixed assets | Loss on disposal of fixed assets, fire damage |
| **Financial – recurring** | Interest on current investments | Bank charges, interest on loans |
| **Financial – non-recurring** | Gain on disposal of financial fixed assets | Loss on disposal of financial fixed assets |

### 5.3 The template income statement

```
   Income statement 20X0
     Operating revenues
   − Operating expenses
   = OPERATING PROFIT (LOSS)
   + Financial revenues
   − Financial expenses
   = PROFIT (LOSS) OF THE PERIOD BEFORE TAXES
   − Income taxes on the result
   = PROFIT (LOSS) AVAILABLE FOR APPROPRIATION
```

### 5.4 The debit/credit rules for income statement accounts

Expenses and revenues are recorded in **income statement accounts**. The rules mirror the balance sheet logic:

| Account type | Increase (+) → | Decrease (−) → |
|---|---|---|
| **EXPENSE** account (class 6) | **DEBIT** | credit |
| **REVENUE** account (class 7) | **CREDIT** | debit |

**Mnemonic:** *Expenses are “bad” for profit → they behave like assets (debit to increase). Revenues are “good” → they behave like equity (credit to increase).*

And again, for every entry: **total DEBIT = total CREDIT**.

> **Deeper why:** an expense ultimately reduces equity (profit) and a revenue increases equity. Since equity increases on the credit side, revenues are credited; since expenses reduce equity, they are debited. This is why expenses “point the same way” as assets and revenues “point the same way” as equity.

### 5.5 The updated 4-question procedure

Now question 2 has more options:

1. Which accounting document?
2. Which account — **asset / liability / equity**, or **expense / revenue**?
3. What change — increase or decrease?
4. Debit or credit?

---

## 6. VAT — The One Thing Students Trip Over

VAT (Value Added Tax) confuses everyone at first. Slow down here.

**Big idea:** VAT is a tax on consumption. The company is a **middleman** that collects VAT for the government — the VAT is *not* the company's income or expense. It flows *through* the company.

### 6.1 VAT on a **purchase** (input VAT) → an **ASSET**

- General principle: the company **pays VAT to its supplier** on each purchase.
- The VAT administration will later **refund** that VAT to the company.
- So, until refunded, the company has a **claim / receivable** on the VAT administration.

> **Account “VAT to reclaim” (411) = an ASSET.** It **increases on the DEBIT** side when you buy.

### 6.2 VAT on a **sale** (output VAT) → a **LIABILITY**

- General principle: the **customer pays VAT to the company** on each sale.
- The company must **pay that VAT to the VAT administration**.
- So, until paid, the company has a **debt** to the VAT administration.

> **Account “VAT due” (451) = a LIABILITY.** It **increases on the CREDIT** side when you sell.

### 6.3 The two VAT templates (memorise these!)

**Purchase invoice** (buy goods worth *Net*, VAT rate *r*):

| Account | Type | Debit | Credit |
|---|---|---|---|
| Purchase / asset (the thing bought) | expense or asset | *Net* | |
| VAT to reclaim (411) | asset | *Net × r* | |
| **@ Suppliers (440)** | liability | | *Net × (1 + r)* |

**Sales invoice** (sell goods worth *Net*, VAT rate *r*):

| Account | Type | Debit | Credit |
|---|---|---|---|
| Trade debtors (400) | asset | *Net × (1 + r)* | |
| **@ Sales of goods for resale (70)** | revenue | | *Net* |
| **@ VAT due (451)** | liability | | *Net × r* |

> **Gross = Net + VAT.** With a 21 % rate: VAT = Net × 0.21, and Gross = Net × 1.21. The **supplier** or **customer** always deals in the **gross** (VAT-inclusive) amount; the tax office gets the VAT slice.

---

## 7. The Chart of Accounts

### 7.1 What & why

> A **chart of accounts** is a **structured plan** in which **all accounts are judiciously placed**, that may appear in a particular accounting system.

**Objectives:**
- **Unity** in accounting terminology (everyone uses the same names/numbers).
- To **facilitate auditing (control) and comparison** between companies and years.

It is a **decimal system** — accounts are grouped by their leading digits.

### 7.2 The structure (levels)

| Level | Number of digits | Example |
|---|---|---|
| **Class** | 1 digit | `2` = Fixed assets & receivables > 1 year |
| **Group** | 2 digits | `23` = Plant, machinery and equipment |
| **Account** | 3 digits | `232` = Equipment |
| **Subaccount** | 4 digits | `2320` = Equipment – cost of acquisition |

Sometimes a **specific last digit** carries meaning (e.g. for fixed assets: `…0` = cost of acquisition, `…8` = revaluation surplus, `…9` = depreciation). Sometimes a **specific subaccount** is used (e.g. per bank).

### 7.3 The classes you need for this chapter

| Class | Meaning | B/S or I/S |
|---|---|---|
| **1** | Equity, provisions, amounts payable > 1 year | Balance sheet — E+L |
| **2** | Fixed assets & amounts receivable > 1 year | Balance sheet — Assets |
| **3** | Inventories & contracts in progress | Balance sheet — Assets |
| **4** | Amounts receivable/payable ≤ 1 year (and VAT, accruals) | Balance sheet — both |
| **5** | Current investments & cash at bank and in hand | Balance sheet — Assets |
| **6** | **Expenses** (charges) | Income statement |
| **7** | **Revenues** (income) | Income statement |

Handy sub-splits for the income statement:
- **60/64** operating expenses, **65** recurring financial expenses, **66** non-recurring financial expenses, **67** income taxes, **69** result appropriation (expense side).
- **70/74** operating revenues, **75** recurring financial revenues, **76** non-recurring financial revenues, **77** adjustment of income taxes, **79** result appropriation (revenue side).

### 7.4 The account numbers used in the TELECONNECT example

Keep this table handy — you'll reuse it constantly:

| No. | Account | Type |
|---|---|---|
| **100** | Capital | Equity |
| **140** | Profit carried forward | Equity |
| **173** | Loan FORTIS (amounts payable > 1 year) | Liability |
| **2320** | Equipment | Asset (fixed) |
| **2400** | Furniture | Asset (fixed) |
| **2420** | Desktops | Asset (fixed) |
| **400** | Trade debtors | Asset (receivable ≤ 1 yr) |
| **411** | VAT to reclaim | Asset |
| **416** | Current account manager (other receivable) | Asset |
| **440** | Suppliers | Liability (payable ≤ 1 yr) |
| **451** | VAT due | Liability |
| **489** | Other amounts payable | Liability |
| **5500** | Bank account | Asset (cash) |
| **604** | Purchases of goods for resale | Expense |
| **61…** | Services & other goods (e.g. phone charges) | Expense |
| **6500** | Interests (debt charges) | Expense |
| **693** | Profit to be carried forward | Expense (appropriation) |
| **70** | Sales of goods for resale | Revenue |

---

## 8. The General Ledger and the Journal

Two books, two jobs. You need both.

### 8.1 The general ledger

> **The book in which all T-accounts are kept.** Documents are sorted and logically recorded; each account has a double page — **left = debit** amounts, **right = credit** amounts.

The ledger answers: *“What is the situation of **this one account** (e.g. the bank) right now?”* It's organised **by account**.

### 8.2 The journal

> **The accounting diary** in which the entrepreneur enters **all transactions without delay, faithfully, completely and in time order.**

The journal answers: *“What happened, in **chronological order**?”* It's organised **by date**. It is legally required.

### 8.3 The standardised journal entry

Every journal entry has the same 6 parts:

1. **Date** of the entry
2. **Order number** of the entry
3. **Account numbers**
4. The **actual entry**: *debited accounts* → *“at / @” credited accounts* + a short **description**
5. **Column of debited amounts**
6. **Column of credited amounts**

**Layout (this is what an exam answer should look like):**

```
Date        No.   Acc.no.  Account name                    Debit        Credit
07/01/20X0  (2)   2320     Equipment                      25 000,00
                  411      VAT to reclaim                  5 250,00
                  @ 489    Other amounts payable                        30 250,00
                           (Shop Design, PI …/2)
```

**Rules of thumb for writing a journal entry:**
- **Debited accounts are written first** (flush left), credited accounts underneath, introduced by **“at”/“@”** and usually **indented**.
- The **debit column total = credit column total** for the entry.
- Always add a short **description** naming the document (e.g. `PI 20X0/002`).

---

## 9. The Trial Balance

### 9.1 What it is

> The **trial balance** is an **interim control balance** (a check — *not required by law*) that lists **all** accounts (balance sheet **and** income statement) and verifies the books are internally consistent.

There are two versions:

**(a) Trial balance with footings (“totals”)**
For every account, total the **debit side** and total the **credit side** and put those two totals in the trial balance.
- **Check:** total of the debit-totals column **=** total of the credit-totals column.

**(b) Trial balance with balances**
For every account, compute the **balance** (debit total − credit total) and list it as either a debit balance or a credit balance.
- **Check:** total debit balances **=** total credit balances.
- Closing (balancing) the accounts = producing this version.

### 9.2 Why it's useful

- It's your **error detector**: if debit ≠ credit, you *definitely* made a mistake somewhere (a one-sided entry, a transposed digit, a wrong side).
- ⚠️ But it is **not foolproof**: it will *not* catch errors that keep debit = credit — e.g. posting to the *wrong account*, omitting a transaction *entirely*, or recording it *twice*.

> **Analogy:** the trial balance is like checking that your bank statement's debits and credits add up. It proves the arithmetic is consistent — it does *not* prove you spent the money on the right things.

---

## 10. From Opening to Closing Balance Sheet

This is where balance sheet and income statement finally **link together**.

### 10.1 Inventory & end-of-period entries (preview)

At year-end you take an **inventory**: a detailed statement of all assets, receivables, debts and other liabilities reflecting the **actual** situation. Accounts are then adjusted to match reality via **end-of-period entries** (value decreases/increases, stock changes, provisions, closing VAT accounts, accruals & deferrals…). **Most of this is developed in later chapters** — in this chapter we compute the result *before* these adjustments.

### 10.2 Where the result comes from — two ways, same answer

Once all accounts are closed, the profit (or loss) shows up in **two independent places** that must agree:

**From the income statement accounts:**

```
   Total credit balances (revenues, class 7)   10 200,00
 − Total debit balances (expenses, class 6)    − 7 818,75
 = PROFIT of the accounting period              2 381,25
```

**From the balance sheet accounts:**

```
   Total debit balances (asset accounts)       140 784,25
 − Total credit balances (equity + liability) − 138 403,00
 = PROFIT of the accounting period               2 381,25
```

Both give **€2 381,25**. This is the beautiful self-consistency of double-entry: the profit calculated from “revenues − expenses” **must** equal the profit calculated from “assets − (equity + liabilities before profit)”.

> **The link in one sentence:** the income statement explains *why* equity changed during the year; the profit it computes is exactly the amount needed to make the closing balance sheet balance again.

### 10.3 Appropriation of the result

The profit (or loss) must be “given a home” — this is **appropriation**:

- **In case of PROFIT**, the balance to appropriate can be:
  - **Added to equity** (reserves),
  - **Carried forward** to next year (profit carried forward),
  - **Distributed** to partners (a debt from profit appropriation).
- **In case of LOSS**, the balance can be:
  - **Withdrawn from equity** (contributions ↓),
  - **Carried forward** (loss carried forward),
  - Covered by an **intervention of partners** (a receivable).

**Example entry (carry the whole profit forward):**

```
No.   Acc.no.  Account                          Debit       Credit
      693      Profit to be carried forward    2 381,25
      @ 140    Profit carried forward                       2 381,25
```

This moves the profit out of the income statement (via the 69-group “appropriation” expense account) into an **equity** account (140) on the balance sheet — closing the loop.

---

## 11. Guided Practice — the TELECONNECT plc story

We now follow **TELECONNECT plc** through year 20X0. **Read each entry, cover the solution, and try it yourself first.** VAT rate throughout = **21 %**.

### 11.0 Opening balance sheet (01/01/20X0)

The company starts with capital of €75 000 deposited in the bank.

| ASSETS | | EQUITY + LIABILITIES | |
|---|---|---|---|
| Bank account (5500) | 75 000,00 | Capital (100) | 75 000,00 |
| **TOTAL** | **75 000,00** | **TOTAL** | **75 000,00** |

**Opening journal entry:**

```
01/01  5500  Bank account          75 000,00
       @ 100 Capital                            75 000,00
             (opening of accounts)
```

---

### 11.1 Worked Example A — a purchase invoice with VAT

> **05/01/20X0** — Purchase invoice **PI 20X0/001** from supplier **FURNIFIT plc** for office **furniture**: **10 000,00 EUR excl. 21 % VAT**. Payable 10 days after invoice date.

**Step-by-step reasoning:**

1. *Document?* Purchase invoice PI 20X0/001. ✔
2. *Which accounts?*
   - Furniture → **asset** (2400)
   - VAT we paid the supplier → **VAT to reclaim**, an **asset** (411)
   - We haven't paid yet → we owe the supplier → **Suppliers**, a **liability** (440)
3. *What change?* Furniture ↑, VAT to reclaim ↑, Suppliers ↑.
4. *Debit/credit?* Assets ↑ → **debit**; liability ↑ → **credit**.

**Amounts:** Net 10 000 → VAT = 10 000 × 21 % = 2 100 → Gross = 12 100.

**Journal entry:**

```
05/01  2400  Furniture             10 000,00
       411   VAT to reclaim         2 100,00
       @ 440 Suppliers                          12 100,00
             (FURNIFIT, PI 20X0/001)
```

✔ Check: debit 10 000 + 2 100 = 12 100 = credit. **Balanced.** ✅

---

### 11.2 Worked Example B — paying a supplier

> **12/01/20X0** — Bank statement **C/A 20X0/002**: payment of PI 20X0/001 to FURNIFIT plc by bank transfer, **12 100,00 EUR**.

**Reasoning:** We use money from the bank (asset ↓) to reduce what we owe the supplier (liability ↓). This is **case ②** (asset ↓ and liability ↓).

- Bank account (5500), asset, **decrease → credit**.
- Suppliers (440), liability, **decrease → debit**.

**Journal entry:**

```
12/01  440   Suppliers             12 100,00
       @ 5500 Bank account                      12 100,00
             (C/A 20X0/002, pay PI 20X0/001)
```

> Notice: paying off a debt with VAT included is just *gross* out of the bank. No new VAT is created — the VAT was already recorded when the invoice arrived.

---

### 11.3 Worked Example C — taking out a loan

> **17/01/20X0** — Bank statement **C/A 20X0/003**: a loan from **FORTIS**, 25 000,00 EUR at 3 % annual interest, repaid in 5 equal instalments of 5 000,00 EUR each 31/12, first on 31/12/20X0.

**Reasoning:** Money comes *into* the bank (asset ↑) and we now owe the bank (liability ↑). **Case ①**.

- Bank account (5500), asset ↑ → **debit**.
- Loan FORTIS (173), liability ↑ → **credit**.

```
17/01  5500  Bank account          25 000,00
       @ 173 Loan FORTIS                        25 000,00
             (C/A 20X0/003, FORTIS loan)
```

---

### 11.4 Worked Example D — a sale with VAT (the mirror of a purchase)

> **05/03/20X0** — Sales invoice **SI 20X0/001**: sold **10 smartphones** to customer PEETERS at **340,00 EUR/unit excl. 21 % VAT**. Payable in 10 days.

**Reasoning:**

1. *Document?* Sales invoice SI 20X0/001. ✔
2. *Accounts?*
   - Customer owes us → **Trade debtors** (400), **asset**.
   - We earned income → **Sales of goods for resale** (70), **revenue**.
   - We collected VAT for the tax office → **VAT due** (451), **liability**.
3. *Change?* Debtors ↑, Sales ↑ (revenue), VAT due ↑.
4. *Debit/credit?* Asset ↑ → debit; revenue ↑ → credit; liability ↑ → credit.

**Amounts:** Net = 10 × 340 = 3 400 → VAT = 3 400 × 21 % = 714 → Gross = 4 114.

```
05/03  400   Trade debtors          4 114,00
       @ 70  Sales of goods for resale           3 400,00
       @ 451 VAT due                                714,00
             (PEETERS, SI 20X0/001)
```

✔ Check: 4 114 = 3 400 + 714. ✅ **Compare with Example A** — a sale is the mirror image of a purchase: the debtor plays the role the supplier played, and “VAT due (liability)” replaces “VAT to reclaim (asset)”.

---

### 11.5 Worked Example E — a mixed private/business expense (the tricky one)

> **11/04/20X0** — Purchase invoice **PI 20X0/006** from TELENET. Phone bill **125,00 EUR excl. 21 % VAT**. Allocation: **20 % private** (borne by the manager), **80 % company**.

**Reasoning:** Only the **business** part is a company expense; the VAT can only be reclaimed on the **business** part; the **private** part is a personal amount the manager owes the company (a receivable, account 416 “C/A manager”).

**Amounts:**
- Net 125 → VAT = 125 × 21 % = 26,25 → Gross = 151,25.
- Business 80 %: expense = 125 × 80 % = **100,00**; reclaimable VAT = 26,25 × 80 % = **21,00**.
- Private 20 %: 125 × 20 % + 26,25 × 20 % = 25 + 5,25 = **30,25** → owed by the manager (416).

```
11/04  61…   Phone charges            100,00
       411   VAT to reclaim            21,00
       416   Current account manager   30,25
       @ 440 Suppliers                             151,25
             (TELENET, PI 20X0/006, 80% business)
```

✔ Check: 100 + 21 + 30,25 = 151,25. ✅
> **Why it matters:** the €151,25 you owe TELENET is the full gross bill, but only €100 hits the income statement as a company expense — the rest is a private matter and reclaimable VAT.

---

### 11.6 Worked Example F — loan repayment + interest (a 3-account entry)

> **31/12/20X0** — Bank statement **C/A 20X0/007**: redemption of 1/5 of the loan (5 000,00) **plus** 718,75 interest.

**Reasoning:** Two very different things happen in one payment:
- Repaying **principal** reduces a *liability* (Loan FORTIS 173 ↓ → debit).
- Paying **interest** is an *expense* (Interests 6500 ↑ → debit).
- Both leave the bank (5500 ↓ → credit), total 5 718,75.

```
31/12  173   Loan FORTIS            5 000,00
       6500  Interests                718,75
       @ 5500 Bank account                       5 718,75
             (C/A 20X0/007, instalment + interest)
```

> **Key distinction:** repaying the *loan itself* is **not** an expense — it just shrinks a debt. Only the **interest** is an expense. Mixing these up is one of the most common exam errors.

---

### 11.7 The full year on T-accounts (all 11 entries)

Here is the complete ledger after all transactions (entry numbers in brackets; OB = opening balance). Study how each amount traces back to an entry above.

*(Entries: (1) cash register PI003, (2) pay PI003, (3) desktops PI004, (4) buy 30 phones PI005, (5) sell 10 phones SI001, (6) collect PEETERS, (7) TELENET phone, (8) buy 20 phones PI007, (9) sell 20 phones SI002, (10) pay PI005+PI006, (11) loan instalment+interest. Plus the January entries opening the company.)*

**Selected asset accounts**

```
D   5500 Bank account         C          D   411 VAT to reclaim      C
OB   87 900,00 |  4 235,00 (2)           OB    7 350,00 |
(6)   4 114,00 |  5 233,25 (10)          (1)     735,00 |
             |   5 718,75 (11)           (3)   1 323,00 |
             |                           (4)     882,00 |
DB (bal) 76 827,00                       (7)      21,00 |
                                         (8)     588,00 |
                                         DB (bal) 10 899,00
```

**Selected liability & income statement accounts**

```
D   440 Suppliers             C          D   70 Sales of GFR         C
(2)  4 235,00 | OB   30 250,00           (bal)10 200,00| (5) 3 400,00
(10) 5 233,25 | (1)   4 235,00                          | (9) 6 800,00
             | (3)   7 623,00            CB 10 200,00
             | (4)   5 082,00
             | (7)     151,25            D   604 Purchases of GFR    C
             | (8)   3 388,00            (4)  4 200,00 |
CB (bal) 41 261,00                       (8)  2 800,00 | (bal) 7 000,00
                                         DB 7 000,00
```

*(For the complete set, reproduce every account from §7.4. The numbers reconcile to the trial balance in §11.8.)*

### 11.8 The trial balance (with balances) at 31/12/20X0

| Acc. | Account | Debit balance | Credit balance |
|---|---|---|---|
| 100 | Capital | | 75 000,00 |
| 173 | Loan FORTIS | | 20 000,00 |
| 2320 | Equipment | 28 500,00 | |
| 2400 | Furniture | 10 000,00 | |
| 2420 | Desktops | 6 300,00 | |
| 400 | Trade debtors | 8 228,00 | |
| 411 | VAT to reclaim | 10 899,00 | |
| 416 | C/A manager | 30,25 | |
| 440 | Suppliers | | 41 261,00 |
| 451 | VAT due | | 2 142,00 |
| 5500 | Bank account | 76 827,00 | |
| **—** | **Total balance-sheet accounts** | **140 784,25** | **138 403,00** |
| 604 | Purchases of goods for resale | 7 000,00 | |
| 61… | Phone charges | 100,00 | |
| 6500 | Interests | 718,75 | |
| 70 | Sales of goods for resale | | 10 200,00 |
| **—** | **Total income-statement accounts** | **7 818,75** | **10 200,00** |

**Result check (both must match):**
- Revenues − Expenses = 10 200,00 − 7 818,75 = **2 381,25 profit**.
- Assets − (Equity + Liab.) = 140 784,25 − 138 403,00 = **2 381,25 profit**. ✅

### 11.9 The financial statements

**Income statement 20X0:**

```
   Operating revenues (Sales)          10 200,00
 − Operating expenses (7 000 + 100)   − 7 100,00
 = Operating profit                     3 100,00
 − Financial expenses (interest)         − 718,75
 = Profit before taxes                  2 381,25
```

**Closing balance sheet (31/12/20X0), after appropriation:**

| ASSETS | | EQUITY + LIABILITIES | |
|---|---|---|---|
| Equipment | 28 500,00 | Capital | 75 000,00 |
| Furniture | 10 000,00 | Profit carried forward | 2 381,25 |
| Desktops | 6 300,00 | Loan FORTIS | 20 000,00 |
| Trade debtors | 8 228,00 | Suppliers | 41 261,00 |
| VAT to reclaim | 10 899,00 | VAT due | 2 142,00 |
| C/A manager | 30,25 | | |
| Bank account | 76 827,00 | | |
| **TOTAL** | **140 784,25** | **TOTAL** | **140 784,25** |

The €2 381,25 profit, carried to equity (account 140), is exactly what makes the closing balance sheet balance. **Loop closed.** 🎉

---

## 12. Interactive Practice Section

> ✍️ **Instructions:** Try each question *before* looking at [§13 Solutions](#13-solutions--explanations). Write full journal entries with account numbers, amounts, and a one-line description. VAT rate = **21 %** unless stated. Difficulty rises as you go.

### Level 1 — Basic recall (warm-up)

**Q1.** Fill in the blanks:
(a) Assets increase on the ____ side. (b) Liabilities increase on the ____ side. (c) Expenses increase on the ____ side. (d) Revenues increase on the ____ side.

**Q2.** For each account, state its type (asset / liability / equity / expense / revenue) and its “home” balance (debit or credit): *Bank account, Suppliers, Sales of goods for resale, VAT to reclaim, VAT due, Interests, Capital.*

**Q3.** True or false: “Repaying the principal of a bank loan is an expense.” Explain.

**Q4.** What are the two checks a trial balance performs, and name one type of error it will **not** detect.

### Level 2 — Single transactions (build the reflex)

For each, write the full journal entry.

**Q5.** 03/02 — Purchase invoice: a laptop (equipment, acct 2320) for **2 000,00 EUR excl. VAT**, on credit.

**Q6.** 10/02 — Sales invoice: services supplied to a client for **1 500,00 EUR excl. VAT**, on credit (use “Sales/Services” revenue acct 70 and Trade debtors 400).

**Q7.** 14/02 — Bank statement: the client of Q6 pays the full amount by bank transfer.

**Q8.** 20/02 — Bank statement: you pay the supplier of Q5 in full by bank transfer.

**Q9.** 25/02 — Bank statement: a loan of **40 000,00 EUR** is credited to the bank account (acct 173).

### Level 3 — Application (multi-account & VAT)

**Q10.** 02/03 — Purchase invoice PI/x: **50 units** of goods for resale at **12,00 EUR/unit excl. VAT**, on credit. (Purchases of GFR = 604.)

**Q11.** 08/03 — Sales invoice SI/x: **30 units** of those goods sold at **25,00 EUR/unit excl. VAT**, on credit.

**Q12.** 15/03 — Purchase invoice from the electricity company: **600,00 EUR excl. VAT**, on credit. (Use expense acct 61… “services & other goods”.)

**Q13.** 31/03 — Bank statement: bank charges of **15,00 EUR** are deducted (no VAT). (Financial expense, acct 65…)

### Level 4 — Scenario-based (exam-style)

**Q14 (mixed private/business).** 05/04 — Phone invoice **200,00 EUR excl. 21 % VAT**; **75 %** is business, **25 %** private (manager, acct 416). Write the entry.

**Q15 (loan instalment + interest).** 31/12 — Bank statement: you repay a **10 000,00 EUR** instalment of a loan **and** pay **450,00 EUR** interest, all from the bank in one payment. Write the entry.

**Q16 (mini-cycle).** A start-up, **BREAD & CO plc**, has these events in January 20X1 (VAT 21 %):

1. 02/01 — Owner deposits **50 000,00 EUR** as capital into the bank.
2. 04/01 — Buys an **oven** (equipment 2320) for **8 000,00 EUR excl. VAT** on credit.
3. 06/01 — Buys **stock of flour** (goods for resale 604) for **1 000,00 EUR excl. VAT** on credit.
4. 10/01 — Sells bread for **2 000,00 EUR excl. VAT**, customer pays immediately by bank.
5. 15/01 — Pays the oven supplier in full by bank.

Tasks: (a) journal-entry all five events; (b) compute the closing balance of the **Bank account** and of **Suppliers**; (c) what is the profit for January (ignore inventory changes)?

**Q17 (result determination — reasoning).** After a year, a company's income statement accounts show total revenue credit balances of **85 000,00** and total expense debit balances of **91 000,00**. (a) Profit or loss, and how much? (b) Which appropriation account (69-group or 79-group) will be used, and to which equity/asset account does it flow?

---

## 13. Solutions & Explanations

### Level 1

**A1.** (a) **debit** (b) **credit** (c) **debit** (d) **credit**. *Assets & expenses are “debit-natured”; liabilities, equity & revenues are “credit-natured”.*

**A2.**
| Account | Type | Home balance |
|---|---|---|
| Bank account | Asset | Debit |
| Suppliers | Liability | Credit |
| Sales of goods for resale | Revenue | Credit |
| VAT to reclaim | Asset | Debit |
| VAT due | Liability | Credit |
| Interests | Expense | Debit |
| Capital | Equity | Credit |

**A3.** **False.** Repaying the *principal* only reduces a liability (Loan ↓, Bank ↓) — it never touches the income statement. Only the **interest** portion is an expense. *(This is exactly Worked Example F.)*

**A4.** The trial balance checks that (1) total debit **footings** = total credit footings, and (2) total debit **balances** = total credit balances. It will **not** detect: a transaction posted to the *wrong account*, a transaction *omitted entirely*, or one *recorded twice* — because those keep debit = credit.

### Level 2

**A5.** Net 2 000 → VAT 420 → Gross 2 420.
```
03/02  2320  Equipment              2 000,00
       411   VAT to reclaim           420,00
       @ 440 Suppliers                            2 420,00
```

**A6.** Net 1 500 → VAT 315 → Gross 1 815.
```
10/02  400   Trade debtors          1 815,00
       @ 70  Sales / Services                     1 500,00
       @ 451 VAT due                                 315,00
```

**A7.** Money in (bank ↑, debit), receivable settled (debtors ↓, credit). Gross 1 815.
```
14/02  5500  Bank account           1 815,00
       @ 400 Trade debtors                        1 815,00
```

**A8.** Debt settled (suppliers ↓, debit), money out (bank ↓, credit). Gross 2 420.
```
20/02  440   Suppliers              2 420,00
       @ 5500 Bank account                        2 420,00
```

**A9.** Money in (bank ↑, debit), new debt (loan ↑, credit).
```
25/02  5500  Bank account          40 000,00
       @ 173 Loan                              40 000,00
```

### Level 3

**A10.** Net = 50 × 12 = 600 → VAT 126 → Gross 726.
```
02/03  604   Purchases of GFR         600,00
       411   VAT to reclaim           126,00
       @ 440 Suppliers                              726,00
```

**A11.** Net = 30 × 25 = 750 → VAT 157,50 → Gross 907,50.
```
08/03  400   Trade debtors           907,50
       @ 70  Sales of GFR                          750,00
       @ 451 VAT due                               157,50
```
> Note: we do **not** touch the stock account here — the cost of what was sold is handled by *inventory / end-of-period entries* in a later chapter. For now, purchases are fully expensed and sales fully booked as revenue.

**A12.** Net 600 → VAT 126 → Gross 726.
```
15/03  61…   Electricity (services & other goods)  600,00
       411   VAT to reclaim                        126,00
       @ 440 Suppliers                                        726,00
```

**A13.** No VAT; pure financial expense straight from the bank.
```
31/03  65…   Bank charges              15,00
       @ 5500 Bank account                          15,00
```

### Level 4

**A14.** Net 200 → VAT 42 → Gross 242. Business 75 %: expense 150, VAT 31,50. Private 25 %: 50 + 10,50 = 60,50.
```
05/04  61…   Phone charges            150,00
       411   VAT to reclaim            31,50
       416   Current account manager   60,50
       @ 440 Suppliers                              242,00
```
✔ 150 + 31,50 + 60,50 = 242,00.

**A15.**
```
31/12  173   Loan                   10 000,00
       6500  Interests                 450,00
       @ 5500 Bank account                       10 450,00
```

**A16 — BREAD & CO plc.**

(a) Journal entries:
```
02/01  5500  Bank account          50 000,00
       @ 100 Capital                             50 000,00

04/01  2320  Equipment              8 000,00
       411   VAT to reclaim         1 680,00
       @ 440 Suppliers                            9 680,00

06/01  604   Purchases of GFR       1 000,00
       411   VAT to reclaim           210,00
       @ 440 Suppliers                            1 210,00

10/01  5500  Bank account           2 420,00
       @ 70  Sales of GFR                         2 000,00
       @ 451 VAT due                                420,00

15/01  440   Suppliers              9 680,00
       @ 5500 Bank account                        9 680,00
```

(b) **Bank account** balance: 50 000 + 2 420 − 9 680 = **42 740,00 (debit balance)**.
**Suppliers** balance: (9 680 + 1 210) − 9 680 = **1 210,00 (credit balance)**.

(c) **Profit** (ignoring inventory changes) = Revenues − Expenses = Sales 2 000 − Purchases 1 000 = **1 000,00 profit**. *(VAT is never revenue or expense; the oven is an asset, not an expense.)*

**A17.**
(a) Expenses (91 000) > Revenues (85 000) → **LOSS of 6 000,00**.
(b) A **loss** uses the **79-group** appropriation account; it flows to **equity** as a reduction (e.g. loss carried forward / withdrawal from equity). *(A profit would use the **69-group**, flowing to an equity account like 140 “profit carried forward”.)*

---

## 14. Quick Check / Active Recall

Cover the answers. Say each one out loud.

**Flashcards**

1. Balance sheet = ? → *A snapshot of financial position at one moment; Assets = Equity + Liabilities.*
2. Income statement = ? → *Revenues − Expenses over a period = profit or loss.*
3. Assets increase on the → *debit* side.
4. Liabilities & equity increase on the → *credit* side.
5. Expenses increase on the → *debit*; revenues on the → *credit*.
6. “VAT to reclaim” is a(n) → *asset* (we're owed a refund).
7. “VAT due” is a(n) → *liability* (we owe the tax office).
8. General ledger is organised by → *account*; the journal by → *date*.
9. Trial balance checks that → *total debits = total credits*.
10. Fixed assets are listed → *first* (least liquid); cash → *last*.
11. Repaying loan principal affects the income statement? → *No* — only interest does.
12. Profit from the I/S accounts must equal profit from the → *B/S accounts* (assets − (E+L)).

**60-second self-test (write answers):**
- Give the debit/credit rule for all five account types.
- Write, from memory, the standard VAT purchase entry and VAT sales entry.
- State the four ways a transaction can move the balance sheet (§3.5).

---

## 15. Common Mistakes

| ❌ Mistake | ✅ Fix / Why |
|---|---|
| Treating **loan repayment** as an expense | Only the **interest** is an expense; principal repayment just reduces the liability. |
| Putting **VAT to reclaim on the credit** side | It's an **asset** (a receivable from the tax office) → **debit**. VAT *due* is the liability (credit). |
| Booking the **gross amount as the expense/asset** | The expense/asset is the **net** amount. VAT is booked **separately**; only the *supplier/customer* line carries the gross. |
| Forgetting that **debit must equal credit** in every entry | If they don't match, you're missing a line or used the wrong side. Check *before* moving on. |
| Recording the **stock cost** at the moment of sale | In this chapter, purchases are expensed and sales booked as revenue; the cost-of-goods matching is an **end-of-period entry** (later chapter). |
| Confusing **VAT to reclaim (411)** with **VAT due (451)** | *Reclaim* = you paid it on a **purchase** (asset). *Due* = you collected it on a **sale** (liability). |
| Listing assets/liabilities in the **wrong order** | Assets: increasing **liquidity** (cash last). E+L: increasing **callability** (equity first). |
| Thinking the **trial balance proves correctness** | It only proves debits = credits. Wrong-account, omitted, or duplicated entries slip through. |
| Booking a **mixed private/business** cost entirely as company expense | Split it: only the business % is an expense; the private % becomes a receivable on the manager (416), and VAT is reclaimable only on the business part. |
| Mixing up the **T-account header notation** on the slides | Ignore the header letter order; always draw **debit = left, credit = right**. |

---

## 16. Summary Sheet

**The one equation:** `ASSETS = EQUITY + LIABILITIES` — always balanced, after every transaction.

**Debit / credit rules (memorise the table):**

| | Increase | Decrease | Home side |
|---|---|---|---|
| **Asset** | Debit | Credit | Debit |
| **Liability / Equity** | Credit | Debit | Credit |
| **Expense** (class 6) | Debit | Credit | Debit |
| **Revenue** (class 7) | Credit | Debit | Credit |

*Rule of thumb: Assets & Expenses are debit-natured; Liabilities, Equity & Revenues are credit-natured.* **Every entry: total DEBIT = total CREDIT.**

**The 4-question procedure:** ① Which document? ② Which account (asset/liab/equity or expense/revenue)? ③ Increase or decrease? ④ Debit or credit?

**VAT:**
- Purchase → **VAT to reclaim (411)** = **asset**, debit. Gross = Net × 1,21.
- Sale → **VAT due (451)** = **liability**, credit.

**VAT entry skeletons:**
```
PURCHASE:  Asset/Expense (net) D  |  VAT to reclaim (net×r) D  |  @ Suppliers (gross) C
SALE:      Trade debtors (gross) D |  @ Sales (net) C  |  @ VAT due (net×r) C
```

**Chart of accounts (decimal):** Class (1 digit) → Group (2) → Account (3) → Subaccount (4).
Classes: 1 = equity/LT payables, 2 = fixed assets, 3 = inventories, 4 = ST receivables/payables & VAT, 5 = cash, **6 = expenses**, **7 = revenues**.

**The two books:** **Ledger** = all T-accounts, organised *by account*. **Journal** = all transactions in *time order* (legally required); entry = *debited accounts → “at/@” credited accounts + description*.

**Trial balance:** interim control (not legally required). Footings version & balances version. Check: **total debit = total credit**. Does **not** catch wrong-account / omitted / duplicated entries.

**The result (two equal routes):**
```
Profit = Σ revenue balances − Σ expense balances
       = Σ asset balances − Σ (equity + liability) balances
```
The income statement explains *why* equity changed; the profit balances the closing balance sheet. **Appropriation:** profit → 69-group → equity (reserves / carried forward / distribution); loss → 79-group → equity reduction / carried forward / partner intervention.

**The cycle:** Opening B/S → record transactions (journal + ledger) → 1st trial balance → inventory & end-of-period entries → 2nd trial balance (result before tax) → taxes → final trial balance → financial statements → appropriation.

---

### 📚 Where to read & practise more

- **Textbook:** *A Practical Guide to Financial Accounting*, **Chapter 3** (p. 41 → p. 70).
- **Exercises:** Exercise 1 (p. 71), Exercise 2 *BARRAQUITO* (p. 72), Exercise 3 *KEEP IT SIMPLE* (p. 72–73).

**You've got this.** Work through the Level 1–4 questions until the journal entries feel automatic — that reflex is exactly what the exam tests. 💪
