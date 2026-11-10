(() => {
  const state = {
    data: null,
    catalog: null,
    datasetId: null,
    filtered: [],
    index: 0,
    answerVisible: false,
  };

  const $ = (id) => document.getElementById(id);

  function pv(obj) {
    if (obj && typeof obj === "object" && "value" in obj) {
      return { value: obj.value, status: obj.status || "original", rationale: obj.rationale, tools: obj.tools };
    }
    return { value: obj ?? "", status: "original" };
  }

  function badge(status, label) {
    const span = document.createElement("span");
    span.className = `badge ${status || ""}`;
    span.textContent = label || status;
    return span;
  }

  function unique(values) {
    return [...new Set(values.filter(Boolean))].sort((a, b) => String(a).localeCompare(String(b), "ja"));
  }

  function fillSelect(select, values, allLabel) {
    const cur = select.value;
    select.innerHTML = "";
    const optAll = document.createElement("option");
    optAll.value = "all";
    optAll.textContent = allLabel;
    select.appendChild(optAll);
    for (const v of values) {
      const opt = document.createElement("option");
      opt.value = v;
      opt.textContent = v;
      select.appendChild(opt);
    }
    if ([...select.options].some((o) => o.value === cur)) select.value = cur;
  }

  function questionStatuses(q) {
    const statuses = [pv(q.stem).status, pv(q.answer).status];
    if (q.explanation) statuses.push(pv(q.explanation).status);
    return statuses;
  }

  function applyFilters() {
    const subject = $("subjectFilter").value;
    const unit = $("unitFilter").value;
    const form = $("formFilter").value;
    const onlyUncertain = $("onlyUncertain").checked;
    const examSubject = state.data?.subject;

    let list = state.data?.questions || [];
    if (subject !== "all" && examSubject && subject !== examSubject) {
      list = [];
    }
    if (unit !== "all") list = list.filter((q) => q.unit === unit);
    if (form !== "all") {
      list = list.filter((q) => {
        if (form === "other") {
          return !["flashcard", "multiple_choice", "cloze", "short_answer", "calculation"].includes(q.form);
        }
        if (form === "flashcard") return q.form === "flashcard" || q.form === "short_answer";
        return q.form === form;
      });
    }
    if (onlyUncertain) {
      list = list.filter((q) => questionStatuses(q).some((s) => s === "inferred" || s === "unverified"));
    }

    state.filtered = list;
    state.index = 0;
    state.answerVisible = $("modeSelect").value === "study" ? false : false;
    renderStats();
    renderCard();
  }

  function renderStats() {
    const total = state.data?.questions?.length || 0;
    const n = state.filtered.length;
    const uncertain = state.filtered.filter((q) =>
      questionStatuses(q).some((s) => s === "inferred" || s === "unverified")
    ).length;
    const conflicts = state.filtered.filter((q) => (q.conflicts || []).length).length;
    $("stats").innerHTML = `
      <span>表示 ${n} / 全 ${total}</span>
      <span>推定・未確認 ${uncertain}</span>
      <span>conflicts ${conflicts}</span>
      <span>${state.index + (n ? 1 : 0)} 問目</span>
    `;
  }

  function typeset(el) {
    if (window.MathJax?.typesetPromise) {
      window.MathJax.typesetPromise([el]).catch(() => {});
    }
  }

  function renderCard() {
    const empty = $("empty");
    const card = $("card");
    if (!state.filtered.length) {
      card.hidden = true;
      empty.hidden = false;
      empty.textContent = state.data ? "条件に合う問題がありません。" : "データを読み込めませんでした。";
      return;
    }
    empty.hidden = true;
    card.hidden = false;

    const q = state.filtered[state.index];
    const stem = pv(q.stem);
    const answer = pv(q.answer);
    const expl = pv(q.explanation);

    const badges = $("badges");
    badges.innerHTML = "";
    badges.appendChild(badge("form", q.form || "other"));
    for (const st of unique(questionStatuses(q))) {
      const label = st === "inferred" ? "推定" : st === "unverified" ? "未確認" : "原文";
      badges.appendChild(badge(st, label));
    }
    if ((q.conflicts || []).length) badges.appendChild(badge("inferred", "conflict"));

    $("qid").textContent = q.id || "";
    $("unitLine").textContent = `${q.unit || ""} · tags: ${(q.tags || []).join(", ") || "—"}`;
    $("stem").textContent = String(stem.value ?? "");

    const choicesEl = $("choices");
    choicesEl.innerHTML = "";
    for (const c of q.choices || []) {
      const text = pv(c.text);
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "choice";
      btn.textContent = `(${c.key}) ${text.value}`;
      btn.addEventListener("click", () => {
        const correct = String(answer.value) === String(c.key) || String(answer.value) === String(text.value);
        btn.classList.add(correct ? "correct" : "wrong");
        showAnswer(true);
      });
      choicesEl.appendChild(btn);
    }

    $("answerBlock").hidden = !state.answerVisible;
    if (state.answerVisible) fillAnswer(q, answer, expl);

    typeset(card);
    renderStats();
  }

  function fillAnswer(q, answer, expl) {
    $("answer").textContent = String(answer.value ?? "");
    $("answerBadge").innerHTML = "";
    $("answerBadge").appendChild(
      badge(answer.status, answer.status === "inferred" ? "推定" : answer.status === "unverified" ? "未確認" : "原文")
    );
    $("explanation").textContent = String(expl.value ?? "（解説なし）");
    $("explBadge").innerHTML = "";
    if (q.explanation) {
      $("explBadge").appendChild(
        badge(expl.status, expl.status === "inferred" ? "推定" : expl.status === "unverified" ? "未確認" : "原文")
      );
    }

    const conf = $("conflicts");
    if ((q.conflicts || []).length) {
      conf.innerHTML = "<strong>conflicts</strong>";
      const ul = document.createElement("ul");
      for (const c of q.conflicts) {
        const li = document.createElement("li");
        li.textContent = `${c.field}: ${c.reason} / ` + (c.values || []).map((v) => `${v.source}=${v.value}`).join(" · ");
        ul.appendChild(li);
      }
      conf.appendChild(ul);
    } else {
      conf.innerHTML = "";
    }

    const src = $("sources");
    src.textContent = "出典: " + (q.sources || []).map((s) => `${s.file}${s.page ? " p." + s.page : ""}`).join("; ");
  }

  function showAnswer(visible) {
    state.answerVisible = visible;
    if (!state.filtered.length) return;
    const q = state.filtered[state.index];
    $("answerBlock").hidden = !visible;
    if (visible) fillAnswer(q, pv(q.answer), pv(q.explanation));
    typeset($("card"));
  }

  function move(delta) {
    if (!state.filtered.length) return;
    state.index = (state.index + delta + state.filtered.length) % state.filtered.length;
    state.answerVisible = false;
    renderCard();
  }

  function fillDatasetSelect() {
    const select = $("datasetFilter");
    if (!select || !state.catalog) return;
    const cur = state.datasetId || state.catalog.default;
    select.innerHTML = "";
    for (const ds of state.catalog.datasets || []) {
      const opt = document.createElement("option");
      opt.value = ds.id;
      opt.textContent = `${ds.exam || ""} ${ds.subject || ds.id}`.trim();
      select.appendChild(opt);
    }
    if ([...select.options].some((o) => o.value === cur)) select.value = cur;
  }

  async function loadDataset(datasetId) {
    const ds = (state.catalog?.datasets || []).find((d) => d.id === datasetId)
      || (state.catalog?.datasets || [])[0];
    const file = ds?.file || "questions.json";
    const res = await fetch(`data/${file}`, { cache: "no-store" });
    if (!res.ok) throw new Error(`${file}: ${res.status}`);
    state.data = await res.json();
    state.datasetId = ds?.id || datasetId;
    $("metaLine").textContent = `${state.data.exam || ""} / ${state.data.subject || ""} · ${state.data.questions?.length || 0}問`;
    fillSelect($("subjectFilter"), state.data.subject ? [state.data.subject] : [], "すべて");
    fillSelect($("unitFilter"), unique((state.data.questions || []).map((q) => q.unit)), "すべて");
    applyFilters();
  }

  async function load() {
    try {
      try {
        const catRes = await fetch("data/catalog.json", { cache: "no-store" });
        if (catRes.ok) state.catalog = await catRes.json();
      } catch (_) {
        state.catalog = null;
      }
      if (state.catalog?.datasets?.length) {
        fillDatasetSelect();
        await loadDataset(state.catalog.default || state.catalog.datasets[0].id);
      } else {
        const res = await fetch("data/questions.json", { cache: "no-store" });
        if (!res.ok) throw new Error(String(res.status));
        state.data = await res.json();
        $("metaLine").textContent = `${state.data.exam || ""} / ${state.data.subject || ""} · ${state.data.questions?.length || 0}問`;
        fillSelect($("subjectFilter"), state.data.subject ? [state.data.subject] : [], "すべて");
        fillSelect($("unitFilter"), unique((state.data.questions || []).map((q) => q.unit)), "すべて");
        applyFilters();
      }
    } catch (err) {
      $("empty").textContent = `データを読めません（ローカルは簡易サーバ推奨）: ${err}`;
    }
  }

  if ($("datasetFilter")) {
    $("datasetFilter").addEventListener("change", () => {
      loadDataset($("datasetFilter").value).catch((err) => {
        $("empty").textContent = `データセット切替失敗: ${err}`;
      });
    });
  }
  $("subjectFilter").addEventListener("change", applyFilters);
  $("unitFilter").addEventListener("change", applyFilters);
  $("formFilter").addEventListener("change", applyFilters);
  $("modeSelect").addEventListener("change", () => {
    state.answerVisible = false;
    renderCard();
  });
  $("onlyUncertain").addEventListener("change", applyFilters);
  $("showAnswer").addEventListener("click", () => showAnswer(true));
  $("prevBtn").addEventListener("click", () => move(-1));
  $("nextBtn").addEventListener("click", () => move(1));
  $("themeToggle").addEventListener("click", () => {
    const root = document.documentElement;
    const next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
    if (next === "light") root.setAttribute("data-theme", "light");
    else root.removeAttribute("data-theme");
    $("themeToggle").textContent = next === "light" ? "☀" : "☾";
  });

  load();
})();
