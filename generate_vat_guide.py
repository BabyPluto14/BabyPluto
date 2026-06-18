from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ── colour palette ──────────────────────────────────────────────────────────
DARK_BLUE   = colors.HexColor("#1a3a5c")
MID_BLUE    = colors.HexColor("#2563a8")
LIGHT_BLUE  = colors.HexColor("#dbeafe")
ACCENT      = colors.HexColor("#f59e0b")
GREEN       = colors.HexColor("#166534")
GREEN_BG    = colors.HexColor("#dcfce7")
RED         = colors.HexColor("#991b1b")
RED_BG      = colors.HexColor("#fee2e2")
GREY_BG     = colors.HexColor("#f3f4f6")
WHITE       = colors.white
TEXT        = colors.HexColor("#1f2937")

W, H = A4
LEFT_MARGIN = RIGHT_MARGIN = 2 * cm
TOP_MARGIN = BOTTOM_MARGIN = 2 * cm

# ── document ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    "/home/user/BabyPluto/Chapter11_VAT_Study_Guide.pdf",
    pagesize=A4,
    leftMargin=LEFT_MARGIN, rightMargin=RIGHT_MARGIN,
    topMargin=TOP_MARGIN,   bottomMargin=BOTTOM_MARGIN,
    title="Chapter 11 – VAT Study Guide",
    author="Principles of Taxation – Bammens & Debelva",
)

# ── shared styles ─────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

TITLE = S("MyTitle",
    fontSize=26, textColor=WHITE, alignment=TA_CENTER,
    fontName="Helvetica-Bold", leading=34, spaceAfter=4)

SUBTITLE = S("MySubtitle",
    fontSize=13, textColor=LIGHT_BLUE, alignment=TA_CENTER,
    fontName="Helvetica", leading=18, spaceAfter=2)

H1 = S("H1",
    fontSize=16, textColor=WHITE, fontName="Helvetica-Bold",
    leading=22, spaceBefore=18, spaceAfter=8, leftIndent=0)

H2 = S("H2",
    fontSize=13, textColor=DARK_BLUE, fontName="Helvetica-Bold",
    leading=18, spaceBefore=14, spaceAfter=6)

H3 = S("H3",
    fontSize=11, textColor=MID_BLUE, fontName="Helvetica-Bold",
    leading=16, spaceBefore=10, spaceAfter=4)

BODY = S("Body",
    fontSize=10, textColor=TEXT, fontName="Helvetica",
    leading=15, spaceAfter=6, alignment=TA_JUSTIFY)

BULLET = S("Bullet",
    fontSize=10, textColor=TEXT, fontName="Helvetica",
    leading=15, spaceAfter=4, leftIndent=14, bulletIndent=4,
    alignment=TA_LEFT)

BULLET2 = S("Bullet2",
    fontSize=10, textColor=TEXT, fontName="Helvetica",
    leading=14, spaceAfter=3, leftIndent=28, bulletIndent=18)

CODE = S("Code",
    fontSize=9.5, textColor=DARK_BLUE, fontName="Helvetica-Bold",
    leading=14, spaceAfter=4, leftIndent=10, backColor=LIGHT_BLUE)

CAPTION = S("Caption",
    fontSize=8.5, textColor=colors.grey, fontName="Helvetica-Oblique",
    leading=12, alignment=TA_CENTER, spaceAfter=4)

LABEL_G = S("LabelG",
    fontSize=9, textColor=GREEN, fontName="Helvetica-Bold", leading=13)
LABEL_R = S("LabelR",
    fontSize=9, textColor=RED,   fontName="Helvetica-Bold", leading=13)
LABEL_B = S("LabelB",
    fontSize=9, textColor=MID_BLUE, fontName="Helvetica-Bold", leading=13)

EXAM_HEAD = S("ExamHead",
    fontSize=10, textColor=WHITE, fontName="Helvetica-Bold",
    leading=14, alignment=TA_LEFT)

EXAM_BODY = S("ExamBody",
    fontSize=10, textColor=TEXT, fontName="Helvetica",
    leading=14, spaceAfter=3, leftIndent=8)


# ── helper builders ───────────────────────────────────────────────────────────

def title_block(title_text, subtitle_text, course_text=""):
    """Blue cover banner."""
    data = [[
        Paragraph(title_text, TITLE),
        Paragraph(subtitle_text, SUBTITLE),
        Paragraph(course_text, SUBTITLE) if course_text else Spacer(1, 1),
    ]]
    # use a single-row table rendered as a banner
    t = Table([[
        Paragraph(title_text, TITLE),
    ]], colWidths=[W - LEFT_MARGIN - RIGHT_MARGIN])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), DARK_BLUE),
        ("ROUNDEDCORNERS", [8]),
        ("TOPPADDING",    (0,0), (-1,-1), 18),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 16),
    ]))
    sub = Table([[
        Paragraph(subtitle_text, SUBTITLE),
    ]], colWidths=[W - LEFT_MARGIN - RIGHT_MARGIN])
    sub.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), MID_BLUE),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 16),
    ]))
    return [t, sub, Spacer(1, 0.3*cm)]


def section_header(number, text):
    """Dark-blue full-width section banner."""
    t = Table([[
        Paragraph(f"{number}   {text}", H1),
    ]], colWidths=[W - LEFT_MARGIN - RIGHT_MARGIN])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), DARK_BLUE),
        ("ROUNDEDCORNERS", [6]),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ]))
    return [t, Spacer(1, 0.2*cm)]


def info_box(label, text, bg=LIGHT_BLUE, label_style=None, body_style=None):
    """Coloured info / definition box."""
    ls = label_style or LABEL_B
    bs = body_style or BODY
    t = Table([[
        Paragraph(f"<b>{label}</b>", ls),
        Paragraph(text, bs),
    ]], colWidths=[2.8*cm, W - LEFT_MARGIN - RIGHT_MARGIN - 2.8*cm - 0.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("TOPPADDING",    (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return [t, Spacer(1, 0.2*cm)]


def example_box(title_text, body_text):
    """Amber-accent example box."""
    t = Table([[
        Paragraph(f"<font color='#92400e'><b>Example – {title_text}</b></font>", BODY),
    ], [
        Paragraph(body_text, BODY),
    ]], colWidths=[W - LEFT_MARGIN - RIGHT_MARGIN])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), colors.HexColor("#fef3c7")),
        ("BACKGROUND",    (0,1), (-1,-1), colors.HexColor("#fffbeb")),
        ("LINEAFTER",     (0,0), (0,-1), 3, ACCENT),
        ("LINEBEFORE",    (0,0), (0,-1), 3, ACCENT),
        ("TOPPADDING",    (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return [t, Spacer(1, 0.25*cm)]


def exam_tip(text):
    """Red exam-tip callout."""
    t = Table([[
        Paragraph("★ EXAM TIP", EXAM_HEAD),
    ], [
        Paragraph(text, EXAM_BODY),
    ]], colWidths=[W - LEFT_MARGIN - RIGHT_MARGIN])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), RED),
        ("BACKGROUND",    (0,1), (-1,-1), RED_BG),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return [t, Spacer(1, 0.25*cm)]


def green_box(label, text):
    return info_box(label, text, bg=GREEN_BG, label_style=LABEL_G)


def two_col_table(left_head, right_head, rows, col_widths=None):
    col_w = col_widths or [
        (W - LEFT_MARGIN - RIGHT_MARGIN) * 0.42,
        (W - LEFT_MARGIN - RIGHT_MARGIN) * 0.58,
    ]
    data = [[Paragraph(f"<b>{left_head}</b>", LABEL_B),
             Paragraph(f"<b>{right_head}</b>", LABEL_B)]]
    for l, r in rows:
        data.append([Paragraph(l, BODY), Paragraph(r, BODY)])
    t = Table(data, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), DARK_BLUE),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [WHITE, GREY_BG]),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("GRID",          (0,0), (-1,-1), 0.5, colors.HexColor("#d1d5db")),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ]))
    return [t, Spacer(1, 0.25*cm)]


def bp(text):
    """Bullet paragraph helper."""
    return Paragraph(f"• {text}", BULLET)


def bp2(text):
    """Indented bullet."""
    return Paragraph(f"– {text}", BULLET2)


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e5e7eb"),
                      spaceAfter=8, spaceBefore=4)


# ── CONTENT ───────────────────────────────────────────────────────────────────
story = []

# ════════════════════════════════════════════════════════════════════════════
#  COVER PAGE
# ════════════════════════════════════════════════════════════════════════════
cover = Table([[
    Paragraph("Chapter 11", S("ct1", fontSize=14, textColor=LIGHT_BLUE,
              fontName="Helvetica", leading=20, alignment=TA_CENTER)),
    Paragraph("Basic Mechanism of Value Added Tax",
              S("ct2", fontSize=24, textColor=WHITE, fontName="Helvetica-Bold",
                leading=30, alignment=TA_CENTER)),
    Paragraph("Expanded Study Guide",
              S("ct3", fontSize=13, textColor=LIGHT_BLUE, fontName="Helvetica-Oblique",
                leading=18, alignment=TA_CENTER)),
    Spacer(1, 0.5*cm),
    Paragraph("Principles of Taxation | Prof. dr. Niels Bammens & Prof. dr. Filip Debelva",
              S("ct4", fontSize=10, textColor=colors.HexColor("#93c5fd"),
                fontName="Helvetica", leading=14, alignment=TA_CENTER)),
]], colWidths=[W - LEFT_MARGIN - RIGHT_MARGIN])
cover.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), DARK_BLUE),
    ("TOPPADDING",    (0,0), (-1,-1), 40),
    ("BOTTOMPADDING", (0,0), (-1,-1), 40),
    ("LEFTPADDING",   (0,0), (-1,-1), 20),
    ("ROUNDEDCORNERS", [10]),
]))
story += [Spacer(1, 2*cm), cover, Spacer(1, 1*cm)]

story.append(Paragraph(
    "This guide expands every section of the lecture slides with plain-English explanations, "
    "worked examples, comparison tables, and exam-focused tips. Read it alongside (not instead of) "
    "the original slides.",
    S("intro", fontSize=10.5, textColor=TEXT, fontName="Helvetica-Oblique",
      leading=15, alignment=TA_JUSTIFY)))
story.append(Spacer(1, 0.5*cm))

# Quick TOC
toc_rows = [
    ("11.1", "VAT as an Indirect Consumption Tax"),
    ("11.2", "VAT vs Other Consumption Taxes"),
    ("11.3", "The European Dimension of VAT"),
    ("11.4", "When Is a Business a VAT Taxable Person?"),
    ("11.5", "Exempt Taxable Persons"),
    ("11.6", "Non-Taxable Legal Persons"),
    ("11.8", "VAT Grouping"),
    ("11.9", "Which Transactions Are Taxable?"),
    ("11.10", "Intra-Community Acquisition (ICA)"),
    ("11.11", "Which Transactions Are Exempt?"),
    ("11.12", "How Much VAT Is Due?"),
    ("11.13", "Deduction of Input VAT"),
    ("11.14", "Advanced Issues – VAT Gap, Fraud & Abuse"),
]
story += two_col_table("Section", "Topic", toc_rows,
                       col_widths=[1.5*cm, W-LEFT_MARGIN-RIGHT_MARGIN-1.5*cm])
story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.1  VAT: AN INDIRECT CONSUMPTION TAX
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.1", "VAT: An Indirect Consumption Tax")

story.append(Paragraph("What is VAT?", H2))
story.append(Paragraph(
    "Value Added Tax (VAT) is the most important indirect tax used across the European Union "
    "and over 170 countries worldwide. It is fundamentally a <b>consumption tax</b> — it is designed "
    "to tax the final private consumption of goods and services, not business income or profit.",
    BODY))

story += info_box("Definition", (
    "VAT is a <b>broad-based consumption tax</b> levied on the supply of goods and services "
    "at each stage of the production and distribution chain. The final economic burden "
    "always falls on the <b>end consumer</b>, while registered businesses act as unpaid "
    "tax collectors for the state."), bg=LIGHT_BLUE)

story.append(Paragraph("The three core characteristics", H2))
story.append(Paragraph(
    "Understanding VAT requires grasping three interlocking characteristics:", BODY))

story += [
    bp("<b>Consumption tax</b> – VAT is a tax on the <i>private expenditure</i> of income or wealth. "
       "When you buy a phone, clothes, or a meal, the price includes VAT that is ultimately borne by you "
       "as the final consumer. Businesses are, in economic terms, merely <i>conduits</i> for the tax."),
    bp("<b>Indirect tax</b> – Unlike income tax (paid directly by the person who earns), VAT is collected "
       "by a third party (the seller) and remitted to the tax authority. The legal obligation to pay sits "
       "with businesses, but the economic cost is passed on to consumers through the price."),
    bp("<b>Right of deduction for businesses</b> – Every business in the VAT chain can reclaim the VAT it "
       "paid on its own purchases (input VAT), meaning VAT does not compound as it moves through the chain. "
       "Only the value added at each stage is taxed."),
    Spacer(1, 0.3*cm),
]

story += example_box(
    "Basic Flow",
    "A timber merchant sells wood to a furniture maker. The furniture maker sells chairs to a retailer. "
    "The retailer sells to a family at home. At every step VAT is charged and collected, but each "
    "business deducts the VAT it already paid on its purchases. The net result: the tax authority "
    "collects VAT <i>equal to the standard rate applied to the final retail price</i> — exactly what "
    "the end family pays, and nothing more.")

story += exam_tip(
    "VAT is NOT a tax on business profit. It is economically borne by the final consumer. "
    "Businesses are neutral — they collect VAT, deduct what they paid, and pass the difference "
    "to the government. This neutrality is tested frequently.")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.2  VAT VS OTHER CONSUMPTION TAXES
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.2", "VAT vs Other Consumption Taxes")

story.append(Paragraph("The landscape of consumption taxes", H2))
story.append(Paragraph(
    "Before diving deeper into VAT, it helps to understand how it differs from related taxes. "
    "Three other consumption taxes are frequently compared:", BODY))

story += two_col_table(
    "Tax Type", "Key Feature & Drawback",
    [
        ("<b>Turnover Tax</b>",
         "Levied on total sales of a business regardless of profit. Simple to administer but "
         "creates a 'tax-on-tax' cascading effect."),
        ("<b>Sales Tax</b>",
         "Applied once at the point of final purchase (retail). The rate is a % of the retail price "
         "(ad valorem). Revenue depends on the price level. Widely used in the US."),
        ("<b>Excise Tax</b>",
         "A specific type of sales tax charged at a fixed fee per unit sold (e.g. €0.50 per litre of fuel). "
         "Revenue depends on volume, not price."),
        ("<b>VAT</b>",
         "Levied at each stage of production/distribution on the value added. Input VAT is deductible — "
         "no cascading. The final consumer bears the full burden."),
    ]
)

story.append(Paragraph("Why VAT wins over sales and turnover taxes", H2))
story.append(Paragraph(
    "Two alternative designs highlight the advantages of VAT:", BODY))

story += [
    bp("<b>Final sales tax</b> – Only the last (retail) stage is taxed. Simple in theory, "
       "but prone to fraud: if a seller under-reports the final sale, the entire tax is lost. "
       "It also creates strong incentives to misclassify retail as wholesale."),
    bp("<b>Cumulative sales tax</b> – Every sale in the chain is taxed on the full price. "
       "This creates a <i>tax-on-tax</i> (cascading) problem that distorts prices and punishes "
       "industries with long supply chains."),
    Spacer(1, 0.2*cm),
]

story += info_box("Key Advantage of VAT",
    "VAT avoids cascading because each business deducts the input VAT it paid. "
    "Even if one link in the chain cheats, the fraud is limited to <i>that stage's</i> value added, "
    "not the total price. This makes VAT more fraud-resistant than a final sales tax at scale.",
    bg=GREEN_BG, label_style=LABEL_G)

story.append(Paragraph("The neutrality principle", H2))
story.append(Paragraph(
    "VAT should be <b>economically neutral</b> — it should not distort business decisions. "
    "This principle has four dimensions:", BODY))
story += [
    bp("<b>Neutral for businesses</b> – Because businesses can deduct input VAT, they are not "
       "permanently burdened by VAT costs. VAT is a zero-cost 'pass-through' for them."),
    bp("<b>Neutral between taxpayers</b> – All VAT-registered entities (companies, individuals, "
       "NGOs, governments) are treated equally."),
    bp("<b>Neutral between transactions</b> – Domestic and cross-border supplies should bear "
       "the same VAT burden to avoid distorting trade."),
    bp("<b>Neutral between consumers</b> – All final consumers face the same VAT-inclusive price "
       "regardless of where in the chain they buy."),
    Spacer(1, 0.3*cm),
]

story += example_box(
    "Numerical walk-through (21% VAT)",
    "<b>Step 1 – Raw materials → Manufacturer:</b> Seller charges €100 + €21 VAT. "
    "Seller pays €21 to government. Manufacturer reclaims €21 input VAT.<br/>"
    "<b>Step 2 – Manufacturer → Retailer:</b> Manufacturer sells for €200 + €42 VAT. "
    "Manufacturer pays €42 − €21 (input VAT) = €21 to government.<br/>"
    "<b>Step 3 – Retailer → Consumer:</b> Retailer sells for €300 + €63 VAT. "
    "Retailer pays €63 − €42 = €21 to government.<br/>"
    "<b>Total VAT collected:</b> €21 + €21 + €21 = <b>€63 = 21% × €300</b>. "
    "The consumer pays exactly 21% on the final price.")

story += exam_tip(
    "The 'VAT gap' is the difference between expected and actually collected VAT. "
    "Know that it exists due to fraud, bankruptcy, and administrative errors — "
    "not because the VAT design is flawed.")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.3  EUROPEAN DIMENSION OF VAT
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.3", "The European Dimension of VAT")

story.append(Paragraph("Council Directive 2006/112/EC — the EU VAT Directive", H2))
story.append(Paragraph(
    "VAT in Europe is built on a single EU-wide legal framework: <b>Council Directive 2006/112/EC</b>, "
    "known as the VAT Directive (VAT-D). It replaced the earlier Sixth Directive and sets the "
    "rules that all EU Member States must implement in their national VAT legislation.", BODY))

story += info_box("What the Directive does",
    "• Sets the <b>structure</b> of VAT (who is taxable, what is taxed, how much).<br/>"
    "• Establishes <b>minimum rates</b> (standard ≥ 15%, reduced ≥ 5%) but leaves Member States "
    "free to set higher rates.<br/>"
    "• Allows limited derogations and options for Member States.<br/>"
    "• Does <b>not</b> fully harmonise rates — each country chooses its own within the bounds.")

story.append(Paragraph("Role of the Court of Justice of the EU (CJEU)", H2))
story.append(Paragraph(
    "Because national courts may be uncertain how to apply the Directive, they can send "
    "<b>preliminary questions</b> to the CJEU. The CJEU's rulings are binding on all Member States "
    "and frequently clarify or extend VAT rules. This makes EU case law an essential "
    "part of understanding VAT.", BODY))

story += example_box(
    "Banca Popolare di Cremona",
    "Italy levied a regional business tax (IRAP) that had features resembling VAT. "
    "The CJEU examined whether IRAP was prohibited under Article 401 VAT-D because it had "
    "the same characteristics as VAT. The court held IRAP was NOT equivalent to VAT, "
    "as it lacked the right to deduction mechanism and was not proportional to price.")

story.append(Paragraph("Article 401 VAT-D — the four hallmarks of VAT", H2))
story.append(Paragraph(
    "A Member State may keep or introduce other taxes (insurance taxes, gambling taxes, stamp duties) "
    "<i>only if</i> those taxes do not share all four core features of VAT:", BODY))

story += two_col_table(
    "Hallmark", "Explanation",
    [
        ("1. Applies to goods & services",
         "The tax covers the supply of goods and services in general, not a narrow category."),
        ("2. Proportional to the price",
         "The tax is a percentage of the consideration — not a fixed amount per unit."),
        ("3. Charged at each stage",
         "The tax applies throughout the production and distribution chain."),
        ("4. Deduction of prior-stage tax",
         "There is a mechanism to deduct tax paid at earlier stages so the final burden lands on the consumer."),
    ]
)

story += info_box("Territorial scope",
    "European VAT only applies to transactions that take place <b>within the EU</b>. "
    "Transactions outside EU borders are governed by different rules (export exemptions, import VAT, etc.).")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.4  WHEN IS A BUSINESS A VAT TAXABLE PERSON?
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.4", "When Is a Business a VAT Taxable Person?")

story.append(Paragraph(
    "Not every person or entity is automatically a VAT taxable person. Whether you are "
    "determines a cascade of obligations and rights.", BODY))

story.append(Paragraph("Why it matters — practical consequences", H2))
story += [
    bp("<b>VAT registration</b> – Must register with the tax authority and obtain a VAT number."),
    bp("<b>Invoicing</b> – Must issue VAT invoices for every VATable transaction, "
       "showing the VAT number, amount, and rate."),
    bp("<b>Collecting output VAT</b> – Must charge VAT on every taxable sale."),
    bp("<b>Filing VAT returns</b> – Must submit periodic returns (monthly or quarterly) "
       "showing output VAT minus input VAT."),
    bp("<b>Deducting input VAT</b> – Has the right to reclaim VAT paid on business purchases."),
    Spacer(1, 0.2*cm),
]

story.append(Paragraph("Type 1: Basic (ordinary) taxable persons — Article 9(1) VAT-D", H2))
story += info_box("Legal definition (Art. 9(1))",
    '"Taxable person" shall mean <b>any person who, independently, carries out in any place any '
    'economic activity, whatever the purpose or results of that activity</b>.')

story.append(Paragraph("Unpacking the three elements:", H3))

story.append(Paragraph("<b>1. Any person</b>", BODY))
story += [
    bp("Includes <b>individuals</b> (sole traders, freelancers, self-employed professionals) "
       "and <b>legal entities</b> (companies, foundations, associations)."),
    bp("Irrelevant: age, nationality, place of incorporation, profit motive."),
    bp("A 16-year-old who runs a business selling handmade goods online is a taxable person."),
    Spacer(1, 0.1*cm),
]

story.append(Paragraph("<b>2. Carrying on an economic activity</b>", BODY))
story += [
    bp("Economic activity = any activity of producers, traders, or service providers (non-exhaustive list)."),
    bp("Includes mining, agriculture, and the professions."),
    bp("Key requirement: the activity involves <i>transactions for consideration</i> — "
       "agreed remuneration with a direct link between payment and the goods/services."),
    bp("Whether the entity is for-profit or not-for-profit is <b>irrelevant</b> — VAT neutrality applies."),
    bp("<b>Exception:</b> passive holding companies (mere ownership of shares without active involvement "
       "in management) are NOT carrying on an economic activity."),
    Spacer(1, 0.1*cm),
]

story.append(Paragraph("<b>3. Independence — Article 10 VAT-D</b>", BODY))
story += info_box("Art. 10",
    "The 'independently' requirement excludes <b>employees and other dependent persons</b> who are "
    "bound to an employer by an employment contract or similar legal ties (working conditions, "
    "remuneration, employer's liability).")
story += [
    bp("<b>Employees and civil servants → NOT VAT taxable persons</b> (even if they earn significant income)."),
    bp("<b>Independent contractors, freelancers, self-employed → ARE VAT taxable persons</b>."),
    bp("The same person can have two roles: an employee on weekdays and a freelance consultant at weekends "
       "— only the freelance activity makes them a taxable person."),
    bp("<b>Companies are always considered to act independently</b> for VAT purposes."),
    Spacer(1, 0.2*cm),
]

story += exam_tip(
    "Profit motive and non-profit status are irrelevant for VAT taxable person status. "
    "The test is: (1) any person, (2) independently, (3) carrying on an economic activity. "
    "All three must be present.")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.5  EXEMPT TAXABLE PERSONS
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.5", "Exempt Taxable Persons")

story.append(Paragraph("Type 2: Exempt taxable persons — Articles 132–137 VAT-D", H2))
story.append(Paragraph(
    "Some entities technically qualify as taxable persons (they carry on economic activities "
    "independently) but their specific activities are <b>exempt</b> from VAT by law. "
    "They are called <b>taxable persons without the right of deduction</b>.", BODY))

story += info_box("What 'exempt' means here",
    "Exempt taxable persons do NOT have to charge output VAT on their supplies. "
    "But the flipside is that they also CANNOT deduct the input VAT they pay on their purchases. "
    "The VAT they pay on inputs becomes a <b>cost</b> embedded in their prices.")

story.append(Paragraph("Examples of exempt activities (Art. 132–137 VAT-D):", H3))
story += [
    bp("Hospital and medical care services"),
    bp("Education (schools, universities)"),
    bp("Insurance and reinsurance transactions"),
    bp("Banking and financing services"),
    bp("The supply of human organs, blood, and mother's milk"),
    bp("Services supplied by non-profit organisations to their members"),
    bp("Cultural services by public bodies"),
    Spacer(1, 0.15*cm),
]

story.append(Paragraph("Mixed taxable persons", H2))
story.append(Paragraph(
    "Many entities carry on <i>both</i> exempt and taxable activities. These are called "
    "<b>mixed taxable persons</b> and they have a <b>partial right of deduction</b>.", BODY))

story += two_col_table(
    "Entity", "Mix of Activities",
    [
        ("University",
         "Education (exempt, Art. 132(1)(i)) + scientific conferences subject to VAT → "
         "can deduct input VAT only on the proportion linked to taxable activities."),
        ("Bank",
         "Granting loans (exempt, Art. 135(1)(b)) + leasing of personal property (VATable) → "
         "partial deduction."),
        ("Sports Club (non-profit)",
         "Providing sport facilities (exempt, Art. 132(1)(m)) + selling beverages (VATable) → "
         "partial deduction."),
    ]
)

story += exam_tip(
    "Distinguish clearly: an exempt taxable person charges NO output VAT but gets NO "
    "input VAT deduction. A standard taxable person charges output VAT AND gets full input VAT deduction. "
    "A mixed person gets partial deduction.")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.6  NON-TAXABLE LEGAL PERSONS
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.6", "Non-Taxable Legal Persons")

story.append(Paragraph("Type 3: Non-taxable legal persons — Article 13 VAT-D", H2))
story.append(Paragraph(
    "Government authorities and public-law bodies are a special category. When they act as "
    "<b>public authorities</b> (exercising sovereign powers), they are <b>not</b> considered "
    "VAT taxable persons, even if they collect fees or charges.", BODY))

story += info_box("Art. 13(1) — the general rule",
    "States, regional and local government authorities and other public-law bodies are NOT "
    "taxable persons when they engage in activities <b>as public authorities</b>, even where they "
    "collect dues, fees, or payments for those activities.")

story += example_box(
    "Typical non-taxable public activities",
    "• Issuing traffic fines (coercive sovereign power — no VAT).<br/>"
    "• Civil registration (birth, marriage, death certificates).<br/>"
    "• Issuing building permits.<br/>"
    "• Collecting property taxes.")

story.append(Paragraph("Two important exceptions — when public bodies ARE taxable", H2))

story += [
    bp("<b>Exception 1 — Significant distortion of competition:</b> If treating the public body "
       "as a non-taxable person would distort competition significantly with private operators, "
       "it must be treated as a taxable person."),
    Spacer(1, 0.1*cm),
]
story += example_box(
    "Municipality parking lot",
    "A municipality operates a public car park. If it is treated as non-taxable (no VAT charged), "
    "it gains an unfair price advantage over private car-park operators who must charge VAT. "
    "Therefore the municipality IS treated as a taxable person for this activity.")

story += [
    bp("<b>Exception 2 — Annex I activities:</b> Public bodies are ALWAYS taxable for certain "
       "commercial activities listed in Annex I of the VAT-D, regardless of scale:"),
    bp2("Telecommunications services"),
    bp2("Supply of water, gas, electricity, and steam"),
    bp2("Transport of goods and passengers"),
    bp2("Port and airport services"),
    bp2("Organisation of trade fairs and exhibitions"),
    bp2("Warehousing services"),
    Spacer(1, 0.2*cm),
]

story += exam_tip(
    "The test for a public body: Are they acting as a public authority (exercising sovereign powers)? "
    "If yes → not a taxable person (unless competition distortion or Annex I applies). "
    "If no (acting commercially) → they ARE a taxable person.")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.8  VAT GROUPING
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.8", "VAT Grouping")

story.append(Paragraph("What is a VAT group? — Article 11 VAT-D", H2))
story += info_box("Art. 11",
    "After consulting the VAT Committee, each Member State <b>may</b> regard as a single taxable "
    "person any persons established in that MS who, while legally independent, are closely bound "
    "to one another by <b>financial, economic, and organisational links</b>.")

story.append(Paragraph("Requirements for VAT grouping:", H3))
story += [
    bp("At least <b>two persons</b>."),
    bp("All persons are <b>established in the territory</b> of the same Member State "
       "(cross-border VAT groups are not possible under Art. 11)."),
    bp("The persons are <b>closely bound</b> by all three types of links: financial "
       "(common ownership/control), economic (shared business purpose), and organisational "
       "(common management or direction)."),
    Spacer(1, 0.15*cm),
]
story += example_box(
    "VAT group",
    "A German parent company has three German subsidiaries. All four entities are legally "
    "separate but share the same management team and are 100% owned by the parent. "
    "Germany allows them to form a single VAT group → they file one VAT return and "
    "transactions between group members are <b>not VAT-able</b>.")

story.append(Paragraph("Practical effects of VAT grouping:", H2))
story += two_col_table(
    "Type of transaction", "VAT treatment",
    [
        ("Between group members (intra-group)",
         "NOT treated as taxable supplies — VAT is not charged on transactions between members. "
         "This eliminates cash-flow costs for exempt group members who cannot recover input VAT."),
        ("With external parties (outside the group)",
         "Treated as taxable supplies — VAT is charged normally, as if the group were a single entity."),
    ]
)

story += [
    bp("This is an <b>optional article</b> — Member States can choose whether to implement it."),
    bp("Where implemented, the specific rules and thresholds vary by country."),
    bp("The key benefit is <b>administrative simplification</b>: one VAT return, one VAT number, "
       "no pre-financing of VAT on intra-group services."),
    Spacer(1, 0.2*cm),
]

story += exam_tip(
    "VAT grouping is optional for Member States. Not all EU countries implement it. "
    "The benefit is neutralising VAT costs on intra-group flows — especially valuable when "
    "some group members are exempt (e.g. a bank group).")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.9  WHICH TRANSACTIONS ARE TAXABLE?
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.9", "Which Transactions Are Taxable?")

story.append(Paragraph(
    "Article 2(1) VAT-D lists the four categories of transaction subject to VAT:", BODY))
story += [
    bp("(a) Supply of goods for consideration within a Member State by a taxable person"),
    bp("(b) Intra-Community acquisition of goods (ICA) by a taxable person or a non-taxable "
       "legal person"),
    bp("(c) Supply of services for consideration within a Member State by a taxable person"),
    bp("(d) Importation of goods"),
    Spacer(1, 0.2*cm),
]

# ---- Supply of goods ----
story.append(Paragraph("A. Supply of Goods", H2))
story += info_box("Art. 14(1) definition",
    '"Supply of goods" = <b>the transfer of the right to dispose of tangible property as owner</b>. '
    'The key is the transfer of ownership rights (use, sell, destroy), not necessarily the '
    'physical handover.')

story.append(Paragraph("What counts as 'goods'?", H3))
story += [
    bp("Tangible (physical) property — anything you can touch."),
    bp("Electricity, gas, heat, cooling energy are <b>deemed tangible goods</b> (Art. 15(1))."),
    bp("Member States may also treat certain interests in immovable property as goods (Art. 15(2))."),
    bp("<b>Intangible property (patents, software licences, know-how) → supply of SERVICES, not goods.</b>"),
    Spacer(1, 0.1*cm),
]

story.append(Paragraph("Three cumulative requirements for a taxable supply of goods:", H3))
story += [
    bp("<b>For consideration</b> — the seller must receive agreed payment linked to the supply."),
    bp("<b>By a taxable person</b> — the seller must be a VAT taxable person acting as such."),
    bp("<b>Within the territory of a Member State</b> — the place of supply rules (Arts 31–37) "
       "determine which country's VAT applies."),
    Spacer(1, 0.2*cm),
]

story.append(Paragraph("Self-supply of goods — Article 16 VAT-D", H2))
story += info_box("Purpose of Art. 16",
    "When a business buys goods and deducts input VAT (on the assumption they will be used for "
    "taxable business purposes), then later diverts those goods to <b>private use or non-business "
    "purposes</b>, a <b>deemed taxable supply</b> arises. This corrects the wrongly-claimed deduction.")

story += [
    bp("<b>What triggers self-supply:</b> applying business assets to private use, giving goods away "
       "free of charge, or using them for purposes unrelated to the business."),
    bp("<b>Exception:</b> samples or gifts of small/negligible value — these are not treated as a "
       "taxable supply."),
    bp("<b>Tax base for self-supply:</b> the purchase price of the goods or similar goods "
       "(i.e. cost price, not marked-up retail price)."),
    Spacer(1, 0.1*cm),
]
story += example_box(
    "Self-supply of goods",
    "A car dealer buys a car for €20,000 (deducts €4,200 input VAT at 21%). The dealer then "
    "permanently uses the car for his own private commuting. This triggers a self-supply: output "
    "VAT of 21% × €20,000 = €4,200 must be declared. The input VAT deduction is effectively "
    "reversed without actually amending the original deduction.")

story.append(Paragraph("Excluded transactions — Article 19 VAT-D", H2))
story += info_box("Corporate restructurings",
    "When a <b>totality of assets</b> (or a branch of a business) is transferred — whether for "
    "consideration or not — Member States <b>may</b> treat this as a non-supply. The transferee "
    "steps into the shoes of the transferor and inherits all VAT rights and obligations.")
story += example_box(
    "Merger",
    "Company A merges into Company B, transferring all its assets. Strictly this is a 'supply' "
    "of those assets, which could trigger massive VAT. Under Art. 19, Member States can treat "
    "this as VAT-neutral: no output VAT is charged and Company B assumes all Company A's VAT "
    "history.")

story.append(Paragraph("Place of supply of goods — where is VAT due?", H2))
story.append(Paragraph(
    "The place of supply determines which Member State's VAT system (including its rate) applies.", BODY))

story += two_col_table(
    "Situation", "Place of Supply",
    [
        ("Goods are not moved (stationary goods)",
         "Where the goods are physically located at the time of supply (Art. 31)."),
        ("Goods transported by supplier/customer/third party",
         "Where the goods are located when <b>transport begins</b> (Art. 32). "
         "[Export exemption may apply if destination is outside EU.]"),
        ("Goods installed or assembled by the supplier",
         "Where the installation or assembly takes place."),
        ("Goods supplied on ships/planes/trains (within EU)",
         "Point of departure of the transport."),
    ]
)
story += example_box(
    "Place of supply examples",
    "<b>1.</b> French company A sells radiators and installs them in a Brussels building → "
    "place of supply = Belgium (where installation takes place).<br/>"
    "<b>2.</b> Belgian seller ships goods to a Swiss buyer → place of supply = Belgium "
    "(where transport begins); export exemption may apply.<br/>"
    "<b>3.</b> Passengers on a Thalys train departing Brussels buy food on board → place of supply "
    "= Belgium (point of departure).")

story.append(Paragraph("Time of supply of goods (chargeable event) — Article 63 VAT-D", H2))
story += info_box("General rule",
    "VAT becomes chargeable when the goods are <b>supplied</b>. This is when the supplier's "
    "obligation to pay arises and the customer's right to deduct input VAT begins.")
story += [
    bp("<b>Exception for successive supplies</b> (e.g. gas, electricity, water delivered on a "
       "continuous basis): supply is deemed complete at the end of each billing period."),
    Spacer(1, 0.2*cm),
]

# ---- Services ----
story.append(Paragraph("B. Supply of Services", H2))
story += info_box("Art. 24 definition",
    '"Supply of services" = <b>any transaction that does not constitute a supply of goods</b>. '
    'This is a residual, catch-all definition ensuring everything not covered as a good '
    'falls under services.')
story.append(Paragraph("The wide scope includes:", H3))
story += [
    bp("IT services, software-as-a-service"),
    bp("Hotel and restaurant services"),
    bp("Telecommunications, broadcasting"),
    bp("Cleaning, maintenance, security"),
    bp("Construction, renovation, and services relating to immovable property"),
    bp("Accounting, legal, translation, advertising services"),
    bp("All transactions relating to intangible property — both <b>sale</b> (transfer of title) "
       "and <b>licensing</b> (transfer of user rights) — fall under services (Art. 25 VAT-D)."),
    Spacer(1, 0.1*cm),
]

story.append(Paragraph("Self-supply of services — Article 26 VAT-D", H2))
story += info_box("Two triggers (Art. 26)",
    "(a) Using a <b>business asset</b> for private purposes when input VAT on that asset was deductible.<br/>"
    "(b) Providing services <b>free of charge</b> for non-business purposes.")
story += example_box(
    "Self-supply of a service",
    "A company buys a company car and deducts input VAT. An employee uses the car for "
    "private trips at the weekend. The private use constitutes a self-supply of services: "
    "output VAT must be declared on the market value of that private use.")

story.append(Paragraph("Place of supply of services — B2B vs B2C", H2))
story.append(Paragraph(
    "The place-of-supply rules for services hinge on whether the recipient is a "
    "<b>taxable person (B2B)</b> or a <b>non-taxable person (B2C)</b>.", BODY))

story += two_col_table(
    "Who is 'taxable person' for place-of-service rules?",
    "Examples",
    [
        ("Ordinary taxable persons (Art. 9)",
         "Any business, sole trader, etc."),
        ("Exempt taxable persons",
         "Hospitals, schools, insurance companies, banks"),
        ("Mixed taxable persons",
         "Universities, sports clubs, banks"),
        ("Non-taxable legal persons identified for VAT",
         "Government bodies registered for VAT (as acquirers)"),
    ]
)

story += info_box("General rule B2B (Art. 44)",
    "The place of supply is where the <b>recipient (customer)</b> is established. "
    "Mechanism: <b>reverse charge</b> — the customer self-assesses VAT in its own country.")
story += info_box("General rule B2C (Art. 45)",
    "The place of supply is where the <b>supplier</b> is established.",
    bg=GREEN_BG, label_style=LABEL_G)

story += example_box(
    "B2B service — general rule",
    "A Belgian law firm provides legal advice to a German GmbH (a taxable person). "
    "Under B2B rules, the place of supply is Germany (where the customer is). "
    "The Belgian firm issues an invoice WITHOUT VAT; the German GmbH self-assesses "
    "German VAT via reverse charge and can deduct it in the same return.")
story += example_box(
    "B2C service — general rule",
    "A French graphic designer provides logo design to a private individual in Spain. "
    "The place of supply is France (where the supplier is). French VAT applies.")

story.append(Paragraph("Exceptions — same rule for both B2B and B2C:", H3))
story += two_col_table(
    "Type of service", "Place of supply",
    [
        ("Services connected with immovable property "
         "(estate agents, hotel accommodation, architects, construction)",
         "Where the property is located"),
        ("Admission to cultural, sporting, scientific, entertainment events "
         "(concerts, fairs, exhibitions)",
         "Where the event takes place"),
        ("Restaurant & catering services",
         "Where the service is physically provided"),
        ("Short-term car rental (≤ 30 days)",
         "Where the vehicle is put at the customer's disposal"),
    ]
)

story.append(Paragraph("Additional exceptions — B2C only:", H3))
story += two_col_table(
    "Service (B2C)", "Place of supply",
    [
        ("Telecommunications, broadcasting, electronic services",
         "Where the non-taxable <b>customer</b> is established, has their permanent address, "
         "or usually resides. (Destination principle for digital services.)"),
        ("Intellectual property, advertising, professional services to non-EU non-taxable persons",
         "Where the non-taxable customer outside the EU is established → no EU VAT applies."),
    ]
)

story.append(Paragraph("Reverse charge mechanism (B2B cross-border services)", H2))
story += info_box("Why reverse charge exists",
    "Under the general B2B rule, the place of supply is where the customer is. Without reverse "
    "charge, the foreign supplier would need to register for VAT in every country where it has "
    "customers — an enormous administrative burden. Reverse charge solves this: the customer "
    "self-assesses the VAT in its home country, charges itself output VAT, and deducts that same "
    "amount as input VAT in the same return (net effect = zero cost for a fully taxable business).")

story.append(Paragraph("Time of supply of services", H2))
story += [
    bp("<b>General rule:</b> when the service is supplied (completed)."),
    bp("<b>Exception for successive services</b> (e.g. monthly streaming subscription): "
       "supply is deemed complete at the end of each billing/accounting period."),
    Spacer(1, 0.2*cm),
]

# ---- Importation ----
story.append(Paragraph("C. Importation of Goods", H2))
story += info_box("Art. 30 VAT-D",
    "Importation = the entry of goods from <b>outside the EU</b> into the EU territory.")
story += [
    bp("<b>General rule (Art. 60):</b> place of importation = the Member State in whose "
       "territory the goods are located when they enter the EU."),
    bp("<b>Exception 1:</b> goods immediately exported onwards outside the EU → importation "
       "not treated as taxable."),
    bp("<b>Exception 2 (Art. 156):</b> goods placed in a customs warehouse → VAT payment is "
       "<b>suspended</b> until the goods are released into free circulation."),
    Spacer(1, 0.1*cm),
]
story += info_box("Time of importation",
    "VAT liability arises at the <b>moment the goods physically enter EU territory</b> and become "
    "subject to customs controls — or when they are withdrawn from a suspension arrangement "
    "(e.g. taken out of a customs warehouse).")
story += example_box(
    "Importation",
    "A Belgian company imports textiles from Bangladesh. The goods arrive at the port of Antwerp. "
    "Import VAT is due in Belgium at the moment of entry. The company can deduct this import VAT "
    "as input VAT in its Belgian VAT return.")

story += exam_tip(
    "Four taxable transactions: (1) domestic supply of goods, (2) supply of services, "
    "(3) import of goods, (4) intra-Community acquisition. Know the conditions and place/time rules for each.")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.10  INTRA-COMMUNITY ACQUISITION (ICA)
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.10", "Intra-Community Acquisition (ICA) of Goods")

story += info_box("Art. 20 definition",
    '"Intra-Community acquisition of goods" = the acquisition of the right to dispose as owner of '
    '<b>movable tangible property dispatched or transported</b> to the acquirer in a Member State '
    'other than that in which the dispatch or transport began.')

story.append(Paragraph(
    "ICA arises when goods physically <i>cross</i> an EU internal border from one MS to another — "
    "it is the buyer's-side event mirroring the seller's Intra-Community Supply (ICS).", BODY))

story.append(Paragraph("Key conditions for ICA:", H3))
story += [
    bp("The goods must be <b>movable and tangible</b> (ICA does not apply to services)."),
    bp("The <b>seller</b> must be a taxable person."),
    bp("The <b>buyer (acquirer)</b> must ordinarily be a taxable person — "
       "ICA generally does NOT arise for private individuals, exempt taxable persons, "
       "or non-taxable legal persons (unless exceptions apply)."),
    Spacer(1, 0.15*cm),
]

story.append(Paragraph("Scenario 1 — Both supplier and customer are ordinary taxable persons", H2))
story += [
    bp("Conditions of Art. 20 are met → ICA occurs."),
    bp("VAT liability arises in the <b>Member State of destination</b>."),
    bp("Mechanism: <b>reverse charge (Art. 200 VAT-D)</b>:"),
    bp2("Supplier issues an invoice <b>without VAT</b>."),
    bp2("The supplier's side = exempt Intra-Community Supply (ICS) in the MS of origin."),
    bp2("The purchaser declares VAT in its own return (self-assesses ICA VAT) and simultaneously "
        "deducts it as input VAT → net effect usually zero."),
    Spacer(1, 0.1*cm),
]
story += example_box(
    "ICA — B2B",
    "A French manufacturer sells machinery to a Belgian distributor. The machinery is transported "
    "from France to Belgium. <b>France:</b> the French company makes an exempt ICS — no French VAT "
    "charged. <b>Belgium:</b> the Belgian company reports an ICA and pays Belgian VAT on the invoice "
    "value. It simultaneously deducts that Belgian VAT as input VAT. Net cost = €0.")

story.append(Paragraph("Scenario 2 — Supplier is a taxable person; customer is a private individual", H2))
story += [
    bp("No ICA arises in principle."),
    bp("VAT should be paid in the <b>country of origin</b> (where transport begins)."),
    bp("Special distance-selling rules may modify this for high-volume B2C cross-border sales "
       "(but those are marked as 'not to be studied' in the course)."),
    Spacer(1, 0.15*cm),
]

story.append(Paragraph("Place and time of ICA:", H3))
story += [
    bp("<b>Place:</b> the Member State where the dispatch or transport of goods to the acquirer ends."),
    bp("<b>Time:</b> when the goods are acquired (generally when the ICA 'event' occurs, "
       "i.e. upon delivery of the goods at destination)."),
    Spacer(1, 0.2*cm),
]

story += exam_tip(
    "ICA is the mirror image of ICS. The seller makes an exempt ICS in the MS of departure. "
    "The buyer makes a taxable ICA in the MS of destination, using reverse charge. "
    "Result: VAT is levied in the country of consumption.")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.11  WHICH TRANSACTIONS ARE EXEMPT FROM VAT?
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.11", "Which Transactions Are Exempt from VAT?")

story.append(Paragraph(
    "Exemptions are transactions that meet all the requirements to be taxable, but the law "
    "specifically removes the VAT obligation. There are two very different types of exemption "
    "with opposite consequences.", BODY))

story += two_col_table(
    "Type of Exemption", "Right to Deduct Input VAT?",
    [
        ("Exempt WITH right of deduction ('zero-rated')",
         "YES — the business still deducts input VAT, even though it charges no output VAT."),
        ("Exempt WITHOUT right of deduction",
         "NO — the business neither charges output VAT nor deducts input VAT. VAT becomes a cost."),
    ]
)

story.append(Paragraph("Category 1 — Exempt WITH right of deduction (zero-rated)", H2))
story += info_box("Why this category exists",
    "Goods leaving one Member State for another (ICS) or leaving the EU entirely (exports) should "
    "not bear VAT from the country of departure — they are consumed elsewhere. But the exporting "
    "business should not be penalised by losing its input VAT deduction. Solution: exempt the "
    "outgoing supply BUT preserve the right to deduct input VAT.")

story.append(Paragraph("Two main cases:", H3))

story.append(Paragraph("<b>1. Intra-Community Supply of goods (ICS) — Art. 138 VAT-D</b>", BODY))
story += [
    bp("The seller in MS A makes an <b>exempt ICS</b> (no output VAT charged)."),
    bp("The buyer in MS B makes a <b>taxable ICA</b> (pays VAT in MS B)."),
    bp("No double taxation — VAT is collected once, in the destination MS."),
    bp("The seller retains the right to deduct input VAT on costs related to the ICS."),
    Spacer(1, 0.1*cm),
]
story += example_box(
    "ICS",
    "A Belgian company sells and ships laptops to a German GmbH. Belgian VAT: exempt ICS "
    "(zero-rated), but the Belgian company keeps the right to deduct all input VAT on its "
    "purchases. German side: the GmbH reports an ICA and pays German VAT, which it deducts "
    "immediately.")

story.append(Paragraph("<b>2. Export (supply outside EU) — Art. 146 VAT-D</b>", BODY))
story += [
    bp("The supply of goods dispatched to a destination <b>outside the EU</b> is exempt from VAT "
       "in the exporting country."),
    bp("The goods are intended for consumption outside the EU → no EU VAT should follow them."),
    bp("The exporter retains the right to deduct all input VAT related to the exported goods."),
    Spacer(1, 0.1*cm),
]
story += example_box(
    "Export",
    "A German car manufacturer exports cars to Japan. German VAT: exempt export. The manufacturer "
    "still deducts German input VAT on steel, components, and factory costs. Japanese import duties "
    "and taxes apply separately.")

story.append(Paragraph("Category 2 — Exempt WITHOUT right of deduction (Arts. 132–137)", H2))
story.append(Paragraph(
    "These are 'true' exemptions for social, cultural, or policy reasons. The logic is different: "
    "these sectors are excluded from the VAT system entirely. They receive services without paying "
    "VAT to their clients, but they cannot recover VAT on their own costs.", BODY))

story += two_col_table(
    "Exempt Activity", "Policy Rationale",
    [
        ("Hospital & medical care", "Essential health services should be affordable; VAT would raise costs."),
        ("Education", "Public interest — affordable learning, especially for lower-income groups."),
        ("Banking & insurance", "Technically difficult to calculate VAT on financial margins/premiums."),
        ("Supply of human organs, blood", "Humanitarian — not appropriate to commercialise."),
        ("Non-profit organisations' services to members",
         "Support for civil society and voluntary sector."),
        ("Postal services by public bodies", "Universal service obligations."),
    ]
)

story += info_box("Hidden cost of exemption without deduction",
    "Because these entities cannot deduct input VAT, the VAT they pay on their inputs "
    "(e.g. hospital equipment, bank computer systems) becomes an <b>embedded cost</b>. "
    "This creates an incentive to in-source services rather than buy them externally. "
    "Economists call this the 'hidden' VAT cost on exempt sectors.")

story += exam_tip(
    "Always ask two questions about an exemption: (1) Does the transaction meet all requirements "
    "for a taxable supply? (2) Is it exempt? Then ask: (3) Is it exempt WITH or WITHOUT the right "
    "to deduct input VAT? The answer determines whether the exemption is commercially beneficial "
    "(zero-rated exports/ICS) or a hidden cost (education, health, banking).")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.12  HOW MUCH VAT IS DUE?
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.12", "How Much VAT Is Due?")

story.append(Paragraph("VAT is calculated as: <b>Taxable Amount × VAT Rate</b>", H2))

story.append(Paragraph("A. VAT Rates", H2))
story += info_box("Minimum rates under VAT-D",
    "• <b>Standard rate:</b> each MS sets its own, but it must be <b>at least 15%</b> (Art. 97).<br/>"
    "• <b>Reduced rate(s):</b> one or two rates of at least <b>5%</b> (Art. 98(1)), applied to up to "
    "24 categories from Annex III of the VAT-D.<br/>"
    "• <b>Super-reduced rate:</b> below 5%, available for up to 7 goods/services from Annex III (Art. 98(2)).")

story += two_col_table(
    "Rate Category", "Description & Examples",
    [
        ("Standard rate (≥ 15%)",
         "Default rate for all goods and services not covered by a lower rate. "
         "Belgium: 21% | Germany: 19% | Luxembourg: 17%."),
        ("Reduced rate (≥ 5%)",
         "Applied to social necessities: food, books, newspapers, medicines, hotel accommodation, "
         "children's clothing. Belgium 6% or 12%."),
        ("Super-reduced rate (< 5%)",
         "Very limited items — certain foods, newspapers, social housing, restaurant meals "
         "(where permitted). Luxembourg applies 3% on certain items."),
        ("Zero rate (0%)",
         "Technically a reduced rate at 0% — allows full input VAT deduction. "
         "UK (before Brexit) used this extensively for children's clothes, food. "
         "Not all MS use a 0% rate."),
    ]
)

story.append(Paragraph("B. The Taxable Amount (VAT Base) — Article 73 VAT-D", H2))
story += info_box("Art. 73 definition",
    "The taxable amount = <b>everything which constitutes consideration obtained by the supplier "
    "from the customer in return for the supply</b>.")
story += [
    bp("Normally = the selling price (invoice amount excluding VAT)."),
    bp("Includes: delivery charges, packaging, insurance linked to the supply."),
    bp("<b>Excluded from the taxable amount:</b>"),
    bp2("Price reductions and discounts granted at the time of supply."),
    bp2("Rebates for early payment."),
    bp2("Amounts received as agent on behalf of the customer."),
    Spacer(1, 0.1*cm),
]

story.append(Paragraph("Special cases:", H3))
story += two_col_table(
    "Transaction type", "Taxable Amount",
    [
        ("Self-supply of goods (Art. 74)",
         "The <b>purchase price</b> of those goods or similar goods, or the cost of production."),
        ("Self-supply of services (Art. 75)",
         "The <b>full cost</b> of providing the service (materials + labour + overhead)."),
        ("Barter / non-monetary consideration",
         "The <b>open market value</b> of the goods or services received."),
    ]
)

story += example_box(
    "Taxable amount calculation",
    "A retailer sells goods for €1,000. The invoice shows:<br/>"
    "• Goods: €1,000<br/>"
    "• Early payment discount (2% if paid in 10 days): not deducted from taxable amount unless taken.<br/>"
    "• Delivery fee: €50 (part of taxable amount)<br/>"
    "• <b>Taxable amount = €1,050; VAT at 21% = €220.50</b><br/>"
    "If the customer pays early and claims the 2% discount (€21), the taxable amount can be "
    "adjusted to €1,029 and VAT becomes €216.09.")

story += exam_tip(
    "The taxable amount is the consideration received — typically the price excl. VAT. "
    "Discounts granted AT the time of sale reduce the taxable amount. "
    "Discounts granted AFTER the fact (credit notes) also allow correction. "
    "Self-supply bases are cost-based, not market-price based.")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.13  DEDUCTION OF INPUT VAT
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.13", "Deduction of Input VAT")

story.append(Paragraph(
    "The right of deduction is what makes VAT neutral for businesses. Without it, VAT would "
    "cascade and businesses would bear a permanent cost. The mechanics matter enormously in practice.", BODY))

story.append(Paragraph("Conditions for deduction", H2))
story += [
    bp("The goods or services must be used for the purposes of the taxable person's "
       "<b>taxable transactions</b> (or exempt transactions with right of deduction)."),
    bp("'Taxable transactions' means both ordinary taxed supplies <i>and</i> zero-rated supplies "
       "(ICS/exports) — because both generate output VAT or are equivalent."),
    bp("<b>Immediate deduction</b> — you do not need to wait until you make the output sale. "
       "Deduction arises as soon as the purchase is made (destination principle)."),
    bp("This means input VAT deduction and the related output VAT liability fall in the <b>same "
       "VAT return period</b>."),
    Spacer(1, 0.15*cm),
]

story.append(Paragraph("Transitional correction — change from taxable to exempt use", H2))
story += info_box("Correction mechanism",
    "If an asset was originally acquired for taxable purposes (input VAT deducted) but is later "
    "used for exempt purposes, a <b>self-supply correction</b> applies (see Art. 16 and Art. 26). "
    "This output VAT charge effectively reverses the earlier deduction.")

story.append(Paragraph("Mixed taxpayers — partial deduction", H2))
story.append(Paragraph(
    "When a business carries on BOTH taxable activities (right to deduct) AND exempt activities "
    "(no right to deduct), it is a <b>mixed taxpayer</b>. Its input VAT deduction is limited to "
    "a proportional fraction — Arts. 173–174 VAT-D.", BODY))

story += info_box("Pro-rata formula (Art. 174)",
    "Deductible fraction = <b>Turnover from taxable activities ÷ Total turnover (taxable + exempt)</b><br/>"
    "Rounded up to the nearest whole number.")

story += example_box(
    "Mixed taxpayer deduction",
    "A university earns €400,000 from conferences (VATable) and €600,000 from tuition (exempt). "
    "Total turnover = €1,000,000. Pro-rata = 400,000 / 1,000,000 = <b>40%</b>.<br/>"
    "If the university pays €50,000 input VAT on shared costs (building maintenance, IT), "
    "it can only deduct 40% × €50,000 = <b>€20,000</b>. "
    "The remaining €30,000 becomes a cost embedded in tuition pricing.")

story += two_col_table(
    "Business type", "Input VAT deduction",
    [
        ("Fully taxable (standard/reduced rate only)", "100% deduction"),
        ("Zero-rated / ICS / exports", "100% deduction (right of deduction maintained)"),
        ("Fully exempt (hospital, bank, school)", "0% — no deduction"),
        ("Mixed (university, bank + leasing, sports club + bar)", "Pro-rata % deduction"),
    ]
)

story += exam_tip(
    "The pro-rata for mixed taxpayers is a core calculation topic. Always check: "
    "(1) Is the business mixed? (2) What is the taxable/total revenue split? "
    "(3) Apply the fraction to shared input VAT. Input VAT directly attributable to a specific "
    "activity (taxable or exempt) is deducted in full or not at all — only truly 'shared' "
    "costs use the pro-rata.")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  11.14  ADVANCED ISSUES
# ════════════════════════════════════════════════════════════════════════════
story += section_header("11.14", "Advanced Issues — VAT Gap, Fraud & Abuse")

story.append(Paragraph("A. Budgetary Importance of VAT and the VAT Gap", H2))
story += info_box("Scale of VAT revenues",
    "VAT generates approximately <b>€1 trillion per year</b> across all EU Member States — "
    "making it one of the most significant revenue sources for governments. It typically "
    "represents 15–25% of total government tax revenue in EU countries.")

story += info_box("The VAT Gap",
    "The VAT gap = the difference between <b>expected VAT revenues</b> (if all rules were perfectly "
    "followed) and VAT revenues <b>actually collected</b>. It represents lost public resources.",
    bg=RED_BG, label_style=LABEL_R)

story.append(Paragraph("Why does the VAT gap exist?", H3))
story += two_col_table(
    "Cause", "Explanation",
    [
        ("Fraud", "Deliberate evasion — taxpayers conceal taxable activities or claim false refunds."),
        ("Tax avoidance", "Legal but unintended exploitation of loopholes to reduce VAT liability."),
        ("Bankruptcies / insolvencies",
         "Companies collect VAT from customers but go bankrupt before remitting it to the government."),
        ("Miscalculations / administrative errors",
         "Honest mistakes in applying complex VAT rules."),
    ]
)
story += example_box(
    "Scale of the VAT gap",
    "The EU estimates the total annual VAT gap at roughly €60–90 billion. That lost revenue "
    "could fund approximately 185 state-of-the-art hospitals per year, or build 1,700 km of "
    "high-speed railway from Berlin to Bucharest. There are huge disparities: Finland has a "
    "gap of ~1.3% of expected revenue; Italy's gap has historically exceeded 20%.")

story.append(Paragraph("B. VAT Fraud", H2))
story += info_box("Definition",
    "VAT fraud = <b>deliberate and illegal</b> activities undertaken to evade or defraud the VAT system.",
    bg=RED_BG, label_style=LABEL_R)

story.append(Paragraph("The most important type: Missing Trader Intra-Community (MTIC) fraud", H3))
story += [
    bp("A chain of transactions is constructed across different EU MS."),
    bp("One company (the 'missing trader' or 'buffer') collects VAT from its customer but "
       "disappears without remitting it to the tax authority."),
    bp("Other companies in the chain may be genuine or complicit."),
    bp("The result: the fraudster pockets the VAT, and someone else in the chain claims an "
       "input VAT refund for VAT that was never paid."),
    Spacer(1, 0.1*cm),
]
story += example_box(
    "MTIC / Carousel fraud",
    "Company A (France) supplies goods VAT-free (ICS) to Company B (Belgium). "
    "Company B charges VAT to Company C and collects it, but disappears. "
    "Company C claims input VAT deduction on its purchase from B. "
    "Company C then sells goods back to France (ICS — exempt). The goods 'carousel' around "
    "EU borders with the VAT being claimed but never paid, draining the treasury.")

story.append(Paragraph("Other types of VAT fraud:", H3))
story += [
    bp("<b>Fictitious invoicing:</b> issuing or receiving fake invoices for transactions that "
       "never occurred, solely to fraudulently claim input VAT deduction."),
    bp("<b>False/overstated VAT refund claims:</b> submitting inflated refund claims to obtain "
       "money from the tax authority that is not owed."),
    Spacer(1, 0.2*cm),
]

story.append(Paragraph("C. VAT Abuse", H2))
story += info_box("Distinction from fraud",
    "VAT abuse = exploiting <b>weaknesses or loopholes</b> in VAT legislation to gain "
    "unintended tax advantages. It involves <b>no illegal activity</b>, but still distorts "
    "the VAT system and creates unfair advantages.")

story.append(Paragraph("Examples of VAT abuse:", H3))
story += [
    bp("<b>Artificial splitting of transactions:</b> a business splits its activities into separate "
       "entities to stay below VAT registration thresholds or to qualify for lower rates that would "
       "not apply to a single larger entity."),
    bp("<b>Improper use of VAT exemptions:</b> misinterpreting eligibility criteria for exemptions "
       "(e.g. claiming an educational exemption for what is actually a commercial training "
       "programme)."),
    bp("<b>Manipulation of supply chains:</b> creating artificial intermediate companies or "
       "complex transaction structures to reduce VAT liability or maximise refund claims."),
    Spacer(1, 0.15*cm),
]

story += two_col_table(
    "VAT Fraud vs VAT Abuse",
    "Key Distinction",
    [
        ("Fraud", "Illegal — criminal penalties may apply. E.g. MTIC, fictitious invoices."),
        ("Abuse", "Legal but contrary to VAT principles — corrected by anti-avoidance rules "
                  "and the principle of abuse of rights (Halifax doctrine, CJEU)."),
    ]
)

story.append(Paragraph("Countermeasures:", H3))
story += [
    bp("<b>Data analytics:</b> tax authorities use transaction-level data (VIES system, "
       "SAF-T reporting) to detect suspicious patterns."),
    bp("<b>Information sharing:</b> Eurofisc is an EU-wide network for rapid exchange of "
       "targeted information on VAT fraud."),
    bp("<b>Anti-avoidance rules:</b> the Halifax doctrine (CJEU) allows tax authorities to "
       "deny VAT benefits where arrangements constitute an abuse of EU law."),
    bp("<b>Reverse charge extension:</b> applying reverse charge to domestic high-risk sectors "
       "(e.g. construction, mobile phones) eliminates the opportunity for the supplier to "
       "disappear with VAT."),
    Spacer(1, 0.2*cm),
]

story += exam_tip(
    "Fraud = illegal; abuse = legal but exploiting loopholes. Know both MTIC carousel fraud "
    "(the mechanics and why it works) and the three main abuse types. Both topics signal "
    "policy awareness — examiners love asking 'why is this a problem and how is it addressed?'")

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════════════════
#  QUICK REFERENCE SUMMARY
# ════════════════════════════════════════════════════════════════════════════
story += section_header("QUICK REFERENCE", "Key Concepts at a Glance")

story.append(Paragraph("Three types of VAT taxpayers", H2))
story += two_col_table(
    "Type", "Description",
    [
        ("Basic taxable person (Art. 9)",
         "Any person independently carrying on an economic activity. Full VAT obligations + full right to deduct."),
        ("Exempt taxable person (Arts. 132-137)",
         "Economic activity, but specific supplies are exempt. No output VAT + no input VAT deduction."),
        ("Non-taxable legal person (Art. 13)",
         "Public authorities acting as such. Not a taxable person unless competition distortion or Annex I."),
    ]
)

story.append(Paragraph("The four taxable transactions", H2))
story += two_col_table(
    "Transaction", "Key rule",
    [
        ("Supply of goods (Art. 2(1)(a))",
         "Transfer of disposal right over tangible goods for consideration, by a taxable person, within a MS."),
        ("Supply of services (Art. 2(1)(c))",
         "Any transaction not being a supply of goods. B2B: place = customer's location. "
         "B2C: place = supplier's location (with exceptions)."),
        ("ICA (Art. 20)",
         "Cross-border transfer of goods between taxable persons within the EU. "
         "Taxed in destination MS via reverse charge."),
        ("Importation (Art. 30)",
         "Entry of goods from outside EU. VAT due in MS where goods enter the EU."),
    ]
)

story.append(Paragraph("VAT rates framework", H2))
story += two_col_table(
    "Rate", "Minimum | Applies to",
    [
        ("Standard rate", "≥ 15% | All goods and services not otherwise rated"),
        ("Reduced rate", "≥ 5% | Up to 24 items from Annex III (food, books, hotel, medicines)"),
        ("Super-reduced rate", "< 5% | Up to 7 items from Annex III (selective policy items)"),
        ("Zero rate / ICS / Export", "0% | Cross-border supplies; full input VAT deduction maintained"),
    ]
)

story.append(Paragraph("Exemption comparison", H2))
story += two_col_table(
    "Exemption type", "Output VAT charged? | Input VAT deducted?",
    [
        ("Exempt WITH right of deduction (ICS, export)",
         "No output VAT | YES — full deduction"),
        ("Exempt WITHOUT right of deduction (health, education, banking)",
         "No output VAT | NO — no deduction"),
    ]
)

# final note
story.append(Spacer(1, 0.5*cm))
story.append(HRFlowable(width="100%", thickness=1, color=DARK_BLUE, spaceAfter=8))
story.append(Paragraph(
    "Study tip: Work through the chapter sections in order and practice applying the rules "
    "to short fact patterns. Each section builds on the previous — knowing who is a taxable person "
    "is the prerequisite for deciding which transactions are taxable, which in turn determines "
    "whether VAT is due and whether input VAT can be deducted.",
    S("final", fontSize=10, textColor=DARK_BLUE, fontName="Helvetica-Oblique",
      leading=14, alignment=TA_JUSTIFY)))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "Based on Chapter 11 of <i>Principles of Taxation</i> by Prof. dr. Niels Bammens & "
    "Prof. dr. Filip Debelva · Expanded study guide",
    CAPTION))

# ── BUILD ─────────────────────────────────────────────────────────────────────
doc.build(story)
print("PDF generated: Chapter11_VAT_Study_Guide.pdf")
