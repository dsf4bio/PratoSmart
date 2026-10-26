# PratoSmart — istruzioni rapide

## Cosa modificare (e dove)

| Cosa | File |
|---|---|
| Prodotti, link affiliati, foto, dati tecnici, badge | `assets/products.js` |
| Nome ed email del titolare (privacy), autore, date, barra Black Friday | `assets/products.js` → `SITE_CONFIG` |
| Testi delle guide | `_sorgente/guide.py`, poi rigenera le pagine |
| Colori e stile | `assets/style.css` |

Prodotti e configurazione si aggiornano su tutte le pagine **senza rigenerare nulla**.

## Rigenerare le pagine HTML

Serve solo se cambi i testi in `_sorgente/` o il dominio:

```
python3 _sorgente/genera_sito.py
```

## Prima di pubblicare

1. Compila `affiliateUrl`, `images` e `specs` (almeno `area` e `slope`) in `assets/products.js`.
2. Compila `ownerName` e `ownerEmail` in `SITE_CONFIG`.
3. Scrivi il tuo dominio in `SITE_URL` dentro `_sorgente/genera_sito.py` e rigenera:
   così sitemap, robots.txt e canonical usano l'indirizzo giusto.
4. Pubblica la cartella su Vercel. I link sono relativi (`guide.html`, `index.html#quiz`):
   il sito funziona uguale anche aprendo `index.html` dal computer o con Live Server in VS Code.
5. Registra il sito su Google Search Console e invia `https://tuodominio/sitemap.xml`.
