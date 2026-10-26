"""Blocchi HTML riutilizzabili nelle pagine di PratoSmart."""
import html
import itertools

_block_ids = itertools.count(1)

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>')


def esc(text):
    return html.escape(text, quote=True)


def check_list(items):
    return '<ul class="check-list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def table(headers, rows, caption=""):
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = ""
    for row in rows:
        cells = f'<th scope="row">{row[0]}</th>' + "".join(f"<td>{c}</td>" for c in row[1:])
        body += f"<tr>{cells}</tr>"
    cap = f"<caption>{caption}</caption>" if caption else ""
    return (f'<div class="data-table-wrap"><table class="data-table">{cap}'
            f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>")


def callout(title, text, warn=False):
    kind = " is-warn" if warn else ""
    return f'<div class="callout{kind}"><p><strong class="callout-title">{title}</strong>{text}</p></div>'


def inline_cta(title="Trova il robot giusto in 30 secondi",
               text="Rispondi a quattro domande sul tuo giardino: ti mostriamo i robot della selezione più adatti, con il motivo di ogni consiglio.",
               href="/#quiz", label="Fai il quiz"):
    return (f'<div class="inline-cta"><p><strong>{title}</strong>{text}</p>'
            f'<a class="btn btn-cta" href="{href}">{label} {ARROW}</a></div>')


def products_block(eyebrow, title, intro, **filters):
    """Griglia di prodotti filtrata (vedi i data-* descritti in assets/site.js).
    Se nessun prodotto corrisponde ai filtri, il blocco si nasconde da solo."""
    block_id = f"robot-{next(_block_ids)}"
    attrs = " ".join(f'data-{key}="{esc(str(value))}"' for key, value in filters.items())
    return f'''<section class="product-block" id="{block_id}" data-product-block aria-labelledby="{block_id}-title">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">{eyebrow}</p>
        <h2 class="section-title is-small" id="{block_id}-title">{title}</h2>
      </div>
      <p class="section-intro">{intro}</p>
    </div>
    <div class="product-grid" data-products {attrs}></div>
  </div>
</section>'''


def picks_table(ids=""):
    ids_attr = f' data-ids="{esc(ids)}"' if ids else ""
    return f'''<div class="picks-table-wrap">
      <table class="picks-table">
        <caption class="visually-hidden">Confronto dei robot tagliaerba consigliati</caption>
        <thead>
          <tr>
            <th scope="col">Robot</th>
            <th scope="col">Superficie</th>
            <th scope="col">Pendenza</th>
            <th scope="col">Installazione</th>
            <th scope="col">App</th>
            <th scope="col"><span class="visually-hidden">Acquisto</span></th>
          </tr>
        </thead>
        <tbody data-picks{ids_attr}></tbody>
      </table>
    </div>
    <p class="picks-note">Dati dichiarati dai produttori: verificali sempre nella scheda Amazon prima dell'acquisto.</p>'''


def picks_block(eyebrow, title, intro, ids="", block_id=None):
    """Tabella "Le migliori scelte": prodotti con badge, oppure gli id indicati."""
    block_id = block_id or f"robot-{next(_block_ids)}"
    return f'''<section class="picks" id="{block_id}" data-picks-section aria-labelledby="{block_id}-title">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">{eyebrow}</p>
        <h2 class="section-title is-small" id="{block_id}-title">{title}</h2>
      </div>
      <p class="section-intro">{intro}</p>
    </div>
    {picks_table(ids)}
  </div>
</section>'''
