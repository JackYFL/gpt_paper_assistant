

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
      <p class="eyebrow">Daily ArXiv / September 29, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>7</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>14</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>10.7</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.74rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="5 mentions">action</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">admission</span><span class="cloud-word" style="font-size:2.19rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 70%, var(--accent))" title="7 mentions">agent</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">bioeval</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">challenging</span><span class="cloud-word" style="font-size:2.19rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 70%, var(--accent))" title="7 mentions">claim</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">count</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">coverage</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">cryoem</span><span class="cloud-word" style="font-size:1.74rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="5 mentions">deeplink</span><span class="cloud-word" style="font-size:1.74rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="5 mentions">embodied</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="2 mentions">environment</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">executable</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">expert</span><span class="cloud-word" style="font-size:2.40rem;opacity:0.9;color:color-mix(in srgb, var(--accent-2) 81%, var(--accent))" title="8 mentions">explanation</span><span class="cloud-word" style="font-size:1.97rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="6 mentions">false</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">fixed</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">generate</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">ground</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">interpretation</span><span class="cloud-word" style="font-size:1.97rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="6 mentions">item</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">laboratory</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="2 mentions">lack</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">literature</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">memory</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">multimodal</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">paraphrase</span><span class="cloud-word" style="font-size:2.19rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 70%, var(--accent))" title="7 mentions">policy</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">protocol</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">question</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">reasoning</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">reliable</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">scaling</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">scientific</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">scihorizon-elab</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">shared</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="10 mentions">source</span><span class="cloud-word" style="font-size:2.19rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 70%, var(--accent))" title="7 mentions">spatial</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">spatially</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">subfield</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">subject</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="4 mentions">success</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">synthesis</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">synthetic</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="3 mentions">truth</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="124 mentions">action</span><span class="cloud-word" style="font-size:1.85rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 53%, var(--accent))" title="142 mentions">agent</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">alignment</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="61 mentions">annotation</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="55 mentions">architecture</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="63 mentions">attention</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">backbone</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="58 mentions">camera</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="55 mentions">challenging</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="61 mentions">consistency</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">control</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">dense</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="64 mentions">detection</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">driving</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="99 mentions">dynamic</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="65 mentions">environment</span><span class="cloud-word" style="font-size:1.84rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="141 mentions">evidence</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="70 mentions">foundation</span><span class="cloud-word" style="font-size:2.31rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="196 mentions">generation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">geometric</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="77 mentions">geometry</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="64 mentions">grounding</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="69 mentions">inference</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="95 mentions">interaction</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="92 mentions">language</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="77 mentions">memory</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="101 mentions">motion</span><span class="cloud-word" style="font-size:1.96rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="154 mentions">multimodal</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">multiple</span><span class="cloud-word" style="font-size:1.69rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="125 mentions">object</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="94 mentions">observation</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="58 mentions">optimization</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="60 mentions">perception</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="58 mentions">pipeline</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="76 mentions">point</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">policy</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">produce</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="61 mentions">query</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">question</span><span class="cloud-word" style="font-size:1.82rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="139 mentions">reasoning</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="55 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">region</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="132 mentions">scene</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="132 mentions">semantic</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">source</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">space</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="108 mentions">spatial</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">structured</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="65 mentions">supervision</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="80 mentions">support</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="68 mentions">target</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="87 mentions">temporal</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="85 mentions">token</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="100 mentions">trajectory</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="71 mentions">understanding</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="69 mentions">unified</span><span class="cloud-word" style="font-size:2.29rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 75%, var(--accent))" title="194 mentions">video</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="72 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="260 mentions">visual</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="109 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>7 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents</strong>
          <small>Maokai Qin, Chuan Qin, Qi Zhang, Dianyu Liu, Zirui Liu, Hongting Niu, Yuanchun Zhou, Hengshu Zhu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI Benchmark</span>
<span class="topic-tag">Simulation</span>
<span class="topic-tag">Scientific Robotics</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2609.30971</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.30971">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it proposes a simulator-based benchmark and protocol-to-task compiler for scientific embodied agents, a new embodied AI evaluation setup.</p>
        <p class="abstract">Embodied agents offer a promising route to automating scientific experimentation, yet their progress is constrained by the lack of reliable and systematic evaluation environments. Existing simulation-based laboratory benchmarks rely heavily on manual task engineering, making it challenging to systematically compile diverse scientific protocols into executable and verifiable embodied tasks at scale. To address this challenge, we introduce SciHorizon-eLab, an agentic protocol-to-task compiler that formulates scientific embodied task construction as a compilation problem. Given a natural-language protocol of scientific experiments, SciHorizon-eLab progressively compiles laboratory protocols into semantic-preserving embodied tasks through semantic grounding, executable task synthesis, and multi-stage simulation-based certification. The system generates semantically grounded environments, executable manipulation programs, and step-level success specifications, while enabling reproducible generation of expert demonstrations and execution traces. Using this pipeline, we further construct \BenchName, a ready-to-use benchmark comprising 300 certified tasks across diverse laboratory operations. It supports HIL task execution, reproducible expert-demonstration generation, and ordered step-level evaluation. Across representative tasks, the strongest policy attains an average success rate of only 49.7%, with further evaluations revealing pronounced weaknesses in human and embodied agent coordination. We publicly release the code, benchmark data, and evaluation toolkit at https://github.com/SciHorizon-elab/SciHorizon-elab.</p>
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
          <strong>From Tapping to Hopping: Augmenting Mobile GUI Agents with App-Native Deeplinks</strong>
          <small>Yuchen Sun, Chenglin Cai, Gongjie Zhang, Tianyu Xia, Quyu Kong, Panrong Tong, Zhengwen Zeng, Long Chen, Steven Hoi, Chongyang Zhang, Yue Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Mobile GUI Agents</span>
<span class="topic-tag">Tool Use</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2609.30887</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.30887">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied/mobile GUI-agent method that adds app-native deeplinks as a novel interaction modality for navigation.</p>
        <p class="abstract">Mobile GUI agents complete tasks using GUI actions like taps and swipes. These actions are broadly applicable across applications, but reaching a navigation interface. A single deeplink call can replace a sequence of screen-by-screen GUI actions. We therefore introduce hybrid interaction, using deeplinks for direct navigation and GUI actions for other on-screen operations and fallback. To enable this, we discover candidate deeplinks through static analysis, validate them on real devices, and describe their observed landing screens. This process creates a verified and grounded deeplink catalog that pairs each working deeplink with a description of its landing screen. Using this catalog, we introduce GUI-Hopper, a improves task success in commercial applications on real devices, further demonstrating the benefits of hybrid interaction.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multi-Agent Memory</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory</strong>
          <small>Xiaoyang Li, Yiqi Wang, Chencheng Zhu, KE XU, Wencheng Yang, Zequn Sun, Pingan Song, Yiqun Duan, Taotao Cai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multi-Agent Memory</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Information Sharing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2609.30813</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.30813">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 somewhat: it introduces a benchmark and diagnostic study for shared agent memory, which is a novel angle for multi-agent systems, though not embodied AI specifically.</p>
        <p class="abstract">Evaluating claim admission in shared agent memory is challenging because repeated claims may be mistaken for independent evidence. An agent may copy or paraphrase a retrieved belief, while admitting a false claim exposes subsequent agents to it. To study this problem, we introduce the Correlated Promotion Benchmark (CPB), which evaluates whether candidate claims should be admitted to shared memory.CPB-Static constructs a frozen test split from publicly annotated sources with fixed gold actions. CPB-Live runs multi-agent teams over a shared store, records all writes and retrievals, and tracks source lineage defined by each scenario. A separate consumer answers from the store alone. We evaluate eight admission policies across four agent families. Our results show that policies which deduplicate sources reject many true claims alongside false ones, whereas policies preserving answer coverage admit nearly as many false claims as unrestricted sharing. Gating on declared source type reduces false adoption to 0.06--0.09, compared with 0.22--0.47 for other answering policies. Once an uncontested false belief enters memory, the consumer asserts it in 0.97--0.99 of probes across all families. No non-oracle policy consistently rejects false claims across verbatim copies, paraphrases, and paraphrases declared authoritative. These findings reveal the limitations of admission policies without access to source lineage.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>Atelier: Learning Local Self-Supervised Features for CryoEM Volumes via Hypernetworks</strong>
          <small>Phillip Lo, Sudarshan Babu, Dari Kimanius, Aly A. Khan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">3D CryoEM</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">stat.ML</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2609.30569</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.30569">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately: it learns self-supervised local features for cryoEM volumes using hypernetworks, an application of foundation-style representation learning to 3D vision data.</p>
        <p class="abstract">CryoEM map interpretation requires features that are spatially localized, consistent across samples, and informative across spatial scales. Most deep learning methods for map annotation extract features from fixed voxel grids. However, implicit neural representations (INRs) are able to model volumetric data as scale-agnostic, coordinate-conditioned functions. INRs are therefore attractive for cryoEM, but fitting a separate INR for each map is too expensive for large-scale feature extraction and produces representations that are not aligned across samples. We introduce Atelier, a self-supervised framework that amortizes INR fitting for reconstructed cryoEM maps. Pretrained on 5,439 Electron Microscopy Data Bank maps, Atelier is a transformer-based hypernetwork that generates high-fidelity reconstructions across a wide range of protein structures, including large multi-subunit assemblies. Beyond reconstruction, the INR generated by the pretrained transformer exposes a continuous, local feature field through its intermediate activations at any spatial query point, a property that voxel grid and patch-tokenizer architectures do not naturally provide. Used as auxiliary channels to a 3D nested U-Net annotation head trained from scratch, these coordinate-conditioned features improve performance on eight voxel-level property prediction tasks over a volume-only baseline. Our results demonstrate that amortized implicit neural representations are an effective primitive for geometry-aware analysis of cryoEM data.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Explainable AI</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>A Synthetic Ground-Truth Framework for the Evaluation of Explainable AI Methods</strong>
          <small>Miquel Mir\&#x27;o-Nicolau, Francesco Spinnato, Riccardo Guidotti</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Explainable AI</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Synthetic Ground Truth</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2609.30397</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.30397">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only loosely: it proposes a synthetic intervention-based benchmark for evaluating XAI methods, but it is not embodied AI or vision foundation models.</p>
        <p class="abstract">Evaluating explainable Artificial Intelligence (XAI) methods is a challenging task due to the lack of reliable evaluation procedures and, in particular, the absence of ground truth explanations. In the literature, existing evaluation approaches typically assess explanations by measuring their fidelity with respect to the predictions of a black-box model. However, such evaluation strategies only quantify the degree to which an explanation reproduces the model&#x27;s output, without ensuring that the explanation correctly reflects the underlying decision process. As a consequence, different explanations may achieve similar fidelity scores while providing inconsistent or misleading interpretations of the model behavior. In this paper, we propose a framework for the evaluation of XAI methods based on synthetic ground truth. The proposed approach relies on controlled interventions to generate synthetic datasets in which the importance of input components can be determined by design. This enables the construction of ground truth explanations that are directly aligned with the behavior of the model under analysis. The framework is instantiated across three data domains, namely binary images, tabular data, and time series, allowing a comprehensive assessment of explanation methods in heterogeneous settings. Experimental results obtained by evaluating nine widely used XAI methods show significant limitations in current techniques and highlight the importance of synthetic, intervention-based benchmarks for a reliable assessment of explanation quality.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Representation Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Samples, Sources, Space: Decomposing Data Scale in Spatially Structured Representation Learning of Human Brain Microarchitecture</strong>
          <small>Christian Schiffer, Mathis Bode, Thomas Lippert, Katrin Amunts, Timo Dickscheid</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Representation Learning</span>
<span class="topic-tag">Medical Imaging</span>
<span class="topic-tag">Scaling Laws</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2609.31201</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.31201">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is spatially structured representation learning in brain histology, which is adjacent to spatial understanding but not embodied agents or vision foundation models.</p>
        <p class="abstract">Scaling studies typically represent training data by a single count of samples. For hierarchically and spatially structured data, however, the same number of samples can be drawn from few or many sources and distributed differently across the underlying domain. We therefore study data scaling as an allocation problem, separating unique sample count, source diversity, and spatial coverage. We study this decomposition in microscopic whole-brain histology, where a source is an individual brain, and a sample is an image patch at a specific spatial location. Across 93 controlled pretraining runs of a contrastive model that uses spatial proximity for supervision, we vary data allocation, compute, and model capacity over 11.6 million spatially anchored image patches from 21 human brains. Performance improves with more unique samples, broader spatial coverage, additional compute, and larger model capacity. At fixed sample count, distributing samples across one to 18 subjects produces no detectable improvement, even though representations generalize substantially better to subjects encountered during pretraining. Inter-subject variation therefore strongly affects generalization, but additional subjects provide no benefit when a fixed sample budget is distributed across more sources. These results establish sample count, source diversity, and spatial coverage as distinct axes of data scaling in spatially structured representation learning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>BioEVAL: A global, multi-institutional benchmark of large language and multimodal models for bioengineering</strong>
          <small>Shun Ye, Vinny Chandran Suja, Chenlong Li, Chongming Jiang, Reza Zamani, Xiang Li, Christopher Bain, Yuqi Zhou, Walker Peterson, Huidong Wang, Chenglang Hu, Jongchan Park, Xiao Cheng, Benjamin Swedlund, Sandra Murillo, Anjali Sivanandan, Shiyu Sun, Liang Lanfeng, Mohammad Tariqul Islam, Baju C. Joy, Ishaq N. Khan, Sreedhar S. Kumar, Gabriel Mercado-V\&#x27;asquez, James V. Vizzard, Jonathan M. Matthews, Helen Huang, Xiaolu Guo, Ethan Nicklow, Guorui Chen, Ryan A. Neff, Surjendu Maity, Hyeonjin Park, Han-ho Joo, Katherine Dong, Yuyan Cai, Weihang Huang, Yichen Zou, Rui Yan, Raphael Figueroa, Artem Goncharov, Bella Rose Schremmer, Lian Elsa Linton, Keisuke Goda, Liang Gao, Ke Cheng, Leonardo Morsut, Jennifer L. Wilson, Jianping Fu, Lim Chwee Teck, Deblina Sarkar, Andreas Hierlemann, Sava\c{s} Tay, Alexander Hoffmann, Donald Richieri Griffin, Jun Chen, Shana O. Kelley, Shyni Varghese, Jinwoo Cheon, Wilbur A. Lam, James J. Moon, Wilson W. Wong, Samir Mitragotri, Dino Di Carlo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Benchmark</span>
<span class="topic-tag">Bioengineering</span>
<span class="topic-tag">Evaluation Protocols</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2609.30489</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.30489">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 only loosely: it benchmarks large language and multimodal models, but the domain is bioengineering rather than a new VLLM/MLLM method.</p>
        <p class="abstract">Large Language Models (LLMs) have demonstrated historic breakthroughs in general reasoning with early successes in biomedical science. However, existing LLM benchmarking emphasizes factual recall, offering limited insight into model performance on frontier and multimodal tasks. We assembled BioEVAL (BioEngineering Validation of AI and LLMs), a global, multi-institutional initiative designed to assess experimental reasoning capability across bioengineering (BE) subfields. BioEVAL spans 11 major BE subfields plus a set of uncategorized items, bringing together 22 research groups to create a PhD-level benchmark comprising 608 evaluation items: 1) 380 multiple-choice questions (MCQs, 359 retained after audit), 2) 218 literature synthesis tasks, and 3) 10 multimodal problems with experimental image interpretation. Benchmark items underwent authoring-group expert review and centralized quality control before evaluation. Following evaluation, a blinded cross-group consensus audit of the highest- and lowest-accuracy MCQ items flagged 21 questions for revision or removal; these were withheld, and all reported MCQ results are computed on the 359 retained items. We evaluated diverse cloud-scale foundation/multimodal models (e.g., ChatGPT, Gemini, and Grok) and locally deployable models suitable for inference on consumer-grade GPUs. Models achieved the highest accuracy of up to 90% on MCQs, similarity score of 0.72 on literature synthesis, and accuracy of 80% on a small sample of multimodal reasoning questions, with substantial performance variation across subfields. Leaderboard rankings characterize current capabilities, limitations, and development priorities across the evaluated BE task categories. BioEVAL is maintained as an extensible benchmark with standardized protocols for continuing expert item contribution and model evaluation.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-08-29.html">
          <span>August 29, 2026</span>
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
