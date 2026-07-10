

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
      <p class="eyebrow">Daily ArXiv / July 10, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>19</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>13</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>10.9</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">aerotrack</span><span class="cloud-word" style="font-size:1.97rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="14 mentions">alignment</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">animation</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="12 mentions">camera</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">category</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">comprehensive</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">construct</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">detection</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">dynamic</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">environment</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">geometry</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">hand</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">hierarchy</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">identity</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">illumination</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">instance</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">jointly</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">latent</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">low-rank</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">motion</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">multimodal</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="23 mentions">object</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">perception</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">psychiatric</span><span class="cloud-word" style="font-size:1.64rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="11 mentions">query</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">reasoning</span><span class="cloud-word" style="font-size:1.64rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="11 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">robust</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="12 mentions">scene</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="9 mentions">semantic</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">sequence</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">space</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">struggle</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">support</span><span class="cloud-word" style="font-size:1.86rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="13 mentions">target</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">textbf</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">thinking</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="10 mentions">track</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="9 mentions">trajectory</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">unified</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">vehicle</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="23 mentions">video</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">view</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="12 mentions">visual</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">will</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="90 mentions">action</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="96 mentions">agent</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="76 mentions">alignment</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="63 mentions">attention</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="59 mentions">camera</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="59 mentions">consistency</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">construct</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="61 mentions">detection</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">diffusion</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="60 mentions">domain</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="66 mentions">driving</span><span class="cloud-word" style="font-size:1.39rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="103 mentions">dynamic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">editing</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">event</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="114 mentions">evidence</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="71 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">foundation</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">frame</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">generate</span><span class="cloud-word" style="font-size:1.90rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 55%, var(--accent))" title="163 mentions">generation</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="59 mentions">geometric</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="59 mentions">geometry</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">grounding</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="68 mentions">inference</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="59 mentions">interaction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">knowledge</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="101 mentions">language</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="68 mentions">latent</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">mechanism</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="78 mentions">memory</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="102 mentions">motion</span><span class="cloud-word" style="font-size:1.77rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="146 mentions">multimodal</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">multiple</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="136 mentions">object</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">paradigm</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">physical</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="76 mentions">pipeline</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="55 mentions">policy</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="75 mentions">real-world</span><span class="cloud-word" style="font-size:2.14rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 68%, var(--accent))" title="196 mentions">reasoning</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="81 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="63 mentions">region</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="58 mentions">reward</span><span class="cloud-word" style="font-size:1.62rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="128 mentions">scene</span><span class="cloud-word" style="font-size:1.80rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="150 mentions">semantic</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="65 mentions">space</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="112 mentions">spatial</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="58 mentions">supervision</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="55 mentions">support</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="79 mentions">target</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="101 mentions">temporal</span><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="121 mentions">token</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="72 mentions">trajectory</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="79 mentions">understanding</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="73 mentions">unified</span><span class="cloud-word" style="font-size:2.44rem;opacity:0.92;color:color-mix(in srgb, var(--accent-2) 83%, var(--accent))" title="242 mentions">video</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="54 mentions">view</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="72 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="298 mentions">visual</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="87 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>16 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>UAV-OVVIS: Unmanned Aerial Vehicles Also Need Open-Vocabulary Video Instance Segmentation</strong>
          <small>Mingyu Dou, Shi Qiu, Ming Hu, Yifan Chen, Zhe Sun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Open-Vocabulary Segmentation</span>
<span class="topic-tag">Video Instance Segmentation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2607.08075</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08075">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it introduces a new embodied perception benchmark for UAV open-vocabulary video instance segmentation, plus a training-free method built around visual foundation models.</p>
        <p class="abstract">Unmanned Aerial Vehicle (UAV) videos are widely used in traffic monitoring, urban management, and emergency rescue. However, existing UAV video perception mainly relies on box-level localization and trajectory association under predefined categories, making it difficult to simultaneously support flexible queries and fine-grained instance-level dynamic understanding in open scenarios. To this end, we introduce a new task, UAV Open-Vocabulary Video Instance Segmentation (UAV-OVVIS), which discovers targets in UAV videos according to open-vocabulary queries and outputs instance-level segmentation trajectories with globally consistent identities. Considering the scarcity of instance-level annotations in UAV scenarios, we propose AeroTrack, a training-free unified framework. AeroTrack centers on periodic open-vocabulary detection, short-segment mask propagation, and cross-segment identity unification, reusing existing visual foundation models to enable UAV-OVVIS. Based on this framework, we instantiate five AeroTrack variants and construct AeroVIS, an evaluation benchmark for UAV-OVVIS containing 9 UAV object categories and 8,279 trajectories. Experiments show that AeroTrack substantially outperforms existing general video instance segmentation methods in UAV scenarios and demonstrates strong open-vocabulary robustness and generalization. To support future research, we release AeroTrack and AeroVIS as a unified framework and benchmark for UAV-OVVIS.</p>
      </div>
    </details>


    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>GIRAF: Towards Generalizable Human Interactions with Articulated Objects</strong>
          <small>Xiaohan Zhang, Sebastian Starke, Alexander Winkler, Federica Bogo, Samir Aroudj, Yuting Ye</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Human-Object Interaction</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Articulated Objects</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2607.07880</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.07880">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: embodied AI / human-object interaction with a new method for full-body interaction with articulated objects.</p>
        <p class="abstract">Synthesizing realistic full-body human interactions with articulated objects is a fundamental challenge for embodied AI and graphics, with applications in robotics training and virtual agents. Existing models remain limited: some focus on simple activities with static objects, while others restrict attention to hand-only manipulation. This leaves open the problem of generating coordinated full-body motion that approaches, manipulates, and moves articulated objects in a realistic and generalizable way. The key difficulty lies in reasoning jointly about locomotion, fine-grained contact, and object articulation. Models must capture subtle hand-object correspondences that transfer across object geometries, while also producing seamless transitions from navigation to manipulation. At the same time, the scarcity of large-scale paired motion-scene data makes it difficult to generalize across diverse object positions and shapes. We introduce a text-conditioned diffusion model that addresses these challenges through three core ideas: an object-centric representation that unifies hand-object contact with object surfaces, a mixed-domain training strategy that balances locomotion and interaction, and a contact-based augmentation scheme that expands training diversity. Through experiments, our method demonstrated strong generalization to unseen object configurations, surpassing current state-of-the-art methods.</p>
      </div>
    </details>


    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery</strong>
          <small>Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Deformable SLAM</span>
<span class="topic-tag">Medical Robotics</span>
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
          <span>Paper 8 / arXiv:2607.08408</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08408">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: an embodied/simulation-related method paper on online SLAM for deformable robotic surgery, with a novel motion-aware pose optimization angle.</p>
        <p class="abstract">Gaussian splatting is the current state-of-the-art for dense, deformable 3D anatomy reconstruction in robot-assisted minimally invasive surgery (RAMIS); however, most pipelines are offline and depend on accurate camera trajectory priors (often from robotic kinematics), limiting applicability when priors are missing or noisy. To address these limitations, we propose Track2Map, an online 3D Gaussian Splatting pipeline that jointly optimizes camera trajectory and 3D deformable scene representation directly from surgical video. Track2Map is therefore capable of robust 3D reconstructions when camera trajectory priors are either absent or noisy, and due to its online nature it effectively works as a Simultaneous Localisation and Mapping (SLAM) method. To stabilize optimization in the presence of tissue motion and ambiguous visual cues, we introduce a track-anchored deformation initialization using dense 2D point tracks. Track statistics are further utilized to disentangle camera motion from scene deformation by detecting static camera periods and reducing drift during incremental mapping. Experiments on StereoMIS show improved reconstruction quality and camera trajectory against competing SLAM methods, as well as compared to non-SLAM methods that utilize camera trajectory priors. The code is available at https://track2map.github.io/.</p>
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
          <strong>LEEVLA: Seeing What Matters in Latent Environment Evolution for Vision-Language-Action</strong>
          <small>Qi Lyu, Baicheng Liu, Xudong Wang, Jiahua Dong, Lianqing Liu, Zhi Han</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Latent World Models</span>
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
          <span>Paper 2 / arXiv:2607.08182</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08182">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 and 2: a new Vision-Language-Action (VLA) method with explicit latent environment evolution modeling for embodied agents.</p>
        <p class="abstract">Vision-language-action (VLA) models aim to map multimodal inputs to robot actions. However, most existing approaches struggle to cover complex dynamic scenarios due to treating all visual tokens uniformly and reasoning with human-selected factors, which lack mechanisms to emphasize task-critical evidence and ignore underlying factors. To address this issue, we propose LEEVLA, a VLA architecture for seeing what matters in Latent Environment Evolution that explicitly guides the model toward informative regions while preserving the structured evolution of latent world representations. To identify salient and instruction-relevant regions, we introduce drift-guided dynamic prioritization (DGDP), which combines dynamic position prioritization (DPP) with semantic drift guidance (SDG) to guide the VLA agent where to attend during training. On top of this, we introduce structured feature flow generation (SFFG), which models how these prioritized features should evolve in latent space via prototype-to-periphery (P2P) prediction, and a mutual-neighborhood contrastive (MC) loss to maintain topological consistency among neighborhoods. Together, DGDP and SFFG form a task-aware &quot;where-how&quot; training framework. Extensive experiments on VLA benchmarks show that LEEVLA consistently outperforms prior methods, confirming that explicit task-evidence guidance and structured latent reasoning are both crucial for scalable VLA. Our code is available at https://github.com/LyuQi127/LEEVLA.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Grounding</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>UniRef-UAV: A Multimodal Benchmark for Universal Referring in UAV Imagery</strong>
          <small>Haibin Tian, Huichao Xie, Xuelin Qian, Ruitao Lu, Junwei Han, Dingwen Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Grounding</span>
<span class="topic-tag">UAV Perception</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2607.08267</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08267">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it introduces a new multimodal UAV referring benchmark and a baseline for universal referring, which is a novel spatial grounding/evaluation setting.</p>
        <p class="abstract">Unmanned aerial vehicles (UAVs) increasingly rely on visual grounding capabilities to localize task-relevant targets from diverse instructions in complex aerial scenes. Existing referring expression comprehension (REC) benchmarks and methods, however, are largely built around text-only queries and single-object outputs, which limits their applicability to practical UAV scenarios involving reference images, multimodal instructions, absent targets, and multiple valid target instances. To address this gap, we introduce \emph{Universal Referring}, a generalized UAV referring task that jointly expands the query modality and the output cardinality. We construct \emph{UniRef-UAV}, a multimodal benchmark that supports text-only, image-only, and text+image queries with modality-dependent target cardinality, where text-only and text+image queries admit no-target, single-target, and multi-target grounding while image-only queries focus on existence-aware single-instance grounding. It also provides in-domain and cross-domain evaluation protocols for visual-query generalization. We further present \emph{UAV-URNet}, a detection-style baseline that maps heterogeneous queries into a shared query space and predicts variable-size target sets through set prediction. Extensive experiments show that UAV-URNet provides a stable and reproducible baseline with more consistent no-target discrimination and a more lightweight, reproducible implementation than large general-purpose MLLMs. Additional domain analysis, query-representation analysis, and ablation studies demonstrate that multimodal queries help reduce visual-query ambiguity and promote a more unified query--target alignment space. The annotations, visual query crops/images, train/validation/test splits, evaluation scripts, and baseline code will be made publicly available to facilitate reproducible research.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Reconstruction</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>LTM: Large-scale Terrain Model for Wildfire-prone Landscapes</strong>
          <small>Xiao Fu, Yue Hu, Meida Chen, Peter Anthony Beerel, Barath Raghavan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Simulation</span>
<span class="topic-tag">Multi-Modal Geometry</span>
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
          <span>Paper 5 / arXiv:2607.08711</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08711">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it proposes a new simulator for large-terrain reconstruction in wildfire-prone landscapes and a multi-modal method using legacy DEM priors, which is a novel embodied/spatial angle.</p>
        <p class="abstract">Accurate 3D terrain maps are essential for emergency response when assessing wildfire hazards. However, wildfire-prone regions often span vast areas where conventional reconstruction methods underperform. Airborne LiDAR systems provide high-resolution terrain data, but they are expensive and infrequently updated. Image-based methods offer a lower-cost alternative, but struggle due to sparse visual features and limited image overlap. We propose a multi-modal reconstruction framework leveraging outdated Digital Elevation Models (DEMs) as geometric priors for image-based 3D reconstruction. Our key innovation is physics-based pixel-pixel alignment between images and DEM data, dramatically reducing computational complexity by eliminating expensive feature matching procedures. To validate our approach, we developed a large-terrain simulator based on a real wildfire-prone area, generating realistic images enabling a comprehensive evaluation. Given posed images and legacy DEMs, our method produces high-fidelity depth maps while maintaining real-time performance. We find significant improvements in reconstruction accuracy and computational efficiency over existing techniques, offering a scalable solution for wildfire response.</p>
      </div>
    </details>


    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction</strong>
          <small>Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Panoramic Vision</span>
<span class="topic-tag">Gaussian Splatting</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2607.08769</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08769">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it introduces a new benchmark for panoramic outdoor reconstruction and a geometry/gradient partitioning method for scalable reconstruction.</p>
        <p class="abstract">Scaling 3D Gaussian Splatting (3DGS) to large outdoor scenes is costly in both data acquisition and computation. Adopting panoramic images with equirectangular projection (ERP) can reduce capture effort via their full $360^{\circ}$ field of view, yet the resulting omnipresent visibility invalidates existing partitioning strategies that rely on local camera frustums, causing block-wise optimization to degenerate into global training. Thus, we propose PanoLOG, a two-stage coarse-to-fine framework equipped with a Geometry and Gradient-based Partitioning Strategy tailored for large-scale panoramic 3DGS reconstruction. In the global coarse stage, PanoLOG leverages sky-sphere modeling and panoramic monocular depth supervision for reliable geometry, while in the refinement stage, G$^2$PS builds adaptive bounding volumes via parallax-driven uncertainty and assigns cameras via gradient-based importance scoring. Furthermore, we construct Pano360, the first benchmark on large-scale panoramic dataset for outdoor scene reconstruction. Extensive experiments demonstrate that G$^2$PS achieves state-of-the-art rendering quality while maintaining scalable, block-parallel training. Our models, training code, and dataset are publicly available.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Alignment</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Dive Into the Implicit Biases of Low-rank Vision-language Alignment</strong>
          <small>Mingjia Shi, Shuo Wang, Xiaobo Wang, Sifan Zhou, Kai Wang, Tianyu Fu, Chenxu Zhao, Anyang Su, Ping Jiang, Minghui Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Alignment</span>
<span class="topic-tag">Low-Rank Adaptation</span>
<span class="topic-tag">VLM Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2607.08194</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08194">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 and partly 2: it studies low-rank vision-language alignment and gives insightful empirical/theoretical results on alignment behavior.</p>
        <p class="abstract">Vision-language alignment, the stage that bridges pretrained vision encoders and large language models, is widely treated as a form of pretraining requiring full-parameter updates. We challenge this view and investigate what happens when low-rank adaptation is applied to the LLM during this stage instead. We find that low-rank alignment not only reduces computational costs but also outperforms full-parameter alignment on most benchmarks. To understand this phenomenon, we systematically characterize the implicit biases introduced by low-rank adaptation during alignment. Empirically, we find that low-rank alignment shifts model behavior from hallucinatory to conservative and preserves per-token linear separability of visual features that full-parameter alignment disrupts, a phenomenon we term LS-curse. Geometrically, low rank aligned models exhibit more homogeneous and structurally stable visual representations, maintaining modality-specific knowledge rather than prematurely fusing entity-level semantics. Theoretically, we establish two theorems showing that low-rank alignment induces preferences for parameter subspaces with flat gradients and feature subspaces robust to perturbations, providing a principled explanation for the observed structure-preserving behavior. Extensive experiments cover ablation over 100 alignment configurations, three families of low-rank operators, and various rank, encoder, and other settings.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting</strong>
          <small>Zixin Guo, Yehonathan Litman, Yifeng He, John Miller, Chuhan Chen, Deva Ramanan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Video Relighting</span>
<span class="topic-tag">Diffusion Refinement</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.GR</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2607.08016</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08016">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a vision foundation model–based application (post-training CogVideoX) for controllable video relighting, with a new benchmark contribution.</p>
        <p class="abstract">Video relighting requires balancing long-form temporal consistency with a physically grounded understanding of light transport, which depends on accurate estimation of intrinsic scene properties such as materials, geometry, and illumination. Existing methods follow two paradigms: (1) reconstruct a video&#x27;s photometric properties via inverse rendering and relight them to a target illumination via forward rendering, using physically-based rendering (PBR) or a neural renderer; these suffer from noisy reconstructions and struggle with hard-to-model effects such as global illumination. (2) Frame the task as generative video-to-video translation conditioned on relighting targets (a target environment map or text); this limits relighting control and temporal stability, since diffusion models struggle to translate long-form videos, and is constrained by the availability of input/relit training pairs. We propose LightCrafter, a hybrid pipeline that reformulates video relighting as video translation of a proxy video: rather than translating the input video directly to the target, we translate a PBR rendering of the input under the target illumination to the final target. This bakes illumination targets into the PBR proxy, removing the need to teach the diffusion model illumination concepts like environment maps, and enables more intricate lighting control while naturally providing long-form temporal consistency. We show PBR renders alone already outperform some prior art but struggle with effects like global illumination; to capture these, we leverage photometric priors in video generation models by post-training CogVideoX on synthetic video pairs and real-world unpaired videos. We outperform prior state-of-the-art on existing real-world relighting benchmarks and contribute a synthetic benchmark for further analysis. We will release our dataset, benchmark, metrics, and code.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>WaspMOT: A Benchmark for Long-Term Multi-Object Tracking of Trichogramma Wasps</strong>
          <small>Tomasz Stanczyk, Yuan Gao, Hardik Agarwal, Seongroo Yoon, Tiantao Zhang, Vincent Calcagno, Francois Bremond</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multi-Object Tracking</span>
<span class="topic-tag">Long-Term Association</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2607.08729</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08729">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it builds a new benchmark for long-term multi-object tracking, emphasizing identity preservation over long horizons, which is a novel evaluation angle often ignored by prior work.</p>
        <p class="abstract">Multi-object tracking (MOT) has achieved strong performance on benchmarks dominated by short video sequences. However, such datasets do not adequately evaluate long-term identity preservation, where objects must be tracked consistently over extended durations. We introduce WaspMOT, a benchmark designed to address this gap through long-duration tracking of Trichogramma wasps in controlled ecological experiments. The dataset contains 10 sequences of approximately 12,000 frames each (over 8 minutes at 25 FPS), with dense MOTChallenge annotations and oracle detections to isolate association performance.   Unlike existing benchmarks, WaspMOT forms a closed-set tracking scenario where all individuals remain present throughout the sequence, requiring consistent identity assignment across thousands of frames despite abrupt jumps, occlusions, and highly similar appearance. We establish a benchmark by evaluating five tracking-by-detection methods, including ByteTrack, BoT-SORT, C-BIoU, OC-SORT, and McByte, under a unified protocol. Results show that all methods suffer from significant trajectory fragmentation, highlighting the difficulty of long-term identity preservation even with perfect detections. A simple spatial tracklet stitching baseline consistently improves performance, indicating that substantial gains remain possible.   WaspMOT provides a new benchmark for studying long-term association and reveals limitations of current tracking approaches that are not observable on conventional datasets. The benchmark will be made publicly available at the project repository: https://github.com/tstanczyk95/WaspMOT/ .</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Egocentric Tracking</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Whareformer: Learning to Track What is Where in Long Egocentric Videos</strong>
          <small>Jacob Chalk, Saptarshi Sinha, Dima Damen, Yannis Kalantidis, Diane Larlus</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Egocentric Tracking</span>
<span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Long-Horizon Memory</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2607.08537</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08537">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new learning-based method for long egocentric video object tracking, a clear embodied perception problem with &#x27;where/what&#x27; reasoning.</p>
        <p class="abstract">The recently established &#x27;Out of Sight, Not out of Mind&#x27; (OSNOM) task for egocentric videos focuses on tracking objects that are moved by the camera wearer, online, maintaining knowledge of instance locations throughout the video even when they leave the field of view or become heavily occluded. In this paper, we propose the first learning-based solution to the OSNOM task: Whareformer, a transformer-based model with two components: an updatable memory of established tracks and a track assignment module that associates observations with existing tracks in a feed-forward manner. Whareformer jointly reasons over evolving object appearance (what) and updated 3D location (where), and employs a dedicated New Track token to reason about novel objects.   Thanks to its design choices of using relative distances and evolving track representations, Whareformer is trained on a small set of 56 videos but achieves SOTA performance on 260 long test videos from three datasets: EPIC-KITCHENS-100 (unseen videos), IT3DEgo, and HD-EPIC, with significant absolute improvements over prior work.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Egocentric VLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Do Egocentric Video-Language Models Capture Both Hand- and Object-Centric Cues?</strong>
          <small>Masatoshi Tateno, Alexandros Stergiou, Risa Shinoda, Yoichi Sato, Dima Damen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Egocentric VLMs</span>
<span class="topic-tag">Embodied Perception</span>
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
          <span>Paper 13 / arXiv:2607.08514</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08514">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 and partly 3: it studies egocentric video-language models and proposes cue-isolated evaluation plus hand/object-centric training for embodied understanding.</p>
        <p class="abstract">Hand-object interaction (HOI) recognition requires capturing both hand manipulations and object transformations. However, existing video-language models often fall into shortcuts by relying on spurious correlations among hands, objects, or environmental context, rather than reasoning from the appearance and dynamics of hands and objects themselves. To address this limitation, we propose a new learning paradigm that combines (i) hand-object masked training, which enables robust reasoning from partial hand or object observations, and (ii) an HOI-dynamics-aware decoder that explicitly learns hand- and object-centric embeddings through auxiliary predictions of their locations and semantics, enhancing sensitivity to both cues. To systematically evaluate such cue-specific reasoning, we introduce Cue-Isolated HOI (CI-HOI), a new evaluation that assesses models&#x27; ability to predict actions from hand- and object-related cues independently. To enable CI-HOI, we curate the DEHOI testbed, which separates hand- and object-related observations for disentangled HOI evaluation through inpainting. Using DEHOI, we demonstrate both quantitatively and qualitatively that our training strategy exploits hand- and object-centric information more effectively than existing models. Our approach improves over existing models on DEHOI, standard action recognition, object state recognition, and even robot manipulation action recognition, leading to more robust HOI understanding.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Object-Centric Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>HSA: Hierarchical Slot Attention for Multi-granularity Scene-Decomposition</strong>
          <small>Neelu Madan, Rongzhen Zhao, Andreas Mogelmose, Juho Kannala, Joni Pajarinen, Graham W. Taylor, Thomas B. Moeslund</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Object-Centric Learning</span>
<span class="topic-tag">Scene Decomposition</span>
<span class="topic-tag">Slot Attention</span>
<span class="topic-tag">Vision Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2607.08249</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08249">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: vision representation learning for multi-granularity scene decomposition with slot attention, which is relevant to foundation-model-style visual understanding.</p>
        <p class="abstract">Slot attention is a powerful framework for object-centric learning, decomposing visual scenes into latent slots through iterative competitive attention. However, existing methods share two critical limitations: they decompose scenes into a flat set of slots at a single granularity, and this decomposition is based on appearance rather than semantics. Yet humans understand scenes through semantic hierarchies: separating foreground from background, recognizing object categories, and identifying individual instances. Crucially, such semantic hierarchies cannot emerge without supervision, because category names are human constructs, not visual patterns. We propose Hierarchical Slot Attention (HSA), which learns multi-granularity semantic scene decomposition from a single model. HSA decomposes scenes at three levels: holistic (foreground/background), semantic (object categories), and panoptic (individual instances). Using only 10\% labeled data, combined with hierarchical alignment loss, HSA learns all three levels jointly. We further introduce grouping purity and containment to measure whether the hierarchy is encoded in representation space, not just output masks. Experiments on COCO and PASCAL VOC demonstrate that HSA outperforms the strongest flat baseline by up to \textbf{$+$41.5} ARI at holistic, \textbf{$+$14.6} at semantic, and \textbf{$+$10.4} at panoptic level on COCO, with even larger gains on Pascal VOC, while requiring a single model instead of three. Code will be made available upon acceptance.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">4D Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>SkelGen4D: Weakly-Supervised Skeleton-Based 4D Generation for Text-Driven Mesh Animation</strong>
          <small>Hao Feng, Zhi Zuo, Jia-Hui Pan, Ka-Hei Hui, Zhengzhe Liu, Dian Zhang, Haoran Xie, Bin Sheng, Jingyu Hu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">4D Generation</span>
<span class="topic-tag">Mesh Animation</span>
<span class="topic-tag">Generative Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2607.08246</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08246">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 only loosely: it is a generative 4D content creation method, but it is not specifically about vision foundation models or embodied spatial intelligence.</p>
        <p class="abstract">We study 4D generation to synthesize temporally coherent sequences of 3D geometry for animation and content creation. In contrast to existing SDS-based optimization methods and video-driven animation approaches, we adopt a skeleton-driven animation framework aligned with standard industrial pipelines, which enables explicit control and editing. To this end, we propose SkelGen4D, a weakly supervised feed-forward framework for text-driven mesh animation that generates explicit skeleton motions without requiring per-frame skeleton annotations. SkelGen4D first recovers temporally consistent pseudo-skeletons from animated meshes via differentiable fitting, and then generates text-conditioned skeleton motion sequences in a feed-forward manner, further refined with Motion-GRPO to ensure temporally coherent, physically plausible, and articulated animation. We evaluate our method on two large-scale benchmarks, Truebones Zoo and Diffusion4D. Our results show that our weakly supervised skeleton modeling matches or surpasses fully supervised baselines while scaling to diverse object categories for high-quality text-driven mesh animation. Further, our method supports flexible motion editing and is aligned with standard animation production pipelines.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">RGB-T Fusion</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>Dual-Correlation Hypergraph Network for Unaligned RGBT Video Object Detection and A Large-scale Benchmark</strong>
          <small>Qishun Wang, Yapeng Li, Bin Luo, Zhengzheng Tu, Chenglong Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">RGB-T Fusion</span>
<span class="topic-tag">Video Object Detection</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2607.08191</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08191">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only loosely: it adds a new benchmark and method for RGB-T video object detection, but this is not strongly embodied AI.</p>
        <p class="abstract">RGB-Thermal (RGBT) Video Object Detection (VOD) has gained significant traction due to its ability to overcome the limitations of conventional RGB-based VOD under challenging conditions. However, spatial misalignment commonly exists between RGBT image pairs. To address this, we propose a Dual-Correlation Hypergraph Network (DHNet) that captures high-dimensional complementary information by explicitly modeling two types of correlations: temporal correlation across consecutive frames and spatial correlation from cross-modal features. Specifically, we first design a Patch-based Spatial Alignment Module (PSAM) to sequentially align the multimodal features at the local region level. Subsequently, we introduce a Dual Hypergraph Fusion Module (DHFM), which constructs separate temporal and multimodal hypergraphs to enhance object discriminability through dual-correlation learning. Furthermore, the field currently lacks a large-scale, scene-diverse benchmark dataset for comprehensive evaluation. To address this gap, we construct DVT-VOD1000, a large-scale RGBT VOD dataset containing 1,000 video sequences with 103,464 RGBT image pairs. The dataset covers diverse scenarios, including campuses, parks, transportation, rural areas, night scenes, rain, and snow. Comprehensive experiments on VT-VOD50 and our DVT-VOD1000 demonstrate that DHNet achieves state-of-the-art detection accuracy. The dataset and source code will be made publicly available on https://github.com/tzz-ahu/ to support academic research.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Re-Identification</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>Mixture of Enhanced-View Experts for Multi-Query Vehicle ReID and A Large-Scale Benchmark</strong>
          <small>Aihua Zheng, Jie Zhen, Chenglong Li, Jiaxiang Wang, Jin Tang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Re-Identification</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multi-View Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2607.08085</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08085">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only loosely: it introduces a new large-scale benchmark for multi-query vehicle ReID, which is vision-centric but not embodied AI.</p>
        <p class="abstract">Multi-query vehicle ReID aims to leverage complementary information from diverse views for robust feature learning. However, current methods suffer from simplistic feature fusion and thus easily ignores some important view information and cross-view relationships. To handle these problems, this work presents a novel approach called Mixture of Enhanced-View Experts (EV-MoE), which enhances the feature representation of each view and efficiently integrate the view-specific enhanced features by MoE, for robust multi-query ReID. In particular, we design a mixture of enhanced-view experts module, which consists of two parts including view-specific feature enhancement sub-Module (VFEM) and dynamic multi-view fusion sub-Module (DMFM). Moreover, we further introduce Multi-view Alignment Loss (MAL), which aligns features through bidirectional crossview contrastive learning and reconstruction constraints, addressing the challenges of consistency between multi-query features and single-image features. In addition, to evaluate multi-query ReID in real-world environments, we collect LCRI-1K, a largescale vehicle ReID dataset with 1,090 identities, 107,805 images, across 23,637 cameras, where each vehicle appears in an average of 67.5 cameras, providing a comprehensive benchmark to test the robustness in complex environments. Extensive experiments demonstrate the robustness of CAFNet in addressing the multiquery vehicle ReID problem. The code is available at https: //github.com/xiaozhen28/CAFNet.</p>
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
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>MentalHospital: A Virtual Environment for Evaluating Psychiatric Clinical Encounters</strong>
          <small>Yuming Yang, Xiao Sun, Yuanwei Zou, Zhengxiao Wu, Yun Chen, Jiang Zhong, Haoyang Zeng, Jingwang Huang, Kaiwen Wei</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">LLM Agents</span>
<span class="topic-tag">Clinical Simulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2607.08257</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08257">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it proposes a new benchmark/virtual environment for evaluating full psychiatric clinical encounters in an embodied, simulator-like setup.</p>
        <p class="abstract">Large language models (LLMs) have shown strong performance on isolated psychiatric tasks, including dialogue, diagnosis, and treatment planning, yet existing benchmarks rarely simulate complete psychiatric clinical encounters. We introduce $\textbf{MentalHospital}$, a virtual evaluation environment for LLM-based psychiatric clinical encounters. MentalHospital instantiates the Subjective Interviewing, Objective Examination, Diagnostic Assessment, and Treatment Planning (S.O.A.P.) workflow, using skill-augmented standardized patients constructed from 1,193 de-identified psychiatric electronic health record (EHR) cases spanning all major ICD-11 categories and 76 disorders. Each encounter is assessed through a dual-track protocol that combines objective comparison against EHR-derived references with subjective assessment of clinical process quality. To scale specialist judgment, we develop $\textbf{MentalEval}$, five domain-specific evaluators covering communication empathy, interviewing professionalism, clinical-note quality, diagnostic rigor, and treatment appropriateness, trained with rubric-grounded SFT and expert-guided DPO. Survey responses from 22 clinicians support MentalHospital&#x27;s clinical fidelity (3.88/5), while MentalEval achieves strong expert alignment with an average QWK of 0.944. Benchmarking shows that even the strongest LLM trails clinicians by 37.28 percentage points in objective psychiatric competence, with mental status assessment as a key bottleneck.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Active Perception</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>A First-Principles Theory of Slow Thinking and Active Perception</strong>
          <small>Hongkang Yang, Zhi-Qin John Xu, Feiyu Xiong, Weinan E</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Active Perception</span>
<span class="topic-tag">Theory</span>
<span class="topic-tag">Generative Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2607.08196</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08196">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very loosely: it offers a theory of active perception/slow thinking, but it is primarily a theoretical paper rather than a concrete spatial-intelligence method.</p>
        <p class="abstract">As part of a series on first-principles modeling of cognitive functions, this paper attempts to provide a mathematical formulation of thinking and perception. It formally derives slow thinking or more generally, active perception, and encompasses the design, training and inference of slow thinking large language models. Our starting point is the lifting and projection of probability distributions on the observable and latent spaces, with the objective of representing complex data distributions by simple function families such as neural networks. A theory called &quot;active lifting&quot; is proposed, based on the sampling of latent sequences and an intrinsic drive to reduce uncertainty with maximum rate. It derives a large design space, containing the slow thinking models in a subspace that we call the static theory. These models are positioned on the representation hierarchy and sampler hierarchy induced by the static theory, and can be upgraded by climbing the two hierarchies. Active lifting further derives an inference process with an internal time axis, and a training objective that resembles minimum-length coding as well as the invention of languages. Thus, it characterizes the agency of perception, including the emergence of the slow thinking formats. Technical by-products of this theory include a three-stage pathway for improving slow thinking models, a unified approach to constructing encoders and generative models for all data modalities, a priori formation of human-like visual representations, and a possible solution to policy collapse.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice</strong>
          <small>Qian Jiang, Zhecheng Shi, Jingpu Yang, Zirui Song, Miao Fang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Healthcare Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2607.08423</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.08423">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 4: a new VLM benchmark for nutrient reasoning and personalized health advice, with strong evaluation of model failures.</p>
        <p class="abstract">The rapid integration of Large Vision-Language Models (VLMs) into critical infrastructure promises to revolutionize   personalized healthcare and dietary management. However, in the domain of food systems, autonomous agents face a   unique and persistent challenge: the &quot;Systemic Information Asymmetry&quot; between visual appearance and intrinsic   nutritional composition. Existing benchmarks primarily focus on coarse-grained classification tasks, such as food   category recognition, which fail to evaluate the intricate reasoning chain required for real-world dietary management   -- specifically, the ability to traverse from identifying hidden ingredients to estimating physical mass, and finally   synthesizing safety-critical medical advice. In this paper, we introduce OmniFood-Bench, a comprehensive benchmark   constructed from the MM-Food-100K dataset. Unlike previous works, OmniFood-Bench evaluates VLMs across three   progressive capabilities: Basic Perception (Ingredients &amp; Cooking Methods), Quantitative Reasoning (Portion Size &amp;   Nutritional Profiling), and Safety-Critical Advisory (Disease-Specific Recommendations). We evaluate six   state-of-the-art VLMs, including gpt-5.1, gemini-3-flash, and qwen3-vl-8B. Our extensive experiments reveal a   startling &quot;Semantic-Physical Gap&quot;: while models achieve near-human accuracy in naming dishes, they exhibit   catastrophic failure in mass estimation and frequently hallucinate benign advice for high-risk diabetic profiles. This   work establishes a rigorous standard for trustworthiness in autonomous agents deployed for public health. The code   and datasets are available in: https://anonymous.4open.science/r/OmniFood-Bench-7D0B</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
