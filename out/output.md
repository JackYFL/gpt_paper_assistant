

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
      <p class="eyebrow">Daily ArXiv / November 24, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>24</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>15</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>11.8</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.00rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 61%, var(--accent))" title="15 mentions">action</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="23 mentions">agent</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">annotation</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">average</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="9 mentions">change</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="10 mentions">clinical</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="9 mentions">decision</span><span class="cloud-word" style="font-size:1.66rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="12 mentions">evidence</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">execution</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="8 mentions">finding</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">five</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="9 mentions">fixed</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="10 mentions">four</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="8 mentions">generation</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="9 mentions">harness</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="9 mentions">interaction</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="8 mentions">joint</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">knowledge</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">label</span><span class="cloud-word" style="font-size:1.89rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 55%, var(--accent))" title="14 mentions">language</span><span class="cloud-word" style="font-size:1.54rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="11 mentions">layout</span><span class="cloud-word" style="font-size:2.41rem;opacity:0.91;color:color-mix(in srgb, var(--accent-2) 81%, var(--accent))" title="19 mentions">memory</span><span class="cloud-word" style="font-size:1.66rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="12 mentions">object</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="8 mentions">pretraining</span><span class="cloud-word" style="font-size:1.89rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 55%, var(--accent))" title="14 mentions">question</span><span class="cloud-word" style="font-size:2.50rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 86%, var(--accent))" title="20 mentions">reasoning</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="8 mentions">reference</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">response</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">rule</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="10 mentions">semantic</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="9 mentions">skill</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">source</span><span class="cloud-word" style="font-size:2.50rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 86%, var(--accent))" title="20 mentions">spatial</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="10 mentions">step</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">structure</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">subsequent</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="10 mentions">supervision</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">support</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="7 mentions">target</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="8 mentions">token</span><span class="cloud-word" style="font-size:2.50rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 86%, var(--accent))" title="20 mentions">video</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="10 mentions">view</span><span class="cloud-word" style="font-size:1.66rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="12 mentions">vision-language</span><span class="cloud-word" style="font-size:2.59rem;opacity:0.95;color:color-mix(in srgb, var(--accent-2) 91%, var(--accent))" title="21 mentions">visual</span><span class="cloud-word" style="font-size:1.89rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 55%, var(--accent))" title="14 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="67 mentions">action</span><span class="cloud-word" style="font-size:2.73rem;opacity:0.99;color:color-mix(in srgb, var(--accent-2) 98%, var(--accent))" title="156 mentions">agent</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="39 mentions">alignment</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="40 mentions">answer</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="41 mentions">attention</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="38 mentions">camera</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="43 mentions">change</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="31 mentions">control</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="30 mentions">detection</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="37 mentions">dynamic</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="32 mentions">embedding</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="45 mentions">environment</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="36 mentions">error</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="60 mentions">evidence</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="46 mentions">execution</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="33 mentions">fixed</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="35 mentions">foundation</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="34 mentions">four</span><span class="cloud-word" style="font-size:1.70rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="76 mentions">generation</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="41 mentions">inference</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="48 mentions">interaction</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="33 mentions">knowledge</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="49 mentions">language</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="48 mentions">latent</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="61 mentions">memory</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="41 mentions">motion</span><span class="cloud-word" style="font-size:1.33rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="54 mentions">multimodal</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="73 mentions">object</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="41 mentions">observation</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="36 mentions">pair</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="31 mentions">perception</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="39 mentions">physical</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="59 mentions">point</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="57 mentions">policy</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="32 mentions">prompt</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="52 mentions">question</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="31 mentions">real</span><span class="cloud-word" style="font-size:1.87rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="87 mentions">reasoning</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="38 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="35 mentions">reference</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="44 mentions">reward</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="31 mentions">robot</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="48 mentions">same</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="62 mentions">scene</span><span class="cloud-word" style="font-size:1.99rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 60%, var(--accent))" title="96 mentions">semantic</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="36 mentions">skill</span><span class="cloud-word" style="font-size:1.59rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="69 mentions">spatial</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="55 mentions">step</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="45 mentions">structure</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="31 mentions">success</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="42 mentions">supervision</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="48 mentions">support</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="42 mentions">target</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="39 mentions">token</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="40 mentions">trajectory</span><span class="cloud-word" style="font-size:2.10rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 66%, var(--accent))" title="104 mentions">video</span><span class="cloud-word" style="font-size:1.33rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="54 mentions">view</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="47 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="160 mentions">visual</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="47 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>18 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">3D Vision</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>3D Open-Vocabulary Detection via Visual Alignment and Generative Captions</strong>
          <small>Thomas E. Huang, Alex Zihao Zhu, Hao Xiang, Tianyi Cai, Jingwei Ji, Yuliang Zou, Jiafan Yu, Xin Huang, Mingxing Tan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Vision</span>
<span class="topic-tag">Open-Vocabulary Detection</span>
<span class="topic-tag">Vision-Language Distillation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2611.26842</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.26842">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 and partially criterion 1: it transfers VLM/MLLM semantics into 3D open-vocabulary detection via visual alignment and generative captions.</p>
        <p class="abstract">Open-vocabulary 3D object detection remains a significant challenge for outdoor scenes, with existing methods often struggling to effectively transfer the rich semantic knowledge from powerful 2D Vision-Language Models (VLMs) into a 3D context. We propose a novel, two-part framework for this task. First, we introduce a direct, object-level distillation method. We generate class-agnostic 3D proposals to source regions from the entire scene, without relying on any manual labels. We leverage a spatially-aware VLM to extract a semantic embedding from each proposal&#x27;s projected 2D bounding box and supervise our 3D model to predict this embedding on a per-instance basis. Second, to enhance zero-shot capability and inject domain-specific information, we employ a powerful Multimodal Large Language Model (MLLM) as an image captioner to generate rich textual captions for each of these proposals. These captions are integrated into the training objective to directly align the 3D features with these rich semantics, creating a composite loss that combines direct feature distillation with caption-based semantic enrichment. Our experiments validate the effectiveness of our approach, establishing a new state of the art in 3D open-vocabulary detection on the Waymo Open Dataset and nuScenes.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT</strong>
          <small>Maximilian Rokuss, Jeya Maria Jose Valanarasu, Alejandro Lozano, Benjamin Hamm, Yannick Kirchhoff, Fabian Isensee, Klaus Maier-Hein</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Agents</span>
<span class="topic-tag">Longitudinal Reasoning</span>
<span class="topic-tag">Foundation Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.MA</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2611.27876</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27876">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: a new training-free agentic method for longitudinal CT reasoning, lesion tracking, and guideline-based response assessment.</p>
        <p class="abstract">Every few months, a cancer patient&#x27;s CT scans decide whether treatment continues. 3D foundation models can now detect, segment, register and track lesions, yet none of them reads the scans as a radiologist does. A radiologist decides which findings are lesions, which are the same lesion months later and whether a new spot means progression, and checks each decision against the extensive rules of a clinical guideline. We introduce LesionAgent, an LLM agent that performs this read end to end without task-specific training. It operates frozen 3D models as tools, acts in 3D through coordinate-labelled views, remembers every lesion across visits in a registry, verifies every model output it relies on, and leaves every number to a deterministic guideline engine. On four public longitudinal CT datasets, LesionAgent tracks more lesions and measures them more accurately than every automatic baseline, and where the same 3D models chained by fixed rules call progression falsely at 33 of 56 follow-ups, it does so twice. On clinical follow-up CTs, it agrees with the radiologists&#x27; response at 20 of 23 follow-ups, including every change in response, and without training on DeepLesion, it retrieves more of its lesions than every tracker trained on it (89.0% vs. 87.4%). Its harness, not its LLM, makes the difference: given the same LLM and 3D models but not the harness, Claude Code reaches a detection F1 of 41% and LesionAgent 78%, and an open-weight LLM that can run inside the hospital rises from 6% to 73%. LesionAgent and a napari reading app for any LLM are available at https://github.com/MIC-DKFZ/LesionAgent.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>TouchBench: Can Vision-Language Models Feel Invisible Physical Properties?</strong>
          <small>Ziyao Zeng, Ziyi Kou, Chuan Qin, Mia Huang, Roger Boldu, Zhiwen Fan, Daniel Rakita, Eric Whitmire, Li Guan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI Benchmark</span>
<span class="topic-tag">Tactile Perception</span>
<span class="topic-tag">Vision-Language Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2611.26883</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.26883">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: an embodied perception benchmark combining vision-language and tactile sensing, plus a new prompting method for physical reasoning.</p>
        <p class="abstract">Vision-language models (VLMs) are increasingly used for embodied perception and reasoning, yet their physical understanding is largely evaluated on questions answerable from images. Many properties critical to manipulation, such as an opaque bottle&#x27;s fill level or an object&#x27;s compliance, may only be revealed through touch. We introduce TouchBench, an egocentric vision-language-tactile benchmark that distinguishes visually answerable questions (Tier A) from those involving properties hidden from the camera (Tier B). It pairs head-mounted video with synchronized 137-channel whole-hand tactile sensing, comprising 900 clips from five participants across 11 tasks, with 900 absolute and 4,102 relative questions. Four state-of-the-art VLMs average 66.4% accuracy on Tier A relative questions but only 49.8% on Tier B, near chance (50%). To bridge this gap, we propose Tactile-as-Prompt (TaP), which presents 34 interpretable tactile statistics as text, enabling VLMs to reason with touch without a learned tactile encoder. TaP raises zero-shot Tier B relative accuracy to 62.9% and reaches 73.1% after leave-one-user-out fine-tuning, outperforming video alone (67.4%) and a learned tactile-token encoder (67.3%). The gains extend to unseen objects and users. On a separate 20-hour in-the-wild corpus, tactile text improves fine-tuned contact-question accuracy from 67.1% to 75.5%. These results highlight the limits of vision-only physical reasoning and establish language as an effective interface for tactile perception.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Zing-1.0: A Playable World System Built on Controllable Rendering</strong>
          <small>Wenbo Zhang, Guoli Zhang, Xuewen Yu, Xueliang Yang, Jiangqiao Yan, Teng Xia, Xinmiao Wu, Zeyang Tian, Haoze Sun, Jinghui Niu, Hongli Ning, Zhiyuan Liu, Xinna Liu, Weimin Liu, Jialin Liu, Tianpeng Li, Kejun Li, Jun Li, Jiawen Li, Yirong He, Haoyuan Guo, Bosheng Gong, Junhao Gao, Xiaoxiao Fu, Xuezhi Chen, Shengdong Chen, Mingyang Chen, Diying Chen, Yinglun Chai, Yiwen Cai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Playable World Models</span>
<span class="topic-tag">Controllable Rendering</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2611.27336</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27336">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it proposes a new embodied/world system and simulator-like playable environment with controllable rendering and interaction runtime.</p>
        <p class="abstract">We present Zing-1.0, a Playable World System built on Controllable Rendering. An executable engine resolves player actions under the world&#x27;s rules and produces proxy video from the updated state. A streaming video model synthesizes the player&#x27;s view from this proxy, and the runtime delivers it to inform subsequent actions. (1) Principle and system. We formulate Controllable Rendering and define the interfaces among world construction, world execution, observation synthesis, and the interaction runtime. To our knowledge, this is the first implementation-independent specification of a Playable World System. (2) AI-native engine. WorldKit provides structured authoring tools and reusable character, camera, and control components for coding agents to construct executable proxy worlds. It supports extensible interactions and precise geometric motion control while separating executable behavior from final visual appearance. (3) Streaming renderer. We adapt MiniMax-H3 for block-causal autoregressive generation and incremental decoding. Proxy video constrains structure and motion, while text and separate scene and subject references specify appearance. We train the generator on diverse tasks and distill it to generate each block in a few denoising steps. The renderer leads the compared streaming editors on OpenVE (3.90) and LongV2VBench (3.44). On StreamEval, Zing-1.0 scores 57.86 on instruction editing and 54.06 on reference editing, exceeding the published baselines on both tracks. (4) Interaction infrastructure. We build an Interaction Runtime that routes player actions to WorldKit while supporting in-play prompt and reference updates. Cross-block joint execution and sparse attention with compressed K/V reduce inference overhead. With the DiT on a single H200 and encoding and decoding on one H100 each, the serving system achieves a steady-state throughput of 23.82 FPS at $832\times480$.</p>
      </div>
    </details>


    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Taking Apart and Putting Together: Tracking Objects Through Physical Transformations</strong>
          <small>Davide Gardenal, Mingxuan Liu, Flavio Vella, Quentin Guimard, Elisa Ricci</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Video Object Tracking</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2611.27398</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27398">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it introduces a new embodied/interactive vision benchmark for tracking objects through physical transformations, plus a method that handles assemblies and disassemblies.</p>
        <p class="abstract">We introduce Transformation Tracking and Understanding (TTU), extending video object tracking to environments where objects undergo physical assemblies and disassemblies. TTU requires continuously tracking objects through transformations, identifying new entities, maintaining a state graph of their relationships, and assigning semantic labels to transformations. While foundation models (e.g., SAM 2/3) maintain tracklets through appearance changes, they cannot update semantic identities as objects physically evolve. Prior work addresses only disassemblies, relying on expensive searches triggered only when tracking fails. We propose Tracking Instances via Proposals and Overlaps (TIPO), a training-free framework that continuously infers transformations via a generate-evaluate-judge pipeline. TIPO generates split and merge proposals from disjoint mask components, scores them against mask-decoder priors using inner and external overlap, and queries an MLLM on the top proposal for visual verification and semantic labeling. To benchmark TTU, we curate Video Instances, States, and Transformation Annotations (VISTA), a dataset including state graphs with 124 assembly and 132 disassembly events across 50 sequences and over 26,000 frames. TIPO achieves state-of-the-art tracking and state-graph accuracy on VISTA, while operating $6\times$ to $15\times$ faster than prior methods. Project page: https://davidegardenal.github.io/tipo-tracking</p>
      </div>
    </details>


    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>SCAP: Stochastic Context for Action Expert Pretraining</strong>
          <small>Xiao Lin, Yaoxu Lyu, Ronghao Dang, Zhili Liu, Kaijing Ma, Yang Zhou, Dingning Liu, Runzhe Teng, Jun Cen, Shanghang Zhang, Chengju Liu, Qijun Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Robot Manipulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2611.27187</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27187">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: a new method for vision-language-action pretraining aimed at embodied manipulation, with real-robot results.</p>
        <p class="abstract">Single-modality action-expert pretraining controls competition from visual shortcuts before vision--language--action (VLA) adaptation. Yet single-modality pretraining can impair the vision--language interactions needed for subsequent joint prediction. We construct a diagnostic model in which VA or LA pretraining can disable an initially active pathway for joint vision--language modeling. In this model, subsequent training with complete visual and language inputs cannot restore the pathway, even with unlimited adaptation. We therefore introduce Stochastic Context for Action Expert Pretraining (SCAP), a new action-expert pretraining stage that precedes full-input training. During this stage, visual and text tokens are randomly masked before entering the VLM. In this unified diagnostic model, SCAP can preserve the joint vision--language modeling pathway during pretraining and subsequent full-input training. Compared with direct full-input training, it can also reduce reliance on visual shortcuts and increase reliance on language instructions. SCAP consistently improves performance across four different VLA architectures. In real-robot experiments, it achieves 76.67% average success across three instruction-conditioned manipulation tasks, outperforming full-input pretraining by 25 percentage points.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>ENC-QA: A Diagnostic Benchmark for Vision-Language Models on Electronic Navigational Charts</strong>
          <small>Jiyoon Pyo, Jacob Arndt, Yao-Yi Chiang, Dalton Lunga</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2611.27858</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27858">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 3: a new diagnostic benchmark for VLMs on nautical charts, emphasizing spatial reasoning and safety-critical chart change assessment.</p>
        <p class="abstract">Nautical charts encode safety-critical maritime information through standardized symbols, attributes, text, and heterogeneous geometries. Interpreting these charts and assessing the navigational significance of successive chart updates requires recognizing nautical features, determining their spatial relationships, and applying navigational knowledge. Vision-language models (VLMs) offer a promising approach to nautical-chart interpretation, yet systematic evaluation of their fine-grained nautical feature recognition, chart-based spatial reasoning, and application of navigational knowledge to assessing chart changes remains limited. We introduce ENC-QA, a diagnostic benchmark comprising 77,312 questions derived from 6,612 National Oceanic and Atmospheric Administration (NOAA) Electronic Navigational Charts (ENCs). The benchmark evaluates four complementary capabilities: ENC Perception, Spatial Reasoning, Joint Perception and Spatial Reasoning, and Application. Of these, 8,227 questions form a progressive subset that decomposes selected chart-change cases into linked questions progressing from change detection to criticality assessment, enabling case-level analysis of how models use perceptual and spatial evidence to determine the navigational significance of chart changes. Evaluations of 10 open-weight VLMs reveal substantial limitations in fine-grained nautical feature recognition and feature-grounded spatial reasoning. Controlled evidence interventions show that relevant perceptual and spatial information improves change-criticality accuracy. Our findings establish ENC-QA as a diagnostic resource for nautical-chart understanding and safety-critical navigational decisions. We will release the benchmark and evaluation code upon publication.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Foundation Model</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>EchoAlign: Echocardiography foundation model with multilevel report alignment</strong>
          <small>Ahmed Aly, Darya Taratynova, Lotfi Abdelkrim Mecharbat, Roman A. Sandler, Joseph Z. Sokol, Joshua Penn, Klaus H. Maier-Hein, Numan Saeed, Mohammad Yaqub</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Foundation Model</span>
<span class="topic-tag">Medical AI</span>
<span class="topic-tag">Report Alignment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2611.27517</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27517">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: a vision-language foundation model for echocardiography with multilevel report alignment and large-scale pretraining.</p>
        <p class="abstract">Echocardiography assesses the structure and function of the heart. Cardiologists read each study across several standard views and report the findings visible in those views by cardiac structure. AI foundation models can learn to analyze these studies from clinical reports, reducing annotation burden and supporting clinical interpretation. However, existing models are trained by pairing each video with the full clinical report, including structures and findings its view does not show. This mismatch lets a model associate a finding with incidental or spurious signals rather than its visual evidence, which limits accuracy, anatomical grounding and clinical trust. Here we introduce EchoAlign, a vision-language foundation model developed on 2.87 million echocardiographic videos and images from 159 clinical centers. EchoAlign aligns each cardiac structure, video and study with its report text, and a visibility matrix restricts supervision to the views that actually depict each structure. We compare it with five public foundation models on 0.47 million test videos across ten unseen external datasets from more than 25 clinical centers. EchoAlign achieves the highest mean AUROC of 0.890 (95% CI, 0.881 to 0.897) for classification and the highest mean quadratic weighted kappa of 0.530 (95% CI, 0.511 to 0.544) for severity grading. Across 62 clinical findings, EchoAlign provides one model that detects findings, grades their severity, estimates measurements and segments cardiac structures.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Spatial Query Execution as Verifiable Rewards for Multi-step Spatial Reasoning</strong>
          <small>Jiyoon Pyo, Dongwon Jung, Zekun Li, Nayeon Kim, Muhao Chen, Yao-Yi Chiang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">RLVR</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2611.26787</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.26787">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: it proposes a method for multi-step spatial reasoning in LVLMs using spatial query execution and verifiable rewards.</p>
        <p class="abstract">Large vision-language models (LVLMs) remain unreliable on spatial reasoning problems that require composing grounded relations across multiple objects. Yet, scaling reasoning supervision is challenging since human-annotated visual datasets often rely on fixed relational annotations and coarse object localization, making it difficult to obtain precise intermediate reasoning states across diverse spatial configurations and complexities. We introduce FARON (Fully Automated Reasoning Over spatial relatioNs), a framework that executes spatial queries to provide both execution-grounded reasoning supervision and verifiable outcome rewards. Rather than relying on existing annotated data, FARON constructs synthetic 2D and 3D scenes with explicit geometries, enabling configurable object arrangements, spatial relations, and multi-step compositions. Deterministic query execution yields intermediate sets and final answers, providing precise supervision without manual relation annotation. Our pipeline converts intermediate states into natural-language reasoning traces for supervised fine-tuning (SFT), while the execution-derived answers provide verifiable rewards for reinforcement learning with verifiable rewards (RLVR). Controlled experiments show that trace-based SFT improves multi-step spatial reasoning over final-answer supervision and that subsequent group relative policy optimization (GRPO) provides further gains. The resulting models also demonstrate transfer across external spatial reasoning benchmarks and multiple LVLM backbones without benchmark-specific fine-tuning. These results show the potential of using spatial query execution as a unified, flexible source of reasoning supervision and verifiable outcome rewards for multimodal spatial reasoning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>ReactDrive: Self-Reactive Driving World Model</strong>
          <small>Yifan Wang, Xiaoqi Wang, Cho-Ying Wu, Wenbin He, Chenyu You, Liu Ren</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Embodied Simulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2611.27024</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27024">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a new embodied-driving world model benchmarked on reactive agent dynamics and visual future generation.</p>
        <p class="abstract">The world evolves through the dynamics of its constituent entities and their interactions, with changes in one entity influencing the behavior of others. To simulate this evolution under different actions, interactive world models need to capture the resulting agent responses as part of the world&#x27;s own dynamics. In autonomous driving, errors in modeling these responses can misrepresent maneuver safety and undermine the reliability of generated videos used for policy evaluation and learning. To formalize this intrinsic requirement for driving world model, we define self-reactivity as the capability to model agent responses from observed history and a specified ego action, and generate visual futures that reflect those responses without prescribed future agent trajectories. To realize this capability, we introduce ReactDrive, a driving world model that jointly learns agent dynamics and visual generation through a shared agent state representation. Within this framework, dynamics supervision grounds a reactive dynamics prior in observed agent states, while the video objective jointly optimizes the self-reactivity and visual realism. Experiments show improved agent responses, ego controllability, and video quality, a 96.0% preference for agent reactivity in human comparisons across five baselines, and better downstream planning through augmentation with generated videos. We hope this work encourages the community to recognize self-reactivityas a foundational capability for developing and evaluating interactive world models. Project page: https://reactdrive.github.io/ .</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>PhiJEPA: Denoising Latent Predictions for Visual Representation Learning</strong>
          <small>Makoto Yamada, Yao-Hung Hubert Tsai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">World Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">stat.ML</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2611.27516</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27516">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it studies a vision foundation model style representation learner and shows an application to occluded visual completion in a world-model/planning setting.</p>
        <p class="abstract">Can a predictor trained to infer hidden image regions still help a world model plan when part of an object disappears from view and the visible context is blurred? We introduce PhiJEPA, a joint-embedding predictive architecture that adapts PhiNet&#x27;s two-stage prediction to masked Transformers. From sparse, photometrically corrupted context, a Transformer block predicts hidden tokens of an independently corrupted teacher view. A token-wise MLP then maps these predictions to clean teacher tokens. Controlled ablations show that the combined objective improves dense features over the tested one-stage alternatives. Pre-trained on ImageNet-1K with $5.6\times10^{19}$ training FLOPs, PhiJEPA achieves 69.3 mIoU on linear PASCAL VOC segmentation, exceeding the evaluated I-JEPA and DSeq-JEPA checkpoints in segmentation accuracy, with 25\% fewer training FLOPs than I-JEPA. It also improves hidden-region segmentation over Simple I-JEPA (49.1 vs.\ 44.3 mIoU). As an application, we use the frozen encoder in DINO-WM on PushT, and reuse the pre-training predictor, which JEPAs usually discard, to complete occluded tokens without fine-tuning. In open-loop planning with simultaneous object occlusion and Gaussian blur ($\sigma=2$ pixels), predictor completion raises success from 33\% to 65\%, compared with 25\% for Simple I-JEPA with its predictor and 40\% for iBOT with pixel inpainting. Together, these results support two-stage latent prediction as an efficient approach to learning visual representations that remain useful under photometric degradation and support completion under partial observation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal LLM</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Automating Multi-View Quality Assessment of 3D Annotation Layouts</strong>
          <small>Hongyi Yang, Jinao Wu, Yanwei Zhang, Shengwen Fu, Haibin Ling, Bingyao Huang, Jingwei Qu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLM</span>
<span class="topic-tag">3D Visualization</span>
<span class="topic-tag">Quality Assessment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2611.27621</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27621">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: it uses an MLLM for multi-view quality assessment, with a new benchmark for 3D annotation layout evaluation.</p>
        <p class="abstract">Text labels provide descriptive information about elements in visual scenes. In 3D visualization, the arrangement of these labels and their connections to target locations forms an annotation layout. Assessing layout quality supports comparisons between alternative layouts. However, existing quality measures often focus on specific layout properties and may not fully reflect human judgments of overall quality. Moreover, a layout may appear clear from one viewpoint but suffer from occlusion or clutter from another. To address these issues, we propose a multi-view quality assessment method based on a multimodal large language model (MLLM). We fine-tune a compact MLLM using structured supervision from human ratings to predict a rating for each quality dimension in each view. These ratings are aggregated into view-level and sample-level quality scores. To support training and evaluation, we construct the Annotation Layouts with Quality Assessment (ALQA) dataset, containing 3,216 layout samples from 1,072 3D objects across 13 categories. Each layout is rendered from 5 predefined viewpoints, and each view is independently rated by 3 human raters across 5 quality dimensions. On ALQA, our method agrees more closely with human reference scores than the evaluated MLLM baselines, and a user study demonstrates strong agreement with human preferences in layout ranking.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Remote Sensing Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>RemoteEvolver: Expanding Earth Observation Capabilities through Agent Harness Evolution</strong>
          <small>Shengxiang Xu, Liang Yao, Shuyi Chen, Yishu Wang, Shimin Di, Fan Liu, Bishun Yao, Hanghui Guo, Xinyu Liu, Chengye Liang, Yuyu Luo, Min-Ling Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Remote Sensing Agents</span>
<span class="topic-tag">Tool Learning</span>
<span class="topic-tag">Continual Adaptation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2611.27110</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27110">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately well: an embodied/agentic remote-sensing system with evolving tools and workflows, though it is more remote sensing than classic embodied AI.</p>
        <p class="abstract">We are interested in developing a continually self-improving remote sensing agentic system. It should identify and address its capability gaps, retaining the resulting improvements to enhance performance on subsequent tasks. However, existing systems typically rely on fixed toolsets and confine their experience accumulation to re-orchestrating predefined capabilities, constraining both capability expansion and the transfer of improvements across tasks. As the infrastructure for agentic systems, the harness manages tools and workflow knowledge as editable, persistent resources outside the base model. These resources can therefore be updated and reused across tasks without additional post-training. Based on these observations, we propose RemoteEvolver, an external harness for remote sensing agents that drives tool and workflow evolution through execution feedback. With the base model parameters fixed, RemoteEvolver acquires missing specialized tools on demand and distills verified successful execution experience from individual tasks into agent skills that can be reused across tasks. The acquired tools and accumulated skills jointly support planning and execution on subsequent tasks. Experiments on Earth-Bench and OpenEarthAgent-Bench show that RemoteEvolver achieves average accuracy gains of 8.18 and 23.86 percentage points over its initial state when tools are fully available and partially missing. Under the same settings, it also outperforms the state-of-the-art methods by an average of 6.77 and 17.10 percentage points, respectively.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Understanding</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>VMSA: Video Memory Skill Agent for Long Video Understanding</strong>
          <small>Changin Choi, Jungwon Park, Jungmin Ko, Jimyeong Kim, Wonjong Rhee</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Understanding</span>
<span class="topic-tag">Memory-Augmented Agents</span>
<span class="topic-tag">Long-Context Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 20 / arXiv:2611.27381</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27381">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Partial match to criterion 4: it is a video understanding system built around structured memory and agent skills, but it is more a long-video QA method than a core vision foundation model paper.</p>
        <p class="abstract">Long-video question answering requires retrieving and integrating relevant evidence from videos spanning hours or even days. Recent agentic approaches organize video information into external memories and iteratively retrieve evidence to answer questions. However, effective retrieval and reasoning remain challenging, as agents must determine what information to search for, which memory sources to access, and how to connect evidence across distant temporal intervals. To address these challenges, we propose Video Memory Skill Agent (VMSA), a framework that jointly designs structured video memories and memory skills for long-video understanding. VMSA constructs three complementary memory components. Segment Caption Memory and Entity Event Memory serve as searchable evidence sources, while Entity-Aware Episode Memory provides broad yet detailed video context to guide evidence retrieval and reasoning. To further support effective memory utilization, VMSA induces memory skills from successful agent trajectories, incrementally refining or extending a compact skill library to guide iterative evidence retrieval, reasoning, and verification. Across seven long-video question-answering benchmarks, VMSA achieves the highest accuracy on all three week-long egocentric benchmarks, outperforming the strongest baseline by up to 9.4% on Ego-R1 Bench, and the best or competitive performance on four additional benchmarks. Ablation studies further demonstrate the contributions of all three memory components and memory skills, with memory skills also improving temporal evidence localization.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Document AI</summary>
      <div class="queue">

    <details class="paper-row" id="link20">
      <summary class="paper-row-summary">
        <span class="queue-index">21</span>
        <span class="paper-row-copy">
          <strong>SAVIOR: Sample-efficient Adaptation of Vision-Language Models for OCR Representation</strong>
          <small>Akshata A Bhat, Sharath Naganna, Saiful Haq, Prashant Khatri, Krishna Chaitanya Reddy Tamataam, Neha Arun, Niyati Chhaya, Pushpak Bhattacharyya</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Document AI</span>
<span class="topic-tag">OCR</span>
<span class="topic-tag">Vision-Language Adaptation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 21 / arXiv:2611.27319</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27319">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: vision foundation model adaptation for OCR-heavy document understanding, with a sample-efficient curation method and new evaluation metric.</p>
        <p class="abstract">Optical Character Recognition (OCR) pipelines and vision-language models exhibit high accuracy on standard OCR and document-understanding benchmarks, yet they systematically underperform on document patterns that are operationally critical in financial workflows. These patterns include vertical or rotated text, logo-embedded vendor names, fine-print regulatory clauses, degraded scans, and complex multi-column layouts. While underrepresented in public datasets, they constitute a substantial portion of real-world failure cases. We introduce SAVIOR, a sample-efficient data curation methodology that targets such high-impact failure scenarios to adapt vision-language models for robust financial OCR. We further propose PaIRS, a structure-aware evaluation metric that measures layout fidelity by comparing pairwise spatial relationships between tokens. Fine-tuning Qwen2.5-VL-Instruct with SAVIOR-Train achieves a word recall of 0.93. When the resulting layout-aware OCR output is used as context for document question answering, it attains an F1 score of 0.89, outperforming both open- and closed-source models such as GPT-4o, Mistral-OCR, PaddleOCR-VL, and DeepSeek-OCR.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link21">
      <summary class="paper-row-summary">
        <span class="queue-index">22</span>
        <span class="paper-row-copy">
          <strong>PaMuk-Bench: A Parallel Multilingual Multitask Benchmark for Vision-Language Tasks</strong>
          <small>Silviu-Florin Gheorghe, Radu-Stefan Popa, Adriana Valentina Costache, Adrian-Gabriel Chifu, Alessia Amelio, Paul Irofti, Anders Skaarup Johansen, Lallouani Bouchakour, Mohamed Lichouri, Khaled Lounnas, Neelu Madan, Yashvir Malik, Radu Tudor Ionescu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Benchmark</span>
<span class="topic-tag">Multilingual Learning</span>
<span class="topic-tag">Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 22 / arXiv:2611.27521</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27521">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a new multilingual vision-language benchmark for multiple VLM tasks, useful for evaluating vision foundation models across languages.</p>
        <p class="abstract">While vision-language models (VLMs) currently obtain notable results for highly-studied languages, e.g. English, they exhibit significant performance drops in certain low-resource languages, especially due to the lack of annotated datasets. To this end, we propose PaMuk-Bench, a novel parallel multilingual multitask benchmark for vision-language tasks. Our benchmark includes a set of over 10K curated English prompts that are translated into six languages: Arabic, Danish, French, Hindi, Italian, Romanian. Parallel translations, which are obtained via a semi-automatic process, along with accompanying generated and retrieved images enable the comparative development and evaluation of VLMs across a wide range of tasks: text-to-image generation, image captioning, content-based image retrieval, image generation difficulty estimation, image retrieval difficulty estimation. We empirically show that zero-shot English and multilingual pre-trained VLMs compare consistently worse than their fine-tuned counterparts, confirming that PaMuk-Bench is a valuable resource that can drastically reduce the language gap across a variety of VLM architectures and tasks. PaMuk-Bench is available at https://github.com/ghesil/pamuk_bench.</p>
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
          <strong>Towards Text-Mask Consistency in Medical Image Segmentation</strong>
          <small>Jie Gui, Hang Tu, Wen Sha, Xiuquan Du</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Vision-Language</span>
<span class="topic-tag">Segmentation</span>
<span class="topic-tag">Cross-Modal Alignment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 23 / arXiv:2611.27050</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27050">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 only loosely: it is a vision-language model method, but the task is medical image segmentation rather than a new VLLM/MLLM foundation model direction.</p>
        <p class="abstract">Vision-language models for medical image segmentation often produce masks that conflict with the accompanying text, especially under multi-site/multi-lesion descriptions. We trace this failure to two factors: (i) highly templated and repetitive clinical language causes one-to-one hard contrastive learning to yield numerous false negatives, weakening cross-modal alignment; and (ii) predominantly vision-driven, one-way cross-attention lacks a language-dominant, spatially aware pathway, hindering effective injection of textual semantics into the spatial visual domain. To this end, we propose Consistency-enhanced Two-stage Segmentation (C2Seg). In the pretraining stage, Cluster-aware Contrastive Learning uses a frozen strong baseline to construct an intra-batch text similarity matrix as soft labels, thereby alleviating false negative conflicts and producing more discriminative visual representations. In the fusion stage, we introduce a Bidirectional Complementary Attention Module, where each modality dominates attention along its own path, fostering deep interaction and structural consistency between visual and textual representations. In order to enhance the expressive power of multimodal features, we further adopt KAN-based Attention Gating. Without updating the language encoder, our approach significantly improves text-mask consistency and segmentation accuracy on four public medical imaging datasets. The source code is available at https://github.com/JGuiidev/C2Seg.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Skeleton Action Recognition</summary>
      <div class="queue">

    <details class="paper-row" id="link23">
      <summary class="paper-row-summary">
        <span class="queue-index">24</span>
        <span class="paper-row-copy">
          <strong>Crafting the Difference, Grounding the Evidence: Discriminative Concept Learning for Zero-Shot Skeleton Action Recognition</strong>
          <small>Siyu Zhu, Feng Ding, Zixiao Jin, Kaizhi Li, Xin Dong, Haisheng Fu, Yuchen Zou, Guohe Zhang, Jie Liang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Skeleton Action Recognition</span>
<span class="topic-tag">Zero-Shot Learning</span>
<span class="topic-tag">Vision-Language Alignment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 24 / arXiv:2611.27135</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27135">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; it is a skeleton action recognition method using LLM-generated concepts, but it is not really about embodied agents or a new VLLM/MLLM.</p>
        <p class="abstract">LLM-generated descriptions enrich zero-shot skeleton-based action recognition but repeat cues shared by confusable actions. Their contextual semantics also lack explicit links to skeleton features. To address these challenges, we propose CRAFT, which couples Concept Refinement and Feature-grounded Tokens. Hard-negative-conditioned generation and contrastive scoring identify concepts that distinguish each action from its closest rivals. Unique-QDPP selects complementary descriptions within each semantic slot and prevents their reuse across slots. This bank supervises learnable concept tokens that read motion and context cues from each skeleton. On fixed NTU-60 and NTU-120 splits, CRAFT improves five baselines spanning four recognition paradigms. ZSL accuracy and GZSL harmonic mean increase on every baseline-split pair, by 5.4 and 5.9 percentage points on average. Random-split experiments extend these gains to three datasets, including PKU-MMD. Code will be released after acceptance.</p>
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
      <summary class="topic-heading">Agentic Benchmarks</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?</strong>
          <small>Chuan Xiao, Baojie Wang, Haizhao Fan, Hongzhe Du, Xander Xu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agentic Benchmarks</span>
<span class="topic-tag">LLM Researchers</span>
<span class="topic-tag">Tool-Using Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2611.27116</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27116">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: a new benchmark for evaluating recursive co-evolution of agentic systems, with an agent/research harness setup and domain-specific testbed.</p>
        <p class="abstract">The performance of an LLM agent depends on both its model and its harness, the code that mediates its interaction with tools and environments. Can LLM researchers drive this co-evolution as a recursive improvement process, deciding round after round which component to change when each change alters the value of the other? Existing benchmarks evaluate post-training or data research with the harness out of scope, or harness optimization with the model fixed, leaving this joint decision unmeasured. We introduce CoEvoBench, a benchmark that evaluates LLMs as researchers co-evolving the model and harness of a target agent across five agentic domains. Researchers start from a common base model and initial harness, train and revise within a 24-hour budget, and submit a model-harness pair that is scored on separate test tasks. Across five frontier researchers, the strongest closes more than four fifths of the gap to an instruction-tuned reference system, and co-evolution succeeds on interaction tasks but rarely on long-horizon coding. These results suggest that current LLMs can make a strong first improvement, but cannot yet turn feedback from an improved system into the next one. CoEvoBench provides a controlled testbed for measuring the research capabilities that recursive co-evolution requires.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Process Reward Models</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Decision Models Are General-Purpose Process Reward Models</strong>
          <small>Jiajun Fan, Qinglong Zheng, Ziwen Wang, Bangji Yang, Neil He, Ruihan Guo, Chaoran Cheng, Ge Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Process Reward Models</span>
<span class="topic-tag">Reinforcement Learning</span>
<span class="topic-tag">Embodied Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2611.27068</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27068">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it introduces a new training method for process reward models in embodied/task environments like ALFWorld and WebShop.</p>
        <p class="abstract">Reinforcement learning (RL) from verifiable outcomes gives a language agent one reward per episode: every step is credited alike, and nothing about the task is learned when all rollouts fail. The last mile, step-level credit, usually requires step labels, a learned critic, costly LLM judges or hand-written rules. We introduce DM-PRM, which turns a general-purpose decision model -- one answering yes/no questions with probabilities -- into a general-purpose process reward model (PRM), zero-shot: no step labels, no fine-tuning, no critic. DM-PRM asks one question per step and adds the standardised answers to the advantage. It plugs into any policy-gradient method; one model, with one question text per environment, serves household tasks, web shopping and multiple RL methods. With Qwen2.5-1.5B it lifts GRPO by over twenty points on ALFWorld and over ten on WebShop, overtakes GiGPO on ALFWorld and learns in far fewer iterations; it also improves GiGPO and GraphGPO on both benchmarks and reaches the highest success of our comparison, ahead of critic-based PPO and of state-of-the-art GiGPO, HGPO and GraphGPO. Its scores locate useful steps in failed rollouts, and trained agents drop idle actions and explore instead of circling. DM-PRM shows that step credit need not be learned: it can be asked for.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation</strong>
          <small>Yalin Yang, Xiao Huang, Yanan Wu, Hao Yang, Ryan Zhenqi Zhou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Parameter-Efficient Fine-Tuning</span>
<span class="topic-tag">Weight-Space Editing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2611.27089</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27089">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: it studies spatial reasoning and compares weight-space programming versus low-rank adaptation on spatial tasks, with insightful empirical trade-offs.</p>
        <p class="abstract">Weight-space programming lets a language model inspect and edit another model&#x27;s weights, offering an alternative to gradient-based adaptation. We evaluated both approaches using Qwen3.5-0.8B on a fixed reference-frame task (128 items), StepGame (200 items), and two untrained distance-comparison tasks. With thinking enabled, the public patch (p50c) raised mean accuracy from 0.0% to 22.1% on the reference-frame task and from 19.2% to 33.7% on StepGame across three sampling seeds. Randomly permuting its weight change removed the gain. Further closed-form edits did not improve on p50c, whereas a rank-1 LoRA adapter trained on worked solutions reached 100% and 98.8%, respectively, with 0.09% trainable parameters. Removing the worked solutions from supervision prevented the adapter from passing the learning gate. The trained adapters reached 82% accuracy on unseen StepGame sentence templates, 42% on held-out difficulty levels 6-10 after training on levels 1-5, and 33-50% on unseen heading-answer combinations. Their target gains coincided with a sharp decline on the distance tasks: accuracy fell from 94% and 92% under p50c to 0-2%, and their outputs applied the StepGame solution template to distance questions. With thinking disabled and reasoning requested in the visible answer, the base model also solved the distance tasks while remaining weak on the target tasks. The comparison reveals a trade-off between improving spatial task performance and preserving neighbouring skills: the public edit restored completion while preserving distance performance, whereas supervised adaptation produced much larger target gains together with interference across tasks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>WePM: Hierarchical Conflict Reconciliation for Unified MLLMs</strong>
          <small>Zhiqiang Yuan, Qiwei Yan, Liwei Yang, Jinzhe Liu, Yang Liu, Zhongyan Hou, Liyan Xu, Peixiang Luo, Jiapei Zhang, Ying Deng, Jie Zhou, Jinchao Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM</span>
<span class="topic-tag">Model Compression</span>
<span class="topic-tag">Multitask Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2611.27365</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27365">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: this is a new unified MLLM family with multi-granularity visual budgeting and multitask optimization for visual-language capabilities.</p>
        <p class="abstract">Bringing multimodal intelligence from the cloud to users&#x27; devices keeps sensitive data local and reduces inference cost, but deploying a specialized model per capability duplicates vision-language capacity under tight memory and compute budgets. We formalize heterogeneous capability density (HCD), measuring how broadly and effectively a model serves heterogeneous task families per unit of resident inference memory. High HCD across representation, generation, and decision raises two challenges: these capabilities need visual evidence at different spatial granularities under a fixed token budget, and separately collected task corpora yield conflicting updates to shared parameters, while cross-task paired supervision is costly and ambiguous for open-ended inputs. We present WePM, a family of pocket models unifying representation, generation, and decision within one vision-language backbone. Multi-Granularity Visual Budgeting (MGVB) allocates a fixed visual-token budget across global, regional, and fine-grained banks; Unified Listwise Knowledge Distillation (ULKD) enriches separately collected data with soft teacher guidance, avoiding cross-task paired annotation; Stable and Efficient Multitask Optimization (SEMO) regulates each task&#x27;s contribution through explicit loss weights and exposure schedules, with sequential gradient accumulation under memory constraints. In the joint representation-generation setting, WePM outperforms all baselines across five evaluation groups, raising the Joint score from 38.15 to 52.74. In single-task evaluation, WePM-4B attains the best average score over 30 embedding, 39 generation, and seven typed-decision benchmarks (72.86, 62.41, 61.11). Against the separate-model stack with the highest HCD, WePM achieves slightly higher balanced performance with 61.9% less resident weight memory, a 2.64-fold higher HCD.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>Bel: Step-Level Policy Improvement of Visual Agents Without Training</strong>
          <small>Jiajun Fan, Ziwen Wang, Zhaoyu Zhu, Changyi Yang, Neil He, Chaoran Cheng, Ge Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">GUI Agents</span>
<span class="topic-tag">Decision-Time Reranking</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2611.27222</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27222">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: it targets step-level policy improvement for visual agents acting in GUI/robotic settings, which is a spatially grounded embodied-agent method.</p>
        <p class="abstract">A visual agent acts on what it sees: it taps and types on a screen, or points on a camera image to show a robot where to act. One wrong step can fail its task, yet the right action is often among its own samples, passed over by its greedy decode. Choosing it is a visual judgment, since an action is best judged where it acts, not by its text or coordinates alone: as text, a tap is two numbers; drawn on the screen, it is the Post button of an empty draft. We find that this is decisive: given the screenshot and a tap&#x27;s coordinates, a decision model chooses among GUI-R1-3B&#x27;s samples significantly worse on average than when the tap is drawn where it lands. Bel turns this finding into a method that trains nothing and needs only a frozen policy&#x27;s samples and an image on which each action can be drawn. It marks each candidate on its own copy of the image it acts on, asks a decision model for the probability that executing it is the right decision, so that every kind of action shares one scale, and acts on another candidate only when greedy scores below a threshold and trails it by a margin. On recorded GUI steps, for each of three policies, Bel significantly beats greedy decoding on mobile, web and desktop screens alike and, on the same candidates, gives each a significantly higher mean step success than voting, CATTS, the trained GUI-Critic-R1 and two prompted Qwen3-VL judges shown the same marks; it also significantly improves the much larger Qwen3-VL-235B-A22B on every step-level test set. With GUI-R1-3B&#x27;s thresholds unchanged, Bel significantly raises live AndroidWorld and MiniWoB++ task success for two other policies and robot-pointing success for three policies on each of two groups of benchmarks. Judging each action where it acts thus gives step-level policy improvement of visual agents without training, with significant gains for GUI agents and robot pointing.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Probabilistic Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>Double counting in LLM evidence fusion: exact posteriors separate rule compliance from posterior gain</strong>
          <small>Tengfei Shao, Asma Rezaei, Ali Reza Kamali</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Probabilistic Reasoning</span>
<span class="topic-tag">Calibration</span>
<span class="topic-tag">Evidence Fusion</span>
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
          <span>Paper 19 / arXiv:2611.27138</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.27138">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Relevant to the friend’s interest in clever statistical tricks, but does not directly match a listed criterion; it focuses on evidence fusion calibration and exact posteriors.</p>
        <p class="abstract">Language models fuse reports in retrieval, multi-agent consensus and agent memory, where treating shared-source reports as independent can double count evidence. A common remedy is an instruction to count each source once. Its value depends on the receiver&#x27;s raw baseline. Pricing it needs an exact reference. We build the graded-dependence exact reference: binary worlds with single-report reliability 0.65 and four dependence levels, whose disclosed parameters give every world an exact posterior and every rule a target risk. The paired gain protocol scores raw and instructed answers of four configurations on 2,976 worlds. Agreement and gain separate in both directions. At $\delta$ = 0, claude-opus-5-5 and gpt-6.1-sol agreed with the rule within 0.001 in 744 of 744, and the instruction raised their posterior mismatch by 0.044; gpt-6-luna agreed in 165 of 744 and gained 0.0140 (95% interval 0.0064 to 0.0219); claude-haiku-5-5&#x27;s gain moved from -0.0295 ($\delta$ = 0) to +0.0302 ($\delta$ = 1) (descriptive). The prespecified first-child endpoint contrast, gain at $\delta$ = 1 minus $\delta$ = 0, was 0.0342 (0.0303 to 0.0382). In the preregistered tests, the raw source-weight contrast was positive (0.259, 95% interval 0.182 to 0.337; Holm rejected zero) and the grouping endpoint difference was not detected (0.0004, -0.0023 to 0.0031). This interval excludes differences larger than 0.0031 in magnitude and lies within the registered precision bound of $\pm$0.0046. The reference prices the rule before any model call. The paired gain, estimable as a Brier difference on labelled deployment items, decides adoption per receiver and prompt condition.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

        <a class="archive-link" href="past_arxiv/2026-11-20.html">
          <span>November 20, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-19.html">
          <span>November 19, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-18.html">
          <span>November 18, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-16.html">
          <span>November 16, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-14.html">
          <span>November 14, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-11.html">
          <span>November 11, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-09.html">
          <span>November 09, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-06.html">
          <span>November 06, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-05.html">
          <span>November 05, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-03.html">
          <span>November 03, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-02.html">
          <span>November 02, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-31.html">
          <span>October 31, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-28.html">
          <span>October 28, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-27.html">
          <span>October 27, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-26.html">
          <span>October 26, 2026</span>
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
