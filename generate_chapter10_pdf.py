#!/usr/bin/env python3
"""
Expanded Study Guide: Chapter 10 - Tax Treaty Provisions
Based on: Principles of Taxation, Bammens & Debelva (KU Leuven)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# ── Colour palette (KU Leuven-inspired) ───────────────────────────────────────
DARK_BLUE  = colors.HexColor("#003D6B")
TEAL       = colors.HexColor("#007FA3")
LIGHT_TEAL = colors.HexColor("#E8F4F8")
LIGHT_GREY = colors.HexColor("#F2F2F2")
ORANGE_TIP = colors.HexColor("#E87722")
WHITE      = colors.white
TEXT_DARK  = colors.HexColor("#1A1A2E")

PAGE_W, PAGE_H = A4
MARGIN = 2.0 * cm

# ── Style helpers ──────────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    def s(name, parent="Normal", **kw):
        p = ParagraphStyle(name, parent=base[parent])
        for k, v in kw.items():
            setattr(p, k, v)
        return p

    styles = {}
    styles["title"]      = s("title",   "Title",  fontSize=26, textColor=WHITE,
                               alignment=TA_CENTER, spaceAfter=6,
                               fontName="Helvetica-Bold")
    styles["subtitle"]   = s("subtitle","Normal", fontSize=13, textColor=LIGHT_TEAL,
                               alignment=TA_CENTER, spaceAfter=4,
                               fontName="Helvetica")
    styles["h1"]         = s("h1",      "Heading1", fontSize=17, textColor=WHITE,
                               fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=6,
                               leftIndent=0)
    styles["h2"]         = s("h2",      "Heading2", fontSize=13, textColor=DARK_BLUE,
                               fontName="Helvetica-Bold", spaceBefore=10, spaceAfter=4)
    styles["h3"]         = s("h3",      "Heading3", fontSize=11, textColor=TEAL,
                               fontName="Helvetica-Bold", spaceBefore=7, spaceAfter=3)
    styles["body"]       = s("body",    "Normal",   fontSize=10, textColor=TEXT_DARK,
                               leading=15, spaceAfter=5, alignment=TA_JUSTIFY,
                               fontName="Helvetica")
    styles["bullet"]     = s("bullet",  "Normal",   fontSize=10, textColor=TEXT_DARK,
                               leading=14, spaceAfter=3, leftIndent=16,
                               firstLineIndent=-10, fontName="Helvetica",
                               bulletText="•")
    styles["bullet2"]    = s("bullet2", "Normal",   fontSize=10, textColor=TEXT_DARK,
                               leading=13, spaceAfter=2, leftIndent=32,
                               firstLineIndent=-10, fontName="Helvetica",
                               bulletText="–")
    styles["code"]       = s("code",    "Normal",   fontSize=9.5, textColor=DARK_BLUE,
                               leading=13, fontName="Helvetica-Oblique",
                               leftIndent=12, spaceAfter=4)
    styles["tip"]        = s("tip",     "Normal",   fontSize=10, textColor=DARK_BLUE,
                               fontName="Helvetica-Bold", leading=14, spaceAfter=0)
    styles["toc"]        = s("toc",     "Normal",   fontSize=11, textColor=DARK_BLUE,
                               leading=18, fontName="Helvetica")
    styles["caption"]    = s("caption", "Normal",   fontSize=9, textColor=TEAL,
                               fontName="Helvetica-Oblique", alignment=TA_CENTER,
                               spaceAfter=4)
    styles["table_hdr"]  = s("table_hdr","Normal",  fontSize=10, textColor=WHITE,
                               fontName="Helvetica-Bold", alignment=TA_CENTER)
    styles["table_cell"] = s("table_cell","Normal", fontSize=10, textColor=TEXT_DARK,
                               fontName="Helvetica", alignment=TA_CENTER, leading=13)
    styles["exam_flag"]  = s("exam_flag","Normal",  fontSize=10, textColor=ORANGE_TIP,
                               fontName="Helvetica-Bold", spaceAfter=2)
    return styles

# ── Flowable factories ─────────────────────────────────────────────────────────
def section_banner(text, styles):
    """Dark-blue banner for top-level section headings."""
    tbl = Table([[Paragraph(text, styles["h1"])]], colWidths=[PAGE_W - 2*MARGIN])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), DARK_BLUE),
        ("LEFTPADDING",  (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING",   (0,0), (-1,-1),  7),
        ("BOTTOMPADDING",(0,0), (-1,-1),  7),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return tbl

def info_box(content_paras, styles, bg=LIGHT_TEAL, border=TEAL):
    """Teal-background info/law-text box."""
    cells = [[p] for p in content_paras]
    tbl = Table(cells, colWidths=[PAGE_W - 2*MARGIN - 24])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), bg),
        ("BOX",          (0,0), (-1,-1), 1.5, border),
        ("LEFTPADDING",  (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING",   (0,0), (-1,-1),  6),
        ("BOTTOMPADDING",(0,0), (-1,-1),  6),
    ]))
    return tbl

def exam_box(text, styles):
    """Orange exam-tip box."""
    tbl = Table([[Paragraph("EXAM FOCUS — " + text, styles["exam_flag"])]],
                colWidths=[PAGE_W - 2*MARGIN])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), colors.HexColor("#FFF3E0")),
        ("BOX",          (0,0), (-1,-1), 1.5, ORANGE_TIP),
        ("LEFTPADDING",  (0,0), (-1,-1), 10),
        ("TOPPADDING",   (0,0), (-1,-1),  6),
        ("BOTTOMPADDING",(0,0), (-1,-1),  6),
    ]))
    return tbl

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=TEAL, spaceAfter=4, spaceBefore=4)

def sp(n=6):
    return Spacer(1, n)

def numeric_table(headers, rows, col_widths=None, styles_dict=None):
    """Styled table for numerical examples."""
    if col_widths is None:
        avail = PAGE_W - 2*MARGIN - 1*cm
        col_widths = [avail / len(headers)] * len(headers)
    hdr_row = [Paragraph(h, styles_dict["table_hdr"]) for h in headers]
    data = [hdr_row]
    for i, row in enumerate(rows):
        cells = [Paragraph(str(c), styles_dict["table_cell"]) for c in row]
        data.append(cells)
    tbl = Table(data, colWidths=col_widths)
    style = [
        ("BACKGROUND",   (0,0), (-1,0), DARK_BLUE),
        ("TEXTCOLOR",    (0,0), (-1,0), WHITE),
        ("ALIGN",        (0,0), (-1,-1), "CENTER"),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 10),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [LIGHT_GREY, WHITE]),
        ("GRID",         (0,0), (-1,-1), 0.5, TEAL),
        ("TOPPADDING",   (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0), (-1,-1), 5),
    ]
    # bold last row (totals)
    if len(rows) >= 1:
        style.append(("FONTNAME", (0,-1), (-1,-1), "Helvetica-Bold"))
        style.append(("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#D0E8F2")))
    tbl.setStyle(TableStyle(style))
    return tbl

# ══════════════════════════════════════════════════════════════════════════════
#  CONTENT BUILDER
# ══════════════════════════════════════════════════════════════════════════════
def build_story(styles):
    S = styles
    story = []

    def h1(t):  return section_banner(t, S)
    def h2(t):  return Paragraph(t, S["h2"])
    def h3(t):  return Paragraph(t, S["h3"])
    def p(t):   return Paragraph(t, S["body"])
    def b(t):   return Paragraph(t, S["bullet"])
    def b2(t):  return Paragraph(t, S["bullet2"])
    def cod(t): return Paragraph(t, S["code"])
    def ex(t):  return exam_box(t, S)

    # ─────────────────────────────────────────────────────────────────────
    # COVER PAGE
    # ─────────────────────────────────────────────────────────────────────
    cover_tbl = Table(
        [[Paragraph("CHAPTER 10", ParagraphStyle("cv1", fontName="Helvetica-Bold",
            fontSize=14, textColor=LIGHT_TEAL, alignment=TA_CENTER))],
         [Paragraph("Tax Treaty Provisions", ParagraphStyle("cv2", fontName="Helvetica-Bold",
            fontSize=30, textColor=WHITE, alignment=TA_CENTER, leading=34))],
         [Spacer(1, 8)],
         [Paragraph("An Expanded Study Guide", ParagraphStyle("cv3", fontName="Helvetica",
            fontSize=14, textColor=LIGHT_TEAL, alignment=TA_CENTER))],
         [Spacer(1, 20)],
         [Paragraph("Principles of Taxation · KU Leuven<br/>Prof. dr. F. Debelva &amp; Prof. dr. N. Bammens",
            ParagraphStyle("cv4", fontName="Helvetica", fontSize=11,
            textColor=colors.HexColor("#AACFDD"), alignment=TA_CENTER, leading=16))]],
        colWidths=[PAGE_W - 2*MARGIN]
    )
    cover_tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0,0), (-1,-1), DARK_BLUE),
        ("TOPPADDING",   (0,0), (-1,-1), 18),
        ("BOTTOMPADDING",(0,0), (-1,-1), 18),
        ("LEFTPADDING",  (0,0), (-1,-1), 24),
        ("RIGHTPADDING", (0,0), (-1,-1), 24),
    ]))
    story += [sp(80), cover_tbl, sp(30)]

    note_tbl = Table([[Paragraph(
        "This document expands on the lecture slides with detailed explanations, "
        "worked examples, and exam-focus notes. All article references are to the "
        "<b>OECD Model Tax Convention</b> unless stated otherwise.",
        ParagraphStyle("note", fontName="Helvetica", fontSize=10,
            textColor=DARK_BLUE, alignment=TA_JUSTIFY, leading=14))]],
        colWidths=[PAGE_W - 2*MARGIN]
    )
    note_tbl.setStyle(TableStyle([
        ("BACKGROUND",  (0,0),(-1,-1), LIGHT_TEAL),
        ("BOX",         (0,0),(-1,-1), 1, TEAL),
        ("LEFTPADDING", (0,0),(-1,-1), 12),
        ("TOPPADDING",  (0,0),(-1,-1),  8),
        ("BOTTOMPADDING",(0,0),(-1,-1), 8),
    ]))
    story += [note_tbl, PageBreak()]

    # ─────────────────────────────────────────────────────────────────────
    # TABLE OF CONTENTS
    # ─────────────────────────────────────────────────────────────────────
    story += [h2("Table of Contents"), hr(), sp(4)]
    toc_items = [
        ("10.1", "Material Scope of Application — Article 2"),
        ("10.2", "Personal Scope of Application — Articles 1 & 4"),
        ("10.3", "Income from Immovable Property — Article 6"),
        ("10.4", "Business Profits — Articles 5, 7 & 8"),
        ("10.5", "Employment Income — Articles 15–19"),
        ("10.6", "Investment Income — Articles 10, 11 & 12"),
        ("10.7", "Students — Article 20"),
        ("10.8", "Other Income — Article 21"),
        ("10.9", "Elimination of Double Taxation — Articles 23A & 23B"),
    ]
    for num, title in toc_items:
        story.append(Paragraph(f"<b>{num}</b>  &nbsp; {title}",
            ParagraphStyle("toc_i", fontName="Helvetica", fontSize=11,
                textColor=DARK_BLUE, leading=20, leftIndent=8)))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────────────
    # INTRODUCTION
    # ─────────────────────────────────────────────────────────────────────
    story += [h2("Introduction: Why Do Tax Treaties Exist?"), hr(), sp(4)]
    story.append(p(
        "When a person earns income that crosses international borders, two countries "
        "often claim the right to tax that same income — the country where the income "
        "arises (<b>source state</b>) and the country where the taxpayer lives "
        "(<b>residence state</b>). This creates <b>international double taxation</b>, "
        "which discourages cross-border investment and trade."
    ))
    story.append(p(
        "Tax treaties (formally: Double Taxation Conventions, or DTCs) are bilateral "
        "agreements between two states that <b>allocate taxing rights</b> and "
        "<b>eliminate double taxation</b>. The vast majority of the world's tax "
        "treaties are based on the <b>OECD Model Tax Convention</b>, whose articles "
        "are the backbone of this chapter."
    ))
    story.append(p(
        "To benefit from a tax treaty, a taxpayer must clear <b>two gateway tests</b>:"
    ))
    story += [
        b("(1) <b>Personal scope</b> — the taxpayer must be a <i>resident</i> of one or "
          "both contracting states (Arts. 1 & 4)."),
        b("(2) <b>Material scope</b> — the tax at issue must be a type of tax covered "
          "by the treaty (Art. 2)."),
        sp(8)
    ]

    # ─────────────────────────────────────────────────────────────────────
    # 10.1  MATERIAL SCOPE
    # ─────────────────────────────────────────────────────────────────────
    story += [h1("10.1  Material Scope of Application — Article 2"), sp(6)]

    story.append(h2("What Does Article 2 Say?"))
    story.append(info_box([
        cod("Article 2(1): This Convention shall apply to taxes on income and on "
            "capital imposed on behalf of a Contracting State or of its political "
            "subdivisions or local authorities, irrespective of the manner in which "
            "they are levied."),
        cod("Article 2(4): The Convention shall also apply to any identical or "
            "substantially similar taxes that are imposed after the date of signature "
            "of the Convention in addition to, or in place of, the existing taxes."),
    ], S))
    story.append(sp(6))

    story.append(h3("Key Points"))
    story += [
        b("<b>Only taxes on income and capital are covered.</b> The following are "
          "<u>NOT</u> covered: VAT, customs duties, succession/inheritance duties, "
          "social security contributions, and most local levies that are not income "
          "or capital taxes."),
        b("<b>Level of government is irrelevant.</b> Whether the tax is levied by the "
          "central government, a region, a province, or a municipality, it is still "
          "covered — as long as it is a tax on income or capital."),
        b("<b>Non-exhaustive list (Art. 2(3)).</b> The treaty lists 'in particular' "
          "the taxes to which it applies. Because the word 'particularly' is used, "
          "the list is not closed — other income/capital taxes not explicitly listed "
          "may still fall within scope."),
        b("<b>Future taxes are also covered (Art. 2(4)).</b> If a contracting state "
          "introduces a new tax after the treaty is signed that is 'identical or "
          "substantially similar' to the listed taxes, that new tax is also covered. "
          "The competent authorities must notify each other of significant tax law "
          "changes."),
        b("<b>Exception:</b> Art. 24 (non-discrimination) is one provision that can "
          "apply even to taxes not covered by Art. 2 in some contexts."),
        sp(6)
    ]
    story.append(ex("Know what is NOT covered (VAT, social security, succession "
                    "duties). Expect scenario questions asking whether a specific "
                    "tax falls within the treaty's scope."))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────────────
    # 10.2  PERSONAL SCOPE
    # ─────────────────────────────────────────────────────────────────────
    story += [h1("10.2  Personal Scope of Application — Articles 1 & 4"), sp(6)]

    story.append(h2("Article 1: The Basic Rule"))
    story.append(info_box([
        cod("This Convention shall apply to persons who are residents of one or both "
            "of the Contracting States.")], S))
    story.append(sp(6))
    story.append(p(
        "Two questions therefore arise: (a) Who counts as a <b>person</b>? "
        "(b) What makes someone a <b>resident</b> of a contracting state?"
    ))

    story.append(h2("Who Is a 'Person'? — Article 3(1)(a)-(b)"))
    story.append(info_box([
        cod("The term 'person' includes an individual, a company and any other body "
            "of persons. The term 'company' means any body corporate or any entity "
            "that is treated as a body corporate for tax purposes.")], S))
    story.append(sp(4))
    story += [
        b("<b>Individuals</b> — natural persons."),
        b("<b>Companies</b> — any legal entity taxed as a corporation."),
        b("<b>Other bodies of persons</b> — e.g., partnerships (depending on how "
          "they are classified under domestic law), trusts, estates, etc."),
        sp(6)
    ]

    story.append(h2("Who Is a 'Resident'? — Article 4"))
    story.append(info_box([
        cod("For the purposes of this Convention, the term 'resident of a Contracting "
            "State' means any person who, under the laws of that State, is liable to "
            "tax therein by reason of his domicile, residence, place of management or "
            "any other criterion of a similar nature ... This term, however, does not "
            "include any person who is liable to tax in that State in respect only of "
            "income from sources in that State or capital situated therein.")], S))
    story.append(sp(6))

    story.append(h3("Breaking Down the Definition"))
    story += [
        b("<b>'Liable to tax'</b> — The person must be subject to tax in that state "
          "based on a <i>personal nexus</i> (domicile, residence, place of management, "
          "or similar). This means the state has the right to tax the person's "
          "<i>worldwide income</i> (unlimited tax liability)."),
        b2("Important distinction: being <b>liable to tax</b> (the legal "
           "obligation exists) is <u>not the same as</u> actually paying "
           "tax (<b>subject to tax</b>). An exempt entity (e.g., a pension fund) "
           "that is still theoretically within the scope of the tax law is 'liable "
           "to tax' and therefore qualifies as a resident."),
        b("<b>Territorial tax systems</b> — Some states (e.g., Hong Kong, Panama) "
          "only tax domestic income, not worldwide income. A person resident in such "
          "a state is still a 'resident' under Art. 4 <i>if</i> the basis of "
          "residence is a personal nexus (e.g., physical presence/domicile), not "
          "merely the fact of earning local income."),
        b("<b>Exclusion clause</b> — A person who is only liable to tax in a state "
          "in respect of income <i>from sources in that state</i> (not worldwide) is "
          "<u>not</u> a resident for treaty purposes. This prevents third-country "
          "residents from claiming treaty benefits simply because they earn local "
          "income."),
        b("<b>States and subdivisions</b> — A contracting state itself, its political "
          "subdivisions, and recognised pension funds are also considered residents."),
        sp(6)
    ]
    story.append(ex("Frequently tested: the difference between 'liable to tax' and "
                    "'subject to tax'. You do not need to actually pay taxes to qualify "
                    "as a resident — the liability must merely exist."))

    story.append(h2("Dual Residence — Individuals: Tie-Breaker Rules (Art. 4(2))"))
    story.append(p(
        "A person can be a 'resident' under the <i>domestic law</i> of both "
        "contracting states simultaneously — for example, one state uses domicile "
        "and the other uses a days-of-presence test. To avoid a situation where both "
        "states claim full residence, Art. 4(2) provides a cascade of "
        "<b>tie-breaker rules</b>, applied <i>in strict sequential order</i>. "
        "Only if a test fails to produce a conclusive result do you move to the next."
    ))

    tie_data = [
        ["Priority", "Test", "Key Concept"],
        ["1", "Permanent home", "Where does the individual have a dwelling continuously available at all times? Any form of home qualifies (owned, rented, borrowed) — the key is permanence, not ownership."],
        ["2", "Centre of vital interests", "Which state has the closer personal and economic ties? Looks at: family, social relations, occupations, political/cultural activities, place of business. Personal relations are generally decisive."],
        ["3", "Habitual abode", "Where does the individual customarily or usually spend time? Not a simple day-count; only stays that are part of the settled routine of life are counted. Days in transit are excluded."],
        ["4", "Nationality", "Of which state is the individual a national (citizen)?"],
        ["5", "Mutual agreement", "If none of the above tests resolves the tie, the competent authorities of the two states negotiate a solution under Art. 25 (not examined in detail)."],
    ]
    col_ws = [1.5*cm, 3.5*cm, PAGE_W - 2*MARGIN - 5*cm]
    story.append(numeric_table(["Priority","Test","Key Concept"], tie_data[1:], col_ws, S))
    story.append(sp(6))

    story.append(h3("Closer Look: Permanent Home (Test 1)"))
    story += [
        b("The home can be <b>any form of dwelling</b>: apartment, house, rented room, etc."),
        b("What matters is <b>permanence</b> — the individual must have the home "
          "continuously available, not just for short occasional stays (e.g., holidays "
          "or business trips)."),
        b("If the individual has a permanent home in <i>both</i> states, this test is "
          "inconclusive → move to test 2."),
        sp(4)
    ]
    story.append(h3("Closer Look: Centre of Vital Interests (Test 2)"))
    story += [
        b("Assessed <b>as a whole</b>: no single factor is automatically decisive."),
        b("Typical factors: where the family lives, where social/professional life is "
          "centred, where bank accounts, clubs, church attendance, political activity "
          "are found."),
        b("In practice, <b>personal (family) relations</b> tend to outweigh economic "
          "relations if the two point in different directions."),
        sp(6)
    ]

    story.append(h2("Dual Residence — Companies: Article 4(3)"))
    story.append(p(
        "Companies can also be dual-resident. This arises because states use different "
        "connecting factors: one state may use the <b>place of incorporation</b>, "
        "another the <b>place of effective management</b>. The 2017 OECD Model "
        "removed the automatic tie-breaker (place of effective management) for "
        "companies and now requires a <b>mutual agreement procedure</b> (MAP). "
        "Factors considered: place of effective management, place of incorporation, "
        "and any other relevant factors."
    ))
    story.append(sp(6))
    story.append(ex("Know the 5 tie-breaker tests for individuals and their order. "
                    "For companies: remember the shift to MAP under the 2017 OECD Model."))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────────────
    # 10.3  IMMOVABLE PROPERTY
    # ─────────────────────────────────────────────────────────────────────
    story += [h1("10.3  Income from Immovable Property — Article 6"), sp(6)]

    story.append(h2("The Basic Rule"))
    story.append(p(
        "Article 6 allocates the right to tax income from immovable property to the "
        "<b>state where the property is situated (the source state)</b>. This is a "
        "<i>shared</i> taxing right (the word used is 'may be taxed'), meaning the "
        "residence state can also tax — but must then grant relief under Art. 23."
    ))

    story.append(h2("What Counts as 'Immovable Property'?"))
    story += [
        b("The primary reference is the <b>domestic law of the source state</b>. "
          "If something is 'immovable property' under source-state law, it is covered."),
        b("Regardless of source-state domestic law, the treaty <i>always</i> covers:"),
        b2("Livestock and equipment used in agriculture and forestry"),
        b2("Rights to variable or fixed payments as consideration for the working of, "
           "or the right to work, mineral deposits, sources and other natural "
           "resources"),
        b("<b>Ships and aircraft are expressly excluded</b> from 'immovable property'. "
          "Income from their operation is governed by Article 8."),
        sp(6)
    ]

    story.append(h2("Capital Gains — Article 13(1)"))
    story.append(p(
        "The OECD Model maintains <b>symmetry</b> between recurrent income from "
        "immovable property (Art. 6) and capital gains on its sale (Art. 13(1)). "
        "Both are taxable exclusively in the state where the property is located. "
        "This makes commercial sense: the state that taxes ongoing rental income "
        "should also be able to tax the gain when the property is sold."
    ))
    story.append(sp(6))
    story.append(ex("Art. 6 + Art. 13(1) together: source state has EXCLUSIVE taxing "
                    "rights over both income AND gains from immovable property."))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────────────
    # 10.4  BUSINESS PROFITS
    # ─────────────────────────────────────────────────────────────────────
    story += [h1("10.4  Business Profits — Articles 5, 7 & 8"), sp(6)]

    story.append(h2("The Fundamental Problem"))
    story.append(p(
        "When a company resident in State A (the 'home state') carries on commercial "
        "activities in State B (the 'source state'), two taxation claims arise: "
        "State A taxes on worldwide profits, and State B wants to tax the locally "
        "generated profits. The treaty must allocate who gets to tax what."
    ))
    story += [
        b("<b>Two ways to operate abroad:</b>"),
        b2("<b>Separate legal person</b> (e.g., a subsidiary): creates a new company "
           "tax-resident in State B. That entity is taxed in State B as a local "
           "company. Double taxation is addressed by the parent-subsidiary rules or "
           "treaty dividends provisions (Art. 10)."),
        b2("<b>Permanent establishment (PE)</b>: the original company remains tax-resident "
           "only in State A but carries on activities in State B through a branch or "
           "office. There is no new legal person."),
        sp(6)
    ]

    story.append(h2("The General Rule — Article 7"))
    story.append(info_box([
        cod("Business profits of an enterprise of a Contracting State shall be "
            "taxable only in that State (= home state) unless the enterprise carries "
            "on business in the other Contracting State through a permanent "
            "establishment. If it does, the other state may tax the profits, but only "
            "to the extent they are attributable to that PE.")], S))
    story.append(sp(4))
    story.append(p(
        "The PE concept therefore acts as a <b>threshold</b>: the source state can "
        "only tax if the foreign enterprise has a sufficient presence there. "
        "Without a PE, all profits go to the home state."
    ))
    story.append(sp(6))

    # Art. 5 PE ─────────────────────────────────────────────────────────
    story.append(h2("Article 5: What Is a Permanent Establishment (PE)?"))
    story.append(p(
        "There are <b>two types</b> of PE: the <b>Fixed Place PE</b> "
        "(Arts. 5(1)–(4)) and the <b>Agency PE</b> (Arts. 5(5)–(6))."
    ))

    story.append(h3("A. Fixed Place PE — Article 5(1): The General Definition"))
    story.append(info_box([
        cod("A fixed place of business through which the business of an enterprise "
            "is wholly or partly carried on.")], S))
    story.append(sp(4))
    story.append(p("Three cumulative elements must <i>all</i> be present:"))

    # Element 1
    story.append(h3("Element 1 — A Place of Business"))
    story += [
        b("Any kind of <b>material (physical) presence</b> suffices. The concept is "
          "very broad."),
        b("Does <i>not</i> need to be a building, office, or formal premises. "
          "Examples: a machine, server, pipeline, vending machine, oil well, circus "
          "tent, kiosk."),
        b("Can be located in the premises of <i>another</i> enterprise."),
        b("The nature of the legal right over the place is irrelevant — ownership, "
          "rent, licence, or even illegal occupation can suffice."),
        b("<b>Key requirement</b>: the location must be <i>at the disposal</i> of "
          "the enterprise, meaning it has effective control to use it to conduct its "
          "business. Merely visiting a customer's premises rarely creates a PE."),
        sp(6)
    ]

    # Element 2
    story.append(h3("Element 2 — Fixed"))
    story += [
        b("'Fixed' has two dimensions:"),
        b2("<b>Geographically fixed</b>: there must be a link between the place of "
           "business and a specific geographic location."),
        b2("<b>Temporally fixed</b>: the business must be carried on with a degree "
           "of permanence. There are <i>no fixed time thresholds</i> in the general "
           "rule — assessed case by case."),
        b("Activities across <b>multiple locations</b> in the same state can still "
          "constitute a <i>single</i> PE if they form a coherent commercial and "
          "geographic whole (e.g., a mine with shifting extraction sites; a trader "
          "with different stalls in the same outdoor market)."),
        sp(6)
    ]

    # Element 3
    story.append(h3("Element 3 — Business of the Enterprise Is Carried On Through That Place"))
    story += [
        b("The activities must be <b>commercial in nature</b>. It is not required "
          "that the PE is profitable or carries on the same activities as the head "
          "office."),
        b("Activities are <i>normally</i> conducted by personnel, but personnel is "
          "<i>not</i> a strict requirement. Automated equipment (vending machines, "
          "gaming machines, pipelines) can create a PE."),
        b("Simply <b>making property available</b> (e.g., passively renting out a "
          "building without managing it) does <i>not</i> usually constitute carrying "
          "on a 'business' for PE purposes."),
        sp(6)
    ]

    story.append(h3("B. Article 5(2): Non-Exhaustive List of Examples"))
    story.append(info_box([
        cod("The term 'permanent establishment' includes especially: (a) a place of "
            "management; (b) a branch; (c) an office; (d) a factory; (e) a workshop; "
            "(f) a mine, an oil or gas well, a quarry or any other place of extraction "
            "of natural resources.")], S))
    story.append(sp(4))
    story.append(p(
        "The word 'especially' makes clear this list is <i>not exhaustive</i>. "
        "These examples give a first indication that a PE may exist, but each "
        "must still satisfy all three elements of Art. 5(1) on a case-by-case basis."
    ))
    story.append(sp(6))

    story.append(h3("C. Article 5(3): Construction Sites — Special Rule"))
    story.append(info_box([
        cod("A building site or construction or installation project constitutes a "
            "permanent establishment only if it lasts more than twelve months.")], S))
    story.append(sp(4))
    story += [
        b("This is the <b>only case where a minimum time threshold is specified</b> "
          "in the OECD Model. The general rule of Art. 5(1) has no fixed minimum."),
        b("Broad scope: includes construction of roads, bridges, canals, pipelines, "
          "and installation projects. Does <i>not</i> cover mere maintenance work or "
          "planning activities."),
        b("For <b>different construction sites</b>, the 12-month threshold is applied "
          "<i>separately</i> to each site — unless the sites form a <i>single "
          "commercial whole</i>, in which case they count as one PE."),
        sp(6)
    ]

    story.append(h3("D. Article 5(4): The Negative List — Preparatory or Auxiliary Activities"))
    story.append(p(
        "Even if a fixed place meets the Art. 5(1) definition, a PE is deemed "
        "<i>not</i> to exist if the activity is purely <b>preparatory or auxiliary</b> "
        "in nature. Article 5(4) lists specific excluded activities:"
    ))
    neg_list = [
        ["a)", "Storage, display, or delivery of goods belonging to the enterprise"],
        ["b)", "Maintenance of a stock of goods solely for storage, display or delivery"],
        ["c)", "Maintenance of a stock of goods solely for processing by another enterprise"],
        ["d)", "Maintaining a fixed place solely to purchase goods or collect information for the enterprise"],
        ["e)", "Maintaining a fixed place solely to carry on any other preparatory/auxiliary activity for the enterprise"],
        ["f)", "Any combination of (a)–(e), provided the overall activity is preparatory or auxiliary"],
    ]
    neg_tbl = Table(neg_list, colWidths=[1.5*cm, PAGE_W - 2*MARGIN - 1.5*cm])
    neg_tbl.setStyle(TableStyle([
        ("FONTNAME",     (0,0),(-1,-1), "Helvetica"),
        ("FONTSIZE",     (0,0),(-1,-1), 10),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[LIGHT_GREY, WHITE]),
        ("GRID",         (0,0),(-1,-1), 0.5, TEAL),
        ("TOPPADDING",   (0,0),(-1,-1),  4),
        ("BOTTOMPADDING",(0,0),(-1,-1),  4),
        ("LEFTPADDING",  (0,0),(-1,-1),  6),
        ("FONTNAME",     (0,0),(0,-1),  "Helvetica-Bold"),
        ("TEXTCOLOR",    (0,0),(0,-1),   DARK_BLUE),
    ]))
    story.append(neg_tbl)
    story.append(sp(6))

    story.append(p("Three conditions must ALL be met for the negative list to apply:"))
    story += [
        b("(1) The activity is <b>preparatory or auxiliary</b> in character — it must "
          "not be the <i>core business</i> of the enterprise."),
        b("(2) The activity is <b>expressly listed</b> in Art. 5(4)."),
        b("(3) The activity is carried out <b>exclusively for the head office</b> of "
          "the enterprise (not for a related company, a client, or a third party)."),
        sp(6)
    ]
    story.append(ex("Negative list: if an e-commerce warehouse does both storage AND "
                    "processing of returns for customers, it is no longer purely "
                    "'preparatory or auxiliary' — the negative list would NOT apply."))

    # Agency PE ─────────────────────────────────────────────────────────
    story.append(h3("E. Agency PE — Article 5(5)"))
    story.append(info_box([
        cod("Where a person is acting in a Contracting State on behalf of an "
            "enterprise and in doing so habitually concludes contracts, or habitually "
            "plays the principal role leading to the conclusion of contracts that are "
            "routinely concluded without material modification by the enterprise, "
            "and these contracts are: (A) in the name of the enterprise, or "
            "(B) for the transfer of ownership of, or for the granting of the right "
            "to use, property owned by that enterprise, or (C) for the provision of "
            "services by that enterprise — that enterprise shall be deemed to have a "
            "PE in that State.")], S))
    story.append(sp(4))
    story.append(p(
        "The Agency PE concept catches situations where a foreign enterprise does "
        "not have a physical location in the source state but uses a <i>dependent "
        "agent</i> there to effectively carry on its business. Key points:"
    ))
    story += [
        b("<b>Who triggers it?</b> Any person (individual or company) acting on "
          "behalf of the foreign enterprise — can be an employee, a related company, "
          "or even an independent contractor if they are economically dependent."),
        b("<b>'Habitually concludes contracts'</b>: the agent must do this "
          "repeatedly, not just once or twice. The 2017 revision also extended this "
          "to agents who 'habitually play the principal role' in concluding contracts "
          "that are then routinely rubber-stamped by the enterprise."),
        b("<b>Independent agent exception (Art. 5(6))</b>: A truly independent "
          "agent acting in the ordinary course of its business does NOT create an "
          "Agency PE. Independence is tested both legally and economically."),
        sp(6)
    ]

    # Art. 7 Attribution ─────────────────────────────────────────────────
    story.append(h2("Article 7: Attribution of Profits to a PE"))
    story.append(info_box([
        cod("The profits attributable to the PE are the profits it might be expected "
            "to make if it were a separate and independent enterprise engaged in the "
            "same or similar activities under the same or similar conditions, taking "
            "into account the functions performed, assets used and risks assumed "
            "by the enterprise through the PE and through the other parts of the "
            "enterprise.")], S))
    story.append(sp(6))

    story += [
        b("<b>No 'force of attraction'</b>: the mere fact that income is sourced in "
          "the PE-state does NOT automatically mean it is attributable to the PE. "
          "Example: if the head office makes a direct sale to a customer in State B "
          "without any involvement of the PE in State B, that profit stays with the "
          "home state."),
        b("<b>Authorised OECD Approach (AOA)</b>: the PE is treated as a "
          "hypothetical separate and independent enterprise (the 'functionally "
          "separate entity' approach). Profits are determined by analysing: "
          "functions performed, assets used, and risks assumed by the PE."),
        b("<b>OECD Transfer Pricing Guidelines</b> apply to transactions between "
          "the PE and the rest of the enterprise, just as they would apply between "
          "associated enterprises."),
        sp(6)
    ]

    # Art. 8 ─────────────────────────────────────────────────────────────
    story.append(h2("Article 8: International Shipping and Air Transport"))
    story.append(info_box([
        cod("Profits of an enterprise of a Contracting State from the operation of "
            "ships or aircraft in international traffic shall be taxable only in that "
            "State.")], S))
    story.append(sp(4))
    story += [
        b("<b>Exception to Art. 7</b> — even if the airline/shipping company has a "
          "PE in the other state, Art. 8 overrides and confines taxation to the "
          "home state."),
        b("<b>What is 'international traffic'?</b> Art. 3(1)(e): any transport by "
          "ship or aircraft EXCEPT when operated solely between places in a single "
          "contracting state by an enterprise of the other state. Example: a Swedish "
          "airline flying Copenhagen–Oslo = international traffic (covered by Art. 8). "
          "A Swedish airline flying Oslo–Bergen = domestic Norwegian traffic (Art. 7 "
          "applies, not Art. 8)."),
        b("<b>Ancillary activities</b> are also covered (e.g., cargo handling, "
          "container leasing activities directly connected to the transport)."),
        sp(6)
    ]

    story.append(h2("Capital Gains on Business Assets — Article 13(2) and (3)"))
    story += [
        b("<b>Art. 13(2)</b>: Capital gains from the alienation of movable property "
          "forming part of the business property of a PE may be taxed in the PE-state. "
          "This includes the gain from selling the PE itself."),
        b("<b>Art. 13(3)</b>: Gains from the alienation of ships, aircraft, or "
          "movable property in international traffic are taxable <i>exclusively</i> "
          "in the home state of the enterprise (consistent with Art. 8)."),
        sp(6)
    ]
    story.append(ex("Know the interplay between Art. 5, 7, and 8. A classic exam "
                    "scenario: does a foreign company's activity in State B constitute "
                    "a PE? Apply the three-element test, check the negative list, "
                    "check the Agency PE rules."))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────────────
    # 10.5  EMPLOYMENT INCOME
    # ─────────────────────────────────────────────────────────────────────
    story += [h1("10.5  Employment Income — Articles 15–19"), sp(6)]

    story.append(h2("General Remarks: A Closed System"))
    story.append(p(
        "Articles 15–19 form a <b>closed, self-contained system</b> for income from "
        "employment. Article 15 is the <i>lex generalis</i> (general rule) and "
        "Articles 16–19 are <i>leges speciales</i> (specific rules). Whenever a "
        "special rule applies, it takes precedence over Art. 15."
    ))
    summary_data = [
        ["Article", "Type of Income", "Taxing Right"],
        ["15", "General employment (salaries, wages)", "Residence state; work state if work done there"],
        ["16", "Directors' fees", "State of residence of the paying company"],
        ["17", "Entertainers & sportspersons", "Performance state (where activity is exercised)"],
        ["18", "Private sector pensions", "Exclusively in recipient's residence state"],
        ["19", "Government sector salaries & pensions", "Paying state (with 'close connection' exception)"],
    ]
    story.append(numeric_table(["Article","Type of Income","Taxing Right"],
        summary_data[1:], [1.5*cm, 6*cm, PAGE_W - 2*MARGIN - 7.5*cm], S))
    story.append(sp(8))

    # Art. 15 ─────────────────────────────────────────────────────────────
    story.append(h2("Article 15: General Employment Income"))

    story.append(h3("The Scope: What Income Does Art. 15 Cover?"))
    story.append(info_box([
        cod("'Salaries, wages and other similar remuneration derived … in respect of "
            "an employment.'")], S))
    story.append(sp(4))
    story += [
        b("Very <b>broad concept</b>: <i>any</i> remuneration received by reason of "
          "an employment relationship, regardless of its form or timing."),
        b("Includes <b>exceptional payments</b> such as signing bonuses, golden "
          "handshakes, golden parachutes, and non-compete payments."),
        b("<b>The reason for the payment is decisive, not the timing.</b> A bonus "
          "paid one year after the employment ends can still be employment income "
          "under Art. 15 if it relates to past services."),
        sp(4)
    ]

    story.append(h3("Exceptional Payments After Employment Ends"))
    story += [
        b("<b>Severance payments</b>: OECD Commentary suggests allocation on a "
          "<i>pro-rata basis</i> reflecting where the employment was exercised over "
          "the relevant period."),
        b("<b>Non-compete payments</b>: taxable only in the <i>residence state</i> "
          "at the time of payment, since they relate to future restraint, not past "
          "work."),
        sp(6)
    ]

    story.append(h3("The Basic Rule — Article 15(1)"))
    story += [
        b("<b>General rule</b>: employment income is taxable <i>only</i> in the "
          "employee's <b>state of residence</b>."),
        b("<b>Exception</b>: if the employment is <i>physically exercised</i> in "
          "another state (the 'work state'), that work state may also tax the "
          "income <i>attributable</i> to those workdays."),
        b("<b>How is the attribution calculated?</b> Proportion of workdays spent "
          "in the work state ÷ total workdays × total salary."),
        sp(6)
    ]

    story.append(h3("The Exception to the Exception — Article 15(2): The 183-Day Rule"))
    story.append(p(
        "Even where work is physically done in another state (which normally "
        "triggers source-state taxing rights under Art. 15(1)), the <b>work state "
        "loses its taxing right</b> if <b>all three</b> of the following conditions "
        "are met simultaneously:"
    ))
    conditions_183 = [
        ["Condition", "Description", "Underlying Rationale"],
        ["1 — Days",
         "The employee's physical presence in the work state does NOT exceed 183 days "
         "in any 12-month period commencing or ending in the fiscal year.",
         "Short-term presence has limited economic impact on the work state."],
        ["2 — Employer",
         "The remuneration is NOT paid by, or on behalf of, an employer who is "
         "a RESIDENT of the work state.",
         "Matching principle: if the employer deducts salary in the work state, "
         "that state should have the right to tax it."],
        ["3 — PE",
         "The remuneration is NOT borne by a permanent establishment that the "
         "employer has in the work state.",
         "Again matching principle: PE deductions → PE-state gets taxing right."],
    ]
    story.append(numeric_table(["Condition","Description","Underlying Rationale"],
        conditions_183[1:],
        [3*cm, 6.5*cm, PAGE_W - 2*MARGIN - 9.5*cm], S))
    story.append(sp(4))
    story.append(p(
        "<b>Practical consequence</b>: if ALL THREE conditions are satisfied, "
        "only the residence state taxes. As soon as ONE condition fails, the "
        "work state regains its taxing right."
    ))

    story.append(h3("Condition 1 in Detail: Counting 183 Days"))
    story += [
        b("<b>What counts as 'presence'?</b> All days (and parts of days) spent in "
          "the work state, including weekends, holidays, sick days, and arrival/departure "
          "days — even when not working."),
        b("<b>Exceptions</b> to the day-count: (1) days of illness that prevent the "
          "employee from leaving the work state are excluded; (2) days spent in "
          "transit through the work state are excluded."),
        b("<b>Twelve-month period</b>: the 183-day period is measured over any "
          "rolling 12-month window that either starts or ends in the relevant tax "
          "year (not necessarily a calendar year). This prevents artificial "
          "splitting of stays across year-end."),
        sp(6)
    ]

    story.append(h3("Condition 2 in Detail: Matching Principle"))
    story += [
        b("<b>Paid 'by'</b>: the employer (not resident in the work state) directly "
          "pays and bears the cost."),
        b("<b>Paid 'on behalf of'</b>: a third party (e.g., a subsidiary in the "
          "work state) advances the salary, but the <i>real economic cost</i> is "
          "ultimately borne by the employer (not in the work state) — e.g., via "
          "an inter-company recharge."),
        b("Both situations are caught by the condition ('or'). The key is where "
          "the <i>ultimate economic burden</i> of the salary lies."),
        sp(6)
    ]

    story.append(h3("Article 15(3): Employment Aboard Ships or Aircraft"))
    story += [
        b("An employee working aboard a ship or aircraft in international traffic "
          "is taxed <i>exclusively</i> in their <b>state of residence</b>."),
        b("Rationale: the physical-presence test of Art. 15(1)/(2) is impossible "
          "to apply in practice (the vessel moves between jurisdictions constantly)."),
        b("Only for employees <i>aboard</i> ships/aircraft. Truck drivers, train "
          "drivers, and sales representatives travelling internationally are NOT "
          "covered by Art. 15(3) and follow the general Art. 15(1)/(2) rules."),
        sp(6)
    ]
    story.append(ex("Exam-critical: the 183-day exception. All three conditions must "
                    "hold simultaneously. If any ONE fails, the work state gets to "
                    "tax. Watch for scenarios involving employer-resident-in-work-state "
                    "or salary borne by a PE in the work state."))

    # Art. 16 ─────────────────────────────────────────────────────────────
    story.append(h2("Article 16: Directors' Fees"))
    story += [
        b("Directors' fees are taxable in the state where the <b>paying company is "
          "resident</b> — regardless of where the director lives or where board "
          "meetings are held."),
        b("Rationale: it is practically difficult to track where directors perform "
          "their management functions."),
        b("Scope: monthly salary, <i>tantièmes</i> (profit-linked remuneration), "
          "and attendance fees paid for board participation."),
        b("Note: if a director also performs ordinary employment services (not "
          "director capacity), that portion falls under Art. 15."),
        sp(6)
    ]

    # Art. 17 ─────────────────────────────────────────────────────────────
    story.append(h2("Article 17: Entertainers and Sportspersons"))
    story.append(p(
        "Article 17 is an <b>exception to both Art. 7 and Art. 15</b>. "
        "It allocates taxing rights to the <b>performance state</b> — where the "
        "public activity takes place — regardless of whether the person is an "
        "employee or independent contractor, regardless of how many days they "
        "spend in that state, and regardless of whether they have a PE there."
    ))

    story.append(h3("Who Is an 'Entertainer'?"))
    story += [
        b("Theatre, motion picture, radio/television artists, musicians performing "
          "publicly. Performances broadcast via media are included."),
        b("Must be a <b>public performance with entertainment character</b>. "
          "Visual artists (sculptors, painters) are generally <i>not</i> covered."),
        b("Support staff — camera operators, directors, choreographers, road crew "
          "— are <i>not</i> covered by Art. 17 (they fall under Art. 15 or 7)."),
        sp(4)
    ]

    story.append(h3("Who Is a 'Sportsperson'?"))
    story += [
        b("Broad concept: athletes in traditional sports AND golfers, football "
          "players, tennis players, racing drivers, billiard players, snooker, "
          "chess, bridge."),
        b("Coaches, nutritionists, physiotherapists, mechanics are <i>not</i> "
          "sportspersons."),
        sp(4)
    ]

    story.append(h3("What Income Is Covered?"))
    story += [
        b("<b>Only payments for the public performance</b>. Example: a musician's "
          "performance fee at a live concert → Art. 17. Revenue from streaming or "
          "CD sales of recordings from that same concert → <i>not</i> Art. 17 "
          "(likely Art. 12 royalties or Art. 7 business profits)."),
        b("<b>Sponsorship money</b>: covered if there is a <i>close connection</i> "
          "to a specific performance (e.g., logo on jersey during the match). "
          "General year-round sponsorship unrelated to a particular performance → "
          "not Art. 17."),
        b("<b>Preparatory activities</b> (rehearsals, training): considered part of "
          "normal activities → covered by Art. 17 and taxed in the performance state."),
        sp(6)
    ]

    story.append(h3("Article 17(2): The 'Rent-a-Star' Anti-Abuse Rule"))
    story.append(p(
        "Without Art. 17(2), an entertainer could avoid source-state taxation by "
        "routing the performance fee through a company they control. Art. 17(2) "
        "extends the performance-state taxing right to any situation where income "
        "from the activity is paid <b>to a third party</b> (not the entertainer "
        "personally). Importantly, Art. 17(2) applies even where there is <i>no "
        "abuse</i> — any third-party payment for a performance triggers it."
    ))
    story.append(sp(6))
    story.append(ex("Art. 17 overrides Art. 7 and Art. 15: no need for a PE, no "
                    "183-day test. The performance state always taxes. Art. 17(2) "
                    "catches the 'rent-a-star' structure."))

    # Art. 18 ─────────────────────────────────────────────────────────────
    story.append(h2("Article 18: Pensions (Private Sector)"))
    story += [
        b("Covers pensions and <b>other similar remuneration paid in consideration "
          "of past employment</b> in the <i>private</i> sector."),
        b("Government/public pensions: governed by Art. 19, <i>not</i> Art. 18."),
        b("Scope: not just payments to the former employee — also widow's/survivor "
          "pensions are covered."),
        b("<b>Exclusively taxable in the recipient's state of residence.</b> The "
          "source state (paying state) has no taxing right."),
        b("Payments from individual life insurance contracts with no link to past "
          "employment are <i>not</i> covered by Art. 18 (likely Art. 21 other income)."),
        sp(6)
    ]

    # Art. 19 ─────────────────────────────────────────────────────────────
    story.append(h2("Article 19: Government Services"))
    story.append(p(
        "Covers salaries, wages, and pensions paid by a government or political "
        "subdivision for services rendered to that government."
    ))

    story.append(h3("Article 19(1)(a): General Rule for Salaries"))
    story += [
        b("Income paid by a government is taxable <i>only</i> in the "
          "<b>paying state</b> — regardless of where the services are performed "
          "or where the employee lives."),
        sp(4)
    ]

    story.append(h3("Article 19(1)(b): Exception"))
    story.append(p(
        "The work state (not the paying state) may tax if <b>all three</b> of the "
        "following apply:"
    ))
    story += [
        b("(1) The employment is exercised in the work state (the <i>other</i> "
          "contracting state, not the paying state)."),
        b("(2) The employee is a resident of the work state."),
        b("(3) The employee has a <b>close connection</b> to the work state: either "
          "(a) is a national of the work state, OR (b) did not become a resident "
          "of the work state solely for the purpose of rendering those services."),
        sp(4)
    ]
    story.append(p(
        "Rationale for the 'close connection' requirement: An ambassador or consular "
        "official posted abroad should still be taxed at home. But if a local national "
        "happens to be employed by a foreign government in their own country, it is "
        "more natural for the local (work) state to tax."
    ))

    story.append(h3("Article 19(2): Government Pensions"))
    story += [
        b("Same logic as Art. 19(1): taxed in the paying state, subject to the "
          "same 'close connection' exception."),
        sp(4)
    ]

    story.append(h3("State-Owned Enterprises: Important Exception"))
    story += [
        b("If the government carries on a <i>commercial business</i> (e.g., a "
          "state-owned airline, railway, or telecom company), employees are "
          "treated as private-sector employees → Art. 15, 16, 17, or 18 apply, "
          "<i>not</i> Art. 19."),
        sp(6)
    ]
    story.append(ex("Art. 19 exam trap: does the 'close connection' exception apply? "
                    "Check (1) where work is performed, (2) where employee resides, "
                    "(3) nationality or prior residence."))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────────────
    # 10.6  INVESTMENT INCOME
    # ─────────────────────────────────────────────────────────────────────
    story += [h1("10.6  Investment Income — Articles 10, 11 & 12"), sp(6)]

    story.append(h2("Active vs. Passive Income: The Fundamental Distinction"))
    active_passive = [
        ["Feature", "Business Profits (Active)", "Investment Income (Passive)"],
        ["Articles", "Arts. 7, 8", "Arts. 10, 11, 12"],
        ["Primary taxing right", "Source state (if PE exists)", "Residence state of recipient"],
        ["Source-state right", "Full taxation (if PE)", "Limited withholding tax only"],
        ["PE requirement", "Yes — no PE, no source-state tax", "No PE needed for source state to WHT"],
    ]
    story.append(numeric_table(["Feature","Business Profits (Active)","Investment Income (Passive)"],
        active_passive[1:],
        [4*cm, 5.5*cm, PAGE_W - 2*MARGIN - 9.5*cm], S))
    story.append(sp(8))

    # Dividends ──────────────────────────────────────────────────────────
    story.append(h2("Article 10: Dividends"))
    story.append(p(
        "Dividends are distributions from a company resident in one state to a "
        "shareholder resident in another. The OECD Model grants <b>shared taxing "
        "rights</b>: both the residence state of the shareholder AND the source "
        "state of the distributing company may tax, but the source state is capped."
    ))

    story.append(h3("Withholding Tax Rates Under the OECD Model"))
    div_rates = [
        ["Situation", "Source State WHT Rate", "Condition"],
        ["Substantial shareholding\n(parent-subsidiary)", "Maximum 5%",
         "Direct holding ≥ 25% of capital of the distributing company; "
         "held continuously for 365 days including the day of payment "
         "(anti-'dividend-stripping' rule)"],
        ["All other cases\n(portfolio / individuals)", "Maximum 15%", "No special condition required"],
    ]
    story.append(numeric_table(["Situation","Source State WHT Rate","Condition"],
        div_rates[1:],
        [4.5*cm, 3*cm, PAGE_W - 2*MARGIN - 7.5*cm], S))
    story.append(sp(4))
    story.append(p(
        "The withholding tax is withheld by the <i>distributing company</i> at the "
        "time of payment and remitted to the source state's treasury. The "
        "shareholder receives the dividend net of WHT and then claims relief "
        "(exemption or credit) in the residence state under Art. 23."
    ))

    story.append(h3("The Beneficial Ownership (BO) Requirement"))
    story.append(p(
        "The reduced WHT rates in Art. 10(2) are only available if the recipient "
        "is the <b>beneficial owner</b> of the dividend. This anti-avoidance rule "
        "targets <b>treaty shopping</b> — routing payments through a conduit "
        "company in a favourable-treaty country."
    ))
    story += [
        b("'Beneficial owner' has an <b>economic (not merely legal) meaning</b>: "
          "the recipient must have the right to freely use and enjoy the income "
          "without being bound to pass it on to another party."),
        b("A conduit company that is legally obliged to transmit dividends to a "
          "parent in a non-treaty state is <i>not</i> the beneficial owner."),
        sp(4)
    ]
    story.append(info_box([
        Paragraph(
            "<b>Treaty Shopping Example (from slides):</b> AustriaCo pays dividends "
            "to BermudaCo. Austria–Bermuda: no treaty, 25% WHT. Austria–Luxembourg: "
            "treaty, 0% WHT. Luxembourg domestic law: no outgoing WHT. "
            "The group inserts LuxCo (legally obliged to pass dividends to BermudaCo) "
            "to reduce WHT to 0%. → LuxCo is NOT the beneficial owner → reduced "
            "treaty rate does NOT apply.",
            ParagraphStyle("ib", fontName="Helvetica", fontSize=10,
                textColor=DARK_BLUE, leading=14))
    ], S, bg=colors.HexColor("#FFF3E0"), border=ORANGE_TIP))
    story.append(sp(6))
    story.append(p(
        "<b>Important:</b> the same beneficial ownership requirement applies to "
        "interest (Art. 11) and royalties (Art. 12)."
    ))

    # Interest ──────────────────────────────────────────────────────────
    story.append(h2("Article 11: Interest"))
    story += [
        b("Interest arises in a state where the borrower (the payor) is resident. "
          "The creditor/lender is resident in the other state."),
        b("<b>Shared taxing rights</b>: the residence state of the lender may tax "
          "(usually fully); the source state may also tax, but capped at "
          "<b>10% WHT</b> on the gross amount."),
        b("The BO requirement also applies."),
        b("'Interest' generally means income from debt claims — bonds, loans, "
          "debentures, deposits. Penalty payments for late payment are generally "
          "not 'interest'."),
        sp(6)
    ]

    # Royalties ──────────────────────────────────────────────────────────
    story.append(h2("Article 12: Royalties"))
    story.append(p(
        "Royalties are payments for the use of, or the right to use, intellectual "
        "property. The OECD Model grants <b>exclusive taxing rights to the residence "
        "state of the beneficial owner</b>."
    ))
    story += [
        b("<b>What qualifies as a royalty?</b> Payments for: copyrights (literary, "
          "artistic, scientific works), patents, trademarks, designs/models, secret "
          "formulas, and know-how (industrial, commercial, or scientific experience)."),
        b("<b>No source-state WHT under the OECD Model</b> — all taxing rights go "
          "to the residence state of the recipient."),
        b("<b>Important exception — UN Model</b>: Many bilateral treaties with "
          "developing countries follow the UN Model, which allows the source state "
          "to levy a limited WHT on royalties (typically 10–15%). So in practice, "
          "purely residence-state taxation of royalties is not universal."),
        b("The BO requirement applies here too."),
        sp(6)
    ]

    # Comparison table ─────────────────────────────────────────────────
    story.append(h2("Summary: Investment Income at a Glance"))
    inv_summary = [
        ["Income Type", "Article", "Source State WHT", "Residence State", "BO Required?"],
        ["Dividends\n(substantial)", "10", "Max 5%", "May also tax", "Yes"],
        ["Dividends\n(portfolio)", "10", "Max 15%", "May also tax", "Yes"],
        ["Interest", "11", "Max 10%", "May also tax", "Yes"],
        ["Royalties\n(OECD Model)", "12", "None (0%)", "Exclusive right", "Yes"],
    ]
    story.append(numeric_table(
        ["Income Type","Article","Source State WHT","Residence State","BO Required?"],
        inv_summary[1:],
        [3.5*cm, 1.5*cm, 3.5*cm, 3.5*cm, 2.5*cm], S))
    story.append(sp(6))
    story.append(ex("Investment income: remember the WHT caps (5/15/10/0). The BO "
                    "requirement applies to ALL three types. Royalties under the OECD "
                    "Model: 0% source WHT (but UN Model treaties differ)."))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────────────
    # 10.7  STUDENTS
    # ─────────────────────────────────────────────────────────────────────
    story += [h1("10.7  Students — Article 20"), sp(6)]
    story.append(p(
        "Article 20 protects students and business apprentices studying abroad "
        "from being taxed in the country of study on payments received for their "
        "maintenance, education, or training."
    ))
    story.append(h2("Conditions"))
    story += [
        b("(1) The person is a <b>student or business apprentice</b> who is "
          "physically present in Contracting State A <i>solely for the purpose "
          "of education or training</i>."),
        b("(2) The person is (or was immediately before visiting State A) a "
          "<b>resident of Contracting State B</b>."),
        b("(3) The person receives a <b>payment from a source outside State A</b>, "
          "made for the purpose of maintenance, education, or training."),
        sp(4)
    ]
    story.append(p(
        "<b>Consequence</b>: State A (the study state) is <i>not</i> entitled to "
        "tax those payments. The student's home state (State B) retains the right."
    ))
    story.append(h2("What Is NOT Covered?"))
    story += [
        b("Income earned from services performed in State A (e.g., a part-time job) "
          "is <i>not</i> exempt under Art. 20. It is covered by Art. 15 (if employee) "
          "or Art. 7 (if self-employed)."),
        b("Investment income, prizes, or grants from within State A also fall "
          "outside Art. 20 and are governed by the applicable distributive article."),
        sp(6)
    ]
    story.append(ex("Art. 20 only covers: (a) students, (b) studying abroad, "
                    "(c) payments from outside the study state, (d) for maintenance/"
                    "education/training. Employment income from working in the "
                    "study state is fully taxable under Art. 15."))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────────────
    # 10.8  OTHER INCOME
    # ─────────────────────────────────────────────────────────────────────
    story += [h1("10.8  Other Income — Article 21"), sp(6)]
    story.append(p(
        "Article 21 is the <b>residual catch-all provision</b>. It applies to any "
        "item of income that is <i>not</i> covered by Articles 6–20."
    ))
    story += [
        b("<b>Taxing right</b>: exclusively in the <b>recipient's state of "
          "residence</b>. The source state has no right to tax."),
        b("<b>Examples</b>: maintenance (alimony) payments; gambling and lottery "
          "winnings; pensions of self-employed persons (no link to employment); "
          "certain scholarships not covered by Art. 20."),
        b("Art. 21 should be seen as a safety net — if income fits into any of "
          "Arts. 6–20, Art. 21 does not apply."),
        sp(6)
    ]

    # ─────────────────────────────────────────────────────────────────────
    # 10.9  ELIMINATION OF DOUBLE TAXATION
    # ─────────────────────────────────────────────────────────────────────
    story += [h1("10.9  Elimination of Double Taxation — Articles 23A & 23B"), sp(6)]

    story.append(h2("When Is Article 23 Needed?"))
    story.append(p(
        "Many distributive articles allocate taxing rights to one state only "
        "('shall be taxable <i>only</i> in'). Where only one state can tax, there "
        "is no double taxation and Article 23 is not needed."
    ))
    story.append(p(
        "However, some distributive articles allow both states to tax simultaneously "
        "('may be taxed in'). Examples: Art. 6 (immovable property), Art. 10 "
        "(dividends), Art. 11 (interest). In these cases, Article 23 requires the "
        "<b>residence state</b> to grant relief."
    ))
    story += [
        b("<b>Art. 23 imposes obligations only on the residence state</b>, not the "
          "source state. The source state's right to tax is left intact."),
        b("Two alternative relief mechanisms exist in the OECD Model:"),
        b2("<b>Exemption method</b> — Article 23A"),
        b2("<b>Credit method</b> — Article 23B"),
        sp(6)
    ]

    # Exemption ─────────────────────────────────────────────────────────
    story.append(h2("A. The Exemption Method — Article 23A"))
    story.append(info_box([
        cod("Where a resident of a Contracting State derives income which, in "
            "accordance with the provisions of this Convention, may be taxed in the "
            "[source] State, the [resident] State shall, subject to the provisions of "
            "paragraphs 2 and 3, exempt such income from tax.")], S))
    story.append(sp(4))
    story.append(p(
        "The residence state simply <b>excludes the foreign income from its tax "
        "base</b>. The income is taxed only once — in the source state."
    ))

    story.append(h3("Economic Philosophy: Capital Import Neutrality (CIN)"))
    story.append(p(
        "The exemption method promotes <b>Capital Import Neutrality (CIN)</b>: all "
        "investments in a given country are subject to the same local tax rate, "
        "regardless of the investor's home country. A Belgian investor and a German "
        "investor earning rental income from French property both pay French tax at "
        "the same rate — their residence-country tax systems do not distort the "
        "competitive balance in France."
    ))

    story.append(h3("Two Variants of the Exemption Method"))
    story += [
        b("<b>Full exemption</b>: the foreign income is completely disregarded in "
          "the residence state. The residence state taxes only the domestic income, "
          "at the domestic income rate."),
        b("<b>Exemption with progression</b>: the foreign income is excluded from "
          "the tax base, BUT the residence state may still use it to determine the "
          "<i>applicable tax rate</i> (progression clause). The higher combined "
          "income pushes the taxpayer into a higher bracket, and that higher rate "
          "then applies to the domestic income only."),
        sp(6)
    ]

    story.append(h3("Worked Example — All Three Exemption Variants"))
    story.append(p(
        "Facts: Individual resident in State R. Total income = 100,000. "
        "80,000 sourced in State R; 20,000 sourced in State S (taxed at "
        "20% in Scenario 1, 40% in Scenario 2). "
        "State R progressive rates: 30% avg on 80,000; 35% avg on 100,000."
    ))

    story.append(h3("Step 0: Without Any Relief (Double Taxation)"))
    story.append(numeric_table(
        ["", "Scenario 1\n(S rate 20%)", "Scenario 2\n(S rate 40%)"],
        [["Tax in State R (35% × 100,000)", "35,000", "35,000"],
         ["Tax in State S", "4,000", "8,000"],
         ["TOTAL TAX (double taxation)", "39,000", "43,000"]],
        [8*cm, 4.5*cm, 4.5*cm], S))
    story.append(sp(6))

    story.append(h3("Step 1: Full Exemption (State R exempts the 20,000)"))
    story.append(p(
        "State R taxes only on 80,000 (its domestic income). "
        "Rate applied: 30% (average rate applicable to 80,000)."
    ))
    story.append(numeric_table(
        ["", "Scenario 1", "Scenario 2"],
        [["Tax in State R (30% × 80,000)", "24,000", "24,000"],
         ["Tax in State S", "4,000", "8,000"],
         ["TOTAL TAX", "28,000", "32,000"],
         ["Relief granted in State R vs. no-relief", "11,000", "11,000"]],
        [8*cm, 4.5*cm, 4.5*cm], S))
    story.append(sp(4))
    story.append(p(
        "<b>Why is the relief 11,000 and not just 7,000?</b> Because the exemption "
        "has two effects: (1) it removes 20,000 from the base, saving 35% × 20,000 = <b>7,000</b>; "
        "and (2) the lower base (80k instead of 100k) triggers a lower average rate "
        "(30% instead of 35%), saving an additional 5% × 80,000 = <b>4,000</b>. "
        "Total relief = 7,000 + 4,000 = <b>11,000</b>. "
        "This is independent of the State S tax rate, which is why both scenarios give the same relief."
    ))
    story.append(sp(6))

    story.append(h3("Step 2: Exemption with Progression"))
    story.append(p(
        "State R exempts the 20,000 from its tax base but uses the full 100,000 "
        "to determine the applicable rate. Rate applied: 35% (rate for 100,000), "
        "applied only to the domestic 80,000."
    ))
    story.append(numeric_table(
        ["", "Scenario 1", "Scenario 2"],
        [["Tax in State R (35% × 80,000)", "28,000", "28,000"],
         ["Tax in State S", "4,000", "8,000"],
         ["TOTAL TAX", "32,000", "36,000"],
         ["Relief granted in State R vs. no-relief", "7,000", "7,000"]],
        [8*cm, 4.5*cm, 4.5*cm], S))
    story.append(sp(4))
    story.append(p(
        "Under exemption with progression, the relief (7,000) is lower because "
        "the higher rate (35%) is still applied to the domestic income — the "
        "progression clause ensures the taxpayer does not benefit from an "
        "artificially lower bracket."
    ))
    story.append(sp(6))

    # Credit ─────────────────────────────────────────────────────────────
    story.append(h2("B. The Credit Method — Article 23B"))
    story.append(info_box([
        cod("Where a resident of a Contracting State derives income […] which may "
            "be taxed in the [source state], the [home state] shall allow as a "
            "deduction from the tax on the income of that resident an amount equal "
            "to the income tax paid in [the source state]. Such deduction shall not "
            "exceed that part of the income tax, as computed before the deduction "
            "is given, which is attributable to the income which may be taxed in "
            "the [source state].")], S))
    story.append(sp(4))
    story.append(p(
        "The residence state taxes the taxpayer's <b>worldwide income</b> (including "
        "the foreign income) but then allows a <b>tax credit</b> for taxes paid "
        "in the source state."
    ))

    story.append(h3("Economic Philosophy: Capital Export Neutrality (CEN)"))
    story.append(p(
        "The credit method promotes <b>Capital Export Neutrality (CEN)</b>: a "
        "taxpayer pays the same total tax regardless of whether they invest at "
        "home or abroad. The combined tax burden always equals the higher of "
        "the two rates — effectively the residence-state rate (assuming it is "
        "higher than the source-state rate). This prevents capital from flowing "
        "to low-tax countries purely for tax reasons."
    ))

    story.append(h3("Two Variants of the Credit Method"))
    story += [
        b("<b>Full credit</b>: the residence state deducts the <i>entire</i> amount "
          "of foreign tax paid. If the foreign tax exceeds the residence-state tax "
          "on that income, the excess is refunded. (Used rarely in practice.)"),
        b("<b>Ordinary (limited) credit</b>: the deduction is capped at the "
          "residence-state tax attributable to the foreign income "
          "(= residence rate × foreign income). If foreign tax > this cap, the "
          "excess is not refunded — this is called an 'excess foreign tax credit'. "
          "This is the OECD Model approach and the most common in practice."),
        sp(6)
    ]

    story.append(h3("Worked Example — Credit Method"))
    story.append(p(
        "Same facts as before: total income 100,000 (80k domestic, 20k foreign). "
        "State R: 35% average rate on 100,000. State S: 20% (Scenario 1) or 40% "
        "(Scenario 2). Ordinary credit cap = 35% × 20,000 = 7,000."
    ))

    story.append(h3("Full Credit"))
    story.append(numeric_table(
        ["", "Scenario 1", "Scenario 2"],
        [["Hypothetical tax in State R (35% × 100,000)", "35,000", "35,000"],
         ["Less: tax paid in State S (full credit)", "(4,000)", "(8,000)"],
         ["Actual tax due in State R", "31,000", "27,000"],
         ["TOTAL TAX (State R + State S)", "35,000", "35,000"]],
        [8*cm, 4.5*cm, 4.5*cm], S))
    story.append(sp(4))
    story.append(p(
        "Under full credit, the total tax is ALWAYS equal to the residence-state "
        "tax (35,000), regardless of the foreign rate — perfect CEN."
    ))
    story.append(sp(6))

    story.append(h3("Ordinary (Limited) Credit"))
    story.append(p("Credit is capped at 35% × 20,000 = <b>7,000</b>."))
    story.append(numeric_table(
        ["", "Scenario 1\n(S rate 20%)", "Scenario 2\n(S rate 40%)"],
        [["Hypothetical tax in State R (35% × 100,000)", "35,000", "35,000"],
         ["Less: foreign tax (capped at 7,000)", "(4,000)", "(7,000)"],
         ["Actual tax due in State R", "31,000", "28,000"],
         ["TOTAL TAX (State R + State S)", "35,000", "36,000"],
         ["Relief granted in State R", "4,000", "7,000"]],
        [8*cm, 4.5*cm, 4.5*cm], S))
    story.append(sp(4))
    story.append(p(
        "Scenario 2: the foreign rate (40%) exceeds the cap (7,000), so the "
        "taxpayer bears 8,000 in State S but only gets 7,000 credit in State R. "
        "The 1,000 excess foreign tax is unrelieved — this is the classic "
        "'excess foreign tax credit' problem under the ordinary credit method."
    ))
    story.append(sp(6))

    # Comparison ─────────────────────────────────────────────────────────
    story.append(h2("Summary Comparison: All Four Methods"))
    story.append(p(
        "Sc.1 = State S rate 20% (foreign tax = 4,000). "
        "Sc.2 = State S rate 40% (foreign tax = 8,000). "
        "State R tax on worldwide income without relief = 35% × 100,000 = 35,000."
    ))
    story.append(numeric_table(
        ["Method", "State R tax (Sc.1)", "State R tax (Sc.2)", "State S tax (Sc.1)", "State S tax (Sc.2)", "Total (Sc.1)", "Total (Sc.2)", "Philosophy"],
        [["No relief",         "35,000", "35,000", "4,000", "8,000", "39,000", "43,000", "—"],
         ["Full exemption",    "24,000", "24,000", "4,000", "8,000", "28,000", "32,000", "CIN"],
         ["Exemp. w/ prog.",   "28,000", "28,000", "4,000", "8,000", "32,000", "36,000", "CIN"],
         ["Full credit",       "31,000", "27,000", "4,000", "8,000", "35,000", "35,000", "CEN (pure)"],
         ["Ordinary credit",   "31,000", "28,000", "4,000", "8,000", "35,000", "36,000 ⚠", "CEN"]],
        [3.2*cm, 2.2*cm, 2.2*cm, 2*cm, 2*cm, 1.8*cm, 1.8*cm, PAGE_W-2*MARGIN-15.2*cm], S))
    story.append(sp(4))
    story.append(p(
        "⚠ Ordinary credit Sc.2: foreign tax paid = 8,000 but credit is capped at "
        "35% × 20,000 = 7,000. State R credits only 7,000, leaving 1,000 of "
        "foreign tax unrelieved ('excess foreign tax credit'). Total = 28,000 + 8,000 = 36,000."
    ))
    story.append(sp(6))
    story.append(ex("Know the mechanics of all four methods and be able to compute "
                    "the tax outcomes. CIN (exemption) vs. CEN (credit) is a "
                    "frequently tested conceptual distinction."))

    # ─────────────────────────────────────────────────────────────────────
    # FINAL OVERVIEW TABLE
    # ─────────────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story += [h1("Quick Reference: All Distributive Articles"), sp(6)]
    story.append(p(
        "The following table summarises the key allocation rules across all "
        "distributive provisions. Use this as a rapid diagnostic tool in "
        "exam scenarios."
    ))
    overview = [
        ["Article", "Income Type", "Primary Taxing Right", "Notes"],
        ["6",  "Immovable property income", "Source state (may be taxed)", "Art. 13(1) mirrors for gains"],
        ["7",  "Business profits", "Home state ONLY unless PE", "Source state taxes only PE profits"],
        ["8",  "Intl. shipping/air", "Home state ONLY", "Overrides Art. 7"],
        ["10", "Dividends", "Residence state + source (5%/15% WHT)", "BO required"],
        ["11", "Interest", "Residence state + source (10% WHT)", "BO required"],
        ["12", "Royalties", "Residence state ONLY (OECD)", "UN Model allows source WHT"],
        ["13(1)","Immov. property gains","Source state","Mirrors Art. 6"],
        ["13(2)","PE asset gains","PE state","Incl. sale of PE itself"],
        ["13(3)","Shipping/aircraft gains","Home state","Mirrors Art. 8"],
        ["15",  "Employment income", "Residence state; work state if work done there", "Art. 15(2): 183-day exception"],
        ["16",  "Directors' fees", "State of paying company", "Simplification rule"],
        ["17",  "Entertainers/sports", "Performance state", "Overrides Arts. 7 & 15"],
        ["18",  "Private pensions", "Residence state ONLY", "Linked to past employment"],
        ["19",  "Govt. salaries/pensions", "Paying state (with exception)", "Close connection → work state"],
        ["20",  "Student payments", "Not taxed in study state", "Must be from outside study state"],
        ["21",  "Other income", "Residence state ONLY", "Catch-all residual provision"],
    ]
    story.append(numeric_table(
        ["Article","Income Type","Primary Taxing Right","Notes"],
        overview[1:],
        [1.5*cm, 3.5*cm, 5.5*cm, PAGE_W-2*MARGIN-10.5*cm], S))

    story.append(sp(10))
    story.append(hr())
    story.append(Paragraph(
        "End of Chapter 10 Expanded Study Guide — Good luck on your exam!",
        ParagraphStyle("end", fontName="Helvetica-Oblique", fontSize=10,
            textColor=TEAL, alignment=TA_CENTER, spaceBefore=6)
    ))
    return story


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════
def main():
    output_path = "/home/user/BabyPluto/Chapter10_Tax_Treaty_Provisions_Expanded.pdf"
    styles = build_styles()
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
        title="Chapter 10: Tax Treaty Provisions — Expanded Study Guide",
        author="KU Leuven — Principles of Taxation"
    )

    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(TEAL)
        canvas.drawString(MARGIN, 1.0*cm,
            "Chapter 10: Tax Treaty Provisions — Expanded Study Guide")
        canvas.drawRightString(A4[0] - MARGIN, 1.0*cm, f"Page {doc.page}")
        canvas.restoreState()

    story = build_story(styles)
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    main()
