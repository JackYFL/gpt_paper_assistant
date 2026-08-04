

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
      <p class="eyebrow">Daily ArXiv / August 04, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>31</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>14</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>10.2</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="8 mentions">alignment</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="16 mentions">camera</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="10 mentions">caption</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="8 mentions">challenging</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="7 mentions">complementary</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="7 mentions">consistency</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="9 mentions">consistent</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="17 mentions">control</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="10 mentions">detection</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="11 mentions">document</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="9 mentions">editing</span><span class="cloud-word" style="font-size:2.30rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="27 mentions">evidence</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="14 mentions">fine-grained</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="12 mentions">fixed</span><span class="cloud-word" style="font-size:2.19rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 70%, var(--accent))" title="25 mentions">frame</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="12 mentions">fusion</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="13 mentions">gaussian</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="7 mentions">generated</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="16 mentions">generation</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="10 mentions">interaction</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="17 mentions">motion</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="10 mentions">multimodal</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="8 mentions">multiple</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="14 mentions">object</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="9 mentions">optimization</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="7 mentions">paradigm</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="14 mentions">query</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="15 mentions">reasoning</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="7 mentions">residual</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="16 mentions">retrieval</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="12 mentions">scene</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="10 mentions">semantic</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="11 mentions">sparse</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="12 mentions">spatial</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="7 mentions">stream</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="8 mentions">supervision</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="9 mentions">temporal</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="7 mentions">understanding</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="10 mentions">unified</span><span class="cloud-word" style="font-size:2.01rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 61%, var(--accent))" title="22 mentions">video</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="10 mentions">view</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="7 mentions">vision</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="7 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="36 mentions">visual</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="8 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="91 mentions">action</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="151 mentions">agent</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="90 mentions">alignment</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="59 mentions">attention</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="67 mentions">camera</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="67 mentions">challenging</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="83 mentions">consistency</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="60 mentions">consistently</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="66 mentions">control</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="60 mentions">cost</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="86 mentions">detection</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="77 mentions">diffusion</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="65 mentions">domain</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="88 mentions">dynamic</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="70 mentions">environment</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="131 mentions">evidence</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="97 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="69 mentions">foundation</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="79 mentions">frame</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="66 mentions">fusion</span><span class="cloud-word" style="font-size:2.07rem;opacity:0.82;color:color-mix(in srgb, var(--accent-2) 64%, var(--accent))" title="241 mentions">generation</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="62 mentions">geometry</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="88 mentions">inference</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="112 mentions">interaction</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="131 mentions">language</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="63 mentions">latent</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="81 mentions">memory</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="66 mentions">mllm</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="63 mentions">modality</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="130 mentions">motion</span><span class="cloud-word" style="font-size:1.77rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="186 mentions">multimodal</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="77 mentions">multiple</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="146 mentions">object</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="66 mentions">perception</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="85 mentions">pipeline</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="69 mentions">point</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="67 mentions">query</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="79 mentions">real-world</span><span class="cloud-word" style="font-size:1.69rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="173 mentions">reasoning</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="96 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="73 mentions">region</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="64 mentions">retrieval</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="63 mentions">robust</span><span class="cloud-word" style="font-size:1.51rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="144 mentions">scene</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="64 mentions">segmentation</span><span class="cloud-word" style="font-size:1.70rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="174 mentions">semantic</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="81 mentions">space</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="126 mentions">spatial</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="75 mentions">support</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="96 mentions">target</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="109 mentions">temporal</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="154 mentions">token</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="64 mentions">trajectory</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="128 mentions">understanding</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="96 mentions">unified</span><span class="cloud-word" style="font-size:2.52rem;opacity:0.94;color:color-mix(in srgb, var(--accent-2) 87%, var(--accent))" title="338 mentions">video</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="63 mentions">vision</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="68 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="398 mentions">visual</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="76 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>31 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">World Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation</strong>
          <small>Jiaming Chen, Guoan Xu, Aoshen Huang, Haozhuo Zhang, Yang Li, Wei Pan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Modeling</span>
<span class="topic-tag">Autonomous Navigation</span>
<span class="topic-tag">Vision Foundation Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2608.02428</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02428">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 3: it proposes a new world-modeling method for autonomous navigation with a frozen vision foundation model, and reports zero-shot deployment in a robotic simulator.</p>
        <p class="abstract">Forecasting future states from video sequences is a critical challenge for autonomous robotic systems and a fundamental objective of world modeling. Prior generative methods operating at the pixel level inevitably overemphasize task-irrelevant details, leading to prohibitive computational overhead. While latent-based approaches attempt to mitigate this by predicting features directly, the persistent reliance on heavy decoders for state-to-task mapping remains a computational bottleneck. In this work, we propose Decoder-Free Feature Forecasting (DF$^3$), a novel framework that models world evolution entirely within the latent space and directly derives task outputs, completely eliminating the need for a decoder. Specifically, DF$^3$ injects learnable spatial queries into the terminal blocks of a frozen vision foundation model to extract future state representations directly. By employing a lightweight, unified Motion-Aware Context Fusion (MACF) mechanism that seamlessly integrates coarse flow warping with fine-grained latent cross-correlation, these queries interact with historical token representations to explicitly align and forecast the feature of the next frame. Subsequently, a specialized set of task queries probes these forecasted features for the downstream task. Extensive experiments on public benchmarks and zero-shot deployment in a robotic simulator demonstrate that DF$^3$ achieves performance comparable to state-of-the-art methods while offering superior efficiency and flexibility for integrated perception and control.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>GROVE: Growing and Reasoning over Temporally Stratified Memory from Streaming Video Experience</strong>
          <small>Sitong Gong, Caixin Kang, Tianyu Yan, Guo Chen, Bo Zheng, Kaipeng Zhang, Yunzhi Zhuge, Xiang Ruan, Huchuan Lu, Yifei Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Video Memory</span>
<span class="topic-tag">Proactive Assistants</span>
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
          <span>Paper 2 / arXiv:2608.02392</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02392">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: an embodied/video-memory benchmark-style system for streaming video experience with proactive assistant behavior and temporally stratified memory.</p>
        <p class="abstract">A wearable assistant should both answer questions about its visual history and recognize when that history is useful to the present situation. Existing video-memory systems primarily support question-conditioned recall, whereas proactive assistants typically use separate memory and control mechanisms. We introduce GROVE, a training-free framework that supports both behaviors with one memory grown causally from a continuous video stream. GROVE retains fine-grained perceptual evidence and incrementally consolidates it into time-stamped moments, coherent episodes, and recurring cross-day patterns. Each stratum is paired with a scale-native retrieval skill for locating an observation, replaying an activity, or traversing long-range regularities. Reactive QA and proactive assistance share this memory and access interface, differing in whether retrieval is initiated by a user query or the current situation. Across multiple benchmarks including the challenging MM-lifelong and EgoServe, GROVE achieves the best results among the compared methods. Controlled ablations show that the temporal strata and their access skills are complementary, with patterns providing the largest benefit when evidence spans multiple days. Code will be available at https://github.com/SitongGong/GROVE.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Egocentric Video</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>HiResNets: Native Full-HD Video Recognition with Foveal Residual Streams</strong>
          <small>Shivani Mall, Swarnim Jain, Joao F. Henriques</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Egocentric Video</span>
<span class="topic-tag">Spatial Attention</span>
<span class="topic-tag">High-Resolution Recognition</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.PF</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2608.02140</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02140">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: it targets high-resolution video recognition with foveal residual streams and explicitly studies human-like foveation for egocentric video, which is closely related to spatial understanding in embodied perception.</p>
        <p class="abstract">Much of the recent progress in image and video recognition has come at the cost of memory: larger models, increased resolution, and longer temporal contexts. An inevitable component is the quadratic (or larger) growth of memory and compute based on image resolution, which is a property of the grid sampling used in convolutional networks and vision transformers. In this work we study residual networks whose convolutional blocks have logarithmic-square growth instead, enabling them to process very high-resolution video quickly. The key insight is to use a residual architecture&#x27;s residual stream as a high-resolution buffer, to which convolutional blocks only read and write via log-polar image warp operations. Layers adaptively focus on different parts of each frame, with very high resolution only near the focus point. A complete high-resolution representation is built up in the residual stream, analogous to eye saccades creating a complete picture in biological vision, and a theoretical construction is presented that eliminates the quadratic dependency of the residual stream resolution. Experiments demonstrate that our proposed HiResNets learn to foveate around scenes similarly to human vision, and have superior performance in difficult egocentric video recognition tasks, especially egocentric video with small objects and fine-grained recognition.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity</strong>
          <small>Yuxue Yang, Shuyao Shang, Jiahe Wang, Zitong Zhou, Liang Tan, Junhan Zeng, Ruizhi Li, Junyan Li, Yu Liu, Xiao Yang, Yong Li, Jun Zhu, Hongsheng Li, Tieniu Tan, Lue Fan, Zhaoxiang Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Spatial Consistency</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2608.02603</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02603">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: proposes a benchmark for world models with spatial consistency and world reactivity, directly relevant to embodied/simulated agent evaluation.</p>
        <p class="abstract">Controllable video generation models are increasingly being developed as world models. Accordingly, evaluating them in this role extends beyond the apparent appearance of generated videos to the inherent reactivity of the worlds they depict: the ability to infer from the scene state how the world should react and to generate plausible consequences not explicitly described in the input. Yet existing benchmarks mainly assess visual quality or explicit instruction fulfillment by checking whether requested actions and interaction outcomes are realized, leaving inherent reactivity underexamined. We introduce WorldExam, a hierarchical diagnostic benchmark spanning four levels: Visual Quality, Control Adherence, Spatial Consistency, and World Reactivity. It comprises 1,474 cases across eight dedicated tasks and supports unified evaluation of camera-, action-, and language-driven model paradigms. The World Reactivity level evaluates scene-conditioned reactions and goal-directed behaviors beyond what is explicitly specified in the input. Evaluation of 20 representative models reveals a clear capability split. Camera-driven models excel at camera control, but their interfaces do not support dynamic interaction; action-driven models control subjects more precisely but often leave the world unresponsive; and language-driven models perform better on interaction but follow complex controls less faithfully. No model combines broad task coverage with consistently strong performance, showing that high visual quality and explicit instruction fulfillment do not guarantee inherent reactivity.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal LLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>VC-Tooler: Learning Compositional and Adaptive Visual Tool Use</strong>
          <small>Yizheng Wu, Jiashen Hua, Bing Deng, Jieping Ye</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Visual Tool Use</span>
<span class="topic-tag">Agentic Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2608.02217</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02217">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: a new VLM-style agentic visual tool-use method with compositional and adaptive multi-step tool interactions.</p>
        <p class="abstract">Agentic multimodal reasoning extends passive image understanding by allowing VLMs to actively acquire and refine visual evidence through visual tool interactions. Effective visual tool use requires three capabilities: grounding tool calls in visual context, composing tools across multiple steps, and adapting reasoning to tool-returned observations. However, existing approaches largely focus on grounding within fixed tool spaces and rigid invocation patterns, leaving composition and adaptation insufficiently addressed. We present VC-Tooler, which learns visual tool use as a compositional and adaptive capability. To this end, we first build a trajectory bank through a hierarchical synthesis pipeline covering three capability levels: single-tool grounding, multi-tool composition, and diverse tool contexts and interfaces. We then train the model in two stages: a supervised cold start that establishes these capabilities, followed by reinforcement learning that encourages accurate, efficient, and context-aware visual tool use. VC-Tooler achieves state-of-the-art performance among open-source models on both general-purpose and agentic benchmarks, including $95.8\%$ on V* and $35.3\%$ on VTC-Bench, and shows promising transfer under richer tool settings at inference time. Project page: https://w1zheng.github.io/VC-Tooler</p>
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
          <strong>Recompute or Reuse? Diagnosing and Mitigating Textual Shortcuts in VLM Self-Reflection</strong>
          <small>Wenxiao Fan, Jingling Fu, Fang Li, Luohang Liu, Yu He, Lichen Ma, Zhiyang Yu, Weishan Bi, Junshi Huang, Yan Li, Gu Simiu, Kan Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Interpretability</span>
<span class="topic-tag">Test-Time Intervention</span>
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
          <span>Paper 6 / arXiv:2608.01930</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01930">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: analyzes VLM self-reflection behavior and introduces a training-free intervention for visual recomputation versus textual reuse.</p>
        <p class="abstract">Vision-language models (VLMs) are expected to revise their reasoning when visual evidence changes. Failures to do so are often attributed to insufficient visual attention or contextual inertia, leaving unclear what models reuse instead of recomputing from the current image. We show that evidence-bearing reasoning in a prior chain of thought (CoT) can form a textual shortcut that competes behaviorally with visual recomputation. Across 16 VLMs, a matched counterfactual analysis identifies evidence-bearing content as the most robust carrier of prior-CoT influence. Removing this evidence-bearing content shifts answer preference more than removing length-matched non-evidence context or the final-answer span, with prior control weakening progressively as more stale evidence is removed. Reordering this evidence also weakens prior control, showing that its organization modulates shortcut strength. Beyond the immediate answer, the shortcut can retain residual influence after answer correction: weakening current-image support shifts preference back toward the prior answer, while repeated prior answers and reused premises arise mainly when the shortcut remains active. To limit this influence, we introduce Fresh-State Attention Firewall (FSAF), a training-free intervention that isolates fresh computation from the prior CoT. Across five VLMs, FSAF raises visual update rate from 35.28% to 53.61% and reduces prior-answer rate from 39.22% to 3.67%. Reliable VLM self-reflection therefore requires more than looking again: fresh visual recomputation must be protected from stale textual reuse.</p>
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
          <strong>Generated Images Are Easier to Forget: A Machine Unlearning Perspective for Synthetic Image Detection</strong>
          <small>Jun Nie, Yonggang Zhang, Tongliang Liu, Yiu-ming Cheung, Bo Han, Xinmei Tian</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Synthetic Image Detection</span>
<span class="topic-tag">Machine Unlearning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2608.00716</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.00716">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it studies a vision foundation model/LVM application for synthetic image detection, with a novel unlearning-based perspective and an insightful empirical finding about forgetting dynamics.</p>
        <p class="abstract">Robust detection of generated images is critical to counter the misuse of generative models. Existing methods primarily depend on learning from human-annotated training datasets, limiting their generalization to unseen distributions. In contrast, large-scale vision models (LVMs) pre-trained on web-scale datasets exhibit exceptional generalization power through exposure to diverse distributions, offering a transformative paradigm for this task. However, our experimental results reveal that LVMs pre-trained on natural-image-dominated data can effectively capture the features of both natural and generated images, yielding comparably low losses and thus limited discriminative capacity between them. This prompts a key question: When and how do LVMs exhibit different behaviors when capturing features of natural and generated images? This investigation reveals an insight: during unlearning, LVMs exhibit disparate forgetting dynamics with feature degradation for generated images escalating faster than natural ones. Inspired by the disparate dynamics, we introduce two detection methods: 1) data-free detection, which prunes model parameters to induce unlearning without data access, and 2) data-driven detection, which optimizes LVMs to unlearn knowledge tied to generated images. Extensive experiments conducted on various benchmarks demonstrate that our unlearning-based approach outperforms conventional detection methods. By recasting the detection task as a problem of machine unlearning, our work establishes a new paradigm for generated image detection.</p>
      </div>
    </details>


    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors</strong>
          <small>Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">3D Gaussian Splatting</span>
<span class="topic-tag">Character Animation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2608.01726</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01726">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it leverages 2D vision foundation models to distill motion priors for 3D Gaussian skinning, a clear vision-foundation-model application.</p>
        <p class="abstract">3D Gaussian Splatting has achieved remarkable success in photorealistic and efficient rendering, leading to a rapid increase in 3D assets represented by 3D Gaussian primitives. Directly rigging these assets with arbitrary skeleton topologies is highly desirable. However, training a feed-forward skinning framework is infeasible due to the lack of high-quality 3D Gaussian rigging datasets. An alternative solution is to transfer mesh-based techniques to 3D Gaussian-based representation, but 3D Gaussian primitives are not restricted to the surface and lack explicit topological connectivity. Moreover, this kind of method suffers from poor generalization to unseen data due to its strong dependence on training data, while acquiring high-quality rigging data is prohibitively expensive. To address this challenging problem, we propose G-Skin, a novel generative skinning framework designed for expressive and high-fidelity animation with 3D Gaussian representation. To overcome this 3D data scarcity, we introduce a skeleton-controllable image generation model leveraging 2D vision foundation models to distill powerful motion priors into pseudo-guidance. Guided by these priors, we formulate an optimization pipeline incorporating geometry-aware regularizations, which stabilizes the learning process and ensures smooth, structurally coherent skinning weights. G-Skin also generalizes flexibly to the augmented variants of 3D Gaussian representation designed to mitigate animation-induced rendering artifacts. Extensive experiments validate the effectiveness of our approach, demonstrating clear advantages over state-of-the-art methods. Project page: https://yaoyx689.github.io/GSkin.html.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Few-Shot Object Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Prompt-Driven Simulation with Feature Perturbation for Cross-Domain Few-Shot Object Detection</strong>
          <small>Linhai Zhuo, Junxi Cai, Tianwen Qian, Qingping Zheng, Yang Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Few-Shot Object Detection</span>
<span class="topic-tag">VLM-Guided Data Augmentation</span>
<span class="topic-tag">Domain Generalization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2608.01348</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01348">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 and partly 4: it uses a large VLM for prompt-driven simulation, but the core contribution is a new cross-domain few-shot object detection method with grounding-aware synthetic domain generation and feature perturbation.</p>
        <p class="abstract">Data augmentation, which simulates diverse visual variations to expand the source distribution and induce synthetic domain shifts, is a simple yet effective strategy for mitigating severe domain shifts and limited labeled target data in cross-domain few-shot object detection (CD-FSOD). Existing approaches rely on conventional data augmentation, such as Color-Jitter, Mosaic, and background-centric adaptation (e.g., Domain-RAG), which are limited in modeling complex domain shifts and often lead to suboptimal performance. In this paper, we propose PSP-FSOD, a principled framework that integrates prompt-driven domain simulation with feature perturbation regularization to improve generalization in CD-FSOD. To enable controllable domain synthesis, we design a prompt-driven strategy that leverages the visual grounding capability of large VLMs to jointly model foreground and background variations, generating semantically consistent yet domain-diverse training samples. Moreover, we adopt a grounding-aware generation scheme that guides object placement and alleviates semantic-spatial misalignment, thereby improving foreground adaptation. To ensure training stability and robustness, we further introduce a noise-induced feature perturbation mechanism that injects Gaussian noise into multi-scale intermediate features with distribution correction, encouraging consistent predictions under perturbations and reducing reliance on domain-specific cues. Extensive experiments demonstrate that PSP-FSOD produces high-quality domain-diverse supervision and learns domain-invariant representations, consistently improving performance across CD-FSOD benchmarks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Fusion</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Unleashing the Power of Text: Text-Guided Flow Matching for Image Fusion under Complex Degradations</strong>
          <small>Axi Niu (School of Computer Science, Northwestern Polytechnical University, Xi&#x27;an, China), Jieheng Li (School of Computer Science, Northwestern Polytechnical University, Xi&#x27;an, China), Kang Zhang (School of Electrical Engineering, KAIST, Daejeon, Republic of Korea), Qingsen Yan (School of Computer Science, Northwestern Polytechnical University, Xi&#x27;an, China), Jinqiu Sun (School of Aeronautics and Astronautics, Northwestern Polytechnical University, Xi&#x27;an, China), Yanning Zhang (School of Computer Science, Northwestern Polytechnical University, Xi&#x27;an, China)</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Fusion</span>
<span class="topic-tag">Text Guidance</span>
<span class="topic-tag">Flow Matching</span>
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
          <span>Paper 9 / arXiv:2608.00530</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.00530">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a text-guided generative fusion method that uses structured prompts and flow matching for multi-modal image restoration/fusion.</p>
        <p class="abstract">Infrared-visible image fusion under realistic degradation scenarios is a challenging task, as degradations not only cause a loss of reliable modality-specific information in observed images but also hinder the fusion process. Recent studies indicate that text can provide prior information about degradation characteristics, complementing the limited evidence available from corrupted input images and facilitating fusion. However, existing methods typically inject fixed global text representations into visual features, making it difficult for textual guidance to adapt to spatially varying degradations, local structures, and thermal saliency. To this end, we propose TGFusion, a text-guided latent-space flow matching framework that unifies degradation suppression and cross-modal fusion. TGFusion encodes task, degradation, and generation cues into structured prompts. To fully exploit these priors, we design a Prompt-conditioned Multi-stream Joint Flow Transformer that represents text as an independent semantic stream alongside fusion, visible, and infrared streams. Joint attention enables token-level bidirectional interaction and layer-wise updating among semantic and visual representations, allowing degradation semantics to dynamically guide reliable information selection and fusion latent generation. Extensive experiments on public benchmarks and complex degradation scenarios demonstrate that TGFusion achieves superior or competitive performance in perceptual quality, image naturalness, structural-detail preservation, and infrared-saliency retention, while remaining robust across diverse single and compound degradations.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Vision-Language Pretraining</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Learning How Much, Not Just What: Cross-Patient Burden Order for CT Vision-Language Pretraining</strong>
          <small>Guoliang You, Haifan Gong, Xiaomeng Chu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Vision-Language Pretraining</span>
<span class="topic-tag">3D CT</span>
<span class="topic-tag">Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2608.00231</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.00231">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: vision-language pretraining for CT with anatomy-conditioned representations and a clever weak-ordering/burden alignment trick.</p>
        <p class="abstract">Volumetric CT vision-language pretraining learns 3D representations from scan-report pairs, but global and anatomy-aware objectives supervise only correspondence: they establish what is present and leave how much unconstrained. Nothing separates a mild from an extensive case of the same finding along a consistent direction, so the graded burden language in reports collapses into a present/absent signal. Longitudinal supervision would supply this order, but patient-matched CT pairs are scarce at scale; cross-sectional cohorts already encode weak burden cues across different patients. We introduce Spectrum, an anatomy-conditioned framework that represents each study at whole-study and organ scopes. For each organ-mapped pathology, a rule-based scorer mines confidence-filtered lower-to-higher pairs of different patients, and Burden-Direction Alignment (BDA) aligns the pathology-conditioned image delta with the report delta at each scope, separating that direction from its reverse. Because the endpoints are different people, a target-conditioned aligner first makes them comparable, so the delta reflects burden rather than between-patient variation. BDA further separates the selected direction from its reverse, anchors it to the observed higher-burden endpoint, and enforces consistency across ordered triplets. Since every pair is drawn within a single pathology, BDA is designed to constrain intra-class structure that image-report contrast alone never touches. Spectrum attains 85.6 zero-shot AUROC on CT-RATE and 72.7 on external RAD-ChestCT, with consistent gains in linear probing and retrieval. Weak cross-patient order is thus a scalable complement to anatomy-aware correspondence, yielding burden-aware CT representations without longitudinal data.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Visual Document Retrieval</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>VaRS-Doc: Interpretation-Aware Variant Representations via Latent Self-Probing for Visual Document Retrieval</strong>
          <small>Haocheng Wang, Tongkun Guan, Wei Shen, Xiaokang Yang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Visual Document Retrieval</span>
<span class="topic-tag">Late Interaction</span>
<span class="topic-tag">Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2608.01211</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01211">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: visual document retrieval with a new latent self-probing representation scheme for visual document understanding.</p>
        <p class="abstract">Visual document retrieval has recently become increasingly important in applications such as enterprise search, scientific literature discovery, and retrieval-augmented generation. These applications depend on efficiently identifying query-relevant pages across large collections of visually rich documents. Existing methods commonly adopt late-interaction architectures that encode and index documents offline to enable scalable and low-latency online retrieval. Despite its efficiency, this paradigm requires each document to be encoded into a fixed representation before the query is known. However, the same content in a visual document may induce different interpretations depending on the query intent, which a fixed representation struggles to capture. Yet postponing document encoding until the query arrives would incur prohibitive online retrieval latency. To address this gap, we propose VaRS-Doc, a visual document retrieval framework that diversifies document representations by enabling the model to actively explore variant latent interpretations during document encoding, while preserving efficient late-interaction retrieval in which each query adaptively selects the best-fit representation. We further introduce a two-stage training strategy that encourages the model to capture complementary semantic interpretations and prevents it from falling back to train a single dominant representation. Experiments on visual document retrieval benchmarks show that VaRS-Doc achieves state-of-the-art retrieval performance, offering a practical solution to the mismatch between query-agnostic document encoding and query-specific retrieval needs. Code is available at https://github.com/bokufa/VaRS-Doc.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>AdaThinkV: Adaptive Thinking for Token-Efficient Video Reasoning</strong>
          <small>Jingqi Tian, Haoji Zhang, Lin Chen, Hongbo Jin, Haonan Xu, Tianrui Zhu, Xingming Shui, Shilin Ma, Wenjing Yang, Yansong Tang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Reasoning</span>
<span class="topic-tag">MLLM</span>
<span class="topic-tag">Efficient Inference</span>
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
          <span>Paper 12 / arXiv:2608.01980</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01980">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: this is a new video MLLM reasoning framework with adaptive thinking and token-efficient inference.</p>
        <p class="abstract">Chain-of-thought (CoT) reasoning can improve performance on difficult video questions but often wastes decoding tokens on simple ones. We study whether a video multimodal large language model can adapt its reasoning effort to each question. We propose AdaThinkV, an adaptive framework for video reasoning that learns whether to reason explicitly without offline difficulty labels, manually tuned confidence thresholds, or an external router. During reinforcement learning, AdaThinkV samples matched rollouts in explicit reasoning and direct answering modes for each prompt. ThinkGain estimates the prompt-level utility of explicit reasoning by balancing its accuracy gain against additional response length, providing supervision for both conditional response generation and autonomous mode selection. For difficult prompts, limited rollout exploration can yield groups in which every response is unsuccessful and accuracy rewards show little variation, providing insufficient signal for learning. We therefore introduce Variance Recovery Policy Optimization (VRPO), which retains and progressively expands these groups to recover informative signals from prompts that are difficult yet solvable. At inference, AdaThinkV selects a response mode and generates the response in a single autoregressive sequence. Across a unified suite of video reasoning evaluations, AdaThinkV achieves a mean accuracy of 40.79 with an average of 257.20 output tokens, outperforming the strongest evaluated adaptive baseline by 2.98 points while using 22.7% fewer tokens. Project page: https://trilarflagz.github.io/AdaThinkV/</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>SpatialQuery: Benchmarking Geometry-Grounded Multi-Instance Spatial Reasoning in Vision-Language Models</strong>
          <small>Hai Nguyen, Tung Vu, Cong Tran</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Spatial Intelligence</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2608.01709</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01709">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: it targets spatial understanding in VLMs with geometry-grounded multi-instance spatial reasoning and a new benchmark.</p>
        <p class="abstract">Vision-language models (VLMs) achieve strong semantic understanding but remain unreliable in metric spatial reasoning, particularly when queries require comparing multiple instances of the same object category. We study this problem through the Closest-Instance Distance Query (CIDQ), where a model must identify the nearest visible candidate to a unique reference object and estimate their gravity-aligned floor-plane distance. We introduce SPATIALQUERY, a training- free framework for CIDQ reasoning from a single RGB image, together with SPATIALQUERY-1M, a benchmark containing over one million RGB-only question-answer pairs from 200 indoor scenes. SPATIALQUERY recovers instance-level metric geometry and transforms it into a canonical Bird&#x27;s-Eye View through Scene Cubifying, which represents objects as uniformly sized, category-coded blocks to emphasize their relative floor- plane locations. We further propose Uncertainty-Aware Chain-of-Thought (UA-CoT) prompting, which incorporates geometry- derived per-instance uncertainty into the VLM reasoning process. Without task-specific fine-tuning or architectural modification, SPATIALQUERY with Qwen3-VL-8B achieves a Floor-MAE of 0.259 m, an Unc-Acc@0.3 m of 90.5%, and a proximity-decision accuracy of 84.18%, outperforming fine-tuned spatial specialists, general-purpose VLMs, and closed-source frontier models. Code, benchmark resources, and an interactive demo are available at https://namhai1810.github.io/SpatialQuery/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Vision-Language</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Semantically Calibrated Evidence Composition for CT Vision-Language Learning</strong>
          <small>Guoliang You, Haifan Gong, Xiaomeng Chu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Vision-Language</span>
<span class="topic-tag">Multimodal Representation Learning</span>
<span class="topic-tag">Cross-Modal Retrieval</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2608.00239</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.00239">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: this is a vision-language model for CT-report learning, with anatomy-grounded multimodal alignment and evidence composition.</p>
        <p class="abstract">Learning transferable representations from CT-report pairs requires combining whole-volume context with anatomy-specific evidence. Existing methods typically emphasize either global CT-report alignment or fine-grained anatomy-level correspondence. Global alignment preserves broad study context but leaves the contribution of localized evidence implicit, whereas anatomy-level alignment explicitly grounds local findings but does not specify how independently represented evidence should interact, acquire study-level meaning, and contribute to a global CT representation. To address this gap, we propose SCOPE (Semantic Calibration Of comPosed Evidence), a framework for semantically calibrated evidence composition in CT vision-language learning. Under organ-specific report supervision, mask-guided queries with fixed anatomical identities extract context-aware organ evidence from shared, uncropped volumetric features, while an unrestricted global query retains access to whole-volume context. The global query then drives Local-Global Coupling to compose the organ evidence into a unified evidence representation. The composed evidence is subsequently calibrated using the diagnostic summary, providing study-level semantic supervision beyond local organ descriptions, and is finally integrated as a controlled residual into a context-preserving whole-volume representation aligned with the complete report. This progressive pathway connects localized evidence with study-level semantics without reducing the CT representation to a predefined set of organs. On CT-RATE and RadChestCT, SCOPE achieves macro AUCs of 85.0 and 72.2, respectively, outperforming the previous SOTA by 7.2 and 4.2, while also yielding substantial gains in linear probing and cross-modal retrieval. These results demonstrate the effectiveness of semantically calibrated evidence composition.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">SLAM</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>CHOW-SLAM: Compact Hybrid Representation with Complementary Overlap Window Optimization for RGB-D SLAM</strong>
          <small>Wenxuan Ji, Jin Xiao, Xiaoguang Hu, Jiaqi Shi, Zichong Jia, Baochang Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">SLAM</span>
<span class="topic-tag">RGB-D Reconstruction</span>
<span class="topic-tag">Embodied Spatial Mapping</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2608.01914</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01914">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: this is a new SLAM method with explicit spatial/temporal constraints and a novel overlap-window optimization, which is strongly aligned with embodied AI / simulator-style spatial understanding.</p>
        <p class="abstract">Simultaneous localization and mapping (SLAM) based on Neural Radiance Fields (NeRF) enables dense, continuous scene reconstruction. However, existing systems operating with limited online resources struggle to simultaneously construct two types of constraints, namely, compact yet discriminative spatial constraints derived from scene representations and persistent temporal constraints derived from historical observations. To address this challenge, we propose CHOW-SLAM, a dense RGB-D SLAM framework that explicitly constructs these complementary spatial and temporal constraints. Spatially, we propose a compact parametric-hash (P-H) hybrid representation that organizes components based on planes and grids across scales in P and H branches. A unified multi-output decoder further aligns the ray termination distributions induced by TSDF and density, preserving geometry and appearance under a compact parameter budget. Temporally, we propose a complementary overlap-window strategy to prevent optimization from being dominated by short-term overlap or weakly related historical observations. Within a fixed budget, the strategy retains recent frames, selects high-overlap local frames, and introduces temporally distributed historical keyframes. Loss-aware keyframe insertion and bundle adjustment scheduling further adapt optimization to tracking quality. In addition, ORB-based tracking and geometric pose estimation are used for pose initialization, followed by neural rendering optimization to improve tracking stability. Extensive evaluations on multiple datasets demonstrate that CHOW-SLAM outperforms state-of-the-art methods in both scene reconstruction quality and camera tracking accuracy. The source code is available at https://github.com/jinjidexiaohuoban/CHOW-SLAM.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video VLM</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>RSVideo: Are Your Vision-Language Models Ready for Remote Sensing Videos?</strong>
          <small>Hongjie Zhou, Shiqin Wang, Haoyang Chen, Haonan Guo, Di Wang, Juhua Liu, Fu Lin, Yong Luo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video VLM</span>
<span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2608.02039</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02039">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: this builds a remote-sensing video benchmark and a VLM/RL framework for spatiotemporal video understanding.</p>
        <p class="abstract">Remote-sensing videos enable real-time observation of changes in target attributes, short-term activities, and scene evolution. They record motion, actions, interactions, and scene changes that cannot be captured by isolated images. Existing models primarily target single images or discrete temporal observations spanning a long time range. However, a unified evaluation setting for assessing vision-language models on continuous remote-sensing video understanding remains lacking. We introduce RSVideo-10K, a remote-sensing video dataset comprising 10,773 instances, 1.47 million frames, and 17.02 hours of footage, containing both unmanned aerial vehicles and satellite platforms. Its fixed evaluation benchmark, RSVideo-Bench, contains 2,731 test instances and evaluates two complementary aspects of remote-sensing video understanding: L1 Perception and L2 Reasoning, spanning seven capability groups and 17 tasks. Evaluations show that current vision-language models still struggle to recover small local evidence, track short-lived states, and use scene-constrained spatial relations. Based on this analysis, we further propose RSVideo, a reinforcement learning framework for small-target spatiotemporal focusing that selects question-relevant regions across frames and suppresses redundant background tokens. RSVideo achieves a maximum absolute improvement of 9.01% with InternVL3.5-14B and attains the highest accuracy of 40.63% with Qwen3.6-27B across 26 open-source vision-language backbones.Codes will be available at https://github.com/HongjieZhou0329/RSVideo.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Gaussian Splatting</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>QuerySplat: Decoupling Geometry and Appearance Representations in 3DGS Prediction</strong>
          <small>Yinglong Li, Donghui Shen, Xiaoyu Zhang, Zhichao Ye, Hongyu Wu, Aimin Hao, Guofeng Zhang, Haomin Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Gaussian Splatting</span>
<span class="topic-tag">Geometric Priors</span>
<span class="topic-tag">Novel View Synthesis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2608.01186</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01186">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a 3D reconstruction/3DGS method leveraging pretrained vision-geometric priors and explicit appearance decoupling.</p>
        <p class="abstract">While feed-forward 3D Gaussian Splatting (3DGS) enables efficient 3D reconstruction, achieving high-fidelity rendering remains challenging. Existing pixel-aligned approaches suffer from spatial inflexibility and massive structural redundancy, whereas query-based methods lack 3D priors and entangle geometry with appearance, yielding blurry, pose-dependent results. To overcome these deficiencies, we propose \textbf{QuerySplat}, a feed-forward 3DGS framework driven by geometric priors and explicit appearance decoupling. Specifically, we design a dual-branch query-based decoder: the geometry branch leverages a pretrained Vision Geometric Model for spatial understanding, which intrinsically endows QuerySplat with pose-free modeling capabilities, while the appearance branch recovers high-frequency details through a dedicated pathway separated from geometric attribute regression. Extensive experiments demonstrate that QuerySplat mitigates the blurry rendering issues of early query-based models and consistently outperforms pixel-aligned approaches in rendering fidelity. On the challenging DL3DV benchmark, it achieves state-of-the-art novel view synthesis performance, with average PSNR gains of 2.30 dB and 1.04 dB over the best pose-free and pose-required baselines, respectively. Project Page: https://inspatio.github.io/querysplat.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>MIEScore: Human-Aligned Evaluation for Multi-Source Image Editing</strong>
          <small>Zitong Xu, Huiyu Duan, Xinyun Zhang, Weifei Xiong, Tianyi Zheng, Xiongkuo Min, Qiang Hu, Zhengxue Cheng, Bo Li, Guangtao Zhai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM Evaluation</span>
<span class="topic-tag">Image Editing</span>
<span class="topic-tag">Human Preference Benchmark</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.MM</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2608.02059</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02059">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 4: it introduces an MLLM-based evaluator for multi-source image editing and a new benchmark with human preference annotations.</p>
        <p class="abstract">Recent advances in unified multimodal models have significantly improved text-guided image editing abilities. In particular, models such as Nano-Banana-Pro and GPT-Image-2 demonstrate emerging capabilities in multi-source image editing (MIE), including tasks such as object synthesis, person-background composition, and cross-image style fusion. However, existing benchmarks and image editing assessment (IEQA) methods remain primarily focused on single-image editing tasks and largely overlook the more challenging setting of MIE. This highlights the urgent need for a comprehensive and human-aligned benchmark for MIE. To this end, we introduce MIE-Bench, the first large-scale multiple image editing benchmark with fine-grained human preference annotations. Specifically, MIE-Bench includes 3,000 editing instances across 16 tasks, each involving more than two source images and an editing prompt, together with 36K edited images produced by 12 state-of-the-art editing models and over 108K mean opinion scores (MOSs) covering visual quality, instruction following, and attribute preservation. Based on MIE-Bench, we propose MIEScore, a multimodal large language model (MLLM)-based evaluation model enhanced with skill optimization and multi-dimensional supervised fine-tuning, to provide human-aligned feedback for MIE. Extensive experiments show that MIEScore achieves state-of-the-art performance in aligning with human preferences and generalizes well across other IEQA datasets. Both the dataset and the model are available at https://github.com/IntMeGroup/MIEScore.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Reconstruction</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction</strong>
          <small>Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Gaussian Splatting</span>
<span class="topic-tag">Vision Foundation Models</span>
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
          <span>Paper 20 / arXiv:2608.02145</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02145">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: this is a vision foundation model–style 3D reconstruction method using feed-forward Gaussian splatting with improved generalization.</p>
        <p class="abstract">In this paper, we propose UniqueSplat, a view-conditioned feed-forward 3D Gaussian Splatting model to reconstruct customized 3D radiance fields for each view query. Existing feed-forward methods such as pixelSplat and MVSplat aim to generate fixed Gaussians across all views of each scene by minimizing the error between rendered views and ground-truth images. However, such fixed Gaussians generally render images from all views and lack the ability to adapt to specific viewpoints, as they do not incorporate target view information when predicting Gaussians. To address this, our UniqueSplat learns the view-conditioned information as a prior and incorporates this knowledge into network parameters, so that Gaussians are dynamically adjusted in accordance with different views. Specifically, we propose a two-branch view-conditioned hyperNetwork to simultaneously learn view-agnostic embeddings and view-specific knowledge, which not only explores the shareable knowledge from various views, but also adapts the model to specific views at test time. Extensive experiments on widely-used datasets including RealEstate10K, ACID and DTU demonstrate the superiority of UniqueSplat over the state-of-the-art methods. Moreover, UniqueSplat encouragingly outperforms existing methods in cross-dataset evaluation, showing its notable generalization ability.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Human Motion Capture</summary>
      <div class="queue">

    <details class="paper-row" id="link20">
      <summary class="paper-row-summary">
        <span class="queue-index">21</span>
        <span class="paper-row-copy">
          <strong>Sen-Cap: Sensor-Flexible and Noise-Resilient Human Motion Capture via LiDAR-Camera Integration</strong>
          <small>Aoru Xue (ShanghaiTech University, Shanghai, China), Yujing Sun (Digital Trust Centre, Nanyang Technological University, Singapore), Yiming Ren (ShanghaiTech University, Shanghai, China, Digital Trust Centre, Nanyang Technological University, Singapore), Kwok-Yan Lam (Digital Trust Centre, Nanyang Technological University, Singapore), Mao Ye (EABOT.AI, China), Yuexin Ma (ShanghaiTech University, Shanghai, China)</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Human Motion Capture</span>
<span class="topic-tag">LiDAR-Camera Fusion</span>
<span class="topic-tag">Robust Estimation</span>
<span class="topic-tag">Sensor Fusion</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 21 / arXiv:2608.02285</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02285">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; it is a human motion capture method with LiDAR-camera fusion, which is adjacent to embodied sensing but not an embodied AI benchmark/method or a foundation-model paper.</p>
        <p class="abstract">We propose Sen-Cap, a Sensor-Flexible and Noise-Resilient 3D human motion Capture framework that integrates multi-modal data from LiDAR and camera. While multi-modal sensors provide richer information than single-modal sensors, existing approaches still suffer from two core challenges. First, multi-modal alignment/matching across arbitrarily deployed sensors is typically handled by explicit calibration, which propagates errors under changing viewpoints and in turn constrains deployment to fixed, highly overlapped layouts. Second, prior methods degrade under severe noise or partial sensor failures, which are common in real-world environments. To address these challenges, Sen-Cap introduces a Unified Across-Sensor Motion Estimator that reconstructs local pose and shape in a human-centric space without calibrations between sensors, supporting a flexible number of sensors, as well as a Noise-Resistant Trajectory Tracker that maintains robustness under severe point cloud noise through iterative refinement. These sensor-flexible and noise-resilient features make Sen-Cap more practical in real-world deployment. Notably, operating in real time, Sen-Cap achieves state-of-the-art performance on major metrics on Human-M3 and FreeMotion, as well as strong cross-domain performance on LiDARHuman26M and RELI11D. This combination of flexibility and robustness opens new opportunities for motion capture in real-world scenarios, e.g. sports analytics, field robotics, and large-scale immersive environments.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link21">
      <summary class="paper-row-summary">
        <span class="queue-index">22</span>
        <span class="paper-row-copy">
          <strong>UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation</strong>
          <small>Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Motion Control</span>
<span class="topic-tag">Camera Control</span>
<span class="topic-tag">Multimodal Conditioning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 22 / arXiv:2608.01944</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01944">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; it is more about controllable human video generation with motion/camera conditioning than VLLMs/MLLMs or embodied AI benchmarks/methods.</p>
        <p class="abstract">Controlling human motion and camera movement is essential for faithful human-oriented video generation, yet remains challenging in multi-person scenes with large body motions, occlusions, and dynamic cameras. Existing pipelines typically rely on visual motion sequences, such as skeleton maps, pose maps, or rendered body representations, for motion control, while using camera embeddings for camera control. Such heterogeneous control interfaces force video generation models to reconcile pixel-aligned visual cues with non-visual geometric embeddings, making motion-camera attribution difficult and sensitive to camera estimation errors. We propose \textbf{UniMoCa}, a representation-driven framework that unifies motion and camera controls in visual space. At the core of UniMoCa is \textbf{Motion-Camera Visual Proxy} (\textbf{MCVP}), a mutually-sharable novel representation that converts 3D human motion and camera trajectories extracted from driving videos into an identity-neutral visual proxy. MCVP renders temporally aligned human geometry under the recovered camera trajectory and augments it with explicit camera trajectory markers, replacing heterogeneous visual-parametric controls with distinguishable visual cues. As both control factors are represented in the same visual space, they become mutually compatible rather than heterogeneous, enabling consistent joint reasoning and editing during video generation. We further curate a \textbf{MCVP-Video} dataset covering complex actions, multi-person interactions, and diverse camera trajectories. Experiments based on the Wan2.2 I2V show that UniMoCa achieves substantial gains in human motion control, camera control, temporal consistency, and camera-aware robustness with minimal additional complexity. More details are shown in our Project page: https://tanliming-daniel.github.io/UniMoCa/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Motion-Language Alignment</summary>
      <div class="queue">

    <details class="paper-row" id="link22">
      <summary class="paper-row-summary">
        <span class="queue-index">23</span>
        <span class="paper-row-copy">
          <strong>FineMoLA: Towards Fine-Grained Motion-Language Alignment from Clip-Level Supervision</strong>
          <small>Tongyan Wang, Zhengyuan Li, Muhan Lin, Shengyang Luo, Yifan Shen, Aniket Bera, Baijian Yang, Yingjie Victor Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Motion-Language Alignment</span>
<span class="topic-tag">Weak Supervision</span>
<span class="topic-tag">Optimal Transport</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 23 / arXiv:2608.01392</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01392">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Relevant to criterion 1 in a broad sense: improves fine-grained spatial-temporal alignment between motion and language, but it is not embodied spatial intelligence on agents.</p>
        <p class="abstract">Text-conditioned human motion generation has made rapid progress with the emergence of large-scale motion--language datasets. However, even datasets with rich long-form descriptions typically provide supervision only at the clip level, without explicit temporal correspondence between motion frames and language. This limits fine-grained motion--text grounding and temporally precise generation. We propose FineMoLA, a weakly supervised framework that learns fine-grained frame--phrase correspondence directly from clip-level annotations. Our method first segments long-form descriptions into action-bearing phrases, and then formulates motion--language alignment as an optimal transport problem, which naturally models many-to-many relations between motion frames and text under global constraints. With entropic regularization and Sinkhorn iterations, FineMoLA efficiently infers pseudo frame-level alignments without human labeling. Experiments on SnapMoGen demonstrate that the learned alignments outperform baselines in motion--text grounding.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Retrieval</summary>
      <div class="queue">

    <details class="paper-row" id="link23">
      <summary class="paper-row-summary">
        <span class="queue-index">24</span>
        <span class="paper-row-copy">
          <strong>UEmbed: Unified Sparse and Dense Multimodal Embeddings</strong>
          <small>Tingyu Song, Mingxin Li, Yanzhao Zhang, Dingkun Long, Pengjun Xie, Zhijie Nie, Yilun Zhao, Shu Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Retrieval</span>
<span class="topic-tag">Sparse-Dense Embeddings</span>
<span class="topic-tag">Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.IR</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 24 / arXiv:2608.02583</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02583">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 moderately: it introduces a unified multimodal embedding model, but it is for retrieval embeddings rather than a VLLM/MLLM used for open-ended multimodal reasoning.</p>
        <p class="abstract">Sparse retrieval underpins modern search systems, from web search to retrieval-augmented generation. Existing work has introduced Learned Sparse Retrieval (LSR) to push beyond exact lexical matching toward richer semantics. Yet LSR has so far remained tied to encoder-style bidirectional architectures, and its extension to multimodal settings still relies heavily on auxiliary cross-modal modules. To address these limitations, we introduce UEmbed (Unified Embedding), a decoder-only multimodal embedding model that produces both sparse lexical and dense representations in one causal forward pass. UEmbed appends N learnable special tokens to the input and partitions the vocabulary into N disjoint subsets. Each token&#x27;s causal hidden state predicts sparse weights over its assigned subset, and the N subsets are concatenated into the full sparse vector. Trained on public data, we release UEmbed at 2B, 4B, and 9B scales. UEmbed-9B reaches 71.8 (dense) and 71.0 (sparse) on MMEB-v2, outperforming multimodal embedding models trained on publicly available data (e.g., RzenEmbed). On BEIR, UEmbed also remains competitive with strong dense and sparse baselines. Furthermore, we demonstrate the practical utility of UEmbed across three dimensions: effectiveness, efficiency, and agentic applications. Overall, UEmbed offers a new paradigm: it unifies dense and sparse embeddings in one model, while further extending sparse retrieval to unify text and multimodal inputs.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link24">
      <summary class="paper-row-summary">
        <span class="queue-index">25</span>
        <span class="paper-row-copy">
          <strong>CAPEval: A Decoupled Caption Evaluation across Understanding and Generation</strong>
          <small>Zhipeng Liu, Haochen Wang, Zhaoxiang Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Captioning</span>
<span class="topic-tag">Multimodal Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 25 / arXiv:2608.02589</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02589">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 only loosely: it is a benchmark/evaluation paper for captions, which is useful for multimodal learning but not a direct VLLM/embodied AI method or spatial intelligence paper.</p>
        <p class="abstract">Captions serve as a primary supervision signal for both multimodal understanding and text-to-image generation. However, previous evaluations treat the caption quality as a single scalar objective, which conflates two distinct properties: (1) how much visual information a caption covers and (2) how reliably the image supports its stated claims. To this end, we design a decoupled caption evaluation benchmark, CAPEval (Coverage And Precision Evaluation), with human-written ground-truth captions and human-verified atomic checklist items. Specifically, CAPEval decomposes caption quality into Coverage and Precision. The former quantifies how thoroughly a caption covers ground-truth factual content, while the latter reflects the factual correctness rate of all claims expressed in the caption. We select 10 captioners and further conduct controlled downstream end-to-end experiments with them from four model families, where the caption source is the only variable. Empirically, we find a consistent task-dependent dissociation: Coverage serves as the stronger correlate for understanding performance, whereas Precision acts as the dominant predictor for generation performance. This decoupled evaluation paradigm not only delivers a more fine-grained diagnosis of caption quality, but also offers actionable guidance for selecting and optimizing captioners tailored to different downstream tasks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Personalized Image Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link25">
      <summary class="paper-row-summary">
        <span class="queue-index">26</span>
        <span class="paper-row-copy">
          <strong>CopyCat: Improving Fine-Grained Subject Consistency in Subject-to-Image Models within Seconds</strong>
          <small>Peng Zheng, Ruiqi Liu, Rui Ma, Zuxuan Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Personalized Image Generation</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Fine-Grained Consistency</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 26 / arXiv:2608.00674</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.00674">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Relevant to criterion 4 in a broad sense: subject-to-image personalization and fine-grained consistency for generative vision models, but not a foundation-model paper per se.</p>
        <p class="abstract">Recent subject-to-image models have achieved impressive progress in personalized image generation, yet they still struggle to preserve fine-grained subject-specific details. A major reason is the lack of high-quality fine-grained identity supervision: real paired data are expensive to collect, while synthesized training pairs often preserve only coarse subject appearance and fail to capture subtle subject-specific details. In this work, we propose CopyCat, a lightweight model-refinement framework that improves fine-grained subject consistency within only a few seconds. CopyCat performs a one-time refinement of a pretrained subject-to-image model by attaching a lightweight Fine-grained Consistency LoRA (FCLoRA) and optimizing it using a single proxy image, which is used as both the conditioning image and the reconstruction target. This exact self-reconstruction objective substantially simplifies the optimization task, enabling effective fine-grained refinement within only a few seconds. The refinement is performed only once; the resulting model can be directly applied to diverse unseen reference subjects and prompts without further subject-specific optimization. We further revisit subject-to-image LoRA training in double-stream diffusion transformers and find that adapting only the visual stream consistently improves subject consistency. Extensive experiments on DreamBench and XVerseBench demonstrate consistent improvements in fine-grained subject consistency across representative subject-to-image models under both single- and multi-subject settings.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Surgical Video</summary>
      <div class="queue">

    <details class="paper-row" id="link26">
      <summary class="paper-row-summary">
        <span class="queue-index">27</span>
        <span class="paper-row-copy">
          <strong>Extended KAFR: A kinematic-adaptive paradigm for the efficient analysis of surgical video</strong>
          <small>Huu Phong Nguyen, Shekhar Madhav Khairnar, Ganesh Sankaranarayanan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Surgical Video</span>
<span class="topic-tag">Frame Selection</span>
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
          <span>Paper 27 / arXiv:2608.01058</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01058">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Only a loose fit to criterion 3: embodied/surgical video analysis, but mainly an efficiency frame-selection pipeline rather than a new embodied benchmark or novel spatial-intelligence method.</p>
        <p class="abstract">Artificial Intelligence is increasingly applied to surgical video analysis for phase segmentation, skill assessment, and workflow optimization. A key challenge is the length of surgical recordings, often one to several hours, creating substantial computational burden. We previously developed Kinematics-Adaptive Frame Recognition (KAFR) for robotic surgery, showing that tracking tool motion effectively identifies informative frames while filtering redundant content. However, laparoscopic surgery introduces additional challenges: manual camera control causes frequent motion artifacts, and image quality is generally lower than robotic systems. This study evaluates whether KAFR generalizes to laparoscopic surgery using the Cholec80 benchmark, comprising 80 laparoscopic cholecystectomy procedures annotated for seven surgical phases. KAFR operates in three stages: a fine-tuned YOLO model detects and segments surgical tools; frames are adaptively selected based on tool displacement or velocity variation; and an X3D model classifies selected frames into surgical phases. KAFR achieved a 91.0\% F1 score using only 0.58\% of frames for phase classification, representing an approximately seven-fold reduction compared to typical 4\% frame sampling, while maintaining performance comparable to LoViT (90.2\%) and Trans-SVNet (89.7\%). These results demonstrate that kinematics-based frame selection transfers effectively to the challenging laparoscopic environment.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Long-Video QA</summary>
      <div class="queue">

    <details class="paper-row" id="link27">
      <summary class="paper-row-summary">
        <span class="queue-index">28</span>
        <span class="paper-row-copy">
          <strong>Ground, Cover, and Refine: Evidence-Centric Frame Selection for Long-Video Question Answering</strong>
          <small>Fan Wei, Siru Zhong, Runmin Dong, Miao Yang, Zhaoyang Luo, Haohuan Fu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Long-Video QA</span>
<span class="topic-tag">Frame Selection</span>
<span class="topic-tag">Vision-Language Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 28 / arXiv:2608.01660</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01660">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 only indirectly: it is a training-free long-video QA frame-selection method for VLMs, not a new foundation model or benchmark.</p>
        <p class="abstract">Long-video question answering requires identifying sparse yet critical evidence from videos containing thousands of frames under a constrained visual-token budget. Existing methods either select query-aware frames in a single pass or rely on timestamped text solely as retrieval guidance, leading to two key limitations. First, selected frames tend to cluster around local relevance peaks, and once the budget is exhausted, omitted evidence cannot be recovered. Second, textual and visual evidence remain weakly aligned. We propose GCR, a training-free framework that casts fixed-budget frame selection as a joint evidence curation problem. Ground converts timestamped text into temporal events, selects query-relevant real frame anchors, and renders each event text onto its temporally aligned frame. Cover supplements grounded events with direct visual anchors for complementary visual evidence and applies global maximal marginal relevance to preserve diverse context. Refine revisits omitted temporal regions and replaces the weakest revisable context frame with a real-frame medoid---but only when the medoid offers greater evidence value. GCR maintains a fixed number of chronologically ordered frames and requires no VLM training or architectural modification. Experiments on LongVideoBench and Video-MME, across three 7B backbones and frame budgets of 8, 32, and 64, demonstrate consistent improvements in long-video QA. With the 7B LLaVA-OV backbone and 32 frames, GCR achieves 64.25% and 62.15% on the two benchmarks, outperforming the strongest reproduced baselines by 2.54 and 1.93 percentage points, respectively.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Interactive Segmentation</summary>
      <div class="queue">

    <details class="paper-row" id="link28">
      <summary class="paper-row-summary">
        <span class="queue-index">29</span>
        <span class="paper-row-copy">
          <strong>ISRS-DETR: Detection-Guided Click Propagation for Remote Sensing Interactive Segmentation</strong>
          <small>Thanh Duc Pham, Anh Nguyen, Duong Duc Hieu, Minh-Tan Pham</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Interactive Segmentation</span>
<span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Detection-Guided Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 29 / arXiv:2608.02468</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02468">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 weakly: it is a new method for interactive segmentation in remote sensing, but not an embodied-AI benchmark/simulator or spatial-intelligence paper.</p>
        <p class="abstract">Interactive segmentation reduces the prohibitive cost of pixel-level annotation by allowing users to delineate objects with a few clicks. However, applying this paradigm directly to remote sensing imagery is non-trivial: ultra-high resolutions, small object sizes, and sparse spatial distributions all degrade segmentation quality. Recent work has addressed the resolution barrier and achieved competitive results in interactive segmentation for remote sensing (ISRS). However, they treat all instances of a class within an image as a single objective target. Consequently, interactions spent on one object contribute nothing to its same-class neighbours, and satisfactory masks may demand up to 40 clicks per image, hindering the practicality of these frameworks. We observe that remote sensing scenes exhibit markedly strong inter-object correlation, meaning a single clicked object is highly informative about the rest of its category. Building on this, we propose ISRS-DETR, a detection-guided interactive segmentation framework that injects object-level evidence into both training and inference. Our ISRS-DETR employs an RF-DETR decoder with the interactive segmentation backbone to localise co-occurring same-class objects, and introduces a Dynamic Top-K Click Selection strategy that retains only reliable proposals and converts each into a simulated click, so one user interaction propagates across an entire class. Experiments on three standard remote sensing benchmarks show that ISRS-DETR achieves state-of-the-art accuracy while substantially reducing Number of Clicks per Image (NoC-I). All codes and data splits will be released for reproducibility upon acceptance.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Pathology Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link29">
      <summary class="paper-row-summary">
        <span class="queue-index">30</span>
        <span class="paper-row-copy">
          <strong>Understanding Synergistic Interactions among Pathology Foundation Models via Adaptive Fusion</strong>
          <small>Yuxiang Xiao, Yang Hu, Bin Li, Tianyang Zhang, Zexi Li, Huazhu Fu, Jens Rittscher, Kaixiang Yang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Pathology Foundation Models</span>
<span class="topic-tag">Adaptive Fusion</span>
<span class="topic-tag">Medical AI</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 30 / arXiv:2608.01370</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.01370">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; it is adaptive fusion of pathology foundation models, which fits vision foundation model applications broadly but not especially the requested spatial/embodied or VLLM/MLLM themes.</p>
        <p class="abstract">Pathology foundation models (PFMs) provide strong tile-level representations via self-supervised pre-training on large-scale pathology images. Yet, PFMs are developed under diverse and often opaque data, architecture, and objective choices, inducing latent representational biases that limit robustness and obscure what each model specialises in. We present AdaFusion, a lightweight adaptive fusion framework that integrates complementary signals from multiple frozen PFMs through (1) low-dimensional feature compression and (2) a sample-conditioned gating module that reweights model-wise (and optionally channel-wise) contributions. Beyond improving predictive accuracy, AdaFusion provides contribution-driven interpretation that offers evidence consistent with model-specific preferences and synergistic interactions across tissue phenotypes. We evaluate AdaFusion on three public benchmarks spanning treatment response prediction, prostate cancer grading, and spatial gene expression inference. AdaFusion consistently outperforms individual PFMs and other fusion baselines, while providing interpretable tissue visualisation which aligns model preferences with morphological patterns. Code is available at: https://github.com/xyx-98/PathoOracle.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Fusion</summary>
      <div class="queue">

    <details class="paper-row" id="link30">
      <summary class="paper-row-summary">
        <span class="queue-index">31</span>
        <span class="paper-row-copy">
          <strong>Deep Multimodal Fusion Detection through Spatial Mask and Channel Fusion</strong>
          <small>Guandi Wang, Ming Li, Yunsen Xing, Junle Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Fusion</span>
<span class="topic-tag">Object Detection</span>
<span class="topic-tag">Attention Mechanisms</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.MM</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 31 / arXiv:2608.02092</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.02092">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 only loosely: a multimodal fusion detection method, but it is not a vision foundation model or VLLM/MLLM paper, and it is not embodied AI/spatial intelligence in the sense of agents or navigation.</p>
        <p class="abstract">Deep multimodal fusion for object detection has demonstrated good performance through mining modal characteristics. However, existing feature-level fusion methods mainly weigh between two modalities and unify them in a unified representation space. This can lead to overfitting or over-specialization of the statistical properties of a single modality within a dual-backbone architecture. This paper proposes an Attention-Driven Complementarity Resampling framework for robust improvement of cross-modality object detection. Based on a shared channel spatial attention mechanism, we first introduce the semantic mask exchange to actively mix the boundaries of the modalities during the training phase, forcing the backbone network to learn generalized features without relying on fixed modal labels. Then we propose a learnable channel competition to sample and aggregate features in a channel-wise and learnable way. Our experiments on multiple datasets demonstrate that the proposed method is effective and yields competitive results among existing state-of-the-art approaches. The source code is provided in the supplementary material.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
