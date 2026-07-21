

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
      <p class="eyebrow">Daily ArXiv / July 21, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>20</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>15</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>9.9</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="8 mentions">agent</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">aligned</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">alignment</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">brain</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">consistency</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">diagram</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">diffusion</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="9 mentions">distribution</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">editing</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="7 mentions">embedding</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="7 mentions">emotion</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">encoder</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">fidelity</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="11 mentions">fine-tuning</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="9 mentions">foundation</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="8 mentions">fusion</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">generalization</span><span class="cloud-word" style="font-size:2.06rem;opacity:0.82;color:color-mix(in srgb, var(--accent-2) 64%, var(--accent))" title="16 mentions">generation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">geometric</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">geometry</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">hybrid</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">inference</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="11 mentions">interaction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">latent</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="7 mentions">localization</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="9 mentions">medical</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="7 mentions">modality</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">motion</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="10 mentions">multi-view</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="9 mentions">multimodal</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="7 mentions">optimization</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="7 mentions">region</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">robust</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">search</span><span class="cloud-word" style="font-size:1.97rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="15 mentions">segmentation</span><span class="cloud-word" style="font-size:2.15rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 68%, var(--accent))" title="17 mentions">semantic</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="7 mentions">skeleton</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="9 mentions">structural</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="25 mentions">target</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="8 mentions">textual</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="8 mentions">token</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="10 mentions">understanding</span><span class="cloud-word" style="font-size:1.69rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="12 mentions">video</span><span class="cloud-word" style="font-size:1.97rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="15 mentions">visual</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">volume</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="84 mentions">action</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="143 mentions">agent</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="75 mentions">alignment</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="58 mentions">camera</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">challenging</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">concept</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="71 mentions">consistency</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">dense</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="76 mentions">detection</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="64 mentions">diffusion</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="67 mentions">domain</span><span class="cloud-word" style="font-size:1.39rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="100 mentions">dynamic</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">environment</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="58 mentions">event</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="69 mentions">evidence</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="71 mentions">fine-grained</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="73 mentions">foundation</span><span class="cloud-word" style="font-size:2.22rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 72%, var(--accent))" title="201 mentions">generation</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="66 mentions">geometric</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">geometry</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="64 mentions">inference</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="66 mentions">interaction</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="52 mentions">knowledge</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="107 mentions">language</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">latent</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">mechanism</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">memory</span><span class="cloud-word" style="font-size:1.51rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="112 mentions">motion</span><span class="cloud-word" style="font-size:1.72rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 46%, var(--accent))" title="136 mentions">multimodal</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="60 mentions">multiple</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="119 mentions">object</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">optimization</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="59 mentions">perception</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="59 mentions">physical</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="90 mentions">pipeline</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="51 mentions">point</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="58 mentions">pose</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="79 mentions">real-world</span><span class="cloud-word" style="font-size:1.84rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="150 mentions">reasoning</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="90 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="61 mentions">region</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">robust</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="140 mentions">scene</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="75 mentions">segmentation</span><span class="cloud-word" style="font-size:2.00rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 60%, var(--accent))" title="170 mentions">semantic</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="72 mentions">space</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="114 mentions">spatial</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="59 mentions">support</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="83 mentions">target</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="95 mentions">temporal</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="95 mentions">token</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="61 mentions">trajectory</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="91 mentions">understanding</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="84 mentions">unified</span><span class="cloud-word" style="font-size:2.67rem;opacity:0.98;color:color-mix(in srgb, var(--accent-2) 95%, var(--accent))" title="270 mentions">video</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="52 mentions">view</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="52 mentions">vision</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="64 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="286 mentions">visual</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="83 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>15 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>SAMRI-3D: Adapting SAM2 for 3D MRI Segmentation with Global Volume Tokens</strong>
          <small>Zhao Wang, Wei Dai, Hongfu Sun, Craig Engstrom, Shekhar S. Chandra</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Medical Segmentation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">3D Adaptation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2607.18014</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.18014">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it adapts a vision foundation model (SAM2) to 3D MRI segmentation and introduces a new benchmark plus a zero-cost token-based method.</p>
        <p class="abstract">Foundation models such as Segment Anything Model 2 (SAM2) have transformed natural-image and video segmentation, and recent work has begun adapting them to medical imaging. These adaptations, however, are largely general-purpose models that treat MRI as one modality among many; large-scale, MRI-specific modelling and benchmarking remain limited, even though MRI&#x27;s low soft-tissue contrast leaves many boundaries effectively invisible on individual slices. We present SAMRI-3D, a benchmark and method for 3D MRI segmentation with SAM2. The SAMRI-3D benchmark is the largest MRI-only evaluation to date - 10,392 volumes from 34 datasets (27 public, 7 in-house) spanning 12 anatomical domains and 10+ sequences, with explicit seen/unseen splits. Freezing the image encoder and fine-tuning only the lightweight decoder and memory modules raises mean Dice from 0.58 (zero-shot SAM2) to 0.76, surpassing recent SAM-based medical models (SAMed-2 0.69, Medical-SAM2 0.49, SAM-Med3D 0.37) with strong statistical significance. To target invisible boundaries, we introduce Global Volume Tokens (GVT): persistent memory tokens trained with a Truncated Signed Distance Field (TSDF) reconstruction objective that is discarded at inference (zero added cost). This full model, SAMRI-3D, attains the best accuracy (0.78) and lowest variance across all 34 datasets and, uniquely, shows no drop on 8 held-out datasets (0.79 unseen vs. 0.78 seen); per-sequence analysis confirms the TSDF objective helps most where per-slice contrast is weakest. We will release the benchmark, code, and models in this paper.</p>
      </div>
    </details>


    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>SciForma: Structure-Faithful Generation of Scientific Diagrams</strong>
          <small>Yuxuan Luo, Peng Zhang, Xinjie Zhang, Xun Guo, Zhouhui Lian, Yan Lu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Diagram Generation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.GR</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2607.18091</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.18091">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and criterion 4 very closely: it introduces a new generative model and benchmark for structure-faithful scientific diagram generation.</p>
        <p class="abstract">Structural fidelity is essential to scientific methodology diagrams. To communicate research logic, these diagrams must faithfully render components, directional relations, and textual annotations. Since a single error, such as a reversed arrow or an unreadable equation, can invalidate the entire figure, structural fidelity is inherently conjunctive: correctness on one axis cannot compensate for failure on another. Current open-source models fail to satisfy this criterion. Supervised fine-tuning (SFT) learns plausible layouts but cannot reliably ensure structural correctness, while scalar reward-based post-training obscures which structural dimension has failed. To address this, we introduce SciForma, a framework for the structure faithful generation of scientific methodology diagrams. Specifically, SciForma decomposes diagram quality into three structural axes: Component, Arrow, and Text, guided by a structural inventory. Built on this foundation, we curate SciFormaData-700K for structured training and SciFormaBench-2K for logic-verified evaluation. To close the gap left by SFT, we develop Multi-Dimensional Conjunctive Preference Optimization (M-DPO), which enforces simultaneous correctness across all axes and adaptively routes gradients to the most deficient dimension in post-training. The same structural inventory also enables iterative editing at inference time to correct residual errors. This combination allows SciForma-9B to exceed all open-source baselines and GPT-Image-1.5 on both SciFormaBench-2K and AIBench, bringing open scientific diagram generation close to proprietary-level structural fidelity. Our code and data will be available at: https://github.com/microsoft/SciForma.</p>
      </div>
    </details>


    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>RegionFM: Interpretable Region-Based Brain MRI Classification Using Foundation Model Embeddings</strong>
          <small>Wei Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Medical Imaging</span>
<span class="topic-tag">Interpretability</span>
<span class="topic-tag">MRI Classification</span>
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
          <span>Paper 4 / arXiv:2607.16325</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.16325">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it applies foundation-model embeddings to a medical vision task with an anatomically interpretable design.</p>
        <p class="abstract">Foundation models provide powerful representations for brain MRI analysis, but their predictions remain difficult to interpret in anatomically meaningful terms. Clinical assessment of brain MRI is commonly organized around anatomically defined structures and regional abnormalities, whereas conventional explanation methods typically produce voxel- or patch-level importance maps that do not explicitly quantify the contributions of individual brain regions. To address this mismatch, we propose RegionFM, an interpretable framework that integrates anatomical segmentation with brain MRI foundation-model embeddings. RegionFM first divides each MRI scan into anatomical regions and constructs a separate MRI volume for each region. A frozen foundation model then encodes each region into an embedding, and a region-additive logistic model combines these embeddings such that every anatomical region contributes an explicit scalar term to the final prediction. This formulation supports both subject-level and cohort-level analyses of regional contributions. We evaluate RegionFM on cognitive-impairment classification using embeddings from multiple pretrained brain MRI foundation models. The results show that RegionFM maintains performance comparable to less interpretable fine-tuning approaches while providing anatomically grounded explanations. Randomized embedding ablations yield near-chance performance, indicating that the predictions rely on meaningful structure captured by the foundation-model embeddings rather than simple feature statistics. Overall, RegionFM better aligns model explanations with anatomy-based clinical reasoning while maintaining competitive predictive performance.</p>
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
          <strong>HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis</strong>
          <small>Lingwei Dang, Juntong Li, Zonghan Li, Hongwen Zhang, Liang An, Wei Min, Yebin Liu, Qingyao Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Hand-Object Interaction</span>
<span class="topic-tag">Multi-view Generation</span>
<span class="topic-tag">3D Motion</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2607.17097</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17097">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied-AI-adjacent HOI synthesis method with a strong simulator/generation angle and multi-view 3D motion consistency, emphasizing a novel geometry-aware direction.</p>
        <p class="abstract">Hand-Object Interaction (HOI) synthesis is a cornerstone for animation production and embodied AI. Despite the strong priors of video foundation models, multi-view consistent HOI synthesis remains challenging due to complex hand motions and occlusions. We present HarmoHOI, a unified diffusion framework that jointly and harmoniously generates synchronized multi-view HOI videos and globally aligned 3D point tracks. Our core insight is that robust multi-view consistency fundamentally requires globally aligned 3D geometry and motion. To this end, we propose a Mixture of Multi-view Diffusion Transformer that co-models RGB videos and 3D point tracks. By representing point tracks as pseudo-videos, we align 3D geometric signals with the 2D latent space of foundation models, thereby minimizing the domain gap and easing adaptation of priors. To further ensure geometry consistency, we introduce Global Motion Aligning Diffusion, which refines coarse point tracks into metric-scale, globally aligned 3D trajectories. HarmoHOI enables on-the-fly co-evolution of 2D appearance and 3D motion during denoising. To overcome the scarcity of multi-view HOI data, we employ a hybrid data curriculum learning strategy that successfully transfers generic priors from single-view data to synchronized multi-view generation. Experimental results show that HarmoHOI achieves state-of-the-art performance in visual quality, motion plausibility, and multi-view geometric consistency. Project page available at https://droliven.github.io/HarmoHOI_project.</p>
      </div>
    </details>


    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Understanding From Human Perspective: A Multi-agent System for Interactive Egocentric Medical Image Segmentation</strong>
          <small>Rongjun Ge, Dongyang Wang, Heng Zhu, Zhirui Li, Yang Chen, Yuting He</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Egocentric Segmentation</span>
<span class="topic-tag">Multi-Agent Systems</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2607.17341</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17341">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: an embodied/interactive segmentation method for egocentric video with a multi-agent workflow.</p>
        <p class="abstract">Interactive egocentric medical image segmentation (IEMIS) plays an important role in smart-glasses-assisted medical image review, segmenting the medical targets a clinician refers to from their egocentric view. Once it succeeds, the object-level visual evidence it provides strengthens the review and underpins fine-grained analysis and clinical decision-making. However, the instruction and the video both come from the user&#x27;s egocentric perspective, which poses two challenges. (1) Semantic ambiguity leaves the model unable to confirm the user-intended target. (2) Visual variability makes the segmentation jump from frame to frame. In this paper, we propose EgoMed-Agent, a multi-agent system that understands the target from the human perspective through two workflows. (1) The \textit{Target Confirmation Workflow} grounds the instruction against candidate targets with a reliability score, confirming the target when the grounding is reliable and asking the user to clarify when it is not, thereby confirming the segmentation target. (2) The \textit{Localization-Guided Propagation Workflow} couples mask propagation with per-frame target localization, using the localized target to correct the propagated mask whenever the two diverge, so the segmentation stays on the target across the egocentric video. Extensive experiments show that EgoMed-Agent reaches 71.34\% average Dice, far above the best text-prompted baseline (11.70\%). Our code is available at \href{https://github.com/wdyyyyyy/EgoMed-Agent}{our project page}.</p>
      </div>
    </details>


    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>STAR: Skeletal Token Alignment and Rearrangement for Interaction Recognition</strong>
          <small>Yuhang Wen, Mengyuan Liu, Zixuan Tang, Junsong Yuan, Sirui Li, Beichen Ding</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Interaction Recognition</span>
<span class="topic-tag">Skeleton-Video Fusion</span>
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
          <span>Paper 11 / arXiv:2607.17342</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17342">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: this is an embodied/3D interaction recognition method using skeletal + RGB cues for human-robot and human-human interactions.</p>
        <p class="abstract">Understanding physical human-robot and human-human interactions is a challenging yet emerging topic in 3D vision. While most existing methods rely on skeleton sequences--effective in low-light and privacy-sensitive environment--they face two major challenges: 1) learning and effectively exploiting interaction cues from skeletal data, and 2) compensating for the lack of visual information absent in skeletons alone. To address these challenges, we propose skeletal token alignment and rearrangement (STAR) for human-robot and human-human interaction recognition. It learns interaction-specific skeleton features and enriches them using visual cues by aligning skeleton and RGB video representations in a shared latent space. Specifically, STAR consists of three key components. First, we design a skeleton encoder that captures fine-grained interdependencies using Entity Rearrangement (ER) and Interactive Spatiotemporal Tokens (ISTs). Second, we present Visual Interaction Encoding that introduces a Focus on Interactions (FoI) strategy to attend to spatiotemporal regions relevant to interactions in RGB videos. Finally, these representations are aligned via a contrastive learning objective, with a refinement head further refines predictions. During training, STAR leverages both skeleton and RGB video data to learn robust, discriminative interaction representations. At inference time, it operates on skeletons alone, retaining visual-informed benefits while preserving skeleton-only efficiency. Extensive experiments on Chico, HARPER, NTU Mutual 11 and 26 datasets consistently validate our approach by demonstrating superior performance over state-of-the-art methods. Our code is publicly available at https://github.com/Necolizer/STAR.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Monocular Depth Estimation</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>DepthART: Scaling Foundation Monocular Depth to Tiny Models</strong>
          <small>Feng Xue, Wu Chen, Mingshuai Zhao, Guofeng Zhong, Anlong Ming, Haozhe Wang, Dianqiao Lei, Zhaowen Lin, Haiyang Zhang, Nicu Sebe</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Monocular Depth Estimation</span>
<span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">On-Device AI</span>
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
          <span>Paper 6 / arXiv:2607.17099</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17099">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 well: it advances a geometric vision foundation-model line for monocular depth estimation by scaling it to tiny on-device models.</p>
        <p class="abstract">Recent geometric foundation models (e.g., Metric3D, Depth Anything and UniDepth) have substantially improved monocular depth estimation (MDE) in both cross-scene generalization and metric-scale prediction, yet these gains have not translated to tiny models. We bridge this gap with DepthART (Depth Anything Rethought for Tiny Models), which is a compact MDE model for on-device deployment across diverse scenes. We first identify two capacity-driven bottlenecks in tiny models: (i) overfitting to dataset-specific distribution bias and (ii) unstable metric adaptation under camera shift, where full fine-tuning easily damages transferable geometry. Accordingly, DepthART combines two simple but effective strategies: a bias-resistant data sampling scheme to reduce distribution bias under the same training budget, and a camera-conditioned fine-tuning protocol that freezes the distilled encoder and adjusts metric scale conditioned on intrinsics while better preserving cross-dataset generalization. Across datasets, DepthART consistently surpasses previous tiny baselines in both zero-shot generalization and metric accuracy (e.g., zero-shot $\delta_1$=0.964 for DepthART-S on NYUD v2), and in some cases approaches heavy models. We further provide a scalable model family, with DepthART-S reaching 347/245 FPS (strict FP32) on an RTX A6000 at $224^2/448^2$, 102 FPS (TF32) on a Orin NX 8GB, and over 15 FPS (FP32) on a Jetson Nano 4GB.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM Integration</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>HOMIE: Human-object Centric Video Personalization via Multimodal Intelligent Enchancement</strong>
          <small>Yiyang Cai, Nan Chen, Rongchang Xie, Junwen Pan, Chunyang Jiang, Cheng Chen, Wen Zhou, Zhenbang Sun, Wei Xue, Wenhan Luo, Yike Guo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM Integration</span>
<span class="topic-tag">Video Generation</span>
<span class="topic-tag">Human-Object Interaction</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2607.18217</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.18217">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it proposes a new MLLM-integrated framework for human-object centric video personalization.</p>
        <p class="abstract">Human-object centric video personalization (HOCVP) is a core task within subject-driven video generation. However, existing methods suffer from two key limitations. First, most approaches focusing on inter-subject personalization still struggle to strike a balance between high subject fidelity and accurate interaction patterns between humans and diverse objects, especially when objects represent abstract concepts such as logos. Second, while intra-subject references (e.g., OCR maps, multi-view inputs) are expected to enhance subject fidelity, most existing works lack mechanisms to understand such latent correspondence. To address both challenges, we propose HOMIE, an HOCVP framework that tackles both inter- and intra-subject input settings in a unified manner. Compared to previous approaches, HOMIE proposes a better MLLM integration strategy to extract knowledge of reference-level relationships without compromising the controllability of text encoders or incurring costly re-alignment. Specifically, we introduce global multimodal guidance within self-attention to better align MLLM-derived semantic features with VAE tokens. Furthermore, we propose modality-reference embedding to differentiate tokens from MLLM features and VAE tokens and associate intra-subject reference image tokens. Extensive experiments validate that our method achieves state-of-the-art performance across various HOCVP tasks. Project Page: https://yiyangcai.github.io/homie-page.github.io/</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Relighting</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Consistent Feature Transport for Image Relighting</strong>
          <small>Bohan Zhang, Huanwei Liang, Yuhan He, Hongteng Xu, Quxiao Chao, Luoqi Liu, Dixin Luo, Ting Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Relighting</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Feature Transport</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2607.17833</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17833">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: it is a vision foundation-model-adjacent generative editing method for image relighting, with a new transport formulation.</p>
        <p class="abstract">Image relighting modifies illumination while preserving non-lighting content such as identity and geometry. Existing diffusion-based methods often suffer from unstable illumination changes or inconsistent content preservation under complex lighting, as they lack an explicit mechanism to learn feature transformations between images. We reformulate relighting as an illumination feature transport problem and introduce Consistent Feature Transport (CFT), a training principle that explicitly enforces illumination-consistent transport between source and target image distributions. Built upon rectified flow, CFT jointly models noise-to-image generation and illumination-consistent source-to-target transport through trajectory-level supervision. This dual-transport formulation encourages isolation of illumination-specific variations while preserving content-aligned features. To support complex lighting scenarios, we construct a large-scale portrait relighting dataset with diverse relighting effects. Experiments show consistent improvements over existing state-of-the-art relighting approaches and demonstrate that CFT can generalize to other editing tasks, including style transfer. Code is available at https://github.com/Dixin-Lab/CFT.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Simple Domain Generalization for Strong Pixel-Level Image Tampering Detection in Modern VLMs</strong>
          <small>Yi Tang, Xinyi Shang, Jiacheng Cui, Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao, Tran Dinh Tien, Ahmed Elhagry, Salwa K. Al Khatib, Tianjun Yao, Yonina C. Eldar, Jing-Hao Xue, Hao Li, Salman Khan, Zhiqiang Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Tampering Detection</span>
<span class="topic-tag">Domain Generalization</span>
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
          <span>Paper 10 / arXiv:2607.18230</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.18230">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it is about robust pixel-level tampering detection on modern VLM-generated images, an application built around vision-language foundation models.</p>
        <p class="abstract">Modern vision-language models (VLMs) have significantly improved image generation and editing capabilities, making pixel-level image tampering detection increasingly important yet challenging under cross-model and out-of-distribution shifts. This work studies domain generalization for pixel-level image tampering detection in modern VLMs like ChatGPT, Gemini, Qwen-Image, etc., aiming to learn tampering localization models that remain robust across diverse VLM-generated manipulation distributions. We propose a simple yet effective domain-generalized training framework built on two practical strategies. First, we introduce a balanced minibatch sampling scheme that strategically samples tampered and real images in each minibatch, preventing biased optimization toward either manipulated artifacts or clean-image priors and avoiding training collapse, ensuring that each optimization step receives proper sampled gradient signals. Second, we adopt a simple late-injection strategy, where the detector is first trained on large-scale base data until stable convergence, and then exposed to a small amount of newly selected supporting data from emerging VLM distributions, improving adaptability without overfitting to limited new domains. Together, these components provide a simple yet strong recipe for improving pixel-level tampering localization and OOD robustness across modern VLMs. Despite the conceptual simplicity, our framework outperforms the prior state-of-the-art PIXAR by a large margin of 26.1% and 26.8% relative improvement in average gIoU and cIoU, respectively, across OOD VLMs of GPT-Images-2.0, Gemini-3.1, FLUX.2, and Seedream 4.5. Our code is available at https://github.com/VILA-Lab/PIXAR-DG</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Reconstruction</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>TopoGS: Planar Reconstruction via Topology-aware 3D Gaussian Splatting</strong>
          <small>Shanshan Pan, Jiale Chen, Yilin Liu, Hui Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Gaussian Splatting</span>
<span class="topic-tag">Topology-aware Geometry</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.GR</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2607.16838</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.16838">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Only a partial match to criterion 4: it is a 3D reconstruction method, but it does not center on vision foundation models or embodied agents.</p>
        <p class="abstract">Extracting structured, parametric 3D representations from raw images remains a fundamental challenge in computer vision and graphics. While recent advancements in the 3D Gaussian Splatting (3DGS) pipeline integrate planar primitives to yield compact and editable geometry, these approaches typically treat planes as isolated, discrete sets. This lack of topological connectivity hinders robust geometric reasoning, leading to fragmented reconstructions and misaligned boundaries that fall short of the precision for rigorous spatial analysis and professional design workflows. To address this, we introduce TopoGS, the first 3DGS framework to explicitly integrate both planar and topological constraints for coherent 3D reconstruction. Specifically, we extract global 2D topological relationships from multi-view image segmentations and anchor Gaussian primitives to these structural elements. This formulation enables the joint optimization of plane parameters, rendering fidelity, and topological adjacency. By enforcing strict multi-view consistency alongside these topological constraints, our method significantly mitigates geometric misalignments and produces connected, structured 3D models. Extensive evaluations on the ScanNet++ dataset demonstrate that TopoGS achieves state-of-the-art performance, providing a highly robust solution for generating accurate, topologically sound, and visually faithful scene representations.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Unified Multimodal Models</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>STBridge: Shared-Target Alignment for Bridging Understanding and Generation in UMMs</strong>
          <small>Ye Wang, Hongjun Wang, Hao Fang, Tongyuan Bai, Zuwei Long, Peixian Chen, Wei Liu, Weibo Gu, Xing Sun, Rui Ma</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Unified Multimodal Models</span>
<span class="topic-tag">Image Editing</span>
<span class="topic-tag">Understanding-Generation Alignment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2607.17140</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17140">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and criterion 4 somewhat: it studies unified multimodal models and their understanding-generation alignment for image editing.</p>
        <p class="abstract">Unified multimodal models (UMMs) aim to integrate visual understanding and generation within a single architecture, but architectural unification alone does not ensure semantic consistency. A model may describe the intended target correctly while generating an inconsistent edit. This exposes an understanding-generation alignment gap: linguistic and visual outputs live in different spaces, yet should be governed by the same target semantics. We study this gap in image editing, where an instruction defines a target state that can be both described and visually realized. Given a source image and an edit instruction, we compare a UMM&#x27;s target caption with its edited image to test whether the two outputs converge on the same result. Our analysis shows that existing UMMs remain weakly aligned, especially for fine-grained entities, attributes, spatial relations, and local details, indicating that semantic unification is not achieved by architecture alone. To bridge this gap, we propose STBridge, a shared-target alignment framework that connects understanding and generation through a common target state. Here the target caption expresses the desired visual result, while the edited image realizes it visually, replacing separate task-specific paths with a shared information flow from target expression to target realization. STBridge follows an align-then-optimize strategy: supervised fine-tuning first establishes the shared-target channel, and sequential reinforcement learning further refines target-centered coordination. Across visual understanding, image generation, and image editing benchmarks, STBridge consistently improves over the initialization model. Alignment analysis confirms that STBridge narrows the gap between what the model describes and what it generates, demonstrating shared-target alignment as an effective post-training strategy for bridging understanding and generation in UMMs.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Diffusion Models</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>MixDiffusion: Mixing Diffusion-based Uni-condition Text-to-Image Generation Models for Multi-condition Image Synthesis</strong>
          <small>Pengcheng Wan, Liang Han, Lin Xu, Bowen Xiao, Liqiang Nie</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Controllable Generation</span>
<span class="topic-tag">Multi-Condition Synthesis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2607.17634</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17634">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: it is a diffusion-based multi-condition image synthesis method, but it is not specifically a vision foundation model paper.</p>
        <p class="abstract">Recent advances in text-to-image (T2I) generation have enabled controllable image synthesis by incorporating conditions beyond text. However, most existing diffusion-based methods are limited to a single type of control condition (e.g., bounding boxes or keypoints), which restricts their flexibility. To address this limitation, we propose MixDiffusion, a training-free diffusion framework for multi-condition T2I generation. MixDiffusion theoretically supports an arbitrary number of control conditions, including bounding boxes, keypoints, sketches, depth maps, reference images, and text, by collaboratively integrating multiple pre-trained uni-condition diffusion models. The key insight of the proposed approach is to derive the predicted noise distribution in each denoising step of the diffusion-based multi-condition image generation model from the predicted noise distributions of multiple diffusion-based uni-condition models with a derived integration formula, which is supported by rigorous theory proof. Owing to its training-free nature, MixDiffusion is easy to deploy and readily extensible to new control modalities.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Emotion</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>SpEmoC: A Balanced Speaker-Segment Multimodal Emotion Benchmark</strong>
          <small>Sania Bano, Shahzad Ahmad, Santosh Kumar Vipparthi, Sukalpa Chanda, Subrahmanyam Murala</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Emotion</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Dataset Design</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2607.18109</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.18109">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to the listed criteria; it is a multimodal emotion benchmark, which is adjacent to multimodal learning but not specifically criterion 2, 3, or 4.</p>
        <p class="abstract">Understanding human emotions in spoken conversations is a key challenge in affective computing, with applications in empathetic AI, human computer interaction, and mental health monitoring. However, existing datasets vary in scale, emotion distribution, modality alignment, and data partitioning strategies, which can influence reliable cross-dataset generalization and minority-emotion modeling. We introduce SpEmoC a Speaking segment Emotion for Conversations comprising 306,544 raw clips from 3,100 English language movies and TV series. From these, 30,000 high quality, class balanced clips are curated, featuring synchronized visual, audio, and textual modalities annotated for seven emotions through a hybrid pipeline that integrates pretrained models with human validation. SpEmoC uses strict movie- and series-level splits to prevent content overlap between split sets, allowing more reliable evaluation of model generalization. The dataset also maintains a near-balanced distribution across seven emotions, including minority classes such as Fear and Disgust, which supports more balanced learning across categories. Extensive experiments, including in-domain benchmarking, cross-dataset transfer, low-data training, class-imbalance analysis, and modality transfer show that balanced data and careful splitting lead to more stable performance across emotions when models are evaluated on other datasets. These results highlight the importance of dataset design for robust and transferable multimodal emotion recognition.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical AI</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>Localization-Infused Vision-Language Semantic Fusion for Text-Guided Medical Image Segmentation</strong>
          <small>Songyue Han, Mingye Zou, Shuchang Ye, Lei Bi, Mingyuan Meng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical AI</span>
<span class="topic-tag">Vision-Language Segmentation</span>
<span class="topic-tag">Semantic Fusion</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2607.16327</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.16327">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: this is a vision-language method for text-guided medical image segmentation, an application of multimodal models rather than a foundation model paper.</p>
        <p class="abstract">Medical image segmentation is essential for modern computer-aided medicine. Recently, text-guided segmentation has shown promise by incorporating clinician-formulated textual reports as semantic guidance for image segmentation. These reports describe target appearance, location, and neighboring anatomy, providing explicit guidance for localization and delineation. Existing text-guided segmentation methods typically extract textual semantics implicitly through a pretrained text encoder and then integrate vision-language semantics via straightforward image-text feature fusion. However, these methods do not explicitly capture target-oriented information embedded in textual reports, particularly target location, and do not explore multi-level information fusion strategies beyond basic feature-level fusion, limiting the extraction and integration of critical textual semantics. In this study, we propose LoG, a localization-infused vision-language fusion framework for text-guided medical image segmentation. By jointly performing multi-scale target localization tasks, LoG explicitly captures target-oriented vision-language semantics and enables three-level localization-infused semantic fusion: (i) localization-guided feature fusion that directly infuses location-relevant semantics into visual features, (ii) localization-gated attention fusion that redirects multi-scale localization predictions to reinforce critical regions, and (iii) localization-constrained loss fusion that supervises segmentation based on spatial consistency with target localization. Extensive experiments on three benchmark datasets, involving three medical imaging modalities with paired textual reports, demonstrate that LoG achieves Dice scores of 91.59%, 80.71%, and 94.59% on QaTa-COV19, MosMedData+, and Kvasir-SEG, respectively, consistently outperforming state-of-the-art medical image segmentation methods.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>5 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Foundation Model</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Pailitao-MMSearch: Building Native E-Commerce Multimodal Search Foundation</strong>
          <small>Xiaohan Ye, Xu Chen, Zihan Gong, Jian Ding, Lianyu Du, Baicheng Chen, Yunmeng Shu, Jingqian Zhao, Zhixiang Zhao, Shuaiqi Jia, Chong Ma, Shuwen Xiao, Xiangheng Kong, Yuan Gao, Jun Song, Jinsong Lan, Xiaoyong Zhu, Bo Zheng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Foundation Model</span>
<span class="topic-tag">E-Commerce Search</span>
<span class="topic-tag">Vision-Language Retrieval</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2607.17499</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17499">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: this is a new native multimodal foundation model for e-commerce multimodal search.</p>
        <p class="abstract">The evolution of e-commerce has fundamentally transformed how users search for products, shifting from simple text-based keyword queries to complex multimodal interactions that seamlessly combine product images, natural language descriptions, and mixed-intent instructions. However, existing approaches face a critical dilemma: single-modal specialist models, deployed independently for text retrieval, visual search, and voice recognition, operate in isolation and cannot handle cross-modal queries, while general-purpose vision-language models lack the domain-specific knowledge necessary for fine-grained product understanding, user behavior modeling, and commercial intent reasoning. In this work, we present Pailitao-MMSearch, one native e-commerce multimodal search foundation model designed to bridge this gap. Our approach introduces three key innovations: (1)HybSID (Hybrid Semantic ID);(2)a two-stage continual pre-training strategy; and (3)a hybrid reasoning post-training pipeline. Built upon Qwen and deployed on Taobao&#x27;s Pailitao multimodal search platform, Pailitao-MMSearch achieves substantial improvements in online A/B testing, including up to +13.61\% in Gross Merchandise Volume (GMV) and +8.21\% in transaction volume compared to traditional multi-modal search pipeline, demonstrating the effectiveness of our native e-commerce multimodal search large language models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Representation</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>From Modalities to Propositions: A Language-Centric Framework for Multimodal Intelligence</strong>
          <small>Nadine Chang, Maying Shen, Shizhe Diao, Jialiang Wang, Jingde Chen, Thomas Breuel, Pavlo Molchanov, Rafid Mahmood, Jose M. Alvarez</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Representation</span>
<span class="topic-tag">Scene Propositions</span>
<span class="topic-tag">Cross-modal Retrieval</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
<span class="category-tag">cs.MM</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2607.16560</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.16560">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to the listed criteria; it is a multimodal intelligence framework, but not clearly a new VLLM/MLLM or embodied-AI benchmark/method in the sense of criteria 2 or 3.</p>
        <p class="abstract">We propose a language representation for multimodal data in which any observation, whether image, video, or text, is expressed as a bag of atomic propositions, simple statements about the entities, actions, and relations in a scene. A global semantic codebook unifies these into a shared vocabulary of canonical atomic propositions, placing every modality and observation into one interpretable space that spans fine grained facts to high level concepts and composes into richer ones. This brings interpretability with reasoning, cross-modal understanding and retrieval, and compositionality that enables complex multimodal understanding, rich data curation and complex structured retrieval. We demonstrate the framework on autonomous driving and open-world data.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Text-to-Image</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>Dynamic Defense Profiling Enables Cognitive Jailbreak of Text-to-Image Models</strong>
          <small>Dongdong Yang, Deyue Zhang, Zhao Liu, Zonghao Ying, Wenzhuo Xu, Jiankai Jin, Xiangzheng Zhang, Quanchen Zou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Image</span>
<span class="topic-tag">Safety &amp; Jailbreaks</span>
<span class="topic-tag">Generative Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2607.17779</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17779">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 only indirectly: it studies attacks on text-to-image models, which are vision generative models, but the paper is primarily about jailbreaks and safety rather than foundation-model applications.</p>
        <p class="abstract">Text-to-Image (T2I) generative models have achieved remarkable progress in synthesizing high-quality visual content, yet they remain vulnerable to adversarial misuse, particularly in generating Not-Safe-For-Work (NSFW) images. Most existing jailbreak attacks primarily rely on heuristic prompt engineering or black-box optimization, treating model feedback as a binary signal (success or failure). This coarse-grained paradigm overlooks the rich information embedded in diverse failure modes, such as textual refusal, visual blocking, and semantic sanitization, resulting in inefficient exploration and severe semantic collapse.   In this paper, we propose MIND, a cognitive jailbreak framework that reframes adversarial prompt generation as a belief-state inference problem over latent defense mechanisms. Instead of blindly searching for bypass prompts, MIND actively models the target system&#x27;s latent defense mechanisms by interpreting multi-modal feedback as high-density signals. Specifically, the framework integrates three core components: (1) a Multi-modal Judge for fine-grained feedback decomposition, (2) a Defense Profiler for iterative belief updating, and (3) a Meta-Memory module for retrieving historically effective attack strategies. These components are unified within a reasoning-driven evolutionary optimization process, enabling adaptive and semantically consistent jailbreak generation. Extensive experiments on the I2P benchmark demonstrate the effectiveness of MIND. Under six representative pre-processing and post-processing defense settings applied to the Stable Diffusion v1.5 model, MIND achieves an Attack Success Rate (ASR) of 95.62%, significantly outperforming existing methods. Additionally, the effectiveness of the proposed framework is validated across four widely used commercial T2I systems, achieving the highest ASR of 91.58% on Wan-2.5.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Hallucination Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Diversity-Oriented Fine-Tuning for Uncertainty-Based Hallucination Detection</strong>
          <small>Qiuyuan Li, Hongliang Dai, Piji Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Hallucination Detection</span>
<span class="topic-tag">Fine-Tuning</span>
<span class="topic-tag">Uncertainty Estimation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2607.16643</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.16643">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; it is about hallucination detection fine-tuning for multimodal/LLM outputs, which is adjacent to criterion 2 but not a new VLLM/MLLM method itself.</p>
        <p class="abstract">Existing hallucination detection methods are typically conducted at the inference stage, without making any modifications to the model itself. In this paper, we are interested in exploring fine-tuning strategies that enhance the detectability of hallucinations in the resulting model. Focusing on semantic-entropy-based detection, we observe that many erroneous outputs remain undetected because the model produces nearly identical incorrect answers across multiple runs. To address this, we propose diversity-oriented fine-tuning to encourage more varied generations. We introduce two specific strategies: one based on Supervised Fine-Tuning (SFT) and the other on Direct Preference Optimization (DPO). Extensive experiments are conducted to evaluate our approach and analyze the behavior of the models before and after fine-tuning. We find that after adopting our fine-tuning methods, the models become less likely to produce low semantic entropy responses for hallucinated answers, thereby improving the effectiveness of hallucination detection, eventually yielding results better than or comparable with state of the art methods. The code will be publicly released.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Long-Context Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>Is Progressive Disclosure All You Need for Long-Context Agents?</strong>
          <small>Yifeng He, Yinzhe Zhao, Jicheng Wang, Hao Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Long-Context Agents</span>
<span class="topic-tag">Retrieval</span>
<span class="topic-tag">Agentic Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.SE</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 20 / arXiv:2607.17598</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.17598">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only loosely: it studies agentic long-context document navigation and progressive disclosure, but it is not an embodied AI benchmark/method paper.</p>
        <p class="abstract">Long-document question answering usually forces a choice between loading the whole document into the context window and bolting on a separate retriever. Agentic AI suggests a broader option, giving the agent the document path and letting it decide how and what to read. Agent Skills, a standard for packaging expertise into folders an agent loads on demand, supply a ready mechanism: progressive disclosure, which exposes only what a query needs, from a short description down to the specific passages. Practitioners rapidly adopted this pattern for book-length understanding tasks, but the evidence to support such choices has been anecdotal. We run the first controlled study of the pattern, comparing raw-document navigation and several designs of Agent Skills packs against a classical hybrid retriever across three agent harnesses and three model families on InfiniteBench. On a single book, the gain depends on the harness, running large when the agent navigates the raw document poorly but near zero when a strong agent harness already divides and retrieves on its own. When scaling up to tasks that span many books, raw-document navigation collapses while one-level progressive disclosure degrades more slowly and pulls ahead. A second, deeper routing level never helps and sometimes breaks accuracy outright, so one level is enough. Progressive disclosure buys context, not intelligence: it is redundant while a strong agent can locate the right passages itself, and decisive once the corpus grows too large to navigate by reading.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-07-03.html">
          <span>July 03, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-02.html">
          <span>July 02, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-01.html">
          <span>July 01, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-30.html">
          <span>June 30, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-29.html">
          <span>June 29, 2026</span>
        </a>


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
