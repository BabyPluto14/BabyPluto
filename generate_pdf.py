from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    KeepTogether, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

PAGE_W, PAGE_H = A4
MARGIN = 2.2 * cm

def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles['cover_title'] = ParagraphStyle(
        'cover_title',
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=colors.HexColor('#1a3a5c'),
        alignment=TA_CENTER,
        spaceAfter=12,
    )
    styles['cover_sub'] = ParagraphStyle(
        'cover_sub',
        fontName='Helvetica',
        fontSize=14,
        leading=20,
        textColor=colors.HexColor('#4a6fa5'),
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    styles['cover_detail'] = ParagraphStyle(
        'cover_detail',
        fontName='Helvetica-Oblique',
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#555555'),
        alignment=TA_CENTER,
        spaceAfter=6,
    )

    styles['section_title'] = ParagraphStyle(
        'section_title',
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#1a3a5c'),
        spaceBefore=20,
        spaceAfter=8,
        borderPad=4,
    )
    styles['subsection_title'] = ParagraphStyle(
        'subsection_title',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#2c5f8a'),
        spaceBefore=14,
        spaceAfter=6,
    )
    styles['body'] = ParagraphStyle(
        'body',
        fontName='Helvetica',
        fontSize=10.5,
        leading=16,
        textColor=colors.HexColor('#222222'),
        alignment=TA_JUSTIFY,
        spaceAfter=8,
    )
    styles['bullet'] = ParagraphStyle(
        'bullet',
        fontName='Helvetica',
        fontSize=10.5,
        leading=16,
        textColor=colors.HexColor('#222222'),
        alignment=TA_LEFT,
        leftIndent=18,
        spaceAfter=4,
        bulletIndent=4,
    )
    styles['speaker_tdb'] = ParagraphStyle(
        'speaker_tdb',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#1a6b3a'),
        spaceBefore=10,
        spaceAfter=2,
    )
    styles['speaker_cc'] = ParagraphStyle(
        'speaker_cc',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#7b2d8b'),
        spaceBefore=10,
        spaceAfter=2,
    )
    styles['speech'] = ParagraphStyle(
        'speech',
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        textColor=colors.HexColor('#333333'),
        alignment=TA_JUSTIFY,
        leftIndent=14,
        spaceAfter=4,
    )
    styles['note'] = ParagraphStyle(
        'note',
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#666666'),
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )
    styles['interlude'] = ParagraphStyle(
        'interlude',
        fontName='Helvetica-BoldOblique',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#995500'),
        alignment=TA_CENTER,
        spaceBefore=10,
        spaceAfter=10,
    )

    return styles


def hr(color='#cccccc', thickness=0.8):
    return HRFlowable(width='100%', thickness=thickness, color=colors.HexColor(color), spaceAfter=6)


def build_story(styles):
    story = []

    # ── COVER ──────────────────────────────────────────────────────────────
    story.append(Spacer(1, 3 * cm))
    story.append(Paragraph("Module 10", styles['cover_sub']))
    story.append(Paragraph("Leadership &amp; Marketing", styles['cover_title']))
    story.append(hr('#1a3a5c', 2))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("Podcast Transcript – Detailed Explanations", styles['cover_sub']))
    story.append(Spacer(1, 0.6 * cm))
    story.append(Paragraph(
        "A conversation between<br/>"
        "<b>Prof. Dr. Tine De Bock</b> (TDB) &amp; <b>Prof. Dr. Christel Claeys</b> (CC)<br/>"
        "Department of Marketing, KU Leuven",
        styles['cover_detail']
    ))
    story.append(Spacer(1, 1.2 * cm))
    story.append(Paragraph(
        "This document provides a complete, detailed record of the Module 10 podcast "
        "transcript, organised by theme. The transcript forms part of the <i>examinable</i> "
        "course material. Concepts explained verbally in the podcast are preserved in full "
        "so that you can study them at your own pace.",
        styles['note']
    ))
    story.append(PageBreak())

    # ── SECTION 1: INTRODUCTION ─────────────────────────────────────────────
    story.append(Paragraph("1. About This Podcast", styles['section_title']))
    story.append(hr())
    story.append(Paragraph(
        "Module 10 of the course focuses on <b>Leadership (Skills) &amp; Marketing</b>. "
        "The central resource for this module is a podcast recorded in Dutch by "
        "<b>Prof. Dr. Tine De Bock</b> (professor of marketing, KU Leuven) together with "
        "subject-matter expert <b>Prof. Dr. Christel Claeys</b>, who holds a PhD in Marketing "
        "(consumer psychology) and has been affiliated with KU Leuven since 2001. "
        "This document is the full English translation of that podcast.",
        styles['body']
    ))
    story.append(Paragraph(
        "<b>Speaker key:</b><br/>"
        "&#8226; <b>TDB</b> – Tine De Bock<br/>"
        "&#8226; <b>CC</b> – Christel Claeys",
        styles['note']
    ))

    # ── SECTION 2: KEY CONCEPTS EXPLAINED ─────────────────────────────────
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph("2. Key Concepts – Thematic Overview", styles['section_title']))
    story.append(hr())
    story.append(Paragraph(
        "Before the full transcript, this section summarises the central themes "
        "discussed in the podcast to give you an orientation.",
        styles['body']
    ))

    concepts = [
        (
            "2.1 What Are Leadership / Soft Skills in Marketing?",
            [
                "Also called <i>soft skills</i>, <i>human skills</i>, or <i>power skills</i>. "
                "The label 'soft' can be misleading – these skills are anything but trivial.",

                "At the core sits <b>communication</b>, described as the 'queen (or king) of soft skills.' "
                "Communication runs through every interaction and every discipline.",

                "We all 'wear our own pair of glasses': we approach others through the lens of our "
                "own background, assumptions and experiences, which makes communication inherently complex.",

                "Historically associated with HRM and therefore undervalued in marketing curricula; "
                "only in recent years have marketing programmes begun to embed them systematically.",
            ]
        ),
        (
            "2.2 Why Are Soft Skills Relevant to Marketing?",
            [
                "Marketing is a <i>philosophy</i> that must flow through every layer of an organisation – "
                "not just advertising or promotions.",

                "CMOs and marketers need soft skills to <b>bring colleagues and other departments on board</b>, "
                "to champion the customer perspective internally.",

                "Even in an increasingly digital world, human connection remains crucial: "
                "consumers still crave human contact, and chatbots cannot fully replace that.",

                "Soft skills create a direct link to <b>employer branding</b>: the way people inside the "
                "organisation communicate shapes how the brand is perceived externally by job seekers "
                "and customers alike.",
            ]
        ),
        (
            "2.3 The Framework: Intrapersonal vs. Interpersonal Skills",
            [
                "<b>Intrapersonal skills</b> (within the person): Before you can lead others, you must be "
                "able to lead yourself. This starts with <i>self-knowledge</i> – knowing your strengths, "
                "weaknesses, values, triggers and blind spots. Self-awareness is 'the beginning of all wisdom.'",

                "Self-knowledge grows throughout life; it deepens with age and experience and is developed "
                "both alone (reflection) and in interaction with others (feedback from colleagues, friends, mentors).",

                "<b>Interpersonal skills</b> (between people): Interactions one-on-one or in small groups – "
                "internally with colleagues and managers, externally with customers and other stakeholders.",

                "The two skill sets are <i>interdependent</i>: intrapersonal insight provides the vocabulary "
                "and empathy needed for interpersonal effectiveness. You cannot have one without the other.",

                "Communication acts as the central thread that ties both sets together.",
            ]
        ),
        (
            "2.4 Active Listening",
            [
                "Everyone assumes they are a good listener – yet genuinely <i>active</i> listening is one of "
                "the hardest skills to master.",

                "<b>Passive vs. active listening</b>: Simply keeping quiet while the other person speaks is "
                "a start but is not enough. In passive mode we 'hear' words; in active mode we truly "
                "<i>listen</i> – to content, feeling and intent.",

                "While someone else speaks, most of us are simultaneously thinking about our own response, "
                "managing our self-image, or worrying about something else entirely. This 'mental noise' "
                "blocks genuine understanding.",

                "The antidote is <b>letting go</b> (symbolised by the first musical interlude, "
                "<i>Let It Go</i> from Frozen) – releasing your own internal dialogue and focusing "
                "fully on the other person.",

                "<b>Marketing application</b>: Asking what the customer truly needs before pitching a "
                "product. The pen-selling exercise illustrates this perfectly – launching into a sales "
                "pitch without first asking questions guarantees misalignment. The customer's needs must "
                "be discovered, not assumed.",

                "People who feel unheard become frustrated, unhappy or angry. Being listened to is a "
                "universal human need, yet it is often neglected even in professional service contexts "
                "(illustrated by the estate-agent example).",

                "On AI &amp; chatbots: a chatbot is free from the mental noise humans experience, "
                "so it can in some ways 'listen' more attentively. However, it lacks empathy and the "
                "ability to respond to emotion – the human dimension remains indispensable.",
            ]
        ),
        (
            "2.5 Giving Feedback",
            [
                "Unlike listening, most people <i>know</i> that giving feedback is difficult. "
                "Research shows that many leaders systematically avoid giving negative feedback – "
                "they soften it, delay it, or omit it entirely.",

                "Core misconception: feedback is equated with criticism. In reality, well-delivered "
                "feedback is a gift; it is one of the most effective tools for growth.",

                "<b>Key principle</b>: Be <i>firm on content</i> (dare to name the issue, 'name the "
                "elephant in the room') but <i>gentle on the relationship</i>. Every communication "
                "has two dimensions: the content (what is said) and the relational dimension (how it is said).",

                "<b>Descriptive vs. evaluative language</b>: Avoid 'you always…' or 'you never…' – "
                "these are evaluative and immediately trigger defensiveness. Instead, stick strictly to "
                "observable, concrete facts: what did you see or hear, when, and how often?",

                "<b>Speak from 'I'</b>: Express the impact of the behaviour on you using 'I-statements' "
                "('When X happens, I feel Y') rather than 'you-statements' that label or blame.",

                "Additional principles: be <i>specific</i>, focus on the <i>problem</i> not the person, "
                "and always speak about <i>changeable</i> behaviour.",

                "<b>Marketing application</b>: Customer-facing employees (receptionists, service staff) "
                "must also be trained in feedback skills – they need to handle complaints gracefully "
                "and, when necessary, deliver difficult messages to assertive or misbehaving customers. "
                "Handling a complaint well can prevent it from becoming a public negative review on "
                "social media, which again links back to reputation and brand image.",
            ]
        ),
        (
            "2.6 Coaching Conversation Skills",
            [
                "Active listening and feedback giving are often elements within a broader conversation "
                "rather than standalone moments. The 'meta-skill' that frames them is <b>coaching "
                "conversation technique</b>.",

                "<b>Solution-oriented vs. problem-oriented</b>: In a business context, conversations "
                "should focus on the future and on solutions – not dwell on past problems. "
                "Problem-focused deep-dives are the domain of therapists, not of managers or marketers.",

                "A leader or manager is a coach in certain situations, but not only a coach – "
                "they also guide, instruct, and make decisions.",

                "<b>Marketing application</b>: Coaching skills fit naturally with "
                "<i>service-dominant logic</i>, where value is co-created with the customer in "
                "interaction, rather than embedded in a product handed over (goods-dominant logic). "
                "Guiding a customer through a complaint or complex need requires exactly this "
                "solution-oriented conversational approach.",
            ]
        ),
    ]

    for title, bullets in concepts:
        story.append(Paragraph(title, styles['subsection_title']))
        for b in bullets:
            story.append(Paragraph(f"&#8226; {b}", styles['bullet']))
        story.append(Spacer(1, 0.2 * cm))

    story.append(PageBreak())

    # ── SECTION 3: FULL TRANSCRIPT ─────────────────────────────────────────
    story.append(Paragraph("3. Full Transcript", styles['section_title']))
    story.append(hr())
    story.append(Paragraph(
        "The complete English translation of the podcast is presented below, "
        "organised in the order it was recorded. Musical interludes are indicated "
        "in the flow of the conversation.",
        styles['body']
    ))
    story.append(Spacer(1, 0.3 * cm))

    transcript = [
        ('TDB', "Good morning, good afternoon, good evening, or maybe even good night. Welcome to this podcast. My name is Tine De Bock, I am a professor of marketing at KU Leuven. In this podcast, I would like to take you along into the fascinating world of marketing, and today we will focus on a theme that is very close to my heart: leadership skills for marketers. And for that, I have a wonderful guest with me today."),
        ('CC', "Hello Tine."),
        ('TDB', "Let me briefly introduce you to our listeners, Christel. Christel obtained a PhD in Marketing, more specifically in consumer psychology, and has been affiliated with the Department of Marketing at KU Leuven since 2001. From the very beginning, her focus has been on the human side of marketing. She teaches leadership skills to students of the Master of Marketing programme as well as to executive education participants. A very warm welcome, Christel."),
        ('CC', "Thank you, Tine, and also thank you for the invitation and the introduction. I actually find it quite nice—and a little challenging—to try this."),
        ('TDB', "Christel, I also asked you to select two songs as a kind of musical intermezzo for this podcast. Each song connects very well with one of the messages you will soon share in this conversation, but let's save those for later. I suggest we really get started now, if that's okay with you."),
        ('CC', "Absolutely."),
        ('TDB', "As I mentioned earlier, this podcast revolves around leadership skills for marketers. I think I have a fairly logical opening question, Christel. What exactly do we mean by leadership skills in marketing?"),
        ('CC', "Leadership skills—indeed, quite a mouthful. I can already say that there are many alternative terms circulating that refer to more or less the same thing. Think of soft skills, human skills. Some people even talk about power skills, because the term 'soft skills' may sound a bit too soft, as if these skills are less important than hard skills—technical skills such as SEO, data analysis, and so on. That would be a misconception. Let me start by saying that I place communication at the very core of all these skills: it's actually the queen—or king, if you prefer—of soft skills. Everything runs through communication. But at the same time, I already want to add that communication is not as straightforward as it seems."),
        ('TDB', "So communication is not as self-evident as we might think, if I understand you correctly. Why is that? Why is communication less straightforward than it appears?"),
        ('CC', "There are several reasons. I'll already mention a few. First of all, we all approach communication from our own angle, from a different perspective. I often say: we all wear our own pair of glasses. We tend to approach our conversation partner as if they have exactly the same background as we do, with the same assumptions, the same references, the same experiences. And of course, that's not the case. That is already one of the reasons why communication is more complex than it seems. Fortunately, this is something you can work on."),
        ('TDB', "Absolutely. When you explain it like that, it becomes clear that communication is not necessarily an easy task. As I mentioned earlier, Christel, this podcast is about the wonderful world of marketing. It is somewhat my goal to show listeners that marketing is so much more than advertising, or perhaps even the purely digital side of things. Marketing is genuinely a philosophy, and it has to flow through every layer and every cell of the organisation. And so I'm wondering: why is it that soft skills have been somewhat ignored in the context of marketing?"),
        ('CC', "Tine, that's a very interesting question, and I would actually like to reframe it: why has it been ignored for so long? Why is it only in recent years that we have included this in our curriculum? Soft skills are often associated with HRM, as if managers-in-training from other areas of business administration don't need them. That is a misconception. And in marketing, specifically, I would like to make the following argument: marketing is indeed a philosophy. And if you want that philosophy to flow through the entire organisation, then you—as a marketer, as a CMO—actually need to convince all those other people of that vision. And for that, you need leadership skills. You need the right tools to bring people on board."),
        ('TDB', "I think that already makes a very compelling case for putting these skills more firmly on the marketing agenda. They may sometimes be overshadowed, but they certainly deserve more attention. That brings me to a perhaps slightly provocative question, Christel. Digitalization and digital markets are increasingly important. Does the rise of digitalization perhaps make these soft skills less relevant?"),
        ('CC', "I understand that question. At first glance, you might indeed think that everything is becoming digital—tasks are automated, interactions with customers often happen via chatbots or other digital tools. That is efficient. But we should also ask ourselves: is that really what consumers want? Is that always the right approach? We still have a strong need for human contact. And within the organisation as well, the human side is at least as important. So I would rather argue that these skills remain absolutely essential, precisely in a digital environment where there is a risk of losing that human touch."),
        ('TDB', "Absolutely, I fully agree. Marketing is a philosophy that should flow through every layer of the organization. And indeed, you need soft skills to bring everyone on board and to make clear that the CMO plays a crucial role."),
        ('CC', "Exactly."),
        ('TDB', "A strong argument, and certainly something we as marketers can work with, I think. Maybe I'll build a little bridge here—one that might seem a bit far-fetched to the listener at first. When you explain all of this, a light goes on for me and I start thinking about employer branding. And then I think: oh, maybe this isn't such a strange connection after all. Do you see a link between soft skills and employer branding?"),
        ('CC', "Indeed. I hadn't really thought about it myself yet, but employer branding is indeed about developing that employer brand externally, so that job seekers feel attracted to you, and so that potentially customers can also think: wow, this must be a good company, so they probably offer good products or good service. And the way in which employees communicate—and behave, and are treated—that radiates outward. That influences that employer brand. So yes, there is definitely a link."),
        ('TDB', "I find it very nice to see how soft skills, perhaps surprisingly, connect seamlessly with everything in marketing. They seem like an underlying thread, a kind of foundation you simply cannot miss, neatly linking all the different disciplines within the marketing field. That really convinces me of the importance of these skills. Maybe we should discuss how you personally teach them or approach them as a framework?"),
        ('CC', "Tine, I can really only tell you how I approach this myself—that's what it is, not the way. For me, for instance, it is very important to distinguish between intrapersonal and interpersonal skills. In addition, I use communication as a kind of central core skill. It actually runs through everything I just said: both the intrapersonal and the interpersonal dimension."),
        ('TDB', "So communication is the queen—or king—of soft skills, and of the skills we are discussing today. And then there are intrapersonal and interpersonal skills. Perhaps we should start with the one I am least familiar with—and I suspect the listener might be as well—which is intrapersonal skills. What exactly are those?"),
        ('CC', "That is quite a mouthful. Intrapersonal—so, within the person—is essentially a difficult way of saying that before we can lead others, we must first be able to lead ourselves. At its core, this means strongly investing in self-knowledge: knowing who you are, what your strengths and weaknesses are, what your values are, where your triggers lie, what makes you who you are. And I immediately want to add: knowing ourselves also means knowing what impact we have on others, what kind of image we project."),
        ('TDB', "This strongly reminds me of something my father always used to say to me: Tine, self-knowledge—or self-awareness, I might say—is the beginning of all wisdom. That fits very well here. And yet it seems incredibly difficult to me. I can imagine it being very enriching to grow to a higher level of self-awareness, but it also seems like a long road."),
        ('CC', "It probably sounds more difficult than it is. By that I don't mean it is easy—it is hard work—but it is within everyone's reach. In that sense, it is not inaccessible. Your father is absolutely right. I have to agree with him."),
        ('TDB', "I'll be sure to pass that on to him."),
        ('CC', "Self-awareness, self-knowledge, really is the start of everything. And of course, it is a continuous process. Let me be clear: at the age of twenty, you do not have the same level of self-knowledge as someone who is perhaps fifty-plus. That may be one of the few advantages of getting somewhat older."),
        ('TDB', "But Christel, does that mean this is something you have to do entirely on your own? Because it sounds quite isolating—being so focused on yourself and on reflection. Quite intense, I imagine."),
        ('CC', "That's a very good question, and I was just about to say something about that. There is indeed a part of working on yourself that you do alone. But as human beings, we don't live in isolation—we don't live on an island. And to truly get to know ourselves, we need other people: colleagues, friends, sometimes even competitors—people who give us feedback and hold up a mirror to us."),
        ('TDB', "When you put it like that… Earlier, you talked about intrapersonal skills, which have become much clearer now. You also mentioned interpersonal skills. 'Inter' meaning between people. Have I understood it correctly that intrapersonal skills are necessary for interpersonal skills to truly come into their own?"),
        ('CC', "You've understood that perfectly."),
        ('TDB', "I was listening carefully."),
        ('CC', "I couldn't have said it better myself. Absolutely. By gaining more insight into ourselves, we gain that language, that vocabulary and those ideas to also better understand others. When we understand others better, we may begin to appreciate them more, and instead of rejecting differences, we can see them as enriching. It really is a chain."),
        ('TDB', "So we have intrapersonal skills and interpersonal skills. We've established that they cannot exist without each other—you need one for the other to function well. But so far, we haven't gone into much detail yet about interpersonal skills themselves. What kinds of skills are we talking about exactly?"),
        ('CC', "Interpersonal— the word says it all—means between people. This can be one-on-one, one-on-two, or in a group. In my course, I focus exclusively on one-on-one or small-group interactions, so I leave group dynamics aside. In a business context, these skills apply internally, with colleagues and managers, as well as externally, with customers and other stakeholders. The specific skills I focus on in my course are: active listening, giving feedback, and coaching conversation skills."),
        ('TDB', "Maybe I'll bring in my personal life here for a moment. I sometimes feel, Christel, that I'm not always such a good listener. Perhaps others feel the same way. That's probably why I'm particularly interested in listening—and why maybe we should start with active listening as one of those interpersonal skills."),
        ('CC', "Listening is perhaps the prototypical example of a soft skill everyone thinks they have mastered, that seems easy. And yet it isn't that simple when you really want to listen."),
        ('TDB', "Why is that? I always think: if I just keep my mouth shut and listen, I'm doing fine. Or am I mistaken?"),
        ('CC', "It is certainly a start—to not speak yourself—but very often we listen passively. We hear what the other person says, but we don't truly listen. To illustrate that, I'd like to do a small exercise. May I test whether you are a good listener, Tine?"),
        ('TDB', "Oh dear. Yes, that's fine. I hope it won't be too embarrassing, but sure."),
        ('CC', "It's a learning exercise. Okay, Tine, I'm going to read a short text. Here it comes. 'Modern managers spend a large part of their time actively solving small and large problems between individual employees and within teams. TNO Labour has calculated that annually between 60,000 and 100,000 people are confronted with a serious conflict at work. The costs to the employer amount to approximately €2,000 per employee per day. In total, that means that work-related conflicts in the Netherlands alone cost approximately 2.3 billion euros per year.' I'll stop there."),
        ('TDB', "Now I'm curious."),
        ('CC', "Here is your question: what went through your mind while you were listening? What did you feel? What did you think?"),
        ('TDB', "To be completely honest, it was a bit chaotic because there was so much information. A lot of numbers I was trying to remember, and I was wondering: okay, what's coming next, what will I have to do after this? Will I answer correctly? A bit of exam stress resurfacing, to be honest."),
        ('CC', "Yes—and what does that show? I completely understand, and thank you for participating so openly in the exercise. It shows that we are very often already occupied with ourselves while listening. Your response is perfectly recognizable. While someone else is speaking, we are already thinking: what will I say next? Or we are evaluating: do I agree with this? Or, as in your case, we are anxious about what will follow. That mental occupation—that noise in our head—often prevents us from truly listening to what the other person is saying. And that's what we need to practice: letting go. Letting go of yourself, making space for the other person."),
        ('TDB', "What I take away most from this is 'letting go.' And that brings us very naturally to the first song. The first song, Christel, that you chose as a kind of musical intermezzo—to let everything settle for a moment, all the information you've shared. I suggest we listen to the song first and then continue."),
        ('INTERLUDE', "1st MUSICAL INTERLUDE — \"Let It Go\" (Disney's Frozen)\nhttps://www.youtube.com/watch?v=moSFlvxnbgk"),
        ('TDB', "That was Let It Go from the well-known Disney film Frozen. Christel, why did you choose this song? It seems rather straightforward."),
        ('CC', "Let It Go captures very well what we should all be doing: let go—especially let go of yourself—and listen and focus on the other person."),
        ('TDB', "Staying with active listening for a moment, Christel: it's harder than one might think. I do feel that it's something you can train, that you can actually get better at. This podcast is, of course, also about marketing, so I would like to ask the following: if we translate active listening very specifically to the marketing field and all that entails, what kind of valuable applications do you see?"),
        ('CC', "Tine, I think you're really pointing at the question: how do we use this externally? How do we apply it in interactions with customers? So I'll focus on that aspect and pay a bit less attention to the internal relevance. Now, customers—how can we help our customers better if we actively listen? Well, it starts with asking what the customer really needs. Not launching immediately into your pitch or your product. That immediately makes me want to do a small exercise with you, if you're willing."),
        ('TDB', "Absolutely. I am your guinea pig at your service."),
        ('CC', "Indeed. Look, Tine, I see that you're holding a pen. I'll take something very simple as a test. The idea is that you try to sell me that pen. Try to sell it to me in such a way that I really can't help but say: Tine, this is a pen I truly want."),
        ('TDB', "Okay, I'll do my best. Hello, dear customer—whose name I don't actually know yet—welcome to this wonderful pen store. I have a beautiful pen for you here. As you can see, it fits very well in the hand, but perhaps most importantly—let me try to be original—it's a pen that will last a lifetime. For years and years you'll be able to write beautifully with it, and you'll never have to buy another pen."),
        ('CC', "I am not interested in your pen."),
        ('TDB', "Oh dear."),
        ('CC', "I don't want a pen that lasts a lifetime at all. I want a pen I can replace regularly, because that's actually fun: a different colour, a different design. So Tine, despite your nice sales pitch, where exactly did things go wrong? You didn't ask what I, as a customer, find important in a pen. So you started from your own assumptions, your own perspective—your own pair of glasses—and you missed what the customer actually wants. And this is of course a very simple example, but it does show the principle very clearly. In marketing, the same applies: you have to start from the customer's perspective. So: first listen, first ask questions, and then you'll know how to connect with the customer."),
        ('TDB', "When you put it like that, Christel, I have to say it sounds extremely familiar. Perhaps I should share an example from my own life, not so long ago. A few months ago, I had the idea of having my house appraised, because I was considering selling it. So I invited an estate agent to come over—and to be honest, before I knew it, she had pressed her card into my hand and was out the door. She hadn't asked a single question. Not a single question about why I was considering selling, what my situation was, what I needed. I felt completely unheard. And at that point, I thought: I want nothing to do with this estate agent."),
        ('CC', "You're actually pointing to an important emotional dimension that I didn't explicitly mention yet. Look at what it does to you when you're not listened to. Nobody likes that. People immediately feel frustrated, perhaps unhappy, angry—depending on the situation. People want to be heard, and yet it is something that we often find difficult to do ourselves. That is also an important observation."),
        ('TDB', "I follow your reasoning, but I'm going to put my daring shoes on again, Christel. We've already talked about digital marketing becoming increasingly important, and we can assume that more and more organizations will use chatbots to answer these kinds of questions. Then I think: that chatbot will not have any self-focused mental noise. So does a chatbot listen better than a human being?"),
        ('CC', "Indeed—an interesting question, or observation. Look, I have to agree with you to a certain extent. When I reflect on it myself, I think: a chatbot is not plagued by the same mental noise we experience—the distractions, the self-presentation, the other things on our mind. In that sense, yes, it could process the information of the conversation more objectively and more fully. But—and this is an important 'but'—a chatbot does not have empathy. A chatbot cannot respond to the emotional dimension of a conversation in the way that a human being can. And precisely in situations where the customer is frustrated, angry, or emotionally involved—which is often the case in a service context—that human dimension is indispensable."),
        ('TDB', "It's certainly one of the hot topics in marketing at the moment—this whole artificial intelligence versus human intelligence debate. I don't think we've seen the end of it yet. It's a fascinating discussion, and I think we are both very curious to see where it will lead. That actually brings us to the second musical intermezzo—the second song you chose, Christel."),
        ('INTERLUDE', "2nd MUSICAL INTERLUDE — \"Listen Up\" by Balthazar"),
        ('TDB', "That was the band Balthazar with the beautiful Listen Up. Christel, I know—it may seem rather straightforward—but why did you choose this song?"),
        ('CC', "Well, I'm personally quite a fan of Balthazar? And in the end, it's all about listening, so the choice wasn't very difficult."),
        ('TDB', "That's true. Now, beyond active listening—or alongside active listening as a skill, which we've discussed quite extensively in this podcast—there are several other interpersonal skills that we really shouldn't overlook or forget in the context of marketing and leadership skills within marketing. You mentioned giving feedback. Can you tell us more about that?"),
        ('CC', "Unlike listening—where everyone tends to think they are good listeners—this is not the case for giving feedback. Through experience alone, most people already know that giving good, constructive feedback is not easy. When we shift to a business context, research shows that many leaders, department heads, and managers systematically avoid giving feedback. Why? Because they are afraid. They avoid it, try to soften it, don't dare to put their finger on the sore spot. And it's difficult between colleagues as well. Most people don't like giving what they perceive as negative feedback to a colleague or employee."),
        ('TDB', "Yes—why, exactly?"),
        ('CC', "They avoid it, try to soften it, don't dare to put their finger on the sore spot. And it's difficult between colleagues as well. Most people don't like giving what they perceive as negative feedback to a colleague or employee."),
        ('TDB', "Is that because they think there will be negative consequences attached to it?"),
        ('CC', "Very often, yes. People are afraid that feedback will be perceived as criticism—and that's a big misconception. Feedback is often equated with criticism, and people fear the reaction of the recipient: will this person get angry, disappointed? Then they think: I still have to work with this person. So they avoid it, or they wrap the message in so much cotton wool that the real message gets completely lost. That is of course a shame, because well-delivered feedback is actually a gift. It gives someone the opportunity to grow, to do things differently. But there are models and frameworks that can really help with this."),
        ('TDB', "Could you tell us a bit more about those models? That actually really interests me."),
        ('CC', "Let me put it this way. At the core of giving feedback lies one essential principle: be firm on content—dare to say what is really going on, name the elephant in the room—but be gentle on the relationship. Every communication, as I may have said earlier, has two dimensions: what is said, and the relationship between the people involved. You should never let the content suffer for the sake of the relationship. But at the same time, in the way you bring your message, you must respect and protect the relationship. That is a fundamental starting point. And now I want to add a second principle: work descriptively."),
        ('TDB', "So how should you do it instead?"),
        ('CC', "How should you do it? First of all, consider that if I were to say: 'Tine, you always interrupt me,' you would probably immediately become defensive. You might say: 'That's not true—the last two times I wasn't late.' And then escalation begins. So staying descriptive means sticking strictly to facts—what you actually observed, heard, or saw—and not sliding into evaluations or judgments. That's the second principle."),
        ('TDB', "Yes, that's exactly what I was about to add. Facts are one thing, but sometimes what bothers you is more of a feeling—how someone communicates with you. That can be hard to translate into facts. But I find it very valuable that you say: you should also add how it makes you feel."),
        ('CC', "Of course, there is actually more behind this. I am trying to explain that principle now. We then really arrive at the model—this is actually already part of the model. I say something that I hear or see. But I do need to correct you briefly on one point, namely the idea that you cannot say what you feel. You absolutely can—and in fact, you should. But you have to be precise about what exactly you feel. You cannot say 'I don't like your communication'—that is still too abstract."),
        ('TDB', "Really?"),
        ('CC', "Yes, because you've just done it again yourself—and this actually shows very nicely how we tend to communicate immediately at a fairly abstract level. You are essentially saying: I don't like your communication. But then you have to ask yourself: what exactly is bothering me? Is it because the person interrupts me? Is it the tone of voice? Is it the word choice? So you also have to describe your own feelings concretely and specifically."),
        ('TDB', "That really is an eye-opener. Yes, that's true."),
        ('CC', "So you have to force yourself—and of course, you need to prepare for this—and then—perhaps I'm getting ahead of myself, and I don't think I can explain all those models within this time frame—but that descriptive starting point is embedded in a broader model, where the core really is: speak from 'I.' Use 'I-statements': when X happens, I feel Y. And then add: what you need, what you would prefer. This shifts the conversation away from blame and toward dialogue."),
        ('TDB', "Yes, absolutely."),
        ('CC', "So that is one important principle. And again, we talked about awareness, consciousness, at the beginning. Is it difficult? No. But you do need to reach insight and awareness. There are other principles as well, such as: you need to be specific, and you need to focus on the problem, not on the person. And you should only give feedback on things the other person can actually change. You wouldn't give someone feedback on their height, for instance."),
        ('TDB', "Yes, unfortunately, because I think you also gain so many benefits from this in your personal life. But bringing it back to marketing—because this podcast is about marketing—I indeed think: giving feedback to your own employees or colleagues is already difficult enough. But what about other stakeholders? Customers? What about the interface with customers?"),
        ('CC', "I agree with you. I think that internally, the usefulness of good feedback has definitely been proven. Everyone also appreciates constructive feedback. But what about customers? Let me turn the question around. Should we give feedback to customers? I'm now speaking as we, as marketers. Yes, undeniably—and in a very specific situation that I find extremely relevant: customer complaints. We give feedback—reactive—when a customer comes to us with a complaint, perhaps in a somewhat less pleasant manner. So we have to be able to receive that feedback, the complaint, and process it. But we also have to be able to guide the customer in a professional way."),
        ('TDB', "Yes absolutely."),
        ('CC', "The customer gives us feedback. Depending on the customer, that might not always be done in a pleasant way. And here we are again dealing with what I mentioned earlier. The customer brings us something whose content can be very valuable—because we can work with a complaint—but the way it is said can be very challenging to deal with. I'll give you a concrete example: an employee at a hotel reception desk who receives an angry customer—a customer who feels they were not properly informed about the facilities. Well, that employee needs to be able to deal with that well: listen carefully, process the complaint professionally, and perhaps also give feedback on the customer's behaviour if they are being overly assertive or aggressive."),
        ('TDB', "I think we reflect on that too little indeed. Your employees—for example, that receptionist—are often the only interaction customers have with your brand or your organization. They really need to be well trained in these skills. We're talking about leadership skills, and they may not be leaders in the traditional sense, but they do need to be strong communicators."),
        ('CC', "Indeed. Being trained in giving feedback should really be a requirement, because sometimes, as an employee, you also have to deliver less pleasant messages to a customer who may be misbehaving or overly assertive. That has to be possible."),
        ('TDB', "Yes, absolutely. I can also imagine that this allows you to put out small fires. If you approach a difficult customer in the right way, that also means they are less likely to post negative messages about your company, for example on social media. This again shows how everything is connected within the marketing domain."),
        ('CC', "Yes, these are all topics that are covered. I already mentioned that we shouldn't see these skills in isolation—active listening, giving feedback. They are often elements within a broader conversation. I therefore conclude with what I would call the broader conversation, which I refer to as coaching conversation skills or coaching techniques."),
        ('TDB', "Could you give an example of solution-oriented thinking, and of why it's better to avoid a problem-oriented approach?"),
        ('CC', "In a business context, we are actually not trained to deal with problem-focused approaches—that's really the domain of therapists. I would also like to say—because this is a concern that often comes up—that a leader, a department head, or anyone who manages people is not only a coach. They have many different roles. But in certain situations, coaching skills are extremely valuable. And the core principle of that is: focus on solutions, not on problems. Look forward, not backward. Focus on what is possible, not on what went wrong."),
        ('TDB', "Okay, that's very useful to know. And maybe as a closing question: do you also see applications for coaching in relationships with customers?"),
        ('CC', "Yes, absolutely. I already hinted at this earlier with the hotel example, even though I framed it through feedback. You can easily extend that to coaching conversation skills. The receiver—the receptionist—will benefit greatly from such techniques to guide the conversation properly. Beyond complaints, think also of advisory conversations: a financial advisor guiding a client through a complex decision, or a personal shopper helping a customer identify what they truly need. These are all coaching-type conversations: listening, asking the right questions, co-creating a solution."),
        ('TDB', "Now that you explain it like this, Christel, I also feel that coaching skills are a much better fit with service-dominant logic than with goods-dominant logic."),
        ('CC', "Absolutely, Tine."),
        ('TDB', "It's really beautiful to see how everything links together. Christel, may I thank you very warmly for taking the time for this very pleasant conversation and, above all, for the many insights. I personally gained a lot from it, and I'm convinced that our listeners will as well. I truly believe these insights will enrich not only their professional lives, but also their personal lives. So thank you very much."),
        ('CC', "You're very welcome."),
    ]

    for speaker, text in transcript:
        if speaker == 'TDB':
            story.append(Paragraph("TDB — Tine De Bock:", styles['speaker_tdb']))
            story.append(Paragraph(text, styles['speech']))
        elif speaker == 'CC':
            story.append(Paragraph("CC — Christel Claeys:", styles['speaker_cc']))
            story.append(Paragraph(text, styles['speech']))
        elif speaker == 'INTERLUDE':
            story.append(Spacer(1, 0.3 * cm))
            story.append(hr('#995500', 1))
            story.append(Paragraph(text, styles['interlude']))
            story.append(hr('#995500', 1))
            story.append(Spacer(1, 0.3 * cm))

    return story


def main():
    output_path = "/home/user/BabyPluto/Module10_Leadership_Marketing_Transcript.pdf"
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="Module 10: Leadership & Marketing – Podcast Transcript",
        author="KU Leuven – Tine De Bock & Christel Claeys",
    )
    styles = build_styles()
    story = build_story(styles)
    doc.build(story)
    print(f"PDF created: {output_path}")


if __name__ == "__main__":
    main()
