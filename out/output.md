

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
      <p class="eyebrow">Daily ArXiv / November 18, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>13</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>16</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>10.8</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">agent</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">alignment</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">average</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">camera</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">cost</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">decoder</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">discriminative</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">dynamic</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="9 mentions">encoder</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">generated</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">generation</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">generative</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">generator</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">guidance</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">hand</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">harness</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">height</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">inference</span><span class="cloud-word" style="font-size:2.58rem;opacity:0.95;color:color-mix(in srgb, var(--accent-2) 90%, var(--accent))" title="17 mentions">latent</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">loss</span><span class="cloud-word" style="font-size:2.03rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 62%, var(--accent))" title="12 mentions">motion</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">object</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">pair</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">perceptual</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">point</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">reasoning</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="9 mentions">reconstruction</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">render</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">reward</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">same</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">scene</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">semantic</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">simulation</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">skill</span><span class="cloud-word" style="font-size:2.15rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 68%, var(--accent))" title="13 mentions">spatial</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">starting</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">static</span><span class="cloud-word" style="font-size:2.03rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 62%, var(--accent))" title="12 mentions">step</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">support</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">textual</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">thought</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="19 mentions">video</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">view</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="10 mentions">visual</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="77 mentions">action</span><span class="cloud-word" style="font-size:2.42rem;opacity:0.91;color:color-mix(in srgb, var(--accent-2) 82%, var(--accent))" title="146 mentions">agent</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="46 mentions">alignment</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="45 mentions">answer</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="39 mentions">attention</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="47 mentions">camera</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="41 mentions">change</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="45 mentions">control</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="51 mentions">detection</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="44 mentions">diffusion</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="37 mentions">domain</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="36 mentions">dynamic</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="40 mentions">environment</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="47 mentions">error</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="75 mentions">evidence</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="35 mentions">foundation</span><span class="cloud-word" style="font-size:2.00rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 60%, var(--accent))" title="109 mentions">generation</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="42 mentions">generative</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="37 mentions">geometric</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="37 mentions">geometry</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="47 mentions">inference</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="46 mentions">interaction</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="47 mentions">language</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="55 mentions">latent</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="69 mentions">memory</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="43 mentions">motion</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="55 mentions">multimodal</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="40 mentions">multiple</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="76 mentions">object</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="38 mentions">observation</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="39 mentions">pair</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="47 mentions">physical</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="65 mentions">point</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="54 mentions">policy</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="35 mentions">produce</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="49 mentions">prompt</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="47 mentions">question</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="75 mentions">reasoning</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="44 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="38 mentions">region</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="36 mentions">reward</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="60 mentions">same</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="69 mentions">scene</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="35 mentions">segmentation</span><span class="cloud-word" style="font-size:1.83rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="96 mentions">semantic</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="38 mentions">space</span><span class="cloud-word" style="font-size:1.33rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="62 mentions">spatial</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="40 mentions">step</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="50 mentions">structure</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="40 mentions">supervision</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="53 mentions">support</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="39 mentions">target</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="49 mentions">token</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="39 mentions">trajectory</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="36 mentions">user</span><span class="cloud-word" style="font-size:2.15rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 68%, var(--accent))" title="122 mentions">video</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="44 mentions">view</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="46 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="180 mentions">visual</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="59 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>12 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>From Perception to Simulation: Unveiling and Empowering Mental Spatial Dynamics in MLLMs</strong>
          <small>Jiachun Li, Zhuoran Jin, Kang Liu, Jun Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">MLLM Benchmark</span>
<span class="topic-tag">Curriculum Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2611.22541</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22541">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely, and also fits criterion 2: it targets spatial simulation/spatial intelligence in MLLMs with a new benchmark and a curriculum method.</p>
        <p class="abstract">Spatial reasoning is a fundamental component of world understanding for Multimodal Large Language Models (MLLMs). While existing research has advanced the perception of spatial relations in static scenes, the domain of dynamic spatial simulation remains relatively unexplored. To bridge this gap, we introduce MentalGrid, a benchmark focused on spatial reasoning tasks that require models to simulate evolving spatial states without intermediate visual feedback. Extensive evaluation on our benchmark reveals a significant deficiency in the spatial simulation capabilities of existing models. Specifically, we find that performance is constrained by perceptual limitations in simple simulation scenarios and hindered by inadequate multi-step reasoning as complexity increases. To address these challenges, we propose a three-stage curriculum learning framework utilizing 16k specialized spatial reasoning samples. This approach yields SpatialWalker, which achieves a 33.8% average improvement over its base model, surpassing proprietary models like Gemini-3-Flash in spatial simulation. Furthermore, SpatialWalker demonstrates robust generalization, maintaining a 4.9% average gain on out-of-domain benchmarks, demonstrating the pivotal role of spatial simulation as a fundamental building block for broader spatial intelligence.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>MAVE: Reconstructing Editable 3D Blockouts from Film Shots</strong>
          <small>Yifan Chang, Jian Yang, Jiangnan Shao, Xiaofeng Wang, Zhaoxin Fan, Renjing Xu, Ming Lu, Xingang Wang, Zheng Zhu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Benchmark</span>
<span class="topic-tag">3D Scene Reconstruction</span>
<span class="topic-tag">Video-to-Blockout</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2611.22464</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22464">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it introduces an embodied/video-to-3D blockout benchmark and a simulator/editorial reconstruction method with editable scenes.</p>
        <p class="abstract">Animated 3D blockouts support previsualization and provide structural conditions for video generation, but manually reconstructing them from reference videos is costly. This limits both their use by creators and the production of paired training data. We introduce MAVEBench, a benchmark of 50 film shots and 416 keyframes for evaluating camera motion, spatial layout, and character blocking. We propose MAVE, a video-to-blockout framework combining Metric observation, Agentic modeling, and evidence-based VErification. It first recovers cameras, human motion, and geometric evidence in a shared metric coordinate system. An agent then constructs an editable environment under constraints from these observations, while programmatic checks report inconsistencies to guide refinement. The outputs are editable Blender scenes and frame-aligned blockout videos. On MAVEBench, MAVE improves overall scores by 27.5-41.1 points across three agents over their corresponding vanilla baselines. With DeepSeek-1017, it achieves a score of 73.2 at an average API cost of only USD 0.054 per shot, outperforming the strongest vanilla baseline while reducing total reconstruction time by 53%. We also construct MAVEData-3K, a dataset of 3,000 blockout-video pairs for model training, and will release it publicly. Creators can change viewpoints and character paths, then render the edited scenes to condition video generation. Code is available at https://github.com/yfChang-cv/MAVE.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models</strong>
          <small>Sheng Lu, Guangpin Tao, Tong Lu, Ying Tai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied World Models</span>
<span class="topic-tag">Video Simulation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Viewpoint Consistency</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2611.21782</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.21782">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied AI / video world-model simulator paper with a new benchmark focused on camera-height consistency, a novel angle previous work often ignored.</p>
        <p class="abstract">Interactive video world models serve as simulators for embodied agents: from a starting image and an action trajectory, they generate the views the agent would see. The starting image fixes how high the camera is, for example 0.15 m for a floor robot or 2.2 m for an overhead camera, and a faithful simulator must keep this height as the camera moves. We show that six recent open-weight models fail to do so: as motion replaces the starting view with generated content, they move the camera toward human eye level, a failure we call camera-height regression. Our benchmark, EyeHeight, pairs six rendered elevations (0.15 m to 2.2 m) and four calibrated real-world rig heights with scale-free multi-view height estimation. All six models lose their initial height during a $180^\circ$ turn-and-walk rollout: initialized at 0.15 m, only 0-20% of clips end within $1.3\times$ of the starting height as inferred viewpoints converge to human heights of 1.1 m to 1.5 m, whereas ground-truth renders remain within a few percent. In Matrix-Game models, homography-tracked floor motion stays consistent with constant elevation during rotation even as newly outpainted room geometry yields a higher reconstructed viewpoint. Regression grows with rotation angle, begins while the start frame remains in context, and largely reverses in SANA-WM when a $360^\circ$ turn restores the initial view. We trace this pull to human-centric video priors in which floor-level views are nearly absent: in SANA-WM, textual height cues and dense floor-disparity maps do not prevent it, whereas classifier-free text guidance during the first half of denoising strengthens it. Combining unguided sampling with height-balanced fine-tuning recovers more retention but costs 5 MUSIQ points, a loss fixed during those same early steps. Viewpoint drift alone shifts the paths predicted by visual navigation policies.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>Sketch, Don&#x27;t Paint: Allocating Test-Time Compute in Generative Visual Reasoning</strong>
          <small>Sheng Lu, Guangpin Tao, Tong Lu, Ying Tai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Reasoning</span>
<span class="topic-tag">Test-Time Compute</span>
<span class="topic-tag">Spatial Planning</span>
<span class="topic-tag">Generative Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2611.21812</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.21812">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: it studies test-time compute allocation for generative visual reasoning, including spatial planning and maze/video reasoning in multimodal models.</p>
        <p class="abstract">Multimodal models increasingly reason by synthesizing pixels, sketching maze paths within interleaved chains of thought or rolling out video solutions frame by frame. Each visual thought runs the full diffusion schedule inherited from photorealistic synthesis, so iterative denoising dominates inference cost. We study how to allocate test-time compute along two axes: when to render visual thoughts rather than thinking in text or answering directly, and how many denoising steps each thought requires. Controlled interventions that vary only how the thought is rendered uncover three regimes. Causal thoughts carry the plan and become legible early: an 8-step sketch nearly matches a 50-step render in accuracy, commits to the same plan as often as two independent full renders agree, and in video models mostly fails by stalling short of the goal, so the rollout abstains. Decorative thoughts can be omitted without loss, whereas harmful thoughts lower accuracy. Because the regime depends on both model and task, always drawing is suboptimal. Across 14 model-benchmark pairs of three interleaved reasoners, answering directly, without any thinking, wins 9 pairs, and choosing among direct, text-only, and visual tiers from ten labeled examples per pair raises mean accuracy from 60.7% (always drawing) to 65.1%. Where drawing pays, we propose sketch-and-vote, which samples 8-step sketches (a step count chosen without labels) from independent noises until one answer reaches three votes. With this one setting, sketch-and-vote beats full rendering with fewer denoising steps on an image reasoner and two video reasoners, by 8.6 points on VSP spatial planning and by 9.6 and 22.1 points on mazes.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Generative Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Sample-Aligned Decoders for Latent Generative Models</strong>
          <small>Yu Lei, Yi Li, Hongcheng Gao, Yipeng Wei, Liang Li, Li Su, Qingming Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Decoder Fine-Tuning</span>
<span class="topic-tag">Foundation Models</span>
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
          <span>Paper 5 / arXiv:2611.22458</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22458">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: it is about improving latent generative models and explicitly extends to text-to-image generation, which is relevant to vision foundation model pipelines.</p>
        <p class="abstract">Latent generative models synthesize images by decoding generated latents, yet their decoder is trained only to reconstruct encoder latents and never sees the latents it decodes at test time, so the residual errors of the generator are rendered directly into the final image. Existing remedies retrain the generator, add cost at every sampling step, or make the decoder robust to perturbed real latents, assuming that generator errors resemble such perturbations. We find that they do not. Generated latents lie on the encoder latent manifold as closely as real ones, yet follow a different distribution. The decoder should therefore be adapted to the distribution of generated latents, which raises two challenges: (1) unpaired supervision, since a generated latent has no ground-truth image, and (2) latent-space drift, since a decoder freed from paired targets forgets the latent space it must decode. We propose Sample-Aligned Decoders (SAD), a post-training framework that fine-tunes only the decoder of a frozen generator at no inference cost. Generated-Sample Distribution Alignment matches decoded generated latents to unpaired real images in a frozen foundation-model feature space, and Encoder Anchor Preservation keeps the decoder close to the original one on encoder latents. Our analysis shows that the alignment is effective only on generated latents, where it corrects each sample in proportion to how much more often the generator produces such latents than the encoder; on encoder latents it can only work against the anchor. SAD improves four state-of-the-art ImageNet generators across three tokenizers, e.g., FID-50K from 1.15 to 0.98 for REPA-E, complements discriminator guidance, and extends to text-to-image generation. Our code and models are available at https://torpedo2003.github.io/SAD/.</p>
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
          <strong>Rethinking Perceptual Similarity for Remote Sensing: Multi-Layer Attention Scoring and Human Preference Benchmarking</strong>
          <small>Eli Underwood, Marc Bosch, Neil Joshi, Jeffrey Wen, Myron Brown</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Perceptual Metric</span>
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
          <span>Paper 7 / arXiv:2611.21816</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.21816">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it is a vision foundation model application (RemoteCLIP) used to build a new perceptual similarity metric and benchmark for remote sensing generation.</p>
        <p class="abstract">Perceptual similarity metrics for natural images transfer poorly to remote sensing (RS), where severe geospatial and semantic failures can remain visually plausible while still being decisively wrong for downstream use. To address this, we develop a novel human-aligned perceptual quality metric for generated RS imagery and evaluate it across several generation tasks. We first conduct a controlled perturbation study where we progressively increase the severity of common synthetic perturbations. Using the layer-wise Aligned Attention Score (AAS) responses in RemoteCLIP, we find that different RS artifacts are best captured at different depths. Based on these findings, we introduce Remote Sensing Perceptual Distance (RSPD), a pairwise metric that averages seven independently calibrated layer distances without tuning on human-preference labels. To evaluate our metric on realistic RS generation tasks, we construct a blind, reference-conditioned two-alternative forced-choice (2AFC) benchmark with five 300-triplet subsets spanning synthetic artifacts, airborne and spaceborne super-resolution, SAR-to-optical translation, and timeseries controls. We also construct a 300-triplet ordered misregistration benchmark with deterministic labels. Using the same RemoteCLIP checkpoint, RSPD substantially outperforms simple cosine distance with the final global embedding and is competitive with the strongest generic baselines across the realistic RS generation tasks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Inertial Video World Models</strong>
          <small>Yuan Gao, Fan Xu, Yu Guo, Yuxu Lu, Zhengru Fang, Hao Wu, Xiaomeng Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Video Prediction</span>
<span class="topic-tag">Robot Simulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2611.22314</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22314">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; it is a video world model with inertial state propagation, relevant to embodied simulation but not directly a new benchmark or an MLLM/VLLM paper.</p>
        <p class="abstract">The physical world has inertia: it evolves from what already exists rather than being recreated at every instant. However, many existing video world models lack an explicit mechanism for inertial state evolution, leaving the continuity of motion and structure implicit in video prediction. During autoregressive rollouts, repeated reconstruction can accumulate errors and destabilize the predicted dynamics. To address this limitation, we introduce InertialWorld, an Inertial Video World Model that makes inertia a structural prior for autoregressive prediction: existing scene evidence is carried across time rather than reconstructed at every step. Central to this formulation is Inertial Memory, which turns memory from passive predictive context into an evolving video state with two complementary views: a dense Eulerian grid preserves scene-aligned evidence, while persistent Lagrangian carriers bind local content to learned canonical coordinates. At each step, the model transports the carrier content according to action-conditioned motion, predicts the complete next video state from the transported carriers and dense grid, and uses a learned gate to combine transported and newly predicted content into the memory for the next step. Extensive experiments across multiple domains, including robot manipulation, 3D game simulation, and open-world navigation, demonstrate that InertialWorld achieves competitive autoregressive prediction performance against strong video world model baselines. Codes link: https://github.com/YuanGao-YG/InertialWorld</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Representation Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>When AUC Meets Generative Reconstruction: A Unified Principle for Balanced Visual Representation Learning</strong>
          <small>Boyu Han, Qianqian Xu, Shilong Bao, Zhiyong Yang, Qingming Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Representation Learning</span>
<span class="topic-tag">Generative Reconstruction</span>
<span class="topic-tag">AUC Optimization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2611.22094</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22094">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: it proposes a new visual representation learning objective relevant to training vision encoders for MLLMs, though it is not itself a VLLM/MLLM system paper.</p>
        <p class="abstract">Multimodal large language models (MLLMs) require visual encoders that extract fine-grained visual features while constructing semantically disentangled and discriminative representations. Conventional methodologies encounter a fundamental trade-off: contrastive learning enhances inter-class discrimination by suppressing intra-class variability, whereas generative reconstruction emphasizes perceptual fidelity but lacks explicit comparative supervision. The naive aggregation of these objectives via composite loss functions often induces optimization conflicts and instability due to gradient interference within the shared latent space. To resolve this, we introduce a unified representation-learning paradigm that reformulates generative reconstruction as a discriminative ranking problem within the generative output manifold. Our approach maintains perceptual reconstruction as a supervisory signal and integrates a ranking-based discriminative constraint by systematically ordering matched and mismatched reconstruction outputs. This formulation embeds discriminative information seamlessly into the generative process, alleviating the risk of loss competition. Specifically, we propose AUC Generative Reconstruction (AUCGR), which optimizes the area under the ROC curve (AUC) by ensuring higher scores for matched pairs than for mismatched pairs, and Partial AUC Generative Reconstruction (pAUCGR), which addresses supervision bias by focusing on mismatched comparisons within reliable feature subspaces. The proposed objectives are designed to be plug-and-play, requiring no architectural modifications to existing generative reconstruction frameworks. Theoretical analysis establishes rigorous connections to AUC/pAUC optimization and provides generalization guarantees. Extensive experiments validate that our method advances both discriminative accuracy and fine-grained perceptual representation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Editing</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Motion-Aware Reward Modeling for Instruction-Guided Video Editing</strong>
          <small>Li Li, Xiangbo Gao, Bo Ni, Samyadeep Basu, Viet Dac Lai, Jing Shi, Seunghyun Yoon, Gang Wu, Yu Wang, Thien Huu Nguyen, Tyler Derr, Franck Dernoncourt, Zhengzhong Tu, Yue Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Editing</span>
<span class="topic-tag">Reward Modeling</span>
<span class="topic-tag">Motion Consistency</span>
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
          <span>Paper 10 / arXiv:2611.22495</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22495">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; it is a reward model for video editing, which is a useful multimodal learning result but not a direct match to the listed categories.</p>
        <p class="abstract">Reward models for instruction-guided video editing can favor temporal consistency at the expense of motion. We study this failure, termed \emph{motion collapse}, using controlled motion-suppression variants of real edits. On VE-Bench, the evaluated composite reward prefers a motion-suppressed candidate in $97\%$ of cases. Learned video rewards and a VLM judge also struggle with mild suppression, while latent optimization and reward-guided fine-tuning exploit this weakness to increase reward as motion declines. A linear probe of our base reward backbone performs near chance on mild suppression, motivating an explicit inter-frame dynamics input. We propose a motion-aware reward model that combines an RGB frame-difference stream with preference training against motion-suppressed and fabricated-motion negatives. A distillation anchor preserves alignment with human quality judgments. On the VE-Bench motion ladder, our model reduces the rate of selecting motion-suppressed candidates to $0\%$ while achieving a Spearman correlation of $0.57$ with human quality ratings. It also detects unseen suppression variants and preserves motion during reward-guided fine-tuning on two editing pipelines. These results support explicitly modeling motion in rewards for video editing.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Hand Pose Estimation</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>HandRSI: Recursive Self-Improvement for Hand Pose Estimation</strong>
          <small>Zhekai Wang, Luqing Luo, Wenhao Yao, Junjie Lu, Huanan Zhu, Feifei Gao, Yuhua Jiang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Hand Pose Estimation</span>
<span class="topic-tag">Self-Improvement</span>
<span class="topic-tag">Egocentric Vision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2611.22164</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22164">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; it is an egocentric hand pose estimation improvement, which is vision/embodied-adjacent but not a new embodied benchmark or spatial intelligence method.</p>
        <p class="abstract">Egocentric 3D hand pose estimators still miss hands at the image border, misplace occluded hands and jitter. Such failures are usually fixed by hand-written inference refinements and by fine-tuning, two interdependent steps that are tuned separately. We present HandRSI, a recursive self-improvement framework for a hand pose system that consists of a video estimator and its executable inference harness. In each round, coding agents refine the harness, and a change is accepted only if it improves a composite of all ten benchmark metrics on held-out data without significantly regressing any of them. The accepted harness then guides the estimator through selective distillation, which supervises hand presence and temporal consistency on frames without ground truth, while ground truth supervises pose. Since the updated estimator may change which refinements remain useful, the harness is re-validated on it. Starting from the released ACE-Ego-Hand model, five rounds reduce MPJPE-p by 35% on HOT3D and 11% on ARCTIC and roughly halve jitter. On HOT3D, HandRSI&#x27;s MPJPE-p is 16% lower than that of ACE-Ego-Hand fine-tuned on the same ground truth. Under a unified protocol, it outperforms nine re-run published methods on all ten metrics of both benchmarks. Hypervolume selection on the accuracy-speed front yields Lite, Medium and Heavy systems running at 20.7 to 41.1 FPS. This report gives the full method, every stage of every round and the complete protocol. Code, evaluator, harnesses and weights are public.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>RetiDual-Select: Reliability-Aware Specialist-Generalist Routing for Retinal OCT under Image-Quality Shift</strong>
          <small>Zihao Han, Philippe De Wilde</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Vision-Language Models</span>
<span class="topic-tag">Ensemble Routing</span>
<span class="topic-tag">Robustness</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2611.22117</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22117">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; it uses a medical vision-language model, but the paper is about reliability-aware routing under image-quality shift rather than a new VLLM/MLLM method or embodied/spatial understanding.</p>
        <p class="abstract">Adaptive fusion can repair a static ensemble&#x27;s errors, but can also overturn correct decisions. RetiDual-Select combines retinal specialist RETFound with the image encoder of the medical vision-language model MedSigLIP, separating candidate fusion, routing safety and predictive review. Calibrated product-of-experts (PoE) fusion is the static reference, a small gate proposes an alternative for each image, a validation-frozen harm guard decides whether that candidate may replace the reference, and a separate score prioritizes review. Static PoE reached the highest or joint-highest clean accuracy on all three datasets. At a clean 2% accepted-error target the review policy accepted 94.3% of Kermany-4 images at 99.89% selective accuracy, and 92.4% of OCT-C8 at 98.65%. Both branches were correct on 95.0% and 91.8% of clean images; only 4.4% and 6.2% had exactly one correct branch. Across 15 prespecified synthetic conditions, adaptive gains were concentrated in severe contrast reduction, where this routing opportunity widened roughly ninefold; percentile rescaling largely removed the effect, linking it to compressed dynamic range. In post-hoc validation-only analyses, gain was higher when the gate followed the more reliable branch, and a frozen guard cut the worst-condition OCT-C8 loss from 1.39 to 0.36 percentage points. Adaptive routing was useful when image quality created a reliability opportunity and the gate followed it; otherwise the system retained Static PoE or deferred for review. The findings are bounded by the synthetic perturbations evaluated and do not establish robustness to natural acquisition or scanner shift.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Open-Vocabulary Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Text-Guided Modality Correction for Open-Vocabulary Object Detection</strong>
          <small>Yu Quan, Dong Zhang, Ping Gong, Peng Huang, JinHui Tang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Open-Vocabulary Detection</span>
<span class="topic-tag">Vision-Language Alignment</span>
<span class="topic-tag">Multi-Scale Features</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2611.22126</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22126">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; this is open-vocabulary object detection with text-guided feature correction, which is useful vision-language work but not a direct match to the requested categories.</p>
        <p class="abstract">Open-vocabulary object detection (OVD) is essential for detecting objects beyond the categories seen during training. Establishing vision-language associations is crucial for recognizing unseen categories, while integrating complementary visual features across levels supports detection at different scales. However, existing methods often provide insufficient textual guidance for object regions, rely on limited cross-modal alignment strategies, and underuse complementary features across levels, limiting their ability to detect unseen categories and objects of varying scales. To address these limitations, we propose a Text-Guided Modality Correction Network (TMCNet) that incorporates textual guidance into region feature extraction, cross-modal alignment, and multi-scale decoding to strengthen region-category semantic correspondence and promote complementary feature fusion across levels. First, a text-guided modality encoder incorporates textual semantics into queries to guide regional feature aggregation, reducing semantic ambiguity in object representations. Second, a cross-modal alignment module strengthens the correspondence between region representations and category semantics through interactions between visual and textual features. Finally, a progressive text correction decoder combines a top-down pathway with lateral connections to progressively fuse text-guided deep semantic features with shallow visual features at the corresponding scales, preserving both semantic information and spatial detail for objects of different sizes. Experiments on two public datasets, COCO-OVD and LVIS-OVD, demonstrate that TMCNet achieves strong performance in open-vocabulary object detection using simple text queries as guidance. Extending TMCNet to open-vocabulary segmentation also yields performance gains, demonstrating its cross-task applicability and extensibility.</p>
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
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Reconfiguring Procedural Knowledge for Compositional Robot Skill Adaptation</strong>
          <small>Daehee Lee, Dongsu Lee, Sanghyun Ahn, Minjong Yoo, Honguk Woo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Robot Skill Adaptation</span>
<span class="topic-tag">Long-Horizon Manipulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2611.22174</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22174">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied AI / robot skill adaptation method for long-horizon manipulation in Franka Kitchen, with a novel compositional angle on procedural knowledge.</p>
        <p class="abstract">General-purpose behavior models increasingly internalize broad procedural knowledge during training, making their adaptation to new goals and skill interfaces less a problem of learning entirely new behaviors than of reconfiguring existing competence. We study this capability as reconfigurability, the ability to realize new behaviors by cost-efficiently restructuring existing components and relations under sparse governing information, where task specifications provide high-level goals and procedure specifications expose a limited set of reusable factors, leaving the concrete bindings and compositions required for execution underdetermined. We propose RecPo, a framework that represents skills task-agnostically through multiple procedure views and materializes executable skill sequences by composing stored transitions to realize task-specific changes. RecPo maintains a procedure knowledge base of skill-induced transitions, with each view exposing a reusable factor and preserving local skill connectivity. At deployment, it interprets task specifications through the same views and resolves the resulting compositional queries over the stored relations to bind skills for execution. On long-horizon tasks in an extended Franka Kitchen benchmark, RecPo achieves 91.9% ordered completion with 1.0 ms of task inference per episode across varying procedure support and task-record sparsity. Real-robot studies further demonstrate adaptation through local memory edits without task-specific retraining.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-10-23.html">
          <span>October 23, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-22.html">
          <span>October 22, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-21.html">
          <span>October 21, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-19.html">
          <span>October 19, 2026</span>
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
