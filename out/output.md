

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
      <p class="eyebrow">Daily ArXiv / November 19, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>21</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>16</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.23rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="9 mentions">action</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">affordance</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">against</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">agent</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">attention</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">camera</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">causal</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">change</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">complementary</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">consistency</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">content</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">depth</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="11 mentions">dimension</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">effect</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="11 mentions">environment</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="10 mentions">evidence</span><span class="cloud-word" style="font-size:1.67rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="13 mentions">execution</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">expert</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">gaussian</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">hand</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">interaction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">limit</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">nominal</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">object</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="12 mentions">observation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">paired</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">point</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="11 mentions">policy</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">question</span><span class="cloud-word" style="font-size:2.14rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 68%, var(--accent))" title="18 mentions">reasoning</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">reference</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">reliability</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">response</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">restoration</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="10 mentions">scene</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">selection</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">semantic</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">skill</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="9 mentions">success</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">textual</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">thermal</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="11 mentions">trajectory</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="8 mentions">video</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="9 mentions">view</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="26 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="86 mentions">action</span><span class="cloud-word" style="font-size:2.30rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="153 mentions">agent</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="50 mentions">alignment</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="46 mentions">answer</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="46 mentions">attention</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="55 mentions">camera</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="48 mentions">change</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="48 mentions">control</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="37 mentions">depth</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="51 mentions">detection</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="44 mentions">diffusion</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="51 mentions">environment</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="50 mentions">error</span><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="85 mentions">evidence</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="47 mentions">execution</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="39 mentions">fixed</span><span class="cloud-word" style="font-size:1.88rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="112 mentions">generation</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="43 mentions">generative</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="38 mentions">geometric</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="41 mentions">geometry</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="52 mentions">inference</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="52 mentions">interaction</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="49 mentions">language</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="58 mentions">latent</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="73 mentions">memory</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="48 mentions">motion</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="59 mentions">multimodal</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="42 mentions">multiple</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="82 mentions">object</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="50 mentions">observation</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="40 mentions">pair</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="49 mentions">physical</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="73 mentions">point</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="65 mentions">policy</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="50 mentions">prompt</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="53 mentions">question</span><span class="cloud-word" style="font-size:1.66rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="93 mentions">reasoning</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="47 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="37 mentions">reference</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="41 mentions">region</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="40 mentions">reward</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="63 mentions">same</span><span class="cloud-word" style="font-size:1.48rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="79 mentions">scene</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="37 mentions">segmentation</span><span class="cloud-word" style="font-size:1.79rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="104 mentions">semantic</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="38 mentions">space</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="64 mentions">spatial</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="44 mentions">step</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="55 mentions">structure</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="45 mentions">supervision</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="57 mentions">support</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="43 mentions">target</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="52 mentions">token</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="50 mentions">trajectory</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="38 mentions">user</span><span class="cloud-word" style="font-size:2.07rem;opacity:0.82;color:color-mix(in srgb, var(--accent-2) 64%, var(--accent))" title="130 mentions">video</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="53 mentions">view</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="48 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="206 mentions">visual</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="63 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>19 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>GRID-UAV: Geometry and Ray-depth Integrated Decision-making for Unmanned Aerial Vehicles</strong>
          <small>Anas Anwarul Haq Khan, Amrin Kareem, Muhammad Umer Sheikh, Biplab Banerjee, Muhammad Haris Khan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">UAV Navigation</span>
<span class="topic-tag">3D Spatial Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2611.23491</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23491">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criteria 1 and 3 very closely: an embodied AI method for UAV spatial understanding that explicitly improves 3D grounding and navigation.</p>
        <p class="abstract">Vision-language-action models (VLAs) encode images with 2D encoders that capture little 3D structure. A common approach is to feed the policy estimated depth, but a UAV chooses its own altitude, must judge distances tens of meters away, where monocular depth is less reliable, and must relate its forward and downward views. On long aerial routes, adding depth features directly brings no significant gain (42.5% vs. 42.6% success), so we study how 3D information should be given to the policy. Analyzing flight failures, we find that two forms of 3D grounding fail in opposite ways: explicit 3D lifting of depth collides less on the way but more often fails to finish at the target, while implicit alignment with a 3D geometry model finishes more often but collides more. We propose GRID, which combines both: (1) it lifts monocular depth into ray-corrected 3D positions in the UAV&#x27;s frame for both cameras, and (2) during training only, it aligns its visual features with a frozen multi-view geometry model, at no inference cost. GRID adding explicit lifting to implicit alignment significantly increases how often the policy reaches the target ($61.5\% \rightarrow 69.5\%$, $p&lt;0.001$), and adding implicit alignment to explicit lifting significantly increases how often it completes the task once there ($57.7\% \rightarrow 61.4\%$, $p&lt;0.05$). On TravelUAV (3,005 test episodes), GRID achieves the best success rate on every split, with relative gains over the state of the art of 9.5% (seen), 17.1% (unseen objects) and 25.4% (unseen map).</p>
      </div>
    </details>


    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>ART: Bridging the Embodiment Gap in 3D Human-to-Robot Affordance Transfer</strong>
          <small>Zichen Zhang, Wei Zhai, Xuji Zhang, Yang Cao, Yu Kang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Affordance Learning</span>
<span class="topic-tag">Robotics Benchmark</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2611.24182</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24182">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 3: it proposes a new embodied/robotic benchmark for human-to-robot affordance transfer and a new method for bridging embodiment mismatch.</p>
        <p class="abstract">3D affordance acts as a critical link between perception and action, providing priors for robotic manipulation. While existing approaches predominantly leverage human priors as direct references, they often overlook that affordance is not an object-intrinsic property but is inherently coupled with the agent&#x27;s embodiment. Due to the structural and morphological disparities between human hands and robot end-effectors, directly applying human priors causes severe incompatibility for robotic execution. Motivated by this, we introduce a novel task setting, 3D Human-to-Robot Affordance Transfer, which addresses the affordance misalignment arising from distinct embodiment structures. To support this task, we construct the Human-Robot Paired Affordance Dataset (HPAD), the first large-scale 3D affordance benchmark in which every object is annotated with both human-prior and simulation-validated robot labels. HPAD covers 2,137 objects across 80 categories and 13 atomic action primitives, yielding over 27,000 object-action pairs. On top of HPAD, we propose the 3D Affordance tRansfer neTwork (ART). ART first filters geometric false positives in the human prior via a reliability gating stream, then reconstructs the prior into a robot-actionable distribution through hierarchical reconstruction and a graph-diffusion refinement that resolves the topological mismatch between human and robot affordances. Experiments on HPAD demonstrate the reliability of the proposed task and the superiority of ART. We further validate ART on a 6-DoF arm with a parallel-jaw gripper in a 2,400-execution benchmark across 12 objects and 4 action categories; ART attains the best success rate (86.5% over its 480 trials), confirming the practicality of the transfer paradigm. Project page: https://derek0907.github.io/ART/</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>HandWorldBench: A Unified Benchmark for Hand-Centric World Models</strong>
          <small>Zhaolu Wang, Jiacheng Xu, Lihong Wang, Shuqing Wang, Jianjie Fang, Ziyou Wang, Xvyuan Liu, Rongze Tang, Yiding Ma, Xin Zhang, Jiawei Chen, Wei Wu, Chen Gao, Yong Li, Zhibo Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied World Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Dexterous Manipulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2611.24731</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24731">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: a new benchmark for embodied/world-model evaluation focused on hand-centric interactions and simulator/real dexterous settings.</p>
        <p class="abstract">Recent advances in world models are opening new possibilities for fine-grained embodied tasks, with hand-object interaction offering a particularly demanding setting. Modeling these interactions involves capturing how hand actions change objects and how the resulting states persist over time. Yet systematic evaluation tailored to these hand-centric capabilities remains underdeveloped. To address this gap, we introduce HandWorldBench, a unified benchmark that systematically evaluates hand-centric world models across human hands, simulated dexterous hands, and real dexterous hands along six dimensions: visual quality, hand fidelity, appearance consistency, instruction following, physical consistency, and temporal coherence. To construct the benchmark, we develop a data curation pipeline that extracts hand-object interaction clips and screens them for quality, yielding 20,500 high-quality egocentric clips from over 600 hours of footage. We then manually select 500 clips covering seven task families for evaluation. Benchmarking eleven models under a unified protocol reveals that stronger hand-pose control does not consistently translate into coherent object-state evolution and persistence or robust cross-embodiment performance, with several specialized hand-control models underperforming general-purpose text/image-to-video generators on dexterous-hand tasks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>AVTR: Adaptive Multimodal Reasoning with Visual Imagination</strong>
          <small>Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao, Saksham Suri, Chong Zhou, Zechun Liu, Zhipeng Cai, Zhuang Liu, Qi Qian, Wei Wen, Hongyu Xu, Hanxian Huang, Ernie Chang, Yanbei Chen, Vikas Chandra, Raghuraman Krishnamoorthi, Mohamed Elhoseiny, Lemeng Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Multimodal Routing</span>
<span class="topic-tag">Visual Imagination</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2611.24161</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24161">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: a new VLM/MLLM reasoning method with adaptive visual-textual reasoning and visual imagination.</p>
        <p class="abstract">Vision-Language Models increasingly rely on textual reasoning to solve advanced multimodal tasks. Despite its effectiveness, this paradigm faces two fundamental limitations. First, relying on textual reasoning alone can limit perceptual ability in vision-centric questions, where accurate answers depend on interpreting task-relevant visual evidence. Second, applying textual reasoning uniformly across inputs overlooks question-dependent variation in both reasoning modality and depth, often producing verbose and unnecessary traces when little logical inference is required. To this end, we propose Adaptive Visual-Textual Reasoning (AVTR), which introduces visual imagination as a complementary reasoning modality to textual thinking, enabling the model to revisit its visual observations and distill the salient evidence through generative visual reflection. Furthermore, we formulate reasoning-modality selection as a learned routing problem, allowing a single policy to adaptively harness the complementary strengths of visual reflection and textual reasoning in response to the perceptual and inferential demands of the input. Across 16 benchmarks, AVTR improves the average score by 4.5 points over Qwen3.5 baseline, while reducing inference latency by 33\%. It also scales effectively into a smaller size backbone, outperforming the evaluated 2B-scale baselines.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model</strong>
          <small>Chuang Wang, Rui Nie, Jie Song, Junyuan Gao, Jiahe Song, Haitao Zhou, Boyu Zhu, Xing Li, Jiang Wu, Conghui He, Qian Yu, Weijia Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Interactive Video</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2611.24408</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24408">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 3: it introduces a new benchmark for interactive video world models focused on scene rigidity and action consistency, a novel evaluation angle that prior benchmarks miss.</p>
        <p class="abstract">Interactive video world models turn user commands into the exploration of a generated scene, which requires the scene to keep its 3D structure as the camera moves and each action to keep a stable effect. Existing benchmarks mostly evaluate these properties against references fitted to the video under test, either a scene reconstructed from its own frames or a camera trajectory aligned to the command path with a free scale. Such references can absorb gradual scene deformation and changes in pace and route length, so these errors can pass undetected. We therefore introduce StrideWorld, a benchmark whose references are fixed before the motion they judge. It evaluates scene rigidity against the ground-truth geometry of the start view, and action consistency against the stride of each action, the camera motion of one command. The stride is measured on the model&#x27;s first steps and then used to test the steps that follow, so each model is judged only against its own steps. Its measurements are validated on rendered videos with known camera motion, and its scores agree with human judgments. Across \nvideos{} videos generated by \nmodels{} open models from $140$ start views, all models but one deform their scenes as the camera moves, with offsets up to $7.3$ times those of a rigid rendering along the same camera path. Most models keep a steady pace when a single action is held. Along composed routes, several models often stall, and most completed routes end away from the positions predicted by each model&#x27;s own strides. Only the two models that scale commands by the estimated scene depth bring most routes close to these positions. Fine-tuning two models on a few rendered clips removes most of their mid-route stalls. Code, data, and a leaderboard are publicly available at https://github.com/chuangwang123/strideworld.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>EyeDiT: Anatomy-Grounded Multi-Modal Eye Generation and Simulation</strong>
          <small>Yonghan Lee, Zachary Willms, Kun Liu, Pushkar Anand, Ali Behrooz, Dmitri Model, Dinesh Manocha, Yatong An</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Generation</span>
<span class="topic-tag">3D Simulation</span>
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
          <span>Paper 6 / arXiv:2611.23670</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23670">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 strongly: it is a multimodal generative model for anatomy-grounded 3D eye synthesis and simulation, with a clear vision foundation / generative modeling flavor.</p>
        <p class="abstract">Synthetic eye data are critical for rapid development of eye tracking (ET) in AR/VR applications. However, existing synthetic eye generators are largely image-centric and lack a high-quality underlying 3D anatomy of the eye, which limits their control mainly to the gaze and provides no anatomical labels. To address this problem, we propose EyeDiT, an anatomy-grounded, multi-modal 3D eye generation and simulation model trained with optical coherence tomography (OCT), labeled anatomy point clouds and near-eye images. Our pipeline first trains a Multi-Modal Anatomy Variational Autoencoder (VAE), which encodes an anatomy-aware latent representation from all input modalities. Then, our Eye Latent DiT is trained to generate latent samples conditioned on the optical axis, the pupil position and radius, and the subject identity. Together with Gaussian decoders for novel-view simulation, our model enables control over the pupil, subject identity and viewpoint for data synthesis. We show that our model outperforms previous eye image synthesis models in novel-view synthesis (24.9 against 21.8 dB PSNR from a single view), and that a public ET neural network trained on our synthetic data shows a smaller sim-to-real gap than when trained on data from other generators (3.5$^\circ$ vs. 8.4$^\circ$ gaze error), approaches a network trained on real data, and further improves ET performance when combined with real data (2.3$^\circ$ vs. 2.6$^\circ$). More information is available on the project page: https://lyhan12.github.io/eyedit</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Keep the Image in Mind: A Visual Board for Multimodal Agents</strong>
          <small>Haiming Zhu, Zhiwei Chen, Ding Cao, Tianxiang Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Agents</span>
<span class="topic-tag">Visual Reasoning</span>
<span class="topic-tag">Tool-Using VLMs</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2611.23872</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23872">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: a multimodal agent framework that structures visual evidence for better multi-step reasoning.</p>
        <p class="abstract">Multi-step visual reasoning suffers when early visual misinterpretations persist as incorrect premises in subsequent reasoning. We argue that how visual evidence is represented during reasoning matters as much as how much of it is gathered. Rather than appending observations and inferences to an ever-growing dialogue, we introduce a Visual Board-centered harness that separates visual observations, uncertain interpretations, and derived reasoning within a structured, capacity-bounded, and revisable workspace. This separation makes each premise explicit and auditable, so that conflicts between what is seen and what is derived become detectable even by a text-only critic and can trigger targeted reinspection of the original image. Without task-specific training, our harness consistently outperforms standalone models across 4B, 8B, Qwen3-VL-Flash, and 32B configurations on Euclid30K, SolidGeo, and ChartQA bar charts, with gains of up to 11.68, 18.42, and 24.82 percentage points, respectively. Under identical tools, critic, and interaction limits, the structured Board outperforms shared free-form notes by 6.67 to 13.00 points and no-Board retries by 7.35 to 18.80 points while using 7.9\% to 38.2\% fewer tokens. Supervised fine-tuning on harness trajectories further improves direct answering and critic-free tool use, with positive transfer to chart reasoning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Bits, Not Boxes: Label-Free Layer Selection for Visual Localization in VLMs</strong>
          <small>Haisheng Fu, Gexin Huang, Haikai Zhao, Jie Liang, Zhenman Fang, Jingning Han, Xiaoxiao Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Visual Localization</span>
<span class="topic-tag">Attention Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">stat.ME</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2611.23432</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23432">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a vision foundation model/VLM application for label-free visual localization using attention-based layer selection.</p>
        <p class="abstract">Attention maps cheaply show where a vision-language model (VLM) looks, but attention sinks make them unreliable for localization. Contrasting the question with a generic prompt suppresses sinks, yet only some layers localize the queried object. Existing methods find these layers with box annotations or fixed rules. We show that attention itself can identify them. A question changes how much a head attends to the image and where this attention goes. The two effects separate exactly, and the second, measured in bits on unlabeled questions, indicates which layers localize. WhereBits turns these where-to-look bits into a layer prior and combines it with per-head contrastive scores. Its three design constants were fixed once on labeled COCO data, and a new model or resolution needs only unlabeled questions. Across eight VLMs, WhereBits matches the pointing accuracy of box-tuned layers on COCO and RefCOCO and ranks target tokens better. This advantage holds on a held-out model family and at higher resolutions. Its COCO pointing accuracy is 0.72, against 0.22 for mean attention. In training-free zoom-in, its crops raise V* accuracy by 6.0 points under forced-choice evaluation.</p>
      </div>
    </details>


    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>CoScan: Multi-Scale Content-Adaptive Space-Filling Scans for Causal State-Space Image Restoration</strong>
          <small>Wei Dong, Terry Ji, Yan Min, Shahram Shirani, Jun Chen, Han Zhou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Image Restoration</span>
<span class="topic-tag">State-Space Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2611.23717</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23717">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 in a methods sense: it improves a vision backbone for image restoration via a new content-adaptive scan strategy for state-space models.</p>
        <p class="abstract">Selective state-space models (SSMs) have recently shown strong potential for efficient image restoration. A central difficulty, however, is that a 2D feature map typically needs to be linearized into a 1D token sequence for causal state-space updates, making restoration performance highly sensitive to the imposed scan order. Existing deterministic scans follow space-filling principles but remain fixed and content-agnostic, and can yield fragmented or semantically inconsistent contexts under degradations. We propose \textbf{CoScan}, a \textbf{co}ntent-adaptive \textbf{scan}-order design for causal vision SSMs. CoScan learns image-dependent space-filling traversals via differentiable proxy supervision driven by \textbf{scan-quality objectives} that \textit{encourage short-range coherence and causal predictability, while preserving spatial adjacency}. To support hierarchical restoration backbones, we introduce an \textbf{efficient multi-scale scan construction by coarsening a fine-level minimum spanning tree}, producing coherent scans across feature resolutions. In addition, a \textbf{frequency-guided start selection strategy} is designed to \textit{place informative structures early in the sequence prefix to strengthen causal context formation}. Plugged into existing Mamba-based backbones, CoScan yields consistent improvements across several restoration benchmarks with minimal overhead and shows promising results on high-level vision tasks. Code will be released at https://github.com/dongw22/CoScan</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Vision</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>GaussLearner: 3D Gaussian Primitives as Self-Regulating Continual Learners</strong>
          <small>Gaoxiang Linghu, Haonan Zhou, Xuanhe Liu, Weili Xu, Kaiyue Zhou, Jun Xiao, Gaoang Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Vision</span>
<span class="topic-tag">Continual Learning</span>
<span class="topic-tag">3D Gaussian Splatting</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2611.23736</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23736">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 and is also relevant to spatial understanding: it introduces a new continual-learning method for 3D Gaussian scene representations in evolving environments.</p>
        <p class="abstract">Continual learning of 3D Gaussian fields aims to maintain faithful reconstructions of the evolving world. However, directly fine-tuning an existing Gaussian field on new observations can cause catastrophic forgetting of previously reconstructed content. To address this challenge, existing methods employ selective local optimization, replay, or parameter regularization, yet still struggle to balance adaptation to scene changes with preservation of still-valid content. Our key insight is to view 3D Gaussian primitives themselves as self-regulating continual learners. Based on this insight, we introduce GaussLearner, which equips each Gaussian with a closed continual-learning loop connecting observation, self-regulation, and adaptation at the primitive level. At each novel state, GaussLearner first attributes pixel-wise inconsistencies in current observations to their contributing Gaussians. Each Gaussian then self-regulates through a learning weight that balances current observations against cross-state reliability. This weight governs both Gaussian parameter adaptation and optimizer memory refresh. As current inconsistencies are resolved, the adaptation outcome renews each Gaussian&#x27;s reliability for future states. The resulting field is a globally coupled population of locally self-regulating learners. Across scenes from CL-Splats, WAT, and our CL-3D dataset, GaussLearner improves average PSNR by 3.41 dB over the strongest baseline. On CL-3D, it achieves the best reconstruction quality on both changed and unchanged views.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Self-Supervised Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>ReCoCo: From Patches to Compositions for Visual Representation Learning</strong>
          <small>Juan Guti\&#x27;errez, Saman Zadtootaghaj, Jos\&#x27;e Luis Blanco-Murillo, Sara Atito</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Visual Foundation Models</span>
<span class="topic-tag">Dense Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2611.24806</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24806">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it advances visual foundation models via a new self-supervised representation learning method that improves dense features without explicit patch correspondences.</p>
        <p class="abstract">Self-supervised learning has produced powerful visual representations, yet learning strong dense features remains challenging. While consistency between augmented views provides strong image-level supervision, extending this principle to local visual content is less straightforward. Existing approaches often match individual patches across views or identify coherent regions, introducing uncertainties in correspondence estimation and assumptions about how visual content should be grouped. We introduce ReCoCo (Regional Composition Consistency), a principled approach that extends cross-view consistency to the regional level without requiring such correspondences or semantic grouping. ReCoCo represents the content shared between augmented views through compositions of their patch-level predictions over learned visual prototypes. By aligning these compositions, the model learns from regions containing multiple visual concepts without requiring them to be separated beforehand. ReCoCo integrates naturally with teacher-student self-distillation and introduces no additional learned parameters. Extensive experiments demonstrate substantial improvements in frozen-feature segmentation, clustering, and regional retrieval while maintaining competitive image-level recognition, alleviating the trade-off between dense and global representation quality.</p>
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
          <strong>CausalDrive: Causal Decomposition for Data-Efficient End-to-End Autonomous Driving</strong>
          <small>Xiaobao Wei, Jingxian Wu, Lirong Yang, Qing Han, Yuan Gao, Ziwei Yang, Shuai Yang, Weiwei Liu, Chang Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Causal Learning</span>
<span class="topic-tag">Behavior Cloning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2611.24080</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24080">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 in the embodied-control sense: it proposes a new data-efficient autonomous driving method with causal decomposition and counterfactual supervision.</p>
        <p class="abstract">Efficient use of expert demonstrations is essential for end-to-end autonomous driving. However, directly imitating expert trajectories couples nominal intention, which specifies where the vehicle should go, with multimodal driving styles, which determine how that intention is executed. Different combinations of these factors can yield similar expert trajectories, obscuring their respective causal contributions and forcing the policy to learn both from a single entangled target. This ambiguity limits how effectively the policy can exploit expert demonstrations. We propose CausalDrive, a causal decomposition framework for data-efficient driving policy learning that separates deterministic nominal intention prediction from probabilistic driving style modeling. Specifically, we construct counterfactual nominal trajectories from navigation command, map topology, and ego state by removing style dependent effects, providing a Nominal Intention Planner with supervision independent of expert trajectories. Conditioned on the predicted nominal intention and surrounding agents, a diffusion-based Style Execution Policy models diverse driving styles as a multimodal distribution over residuals between nominal and expert trajectories. This causally structured supervision reduces redundant learning of shared nominal behavior in routine scenarios, directing expert supervision toward informative execution variations and improving data utilization. CausalDrive achieves 91.2 PDMS on NAVSIM v1 and 89.5 EPDMS on NAVSIM v2, matching or surpassing state-of-the-art performance. Further experiments demonstrate strong performance with limited expert data and clear advantages in challenging interactive scenarios.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal LLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Benchmarking Reasoning Reliability,Prior_Evidence Contrast,and Spectral Discrimination in Remote-Sensing Geological Image Interpretation</strong>
          <small>Jun Wang, Fengpeng Li, Wei Han, Yuxuan Li, Tianjin Huang, Jining Yan, Sheng Wang, Kan Sun, Lizhe Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Remote Sensing</span>
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
          <span>Paper 12 / arXiv:2611.24068</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24068">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: it benchmarks multimodal large language models on remote-sensing geological interpretation and adds a tool-augmented MLLM method.</p>
        <p class="abstract">Reliable lithology interpretation requires accurate geological recognition and reasoning grounded in visual evidence. Although Multimodal Large Language Models show promise in remote sensing, their reliability in geological interpretation remains unclear. We introduce HyGeoBench, a diagnostic benchmark of 10,000 questions based on hyperspectral imagery across three dimensions: reasoning reliability, prior_evidence contrast, and spectral discrimination. It covers ten task types, with both multiple-choice and open-ended response formats. Integrating hyperspectral satellite imagery with geological annotations and verified evidence, HyGeoBench examines reasoning errors, conflicts between geological priors and visual evidence, and cross-band inconsistencies. Evaluations reveal limitations in fine-grained recognition and evidence-grounded interpretation. To address these challenges, we propose HyGeoAgent, a tool-augmented framework integrating region observation, text knowledge retrieval, same-band image retrieval, and native PCA analysis through adaptive tool use. Experiments demonstrate consistent improvements over the corresponding base models, improving geological image interpretation across diagnostic dimensions.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">GUI Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>How Complete Must an Environment Be to Train a Capable GUI Agent?</strong>
          <small>Jingxing Wang, Teng Wang, Xingyu Lou, Zihan Guo, Jun Wang, Weiwen Liu, Weinan Zhang, Jianghao Lin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">GUI Agents</span>
<span class="topic-tag">Benchmark Design</span>
<span class="topic-tag">Embodied AI</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2611.23946</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23946">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it studies how to build a capable GUI-agent environment and derives a new benchmark environment design with empirical findings on environment completeness.</p>
        <p class="abstract">Graphical user interface (GUI) agents are widely trained in executable GUI environments. To lower cost, build environments in batches, and reduce manual effort, each work trades away part of the environment through its construction choices. We describe these choices along three dimensions: reward coverage, the goal-reaching trajectories the verifier rewards; data coverage, the application data the agent is exposed to beyond what the task reads or writes; and feature coverage, the application features beyond what the task uses. Existing works set each dimension on engineering grounds, but they do not measure its effect on training. How complete must an environment be to train a capable agent, and along which dimensions? In MobileGym, we adjust each dimension separately, train Qwen3-VL-4B-Instruct, and evaluate every policy in the original full environment. A verifier that rewards only one reference path lowers success by 10.53 points, and removing unneeded records also lowers success. Pruning unneeded features instead raises success from 51.61% to 56.13%, entirely on tasks whose environments it left unchanged. The gain reverses when each episode is weighted equally and vanishes when only episodes on the pruned tasks are balanced. Without pruning, length weighting there reinforces long detour successes that erode skills on other tasks. Following these findings, we build MobileGym-Lite, which keeps reward and data coverage complete and prunes unneeded features. It outperforms Full in the full environment (55.48% versus 51.61% success) with lower construction cost.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Open-Vocabulary Segmentation</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Fuse to Recognize the Unseen: Class-Relative Infrared-Visible Fusion for Open-Vocabulary Semantic Segmentation</strong>
          <small>Zehao Gao, Jie Feng, Wenda Zhao, Junpeng Zhang, Ronghua Shang, Weisheng Dong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Open-Vocabulary Segmentation</span>
<span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Multimodal Fusion</span>
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
          <span>Paper 14 / arXiv:2611.24316</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24316">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it is a vision-language application built on CLIP-style open-vocabulary segmentation, with a new infrared-visible fusion method.</p>
        <p class="abstract">Visible-infrared image fusion leverages complementary thermal cues to enhance visual perception, particularly under challenging illumination. However, such perceptual complementarity does not readily translate into semantic gains in open-vocabulary semantic segmentation (OVSS), where CLIP-based models are predominantly pretrained on RGB imagery. Directly introducing IR information may instead disrupt RGB-language alignment, turning promising thermal cues into semantic interference that undermines unseen-class recognition. Our pixel-level RGB-IR semantic analysis reveals that class-relevant thermal cues can correct certain RGB misclassifications while preserving reliable RGB predictions, motivating RGB-anchored, class-relative thermal cue selection. Based on this insight, we propose EmergeFuse, an infrared-visible fusion framework for OVSS that selectively converts complementary thermal evidence into unseen-class semantic corrections. Specifically, class-relative cue selection evaluates RGB-IR semantic responses and calibrated thermal evidence relative to RGB predictions, generating class-relative correction requests through competitive selection. Text-contrast image rectification then translates these selected requests into semantic rectification directions through text contrasts, guiding evidence-gated feature updates to realize complementary thermal evidence for unseen-class recognition. Experiments on three benchmarks demonstrate gains of up to 4.755% in unseen-class mIoU and 15.730% in strict complementary conversion rate over existing fusion methods, while maintaining competitive fusion quality.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>EVF-Bench: A Comprehensive Benchmark for E-commerce Visual Effects in Video Generation</strong>
          <small>Run Ling, Ke Cao, Runze He, Jie Gao, Ao Ma, Wei Feng, Zhanjie Zhang, Hao Wang, Jinghe Hu, Guibing Guo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Video Generation</span>
<span class="topic-tag">Multimodal Datasets</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2611.24116</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24116">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Closely matches criterion 3: it proposes a new benchmark plus dataset for a task-specific generative setting, here evaluation of e-commerce visual effects in video generation.</p>
        <p class="abstract">E-commerce visual effects (EVF) are dynamic, product-centered visual presentations in e-commerce videos, often accompanied by promotional text. They play an important role in attracting viewer attention and conveying product information. However, general measures of visual quality and text relevance alone do not establish whether generated videos preserve product appearance, maintain readable text, and produce coherent, contextually appropriate effects. To address this issue, we introduce EVF-Bench, a dedicated benchmark spanning six evaluation dimensions: visual quality and text relevance as general dimensions, and motion, product consistency, text stability, and creative rationality as EVF-specific dimensions. To complement the benchmark and support task-aligned research and model adaptation, we further construct EVF-32K, a dataset of over 32000 curated image-text-video triples tailored to e-commerce scenarios. Using this suite, we systematically evaluate representative video generation models and their domain-adapted variants. The results reveal complementary strengths, with no evaluated configuration leading all six dimensions. Together, EVF-Bench and EVF-32K provide a task-oriented evaluation framework and a supporting data resource for e-commerce video generation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Ego-Vision</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>HHW-Ego: DSLR-Quality Enhancement for Multi-Source Wearable Ego Imaging</strong>
          <small>Yunfei Tong, Qianqian Sun, Jixiang Luo, Dell Zhang, Hao Sun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Ego-Vision</span>
<span class="topic-tag">Low-Light Enhancement</span>
<span class="topic-tag">Dataset Construction</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2611.24010</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.24010">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it introduces a dataset and enhancement pipeline for wearable ego-centric imaging, which is relevant to vision foundation model applications in embodied settings.</p>
        <p class="abstract">Wearable ego-centric images are now in high demand for scenarios ranging from daily smart glass usage to embodied intelligence. But the image quality is far behind smart phone due to the lacking paired high-quality reference images and the dedicated enhancement systems. To solve this, a customized degradation pipeline is designed to generate paired samples matching wearable camera images, boosting the upper limit of enhancement performance. Besides a two-stage enhancement framework is further built: first, tuning an efficient model on the paired dataset to enhance real wearable images; second, using hyperspectral data to refine color temperature for better quality. Moreover we present HHW-Ego, a multi-source paired dataset integrating with Hyperspectral, High-dynamic range and Wearable Ego-centric data, which includes 5,000 image groups spanning indoor/outdoor and day/night scenes. On held-out paired data, Stage-1 fine-tuning improves PSNR, SSIM, Lab distance, and LPIPS for Real-ESRGAN and PFT-SR. On real wearable images, no-reference metrics, human preference, gamut analysis, and visual comparisons characterize the effects of Stage 2.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Restoration</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>Beyond Additive Composition: Interventional Modeling of State-Dependent Cross-Degradation Responses for Composite Image Restoration</strong>
          <small>Zongda Tang, Jie Feng, Wenda Zhao, Mingtao Feng, Yuping Liang, Ronghua Shang, Weisheng Dong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Restoration</span>
<span class="topic-tag">Causal Modeling</span>
<span class="topic-tag">Benchmark</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2611.23889</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23889">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; this is image restoration with a clever interventional/statistical framing, which may still appeal for the methodology but is not a strong fit.</p>
        <p class="abstract">Composite image restoration aims to recover images corrupted by multiple coexisting degradations. Existing methods predominantly decompose composite corruptions into individual factors, relying on these isolated priors to guide restoration. However, coexisting degradations are inherently interdependent: the manifestation of one degradation dynamically shifts with the states of others, inducing non-additive interactions that factor-wise paradigms fail to capture. To bridge this gap, we formulate state-dependent cross-degradation responses and propose PROBE, an interventional framework that explicitly models how coexisting degradations influence one another. Specifically, we first construct unified degradation axes by aligning visual and textual degraded-clean offsets. Along these axes, a calibrated coordinate head estimates current degradation states, while bidirectional feature perturbations are injected to probe cross-coordinate responses under the current states. Contrasting these responses with corresponding intensity-matched single-degradation references quantifies intrinsic non-additive deviations, allowing the resulting response descriptors and state coordinates to jointly guide restoration. For comprehensive evaluation, we introduce SCD-15, a new benchmark covering all 15 nonempty combinations of four degradation factors at three severity levels. Experiments demonstrate that PROBE achieves state-of-the-art performance on the CDD-11, AWMM-100K, and SCD-15 composite restoration datasets using a compact model with modest GPU memory requirements.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Motion Analysis</summary>
      <div class="queue">

    <details class="paper-row" id="link20">
      <summary class="paper-row-summary">
        <span class="queue-index">21</span>
        <span class="paper-row-copy">
          <strong>PRISM: Profiling and Representation of Individual Stereotypical Motion</strong>
          <small>Austin A. MBaye, Savik Kinger, Matthew S. Goodwin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Motion Analysis</span>
<span class="topic-tag">Pose Estimation</span>
<span class="topic-tag">Vision-Language Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 21 / arXiv:2611.23646</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.23646">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 only very loosely: it studies interpretable motion profiling from pose/flow and includes a VLM comparison, but it is more about behavioral measurement than embodied spatial intelligence.</p>
        <p class="abstract">An anatomical pose provides interpretable joint structure, but no fixed set of physical landmarks can fully specify a person&#x27;s movement. We introduce PRISM, a complementary representation that characterizes repetitive movement using tracked masks and dense optical flow. Torso-relative flow measures intensity, frame-wise mask variation measures spatial extent, signed-flow recurrence estimates frequency, and persistent sliding-window geometry describes the rhythmicity of the movement. Across 1,890 synthetic conditions, the measurements recover controlled speed, amplitude, and frequency while exposing observation limits. An idealized hand-motion experiment demonstrates variation omitted by identical exact COCO-17 trajectories; controlled corruption experiments separately examine measurement sensitivity. Audits of two pose methods on the same data cohort and 36,930 external skeleton clips document incomplete observation and dependence on processing choices. In 1,404 annotated complex stereotypical motor movement bouts from six autistic participants, total flow converges with pose motion, while matched-coordinate examples and repeated-session profiles show differences in intensity, extent, frequency, and rhythmicity within behavior labels. A separate VLM comparison evaluates quantitative frequency estimation, and a profile-conditioned decoder links the measurements to illustrative skeletal movements. PRISM connects numerical profiles to visible examples, providing an interpretable way to compare how the same behavior is expressed beyond its label or event count.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>2 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Agent Memory</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>When Agent Skills Go Stale: Runtime Behavior and Selective Maintenance in Evolving Environments</strong>
          <small>\&quot;Omer Faruk Akg\&quot;ul, Shuli Jiang, Yuting Zhang, Yi Zhang, Xiaohan Fei, Wei Xia, Stefano Soatto</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agent Memory</span>
<span class="topic-tag">Runtime Adaptation</span>
<span class="topic-tag">Planning</span>
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
          <span>Paper 18 / arXiv:2611.22525</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22525">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only loosely: it studies agent skills in changing environments, but it is not an embodied AI benchmark or simulator-centric paper.</p>
        <p class="abstract">Agent skills use past experience and current observations to guide decisions and actions on related tasks. This experience is retained in skill state, whose reuse can amortize inference-time reasoning and environment interaction. When environment changes, parts of this state can become outdated while others remain useful. Across four task settings and two models, we compare skill reuse before and after environment changes. Previously beneficial skills can reduce task performance by over 10 percentage points or increase execution cost by nearly 40% relative to no skill. Task success can also remain unchanged while execution savings decline. These effects depend on which environment-specific details become outdated and the agent&#x27;s ability to compensate using current observations. We introduce selective maintenance, which replays checks from successful executions without additional model calls. It verifies whether observed differences conflict with skill state, repairs affected content, and validates updates, rebuilding when local repair is insufficient. No description of the change is supplied. Relative to reusing stale state, maintenance improves task accuracy by up to 67pp and reduces execution steps by up to 37%. These results suggest that preserving a skill&#x27;s inference time value as environments evolve requires selectively maintaining its state.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Large Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks</strong>
          <small>Xingchen AGI Lab, :, Baotian Hu, Bingkai Yang, Boyang Wang, Changzai Pan, Chao Lyu, Chao Wang, Chen Li, Chenshuo Pan, Chenyu Lin, Chenyuan Zhang, Chongming Liu, Dawei Fan, Di Wu, Dong Guo, Dong Li, Dongfang Li, Enlin Liu, Fanye Xiao, Fengkai Li, Fubei Yao, Gang Lin, Han Gao, Hanming Wu, Haowei He, Huapeng Liu, Hua Wang, Huinan Xu, Jiahong Xiong, Jiaxin Peng, Jianxiang Ma, Jianxing Zhuge, Jie Zhang, Ji Xiong, Jinglin Chen, Jingqi Li, Jingxuan Li, Jiwang Ye, Junchen Li, Junbiao Li, Junyang Wu, Kaidong Yu, Kaipeng Jia, Kehai Chen, Kuai Li, Laobin Liu, Lei Li, Libo Qin, Lingling Shi, Luwen Pu, Menghao Xu, Mengjiao Bao, Mengqi Chen, Min Zhang, Mingrui Wang, Naying Wang, Peicong Han, Peiming Guo, Pengfei Li, Qiang Feng, Qi Wang, Qingjun Zhu, Qingli Li, Qitai Ding, Qiyi Xie, Quanchao Zhao, Rongbao Han, Rui Xue, Ruiyu Fang, Ruiting Song, Shijie Li, Shiquan Wang, Shuangyong Song, Sishi Xiong, Teng Su, Wankang Bao, Weijie Zhang, Wei Mao, Weiwei Fu, Weiyang Huang, Wenmin Deng, Wenqing Hu, Wujie Zhong, Xi Yu, Xiaohui Hu, Xiaomin Fang, Xiaomeng Huang, Xiaoqiong Shi, Xiaotong Shang, Xiaoyu Li, Xinglei Xu, Xin Jiang, Xin Wang, Xin Zhang, Xinzhang Liu, Xue Liu, Xuefeng Bai, Xuewei He, Yahan Li, Yanhan Zhang, Yanlei Xue, Yanzhang Wu, Yang Yu, Yi Liu, Yin Zhang, Yingyan Li, Yitong Yao, Yixuan Li, Yongqiang Xia, Yongxiang Li, Yinzhou Zhu, Yu Zhao, Yuhao Jiang, Yunpeng Zhang, Yuting Lin, Yuxuan Wu, Yuyao Huang, Yuyi Wang, Zebo Peng, Zhenwu Pei, Zhenxiong Li, Zhao Wang, Zhaoxi Zhang, Zhihao Yang, Zhiqiang Dong, Zhiwei Yan, Zhilong Lu, Zhonghao Guo, Zhongheng Wu, Zhongjiang He, Zhongqiu Li, Zhu Yuan, Zhuoru Jiang, Zhuoyi Wei, Zijia Guo, Zilu Huang, Zhipeng Guo, Zirui Li, Zihan Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Large Language Models</span>
<span class="topic-tag">Agentic Training</span>
<span class="topic-tag">Systems</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 20 / arXiv:2611.22115</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.22115">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 in a loose sense: it reports frontier agentic LLM development and training infrastructure, but not a clearly novel visual/multimodal model.</p>
        <p class="abstract">We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning architecture selection, large-scale pretraining, and reasoning and agentic post-training. We study how sparse activation, attention design, model depth and width, and speculative decoding balance model capacity with computation, memory access, and execution overhead. Our pretraining infrastructure builds on MindSpore HyperParallel, combining topology-aware hybrid sharding, efficient distributed optimizer execution, and coordinated management of long-sequence workloads and activation memory. CPU affinity and core isolation further reduce host scheduling interference. Together, these mechanisms support the pretraining of a 285B-parameter model on 8,192 Ascend 910C cards, providing a concrete setting for the architectural and systems studies. For post-training, we introduce TeleGym, a unified agent execution platform that connects execution, evaluation, and trajectory construction to policy optimization. Disaggregated asynchronous execution, bounded oversampling, and partial rollout accommodate heterogeneous task durations while preserving trajectory continuity across policy updates. Together, these advances establish an Ascend-oriented training foundation for the continued development of Xing 4 across model scales and increasingly demanding reasoning and agent workloads.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
