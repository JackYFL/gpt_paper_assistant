

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
      <p class="eyebrow">Daily ArXiv / November 20, 2026</p>
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
      <strong>15</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>11.6</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">absclaw</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">accurate</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">acquire</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">action</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="31 mentions">agent</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">answer</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">condition</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">decision</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">draft</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">dynamic</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">editor</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">embodied</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">environment</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">event</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">evidence</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">execution</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">experience</span><span class="cloud-word" style="font-size:1.54rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="11 mentions">figure</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">four</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">game</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">generative</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">graph</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">interaction</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">judge</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">knowledge</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">loop</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">memory</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">multimodal</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">navigation</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">physical</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">question</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">radiologist</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">read</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="9 mentions">real</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">real-world</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">reasoning</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">robot</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">simulation</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">skill</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">slice</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="9 mentions">step</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">target</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">visual</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">weight</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="83 mentions">action</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="37 mentions">against</span><span class="cloud-word" style="font-size:2.61rem;opacity:0.96;color:color-mix(in srgb, var(--accent-2) 92%, var(--accent))" title="181 mentions">agent</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="50 mentions">alignment</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="54 mentions">answer</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="45 mentions">attention</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="51 mentions">camera</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="44 mentions">change</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="44 mentions">control</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="47 mentions">detection</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="37 mentions">domain</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="42 mentions">dynamic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="36 mentions">embedding</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="53 mentions">environment</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="49 mentions">error</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="86 mentions">evidence</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="49 mentions">execution</span><span class="cloud-word" style="font-size:1.82rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="103 mentions">generation</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="44 mentions">generative</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="42 mentions">geometry</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="37 mentions">grounding</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="54 mentions">inference</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="55 mentions">interaction</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="50 mentions">language</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="61 mentions">latent</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="69 mentions">memory</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="45 mentions">motion</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="62 mentions">multimodal</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="40 mentions">multiple</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="82 mentions">object</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="50 mentions">observation</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="39 mentions">pair</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="57 mentions">physical</span><span class="cloud-word" style="font-size:1.39rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="70 mentions">point</span><span class="cloud-word" style="font-size:1.33rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="66 mentions">policy</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="40 mentions">prompt</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="57 mentions">question</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="41 mentions">real</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="96 mentions">reasoning</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="47 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="41 mentions">region</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="41 mentions">reward</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="36 mentions">robot</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="59 mentions">same</span><span class="cloud-word" style="font-size:1.51rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="79 mentions">scene</span><span class="cloud-word" style="font-size:1.81rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="102 mentions">semantic</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="39 mentions">space</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="63 mentions">spatial</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="52 mentions">step</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="57 mentions">structure</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="43 mentions">supervision</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="57 mentions">support</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="46 mentions">target</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="51 mentions">token</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="50 mentions">trajectory</span><span class="cloud-word" style="font-size:2.13rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 67%, var(--accent))" title="131 mentions">video</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="47 mentions">view</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="50 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="199 mentions">visual</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="68 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>11 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>Space-X: Self-Evolving Spatial Agents Weaving Clues into Evidence Chains</strong>
          <small>Zijian Zhang, Wenqing Tian, Qiang Liu, Liang Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Embodied Agents</span>
<span class="topic-tag">Tool-Augmented Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2611.24004</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24004">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 1: it is explicitly about spatial reasoning for embodied agents and evidence-chain construction from visual/geometric clues.</p>
        <p class="abstract">Spatial reasoning connects visual observations, geometric estimates, and linguistic decisions into a coherent derivation. Yet tool-augmented agents often acquire evidence without clear targets, combine outputs under inconsistent object or reference-frame semantics, and misjudge evidence sufficiency. Thus, more tools or calls do not reliably improve reasoning. We introduce Space-X, a spatial-reasoning framework that self-evolves toward complete, continuous evidence-chain construction. An Execution Agent acquires, associates, and judges evidence per problem using role-specific memory. A Control Agent diagnoses evidence-chain breaks from execution traces and jointly revises tools, interfaces, skills, memory organization, and decision rules. This loop co-evolves capability and evidence use: evidence needs guide capability development; usable results guide actions. Across multiple benchmarks, Space-X yields gains with four base models. Relative to baselines, GPT-6-sol improves answer accuracy on ViewSpatial and MMSI by 50.39% and 23.07%, respectively; Gemini-3.8-Flash gains 47.50% and 25.22% on these benchmarks. This provides a unified route from fragmented spatial clues to traceable, derivable answers.</p>
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
          <strong>Embodied Graph: A Relational World Model for Long-Horizon Tasks</strong>
          <small>Zongyuan Wu, Xin Wang, Tongtong Feng, Yuan Meng, Zeyang Zhang, Ling Feng, Wenwu Zhu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Graph-Based Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2611.24115</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24115">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 1 and criterion 3: it proposes a relational world model for embodied long-horizon planning, with experiments in Minecraft/Crafter and web interaction.</p>
        <p class="abstract">Long-horizon tasks in embodied and web environments involve extended decision sequences and delayed feedback, making accurate planning crucial for success. World models tackle this by learning latent dynamics for imagination-based planning. However, existing approaches merely rely on dense pixel-level observations, which forces the model to absorb redundant information while overlooking relations among task-relevant entities. Consequently, small errors may accumulate over long imagined rollouts and gradually corrupt the predictions. In this paper, we explore world models that imagine over sparse state abstractions, which poses two key challenges: 1) how to remove redundant information and form a compact state abstraction; 2) how to incorporate the relational structure to learn reliable long-horizon dynamics. To address these challenges, we propose Embodied Graph, a relational state abstraction that supports structured dynamics modeling and long-horizon imagination, and the Relational World Model (RWM), which performs imagination directly over graph states. RWM consists of (i) a Task-Aware Embodied Graph Constructor that filters redundant details and maintains graph memory through online updates, and (ii) an Embodied Graph Recurrent State Space Model that learns node-wise latent dynamics while capturing inter-node dependencies. The imagined graph states provide predictions of action consequences to guide decision-making. Experiments on Minecraft and Crafter demonstrate the effectiveness of RWM in embodied environments. Notably, in Minecraft, RWM is the only method that obtains diamonds within the given budget. Experiments on web interaction further illustrate the applicability of relational state prediction to the decision making process of web agents.</p>
      </div>
    </details>


    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>RoboBuilder: Agentic Robot Co-Design with Real-world Video Feedback in the Loop</strong>
          <small>Ghadi Nehme, Dahyun Nam, Akshay Govind Srinivasan, Faez Ahmed</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Robot Design</span>
<span class="topic-tag">Sim-to-Real</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2611.23855</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23855">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it is an embodied/robotic co-design benchmark with real-world video feedback, explicitly closing the sim-to-real loop for robot design.</p>
        <p class="abstract">Can AI agents design robots that work in the real world? We introduce RoboBuilder, a benchmark in which coding agents co-design a robot&#x27;s hardware and program from standard parts, motors and a custom 3D-printed part, and every design that passes in simulation is built and tested on a physical course. Simulation alone is not enough: under public part data, none of 15 initial passing designs crossed the real course, so an agent learns the simulator from measurements it requests and videos of real runs. Across four frontier coding agents, ten obstacles at three difficulty levels, 16,427 simulations of 12,774 distinct robots and 135 physical robots built in an estimated 240 hours, agents solve nearly all easy obstacles and invent mechanisms our search baselines do not reach, but falter at harder levels, when one robot must cross every obstacle, and in the real world, where 66% of simulated passes hold across all levels. Closing the loop helps: shown a video of its real failure, an agent redesigns the robot, sometimes correcting its simulator, and removes 72% of level-1 and level-2 failures. RoboBuilder measures progress toward agents that engineer real machines. Project Page: https://ghadinehme.com/robobuilder.github.io/</p>
      </div>
    </details>


    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>OpenKAGE: Open-Ended Lifelong Learning in the Open World via Knowledge-Sharing Agent-Group Evolution</strong>
          <small>Wenhao Yuan, Longhui Yuan, Zexi Jia, Ningzhe Shi, Jingwei Li, Shipeng Cen, Pengcheng Luo, Jie Zhou, Jinchao Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Lifelong Learning</span>
<span class="topic-tag">Knowledge Sharing</span>
<span class="topic-tag">Minecraft</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.MA</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2611.24302</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24302">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it proposes a new embodied-agent lifelong learning framework in Minecraft, centered on open-ended skill accumulation and knowledge sharing across agents.</p>
        <p class="abstract">Building autonomous agents that continually explore open worlds and acquire new capabilities through experience is a long-standing aspiration in artificial intelligence. Existing research often pursues lifelong learning within predefined tasks, curricula, or objectives, with self-improvement largely confined to individual agents. We introduce OpenKAGE, an agent-group evolution framework for open-ended lifelong learning. Within this framework, agents autonomously explore open worlds and continually acquire new capabilities by accumulating and reusing knowledge from their own interactions and the experience of others. OpenKAGE builds on two key mechanisms: (1) a two-layer knowledge representation, with a memory layer for situated memories and an experience layer for transferable experience and skills that retains the applicability conditions needed for reuse; and (2) a knowledge-sharing mechanism that semantically consolidates textual experience into a continuously evolving shared knowledge graph, while executable skills are shared verbatim. In Minecraft, OpenKAGE supports open-ended lifelong learning, enabling agent groups to sustain exploration and reach advanced technological milestones. Furthermore, the accumulated knowledge can be transferred to a newly initialized agent group on a different backbone model, improving its survival and exploration progress.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Vanguard: Knowing When to Trust the Draft in Speculative Vision-Language Agents</strong>
          <small>Hanqi Mao, Jiajun Fan, Ruihan Guo, Shuaike Shen, Ziwen Wang, Hui Ren, Xianrui Zhong, Ge Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Agents</span>
<span class="topic-tag">Speculative Decoding</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2611.23917</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23917">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 2, and also relevant to criterion 3 through embodied/mobile agents: it studies speculative VLM agents with a screenshot-aware judge.</p>
        <p class="abstract">Vision-language agents that browse websites, operate phones and act in homes reason before every action, so every step waits for a large model, a latency and cost that stand in the way of deployment. Step-level speculation lets a small model draft each step and calls the large model only on rejected drafts, but its outcome rests on the judge, and a judge that reads only a step&#x27;s text cannot tell whether the step fits the screen it acts on. We find that a few samples of a small model can contain a correct step about as often as the large model gets the step right, and not always on the same steps: checked against the screen, small drafts can be not only cheaper but better. We present Vanguard, a training-free judge that leaves the draft and target models unchanged: a general decision model, with the screenshot in view, gives each candidate step a probability of being right in one forward pass; the best candidate is kept if it clears a threshold, and otherwise the large model writes the step. On web, mobile and embodied agents, a 2B draft judged by Vanguard is at least as accurate as its 8B target and significantly more accurate on Mind2Web and EB-ALFRED, while the target writes only a minority of the steps; it completes far more closed-loop episodes, and with a 27B target from another family it is both faster and more accurate. Vanguard is the most accurate judge we compare on the agent tasks; it relies on the screenshot on web and mobile tasks, its calibrated threshold transfers to unseen websites, and across model families its gain over the target grows with the draft&#x27;s pass@4 relative to the target&#x27;s accuracy. Vanguard composes with token-level speculative decoding and matches trained process reward models on mathematics, turning speculation from a way to save the large model&#x27;s work into one that can improve on it.</p>
      </div>
    </details>


    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Diagnostic Accuracy and Navigation Behavior of Vision-Language Model Agents Reading Emergency CT and MRI Examinations</strong>
          <small>Jonathan Lichtle, Aymen Meddeb, Antonin Birot, Ibrahima Niang, Lisa Gastaud, Riyad Hanafi, Sofiane Dujardin, Corentin Selomme, Guillaume Cachard, Aghiles Hamroun, Gr\&#x27;egory Kuchcinski, Su Hwan Kim, Bastien Le Guellec</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Agents</span>
<span class="topic-tag">Medical Imaging</span>
<span class="topic-tag">Behavior Analysis</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2611.23480</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23480">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>3</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: it analyzes VLM agents’ navigation and decision behavior in medical image reading, giving an insightful evaluation of how visual-language agents explore and commit to hypotheses.</p>
        <p class="abstract">Purpose. To evaluate the diagnostic accuracy and image navigation behavior of vision-language model (VLM) agents under varying exploration strategies. Materials and Methods. In this retrospective study, six VLMs read 100 emergency CT and MRI examinations published in a public archive (March 2025-August 2026) under four conditions (free navigation, navigation from a key slice, and all slices or key slices in a single request), twice each (4800 runs). Nine radiologists read 30 of those cases. A large language model judge validated against two radiologists graded the answers. Conditions were compared with generalized estimating equations clustered by case. Results. Pooled accuracy was lowest under free navigation (32.6%; 391/1200), followed by navigation from a key slice (37.9%; 455/1200; P = .003), and highest with all slices (42.2%; 506/1200) or key slices (42.5%; 510/1200) in one request (both P &lt; .001). On the 30 cases read by radiologists, freely navigating models were correct in 30.0% of runs (108/360) versus 77.0% for radiologists (208/270; P &lt; .001). Models formed a first hypothesis after a median of 10.8% of the slices and kept it in 63.1% of runs (755/1196); final answers were correct in 12.4% of runs after a wrong first hypothesis (110/885) versus 90.4% after a right one (281/311; P &lt; .001). Median stated confidence in the final answers was 90%, whereas 38.9% of them were correct (1861/4778). Conclusion. Across all exploration strategies, VLM agents remained far less accurate than radiologists. They adopted an early hypothesis and usually kept it, seldom correcting a wrong one.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial-Temporal Alignment</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>From Points to Trajectories: Rethinking Multimodal Alignment for Physical Events</strong>
          <small>Yiyang Zhu, Guangyuan Liu, Jingdi Lei, Li Wei, Chau Yuen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial-Temporal Alignment</span>
<span class="topic-tag">Physical AI</span>
<span class="topic-tag">Multimodal Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">eess.SP</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2611.24249</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24249">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: it introduces a method for finer-grained spatial/temporal multimodal alignment for physical events, aimed at improving understanding of cross-modal dynamics over time.</p>
        <p class="abstract">Advancing physical artificial intelligence (Physical AI) requires moving beyond static object recognition to ground how real-world mechanics (e.g., impact, friction, and force transfer) unfold over time. While multimodal aligners seek to capture these interactions by matching multi-sensor streams, prevailing architectures compress each temporal sequence into a single pooled embedding. We show that this paradigm fails on twin events: distinct physical executions recorded under identical task conditions. Collapsing the temporal dimension averages out transient cross-modal dynamics, effectively reducing physical event alignment to static scene recognition. Formally, we prove that as sequence length increases, any temporally pooled representation converges to the stationary recording condition. Consequently, as windows grow, no choice of loss function or embedding geometry can disambiguate twin events from pooled features alone. Instead, we show that physical events are uniquely identified by the event gap, namely the instantaneous, synchronous co-fluctuations across modalities that are erased by pooling and accumulate only along unpooled trajectories. To recover this signal, we introduce CounterPoint, a lightweight plug-in module that strips out each modality&#x27;s temporal mean to score frame-level cross-modal agreement. Integrated across four state-of-the-art (SOTA) multimodal aligners, CounterPoint shifts representations from coarse condition matching to fine-grained physical event alignment, consistently outperforming existing temporal alignment methods.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Continual Tool-Space Extension Learning for Multimodal Agents</strong>
          <small>Jinbae Seo, Jungin Park, Hyunsung Jang, Namkoo Ha, Jiyoung Lee, Kwanghoon Sohn</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Agents</span>
<span class="topic-tag">Tool Use</span>
<span class="topic-tag">Continual Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2611.23810</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23810">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 2, and a mild fit for criterion 4 via specialist vision tools: it extends multimodal agents with new tools and evaluates vision-language benchmarks.</p>
        <p class="abstract">Multimodal agents largely rely on generic tools such as cropping, search, and code execution, leaving specialist vision models outside their tool space. However, bringing such a model into an already trained agent is not straightforward. The challenge is to learn each new tool efficiently while retaining the ability to use existing ones. This work proposes COTEX, continual tool-space extension learning, that adds new tools at efficient adapter-level cost. COTEX locates two sets of parameter directions; one triggers a tool call and thereby opens a multi-turn reasoning trajectory, while the other determines which tool is chosen. The adapter of a new tool is restricted to the calling directions that leave earlier tool choices unaffected by orthogonal constraint. We further introduce a protocol that converts specialist models&#x27; existing task-specific annotations into verified tool-use trajectories. Experiments on two representative agents and three specialist tools show gains on ten vision-language benchmarks, with at most a 0.3-point drop on existing tools.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Think Offline, Act in Real Time: Self-Improving Visual Game Agents through Code</strong>
          <small>Zipeng Qiu, Shusheng Xu, Jiale Li, Yukun Zhou, Chenyue Li, Wenshuang Li, Tongkai Yang, Binhang Yuan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Agents</span>
<span class="topic-tag">Game Agents</span>
<span class="topic-tag">Self-Improvement</span>
<span class="topic-tag">Program Synthesis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2611.24590</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24590">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it studies a new method for self-improving visual game agents, with code-as-policy for real-time embodied-like interaction and online adaptation.</p>
        <p class="abstract">Pre-trained models can read screens and reason about games, yet on an unfamiliar game, an agent still has to learn to play. We ask how an agent can self-improve on such a game from a few of its own attempts, in real-time visual games where the agent sees only the screen and the game keeps running while the agent thinks. We study two kinds of policy that can carry this improvement. In model as policy, a model selects actions during play; we adapt real-time chunking so that committed actions keep executing while the model reasons, and train a 2B controller for this interface. In code as policy, a model writes, tests, and revises a program between attempts, and the program acts during play. Across 170 GameWorld tasks, with at most eight one-minute executions per run, code as policy reaches 47.80% mean progress, against 30.90% for our trained controller, and leads in all five game categories. Improving the controller&#x27;s weights on a single game, by contrast, yields only modest gains. These results favor letting a model think offline and storing what it learns in a program that acts in real time. Project repository: https://github.com/TabibitoQZP/SIGame</p>
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
          <strong>ABSClaw: From Invented Worlds to Reality-Grounded Social Simulation</strong>
          <small>Shaobin He, Yan Gao, Quan Zheng, Zhenyang Lin, Zhen Liu, Jiyan He, Shuxin Zheng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Social Simulation</span>
<span class="topic-tag">Agent-Based Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2611.24517</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24517">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Partial match to criterion 3: it builds a new benchmark and simulator framework for social simulation, but it is not really embodied AI or spatial intelligence.</p>
        <p class="abstract">LLM-based artificial societies exhibit rich behavior but often lack scientific grounding: personas and environments are assumed, interaction networks are synthetic, and simulators are generated as free-form code, making results difficult to tie to real populations and sensitive to the backbone model. We argue that simulated worlds should be sampled from observed data, while simulation logic should be implemented by composing operations from a shared, task-independent vocabulary. In this paper, we introduce ABSClaw, a zero-code agent that compiles natural-language requests into executable, reality-grounded social simulations. ABSClaw grounds who acts, where they act, and with whom they interact in survey and census data, geospatial sources, and real networks. It expresses state transitions through 26 atomic operations. To support an open and extensible ecosystem, ABSClaw further allows capabilities to be added as lifecycle-scoped skills without modifying its core. Furthermore, we propose ABSBench, a benchmark of 193 real-world social-simulation tasks. On ABSBench, ABSClaw achieves the best overall performance among the evaluated social simulators. Three real-world case studies show that grounding personas, environments, and interaction networks each improves agreement with observed outcomes. With one runtime skill, ABSClaw executes 13 population-scale simulations, collectively involving 25 million agents. Together, these results demonstrate ABSClaw&#x27;s real-world fidelity, extensibility, and scalability.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Document Understanding</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>When Figures Disagree with Text: Evaluating Autonomous Visual Evidence Verification in Scientific Papers</strong>
          <small>Guijia Zhang, Hongbo Qiu, Jiajun Zha, Guohao Cai, Hao Zheng, Huihao Jing, Kexu Cheng, Shipeng Luo, JinYang Huang, Shing-Chi Cheung, Changsheng Lu, Haoxuan Che, Harry Yang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Document Understanding</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Vision-Language Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2611.24353</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24353">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it is a new benchmark/evaluation setting for multimodal document understanding focused on autonomous figure-text verification in full scientific papers.</p>
        <p class="abstract">Scientific figures carry evidence for the claims that cite them, so reviewing a paper means checking that a figure agrees with the text, and not only describing what the figure shows. Benchmarks of figure-text verification typically hand the model the figure, the claim, or the knowledge that an inconsistency exists, which leaves untested whether a model can find the figure worth checking in a complete paper, relate a visual element to the claim it conflicts with, and recognize the conflict. We study this autonomous setting on 31 full manuscripts, each carrying a reviewer-documented figure-text inconsistency from PRISMM-Bench that is hidden from the model. Six multimodal models review each PDF under a neutral prompt, and we then add one input at a time to the same manuscripts. Of 1,445 open-ended reviews, 60.6% mention the flawed figure, yet a grading rubric accepts only 3.3% as diagnosing its contradiction; a blind audit finds the rubric lenient, so we read these as rubric-accepted rates and compare conditions rather than absolute values. In a separate controlled run, naming the figure, without stating that it is flawed, raises rubric-accepted diagnosis from 4.3% to 20.4%, while a consistency instruction and coarse visual cues do not. When the contradiction is visible only in the rendered figure, text-only review yields no accepted diagnosis, while review of the rendered pages with the figure named reaches 15.8%. A baseline that lets the model choose which figures to check, ranked by centrality, stays at 4.8%. Deciding what to verify is thus a large part of the difficulty, and the selection rule we tested does not resolve it. Multimodal document understanding should be evaluated on whether a model can propose what to verify, not only answer questions about a figure it is handed.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>2 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">3D Reconstruction</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>Infer3D: Inverse Generative Modeling Enables Robust 3D Reconstruction</strong>
          <small>Amani Kiruga, Mark Hamilton, Joshua B. Tenenbaum, William T. Freeman, Vincent Sitzmann, Yilun Du, Ayush Tewari</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Out-of-Distribution Generalization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2611.25061</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.25061">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 4: it is a vision-reconstruction method centered on inverse generative modeling, with broader vision foundation-model style implications.</p>
        <p class="abstract">Humans can understand the 3D structure of scenes even from highly unfamiliar or extreme viewpoints. Cognitive science suggests this generalization stems from a top-down generative inference strategy. In contrast, state-of-the-art 3D reconstruction neural networks typically rely on amortized, feedforward inference. While fast, this pattern-matching approach degrades when faced with out-of-distribution (OOD) scene conditions unseen during training. Inspired by the generative nature of human vision, we propose Infer3D, an inverse generative modeling framework that recovers the latent variables of a generative model to best match the monocular input. To prevent degenerate flat outputs, we couple the generative image prior with a frozen 3D lifting network that constrains the optimization space to a valid, multi-view-consistent 3D manifold. Across a variety of controlled synthetic and real-world tasks, Infer3D demonstrates superior OOD reconstruction accuracy compared to feedforward networks trained on equal or larger datasets. Furthermore, mirroring how human perception requires more time to process confusing stimuli, we introduce an adaptive inference strategy that expends more test-time compute on ambiguous OOD examples while efficiently routing in-distribution inputs. Project website: https://amanikiruga.github.io/infer3d-site/</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>Keel: A Frontier Model Teaches a Vision-Language Model by Rewriting Its Weights</strong>
          <small>Jiajun Fan, Neil He, Bangji Yang, Qinglong Zheng, Ziwen Wang, Chaoran Cheng, Changyi Yang, Hanqi Mao, Ge Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Model Editing</span>
<span class="topic-tag">GUI Grounding</span>
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
          <span>Paper 4 / arXiv:2611.25257</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.25257">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 2: it is a method for repairing a vision-language model via weight editing, with direct results on image tasks and GUI grounding.</p>
        <p class="abstract">Can a frontier model repair a vision-language model (VLM) by rewriting its weights? Small reasoning VLMs such as Qwen3.5 need such a repair: in thinking mode they fall into loops on many image questions, repeating themselves until the token limit, spending the whole budget and losing the answer. The usual remedies act on the decoding, leaving the looping model as it was, or must be told what to change. Yet the cause is written in the weights. Keel, the first agentic weight-editing method for VLMs on image tasks, finds and removes it there. Told only the symptom, an editor, a frontier multimodal LLM acting as an agent, locates the cause, edits the weights and tests them, with a failure census and instruments showing it the failing images and where the VLM attends; among several editors, the harness keeps only edits that clearly reduce the failure without lowering accuracy on questions no editor saw. The repair needs no training, keeps the model&#x27;s size and per-token cost, and applies to already-edited weights. The editors expose where the loops live: from the original weights, independent editors on both models trace them to the attention outputs of the middle layers, and the smaller VLM stops consulting the image inside a loop. On Qwen3.5-0.8B and Qwen3.5-2B, across six image benchmarks from visual mathematics to GUI grounding, the edit removes most loops on every benchmark and shortens answers, and the edited models are significantly more accurate than the thinking models on average; the larger one gains most on GUI grounding, a task absent from the practice questions. Because the repair lives in the weights, it combines with budget forcing where held-out questions favor it: on the best available weights, Keel has the best average accuracy on both models, significantly above every training-free baseline we compare on the larger one.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-10-23.html">
          <span>October 23, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-22.html">
          <span>October 22, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-21.html">
          <span>October 21, 2026</span>
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
