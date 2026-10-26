"""
Testi delle guide di PratoSmart.

Ogni guida è un dizionario:
- slug        indirizzo della pagina (es. /robot-tagliaerba-senza-filo)
- short       nome breve per il percorso di navigazione (breadcrumb)
- card_title, card_text   testo della scheda nelle pagine "Guide"
- title, desc  titolo e descrizione per Google (title ~60 caratteri, desc ~155)
- eyebrow, h1, lead       intestazione della pagina
- tldr        punti del riquadro "In breve"
- body        elenco di sezioni:
                ("s", id, titolo, html)  sezione di testo (compare nell'indice)
                ("b", html)              blocco a tutta larghezza (prodotti, tabelle)
- faq_title, faq          domande frequenti (testo semplice)
- related     slug di 3 guide collegate
"""
from componenti import table, callout, inline_cta, check_list, products_block, picks_block

ARTICLES = [
    # ------------------------------------------------------------------
    {
        "slug": "come-scegliere-robot-tagliaerba",
        "short": "Come scegliere",
        "card_title": "Come scegliere un robot tagliaerba",
        "card_text": "I sette criteri che contano davvero, nell'ordine giusto, e gli errori da evitare.",
        "title": "Come scegliere un robot tagliaerba: guida completa 2026",
        "desc": "Superficie, pendenza, filo o senza filo, app, sicurezza e budget: i 7 criteri per scegliere il robot tagliaerba giusto ed evitare errori costosi.",
        "eyebrow": "Guida completa · 2026",
        "h1": "Come scegliere un robot tagliaerba senza sbagliare",
        "lead": "Un robot tagliaerba può restituirti decine di ore all'anno, ma solo se è adatto al tuo giardino. In questa guida trovi i sette criteri che contano davvero, nell'ordine in cui conviene valutarli.",
        "tldr": [
            "Parti dalla superficie: scegli un robot che dichiari almeno il 20–30% in più del tuo prato.",
            "Misura la pendenza nel punto più ripido e confrontala con quella massima supportata.",
            "Decidi se posare il filo perimetrale o puntare su un modello senza filo.",
            "Controlla passaggi stretti, zone separate e Wi-Fi in giardino.",
            "Valuta sicurezza, antifurto e costi nel tempo, non solo il prezzo.",
        ],
        "body": [
            ("s", "perche", "Perché un robot tagliaerba conviene", """
<p>Un robot tagliaerba non sostituisce solo il tosaerba: cambia il modo in cui curi il prato. Invece di un taglio deciso una volta alla settimana, taglia pochi millimetri alla volta, molto spesso. I frammenti d'erba sono così piccoli che restano sul prato e si decompongono (<strong>mulching</strong>), restituendo nutrienti al terreno. Con il tempo il prato diventa più fitto e uniforme.</p>
<p>Il vantaggio più concreto, però, è il tempo. Se oggi dedichi un'ora alla settimana al prato da aprile a ottobre, sono circa <strong>30 ore all'anno</strong> che tornano a te. Il robot lavora da solo, secondo gli orari che imposti, e rientra alla base quando deve ricaricarsi.</p>
<ul>
  <li><strong>Nessuna raccolta</strong>: niente sacchi d'erba da svuotare.</li>
  <li><strong>Molto più silenzioso</strong> di un tosaerba a scoppio.</li>
  <li><strong>Niente carburante</strong>: si ricarica dalla corrente, con consumi contenuti.</li>
  <li><strong>Programmabile</strong>: il prato resta in ordine anche quando sei in vacanza.</li>
</ul>"""),
            ("s", "superficie", "1. Quanto è grande il tuo prato", """
<p>È il primo dato da conoscere, perché ogni robot dichiara una <strong>superficie massima</strong>. Per un prato rettangolare basta moltiplicare lunghezza per larghezza. Se la forma è irregolare, dividilo in rettangoli e somma le aree. In alternativa, molte app di mappe permettono di disegnare il perimetro del giardino sulla vista satellitare e calcolano l'area per te.</p>
<p>Attenzione: la superficie dichiarata si riferisce a condizioni ideali, cioè un prato regolare, piano e senza ostacoli. Aiuole, alberi, passaggi stretti e pendenze riducono la superficie che il robot gestisce davvero. Per questo conviene scegliere un modello che dichiari <strong>almeno il 20–30% in più</strong> della tua superficie.</p>
""" + table(
                ["Il tuo prato", "Superficie dichiarata consigliata", "Guida dedicata"],
                [
                    ["Fino a 300 m²", "400–500 m²", '<a href="/robot-tagliaerba-piccoli-giardini">Piccoli giardini</a>'],
                    ["300–500 m²", "600–800 m²", '<a href="/robot-tagliaerba-piccoli-giardini">Piccoli giardini</a>'],
                    ["500–1.000 m²", "1.200–1.500 m²", '<a href="/robot-tagliaerba-giardini-medi">Giardini medi</a>'],
                    ["1.000–1.500 m²", "Circa 2.000 m²", '<a href="/robot-tagliaerba-giardini-medi">Giardini medi</a>'],
                    ["Oltre 1.500 m²", "Almeno il 30% in più", '<a href="/robot-tagliaerba-giardini-grandi">Giardini grandi</a>'],
                ],
                caption="Indicazioni generali: con molti ostacoli o pendenze, scegli un margine più ampio.",
            ) + callout(
                "Il consiglio in più",
                "Se sei indeciso tra due modelli, scegli quello con la superficie dichiarata più alta. Il robot lavorerà meno ore al giorno e il prato resterà in ordine anche in primavera, quando l'erba cresce più in fretta.",
            )),
            ("b", picks_block(
                "Confronto rapido",
                "Le migliori scelte del momento",
                "Un robot consigliato per ogni esigenza: confronta i dati principali e verifica prezzo e disponibilità su Amazon.it.",
            )),
            ("s", "pendenza", "2. La pendenza del terreno", """
<p>Ogni robot indica una <strong>pendenza massima</strong>, quasi sempre in percentuale. Non va confusa con i gradi: una pendenza del 100% corrisponde a 45°, una del 35% a circa 19°. Un prato che a occhio sembra «un po' in salita» spesso supera il 20%.</p>
<p>Per misurarla ti bastano un'asse dritta lunga un metro, una livella e un metro da muratore: appoggia un'estremità dell'asse nel punto più alto, tienila in bolla e misura in centimetri la distanza tra l'altra estremità e il terreno. Quel numero è la pendenza in percentuale. Misura il punto più ripido del prato, non quello medio.</p>
<p>Se il giardino supera il 35–40%, valuta i modelli a trazione integrale. Trovi tutti i dettagli nella <a href="/robot-tagliaerba-pendenza">guida ai robot per terreni in pendenza</a>.</p>"""),
            ("s", "installazione", "3. Con filo perimetrale o senza filo", """
<p>È la scelta che cambia di più l'esperienza d'uso.</p>
<h3>Robot con filo perimetrale</h3>
<p>Un cavo posato lungo i bordi del prato delimita l'area di lavoro. È una tecnologia collaudata, affidabile anche sotto gli alberi e di solito più economica. Lo svantaggio è l'installazione: il filo va posato con cura e, se il giardino cambia, va spostato.</p>
<h3>Robot senza filo</h3>
<p>Si orientano con il posizionamento satellitare GPS RTK, con telecamere o con una combinazione di sensori. I confini si disegnano dall'app e si modificano in pochi minuti. In genere costano di più e, nel caso degli RTK, hanno bisogno di una buona visibilità del cielo.</p>
<p>Abbiamo messo le due soluzioni a confronto punto per punto in <a href="/filo-perimetrale-o-senza-filo">Robot con filo o senza filo: quale conviene?</a></p>
""" + inline_cta("Non sai ancora cosa ti serve?")),
            ("s", "forma", "4. Forma del giardino, passaggi e zone separate", """
<p>Due giardini della stessa superficie possono richiedere robot diversi. Prima di scegliere, fai un giro del prato e annota:</p>
<ul>
  <li><strong>Passaggi stretti</strong> tra casa e recinzione o tra due aiuole: ogni produttore indica la larghezza minima che il robot riesce ad attraversare.</li>
  <li><strong>Zone separate</strong>, per esempio davanti e dietro casa: serve un robot che gestisca più zone, oppure un collegamento tra le aree.</li>
  <li><strong>Ostacoli</strong> come alberi, giochi, vasi e radici sporgenti: i modelli con sensori a ultrasuoni, telecamere o LiDAR li aggirano invece di urtarli.</li>
  <li><strong>Bordi</strong> lungo muri e recinzioni: quasi tutti i robot lasciano una striscia d'erba da rifinire. Se per te è importante, cerca i modelli che dichiarano un taglio vicino ai bordi.</li>
</ul>"""),
            ("s", "connettivita", "5. App e connettività", """
<p>Quasi tutti i robot recenti si gestiscono dallo smartphone, ma il tipo di connessione fa la differenza:</p>
<ul>
  <li><strong>Bluetooth</strong>: funziona solo quando sei vicino al robot. Va bene per un giardino piccolo.</li>
  <li><strong>Wi-Fi</strong>: controlli il robot anche da fuori casa, ma il segnale del router deve arrivare in giardino. Se non arriva, un ripetitore per esterni risolve quasi sempre.</li>
  <li><strong>Rete mobile (4G)</strong>: presente su alcuni modelli, è utile per giardini grandi o lontani dal router e per l'antifurto. Controlla se, dopo un periodo iniziale, è richiesto un abbonamento.</li>
</ul>"""),
            ("s", "sicurezza", "6. Sicurezza, bambini, animali e antifurto", """
<p>I robot tagliaerba venduti in Europa fanno riferimento alla norma di sicurezza EN 50636-2-107: tra le altre cose, le lame si fermano quando il robot viene sollevato o ribaltato e sono protette sotto la scocca. Restano comunque macchine con lame affilate.</p>
<ul>
  <li>Tieni bambini e animali domestici lontani dal robot mentre lavora, oppure programma il taglio quando il giardino è libero.</li>
  <li><strong>Programma il taglio di giorno</strong>: di notte i ricci e altri piccoli animali selvatici sono attivi nei prati e rischiano di essere feriti.</li>
  <li>Per l'antifurto, cerca il blocco con PIN, l'allarme in caso di sollevamento e, se il giardino è visibile dalla strada, la localizzazione GPS.</li>
</ul>"""),
            ("s", "costi", "7. Il budget e i costi nel tempo", """
<p>Il prezzo d'acquisto non è l'unica spesa: contano anche l'installazione, le lame di ricambio, eventuali accessori come il garage e, dopo alcune stagioni, la batteria. In compenso non ci sono carburante, olio e cinghie come nei tosaerba a scoppio, e la corrente consumata è poca.</p>
<p>Abbiamo fatto i conti, fascia per fascia, nella guida <a href="/quanto-costa-robot-tagliaerba">Quanto costa un robot tagliaerba</a>. Se stai pensando di acquistare in questo periodo, leggi anche la <a href="/robot-tagliaerba-black-friday">guida al Black Friday 2026</a>.</p>"""),
            ("s", "marche", "Le marche più diffuse in Italia", """
<p>Su Amazon.it e nei negozi trovi robot tagliaerba di marchi storici del giardinaggio, come Husqvarna, Gardena, Stiga, Bosch e Worx, e di marchi più giovani che hanno puntato sui modelli senza filo, come Segway Navimow, Mammotion, Ecovacs e Dreame.</p>
<p>La marca da sola non basta per scegliere: ogni produttore ha modelli d'ingresso e modelli di fascia alta. Conviene partire dalle caratteristiche del tuo giardino e poi confrontare i modelli che le soddisfano. Valuta anche la presenza di assistenza e ricambi in Italia.</p>"""),
            ("s", "errori", "Gli errori più comuni da evitare", """
<ol>
  <li><strong>Scegliere il robot «giusto giusto»</strong> per la superficie: in primavera l'erba cresce in fretta e il robot non riesce a starle dietro.</li>
  <li><strong>Ignorare il punto più ripido</strong>: il robot slitta e lascia segni sul prato.</li>
  <li><strong>Dimenticare il Wi-Fi in giardino</strong>: senza connessione molte funzioni dell'app non sono disponibili.</li>
  <li><strong>Non misurare i passaggi stretti</strong>: il robot non raggiunge una parte del prato.</li>
  <li><strong>Programmare il taglio di notte</strong>: è più discreto per i vicini, ma pericoloso per i ricci.</li>
</ol>"""),
            ("b", products_block(
                "La selezione",
                "Tutti i robot della selezione",
                "Apri “Scopri di più” per caratteristiche, pregi e limiti, poi verifica prezzo e disponibilità aggiornati su Amazon.it.",
                robots="true",
            )),
        ],
        "faq_title": "Domande frequenti sulla scelta",
        "faq": [
            ("Qual è il miglior robot tagliaerba?", "Non esiste un modello migliore in assoluto: il migliore è quello adatto alla superficie, alla pendenza e alla forma del tuo giardino. Per restringere la scelta in pochi secondi puoi usare il quiz in home oppure la tabella delle migliori scelte."),
            ("Quante ore al giorno lavora un robot tagliaerba?", "Dipende dalla superficie e dal modello. In piena stagione molti robot lavorano diverse ore al giorno, alternando cicli di taglio e di ricarica. Più la superficie dichiarata è ampia rispetto al tuo prato, meno ore servono."),
            ("Il robot taglia anche i bordi?", "Di solito lascia una striscia d'erba lungo muri, recinzioni e aiuole rialzate, che va rifinita con un tagliabordi. Alcuni modelli dichiarano un taglio più vicino ai bordi: controlla questa voce nella scheda del prodotto."),
            ("Funziona anche con l'erba alta?", "Il robot è pensato per mantenere il prato, non per tagliare erba molto alta. Prima di metterlo in funzione conviene fare un taglio con un tosaerba tradizionale all'altezza desiderata: poi il robot manterrà quella lunghezza."),
            ("Un robot tagliaerba può lavorare di notte?", "Tecnicamente sì, ma è sconsigliato: di notte i ricci e altri piccoli animali selvatici sono attivi nei prati e possono essere feriti. Programma il taglio durante il giorno."),
        ],
        "related": ["filo-perimetrale-o-senza-filo", "robot-tagliaerba-senza-filo", "robot-tagliaerba-pendenza"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "robot-tagliaerba-senza-filo",
        "short": "Robot senza filo",
        "card_title": "Robot tagliaerba senza filo",
        "card_text": "RTK, visione artificiale e LiDAR: come funzionano, pro e contro, e quando conviene davvero.",
        "title": "Robot tagliaerba senza filo perimetrale: guida 2026",
        "desc": "RTK, visione artificiale o LiDAR: come funzionano i robot tagliaerba senza filo, pro e contro di ogni tecnologia e come scegliere quello giusto per il tuo giardino.",
        "eyebrow": "Senza filo · Guida 2026",
        "h1": "Robot tagliaerba senza filo: come funzionano e quale scegliere",
        "lead": "Niente cavo da posare, confini disegnati dall'app e taglio a strisce ordinate. I robot senza filo sono la novità più richiesta degli ultimi anni: ecco come funzionano e quando sono davvero la scelta giusta.",
        "tldr": [
            "Si orientano con GPS RTK, telecamere, LiDAR o una combinazione di queste tecnologie.",
            "L'installazione è più rapida: confini e zone si definiscono dall'app.",
            "Gli RTK lavorano meglio con cielo aperto: alberi fitti e muri alti possono disturbare il segnale.",
            "I sistemi ibridi combinano più sensori per lavorare anche nelle zone d'ombra.",
        ],
        "body": [
            ("s", "come-funzionano", "Come fa un robot a orientarsi senza filo", """
<p>Un robot con filo «sente» il cavo posato lungo i bordi e capisce dove fermarsi. Un robot senza filo, invece, deve sapere in ogni momento <strong>dove si trova</strong> rispetto a una mappa del giardino. Per farlo usa una o più di queste tecnologie: il posizionamento satellitare RTK, la visione artificiale con telecamere e, nei modelli più recenti, sensori LiDAR.</p>
<p>La configurazione avviene dall'app: di solito accompagni il robot lungo il perimetro del prato con lo smartphone, come se lo guidassi con un telecomando, e lui memorizza i confini. Allo stesso modo puoi creare zone separate, percorsi di collegamento e <strong>zone vietate</strong> come aiuole, orto o piscina.</p>"""),
            ("s", "rtk", "GPS RTK: precisione al centimetro", """
<p>Il normale GPS dello smartphone ha un margine di errore di alcuni metri: troppo per tagliare l'erba lungo un'aiuola. La tecnologia <strong>RTK</strong> (Real Time Kinematic) corregge il segnale satellitare grazie a una stazione di riferimento fissa e porta la precisione nell'ordine dei centimetri.</p>
<p>Nella maggior parte dei casi la stazione è un'antenna da installare in giardino o sul tetto, in un punto con ampia visibilità del cielo. Alcuni produttori offrono anche la correzione tramite rete, senza antenna propria: verifica nella scheda cosa è incluso.</p>
<ul>
  <li><strong>Punti di forza</strong>: grande precisione, taglio a linee parallele, ottimo su prati ampi e aperti.</li>
  <li><strong>Attenzione a</strong>: alberi con chioma fitta, muri alti e tettoie possono indebolire il segnale. Molti modelli recenti affiancano all'RTK telecamere o altri sensori proprio per lavorare anche in queste zone.</li>
</ul>"""),
            ("s", "visione", "Visione artificiale: il robot che «vede» il prato", """
<p>I robot con visione usano una o più telecamere e algoritmi di intelligenza artificiale per riconoscere l'erba, i bordi e gli ostacoli. Non dipendono dai satelliti, quindi possono funzionare bene anche in giardini con molti alberi.</p>
<ul>
  <li><strong>Punti di forza</strong>: installazione rapida, nessuna antenna, buon riconoscimento degli ostacoli.</li>
  <li><strong>Attenzione a</strong>: luce scarsa e bordi poco definiti, per esempio un prato che sfuma nella terra, possono rendere il lavoro meno preciso. Controlla i requisiti indicati dal produttore.</li>
</ul>"""),
            ("s", "lidar", "LiDAR e sistemi ibridi", """
<p>Il LiDAR misura le distanze con impulsi laser e costruisce una mappa tridimensionale dell'ambiente, come fanno i robot aspirapolvere più evoluti. Alcuni robot tagliaerba recenti lo usano da solo o insieme a RTK e telecamere.</p>
<p>La tendenza del 2026 è proprio questa: <strong>combinare più tecnologie</strong> per compensare i limiti di ciascuna. Un sistema ibrido può usare l'RTK in campo aperto e affidarsi a telecamere o LiDAR sotto gli alberi.</p>
""" + table(
                ["Tecnologia", "Come si orienta", "Ideale per", "Attenzione a"],
                [
                    ["GPS RTK", "Satelliti corretti da una stazione di riferimento", "Prati ampi e aperti", "Alberi fitti, muri alti, tettoie"],
                    ["Visione AI", "Telecamere e intelligenza artificiale", "Giardini con alberi e ostacoli", "Luce scarsa, bordi poco definiti"],
                    ["LiDAR", "Scansione laser dell'ambiente", "Giardini articolati", "Requisiti indicati dal produttore"],
                    ["Ibrido", "Più sensori combinati", "Giardini misti, tra sole e ombra", "Prezzo in genere più alto"],
                ],
                caption="Indicazioni generali: per il singolo modello fanno fede i requisiti del produttore.",
            )),
            ("b", products_block(
                "Senza filo",
                "I robot senza filo della selezione",
                "Confronta tecnologie e caratteristiche, poi verifica prezzo e disponibilità aggiornati su Amazon.it.",
                wireless="true",
            )),
            ("s", "vantaggi", "I vantaggi rispetto al filo perimetrale", check_list([
                "Nessuno scavo e nessun cavo da posare lungo i bordi.",
                "Confini, zone e aree vietate si modificano dall'app in pochi minuti.",
                "Nessun rischio di tagliare il filo mentre lavori in giardino.",
                "Taglio a linee parallele, più ordinato e spesso più efficiente.",
                "Più zone separate gestite con un solo robot.",
            ])),
            ("s", "limiti", "I limiti da conoscere prima di comprare", """
<p>Un buon consiglio d'acquisto racconta anche i limiti. Quelli dei robot senza filo sono:</p>
<ul>
  <li><strong>Prezzo</strong>: in media più alto rispetto ai modelli con filo di pari superficie.</li>
  <li><strong>Segnale</strong>: gli RTK hanno bisogno di cielo libero; i modelli con visione, di una buona illuminazione.</li>
  <li><strong>Configurazione iniziale</strong>: richiede un po' di pazienza con l'app, anche se è più rapida della posa del filo.</li>
  <li><strong>Software</strong>: molte funzioni dipendono dall'app e dagli aggiornamenti del produttore.</li>
</ul>
""" + callout(
                "Il nostro consiglio",
                "Se il tuo prato è aperto e soleggiato, un robot RTK è spesso la scelta più precisa. Se hai molti alberi o zone d'ombra, orientati su un modello con visione artificiale o su un sistema ibrido.",
            )),
            ("s", "scegliere", "Come scegliere il robot senza filo giusto", """
<ol>
  <li><strong>Guarda il giardino dall'alto</strong>: quanto cielo libero c'è? Quanti alberi e muri alti?</li>
  <li><strong>Scegli la tecnologia</strong> di conseguenza: RTK per spazi aperti, visione o sistemi ibridi per giardini con molta ombra.</li>
  <li><strong>Controlla la superficie</strong> dichiarata, con almeno il 20–30% di margine.</li>
  <li><strong>Verifica la pendenza</strong> massima e, se serve, la trazione integrale.</li>
  <li><strong>Valuta la connettività</strong>: Wi-Fi che arriva in giardino oppure un modello con rete mobile.</li>
  <li><strong>Leggi le opinioni</strong> degli acquirenti con giardini simili al tuo.</li>
</ol>
""" + inline_cta()),
        ],
        "faq_title": "Domande frequenti sui robot senza filo",
        "faq": [
            ("Un robot senza filo funziona sotto gli alberi?", "Dipende dalla tecnologia. Gli RTK possono perdere precisione sotto chiome fitte o vicino a muri alti; i modelli con visione artificiale o con sistemi ibridi gestiscono meglio queste zone. Controlla i requisiti indicati dal produttore."),
            ("Serve per forza il Wi-Fi?", "Per configurare e gestire il robot dall'app serve una connessione: Wi-Fi in giardino, Bluetooth da vicino o, in alcuni modelli, la rete mobile. Verifica nella scheda quali connessioni supporta il modello."),
            ("È più facile da rubare di un robot con filo?", "Non necessariamente. Molti robot senza filo hanno blocco con PIN, allarme e localizzazione GPS, e senza l'app associata al proprietario sono difficili da usare."),
            ("È più preciso di un robot con filo?", "Lungo i bordi la precisione è simile; la differenza principale è nel modo di tagliare. I robot senza filo lavorano di solito a linee parallele, mentre molti robot con filo si muovono in modo casuale all'interno del perimetro."),
            ("Si può installare da soli?", "Sì, è pensato per essere configurato dall'app senza attrezzi particolari. Per i modelli RTK la parte più delicata è scegliere una buona posizione per l'antenna."),
        ],
        "related": ["filo-perimetrale-o-senza-filo", "installazione-robot-tagliaerba", "robot-tagliaerba-giardini-grandi"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "filo-perimetrale-o-senza-filo",
        "short": "Con filo o senza filo",
        "card_title": "Con filo o senza filo: quale conviene?",
        "card_text": "Installazione, precisione, prezzo e manutenzione a confronto, punto per punto.",
        "title": "Robot tagliaerba con filo o senza filo? Confronto 2026",
        "desc": "Robot tagliaerba con filo perimetrale o senza filo? Installazione, precisione, prezzo e manutenzione a confronto, per capire quale conviene al tuo giardino.",
        "eyebrow": "Confronto · 2026",
        "h1": "Robot tagliaerba con filo o senza filo: quale conviene?",
        "lead": "È la domanda che si fanno quasi tutti prima di acquistare. La risposta dipende dal tuo giardino, dal tempo che vuoi dedicare all'installazione e dal budget: ecco il confronto completo.",
        "tldr": [
            "Con filo: tecnologia collaudata, affidabile sotto gli alberi, di solito più economica.",
            "Senza filo: installazione più rapida e confini modificabili dall'app, ma prezzo più alto.",
            "Con molti alberi o muri alti, meglio il filo o un senza filo con visione o sistema ibrido.",
            "Se il giardino cambia spesso, il senza filo ti fa risparmiare tempo negli anni.",
        ],
        "body": [
            ("s", "filo", "Come funziona un robot con filo perimetrale", """
<p>Il filo perimetrale è un cavo sottile che parte dalla base di ricarica, segue tutto il bordo del prato e torna alla base. La base fa passare nel cavo un debole segnale: il robot lo rileva e capisce che non deve oltrepassarlo. Aiuole e ostacoli fissi si escludono facendo girare il filo intorno a loro.</p>
<p>Molti modelli usano anche un <strong>filo guida</strong>, che attraversa il prato e aiuta il robot a tornare alla base o a raggiungere zone lontane passando per i corridoi stretti.</p>"""),
            ("s", "senza", "Come funziona un robot senza filo", """
<p>Il robot senza filo si orienta da solo grazie al posizionamento satellitare RTK, alle telecamere o ad altri sensori. I confini del prato si disegnano nell'app, di solito guidando il robot lungo il perimetro con lo smartphone. Approfondisci nella <a href="/robot-tagliaerba-senza-filo">guida completa ai robot senza filo</a>.</p>"""),
            ("s", "confronto", "Il confronto punto per punto", table(
                ["Aspetto", "Con filo perimetrale", "Senza filo"],
                [
                    ["Installazione", "Posa del filo lungo tutto il bordo: da qualche ora a una giornata", "Mappatura dall'app, in genere più rapida"],
                    ["Modifiche al giardino", "Bisogna spostare il filo", "Si ridisegnano i confini dall'app"],
                    ["Modo di tagliare", "Spesso percorsi casuali all'interno del perimetro", "Di solito linee parallele ordinate"],
                    ["Sotto gli alberi", "Affidabile", "Dipende dalla tecnologia: RTK, visione o ibrido"],
                    ["Manutenzione", "Il filo può essere tagliato per errore e va riparato", "Nessun filo da riparare; contano gli aggiornamenti software"],
                    ["Prezzo", "In genere più accessibile", "In genere più alto"],
                    ["Ideale per", "Giardini stabili e alberati, budget contenuto", "Chi vuole installare in fretta e cambiare spesso le zone"],
                ],
            )),
            ("s", "quando-filo", "Quando conviene il filo perimetrale", check_list([
                "Il giardino ha molti alberi alti o è circondato da edifici.",
                "La forma del prato è stabile e non pensi di cambiarla.",
                "Vuoi contenere la spesa iniziale.",
                "Non ti pesa dedicare una giornata all'installazione, oppure affidarla a un installatore.",
            ])),
            ("s", "quando-senza", "Quando conviene il senza filo", check_list([
                "Il prato è ampio e con buona visibilità del cielo, oppure scegli un modello con visione o sistema ibrido.",
                "Vuoi evitare picchetti e scavi lungo i bordi.",
                "Modifichi spesso aiuole, orto o zone gioco.",
                "Hai più zone separate da gestire.",
            ]) + inline_cta("Ancora indeciso?", "Il quiz ti chiede se vuoi evitare il filo e ti propone i robot più adatti al tuo giardino.")),
            ("b", products_block(
                "Senza filo",
                "I robot senza filo della selezione",
                "Per chi vuole installare in fretta e gestire tutto dall'app.",
                wireless="true",
            )),
            ("b", products_block(
                "Con filo perimetrale",
                "I robot con filo della selezione",
                "Per chi cerca una soluzione collaudata e una spesa più contenuta.",
                wireless="false",
            )),
            ("s", "installatore", "E se l'installazione la fa un professionista?", """
<p>Se non hai tempo o voglia di posare il filo, molti rivenditori e giardinieri offrono l'installazione a pagamento. È una spesa da aggiungere al prezzo del robot con filo quando lo confronti con un modello senza filo: a volte la differenza tra le due soluzioni si riduce parecchio.</p>
<p>Se preferisci fare da te, trovi tutti i passaggi nella <a href="/installazione-robot-tagliaerba">guida all'installazione</a>.</p>"""),
        ],
        "faq_title": "Domande frequenti su filo e senza filo",
        "faq": [
            ("Il filo perimetrale va interrato?", "Non è obbligatorio. Si può fissare in superficie con i picchetti in dotazione: in poche settimane l'erba lo ricopre. Interrarlo di qualche centimetro lo protegge meglio da arieggiatori e attrezzi da giardino."),
            ("Il filo si rompe spesso?", "Se posato bene, può durare molti anni. I danni più comuni sono i tagli accidentali con vanga, arieggiatore o tagliabordi, che si riparano in pochi minuti con giunti appositi."),
            ("Posso passare da un robot con filo a uno senza filo?", "Sì. Il filo esistente può restare nel terreno: il robot senza filo semplicemente non lo usa. Al contrario, un robot con filo richiede sempre la posa del cavo."),
            ("Un robot con filo taglia peggio?", "No: la qualità del taglio dipende soprattutto dalle lame e dalla frequenza dei passaggi. Cambia il percorso, casuale per molti modelli con filo e a linee parallele per molti modelli senza filo."),
        ],
        "related": ["robot-tagliaerba-senza-filo", "installazione-robot-tagliaerba", "quanto-costa-robot-tagliaerba"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "robot-tagliaerba-piccoli-giardini",
        "short": "Piccoli giardini",
        "card_title": "Robot per piccoli giardini",
        "card_text": "Fino a 500 m²: passaggi stretti, rumore, antifurto e come non spendere più del necessario.",
        "title": "Robot tagliaerba per piccoli giardini: guida 2026",
        "desc": "Il robot tagliaerba giusto per giardini fino a 500 m²: superficie, passaggi stretti, rumore e antifurto. Consigli pratici e modelli da confrontare su Amazon.it.",
        "eyebrow": "Fino a 500 m² · Guida 2026",
        "h1": "Robot tagliaerba per piccoli giardini: come sceglierlo",
        "lead": "Anche un prato di pochi metri quadrati chiede tempo ogni settimana. Un robot compatto lo tiene in ordine al posto tuo, in silenzio e senza sacchi d'erba da svuotare.",
        "tldr": [
            "Scegli un modello che dichiari 20–30% in più della superficie del tuo prato.",
            "Misura i passaggi stretti: nei giardini a schiera sono il problema più frequente.",
            "Se i vicini sono vicini, controlla il rumore dichiarato.",
            "Con la base visibile dalla strada, valuta PIN e allarme antifurto.",
        ],
        "body": [
            ("s", "conviene", "Ha senso un robot per un piccolo giardino?", """
<p>Sì, ed è spesso il caso in cui il robot dà più soddisfazione. Un prato piccolo cresce come uno grande: in primavera serve un taglio ogni pochi giorni. Il robot lo fa da solo, mentre tu non devi tirare fuori il tosaerba, svuotare il cesto e pulire.</p>
<p>I modelli per piccoli giardini sono anche i più accessibili: compatti, leggeri e facili da riporre in garage o in cantina durante l'inverno.</p>"""),
            ("s", "cosa-guardare", "Cosa guardare nella scheda", """
<h3>Superficie dichiarata</h3>
<p>Per un prato fino a 500 m² cerca modelli che dichiarano il 20–30% in più della tua superficie. Così il robot lavora meno ore al giorno e il prato resta in ordine anche nei periodi di crescita rapida.</p>
<h3>Larghezza minima dei passaggi</h3>
<p>Nei giardini a schiera e nei cortili il prato è spesso collegato da corridoi stretti. Misurali e confrontali con il valore indicato dal produttore.</p>
<h3>Rumore</h3>
<p>I robot sono molto più silenziosi di un tosaerba a scoppio: molti dichiarano valori intorno ai 55–65 dB. Se i vicini sono a pochi metri, scegli un modello con un valore basso e programma il taglio negli orari previsti dal regolamento del tuo Comune.</p>
<h3>Altezza di taglio</h3>
<p>Una regolazione ampia ti permette di tenere il prato più alto in estate, quando soffre il caldo, e più basso in primavera.</p>
<h3>Antifurto</h3>
<p>Nei giardini fronte strada, il blocco con PIN e l'allarme in caso di sollevamento sono una protezione utile.</p>"""),
            ("b", products_block(
                "Piccoli giardini",
                "I robot per piccoli giardini della selezione",
                "Modelli compatti, pensati per prati fino a circa 500 m². Apri “Scopri di più” per pregi e limiti.",
                category="Giardini piccoli",
            )),
            ("s", "filo-o-no", "Con filo o senza filo in un giardino piccolo?", """
<p>Per un prato piccolo e regolare, un robot con filo è spesso la scelta più economica: il perimetro è corto e la posa richiede poche ore. Un modello senza filo ha senso se vuoi evitare del tutto i lavori in giardino o se sposti spesso aiuole e vasi. Il confronto completo è nella guida <a href="/filo-perimetrale-o-senza-filo">con filo o senza filo</a>.</p>"""),
            ("s", "errori", "Errori tipici nei giardini piccoli", """
<ul>
  <li><strong>Comprare il modello più piccolo in assoluto</strong>: risparmi poco e il robot lavora sempre al limite.</li>
  <li><strong>Mettere la base in un angolo stretto</strong>: il robot ha bisogno di spazio libero davanti per entrare e uscire.</li>
  <li><strong>Dimenticare i bordi</strong>: in un giardino piccolo la striscia lungo i muri si nota di più. Tieni a portata di mano un tagliabordi.</li>
</ul>
""" + inline_cta()),
        ],
        "faq_title": "Domande frequenti sui piccoli giardini",
        "faq": [
            ("Ha senso un robot per un prato di 100 m²?", "Sì, se vuoi dimenticarti del taglio dell'erba. Su superfici così piccole un modello d'ingresso è più che sufficiente e lavora poche ore alla settimana."),
            ("Quanto spazio occupa la base di ricarica?", "Poco: di solito meno di un metro quadrato, più lo spazio libero davanti per l'ingresso del robot. Le misure precise sono nella scheda del modello."),
            ("Funziona su un prato con tante aiuole?", "Sì. Con il filo perimetrale le aiuole si escludono facendo girare il cavo intorno; con i modelli senza filo si disegnano zone vietate nell'app."),
            ("Disturba i vicini?", "Molto meno di un tosaerba tradizionale. Per stare tranquillo scegli un modello silenzioso e programma il taglio negli orari previsti dal regolamento del tuo Comune."),
        ],
        "related": ["robot-tagliaerba-giardini-medi", "filo-perimetrale-o-senza-filo", "installazione-robot-tagliaerba"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "robot-tagliaerba-giardini-medi",
        "short": "Giardini medi",
        "card_title": "Robot per giardini medi",
        "card_text": "Da 500 a 1.500 m²: Wi-Fi in giardino, ostacoli, sensore pioggia e gestione di più zone.",
        "title": "Robot tagliaerba per giardini medi (500–1.500 m²)",
        "desc": "Come scegliere un robot tagliaerba per giardini da 500 a 1.500 m²: superficie consigliata, Wi-Fi in giardino, ostacoli, sensore pioggia e gestione di più zone.",
        "eyebrow": "Da 500 a 1.500 m² · Guida 2026",
        "h1": "Robot tagliaerba per giardini medi: guida alla scelta",
        "lead": "È la fascia più richiesta e quella con più scelta. Aiuole, alberi e zone d'ombra rendono questi giardini più complessi: ecco cosa conta davvero, da 500 a 1.500 m².",
        "tldr": [
            "Per 1.000 m² di prato cerca modelli da almeno 1.200–1.500 m² dichiarati.",
            "App e Wi-Fi diventano importanti: verifica che il segnale arrivi in giardino.",
            "Sensori per gli ostacoli e sensore pioggia fanno la differenza ogni giorno.",
            "Con il prato diviso in più aree, scegli un modello multizona.",
        ],
        "body": [
            ("s", "caratteristiche", "Le caratteristiche che contano", """
<h3>Superficie con margine</h3>
""" + table(
                ["Il tuo prato", "Superficie dichiarata consigliata"],
                [["500–750 m²", "900–1.000 m²"], ["750–1.000 m²", "1.200–1.500 m²"], ["1.000–1.500 m²", "1.800–2.000 m²"]],
            ) + """
<h3>Gestione da app</h3>
<p>Con un giardino medio vorrai regolare orari, altezza di taglio e zone senza uscire di casa. Un modello con Wi-Fi o rete mobile ti permette di farlo anche quando sei fuori.</p>
<h3>Ostacoli</h3>
<p>Alberi, giochi, mobili da giardino: i sensori a ultrasuoni, le telecamere o il LiDAR permettono al robot di aggirarli invece di urtarli.</p>
<h3>Sensore pioggia</h3>
<p>Quando piove il robot torna alla base e riprende più tardi. L'erba bagnata si taglia peggio e le ruote rischiano di lasciare segni.</p>
<h3>Più zone</h3>
<p>Prato davanti e dietro casa? Cerca la gestione multizona e controlla come il robot si sposta da un'area all'altra.</p>"""),
            ("b", products_block(
                "Giardini medi",
                "I robot per giardini medi della selezione",
                "Pensati per prati da 500 a 1.500 m² con aiuole, alberi e qualche zona da gestire.",
                category="Giardini medi",
            )),
            ("s", "wifi", "Il Wi-Fi non arriva in giardino?", """
<p>È il problema più frequente in questa fascia. Prima di comprare, prova con lo smartphone: vai nel punto più lontano del prato e controlla se la connessione funziona. Se il segnale è debole hai tre possibilità:</p>
<ol>
  <li>un <strong>ripetitore Wi-Fi o un sistema mesh</strong> con un'unità da esterni;</li>
  <li>un robot con <strong>rete mobile integrata</strong>;</li>
  <li>un robot gestibile anche via <strong>Bluetooth</strong>, accettando di usare l'app solo da vicino.</li>
</ol>"""),
            ("s", "frequenza", "Quanto deve lavorare il robot", """
<p>In primavera, quando l'erba cresce più in fretta, il robot può lavorare quasi ogni giorno. In estate e in autunno puoi ridurre le ore. Molte app propongono una programmazione automatica in base alla superficie: è un buon punto di partenza da adattare.</p>
<p>Lascia libere le ore serali e notturne: è la scelta più sicura per i ricci e gli altri piccoli animali del giardino.</p>
""" + inline_cta()),
        ],
        "faq_title": "Domande frequenti sui giardini medi",
        "faq": [
            ("Meglio con filo o senza filo per 1.000 m²?", "Entrambe le soluzioni funzionano. Il senza filo fa risparmiare la posa di parecchi metri di cavo e semplifica le modifiche; il filo resta più economico e affidabile nei giardini molto alberati."),
            ("Quante volte a settimana deve tagliare?", "In piena stagione quasi tutti i giorni, per poche ore. Il taglio frequente mantiene il prato fitto e i frammenti d'erba restano sul terreno come fertilizzante naturale."),
            ("Serve la trazione integrale?", "Solo con pendenze impegnative o terreno molto irregolare. Per un prato medio quasi in piano bastano due ruote motrici."),
        ],
        "related": ["robot-tagliaerba-piccoli-giardini", "robot-tagliaerba-giardini-grandi", "robot-tagliaerba-pendenza"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "robot-tagliaerba-giardini-grandi",
        "short": "Giardini grandi",
        "card_title": "Robot per giardini grandi",
        "card_text": "Oltre 1.500 m²: autonomia, trazione, rete mobile e quando conviene usare due robot.",
        "title": "Robot tagliaerba per giardini grandi: guida 2026",
        "desc": "Robot tagliaerba per giardini oltre 1.500 m²: autonomia, larghezza di taglio, trazione integrale, rete mobile e senza filo RTK. Cosa serve e cosa evitare.",
        "eyebrow": "Oltre 1.500 m² · Guida 2026",
        "h1": "Robot tagliaerba per giardini grandi: cosa serve oltre i 1.500 m²",
        "lead": "Sulle grandi superfici il robot lavora molte ore e deve gestire distanze, zone e terreni diversi. Ecco come scegliere un modello all'altezza, senza pagare funzioni che non userai.",
        "tldr": [
            "Oltre i 1.500 m² contano autonomia, larghezza di taglio e tempi di ricarica.",
            "Su terreni irregolari o in pendenza valuta la trazione integrale.",
            "La rete mobile semplifica la gestione quando il Wi-Fi non copre tutto.",
            "Con zone molto separate, due robot possono lavorare meglio di uno.",
        ],
        "body": [
            ("s", "cosa-cambia", "Cosa cambia nei giardini grandi", """
<p>Un prato di 3.000 m² non è semplicemente un prato piccolo più grande. Il robot percorre distanze lunghe per tornare alla base, attraversa zone con caratteristiche diverse e deve completare il lavoro prima che l'erba ricresca. Per questo, oltre alla superficie dichiarata, servono alcuni dati in più.</p>"""),
            ("s", "dati", "I dati da confrontare", """
<ul>
  <li><strong>Superficie massima</strong>, sempre con almeno il 30% di margine.</li>
  <li><strong>Larghezza di taglio</strong>: più è ampia, meno passaggi servono.</li>
  <li><strong>Autonomia e tempo di ricarica</strong>: insieme determinano quanto prato il robot taglia in un giorno.</li>
  <li><strong>Trazione</strong>: due o quattro ruote motrici, in base al terreno.</li>
  <li><strong>Gestione multizona</strong> e percorsi di collegamento tra le aree.</li>
  <li><strong>Connettività</strong>: Wi-Fi esteso o rete mobile.</li>
</ul>
""" + callout(
                "Un calcolo semplice",
                "Se un robot dichiara 3.000 m² e il tuo prato ne misura 2.000, ha un margine del 50%: lavorerà meno ore e gestirà meglio la crescita primaverile. Se il tuo prato è di 2.900 m², lo stesso robot lavorerà sempre al limite.",
            )),
            ("b", products_block(
                "Giardini grandi",
                "I robot per giardini grandi della selezione",
                "Per prati ampi, terreni irregolari o più zone separate.",
                category="Giardini grandi",
            )),
            ("s", "senza-filo", "Il senza filo nei grandi spazi", """
<p>Sulle grandi superfici il filo perimetrale significa centinaia di metri di cavo da posare. Per questo molti scelgono un robot senza filo con RTK, che si configura dall'app e taglia a linee parallele. Controlla la copertura della stazione di riferimento e le zone d'ombra dovute ad alberi ed edifici. Approfondisci nella <a href="/robot-tagliaerba-senza-filo">guida ai robot senza filo</a>.</p>"""),
            ("b", products_block(
                "Senza filo",
                "Robot senza filo da valutare per i grandi spazi",
                "Niente cavo da posare: confini e zone si disegnano dall'app.",
                wireless="true",
            )),
            ("s", "due-robot", "Uno o due robot?", """
<p>Oltre una certa superficie, o con zone molto distanti tra loro, due robot di fascia media possono lavorare meglio di un solo modello grande: ognuno ha la sua area e la sua base. È una soluzione da valutare quando il giardino è diviso in parti nettamente separate, per esempio da un vialetto carrabile o da un edificio.</p>"""),
            ("s", "corrente", "La corrente in giardino", """
<p>La base di ricarica va collegata a una presa elettrica. Nei giardini grandi conviene metterla in posizione centrale rispetto al prato, per ridurre gli spostamenti del robot. Se serve portare la corrente in un nuovo punto, affidati a un elettricista e usa materiali adatti all'esterno.</p>
""" + inline_cta()),
        ],
        "faq_title": "Domande frequenti sui giardini grandi",
        "faq": [
            ("Un solo robot può gestire 5.000 m²?", "Esistono modelli che dichiarano superfici di questo ordine, soprattutto tra quelli senza filo e a trazione integrale. Verifica sempre che il margine sia sufficiente e che il giardino non abbia troppe zone separate."),
            ("Quanto tempo impiega a tagliare tutto il prato?", "Il robot non taglia tutto in una volta: lavora a cicli, ogni giorno, mantenendo l'erba sempre alla stessa altezza. Conta la superficie che riesce a gestire nell'arco della settimana, non in un singolo giro."),
            ("Serve una presa elettrica in giardino?", "Sì, la base di ricarica va alimentata. Se la presa è lontana, un elettricista può portare la corrente nel punto migliore con materiali adatti all'esterno."),
        ],
        "related": ["robot-tagliaerba-pendenza", "robot-tagliaerba-senza-filo", "quanto-costa-robot-tagliaerba"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "robot-tagliaerba-pendenza",
        "short": "Terreni in pendenza",
        "card_title": "Robot per terreni in pendenza",
        "card_text": "Come misurare la pendenza, percentuale o gradi, e quando serve la trazione integrale.",
        "title": "Robot tagliaerba per terreni in pendenza: guida 2026",
        "desc": "Robot tagliaerba per giardini in pendenza: come misurare la pendenza, differenza tra percentuale e gradi, trazione integrale e consigli per scegliere senza errori.",
        "eyebrow": "Pendenze · Guida 2026",
        "h1": "Robot tagliaerba per terreni in pendenza: come misurare e cosa scegliere",
        "lead": "Le salite sono la prima causa di delusione con i robot tagliaerba. Con una misura fatta bene e il modello giusto, però, anche un giardino in collina si tiene in ordine.",
        "tldr": [
            "La pendenza dei robot si esprime in percentuale: il 100% equivale a 45°.",
            "Misura il punto più ripido del prato, non la pendenza media.",
            "Alcuni produttori indicano una pendenza massima più bassa lungo i bordi.",
            "Oltre il 35–40%, valuta un modello a trazione integrale.",
        ],
        "body": [
            ("s", "percentuale", "Percentuale o gradi? Facciamo chiarezza", """
<p>I produttori indicano quasi sempre la pendenza in <strong>percentuale</strong>: quanti centimetri sale il terreno per ogni metro in orizzontale. Una pendenza del 30% sale di 30 cm ogni metro. Non va confusa con i gradi: il 100% corrisponde a 45°.</p>
""" + table(
                ["Pendenza", "Gradi (circa)", "Come appare"],
                [
                    ["10%", "6°", "Leggera, quasi impercettibile"],
                    ["20%", "11°", "Si nota camminando"],
                    ["30%", "17°", "Salita evidente"],
                    ["35%", "19°", "Impegnativa per molti robot d'ingresso"],
                    ["45%", "24°", "Ripida"],
                    ["60%", "31°", "Molto ripida"],
                    ["80%", "39°", "Estrema: solo modelli specifici"],
                ],
            )),
            ("s", "misurare", "Come misurare la pendenza del tuo prato", """
<ol>
  <li>Procurati un'asse dritta lunga esattamente 1 metro, una livella e un metro.</li>
  <li>Individua il <strong>punto più ripido</strong> del prato.</li>
  <li>Appoggia un'estremità dell'asse sul terreno nel punto più alto, in direzione della discesa.</li>
  <li>Solleva l'altra estremità finché l'asse è in bolla.</li>
  <li>Misura in centimetri la distanza tra l'estremità sollevata e il terreno: quel numero è la pendenza in percentuale.</li>
</ol>
<p>In alternativa, molte app per smartphone funzionano da inclinometro: appoggia il telefono sull'asse, leggi i gradi e convertili con la tabella qui sopra.</p>
""" + callout(
                "Attenzione ai bordi",
                "Per i robot con filo, alcuni produttori indicano una pendenza massima più bassa lungo il perimetro rispetto all'interno del prato. Se il bordo del tuo giardino è in salita, controlla anche questo valore nel manuale.",
                warn=True,
            )),
            ("b", products_block(
                "Pendenze",
                "I robot della selezione per terreni in pendenza",
                "Verifica sempre nella scheda la pendenza massima dichiarata e confrontala con la tua misura.",
                tag="pendenza",
            )),
            ("s", "trazione", "Due ruote motrici o trazione integrale?", """
<p>La maggior parte dei robot ha <strong>due ruote motrici</strong> posteriori e una o due ruote anteriori libere. Funzionano bene su prati piani o con salite moderate.</p>
<p>I modelli a <strong>trazione integrale (AWD o 4WD)</strong> hanno tutte le ruote motrici: mantengono l'aderenza su pendenze forti, terreno irregolare ed erba umida. Costano di più, ma su un giardino in collina fanno la differenza tra un robot che lavora e uno che slitta.</p>
<ul>
  <li><strong>Fino al 25–30%</strong>: vanno bene molti modelli a due ruote motrici.</li>
  <li><strong>Dal 30 al 45%</strong>: scegli un modello che dichiari espressamente questi valori, con ruote dal battistrada marcato.</li>
  <li><strong>Oltre il 45%</strong>: orientati sulla trazione integrale.</li>
</ul>"""),
            ("s", "consigli", "Consigli per chi ha il giardino in pendenza", """
<ul>
  <li><strong>Lascia un margine</strong>: se il punto più ripido è al 35%, scegli un robot che ne dichiari almeno il 40–45%.</li>
  <li>Evita di far lavorare il robot sull'erba bagnata in pendenza: perde aderenza e lascia segni.</li>
  <li>Metti la base di ricarica in un punto piano.</li>
  <li>Pulisci spesso le ruote: il fango riduce l'aderenza.</li>
</ul>
""" + inline_cta()),
        ],
        "faq_title": "Domande frequenti sulle pendenze",
        "faq": [
            ("Cosa succede se la pendenza supera il limite del robot?", "Il robot può slittare, non riuscire a salire, lasciare segni sul prato o fermarsi con un errore. Su pendenze eccessive aumenta anche il rischio di ribaltamento: per questo i sensori fermano le lame."),
            ("Una pendenza del 45% è tanto?", "Sì: corrisponde a circa 24 gradi, una salita che a piedi si sente. Serve un robot progettato espressamente per le pendenze."),
            ("La trazione integrale serve anche in piano?", "Non è necessaria. In piano un buon robot a due ruote motrici basta e costa meno."),
        ],
        "related": ["robot-tagliaerba-giardini-grandi", "come-scegliere-robot-tagliaerba", "robot-tagliaerba-senza-filo"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "quanto-costa-robot-tagliaerba",
        "short": "Quanto costa",
        "card_title": "Quanto costa un robot tagliaerba",
        "card_text": "Fasce di prezzo, costi nascosti, consumi elettrici e quando conviene rispetto al tosaerba.",
        "title": "Quanto costa un robot tagliaerba? Prezzi e costi 2026",
        "desc": "Quanto costa un robot tagliaerba nel 2026: fasce di prezzo, installazione, lame, batteria e consumi elettrici. Conviene rispetto al tosaerba? Facciamo i conti.",
        "eyebrow": "Prezzi e costi · 2026",
        "h1": "Quanto costa un robot tagliaerba: prezzo, installazione e costi nel tempo",
        "lead": "Il prezzo sull'etichetta è solo l'inizio. Ecco quanto si spende davvero per un robot tagliaerba, fascia per fascia, e come capire se conviene rispetto al tosaerba tradizionale.",
        "tldr": [
            "I prezzi vanno da qualche centinaio di euro a oltre duemila, in base a superficie e tecnologia.",
            "Al prezzo d'acquisto aggiungi installazione, lame, accessori e, dopo alcune stagioni, la batteria.",
            "La corrente consumata costa in genere pochi euro all'anno.",
            "Il risparmio più grande è il tempo: decine di ore all'anno.",
        ],
        "body": [
            ("s", "fasce", "Le tre fasce di prezzo", """
<p>I prezzi cambiano spesso, anche più volte al mese: quelli aggiornati sono sempre sulla pagina Amazon del prodotto. Per orientarti, puoi ragionare per fasce:</p>
""" + table(
                ["Fascia", "Cosa trovi di solito", "Per chi"],
                [
                    ["Base", "Robot con filo per piccoli giardini, funzioni essenziali, app semplice o pannello di comando", "Prati piccoli e regolari, budget contenuto"],
                    ["Media", "Superfici maggiori, app con Wi-Fi, sensori per ostacoli e pioggia, primi modelli senza filo", "Giardini medi, chi vuole gestire tutto dallo smartphone"],
                    ["Alta", "Senza filo con RTK, visione o LiDAR, trazione integrale, rete mobile, grandi superfici", "Giardini grandi, in pendenza o complessi"],
                ],
                caption="Fasce indicative: il prezzo aggiornato è sempre quello sulla pagina Amazon del prodotto.",
            ) + """
<p>Indicativamente, i modelli d'ingresso con filo partono da qualche centinaio di euro, mentre i modelli senza filo per grandi superfici o a trazione integrale possono superare i 2.000 €. In mezzo c'è la fascia più ampia, quella dei giardini medi.</p>"""),
            ("s", "nascosti", "I costi che non vedi sull'etichetta", """
<ul>
  <li><strong>Installazione</strong>: gratuita se la fai da te, a pagamento se ti affidi a un installatore per il filo perimetrale.</li>
  <li><strong>Lame di ricambio</strong>: vanno sostituite periodicamente, spesso più volte a stagione. Costano poco, ma vanno messe in conto.</li>
  <li><strong>Accessori</strong>: garage o tettoia, kit di riparazione del filo, ruote per terreni difficili.</li>
  <li><strong>Batteria</strong>: dopo alcune stagioni può perdere autonomia e va sostituita.</li>
  <li><strong>Rete mobile</strong>: alcuni modelli con 4G prevedono un abbonamento dopo il periodo incluso.</li>
  <li><strong>Manutenzione</strong>: alcuni rivenditori offrono un tagliando invernale a pagamento.</li>
</ul>"""),
            ("s", "elettricita", "Quanta corrente consuma?", """
<p>Poca. Facciamo un esempio con numeri tondi: se la batteria del robot ha una capacità di 100 Wh e viene ricaricata una volta al giorno per 200 giorni all'anno, il consumo è di circa 20 kWh. Con un costo dell'energia di 0,30 € al kWh, si spendono circa <strong>6 € all'anno</strong>.</p>
<p>Anche raddoppiando o triplicando le ricariche, la spesa resta nell'ordine di poche decine di euro: molto meno del carburante di un tosaerba a scoppio. Per un calcolo preciso, controlla la capacità della batteria nella scheda del modello e il prezzo dell'energia nella tua bolletta.</p>"""),
            ("s", "conviene", "Conviene rispetto al tosaerba tradizionale?", """
<p>Dal punto di vista economico puro, un tosaerba elettrico costa meno all'acquisto. Ma il conto cambia se dai un valore al tuo tempo:</p>
<ul>
  <li>un'ora alla settimana da aprile a ottobre sono circa <strong>30 ore all'anno</strong>;</li>
  <li>in cinque anni sono <strong>150 ore</strong>, quasi quattro settimane di lavoro;</li>
  <li>se oggi paghi un giardiniere per il taglio, il robot può ripagarsi in poche stagioni.</li>
</ul>
<p>C'è poi la qualità del prato: il taglio frequente e il mulching lo rendono più fitto e uniforme di quanto si ottenga con un taglio settimanale.</p>"""),
            ("b", products_block(
                "Fascia base",
                "Robot della selezione · fascia base",
                "Per prati piccoli e regolari, con le funzioni essenziali.",
                budget="base", robots="true",
            )),
            ("b", products_block(
                "Fascia media",
                "Robot della selezione · fascia media",
                "Più superficie, app e sensori: il miglior equilibrio per molti giardini.",
                budget="medio", robots="true",
            )),
            ("b", products_block(
                "Fascia alta",
                "Robot della selezione · fascia alta",
                "Senza filo, trazione integrale e grandi superfici.",
                budget="alto", robots="true",
            )),
            ("s", "risparmiare", "Come risparmiare sull'acquisto", """
<ol>
  <li><strong>Compra fuori stagione</strong>: tra autunno e inverno la domanda cala e le promozioni sono più frequenti.</li>
  <li><strong>Segui il Black Friday</strong>: è uno dei momenti migliori dell'anno. Leggi la <a href="/robot-tagliaerba-black-friday">guida al Black Friday 2026</a>.</li>
  <li><strong>Valuta il modello dell'anno precedente</strong>: quando escono le novità, i modelli precedenti spesso scendono di prezzo.</li>
  <li><strong>Non sovradimensionare troppo</strong>: un margine del 20–30% basta, oltre paghi capacità che non usi.</li>
  <li><strong>Controlla venditore e garanzia</strong>: un prezzo più basso da un venditore poco affidabile può costare caro in caso di problemi.</li>
</ol>
""" + inline_cta()),
        ],
        "faq_title": "Domande frequenti su prezzi e costi",
        "faq": [
            ("Quanto dura un robot tagliaerba?", "Con una manutenzione regolare può durare molte stagioni. Le parti soggette a usura, come lame e batteria, si sostituiscono. Prima di acquistare controlla la disponibilità dei ricambi in Italia."),
            ("Conviene comprarlo in autunno?", "Spesso sì: la stagione del taglio è finita, ci sono le promozioni del Black Friday e hai tutto l'inverno per prepararti. In primavera il robot sarà pronto a partire."),
            ("Esistono bonus o detrazioni?", "Le agevolazioni fiscali per il verde privato cambiano di anno in anno. Prima di contarci, verifica le regole in vigore sul sito dell'Agenzia delle Entrate o con il tuo commercialista."),
            ("Quanto costano le lame di ricambio?", "In genere poco: si vendono in confezioni da più pezzi. Il prezzo aggiornato dei set compatibili con il tuo modello è su Amazon.it."),
        ],
        "related": ["robot-tagliaerba-black-friday", "come-scegliere-robot-tagliaerba", "manutenzione-robot-tagliaerba"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "installazione-robot-tagliaerba",
        "short": "Installazione",
        "card_title": "Come installare un robot tagliaerba",
        "card_text": "Base di ricarica, posa del filo e mappatura dei modelli senza filo, passo per passo.",
        "title": "Come installare un robot tagliaerba: guida passo passo",
        "desc": "Come installare un robot tagliaerba: preparazione del prato, posizione della base, posa del filo perimetrale e configurazione dei modelli senza filo. Errori da evitare.",
        "eyebrow": "Installazione · Passo passo",
        "h1": "Come installare un robot tagliaerba: la guida passo passo",
        "lead": "Un'installazione fatta bene è metà del risultato. Ecco come preparare il prato, dove mettere la base e come posare il filo o mappare il giardino, evitando gli errori più comuni.",
        "tldr": [
            "Prima di iniziare, taglia l'erba con un tosaerba tradizionale e libera il prato.",
            "La base va in un punto piano, vicino a una presa, con spazio libero davanti.",
            "Il filo si fissa con i picchetti seguendo le distanze indicate nel manuale.",
            "Nei modelli RTK, la posizione dell'antenna è il passaggio più importante.",
        ],
        "body": [
            ("s", "preparare", "Prima di iniziare: prepara il prato", """
<ul>
  <li>Taglia l'erba all'altezza desiderata con un tosaerba tradizionale.</li>
  <li>Raccogli rami, sassi, giochi e tutto ciò che potrebbe intralciare il robot.</li>
  <li>Riempi buche e avvallamenti profondi.</li>
  <li>Leggi il manuale del tuo modello: distanze e requisiti cambiano da produttore a produttore.</li>
</ul>"""),
            ("s", "base", "Dove posizionare la base di ricarica", """
<p>La posizione della base influisce sull'efficienza del robot e sulla sua durata.</p>
<ul>
  <li><strong>In piano</strong>: un terreno inclinato rende difficile l'aggancio alla ricarica.</li>
  <li><strong>Vicino a una presa</strong> adatta all'esterno; l'alimentatore va protetto come indicato nel manuale.</li>
  <li><strong>Con spazio libero davanti</strong>, per l'ingresso e l'uscita del robot.</li>
  <li><strong>All'ombra, se possibile</strong>: il sole diretto scalda la batteria. Un garage per robot aiuta.</li>
  <li><strong>In posizione centrale</strong> nei giardini grandi, per ridurre gli spostamenti.</li>
</ul>"""),
            ("s", "filo", "Installare un robot con filo perimetrale", """
<ol>
  <li><strong>Progetta il percorso</strong>: disegna su un foglio il perimetro, le aiuole da escludere e i passaggi stretti.</li>
  <li><strong>Parti dalla base</strong> e posa il filo lungo il bordo del prato, rispettando le distanze indicate nel manuale: di solito sono diverse per muri, aiuole rialzate e bordi a raso.</li>
  <li><strong>Fissa il filo con i picchetti</strong> a intervalli regolari, ben aderente al terreno.</li>
  <li><strong>Escludi le aiuole</strong> facendo girare il filo intorno e riportandolo indietro affiancato al tratto di andata: i due tratti vicini non vengono «visti» dal robot, che li attraversa.</li>
  <li><strong>Posa il filo guida</strong>, se il tuo modello lo prevede, per aiutare il robot a tornare alla base.</li>
  <li><strong>Collega il filo alla base</strong> con i connettori forniti.</li>
  <li><strong>Fai un giro di prova</strong> e correggi i punti in cui il robot si blocca o esce dal perimetro.</li>
</ol>
""" + callout(
                "Fissare o interrare?",
                "Il filo può restare in superficie, fissato con i picchetti: in poche settimane l'erba lo ricopre. Interrarlo di qualche centimetro lo protegge da arieggiatori e attrezzi. In entrambi i casi segui le indicazioni del produttore.",
            )),
            ("b", products_block(
                "Accessori",
                "Accessori utili per l'installazione",
                "Kit di filo e picchetti per ampliare o riparare il perimetro, garage per proteggere robot e base.",
                category="Accessori",
            )),
            ("s", "senza-filo", "Configurare un robot senza filo", """
<ol>
  <li><strong>Installa la stazione di riferimento</strong> (nei modelli RTK) in un punto con ampia vista del cielo, lontano da alberi alti e muri, seguendo il manuale.</li>
  <li><strong>Collega il robot all'app</strong> e aggiorna il software.</li>
  <li><strong>Mappa il perimetro</strong> guidando il robot lungo il bordo del prato con lo smartphone.</li>
  <li><strong>Crea le zone vietate</strong> per aiuole, orto, piscina e giochi.</li>
  <li><strong>Definisci i percorsi</strong> tra le zone separate.</li>
  <li><strong>Imposta orari e altezza di taglio</strong>, evitando le ore serali e notturne.</li>
  <li><strong>Controlla il primo taglio</strong> e ritocca la mappa dove serve.</li>
</ol>
""" + inline_cta("Non hai ancora scelto il robot?", "Rispondi a quattro domande: ti diciamo se per il tuo giardino conviene un modello con filo o senza filo.")),
            ("s", "errori", "Gli errori più comuni", """
<ul>
  <li>Filo troppo vicino a muri e aiuole rialzate: il robot urta o si incastra.</li>
  <li>Curve troppo strette negli angoli: il robot fatica a seguirle.</li>
  <li>Base in pendenza o senza spazio libero davanti.</li>
  <li>Antenna RTK in un angolo coperto da alberi.</li>
  <li>Primo avvio sull'erba troppo alta.</li>
</ul>"""),
            ("s", "professionista", "Quando chiamare un installatore", """
<p>Se il giardino è grande, molto articolato o hai poco tempo, l'installazione professionale può valere la spesa. Se serve portare la corrente in un nuovo punto del giardino, rivolgiti a un elettricista.</p>
<p>Una volta installato, per tenerlo in forma leggi la <a href="/manutenzione-robot-tagliaerba">guida alla manutenzione</a>.</p>"""),
        ],
        "faq_title": "Domande frequenti sull'installazione",
        "faq": [
            ("Quanto tempo serve per installare il filo?", "Per un piccolo giardino possono bastare poche ore; per un prato grande e articolato anche una giornata o più. Progettare il percorso prima di iniziare fa risparmiare molto tempo."),
            ("Posso installarlo in inverno?", "Sì, ed è un buon momento per prepararsi alla primavera. Per il filo scegli una giornata in cui il terreno non è gelato, così i picchetti entrano facilmente."),
            ("Quanto deve stare lontano il filo dal bordo?", "Dipende dal modello e dal tipo di bordo: le distanze da un muro e da un bordo a raso sono diverse. Il manuale di ogni robot indica i valori corretti."),
        ],
        "related": ["filo-perimetrale-o-senza-filo", "manutenzione-robot-tagliaerba", "robot-tagliaerba-senza-filo"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "manutenzione-robot-tagliaerba",
        "short": "Manutenzione e inverno",
        "card_title": "Manutenzione e rimessaggio invernale",
        "card_text": "Pulizia, lame, batteria e come riporre il robot in inverno per farlo durare di più.",
        "title": "Manutenzione robot tagliaerba e rimessaggio invernale",
        "desc": "Come pulire il robot tagliaerba, quando cambiare le lame, come conservare la batteria e come fare il rimessaggio invernale passo passo. Guida pratica 2026.",
        "eyebrow": "Manutenzione · Inverno 2026",
        "h1": "Manutenzione del robot tagliaerba e rimessaggio invernale",
        "lead": "Pochi minuti di cura ogni settimana e un rimessaggio fatto bene a fine stagione allungano la vita del robot e della batteria. Ecco cosa fare, e quando.",
        "tldr": [
            "Pulisci scocca, ruote e lame regolarmente, senza idropulitrice.",
            "Sostituisci le lame quando il taglio peggiora o secondo le indicazioni del produttore.",
            "In inverno ricarica la batteria e conserva il robot all'asciutto e al riparo dal gelo.",
            "Prima della nuova stagione, aggiorna il software dall'app.",
        ],
        "body": [
            ("s", "settimana", "La cura di ogni settimana", """
<ul>
  <li><strong>Spegni il robot</strong> e attiva il blocco prima di qualsiasi operazione; usa guanti protettivi vicino alle lame.</li>
  <li><strong>Pulisci la parte inferiore</strong> con una spazzola o un raschietto di plastica: l'erba accumulata peggiora il taglio.</li>
  <li><strong>Controlla le ruote</strong> e togli fango ed erba dal battistrada.</li>
  <li><strong>Pulisci i contatti di ricarica</strong> del robot e della base.</li>
  <li><strong>Non usare l'idropulitrice</strong>: l'acqua ad alta pressione può danneggiare l'elettronica. Alcuni modelli si possono sciacquare con acqua a bassa pressione: verifica nel manuale.</li>
</ul>"""),
            ("s", "lame", "Le lame: quando e come sostituirle", """
<p>Lame consumate strappano l'erba invece di tagliarla: le punte ingialliscono e il prato diventa più vulnerabile alle malattie. Molti robot usano lame piccole e leggere, simili a lamette, da sostituire spesso; altri hanno un disco o una lama unica.</p>
<p>Segui gli intervalli indicati dal produttore e anticipali se il prato ha molti rametti, sassi o terreno sabbioso. Sostituisci tutte le lame insieme, con le viti nuove, per mantenere il disco bilanciato.</p>"""),
            ("b", products_block(
                "Ricambi",
                "Ricambi e accessori della selezione",
                "Lame, garage e kit per tenere il robot in forma. Controlla sempre la compatibilità con il tuo modello.",
                category="Accessori",
            )),
            ("s", "batteria", "La batteria", """
<p>Le batterie agli ioni di litio dei robot non amano né il caldo eccessivo né il gelo. In estate un garage o una tettoia sopra la base riducono la temperatura; in inverno la batteria va conservata in un luogo asciutto e non troppo freddo.</p>
<p>Dopo alcune stagioni l'autonomia diminuisce: è normale. Quando il robot non riesce più a completare il lavoro, la batteria si può sostituire con un ricambio originale.</p>"""),
            ("s", "inverno", "Rimessaggio invernale passo passo", """
<ol>
  <li><strong>Fai l'ultimo taglio</strong> quando l'erba smette di crescere, di solito tra fine ottobre e novembre.</li>
  <li><strong>Pulisci a fondo</strong> scocca, lame, ruote e contatti.</li>
  <li><strong>Ricarica la batteria</strong> come indicato dal produttore prima di riporre il robot.</li>
  <li><strong>Spegni il robot</strong> completamente.</li>
  <li><strong>Conservalo in casa, in garage o in cantina</strong>, all'asciutto e al riparo dal gelo, appoggiato sulle ruote.</li>
  <li><strong>Base di ricarica</strong>: molti produttori consigliano di scollegarla e riporla al chiuso; il filo perimetrale può restare nel terreno.</li>
  <li><strong>Antenna RTK</strong>: segui le indicazioni del manuale, alcuni modelli prevedono di lasciarla installata.</li>
</ol>
""" + callout(
                "Il tagliando invernale",
                "Alcuni rivenditori e centri assistenza offrono un controllo completo durante l'inverno: pulizia, verifica della batteria e aggiornamenti. È il momento giusto, perché in primavera i centri sono molto più impegnati.",
            )),
            ("s", "primavera", "La ripartenza in primavera", check_list([
                "Ricarica completamente il robot prima del primo utilizzo.",
                "Aggiorna il software dall'app.",
                "Monta lame nuove.",
                "Controlla il filo perimetrale o la mappa del giardino.",
                "Se l'erba è cresciuta molto, fai un primo taglio con un tosaerba tradizionale.",
                "Riprogramma gli orari, sempre di giorno.",
            ]) + inline_cta("Il tuo robot ha fatto il suo tempo?", "Se pensi a un modello nuovo per la prossima stagione, il quiz ti aiuta a scegliere in 30 secondi.")),
        ],
        "faq_title": "Domande frequenti sulla manutenzione",
        "faq": [
            ("Posso lasciare il robot fuori d'inverno?", "In genere è sconsigliato: gelo e umidità prolungata non fanno bene a batteria ed elettronica. Segui le indicazioni del produttore, che di solito consiglia di conservarlo al chiuso."),
            ("Posso lavarlo con la pompa del giardino?", "Alcuni modelli lo permettono con acqua a bassa pressione, altri no. Non usare mai l'idropulitrice e controlla sempre il manuale."),
            ("Ogni quanto vanno cambiate le lame?", "Dipende dal tipo di lama, dal prato e dalle ore di lavoro. Il produttore indica un intervallo consigliato: anticipalo se noti che l'erba viene strappata invece che tagliata."),
            ("Il filo perimetrale va tolto in inverno?", "No, il filo può restare nel terreno tutto l'anno. Conviene invece scollegare e riporre la base, se il produttore lo consiglia."),
        ],
        "related": ["installazione-robot-tagliaerba", "quanto-costa-robot-tagliaerba", "robot-tagliaerba-black-friday"],
    },
    # ------------------------------------------------------------------
    {
        "slug": "robot-tagliaerba-black-friday",
        "short": "Black Friday 2026",
        "card_title": "Black Friday 2026: guida alle offerte",
        "card_text": "Date, come riconoscere uno sconto vero e cosa controllare prima di acquistare.",
        "title": "Robot tagliaerba Black Friday 2026: guida alle offerte",
        "desc": "Black Friday 2026 il 27 novembre: come riconoscere le offerte vere sui robot tagliaerba, cosa controllare prima di comprare su Amazon.it e i modelli da tenere d'occhio.",
        "eyebrow": "Offerte · Novembre 2026",
        "h1": "Robot tagliaerba al Black Friday 2026: come riconoscere le offerte vere",
        "lead": "Il Black Friday 2026 cade venerdì 27 novembre. Per chi pensa a un robot tagliaerba è uno dei momenti migliori dell'anno per acquistare, a patto di saper distinguere uno sconto vero da uno solo apparente.",
        "tldr": [
            "Black Friday: venerdì 27 novembre 2026. Cyber Monday: lunedì 30 novembre.",
            "Le promozioni su Amazon.it di solito iniziano alcuni giorni prima.",
            "Per legge, uno sconto deve fare riferimento al prezzo più basso dei 30 giorni precedenti.",
            "Scegli prima il modello giusto, poi aspetta l'offerta: non il contrario.",
        ],
        "body": [
            ("s", "date", "Le date del Black Friday 2026", table(
                ["Evento", "Data"],
                [
                    ["Black Friday", "Venerdì 27 novembre 2026"],
                    ["Cyber Monday", "Lunedì 30 novembre 2026"],
                    ["Settimana del Black Friday", "I giorni precedenti, secondo il calendario annunciato da Amazon.it"],
                ],
            ) + """
<p>Negli ultimi anni Amazon ha anticipato le promozioni con una «settimana del Black Friday» che parte alcuni giorni prima del venerdì. Le date precise vengono annunciate di anno in anno: tieni d'occhio la pagina del prodotto che ti interessa.</p>"""),
            ("s", "perche-ora", "Perché novembre è un buon momento", check_list([
                "La stagione del taglio è finita: la domanda cala e le promozioni aumentano.",
                "Hai tutto l'inverno per installare con calma il filo o mappare il giardino.",
                "In primavera, quando l'erba riparte, il robot è già al lavoro.",
                "Puoi trovare in offerta anche i modelli della stagione appena conclusa.",
                "È un regalo di Natale che si usa per anni.",
            ])),
            ("b", picks_block(
                "Da tenere d'occhio",
                "Le migliori scelte da seguire al Black Friday",
                "Un robot per ogni esigenza: apri la pagina Amazon per vedere prezzo e disponibilità aggiornati.",
            )),
            ("s", "sconti-veri", "Come riconoscere uno sconto vero", """
<p>Dal 2023, in Italia, chi annuncia una riduzione di prezzo deve indicare come riferimento il <strong>prezzo più basso applicato nei 30 giorni precedenti</strong>. È una regola introdotta nel Codice del consumo con il recepimento della cosiddetta Direttiva Omnibus, e rende più difficile gonfiare il prezzo pochi giorni prima dello sconto.</p>
<p>Oltre a questo, puoi difenderti così:</p>
<ol>
  <li><strong>Controlla lo storico dei prezzi</strong> con uno dei servizi gratuiti che lo registrano per i prodotti Amazon.</li>
  <li><strong>Confronta modelli simili</strong>, non solo lo stesso modello in momenti diversi.</li>
  <li><strong>Diffida degli sconti enormi</strong> su modelli poco conosciuti o senza recensioni.</li>
  <li><strong>Guarda le caratteristiche, non la percentuale</strong>: un robot inadatto al tuo giardino non è un affare, nemmeno al 40% di sconto.</li>
</ol>"""),
            ("s", "acquisto", "Prima di cliccare su «Acquista»", """
<ul>
  <li><strong>Venditore</strong>: controlla se il prodotto è venduto e spedito da Amazon o da un venditore terzo, e leggi le sue valutazioni.</li>
  <li><strong>Garanzia</strong>: in Italia la garanzia legale di conformità per i consumatori dura 24 mesi. Verifica anche se il produttore offre un'estensione.</li>
  <li><strong>Resi</strong>: negli ultimi anni Amazon ha esteso il periodo di reso per molti acquisti fatti nel periodo natalizio. Controlla le condizioni in vigore quest'anno.</li>
  <li><strong>Compatibilità</strong>: superficie, pendenza, passaggi stretti e Wi-Fi in giardino. Se hai dubbi, fai il <a href="/#quiz">quiz in 30 secondi</a>.</li>
  <li><strong>Accessori</strong>: garage e lame di ricambio sono spesso in promozione nello stesso periodo.</li>
</ul>
""" + callout(
                "La strategia migliore",
                "Scegli adesso il modello adatto al tuo giardino e salva la sua pagina. Quando arriva il Black Friday controlli il prezzo e decidi in un minuto, senza farti guidare dalla fretta.",
            )),
            ("b", products_block(
                "La selezione",
                "Tutti i robot da confrontare",
                "Apri “Scopri di più” per pregi e limiti di ogni modello.",
                robots="true",
            )),
            ("b", products_block(
                "Accessori",
                "Accessori e idee regalo",
                "Garage, lame e kit: utili per chi ha già un robot tagliaerba.",
                category="Accessori",
            )),
            ("s", "regalo", "Un robot tagliaerba come regalo di Natale", """
<p>Per chi ha un giardino è uno dei regali più apprezzati: restituisce tempo ogni settimana, per anni. Se lo regali, scegli un modello adatto al giardino di chi lo riceverà, a partire da superficie e pendenza, e conserva la ricevuta per l'eventuale cambio.</p>
""" + inline_cta()),
        ],
        "faq_title": "Domande frequenti sul Black Friday",
        "faq": [
            ("Quando inizia il Black Friday 2026 su Amazon?", "Il Black Friday è venerdì 27 novembre 2026 e il Cyber Monday lunedì 30 novembre. Le promozioni di Amazon.it di solito partono alcuni giorni prima: le date precise vengono annunciate da Amazon."),
            ("Conviene aspettare la primavera?", "In primavera la domanda è al massimo e gli sconti sono meno frequenti. Comprare a novembre ti permette di approfittare delle promozioni e di installare il robot con calma."),
            ("Le offerte durano poco?", "Alcune sì, altre restano attive per tutta la settimana del Black Friday. Il modo migliore per non farsi prendere dalla fretta è scegliere il modello in anticipo."),
            ("Posso restituire il robot se non va bene?", "Su Amazon.it valgono le condizioni di reso indicate nella pagina del prodotto e del venditore, spesso estese nel periodo natalizio. Come consumatore hai inoltre la garanzia legale di 24 mesi."),
        ],
        "related": ["quanto-costa-robot-tagliaerba", "come-scegliere-robot-tagliaerba", "robot-tagliaerba-senza-filo"],
    },
]

# Raggruppamento nella pagina "Guide" e nel footer
GROUPS = [
    ("Scegliere il robot", [
        "come-scegliere-robot-tagliaerba",
        "filo-perimetrale-o-senza-filo",
        "robot-tagliaerba-senza-filo",
        "quanto-costa-robot-tagliaerba",
        "robot-tagliaerba-black-friday",
    ]),
    ("Per il tuo giardino", [
        "robot-tagliaerba-piccoli-giardini",
        "robot-tagliaerba-giardini-medi",
        "robot-tagliaerba-giardini-grandi",
        "robot-tagliaerba-pendenza",
    ]),
    ("Installazione e cura", [
        "installazione-robot-tagliaerba",
        "manutenzione-robot-tagliaerba",
    ]),
]

# Guide in evidenza in home
HOME_FEATURED = [
    "come-scegliere-robot-tagliaerba",
    "robot-tagliaerba-senza-filo",
    "filo-perimetrale-o-senza-filo",
    "quanto-costa-robot-tagliaerba",
    "robot-tagliaerba-pendenza",
    "robot-tagliaerba-black-friday",
]

HOME_FAQ = [
    ("Serve per forza il filo perimetrale?", "No. I robot tradizionali usano un filo posato lungo i bordi del prato per capire dove fermarsi. I modelli senza filo si orientano con il posizionamento satellitare GPS RTK, che di solito richiede un'antenna con buona vista del cielo, oppure con telecamere e altri sensori. I confini si disegnano dall'app."),
    ("Il robot tagliaerba funziona anche sotto la pioggia?", "Molti modelli hanno un sensore pioggia: quando inizia a piovere tornano alla base e riprendono più tardi. La resistenza all'acqua è indicata dal grado di protezione IP nella scheda del prodotto. Tagliare l'erba bagnata in genere dà un risultato meno pulito."),
    ("Quanto tempo serve per installarlo?", "Con il filo perimetrale bisogna posarlo e fissarlo lungo tutto il bordo del prato: secondo la dimensione e la forma del giardino può volerci da qualche ora a una giornata. I modelli senza filo si configurano dall'app, accompagnando il robot lungo i bordi, e di solito richiedono meno lavoro."),
    ("Devo raccogliere l'erba tagliata?", "No. Il robot taglia spesso e poco alla volta (mulching): i frammenti d'erba sono molto piccoli, restano sul prato e si decompongono, restituendo nutrienti al terreno."),
    ("È sicuro con bambini e animali domestici?", "I robot hanno di norma sensori che fermano le lame se vengono sollevati o ribaltati, e molti rilevano gli urti. Resta buona regola tenere bambini e animali lontani mentre lavora e programmare il taglio di giorno, quando ricci e altri piccoli animali selvatici non sono attivi."),
    ("Si può rubare?", "Molti modelli si bloccano con un codice PIN, hanno un allarme se vengono sollevati e, nei modelli connessi, si possono localizzare dall'app. Alcuni hanno un modulo GPS o la rete mobile per seguirne la posizione: controlla nella scheda quali protezioni offre il modello che ti interessa."),
    ("Quanto costa mantenerlo?", "Le spese principali sono le lame, da sostituire periodicamente per un taglio netto, e la batteria, che dopo alcune stagioni può perdere autonomia. Il consumo elettrico per la ricarica è in genere contenuto: pochi euro all'anno per molti giardini."),
    ("Cosa devo fare in inverno?", "Di solito si pulisce il robot, si ricarica la batteria e lo si ripone al riparo, all'asciutto e lontano dal gelo. Alcuni produttori consigliano di riporre anche la base di ricarica: segui le istruzioni del tuo modello."),
]
