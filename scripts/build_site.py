#!/usr/bin/env python3


import datetime
import hashlib
import html
import json
import re
from pathlib import Path

import content as C

ROOT = Path(__file__).resolve().parent.parent
TODAY = datetime.date.today()
LANGS = ("fr", "en")


def asset_version():
    h = hashlib.sha1()
    for p in ("css/styles.css", "css/fonts.css", "css/script.js"):
        h.update((ROOT / p).read_bytes())
    return h.hexdigest()[:10]


VERSION = asset_version()


def t(value, lang):
    if isinstance(value, dict):
        return value[lang]
    return value


def e(value, lang="fr"):
    return html.escape(t(value, lang) or "", quote=True)


MONTHS = {
    "fr": ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."],
    "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
}
UI = {
    "fr": {
        "present": "aujourd'hui", "year": ("an", "ans"), "month": ("mois", "mois"),
        "skip": "Aller au contenu principal", "menu": "Menu", "close": "Fermer le menu",
        "cv": "Télécharger le CV", "cv_aria": "Télécharger mon CV au format PDF",
        "nav_label": "Navigation principale", "lang_label": "Read this page in English",
        "other_lang": "EN", "new_tab": "(nouvel onglet)",
        "footer_tag": "Développeur full-stack à Antananarivo. Site fait à la main, sans framework.",
        "footer_nav": "Pages", "footer_social": "Réseaux", "breadcrumb_home": "Accueil",
        "github": "Code source", "details": "Voir les détails",
    },
    "en": {
        "present": "present", "year": ("yr", "yrs"), "month": ("mo", "mos"),
        "skip": "Skip to main content", "menu": "Menu", "close": "Close menu",
        "cv": "Download CV", "cv_aria": "Download my CV as a PDF",
        "nav_label": "Main navigation", "lang_label": "Lire cette page en français",
        "other_lang": "FR", "new_tab": "(new tab)",
        "footer_tag": "Full-stack developer in Antananarivo. Handcrafted site, no framework.",
        "footer_nav": "Pages", "footer_social": "Elsewhere", "breadcrumb_home": "Home",
        "github": "Source code", "details": "View details",
    },
}


def month_label(ym, lang):
    y, m = ym
    return f"{MONTHS[lang][m - 1]} {y}"


def months_between(start, end):
    end = end or (TODAY.year, TODAY.month)
    return (end[0] - start[0]) * 12 + end[1] - start[1] + 1


def duration(start, end, lang):
    n = months_between(start, end)
    y, m = divmod(n, 12)
    yw, mw = UI[lang]["year"], UI[lang]["month"]
    parts = []
    if y:
        parts.append(f"{y} {yw[y > 1]}")
    if m:
        parts.append(f"{m} {mw[m > 1]}")
    return " ".join(parts)


def period(start, end, lang, with_duration=True):
    a = month_label(start, lang)
    b = month_label(end, lang) if end else UI[lang]["present"]
    text = a if end == start else f"{a} – {b}"
    if with_duration:
        text += f" · {duration(start, end, lang)}"
    return text


PAGES = {
    "home": {"fr": "/", "en": "/en/"},
    "experience": {"fr": "/experiences/", "en": "/en/experience/"},
    "involvement": {"fr": "/engagements/", "en": "/en/involvement/"},
    "projects": {"fr": "/projets/", "en": "/en/projects/"},
    "skills": {"fr": "/competences/", "en": "/en/skills/"},
    "about": {"fr": "/a-propos/", "en": "/en/about/"},
    "contact": {"fr": "/contact/", "en": "/en/contact/"},
}
NAV_LABELS = {
    "home": {"fr": "Accueil", "en": "Home"},
    "experience": {"fr": "Expériences", "en": "Experience"},
    "involvement": {"fr": "Engagements", "en": "Involvement"},
    "projects": {"fr": "Projets", "en": "Projects"},
    "skills": {"fr": "Compétences", "en": "Skills"},
    "about": {"fr": "À propos", "en": "About"},
    "contact": {"fr": "Contact", "en": "Contact"},
}
META = {
    "home": {
        "title": {"fr": "Tolotra Anthony RANDRIAMBOLOLONA (Arthinez) — Développeur Full-Stack",
                  "en": "Tolotra Anthony RANDRIAMBOLOLONA (Arthinez) — Full-Stack Developer"},
        "desc": {"fr": "Portfolio de Tolotra Anthony RANDRIAMBOLOLONA (Arthinez), développeur full-stack à Antananarivo, étudiant à 42 : TypeScript, Next.js, Docker, Keycloak, C et C++.",
                 "en": "Portfolio of Tolotra Anthony RANDRIAMBOLOLONA (Arthinez), full-stack developer in Antananarivo and 42 student: TypeScript, Next.js, Docker, Keycloak, C and C++."},
    },
    "experience": {
        "title": {"fr": "Expériences professionnelles — Hango, Yas Madagascar, 42 | Arthinez",
                  "en": "Professional experience — Hango, Yas Madagascar, 42 | Arthinez"},
        "desc": {"fr": "Parcours professionnel de Tolotra Anthony : développeur front-end puis junior chez Hango, stage intégration chez Yas Madagascar (Keycloak) et cursus à 42 Antananarivo.",
                 "en": "Tolotra Anthony's professional path: front-end then junior developer at Hango, integration internship at Yas Madagascar (Keycloak) and the 42 Antananarivo curriculum."},
    },
    "involvement": {
        "title": {"fr": "Engagements associatifs — BDE 42, formations, événements | Arthinez",
                  "en": "Involvement — 42 Student Council, training, events | Arthinez"},
        "desc": {"fr": "Trésorier et responsable communication du BDE de 42 Antananarivo, organisation d'événements et formations numériques pour Parklife et Grandir Dignement Madagascar.",
                 "en": "Treasurer and communications manager of the 42 Antananarivo Student Council, event organization and digital training for Parklife and Grandir Dignement Madagascar."},
    },
    "projects": {
        "title": {"fr": "Projets techniques — Transcendence, Webserv, Inception | Arthinez",
                  "en": "Technical projects — Transcendence, Webserv, Inception | Arthinez"},
        "desc": {"fr": "Projets de Tolotra Anthony : authentification Keycloak, plateforme web TypeScript, serveur HTTP en C++, infrastructure Docker et hackathons à 42 Antananarivo.",
                 "en": "Projects by Tolotra Anthony: Keycloak authentication, TypeScript web platform, C++ HTTP server, Docker infrastructure and hackathons at 42 Antananarivo."},
    },
    "skills": {
        "title": {"fr": "Compétences — TypeScript, Docker, Keycloak, C/C++ | Arthinez",
                  "en": "Skills — TypeScript, Docker, Keycloak, C/C++ | Arthinez"},
        "desc": {"fr": "Technologies utilisées par Tolotra Anthony : TypeScript, Next.js, Fastify, Prisma, PostgreSQL, Docker, Keycloak, C, C++ et Linux, avec des débuts sur Kubernetes.",
                 "en": "Technologies used by Tolotra Anthony: TypeScript, Next.js, Fastify, Prisma, PostgreSQL, Docker, Keycloak, C, C++ and Linux, and early steps with Kubernetes."},
    },
    "about": {
        "title": {"fr": "À propos — parcours et formation de Tolotra Anthony | Arthinez",
                  "en": "About — background and education of Tolotra Anthony | Arthinez"},
        "desc": {"fr": "Parcours de Tolotra Anthony RANDRIAMBOLOLONA : 42 Antananarivo depuis 2024, certification AXIAN University, intérêt pour la cybersécurité, le cloud et la data science.",
                 "en": "Background of Tolotra Anthony RANDRIAMBOLOLONA: 42 Antananarivo since 2024, AXIAN University certification, interest in cybersecurity, cloud and data science."},
    },
    "contact": {
        "title": {"fr": "Contact — Tolotra Anthony RANDRIAMBOLOLONA | Arthinez",
                  "en": "Contact — Tolotra Anthony RANDRIAMBOLOLONA | Arthinez"},
        "desc": {"fr": "Contacter Tolotra Anthony (Arthinez), développeur full-stack à Antananarivo : e-mail, LinkedIn, GitHub et CV à télécharger.",
                 "en": "Get in touch with Tolotra Anthony (Arthinez), full-stack developer in Antananarivo: email, LinkedIn, GitHub and downloadable CV."},
    },
}


def url(page, lang):
    return PAGES[page][lang]


def abs_url(path):
    return C.SITE_URL + path


STROKE_ICONS = {
    "arrow-right": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "external": '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    "download": '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M3 13h18"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
    "code": '<path d="m8 7-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
    "server": '<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01"/>',
    "box": '<path d="M21 8 12 3 3 8v8l9 5 9-5V8z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3z"/><path d="m9 12 2 2 4-4"/>',
    "cloud": '<path d="M7 18a5 5 0 0 1-.6-9.96A6 6 0 0 1 18 9a4.5 4.5 0 0 1-.5 9H7z"/>',
    "cpu": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 10h4v4h-4zM9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "trophy": '<path d="M8 4h8v5a4 4 0 0 1-8 0V4zM8 6H4v1a4 4 0 0 0 4 4M16 6h4v1a4 4 0 0 1-4 4M12 13v4M8 21h8M9 17h6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "cap": '<path d="m2 9 10-5 10 5-10 5L2 9z"/><path d="M6 11v5c3 2 9 2 12 0v-5M22 9v6"/>',
    "mic": '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 7 5-3 5 3-1.5-7"/>',
    "database": '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v6c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 11v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/>',
    "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
}
BRAND_ICONS = {
    "github": ('0 0 24 24', '<path d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.52-1.33-1.28-1.69-1.28-1.69-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.19 1.76 1.19 1.03 1.76 2.69 1.25 3.35.96.1-.75.4-1.25.73-1.54-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.29 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.78 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.8 1.19 1.83 1.19 3.09 0 4.42-2.7 5.39-5.26 5.68.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5z"/>'),
    "linkedin": ('0 0 24 24', '<path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/>'),
    "facebook": ('0 0 24 24', '<path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07c0 6.02 4.39 11.02 10.13 11.93v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.96.93-1.96 1.88v2.26h3.33l-.53 3.49h-2.8V24C19.61 23.09 24 18.09 24 12.07z"/>'),
}


def sprite():
    out = ['<svg xmlns="http://www.w3.org/2000/svg" class="sprite" aria-hidden="true" focusable="false">']
    for name, body in STROKE_ICONS.items():
        out.append(f'<symbol id="i-{name}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                   f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{body}</symbol>')
    for name, (vb, body) in BRAND_ICONS.items():
        out.append(f'<symbol id="i-{name}" viewBox="{vb}" fill="currentColor">{body}</symbol>')
    out.append("</svg>")
    return "".join(out)


def icon(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true" focusable="false"><use href="#i-{name}"></use></svg>'


def picture(img, lang, cls="", eager=False, sizes="(min-width: 960px) 40vw, 100vw"):
    srcset = ", ".join(f"/assets/img/{img['src']}-{w}.webp {w}w" for w in img["sizes"])
    largest = img["sizes"][-1]
    h = round(img["h"] * largest / img["w"])
    style = f' style="object-position:{img["pos"]}"' if img.get("pos") else ""
    loading = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    return (f'<img class="{cls}" src="/assets/img/{img["src"]}-{largest}.webp" srcset="{srcset}" '
            f'sizes="{sizes}" width="{largest}" height="{h}" alt="{e(img["alt"], lang)}" '
            f'{loading} decoding="async"{style}>')


def placeholder(icon_name, tone="warm"):
       return (f'<div class="media-ph media-ph--{tone}" aria-hidden="true">'
            f'<span class="media-ph__badge">{icon(icon_name, "media-ph__icon")}</span></div>')


def tags(items, lang, cls="tags", label=None):
    if not items:
        return ""
    note = "en apprentissage" if lang == "fr" else "learning"

    def item(i):
        if t(i, lang) in C.LEARNING:
            return f'<li class="is-learning">{e(i, lang)} <span class="learning">{note}</span></li>'
        return f"<li>{e(i, lang)}</li>"
    lis = "".join(item(i) for i in items)
    label = label or ("Technologies et compétences" if lang == "fr" else "Technologies and skills")
    return f'<ul class="{cls}" aria-label="{label}">{lis}</ul>'


def ext_link(href, label, lang, cls="link-arrow", ico="external"):
    return (f'<a class="{cls}" href="{href}" target="_blank" rel="noopener noreferrer">'
            f'{label}<span class="visually-hidden"> {UI[lang]["new_tab"]}</span>{icon(ico)}</a>')


def section_head(eyebrow, title, intro=None, center=False, hid=None, level=2):
    cls = "section-head section-head--center" if center else "section-head"
    hid_attr = f' id="{hid}"' if hid else ""
    intro_html = f'<p class="section-head__intro">{intro}</p>' if intro else ""
    return (f'<div class="{cls}"><p class="eyebrow">{eyebrow}</p>'
            f'<h{level} class="section-title"{hid_attr}>{title}</h{level}>{intro_html}</div>')


def page_hero(lang, page, eyebrow, title, intro):
    crumbs = (f'<nav class="breadcrumb" aria-label="{"Fil d’Ariane" if lang == "fr" else "Breadcrumb"}"><ol>'
              f'<li><a href="{url("home", lang)}">{UI[lang]["breadcrumb_home"]}</a></li>'
              f'<li aria-current="page">{e(NAV_LABELS[page], lang)}</li></ol></nav>')
    return (f'<section class="page-hero"><div class="container">{crumbs}'
            f'<p class="eyebrow">{eyebrow}</p><h1 class="page-hero__title">{title}</h1>'
            f'<p class="page-hero__intro">{intro}</p></div></section>')


def role_item(title, when, summary, lang, highlights=(), note=None, link=None):
    hl = ""
    if highlights:
        hl = '<ul class="checklist">' + "".join(f"<li>{e(h, lang)}</li>" for h in highlights) + "</ul>"
    if note:
        label, _, rest = t(note, lang).partition(" : " if lang == "fr" else ": ")
        hl += f'<p class="role__note"><strong>{html.escape(label)}</strong> — {html.escape(rest)}</p>'
    if link:
        hl += ext_link(link, ("Voir la plateforme " if lang == "fr" else "Visit the platform ")
                       + link.removeprefix("https://"), lang, cls="link-arrow role__link")
    body = f"<p>{e(summary, lang)}</p>" if summary else ""
    return (f'<li class="role"><div class="role__head"><h4 class="role__title">{e(title, lang)}</h4>'
            f'<span class="role__date">{icon("calendar")}{html.escape(when)}</span></div>{body}{hl}</li>')


def timeline_card(lang, *, anchor, org, kind, when, media, roles, tag_items=(), extra=""):
        return (f'<article class="xp-card reveal-item" id="{anchor}">'
            f'<div class="xp-card__media">{media}</div>'
            f'<div class="xp-card__body">'
            f'<div class="xp-card__meta"><span class="badge">{e(kind, lang)}</span>'
            f'<span class="xp-card__when">{html.escape(when)}</span></div>'
            f'<h3 class="xp-card__org">{e(org, lang)}</h3>'
            f'<ol class="roles">{"".join(roles)}</ol>{extra}'
            f'{tags(tag_items, lang)}</div></article>')


def project_card(p, lang):
    if p.get("image"):
        media = picture(p["image"], lang, "card__img", sizes="(min-width: 960px) 360px, 100vw")
    else:
        media = placeholder(p["icon"], "cool" if p["cat"] == "school" else "warm")
    links = ""
    for kind, href in p["links"]:
        label = UI[lang]["github"] if kind == "github" else UI[lang]["details"]
        ico = "github" if kind == "github" else "external"
        links += ext_link(href, f'{label}', lang, ico=ico)
    card_links = f'<div class="card__links">{links}</div>' if links else ""
    return (f'<article class="card project reveal-item" id="{p["id"]}" data-cat="{p["cat"]}">'
            f'<div class="card__media">{media}</div><div class="card__body">'
            f'<p class="card__kicker">{e(p["context"], lang)}</p>'
            f'<h3 class="card__title">{e(p["title"], lang)}</h3>'
            f'<p class="card__text">{e(p["summary"], lang)}</p>{tags(p["tech"], lang)}'
            f'{card_links}</div></article>')


def cta_band(lang):
    if lang == "fr":
        title, text, btn = ("Un projet, un stage ou une collaboration ?",
                            "Je suis joignable par e-mail ou sur LinkedIn.", "Me contacter")
    else:
        title, text, btn = ("A project, an internship or a collaboration?",
                            "You can reach me by email or on LinkedIn.", "Get in touch")
    return (f'<section class="cta-band"><div class="container cta-band__inner">'
            f'<div><h2 class="cta-band__title">{title}</h2><p>{text}</p></div>'
            f'<a class="btn btn--primary" href="{url("contact", lang)}">{btn}{icon("arrow-right")}</a>'
            f'</div></section>')


def header(lang, page):
    other = "en" if lang == "fr" else "fr"
    switch_to = url(page if page in PAGES else "home", other)
    links = "".join(
        f'<li><a class="nav__link" href="{url(k, lang)}"{' aria-current="page"' if k == page else ""}>'
        f'{e(NAV_LABELS[k], lang)}</a></li>' for k in PAGES)
    return f'''<a class="skip-link" href="#main">{UI[lang]["skip"]}</a>
<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="{url("home", lang)}" aria-label="Arthinez — {e(NAV_LABELS["home"], lang)}">
      <span class="brand__mark" aria-hidden="true"></span><span class="brand__name">Arthi<span>nez</span></span>
    </a>
    <nav class="nav" id="site-nav" aria-label="{UI[lang]["nav_label"]}">
      <ul class="nav__list">{links}</ul>
      <div class="nav__actions">
        <a class="lang-switch" href="{switch_to}" hreflang="{other}" lang="{other}" aria-label="{UI[lang]["lang_label"]}">{UI[lang]["other_lang"]}</a>
        <a class="btn btn--outline btn--sm" href="{C.PERSON["cv"]}" download aria-label="{UI[lang]["cv_aria"]}">{icon("download")}{UI[lang]["cv"]}</a>
      </div>
    </nav>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-label-open="{UI[lang]["menu"]}" data-label-close="{UI[lang]["close"]}">
      {icon("menu", "icon nav-toggle__open")}{icon("close", "icon nav-toggle__close")}<span class="visually-hidden">{UI[lang]["menu"]}</span>
    </button>
  </div>
</header>'''


def social_links(lang, cls="social"):
    names = {"github": "GitHub", "linkedin": "LinkedIn", "facebook": "Facebook"}
    items = "".join(
        f'<li><a href="{href}" target="_blank" rel="noopener noreferrer me" aria-label="{names[k]} {UI[lang]["new_tab"]}">{icon(k)}</a></li>'
        for k, href in C.PERSON["social"].items())
    return f'<ul class="{cls}">{items}</ul>'


def footer(lang):
    links = "".join(f'<li><a href="{url(k, lang)}">{e(NAV_LABELS[k], lang)}</a></li>' for k in PAGES)
    return f'''<footer class="site-footer">
  <div class="container site-footer__grid">
    <div>
      <a class="brand" href="{url("home", lang)}"><span class="brand__mark" aria-hidden="true"></span><span class="brand__name">Arthi<span>nez</span></span></a>
      <p class="site-footer__tag">{UI[lang]["footer_tag"]}</p>
      {social_links(lang)}
    </div>
    <nav aria-label="{UI[lang]["footer_nav"]}"><p class="site-footer__h">{UI[lang]["footer_nav"]}</p><ul class="site-footer__links">{links}</ul></nav>
    <div><p class="site-footer__h">Contact</p>
      <ul class="site-footer__links">
        <li><a href="mailto:{C.PERSON["email"]}">{C.PERSON["email"]}</a></li>
        <li>{C.PERSON["location"]}</li>
        <li><a href="{C.PERSON["cv"]}" download>{UI[lang]["cv"]}</a></li>
      </ul>
    </div>
  </div>
  <div class="container site-footer__bottom"><p>© {TODAY.year} Tolotra Anthony RANDRIAMBOLOLONA — Arthinez</p></div>
</footer>'''


def person_ld(lang):
    p = C.PERSON
    return {
        "@type": "Person",
        "@id": abs_url("/#person"),
        "name": p["name"],
        "givenName": "Tolotra Anthony",
        "familyName": "RANDRIAMBOLOLONA",
        "alternateName": ["Arthinez", "Tolotra Anthony"],
        "jobTitle": t(p["headline"], lang),
        "description": t(p["tagline"], lang),
        "image": abs_url("/assets/img/portrait-og.jpg"),
        "url": abs_url("/"),
        "email": f"mailto:{p['email']}",
        "worksFor": {"@type": "Organization", "name": "Hango"},
        "alumniOf": [{"@type": "EducationalOrganization", "name": "42 Antananarivo"},
                     {"@type": "EducationalOrganization", "name": "AXIAN University"}],
        "memberOf": {"@type": "Organization", "name": "Bureau des Étudiants — 42 Antananarivo"},
        "address": {"@type": "PostalAddress", "addressLocality": "Antananarivo", "addressCountry": "MG"},
        "knowsLanguage": ["fr", "en", "mg"],
        "knowsAbout": sorted({t(i, "en") for g in C.SKILL_GROUPS[:3] for i in g["items"]} - C.LEARNING),
        "award": ["4th place — 42 Antananarivo internal hackathon", "Homer Simpson Award — Stupid Hackathon (best pitch)"],
        "hasCredential": {"@type": "EducationalOccupationalCredential",
                          "name": t(C.EDUCATION[1]["title"], lang),
                          "recognizedBy": {"@type": "Organization", "name": "AXIAN University"}},
        "sameAs": list(p["social"].values()),
    }


def json_ld(lang, page, extra=None):
    page_url = abs_url(url(page, lang))
    graph = [
        {"@type": "WebSite", "@id": abs_url("/#website"), "url": abs_url("/"),
         "name": "Arthinez", "inLanguage": ["fr", "en"], "publisher": {"@id": abs_url("/#person")}},
        person_ld(lang),
        {"@type": "ProfilePage" if page in ("home", "about") else "WebPage",
         "@id": page_url + "#webpage", "url": page_url, "name": t(META[page]["title"], lang),
         "description": t(META[page]["desc"], lang), "inLanguage": lang,
         "isPartOf": {"@id": abs_url("/#website")}, "about": {"@id": abs_url("/#person")},
         "dateModified": DATE_PLACEHOLDER,
         **({"mainEntity": {"@id": abs_url("/#person")}} if page in ("home", "about") else {})},
    ]
    if page != "home":
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": t(NAV_LABELS["home"], lang), "item": abs_url(url("home", lang))},
            {"@type": "ListItem", "position": 2, "name": t(NAV_LABELS[page], lang), "item": page_url}]})
    graph.extend(extra or [])
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    return data.replace("</", "<\\/")


def layout(lang, page, main, extra_ld=None, robots="index, follow, max-image-preview:large, max-snippet:-1",
           title=None, desc=None):
    indexed = page in PAGES
    title = html.escape(title) if title else e(META[page]["title"], lang)
    desc = html.escape(desc) if desc else e(META[page]["desc"], lang)
    canonical = abs_url(url(page, lang)) if indexed else C.SITE_URL + "/"
    seo_links = ""
    if indexed:
        seo_links = (f'<link rel="canonical" href="{canonical}">\n'
                     + "".join(f'<link rel="alternate" hreflang="{lg}" href="{abs_url(url(page, lg))}">\n' for lg in LANGS)
                     + f'<link rel="alternate" hreflang="x-default" href="{abs_url(url(page, "fr"))}">')
        ld_block = f'<script type="application/ld+json">\n{json_ld(lang, page, extra_ld)}\n</script>'
    else:
        ld_block = ""
    og_locale, og_alt = ("fr_FR", "en_US") if lang == "fr" else ("en_US", "fr_FR")
    og_img = abs_url("/assets/img/portrait-og.jpg")
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<meta name="author" content="{C.PERSON["name"]} (Arthinez)">
<meta name="theme-color" content="#FFFFFF">
<meta name="color-scheme" content="light">
{seo_links}
<meta property="og:type" content="{"profile" if page == "home" else "website"}">
<meta property="og:site_name" content="Arthinez">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1600">
<meta property="og:image:alt" content="{"Portrait de" if lang == "fr" else "Portrait of"} {C.PERSON["name"]}">
<meta property="og:locale" content="{og_locale}">
<meta property="og:locale:alternate" content="{og_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:creator" content="@ArthynezDev">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" href="/image/icon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/image/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="preload" href="/assets/fonts/jost-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/fonts.css?v={VERSION}">
<link rel="stylesheet" href="/css/styles.css?v={VERSION}">
<script src="/css/script.js?v={VERSION}" defer></script>
{ld_block}
<noscript><style>@media (max-width:1080px){{.nav{{display:flex!important;position:static;box-shadow:none}}.nav-toggle{{display:none!important}}.site-header__inner{{flex-wrap:wrap}}}}.reveal{{opacity:1;transform:none}}</style></noscript>
</head>
<body class="page-{page}">
{sprite()}
{header(lang, page)}
<main id="main" tabindex="-1">
{main}
</main>
{footer(lang)}
</body>
</html>
'''


PORTRAIT = {"src": "portrait", "w": 720, "h": 960, "sizes": [360, 720],
            "alt": {"fr": "Portrait de Tolotra Anthony RANDRIAMBOLOLONA, souriant, en t-shirt noir",
                    "en": "Portrait of Tolotra Anthony RANDRIAMBOLOLONA smiling, wearing a black t-shirt"}}
ABOUT_PHOTO = {"src": "about-42", "w": 1100, "h": 825, "sizes": [640, 1100], "pos": "28% 40%",
               "alt": {"fr": "Tolotra Anthony avec le badge de 42 Antananarivo lors d'un événement à l'école",
                       "en": "Tolotra Anthony wearing his 42 Antananarivo lanyard during an event at the school"}}


def home(lang):
    fr = lang == "fr"
    hango = C.EXPERIENCES[0]
    floats = "".join(
        f'<span class="float-logo float-logo--{i}"><img src="/assets/img/logo-{k}.webp" width="56" height="56" alt="{n}"></span>'
        for i, (k, n) in enumerate(C.FEATURED_TECH, 1))
    hero = f'''<section class="hero">
  <div class="container hero__grid">
    <div class="hero__text">
      <p class="hero__hello">{"Bonjour, je suis" if fr else "Hi, I'm"}</p>
      <h1 class="hero__name">Tolotra Anthony <span class="hero__alias">alias Arthinez</span></h1>
      <p class="hero__role">{"" if fr else "A "}<span class="hl-green">{e(C.PERSON["headline"], lang)}</span> {"basé à" if fr else "based in"} <span class="hl-purple">Antananarivo</span></p>
      <p class="hero__lead">{"Développeur junior chez Hango et étudiant à 42 Antananarivo. Je construis des applications web en TypeScript et je m’intéresse de près au cloud, au DevOps et à la sécurité." if fr else "Junior developer at Hango and student at 42 Antananarivo. I build web applications with TypeScript and take a close interest in cloud, DevOps and security."}</p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="{url("projects", lang)}">{"Voir mes projets" if fr else "See my projects"}{icon("arrow-right")}</a>
        <a class="btn btn--ghost" href="{url("contact", lang)}">{"Me contacter" if fr else "Get in touch"}</a>
      </div>
      {social_links(lang, "social social--hero")}
    </div>
    <div class="hero__visual">
      <div class="hero__blob" aria-hidden="true"></div>
      <div class="hero__portrait">{picture(PORTRAIT, lang, "hero__img", eager=True, sizes="(min-width: 960px) 360px, 70vw")}</div>
      {floats}
      <p class="hero__status"><span class="dot" aria-hidden="true"></span>{"En poste" if fr else "Currently"} · <strong>{e(hango["title"], lang)}</strong> @ Hango</p>
    </div>
  </div>
</section>'''

    services = [
        ("code", {"fr": "Développement full-stack", "en": "Full-stack development"},
         {"fr": "APIs REST sécurisées et interfaces web avec TypeScript, Fastify, Next.js, Prisma et PostgreSQL.",
          "en": "Secure REST APIs and web interfaces with TypeScript, Fastify, Next.js, Prisma and PostgreSQL."}, "c1"),
        ("cloud", {"fr": "Cloud, DevOps & IAM", "en": "Cloud, DevOps & IAM"},
         {"fr": "Conteneurisation avec Docker, authentification centralisée avec Keycloak et premiers pas en orchestration Kubernetes.",
          "en": "Containerization with Docker, centralized authentication with Keycloak and first steps in Kubernetes orchestration."}, "c2"),
        ("cpu", {"fr": "Bases systèmes solides", "en": "Solid systems foundations"},
         {"fr": "C, C++, Linux et algorithmique, acquis par la pédagogie par projets de 42.",
          "en": "C, C++, Linux and algorithms, learned through 42’s project-based pedagogy."}, "c3"),
    ]
    svc_html = "".join(
        f'<li class="service reveal-item"><span class="service__icon service__icon--{c}">{icon(i)}</span>'
        f'<h3 class="service__title">{e(ti, lang)}</h3><p>{e(tx, lang)}</p></li>' for i, ti, tx, c in services)
    services_sec = f'''<section class="section" aria-labelledby="services-title">
  <div class="container">
    {section_head("Spécialités" if fr else "What I do", "Ce que je fais" if fr else "What I work on", hid="services-title", center=True)}
    <ul class="services">{svc_html}</ul>
    <p class="center"><a class="link-arrow" href="{url("skills", lang)}">{"Toutes mes compétences" if fr else "All my skills"}{icon("arrow-right")}</a></p>
  </div>
</section>'''

    months_42 = duration((2024, 2), None, lang)
    split = f'''<section class="section section--tint" aria-labelledby="journey-title">
  <div class="container split">
    <div class="split__media reveal-item">
      <span class="scribble" aria-hidden="true"></span>
      <div class="split__photo">{picture(ABOUT_PHOTO, lang, "split__img", sizes="(min-width: 960px) 480px, 100vw")}</div>
      <p class="stat stat--a"><strong class="stat__num hl-green">{months_42.split(" ")[0]}</strong><span>{"ans à 42" if fr else "years at 42"}<br>Antananarivo</span></p>
      <p class="stat stat--b"><strong class="stat__num hl-purple">130</strong><span>{"collaborateurs" if fr else "employees"}<br>{"formés" if fr else "trained"}</span></p>
    </div>
    <div class="split__text">
      {section_head("Mon parcours" if fr else "My journey", "Du code bas niveau aux applications web" if fr else "From low-level code to web applications", hid="journey-title")}
      <p>{"Entré à 42 Antananarivo en février 2024, j’ai appris à résoudre des problèmes complexes par la pratique et le travail en équipe : C, C++, Linux, puis développement web et infrastructure. En 2026, j’ai développé l’interface web de la plateforme d’événements Hango, effectué un stage d’intégration chez Yas Madagascar autour de Keycloak, puis rejoint Hango comme développeur junior." if fr else "I joined 42 Antananarivo in February 2024 and learned to solve complex problems through practice and teamwork: C, C++, Linux, then web development and infrastructure. In 2026 I built the web interface of Hango’s events platform, completed an integration internship at Yas Madagascar around Keycloak, then joined Hango as a junior developer."}</p>
      <p>{"En parallèle, je m’engage au BDE de mon école et j’anime des formations au numérique." if fr else "Alongside this, I’m involved in my school’s Student Council and I deliver digital skills training."}</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="{url("experience", lang)}">{"Mes expériences" if fr else "My experience"}{icon("arrow-right")}</a>
        <a class="btn btn--ghost" href="{url("about", lang)}">{"En savoir plus" if fr else "More about me"}</a>
      </div>
    </div>
  </div>
</section>'''

    quick = [
        ("experience", "briefcase", {"fr": "Hango, Yas Madagascar et le cursus 42.", "en": "Hango, Yas Madagascar and the 42 curriculum."}),
        ("involvement", "users", {"fr": "BDE, événements et formations animées.", "en": "Student Council, events and training sessions."}),
        ("projects", "code", {"fr": f"{len(C.PROJECTS)} projets : Keycloak, Webserv, Inception, hackathons…", "en": f"{len(C.PROJECTS)} projects: Keycloak, Webserv, Inception, hackathons…"}),
        ("skills", "cpu", {"fr": "Web, cloud & DevOps, systèmes et soft skills.", "en": "Web, cloud & DevOps, systems and soft skills."}),
    ]
    quick_html = "".join(
        f'<li><a class="quick reveal-item" href="{url(k, lang)}"><span class="quick__icon">{icon(i)}</span>'
        f'<span class="quick__title">{e(NAV_LABELS[k], lang)}</span><span class="quick__text">{e(d, lang)}</span>'
        f'{icon("arrow-right", "icon quick__arrow")}</a></li>' for k, i, d in quick)
    explore = f'''<section class="section" aria-labelledby="explore-title">
  <div class="container">
    {section_head("Portfolio", "Explorer mon parcours" if fr else "Explore my work", "Chaque facette de mon profil a sa propre page." if fr else "Each side of my profile has its own page.", center=True, hid="explore-title")}
    <ul class="quick-grid">{quick_html}</ul>
  </div>
</section>'''
    return hero + services_sec + split + explore + cta_band(lang)


def experience_page(lang):
    fr = lang == "fr"
    work = [x for x in C.EXPERIENCES if x["group"] == "work"]
    school = [x for x in C.EXPERIENCES if x["group"] == "school"]
    cards = ""
    orgs = list(dict.fromkeys(x["org"] for x in work))
    for org in orgs:
        items = [x for x in work if x["org"] == org]
        roles = [role_item(x["title"], period(x["start"], x["end"], lang, len(items) > 1), x["summary"], lang,
                           x["highlights"], x.get("note"), x.get("url")) for x in items]
        first, last = items[-1], items[0]
        loc = f' · {last["location"]}' if last["location"] else ""
        when = (period(first["start"], last["end"], lang, False) if len(items) > 1
                else duration(last["start"], last["end"], lang)) + loc
        tech = list(dict.fromkeys(tg for x in items for tg in x["tech"]))
        cards += timeline_card(lang, anchor=last["id"], org=org, kind=last["type"], when=when,
                               media=placeholder("briefcase", "warm"), roles=roles, tag_items=tech)
    s_roles = [role_item(x["title"], period(x["start"], x["end"], lang), x["summary"], lang) for x in school]
    first = min(x["start"] for x in school)
    s_card = timeline_card(lang, anchor="42-antananarivo", org="42 Antananarivo", kind=school[0]["type"],
                           when=duration(first, None, lang) + " · Antananarivo",
                           media=picture(ABOUT_PHOTO, lang, "xp-card__img", sizes="(min-width: 960px) 380px, 100vw"),
                           roles=s_roles, tag_items=school[1]["tech"])
    body = page_hero(lang, "experience", "Parcours professionnel" if fr else "Career",
                     "Expériences professionnelles" if fr else "Professional experience",
                     "Emplois, stage et cursus à 42 Antananarivo, du plus récent au plus ancien." if fr else
                     "Jobs, internship and the 42 Antananarivo curriculum, most recent first.")
    body += f'''<section class="section section--tight" aria-labelledby="work-title">
  <div class="container">
    {section_head("Entreprises" if fr else "Companies", "Emplois & stages" if fr else "Jobs & internships", hid="work-title")}
    <div class="xp-list">{cards}</div>
  </div>
</section>
<section class="section section--tight" aria-labelledby="school-title">
  <div class="container">
    {section_head("Formation pratique" if fr else "Hands-on training", "Cursus à 42 Antananarivo" if fr else "42 Antananarivo curriculum", hid="school-title")}
    <div class="xp-list">{s_card}</div>
  </div>
</section>'''
    ld = [{"@type": "OrganizationRole", "roleName": t(x["title"], "en"), "startDate": f"{x['start'][0]}-{x['start'][1]:02d}",
           **({"endDate": f"{x['end'][0]}-{x['end'][1]:02d}"} if x["end"] else {}),
           "worksFor" if x["group"] == "work" else "memberOf": {"@type": "Organization", "name": x["org"]}}
          for x in C.EXPERIENCES]
    return body + cta_band(lang), [{"@type": "ItemList", "name": t(META["experience"]["title"], lang),
                                     "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": r} for i, r in enumerate(ld)]}]


def event_link(ev, lang):
    if not ev.get("link"):
        return ""
    label = "Voir la publication" if lang == "fr" else "See the post"
    return f'<div class="card__links">{ext_link(ev["link"], label, lang)}</div>'


def partners(ev, lang):
    if not ev.get("partners"):
        return ""
    label = "Partenaires" if lang == "fr" else "Partners"
    return (f'<div class="card__partners"><p class="card__partners-label">{label}</p>'
            f'{tags(ev["partners"], lang, label=label)}</div>')


def involvement_page(lang):
    fr = lang == "fr"
    b = C.BDE
    bde_roles = [role_item(r["title"], period(r["start"], r["end"], lang), r["summary"], lang) for r in C.BDE_ROLES]
    bde_card = timeline_card(lang, anchor="bde", org=b["org"], kind={"fr": "Association étudiante", "en": "Student association"},
                             when=duration(b["start"], b["end"], lang), media=picture(b["image"], lang, "xp-card__img", sizes="(min-width: 960px) 380px, 100vw"),
                             roles=bde_roles, tag_items=b["skills"])
    events = "".join(
        f'<article class="card event reveal-item" id="{ev["id"]}"><div class="card__media card__media--poster">'
        f'{picture(ev["image"], lang, "card__img", sizes="(min-width: 960px) 360px, 100vw")}</div>'
        f'<div class="card__body"><p class="card__kicker">{icon("calendar")}{e(ev["date"], lang)}</p>'
        f'<h3 class="card__title">{e(ev["title"], lang)}</h3><p class="card__text">{e(ev["summary"], lang)}</p>'
        f'<p class="card__place">{icon("pin")}{e(ev["place"], lang)}</p>'
        f'{partners(ev, lang)}{event_link(ev, lang)}</div></article>' for ev in C.EVENTS)
    trainings = ""
    for tr in C.TRAININGS:
        roles = [role_item(tr["title"] if i == 0 else ({"fr": "Session d’approfondissement", "en": "Follow-up session"}),
                           period(s["start"], s["end"], lang), s["text"], lang) for i, s in enumerate(tr["sessions"])]
        impact = f'<p class="impact">{icon("users")}{e(tr["impact"], lang)}</p>'
        trainings += timeline_card(lang, anchor=tr["id"], org=tr["org"], kind={"fr": "Formation", "en": "Training"},
                                   when=f'{len(tr["sessions"])} sessions · via 42 Antananarivo',
                                   media=picture(tr["image"], lang, "xp-card__img", sizes="(min-width: 960px) 380px, 100vw"),
                                   roles=roles, tag_items=tr["skills"], extra=impact)
    cert = C.EDUCATION[1]
    body = page_hero(lang, "involvement", "Vie associative" if fr else "Community",
                     "Engagements & responsabilités" if fr else "Involvement & responsibilities",
                     "Ce que je fais en dehors du code : la vie étudiante à 42, l’organisation d’événements et la transmission du numérique." if fr else
                     "What I do beyond code: student life at 42, event organization and sharing digital skills.")
    body += f'''<section class="section section--tight" aria-labelledby="bde-title">
  <div class="container">
    {section_head("Bureau des Étudiants" if fr else "Student Council", "Responsabilités au BDE" if fr else "Student Council roles", hid="bde-title")}
    <div class="xp-list">{bde_card}</div>
  </div>
</section>
<section class="section section--tight" aria-labelledby="events-title">
  <div class="container">
    {section_head("Événements" if fr else "Events", "Événements du BDE" if fr else "Student Council events", "Des événements portés par le BDE 404.42 de 42 Antananarivo, ou auxquels l’équipe a pris part, pendant mon mandat." if fr else "Events run by the 42 Antananarivo 404.42 Student Council, or that the team took part in, during my term.", hid="events-title")}
    <div class="card-grid">{events}</div>
  </div>
</section>
<section class="section section--tight" aria-labelledby="training-title">
  <div class="container">
    {section_head("Transmission" if fr else "Teaching", "Formations animées" if fr else "Training I delivered", hid="training-title")}
    <div class="xp-list">{trainings}</div>
    <p class="callout reveal-item">{icon("award")}<span><strong>{e(cert["title"], lang)}</strong> — {cert["org"]}, {e(cert["period"], lang)}</span></p>
  </div>
</section>'''
    ld = [{"@type": "Event", "name": ev["title"], "location": {"@type": "Place", "name": t(ev["place"], lang)},
           "startDate": ev["iso"], "organizer": {"@type": "Organization", "name": "Bureau des Étudiants — 42 Antananarivo"},
           **({"sponsor": [{"@type": "Organization", "name": n} for n in ev["partners"]]} if ev.get("partners") else {}),
           "image": abs_url(f'/assets/img/{ev["image"]["src"]}-{ev["image"]["sizes"][-1]}.webp')}
          for ev in C.EVENTS]
    return body + cta_band(lang), ld


def projects_page(lang):
    fr = lang == "fr"
    filters = "".join(
        f'<button type="button" class="filter" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{e(lbl, lang)}</button>'
        for k, lbl in C.PROJECT_FILTERS)
    cards = "".join(project_card(p, lang) for p in C.PROJECTS)
    body = page_hero(lang, "projects", "Réalisations" if fr else "Work",
                     "Projets techniques" if fr else "Technical projects",
                     "Projets menés en entreprise, dans le cursus 42 et en hackathon." if fr else
                     "Projects built at work, in the 42 curriculum and at hackathons.")
    body += f'''<section class="section section--tight" aria-labelledby="projects-list-title">
  <div class="container">
    <h2 class="visually-hidden" id="projects-list-title">{"Liste des projets" if fr else "Project list"}</h2>
    <div class="filters" role="group" aria-label="{"Filtrer les projets" if fr else "Filter projects"}" hidden>{filters}</div>
    <p class="visually-hidden" aria-live="polite" data-filter-status></p>
    <div class="card-grid" data-filter-grid>{cards}</div>
    <p class="center more">{ext_link(C.PERSON["social"]["github"], "Tous mes dépôts sur GitHub" if fr else "All my repositories on GitHub", lang, cls="btn btn--ghost", ico="github")}</p>
  </div>
</section>'''
    ld = [{"@type": "SoftwareSourceCode", "@id": abs_url(url("projects", lang)) + "#" + p["id"], "name": t(p["title"], lang),
           "description": t(p["summary"], lang), "author": {"@id": abs_url("/#person")},
           "keywords": [t(x, lang) for x in p["tech"]], **({"codeRepository": p["links"][0][1]} if p["links"] and p["links"][0][0] == "github" else {})}
          for p in C.PROJECTS if p["cat"] != "hackathon"]
    return body + cta_band(lang), ld


def skills_page(lang):
    fr = lang == "fr"
    logos = "".join(f'<li><img src="/assets/img/logo-{k}.webp" width="56" height="56" alt="" loading="lazy"><span>{n}</span></li>'
                    for k, n in C.FEATURED_TECH)
    groups = "".join(
        f'<section class="skill-group reveal-item" aria-labelledby="sg-{g["id"]}"><div class="skill-group__head">'
        f'<span class="service__icon service__icon--c{i % 3 + 1}">{icon(g["icon"])}</span>'
        f'<h2 class="skill-group__title" id="sg-{g["id"]}">{e(g["title"], lang)}</h2></div>'
        f'{tags(g["items"], lang, "chips")}</section>' for i, g in enumerate(C.SKILL_GROUPS))
    langs = "".join(f"<li>{x}</li>" for x in C.PERSON["languages"][lang])
    body = page_hero(lang, "skills", "Boîte à outils" if fr else "Toolbox",
                     "Compétences" if fr else "Skills",
                     "Les langages, frameworks et outils que j’utilise en projet et en entreprise." if fr else
                     "The languages, frameworks and tools I use in projects and at work.")
    body += f'''<section class="section section--tight">
  <div class="container">
    <ul class="logo-row" aria-label="{"Technologies principales" if fr else "Core technologies"}">{logos}</ul>
    <div class="skill-grid">{groups}</div>
    <section class="skill-group skill-group--inline reveal-item" aria-labelledby="sg-lang">
      <div class="skill-group__head"><span class="service__icon service__icon--c2">{icon("mic")}</span>
      <h2 class="skill-group__title" id="sg-lang">{"Langues" if fr else "Languages"}</h2></div>
      <ul class="chips">{langs}</ul>
    </section>
    <p class="center more"><a class="link-arrow" href="{url("projects", lang)}">{"Voir ces compétences en action dans mes projets" if fr else "See these skills in action in my projects"}{icon("arrow-right")}</a></p>
  </div>
</section>'''
    return body + cta_band(lang), []


def about_page(lang):
    fr = lang == "fr"
    edu = "".join(
        f'<li class="edu reveal-item"><span class="edu__icon">{icon("cap")}</span><div><h3>{ed["org"]}</h3>'
        f'<p>{e(ed["title"], lang)}</p><p class="muted">{e(ed["period"], lang)}</p></div></li>' for ed in C.EDUCATION)
    interests = "".join(
        f'<li class="service reveal-item"><span class="service__icon service__icon--c{i + 1}">{icon(it["icon"])}</span>'
        f'<h3 class="service__title">{e(it["title"], lang)}</h3><p>{e(it["text"], lang)}</p></li>' for i, it in enumerate(C.INTERESTS))
    body = page_hero(lang, "about", "À propos" if fr else "About me",
                     "Curieux, pragmatique et tourné vers les autres" if fr else "Curious, pragmatic and people-minded",
                     "Mon parcours, ma formation et ce qui me motive." if fr else "My background, education and what drives me.")
    body += f'''<section class="section section--tight" aria-labelledby="bio-title">
  <div class="container split split--about">
    <div class="split__text">
      <h2 class="section-title" id="bio-title">{"Qui suis-je ?" if fr else "Who am I?"}</h2>
      <p>{"Je m’appelle Tolotra Anthony RANDRIAMBOLOLONA — Arthinez en ligne. Je suis développeur full-stack à Antananarivo, passionné par la technologie et tout ce qui l’entoure." if fr else "My name is Tolotra Anthony RANDRIAMBOLOLONA — Arthinez online. I’m a full-stack developer in Antananarivo, passionate about technology and everything around it."}</p>
      <p>{"Depuis février 2024, je me forme à 42 Antananarivo, une école reconnue pour sa pédagogie innovante : pas de cours magistraux, mais des projets concrets et du peer-learning. J’y ai acquis des bases solides en C, Linux et algorithmique, puis en développement web et en infrastructure." if fr else "Since February 2024 I’ve been training at 42 Antananarivo, a school known for its innovative pedagogy: no lectures, just real projects and peer learning. There I built solid foundations in C, Linux and algorithms, then in web development and infrastructure."}</p>
      <p>{"Je suis motivé par la curiosité, l’apprentissage continu et l’envie de contribuer de manière significative au monde numérique de demain — y compris en le rendant accessible à tous, à travers les formations que j’anime." if fr else "I’m driven by curiosity, continuous learning and the ambition to contribute meaningfully to tomorrow’s digital world — including making it accessible to everyone through the training sessions I deliver."}</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="{C.PERSON["cv"]}" download>{icon("download")}{UI[lang]["cv"]}</a>
        <a class="btn btn--ghost" href="{url("contact", lang)}">{"Me contacter" if fr else "Get in touch"}</a>
      </div>
    </div>
    <div class="split__media reveal-item">
      <div class="split__photo split__photo--portrait">{picture(PORTRAIT, lang, "split__img", sizes="(min-width: 960px) 400px, 100vw")}</div>
    </div>
  </div>
</section>
<section class="section section--tint" aria-labelledby="edu-title">
  <div class="container">
    {section_head("Formation" if fr else "Education", "Formation & certification" if fr else "Education & certification", hid="edu-title")}
    <ul class="edu-list">{edu}</ul>
  </div>
</section>
<section class="section" aria-labelledby="interests-title">
  <div class="container">
    {section_head("Centres d’intérêt" if fr else "Interests", "Ce qui me motive" if fr else "What drives me", "Mon objectif : évoluer comme développeur full-stack en approfondissant le cloud, le DevOps et la sécurité." if fr else "My goal: grow as a full-stack developer while going deeper into cloud, DevOps and security.", hid="interests-title", center=True)}
    <ul class="services">{interests}</ul>
  </div>
</section>
<section class="section section--tight" aria-labelledby="awards-title">
  <div class="container">
    {section_head("Distinctions" if fr else "Awards", "Hackathons" if fr else "Hackathons", hid="awards-title")}
    <ul class="awards">
      <li class="reveal-item">{icon("trophy")}<div><strong>{"4e place — Hackathon interne 42 Antananarivo" if fr else "4th place — 42 Antananarivo internal hackathon"}</strong><p>{"Résolution de problèmes et travail d’équipe en environnement compétitif." if fr else "Problem solving and teamwork in a competitive setting."}</p></div></li>
      <li class="reveal-item">{icon("award")}<div><strong>{"Prix Homer Simpson — Stupid Hackathon" if fr else "Homer Simpson Award — Stupid Hackathon"}</strong><p>{"Meilleur pitch de projet." if fr else "Best project pitch."}</p></div></li>
    </ul>
    <p><a class="link-arrow" href="{url("projects", lang)}#hackathon-42">{"Voir les hackathons dans les projets" if fr else "See the hackathons in projects"}{icon("arrow-right")}</a></p>
  </div>
</section>'''
    return body + cta_band(lang), []


def contact_page(lang):
    fr = lang == "fr"
    p = C.PERSON
    items = [
        ("mail", "E-mail" if fr else "Email", p["email"], f'mailto:{p["email"]}', False),
        ("linkedin", "LinkedIn", "in/tolotra-anthony", p["social"]["linkedin"], True),
        ("github", "GitHub", "@Hynoht", p["social"]["github"], True),
    ]
    ext_attr = ' target="_blank" rel="noopener noreferrer"'
    new_tab = f'<span class="visually-hidden"> {UI[lang]["new_tab"]}</span>'
    cards = "".join(
        f'<li><a class="contact-card reveal-item" href="{href}"{ext_attr if ext else ""}>'
        f'<span class="contact-card__icon">{icon(i)}</span><span class="contact-card__label">{lbl}</span>'
        f'<span class="contact-card__value">{html.escape(val)}</span>{new_tab if ext else ""}</a></li>'
        for i, lbl, val, href, ext in items)
    body = page_hero(lang, "contact", "Contact", "Travaillons ensemble" if fr else "Let’s work together",
                     "Une question, une opportunité ou un projet ? Écrivez-moi : je réponds rapidement." if fr else
                     "A question, an opportunity or a project? Drop me a line.")
    body += f'''<section class="section section--tight" aria-labelledby="contact-title">
  <div class="container">
    <h2 class="visually-hidden" id="contact-title">{"Moyens de contact" if fr else "Ways to reach me"}</h2>
    <ul class="contact-grid">{cards}</ul>
    <div class="contact-extra">
      <p>{icon("pin")}{p["location"]} · {"Français, anglais, malgache" if fr else "French, English, Malagasy"}</p>
      <a class="btn btn--primary" href="{p["cv"]}" download>{icon("download")}{UI[lang]["cv"]}</a>
    </div>
  </div>
</section>'''
    return body, [{"@type": "ContactPage", "url": abs_url(url("contact", lang))}]


def not_found():
    main = f'''<section class="page-hero page-hero--404"><div class="container center">
  <p class="eyebrow">Erreur 404 · <span lang="en">Error 404</span></p>
  <h1 class="page-hero__title">Page introuvable</h1>
  <p class="page-hero__intro">Cette page n’existe pas ou plus. <span lang="en">This page doesn’t exist anymore.</span></p>
  <div class="btn-row btn-row--center">
    <a class="btn btn--primary" href="/">Retour à l’accueil{icon("arrow-right")}</a>
    <a class="btn btn--ghost" href="/en/" lang="en">Back to home</a>
  </div>
</div></section>'''
    return layout("fr", "404", main, robots="noindex",
                  title="404 — Page introuvable | Arthinez", desc="Page introuvable.")


BUILDERS = {
    "experience": experience_page, "involvement": involvement_page, "projects": projects_page,
    "skills": skills_page, "about": about_page, "contact": contact_page,
}


DATE_PLACEHOLDER = "@@DATE_MODIFIED@@"
LASTMOD_FILE = ROOT / "scripts" / "lastmod.json"
LASTMOD = json.loads(LASTMOD_FILE.read_text()) if LASTMOD_FILE.exists() else {}


def stamp(path, text):
    normalized = re.sub(r"\?v=[0-9a-f]+", "", text)
    digest = hashlib.sha1(normalized.encode()).hexdigest()
    entry = LASTMOD.get(path)
    if not entry or entry["hash"] != digest:
        entry = {"hash": digest, "date": TODAY.isoformat()}
        LASTMOD[path] = entry
    return text.replace(DATE_PLACEHOLDER, entry["date"])


def write_page(path, text):
    write(path, stamp(path, text))


def write(path, text):
    target = ROOT / path.lstrip("/")
    if path.endswith("/"):
        target = target / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print("  ✓", target.relative_to(ROOT))


def sitemap():
    rows = []
    for page in PAGES:
        for lang in LANGS:
            alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{lg}" href="{abs_url(url(page, lg))}"/>' for lg in LANGS)
            alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(url(page, "fr"))}"/>'
            img = ""
            if page == "home":
                img = f"\n    <image:image><image:loc>{abs_url('/assets/img/portrait-og.jpg')}</image:loc></image:image>"
            rows.append(f'''  <url>
    <loc>{abs_url(url(page, lang))}</loc>
    <lastmod>{LASTMOD.get(url(page, lang), {}).get("date", TODAY.isoformat())}</lastmod>
    <priority>{"1.0" if page == "home" else "0.8"}</priority>{alts}{img}
  </url>''')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:xhtml="http://www.w3.org/1999/xhtml"\n'
            '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def llms_txt():
    L = "en"
    lines = [
        "# Arthinez — Tolotra Anthony RANDRIAMBOLOLONA",
        "",
        "> Portfolio of a full-stack developer based in Antananarivo, Madagascar. This file summarizes the site for AI agents and LLMs.",
        f"> Canonical source: {C.SITE_URL}/ (French) — English version: {C.SITE_URL}/en/",
        "",
        "## Profile",
        f"- Name: {C.PERSON['name']} (alias Arthinez)",
        f"- Headline: {t(C.PERSON['tagline'], L)}",
        f"- Location: {C.PERSON['location']}",
        "- Languages: French, English, Malagasy",
        "",
        "## Professional experience",
    ]
    for x in C.EXPERIENCES:
        desc = f": {t(x['summary'], L)}" if x["summary"] else ""
        site = f" Live: {x['url']}" if x.get("url") else ""
        lines.append(f"- {t(x['title'], L)} — {x['org']} ({period(x['start'], x['end'], L)}){desc}{site}")
    lines += ["", "## Involvement & responsibilities"]
    for r in C.BDE_ROLES:
        lines.append(f"- {t(r['title'], L)} — Student Council, 42 Antananarivo ({period(r['start'], r['end'], L)}): {t(r['summary'], L)}")
    for tr in C.TRAININGS:
        sess = ", ".join(period(s["start"], s["end"], L, False) for s in tr["sessions"])
        lines.append(f"- Trainer — {tr['org']} ({sess}): {t(tr['impact'], L)}. " + " ".join(t(s["text"], L) for s in tr["sessions"]))
    for ev in C.EVENTS:
        sp = f" Partners: {', '.join(ev['partners'])}." if ev.get("partners") else ""
        lines.append(f"- Event — {ev['title']} ({t(ev['date'], L)}, {t(ev['place'], L)}): {t(ev['summary'], L)}{sp}")
    lines += ["", "## Projects"]
    for p in C.PROJECTS:
        tech = f" [{', '.join(t(x, L) for x in p['tech'])}]" if p["tech"] else ""
        lines.append(f"- {t(p['title'], L)} — {t(p['context'], L)}{tech}: {t(p['summary'], L)}")
    lines += ["", "## Skills"]
    for g in C.SKILL_GROUPS:
        lines.append(f"- {t(g['title'], L)}: " + ", ".join(
            t(i, L) + (" (learning, beginner level)" if t(i, L) in C.LEARNING else "") for i in g["items"]))
    lines += ["", "## Education"]
    for ed in C.EDUCATION:
        lines.append(f"- {ed['org']}: {t(ed['title'], L)} ({t(ed['period'], L)})")
    lines += ["", "## Pages"]
    for page in PAGES:
        lines.append(f"- [{t(NAV_LABELS[page], 'en')}]({abs_url(url(page, 'en'))}) / [{t(NAV_LABELS[page], 'fr')}]({abs_url(url(page, 'fr'))})")
    lines += ["", "## Links",
              f"- GitHub: {C.PERSON['social']['github']}",
              f"- LinkedIn: {C.PERSON['social']['linkedin']}",
              f"- Email: {C.PERSON['email']}",
              f"- CV (PDF): {C.SITE_URL}{C.PERSON['cv']}", ""]
    return "\n".join(lines)


def main():
    print(f"Building portfolio (assets v={VERSION})")
    for lang in LANGS:
        write_page(url("home", lang), layout(lang, "home", home(lang)))
        for page, build in BUILDERS.items():
            body, ld = build(lang)
            write_page(url(page, lang), layout(lang, page, body, ld))
    write("/404.html", not_found())
    write("/sitemap.xml", sitemap())
    write("/llms.txt", llms_txt())
    LASTMOD_FILE.write_text(json.dumps(LASTMOD, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
