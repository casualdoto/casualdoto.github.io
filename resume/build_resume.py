from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

import sys, os

def find_font(filename):
    search_dirs = []
    if sys.platform == 'win32':
        search_dirs += [
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts'),
            os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Microsoft', 'Windows', 'Fonts'),
        ]
    elif sys.platform == 'darwin':
        search_dirs += ['/Library/Fonts', '/System/Library/Fonts', os.path.expanduser('~/Library/Fonts')]
    else:
        search_dirs += ['/usr/share/fonts', '/usr/local/share/fonts', os.path.expanduser('~/.fonts')]
    for d in search_dirs:
        for root, _, files in os.walk(d):
            if filename in files:
                return os.path.join(root, filename)
    return None

FONT_MAP = {
    'DejaVu':         ['DejaVuSans.ttf',        'arial.ttf',   'Arial.ttf'],
    'DejaVu-Bold':    ['DejaVuSans-Bold.ttf',    'arialbd.ttf', 'Arial Bold.ttf'],
    'DejaVu-Oblique': ['DejaVuSans-Oblique.ttf', 'ariali.ttf',  'Arial Italic.ttf'],
}
for alias, candidates in FONT_MAP.items():
    for candidate in candidates:
        path = find_font(candidate)
        if path:
            pdfmetrics.registerFont(TTFont(alias, path))
            break
    else:
        print(f"WARNING: No font found for {alias}")

DARK     = colors.HexColor('#0F1923')
ACCENT   = colors.HexColor('#2563EB')
LIGHT_BG = colors.HexColor('#F0F4FF')
GRAY     = colors.HexColor('#64748B')
WHITE    = colors.white
GREEN    = colors.HexColor('#16A34A')

W, H = A4
MARGIN_L = 15*mm
MARGIN_R = 15*mm
MARGIN_T = 12*mm
MARGIN_B = 10*mm

doc = SimpleDocTemplate(
    'CV_Khrestianovskii_Daniil.pdf',
    pagesize=A4,
    leftMargin=MARGIN_L, rightMargin=MARGIN_R,
    topMargin=MARGIN_T,  bottomMargin=MARGIN_B,
)

def style(name, **kw):
    defaults = dict(fontName='DejaVu', fontSize=8.2, leading=11.5, textColor=DARK, spaceAfter=0, spaceBefore=0)
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)

s_name    = style('name',    fontName='DejaVu-Bold',    fontSize=20,  leading=24, textColor=DARK)
s_title   = style('title',   fontName='DejaVu',         fontSize=10,  leading=13, textColor=ACCENT)
s_contact = style('contact', fontSize=7.5, textColor=GRAY, leading=10)
s_section = style('section', fontName='DejaVu-Bold',    fontSize=8.5, leading=11, textColor=ACCENT, spaceBefore=4)
s_company = style('company', fontName='DejaVu-Bold',    fontSize=8.8, leading=11, textColor=DARK)
s_role    = style('role',    fontName='DejaVu-Oblique', fontSize=7.8, leading=10, textColor=GRAY)
s_bullet  = style('bullet',  fontSize=7.8, leading=11,  textColor=DARK, leftIndent=8)
s_body    = style('body',    fontSize=7.8, leading=11)
s_small   = style('small',   fontSize=7.2, textColor=GRAY, leading=10)

def section_header(title):
    return [
        Spacer(1, 1.5*mm),
        Paragraph(title.upper(), s_section),
        HRFlowable(width='100%', thickness=0.7, color=ACCENT, spaceAfter=2),
    ]

def achievement_bullet(text):
    return Paragraph(f'<font name="DejaVu-Bold" color="#16A34A">▲</font> {text}', s_bullet)

story = []

# ── HEADER ──────────────────────────────────────────────────────────────────
story.append(Paragraph('Daniil Khrestianovskii', s_name))
story.append(Paragraph('Golang Backend Developer', s_title))
story.append(Spacer(1, 1.5*mm))

contact_data = [
    [
        Paragraph('khrestyanovskii@gmail.com', s_contact),
        Paragraph('+7 952 267-09-41', s_contact),
        Paragraph('Saint Petersburg, Russia', s_contact),
    ],
    [
        Paragraph('<link href="https://github.com/casualdoto" color="#2563EB">github.com/casualdoto</link>', s_contact),
        Paragraph('<link href="https://casualdoto.github.io" color="#2563EB">casualdoto.github.io</link>', s_contact),
        Paragraph('English B2', s_contact),
    ]
]
t = Table(contact_data, colWidths=[(W - MARGIN_L - MARGIN_R)/3]*3)
t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('TOPPADDING', (0,0), (-1,-1), 1)]))
story.append(t)
story.append(Spacer(1, 1*mm))
story.append(HRFlowable(width='100%', thickness=1.5, color=ACCENT, spaceAfter=1))

# ── SUMMARY ──────────────────────────────────────────────────────────────────
story += section_header('Professional Summary')
story.append(Paragraph(
    'Backend engineer with 2+ years of production Go experience — from greenfield microservice architecture '
    'to real-time data pipelines. Built systems that won a <b>10k$ grant</b> '
    'and supported a pro esports team earning <b>$300K+ in prize money</b>. '
    'Owns the full backend lifecycle: API design, infra, security hardening, delivery.',
    s_body
))

# ── EXPERIENCE ──────────────────────────────────────────────────────────────
story += section_header('Experience')

# TE-Manager
story.append(Paragraph('TE-Manager — Task & Emotion Management App (Startup)', s_company))
story.append(Paragraph('Backend Engineer (Go / Python) · Mar 2024 – Present · Remote, Saint Petersburg', s_role))
story.append(Spacer(1, 1))

bullets_te = [
    ('Rewrote monolithic Flask API into Go + FastAPI microservices',
     'reduced p99 latency by ~40%, enabled independent deployments'),
    ('Implemented RS256 JWT auth with Redis token blacklist + device fingerprinting',
     'zero auth incidents; forced-logout from all devices in <100ms'),
    ('Integrated OAuth2 (Google, Yandex) and open API with scoped JWT tokens',
     'unlocked third-party integrations, reduced onboarding friction'),
    ('Set up Yandex Cloud infra from zero: VPC, Nginx, SSL, Object Storage, PostgreSQL',
     '99.9% uptime; infra cost under $100/mo'),
    ('Added Redis rate limiting + verification code caching',
     'blocked brute-force on signup, cut SMS costs by ~60%'),
    ('Containerised all services with Docker Compose; wrote Swagger docs for every endpoint',
     'reduced dev onboarding from days to hours'),
]
for main, result in bullets_te:
    story.append(Paragraph(f'• {main} <font color="#64748B">— {result}</font>', s_bullet))

story.append(Spacer(1, 1))
story.append(achievement_bullet('<b>Won 10k$ grant</b> — "Student Startup" competition (V round, 2024)'))
story.append(Spacer(1, 2.5*mm))

# Team Avulus
story.append(Paragraph('Team Avulus — Professional Dota 2 Team', s_company))
story.append(Paragraph('Data Engineer & Analyst · Oct 2024 – Apr 2026 · Remote', s_role))
story.append(Spacer(1, 1))

bullets_av = [
    ('Designed and deployed a Go web service aggregating data from 3 external APIs (OpenDota, STRATZ, Spectral.gg)',
     'coach access live analytics 24/7 instead of manually pulling spreadsheets'),
    ('Automated opponent scouting pipeline with Python (Pandas, NumPy, Matplotlib) + MySQL',
     'reduced pre-match prep time from ~4h to ~30 min'),
    ('Built automated analytics reports with interactive visualisations',
     'used by coach before every series esport events'),
]
for main, result in bullets_av:
    story.append(Paragraph(f'• {main} <font color="#64748B">— {result}</font>', s_bullet))

story.append(Spacer(1, 1))
story.append(achievement_bullet('<b>$300,000+ in prize money</b> earned since joining — 1st RES Regional Champions, 4th CCT Series 5, 5-6th ESL One Bangkok 2024, 3x qualifier champion'))

# ── SKILLS ──────────────────────────────────────────────────────────────────
story += section_header('Technical Skills')

skills_table_data = [
    [Paragraph('<b>Languages</b>',    s_body), Paragraph('Go (primary) · Python · SQL · Java (basic)', s_body)],
    [Paragraph('<b>Frameworks</b>',   s_body), Paragraph('FastAPI · Flask · Spring Boot · net/http', s_body)],
    [Paragraph('<b>Databases</b>',    s_body), Paragraph('PostgreSQL · MySQL · Redis', s_body)],
    [Paragraph('<b>Messaging</b>',    s_body), Paragraph('Apache Kafka · RabbitMQ', s_body)],
    [Paragraph('<b>Infra / DevOps</b>', s_body), Paragraph('Docker · Docker Compose · Nginx · Yandex Cloud · Linux · CI/CD · GitHub Actions', s_body)],
    [Paragraph('<b>Security</b>',     s_body), Paragraph('JWT (RS256/HS256) · OAuth2 · HTTPS/TLS · Token blacklisting · Rate limiting', s_body)],
    [Paragraph('<b>Tools</b>',        s_body), Paragraph('Git · Swagger/OpenAPI · SQLAlchemy · Pandas · NumPy · Matplotlib', s_body)],
]
st = Table(skills_table_data, colWidths=[33*mm, (W - MARGIN_L - MARGIN_R - 33*mm)])
st.setStyle(TableStyle([
    ('VALIGN',         (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING',     (0,0), (-1,-1), 2),
    ('BOTTOMPADDING',  (0,0), (-1,-1), 2),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [LIGHT_BG, WHITE]),
    ('LEFTPADDING',    (0,0), (-1,-1), 4),
]))
story.append(st)

# ── EDUCATION ──────────────────────────────────────────────────────────────────
story += section_header('Education')
story.append(Paragraph('Peter the Great St. Petersburg Polytechnic University', s_company))
story.append(Paragraph('B.Sc. Mathematical Software & Information Systems Administration · 2022 – 2026 (in progress)', s_role))
story.append(Paragraph('Core coursework: Databases, Discrete Mathematics, Programming, Systems Administration', s_small))

# ── LINKS ──────────────────────────────────────────────────────────────────
story += section_header('Links')
story.append(Paragraph(
    'Portfolio: <link href="https://casualdoto.github.io" color="#2563EB">casualdoto.github.io</link>   '
    'GitHub: <link href="https://github.com/casualdoto" color="#2563EB">github.com/casualdoto</link>   '
    'Telegram: <link href="https://t.me/dankhrestyan" color="#2563EB">@dankhrestyan</link>',
    s_body
))

doc.build(story)
print("Done!")