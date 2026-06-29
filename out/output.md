

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
      <p class="eyebrow">Daily ArXiv / June 29, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>18</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>18</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>11.9</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">aerial</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">camera</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">category</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">challenging</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="9 mentions">change</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">collaboration</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">condition</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">diffusion</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">distillation</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">dynamic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">fine-grained</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">fine-tuning</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">generated</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">geometric</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">item</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">knowledge</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">localization</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">low-altitude</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">memory</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">mesh</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="19 mentions">motion</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">object</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">paradigm</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">pipeline</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">pose</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">prompt</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">real-world</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="10 mentions">reasoning</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">region</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">restoration</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">reward</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">rsicc</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">scalable</span><span class="cloud-word" style="font-size:1.91rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="11 mentions">scene</span><span class="cloud-word" style="font-size:2.26rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 74%, var(--accent))" title="14 mentions">semantic</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">spatial</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">structured</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">supervision</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">target</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">task-specific</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">temporal</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">understanding</span><span class="cloud-word" style="font-size:1.91rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="11 mentions">video</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">vision-language</span><span class="cloud-word" style="font-size:1.91rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="11 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="60 mentions">action</span><span class="cloud-word" style="font-size:2.24rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 73%, var(--accent))" title="221 mentions">agent</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="58 mentions">alignment</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="64 mentions">architecture</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="76 mentions">attention</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="57 mentions">camera</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="65 mentions">detection</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="62 mentions">diffusion</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="66 mentions">domain</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="63 mentions">driving</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="91 mentions">dynamic</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="60 mentions">editing</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="61 mentions">error</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="61 mentions">event</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="116 mentions">evidence</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="60 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="67 mentions">foundation</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="156 mentions">generation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="56 mentions">geometric</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="68 mentions">geometry</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="77 mentions">inference</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="90 mentions">interaction</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="83 mentions">knowledge</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="133 mentions">language</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="63 mentions">latent</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="72 mentions">mechanism</span><span class="cloud-word" style="font-size:1.72rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 46%, var(--accent))" title="148 mentions">memory</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="65 mentions">mllm</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="91 mentions">motion</span><span class="cloud-word" style="font-size:1.82rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="160 mentions">multimodal</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="68 mentions">multiple</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="106 mentions">object</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="72 mentions">optimization</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="65 mentions">paradigm</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="67 mentions">pipeline</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="66 mentions">point</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="75 mentions">policy</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="70 mentions">real-world</span><span class="cloud-word" style="font-size:2.60rem;opacity:0.96;color:color-mix(in srgb, var(--accent-2) 91%, var(--accent))" title="279 mentions">reasoning</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="65 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="70 mentions">reward</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="120 mentions">scene</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="57 mentions">search</span><span class="cloud-word" style="font-size:1.67rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="142 mentions">semantic</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="65 mentions">skill</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="68 mentions">space</span><span class="cloud-word" style="font-size:1.48rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="119 mentions">spatial</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="61 mentions">structured</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="75 mentions">supervision</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="56 mentions">support</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="76 mentions">target</span><span class="cloud-word" style="font-size:1.33rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="103 mentions">temporal</span><span class="cloud-word" style="font-size:1.67rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="141 mentions">token</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="88 mentions">trajectory</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="95 mentions">understanding</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="67 mentions">unified</span><span class="cloud-word" style="font-size:2.29rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="229 mentions">video</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="56 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="310 mentions">visual</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="63 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>17 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Intelligence</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>SpatialUAV: Benchmarking Spatial Intelligence for Low-Altitude UAV Perception, Collaboration, and Motion</strong>
          <small>Haoyu Zhang, Meng Liu, Qianlong Xiang, Kun Wang, Yaowei Wang, Liqiang Nie</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Intelligence</span>
<span class="topic-tag">UAV Benchmark</span>
<span class="topic-tag">Multi-View Reasoning</span>
<span class="topic-tag">Embodied Perception</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">18</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2606.27876</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27876">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>10</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely, and also criterion 3: it is a benchmark explicitly targeting spatial intelligence for low-altitude UAV perception, collaboration, and motion, with fine-grained spatial and multi-view reasoning tasks.</p>
        <p class="abstract">Spatial intelligence is essential for low-altitude unmanned aerial vehicle (UAV) perception, collaboration, and navigation. However, existing UAV benchmarks often emphasize image-level recognition, single-view understanding, or narrow answer formats, leaving 3D spatial inference, multi-view collaboration, scene dynamics, and diverse task formulations insufficiently evaluated. To address these gaps, we introduce SpatialUAV, a real low-altitude UAV benchmark comprising 4,331 curated instances across 14 fine-grained task types, covering semantic discrimination, spatial relation, aerial--aerial collaboration, aerial--ground collaboration, and motion understanding. SpatialUAV organizes all samples into a unified visual-input--question--answer schema, while supporting seven input configurations and nine answer formats, including option labels, region identifiers, geometric values, cross-view correspondences, and free-form motion descriptions. To ensure reliable and grounded evaluation, our data construction pipeline integrates detector-assisted regions, depth supervision, metadata-derived rules, extensive manual annotation, blind filtering, and multi-turn human validation, together with task-specific metrics for heterogeneous outputs. Evaluating representative vision-language models across three categories, we show that current models remain far from human-level performance, with pronounced bottlenecks in cross-view association, structured grounding, geometric reasoning, and temporal viewpoint understanding. These results offer empirical guidance for advancing low-altitude UAV spatial intelligence. Code and data are available at https://github.com/Hyu-Zhang/SpatialUAV.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning</strong>
          <small>Yelin Wang, Zijia Song, Shuo Ye, Chuanguang Yang, Miaoyu Wang, Yong Xu, Zhulin An, Yongjun Xu, Zitong Yu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Modeling</span>
<span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Change Captioning</span>
<span class="topic-tag">Benchmark &amp; Instruction Tuning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2606.28266</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.28266">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely, and also criterion 4 indirectly through remote-sensing vision-language application: a new MLLM pipeline for remote sensing image change captioning with a new benchmark and instruction data.</p>
        <p class="abstract">Remote Sensing Image Change Captioning (RSICC) aims to describe changes between bi-temporal remote sensing images and holds significant research and application value. However, most existing methods rely on conventional deep learning architectures, and the limited model capacity constrains performance. Although large-model post-training techniques have achieved great success in general domains, their direct transfer to RSICC remains challenging due to data scarcity and the need for fine-grained change understanding. To address this, we propose RSICCLLM, the first post-training framework for large vision-language models in RSICC. Specifically, we design a data generation paradigm, release the instruction dataset RSICI, and establish a task-specific RSICC benchmark. We further introduce Difference-aware Supervised Fine-tuning to explicitly extract change representations and guide the model in perceiving and understanding temporal differences. In addition, we propose Dual-Negative Preference Optimization (DNPO), which employs two complementary negative-sample construction strategies to construct the preference dataset RSICP and further refine model performance. Extensive experiments validate the superior capability of RSICCLLM, which achieves outstanding results with only 7B parameters, surpassing models of substantially larger scales. The code and dataset will be made publicly available at https://github.com/keaill/RSICCLLM.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video MLLM</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>Video-MME-Logical: A Controlled Diagnostic Benchmark for Video Temporal-Logical Reasoning</strong>
          <small>Hohin Kwan, Hongyu Li, Ray Zhang, Manyuan Zhang, Xianghao Kong, Anyi Rao, Jiahao Xie, Si Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video MLLM</span>
<span class="topic-tag">Temporal Reasoning</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2606.27828</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27828">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it introduces a controlled diagnostic benchmark for video temporal-logical reasoning in MLLMs.</p>
        <p class="abstract">Recent interest in multimodal large language models (MLLMs) raises a central question: can they reason over dynamic visual evidence rather than merely recognize objects or events in individual frames? This ability, which we refer to as video temporal-logical reasoning, requires models to maintain, update, and compose evidence as visual states evolve across frames. Existing video benchmarks often conflate this capability with scene complexity, static recognition, or uncontrolled temporal variation. To isolate this capability, we introduce Video-MME-Logical, a controlled benchmark organized around five temporal-logical operations: state tracking, sequential counting, temporal ordering, dynamic spatiality, and structural composition. The benchmark contains 25 fine-grained task categories generated with controlled object states, transitions, temporal dependencies, and logical compositions. It enables difficulty-controlled final-answer evaluation by varying temporal horizon and reasoning complexity, and supports intermediate-state diagnostics by verifying whether models recover the required logical reasoning trace before producing the final answer. Experiments with state-of-the-art MLLMs reveal a substantial human-model gap, especially as temporal-logical complexity increases. Supervised fine-tuning on up to 500K generated samples improves performance but remains insufficient to close the reasoning gap, positioning Video-MME-Logical as a scalable testbed for analyzing and improving temporal-logical reasoning in MLLMs.</p>
      </div>
    </details>


    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>HumanMoveVQA: Can Video MLLMs reason about human movement in videos?</strong>
          <small>Pulkit Gera, Faegheh Sardari, Asmar Nadeem, Valentina Bono, Padraig Boulton, Adrian Hilton, Armin Mustafa</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video MLLM</span>
<span class="topic-tag">Human Motion Reasoning</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2606.27999</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27999">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: this is a benchmark specifically probing whether video MLLMs can reason about human movement in space over time.</p>
        <p class="abstract">Despite the rapid advance of Multimodal Large Language Models (MLLMs) in high-level video understanding, a fundamental bottleneck remains: these models collapse complex human motion into coarse semantic labels. Existing benchmarks mostly focus on scene-centric events or local joint articulations, failing to probe global human motion in space over time (trajectory and orientation changes). We introduce HumanMoveVQA, the first comprehensive benchmark designed to evaluate global trajectory and orientation reasoning from an exocentric perspective. Our benchmark utilizes a first-frame anchored world coordinate system, preserving translation and rotation relative to a fixed starting point. We propose a scalable, multi-stage pipeline that lifts 2D video observations into world-consistent 3D motion tracks to generate over 10K structured question-answer pairs across seven reasoning categories, including motion aggregation, sequential ordering, and trajectory-level inference. Our extensive evaluation reveals a critical capability gap in state-of-the-art proprietary models on deep human motion understanding. However, we demonstrate that this is a learnable problem; by fine-tuning an open-source baseline with our targeted, world-consistent supervision, we achieve a significant improvement.HumanMoveVQA establishes a rigorous geometric foundation for developing next-generation, movement-aware video understanding models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">World Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>MemoBench: Benchmarking World Modeling in Dynamically Changing Environments</strong>
          <small>Haoyu Chen, Kaichen Zhou, Hang Hua, Kaile Zhang, Jingwen Qian, Wufei Ma, Haonan Chen, Chunjiang Liu, Yizhou Zhao, Xiaoyuan Wang, Weiyue Li, Alan Yuille, Paul Pu Liang, Yilun Du</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Modeling</span>
<span class="topic-tag">Video Generation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2606.27537</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27537">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 3 moderately: it is a new benchmark for world modeling in dynamically changing environments, with an emphasis on memory consistency under disappear-and-reappear conditions.</p>
        <p class="abstract">Video generation models aspire to simulate dynamic environments, and several benchmarks now evaluate memory consistency across frames. However, most assess consistency only while the target remains in view, and the few that force objects out of view evaluate static scenes where nothing changes during occlusion. To bridge this gap, we introduce MemoBench, a diagnostic benchmark built around the disappear-and-reappear paradigm in dynamically changing environments: a target object undergoes a physical process, disappears from view, and must be correctly recovered in its updated state upon reappearance. We curate 360 ground-truth clips spanning synthetic and real-world scenes, and design an evaluation suite combining automated metrics with VQA-based assessment across four diagnostic pillars. Evaluation of eight state-of-the-art models reveals key insights and open challenges regarding memory consistency under the disappear-and-reappear paradigm.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Qwen-Image-2.0-RL Technical Report</strong>
          <small>Yixian Xu, Kaiyuan Gao, Yuxiang Chen, Yilei Chen, Zecheng Tang, Zihao Liu, Zikai Zhou, Deqing Li, Hao Meng, Kuan Cao, Jiahao Li, Jie Zhang, Liang Peng, Lihan Jiang, Ningyuan Tang, Shengming Yin, Tianhe Wu, Xiaoyue Chen, Yan Shu, Yanran Zhang, Yi Wang, Yu Wu, Yujia Wu, Zekai Zhang, Zhendong Wang, Xiao Xu, Kun Yan, Chenfei Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Text-to-Image</span>
<span class="topic-tag">RLHF</span>
<span class="topic-tag">Image Editing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2606.27608</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27608">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it is a post-training/reward-modeling report for a vision foundation model for text-to-image generation and image editing, with RLHF and on-policy distillation.</p>
        <p class="abstract">We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. To provide reliable reward signals, we construct task-specific composite reward models by fine-tuning vision-language models with a pointwise scoring paradigm and chain-of-thought reasoning. For text-to-image generation, the reward models cover alignment, aesthetics, and portrait fidelity dimensions. For image editing tasks, the reward system addresses instruction-following accuracy and face identity preservation. Building on this reward system, we develop a scalable GRPO-based RL training framework, incorporating a hybrid classifier-free guidance (CFG) strategy to preserve pre-trained knowledge, prompt curation via intra-group reward range filtering, and per-category reward weight calibration. To merge the task-specialized RL policies for T2I and editing, we propose on-policy distillation as the final training stage, which consolidates multiple teachers into a single student model through trajectory-level velocity matching. Extensive evaluation shows that Qwen-Image-2.0-RL achieves 57.84 overall score on Qwen-Image-Bench (+2.61 over the base model), Elo ratings of 1193 in text-to-image arena (+78) and 1349 in image edit arena (+93), demonstrating consistent gains in aesthetic quality, prompt adherence, and editing accuracy.</p>
      </div>
    </details>


    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>TextDS: Parameter-Efficient Representation Alignment for Scene Text Detection under Distribution Shifts</strong>
          <small>Boyuan Chen, Zichen Dang, Chuang Yang, Lap-pui Chau, Yi Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Scene Text Detection</span>
<span class="topic-tag">Domain Shift</span>
<span class="topic-tag">Parameter-Efficient Fine-Tuning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2606.28077</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.28077">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it uses visual foundation models for scene text detection under distribution shifts, with a new efficient adaptation framework and adverse-condition datasets.</p>
        <p class="abstract">In real-world deployments, scene text detectors inevitably face distribution shifts beyond the training distribution. Prior work often depends on large-scale scene-text pretraining, yet evaluation under cross-domain changes and real-world imaging degradations remains limited. We propose TextDS, an efficient framework for scene text detection under distribution shifts. First, we propose a data-efficient dual-encoder design with visual foundation models, eliminating the reliance on large-scale scene-text pretraining. Second, we introduce Step-wise LoRA adaptation (SWLoRA), which performs progressive low-rank refinement with a dynamic early-exit mechanism for effective feature adaptation. Third, we propose Common Subspace Fusion (CSF) to align and fuse the two branches in a shared subspace while retaining complementary, shift-robust information. Finally, we construct adverse-condition scene text detection datasets to address the gap in evaluating under imaging degradation. Experiments show that TextDS achieves competitive performance in scene text detection, demonstrating robustness across domains and adverse imaging conditions with only 4.9M trainable parameters.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Understanding Cross-Rig Generalization in Automotive Perception: a Multi-Rig Benchmark and Rig Variation Metrics</strong>
          <small>Tim Alexander Bader, Tim Dieter Eberhardt, Maximilian Dillitzer, Wilhelm Stork</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multi-View Perception</span>
<span class="topic-tag">Domain Generalization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2606.27554</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27554">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> This matches criterion 3 closely: it introduces a new benchmark for cross-rig generalization in autonomous driving, focusing on a novel geometric sensor-rig variation angle that prior work often ignored.</p>
        <p class="abstract">Camera-based perception systems for autonomous driving are typically developed and evaluated using fixed sensor rigs, while real-world vehicle fleets exhibit substantial variation in camera placement, orientation, field of view, and camera count. This mismatch introduces a cross-rig domain gap in which only the geometric observation process changes. To study this effect under controlled conditions, we introduce Plentiful CARLA Camera Rigs, a benchmark that renders identical driving scenes under 14 systematically designed camera rigs. This setup enables direct analysis of cross-rig generalization without confounding changes in scene content or appearance. Using the benchmark, we analyze cross-rig transfer behavior of representative multi-view perception architectures and observe substantial performance shifts induced by geometric rig variation. To facilitate structured analysis, we further introduce two calibration-based descriptors derived from rig metadata: Rig Variance, capturing internal rig diversity, and Rig Contrastive Distance, measuring geometric discrepancy between rigs. Our experiments show that geometric rig differences strongly correlate with relative cross-rig performance shifts and that Rig Contrastive Distance provides a reliable proxy for ranking transfer difficulty between sensor rigs.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LVLM Hallucination</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Dismantling Pathological Shortcuts: A Causal Framework for Faithful LVLM Decoding</strong>
          <small>Liu Yu, Can Chen, Ping Kuang, Zhikun Feng, Fan Zhou, Gillian Dobbie</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LVLM Hallucination</span>
<span class="topic-tag">Causal Inference</span>
<span class="topic-tag">Faithful Decoding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2606.27596</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27596">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: this is about LVLM decoding and hallucination mitigation with a causal/inference-time method.</p>
        <p class="abstract">Large Vision-Language Models (LVLMs) exhibit sophisticated reasoning but remain susceptible to object hallucination. Deviating from the prevailing attention intensity assumption, we reveal a deeper dynamic structural misalignment: hallucination is triggered at decision-critical steps where specific attention heads, acting as risky mediators, decouple from visual evidence to lock onto language priors. This establishes a pathological shortcut that bypasses visual grounding. To dismantle this, we propose Fox (Faithfulness and Observational-flow via eXpression-rectification), a training-free inference-time framework. Fox diagnoses structural misalignment using a visual attention entropy probe to localize risky mediators unsupervisedly. We then execute a targeted causal intervention via numerical logit saturation to physically sever the shortcut path. Finally, a conflict-gated cooperative decoding strategy reconciles interventional faithfulness with observational fluency. Extensive experiments demonstrate that Fox achieves SOTA performance, outperforming SID by 29.1% while preserving linguistic richness. Code is available at https://github.com/Cc2021start/Fox.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Aerial Localization</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>SemCityLoc: Aerial 6DoF Localization Using Semantic 3D City Models</strong>
          <small>Jingfeng Mao, Xuyang Chen, Qilin Zhang, Oussema Dhaouadi, Guangming Wang, Brian Sheil, Daniel Cremers, Yan Xia, Olaf Wysocki</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Aerial Localization</span>
<span class="topic-tag">Foundation Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Semantic Mapping</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2606.27444</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27444">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it uses foundation-model-derived semantic priors for aerial localization and also introduces a new benchmark for semantic city-model-based pose estimation.</p>
        <p class="abstract">Aerial 6DoF localization typically relies on precise GNSS signals or radiometrically rich 3D reconstructions, limiting scalability and on-board deployment. We propose SemCityLoc, a semantic-geometric alignment system that reframes aerial pose estimation as structured surface registration between foundation-model-derived visual priors and standardized LoD-compliant 3D city models. Instead of matching sparse contours or dense texture, our method aligns semantic surfaces and monocular depth with lightweight semantic 3D building models, increasing pose discriminability in repetitive and occluded urban environments. To enable accurate evaluation, we introduce SemCityLockeD, the first real-world benchmark combining centimeter-accurate UAV poses with standardized LoD1--LoD3 semantic city models and challenging low-altitude imagery. Experiments demonstrate substantial improvements over existing map-based approaches, improving recall by up to 36% and reducing mean positional error from 9.89m to 2.62m in challenging urban canyons. Our results indicate that semantically structured geometry provides sufficient and scalable constraints for high-precision aerial localization without radiometric scene reconstructions. The code and data are available at https://albertchen98.github.io/SemCityLoc.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>Home3D 1.0: A High-Fidelity Image-to-3D Asset Generation System for Interior Design</strong>
          <small>Yiyun Fei, Guoqiu Li, Jin Song, Chuqiao Wu, Delong Wu, Hong Wu, Ziru Zeng, Haohui Chen, YinDong Kong, Jing Li, Qi Wu, Feng Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Generation</span>
<span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Image-to-3D</span>
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
          <span>Paper 11 / arXiv:2606.27923</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27923">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it is a vision foundation-model-driven pipeline, using image-to-3D generation and multimodal components for interior-design asset creation.</p>
        <p class="abstract">We present Home3D 1.0, a modular image-to-3D generation system that produces high-quality 3D assets from a single reference image, targeting interior design and e-commerce applications. Given a photograph of a furniture or decor item, the system outputs a mesh with physically-based rendering (PBR) materials, and the mesh can be decomposed into material-specific components. The pipeline is organized into four tightly coupled modules: Geometry reconstructs a watertight mesh through latent SDF modelling with a geometry VAE and a coarse-to-fine flow-matching DiT; Texture predicts multiview albedo observations, reprojects them onto the mesh, and completes unseen surface regions with a 3D texture field; Material uses MatWeaver to obtain component masks through video-based segmentation and UV-space voting, then retrieves and bakes PBR maps from a curated material library through hierarchical multi-modal matching; and Parts generates material-editable semantic part meshes with a PartVAE and PartDiT, decoding multi-head part-specific SDF fields in one pass. Each module is evaluated independently with dedicated metrics, highlighting both the current system capability and the remaining gaps toward broader deployment.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Segment Anything</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Temporal-Emerged Prompting for Segment Anything in Multiframe Infrared Small Target Detection</strong>
          <small>Yinghui Xing, Donghao Chu, Shizhou Zhang, Di Xu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Segment Anything</span>
<span class="topic-tag">Infrared Small Target Detection</span>
<span class="topic-tag">Temporal Prompting</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2606.27655</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27655">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 and partly 1: it adapts SAM with temporal prompting for infrared small-target segmentation, which is a foundation-model application to a specialized spatial detection setting.</p>
        <p class="abstract">Accurately localizing and segmenting small targets in low signal-to-noise ratio (SNR) infrared sequences remains a challenging task. Since targets are often indistinguishable from the background in individual frames, existing methods, even when equipped with advanced foundation model and powerful inter-frame association mechanisms, still fail to detect them. Motivated by the observation that targets tend to emerge gradually from the background over time and become distinguishable, we propose Temporal-Emerged Prompting for Segment Anything Model (TEP-SAM), a principled framework designed to explicitly exploit such temporal-emerged cues to modulate and prompt SAM. TEP-SAM operates by jointly modeling global motion patterns and local motion deviations to locate potential targets. It further enhances target region features by leveraging motion discrepancy, thereby generating temporal-emerged cues for SAM and enabling non-interactive segmentation. By bridging large-scale semantic pretraining with task-specific temporal modeling, TEP-SAM effectively adapts SAM to the challenging multiframe infrared small target detection task. Extensive experiments demonstrate the effectiveness of our approach, particularly under severely low-SNR conditions and in complex dynamic background.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Diffusion</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>SIFT: Self-Imagination Fine-Tuning for Physically Plausible Motion in Video Diffusion Models</strong>
          <small>Ruoyu Wang, Jialun Liu, Huayang Huang, Haibin Huang, Jiepeng Wang, Chi Zhang, Xuelong Li, Yu Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Diffusion</span>
<span class="topic-tag">Motion Modeling</span>
<span class="topic-tag">Generative Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2606.27741</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27741">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is a video diffusion method for physically plausible motion, interesting for generative modeling but not specifically embodied AI or VLLM/MLLM work.</p>
        <p class="abstract">Recent advances in video diffusion models have greatly improved visual fidelity, yet their generated motions often violate physical plausibility. We observe a common kinematic failure, &quot;motion entanglement&quot;, the unintended coupling of independent motion sources, such as camera movement and object motion. We identify that this issue stems from data bias and the reconstruction-based training design of diffusion models. Training on noisy videos that still retain coarse motion cues inadvertently encourages the model to replicate existing motion without an incentive to learn how to model kinematically-grounded motions. To address this, we propose a Self-Imagination Fine-Tuning (SIFT) paradigm, which enables the model to learn from its own generated videos rather than directly reconstructing real ones, breaking the reconstruction shortcut. We further employ motion-aware discriminative supervision and a progressive hard-case replay strategy to stabilize and accelerate learning. By leveraging freely-generated text prompts, our method can densely cover a broad motion space, including rare or finely-disentangled scenarios that would be costly to collect as video data. Extensive experiments demonstrate that our approach substantially improves the physical realism, motion disentanglement, and controllability of generated videos.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Diffusion Models</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>PixelU: A U-Shaped Transformer for Efficient End-to-End Pixel Diffusion</strong>
          <small>Zipeng Guo, Lichen Ma, Yu He, Xiaolong Fu, Jingling Fu, Junshi Huang, Yan Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Image Synthesis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2606.27760</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27760">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is a generative modeling paper on pixel-space diffusion, which fits your friend&#x27;s broader interests but not the specific spatial/embodied/VLLM/foundation-model application criteria.</p>
        <p class="abstract">End-to-end pixel-space diffusion models bypass the lossy compression of Latent Diffusion Models (LDMs) but struggle to jointly model low-frequency semantics and high-frequency signals in high-dimensional space. Existing works heavily rely on complex pixel decoders to alleviate this issue. In this paper, we challenge this trend by revealing that these decoders primarily compensate for the optimization difficulties inherent to velocity prediction ($v$-prediction). Under the clean data paradigm ($x$-prediction), they are redundant. Motivated by this insight, we advocate for simplicity over complexity and introduce PixelU, a minimalist, single-stage U-shaped Diffusion Transformer tailored for pixel space. PixelU abandons auxiliary decoders in favor of zero-cost skip connections, which provide an &quot;information highway&quot; that directly routes uncorrupted high-frequency spatial details from shallow to deep layers. To further enable the backbone to focus exclusively on modeling low-frequency semantics, we introduce a constant-channel spatial down-sampling mechanism as a natural low-pass filter, which compresses deep features into a compact, low-frequency semantic manifold. Extensive experiments demonstrate that this decoupling of frequencies could outperform the strong baseline (JiT-G) with only about 1/3 of its computation cost. On ImageNet 256$\times$256 and 512$\times$512, PixelU achieves FID of 1.63 and 1.92 respectively, surpassing recent pixel-space methods and establishing a simple yet powerful new paradigm for end-to-end diffusion models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Restoration</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>BiDeMem: Bidirectional Degradation Memory for Explainable Image Restoration</strong>
          <small>Xinrui Wu, Lichen Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Restoration</span>
<span class="topic-tag">Degradation Modeling</span>
<span class="topic-tag">Explainability</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2606.28112</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.28112">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to the four criteria; it is an explainable image restoration method with a memory mechanism, relevant mainly to clever modeling tricks.</p>
        <p class="abstract">Degradation-aware prompts, conditions, and latent priors are increasingly used in image restoration, yet they are usually judged by a single endpoint: whether the restored image obtains higher PSNR. This is a weak test of semantics. A condition can help by adding capacity, acting as a global correction bias, or exploiting dataset shortcuts, without becoming an interpretable degradation prior. We propose BiDeMem, a bidirectional degradation memory for explainable image restoration. A query built from restoration features and input statistics retrieves a compact top-k subset of memory slots. The same selected slot identity supports the restoration path at inference time and a training-only forward-degradation explanation path. The study centers on verifiability in a controlled multi-degradation NAFNet setting. New controls separate the gain from a correction head alone, a dense query prior, and a static global prior: these variants are 0.2588, 0.2586, and 0.2839 dB below BiRank, respectively. Strong residual supervision and a wider degradation head also remain below the full bidirectional memory model. Intervention probes show that BiRank preserves restoration quality while increasing wrong-prior and native-prior sensitivity, framing degradation memory as both a restoration module and a falsifiable explanation mechanism.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Cross-Modal Distillation</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Large Language Model Teaches Visual Students: Cross-Modality Transfer of Fine-Grained Conceptual Knowledge</strong>
          <small>Thomas Shih-Chao Liang, Zhuoran Yu, Yong Jae Lee</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Cross-Modal Distillation</span>
<span class="topic-tag">Vision Classification</span>
<span class="topic-tag">LLM Supervision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2606.27527</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27527">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 only indirectly: it is a cross-modal distillation method from an LLM to a visual student, but it is not about spatial understanding/embodied agents or a VLLM/MLLM benchmark.</p>
        <p class="abstract">Large Language Models (LLMs) possess broad conceptual knowledge acquired through large-scale text pretraining, yet their potential to supervise models in other modalities remains underexplored. In this work, we propose LaViD--Language-to-Visual Knowledge Distillation--a simple and effective framework for transferring high-level semantic knowledge from a language-only teacher to a vision-only student model. Instead of relying on paired multimodal data, LaViD elicits conceptual signals from an LLM by prompting it to generate multiple-choice questions (MCQs) that probe semantic distinctions between visual classes. Each class is mapped to a soft label distribution over these MCQs, forming a rich conceptual signature that guides the student through an auxiliary distillation loss. Notably, despite using a language-only teacher without access to image data, LaViD consistently outperforms recent methods like MaKD that distill from vision-language models across multiple fine-grained benchmarks. It also achieves competitive or superior performance compared to state-of-the-art visual distillation methods such as DKD and MLKD, with further gains when combined with logit standardization. On the Waterbirds dataset, LaViD substantially improves worst-group accuracy, demonstrating enhanced robustness to spurious correlations with distillation. Code is available at https://github.com/lliangthomas/lavid.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LiDAR Localization</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>Learning 1-Bit LiDAR-based Localization with Auxiliary Objective</strong>
          <small>Kaijie Yin, Zhiyuan Zhang, Tian Gao, Wentao Zhu, Cheng-zhong Xu, Hui Kong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LiDAR Localization</span>
<span class="topic-tag">Binary Neural Networks</span>
<span class="topic-tag">Efficient Inference</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2606.27729</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.27729">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; it is a lightweight LiDAR localization method for autonomous systems, which is adjacent to criterion 1 but not really about embodied spatial intelligence or a new benchmark.</p>
        <p class="abstract">6-DoF LiDAR-based localization is a fundamental capability for autonomous systems operating in large-scale outdoor environments. Many deep-learning-based localization methods have achieved promising performance so far. However, as one of the always-on modules competing for limited on-board computational resources, the localization module is expected to consume only a small portion of the overall compute budget. Most existing learning-based methods are still too heavy for this purpose. In contrast, binary neural networks (BNNs) offer an appealing solution, but the 1-bit compression causes severe information loss and performance drop. In this paper, we address this challenge by proposing Binarized LiDAR-based Localization (BiLoc), the first binary neural network framework for 6-DoF LiDAR localization. Specifically, we reinterpret the training of BNNs from the perspective of the information-bottleneck principle, aiming at retaining minimal yet sufficient representations for pose estimation while suppressing redundant variations. And we introduce an auxiliary objective that adaptively regulates information retention in the binary encoder, effectively mitigating the information loss caused by binarization. This auxiliary objective provides additional optimization signals that compensate for the limited representational capacity and the gradient mismatch inherent in BNNs. Extensive experiments on large-scale outdoor LiDAR datasets demonstrate that BiLoc establishes a new state of the art for LiDAR localization with BNNs.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>1 paper</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">LLM/VLM System</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications</strong>
          <small>Oxygen AIIC, Chan Long, Chao Liu, Chaofan Chen, Chaohui Dong, Chunyuan Guo, Danping Liu, Debin Liu, Deping Xiang, Fulai Xu, Guangyue Liu, Hao Li, Huichun Hu, Jian Yang, Jianan Wang, Jianbo Zhao, Jiaoyang Li, Jiaxing Wang, Jinglong Li, Jinjin Guo, Jun Fang, Jun Liu, Kai Zhou, Li Wang, Lili Gao, Liying Chen, Luning Yang, Mengdi Zhou, Pengzhang Liu, Qi Lv, Qianyun Wang, Qixia Jiang, Ruyue Li, Shimu Liang, Shuxing Wang, Sijie Zhang, Siqi Li, Tianhao Gao, Wang Ke, Weihu Huang, Wencan Lai, Wenjie Zhang, Xiaohui Zhang, Xiaojing Dong, Ya Liu, Yifeng Zhang, Yixiang Wang, Yongtai Zhang, Yongyi Liao, Zhaoru Chen, Zhen Chen, Zhiyong Ma, Zhiyuan Liu, Zhongwei Liu, Ziyan Xing</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LLM/VLM System</span>
<span class="topic-tag">Industrial AI</span>
<span class="topic-tag">Item Understanding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2606.28070</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.28070">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 4 only in a broad industrial sense: it is an LLM/VLM-centered item-understanding system, but more of a platform paper than a new model or benchmark.</p>
        <p class="abstract">JD.com, one of the world&#x27;s largest e-commerce platforms, serves over 700 million active users and millions of merchants, with a catalog of tens of billions of SKUs. At this scale, high-quality, structured item knowledge underpins a better consumer experience, lower management costs, and higher operational efficiency-yet producing and serving it poses three industrial-scale challenges: fast-emerging concepts, high-quality knowledge production for massive SKUs, and diverse downstream requirements. To address these challenges, we present the JD Oxygen AI Item Center (Oxygen AIIC), an industrial-scale platform built on LLMs/VLMs for item-knowledge production and service. Oxygen AIIC is built around four core pillars: (i) ontology engineering driven by efficient human-AI collaboration, which supports the dynamic evolution and agile expansion of an ontology with millions of entries; (ii) a &quot;Semantic Search then Discrimination&quot;(S2D) knowledge identification architecture that, combined with throughput improvement strategies, enables scalable, extensible, and high-throughput AI Item Library production for tens of billions of SKUs; (iii) self-evolving item-understanding LLMs/VLMs that improve in a stable and controllable manner, enabling knowledge production with 94.2% precision and 82.8% recall; and (iv) a unified item tunnel that serves as the data and service hub. Oxygen AIIC now covers tens of thousands of JD categories and processes hundreds of millions of item updates per day on Huawei Ascend NPUs. It has accumulated hundreds of billions of item-knowledge assets. Deployed across core business scenarios-including search, recommendation, operations, category planning-Oxygen AIIC has delivered measurable gains at scale. Search-traffic coverage reaches 80.4%, item-information quality issues drop by 37%, the automated fill rate of core attributes during item listing exceeds 80%.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

        <a class="archive-link" href="past_arxiv/2026-06-26.html">
          <span>June 26, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-25.html">
          <span>June 25, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-24.html">
          <span>June 24, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-20.html">
          <span>June 20, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-19.html">
          <span>June 19, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-18.html">
          <span>June 18, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-17.html">
          <span>June 17, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-16.html">
          <span>June 16, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-15.html">
          <span>June 15, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-12.html">
          <span>June 12, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-11.html">
          <span>June 11, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-10.html">
          <span>June 10, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-09.html">
          <span>June 09, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-08.html">
          <span>June 08, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-06.html">
          <span>June 06, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-05.html">
          <span>June 05, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-04.html">
          <span>June 04, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-03.html">
          <span>June 03, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-02.html">
          <span>June 02, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-01.html">
          <span>June 01, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-05-29.html">
          <span>May 29, 2026</span>
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
