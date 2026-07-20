from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

INK = HexColor("#14161C")
COBALT = HexColor("#2F3EFF")
MUTED = HexColor("#4B4F58")

styles = getSampleStyleSheet()

name_style = ParagraphStyle("Name", parent=styles["Normal"], fontName="Helvetica-Bold",
                             fontSize=20, textColor=INK, spaceAfter=1, leading=23)
title_style = ParagraphStyle("Title", parent=styles["Normal"], fontName="Helvetica-Bold",
                              fontSize=11, textColor=COBALT, spaceAfter=4, leading=13)
contact_style = ParagraphStyle("Contact", parent=styles["Normal"], fontName="Helvetica",
                                fontSize=9, textColor=MUTED, spaceAfter=10, leading=12)
section_style = ParagraphStyle("Section", parent=styles["Normal"], fontName="Helvetica-Bold",
                                fontSize=10.5, textColor=INK, spaceBefore=10, spaceAfter=4,
                                leading=12, alignment=TA_LEFT)
body_style = ParagraphStyle("Body", parent=styles["Normal"], fontName="Helvetica",
                             fontSize=9.3, textColor=INK, spaceAfter=3, leading=12.5)
project_title_style = ParagraphStyle("ProjectTitle", parent=styles["Normal"], fontName="Helvetica-Bold",
                                      fontSize=9.8, textColor=INK, spaceBefore=6, spaceAfter=1, leading=12)
project_meta_style = ParagraphStyle("ProjectMeta", parent=styles["Normal"], fontName="Helvetica-Oblique",
                                     fontSize=8.5, textColor=MUTED, spaceAfter=2, leading=11)
bullet_style = ParagraphStyle("Bullet", parent=styles["Normal"], fontName="Helvetica",
                               fontSize=9, textColor=INK, spaceAfter=2, leading=12,
                               leftIndent=12, bulletIndent=0)
skill_cat_style = ParagraphStyle("SkillCat", parent=styles["Normal"], fontName="Helvetica-Bold",
                                  fontSize=9, textColor=INK, spaceAfter=1, leading=12)
skill_body_style = ParagraphStyle("SkillBody", parent=styles["Normal"], fontName="Helvetica",
                                   fontSize=9, textColor=MUTED, spaceAfter=4, leading=12)

doc = SimpleDocTemplate(
    "/home/claude/portfolio/Wesley_Kipkorir_Resume.pdf",
    pagesize=letter,
    topMargin=0.5 * inch, bottomMargin=0.5 * inch,
    leftMargin=0.65 * inch, rightMargin=0.65 * inch,
)

story = []

story.append(Paragraph("Wesley Kipkorir", name_style))
story.append(Paragraph("Backend &amp; AI Engineer", title_style))
story.append(Paragraph(
    "Nairobi, Kenya &nbsp;|&nbsp; wesley.kipkorir.kip@gmail.com &nbsp;|&nbsp; "
    "linkedin.com/in/wesley-kipkorir-46a568266 &nbsp;|&nbsp; x.com/worsley_KE",
    contact_style
))
story.append(HRFlowable(width="100%", thickness=1, color=INK, spaceAfter=6))

story.append(Paragraph("SUMMARY", section_style))
story.append(Paragraph(
    "Backend software engineer focused on practical, production-shaped systems: RAG pipelines, "
    "AI-assisted operational tooling, and integrations between modern web stacks and enterprise "
    "systems. Comfortable across the full stack, from database design and authentication to "
    "LLM tool-use design and deployment.",
    body_style
))

story.append(Paragraph("PROJECTS", section_style))

projects = [
    {
        "title": "LegacyLink AI — Modernization layer for Progress OpenEdge ERPs",
        "meta": "ABL, Python (FastAPI), JavaScript, SQLite/PostgreSQL, JWT auth",
        "bullets": [
            "Designed a three-tier architecture bridging a legacy OpenEdge/ABL ERP with a modern "
            "Python orchestration layer and a real-time web dashboard.",
            "Implemented the transactional outbox pattern in ABL triggers to enable change-data-capture "
            "without native database log access, consumed by a Python event pipeline for real-time "
            "anomaly alerts (stockouts, revenue drop-offs).",
            "Built a natural-language query engine constrained to an allow-listed set of parameterized "
            "query templates via forced LLM tool-use, eliminating prompt-injection-into-data-query as "
            "an attack surface by design.",
            "Implemented full role-based access control from scratch: JWT sessions, PBKDF2 password "
            "hashing, self-service signup with least-privilege defaults, and admin-managed role promotion.",
        ],
    },
    {
        "title": "Askforge — RAG-based document and web Q&A application",
        "meta": "Python, LangChain, ChromaDB, Multi-provider LLMs, Railway deployment",
        "bullets": [
            "Built and deployed a retrieval-augmented generation application supporting document and "
            "web-based question answering, with multi-provider LLM support.",
            "Diagnosed and resolved production deployment issues including Python version incompatibilities "
            "with native extensions and provider API authentication changes.",
        ],
    },
    {
        "title": "MwalimuPulse — AI-powered school management system (Kenyan CBC context)",
        "meta": "Node.js, Express, MongoDB/Mongoose, Next.js, Tailwind, OpenAI API",
        "bullets": [
            "Built a full-stack school management system with JWT-based role access control and "
            "AI-driven student risk scoring.",
            "Implemented a Next.js/Tailwind dashboard with live data visualizations for school administrators.",
        ],
    },
    {
        "title": "PostgreSQL School Management Database",
        "meta": "PostgreSQL, SQL (triggers, stored functions, views)",
        "bullets": [
            "Designed an 11-table relational schema with triggers, stored functions, and reporting views "
            "for a school administration domain.",
        ],
    },
]

for p in projects:
    story.append(Paragraph(p["title"], project_title_style))
    story.append(Paragraph(p["meta"], project_meta_style))
    for b in p["bullets"]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{b}", bullet_style))

story.append(Paragraph("SKILLS", section_style))
skills = [
    ("Languages", "Python, JavaScript/TypeScript, SQL, ABL (Progress OpenEdge)"),
    ("Backend & APIs", "FastAPI, Node.js/Express, REST API design, JWT authentication, PASOE/OpenEdge integration"),
    ("AI / LLM", "RAG pipelines, LangChain, ChromaDB, prompt/tool-use design, Anthropic &amp; OpenAI APIs"),
    ("Data", "PostgreSQL, MongoDB, SQLite, schema design, triggers &amp; stored procedures"),
    ("Frontend", "React/Next.js, Tailwind CSS, Recharts"),
    ("Tooling & Practices", "Docker, Git, CI-friendly project structure, Claude Code"),
]
for cat, body in skills:
    story.append(Paragraph(cat, skill_cat_style))
    story.append(Paragraph(body, skill_body_style))

doc.build(story)
print("resume built")
