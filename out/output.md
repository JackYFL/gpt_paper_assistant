

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
      <p class="eyebrow">Daily ArXiv / October 01, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>9</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>17</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>12.0</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">action</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">additional</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">agent</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">change</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">connecting</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">control</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">domain</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">evidence</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">failure</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">generated</span><span class="cloud-word" style="font-size:2.31rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="10 mentions">generation</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">graph</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">guidance</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">harness</span><span class="cloud-word" style="font-size:2.31rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="10 mentions">head</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">intelligence</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">interaction</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">latent</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">manipulation</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">megaavatar</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">motion</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">multiple</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">object</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">outcome</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">planning</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">poincar</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">predict</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">preserve</span><span class="cloud-word" style="font-size:1.96rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="8 mentions">reasoning</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">safe</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="6 mentions">safety</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">scene</span><span class="cloud-word" style="font-size:1.96rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="8 mentions">scientific</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">shieldclip</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">spatial</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">spatially</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="5 mentions">supervision</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">support</span><span class="cloud-word" style="font-size:1.77rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="7 mentions">trajectory</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">understanding</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="6 mentions">unsafe</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="4 mentions">v-jepa</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="13 mentions">video</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">view</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="13 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.63rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="133 mentions">action</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="149 mentions">agent</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="59 mentions">alignment</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="66 mentions">annotation</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="58 mentions">architecture</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="64 mentions">attention</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="61 mentions">backbone</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="66 mentions">camera</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="59 mentions">challenging</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="70 mentions">consistency</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="61 mentions">control</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="57 mentions">dense</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="69 mentions">detection</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="59 mentions">domain</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="56 mentions">driving</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="105 mentions">dynamic</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="68 mentions">environment</span><span class="cloud-word" style="font-size:1.72rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 46%, var(--accent))" title="144 mentions">evidence</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="74 mentions">foundation</span><span class="cloud-word" style="font-size:2.26rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 74%, var(--accent))" title="216 mentions">generation</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="80 mentions">geometry</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="67 mentions">grounding</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="77 mentions">inference</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="105 mentions">interaction</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="91 mentions">language</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="58 mentions">latent</span><span class="cloud-word" style="font-size:1.25rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="93 mentions">memory</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="108 mentions">motion</span><span class="cloud-word" style="font-size:1.82rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="156 mentions">multimodal</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="66 mentions">multiple</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="139 mentions">object</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="94 mentions">observation</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="59 mentions">optimization</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="63 mentions">perception</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="60 mentions">pipeline</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="82 mentions">point</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="62 mentions">policy</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="63 mentions">query</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="67 mentions">question</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="145 mentions">reasoning</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="59 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="57 mentions">region</span><span class="cloud-word" style="font-size:1.74rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="146 mentions">scene</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="61 mentions">scientific</span><span class="cloud-word" style="font-size:1.67rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="138 mentions">semantic</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="59 mentions">source</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="66 mentions">space</span><span class="cloud-word" style="font-size:1.48rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="117 mentions">spatial</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="74 mentions">supervision</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="83 mentions">support</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="74 mentions">target</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="87 mentions">temporal</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="88 mentions">token</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="111 mentions">trajectory</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="84 mentions">understanding</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="75 mentions">unified</span><span class="cloud-word" style="font-size:2.26rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 74%, var(--accent))" title="216 mentions">video</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="76 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="298 mentions">visual</span><span class="cloud-word" style="font-size:1.48rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="116 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>2 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>ChronoGraph: Functional 4D Scene Graphs with Vision-Language Models for Interaction Understanding and Grounded Planning</strong>
          <small>Chenyangguang Zhang, Malgorzata Gwiazda, Guanlong Jiao, Yuanchen Ju, Federico Tombari, Koushil Sreenath, Marc Pollefeys, Sunghwan Hong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">4D Scene Graphs</span>
<span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">17</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2609.39665</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.39665">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criteria 1 and 3 closely: introduces a functional 4D scene graph for interaction understanding and grounded planning, plus a new benchmark and VLM training method.</p>
        <p class="abstract">Embodied agents must determine where to act, anticipate the resulting scene changes, and interpret observed outcomes to guide subsequent actions. This requires connecting 4D interaction understanding, which explains how past actions changed the scene, with spatially grounded planning, which determines how and where to act toward a goal and anticipates the resulting scene changes. We introduce ChronoGraph, a functional 4D scene graph that links actions on affordance parts to semantic and geometric state changes. By representing observed and anticipated transitions in the same form, it provides a shared basis for understanding and planning. We construct ChronoGraphBench through an automatic data engine that converts human-interaction videos and simulated robot trajectories into graph-annotated questions for training and evaluating Vision-Language Models (VLMs) on both tasks. Using these annotations, we train ChronoGraphVLM by adapting pretrained VLMs in two stages. Graph-as-Chain-of-Thought supervised fine-tuning teaches the models to reconstruct observed transitions and predict future ones as graph traces before answering. Subsequent joint 4D graph reinforcement learning directly rewards graph properties and answer correctness. Experiments across model scales show improvements over the corresponding pretrained baselines and zero-shot transfer to VLM4D. Real-world demonstrations further show that graph-based planning and affordance grounding support mobile manipulation through existing robot skills without additional fine-tuning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Computer-Use Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>OSWorld-Science: A Benchmark of Computer Use Agents for Learning and Using Scientific Software</strong>
          <small>Dingyuan Dai, Heli Qi, Lei Liu, Yinxi Li, Baiding Chen, Zijun Dou, Qingcheng Zeng, Qi Kang, Oliver Sun, Eric Wang, Bo Zhou, Haixin Wang, Yufan Du, Shi Bo, Ruihan Lin, Mengqi Yuan, Dunjie Lu, Steven Dillmann, Yiming Shi, Tina Su, Amy Xin, Minghao Liu, Xi Wang, Xu Huang, Ge Zhang, Pengyu Nie, Zhen Yang, Jie Tang, Juanzi Li, Weihao Xuan, Tianyu Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Computer-Use Agents</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Scientific Workflows</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2609.39903</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.39903">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied/computer-use benchmark for VLM agents in scientific software environments, with simulator-like interactive tasks and novel evaluation angles.</p>
        <p class="abstract">Scientific software presents a demanding test for computer-using agents based on visual language models (VLMs): completing a research workflow requires interpreting specialized interfaces, manipulating scientific objects, and producing verifiable results. We thus introduce OSWorld-Science, a benchmark and evaluation environment that combines scientifically meaningful tasks, artifact-based evaluation, and an efficient agent harness for studying computer use in the scientific domain. The benchmark contains 12 VLMs and 146 high-quality tasks across several scientific domains and software configurations, covering workflows such as molecular drawing and retrosynthesis, pathology image analysis, statistical computing, and physical simulation. Tasks are developed through expert proposals and iterative human--AI co-design, with selection guided by scientific value and difficulty. Task-specific execution-based evaluators inspect application states and generated artifacts, including molecular structures, segmentation masks, plots, and numerical results, and award partial credit for incomplete outcomes. Our special harness integrates model adapters, interaction-loop control, and trajectory logging to support comparisons of models and interaction strategies. Our results show that current state-of-the-art VLMs with a strong harness still face challenges in addressing key questions in the scientific domains. We also analyze the benchmarking results across multi-linguistics, reasoning efforts, context length and other factors and derive several important conclusions and directions to assist future development. Overall, we provide an integrated framework connecting expert-defined scientific goals to verifiable software outcomes, enabling systematic evaluation of both agent capabilities and harness design in scientific workflows.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>7 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Intelligence</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>KilometerVision: A New Frontier for Large-Scale Spatial Intelligence in VLMs</strong>
          <small>Aravindh Mahendran, Michael King, Matthew Koichi Grimes, Antoine Yang, Tyler Zhu, Joseph Heyward, Tengda Han, Shiry Ginosar, Chen Sun, Dima Damen, Simon Osindero, Noah Snavely, Simon Lynen, Jo\~ao Carreira, Viorica P\u{a}tr\u{a}ucean</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Intelligence</span>
<span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-high">17</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2609.39588</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.39588">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: it introduces a benchmark for large-scale spatial intelligence in VLMs, explicitly probing geographical layout understanding over kilometer-scale videos.</p>
        <p class="abstract">We push the frontier of large-scale spatial intelligence in Vision-Language Models (VLMs) and introduce the first benchmark that probes geographical layout understanding from real-world videos, spanning up to 1km distances. Inspired by the cognitive science literature, we evaluate models against the hierarchical stages of human spatial awareness: anchoring via landmarks, connecting them through routes, and integrating these into global mental maps. Extensive experiments reveal a fundamental divergence in how current AI models process spatial information. Instead of utilising true path integration or forming geometric survey knowledge, we find that VLMs rely almost entirely on 2D visual recognition and text-matching to bypass complex spatial reasoning. The benchmark is publicly available at https://perception-test-challenge.github.io/kilometervision.html.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Self-Supervised Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>Emergent Multi-View Geometry Through Self-Distillation</strong>
          <small>David Nordstr\&quot;om, Thibaut Loiseau, Vincent Lepetit, Michael Felsberg, Guillaume Bourmaud, Fredrik Kahl</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Multi-View Geometry</span>
<span class="topic-tag">3D Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2609.39227</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.39227">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it is a vision foundation model/self-supervised representation paper using multi-view geometry, with applications to pose estimation and 3D reconstruction.</p>
        <p class="abstract">Over a century ago, Henri Poincar\&#x27;e argued that a motionless observer cannot acquire the notion of space. Yet, most visual representation learning methods operate on individual images, while those that leverage multiple views rely on RGB reconstruction, entangling geometry with appearance. We propose Poincar3, a self-supervised method that learns representations from multiple views through self-distillation instead of RGB reconstruction. We combine masked patch and image-level distillation with a teacher that observes additional views, enabling training from scratch without explicit 3D supervision. Poincar3 outperforms both previous single and multi-view self-supervised approaches such as DINOv3, MuM, and Muskie on correspondence estimation, camera pose estimation, and 3D reconstruction. Using a lightweight Poincar\&#x27;e adapter, we also find that our learned features encode camera motion more accurately than existing self-supervised representations.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Talking Avatar Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>MegaAvatar: Controllable Talking Avatar Generation</strong>
          <small>Junyao Gao, Sibo Liu, Weidong Zhang, Cairong Zhao, Jun Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Talking Avatar Generation</span>
<span class="topic-tag">Video Foundation Models</span>
<span class="topic-tag">Multimodal Control</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2609.39273</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.39273">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it is a new multimodal/video generation model for controllable talking-avatar synthesis built on a large vision-language/video foundation model.</p>
        <p class="abstract">This report presents \textbf{MegaAvatar}, a controllable talking avatar generation framework built on top of the Wan2.2-TI2V-5B model. Compared with previous talking-avatar methods that mainly rely on audio or reference-image conditioning, we introduce additional SMPL-X-derived 3D guidance, enabling global control over body pose and head motion. Specifically, we render the driving SMPL-X sequence into dense mesh frames and encode them with a lightweight 3D convolutional encoder, whose outputs are injected into the latent tokens to provide overall motion control. Furthermore, we extend Wan2.2-TI2V-5B with additional audio and face cross-attention modules to enable fine-grained expression control and preserve the input identity, respectively. In addition, we implement an audio-to-SMPL-X model to predict an SMPL-X sequence conditioned on the reference image and input audio, allowing MegaAvatar to support audio-driven inference without user-provided SMPL-X frames. Experiments show that MegaAvatar achieves high-quality talking avatar generation with controllable body and head motion, speech-synchronized facial expressions, and consistent identity preservation. MegaAvatar also supports inference with flexible resolutions and video lengths. Codes, dataset, models will be avaliable in https://github.com/Jeoyal/MegaAvatar</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Exo2EgoHOI: Hand-Object-Interaction Aware Exocentric-to-Egocentric Video Generation</strong>
          <small>Hongjia Zhai, Xiyu Zhang, Haoran Zhang, Zhichao Ye, Haomin Liu, Guofeng Zhang, Ian Reid, Xingxing Zuo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Egocentric Video Generation</span>
<span class="topic-tag">Human-Object Interaction</span>
<span class="topic-tag">Generative Modeling</span>
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
          <span>Paper 6 / arXiv:2609.38615</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.38615">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: an embodied-AI method for exocentric-to-egocentric video generation focused on preserving hand-object interactions and object consistency.</p>
        <p class="abstract">Egocentric videos of human manipulation provide valuable visual experience for embodied intelligence, yet collecting such data at scale is costly. Exocentric-to-egocentric video generation offers a scalable alternative by transforming abundant third-person manipulation videos into first-person observations. However, existing methods often struggle to faithfully preserve demonstrated hand-object interactions (HOI) across large viewpoint changes due to insufficient fine-grained interaction guidance and weak object-centric anchoring. We present Exo2EgoHOI, an HOI-aware video generative framework for interaction-preserving exocentric-to-egocentric translation. To preserve fine-grained HOI, we introduce a unified 4D HOI prior that combines scene geometry, articulated hand renderings, and dense hand-object relation fields, together with a dual-branch residual adapter for injecting structural and relational cues into the video generation backbone. To preserve object consistency, we introduce Decomposed Gated Cross-Attention, which separately encodes object and background references and adaptively integrates global semantic and local appearance features as object-centric anchors. Experiments on ARCTIC-HOI and Ego-Exo4D demonstrate substantial improvements in object consistency and HOI preservation while maintaining competitive visual fidelity. In particular, on ARCTIC-HOI, Exo2EgoHOI improves object mIoU by 32.3% and reduces MPJPE and PA-MPJPE by 34.7% and 50.0%, respectively, relative to the respective best baseline results. Project page: https://rcl-robotics.github.io/Exo2EgoHOI/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical VLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models</strong>
          <small>Chunzheng Zhu, Jiaqi Zeng, Hongbo Zhao, Yihang Chen, Yijun Wang, Jianxin Lin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical VLMs</span>
<span class="topic-tag">Mechanistic Interpretability</span>
<span class="topic-tag">Model Safety</span>
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
          <span>Paper 7 / arXiv:2609.38810</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.38810">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is mechanistic interpretability and safety analysis for medical VLMs rather than a new VLLM/MLLM method or spatial/embodied benchmark.</p>
        <p class="abstract">As vision language models are increasingly deployed in clinical diagnosis, understanding how they internally resolve competing visual and textual signals becomes a safety imperative. Existing mechanistic analyses remain confined to unimodal text and offer no explanation for why a single misleading sentence can override a correct image based diagnosis, or why a model commits to a confident answer despite insufficient visual evidence. We find that these two safety risks, arbitration failure where textual context overrides visual grounding and brake failure where the model commits without adequate evidence, are mediated by spatially disjoint attention head populations: arbitration heads form a mid-to-deep wideband reflecting cross-layer evidence competition, while brake heads concentrate in a narrow middle-to-late layer band that regulates evidence sufficiency and abstention behavior. To ground these observations in causal circuitry, we introduce CRAFT, which localizes each failure mode to a minimal causal head set via dual criteria and verifies necessity and sufficiency through temporal probes and Tuned Lens trajectory analysis. Excising arbitration heads sharply reduces conflict following with negligible degradation on clean inputs, while excising brake heads restores appropriate abstention under degraded visual evidence. The two interventions target spatially disjoint head sets and produce distinct corrective effects, underscoring the mechanistic separability of the failure modes. Experiments across multiple medical VQA benchmarks and VLM architectures validate both the localization and interventions, demonstrating that the identified heads causally drive each failure mode and that targeted modulation generalises without retraining. The code is available at GitHub repository.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Safety</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>ShieldCLIP: Selective Safety Alignment for Harmful Content Mitigation in Multimodal Foundation Models</strong>
          <small>Tobia Poppi, Silvia Cappelletti, Samuele Poppi, Marcella Cornia, Lorenzo Baraldi, Diego Garcia-Olano, Rita Cucchiara</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Safety</span>
<span class="topic-tag">CLIP Alignment</span>
<span class="topic-tag">Harmful Content Mitigation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.MM</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2609.39688</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.39688">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is safety alignment for multimodal foundation models, not a spatial/embodied or benchmark-focused vision foundation paper.</p>
        <p class="abstract">Multimodal encoders such as CLIP underlie many downstream systems, but their web-scale training data embed harmful associations that safety alignment must suppress without unnecessarily changing benign representations. Because ethical and practical constraints prevent collecting real unsafe content at scale, existing datasets pair safe real samples with generated counterparts, but label every generated sample unsafe, even when one modality is individually safe. To address this, we introduce ShieldCLIP, the first framework to condition safety alignment on the observed safety state of each modality rather than the origin of a sample, preserving safe content while redirecting only what is unsafe. We also introduce ViSUv2, a 195k-quadruplet dataset with independent per-modality safety labels across 578 concepts and 28 categories. Using these labels, ShieldCLIP defines a four-way conditional objective beyond pair-level supervision: safe content is anchored, unsafe modalities are redirected to their safe counterparts, mixed pairs update only the unsafe branch, and coherence is enforced when both are unsafe. We evaluate ShieldCLIP on cross-modal retrieval, text-to-image generation with Stable Diffusion v1.4 and SDXL, and image-to-text generation with LLaVA. Across these settings, ShieldCLIP consistently reduces harmful outputs over prior safety-aligned encoders and strong mitigation baselines, while preserving the utility of the original embedding space. Extensive ablation studies further show that both modality-specific supervision and the selective alignment objective contribute to these gains. Source code, trained models, and ViSUv2 (under a controlled-access protocol) will be made publicly available at https://aimagelab.github.io/ShieldCLIP/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>VR-JEPA: Learning Contrastive-State Latent Guidance for Generation-based Video Reasoning</strong>
          <small>Zehua Ma, Kun Xiang, Yunshuang Nie, Quanlin Chen, Haoyuan Li, Xiuwei Chen, Jiang Ji, Haijun Wu, Zhenyu Xie, Michael Kampffmeyer, Hanhui Li, Xiaodan Liang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Reasoning</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Latent Dynamics</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2609.40129</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.40129">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is about generation-based video reasoning and latent guidance, which is adjacent to multimodal learning but not a clear VLLM/MLLM or embodied/spatial benchmark paper.</p>
        <p class="abstract">Reasoning through video generation offers a promising path toward visual intelligence by modeling latent visual states and their dynamics. However, current video generation models often lack explicit guidance on how these states should evolve, leaving generated trajectories prone to physical and structural inconsistencies that undermine reasoning reliability. While the Video Joint-Embedding Predictive Architecture (V-JEPA) provides rich spatiotemporal priors learned through latent prediction, these general priors do not naturally adapt to the logical reasoning capabilities required for complex visual tasks. To bridge this gap, we propose VR-JEPA, a framework that aligns the V-JEPA predictor with task-specific reasoning logic through localized contrastive-state learning and uses its predicted latent trajectories to guide video generation for visual reasoning. Specifically, (i) we pair successful trajectories with generated alternatives under the same input conditions and use discrepancies in their V-JEPA representations to identify informative states and tokens for localized contrastive supervision. (ii) We further equip the V-JEPA predictor with skill-specific experts trained on anchor-task data, allowing the model to adaptively specialize its shared spatiotemporal priors across diverse cognitive domains. Together with skill-specific experts, this contrastive supervision enables VR-JEPA to predict latent trajectories that provide task-specific logical guidance for video generation. Comprehensive experiments on the large-scale VBVR-Pro-Bench dataset demonstrate that VR-JEPA achieves an $11.33\%$ relative improvement over the cutting-edge generation-based reasoning baseline, significantly mitigating physical artifacts and enhancing logical consistency.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-09-04.html">
          <span>September 04, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-03.html">
          <span>September 03, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-02.html">
          <span>September 02, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-01.html">
          <span>September 01, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-31.html">
          <span>August 31, 2026</span>
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
