/* ==================================================================
   PRATOSMART — Funzioni condivise da tutte le pagine
   I dati (prodotti, configurazione, categorie, quiz) sono in
   /assets/products.js: qui NON è necessario modificare nulla.

   Le pagine indicano cosa mostrare con alcuni attributi HTML:
   - data-products            griglia di schede prodotto. Filtri facoltativi:
       data-category="A|B"    solo queste categorie
       data-ids="id1,id2"     solo questi prodotti, in questo ordine
       data-budget="medio"    solo questa fascia di spesa
       data-wireless="true"   solo senza filo ("false": solo con filo)
       data-tag="pendenza"    solo i prodotti con questo tag
       data-robots="true"     esclude gli accessori
       data-limit="6"         numero massimo di schede
   - data-picks               corpo della tabella "Le migliori scelte"
   - #quiz-box                quiz "Trova il tuo robot"
   - #hero-carousel           carosello della home
   ================================================================== */
'use strict';

(function () {
  const toastEl = document.getElementById("toast");

  /* ---------- Utilità ---------- */

  function getCategory(label) {
    return CATEGORIES.find(function (c) { return c.label === label; }) || null;
  }

  let toastTimer = null;
  function showToast(message) {
    if (!toastEl) return;
    toastEl.textContent = message;
    toastEl.classList.add("is-visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toastEl.classList.remove("is-visible");
    }, 5200);
  }

  function prefersReducedMotion() {
    return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  function splitList(value, separator) {
    return String(value || "").split(separator).map(function (s) { return s.trim(); }).filter(Boolean);
  }

  /* ---------- Statistiche facoltative (Plausible o Umami) ----------
     Se in futuro aggiungi Plausible o Umami (configurati senza cookie),
     i clic verso Amazon e i quiz completati vengono registrati da soli.
     Senza questi strumenti la funzione non fa nulla.
     Ricorda di aggiornare privacy e cookie policy prima di attivarli. */
  function track(eventName, props) {
    try {
      if (typeof window.plausible === "function") window.plausible(eventName, { props: props });
      else if (window.umami && typeof window.umami.track === "function") window.umami.track(eventName, props);
    } catch (e) { /* le statistiche non devono mai bloccare il sito */ }
  }

  /* ---------- Dati tecnici ---------- */
  function getSpecs(product) {
    return product && product.specs && typeof product.specs === "object" ? product.specs : {};
  }

  function toPositiveNumber(value) {
    const n = Number(value);
    return Number.isFinite(n) && n > 0 ? n : 0;
  }

  function isRobot(product) {
    return product.category !== "Accessori";
  }

  function isWireless(product) {
    return product.category === "Senza filo perimetrale" ||
      /rtk|visione|senza filo|wire.?free/i.test(String(getSpecs(product).navigation || ""));
  }

  function hasTag(product, tag) {
    return Array.isArray(product.tags) && product.tags.indexOf(tag) >= 0;
  }

  // Elenco dei dati compilati, nell'ordine in cui vengono mostrati
  function getSpecList(product) {
    const s = getSpecs(product);
    const list = [];
    const area = toPositiveNumber(s.area);
    const slope = toPositiveNumber(s.slope);
    const noise = toPositiveNumber(s.noise);
    if (area) list.push({ key: "area", label: "Superficie", value: "fino a " + area.toLocaleString("it-IT") + " m²" });
    if (slope) list.push({ key: "slope", label: "Pendenza", value: "fino al " + slope + "%" });
    if (String(s.navigation || "").trim()) list.push({ key: "navigation", label: "Installazione", value: String(s.navigation).trim() });
    if (String(s.connectivity || "").trim()) list.push({ key: "connectivity", label: "App", value: String(s.connectivity).trim() });
    if (noise) list.push({ key: "noise", label: "Rumore", value: noise + " dB" });
    if (String(s.cutHeight || "").trim()) list.push({ key: "cutHeight", label: "Altezza di taglio", value: String(s.cutHeight).trim() });
    return list;
  }

  function getSpecValue(product, key) {
    const found = getSpecList(product).find(function (item) { return item.key === key; });
    return found ? found.value : "—";
  }

  /* ---------- Validazione dei link affiliati ---------- */
  function checkAffiliateUrl(raw) {
    const value = String(raw || "").trim();
    if (!value) return { ok: false, reason: "missing" };
    let url;
    try {
      url = new URL(value);
    } catch (e) {
      return { ok: false, reason: "invalid" };
    }
    if (url.protocol !== "https:" && url.protocol !== "http:") return { ok: false, reason: "invalid" };
    return { ok: true, href: url.href };
  }

  function affiliateErrorMessage(product, reason) {
    const id = product.id || "(senza id)";
    if (reason === "missing") {
      return "Link affiliato mancante: compila il campo \"affiliateUrl\" del prodotto \"" + id + "\" in assets/products.js.";
    }
    return "Il campo \"affiliateUrl\" del prodotto \"" + id + "\" non contiene un indirizzo valido: deve iniziare con https://";
  }

  /* ---------- Validazione degli URL delle immagini ---------- */
  function getSafeImageUrl(raw) {
    const value = String(raw || "").trim();
    if (!value) return null;
    const isAbsolute = /^([a-z][a-z0-9+.-]*:|\/\/)/i.test(value);
    try {
      const url = new URL(value, document.baseURI);
      if (isAbsolute && url.protocol !== "https:") return null;
      return url.href;
    } catch (e) {
      return null;
    }
  }

  const MAX_IMAGES = 3;

  function getProductImages(product) {
    const list = (Array.isArray(product.images) ? product.images : []).concat(product.imageUrl || []);
    const seen = new Set();
    return list.map(getSafeImageUrl).filter(function (url) {
      if (!url || seen.has(url)) return false;
      seen.add(url);
      return true;
    }).slice(0, MAX_IMAGES);
  }

  /* ---------- Elementi di base (solo metodi DOM sicuri) ---------- */
  function createPlaceholder(product) {
    const ph = document.createElement("div");
    ph.className = "ph";
    ph.setAttribute("role", "img");
    ph.setAttribute("aria-label", "Immagine non ancora disponibile per " + product.title);
    const icon = document.createElement("span");
    icon.className = "ph-icon";
    icon.setAttribute("aria-hidden", "true");
    const label = document.createElement("span");
    label.className = "ph-label";
    label.setAttribute("aria-hidden", "true");
    label.textContent = "PratoSmart";
    ph.append(icon, label);
    return ph;
  }

  function createSvg(paths, strokeWidth) {
    const ns = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(ns, "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", strokeWidth || "2");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    svg.setAttribute("aria-hidden", "true");
    paths.forEach(function (d) {
      const path = document.createElementNS(ns, "path");
      path.setAttribute("d", d);
      svg.appendChild(path);
    });
    return svg;
  }

  function createExternalIcon() {
    return createSvg(["M7 17L17 7", "M9 7h8v8"]);
  }

  function createBadge(product, extraClass) {
    const text = String(product.badge || "").trim();
    if (!text) return null;
    const badge = document.createElement("span");
    badge.className = "badge" + (extraClass ? " " + extraClass : "");
    badge.textContent = text;
    return badge;
  }

  // Miniatura usata nella tabella comparativa e nei risultati del quiz
  function createThumb(product, className) {
    const box = document.createElement("div");
    box.className = className;
    const category = getCategory(product.category);
    if (category) box.style.setProperty("--tint", category.tint);
    const src = getProductImages(product)[0];
    if (src) {
      const img = document.createElement("img");
      img.alt = "";
      img.loading = "lazy";
      img.decoding = "async";
      img.referrerPolicy = "no-referrer";
      img.addEventListener("error", function () {
        img.replaceWith(createPlaceholder(product));
      }, { once: true });
      img.src = src;
      box.appendChild(img);
    } else {
      box.appendChild(createPlaceholder(product));
    }
    return box;
  }

  /* Pulsante "Verifica disponibilità": link affiliato, oppure avviso se manca.
     "placement" indica dove si trova il pulsante (per le statistiche facoltative). */
  function createAffiliateAction(product, placement, noteId) {
    const check = checkAffiliateUrl(product.affiliateUrl);

    if (check.ok) {
      const link = document.createElement("a");
      link.className = "btn btn-cta btn-affiliate";
      link.href = check.href;
      link.target = "_blank";
      link.rel = "sponsored nofollow noopener noreferrer";
      link.dataset.product = product.id;
      link.dataset.placement = placement;
      link.setAttribute("aria-describedby", "affiliate-hint");
      link.append(document.createTextNode("Verifica disponibilità"), createExternalIcon());
      return [link];
    }

    // Link mancante o non valido: nessun reindirizzamento, solo un messaggio chiaro
    const message = affiliateErrorMessage(product, check.reason);
    const button = document.createElement("button");
    button.type = "button";
    button.className = "btn btn-affiliate is-missing";
    button.textContent = "Verifica disponibilità";

    if (!noteId) {
      button.addEventListener("click", function () { showToast(message); });
      return [button];
    }

    const note = document.createElement("p");
    note.className = "card-note";
    note.id = noteId;
    note.hidden = true;
    note.textContent = message;
    button.setAttribute("aria-describedby", noteId);
    button.addEventListener("click", function () {
      note.hidden = false;
      showToast(message);
    });
    return [button, note];
  }

  /* ---------- Galleria foto nelle schede ---------- */
  function createGalleryButton(direction) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "gallery-btn gallery-" + direction;
    btn.setAttribute("aria-label", direction === "prev" ? "Foto precedente" : "Foto successiva");
    btn.appendChild(createSvg([direction === "prev" ? "M15 6l-6 6 6 6" : "M9 6l6 6-6 6"], "1.8"));
    return btn;
  }

  function createGallery(product, images, media) {
    const fragment = document.createDocumentFragment();

    const gallery = document.createElement("div");
    gallery.className = "gallery";
    gallery.tabIndex = 0;
    gallery.setAttribute("role", "group");
    gallery.setAttribute("aria-roledescription", "galleria");
    gallery.setAttribute("aria-label", "Foto di " + product.title);

    const prev = createGalleryButton("prev");
    const next = createGalleryButton("next");
    const dots = document.createElement("div");
    dots.className = "gallery-dots";
    dots.setAttribute("aria-hidden", "true");

    function items() { return gallery.querySelectorAll(".gallery-item"); }
    function currentIndex() {
      return gallery.clientWidth ? Math.round(gallery.scrollLeft / gallery.clientWidth) : 0;
    }

    function update() {
      const count = items().length;
      const index = Math.min(currentIndex(), count - 1);
      const multiple = count > 1;
      prev.hidden = next.hidden = dots.hidden = !multiple;
      prev.disabled = index <= 0;
      next.disabled = index >= count - 1;
      if (dots.children.length !== count) {
        dots.replaceChildren();
        for (let i = 0; i < count; i++) dots.appendChild(document.createElement("span"));
      }
      Array.prototype.forEach.call(dots.children, function (dot, i) {
        dot.classList.toggle("is-active", i === index);
      });
    }

    let animating = false;
    let animationId = 0;
    let targetIndex = 0;
    let finishCurrent = null;
    function baseIndex() { return animating ? targetIndex : currentIndex(); }
    function goTo(index) {
      const list = items();
      if (!list.length) return;
      if (animating && finishCurrent) finishCurrent();
      index = Math.max(0, Math.min(list.length - 1, index));
      const from = gallery.scrollLeft;
      const to = list[index].offsetLeft;
      targetIndex = index;
      if (from === to) return;
      if (prefersReducedMotion()) {
        gallery.scrollLeft = to;
        return;
      }
      const id = ++animationId;
      animating = true;
      finishCurrent = finish;
      gallery.style.scrollSnapType = "none";
      const duration = 380;
      const startTime = performance.now();
      function finish() {
        if (id !== animationId || !animating) return;
        gallery.scrollLeft = to;
        gallery.style.scrollSnapType = "";
        animating = false;
        update();
      }
      function step(now) {
        if (id !== animationId || !animating) return;
        const t = Math.min(1, (now - startTime) / duration);
        const eased = 1 - Math.pow(1 - t, 3);
        gallery.scrollLeft = from + (to - from) * eased;
        if (t < 1) requestAnimationFrame(step);
        else finish();
      }
      requestAnimationFrame(step);
      setTimeout(finish, duration + 120);
    }

    images.forEach(function (src, i) {
      const item = document.createElement("div");
      item.className = "gallery-item";
      const img = document.createElement("img");
      img.alt = images.length > 1 ? product.title + " — foto " + (i + 1) + " di " + images.length : product.title;
      img.loading = "lazy";
      img.decoding = "async";
      img.referrerPolicy = "no-referrer";
      img.width = 600;
      img.height = 600;
      img.addEventListener("error", function () {
        item.remove();
        if (!items().length) {
          media.replaceChildren(createPlaceholder(product));
          const badge = createBadge(product, "card-badge");
          if (badge) media.appendChild(badge);
        } else {
          update();
        }
      }, { once: true });
      img.src = src;
      item.appendChild(img);
      gallery.appendChild(item);
    });

    prev.addEventListener("click", function () { goTo(baseIndex() - 1); });
    next.addEventListener("click", function () { goTo(baseIndex() + 1); });
    gallery.addEventListener("scroll", update, { passive: true });

    update();
    fragment.append(gallery, prev, next, dots);
    return fragment;
  }

  /* ---------- Schede prodotto ---------- */
  function cleanList(value, max) {
    return Array.isArray(value) ? value.map(function (v) { return String(v || "").trim(); }).filter(Boolean).slice(0, max) : [];
  }

  function createFitBlock(kind, heading, items) {
    const block = document.createElement("div");
    block.className = "fit-block fit-" + kind;
    const h = document.createElement("h4");
    h.textContent = heading;
    const list = document.createElement("ul");
    list.className = "fit-list";
    items.forEach(function (text) {
      const li = document.createElement("li");
      li.textContent = text;
      list.appendChild(li);
    });
    block.append(h, list);
    return block;
  }

  const usedCardIds = new Set();

  function createCard(product, suffix) {
    const uid = suffix + "-" + product.id;
    const titleId = "title-" + uid;
    const card = document.createElement("article");
    card.className = "card";
    // L'ancora #card-<id> va solo alla prima scheda di quel prodotto nella pagina
    if (!usedCardIds.has(product.id)) {
      card.id = "card-" + product.id;
      usedCardIds.add(product.id);
    }
    card.dataset.category = product.category;
    card.setAttribute("aria-labelledby", titleId);

    const category = getCategory(product.category);
    if (category) card.style.setProperty("--tint", category.tint);

    const media = document.createElement("div");
    media.className = "card-media";
    const images = getProductImages(product);
    if (images.length) {
      media.appendChild(createGallery(product, images, media));
    } else {
      media.appendChild(createPlaceholder(product));
    }
    const badge = createBadge(product, "card-badge");
    if (badge) media.appendChild(badge);

    const body = document.createElement("div");
    body.className = "card-body";

    const cat = document.createElement("p");
    cat.className = "card-cat";
    cat.textContent = product.category;

    const title = document.createElement("h3");
    title.className = "card-title";
    title.id = titleId;
    title.textContent = product.title;

    body.append(cat, title);

    const specs = getSpecList(product).slice(0, 4);
    if (specs.length) {
      const dl = document.createElement("dl");
      dl.className = "card-specs";
      specs.forEach(function (item) {
        const row = document.createElement("div");
        const dt = document.createElement("dt");
        dt.textContent = item.label;
        const dd = document.createElement("dd");
        dd.textContent = item.value;
        row.append(dt, dd);
        dl.appendChild(row);
      });
      body.appendChild(dl);
    }

    const detailsId = "details-" + uid;
    const desc = document.createElement("p");
    desc.className = "card-desc";
    desc.textContent = product.description;

    const details = document.createElement("div");
    details.className = "card-details";
    details.id = detailsId;
    details.appendChild(desc);

    const benefits = cleanList(product.benefits, 3);
    if (benefits.length) {
      const list = document.createElement("ul");
      list.className = "card-benefits";
      list.setAttribute("aria-label", "Caratteristiche");
      benefits.forEach(function (b) {
        const li = document.createElement("li");
        li.textContent = b;
        list.appendChild(li);
      });
      details.appendChild(list);
    }

    const idealFor = cleanList(product.idealFor, 3);
    const notFor = cleanList(product.notFor, 2);
    if (idealFor.length || notFor.length) {
      const fit = document.createElement("div");
      fit.className = "card-fit";
      if (idealFor.length) fit.appendChild(createFitBlock("yes", "Ideale se", idealFor));
      if (notFor.length) fit.appendChild(createFitBlock("no", "Lascia perdere se", notFor));
      details.appendChild(fit);
    }

    const more = document.createElement("button");
    more.type = "button";
    more.className = "card-more";
    more.textContent = "Scopri di più";
    more.setAttribute("aria-expanded", "false");
    more.setAttribute("aria-controls", detailsId);
    more.addEventListener("click", function () {
      const open = card.classList.toggle("is-open");
      more.setAttribute("aria-expanded", String(open));
      more.textContent = open ? "Mostra meno" : "Scopri di più";
    });

    body.append(details, more);

    const actions = document.createElement("div");
    actions.className = "card-actions";
    actions.append.apply(actions, createAffiliateAction(product, "scheda", "note-" + uid));
    body.appendChild(actions);

    card.append(media, body);
    return card;
  }

  function filterProducts(el) {
    const ids = splitList(el.dataset.ids, ",");
    if (ids.length) {
      return ids.map(function (id) {
        return products.find(function (p) { return p.id === id; });
      }).filter(Boolean);
    }
    const categories = splitList(el.dataset.category, "|");
    const budget = el.dataset.budget || "";
    const wireless = el.dataset.wireless || "";
    const tag = el.dataset.tag || "";
    const robotsOnly = el.dataset.robots === "true";
    return products.filter(function (p) {
      if (categories.length && categories.indexOf(p.category) < 0) return false;
      if (budget && p.budget !== budget) return false;
      if (wireless === "true" && !(isRobot(p) && isWireless(p))) return false;
      if (wireless === "false" && !(isRobot(p) && !isWireless(p))) return false;
      if (tag && !hasTag(p, tag)) return false;
      if (robotsOnly && !isRobot(p)) return false;
      return true;
    });
  }

  function renderProductGrids() {
    document.querySelectorAll("[data-products]").forEach(function (grid, gridIndex) {
      let list = filterProducts(grid);
      const limit = parseInt(grid.dataset.limit, 10);
      if (limit > 0) list = list.slice(0, limit);
      if (!list.length) {
        // Nessun prodotto adatto: si nasconde l'intero blocco
        const block = grid.closest("[data-product-block]");
        if (block) block.hidden = true;
        return;
      }
      grid.replaceChildren.apply(grid, list.map(function (p) { return createCard(p, "g" + gridIndex); }));
    });
  }

  /* ---------- Evidenziazione delle schede ---------- */
  let highlightTimer = null;
  function highlightCards(cards, toastMessage) {
    document.querySelectorAll(".card.is-highlight").forEach(function (c) { c.classList.remove("is-highlight"); });
    if (!cards.length) return;
    cards.forEach(function (c) { c.classList.add("is-highlight"); });
    cards[0].scrollIntoView({ behavior: prefersReducedMotion() ? "auto" : "smooth", block: "center" });
    const more = cards[0].querySelector(".card-more");
    if (more) more.focus({ preventScroll: true });
    if (toastMessage) showToast(toastMessage);
    clearTimeout(highlightTimer);
    highlightTimer = setTimeout(function () {
      cards.forEach(function (c) { c.classList.remove("is-highlight"); });
    }, 6000);
  }

  // Porta alla scheda del prodotto e la apre; se non è in questa pagina, va in home
  function focusCard(productId) {
    const card = document.getElementById("card-" + productId);
    if (!card) {
      const onHome = /\/$|\/index(\.html)?$/.test(location.pathname);
      if (!onHome) window.location.href = "index.html#card-" + encodeURIComponent(productId);
      return;
    }
    if (!card.classList.contains("is-open")) {
      const more = card.querySelector(".card-more");
      if (more) more.click();
    }
    highlightCards([card], null);
  }

  function createCardLink(product) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "link-button";
    button.textContent = "Vedi la scheda";
    button.setAttribute("aria-label", "Vedi la scheda di " + product.title);
    button.addEventListener("click", function () { focusCard(product.id); });
    return button;
  }

  function setupGuideButtons() {
    document.querySelectorAll("[data-guide-category]").forEach(function (button) {
      button.addEventListener("click", function () {
        const category = button.dataset.guideCategory;
        const cards = Array.prototype.filter.call(document.querySelectorAll("#prodotti .card"), function (card) {
          return card.dataset.category === category;
        });
        if (!cards.length) {
          const target = document.getElementById("prodotti");
          if (target) target.scrollIntoView({ block: "start" });
          return;
        }
        highlightCards(cards, cards.length + (cards.length === 1 ? " prodotto adatto: " : " prodotti adatti: ") + category.toLowerCase());
      });
    });
  }

  /* ---------- Tabella "Le migliori scelte" ---------- */
  const PICK_COLUMNS = [
    { key: "area", label: "Superficie" },
    { key: "slope", label: "Pendenza" },
    { key: "navigation", label: "Installazione" },
    { key: "connectivity", label: "App" }
  ];

  function createPickRow(product) {
    const row = document.createElement("tr");

    const productCell = document.createElement("td");
    productCell.className = "pick-cell-product";
    const wrap = document.createElement("div");
    wrap.className = "pick-product";
    const info = document.createElement("div");
    const name = document.createElement("p");
    name.className = "pick-name";
    name.textContent = product.title;
    const badge = createBadge(product);
    if (badge) info.appendChild(badge);
    info.append(name, createCardLink(product));
    wrap.append(createThumb(product, "pick-thumb"), info);
    productCell.appendChild(wrap);
    row.appendChild(productCell);

    PICK_COLUMNS.forEach(function (col) {
      const td = document.createElement("td");
      td.className = "pick-spec";
      td.dataset.label = col.label;
      td.textContent = getSpecValue(product, col.key);
      row.appendChild(td);
    });

    const cta = document.createElement("td");
    cta.className = "pick-cta";
    cta.append.apply(cta, createAffiliateAction(product, "tabella", null));
    row.appendChild(cta);
    return row;
  }

  function renderPicks() {
    document.querySelectorAll("[data-picks]").forEach(function (body) {
      const picks = body.dataset.ids
        ? filterProducts(body)
        : products.filter(function (p) { return String(p.badge || "").trim(); });
      if (!picks.length) {
        const section = body.closest("[data-picks-section]");
        if (section) section.hidden = true;
        return;
      }
      body.replaceChildren.apply(body, picks.map(createPickRow));
    });
  }

  /* ---------- Quiz "Trova il tuo robot" ---------- */
  const SIZE_CATEGORY = { 500: "Giardini piccoli", 1500: "Giardini medi", 3000: "Giardini grandi", 5000: "Giardini grandi" };
  const BUDGET_TIERS = ["base", "medio", "alto"];

  function recommend(answers) {
    const need = answers.area;
    const needSlope = answers.slope;

    const scored = products.filter(isRobot).map(function (p) {
      const s = getSpecs(p);
      const area = toPositiveNumber(s.area);
      const slope = toPositiveNumber(s.slope);
      const wireless = isWireless(p);
      const reasons = [];
      let score = 0;

      // Superficie: il dato tecnico vince sulla categoria
      if (area) {
        if (area >= need) {
          score += area > need * 3 ? 3 : 4;
          reasons.push("Copre fino a " + area.toLocaleString("it-IT") + " m²: adatto al tuo prato");
        } else {
          score -= 6;
        }
      } else if (p.category === SIZE_CATEGORY[need]) {
        score += 3;
        reasons.push("Pensato per " + p.category.toLowerCase());
      } else if (wireless) {
        score += 0.5;
      } else {
        score -= 1;
      }

      // Pendenza
      if (slope) {
        if (slope >= needSlope) {
          score += 2;
          if (needSlope > 10) reasons.push("Supporta pendenze fino al " + slope + "%");
        } else {
          score -= 4;
        }
      } else if (needSlope >= 45 && (hasTag(p, "pendenza") || /pendenz|4wd|trazione/i.test(p.title + " " + p.description))) {
        score += 2;
        reasons.push("Pensato per terreni in pendenza");
      }

      // Filo perimetrale
      if (answers.wire === "no-wire") {
        if (wireless) {
          score += 4;
          reasons.push("Nessun filo perimetrale da posare");
        } else {
          score -= 5;
        }
      }

      // Fascia di spesa
      const tier = BUDGET_TIERS.indexOf(p.budget);
      if (answers.budget !== "any" && tier >= 0) {
        const distance = Math.abs(BUDGET_TIERS.indexOf(answers.budget) - tier);
        if (distance === 0) {
          score += 2;
          reasons.push("Nella fascia di spesa che hai scelto");
        } else if (distance === 2) {
          score -= 2;
        }
      }

      // A parità di punteggio, meglio un prodotto acquistabile e in evidenza
      if (checkAffiliateUrl(p.affiliateUrl).ok) score += 0.5;
      if (String(p.badge || "").trim()) score += 0.3;

      cleanList(p.benefits, 3).forEach(function (b) {
        if (reasons.length < 3) reasons.push(b);
      });
      return { product: p, score: score, reasons: reasons.slice(0, 3) };
    });

    scored.sort(function (a, b) { return b.score - a.score; });
    return scored.filter(function (r) { return r.score > 0; }).slice(0, 2);
  }

  function createQuizResult(result) {
    const p = result.product;
    const item = document.createElement("article");
    item.className = "quiz-result";
    const category = getCategory(p.category);
    if (category) item.style.setProperty("--tint", category.tint);

    const body = document.createElement("div");
    body.className = "quiz-result-body";

    const cat = document.createElement("p");
    cat.className = "card-cat";
    cat.textContent = p.category;

    const title = document.createElement("h4");
    title.className = "quiz-result-title";
    title.textContent = p.title;

    const reasons = document.createElement("ul");
    reasons.className = "card-benefits";
    reasons.setAttribute("aria-label", "Perché te lo consigliamo");
    result.reasons.forEach(function (text) {
      const li = document.createElement("li");
      li.textContent = text;
      reasons.appendChild(li);
    });

    const actions = document.createElement("div");
    actions.className = "quiz-result-actions";
    actions.append.apply(actions, createAffiliateAction(p, "quiz", null));
    const view = document.createElement("button");
    view.type = "button";
    view.className = "btn btn-ghost btn-small";
    view.textContent = "Vedi la scheda";
    view.setAttribute("aria-label", "Vedi la scheda di " + p.title);
    view.addEventListener("click", function () { focusCard(p.id); });
    actions.appendChild(view);

    const badge = createBadge(p);
    if (badge) body.appendChild(badge);
    body.append(cat, title, reasons, actions);
    item.append(createThumb(p, "quiz-result-media"), body);
    return item;
  }

  function setupQuiz() {
    const box = document.getElementById("quiz-box");
    if (!box) return;
    let step = 0;
    let answers = {};

    function createProgress(fraction) {
      const wrap = document.createElement("div");
      wrap.className = "quiz-progress";
      wrap.setAttribute("role", "progressbar");
      wrap.setAttribute("aria-label", "Avanzamento del quiz");
      wrap.setAttribute("aria-valuemin", "0");
      wrap.setAttribute("aria-valuemax", "100");
      wrap.setAttribute("aria-valuenow", String(Math.round(fraction * 100)));
      const bar = document.createElement("span");
      bar.style.width = Math.round(fraction * 100) + "%";
      wrap.appendChild(bar);
      return wrap;
    }

    function answerLabel(question) {
      const opt = question.options.find(function (o) { return o.value === answers[question.key]; });
      return opt ? opt.label : "";
    }

    function renderStep(moveFocus) {
      const q = QUIZ[step];

      const label = document.createElement("p");
      label.className = "quiz-step";
      label.textContent = "Domanda " + (step + 1) + " di " + QUIZ.length;

      const heading = document.createElement("h3");
      heading.className = "quiz-question";
      heading.id = "quiz-question";
      heading.tabIndex = -1;
      heading.textContent = q.question;

      const hint = document.createElement("p");
      hint.className = "quiz-hint";
      hint.textContent = q.hint || "";

      const options = document.createElement("div");
      options.className = "quiz-options";
      options.setAttribute("role", "group");
      options.setAttribute("aria-labelledby", "quiz-question");
      q.options.forEach(function (opt) {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "quiz-option";
        button.textContent = opt.label;
        button.setAttribute("aria-pressed", String(answers[q.key] === opt.value));
        button.addEventListener("click", function () {
          answers[q.key] = opt.value;
          step++;
          if (step < QUIZ.length) renderStep(true);
          else renderResults();
        });
        options.appendChild(button);
      });

      const nav = document.createElement("div");
      nav.className = "quiz-nav";
      if (step > 0) {
        const back = document.createElement("button");
        back.type = "button";
        back.className = "link-button";
        back.textContent = "← Domanda precedente";
        back.addEventListener("click", function () {
          step--;
          renderStep(true);
        });
        nav.appendChild(back);
      }

      box.replaceChildren(createProgress(step / QUIZ.length), label, heading, hint, options, nav);
      if (moveFocus) heading.focus({ preventScroll: true });
    }

    function renderResults() {
      const results = recommend(answers);

      const label = document.createElement("p");
      label.className = "quiz-step";
      label.textContent = "Il tuo risultato";

      const heading = document.createElement("h3");
      heading.className = "quiz-question";
      heading.tabIndex = -1;
      heading.textContent = results.length ? "I robot più adatti al tuo giardino" : "Nessun robot perfetto, per ora";

      const summary = document.createElement("p");
      summary.className = "quiz-summary";
      summary.textContent = "Le tue risposte: " + QUIZ.map(answerLabel).filter(Boolean).join(" · ");

      const list = document.createElement("div");
      list.className = "quiz-results";
      if (results.length) {
        results.forEach(function (r) { list.appendChild(createQuizResult(r)); });
      } else {
        const empty = document.createElement("p");
        empty.className = "quiz-empty";
        empty.textContent = "Nella selezione non c'è ancora un robot che soddisfi tutte le tue risposte. Prova a cambiare qualche risposta o guarda tutti i robot del catalogo.";
        list.appendChild(empty);
      }

      const note = document.createElement("p");
      note.className = "quiz-hint";
      note.style.margin = "16px 0 0";
      note.textContent = "Prima di acquistare, verifica nella scheda Amazon la superficie massima e la pendenza supportata.";

      const actions = document.createElement("div");
      actions.className = "quiz-actions";
      const restart = document.createElement("button");
      restart.type = "button";
      restart.className = "btn btn-ghost btn-small";
      restart.textContent = "Rifai il quiz";
      restart.addEventListener("click", function () {
        step = 0;
        answers = {};
        renderStep(true);
      });
      const all = document.createElement("a");
      all.className = "btn btn-small";
      all.href = "guide.html";
      all.textContent = "Leggi le guide";
      actions.append(restart, all);

      box.replaceChildren(createProgress(1), label, heading, summary, list, note, actions);
      heading.focus({ preventScroll: true });

      track("Quiz completato", {
        superficie: answerLabel(QUIZ[0]),
        pendenza: answerLabel(QUIZ[1]),
        filo: answerLabel(QUIZ[2]),
        budget: answerLabel(QUIZ[3])
      });
    }

    renderStep(false);
  }

  /* ---------- Carosello della home ---------- */
  const CAROUSEL_INTERVAL = 3300; // millisecondi tra un prodotto e l'altro

  function createSlide(product, position, total) {
    const slide = document.createElement("div");
    slide.className = "slide";
    slide.setAttribute("role", "group");
    slide.setAttribute("aria-roledescription", "prodotto");
    slide.setAttribute("aria-label", position + " di " + total + ": " + product.title);

    const media = document.createElement("div");
    media.className = "slide-media";
    const img = document.createElement("img");
    img.alt = product.title;
    img.decoding = "async";
    img.referrerPolicy = "no-referrer";
    img.addEventListener("error", function () {
      img.replaceWith(createPlaceholder(product));
    }, { once: true });
    img.src = getProductImages(product)[0];
    media.appendChild(img);
    const badge = createBadge(product);
    if (badge) media.appendChild(badge);

    const body = document.createElement("div");
    body.className = "slide-body";
    const cat = document.createElement("p");
    cat.className = "slide-cat";
    cat.textContent = product.category;
    const title = document.createElement("p");
    title.className = "slide-title";
    title.textContent = product.title;
    body.append(cat, title);
    body.append.apply(body, createAffiliateAction(product, "carosello", null));
    slide.append(media, body);
    return slide;
  }

  function setupHeroCarousel() {
    const root = document.getElementById("hero-carousel");
    if (!root) return;
    const track = document.getElementById("carousel-track");
    const dotsList = document.getElementById("carousel-dots");
    const controls = document.getElementById("carousel-controls");
    const pauseBtn = document.getElementById("carousel-pause");

    const items = products.filter(function (p) {
      return checkAffiliateUrl(p.affiliateUrl).ok && getProductImages(p).length > 0;
    });

    if (!items.length) {
      root.hidden = true;
      root.parentElement.classList.add("no-carousel");
      return;
    }

    const slides = items.map(function (p, i) { return createSlide(p, i + 1, items.length); });
    track.replaceChildren.apply(track, slides);

    const dots = items.map(function (p, i) {
      const li = document.createElement("li");
      const dot = document.createElement("button");
      dot.type = "button";
      dot.className = "carousel-dot";
      dot.setAttribute("aria-label", "Mostra " + p.title);
      dot.addEventListener("click", function () { goTo(i); restart(); });
      li.appendChild(dot);
      dotsList.appendChild(li);
      return dot;
    });

    let index = 0;
    let timer = null;
    let pausedByUser = prefersReducedMotion();
    let pausedByHover = false;

    function goTo(i) {
      index = (i + items.length) % items.length;
      track.style.transform = "translate3d(" + (-index * 100) + "%, 0, 0)";
      slides.forEach(function (slide, k) {
        const active = k === index;
        slide.setAttribute("aria-hidden", String(!active));
        slide.querySelectorAll("a, button").forEach(function (a) { a.tabIndex = active ? 0 : -1; });
      });
      dots.forEach(function (dot, k) { dot.setAttribute("aria-current", String(k === index)); });
    }

    function stop() {
      clearInterval(timer);
      timer = null;
      track.setAttribute("aria-live", "polite");
    }

    function start() {
      stop();
      if (items.length < 2 || pausedByUser || pausedByHover || document.hidden) return;
      track.setAttribute("aria-live", "off");
      timer = setInterval(function () { goTo(index + 1); }, CAROUSEL_INTERVAL);
    }

    function restart() { if (timer) start(); }

    function updatePauseButton() {
      pauseBtn.setAttribute("aria-label", pausedByUser ? "Riprendi lo scorrimento" : "Metti in pausa lo scorrimento");
      pauseBtn.querySelector('[data-icon="pause"]').toggleAttribute("hidden", pausedByUser);
      pauseBtn.querySelector('[data-icon="play"]').toggleAttribute("hidden", !pausedByUser);
    }

    document.getElementById("carousel-prev").addEventListener("click", function () { goTo(index - 1); restart(); });
    document.getElementById("carousel-next").addEventListener("click", function () { goTo(index + 1); restart(); });
    pauseBtn.addEventListener("click", function () {
      pausedByUser = !pausedByUser;
      updatePauseButton();
      start();
    });

    root.addEventListener("mouseenter", function () { pausedByHover = true; start(); });
    root.addEventListener("mouseleave", function () { pausedByHover = false; start(); });
    root.addEventListener("focusin", function () { pausedByHover = true; start(); });
    root.addEventListener("focusout", function (e) {
      if (!root.contains(e.relatedTarget)) { pausedByHover = false; start(); }
    });
    document.addEventListener("visibilitychange", start);

    let startX = null;
    let startY = null;
    track.addEventListener("touchstart", function (e) {
      startX = e.touches[0].clientX;
      startY = e.touches[0].clientY;
    }, { passive: true });
    track.addEventListener("touchend", function (e) {
      if (startX === null) return;
      const dx = e.changedTouches[0].clientX - startX;
      const dy = e.changedTouches[0].clientY - startY;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) {
        goTo(index + (dx < 0 ? 1 : -1));
        start();
      }
      startX = null;
    }, { passive: true });

    if (items.length < 2) controls.hidden = true;
    updatePauseButton();
    goTo(0);
    start();
  }

  /* ---------- Barra stagionale (es. Black Friday) ---------- */
  function setupSeasonalBar() {
    const s = SITE_CONFIG.seasonal;
    const p = document.querySelector("#topbar p");
    if (!p || !s || !s.start || !s.end || !s.text) return;
    const now = new Date();
    const from = new Date(s.start + "T00:00:00");
    const to = new Date(s.end + "T23:59:59");
    if (isNaN(from) || isNaN(to) || now < from || now > to) return;

    const strong = document.createElement("strong");
    strong.textContent = s.text;
    const parts = [strong];
    if (s.linkText) {
      const link = document.createElement("a");
      link.href = s.href || "index.html";
      link.textContent = s.linkText;
      parts.push(document.createTextNode(" · "), link);
    }
    p.replaceChildren.apply(p, parts);
  }

  /* ---------- Testi configurabili ---------- */
  function fillSiteTexts() {
    document.querySelectorAll("[data-catalog-date]").forEach(function (el) {
      el.textContent = SITE_CONFIG.catalogUpdated;
    });
    document.querySelectorAll("[data-policy-date]").forEach(function (el) {
      el.textContent = SITE_CONFIG.policyUpdated;
    });

    const name = String(SITE_CONFIG.authorName || "").trim();
    document.querySelectorAll("[data-author-box]").forEach(function (box) {
      if (!name) return;
      box.querySelector("[data-author-avatar]").textContent = name.charAt(0).toUpperCase();
      box.querySelector("[data-author-name]").textContent = name;
      box.querySelector("[data-author-bio]").textContent = String(SITE_CONFIG.authorBio || "").trim();
      box.hidden = false;
    });

    // Dati del titolare nelle pagine privacy e cookie
    document.querySelectorAll("[data-owner]").forEach(function (el) {
      const field = el.dataset.owner;
      const value = String(field === "email" ? SITE_CONFIG.ownerEmail : SITE_CONFIG.ownerName).trim();
      el.replaceChildren();
      if (!value) {
        const missing = document.createElement("span");
        missing.className = "owner-missing";
        missing.textContent = field === "email"
          ? "[email da completare in SITE_CONFIG.ownerEmail]"
          : "[nome da completare in SITE_CONFIG.ownerName]";
        el.appendChild(missing);
      } else if (field === "email" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
        const link = document.createElement("a");
        link.href = "mailto:" + value;
        link.textContent = value;
        el.appendChild(link);
      } else {
        el.textContent = value;
      }
    });

    const year = document.getElementById("year");
    if (year) year.textContent = String(new Date().getFullYear());
  }

  /* ---------- Banner cookie ---------- */
  const COOKIE_NOTICE_KEY = "pratosmart-cookie-notice";

  function setupCookieBanner(onChange) {
    const banner = document.getElementById("cookie-banner");
    if (!banner) return;
    let seen = null;
    try { seen = localStorage.getItem(COOKIE_NOTICE_KEY); } catch (e) { /* memoria non disponibile */ }
    if (seen === SITE_CONFIG.cookieNoticeVersion) return;

    banner.hidden = false;
    function dismiss() {
      try { localStorage.setItem(COOKIE_NOTICE_KEY, SITE_CONFIG.cookieNoticeVersion); } catch (e) { /* ignora */ }
      banner.hidden = true;
      onChange();
    }
    document.getElementById("cookie-ok").addEventListener("click", dismiss);
    document.getElementById("cookie-close").addEventListener("click", dismiss);
  }

  /* ---------- Barra fissa "Trova il tuo robot" su smartphone ---------- */
  function setupStickyCta() {
    const bar = document.getElementById("sticky-cta");
    if (!bar) return function () {};
    const banner = document.getElementById("cookie-banner");
    const footer = document.querySelector(".site-footer");
    let ticking = false;
    function update() {
      ticking = false;
      const bannerOpen = banner && !banner.hidden;
      const nearFooter = footer && footer.getBoundingClientRect().top < window.innerHeight;
      bar.classList.toggle("is-visible", window.scrollY > 700 && !bannerOpen && !nearFooter);
    }
    window.addEventListener("scroll", function () {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(update);
      }
    }, { passive: true });
    update();
    return update;
  }

  /* ---------- Menu "Guide" a tendina: si chiude con un clic fuori o con Esc ---------- */
  function setupNavMenu() {
    const menu = document.querySelector("[data-nav-menu]");
    if (!menu) return;
    document.addEventListener("click", function (event) {
      if (menu.open && !menu.contains(event.target)) menu.open = false;
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && menu.open) {
        menu.open = false;
        menu.querySelector("summary").focus();
      }
    });
    // Un clic su un link interno alla stessa pagina (es. #quiz) chiude il menu
    menu.addEventListener("click", function (event) {
      if (event.target.closest("a")) menu.open = false;
    });
  }

  /* ---------- Clic verso Amazon (per le statistiche facoltative) ---------- */
  function setupClickTracking() {
    document.addEventListener("click", function (event) {
      const link = event.target.closest("a[data-placement]");
      if (link) track("Clic Amazon", { prodotto: link.dataset.product, posizione: link.dataset.placement, pagina: location.pathname });
    });
  }

  /* ---------- Controlli di coerenza (visibili nella console del browser) ---------- */
  function validateCatalog() {
    const seen = new Set();
    products.forEach(function (p, i) {
      const where = "Prodotto " + (i + 1) + " (\"" + (p.id || "senza id") + "\")";
      if (!p.id) console.warn(where + ": manca il campo id.");
      if (seen.has(p.id)) console.warn(where + ": id duplicato, deve essere unico.");
      seen.add(p.id);
      if (!p.title) console.warn(where + ": manca il titolo.");
      if (!getCategory(p.category)) console.warn(where + ": la categoria \"" + p.category + "\" non esiste in CATEGORIES.");
      const check = checkAffiliateUrl(p.affiliateUrl);
      if (!check.ok) console.warn(where + ": " + affiliateErrorMessage(p, check.reason));
      (Array.isArray(p.images) ? p.images : []).forEach(function (url, k) {
        if (String(url || "").trim() && !getSafeImageUrl(url)) {
          console.warn(where + ": la foto " + (k + 1) + " non è un indirizzo valido (usa https:// o un percorso locale).");
        }
      });
      if (isRobot(p)) {
        if (!toPositiveNumber(getSpecs(p).area)) console.warn(where + ": manca specs.area (superficie in m²). Il quiz userà la categoria.");
        if (p.budget && BUDGET_TIERS.indexOf(p.budget) < 0) console.warn(where + ": budget deve essere \"base\", \"medio\" o \"alto\".");
      }
    });
  }

  /* ---------- Avvio ---------- */
  validateCatalog();
  renderProductGrids();
  renderPicks();
  setupQuiz();
  setupGuideButtons();
  setupHeroCarousel();
  setupSeasonalBar();
  fillSiteTexts();
  const updateSticky = setupStickyCta();
  setupCookieBanner(updateSticky);
  setupNavMenu();
  setupClickTracking();

  // Link diretti a una scheda (es. /#card-robot-wifi-medi): la apre e la evidenzia
  if (location.hash.indexOf("#card-") === 0) {
    const id = decodeURIComponent(location.hash.slice(6));
    setTimeout(function () { focusCard(id); }, 250);
  }
})();
