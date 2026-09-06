#let data = yaml("resume.yaml")
#let lang = sys.inputs.at("lang", default: "ru")
#assert(lang in ("ru", "en"), message: "Supported languages: ru, en")
#let tr(value) = value.at(lang)
#let accent = rgb("#203e60")
#set document(title: tr(data.name) + " | " + data.title, author: tr(data.name))
#set page(paper: "a4", margin: 15mm)
#set text(font: "Noto Sans", size: 10.5pt, lang: lang, fill: rgb("#202630"))
#set par(leading: 0.48em, spacing: 0.6em)
#set list(indent: 0pt, body-indent: 3.5mm, spacing: 0.4em)
#set heading(numbering: none)
#show heading.where(level: 1): it => block(above: 4mm, below: 2mm,
  stack(dir: ttb, spacing: 1.5mm,
    text(size: 10pt, weight: "bold", fill: accent, upper(it.body)),
    line(length: 100%, stroke: 0.5pt + rgb("#bac6d2")),
  )
)
#let section(ru, en) = heading(level: 1, if lang == "ru" { ru } else { en })
#let date(value) = {
  if value == none { return if lang == "ru" { "наст. время" } else { "Present" } }
  let parts = value.split("-")
  let months = if lang == "ru" {
    ("янв.", "фев.", "март", "апр.", "май", "июнь", "июль", "авг.", "сент.", "окт.", "нояб.", "дек.")
  } else { ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec") }
  months.at(int(parts.at(1)) - 1) + " " + parts.at(0)
}

#text(size: 23pt, weight: "bold", tr(data.name))
#v(-1mm)
#text(size: 12pt, fill: accent, data.title)
#v(1mm)
#tr(data.location)
#linebreak()
#for (i, contact) in data.contacts.enumerate() {
  if i == 3 { linebreak() } else if i > 0 { [ · ] }
  link(contact.url, contact.text)
}

#section("Профиль", "Profile")
#tr(data.summary)

#section("Опыт работы", "Experience")
#for (index, job) in data.experience.enumerate() {
  if index > 0 { v(3mm) }
  block(breakable: false, above: 1.7mm)[
    #text(weight: "bold", job.company) #h(1fr) #text(size: 10pt, date(job.start) + " - " + date(job.end))
    #linebreak()
    #text(weight: "bold", tr(job.role))#if job.remote { [ · #if lang == "ru" { "Удалённо" } else { "Remote" }] }
    #linebreak()
    #text(fill: accent, tr(job.description))
    #v(0.5mm)
    #list(..job.bullets.map(item => [
      #tr(item)
      #if "note" in item {
        linebreak()
        text(size: 9.5pt, style: "italic", fill: accent, tr(item.note))
      }
    ]))
    #if "note" in job { v(2mm); block(tr(job.note)) }
  ]
}

#section("Ключевые навыки", "Technical skills")
#for skill in data.skills [
  #text(weight: "bold", tr(skill.label) + ": ")#skill.value#linebreak()
]
#data.languages.at(lang)

#section("Образование", "Education")
#for (index, school) in data.education.enumerate() {
  if index > 0 { v(2mm) }
  block(breakable: false, above: 1.6mm)[
    #text(weight: "bold", tr(school.institution))
    #linebreak()
    #tr(school.degree) · #school.start - #school.end
    #linebreak()
    #tr(school.program)#if lang == "ru" { [ · #school.code] }
    #if "status" in school { linebreak(); text(fill: accent, tr(school.status)) }
  ]
}
