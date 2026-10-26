/* ==================================================================
   ✏️ PRATOSMART — CATALOGO E CONFIGURAZIONE
   Questo è l'UNICO file da modificare per prodotti, link e dati del sito.
   Tutte le pagine (home e guide) leggono i prodotti da qui:
   tabella "Le migliori scelte", quiz, carosello e schede si aggiornano da sole.
   ================================================================== */
'use strict';

/* ================================================================
   1. PRODOTTI
   ----------------------------------------------------------------
   Per ogni prodotto:

   - id           → codice unico, senza spazi (es. "navimow-i105e")
   - title        → nome mostrato. USA MARCA E MODELLO VERI
                    (es. "Segway Navimow i105E"): è ciò che la gente cerca su Google.
   - category     → una delle categorie in CATEGORIES (più in basso).
                    Decide in quali guide compare il prodotto:
                      "Giardini piccoli"       → guida piccoli giardini
                      "Giardini medi"          → guida giardini medi
                      "Giardini grandi"        → guida giardini grandi
                      "Senza filo perimetrale" → guida robot senza filo
                      "Accessori"              → guide installazione e manutenzione
   - badge        → etichetta in evidenza (es. "Miglior scelta"). Se la compili,
                    il prodotto entra nella tabella "Le migliori scelte".
                    Lascia "" per non metterlo in tabella.
   - budget       → fascia di spesa: "base", "medio" oppure "alto".
                    Serve al quiz e alla guida "Quanto costa".
                    NON scrivere prezzi: Amazon non lo consente senza le sue API.
   - specs        → dati dichiarati dal produttore (copiali dalla scheda Amazon):
        area         superficie massima in m², solo il numero (es. 600)
        slope        pendenza massima in %, solo il numero (es. 45)
        navigation   tipo di installazione (es. "Filo perimetrale", "GPS RTK senza filo")
        connectivity app e connessione (es. "Wi-Fi + Bluetooth")
        noise        rumore in dB, solo il numero (es. 58)
        cutHeight    altezza di taglio (es. "20–60 mm")
      Lascia null o "" i dati che non conosci: non vengono mostrati.
      Superficie e pendenza rendono il quiz molto più preciso.
   - tags         → parole chiave facoltative per comparire in guide specifiche:
                      "pendenza" → compare nella guida ai terreni in pendenza
   - description  → descrizione (toni prudenti). Nella scheda se ne vedono le prime
                    righe: il resto si apre con "Scopri di più".
   - benefits     → 2 o 3 caratteristiche
   - idealFor     → "Ideale se…": 1–3 situazioni in cui è una buona scelta
   - notFor       → "Lascia perdere se…": 1–2 limiti onesti (aumentano la fiducia)
   - affiliateUrl → il TUO link affiliato (https://...)
   - images       → fino a 3 foto. La prima è la principale.
                    Usa preferibilmente le immagini fornite da SiteStripe di Amazon.
                    Lascia "" le foto che non hai: vengono ignorate.

   I dati qui sotto sono ESEMPI: sostituiscili con i robot reali e verifica
   che testi e dati corrispondano al modello scelto.
   L'ordine dell'elenco è l'ordine in cui i prodotti compaiono nelle pagine.
   ================================================================ */
const products = [
  {
    id: "robot-compatto-piccoli",
    title: "Robot tagliaerba compatto per piccoli giardini",
    category: "Giardini piccoli",
    badge: "Per piccoli giardini",
    budget: "base",
    specs: { area: null, slope: null, navigation: "Filo perimetrale", connectivity: "", noise: null, cutHeight: "" },
    tags: [],
    description: "Un robot dalle dimensioni contenute, pensato per prati di casa e giardini a schiera. Si installa con filo perimetrale e lavora secondo gli orari che imposti.",
    benefits: ["Ingombro ridotto, facile da riporre", "Programmazione degli orari di taglio", "Rientro automatico alla base di ricarica"],
    idealFor: ["Hai un prato piccolo e regolare", "Vuoi spendere il giusto"],
    notFor: ["Il tuo prato supera i 500 m²", "Non vuoi posare il filo perimetrale"],
    affiliateUrl: "https://link.amazon/B04JUBOqt",
    images: [
      "https://m.media-amazon.com/images/I/91eUJ5kU2TL._AC_SL1500_.jpg",
      "https://m.media-amazon.com/images/I/81kS0m3AKoL._AC_SL1500_.jpg",
      "https://m.media-amazon.com/images/I/91lebOIaLoL._AC_SL1500_.jpg"
    ]
  },
  {
    id: "robot-app-piccoli",
    title: "Robot tagliaerba con app per giardini piccoli",
    category: "Giardini piccoli",
    badge: "",
    budget: "base",
    specs: { area: null, slope: null, navigation: "", connectivity: "", noise: null, cutHeight: "" },
    tags: [],
    description: "Si controlla dallo smartphone: avvio, pausa e orari di taglio a portata di app. Una soluzione semplice per chi vuole gestire il prato anche quando non è a casa.",
    benefits: ["Controllo da app", "Altezza di taglio regolabile", "Avvisi sullo stato del robot"],
    idealFor: ["Vuoi gestire tutto dallo smartphone", "Il prato è piccolo"],
    notFor: ["Il Wi-Fi non arriva in giardino"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-silenzioso-piccoli",
    title: "Robot tagliaerba per giardini cittadini",
    category: "Giardini piccoli",
    badge: "",
    budget: "base",
    specs: { area: null, slope: null, navigation: "", connectivity: "", noise: null, cutHeight: "" },
    tags: [],
    description: "Pensato per i giardini vicini alle abitazioni: controlla nella scheda il livello sonoro dichiarato dal produttore per scegliere un modello discreto.",
    benefits: ["Adatto a spazi contenuti", "Funzionamento programmabile", "Lame facili da sostituire"],
    idealFor: ["Hai vicini di casa a pochi metri", "Vuoi un robot discreto"],
    notFor: ["Il terreno ha forti pendenze"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-wifi-medi",
    title: "Robot tagliaerba Wi-Fi per giardini medi",
    category: "Giardini medi",
    badge: "Miglior scelta",
    budget: "medio",
    specs: { area: null, slope: null, navigation: "", connectivity: "Wi-Fi", noise: null, cutHeight: "" },
    tags: [],
    description: "Un robot connesso per prati di media grandezza, con aiuole e alberi. Dall'app puoi impostare orari, zone e altezza di taglio.",
    benefits: ["Connessione Wi-Fi e app dedicata", "Gestione degli orari settimanali", "Sensori per aggirare gli ostacoli"],
    idealFor: ["Hai un prato con aiuole e alberi", "Vuoi programmare tutto dall'app"],
    notFor: ["Il Wi-Fi di casa non copre il giardino"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-pendenze-medi",
    title: "Robot tagliaerba per terreni in pendenza",
    category: "Giardini medi",
    badge: "",
    budget: "medio",
    specs: { area: null, slope: null, navigation: "", connectivity: "", noise: null, cutHeight: "" },
    tags: ["pendenza"],
    description: "Per giardini con salite e dislivelli: verifica nella scheda la pendenza massima supportata e confrontala con quella del tuo prato.",
    benefits: ["Ruote con buona aderenza", "Pensato per terreni non piani", "Programmazione da app o da pannello"],
    idealFor: ["Il giardino ha salite e dislivelli"],
    notFor: ["Il prato è in piano: puoi spendere meno"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-sensore-pioggia-medi",
    title: "Robot tagliaerba con sensore pioggia",
    category: "Giardini medi",
    badge: "",
    budget: "medio",
    specs: { area: null, slope: null, navigation: "", connectivity: "", noise: null, cutHeight: "" },
    tags: [],
    description: "Quando inizia a piovere torna alla base e riprende il lavoro più tardi: utile per proteggere il prato e il robot nei giorni di maltempo.",
    benefits: ["Sensore pioggia", "Rientro automatico alla base", "Taglio regolare durante la stagione"],
    idealFor: ["Vivi in una zona piovosa", "Vuoi un robot che si gestisca da solo"],
    notFor: ["Ti serve gestire più zone separate"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-grandi-superfici",
    title: "Robot tagliaerba per grandi superfici",
    category: "Giardini grandi",
    badge: "",
    budget: "alto",
    specs: { area: null, slope: null, navigation: "", connectivity: "", noise: null, cutHeight: "" },
    tags: [],
    description: "Pensato per prati ampi: confronta nella scheda la superficie massima dichiarata, l'autonomia della batteria e i tempi di ricarica.",
    benefits: ["Adatto a superfici estese", "Batteria pensata per sessioni lunghe", "Gestione di più zone"],
    idealFor: ["Hai un prato molto ampio"],
    notFor: ["Il giardino è piccolo: paghi capacità che non usi"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-4wd-grandi",
    title: "Robot tagliaerba a trazione integrale (4WD)",
    category: "Giardini grandi",
    badge: "Per pendenze impegnative",
    budget: "alto",
    specs: { area: null, slope: null, navigation: "", connectivity: "", noise: null, cutHeight: "" },
    tags: ["pendenza"],
    description: "La trazione su quattro ruote aiuta su terreni irregolari e pendenze impegnative. Una scelta da valutare per giardini grandi e articolati.",
    benefits: ["Trazione integrale", "Pensato per terreni irregolari", "Struttura robusta"],
    idealFor: ["Il terreno è irregolare o molto in pendenza", "Il giardino è grande e articolato"],
    notFor: ["Il prato è piccolo e in piano"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-multizona-grandi",
    title: "Robot tagliaerba multizona",
    category: "Giardini grandi",
    badge: "",
    budget: "alto",
    specs: { area: null, slope: null, navigation: "", connectivity: "", noise: null, cutHeight: "" },
    tags: [],
    description: "Per giardini divisi in più aree, ad esempio davanti e dietro casa: dall'app puoi definire le zone e decidere quando tagliare ciascuna.",
    benefits: ["Gestione di più zone di taglio", "Programmazione per singola area", "Controllo da app"],
    idealFor: ["Il giardino è diviso in più aree"],
    notFor: ["Hai un unico prato piccolo"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-rtk-senza-filo",
    title: "Robot tagliaerba senza filo con GPS RTK",
    category: "Senza filo perimetrale",
    badge: "Miglior senza filo",
    budget: "alto",
    specs: { area: null, slope: null, navigation: "GPS RTK, senza filo", connectivity: "", noise: null, cutHeight: "" },
    tags: [],
    description: "Si orienta con il posizionamento satellitare RTK: i confini del prato si disegnano dall'app, senza interrare il filo perimetrale.",
    benefits: ["Nessun filo perimetrale da posare", "Confini e zone definiti da app", "Taglio a linee ordinate"],
    idealFor: ["Non vuoi posare il filo perimetrale", "Vuoi un taglio a strisce ordinate"],
    notFor: ["Il prato è coperto da alberi fitti o vicino a muri alti (il segnale satellitare può soffrirne)"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-visione-senza-filo",
    title: "Robot tagliaerba senza filo con visione AI",
    category: "Senza filo perimetrale",
    badge: "",
    budget: "medio",
    specs: { area: null, slope: null, navigation: "Visione AI, senza filo", connectivity: "", noise: null, cutHeight: "" },
    tags: [],
    description: "Usa telecamere e sensori per riconoscere il prato e gli ostacoli. Verifica nella scheda i requisiti di installazione indicati dal produttore.",
    benefits: ["Riconoscimento visivo degli ostacoli", "Installazione semplificata", "Gestione da app"],
    idealFor: ["Il giardino ha molti ostacoli", "Vuoi un'installazione rapida"],
    notFor: ["Il prato non ha bordi ben definiti"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "robot-mappatura-senza-filo",
    title: "Robot senza filo con mappatura via app",
    category: "Senza filo perimetrale",
    badge: "",
    budget: "medio",
    specs: { area: null, slope: null, navigation: "Senza filo, mappatura da app", connectivity: "", noise: null, cutHeight: "" },
    tags: [],
    description: "Crea la mappa del giardino accompagnando il robot lungo i bordi con lo smartphone, poi lavora in autonomia secondo i tuoi orari.",
    benefits: ["Mappa del giardino nell'app", "Zone vietate impostabili", "Aggiornamenti tramite app"],
    idealFor: ["Vuoi escludere aiuole e orto dall'app"],
    notFor: ["Preferisci un robot senza app"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "garage-robot",
    title: "Garage per robot tagliaerba",
    category: "Accessori",
    badge: "",
    tags: [],
    description: "Una copertura per la base di ricarica che ripara il robot da sole e pioggia e lo rende più ordinato da vedere in giardino.",
    benefits: ["Protegge da sole e pioggia", "Si monta sopra la base", "Verifica la compatibilità con il tuo modello"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "lame-ricambio",
    title: "Lame di ricambio per robot tagliaerba",
    category: "Accessori",
    badge: "",
    tags: [],
    description: "Lame affilate aiutano a ottenere un taglio più pulito. Scegli il set compatibile con la marca e il modello del tuo robot.",
    benefits: ["Per un taglio più netto", "Confezione con più lame", "Controlla la compatibilità"],
    affiliateUrl: "",
    images: ["", "", ""]
  },
  {
    id: "kit-filo-perimetrale",
    title: "Kit filo perimetrale e picchetti",
    category: "Accessori",
    badge: "",
    tags: [],
    description: "Per installare o ampliare il perimetro di lavoro dei robot con filo: utile anche per riparazioni o per aggiungere nuove zone.",
    benefits: ["Filo e picchetti di fissaggio", "Utile per ampliare il perimetro", "Verifica la compatibilità"],
    affiliateUrl: "",
    images: ["", "", ""]
  }
];

/* ================================================================
   2. CONFIGURAZIONE DEL SITO
   ================================================================ */
const SITE_CONFIG = {
  // Dati del titolare per privacy e cookie policy (obbligatori per il GDPR)
  ownerName: "",                     // es. "Mario Rossi (PratoSmart)"
  ownerEmail: "",                    // es. "pratosmart.privacy@gmail.com"
  policyUpdated: "26 ottobre 2026",  // data dell'ultimo aggiornamento delle informative
  cookieNoticeVersion: "2026-10-26", // cambiala se modifichi l'avviso: il banner ricomparirà a tutti

  // Data mostrata sopra il catalogo: aggiornala quando cambi i prodotti
  catalogUpdated: "26 ottobre 2026",

  // Riquadro "Chi cura PratoSmart": compare solo se compili authorName
  authorName: "",                    // es. "Mario Rossi"
  authorBio: "",                     // es. "Ho un giardino di 800 m² in collina e uso un robot tagliaerba dal 2021."

  // Messaggio stagionale nella barra in alto, mostrato solo tra start e end (formato AAAA-MM-GG).
  // Usa date reali: niente finti conti alla rovescia, vietati dal Programma Affiliazione.
  seasonal: {
    start: "2026-11-01",
    end: "2026-12-01",
    text: "Black Friday 2026",
    linkText: "come riconoscere le offerte vere sui robot tagliaerba",
    href: "robot-tagliaerba-black-friday.html"
  }
};

/* ================================================================
   3. CATEGORIE
   "label" deve coincidere con il campo "category" dei prodotti.
   "tint" è il colore del segnaposto quando manca la foto.
   ================================================================ */
const CATEGORIES = [
  { label: "Giardini piccoli",       tint: "#DCEFD2" },
  { label: "Giardini medi",          tint: "#C9E6BB" },
  { label: "Giardini grandi",        tint: "#B5DCA3" },
  { label: "Senza filo perimetrale", tint: "#D6ECF5" },
  { label: "Accessori",              tint: "#FBEBC2" }
];

/* ================================================================
   4. DOMANDE DEL QUIZ (in home)
   Puoi cambiare i testi. Non cambiare "key" e "value":
   servono a calcolare i consigli.
   ================================================================ */
const QUIZ = [
  {
    key: "area",
    question: "Quanto è grande il tuo prato?",
    hint: "Non lo sai? Moltiplica lunghezza per larghezza in metri: basta una stima.",
    options: [
      { label: "Fino a 500 m²", value: 500 },
      { label: "Da 500 a 1.500 m²", value: 1500 },
      { label: "Da 1.500 a 3.000 m²", value: 3000 },
      { label: "Oltre 3.000 m²", value: 5000 }
    ]
  },
  {
    key: "slope",
    question: "Il terreno è in pendenza?",
    hint: "Una pendenza del 25% significa salire di 25 cm ogni metro.",
    options: [
      { label: "Quasi in piano", value: 10 },
      { label: "Qualche salita leggera", value: 25 },
      { label: "Salite impegnative", value: 45 }
    ]
  },
  {
    key: "wire",
    question: "Vuoi evitare il filo perimetrale?",
    hint: "Senza filo non devi posare un cavo lungo i bordi del prato.",
    options: [
      { label: "Sì, niente filo", value: "no-wire" },
      { label: "Il filo va bene", value: "wire" },
      { label: "Non so, consigliami tu", value: "any" }
    ]
  },
  {
    key: "budget",
    question: "Che fascia di spesa hai in mente?",
    hint: "I prezzi aggiornati sono solo su Amazon.it: qui ragioniamo per fasce.",
    options: [
      { label: "Contenuta", value: "base" },
      { label: "Media", value: "medio" },
      { label: "Alta, voglio il massimo", value: "alto" },
      { label: "Indifferente", value: "any" }
    ]
  }
];
