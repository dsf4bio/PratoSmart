#!/usr/bin/env python3
"""
Genera tutte le pagine HTML di PratoSmart.

Uso, dalla cartella del sito:
    python3 _sorgente/genera_sito.py

- I testi delle guide sono in _sorgente/guide.py
- Prodotti, link affiliati e configurazione NON sono qui:
  si modificano in assets/products.js e non serve rigenerare.
- Quando hai il dominio, scrivilo in SITE_URL e rigenera: verranno aggiunti
  canonical, og:url, percorso strutturato (breadcrumb) e sitemap corretta.
"""
import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from componenti import ARROW, esc, check_list, picks_table  # noqa: E402
from guide import ARTICLES, GROUPS, HOME_FAQ, HOME_FEATURED  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_NAME = "PratoSmart"
SITE_URL = ""                 # ✏️ es. "https://www.pratosmart.it" (senza / finale)
UPDATED_ISO = "2026-10-26"
UPDATED_IT = "26 ottobre 2026"
ASSET_VERSION = "20261026b"    # cambialo quando modifichi CSS o JS, per aggiornare la cache

ARTICLE_BY_SLUG = {a["slug"]: a for a in ARTICLES}
GROUP_OF = {slug: name for name, slugs in GROUPS for slug in slugs}

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%232F8F46'/%3E"
           "%3Cpath d='M12 38c0-8 8-13 21-13h9c9 0 13 6 13 12v3H12z' fill='%23FFFFFF'/%3E%3Crect x='39' y='15' width='3' height='10' rx='1.5' fill='%23FFFFFF'/%3E"
           "%3Ccircle cx='40.5' cy='14' r='3' fill='%23FFC233'/%3E%3Ccircle cx='22' cy='44' r='6' fill='%2314321F'/%3E%3Ccircle cx='50' cy='46' r='4' fill='%2314321F'/%3E%3C/svg%3E")

ROBOT_SVG = '''<svg viewBox="0 0 140 72" xmlns="http://www.w3.org/2000/svg">
                  <ellipse cx="72" cy="68" rx="56" ry="4" fill="rgba(20,50,31,0.25)"/>
                  <path d="M14 50C14 31 34 19 64 19H92C116 19 128 33 128 47V52H14Z" fill="#2F8F46"/>
                  <path d="M32 32C42 25 53 22 66 22H90C105 22 115 28 120 37H35Z" fill="#45AE5F"/>
                  <rect x="12" y="47" width="118" height="9" rx="4.5" fill="#14321F"/>
                  <rect x="84" y="5" width="4" height="15" rx="2" fill="#14321F"/>
                  <circle class="robot-led" cx="86" cy="5" r="4" fill="#FFC233"/>
                  <rect x="97" y="28" width="16" height="6" rx="3" fill="#C9F2D3"/>
                  <g class="robot-wheel">
                    <circle cx="34" cy="56" r="13" fill="#14321F"/>
                    <circle cx="34" cy="56" r="5" fill="#9FB8A5"/>
                    <path d="M34 44V68M22 56H46" stroke="#2B4A36" stroke-width="2.5"/>
                  </g>
                  <g class="robot-wheel">
                    <circle cx="113" cy="60" r="8" fill="#14321F"/>
                    <circle cx="113" cy="60" r="3" fill="#9FB8A5"/>
                  </g>
                </svg>'''


def path_of(slug):
    """Indirizzo pubblico della pagina (usato per canonical e sitemap)."""
    return "/" if not slug else "/" + slug + ".html"


# Nei testi i link interni si scrivono "/pagina" o "/#sezione": al salvataggio
# diventano link relativi ai file ("pagina.html", "index.html#sezione"), così
# funzionano sia aprendo i file dal computer o da VS Code, sia su Vercel.
LINK_RE = re.compile(r'(?<!<base )(href|src)="/([^"]*)"')


def to_relative(match):
    attr, rest = match.group(1), match.group(2)
    path, sep, frag = rest.partition("#")
    if not path:
        target = "index.html"
    elif "." in path.split("/")[-1]:
        target = path            # file con estensione: assets/style.css?v=..., sitemap.xml
    else:
        target = path + ".html"
    return f'{attr}="{target}{sep}{frag}"'


def relative_links(html_text, is_home=False):
    if is_home:
        html_text = html_text.replace('href="/#', 'href="#')
    return LINK_RE.sub(to_relative, html_text)


# ======================================================================
# STRUTTURA COMUNE A TUTTE LE PAGINE
# ======================================================================

NAV = [
    ("/#migliori", "Migliori", "", None),
    ("/#quiz", "Quiz", "nav-quiz", None),
    ("MENU", "Guide", "", None),
    ("/robot-tagliaerba-black-friday", "Black Friday", "", "robot-tagliaerba-black-friday"),
]


def guides_menu(active):
    """Menu a tendina "Guide" con tutte le guide, raggruppate."""
    is_guide = active == "guide" or active in ARTICLE_BY_SLUG
    groups = ""
    for name, slugs in GROUPS:
        links = ""
        for s in slugs:
            current = ' aria-current="page"' if s == active else ""
            links += f'<li><a href="/{s}"{current}>{ARTICLE_BY_SLUG[s]["card_title"]}</a></li>'
        groups += f'<div class="nav-menu-group"><p class="nav-menu-title">{name}</p><ul>{links}</ul></div>'
    summary_cls = ' class="is-current"' if is_guide else ""
    return f'''<details class="nav-menu" data-nav-menu>
            <summary{summary_cls}>Guide</summary>
            <div class="nav-menu-panel">
              <div class="nav-menu-groups">{groups}</div>
              <a class="nav-menu-all" href="/guide">Vedi tutte le guide →</a>
            </div>
          </details>'''


def header(active):
    items = ""
    for href, label, cls, key in NAV:
        if href == "MENU":
            items += f'<li>{guides_menu(active)}</li>'
            continue
        attrs = f' class="{cls}"' if cls else ""
        if key and key == active:
            attrs += ' aria-current="page"'
        items += f'<li><a href="{href}"{attrs}>{label}</a></li>'
    return f'''  <div class="topbar" id="topbar">
    <p>Guide e robot tagliaerba selezionati · <strong>prezzi e disponibilità aggiornati su Amazon.it</strong></p>
  </div>

  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="/" aria-label="PratoSmart, vai alla home">
        <span class="logo-mark" aria-hidden="true"></span>
        <span>Prato<span class="logo-accent">Smart</span></span>
      </a>
      <nav class="nav" aria-label="Navigazione principale">
        <ul>{items}</ul>
      </nav>
    </div>
  </header>'''


def footer():
    guide_links = "".join(
        f'<li><a href="/{a["slug"]}">{a["card_title"]}</a></li>' for a in ARTICLES
    )
    return f'''  <footer class="site-footer" id="informazioni" aria-labelledby="footer-title">
    <div class="container">
      <h2 class="visually-hidden" id="footer-title">Informazioni</h2>
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="logo" href="/" aria-label="PratoSmart, vai alla home">
            <span class="logo-mark" aria-hidden="true"></span>
            <span>Prato<span class="logo-accent">Smart</span></span>
          </a>
          <p class="footer-tagline">Guide pratiche e robot tagliaerba selezionati per giardini piccoli, medi e grandi.</p>
        </div>

        <div>
          <h3 class="footer-title">Trasparenza</h3>
          <!-- ✏️ Verifica la formulazione richiesta dalle condizioni aggiornate
               del Programma Affiliazione Amazon.it prima di pubblicare. -->
          <p class="disclosure">In qualità di Affiliato Amazon, ricevo un guadagno dagli acquisti idonei.</p>
          <p class="footer-small">I pulsanti “Verifica disponibilità” rimandano ad Amazon.it tramite link di affiliazione. Prezzi, disponibilità e condizioni di vendita sono indicati esclusivamente sulla pagina Amazon del prodotto.</p>
          <p class="footer-small">PratoSmart è un sito indipendente e non è il negozio ufficiale di Amazon.</p>
        </div>

        <div>
          <h3 class="footer-title">Guide</h3>
          <ul class="footer-links">{guide_links}</ul>
        </div>

        <div>
          <h3 class="footer-title">Informazioni</h3>
          <ul class="footer-links">
            <li><a href="/#quiz">Quiz: trova il tuo robot</a></li>
            <li><a href="/guide">Tutte le guide</a></li>
            <li><a href="/chi-siamo">Chi siamo</a></li>
            <li><a href="/privacy">Privacy policy</a></li>
            <li><a href="/cookie-policy">Cookie policy</a></li>
            <!-- ✏️ Puoi sostituire questo indirizzo con il tuo link affiliato alla home di Amazon.it -->
            <li><a href="https://www.amazon.it/" target="_blank" rel="sponsored nofollow noopener noreferrer">Amazon.it</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© <span id="year">2026</span> PratoSmart. Tutti i diritti riservati.</p>
        <p>Amazon e il logo Amazon sono marchi di Amazon.com, Inc. o delle sue società affiliate.</p>
      </div>
    </div>
  </footer>'''


def tail(sticky_href):
    sticky = ""
    if sticky_href:
        sticky = f'''
  <div class="sticky-cta" id="sticky-cta">
    <a class="btn btn-cta" href="{sticky_href}">Trova il tuo robot in 30 secondi {ARROW}</a>
  </div>'''
    return f'''
  <div class="toast" id="toast" role="status" aria-live="polite"></div>
  <p class="visually-hidden" id="affiliate-hint">Apre la pagina del prodotto su Amazon.it in una nuova scheda. Link di affiliazione.</p>{sticky}

  <!-- Banner cookie informativo: il sito usa solo uno strumento tecnico,
       quindi per le Linee guida del Garante non serve il consenso. -->
  <section class="cookie-banner" id="cookie-banner" aria-labelledby="cookie-banner-title" hidden>
    <button class="cookie-close" type="button" id="cookie-close" aria-label="Chiudi l'avviso sui cookie"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    <h2 id="cookie-banner-title">Niente cookie di profilazione</h2>
    <p>PratoSmart non usa cookie di profilazione, di statistica o di marketing: salva solo un'informazione tecnica per ricordare che hai letto questo avviso. Se clicchi su un prodotto, su Amazon.it valgono i cookie di Amazon.</p>
    <div class="cookie-actions">
      <button class="btn" type="button" id="cookie-ok">Ho capito</button>
      <a href="/cookie-policy">Cookie policy</a>
      <a href="/privacy">Privacy</a>
    </div>
  </section>

  <script src="/assets/products.js?v={ASSET_VERSION}" defer></script>
  <script src="/assets/site.js?v={ASSET_VERSION}" defer></script>'''


def json_ld(data):
    text = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{text}\n</script>'


def faq_schema(faq):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq
        ],
    }


def breadcrumb_schema(items):
    """items: lista di (nome, slug). Generato solo se SITE_URL è impostato."""
    if not SITE_URL:
        return None
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE_URL + path_of(slug)}
            for i, (name, slug) in enumerate(items)
        ],
    }


def page(*, slug, title, desc, body, schemas=(), active=None, noindex=False,
         og_type="website", sticky_href="/#quiz", base_root=False):
    url = SITE_URL + path_of(slug) if SITE_URL else ""
    seo = []
    if base_root:
        # La pagina 404 può comparire a qualsiasi indirizzo: i link partono sempre dalla radice
        seo.append('<base href="/">')
    if noindex:
        seo.append('<meta name="robots" content="noindex, follow">')
    if url:
        seo.append(f'<link rel="canonical" href="{url}">')
        seo.append(f'<meta property="og:url" content="{url}">')
    seo_html = "\n  ".join(seo)
    schema_html = "\n  ".join(json_ld(s) for s in schemas if s)
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  {seo_html}
  <meta name="theme-color" content="#F3F7EF">
  <meta name="color-scheme" content="light only">
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="it_IT">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <!-- ✏️ Immagine per la condivisione sui social (1200×630 px), es.:
  <meta property="og:image" content="https://www.tuodominio.it/img/condivisione.jpg"> -->
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{FAVICON}">
  <link rel="stylesheet" href="/assets/style.css?v={ASSET_VERSION}">
  {schema_html}
</head>

<body>
  <a class="skip-link" href="#contenuto">Vai al contenuto</a>

{header(active)}

  <main id="contenuto">
{body}
  </main>

{footer()}
{tail(sticky_href)}
</body>
</html>
'''


# ======================================================================
# BLOCCHI RIUTILIZZATI
# ======================================================================

def faq_section(faq, title, intro, eyebrow="Domande frequenti"):
    items = "".join(
        f'''
            <details class="faq-item">
              <summary>{esc(q)}</summary>
              <div class="faq-answer"><p>{esc(a)}</p></div>
            </details>''' for q, a in faq
    )
    return f'''    <section class="faq" id="domande" aria-labelledby="faq-title">
      <div class="container">
        <div class="faq-panel">
          <div>
            <p class="eyebrow">{eyebrow}</p>
            <h2 class="section-title is-small" id="faq-title">{title}</h2>
            <p class="section-intro">{intro}</p>
          </div>
          <div class="faq-list">{items}
          </div>
        </div>
      </div>
    </section>'''


def article_card(a):
    return f'''<li><a class="article-card" href="/{a["slug"]}">
            <p class="article-tag">{GROUP_OF.get(a["slug"], "Guida")}</p>
            <h3>{a["card_title"]}</h3>
            <p class="article-card-text">{a["card_text"]}</p>
            <span class="article-more" aria-hidden="true">Leggi la guida →</span>
          </a></li>'''


def cta_band(title="Non sai ancora quale scegliere?",
             text="Rispondi a quattro domande e ti mostriamo i robot più adatti al tuo giardino, con prezzo e disponibilità aggiornati su Amazon.it.",
             secondary=("/guide", "Leggi le guide"), quiz_href="/#quiz"):
    sec = f'<a class="btn btn-ghost" href="{secondary[0]}">{secondary[1]}</a>' if secondary else ""
    return f'''    <section class="cta-band" aria-labelledby="cta-title">
      <div class="container">
        <div class="cta-panel">
          <div>
            <h2 id="cta-title">{title}</h2>
            <p>{text}</p>
          </div>
          <div class="cta-actions">
            <a class="btn btn-cta" href="{quiz_href}">Fai il quiz</a>
            {sec}
          </div>
        </div>
      </div>
    </section>'''


def author_box():
    return '''<div class="author-box" data-author-box hidden>
          <span class="author-avatar" data-author-avatar aria-hidden="true"></span>
          <div>
            <p class="author-label">Chi cura PratoSmart</p>
            <p class="author-name" data-author-name></p>
            <p class="author-bio" data-author-bio></p>
          </div>
        </div>'''


METHOD_VALUES = '''<ul class="values-grid">
          <li class="value">
            <span class="value-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5"/><path d="M4 19h16"/><path d="M8 15v-4"/><path d="M12 15V8"/><path d="M16 15v-6"/></svg>
            </span>
            <div>
              <h3>Partiamo dai dati</h3>
              <p>Confrontiamo le caratteristiche dichiarate dai produttori: superficie, pendenza, installazione e connettività.</p>
            </div>
          </li>
          <li class="value">
            <span class="value-icon is-sun" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>
            </span>
            <div>
              <h3>Ascoltiamo chi li usa</h3>
              <p>Leggiamo le opinioni degli acquirenti per capire pregi e limiti nell'uso di tutti i giorni.</p>
            </div>
          </li>
          <li class="value">
            <span class="value-icon is-sky" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7"/><path d="M21 4v5h-5"/></svg>
            </span>
            <div>
              <h3>Diciamo anche i limiti</h3>
              <p>Per ogni robot indichiamo quando è una buona scelta e quando conviene guardare altro. E aggiorniamo la selezione quando escono novità.</p>
            </div>
          </li>
        </ul>'''


# ======================================================================
# HOME
# ======================================================================

def build_home():
    all_guides = ""
    for name, slugs in GROUPS:
        cards = "".join(article_card(ARTICLE_BY_SLUG[s]) for s in slugs)
        all_guides += f'''
        <h3 class="home-guides-group">{name}</h3>
        <ul class="article-grid">{cards}</ul>'''
    body = f'''    <!-- ============ HERO ============ -->
    <section class="hero" aria-labelledby="hero-title">
      <div class="container">
        <div class="hero-banner">
          <div class="hero-scene" aria-hidden="true">
            <div class="scene-sun"></div>
            <div class="scene-cloud c1"></div>
            <div class="scene-cloud c2"></div>
            <div class="scene-lawn"></div>
            <div class="scene-robot">
              <div class="robot-flip">
                {ROBOT_SVG}
              </div>
            </div>
          </div>

          <div class="hero-content">
            <p class="eyebrow">Robot tagliaerba 2026 · Confronto e guide</p>
            <h1 id="hero-title">Il robot tagliaerba giusto per il tuo giardino, <em>senza sbagliare acquisto.</em></h1>
            <p class="hero-lead">Rispondi a quattro domande e scopri quale robot fa per te. Confronta i modelli con e senza filo perimetrale, leggi pregi e limiti, e verifica prezzo e disponibilità su Amazon.it.</p>
            <div class="hero-actions">
              <a class="btn btn-cta" href="#quiz">Trova il tuo robot {ARROW}</a>
              <a class="btn btn-ghost" href="#migliori">Le migliori scelte</a>
            </div>
            <p class="hero-note">
              <span>Quiz in 30 secondi</span>
              <span>Pregi e limiti di ogni robot</span>
              <span>Link diretti ad Amazon.it</span>
            </p>
          </div>

          <!-- Carosello: si riempie da solo con i prodotti che hanno link e foto -->
          <div class="carousel" id="hero-carousel" role="region" aria-roledescription="carosello" aria-label="Robot in evidenza">
            <div class="carousel-viewport">
              <div class="carousel-track" id="carousel-track" aria-live="off"></div>
            </div>
            <div class="carousel-controls" id="carousel-controls">
              <button class="carousel-btn" type="button" id="carousel-prev" aria-label="Robot precedente">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg>
              </button>
              <ul class="carousel-dots" id="carousel-dots" aria-label="Scegli il robot"></ul>
              <button class="carousel-btn" type="button" id="carousel-next" aria-label="Robot successivo">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>
              </button>
              <button class="carousel-btn" type="button" id="carousel-pause" aria-label="Metti in pausa lo scorrimento">
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" data-icon="pause"><rect x="7" y="6" width="3.2" height="12" rx="1"/><rect x="13.8" y="6" width="3.2" height="12" rx="1"/></svg>
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" data-icon="play" hidden><path d="M8 6.5v11a1 1 0 0 0 1.5.86l9-5.5a1 1 0 0 0 0-1.72l-9-5.5A1 1 0 0 0 8 6.5z"/></svg>
              </button>
            </div>
          </div>

          <!-- Illustrazione di riserva: compare solo finché nessun prodotto ha link e foto -->
          <div class="hero-illustration" aria-hidden="true">
            <div class="illo-disc">
              {ROBOT_SVG}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ VALORI ============ -->
    <section class="values" aria-label="Perché scegliere con PratoSmart">
      <div class="container">
        <ul class="values-grid">
          <li class="value">
            <span class="value-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18"/><path d="M6 20c0-4 1-7 3-9"/><path d="M12 20c0-5 0-9 2-12"/><path d="M18 20c0-3-1-6-3-8"/></svg>
            </span>
            <div>
              <h3>Per ogni giardino</h3>
              <p>Robot divisi per dimensione del prato, pendenza e tipo di installazione, per trovare subito quelli adatti a te.</p>
            </div>
          </li>
          <li class="value">
            <span class="value-icon is-sun" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
            </span>
            <div>
              <h3>Pregi e limiti, onestamente</h3>
              <p>Per ogni robot indichiamo quando è una buona scelta e quando conviene guardare altro.</p>
            </div>
          </li>
          <li class="value">
            <span class="value-icon is-sky" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7"/><path d="M9 7h8v8"/></svg>
            </span>
            <div>
              <h3>Prezzo aggiornato su Amazon</h3>
              <p>Ogni scheda porta alla pagina Amazon.it del robot, con prezzo, disponibilità e opinioni degli acquirenti.</p>
            </div>
          </li>
        </ul>
      </div>
    </section>

    <!-- ============ LE MIGLIORI SCELTE ============ -->
    <section class="picks" id="migliori" data-picks-section aria-labelledby="picks-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Confronto rapido</p>
            <h2 class="section-title" id="picks-title">Le migliori scelte del momento</h2>
          </div>
          <p class="section-intro">Un robot consigliato per ogni esigenza. Confronta i dati principali, poi apri la scheda per pregi, limiti e dettagli.</p>
        </div>
        {picks_table()}
      </div>
    </section>

    <!-- ============ QUIZ ============ -->
    <section class="quiz" id="quiz" aria-labelledby="quiz-title">
      <div class="container">
        <div class="quiz-panel">
          <div class="quiz-intro">
            <p class="eyebrow">Quiz · 30 secondi</p>
            <h2 class="section-title" id="quiz-title">Trova il robot giusto in quattro domande.</h2>
            <p>Dicci com'è il tuo giardino: ti mostriamo i robot della selezione più adatti, con il motivo di ogni consiglio.</p>
            <p class="quiz-privacy">Le risposte restano nel tuo browser: non salviamo e non inviamo nulla.</p>
          </div>
          <div class="quiz-box" id="quiz-box" aria-live="polite">
            <noscript><p>Per usare il quiz attiva JavaScript, oppure leggi la <a href="/come-scegliere-robot-tagliaerba">guida alla scelta</a>.</p></noscript>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ GUIDA PER DIMENSIONE ============ -->
    <section class="guide" id="guida" aria-labelledby="guide-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Guida rapida</p>
            <h2 class="section-title" id="guide-title">Quale robot fa per il tuo giardino?</h2>
          </div>
          <p class="section-intro">Parti dalla superficie del tuo prato: scegli un robot con una superficie massima dichiarata un po' più grande della tua.</p>
        </div>

        <ul class="guide-grid">
          <li class="guide-card">
            <div class="guide-visual s" aria-hidden="true"><span></span></div>
            <p class="guide-size">Fino a circa 500 m²</p>
            <h3>Giardino piccolo</h3>
            <p class="guide-text">Ideale per il prato di casa o un giardino a schiera.</p>
            <ul class="guide-tips">
              <li>Dimensioni compatte, facile da riporre</li>
              <li>Attenzione ai passaggi stretti</li>
              <li>Valuta un livello di rumore contenuto</li>
            </ul>
            <div class="guide-card-actions">
              <button class="btn btn-cta" type="button" data-guide-category="Giardini piccoli">Vedi i robot adatti</button>
              <a class="guide-link" href="/robot-tagliaerba-piccoli-giardini">Leggi la guida ai piccoli giardini</a>
            </div>
          </li>
          <li class="guide-card">
            <div class="guide-visual m" aria-hidden="true"><span></span></div>
            <p class="guide-size">Da 500 a 1.500 m² circa</p>
            <h3>Giardino medio</h3>
            <p class="guide-text">Per prati con aiuole, alberi e qualche zona da gestire.</p>
            <ul class="guide-tips">
              <li>App e Wi-Fi per programmare a distanza</li>
              <li>Controlla la pendenza massima supportata</li>
              <li>Utile il sensore pioggia</li>
            </ul>
            <div class="guide-card-actions">
              <button class="btn btn-cta" type="button" data-guide-category="Giardini medi">Vedi i robot adatti</button>
              <a class="guide-link" href="/robot-tagliaerba-giardini-medi">Leggi la guida ai giardini medi</a>
            </div>
          </li>
          <li class="guide-card">
            <div class="guide-visual l" aria-hidden="true"><span></span></div>
            <p class="guide-size">Oltre 1.500 m²</p>
            <h3>Giardino grande</h3>
            <p class="guide-text">Per grandi superfici, terreni irregolari o più zone separate.</p>
            <ul class="guide-tips">
              <li>Autonomia adeguata alla superficie</li>
              <li>Gestione di più zone di taglio</li>
              <li>Trazione adatta a terreni irregolari</li>
            </ul>
            <div class="guide-card-actions">
              <button class="btn btn-cta" type="button" data-guide-category="Giardini grandi">Vedi i robot adatti</button>
              <a class="guide-link" href="/robot-tagliaerba-giardini-grandi">Leggi la guida ai giardini grandi</a>
            </div>
          </li>
        </ul>

        <div class="guide-extra">
          <p><strong>Non vuoi installare il filo perimetrale?</strong> Alcuni robot si orientano con GPS RTK o con sensori visivi e si configurano dall'app.</p>
          <div class="guide-extra-actions">
            <button class="btn" type="button" data-guide-category="Senza filo perimetrale">Vedi i robot senza filo</button>
            <a class="btn btn-ghost" href="/robot-tagliaerba-senza-filo">Come funzionano</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ CATALOGO ============ -->
    <section class="catalog" id="prodotti" aria-labelledby="catalog-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">La selezione</p>
            <h2 class="section-title" id="catalog-title">Robot tagliaerba e accessori</h2>
            <p class="updated-note">Selezione aggiornata il <span data-catalog-date>{UPDATED_IT}</span></p>
          </div>
          <p class="section-intro">Apri “Scopri di più” per caratteristiche, pregi e limiti, poi verifica prezzo e disponibilità aggiornati su Amazon.it.</p>
        </div>
        <div class="product-grid" data-products></div>
      </div>
    </section>

    <!-- ============ TUTTE LE GUIDE ============ -->
    <section class="related" id="guide" aria-labelledby="hub-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Le guide</p>
            <h2 class="section-title" id="hub-title">Tutto quello che serve sapere prima di comprare</h2>
          </div>
          <p class="section-intro">Undici guide pratiche per scegliere, installare e far durare il tuo robot. <a href="/guide">Apri l'indice delle guide →</a></p>
        </div>{all_guides}
      </div>
    </section>

    <!-- ============ SEZIONE EDITORIALE ============ -->
    <section class="editorial" id="come-scegliere" aria-labelledby="editorial-title">
      <div class="container">
        <div class="editorial-panel">
          <div class="editorial-text">
            <p class="eyebrow">Prima di acquistare</p>
            <h2 class="section-title" id="editorial-title">Quattro cose da controllare nella scheda.</h2>
            <p>Un robot tagliaerba lavora al meglio quando è adatto al tuo giardino. Prima di scegliere, confronta questi quattro punti nella scheda Amazon del prodotto: sono indicati dal produttore e fanno la differenza.</p>
            <p>Vuoi approfondire? Leggi la <a href="/come-scegliere-robot-tagliaerba">guida completa alla scelta</a>.</p>
          </div>

          <ol class="checklist">
            <li><strong>Superficie massima</strong><span>Scegli un modello che copra un po' più metri quadrati del tuo prato.</span></li>
            <li><strong>Pendenza</strong><span>Se il terreno è in salita, controlla la pendenza massima supportata.</span></li>
            <li><strong>Installazione</strong><span>Con filo perimetrale oppure senza filo, con GPS RTK o sensori visivi.</span></li>
            <li><strong>App e connettività</strong><span>Wi-Fi, Bluetooth o rete mobile per programmare orari e zone dal telefono.</span></li>
          </ol>

          <p class="safety-note">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l9 16H3z"/><path d="M12 10v4"/><path d="M12 17v.01"/></svg>
            <span><strong>Sicurezza in giardino.</strong> Segui sempre le istruzioni del produttore. Tieni bambini e animali domestici lontani dal robot mentre lavora e programma il taglio di giorno: di notte molti piccoli animali selvatici, come i ricci, sono attivi nei prati.</span>
          </p>
        </div>
      </div>
    </section>

    <!-- ============ COME SCEGLIAMO ============ -->
    <section class="method" id="metodo" aria-labelledby="method-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Trasparenza</p>
            <h2 class="section-title" id="method-title">Come scegliamo i robot</h2>
          </div>
          <p class="section-intro">Una selezione è utile solo se sai come è stata fatta. <a href="/chi-siamo">Scopri chi siamo →</a></p>
        </div>
        {METHOD_VALUES}
        {author_box()}
      </div>
    </section>

{faq_section(HOME_FAQ, "I dubbi più comuni, chiariti.", "Le risposte valgono in generale: per il singolo modello fanno fede le indicazioni del produttore nella scheda Amazon.")}

{cta_band(quiz_href="#quiz")}'''

    schemas = [
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": SITE_NAME,
            "inLanguage": "it-IT",
            **({"url": SITE_URL + "/"} if SITE_URL else {}),
        },
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": SITE_NAME,
            **({"url": SITE_URL + "/"} if SITE_URL else {}),
        },
        faq_schema(HOME_FAQ),
    ]
    return page(
        slug="",
        title="Robot tagliaerba 2026: confronto, guide e quiz | PratoSmart",
        desc="Trova il robot tagliaerba giusto per il tuo giardino: quiz in 30 secondi, confronto tra modelli con e senza filo, guide pratiche e link diretti ad Amazon.it.",
        body=body,
        schemas=schemas,
        sticky_href="#quiz",
    )


# ======================================================================
# GUIDE
# ======================================================================

def plain_text(html_text):
    return re.sub(r"<[^>]+>", " ", html_text)


def reading_minutes(a):
    words = " ".join([a["lead"]] + a["tldr"] + [p[3] for p in a["body"] if p[0] == "s"] +
                     [q + " " + r for q, r in a["faq"]])
    return max(3, math.ceil(len(plain_text(words).split()) / 200))


def build_article(a):
    first_block = None
    for part in a["body"]:
        if part[0] == "b":
            m = re.search(r'<section class="(?:product-block|picks)" id="([^"]+)"', part[1])
            if m:
                first_block = m.group(1)
                break

    toc = "".join(f'<li><a href="#{p[1]}">{p[2]}</a></li>' for p in a["body"] if p[0] == "s")
    toc += '<li><a href="#domande">Domande frequenti</a></li>'

    sections = ""
    for part in a["body"]:
        if part[0] == "s":
            _, sid, title, content = part
            sections += f'''
    <section class="article-section" id="{sid}" aria-labelledby="{sid}-title">
      <div class="container">
        <div class="prose">
          <h2 id="{sid}-title">{title}</h2>
          {content.strip()}
        </div>
      </div>
    </section>'''
        else:
            sections += "\n    " + part[1]

    second_btn = (f'<a class="btn btn-ghost" href="#{first_block}">Vedi i robot consigliati</a>'
                  if first_block else "")
    related = "".join(article_card(ARTICLE_BY_SLUG[s]) for s in a["related"])

    body = f'''    <div class="container">
      <nav class="breadcrumb" aria-label="Percorso">
        <ol>
          <li><a href="/">Home</a></li>
          <li><a href="/guide">Guide</a></li>
          <li aria-current="page">{a["short"]}</li>
        </ol>
      </nav>

      <header class="article-hero">
        <p class="eyebrow">{a["eyebrow"]}</p>
        <h1>{a["h1"]}</h1>
        <p class="article-lead">{a["lead"]}</p>
        <p class="article-meta">
          <span>Aggiornato il <time datetime="{UPDATED_ISO}">{UPDATED_IT}</time></span>
          <span>Lettura: {reading_minutes(a)} min</span>
          <span>A cura di PratoSmart</span>
        </p>
        <div class="article-actions">
          <a class="btn btn-cta" href="/#quiz">Trova il tuo robot {ARROW}</a>
          {second_btn}
        </div>
      </header>

      <div class="article-intro">
        <aside class="tldr" aria-labelledby="tldr-title">
          <h2 id="tldr-title">In breve</h2>
          {check_list(a["tldr"])}
        </aside>
        <nav class="toc" aria-labelledby="toc-title">
          <h2 id="toc-title">In questa guida</h2>
          <ol>{toc}</ol>
        </nav>
      </div>
    </div>
{sections}

{faq_section(a["faq"], a["faq_title"], "Non trovi la risposta che cerchi? Il quiz in home ti aiuta a scegliere in base al tuo giardino.")}

    <section class="related" aria-labelledby="related-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Continua a leggere</p>
            <h2 class="section-title is-small" id="related-title">Guide collegate</h2>
          </div>
          <p class="section-intro"><a href="/guide">Vedi tutte le guide →</a></p>
        </div>
        <ul class="article-grid">{related}</ul>
      </div>
    </section>

{cta_band()}'''

    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["h1"],
        "description": a["desc"],
        "inLanguage": "it-IT",
        "datePublished": UPDATED_ISO,
        "dateModified": UPDATED_ISO,
        "author": {"@type": "Organization", "name": SITE_NAME},
        "publisher": {"@type": "Organization", "name": SITE_NAME},
        **({"mainEntityOfPage": SITE_URL + path_of(a["slug"])} if SITE_URL else {}),
    }
    return page(
        slug=a["slug"],
        title=a["title"],
        desc=a["desc"],
        body=body,
        schemas=[
            article_schema,
            faq_schema(a["faq"]),
            breadcrumb_schema([("Home", ""), ("Guide", "guide"), (a["short"], a["slug"])]),
        ],
        active=a["slug"],
        og_type="article",
    )


def build_hub():
    groups = ""
    for name, slugs in GROUPS:
        cards = "".join(article_card(ARTICLE_BY_SLUG[s]) for s in slugs)
        groups += f'''
    <section class="hub-group" aria-label="{esc(name)}">
      <div class="container">
        <h2>{name}</h2>
        <ul class="article-grid">{cards}</ul>
      </div>
    </section>'''

    body = f'''    <div class="container">
      <nav class="breadcrumb" aria-label="Percorso">
        <ol>
          <li><a href="/">Home</a></li>
          <li aria-current="page">Guide</li>
        </ol>
      </nav>
      <header class="article-hero">
        <p class="eyebrow">Guide · Aggiornate a {UPDATED_IT.split(" ", 1)[1]}</p>
        <h1>Guide ai robot tagliaerba</h1>
        <p class="article-lead">Come scegliere, quanto spendere, come installare e come far durare il tuo robot tagliaerba. Guide pratiche, scritte per chi vuole decidere con le idee chiare.</p>
        <div class="article-actions">
          <a class="btn btn-cta" href="/#quiz">Trova il tuo robot {ARROW}</a>
          <a class="btn btn-ghost" href="/#migliori">Le migliori scelte</a>
        </div>
      </header>
    </div>
    <div style="height: clamp(40px, 6vw, 64px)"></div>
{groups}

{cta_band(secondary=("/#migliori", "Le migliori scelte"))}'''

    return page(
        slug="guide",
        title="Guide ai robot tagliaerba 2026: scelta, costi, installazione",
        desc="Tutte le guide di PratoSmart sui robot tagliaerba: come scegliere, con o senza filo, giardini piccoli e grandi, pendenze, prezzi, installazione e manutenzione.",
        body=body,
        schemas=[breadcrumb_schema([("Home", ""), ("Guide", "guide")])],
        active="guide",
    )


# ======================================================================
# CHI SIAMO, PRIVACY, COOKIE, 404
# ======================================================================

def simple_hero(crumb, eyebrow, h1, lead, actions=True):
    act = f'''
        <div class="article-actions">
          <a class="btn btn-cta" href="/#quiz">Trova il tuo robot {ARROW}</a>
          <a class="btn btn-ghost" href="/guide">Leggi le guide</a>
        </div>''' if actions else ""
    return f'''    <div class="container">
      <nav class="breadcrumb" aria-label="Percorso">
        <ol>
          <li><a href="/">Home</a></li>
          <li aria-current="page">{crumb}</li>
        </ol>
      </nav>
      <header class="article-hero">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p class="article-lead">{lead}</p>{act}
      </header>
    </div>'''


def build_about():
    body = simple_hero(
        "Chi siamo", "Chi siamo",
        "Aiutiamo a scegliere il robot tagliaerba giusto",
        "PratoSmart è un sito indipendente con guide pratiche e una selezione di robot tagliaerba per giardini piccoli, medi e grandi. L'obiettivo è semplice: farti scegliere con le idee chiare, senza sbagliare acquisto.",
    ) + f'''
    <section class="method" style="padding-top: clamp(40px, 6vw, 64px)" aria-labelledby="method-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Il metodo</p>
            <h2 class="section-title is-small" id="method-title">Come scegliamo i robot</h2>
          </div>
          <p class="section-intro">Nessun modello entra nella selezione solo perché è popolare: deve essere una buona risposta a un'esigenza precisa.</p>
        </div>
        {METHOD_VALUES}
        <!-- ✏️ Compila authorName e authorBio in assets/products.js per mostrare questo riquadro.
             Se provi i robot di persona, raccontalo qui: è ciò che dà più fiducia.
             Non dichiarare test che non hai fatto. -->
        {author_box()}
      </div>
    </section>

    <section class="article-section" aria-labelledby="trasparenza-title">
      <div class="container">
        <div class="prose">
          <h2 id="trasparenza-title">Come si sostiene PratoSmart</h2>
          <p>PratoSmart partecipa al Programma Affiliazione Amazon EU. Quando acquisti un prodotto su Amazon.it dopo aver cliccato su “Verifica disponibilità”, riceviamo una piccola commissione. <strong>Per te il prezzo non cambia.</strong></p>
          <p>Le commissioni ci permettono di scrivere e aggiornare le guide, ma non decidono cosa consigliamo: per ogni robot indichiamo anche i limiti e le situazioni in cui conviene scegliere altro.</p>
          <p>Non mostriamo prezzi sul sito perché cambiano spesso: quelli corretti e aggiornati sono sempre sulla pagina Amazon del prodotto.</p>
          <h2>Contatti</h2>
          <p>Per segnalazioni, correzioni o domande puoi scrivere a <span data-owner="email"></span>.</p>
        </div>
      </div>
    </section>

{cta_band()}'''
    return page(
        slug="chi-siamo",
        title="Chi siamo e come scegliamo i robot | PratoSmart",
        desc="Chi c'è dietro PratoSmart, come selezioniamo i robot tagliaerba e come si sostiene il sito tramite il Programma Affiliazione Amazon.",
        body=body,
        schemas=[breadcrumb_schema([("Home", ""), ("Chi siamo", "chi-siamo")])],
    )


def build_privacy():
    body = simple_hero(
        "Privacy policy", "Informativa", "Informativa sulla privacy",
        "Quali dati vengono trattati quando visiti PratoSmart, perché e con quali diritti.",
        actions=False,
    ) + '''
    <section class="legal">
      <div class="container">
        <div class="prose">
          <p class="policy-meta">Ultimo aggiornamento: <span data-policy-date></span></p>
          <p>Questa informativa spiega quali dati personali vengono trattati quando visiti PratoSmart, ai sensi degli artt. 13 e 14 del Regolamento (UE) 2016/679 (“GDPR”) e del Codice in materia di protezione dei dati personali (D.Lgs. 196/2003, come modificato dal D.Lgs. 101/2018).</p>

          <div class="policy-summary">
            <ul>
              <li>PratoSmart non ha moduli, newsletter, account o carrello: <strong>non ti chiediamo alcun dato</strong>.</li>
              <li>Il quiz funziona solo nel tuo browser: le risposte non vengono salvate né inviate.</li>
              <li>Non usiamo cookie di profilazione, strumenti di statistica o pubblicità mirata.</li>
              <li>Gli acquisti avvengono interamente su Amazon.it, che tratta i tuoi dati in modo autonomo.</li>
            </ul>
          </div>

          <h2>1. Titolare del trattamento</h2>
          <p>Titolare del trattamento è <span data-owner="name"></span>. Per qualsiasi domanda o richiesta sulla privacy puoi scrivere a <span data-owner="email"></span>.</p>

          <h2>2. Dati di navigazione (hosting)</h2>
          <p>Il sito è ospitato da Vercel Inc. Come ogni servizio di hosting, i server registrano automaticamente alcuni dati tecnici necessari a mostrare le pagine e a proteggerle da abusi: indirizzo IP, data e ora della visita, pagina richiesta, tipo di browser e di dispositivo.</p>
          <ul>
            <li><strong>Finalità:</strong> funzionamento e sicurezza del sito.</li>
            <li><strong>Base giuridica:</strong> legittimo interesse del titolare a offrire un sito funzionante e sicuro (art. 6, par. 1, lett. f GDPR).</li>
            <li><strong>Conservazione:</strong> per il tempo strettamente necessario, secondo i periodi tecnici del fornitore di hosting.</li>
            <li><strong>Trasferimento fuori dall'UE:</strong> Vercel opera anche negli Stati Uniti. Il trasferimento avviene sulla base delle garanzie previste dagli artt. 45 e 46 GDPR, come il Data Privacy Framework UE-USA o le Clausole Contrattuali Standard. Maggiori dettagli nella <a href="https://vercel.com/legal/privacy-policy" target="_blank" rel="noopener noreferrer">privacy policy di Vercel</a>.</li>
          </ul>

          <h2>3. Foto dei prodotti e link affiliati Amazon</h2>
          <p>Le foto dei prodotti sono caricate direttamente dai server di Amazon: per mostrarle, il tuo browser comunica ad Amazon il tuo indirizzo IP e i dati tecnici della richiesta.</p>
          <p>PratoSmart partecipa al Programma Affiliazione Amazon EU, un programma di affiliazione che consente ai siti di percepire una commissione pubblicitaria pubblicizzando e fornendo link al sito Amazon.it. In qualità di Affiliato Amazon, il titolare riceve un guadagno dagli acquisti idonei.</p>
          <p>Quando clicchi su “Verifica disponibilità” vieni portato su Amazon.it. Da quel momento i tuoi dati sono trattati da Amazon come titolare autonomo, secondo l'<a href="https://www.amazon.it/gp/help/customer/display.html?nodeId=201909010" target="_blank" rel="noopener noreferrer">Informativa sulla privacy di Amazon.it</a>. Come previsto dal Programma Affiliazione, ti informiamo che terze parti, inclusa Amazon, possono mostrare contenuti, raccogliere informazioni direttamente dai visitatori e installare o riconoscere cookie sui loro browser, ad esempio per attribuire un acquisto al link da cui proviene. Da Amazon riceviamo soltanto report aggregati sulle vendite, che non permettono di identificarti.</p>

          <h2>4. Memoria locale del browser</h2>
          <p>Per non mostrarti ogni volta l'avviso sui cookie, il sito salva nel tuo browser (localStorage) un'informazione tecnica che indica che lo hai già chiuso. Non contiene dati personali, non viene inviata a nessun server e puoi cancellarla in qualsiasi momento dalle impostazioni del browser.</p>

          <h2>5. Chi può ricevere i dati</h2>
          <ul>
            <li>Vercel Inc., fornitore di hosting, che agisce come responsabile del trattamento (art. 28 GDPR).</li>
            <li>Amazon, come titolare autonomo, per le foto dei prodotti e per tutto ciò che avviene su Amazon.it.</li>
          </ul>
          <p>I dati non vengono venduti né usati per profilazione o pubblicità.</p>

          <h2>6. I tuoi diritti</h2>
          <p>Puoi chiedere in qualsiasi momento l'accesso ai tuoi dati, la rettifica, la cancellazione, la limitazione del trattamento, la portabilità e opporti al trattamento basato sul legittimo interesse (artt. 15–22 GDPR), scrivendo all'indirizzo indicato al punto 1. Poiché il sito non raccoglie dati che permettono di identificarti direttamente, potremmo chiederti alcune informazioni per individuare i dati che ti riguardano (art. 11 GDPR).</p>
          <p>Hai inoltre il diritto di proporre reclamo al Garante per la protezione dei dati personali (<a href="https://www.garanteprivacy.it" target="_blank" rel="noopener noreferrer">www.garanteprivacy.it</a>).</p>

          <h2>7. Modifiche</h2>
          <p>Questa informativa può essere aggiornata, ad esempio se cambiano i servizi utilizzati dal sito. La data dell'ultimo aggiornamento è indicata in alto. Leggi anche la <a href="/cookie-policy">cookie policy</a>.</p>
        </div>
      </div>
    </section>'''
    return page(
        slug="privacy",
        title="Privacy policy | PratoSmart",
        desc="Informativa sulla privacy di PratoSmart: quali dati vengono trattati, perché, chi li riceve e quali sono i tuoi diritti secondo il GDPR.",
        body=body,
        sticky_href=None,
    )


def build_cookie():
    body = simple_hero(
        "Cookie policy", "Informativa", "Cookie policy",
        "PratoSmart non usa cookie di profilazione, di statistica o di marketing. Ecco cosa salva il sito e cosa succede quando vai su Amazon.it.",
        actions=False,
    ) + '''
    <section class="legal">
      <div class="container">
        <div class="prose">
          <p class="policy-meta">Ultimo aggiornamento: <span data-policy-date></span></p>
          <p>Questa cookie policy è redatta ai sensi dell'art. 122 del Codice in materia di protezione dei dati personali e delle Linee guida del Garante Privacy sui cookie e altri strumenti di tracciamento del 10 giugno 2021.</p>

          <div class="policy-summary">
            <ul>
              <li><strong>PratoSmart non installa cookie di profilazione, di statistica o di marketing.</strong></li>
              <li>Usa un solo strumento tecnico, che non richiede il tuo consenso.</li>
              <li>Su Amazon.it valgono i cookie e le scelte di Amazon.</li>
            </ul>
          </div>

          <h2>Cosa sono i cookie</h2>
          <p>I cookie e gli strumenti simili, come la memoria locale del browser, sono piccole informazioni che un sito salva sul tuo dispositivo. Quelli <em>tecnici</em> servono a far funzionare il sito e non richiedono consenso. Quelli di <em>profilazione</em> o di <em>statistica non anonima</em> possono essere usati solo con il tuo consenso preventivo.</p>

          <h2>Strumenti usati da PratoSmart</h2>
          <div class="policy-table-wrap">
            <table class="policy-table">
              <thead>
                <tr><th scope="col">Nome</th><th scope="col">Tipo</th><th scope="col">Finalità</th><th scope="col">Durata</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>pratosmart-cookie-notice</code></td>
                  <td>Tecnico, memoria locale del browser (localStorage), prima parte</td>
                  <td>Ricorda che hai chiuso l'avviso sui cookie, per non mostrartelo a ogni visita</td>
                  <td>Fino a quando non lo cancelli dal browser</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p>Il sito non utilizza cookie di terze parti, strumenti di analisi, pixel pubblicitari o pulsanti social. Le foto dei prodotti sono caricate dai server di Amazon senza l'uso di cookie.</p>

          <h2>Quando clicchi su un prodotto</h2>
          <p>Il pulsante “Verifica disponibilità” ti porta su Amazon.it tramite un link di affiliazione. Su Amazon.it vengono usati i cookie di Amazon, anche per attribuire l'eventuale acquisto al nostro link, secondo l'<a href="https://www.amazon.it/gp/help/customer/display.html?nodeId=201890250" target="_blank" rel="noopener noreferrer">Informativa su cookie e pubblicità di Amazon</a>. Puoi gestire le tue preferenze direttamente su Amazon.it.</p>

          <h2>Come gestire o cancellare i cookie</h2>
          <p>Puoi cancellare i dati salvati e bloccare i cookie dalle impostazioni del tuo browser:</p>
          <ul>
            <li><a href="https://support.google.com/chrome/answer/95647?hl=it" target="_blank" rel="noopener noreferrer">Google Chrome</a></li>
            <li><a href="https://support.apple.com/it-it/guide/safari/sfri11471/mac" target="_blank" rel="noopener noreferrer">Safari</a></li>
            <li><a href="https://support.mozilla.org/it/kb/Attivare%20e%20disattivare%20i%20cookie" target="_blank" rel="noopener noreferrer">Mozilla Firefox</a></li>
            <li><a href="https://support.microsoft.com/it-it/microsoft-edge/eliminare-i-cookie-in-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09" target="_blank" rel="noopener noreferrer">Microsoft Edge</a></li>
          </ul>

          <h2>Titolare e contatti</h2>
          <p>Titolare del trattamento è <span data-owner="name"></span> (<span data-owner="email"></span>). Per sapere di più sui tuoi dati e sui tuoi diritti leggi l'<a href="/privacy">informativa sulla privacy</a>.</p>
        </div>
      </div>
    </section>'''
    return page(
        slug="cookie-policy",
        title="Cookie policy | PratoSmart",
        desc="Cookie policy di PratoSmart: il sito non usa cookie di profilazione, statistica o marketing. Scopri quale strumento tecnico usa e come gestirlo.",
        body=body,
        sticky_href=None,
    )


def build_404():
    cards = "".join(article_card(ARTICLE_BY_SLUG[s]) for s in HOME_FEATURED[:3])
    body = f'''    <div class="container page-404">
      <p class="eyebrow">Errore 404</p>
      <h1>Questa pagina si è persa nell'erba alta.</h1>
      <p>Il link potrebbe essere sbagliato o la pagina potrebbe essere stata spostata. Riparti da qui:</p>
      <div class="article-actions">
        <a class="btn btn-cta" href="/#quiz">Trova il tuo robot {ARROW}</a>
        <a class="btn btn-ghost" href="/">Torna alla home</a>
      </div>
    </div>
    <section class="related" aria-label="Guide consigliate">
      <div class="container">
        <ul class="article-grid">{cards}</ul>
      </div>
    </section>'''
    return page(
        slug="404",
        title="Pagina non trovata | PratoSmart",
        desc="La pagina che cerchi non esiste. Torna alla home di PratoSmart o leggi le guide sui robot tagliaerba.",
        body=body,
        noindex=True,
        base_root=True,
    )


# ======================================================================
# SITEMAP, ROBOTS E SCRITTURA DEI FILE
# ======================================================================

def build_sitemap():
    base = SITE_URL or "https://IL-TUO-DOMINIO.it"
    pages = [("", "1.0"), ("guide", "0.8")] + [(a["slug"], "0.8") for a in ARTICLES] + \
            [("chi-siamo", "0.4"), ("privacy", "0.2"), ("cookie-policy", "0.2")]
    urls = "".join(
        f"\n  <url>\n    <loc>{base}{path_of(slug)}</loc>\n    <lastmod>{UPDATED_ISO}</lastmod>\n    <priority>{prio}</priority>\n  </url>"
        for slug, prio in pages
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}\n</urlset>\n'


def build_robots():
    base = SITE_URL or "https://IL-TUO-DOMINIO.it"
    return f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n"


def write(name, content):
    if name.endswith(".html"):
        content = relative_links(content, is_home=(name == "index.html"))
    path = os.path.join(ROOT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("scritto", name)


def main():
    write("index.html", build_home())
    write("guide.html", build_hub())
    for a in ARTICLES:
        write(a["slug"] + ".html", build_article(a))
    write("chi-siamo.html", build_about())
    write("privacy.html", build_privacy())
    write("cookie-policy.html", build_cookie())
    write("404.html", build_404())
    write("sitemap.xml", build_sitemap())
    write("robots.txt", build_robots())
    if not SITE_URL:
        print("\nATTENZIONE: SITE_URL è vuoto. Sitemap e robots.txt usano un dominio segnaposto;\n"
              "canonical e breadcrumb strutturato non sono stati generati.")


if __name__ == "__main__":
    main()
