

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..700&display=swap");

:root {
  color-scheme: light dark;
  --paper-bg: #f6f7f4;
  --ink: #1f2a2e;
  --muted: #647071;
  --line: #d9dfda;
  --panel: #ffffff;
  --accent: #276e6a;
  --accent-2: #a63d40;
  --soft: #e6efe8;
  --soft-2: #f4e8df;
  --tint: #f8fbf9;
  --cream: #fbfaf7;
  --shadow: 0 10px 24px rgba(31, 42, 46, 0.08);
  --serif: Newsreader, "Iowan Old Style", Georgia, serif;
}

@media (prefers-color-scheme: dark) {
  :root {
    --paper-bg: #14181a;
    --ink: #e7ecea;
    --muted: #9aa7a5;
    --line: #2c3537;
    --panel: #1c2225;
    --accent: #7cc7c0;
    --accent-2: #e29a9c;
    --soft: #21302e;
    --soft-2: #34272a;
    --tint: #1e2629;
    --cream: #20262a;
    --shadow: 0 10px 24px rgba(0, 0, 0, 0.35);
  }
}

html {
  scroll-behavior: smooth;
}

::selection {
  background: var(--soft);
}

body {
  margin: 0;
  background: var(--paper-bg);
  color: var(--ink);
  font: 16px/1.6 Inter, ui-sans-serif, system-ui, -apple-system,
    BlinkMacSystemFont, "Segoe UI", sans-serif;
}

a {
  color: inherit;
  text-decoration-color: color-mix(in srgb, var(--accent) 45%, transparent);
  text-underline-offset: 0.18em;
}

.daily-arxiv {
  max-width: 1180px;
  margin: 0 auto;
  padding: 40px 20px 72px;
}

.daily-arxiv::before {
  content: "";
  display: block;
  height: 4px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent), var(--accent-2) 60%, transparent);
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.45fr) minmax(260px, 0.55fr);
  gap: 28px;
  align-items: end;
  padding: 42px 0 30px;
  border-bottom: 1px solid var(--line);
}

.eyebrow, .paper-kicker {
  margin: 0 0 10px;
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0;
  text-transform: uppercase;
}

.hero h1 {
  max-width: 820px;
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(2.2rem, 7vw, 5.8rem);
  font-weight: 600;
  line-height: 1;
  letter-spacing: -0.015em;
}

.hero-copy {
  max-width: 760px;
  margin: 18px 0 0;
  color: var(--muted);
  font-size: 1.06rem;
}

.metrics {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 10px;
}

.archive-hero .metrics {
  grid-template-columns: minmax(220px, 1fr);
  min-width: 220px;
}

.metric {
  min-height: 88px;
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
}

.metric span {
  display: block;
  color: var(--muted);
  font-size: 0.8rem;
  font-weight: 700;
}

.metric strong {
  display: block;
  margin-top: 8px;
  font-family: var(--serif);
  font-size: 1.8rem;
  line-height: 1;
  overflow-wrap: anywhere;
}

.section-title {
  margin: 34px 0 14px;
  font-family: var(--serif);
  font-size: 1.6rem;
  font-weight: 600;
}

.category-groups {
  display: grid;
  gap: 24px;
}

.category-section,
.topic-section {
  scroll-margin-top: 18px;
}

.category-heading,
.topic-heading {
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin: 0 0 10px;
  cursor: pointer;
  list-style: none;
  user-select: none;
}

.category-heading::-webkit-details-marker,
.topic-heading::-webkit-details-marker {
  display: none;
}

.category-heading::before,
.topic-heading::before {
  content: "▾";
  color: var(--accent);
  font-size: 0.9rem;
  line-height: 1;
  transform: rotate(0deg);
  transition: transform 140ms ease;
}

details:not([open]) > .category-heading::before,
details:not([open]) > .topic-heading::before {
  transform: rotate(-90deg);
}

.category-heading h3 {
  color: var(--ink);
  font-size: 1rem;
  margin: 0;
}

.category-heading span {
  color: var(--muted);
  font-size: 0.86rem;
  font-weight: 700;
}

.topic-section {
  display: grid;
  gap: 10px;
  margin-top: 14px;
}

.topic-section h4 {
  margin: 0;
  color: var(--accent-2);
  font-size: 0.9rem;
  font-weight: 900;
}

.topic-heading {
  color: var(--accent-2);
  font-size: 0.9rem;
  font-weight: 900;
}

.topic-heading::before {
  color: var(--accent-2);
}

.queue {
  display: grid;
  gap: 10px;
}

.paper-row {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  overflow: hidden;
  transition: border-color 150ms ease, box-shadow 150ms ease;
}

.paper-row:hover {
  border-color: color-mix(in srgb, var(--accent) 55%, var(--line));
  box-shadow: var(--shadow);
}

.paper-row[open] {
  border-color: color-mix(in srgb, var(--accent) 45%, var(--line));
  box-shadow: inset 3px 0 0 var(--accent), var(--shadow);
}

.paper-row-summary {
  display: grid;
  grid-template-columns: 36px minmax(0, 1fr) auto 14px;
  gap: 12px;
  align-items: start;
  min-height: 74px;
  padding: 14px;
  cursor: pointer;
  list-style: none;
  user-select: none;
  transition: background 140ms ease;
}

.paper-row-summary:hover {
  background: var(--tint);
}

.paper-row-summary:focus-visible,
.category-heading:focus-visible,
.topic-heading:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.paper-row-summary::-webkit-details-marker {
  display: none;
}

.paper-row-summary::after {
  content: "▾";
  grid-column: 4;
  grid-row: 1;
  justify-self: end;
  margin-top: 5px;
  color: var(--muted);
  font-size: 0.85rem;
  line-height: 1;
  transform: rotate(0deg);
  transition: transform 140ms ease;
}

.paper-row:not([open]) > .paper-row-summary::after {
  transform: rotate(-90deg);
}

.queue-index {
  display: grid;
  width: 36px;
  height: 36px;
  place-items: center;
  border-radius: 50%;
  background: var(--soft);
  color: var(--accent);
  font-weight: 800;
  transition: background 140ms ease, color 140ms ease;
}

.paper-row[open] .queue-index {
  background: var(--accent);
  color: var(--panel);
}

.paper-row-copy strong {
  display: block;
  line-height: 1.28;
}

.paper-row-copy small {
  display: block;
  margin-top: 7px;
  color: var(--muted);
  line-height: 1.35;
}

.paper-row-detail {
  padding: 0 18px 18px 62px;
  border-top: 1px solid var(--line);
}

.paper-row[open] .paper-row-detail {
  animation: detail-reveal 200ms ease;
}

@keyframes detail-reveal {
  from {
    opacity: 0;
    transform: translateY(-4px);
  }
  to {
    opacity: 1;
    transform: none;
  }
}

.paper-row-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  justify-content: space-between;
  padding-top: 16px;
  color: var(--muted);
  font-size: 0.82rem;
  font-weight: 800;
  text-transform: uppercase;
}

.category-tags,
.topic-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 10px;
}

.category-tag {
  padding: 4px 8px;
  border: 1px solid color-mix(in srgb, var(--accent) 25%, transparent);
  border-radius: 999px;
  background: var(--tint);
  color: var(--accent);
  font-size: 0.76rem;
  font-weight: 800;
  line-height: 1;
}

.topic-tag {
  padding: 4px 8px;
  border-radius: 999px;
  background: var(--soft-2);
  color: var(--accent-2);
  font-size: 0.76rem;
  font-weight: 800;
  line-height: 1;
}

.score-pill {
  min-width: 38px;
  padding: 5px 8px;
  border-radius: 999px;
  background: var(--soft-2);
  color: var(--accent-2);
  font-size: 0.84rem;
  font-weight: 800;
  text-align: center;
}

.score-pill.score-high {
  background: var(--accent);
  color: var(--panel);
}

.score-pill.score-low {
  border: 1px solid var(--line);
  background: transparent;
  color: var(--muted);
}

.paper-action {
  flex: 0 0 auto;
  align-self: start;
  padding: 8px 12px;
  border: 1px solid var(--accent);
  border-radius: 999px;
  color: var(--accent);
  font-size: 0.88rem;
  font-weight: 800;
  text-decoration: none;
  transition: background 140ms ease, color 140ms ease;
}

.paper-action:hover {
  background: var(--accent);
  color: var(--panel);
}

.authors, .comment, .abstract {
  margin: 14px 0 0;
}

.authors {
  color: var(--muted);
}

.paper-scores {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 16px;
}

.paper-scores span {
  padding: 6px 10px;
  border-radius: 999px;
  background: var(--soft);
  color: var(--accent);
  font-weight: 700;
}

.abstract {
  max-width: 78ch;
  line-height: 1.7;
}

.comment {
  padding: 12px 14px;
  border-left: 4px solid var(--accent);
  border-radius: 0 8px 8px 0;
  background: var(--tint);
}

.prompt-block {
  margin-top: 30px;
  padding: 22px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--cream);
}

.prompt-block pre {
  overflow-x: auto;
  white-space: pre-wrap;
}

.cloud-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 16px;
}

.cloud-card {
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 22px 24px 26px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background:
    radial-gradient(120% 100% at 50% 0%, var(--tint), var(--panel) 70%);
  box-shadow: var(--shadow);
}

.cloud-card h3 {
  margin: 0;
  color: var(--muted);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  text-align: center;
}

.word-cloud {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 2px 16px;
  padding: 6px 4px;
  line-height: 1.15;
  text-align: center;
}

.cloud-word {
  font-weight: 800;
  letter-spacing: -0.015em;
  cursor: default;
  transition: transform 160ms ease, opacity 160ms ease;
}

.cloud-word:hover {
  transform: translateY(-2px) scale(1.06);
  opacity: 1 !important;
}

.cloud-empty {
  margin: 0;
  color: var(--muted);
  text-align: center;
}

.archive-block {
  margin-top: 30px;
  padding: 22px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
}

.archive-block h2 {
  margin: 0;
}

.archive-block p,
.archive-nav {
  color: var(--muted);
}

.archive-links {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 10px;
  margin-top: 14px;
}

.archive-link {
  display: block;
  padding: 12px 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--cream);
  text-decoration: none;
  transition: border-color 150ms ease, box-shadow 150ms ease, transform 150ms ease;
}

.archive-link:hover {
  border-color: color-mix(in srgb, var(--accent) 55%, var(--line));
  box-shadow: var(--shadow);
  transform: translateY(-1px);
}

.archive-link span {
  display: block;
  font-weight: 900;
}

.archive-link small {
  display: block;
  margin-top: 4px;
  color: var(--muted);
}

.archive-summary {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
  margin-top: 24px;
}

.archive-content {
  padding: 24px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
}

.archive-block h2,
.prompt-block h2,
.archive-content h1,
.archive-content h2 {
  font-family: var(--serif);
  font-weight: 600;
  line-height: 1.2;
}

.archive-content h2 {
  margin-top: 26px;
}

@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }

  * {
    transition: none !important;
    animation: none !important;
  }
}

@media (max-width: 760px) {
  .daily-arxiv {
    padding: 24px 14px 56px;
  }

  .hero {
    grid-template-columns: 1fr;
    padding-top: 20px;
  }

  .metrics {
    grid-template-columns: 1fr 1fr;
  }

  .archive-summary {
    grid-template-columns: 1fr;
  }

  .queue {
    grid-template-columns: 1fr;
  }

  .paper-action {
    display: inline-block;
  }

  .paper-row-summary {
    grid-template-columns: 32px minmax(0, 1fr) auto 14px;
    gap: 10px;
    padding: 12px;
  }

  .paper-row-detail {
    padding: 0 14px 16px;
  }
}
</style>


<main class="daily-arxiv">
  <section class="hero">
    <div>
      <p class="eyebrow">Daily ArXiv / October 08, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>14</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>13</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>10.6</strong>
    </div>


    <div class="metric">
      <span>Source</span>
      <strong>ArXiv</strong>
    </div>

    </div>
  </section>


  <h2 class="section-title">Abstract word clouds</h2>
  <div class="cloud-grid">
    <article class="cloud-card">
      <h3>Today</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">alignment</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">anatomical</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">controlled</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">counterfactual</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">delta</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">diagnosis</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">evidence</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">fail</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">failure</span><span class="cloud-word" style="font-size:1.91rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="11 mentions">generation</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="9 mentions">geometric</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="9 mentions">grounding</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">instruction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">interpretation</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">intervention</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">label</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="9 mentions">language</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">lesion</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="10 mentions">medical</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">multiple</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">normal</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">object</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">pairing</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">panoramic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">pathological</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="10 mentions">phenotype</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">phenotypic</span><span class="cloud-word" style="font-size:2.15rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 68%, var(--accent))" title="13 mentions">reasoning</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">region</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">relational</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">relationship</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">same</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">scene</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">space</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">student</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">supervision</span><span class="cloud-word" style="font-size:2.26rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 74%, var(--accent))" title="14 mentions">support</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">target</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">teacher</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">textbf</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">textit</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">trajectory</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">understanding</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">video</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="19 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.74rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="131 mentions">action</span><span class="cloud-word" style="font-size:1.87rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="145 mentions">agent</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="51 mentions">alignment</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">annotation</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="52 mentions">camera</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">change</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="60 mentions">consistency</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="68 mentions">control</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="59 mentions">dense</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">detection</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="53 mentions">domain</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="99 mentions">dynamic</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="62 mentions">environment</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="153 mentions">evidence</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="60 mentions">foundation</span><span class="cloud-word" style="font-size:2.29rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="196 mentions">generation</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="62 mentions">geometric</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="74 mentions">geometry</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="56 mentions">grounding</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="69 mentions">inference</span><span class="cloud-word" style="font-size:1.54rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="110 mentions">interaction</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="90 mentions">language</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="56 mentions">latent</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="85 mentions">memory</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="97 mentions">motion</span><span class="cloud-word" style="font-size:1.74rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="130 mentions">multimodal</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="66 mentions">multiple</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="124 mentions">object</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="93 mentions">observation</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="62 mentions">perception</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="60 mentions">physical</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="56 mentions">pipeline</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="82 mentions">point</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="64 mentions">policy</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="53 mentions">produce</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">query</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="65 mentions">question</span><span class="cloud-word" style="font-size:1.93rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="152 mentions">reasoning</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="58 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">reference</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="55 mentions">region</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="61 mentions">same</span><span class="cloud-word" style="font-size:1.77rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="134 mentions">scene</span><span class="cloud-word" style="font-size:1.82rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="139 mentions">semantic</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="55 mentions">source</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="68 mentions">space</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="109 mentions">spatial</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="72 mentions">supervision</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="97 mentions">support</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="70 mentions">target</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="68 mentions">temporal</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="78 mentions">token</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="103 mentions">trajectory</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="78 mentions">understanding</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="61 mentions">unified</span><span class="cloud-word" style="font-size:2.46rem;opacity:0.92;color:color-mix(in srgb, var(--accent-2) 84%, var(--accent))" title="218 mentions">video</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="52 mentions">view</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="53 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="263 mentions">visual</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="111 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>11 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation</strong>
          <small>Yunheng Liu, Ziqi Cai, Siqi Yang, Yimu Wang, Minggui Teng, Jiaming Tan, Shuchen Weng, Erwin Wu, Kaipeng Zhang, Boxin Shi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Panoramic Video Generation</span>
<span class="topic-tag">Language-Guided Navigation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2610.08941</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.08941">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 3 very closely: it proposes a new method for language-guided panoramic navigation and an embodied world model with a new panorama/video dataset.</p>
        <p class="abstract">Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training. Existing panoramic generators follow predefined trajectories, and interactive world models act through low-level actions in perspective views. We propose SPW-Nav, a streaming panoramic world model that understands movement instructions and streams one minute of 2K 360-degree video in real time from a single panorama. SPW-Nav interprets each instruction in the previously generated panorama as camera motion. Spherical rotation decoupling applies rotation exactly on the sphere, pose-aligned conditioning keeps translation inputs bounded over long streams, and a multi-term memory with a few-step generator continues the scene as instructions change. We also build SPW-NavSet, panoramic videos with camera trajectories and verified instructions. Driven by language, SPW-Nav outperforms prior panoramic generators in camera-following accuracy and video quality, and supports on-the-fly instruction switching.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language-Action</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving</strong>
          <small>Xingtai Gui, Yucheng Zhou, Dongqian Guo, Jiahao Gong, Feiyang Tan, Jianbing Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Geometric Reasoning</span>
<span class="topic-tag">Grounding Dataset</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2610.10390</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.10390">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 3 very closely: it is an embodied VLA driving method with explicit geometric chain-of-thought and a new planning-grounding dataset.</p>
        <p class="abstract">Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving. However, existing VLA models still suffer from a fundamental mismatch: driving actions require precise 3D geometric cues, while visual-language understanding and reasoning are largely conducted in a 2D semantic space. In this paper, we propose GeoCoTDrive, an explicit geometric chain-of-thought framework that grounds geometry in a planning-oriented manner. GeoCoTDrive follows a think with 2D first, drive with dedicated 3D priors paradigm. It first grounds 2D regions corresponding to decision-critical cues, and then retrieves localized 3D priors by sampling features from a geometric foundation model within the grounded regions. These localized geometric features are interleaved into the autoregressive context to support the trajectory generation. To supervise this process, we introduce planning-relevant grounding, a new region-level grounding task that focuses on local spatial cues directly affecting ego planning decisions, and construct the PlanningGrounding dataset to endow VLAs with planning-oriented grounding capability. Experiments across multiple end-to-end autonomous driving benchmarks show that GeoCoTDrive consistently improves safety-critical planning performance, demonstrating the effectiveness of the explicit geometric chain-of-thought process for VLA-based planning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical VLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>$\Delta$Representation: Geometry Supervised Representation Learning of Phenotypes via Counterfactual Reasoning for Medical VLMs</strong>
          <small>Hao Wang, Qiwei Zeng, Jinghao Lin, Shuchang Ye, Yuezhe Yang, Yige Peng, Haoyuan Che, Jinman Kim, Lei Bi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical VLMs</span>
<span class="topic-tag">Counterfactual Reasoning</span>
<span class="topic-tag">Grounding</span>
<span class="topic-tag">Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2610.10286</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.10286">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 1 well: a medical VLM method that uses counterfactual reasoning plus geometry-supervised representations for lesion grounding and phenotype structure.</p>
        <p class="abstract">Medical vision-language models (VLMs) have shown increasing potential for radiological image interpretation. Medical VLMs encode radiological images into visual representations that capture both anatomical and phenotypic information for diagnosis. Existing approaches improve pathological phenotype representations through semantic-guided representation alignment. However, pathological phenotypes arise as lesion-specific visual changes superimposed on underlying normal anatomy. Such semantic alignment approaches fail to model the phenotype-specific increment relative to the corresponding normal anatomical representation. To address this gap, we propose \textbf{$\Delta$Representation}, a visual phenotype representation learning framework based on counterfactual reasoning for medical VLMs. It comprises \textbf{BaseAnatomy}, a geometry-supervised representation learning module, and \textbf{$\Delta$Phenotype}, a counterfactual incremental representation learning module. BaseAnatomy provides fine-grained geometric supervision through spatial relationships across and within anatomical structures. $\Delta$Phenotype computes the representation increment between lesion representations and their corresponding normal anatomical representations, and supervises increments associated with the same phenotype to cluster in the representation space. Experiments on \textit{ReXGroundingCT} and \textit{LIDC-IDRI} demonstrate that $\Delta$Representation effectively structures pathological phenotype representations and improves lesion grounding and phenotype characterization accuracy in medical VLMs. Code is available at https://anonymous.4open.science/r/deltarep-CF6D.</p>
      </div>
    </details>


    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Geometry-Supervised Visual Representation Learning for Multi-Phenotype Lesion Interpretation in Medical VLMs</strong>
          <small>Hao Wang, Qiwei Zeng, Shuchang Ye, Jinghao Lin, Yuezhe Yang, Yige Peng, Jinman Kim, Lei Bi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical VLMs</span>
<span class="topic-tag">Representation Learning</span>
<span class="topic-tag">Grounding &amp; Evidence Aggregation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2610.10238</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.10238">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a medical VLM with geometry-supervised visual representation learning and anatomy-guided evidence aggregation.</p>
        <p class="abstract">Medical vision-language models (VLMs) have shown increasing potential for clinical image interpretation. However, these models still struggle to interpret multi-phenotype lesions whose diagnosis requires the joint assessment of multiple pathological phenotypes. Existing vision-language alignment methods produce visual representations that fail to preserve anatomical hierarchies and relationships among phenotypic subclasses. This stems from their reliance on semantic supervision, which lacks geometric constraints to preserve these relationships in the visual embedding space. Moreover, the sparsity of lesion-related anatomical and phenotypic representations makes it difficult for medical VLMs to capture important diagnostic evidence. To address these limitations, we propose \textbf{PureVision}, a geometry-supervised visual representation learning framework for multi-phenotype lesion interpretation in medical VLMs. It combines a geometry-supervised representation learning module, \textbf{PureEyes}, and an anatomy-guided evidence aggregation module, \textbf{PureNeurons}. PureEyes provides geometric supervision through ideal spatial distributions that encode anatomical hierarchies and phenotypic subclass relationships. PureNeurons projects visual representations into the learned latent space, using their positions to selectively aggregate lesion-specific anatomical and phenotypic evidence. Experiments on \textit{LIDC-IDRI}, \textit{CBIS-DDSM}, and \textit{3DReasonKnee} demonstrate that PureVision improves lesion grounding and phenotype characterization in visual question answering and radiology report generation. Code is available at: https://anonymous.4open.science/r/purevision-06C2.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Referring Expression Segmentation</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>InstanceBench: Diagnosing Referential Reasoning and Target Identity in Referring Expression Segmentation</strong>
          <small>Yuchen Li, Shaoyang Zhou, Yiran Wang, Ruiyi Deng, Haoyu Wang, Ziru Wei, Zhen Zhao, Luping Zhou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Referring Expression Segmentation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Grounding</span>
<span class="topic-tag">Spatial Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2610.09478</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.09478">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 and is also a strong benchmark paper: a diagnostic benchmark for referring expression segmentation, with instance-level reasoning and identity-aware metrics.</p>
        <p class="abstract">Referring Expression Segmentation (RES) links natural-language descriptions to pixel-level object masks. Yet standard evaluation provides limited insight into instance-level referential reasoning: it does not systematically distinguish referential logics, test target preservation across valid grounding paths, or separate target-selection from mask-generation errors. We introduce InstanceBench, an instance-centered diagnostic benchmark comprising 6,194 images, 9,264 target instances, and 25,077 human-verified expressions. Each target-centric expression set (TCES) fixes the image and target mask while pairing a minimal expression with a same-target variant that uses another valid cue or grounding path. A compact referential-logic taxonomy spans direct target evidence, same-class selection, relational and compositional grounding, and exclusion, while logic-critical construction suppresses simpler shortcuts. Identity-aware metrics measure target retention and set-level success while separating selection from mask-generation errors. Across 22 native-mask RES checkpoints from 18 model families, the strongest checkpoint reaches 67.1% mIoU but only 59.6% All@0.7. Controlled interventions confirm language sensitivity, while failure decomposition identifies target selection rather than mask decoding as the main bottleneck. On a controlled training subset, matched supervision improves identity-aware performance, showing that the diagnosed capability responds to targeted supervision. Collectively, InstanceBench supports a measure-diagnose-improve cycle: measuring target consistency across grounding paths, localizing failure sources, and evaluating targeted interventions.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Physical Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Do Vision Models Learn Physical Constraints or Rendering Shortcuts? A Counterfactual Benchmark for Grounded Physical Consistency</strong>
          <small>M. Moein Esfahani, Sepehr Salem, Mohammed Alser, Vince Calhoun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Physical Reasoning</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Image Editing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2610.09205</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.09205">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied/physical-scene benchmark for diagnosing physical consistency in edited images, with simulator-generated controlled violations.</p>
        <p class="abstract">Modern image editing models can satisfy a text instruction while breaking the physics of the edited scene. A new object may cast no shadow, a mirror may fail to reflect visible geometry, or an object may float above a surface that should support it. We study physical plausibility diagnosis, detecting whether an edited image violates scene physics, naming the violation type, localizing the affected region, and explaining the failure in language. We introduce a counterfactual benchmark whose controlled synthetic component uses Mitsuba~3 to generate 5,500 images from 500 scene families. Each family contains one clean image and ten matched violations involving shadows, reflection, support, surface response, and occlusion. The renderer pipeline provides category labels, affected-region masks and boxes, scene metadata, and explanation targets. We use LLaVA-1.5-7B, Qwen2.5-VL-7B, and InternVL3.5-8B as diagnostic baselines rather than proposed methods. On a 1,650-image synthetic test set, the adapted baselines reach 64.0--67.8\% category macro-F1 on standard held-out scenes. For LLaVA-1.5-7B, category macro-F1 falls from 64.0\% on the standard split to 40.8\% under intervention shift. This gap shows that high in-distribution accuracy partly reflects cues tied to rendering and counterfactual construction.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>When to Unpair: Regulating Pairing Dependence in Medical Visual In-Context Learning</strong>
          <small>Cheng Wan, Chenjun Li, Qingyu Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Medical Imaging</span>
<span class="topic-tag">In-Context Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2610.10335</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.10335">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: this is a medical vision foundation model / visual in-context learning paper with a new training strategy that fixes a specific failure mode.</p>
        <p class="abstract">Visual in-context learning (ICL), well suited to label-scarce medical imaging, uses support image-label pairs to demonstrate input-output mappings, while the labels collectively indicate the requested task. We diagnose dependence on individual pairings with a test-time derangement that reassigns every support label to another support image while preserving the query, support images, and label multiset. The resulting pairing gap, defined as shuffled-minus-matched performance, shows that all four released models depend on the pairing, to widely varying degrees. Further analysis of a paired-trained model reveals support-associated spurious regions and lesion-size biases even with real, unaltered supports, alongside sensitivity to mis-registered support labels. To regulate this dependence, we introduce a late unpairing curriculum (LUC), which starts with matched training and then applies random unpairing, replacing each support label with that of another support in the same episode. LUC nearly closes the pairing gap on two backbones while maintaining or improving matched-support performance across all evaluated task types, with gains extending to held-out tasks and cross-dataset episodes. It also mitigates these failure modes. On BraTS whole-tumor segmentation, matched-support DSC rises from 0.733 to 0.857 while the gap shrinks from -0.184 to -0.008. In a released model, brief fine-tuning with random unpairing reduces the gap. A reversed curriculum that places the same number of unpairing epochs at the start of training leaves a large gap. This shows that pairing dependence is shaped by the order of training and not only by the amount of unpaired training.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>From Pixel to Coding: Evaluating the Figure Reproduction Capabilities of MLLMs</strong>
          <small>Zijian Chen, Zhengyu Chen, Bohan Liang, Lirong Deng, Yushuo Zheng, Yanwei Jiang, Qi Jia, Kaiwei Zhang, Wenjun Zhang, Guangtao Zhai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM Evaluation</span>
<span class="topic-tag">Visual Code Generation</span>
<span class="topic-tag">Figure Understanding</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2610.10066</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.10066">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 4 moderately well: it evaluates MLLMs on figure reproduction, probing unified multimodal understanding and generation.</p>
        <p class="abstract">Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in both visual understanding and code generation. However, existing benchmarks typically evaluate these two modalities in isolation, lacking a dedicated assessment of their unification, i.e., how a model can perceive complex visual structures and synthesize them into precise, executable code. Moreover, current visual code generation benchmarks often rely on simplified layouts within single programming environments, falling short of evaluating true unified multimodal reasoning. To bridge this gap, we propose FigCodeBench, a comprehensive framework for rigorously evaluating MLLMs on figure reproduction, integrating multimodal comprehension and generation. We first design a systematic dataset construction pipeline, resulting in a total of 6,194 instances that cover 7 functional categories and 4 types of programming languages. We further categorize figure reproduction into three tiers with visual and code complexity modeling, specifically targeting complex structural reasoning, varying aspect ratios, and dense geometric constraints. We introduce a multi-dimensional evaluation protocol, encompassing visual fidelity and syntactic isomorphism, that aligns highly with the Mean Machine Opinion Score (MMOS) and human preferences. Based on our framework, we conducted extensive experiments on 24 widely used proprietary and open-source MLLMs (e.g., Gemini 3.1 Pro, GPT-5.4, and Kimi-K2.5), where we observed a universal, non-linear performance cliff across different programming languages and difficulty scenarios for all models, and gained several insights, such as the significant metric decline in rigid declarative languages.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical AI</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>Beyond Explanation: Debugging Medical Imaging Models via Concept Intervention</strong>
          <small>Samrajya Thapa, Daniel J. Quest, Timothy L. Kline, Carrie L. Langstraat, Emanuel C. Trabuco, Wei Le</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical AI</span>
<span class="topic-tag">Concept Bottleneck Models</span>
<span class="topic-tag">Model Debugging</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2610.09031</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.09031">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: concept bottleneck intervention for medical imaging models, with a plug-and-play debugging/refinement framework around a vision foundation model encoder.</p>
        <p class="abstract">Medical imaging models often operate as black boxes, limiting interpretability and systematic debugging. We introduce an easy-to-use, plug-and-play framework for concept-based interpretation and model refinement. By aligning a single-modality encoder to BioMedCLIP, we construct a Concept Bottleneck Model (CBM) that enables concept-level interventions. These interventions allow us to isolate causal versus spuriously correlated concepts, validate insights with domain experts, and generate counterfactual samples for targeted fine-tuning. We evaluate our framework on a Mayo Clinic ultrasound dataset and the CheXpert 5x200 chest X-ray dataset. Results demonstrate that concept intervention enables reliable model diagnosis while maintaining, and occasionally improving predictive performance via guided fine-tuning. Our findings highlight the practical value of this framework for controlled, interpretable refinement of clinical deep learning models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>SGF+: Decoupling Gradient Flows for Autoregressive Video Generation</strong>
          <small>Zihan Su, Junhao Zhuang, Yaowei Li, Siwen Lu, Haoran Li, Lingen Li, Haoyu Wu, Weiyang Jin, Songchun Zhang, Haoyang Huang, Chun Yuan, Zeyue Xue, Nan Duan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Autoregressive Modeling</span>
<span class="topic-tag">Temporal Consistency</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2610.10429</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.10429">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No direct match to the listed criteria; it is a video generation method, relevant to generative modeling but not specifically a listed vision foundation model or embodied AI target.</p>
        <p class="abstract">Autoregressive video generation requires denoising the current frames while writing their key-value representations as context for future predictions. However, these two roles typically share parameters, and we find that their gradients exhibit distinct patterns and systematic negative alignment, hindering the joint optimization of visual quality and temporal consistency. We introduce Self Gradient Forcing Plus (SGF+), which assigns separate parameters to context writing and denoising while preserving their interaction through causal attention. Both roles are jointly optimized using the original generation objective without auxiliary losses, with context writing supervised through its contribution to future predictions. This simple change improves visual quality and long-horizon consistency over the evaluated baselines in both framewise and chunkwise generation, without additional video training data or a longer training horizon. Trained on only 5s rollouts, SGF+ supports continuous generation for up to 24 hours without long-video fine-tuning. These results highlight role-specific parameterization as an effective design principle for high-quality autoregressive video generation and native long-horizon extrapolation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Anomaly Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Quasi-Binarized Autoencoders: An Architecture-Independent Information Bottleneck for Medical Image Anomaly Detection</strong>
          <small>Shouhei Hanaoka, Takahiro Nakao, Atsushi Takamatsu, Takeharu Yoshikawa, Osamu Abe</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Anomaly Detection</span>
<span class="topic-tag">Autoencoders</span>
<span class="topic-tag">Information Bottleneck</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2610.09670</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.09670">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 partially: an architecture-independent bottleneck for medical anomaly detection, but it is not a vision foundation model paper in the usual sense.</p>
        <p class="abstract">Unsupervised anomaly detection, which learns only from normal images, is a central task in medical image analysis and remains an open problem. Reconstruction-based methods pass an image through an encoder-decoder network trained on normal data and detect anomalies from the residual between the image and its reconstruction. This works only if the information passed from the encoder to the decoder is limited; otherwise the network learns an identity mapping and reconstructs anomalies too. This limit is usually imposed through architectural choices, tuned per dataset, that cannot be stated in bits. We introduce the quasi-binarizing (QB) layer, which squashes each latent element into [0, 1] and adds Laplace noise of scale 1/epsilon. Each element is then epsilon-locally differentially private, and the mutual information between an image and its reconstruction is bounded by a quantity that depends only on epsilon and the number of QB elements, whatever the encoder and decoder. Placing a QB layer on every encoder-decoder path, including all skip connections, we build QBAE, a seven-level attention U-Net with 32,768 QB elements. On the seven datasets of the MedIAnomaly benchmark, QBAE with one architecture and one configuration reaches a mean image-level AUROC of 0.828, the highest among methods that do not adapt to each dataset, and the best reported results on BraTS2021 (AUROC 0.911, pixel-level AP 0.838). The noise is kept at test time, so that every reconstruction satisfies the bound. Without input corruption, the bottleneck alone prevents identity collapse (mean AUROC 0.805 vs. 0.590). Code is available at https://github.com/hanaokalog/MedIAnomalyQB.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>3 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Matching Object or Relation? Tracing Abstract Reasoning Inside VLMs</strong>
          <small>Gouki Minegishi, Hiroki Furuta, Takeshi Kojima, Yusuke Iwasawa, Yutaka Matsuo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Interpretability</span>
<span class="topic-tag">Abstract Reasoning</span>
<span class="topic-tag">Mechanistic Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2610.07646</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.07646">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: this is a vision-language-model interpretability paper with mechanistic analysis of abstract reasoning circuits.</p>
        <p class="abstract">Vision Language Models (VLMs) excel on visual benchmarks but fail systematically on tasks requiring abstract reasoning. Existing benchmarks document this failure but cannot say \emph{why} it happens or which cognitive capability is missing. We close this gap by adopting the Relational Match-to-Sample (RMTS) paradigm from comparative and developmental psychology and pairing it with a mechanistic analysis of the model&#x27;s internals. On a parametrically controlled stimulus set evaluated across frontier API models (GPT, Claude, Gemini) and three open-source families (Qwen3.5, Gemma-4, InternVL3), we identify four levers that shift VLMs toward the relational match---capability tier, model scale, the number of objects per scene, and the absence of per-object stimulus noise---together producing a developmental-like trajectory that mirrors the human \emph{relational shift}. Opening up the model, a per-layer representational similarity analysis and a causal mediation analysis reveal that VLM abstract reasoning is implemented by two competing circuits: an early circuit that organises images by their surface object features, and a late circuit that organises them by their abstract relation. Extending the analysis to ARC-AGI-1, we find that ablating the relational heads identified on RMTS degrades performance more than ablating random heads, indicating that the relational circuit is recruited beyond our controlled stimuli. We hope this mechanism-level view serves as a step toward understanding how abstract reasoning is implemented in VLMs.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Visual Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>How Well Do LLMs Reason with Noisy Evidence? An Active Visual Reasoning Benchmark</strong>
          <small>Bach Nguyen, Zhaonan Li, Mau Son Nguyen, Sanika Chavan, Nilay Kumar, Hong Anh Nguyen, Khoa Vo, Ben Zhou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Visual Reasoning</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Noisy Perception</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2610.07751</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.07751">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 partially: it is a benchmark for active visual reasoning with noisy VLM feedback, but not an embodied simulator benchmark specifically.</p>
        <p class="abstract">Real-world reasoning rarely reduces to static question answering: agents must actively gather information from tools and sensors that are often noisy and unreliable. Yet most existing active reasoning benchmarks assume that environmental feedback is trustworthy, or introduce noise without exposing an explicit, calibrated uncertainty signal, leaving open how LLMs should reason when the evidence itself is uncertain. We introduce VisualNoiseQA, a novel benchmark for active reasoning under noisy visual feedback. A text-only LLM must solve VQA problems by iteratively querying a fixed, off-the-shelf VLM treated as a stochastic visual sensor. For each query, we draw multiple samples and expose an empirical uncertainty signal via self-consistency, enabling the reasoner to probe from different angles and decide what to ask next and when to stop. Our construction is automatic and scalable: starting from diverse VQA sources and two noisy VLMs, we retain only questions where the sensor is inconsistent yet human-solvable. We evaluate multiple LLM reasoners on 1,000 instances spanning perception, chart understanding, and knowledge-intensive reasoning. VisualNoiseQA thus provides a controlled playground to study how different LLMs exploit uncertainty signals for robust reasoning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LLM Alignment</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Sherpa: Teaching LLMs to Teach Adaptively</strong>
          <small>Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LLM Alignment</span>
<span class="topic-tag">Multi-Agent RL</span>
<span class="topic-tag">Adaptive Tutoring</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2610.08778</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.08778">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 only loosely: it is about training LLMs as adaptive teachers, not a new VLLM/MLLM, but it is an interesting multi-turn RL method for instruction following and simulated learner adaptation.</p>
        <p class="abstract">Large language models (LLMs) have become increasingly capable problem solvers, but being able to solve a problem is not the same as being able to teach it. Existing approaches to training LLMs as teachers rely on demonstrations, preference data, or predefined pedagogical criteria that specify what good teaching looks like. However, these signals are often not grounded in individual student learning outcomes, where effective teaching strategies can vary substantially across learners. To address this, we introduce Sherpa, a multi-turn reinforcement learning framework that instantiates multiple student archetypes with LLMs conditioned on distinct learning preferences and trains a teacher model to adapt its instruction by directly maximizing their learning outcomes. Teacher LLMs trained with Sherpa improve instructed students&#x27; performance across all archetypes by an average of 20.5 percentage points. Under MathTutorBench&#x27;s evaluation, Sherpa raises the overall pedagogy score from 52.5% to 79.2%, indicating better teaching responses. Our human studies show that the trained teacher is preferred over the base model in 79.6% of pairwise comparisons. Together, Sherpa trains LLM teachers to adapt to diverse simulated students and become better aligned with human teachers, paving the road towards AI tutors teaching real students.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

        <a class="archive-link" href="past_arxiv/2026-10-07.html">
          <span>October 07, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-05.html">
          <span>October 05, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-02.html">
          <span>October 02, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-01.html">
          <span>October 01, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-30.html">
          <span>September 30, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-29.html">
          <span>September 29, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-28.html">
          <span>September 28, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-25.html">
          <span>September 25, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-24.html">
          <span>September 24, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-23.html">
          <span>September 23, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-22.html">
          <span>September 22, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-21.html">
          <span>September 21, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-18.html">
          <span>September 18, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-17.html">
          <span>September 17, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-16.html">
          <span>September 16, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-15.html">
          <span>September 15, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-14.html">
          <span>September 14, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-12.html">
          <span>September 12, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-11.html">
          <span>September 11, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-10.html">
          <span>September 10, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-07.html">
          <span>September 07, 2026</span>
        </a>

    </div>
  </section>


  <section class="prompt-block">
    <h2>Paper selection prompt</h2>
    <pre> 1. New methodological improvements to spatial understanding, spatial intelligence on embodied agents;
 2. Shows new VLLMs (visual large language models) or MLLMs (multi-modal large language models)
 3. Embodied AI papers on buliding new benchmark (simulator related) or new methods. These papers should focus on novel angles that previous work ignored.
 4. Vision foundation models related and its applications.

 In suggesting papers to your friend, remember that he enjoys papers on computer vision and machine learning, and generative modeling in multi-modal learning.
 Your friend also likes learning about surprising empirical or insightful results in vision-language models or embodied AI, as well as clever statistical tricks.</pre>
  </section>
</main>
