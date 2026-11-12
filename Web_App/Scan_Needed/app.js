(function () {
  const DATA_URL = "../data/scan_needed_2026_03.json";

  const priorityLabel = {
    critical: "最重要",
    high: "高",
    medium: "中",
    done: "受領済",
  };

  const statusLabel = {
    needed: "未受領",
    received: "受領済",
  };

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    const icon = document.querySelector(".theme-icon");
    if (icon) icon.textContent = theme === "light" ? "🌙" : "☀️";
  }

  function setupTheme() {
    const saved = localStorage.getItem("theme") || "light";
    applyTheme(saved);
    const btn = document.getElementById("themeToggle");
    if (!btn) return;
    btn.addEventListener("click", () => {
      const cur = document.documentElement.getAttribute("data-theme") || "light";
      const next = cur === "light" ? "dark" : "light";
      localStorage.setItem("theme", next);
      applyTheme(next);
    });
  }

  function badge(priority, status) {
    const pri = priority || "medium";
    const st = status || "needed";
    const priText = priorityLabel[pri] || pri;
    const stText = statusLabel[st] || st;
    const priClass = pri === "done" ? "done" : pri;
    const stClass = st === "received" ? "received" : priClass;
    return (
      `<span class="badge ${priClass}">優先: ${escapeHtml(priText)}</span>` +
      `<span class="badge ${stClass}">${escapeHtml(stText)}</span>`
    );
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function renderItem(item) {
    const el = document.createElement("article");
    el.className = "item";
    el.dataset.subject = item.subject || "";
    el.dataset.priority = item.priority || "";
    el.dataset.status = item.status || "";
    el.innerHTML = `
      <div class="item-head">
        <span class="subject">${escapeHtml(item.subject || "")}</span>
        ${badge(item.priority, item.status)}
      </div>
      <div class="what">${escapeHtml(item.what || "")}</div>
      <div class="reason">理由: ${escapeHtml(item.reason || "")}</div>
    `;
    return el;
  }

  function renderAgreed(section, root) {
    const wrap = document.createElement("section");
    wrap.className = "section";
    wrap.id = section.id;
    wrap.innerHTML = `
      <h2>${escapeHtml(section.title)}</h2>
      <p class="desc">${escapeHtml(section.description || "")}</p>
    `;

    (section.groups || []).forEach((group) => {
      const g = document.createElement("div");
      g.className = "group";
      g.dataset.groupId = group.id || "";
      const note = group.excluded_note
        ? `<p class="note">${escapeHtml(group.excluded_note)}</p>`
        : "";
      g.innerHTML = `<h3>${escapeHtml(group.heading)}</h3>${note}`;
      (group.items || []).forEach((item) => g.appendChild(renderItem(item)));
      wrap.appendChild(g);
    });

    root.appendChild(wrap);
  }

  function renderBySubject(section, root) {
    const wrap = document.createElement("section");
    wrap.className = "section";
    wrap.id = section.id;
    wrap.innerHTML = `
      <h2>${escapeHtml(section.title)}</h2>
      <p class="desc">${escapeHtml(section.description || "")}</p>
    `;

    (section.subjects || []).forEach((sub) => {
      const block = document.createElement("div");
      block.className = "subject-block";
      block.dataset.subject = sub.subject || "";
      block.innerHTML = `
        <h3>${escapeHtml(sub.subject || "")}</h3>
        <p class="intake">取込状況: ${escapeHtml(sub.intake || "")}</p>
      `;
      (sub.items || []).forEach((item) => {
        const merged = Object.assign({}, item, {
          subject: item.subject || sub.subject,
        });
        block.appendChild(renderItem(merged));
      });
      wrap.appendChild(block);
    });

    root.appendChild(wrap);
  }

  function collectSubjects(data) {
    const set = new Set();
    (data.sections || []).forEach((sec) => {
      (sec.groups || []).forEach((g) => {
        (g.items || []).forEach((it) => {
          if (it.subject) set.add(it.subject);
        });
      });
      (sec.subjects || []).forEach((s) => {
        if (s.subject) set.add(s.subject);
      });
    });
    return Array.from(set).sort((a, b) => a.localeCompare(b, "ja"));
  }

  function applyFilters() {
    const subject = document.getElementById("subjectFilter").value;
    const priority = document.getElementById("priorityFilter").value;
    document.querySelectorAll(".item").forEach((el) => {
      const okSub = subject === "all" || el.dataset.subject === subject;
      const okPri = priority === "all" || el.dataset.priority === priority;
      el.hidden = !(okSub && okPri);
    });
    document.querySelectorAll(".group, .subject-block").forEach((block) => {
      const visible = Array.from(block.querySelectorAll(".item")).some(
        (it) => !it.hidden
      );
      block.hidden = !visible;
    });
  }

  function setupFilters(data) {
    const subSel = document.getElementById("subjectFilter");
    collectSubjects(data).forEach((name) => {
      const opt = document.createElement("option");
      opt.value = name;
      opt.textContent = name;
      subSel.appendChild(opt);
    });
    subSel.addEventListener("change", applyFilters);
    document
      .getElementById("priorityFilter")
      .addEventListener("change", applyFilters);
  }

  async function main() {
    setupTheme();
    const root = document.getElementById("content");
    const meta = document.getElementById("metaLine");
    try {
      const res = await fetch(DATA_URL, { cache: "no-store" });
      if (!res.ok) throw new Error("HTTP " + res.status);
      const data = await res.json();
      meta.textContent = `${data.period_name || ""} ${data.window_jst || ""} · 更新 ${data.updated || ""}`;
      document.getElementById("privacy").textContent = data.privacy_note || "";
      document.getElementById("rangePolicy").textContent =
        data.range_policy || "";
      if (data.excluded_subjects_note) {
        document.getElementById("excluded").textContent =
          data.excluded_subjects_note;
      }

      (data.sections || []).forEach((sec) => {
        if (sec.id === "agreed_2026-11-10") renderAgreed(sec, root);
        else if (sec.id === "by_subject") renderBySubject(sec, root);
      });

      setupFilters(data);
      document.getElementById("loading").hidden = true;
    } catch (err) {
      document.getElementById("loading").hidden = true;
      document.getElementById("error").hidden = false;
      document.getElementById("error").textContent =
        "データの読み込みに失敗しました。静的サーバ経由で開いているか確認してください。（" +
        err.message +
        "）";
    }
  }

  document.addEventListener("DOMContentLoaded", main);
})();
