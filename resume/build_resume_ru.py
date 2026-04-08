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
    'CV_Хрестьяновский_Даниил.pdf',
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
story.append(Paragraph('Хрестьяновский Даниил Дмитриевич', s_name))
story.append(Paragraph('Golang Backend Developer', s_title))
story.append(Spacer(1, 1.5*mm))

contact_data = [
    [
        Paragraph('khrestyanovskii@gmail.com', s_contact),
        Paragraph('+7 952 267-09-41', s_contact),
        Paragraph('Санкт-Петербург, Россия', s_contact),
    ],
    [
        Paragraph('<link href="https://github.com/casualdoto" color="#2563EB">github.com/casualdoto</link>', s_contact),
        Paragraph('<link href="https://casualdoto.github.io" color="#2563EB">casualdoto.github.io</link>', s_contact),
        Paragraph('Английский — B2', s_contact),
    ]
]
t = Table(contact_data, colWidths=[(W - MARGIN_L - MARGIN_R)/3]*3)
t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('TOPPADDING', (0,0), (-1,-1), 1)]))
story.append(t)
story.append(Spacer(1, 1*mm))
story.append(HRFlowable(width='100%', thickness=1.5, color=ACCENT, spaceAfter=1))

# ── SUMMARY ──────────────────────────────────────────────────────────────────
story += section_header('О себе')
story.append(Paragraph(
    'Backend-разработчик с 2+ годами опыта на Go — от проектирования микросервисной архитектуры '
    'с нуля до production-систем с реальной нагрузкой. Участвовал в проектах, которые выиграли '
    '<b>грант 1 млн руб.</b> и обеспечили аналитическую поддержку команде с <b>$300K+ призовых</b>. '
    'Владею полным бэкенд-стеком: проектирование API, инфраструктура, безопасность, деплой.',
    s_body
))

# ── EXPERIENCE ──────────────────────────────────────────────────────────────
story += section_header('Опыт работы')

# TE-Manager
story.append(Paragraph('TE-Manager — мобильное приложение для управления задачами и эмоциями', s_company))
story.append(Paragraph('Backend-разработчик (Go / Python) · Март 2024 — по н.в. · Удалённо, Санкт-Петербург', s_role))
story.append(Spacer(1, 1))

bullets_te = [
    ('Переписал монолитный Flask API на связку Go + FastAPI микросервисы',
     'снизил p99 latency на ~40%, обеспечил независимый деплой сервисов'),
    ('Реализовал JWT-авторизацию на RS256 с Redis blacklist и device fingerprinting',
     'добился отсутствия инцидентов с авторизацией; принудительный выход со всех устройств за <100мс'),
    ('Интегрировал OAuth2 (Google, Яндекс) и сделал открытый API с JWT tokens',
     'открыл интеграции для сторонних клиентов, снизил порог входа для новых пользователей'),
    ('Развернул инфраструктуру Yandex Cloud с нуля: VPC, Nginx, SSL, Object Storage, PostgreSQL',
     'uptime 99.9%; стоимость инфраструктуры — менее $100/мес'),
    ('Добавил Redis rate limiting и кэширование кодов верификации',
     'защитил систему от брутфорса при регистрации, снизил расходы на SMS на ~60%'),
    ('Контейнеризировал все сервисы через Docker Compose; покрыл API документацией в Swagger',
     'сократил время онбординга нового разработчика с дней до часов'),
]
for main, result in bullets_te:
    story.append(Paragraph(f'• {main} <font color="#64748B">— {result}</font>', s_bullet))

story.append(Spacer(1, 1))
story.append(achievement_bullet('<b>Команда победила в конкурсе "Студенческий стартап" (V очередь, 2024)</b> — грант 1 000 000 руб.'))
story.append(Spacer(1, 2.5*mm))

# Team Avulus
story.append(Paragraph('Team Avulus — профессиональная Dota 2 организация', s_company))
story.append(Paragraph('Дата-инженер и аналитик · Октябрь 2024 — Апрель 2026 · Удалённо', s_role))
story.append(Spacer(1, 1))

bullets_av = [
    ('Разработал и задеплоил Go-сервис, агрегирующий данные из 3 внешних API (OpenDota, STRATZ, Spectral.gg)',
     'тренерский штаб получил доступ к аналитике 24/7 вместо ручного сбора данных'),
    ('Автоматизировал сбор данных по соперникам на Python (Pandas, NumPy, Matplotlib) + MySQL',
     'время подготовки к матчу сократилось с ~4 ч до ~30 мин'),
    ('Реализовал автоматическую генерацию аналитических отчётов с визуализацией',
     'используется тренером перед каждой игрой на турнирах'),
]
for main, result in bullets_av:
    story.append(Paragraph(f'• {main} <font color="#64748B">— {result}</font>', s_bullet))

story.append(Spacer(1, 1))
story.append(achievement_bullet('<b>$300 000+ призовых</b> с момента работы в команде — 1 место RES Regional Champions, 4 место CCT Series 5, 5–6 место ESL One Bangkok 2024, трехкратные победители квалификаций'))

# ── SKILLS ──────────────────────────────────────────────────────────────────
story += section_header('Технические навыки')

skills_table_data = [
    [Paragraph('<b>Языки</b>',         s_body), Paragraph('Go (основной) · Python · SQL · Java (базово)', s_body)],
    [Paragraph('<b>Фреймворки</b>',    s_body), Paragraph('FastAPI · Flask · Spring Boot · net/http', s_body)],
    [Paragraph('<b>Базы данных</b>',   s_body), Paragraph('PostgreSQL · MySQL · Redis', s_body)],
    [Paragraph('<b>Брокеры сообщений</b>',       s_body), Paragraph('Apache Kafka · RabbitMQ', s_body)],
    [Paragraph('<b>Инфраструктура / DevOps</b>',s_body), Paragraph('Docker · Docker Compose · Nginx · Yandex Cloud · Linux · CI/CD · GitHub Actions', s_body)],
    [Paragraph('<b>Безопасность</b>',  s_body), Paragraph('JWT (RS256/HS256) · OAuth2 · HTTPS/TLS · Token blacklisting · Rate limiting', s_body)],
    [Paragraph('<b>Инструменты</b>',   s_body), Paragraph('Git · Swagger/OpenAPI · SQLAlchemy · Pandas · NumPy · Matplotlib', s_body)],
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
story += section_header('Образование')
story.append(Paragraph('Санкт-Петербургский политехнический университет Петра Великого', s_company))
story.append(Paragraph('Бакалавриат · Математическое обеспечение и администрирование информационных систем · 2022 – 2026 (в процессе)', s_role))
story.append(Paragraph('Основные курсы: Базы данных, Дискретная математика, Программирование, Системное администрирование', s_small))

# ── LINKS ──────────────────────────────────────────────────────────────────
story += section_header('Ссылки')
story.append(Paragraph(
    'Портфолио: <link href="https://casualdoto.github.io" color="#2563EB">casualdoto.github.io</link>   '
    'GitHub: <link href="https://github.com/casualdoto" color="#2563EB">github.com/casualdoto</link>   '
    'Telegram: <link href="https://t.me/dankhrestyan" color="#2563EB">@dankhrestyan</link>',
    s_body
))

doc.build(story)
print("Done!")