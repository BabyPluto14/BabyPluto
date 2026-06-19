from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# ── colour palette ──────────────────────────────────────────────────────────
DARK_BLUE   = HexColor("#1A237E")
MED_BLUE    = HexColor("#283593")
LIGHT_BLUE  = HexColor("#3949AB")
ACCENT      = HexColor("#1565C0")
HIGHLIGHT   = HexColor("#E3F2FD")
BULLET_COL  = HexColor("#0D47A1")
QUOTE_BG    = HexColor("#EDE7F6")
QUOTE_LINE  = HexColor("#7E57C2")
BOX_BG      = HexColor("#E8F5E9")
BOX_LINE    = HexColor("#2E7D32")
FAIL_BG     = HexColor("#FFEBEE")
FAIL_LINE   = HexColor("#C62828")
GREY_TEXT   = HexColor("#37474F")
LIGHT_GREY  = HexColor("#ECEFF1")
DIVIDER     = HexColor("#90CAF9")

def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles["cover_title"] = ParagraphStyle(
        "cover_title",
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=36,
        textColor=white,
        alignment=TA_CENTER,
        spaceAfter=12,
    )
    styles["cover_sub"] = ParagraphStyle(
        "cover_sub",
        fontName="Helvetica",
        fontSize=14,
        leading=20,
        textColor=HexColor("#BBDEFB"),
        alignment=TA_CENTER,
        spaceAfter=6,
    )
    styles["cover_meta"] = ParagraphStyle(
        "cover_meta",
        fontName="Helvetica-Oblique",
        fontSize=11,
        leading=16,
        textColor=HexColor("#90CAF9"),
        alignment=TA_CENTER,
    )
    styles["chapter"] = ParagraphStyle(
        "chapter",
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=24,
        textColor=white,
        alignment=TA_LEFT,
        spaceBefore=4,
        spaceAfter=4,
        leftIndent=6,
    )
    styles["section"] = ParagraphStyle(
        "section",
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=18,
        textColor=DARK_BLUE,
        spaceBefore=14,
        spaceAfter=6,
    )
    styles["body"] = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=10.5,
        leading=16,
        textColor=GREY_TEXT,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
    )
    styles["bullet"] = ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=10.5,
        leading=16,
        textColor=GREY_TEXT,
        leftIndent=18,
        firstLineIndent=-10,
        spaceAfter=5,
    )
    styles["sub_bullet"] = ParagraphStyle(
        "sub_bullet",
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        textColor=GREY_TEXT,
        leftIndent=36,
        firstLineIndent=-10,
        spaceAfter=4,
    )
    styles["quote"] = ParagraphStyle(
        "quote",
        fontName="Helvetica-Oblique",
        fontSize=10.5,
        leading=16,
        textColor=HexColor("#4A148C"),
        leftIndent=12,
        rightIndent=12,
        spaceAfter=4,
    )
    styles["box_heading"] = ParagraphStyle(
        "box_heading",
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=16,
        textColor=HexColor("#1B5E20"),
        spaceAfter=4,
    )
    styles["box_body"] = ParagraphStyle(
        "box_body",
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=HexColor("#1B5E20"),
        spaceAfter=4,
    )
    styles["fail_heading"] = ParagraphStyle(
        "fail_heading",
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=16,
        textColor=HexColor("#B71C1C"),
        spaceAfter=4,
    )
    styles["fail_body"] = ParagraphStyle(
        "fail_body",
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=HexColor("#7F0000"),
        spaceAfter=4,
    )
    styles["canvas_label"] = ParagraphStyle(
        "canvas_label",
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=14,
        textColor=DARK_BLUE,
        alignment=TA_CENTER,
    )
    styles["canvas_body"] = ParagraphStyle(
        "canvas_body",
        fontName="Helvetica",
        fontSize=9,
        leading=13,
        textColor=GREY_TEXT,
        alignment=TA_CENTER,
    )
    styles["toc_entry"] = ParagraphStyle(
        "toc_entry",
        fontName="Helvetica",
        fontSize=11,
        leading=18,
        textColor=GREY_TEXT,
    )
    styles["toc_num"] = ParagraphStyle(
        "toc_num",
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=18,
        textColor=ACCENT,
    )
    styles["footer"] = ParagraphStyle(
        "footer",
        fontName="Helvetica",
        fontSize=8,
        leading=10,
        textColor=HexColor("#90A4AE"),
        alignment=TA_CENTER,
    )
    return styles


def chapter_header(title, styles):
    """Blue banner with white chapter title."""
    data = [[Paragraph(title, styles["chapter"])]]
    t = Table(data, colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), DARK_BLUE),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return [t, Spacer(1, 10)]


def quote_box(speaker, text, styles):
    """Purple-tinted pull-quote box."""
    label = Paragraph(f"<b>{speaker}</b>", styles["quote"])
    body  = Paragraph(f"“{text}”", styles["quote"])
    data  = [[label], [body]]
    t = Table(data, colWidths=[16.2*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), QUOTE_BG),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LINEBEFORE",    (0,0), (0,-1), 4, QUOTE_LINE),
    ]))
    return [t, Spacer(1, 8)]


def success_box(title, paras, styles):
    rows = [[Paragraph(title, styles["box_heading"])]]
    for p in paras:
        rows.append([Paragraph(p, styles["box_body"])])
    t = Table(rows, colWidths=[16.2*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), BOX_BG),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LINEBEFORE",    (0,0), (0,-1), 4, BOX_LINE),
    ]))
    return [t, Spacer(1, 10)]


def failure_box(title, paras, styles):
    rows = [[Paragraph(title, styles["fail_heading"])]]
    for p in paras:
        rows.append([Paragraph(p, styles["fail_body"])])
    t = Table(rows, colWidths=[16.2*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), FAIL_BG),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LINEBEFORE",    (0,0), (0,-1), 4, FAIL_LINE),
    ]))
    return [t, Spacer(1, 10)]


def bullet(text, styles, sub=False):
    key = "sub_bullet" if sub else "bullet"
    marker = "◦" if sub else "•"
    return Paragraph(f"{marker}&nbsp;&nbsp;{text}", styles[key])


def build_cover(styles):
    """Dark blue full-width cover page using a table."""
    cover_data = [[
        Paragraph("Module 3", styles["cover_sub"]),
    ],[
        Paragraph("Marketing in a<br/>Network Economy", styles["cover_title"]),
    ],[
        Spacer(1, 8),
    ],[
        Paragraph("Detailed Explanations from the Expert Podcast", styles["cover_sub"]),
    ],[
        Spacer(1, 24),
    ],[
        Paragraph("Based on the podcast with <b>Erwin Knuyt</b> &amp; <b>Prof. Tine De Bock</b>", styles["cover_meta"]),
    ],[
        Paragraph("KU Leuven &nbsp;|&nbsp; Department of Marketing", styles["cover_meta"]),
    ]]
    t = Table(cover_data, colWidths=[17*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), DARK_BLUE),
        ("TOPPADDING",    (0,0), (-1,-1), 14),
        ("BOTTOMPADDING", (0,0), (-1,-1), 14),
        ("LEFTPADDING",   (0,0), (-1,-1), 20),
        ("RIGHTPADDING",  (0,0), (-1,-1), 20),
        ("ROUNDEDCORNERS", [8]),
    ]))
    return [Spacer(1, 60), t, Spacer(1, 40),
            HRFlowable(width="100%", thickness=1, color=DIVIDER),
            Spacer(1, 10),
            Paragraph(
                "This document summarises all concepts, examples, and insights presented in the "
                "Module 3 podcast on Marketing in a Network Economy. It is intended as a study "
                "companion for students at KU Leuven.",
                styles["body"]
            ),
            PageBreak()]


def build_toc(styles):
    items = [
        ("1", "Introduction & Context"),
        ("2", "What Is a Network? Personal vs. Business"),
        ("3", "The Core Pitch of Network Marketing"),
        ("4", "Common Misconceptions"),
        ("5", "Does Network Thinking Change the Essence of Marketing?"),
        ("6", "Network Equity"),
        ("7", "Real-World Success Examples"),
        ("8", "A Notable Failure: Google–Novartis"),
        ("9", "Can Small Companies & Start-ups Use Network Thinking?"),
        ("10", "Why Marketing Leads the Network Agenda"),
        ("11", "Key Skills for a Network Marketeer"),
        ("12", "The Marketing Network Canvas"),
        ("13", "Two-Sided Networks: Uber & Airbnb"),
        ("14", "The Self-Driving Car: Complexity Needs Networks"),
        ("15", "Key Takeaways & Conclusion"),
    ]
    elems = chapter_header("Table of Contents", styles)
    elems.append(Spacer(1, 8))
    for num, title in items:
        row = Table([[Paragraph(num + ".", styles["toc_num"]),
                      Paragraph(title, styles["toc_entry"])]],
                    colWidths=[1.2*cm, 15.8*cm])
        row.setStyle(TableStyle([
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 3),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ]))
        elems.append(row)
    elems.append(PageBreak())
    return elems


def build_body(styles):
    elems = []

    # ── 1. Introduction ──────────────────────────────────────────────────────
    elems += chapter_header("1.  Introduction & Context", styles)
    elems.append(Paragraph(
        "Module 3 of the KU Leuven marketing programme centres on a recorded podcast "
        "conversation between <b>Prof. Tine De Bock</b> (professor of marketing at KU Leuven) "
        "and <b>Erwin Knuyt</b>, a seasoned practitioner with more than 15 years in sales and "
        "marketing roles, a decade as a business consultant at PwC and IBM, and the founder of "
        "Skein Company — a firm specialising in B2B marketing and business transformation. "
        "Knuyt is also a certified alliance manager from the Association of Strategic Alliance "
        "Professionals and a guest professor at both KU Leuven and the University of Antwerp.",
        styles["body"]
    ))
    elems.append(Paragraph(
        "The conversation explores how the rise of network thinking has reshaped the practice of "
        "marketing. Rather than treating marketing as a simple two-way exchange between a brand "
        "and its customers, Knuyt argues that modern marketers must become architects of broad, "
        "multi-stakeholder networks that co-create and deliver value.",
        styles["body"]
    ))
    elems.append(Spacer(1, 6))

    # ── 2. What Is a Network ─────────────────────────────────────────────────
    elems += chapter_header("2.  What Is a Network? Personal vs. Business", styles)
    elems.append(Paragraph(
        "Knuyt begins by making the abstract idea of a network concrete by inviting listeners to "
        "think about their own personal networks:",
        styles["body"]
    ))
    elems += quote_box("Erwin Knuyt",
        "Students have a network of their fellow students that they meet in university. At home you "
        "have your friends, you have your family, you have your sports groups. These are all clusters "
        "of network — some connected, some not connected.", styles)
    elems.append(Paragraph(
        "Networks serve multiple functions: they carry information, ideas, knowledge, and can even "
        "open doors to jobs. Crucially, within any network there are <b>nodes</b> — highly connected "
        "individuals (or organisations) that act as information hubs. In everyday life we call them "
        "'know-it-alls'. In business, being a node means being first to spot trends, opportunities, "
        "and market shifts.",
        styles["body"]
    ))
    elems.append(Paragraph(
        "The same social-network logic, formalised in sociology as <b>Social Network Analysis (SNA)</b>, "
        "can be applied to organisations. SNA visualises how entities are connected, where information "
        "flows, and who the critical connectors are. Applying this lens to a company's partner ecosystem "
        "is the starting point of marketing in a network economy.",
        styles["body"]
    ))
    elems.append(Spacer(1, 6))

    # ── 3. Core Pitch ────────────────────────────────────────────────────────
    elems += chapter_header("3.  The Core Pitch of Network Marketing", styles)
    elems += quote_box("Erwin Knuyt",
        "Today, success doesn't only depend on <i>what</i> you know, but it really depends on "
        "<i>who</i> you know.", styles)
    elems.append(Paragraph(
        "This single sentence captures the philosophical shift that underpins the entire module. "
        "Traditional competitive advantage rested on proprietary knowledge, patents, or production "
        "efficiency — resources owned inside the firm. In a network economy, advantage increasingly "
        "comes from <b>the quality and breadth of an organisation's relationships</b>: its suppliers, "
        "customers, innovation partners, distribution intermediaries, and even competitors in pre-competitive "
        "research consortia.",
        styles["body"]
    ))
    elems.append(Spacer(1, 6))

    # ── 4. Misconceptions ────────────────────────────────────────────────────
    elems += chapter_header("4.  Common Misconceptions", styles)
    elems.append(Paragraph(
        "Two recurring misconceptions arise when Knuyt introduces network marketing to new audiences:",
        styles["body"]
    ))

    elems.append(Paragraph("<b>Misconception 1 — Networking is only for extroverts</b>", styles["section"]))
    elems.append(Paragraph(
        "Students and early-career professionals often feel that networking is out of reach because "
        "they consider themselves introverted or 'not a social person'. Knuyt challenges this "
        "directly: while some people are naturally more inclined to network, <i>everyone has the "
        "capability</i>. Networking is a learnable skill. KU Leuven's Kick skills facility provides "
        "videos and resources to help students develop their personal networking skills.",
        styles["body"]
    ))

    elems.append(Paragraph("<b>Misconception 2 — 'We already network'</b>", styles["section"]))
    elems.append(Paragraph(
        "Many organisations, when first confronted with the idea of network marketing, respond with "
        "'we already have partnerships'. Knuyt does not dispute this — most organisations do have "
        "some form of partnerships. The critical distinction is between <b>accidental networking</b> "
        "(relationships that form informally) and <b>strategic, conscious networking</b> (visualising, "
        "mapping, and actively managing the network). Successful organisations:",
        styles["body"]
    ))
    for item in [
        "Make their network <i>visible</i> — who is connected to whom, and why.",
        "Add new partners proactively when a strategic gap is identified.",
        "Remove or replace partners when they are no longer fit for purpose.",
        "Join innovation consortia or ecosystems to access emerging knowledge.",
    ]:
        elems.append(bullet(item, styles))
    elems.append(Spacer(1, 6))

    # ── 5. Essence of Marketing ──────────────────────────────────────────────
    elems += chapter_header("5.  Does Network Thinking Change the Essence of Marketing?", styles)
    elems.append(Paragraph(
        "Prof. De Bock poses a foundational question: does the network mindset alter what marketing "
        "<i>is</i>? Knuyt's answer is nuanced:",
        styles["body"]
    ))
    elems += quote_box("Erwin Knuyt",
        "In the essence of what we do in marketing, it will not change. Marketing is there to create "
        "value for our customers, our consumers, our organisation, and for society at large. The "
        "question is: <i>where</i> do we generate this value? A lot of the value is created from "
        "bringing in and developing the right alliances.", styles)
    elems.append(Paragraph(
        "In other words, the <b>goal</b> of marketing — creating and capturing value — remains "
        "unchanged. What changes is the <b>mechanism</b>: in a network economy, value is increasingly "
        "co-created across organisational boundaries rather than generated solely within a single firm. "
        "Technologies in AI, biotech, materials science, and digital platforms are advancing so rapidly "
        "that no single company can own all the required knowledge. The firm that builds the right "
        "alliances <i>first</i> gains a significant first-mover advantage.",
        styles["body"]
    ))
    elems.append(Spacer(1, 6))

    # ── 6. Network Equity ────────────────────────────────────────────────────
    elems += chapter_header("6.  Network Equity", styles)
    elems.append(Paragraph(
        "Knuyt introduces an important concept — <b>network equity</b> — that parallels the well-known "
        "idea of brand equity. Just as a brand has equity (the accumulated reputation and trust that "
        "makes consumers choose it over alternatives), an organisation has network equity:",
        styles["body"]
    ))
    elems += quote_box("Erwin Knuyt",
        "Network equity is your attractiveness as an organisation to collaborate. Are you open? Are "
        "you respected? Is there success in the past?", styles)
    elems.append(Paragraph(
        "High network equity means other organisations <i>want</i> to partner with you. Google, for "
        "example, is described as having very high network equity — almost every company would welcome "
        "a collaboration with Google. Network equity is built over time through:",
        styles["body"]
    ))
    for item in [
        "<b>Openness</b> — a willingness to share knowledge and co-invest.",
        "<b>Respect</b> — being seen as a trustworthy, fair partner.",
        "<b>Track record</b> — a history of partnerships that delivered mutual value.",
        "<b>Complementary resources</b> — bringing something unique that others need.",
    ]:
        elems.append(bullet(item, styles))
    elems.append(Spacer(1, 6))

    # ── 7. Success Examples ──────────────────────────────────────────────────
    elems += chapter_header("7.  Real-World Success Examples", styles)

    # COVID vaccines
    elems += success_box(
        "Example A — COVID-19 Vaccine Development",
        [
            "When the pandemic struck, no single company possessed all the capabilities needed to "
            "develop, manufacture, and distribute a vaccine at speed. What followed was a rapid "
            "formation of alliances between biotech firms, pharmaceutical giants, and universities "
            "(e.g., the Oxford University partnership that produced the AstraZeneca vaccine).",
            "Each partner contributed a different, complementary capability:",
            "  •  Biotech firms: cutting-edge mRNA or vector technology.",
            "  •  Pharmaceutical companies: manufacturing scale and regulatory expertise.",
            "  •  Universities: fundamental research and clinical trial infrastructure.",
            "  •  Logistics companies: cold-chain distribution at global scale.",
            "The result was vaccines in a fraction of the normal development timeline. Knuyt "
            "emphasises that many of these partners had pre-existing working relationships; the "
            "crisis activated and deepened them. The lesson: build your network <i>before</i> you "
            "need it, so it is ready when an opportunity or crisis arrives.",
        ],
        styles
    )

    # Xiaomi
    elems += success_box(
        "Example B — Xiaomi & the Mi Ecosystem",
        [
            "Xiaomi began as a smartphone company, entering the Chinese market with high-performance "
            "devices at competitive prices. Rather than remaining a phone manufacturer, Xiaomi used "
            "the smartphone as a platform from which to build a vast <b>ecosystem of connected "
            "products</b> — from doorbells and rice cookers to refrigerators — all marketed under "
            "the Mi brand.",
            "Crucially, Xiaomi does not manufacture most of these products itself. Instead, it:",
            "  •  Identifies best-in-class manufacturers for each product category.",
            "  •  Takes a minority equity stake in each partner, aligning incentives.",
            "  •  Sets design and quality specifications, and integrates the product into the "
            "         Mi ecosystem.",
            "This supplier network strategy allows Xiaomi to expand its product range rapidly without "
            "the capital burden of building manufacturing capability from scratch. It is a textbook "
            "example of <b>network-driven value creation</b>: the brand and ecosystem provide the "
            "customer experience, while partners provide the operational backbone.",
            "Trust and fit are critical: Xiaomi carefully screens partners across technology "
            "compatibility, cultural alignment, and long-term strategic fit.",
        ],
        styles
    )

    # Haier
    elems += success_box(
        "Example C — Haier's Networked Organisation",
        [
            "Haier, the Chinese household-appliance giant, took network thinking to a structural "
            "extreme by dismantling its traditional hierarchy entirely. Instead of departments and "
            "sub-departments reporting to a central boss, Haier restructured into small, autonomous "
            "teams of 15–20 people — each focused on a specific market segment.",
            "For example, one team might be dedicated to 'refrigerators for young urban professionals'. "
            "This team acts as an internal entrepreneur and marketer. Because it is small, it must "
            "connect with other internal teams to access design, production, legal, HR, and finance "
            "services — all of which are also small, networked units.",
            "Haier further allows these micro-units to network with nodes <i>outside</i> the "
            "organisation, creating intense competition and fresh ideas flowing in from the market.",
            "The result is an organisation that is simultaneously:",
            "  •  Customer-obsessed (each team owns a specific market need).",
            "  •  Agile (small teams move faster than large divisions).",
            "  •  Networked (units must collaborate across internal and external boundaries).",
            "Haier is considered one of the most advanced real-world implementations of a fully "
            "networked organisational model.",
        ],
        styles
    )
    elems.append(Spacer(1, 6))

    # ── 8. Failure Example ───────────────────────────────────────────────────
    elems += chapter_header("8.  A Notable Failure: Google–Novartis", styles)
    elems += failure_box(
        "Case — Google & Novartis Smart Contact Lens",
        [
            "In 2014 Google and Novartis publicly announced an ambitious partnership: a smart "
            "contact lens embedded with miniaturised sensors capable of measuring blood-glucose "
            "levels through a patient's tear fluid — a potential replacement for the painful "
            "finger-prick test used by millions of diabetes patients.",
            "Both partners had high network equity: Google brought cutting-edge miniaturisation "
            "and sensor technology; Novartis brought deep pharmaceutical and medical expertise, "
            "as well as regulatory knowledge of diabetes care.",
            "Despite the fanfare, the project eventually failed. The exact technical reasons were "
            "never publicly disclosed, but the tear-fluid glucose measurement proved insufficiently "
            "reliable for clinical use.",
            "Key lessons Knuyt draws from this case:",
            "  •  Do not announce partnerships to the market prematurely — public announcements "
            "         create expectations that are difficult to walk back if the project fails.",
            "  •  Research shows that approximately <b>60% of business partnerships fail</b>. "
            "         This is not an argument against partnerships, but a reminder that careful "
            "         partner selection, governance, and execution are essential.",
            "  •  Once a partnership <i>does</i> deliver, communicate the results effectively "
            "         to build network equity and attract future partners.",
        ],
        styles
    )
    elems.append(Spacer(1, 6))

    # ── 9. Startups ──────────────────────────────────────────────────────────
    elems += chapter_header("9.  Can Small Companies & Start-ups Use Network Thinking?", styles)
    elems.append(Paragraph(
        "A natural objection is that network thinking requires resources that only large corporations "
        "possess. Knuyt rejects this view strongly, pointing to start-ups as the most vivid example "
        "of necessity-driven networking:",
        styles["body"]
    ))
    elems += quote_box("Erwin Knuyt",
        "What does a start-up have? Usually the only thing they have is an idea, a lot of courage, "
        "and a lot of desire to grow. A start-up cannot survive without building the right "
        "partnerships.", styles)
    elems.append(Paragraph(
        "Start-ups typically need partnerships in the following areas simultaneously:",
        styles["body"]
    ))
    for item in [
        "<b>Finance</b> — business angels, venture capitalists, government grants.",
        "<b>Marketing & brand</b> — they lack recognition; partnerships with established brands "
        "lend credibility.",
        "<b>Manufacturing</b> — they cannot afford factories; they must partner with contract "
        "manufacturers.",
        "<b>Distribution</b> — reaching customers requires intermediaries.",
        "<b>Technology</b> — they often need complementary IP or platforms.",
    ]:
        elems.append(bullet(item, styles))
    elems.append(Paragraph(
        "While large corporations may have dedicated <b>alliance managers</b> for this work, "
        "start-up founders typically carry the partnership function themselves. The mindset — "
        "constantly scanning the environment for complementary partners — is the same at every scale.",
        styles["body"]
    ))
    elems.append(Spacer(1, 6))

    # ── 10. Why Marketing Leads ──────────────────────────────────────────────
    elems += chapter_header("10.  Why Marketing Leads the Network Agenda", styles)
    elems.append(Paragraph(
        "Knuyt argues compellingly that marketing is the natural organisational owner of network "
        "strategy. The reasoning:",
        styles["body"]
    ))
    for item in [
        "<b>Voice of the customer</b> — marketers are trained to understand current and future "
        "customer needs. They can translate these insights into the partnership requirements the "
        "organisation needs to fulfil them.",
        "<b>Cross-functional connectors</b> — marketers typically have strong communication and "
        "project management skills, enabling them to orchestrate collaboration across sales, "
        "R&D, operations, and finance internally.",
        "<b>External antenna</b> — marketers scan the competitive landscape and are well placed "
        "to identify which <i>external</i> partnerships are missing from the portfolio.",
        "<b>Strategic input</b> — if a marketer has a seat at the table when partnership decisions "
        "are made, the customer's voice will shape which alliances are formed.",
    ]:
        elems.append(bullet(item, styles))
    elems += quote_box("Erwin Knuyt",
        "If the marketeer can be on the table to discuss partnerships, they will be able to "
        "represent that voice of the customer, and in that way the organisation is going to make "
        "the right decisions in their partner network.", styles)
    elems.append(Spacer(1, 6))

    # ── 11. Skills ───────────────────────────────────────────────────────────
    elems += chapter_header("11.  Key Skills for a Network Marketeer", styles)
    elems.append(Paragraph(
        "Knuyt identifies two core competency clusters for what he calls a <b>MINE</b> — a "
        "Marketeer In a Network Economy:",
        styles["body"]
    ))

    elems.append(Paragraph("<b>Competency 1 — Strategic Insight</b>", styles["section"]))
    elems.append(Paragraph(
        "The ability to think strategically about the firm's value proposition, its internal "
        "capabilities, and the gaps that can only be filled by partners. This includes using "
        "structured frameworks such as the <b>Marketing Network Canvas</b> (see Section 12) "
        "to map and plan the network.",
        styles["body"]
    ))

    elems.append(Paragraph("<b>Competency 2 — Opportunity Mindset</b>", styles["section"]))
    elems.append(Paragraph(
        "An open, entrepreneurial attitude — the capacity to see unmet market needs before others "
        "do. Knuyt illustrates this with the founding stories of two-sided platform companies:",
        styles["body"]
    ))
    for item in [
        "<b>Airbnb</b> — two founders spotted that the classical rental-advertisement market was "
        "failing to connect people with spare rooms and travellers seeking affordable accommodation. "
        "They built a platform that connected the two sides of this market.",
        "<b>Uber</b> — the founders identified a systematic failure in taxi services (unreliable, "
        "opaque pricing, poor customer experience) and built a platform that matched drivers and "
        "passengers in real time.",
    ]:
        elems.append(bullet(item, styles))
    elems.append(Paragraph(
        "In both cases the insight was not technological but relational: there was an unmet need "
        "that could be solved by connecting two groups that had previously not been efficiently "
        "linked. This is the essence of the opportunity mindset.",
        styles["body"]
    ))

    elems.append(Paragraph("<b>The Alliance Manager Role</b>", styles["section"]))
    elems.append(Paragraph(
        "In larger organisations, the partnership function is increasingly professionalised into a "
        "dedicated <b>alliance manager</b> role. Alliance managers are trained to:",
        styles["body"]
    ))
    for item in [
        "Govern the relationship between two independent companies.",
        "Balance the interests of both parties so that value is created for each.",
        "Manage trust, communication, and conflict resolution.",
        "Track performance metrics of the partnership against agreed goals.",
    ]:
        elems.append(bullet(item, styles))
    elems.append(Spacer(1, 6))

    # ── 12. Marketing Network Canvas ─────────────────────────────────────────
    elems += chapter_header("12.  The Marketing Network Canvas", styles)
    elems.append(Paragraph(
        "Inspired by Osterwalder's widely used <b>Business Model Canvas</b>, Knuyt and his "
        "collaborators developed the <b>Marketing Network Canvas</b> — a visual framework that "
        "helps organisations map and manage their network across five clusters.",
        styles["body"]
    ))
    elems.append(Paragraph(
        "The canvas is organised around a central hub (your own organisation) with two wings:",
        styles["body"]
    ))
    for item in [
        "<b>Right-hand side</b> = customer-facing clusters (Customer Network, Distribution/Channel Network).",
        "<b>Left-hand side</b> = input-side clusters (Supplier Network, Innovation Networks).",
        "<b>Centre</b> = Internal Network.",
    ]:
        elems.append(bullet(item, styles))

    elems.append(Spacer(1, 10))

    # ── Visual Canvas Table ──────────────────────────────────────────────────
    def cell(title, desc, bg):
        p1 = Paragraph(title, styles["canvas_label"])
        p2 = Paragraph(desc,  styles["canvas_body"])
        return [p1, Spacer(1,4), p2]

    canvas_data = [
        [
            cell("Innovation\nNetworks",
                 "Pre-competitive consortia, university labs, government-funded R&D clusters. "
                 "Source of frontier knowledge.", HexColor("#E8EAF6")),
            cell("Internal\nNetwork",
                 "Your organisation's departments & cross-functional teams. Marketing must network "
                 "internally to bring the customer voice to every function.", HexColor("#E3F2FD")),
            cell("Customer\nNetwork",
                 "Key customers, early adopters, key opinion leaders (KOLs). Strategic relationships "
                 "that provide insight and market influence.", HexColor("#E8F5E9")),
        ],
        [
            cell("Supplier\nNetwork",
                 "Strategic suppliers from whom you source products, components, or services. "
                 "May involve equity stakes for deep alignment (e.g., Xiaomi).", HexColor("#FFF3E0")),
            cell("YOUR\nORGANISATION",
                 "The hub. Integrator of all network clusters. Marketing sits here, orchestrating "
                 "value creation across all nodes.", HexColor("#FCE4EC")),
            cell("Distribution /\nChannel Network",
                 "Intermediaries between brand and customer — logistical channels (Amazon), "
                 "franchisees (McDonald's), resellers, agents.", HexColor("#F3E5F5")),
        ],
    ]

    col_w = [5.3*cm, 5.4*cm, 5.5*cm]
    c_table = Table(canvas_data, colWidths=col_w, rowHeights=[3.5*cm, 3.5*cm])
    c_table.setStyle(TableStyle([
        # left column
        ("BACKGROUND", (0,0), (0,0), HexColor("#E8EAF6")),
        ("BACKGROUND", (0,1), (0,1), HexColor("#FFF3E0")),
        # centre column
        ("BACKGROUND", (1,0), (1,0), HexColor("#E3F2FD")),
        ("BACKGROUND", (1,1), (1,1), HexColor("#FCE4EC")),
        # right column
        ("BACKGROUND", (2,0), (2,0), HexColor("#E8F5E9")),
        ("BACKGROUND", (2,1), (2,1), HexColor("#F3E5F5")),

        ("GRID",    (0,0), (-1,-1), 1, HexColor("#BDBDBD")),
        ("VALIGN",  (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("FONTNAME", (1,1), (1,1), "Helvetica-Bold"),
        ("FONTSIZE", (1,1), (1,1), 10),
        ("ALIGN",   (0,0), (-1,-1), "CENTER"),
    ]))
    elems.append(c_table)
    elems.append(Spacer(1, 10))

    elems.append(Paragraph(
        "Below is a detailed explanation of each of the five clusters:",
        styles["body"]
    ))

    # Cluster details
    clusters = [
        ("Cluster 1 — Internal Network (Centre)",
         "Every marketer's first networking task is internal. Marketing must connect with R&D to "
         "understand what the company can build, with sales to understand what customers are buying, "
         "with finance to understand resource constraints, and with HR to understand talent availability. "
         "Only a marketer who has mapped and cultivated the internal network can effectively represent "
         "the customer's voice in strategic decisions. Haier's micro-unit model is an extreme but "
         "instructive realisation of what a fully networked internal organisation can look like."),
        ("Cluster 2 — Customer Network (Right Side)",
         "Not all customers are equal in a network economy. The marketer's task is to identify "
         "those customers whose insights are most strategically valuable. In B2C markets these are "
         "typically <b>early adopters</b> — consumers who experiment with new products and whose "
         "feedback shapes the mainstream market. In B2B and medical markets they are <b>key opinion "
         "leaders (KOLs)</b> — specialists whose endorsement influences the purchase decisions of "
         "the broader professional community. Developing deep, trust-based relationships with these "
         "strategic customers is a source of both insight and competitive advantage."),
        ("Cluster 3 — Distribution / Channel Network (Right Side)",
         "Channel partners stand between the brand and the end customer. Their management is one "
         "of the classic 'four Ps' of marketing (Place). In a network economy, the relationship "
         "with distributors, resellers, agents, and franchisees becomes a strategic competency. "
         "McDonald's relationship with its franchisees illustrates this: each franchisee is an "
         "independent company entrusted to represent the McDonald's brand. Selecting franchisees "
         "who embody brand values, training them, and holding them to quality standards is as "
         "much a marketing activity as an advertising campaign. Amazon is a different model — a "
         "logistical channel through which many brands reach consumers, but behind Amazon lies a "
         "vast supplier and logistics partner network."),
        ("Cluster 4 — Supplier Network (Left Side)",
         "Suppliers are increasingly strategic partners rather than commodity vendors. Xiaomi "
         "demonstrates the extreme of this view: its suppliers are not just sourced at the lowest "
         "price — Xiaomi takes minority equity stakes in them, aligning long-term incentives. "
         "The supplier becomes a node in the Xiaomi ecosystem, bound by shared specifications, "
         "quality standards, and ecosystem integration. For marketers, the implication is that "
         "supplier relationships must be evaluated not just on cost and quality, but on strategic "
         "fit, cultural alignment, and the potential to co-develop the value proposition."),
        ("Cluster 5 — Innovation Networks (Left Side)",
         "Innovation networks are pre-competitive consortia, university research groups, government-"
         "funded clusters, and open-innovation ecosystems where organisations collaborate on "
         "early-stage problems before commercialisation. The High Tech Campus in Eindhoven "
         "(formerly the Philips R&D campus) is a prime example: dozens of organisations — "
         "start-ups, scale-ups, and multinationals — co-locate to facilitate serendipitous "
         "collaboration. The campus generates approximately four patents per day. Once an idea "
         "is ready for market, it leaves the campus and is commercialised by one of the partners. "
         "In Europe, many such networks are supported by EU-funded research programmes."),
    ]
    for title, body in clusters:
        elems.append(Paragraph(title, styles["section"]))
        elems.append(Paragraph(body, styles["body"]))

    elems.append(Spacer(1, 6))

    # ── 13. Two-Sided Networks ───────────────────────────────────────────────
    elems += chapter_header("13.  Two-Sided Networks: Uber & Airbnb", styles)
    elems.append(Paragraph(
        "Two-sided (or multi-sided) networks are platforms that simultaneously serve two distinct "
        "user groups whose value to each other increases as each side grows. This is also known as "
        "the <b>network effect</b>: the more drivers on Uber, the shorter wait times for riders; "
        "the shorter wait times, the more riders join; the more riders, the more income for drivers; "
        "the more income, the more drivers join.",
        styles["body"]
    ))
    elems.append(Paragraph(
        "Knuyt highlights both platforms as examples of the <b>opportunity mindset</b> skill:",
        styles["body"]
    ))
    for item in [
        "<b>Airbnb</b>: Identified that millions of people had spare rooms or properties, while "
        "travellers were underserved by expensive hotels. The opportunity was to build a trusted "
        "platform connecting hosts and guests globally.",
        "<b>Uber</b>: Identified systemic failures in the taxi market — opaque pricing, unreliable "
        "availability, inconsistent service quality — and built a platform that matched supply "
        "(private drivers) with demand (passengers) in real time.",
    ]:
        elems.append(bullet(item, styles))
    elems.append(Paragraph(
        "Both companies are now global giants, yet their competitive moat is not a factory or a "
        "patent — it is the <b>network itself</b>. Their marketing challenge is to maintain and "
        "grow both sides of the network simultaneously, managing trust, pricing, and brand "
        "reputation across millions of independent participants.",
        styles["body"]
    ))
    elems.append(Spacer(1, 6))

    # ── 14. Self-Driving Cars ────────────────────────────────────────────────
    elems += chapter_header("14.  The Self-Driving Car: When Complexity Demands a Network", styles)
    elems.append(Paragraph(
        "Knuyt closes the interview with a powerful example of why truly complex societal challenges "
        "can only be solved by a network. The autonomous vehicle — a technology promised by Elon "
        "Musk and many others for well over a decade — remains elusive not primarily for a single "
        "technical reason, but because it requires the simultaneous alignment of a vast partner "
        "ecosystem:",
        styles["body"]
    ))
    for item in [
        "<b>Automotive OEMs</b> — vehicle hardware, safety systems, human-machine interfaces.",
        "<b>Technology companies</b> — AI algorithms, sensor fusion (LiDAR, radar, cameras), "
        "real-time mapping.",
        "<b>Telecommunications companies</b> — 5G/V2X communication so vehicles talk to each "
        "other and to infrastructure.",
        "<b>Infrastructure providers</b> — smart traffic lights, road markings readable by sensors.",
        "<b>Energy companies</b> — battery infrastructure and charging networks.",
        "<b>Insurance companies</b> — new liability models for when the car, not the human, is "
        "the driver.",
        "<b>Regulators & governments</b> — legislation permitting autonomous vehicles on public roads.",
        "<b>Consumer trust</b> — public acceptance of ceding control to a machine.",
    ]:
        elems.append(bullet(item, styles))
    elems.append(Paragraph(
        "No single organisation — not even Tesla, Waymo, or Apple — can provide all of these "
        "components alone. The self-driving car will arrive when a network of organisations "
        "achieves sufficient alignment. This is perhaps the clearest illustration of why, in "
        "a network economy, the ability to build and manage alliances is a <i>strategic "
        "survival capability</i>, not just a nice-to-have.",
        styles["body"]
    ))
    elems.append(Spacer(1, 6))

    # ── 15. Key Takeaways ────────────────────────────────────────────────────
    elems += chapter_header("15.  Key Takeaways & Conclusion", styles)
    elems.append(Paragraph(
        "The following themes recur throughout the podcast and represent the essential learning "
        "outcomes of Module 3:",
        styles["body"]
    ))

    takeaways = [
        ("Networks are everywhere",
         "From personal relationships to corporate alliances, networks are the fundamental "
         "structure through which value and information flow in modern economies."),
        ("'Who you know' now matters as much as 'what you know'",
         "Competitive advantage increasingly comes from relationship capital — the quality and "
         "breadth of an organisation's partner network."),
        ("Marketing's purpose is unchanged; its method has evolved",
         "Creating value for customers, organisations, and society remains the north star. But "
         "the primary vehicle for value creation is now the alliance portfolio, not solely "
         "internal R&D or production."),
        ("Be a strategic node, not an accidental participant",
         "Successful organisations consciously map, cultivate, and manage their networks rather "
         "than leaving relationships to chance."),
        ("Network equity matters",
         "Being a desirable partner is itself a competitive advantage. Invest in openness, "
         "track record, and complementarity."),
        ("The Marketing Network Canvas provides a framework",
         "Five clusters — Internal, Customer, Distribution, Supplier, and Innovation — "
         "provide a structured way to audit and plan the network."),
        ("60% of partnerships fail; governance is everything",
         "Partner selection, cultural fit, shared incentives, and active relationship management "
         "are what separates the 40% that succeed from the 60% that fail."),
        ("Marketers should lead the network agenda",
         "Their unique combination of customer insight, communication skills, and cross-functional "
         "reach makes marketers the natural architects of the organisation's alliance strategy."),
        ("Networking is a learnable skill at any scale",
         "From individual students to global multinationals, the network mindset can be developed "
         "deliberately. Start small, stay curious, and stay open."),
    ]

    for i, (title, body) in enumerate(takeaways, 1):
        row = Table(
            [[Paragraph(f"{i}", styles["toc_num"]),
              Paragraph(f"<b>{title}</b> — {body}", styles["body"])]],
            colWidths=[1.0*cm, 16.0*cm]
        )
        row.setStyle(TableStyle([
            ("VALIGN",        (0,0), (-1,-1), "TOP"),
            ("TOPPADDING",    (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("BACKGROUND",    (0,0), (-1,-1), HIGHLIGHT if i % 2 == 0 else white),
        ]))
        elems.append(row)

    elems.append(Spacer(1, 14))
    elems += quote_box("Erwin Knuyt — closing words",
        "Those companies who are able to make the right alliances first, they will succeed, "
        "they will benefit. There are going to be winners and losers in the networking economy. "
        "The ones who are more aware of it, take better advantage, can better manage their "
        "alliances — they're going to be the winners.", styles)

    elems.append(Spacer(1, 20))
    elems.append(HRFlowable(width="100%", thickness=1, color=DIVIDER))
    elems.append(Spacer(1, 6))
    elems.append(Paragraph(
        "Document compiled from the Module 3 podcast transcript — Marketing in a Network Economy &nbsp;|&nbsp; "
        "KU Leuven &nbsp;|&nbsp; Prof. Tine De Bock &amp; Erwin Knuyt",
        styles["footer"]
    ))

    return elems


def main():
    out = "/home/user/BabyPluto/Marketing_in_a_Network_Economy.pdf"
    doc = SimpleDocTemplate(
        out,
        pagesize=A4,
        leftMargin=2.5*cm,
        rightMargin=2.5*cm,
        topMargin=2.2*cm,
        bottomMargin=2.2*cm,
        title="Marketing in a Network Economy – Module 3",
        author="KU Leuven – Prof. Tine De Bock & Erwin Knuyt",
    )

    styles = build_styles()
    story  = []
    story += build_cover(styles)
    story += build_toc(styles)
    story += build_body(styles)

    doc.build(story)
    print(f"PDF written to: {out}")

if __name__ == "__main__":
    main()
