

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
      <p class="eyebrow">Daily ArXiv / August 07, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>28</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>14</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>10.3</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">action</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="11 mentions">agent</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">alignment</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="11 mentions">audio-visual</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="10 mentions">budget</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="14 mentions">change</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">conditioning</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">consistent</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">constraint</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">cost</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">decision</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="9 mentions">detection</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">diagnostic</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="10 mentions">distribution</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">dynamic</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">end-to-end</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="29 mentions">evidence</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">finding</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="12 mentions">frame</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">frozen</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="12 mentions">generation</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">grad-cam</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="11 mentions">historical</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="9 mentions">latent</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">metadata</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="9 mentions">multimodal</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">noise</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="11 mentions">object</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="14 mentions">point</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">preserve</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">prompt</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="10 mentions">ranking</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">reduce</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="9 mentions">residual</span><span class="cloud-word" style="font-size:2.31rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="22 mentions">semantic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">sparse</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="12 mentions">target</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="9 mentions">temporal</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">textual</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">token</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="9 mentions">uncertainty</span><span class="cloud-word" style="font-size:2.24rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 73%, var(--accent))" title="21 mentions">video</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">vision-language</span><span class="cloud-word" style="font-size:2.51rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 87%, var(--accent))" title="25 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="106 mentions">action</span><span class="cloud-word" style="font-size:1.62rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="183 mentions">agent</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="99 mentions">alignment</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="70 mentions">camera</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">challenging</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="93 mentions">consistency</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="73 mentions">control</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="71 mentions">cost</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="73 mentions">dense</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="103 mentions">detection</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="83 mentions">diffusion</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="70 mentions">distribution</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="74 mentions">domain</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="102 mentions">dynamic</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="76 mentions">environment</span><span class="cloud-word" style="font-size:1.62rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="183 mentions">evidence</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="101 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="76 mentions">foundation</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="95 mentions">frame</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="73 mentions">fusion</span><span class="cloud-word" style="font-size:2.03rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 62%, var(--accent))" title="264 mentions">generation</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="73 mentions">geometry</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="100 mentions">inference</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="129 mentions">interaction</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="140 mentions">language</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="76 mentions">latent</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="98 mentions">memory</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="72 mentions">mllm</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="72 mentions">modality</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="142 mentions">motion</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="208 mentions">multimodal</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="87 mentions">multiple</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="171 mentions">object</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="77 mentions">perception</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="93 mentions">pipeline</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="91 mentions">point</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="72 mentions">query</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="91 mentions">real-world</span><span class="cloud-word" style="font-size:1.63rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="185 mentions">reasoning</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="110 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="82 mentions">region</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="75 mentions">retrieval</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="69 mentions">robust</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="157 mentions">scene</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="74 mentions">segmentation</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="210 mentions">semantic</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="86 mentions">space</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="137 mentions">spatial</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="86 mentions">support</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="117 mentions">target</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="121 mentions">temporal</span><span class="cloud-word" style="font-size:1.59rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="178 mentions">token</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="77 mentions">trajectory</span><span class="cloud-word" style="font-size:1.33rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="136 mentions">understanding</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="107 mentions">unified</span><span class="cloud-word" style="font-size:2.51rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 87%, var(--accent))" title="376 mentions">video</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="71 mentions">vision</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="445 mentions">visual</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="84 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>22 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>TruthLens: Object Hallucination Detection via Self-Evaluating Truthfulness Scores in LVLMs</strong>
          <small>Yanqi Wu, Runhe Lai, Xinhua Lu, Qichao Chen, Zhiping Zhou, Jia-Xin Zhuang, Weijiang Yu, Ruixuan Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Hallucination Detection</span>
<span class="topic-tag">Model Calibration</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2608.05616</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05616">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: a new LVLM method for object hallucination detection with no extra inference cost.</p>
        <p class="abstract">Despite the remarkable progress of large vision language models (LVLMs), object hallucination remains a fundamental challenge that hinders their trustworthy deployment. A key finding motivates our work: real and hallucinated object tokens are clearly separable in hidden representations, yet this separability is largely lost at the language-modeling (LM) head. We propose TruthLens, a self-evaluation framework that teaches the LM head to expose a per-object truthfulness signal without any auxiliary model or additional inference cost. Concretely, a rarely-used special token is repurposed as a reference token. For each object-token position, we extract the log-probability assigned to this special token by the LM head, and define its difference from a predefined constant as the truthfulness score. The model is then fine-tuned with an MSE objective that drives scores toward 1 for real objects and 0 for hallucinated ones, while a divergence constraint preserves the original generation capability. Despite being trained on only a limited set of object categories, TruthLens generalizes effectively to benchmarks with substantially larger label spaces. Extensive experiments across multiple LVLMs demonstrate state-of-the-art performance; notably, on Qwen2.5-VL-7B, TruthLens outperforms the previous best method on MS-COCO by over 17\% in AUROC. Our code is available at https://github.com/wyqstan/TruthLens.</p>
      </div>
    </details>


    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Respect Your Zero-Shot Uncertainty: Conservative Calibration for Test-Time-Adapted Vision-Language Models</strong>
          <small>Jingyan Jiang, Yaru Sun, Xiao Chen, Jiazhen Huang, Caiting Li, Zhijian He, Yin Chen, Pingting Hao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Calibration</span>
<span class="topic-tag">Test-Time Adaptation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2608.05945</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05945">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a calibration method for test-time-adapted vision-language models, with an insightful empirical finding about sharpening and uncertainty.</p>
        <p class="abstract">Test-time adaptation (TTA) can improve the recognition accuracy of vision-language models under distribution shift, but often degrades calibration, making predictive confidence unreliable for downstream decision-making. Many existing label-free calibration approaches are either coupled to prompt optimization or rely on logit-range statistics that provide only a coarse characterization of the predictive distribution. We show that TTA can increase confidence and reduce entropy even when the top-1 prediction and its correctness remain unchanged, a failure mode we term prediction-preserving sharpening. Across diverse TTA methods and benchmarks, larger entropy reductions relative to paired zero-shot predictions are associated with greater increases in Expected Calibration Error (ECE). On entropy-reduced samples, confidence gains also tend to exceed accuracy gains. Based on these findings, we propose Zero-Shot-Anchored Entropy Calibration (ZAEC), a label-free post-hoc method that uses zero-shot entropy as a sample-specific uncertainty reference. ZAEC selectively restores the zero-shot entropy of sharpened predictions through minimal temperature scaling while leaving all other predictions unchanged. It requires no labeled calibration data or learned parameters and preserves class rankings and classification accuracy. Across five TTA methods and 15 datasets, ZAEC achieves the lowest post-hoc macro-average ECE on ViT-B/16, with consistent gains on RN50.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>HERA: Historical Evidence Routing Adapter for Physical Prediction in Latent World Models</strong>
          <small>Yuanruyi, Yue Cao, Haojia Gao, Guanqiu Guo, Ziyuezhang, Shangqin, Junbo Tan, Bokui Chen, Zhuo Zou, Xueqian Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Physical Prediction</span>
<span class="topic-tag">Occlusion Reasoning</span>
<span class="topic-tag">Video Prediction</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2608.05523</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05523">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: a latent world-model adaptation for physical prediction under occlusion, specifically routing historical evidence in predictive video models.</p>
        <p class="abstract">Predictive video models have emerged as promising world models by learning latent visual dynamics from large-scale video. Yet these models remain challenged by physical events under occlusion, where later predictions may depend on object evidence that is no longer available in the current view. Addressing this challenge requires historical evidence not only to be preserved but also to remain accessible when it becomes relevant to a subsequent prediction. Existing approaches mainly enlarge the temporal context, cache generic video features, or impose explicit object-centric states, thereby improving the capacity or structure of retained history. However, they do not directly address how relevant historical evidence can be selectively retrieved and integrated into a pretrained predictor without interfering with its native latent workspace. Accordingly, we introduce HERA (Historical Evidence Routing Adapter), a framework for routing retained historical evidence into a frozen latent predictor, and instantiate it with Register-Routed Patch Memory (RRPM), a lightweight adapter comprising a Structured Memory Bank, Memory Registers, and Workspace Registers. On the IntPhys2 Main split, HERA with RRPM improves the pairwise AvgSurprise accuracy of V-JEPA 2-G from 52.57% to 54.35%. Subgroup analysis shows particularly strong improvements on fixed-camera continuity, from 46.15% to 57.69%, and fixed-camera immutability, from 46.15% to 63.46%. These results support historical evidence routing as a practical adaptation strategy for physical prediction in latent world models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Generative Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Vorch-Omni: Multi-Task Orchestration of Sight and Sound</strong>
          <small>Vorch Team, Xiaoyu Chen, Yang Ding, Cong Han, Menglin Han, Yuxin Hong, Jiebo Hou, Zequn Jie, Xiang Li, Jing Liu, Qi Liu, Yulei Lu, Siyuan Luo, Lin Ma, Xin Ma, Yinlong Qian, Peng Shi, Fang Wan, Siqi Wang, Yaohui Wang, Yaole Wang, Yidi Wu, Siqian Yang, Mingyu Yin, Haoran Yu, Gang Yue, Lisai Zhang, Yuting Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Generative Modeling</span>
<span class="topic-tag">Video Synthesis</span>
<span class="topic-tag">Audio-Visual Generation</span>
<span class="topic-tag">VLM Conditioning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2608.05803</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05803">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: a new multi-task visual/audio generation framework that explicitly uses a VLM as part of the synthesis pipeline.</p>
        <p class="abstract">Recent advances in generative video modeling have enabled diverse generation, reference-based synthesis, extension, and editing, but existing approaches often rely on fragmented task-specific models. A general model must distinguish heterogeneous target, source, and reference signals to determine what to generate, preserve, or use as guidance, while reducing interference among tasks. Joint audio-visual generation further increases this challenge by introducing diverse conditioning and output configurations across modalities. We present Vorch-Omni, a unified multi-task framework for audio-visual synthesis based on an arbitrary-condition-to-arbitrary-output formulation. It flexibly treats video and audio signals as either conditioning inputs or generation targets. Token-level conditioning masks and task identifiers distinguish targets, source content, and references, while position types separate temporal context from independent conditions. To capture semantic and structural information, Vorch-Omni employs complementary visual conditioning pathways: a vision-language model interprets sampled frames with text instructions, and a video VAE encodes conditions into latent tokens for direct guidance. We further build a distributed data pipeline to curate diverse temporally aligned audio-visual clips, generate structured captions and metadata, and balance heterogeneous task distributions. Built on a single flow-matching diffusion transformer without task-specific architectural changes, Vorch-Omni supports over 10 tasks, including text-to-video, text-to-audio-video, image- and reference-conditioned generation, temporal extension, audio-driven generation, video transformation, and audio-visual editing. This unified framework provides a scalable foundation for general-purpose audio-visual generation and manipulation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Agentic Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Beyond Relevance: Bayesian Evidence Acquisition for Agentic Whole-Slide Image Reasoning</strong>
          <small>Bryan Wong, Xun Xu, Huazhu Fu, Nancy F. Chen, Mun Yong Yi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agentic Reasoning</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Medical AI</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2608.05757</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05757">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: an embodied/agentic benchmark-style reasoning framework for whole-slide image evidence acquisition with a novel Bayesian decision angle.</p>
        <p class="abstract">Whole-slide image (WSI) reasoning requires an agent to sequentially acquire visual evidence before answering a diagnostic question. Existing training-free agentic frameworks formulate this process as iterative patch retrieval based on semantic relevance to the question. However, semantic relevance does not necessarily imply diagnostic informativeness in computational pathology, where competing diagnoses often exhibit similar and overlapping morphological patterns, making many patches semantically relevant yet diagnostically non-discriminative. Consequently, relevance-based retrieval may acquire redundant observations and leave diagnostic uncertainty unresolved. We propose BEACON, a plug-and-play agentic framework that reformulates WSI reasoning as a Bayesian evidence acquisition problem. BEACON maintains a probabilistic belief over competing diagnostic hypotheses and sequentially acquires patches by maximizing expected information gain (EIG) to reduce diagnostic uncertainty. An evidence controller then determines whether to answer, acquire additional evidence, or perform higher-resolution inspection. Built entirely from off-the-shelf foundation models, BEACON requires no additional training or fine-tuning. Extensive zero-shot experiments across five WSI-VQA benchmarks demonstrate that BEACON achieves the strongest overall performance among training-free agentic frameworks while substantially improving evidence acquisition efficiency, establishing Bayesian evidence acquisition as a principled paradigm for uncertainty-aware agentic WSI reasoning. The code is available at https://github.com/bryanwong17/BEACON</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multi-Modal LLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Evidence-Driven Dynamic Visual Selector for Efficient Long Video Understanding</strong>
          <small>Bo Zhang, Wenxin Wang, Feng Chen, Zhihao Zhang, Zixuan Wang, Changsheng Li, Yinjie Lei</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multi-Modal LLMs</span>
<span class="topic-tag">Long Video Understanding</span>
<span class="topic-tag">Efficient Inference</span>
<span class="topic-tag">Visual Token Selection</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2608.05780</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05780">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: proposes a new MLLM-based method for long video understanding with evidence-driven visual selection.</p>
        <p class="abstract">Recent advancements in MLLM-based long-form video understanding have mitigated inference-time computational cost and limited context lengths by selecting query-relevant frames. However, existing approaches predominantly rely on external proxy scorers and rigid heuristic rules, inevitably suffering from misalignment with the target MLLM&#x27;s intrinsic evidence and failing to accommodate the non-uniform spatiotemporal information density. In this paper, we propose a fine-grained dynamic visual selection framework named EviSelect, grounded in the target MLLM internal attention evidence. Our method efficiently probes visual evidence via sparse prefilling as a structured prior to guide distribution-aware dynamic sampling. Specifically, we efficiently approximate attention maps of the target MLLM using highly compressed visual inputs and sparse attention, well-aligned to the full counterpart. Conditioned on three complementary attention components derived from this prior, we design a lightweight selector that not only precisely locates query-relevant timestamps but also adaptively adjusts the local sampling rate and spatial resolution. To enable evidence-conditioned spatiotemporal sampling, we formulate the selector as a stochastic policy and optimize it via GRPO under a joint accuracy--efficiency reward. By rewarding correct predictions under lower visual cost through group-relative comparisons, our method encourages the policy to allocate computation dynamically according to the information density of each video. Across three long video understanding benchmarks, EviSelect achieves superior performance compared to existing methods while reducing selected visual tokens by about 50\% and achieving a 3.9x end-to-end speedup.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Registration</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Ordered Diffusion for 3D Human Registration</strong>
          <small>Mattia Masiero, Ilya A. Petrov, Daniel Cremers, Gerard Pons-Moll, Riccardo Marin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Registration</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Spatial Alignment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2608.05804</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05804">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: new methodological improvement for 3D human registration via generative/diffusion modeling of spatial alignment.</p>
        <p class="abstract">3D human registration has historically been treated as a regression task, assuming a unique ground-truth alignment exists between the template and an input point cloud. In reality, acquisition noise, occlusions, and unknown soft tissue dynamics introduce inherent ambiguity into human scans. Regression-based methods consequently converge to an average prediction, often failing to represent a plausible geometry. In our work, we embrace such uncertainty by modeling the registration as a distribution of alignments. We propose ODin, which formulates registration as a 3D diffusion process that generates a point cloud aligned with the target geometry while preserving template semantics through consistent point ordering. To achieve this, ODin relies on global, local, and positional conditioning, guiding each point to its correct location. Our experiments demonstrate that such a generative formulation not only outperforms its regression-based baseline, but also establishes a new state of the art, surpassing highly engineered methods while reducing the registration time by two-thirds. Pre-trained models and code are available at https://riccardomarin.github.io/odin/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Invisible Shortcuts: Why Vision Encoders Know Your Camera</strong>
          <small>Vladan Stojni\&#x27;c, Ryan Ramos, Giorgos Kordopatis-Zilos, Noa Garcia, Giorgos Tolias</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Shortcut Learning</span>
<span class="topic-tag">Robustness</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2608.05424</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05424">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: analyzes vision foundation models/vision encoders and reveals a surprising shortcut effect from invisible metadata traces.</p>
        <p class="abstract">Deep vision models exploit shortcuts, relying on cues that correlate with supervision signals. Prior work has focused on visible biases, such as object-background or texture correlations. We identify a different source of shortcut learning: invisible metadata traces embedded at the pixel level, for metadata such as image processing and photo acquisition. We hypothesize that large-scale semantic supervision, whether through categorical labels (ImageNet) or billion-scale captions (LAION), naturally induces metadata-semantics correlations during pretraining, leading models to convert low-level signals into predictive features. By introducing controlled metadata-semantics correlations, we show that stronger ones produce systematically higher sensitivity to metadata traces and larger performance degradation under metadata distribution shifts. We further explore mitigation strategies applied during and after pretraining that reduce sensitivity not only to targeted metadata but also to unseen ones, without sacrificing performance on downstream tasks. Metadata sensitivity also has a positive side: it partly explains the strong generated-image detection ability of some encoders, while its mitigation can improve out-of-distribution generalization. Code: https://github.com/ryan-caesar-ramos/visual-encoder-traces</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical AI</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>DistMedVL: Distributional Vision-Language Alignment for Uncertainty-Aware Medical Image Segmentation</strong>
          <small>Jiaxuan Li, Qing Xu, Xiangjian He, Yue Li, Daokun Zhang, Fiseha B. Tesema, Rong Qu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical AI</span>
<span class="topic-tag">Vision-Language Segmentation</span>
<span class="topic-tag">Uncertainty Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.MM</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2608.05683</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05683">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: vision-language foundation model used for uncertainty-aware medical image segmentation.</p>
        <p class="abstract">Cross-modal alignment of visual and textual representations is fundamental to multimodal medical image understanding, yet remains hindered by uncertainty in both modalities under real-world clinical conditions. Existing vision-language segmentation methods rely on deterministic cross-modal matching, which overlooks aleatoric uncertainty from ambiguous boundaries and epistemic uncertainty from limited training data, leading to fragile performance under domain shift. To address this issue, we propose DistMedVL, a probabilistic vision-language framework that introduces a lightweight Probabilistic Cross-Modal Adapter (PCM-Adapter) upon frozen encoders to explicitly model representational uncertainty. Specifically, the PCM-Adapter comprises two sequential modules for progressive probabilistic alignment. We first devise a Mahalanobis Alignment Module (MAM) that models textual tokens as Gaussian distributions and computes patch-text compatibility via Mahalanobis distance, yielding variance-conditioned matching that downweights unreliable feature dimensions. Moreover, we devise a Distribution Flow Module (DFM) that estimates modality-wise confidence parameters and performs vision-guided refinement of textual distributions, accommodating distributional variation across imaging modalities. Extensive experiments across eight medical segmentation benchmarks demonstrate that DistMedVL outperforms state-of-the-art methods with only 6.3M trainable parameters, exhibiting superior data efficiency, perturbation robustness and cross-dataset generalization.</p>
      </div>
    </details>


    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>STAIL: Semantic Text-Anchored Incremental Learning for Medical Imaging via Large Language Models</strong>
          <small>Songpan Gao, Yajie Zhang, Guanxing Chen, Jiayu Qian, Zhenzhen Liu, Shijun Li, Xiaowei Zhu, Yao Hu, Kay Chen Tan, Yu-An Huang, Shiqi Wang, Zhi-An Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical AI</span>
<span class="topic-tag">Continual Learning</span>
<span class="topic-tag">Vision-Language Alignment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 20 / arXiv:2608.05808</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05808">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a vision-language/LLM-anchored continual learning method for medical imaging, leveraging textual semantics to preserve knowledge.</p>
        <p class="abstract">Deep learning models applied to medical image analysis suffer from severe catastrophic forgetting when continually adapting to new clinical tasks in dynamic environments. Mainstream incremental learning methods typically mitigate this by rehearsing raw historical images. However, this pixel-level rehearsal incurs significant storage overhead, raises privacy concerns, and fails to adequately capture the true data distribution with sparse exemplars. Inspired by human cognitive mechanisms, we propose a novel framework termed Semantic Text-Anchored Incremental Learning (STAIL) for sequential clinical tasks. To overcome the rehearsal bottleneck, STAIL introduces an asymmetric semantic consolidation buffer (SCB). By incorporating a minimal set of image anchors and extensive textual descriptions, the SCB enables dense semantic reconstruction of old tasks at a minimal storage cost. Furthermore, we design an LLM-derived Semantic Anchoring Mechanism (LSAM) that leverages the stable semantic space of frozen large language models as developmental priors. This mechanism explicitly anchors evolving visual features to textual representations, guiding and constraining plasticity and stability at both macroscopic and microscopic levels. Extensive experiments across three heterogeneous medical datasets, covering fundus, ultrasound, and X-ray imaging, demonstrate that STAIL acts as a highly effective plug-and-play module. It comprehensively enhances the performance of various existing baselines, achieving average gains of 2.24\% in AAA-AUC for sustained performance and 3.55\% in BWT-AUC for reduced forgetting. Code is available.</p>
      </div>
    </details>


    <details class="paper-row" id="link20">
      <summary class="paper-row-summary">
        <span class="queue-index">21</span>
        <span class="paper-row-copy">
          <strong>Text-Guided Refinement of Multi-sequence Glioma Subregion Segmentation with a Vision-Language Foundation Model</strong>
          <small>Zach Eidex, Yu-nong Lin, Mojtaba Safari, Sean Pitroda, Ralph Weichselbaum, Zhen Tian, Xiaofeng Yang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical AI</span>
<span class="topic-tag">Vision-Language Foundation Models</span>
<span class="topic-tag">Interactive Segmentation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 21 / arXiv:2608.05389</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05389">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: uses a vision-language foundation model for text-guided medical segmentation refinement.</p>
        <p class="abstract">Background: Accurate glioma subregion delineation is important for radiotherapy planning and longitudinal monitoring, but manual contour correction is time-consuming. Models such as nnU-Net may generalize imperfectly and lack clinician-directed text correction.   Purpose: We investigated adapting a three-dimensional (3D) vision-language foundation model for text-guided brain tumor segmentation refinement.   Methods: We developed a lightweight VoxTell-based framework. Pretrained VoxTell generated initial masks. Oracle prompts derived from segmentation errors encoded target, action, location, imaging evidence, edit size, and preservation constraints. Frozen Qwen/VoxTell prompt embeddings were injected through trainable projections into its multiscale decoder conditioning; other weights remained frozen. Training, validation, and testing used 901, 100, and 250 BraTS-GLI cases. Cross-dataset transfer was evaluated on 100 meningioma, metastasis, pediatric tumor, and UPENN-GBM cases.   Results: On the internal test set using post-contrast T1-weighted input, correct instructions improved subregion Dice similarity coefficient (DSC; enhancing tumor, edema, and necrotic/non-enhancing core) from $0.774\pm0.158$ to $0.796\pm0.137$. They outperformed blank prompts ($0.762\pm0.155$; Holm-adjusted $p&lt;0.001$, $d_z=0.71$) and contradictory prompts ($0.770\pm0.163$; $p&lt;0.001$, $d_z=0.48$). In cross-dataset testing, correct instructions improved DSC from $0.527\pm0.287$ to $0.550\pm0.278$ and outperformed contradictory instructions ($0.504\pm0.275$; $p&lt;0.001$, $d_z=0.43$).   Conclusion: A 3D vision-language foundation model can perform instruction-guided refinement of glioma subregion segmentations. Sensitivity to correct, blank, and contradictory prompts suggests text-dependent contour editing rather than nonspecific post-processing, supporting further evaluation as a clinician-in-the-loop tool.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification</strong>
          <small>Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, Siqian Yang, Jingyuan Chen, Lin Ma, Yaohui Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Generation</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Audio-Visual Synthesis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2608.05776</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05776">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 weakly: a generative multimodal world model for long-horizon audio-visual generation, but not a vision foundation model application in the usual sense.</p>
        <p class="abstract">Autoregressive continuation provides a natural path toward minute-scale audio-visual generation by repeatedly extending a short-window generator conditioned on previously generated video and audio. However, models are trained on clean ground-truth histories, while inference relies on their own generated histories, where accumulated errors cause identity drift, over-smoothing, and audio-visual desynchronization. Recent methods reduce this mismatch by reusing prediction residuals as synthetic corruption, but we observe that the effectiveness of residual correction critically depends on the flow-matching noise level at which residuals are produced. We propose Vorch-Director, a noise-level-aware residual correction strategy that associates each residual with its originating noise level and injects residuals from matched noise regimes during training. By aligning injected errors with the denoising process, Vorch-Director produces more realistic autoregressive histories while retaining efficient teacher-forcing training. Built on the audio-visual LTX-2 diffusion transformer, Vorch-Director further introduces task embeddings to distinguish historical video, reference images, and target video, enabling unified conditioning for long-horizon generation. Together with a clean conditioning sink and mixed-task training, Vorch-Director supports multi-shot, multi-subject, reference-guided audio-visual long-video generation. We evaluate Vorch-Director on ST-Bench and introduce a new long-horizon audio-visual benchmark with metrics for quality drift and long-range consistency. Extensive experiments demonstrate improved stability and audio-visual fidelity over strong baselines.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Understanding</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>Depth-Guided Video Object Counting in Crowded Scenes</strong>
          <small>Yuanjing Xu, Xinyan Liu, Weidong Chen, Zixuan Zou, Linhao Zhang, Zhuangzhe Meng, Antoni B. Chan, Weigang Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Understanding</span>
<span class="topic-tag">RGB-D Perception</span>
<span class="topic-tag">Object Counting</span>
<span class="topic-tag">Occlusion Reasoning</span>
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
          <span>Paper 15 / arXiv:2608.06236</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.06236">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: improves spatial understanding in crowded scenes with depth-guided RGB-D counting and occlusion-aware detection.</p>
        <p class="abstract">Our primary objective is to advance video object counting in crowded scenes, aiming to robustly count all instances of a target category based on given text or visual prompts. Existing methods rely on RGB information, limiting their discriminative ability in crowded and occluded conditions. To address this, we propose a Depth-Guided Detector (DG-Det) along with a general post-processing pipeline. By integrating depth cues with multi-scale RGB-D cross-attention and explicit occlusion prediction, our method enhances spatial understanding and achieves robust detection in crowded and occluded scenes. Furthermore, we introduce a unified de-duplication framework to eliminate cross-frame redundant counting. To facilitate future research, we also release a new RGB-D Video Object Counting dataset featuring depth information and multiple object categories persequence. Extensive experiments demonstrate that our method achieves a 62.01\% reduction in MAE compared to existing baselines, and also produces consistent improvements in RMSE. We provide the source code at https://github.com/streamer-AP/DG-Net and the dataset at https://huggingface.co/datasets/aerospace123/RGBD-VideoCount.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Long-Video Understanding</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>One Ranking, Any Budget: Matryoshka Evidence-to-Context Frame Selection for Long-Video Understanding</strong>
          <small>Wang Chen, Yu Chen, Xiang Wang, Shuai Li, Jinfa Huang, Xiawu Zheng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Long-Video Understanding</span>
<span class="topic-tag">Frame Selection</span>
<span class="topic-tag">Multimodal Models</span>
<span class="topic-tag">Efficient Inference</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2608.05707</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05707">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a method for long-video understanding and frame selection for LMMs, directly supporting visual foundation model applications.</p>
        <p class="abstract">Frame selection is essential for applying Large Multimodal Models (LMMs) to long videos due to severe frame redundancy and limited context windows. Since the appropriate frame budget varies with the downstream LMM, reasoning demands, and latency constraints, a practical selector should serve multiple budgets. However, existing methods typically optimize an isolated frame subset for each predefined budget: when the budget changes, previously selected evidence may be replaced rather than progressively augmented. Ranking frames by a fixed score would allow prefix reuse across budgets, but it ignores the distinct roles of different ranking positions. In this paper, we formulate long-video frame selection as a Matryoshka ranking problem: constructing a single priority sequence whose small prefixes concentrate query-conditioned evidence, while progressively larger prefixes preserve this evidence and add broader temporal context. Efficiently constructing such a ranking is itself challenging, as densely sampling long videos and evaluating frame-query relevance incurs substantial overhead. We therefore introduce Matryoshka Evidence-to-Context (MEC) Frame Selection, a training-free framework that builds a reusable sparse video index, discovers candidates through sparse probing and local zooming, and greedily constructs a position-adaptive ranking: early positions emphasize evidence; later positions progressively favor temporal coverage while preserving visual diversity. A single ranking can thus be truncated to any target budget without rerunning the selector. Across four benchmarks and six frame budgets, MEC improves average accuracy over uniform sampling by 3.77 percentage points, matches strong state-of-the-art selectors, and reduces end-to-end selection latency by 47.37-51.19%.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Perception</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>LoDA: A Level of Detection Aware Method and a Multimodal Sensing Benchmark for Object Level Change Detection</strong>
          <small>Haitian Wang, Xinyu Wang, Sheldon Fung, Xian Zhang, Zichen Geng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Perception</span>
<span class="topic-tag">LiDAR Change Detection</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Autonomous Driving</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2608.05356</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05356">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: builds a new simulator/benchmark-style resource for object-level change detection in multi-temporal 3D LiDAR, with a novel level-of-detection-aware angle.</p>
        <p class="abstract">High-definition 3D LiDAR maps are important for autonomous driving and smart-city services, which require reliable detection of object-level changes in multi-temporal urban LiDAR to keep digital maps aligned with the physical world. Existing approaches from raster height differencing to depth image and point-cloud networks often remain tile-based and threshold-driven, yielding per-point scores without explicit detection limits or consistent object-level labels. We propose an object-level 3D change-detection pipeline that integrates detection-limit-aware registration, geometry-driven object proxies with rule-based semantic and instance segmentation, and displacement cues in height, volume, and surface-normal direction to assign five change labels with confidence. By decoupling registration, geometry, and semantics, the pipeline propagates pose uncertainty into spatially varying detection limits, stabilizes cross-epoch correspondences, and suppresses false changes caused by residual misalignment and density variation. We also present LoDA, a level-of-detection (LoD) aware benchmark for the Subiaco district with fused multi-temporal vehicle-LiDAR maps constructed with LiDAR, GNSS, and IMU support, semantic instances, and object-level annotations. On this benchmark, our method achieves 95.0% accuracy, 90.8% macro F1, and 83.0% macro IoU, exceeding the best baseline by 8.7 IoU points and 4.4 F1 points. On the public Urb3DCD-V2 benchmark evaluated under the official point-wise protocol, it reaches 96.81% mean accuracy and 89.52% mean change IoU, improving over the strongest reported baselines by 1.36 points in mAcc and 3.18 points in mIoUch.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Character Animation</summary>
      <div class="queue">

    <details class="paper-row" id="link21">
      <summary class="paper-row-summary">
        <span class="queue-index">22</span>
        <span class="paper-row-copy">
          <strong>Wan-Animate-2: Pushing the Application Boundaries of Character Animation</strong>
          <small>Guangyuan Wang, Li Hu, Dechao Meng, Zhongyi Zhang, Peng Zhang, Mingyang Huang, Ruoshi Zhang, Ke Sun, Zhe Zhang, Xingjun Wang, Gang Cheng, Bang Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Character Animation</span>
<span class="topic-tag">Diffusion Transformer</span>
<span class="topic-tag">Real-Time Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 22 / arXiv:2608.06009</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.06009">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No direct match to the listed criteria; it is a character animation/generative modeling paper, which is adjacent to your friend&#x27;s interests but not one of the specified categories.</p>
        <p class="abstract">Character image animation remains a foundational yet challenging task in computer vision. Existing approaches can be broadly categorized into three paradigms: methods based on explicit motion representations suffer from extraction errors and identity drift; methods based on implicit motion features lose fine-grained dynamics through compression; and in-context learning approaches avoid intermediate representations but incur prohibitive computational costs. Furthermore, all current systems are designed for offline synthesis, unable to meet the real-time requirements of interactive applications such as digital avatars and live-streaming hosts. To address these limitations, we present Wan-Animate-2, an end-to-end character animation framework that directly consumes the driving video within a redesigned Diffusion Transformer. Our architecture achieves superior motion fidelity and identity preservation by eliminating intermediate motion extractors entirely. We further introduce text driven viewpoint control that decouples the output camera perspective from the driving video--a capability rarely supported by prior character animation methods that rely on explicit motion representations. Beyond generation quality, we present Wan-Animate-2-Lite, an efficient variant that reduces inference latency to real-time thresholds through a three-stage training paradigm: teacher forcing pretraining with error buffer mechanism, and Self-Forcing distillation with chunk-wise backpropagation. This enables streaming character animation for interactive applications, opening new deployment scenarios that were previously infeasible. Qualitative evaluations and user studies demonstrate that Wan-Animate-2 achieves high-fidelity animation results across diverse characters and motion patterns. To foster further research and community development, we will release the Wan-Animate-2-Base model weights to the public.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Vision-Language</summary>
      <div class="queue">

    <details class="paper-row" id="link22">
      <summary class="paper-row-summary">
        <span class="queue-index">23</span>
        <span class="paper-row-copy">
          <strong>Positive-Unlabeled Preference Optimization For Chest X-ray Report Generation</strong>
          <small>Yuta Kobayashi, Pradyun Ramesh, Muhammad Ahmed Chaudhry, Vincent Jeanselme, Judy Wawira Gichoya, Sanmi Koyejo, Kathleen Capaccione, Shalmali Joshi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Vision-Language</span>
<span class="topic-tag">Preference Optimization</span>
<span class="topic-tag">Report Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 23 / arXiv:2608.05341</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05341">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 loosely: a VLM training/optimization method for chest X-ray report generation, but it is domain-specific rather than a general new MLLM architecture.</p>
        <p class="abstract">Vision-Language Models (VLMs) for radiology report generation are typically trained on retrospective clinical reports, which suffer from omission noise: clinically present findings are left unreported due to the omission of subtle findings. For example, prior studies show that cardiomegaly may be omitted from ICU chest X-ray reports when the imaging request is focused on monitoring support device placement. As a result, models trained with standard approaches inherit these omissions, learning to under-report findings themselves. We propose PU-DPO, a preference optimization framework to prevent omission noise from corrupting the preference signal. We reformulate the objective under a positive-unlabeled (PU) learning framework, treating absent mentions as unlabeled rather than truly negative. Our framework provides preference supervision using constructed contrastive pairs, generated using edits to model responses, producing variants that explicitly mention or omit a specific finding. Generated responses that mention the finding are naturally preferred in the context of visual evidence. Across semi-synthetic experiments and analyses on real-world chest radiograph benchmarks where adjudicated labels are available, PU-DPO yields consistent gains in detection rates and recovery of hidden positives across multiple pathologies, and is more robust to omission noise than prior approaches.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Remote Sensing</summary>
      <div class="queue">

    <details class="paper-row" id="link23">
      <summary class="paper-row-summary">
        <span class="queue-index">24</span>
        <span class="paper-row-copy">
          <strong>DARAD: Dual Adapters and Ranking-Aware Distillation for Continual Remote Sensing Image-Text Retrieval</strong>
          <small>Xi Chen, Xu Chen, Xiangyang Jia, Wei Wang, Xu Zhang, Zhenyuan Sun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Image-Text Retrieval</span>
<span class="topic-tag">Continual Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 24 / arXiv:2608.06059</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.06059">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately: a continual remote-sensing image-text retrieval method built on vision-language alignment, though it is more incremental than foundational.</p>
        <p class="abstract">With the rapid growth of Earth observation technologies, remote sensing archives are rapidly expanding, making remote sensing image-text retrieval (RS-ITR) increasingly important. However, continual RS-ITR remains challenging because scale variation and distribution shifts in RS aggravate cross-modal alignment space distortion, making it difficult for existing continual learning (CL) methods to support reliable continual retrieval. To address this challenge, we propose DARAD, a dual-adapter and ranking-aware distillation framework that preserves the historical cross-modal ranking structure while learning new visual and textual concepts from evolving archives. Specifically, the visual branch introduces a spatial fusion adapter, which integrates coarse regional cues and fine-grained patch cues to accommodate RS scale variation while anchoring visual updates to the pretrained alignment space. The textual branch employs multi-expert semantic routing, which separates shared textual semantics from semantically specialized residuals to absorb newly emerging descriptions while constraining global text embedding drift. Furthermore, bidirectional ranking distillation uses a frozen teacher model and historical anchors to preserve the historical cross-modal ranking structure, thereby mitigating alignment space distortion across continual stages. Experiments under a multi-stage continual retrieval protocol show that DARAD achieves superior performance over existing CL methods, improving adaptation to newly arrived data while maintaining effectiveness on historical data.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LiDAR Scene Completion</summary>
      <div class="queue">

    <details class="paper-row" id="link24">
      <summary class="paper-row-summary">
        <span class="queue-index">25</span>
        <span class="paper-row-copy">
          <strong>Iterate or Widen? When Test-Time Refinement Helps LiDAR Scene Completion: A Controlled Study of Evidence Geometry, Training Coverage, and Compute</strong>
          <small>Shijie Hao, Weining Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LiDAR Scene Completion</span>
<span class="topic-tag">Test-Time Refinement</span>
<span class="topic-tag">3D Perception</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 25 / arXiv:2608.06014</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.06014">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No direct match to the listed criteria; it is a controlled study on LiDAR scene completion and test-time refinement, relevant to embodied/spatial understanding but not a new method or benchmark in a clearly novel angle.</p>
        <p class="abstract">Should a completion model spend extra test-time compute by iterating, or spend a similar parameter budget on a wider one-shot predictor? The answer is easily confounded by denoising curricula, corruption augmentation, capacity, and unpaired evaluation. We study this question in LiDAR semantic scene completion by comparing a one-shot predictor, a parameter-matched wider predictor, and a weight-tied multigrid refiner initialized from the same frozen predictor. The protocol separates coherent region removal, independent thinning, range-dependent attenuation, and additive clutter while preserving exact scene-condition pairing. Across five training seeds and 815 SemanticKITTI sequence-08 frames, the full iterative system improves mIoU over the wide control by 0.911 points under contiguous angular removal, with a 95% moving-block bootstrap interval of [0.804, 1.040] that clears a predeclared 0.5-point practical margin. Under independent 75% thinning, iteration adds only 0.300 points [0.166, 0.436], whereas observation-family augmentation adds 5.975 points [5.662, 6.140]. Neither intervention repairs additive clutter. The iterative system also costs 10.74 ms and 0.75 GiB per frame, versus 6.25 ms and 0.23 GiB for the wide control. These results establish a geometry-conditioned empirical boundary rather than a universal advantage: coherent gaps can justify fixed-depth refinement, broadly thinned evidence is addressed more effectively by training coverage, and spurious evidence requires a different robustness mechanism.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Restoration</summary>
      <div class="queue">

    <details class="paper-row" id="link25">
      <summary class="paper-row-summary">
        <span class="queue-index">26</span>
        <span class="paper-row-copy">
          <strong>Dual-Output Multi-Exposure HDR Reconstruction via SDR Fusion and Gain Map Inverse Tone Mapping</strong>
          <small>Jinho Kim, Jinwoo Kim, Seon Joo Kim</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Restoration</span>
<span class="topic-tag">HDR Reconstruction</span>
<span class="topic-tag">Latent Diffusion</span>
<span class="topic-tag">Computational Photography</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 26 / arXiv:2608.05626</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05626">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: vision reconstruction with latent diffusion and gain-map inverse tone mapping, relevant to vision foundation/model-based image restoration applications.</p>
        <p class="abstract">We propose DOME-HDR, a dual-output multi-exposure HDR reconstruction framework that jointly produces a perceptually balanced SDR image and a consistent HDR image via gain map inverse tone mapping. Given three bracketed LDR inputs, DOME-HDR first synthesizes a base SDR using a LoRA-adapted latent diffusion model. A dual cross-attention fusion module injects complementary structural and color cues from the under- and over-exposed images while anchoring on the mid exposure for stability. The synthesized SDR then guides HPGM, our HDR Prior-guided Gain Map network, to predict a spatially varying gain map for reliable dynamic-range expansion. We evaluate on Kalantari, Tel, and Challenge123 using both full-reference and no-reference metrics, where DOME-HDR achieves state-of-the-art HDR reconstruction quality; ablations further confirm the effectiveness of dual cross-attention and SDR-guided gain map estimation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Physical Reconstruction</summary>
      <div class="queue">

    <details class="paper-row" id="link26">
      <summary class="paper-row-summary">
        <span class="queue-index">27</span>
        <span class="paper-row-copy">
          <strong>BendTwin: Robust Dense-to-Sparse Physical Reconstruction with Bending-Aware Differentiable Spring-Mass Models</strong>
          <small>Yixiong Jing, Qi Wang, Lin Chen, Junwei Jiang, Guangming Wang, Haibing Wu, Olaf Wysocki, Wanli Ma, Brian Sheil</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Physical Reconstruction</span>
<span class="topic-tag">Deformable Objects</span>
<span class="topic-tag">Differentiable Simulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 27 / arXiv:2608.06164</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.06164">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 partially: embodied/physical reconstruction from video for deformable objects, but it is more digital-twin reconstruction than new embodied spatial intelligence.</p>
        <p class="abstract">Reconstructing objects with mechanical properties from video observations enables physically consistent dynamic prediction, benefiting robotics planning and interaction. Existing spring--mass based physical driven reconstruction approaches offer efficient and differentiable physical reconstruction, but they typically rely on axial springs alone. Such formulations oversimplify the underlying structural mechanics and can become mechanically under-constrained when the physical graph is coarsened, limiting their ability to preserve stable local deformation. We present BendTwin, a bending-aware differentiable spring--mass framework for video-based reconstruction and future prediction of deformable objects. BendTwin introduces bending stiffness and damping over local surface triplets, penalizing deviations from rest angles and regularizing higher-order deformation. These bending constraints improve mechanical stability while preserving the simplicity of spring--mass system. Experiments show that BendTwin consistently outperforms the axial-only PhysTwin baseline. Ablation studies further demonstrate that the bending constraints maintain system stability across different downsampling ratios and consistently improve upon the original PhysTwin formulation. Overall, BendTwin provides an effective approach for constructing mechanically faithful digital twins from sparse-view RGB-D videos.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Transformers</summary>
      <div class="queue">

    <details class="paper-row" id="link27">
      <summary class="paper-row-summary">
        <span class="queue-index">28</span>
        <span class="paper-row-copy">
          <strong>Grad-CAM for Vision Transformers: A Systematic Taxonomy and Audit of Methodological Ambiguity in Explainable AI</strong>
          <small>Casey Wall, Longwei Wang, Rodrigue Rizk, KC Santosh</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Transformers</span>
<span class="topic-tag">Explainable AI</span>
<span class="topic-tag">Interpretability Audit</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 28 / arXiv:2608.05258</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05258">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>3</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 weakly: an audit of Grad-CAM adaptations for Vision Transformers, useful for vision foundation model interpretability but not a new model or benchmark.</p>
        <p class="abstract">Gradient-weighted Class Activation Mapping (Grad-CAM) is widely used to visualize model decisions, but it was originally formulated for convolutional neural networks, where spatial feature maps and channel dimensions have clear architectural meanings. Vision Transformers (ViTs) do not provide the same structure, instead representing images through tokens, attention, residual streams, and multimodal interactions. This paper presents a systematic taxonomy and literature audit of how Grad-CAM and related methods are adapted, justified, and reported for ViT-based architectures. From an initial search of more than 550 papers, we identify 175 papers that apply Grad-CAM or Grad-CAM-adjacent methods to ViTs. We find that most papers do not provide a full mathematical or implementation-level account of how Grad-CAM is adapted to transformer representations. To characterize this gap, we introduce a descriptive taxonomy of ViT Grad-CAM adaptations that makes explicit the feature locations, gradient targets, spatial reconstruction steps, and aggregation choices that are often left implicit. This taxonomy is not intended to prescribe a single correct adaptation, but to clarify the range of methodological choices being made. The study shows that Grad-CAM on ViTs is often treated as a trivial extension of CNN-based Grad-CAM, despite requiring nontrivial choices that affect rigor, reproducibility, and interpretation.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>6 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation</strong>
          <small>Yuru Feng, Yaoqi Chen, Beidi Zhao, Qianxi Zhang, Xinjiang Wang, Jianan Lu, Zhirui Wang, Shusen Xu, Zengzhong Li, Qi Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Agents</span>
<span class="topic-tag">Test-Time Adaptation</span>
<span class="topic-tag">Skill Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2608.05628</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05628">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: embodied/agentic paper on autonomous skill improvement with a new test-time exploration-and-exploitation method.</p>
        <p class="abstract">Although agent skills equip LLMs with reusable procedural knowledge, manual maintenance suffers from high costs, unscalability, and misalignment. Real-world deployments thus require autonomous, on-demand skill evolution at test time, constrained by limited interaction budgets and a lack of training or validation sets. This setting introduces a severe sparse reward challenge, where outcomes conflate multiple latent failure causes. Under such ambiguity, existing methods that greedily refine a single incumbent skill are particularly vulnerable to an exploitation trap, allowing early misdiagnoses to exhaust limited trials along unproductive trajectories. To address this, we introduce SkillHEX, a closed-loop framework coupling hypothesis-driven self-verification with evidence-guided tree search. SkillHEX translates falsifiable failure hypotheses into executable tests, producing diagnostic evidence as dense reward without additional environment attempts. This evidence guides a search over persistent skill-revision branches, dynamically balancing the exploitation of supported edits with the exploration of plausible alternatives. Evaluated on 87 tasks from SkillsBench, SkillHEX outperforms existing self-evolving methods and achieves an average pass rate of 55.9% and 57.9% using GPT-5.3-Codex and Claude Opus 4.7 under a five-iteration budget, respectively.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">GUI Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>StepReflect: Structured UI Transition Reflection for Mobile GUI Agents</strong>
          <small>Linqiang Guo (Peter), Wei Liu (Peter), Li Gu (Peter), Yang Wang (Peter), Tse-Hsun (Peter), Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">GUI Agents</span>
<span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Action Reflection</span>
<span class="topic-tag">Mobile Automation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2608.05587</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05587">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new method for mobile GUI agents, focusing on structured step-level reflection for long-horizon embodied interaction.</p>
        <p class="abstract">Autonomous mobile GUI agents require accurate action reflection for reliable long-horizon execution. Existing approaches rely on open-ended multimodal reasoning after each action, which is costly and poorly matched to the structured nature of GUI state transitions. We propose StepReflect, which formulates per-step GUI reflection as supervised structured prediction conditioned on explicit transition specifications and paired visual evidence. StepReflect is trained through a staged pipeline combining supervised fine-tuning, teacher-student distillation, and preference- and reward-based refinement. Offline, the resulting 8B model achieves 82.16% transition-level accuracy on AndroidWorld, exceeding zero-shot GPT-5.2 by 11.83 percentage points under the same structured input. Online, across M3A, Agent-SAMA, MAI-UI-8B, and Seed-2.0-Pro, StepReflect achieves higher task success in three of four agent configurations and remains within one successful task of the GPT-5.2 Reflection Agent in the fourth. It also reduces paid API charges relative to GPT-based reflection in all four configurations. These results establish StepReflect as a practical, locally deployable alternative to repeated frontier-model reflection for long-horizon mobile GUI agents.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LLM Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model</strong>
          <small>Wenhao Lin, Chenyu Yu, Xingwei Lin, Sicong Cao, Xiang Chen, Lei Xue, Le Yu, Letian Sha, Chunming Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LLM Agents</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Safety Guardrails</span>
<span class="topic-tag">Long-Horizon Planning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.CR</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2608.05695</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05695">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: an embodied-agent runtime guardrail with a risk-aware world model, focusing on long-horizon action safety for LLM agents.</p>
        <p class="abstract">As large language model (LLM) agents increasingly invoke external tools and interact with real-world systems, unsafe actions may cause irreversible consequences on external states, user data, and downstream services. Recent runtime guardrails mitigate such risks by checking proposed actions before execution, but many remain reactive: they primarily assess the apparent safety of the current action, lacking an explicit model of how risk evolves across the trajectory. This limitation creates a critical blind spot for long-horizon risks, where individually benign-looking actions can gradually drift the agent toward hazardous states. In response, we propose DreamGuard, a proactive guardrail for LLM agents built around a risk-aware world model. The world model maintains a compact recurrent latent state over the trajectory and predicts future latent states from which DreamGuard derives immediate-hazard and prefix-risk evidence. It then fuses these multi-horizon signals into intervention decisions before execution. Experiments across four benchmarks and an online guardrail evaluation show that DreamGuard outperforms generic, reactive, and proactive guardrail baselines, achieves the best safety-utility trade-off among evaluated guardrails, and maintains an average end-to-end latency of 25 ms per call.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Document Parsing</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>PaDoc: Layout-Grounded Parallel Decoding for Document Parsing</strong>
          <small>Hao Yu, Jiabo Zhan, Kang Liu, Linnan Zhao, Dongxu Yue, Rui Chen, Jinglin Wang, Chong Sun, Chen Li, Jing Lyu, Chun Yuan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Document Parsing</span>
<span class="topic-tag">MLLM Inference</span>
<span class="topic-tag">Parallel Decoding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2608.06146</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.06146">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: proposes a new MLLM-based document parsing system with parallel decoding and vLLM-style serving.</p>
        <p class="abstract">End-to-end document parsers provide a unified interface, but serialize page layouts and regional contents into one autoregressive sequence. This formulation forces independent regions onto a decoding path whose length grows with the total content, whereas crop-based two-stage parsers expose region-level parallelism at the cost of repeated visual prefills and fragmented page context. To retain full-page context while removing dependencies, we propose PaDoc, a layout-grounded parser that treats the predicted layout as a branching structure over a shared page representation. Under a region-sufficiency assumption, we derive a prefix-conditioned factorization in which the layout stream and regional content branches advance concurrently, reducing the decoding depth to the longest layout-content path. We realize this factorization within a single MLLM: packed variable-length ancestor attention preserves the visibility under standard next-token training, while masked parallel decoding creates branches that the evaluated vLLM backend serves as concurrent requests with cache-resident shared-prefix reuse. On OmniDocBench Full, PaDoc attains an Overall layout F1 of 91.1 and, among end-to-end parsers, a top-tier Overall score of 94.24 together with the best Text Edit (0.038) and Formula CDM (95.59). On a 384-page subset and one A800 GPU, it is the fastest end-to-end parser at five concurrency levels, improving valid-page throughput by 67.4-118% and reducing P95 latency by 39.2-54.9% relative to a same-backbone Sequential SFT baseline. Code is available at https://github.com/Longin-Yu/Padoc</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Seeing Is Not Deciding: Can Multimodal LLMs Act as Effective CEOs?</strong>
          <small>Yuyang Dai, Xueqing Peng, Yuxia Wang, Preslav Nakov, Zhuohan Xie</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Benchmark</span>
<span class="topic-tag">Decision Making</span>
<span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2608.05864</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.05864">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: introduces a multimodal benchmark for frontier MLLMs acting on visual business evidence, with careful analysis of multimodal decision-making behavior.</p>
        <p class="abstract">Large language models are increasingly applied as autonomous decision-making agents. However, in executive business decisions, existing benchmarks are limited to textonly settings. This makes it unclear whether models can perceive visual business evidence and effectively integrate it to improve decision quality. We introduce C-SUITEBENCH, a controlled multimodal benchmark that includes five decision tasks under paired text-only and multimodal conditions across 50 scenarios. We place nine frontier models in the role of a chief executive officer and evaluate their decision-making ability. Multimodal inputs consistently improve evidence-centric reasoning, with the largest and most reliable gains appearing in risk forecasting and board-facing justification. However, we uncover a multimodal integration paradox: adding visual business information degrades constrained resource allocation for all nine models, even as visual grounding itself improves. Ablation experiments reveal that this failure emerges from signal crowding, although each visual channel helps individually, their combination disrupts constraint satisfaction during decoding. These findings demonstrate that visual perception and constrained action are separable bottlenecks in multimodal agents, and that indiscriminate visual augmentation can harm high-stakes decision making, motivating selective grounding strategies for future executive AI systems.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Open-Vocabulary Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>CogVis: Must Open-Vocabulary Change Detection Perceive the Scene Anew for Every Query?</strong>
          <small>Zijie Wang, Chen Zhong, Wei He</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Open-Vocabulary Detection</span>
<span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Vision Foundation Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2608.06150</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.06150">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 partially: it is a vision foundation-model application for open-vocabulary change detection, with a novel perception-memory-verification design.</p>
        <p class="abstract">Earth-surface monitoring requires change detection models capable of recognizing arbitrary semantic categories. Open-Vocabulary Change Detection (OVCD) addresses this need. However, existing methods often entangle temporal perception, semantic discrimination, and region verification, causing unstable results and redundant computation. Inspired by human visual change perception, we propose CogVis, a cognitive memory-guided framework that reformulates OVCD as a perception-memory-verification paradigm. CogVis first employs a Scene Change Perceptron (SCP) to extract a reusable, category-agnostic change prior from frozen bi-temporal features, thereby decoupling temporal evidence from semantic category decisions. A Semantic Memory Calibrator (SMC) then compensates for category-dependent score shifts by dynamically estimating an image-query-specific decision threshold. Finally, an Adaptive Region Filter (ARF) filters connected candidates using learned semantic, temporal, and structural reliability. Experiments on seven benchmarks spanning semantic change detection, binary change localization, and building-damage assessment show that CogVis achieves state-of-the-art performance across all evaluated datasets. By sharing scene-level change perception, CogVis further avoids repeating category-agnostic temporal perception across queries and improves inference throughput by 28.50%.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

        <a class="archive-link" href="past_arxiv/2026-08-06.html">
          <span>August 06, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-05.html">
          <span>August 05, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-04.html">
          <span>August 04, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-03.html">
          <span>August 03, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-31.html">
          <span>July 31, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-30.html">
          <span>July 30, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-29.html">
          <span>July 29, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-28.html">
          <span>July 28, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-27.html">
          <span>July 27, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-24.html">
          <span>July 24, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-23.html">
          <span>July 23, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-22.html">
          <span>July 22, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-21.html">
          <span>July 21, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-20.html">
          <span>July 20, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-18.html">
          <span>July 18, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-17.html">
          <span>July 17, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-16.html">
          <span>July 16, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-15.html">
          <span>July 15, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-14.html">
          <span>July 14, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-13.html">
          <span>July 13, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-10.html">
          <span>July 10, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-09.html">
          <span>July 09, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-08.html">
          <span>July 08, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-07.html">
          <span>July 07, 2026</span>
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
