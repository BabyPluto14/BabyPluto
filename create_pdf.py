from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

PAGE_W, PAGE_H = A4
MARGIN = 2.5 * cm

doc = SimpleDocTemplate(
    "/home/user/BabyPluto/Module11_Socially_Responsible_Marketing.pdf",
    pagesize=A4,
    rightMargin=MARGIN,
    leftMargin=MARGIN,
    topMargin=MARGIN,
    bottomMargin=MARGIN,
)

styles = getSampleStyleSheet()

BRAND_BLUE = colors.HexColor("#1a3c6e")
BRAND_ACCENT = colors.HexColor("#2e86ab")
BRAND_LIGHT = colors.HexColor("#f0f6fb")
DIVIDER_COLOR = colors.HexColor("#c8ddf0")

style_main_title = ParagraphStyle(
    "MainTitle",
    parent=styles["Title"],
    fontSize=28,
    leading=36,
    textColor=BRAND_BLUE,
    spaceAfter=8,
    alignment=TA_CENTER,
    fontName="Helvetica-Bold",
)
style_subtitle = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    fontSize=14,
    leading=20,
    textColor=BRAND_ACCENT,
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName="Helvetica",
)
style_meta = ParagraphStyle(
    "Meta",
    parent=styles["Normal"],
    fontSize=11,
    leading=16,
    textColor=colors.HexColor("#555555"),
    spaceAfter=4,
    alignment=TA_CENTER,
    fontName="Helvetica-Oblique",
)
style_section = ParagraphStyle(
    "Section",
    parent=styles["Heading1"],
    fontSize=16,
    leading=22,
    textColor=BRAND_BLUE,
    spaceBefore=18,
    spaceAfter=6,
    fontName="Helvetica-Bold",
    borderPad=4,
)
style_subsection = ParagraphStyle(
    "Subsection",
    parent=styles["Heading2"],
    fontSize=13,
    leading=18,
    textColor=BRAND_ACCENT,
    spaceBefore=12,
    spaceAfter=4,
    fontName="Helvetica-Bold",
)
style_body = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontSize=11,
    leading=17,
    textColor=colors.HexColor("#222222"),
    spaceAfter=10,
    alignment=TA_JUSTIFY,
    fontName="Helvetica",
)
style_callout = ParagraphStyle(
    "Callout",
    parent=styles["Normal"],
    fontSize=11,
    leading=17,
    textColor=BRAND_BLUE,
    spaceAfter=10,
    spaceBefore=6,
    alignment=TA_JUSTIFY,
    fontName="Helvetica-Oblique",
    leftIndent=18,
    rightIndent=18,
    borderPad=8,
    borderColor=BRAND_ACCENT,
    borderWidth=0,
    backColor=BRAND_LIGHT,
)
style_bullet = ParagraphStyle(
    "Bullet",
    parent=styles["Normal"],
    fontSize=11,
    leading=17,
    textColor=colors.HexColor("#222222"),
    spaceAfter=4,
    leftIndent=20,
    bulletIndent=8,
    fontName="Helvetica",
)
style_key_takeaway = ParagraphStyle(
    "KeyTakeaway",
    parent=styles["Normal"],
    fontSize=11,
    leading=17,
    textColor=BRAND_BLUE,
    spaceAfter=6,
    alignment=TA_JUSTIFY,
    fontName="Helvetica",
    leftIndent=14,
    rightIndent=14,
    backColor=BRAND_LIGHT,
    borderPad=10,
)

def divider():
    return HRFlowable(width="100%", thickness=1, color=DIVIDER_COLOR, spaceAfter=10, spaceBefore=10)

def section_header(text):
    return KeepTogether([
        Spacer(1, 0.3 * cm),
        Paragraph(text, style_section),
        HRFlowable(width="100%", thickness=2, color=BRAND_ACCENT, spaceAfter=6, spaceBefore=2),
    ])

def subsection_header(text):
    return Paragraph(text, style_subsection)

def body(text):
    return Paragraph(text, style_body)

def callout(text):
    return Paragraph(text, style_callout)

def bullet_item(text):
    return Paragraph(f"•&nbsp;&nbsp;{text}", style_bullet)


story = []

# ── Cover page ──────────────────────────────────────────────────────────────
story.append(Spacer(1, 3 * cm))
story.append(Paragraph("Module 11", style_subtitle))
story.append(Paragraph("Socially Responsible Marketing", style_main_title))
story.append(Spacer(1, 0.4 * cm))
story.append(HRFlowable(width="60%", thickness=3, color=BRAND_ACCENT,
                         spaceAfter=10, spaceBefore=10, hAlign="CENTER"))
story.append(Paragraph("Transcript Knowledge Clips — Detailed Explanations", style_subtitle))
story.append(Spacer(1, 0.6 * cm))
story.append(Paragraph("Based on lectures by Prof. Tine De Bock, KU Leuven", style_meta))
story.append(PageBreak())

# ── 1. Introduction ──────────────────────────────────────────────────────────
story.append(section_header("1. Introduction"))
story.append(body(
    "This document provides a detailed explanation of the key concepts covered in the Module 11 "
    "video clips on Socially Responsible Marketing, as presented by Professor Tine De Bock of "
    "KU Leuven. The module is built around two foundational concepts — <b>marketing</b> and "
    "<b>social responsibility</b> — and how they combine to form a holistic, forward-looking "
    "approach to business practice."
))
story.append(body(
    "As Prof. De Bock explains in the opening clip: <i>\"There are two concepts that immediately "
    "come to the forefront when we talk about socially responsible marketing. First of all, "
    "there's social responsibility. Secondly, there's 'marketing'. It's kind of hard to introduce "
    "you to socially responsible marketing without talking about these two concepts.\"</i>"
))

# ── 2. What Is Marketing? ────────────────────────────────────────────────────
story.append(section_header("2. What Is Marketing?"))

story.append(subsection_header("2.1 Definition"))
story.append(body(
    "Marketing has countless definitions, but the module anchors itself to the widely-cited "
    "formulation by <b>Philip Kotler</b>, often called the 'father of modern marketing':"
))
story.append(callout(
    "“Marketing is the process by which companies create value for customers and build "
    "strong customer relationships, in order to capture value from customers in return.”"
    " — Philip Kotler"
))
story.append(body(
    "Across many definitions, the common thread is that marketing is about <b>creating value</b> "
    "by identifying, anticipating and satisfying customers' needs and wants — whether those "
    "customers are businesses, individual consumers, or other stakeholders. When an organisation "
    "creates superior value, it receives value in return (financial results, positive word-of-mouth, "
    "brand equity, etc.). Successful marketing is therefore fundamentally about being "
    "<b>customer-centric</b>."
))

story.append(subsection_header("2.2 The Marketing Process"))
story.append(body(
    "Kotler's definition frames marketing as a <b>process</b>. This process provides a structured "
    "sequence of steps organisations follow to create and deliver value:"
))
story.append(bullet_item("<b>Mission & Environment Analysis:</b> Organisations first define their mission "
    "statement, then analyse the market environment and conduct research on client needs and "
    "wants. They assess their own strengths and weaknesses (internal analysis) and identify "
    "external opportunities and threats — a classic SWOT analysis."))
story.append(Spacer(1, 0.1 * cm))
story.append(bullet_item("<b>Marketing Strategy:</b> The insights from the analysis feed into strategy. "
    "This involves segmenting the market, choosing a target audience, determining how to "
    "<b>position</b> the brand or organisation, and setting marketing goals along with an "
    "appropriate budget."))
story.append(Spacer(1, 0.1 * cm))
story.append(bullet_item("<b>Marketing Mix (4 Ps):</b> Strategic choices are translated into tactical "
    "decisions across four dimensions — <b>Product</b> (branding, features), <b>Price</b> "
    "(pricing strategy), <b>Place</b> (production, distribution channels) and <b>Promotion</b> "
    "(advertising, PR, digital marketing). Many people equate marketing with advertising, but "
    "the 4 Ps show that promotion is only one component."))
story.append(Spacer(1, 0.1 * cm))
story.append(bullet_item("<b>Customer Value & Relationships:</b> All steps aim at satisfying customer needs, "
    "delighting customers, and building profitable long-term relationships — ultimately capturing "
    "value from customers in return."))

story.append(Spacer(1, 0.3 * cm))
story.append(body(
    "Note: Different textbooks and online resources may use slightly different labels or pictures "
    "for the marketing process, but the underlying logic is always the same."
))

story.append(subsection_header("2.3 The Old vs. the New Marketing World"))
story.append(body(
    "The marketing process described above was established in an era that now looks very different "
    "from today's environment. Understanding this shift is essential for appreciating why "
    "socially responsible marketing has become so important."
))
story.append(body("<b>The Old Marketing World:</b>"))
story.append(bullet_item("Marketers were often obsessed with their own products and focused heavily on "
    "sales and short-term financial results."))
story.append(bullet_item("Marketing was mainly one-directional: push messages at customers and hope they "
    "buy. Empty promises were tolerated."))
story.append(bullet_item("The relationship was narrowly defined as company–customer; the broader societal "
    "context was largely ignored."))
story.append(bullet_item("Social responsibility was barely on the agenda."))

story.append(Spacer(1, 0.2 * cm))
story.append(body("<b>The New Marketing World:</b>"))
story.append(bullet_item("<b>Technology</b> has empowered consumers with unprecedented access to information, "
    "dramatically raising the bar for honest, relevant marketing."))
story.append(bullet_item("<b>Globalisation</b> means local companies now compete in a global marketplace, "
    "intensifying competition."))
story.append(bullet_item("Marketing must be deeply <b>customer-oriented</b>, focused on experience and "
    "long-term value rather than one-off transactions."))
story.append(bullet_item("Value is increasingly <b>co-created</b> with customers and wider networks; "
    "one-way broadcasting no longer works."))
story.append(bullet_item("Customers have more power and increasingly <b>expect companies to care about "
    "social responsibility</b>."))

story.append(Spacer(1, 0.3 * cm))
story.append(body(
    "Prof. De Bock's key message here: even if you hold on to the classical marketing process as "
    "a framework, you must shape it to fit the new marketing world. The fundamentals are a starting "
    "point, not a fixed blueprint."
))

# ── 3. Social Responsibility ─────────────────────────────────────────────────
story.append(section_header("3. Social Responsibility"))

story.append(subsection_header("3.1 The Bigger Picture — Doughnut Economics"))
story.append(body(
    "To frame social responsibility, the module draws on the work of economist <b>Kate Raworth</b> "
    "and her concept of <b>Doughnut Economics</b>. Raworth's framework describes humanity's "
    "21st-century challenge as a double-sided problem:"
))
story.append(callout(
    "“To meet the needs of all people within the means of this extraordinary, unique, living "
    "planet so that we and the rest of nature can thrive.” — Kate Raworth"
))
story.append(body(
    "The 'doughnut' metaphor illustrates a safe and just space for humanity: a <b>social foundation</b> "
    "(the inner ring — ensuring all people have what they need) and an <b>ecological ceiling</b> "
    "(the outer ring — staying within planetary boundaries). The goal is to live and do business "
    "in the space between these two rings."
))

story.append(subsection_header("3.2 Sustainable Development"))
story.append(body(
    "The doughnut resonates with the concept of <b>sustainable development</b>. In 1983, the UN "
    "General Assembly recognised that the human environment and natural resources were deteriorating. "
    "This led to the formation of the <b>Brundtland Commission</b>, which released its landmark "
    "report <i>Our Common Future</i> in 1987. The report offered the most widely cited definition "
    "of sustainable development:"
))
story.append(callout(
    "“Development that meets the needs of the present without compromising the ability of "
    "future generations to meet their own needs.” — The Brundtland Report (1987)"
))
story.append(body(
    "This definition has two core ideas: (1) meeting <i>current</i> human needs, and (2) not "
    "depleting resources or damaging the environment in ways that prevent <i>future</i> generations "
    "from meeting their own needs."
))

story.append(subsection_header("3.3 Sustainable Development Goals (SDGs)"))
story.append(body(
    "The United Nations operationalised sustainable development through the <b>Sustainable Development "
    "Goals (SDGs)</b> — a collection of <b>17 interlinked goals</b> that form a blueprint for a "
    "better and more sustainable future for all. The SDGs were adopted in 2015 and are intended "
    "to be achieved by <b>2030</b>. Examples include:"
))
story.append(bullet_item("SDG 2: Zero Hunger"))
story.append(bullet_item("SDG 5: Gender Equality"))
story.append(bullet_item("SDG 12: Responsible Consumption and Production"))
story.append(bullet_item("SDG 13: Climate Action"))
story.append(Spacer(1, 0.2 * cm))
story.append(body(
    "The SDGs are highly relevant to businesses because they provide a concrete, internationally "
    "agreed framework against which organisations can measure and communicate their social and "
    "environmental contributions."
))

story.append(subsection_header("3.4 Corporate Social Responsibility (CSR) and the 3 Ps"))
story.append(body(
    "When sustainability thinking is brought into the corporate context it is typically called "
    "<b>Corporate Social Responsibility (CSR)</b>. CSR is about keeping a healthy balance between "
    "the <b>Triple Bottom Line — People, Planet and Profit</b> (the 3 Ps):"
))
story.append(bullet_item("<b>People:</b> Social impact — fair labour, community wellbeing, inclusion."))
story.append(bullet_item("<b>Planet:</b> Environmental stewardship — carbon footprint, biodiversity, "
    "resource use."))
story.append(bullet_item("<b>Profit:</b> Financial viability — without which organisations cannot sustain "
    "their social and environmental commitments."))

# ── 4. Socially Responsible Marketing ────────────────────────────────────────
story.append(section_header("4. Socially Responsible Marketing"))

story.append(subsection_header("4.1 Definition"))
story.append(body(
    "Bringing marketing and social responsibility together yields <b>socially responsible "
    "marketing</b> (also called sustainable marketing or sustainability marketing). The module "
    "deliberately uses the term 'socially responsible' rather than 'sustainable' to avoid narrowing "
    "the concept to only environmental issues:"
))
story.append(callout(
    "Socially responsible marketing is the practice of an organisation meeting the needs of its "
    "current customers in a <b>socially and environmentally responsible manner</b>, without "
    "burdening future generations so that they can no longer meet their own needs."
))
story.append(body(
    "This definition explicitly echoes the Brundtland definition of sustainable development. Where "
    "traditional marketing focused on a dyadic relationship (consumers ↔ organisation), socially "
    "responsible marketing adds a third dimension: <b>societal and environmental well-being</b>."
))

story.append(subsection_header("4.2 Two Directions of the Marketing–Sustainability Relationship"))
story.append(body(
    "Prof. De Bock highlights that the relationship between marketing and sustainability can run "
    "in two directions, each resulting in a distinct type of socially responsible marketing practice:"
))

story.append(Spacer(1, 0.15 * cm))
story.append(body("<b>Direction 1 — Marketing First, Sustainability Added On:</b>"))
story.append(body(
    "The organisation starts with its existing marketing approach and investigates how to make it "
    "more sustainable. This is the most common approach, typically used by profit-oriented "
    "companies that are gradually integrating purpose alongside profit. The marketing process "
    "remains central and sustainability is layered on top."
))
story.append(body(
    "Example: <b>Sustainable Pricing</b> — A sustainable price accounts fully for the economic, "
    "environmental and social costs of a product's manufacture and marketing, while still "
    "providing value for customers and a fair profit for the business. Unlike traditional pricing "
    "strategies focused primarily on competitiveness or margin, sustainable pricing strives for a "
    "healthier balance between People, Planet and Profit. Other examples include biodegradable "
    "or recycled packaging, or manufacturing processes that use fewer resources and produce "
    "less waste."
))

story.append(Spacer(1, 0.15 * cm))
story.append(body("<b>Direction 2 — Sustainability First, Marketing as the Enabler:</b>"))
story.append(body(
    "Here the organisation's primary reason for existence is to address a social or environmental "
    "challenge, and marketing disciplines are used to bring that social responsibility to life. "
    "This approach is more common among organisations for which <b>purpose comes before profit</b> "
    "— non-profits, social enterprises, and many governmental institutions."
))
story.append(body(
    "Specific marketing disciplines that fall under this direction include:"
))
story.append(bullet_item("<b>Non-profit marketing and fundraising</b> — applying marketing techniques "
    "to mobilise resources and support for mission-driven organisations."))
story.append(bullet_item("<b>Social marketing</b> — using marketing to drive <i>social change</i> in "
    "behaviour (e.g., persuading people to recycle, to stop littering, or to adopt healthier "
    "lifestyles)."))

story.append(subsection_header("4.3 Applying Socially Responsible Marketing — The SDG Matrix Exercise"))
story.append(body(
    "A practical tool introduced in the module is a <b>Marketing Process × SDG Matrix</b>. "
    "Organisations can use this framework to systematically explore opportunities to align each "
    "step of their marketing process with one or more of the 17 SDGs:"
))
story.append(bullet_item("Each <b>column</b> represents a step in the marketing process "
    "(environment analysis, strategy, product, price, place, promotion)."))
story.append(bullet_item("Each <b>row</b> represents one of the 17 SDGs."))
story.append(bullet_item("The organisation then considers how it can align each marketing step with each "
    "relevant SDG, filling in concrete actions or commitments."))
story.append(Spacer(1, 0.2 * cm))
story.append(body(
    "This matrix makes socially responsible marketing tangible and actionable. It prevents "
    "sustainability from remaining a vague aspiration and helps teams identify specific, "
    "measurable opportunities across the entire marketing function."
))

story.append(subsection_header("4.4 The Breadth of Socially Responsible Marketing"))
story.append(body(
    "Socially responsible marketing is an <b>umbrella term</b> covering a wide variety of "
    "sub-topics and disciplines, all sharing the common thread of the interplay between social "
    "responsibility and marketing:"
))
story.append(bullet_item("<b>Sustainable consumption behaviour</b> — understanding and influencing "
    "how consumers make choices that are more environmentally and socially responsible."))
story.append(bullet_item("<b>Marketing ethics</b> — the moral principles governing marketing decisions "
    "and practices."))
story.append(bullet_item("<b>Social marketing</b> — using marketing tools to stimulate socially "
    "beneficial behaviour change."))
story.append(bullet_item("<b>Non-profit marketing</b> — marketing in service of mission-driven, "
    "non-commercial organisations."))
story.append(bullet_item("<b>Green/environmental marketing</b> — communicating and delivering "
    "environmentally friendly products and processes."))

# ── 5. Key Takeaways ─────────────────────────────────────────────────────────
story.append(section_header("5. Key Takeaways"))
story.append(body(
    "Prof. De Bock concludes the presentation with a concise summary of the core concepts. "
    "These are reproduced and elaborated below:"
))

takeaways = [
    (
        "1. Marketing is a value-creation process.",
        "Marketing is the process by which organisations create value for customers and build strong "
        "customer relationships in order to capture value in return. Being customer-centric is "
        "central to successful marketing."
    ),
    (
        "2. The marketing world has changed — and so must marketing practice.",
        "The classical marketing process remains a useful framework, but it must be adapted to the "
        "realities of the new marketing world: empowered consumers, globalisation, digital "
        "technology, and rising expectations around social responsibility."
    ),
    (
        "3. Social responsibility is rooted in sustainable development.",
        "Sustainable development — meeting current needs without compromising future generations — "
        "is the cornerstone of social responsibility. The SDGs provide 17 concrete goals that give "
        "organisations a clear framework for action."
    ),
    (
        "4. Socially responsible marketing merges both concepts.",
        "An organisation engaged in socially responsible marketing meets current customer needs in "
        "a socially and environmentally responsible manner, without burdening future generations. "
        "It goes beyond the traditional company–customer dyad to include societal and environmental "
        "well-being."
    ),
    (
        "5. The relationship between marketing and sustainability runs in two directions.",
        "Organisations can start with marketing and add sustainability (most common for profit-first "
        "companies), or start with sustainability and use marketing to advance it (most common for "
        "purpose-first organisations such as non-profits and social enterprises)."
    ),
    (
        "6. Socially responsible marketing is a broad, evolving field.",
        "It encompasses social marketing, non-profit marketing, sustainable consumption behaviour, "
        "marketing ethics and much more. All these topics share the interplay between social "
        "responsibility and marketing."
    ),
]

for title, explanation in takeaways:
    story.append(KeepTogether([
        Paragraph(f"<b>{title}</b>", style_key_takeaway),
        Paragraph(explanation, ParagraphStyle(
            "TakeawayBody",
            parent=style_body,
            leftIndent=14,
            rightIndent=14,
            spaceAfter=12,
        )),
    ]))

# ── Footer note ──────────────────────────────────────────────────────────────
story.append(Spacer(1, 1 * cm))
story.append(divider())
story.append(Paragraph(
    "<i>This document is based on the transcript knowledge clips for Module 11: "
    "Socially Responsible Marketing, as presented by Prof. Tine De Bock, KU Leuven. "
    "All quotations are drawn directly from the lecture transcripts.</i>",
    ParagraphStyle(
        "FooterNote",
        parent=styles["Normal"],
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#777777"),
        alignment=TA_CENTER,
        fontName="Helvetica-Oblique",
    ),
))

doc.build(story)
print("PDF created successfully.")
