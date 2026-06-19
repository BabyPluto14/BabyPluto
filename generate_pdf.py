from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    PageBreak, Table, TableStyle
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import Flowable

# ── colour palette ──────────────────────────────────────────────────────────
PRIMARY   = colors.HexColor("#1a3a5c")   # dark navy
ACCENT    = colors.HexColor("#2d7fc1")   # mid blue
LIGHT_BG  = colors.HexColor("#f0f5fb")   # very light blue
RULE_COL  = colors.HexColor("#2d7fc1")

# ── paragraph styles ────────────────────────────────────────────────────────
def make_styles():
    base = getSampleStyleSheet()

    cover_title = ParagraphStyle(
        "CoverTitle",
        parent=base["Title"],
        fontSize=30,
        leading=38,
        textColor=colors.white,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
    )
    cover_sub = ParagraphStyle(
        "CoverSub",
        parent=base["Normal"],
        fontSize=14,
        leading=20,
        textColor=colors.HexColor("#cce0f5"),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName="Helvetica",
    )
    module_heading = ParagraphStyle(
        "ModuleHeading",
        parent=base["Heading1"],
        fontSize=20,
        leading=26,
        textColor=PRIMARY,
        spaceBefore=18,
        spaceAfter=6,
        fontName="Helvetica-Bold",
        borderPad=4,
    )
    clip_heading = ParagraphStyle(
        "ClipHeading",
        parent=base["Heading2"],
        fontSize=15,
        leading=20,
        textColor=ACCENT,
        spaceBefore=22,
        spaceAfter=8,
        fontName="Helvetica-Bold",
    )
    body = ParagraphStyle(
        "Body",
        parent=base["Normal"],
        fontSize=10.5,
        leading=16,
        textColor=colors.HexColor("#1a1a1a"),
        spaceAfter=9,
        alignment=TA_JUSTIFY,
        fontName="Helvetica",
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=body,
        leftIndent=18,
        bulletIndent=6,
        spaceAfter=4,
    )
    intro_box = ParagraphStyle(
        "IntroBox",
        parent=body,
        backColor=LIGHT_BG,
        borderColor=ACCENT,
        borderWidth=1,
        borderPad=8,
        spaceAfter=12,
    )
    label = ParagraphStyle(
        "Label",
        parent=base["Normal"],
        fontSize=8.5,
        textColor=colors.HexColor("#666666"),
        fontName="Helvetica-Oblique",
        spaceAfter=2,
    )
    return dict(
        cover_title=cover_title,
        cover_sub=cover_sub,
        module_heading=module_heading,
        clip_heading=clip_heading,
        body=body,
        bullet=bullet,
        intro_box=intro_box,
        label=label,
    )


# ── coloured banner flowable for cover ──────────────────────────────────────
class ColorBanner(Flowable):
    def __init__(self, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, stroke=0, fill=1)


# ── header / footer callbacks ────────────────────────────────────────────────
def on_later_pages(canv, doc):
    canv.saveState()
    # header bar
    canv.setFillColor(PRIMARY)
    canv.rect(0, A4[1] - 1.4*cm, A4[0], 1.4*cm, stroke=0, fill=1)
    canv.setFont("Helvetica-Bold", 9)
    canv.setFillColor(colors.white)
    canv.drawString(2*cm, A4[1] - 0.95*cm,
                    "Module 6: Customer Experience Management")
    canv.drawRightString(A4[0] - 2*cm, A4[1] - 0.95*cm,
                         "Transcript of Knowledge Clips")
    # footer
    canv.setFillColor(ACCENT)
    canv.rect(0, 0, A4[0], 0.9*cm, stroke=0, fill=1)
    canv.setFont("Helvetica", 8)
    canv.setFillColor(colors.white)
    canv.drawCentredString(A4[0]/2, 0.28*cm, f"Page {doc.page}")
    canv.restoreState()

def on_first_page(canv, doc):
    # no header/footer on cover
    pass


# ── helper: section divider rule ─────────────────────────────────────────────
def section_rule():
    return HRFlowable(width="100%", thickness=2, color=ACCENT,
                      spaceAfter=6, spaceBefore=2)


# ── build content ────────────────────────────────────────────────────────────
def build_story(doc_path):
    raw = Document(doc_path)
    paras = [p.text for p in raw.paragraphs]

    styles = make_styles()
    story  = []

    # ── COVER PAGE ────────────────────────────────────────────────────────────
    W = A4[0]
    # dark navy banner
    story.append(ColorBanner(W, 4*cm, PRIMARY))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Module 6", styles["cover_sub"]))
    story.append(Paragraph(
        "Customer Experience<br/>Management",
        styles["cover_title"]
    ))
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph(
        "Transcript of Knowledge Clips",
        styles["cover_sub"]
    ))
    story.append(Spacer(1, 0.6*cm))
    story.append(HRFlowable(width="60%", thickness=1,
                             color=colors.HexColor("#2d7fc1"),
                             spaceAfter=14))

    # clip list
    clips = [
        ("1", "Intro", "05'31\""),
        ("2", "What is customer experience?", "17'58\""),
        ("3", "Customer experience management", "12'27\""),
        ("4", "Case 1 – The Hello Kitty Jet", "06'59\""),
        ("5", "Case 2 – Tomorrowland", "04'47\""),
        ("6", "Customer journey mapping", "12'35\""),
    ]
    tbl_data = [["#", "Knowledge Clip", "Duration"]] + \
               [[c[0], c[1], c[2]] for c in clips]

    tbl = Table(tbl_data, colWidths=[1.2*cm, 11*cm, 2.8*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,0),  PRIMARY),
        ("TEXTCOLOR",   (0,0), (-1,0),  colors.white),
        ("FONTNAME",    (0,0), (-1,0),  "Helvetica-Bold"),
        ("FONTSIZE",    (0,0), (-1,0),  10),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",    (0,1), (-1,-1), 10),
        ("ALIGN",       (0,0), (0,-1),  "CENTER"),
        ("ALIGN",       (2,0), (2,-1),  "CENTER"),
        ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",  (0,0), (-1,-1), 7),
        ("BOTTOMPADDING",(0,0), (-1,-1), 7),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("GRID",        (0,0), (-1,-1), 0.4, colors.HexColor("#c0cfe0")),
        ("BOX",         (0,0), (-1,-1), 1,   ACCENT),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.8*cm))

    # intro note
    intro_note = (
        "This document contains the verbatim transcript of all six knowledge "
        "clips for Module 6 (Customer Experience Management) as presented on "
        "the Toledo e-learning platform. The clips are authored by "
        "<b>Prof. Dr. Tine De Bock</b>, building on course material developed "
        "by Prof. Dr. Yves Van Vaerenbergh."
    )
    story.append(Paragraph(intro_note, styles["intro_box"]))
    story.append(PageBreak())

    # ── TRANSCRIPT SECTIONS ───────────────────────────────────────────────────
    # Map paragraph indices to sections
    sections = [
        # (section_number, title, duration, start_para_idx, end_para_idx)
        (1, "Intro",                        "05'31\"",  30,  47),
        (2, "What is customer experience?", "17'58\"",  48,  95),
        (3, "Customer experience management","12'27\"", 96, 137),
        (4, "Case 1: The Hello Kitty Jet",  "06'59\"", 138, 187),
        (5, "Case 2: Tomorrowland",         "04'47\"", 188, 205),
        (6, "Customer journey mapping",     "12'35\"", 206, 263),
    ]

    for sec_num, sec_title, duration, start, end in sections:
        # section heading
        story.append(section_rule())
        story.append(Paragraph(
            f"{sec_num}. {sec_title}",
            styles["clip_heading"]
        ))
        story.append(Paragraph(
            f"Duration: {duration}",
            styles["label"]
        ))
        story.append(Spacer(1, 0.15*cm))

        # body paragraphs for this section
        for p in paras[start:end+1]:
            text = p.strip()
            if not text:
                continue
            story.append(Paragraph(text, styles["body"]))

        story.append(Spacer(1, 0.5*cm))

    return story


def main():
    doc_path = (
        "/root/.claude/uploads/"
        "ee9fd49b-90dc-5b82-b6da-570bddaaebd3/"
        "7fb0b22e-Transcript_clips_1.docx"
    )
    out_path = "/home/user/BabyPluto/Module6_Customer_Experience_Management.pdf"

    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=2.2*cm, rightMargin=2.2*cm,
        topMargin=2.2*cm, bottomMargin=2*cm,
        title="Module 6 – Customer Experience Management",
        author="Prof. Dr. Tine De Bock",
        subject="Transcript of Knowledge Clips",
    )

    story = build_story(doc_path)

    doc.build(
        story,
        onFirstPage=on_first_page,
        onLaterPages=on_later_pages,
    )
    print(f"PDF saved to: {out_path}")


if __name__ == "__main__":
    main()
