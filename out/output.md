

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
      <p class="eyebrow">Daily ArXiv / November 26, 2026</p>
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
      <strong>11.0</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.21rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 71%, var(--accent))" title="20 mentions">action</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">agent</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">articulated</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">backbone</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="10 mentions">base</span><span class="cloud-word" style="font-size:2.70rem;opacity:0.98;color:color-mix(in srgb, var(--accent-2) 97%, var(--accent))" title="27 mentions">camera</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">change</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="11 mentions">control</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">dense</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">difference</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="10 mentions">dynamic</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">fake</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="9 mentions">field</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">flow</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">frame</span><span class="cloud-word" style="font-size:1.80rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="15 mentions">future</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">geometric</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="11 mentions">geometry</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">hand</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="9 mentions">inference</span><span class="cloud-word" style="font-size:1.80rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="15 mentions">joint</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">language</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">manipulation</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">memory</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">mesh</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="12 mentions">motion</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">navigation</span><span class="cloud-word" style="font-size:2.13rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 67%, var(--accent))" title="19 mentions">object</span><span class="cloud-word" style="font-size:2.13rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 67%, var(--accent))" title="19 mentions">observation</span><span class="cloud-word" style="font-size:2.64rem;opacity:0.97;color:color-mix(in srgb, var(--accent-2) 93%, var(--accent))" title="26 mentions">part</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">point</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="9 mentions">pose</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">prompt</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">real</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">scene</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">shared</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">sparse</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">spatial</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="7 mentions">success</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">supervision</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">target</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">token</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="8 mentions">trajectory</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="28 mentions">video</span><span class="cloud-word" style="font-size:1.97rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="17 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="87 mentions">action</span><span class="cloud-word" style="font-size:2.64rem;opacity:0.97;color:color-mix(in srgb, var(--accent-2) 93%, var(--accent))" title="164 mentions">agent</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="39 mentions">alignment</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="42 mentions">answer</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="47 mentions">attention</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="65 mentions">camera</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="49 mentions">change</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="34 mentions">construct</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="42 mentions">control</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="47 mentions">dynamic</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="46 mentions">environment</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="40 mentions">error</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="66 mentions">evidence</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="47 mentions">execution</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="36 mentions">fixed</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="38 mentions">foundation</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="39 mentions">four</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="81 mentions">generation</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="38 mentions">geometry</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="50 mentions">inference</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="48 mentions">interaction</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="36 mentions">knowledge</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="57 mentions">language</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="50 mentions">latent</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="68 mentions">memory</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="53 mentions">motion</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="59 mentions">multimodal</span><span class="cloud-word" style="font-size:1.80rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="92 mentions">object</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="60 mentions">observation</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="41 mentions">pair</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="45 mentions">part</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="41 mentions">physical</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="65 mentions">point</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="63 mentions">policy</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="39 mentions">prompt</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="55 mentions">question</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="37 mentions">real</span><span class="cloud-word" style="font-size:1.79rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="91 mentions">reasoning</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="43 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="37 mentions">reference</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="48 mentions">reward</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="52 mentions">same</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="69 mentions">scene</span><span class="cloud-word" style="font-size:1.86rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 53%, var(--accent))" title="96 mentions">semantic</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="35 mentions">shared</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="40 mentions">skill</span><span class="cloud-word" style="font-size:1.59rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="77 mentions">spatial</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="55 mentions">step</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="45 mentions">structure</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="38 mentions">success</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="50 mentions">supervision</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="52 mentions">support</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="50 mentions">target</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="47 mentions">token</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="48 mentions">trajectory</span><span class="cloud-word" style="font-size:2.30rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="132 mentions">video</span><span class="cloud-word" style="font-size:1.25rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="56 mentions">view</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="50 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="177 mentions">visual</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="52 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>17 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>Towards 360$^\circ$ Embodied UAV Tracking Without Turning</strong>
          <small>Bingyu Li, Wu Du, Zhiyuan Zhao, Junyu Gao, Xuelong Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">UAV Tracking</span>
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
          <span>Paper 1 / arXiv:2611.33934</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33934">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it introduces a new embodied UAV tracking benchmark/simulator setting and a VLA method for 360-degree embodied tracking.</p>
        <p class="abstract">Conventional embodied UAV tracking couples target observability with heading control because targets may leave the field of view of forward-facing cameras. We investigate a complementary paradigm that uses full-spherical perception to follow designated targets without active heading adjustment. To support this setting, we introduce 360UAV-ETrack, a simulation benchmark comprising 2,652 sequences, over 1.73 million synchronized observations, eight tracking tasks, and 150 held-out closed-loop scenarios. We propose 360UAV-TVLA, a panoramic vision--language--action (VLA) framework integrating persistent visual referring (PVR), compressed temporal memory (CTM), and geometry-aligned trajectory supervision (GTS) for instance identification, motion reasoning, and three-dimensional control. Experiments across two VLA backbones show consistent gains over standard fine-tuning, with normalized average tracking frames increasing from 22.56\% to 35.28\% for $\pi_0$ and from 25.68\% to 33.64\% for $\pi_{0.5}$. Our benchmark further reveals a substantial gap between offline imitation accuracy and closed-loop tracking reliability, establishing a challenging testbed for future research https://libingyu01.github.io/360UAV-ETrack_360UAV-TVLA/</p>
      </div>
    </details>


    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>Dynamic Forcing: Learning Action-Grounded Sparse Dynamic Representations with Dense Future Guidance for World Action Models</strong>
          <small>Ziqiang Li, Shisheng Chen, Yunnan Wang, Wenyao Zhang, Zili Lin, Yuyang Zhang, Xudong Yang, Fangzhuo Jin, Chenyu Zhou, Wenjun Zeng, Xin Jin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Robot Manipulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2611.33799</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33799">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a new method for world action models in embodied robotics, with sparse dynamic representations and action-grounded future guidance.</p>
        <p class="abstract">World action models (WAMs) support robot control through visual prediction, but dense future modeling repeatedly encodes static context already available in the current observation, while action-relevant changes are often spatially sparse. We study sparse dynamic representation learning, retaining the current observation as a contextual anchor and using a small set of compact dynamic tokens to represent anticipated changes. We develop CompactWAM, a sparse-dense joint predictive framework that enables sparse representation learning within a video-supervised shared backbone, without requiring a reconstruction objective for the sparse pathway. Since a limited token budget alone does not specify which information to retain, we introduce Dynamic Forcing, which pairs direct action supervision with privileged dense future guidance to promote action relevance and dynamic fidelity. While action prediction gradients directly drive compact tokens to capture control-relevant cues, dense future guidance further shapes them via action functional guidance that matches sparse and dense contributions to the action expert, and dynamics-aware distribution matching, which aligns temporal relational changes relative to a static reference. At inference, a single visual forward pass encodes current observations and compact dynamic tokens for action generation, eliminating dense future modeling. CompactWAM achieves 98.4\% success on LIBERO and 77.9\% on LIBERO-Plus, retaining respective success rates of 98.3\% and 76.6\% with only 9.2\% of the dense future token budget. Evaluations on RoboTwin~2.0 and real-world manipulation further demonstrate the effectiveness of the learned sparse predictive representations.</p>
      </div>
    </details>


    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>ArtKit: Motion-Driven Re-Segmentation and Link Re-Generation for Articulated Objects from RGB-D Video</strong>
          <small>Sylvia Yuan, Dan Wang, Vivian Yu, Ravi Ramamoorthi, Xinrui Cui</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
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
          <span>Paper 5 / arXiv:2611.33403</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33403">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: embodied AI / simulator-related benchmark building and a new method for articulated object reconstruction from RGB-D video, including a new benchmark (HArt).</p>
        <p class="abstract">An RGB-D camera that films an object being moved, often from one viewpoint, sees one side of it and how its parts move. We present ArtKit, which takes such a video as input to create an articulated model with complete parts, a kinematic tree, and typed joints. Our central idea is generating the hidden geometry and verifying it against what the camera sees. A generative part prior proposes complete, part-decomposed geometry based on the first frame. Point tracks, grouped into rigid trajectories, split and merge the generated parts into links. We then fit revolute and prismatic joints, with a visibility-aware energy ensuring that the articulated model explains the depth observed across the video. A rule checks against the video to choose between synchronous group fits and per-frame chain fits, so that one pipeline serves a diverse range of articulated objects, such as household items and robotic hands. Finally, we regenerate each link of the chosen fit as one part and keep it wherever it agrees better with the observations. We evaluate on Articulate-100 and on HArt, a new benchmark of 60 PartNet-Mobility objects and 8 robotic hands and grippers rendered as RGB-D videos with ground-truth parts and joints. ArtKit reduces the axis and part motion errors of the strongest baseline by more than half on the objects, as well as the axis error on the hands. ArtKit also runs on real recordings and generated videos.</p>
      </div>
    </details>


    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>ArtTet: Watertight Part Meshes of Articulated Objects from Rigid-Body Rules and Partitioned Marching Tetrahedra</strong>
          <small>Sylvia Yuan, Dan Wang, Ravi Ramamoorthi, Xinrui Cui</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Articulated Reconstruction</span>
<span class="topic-tag">3D Geometry</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2611.33382</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33382">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: embodied AI / articulated-object reconstruction with a new method for building watertight part meshes and recovering joints from multi-view observations.</p>
        <p class="abstract">We present ArtTet, a method that reconstructs an articulated object from multi-view observations of two articulation states and outputs one watertight mesh per rigid part together with the joints that move them. Mesh splatting gives explicit triangles, but it treats the object as one scene. It extracts a single global surface and cannot keep the triangles of different parts apart; the mesh it exports is layered, self-intersecting, and full of holes. ArtTet follows a divide-and-conquer strategy instead. We first divide the object into rigid parts with dynamic- and geometric-constrained articulation and ownership inference. A multibody registration of the two states recovers the parts and their screw joints. Rigid-body rules on attachment, contact, and swept motion then correct joint types and part labels without any part annotation. We then divide space into part cells with an articulated tetrahedral partition, and conquer each cell with its own differentiable signed distance field on a shared tetrahedral grid. In these partitioned marching tetrahedra the fields are mutually exclusive by construction, so the extracted part meshes are closed and never overlap. All part meshes are optimized jointly from the images of both states through the recovered joints. On Articulate-100, ArtTet gives the most accurate axis directions, part motions, and part geometry over all objects among methods that use no part masks, and its part meshes have virtually no open boundary edges. We also show reconstructions of real captures from the SplArt dataset.</p>
      </div>
    </details>


    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>EgoCARBS: Egocentric Video Meets Active Acoustics for Kitchen Action Understanding</strong>
          <small>Saif Mahmud, Vineet Parikh, Bharath Hariharan, Cheng Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Egocentric Vision</span>
<span class="topic-tag">Audio-Visual Benchmark</span>
<span class="topic-tag">Action Understanding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.HC</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2611.33565</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33565">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it builds a new embodied-action benchmark combining egocentric video with active acoustics for kitchen action understanding, with a novel sensing angle that previous work ignored.</p>
        <p class="abstract">Egocentric video records what a person looks at, but often misses what their body does: the hands leave the frame, and arm motion goes unseen. An exocentric camera recovers this context, but it must be installed wherever the activity happens. Active acoustic sensing can recover it from the wearables themselves: a device&#x27;s speaker emits inaudible chirps, and its microphone senses the motion of the hands, arms, and nearby objects from their echoes. Yet no public dataset pairs it with egocentric video. We present EgoCARBS, with two deliverables. The first is a multimodal dataset and benchmark: 15 participants cook unscripted meals in their own kitchens wearing camera glasses and an off-the-shelf smartwatch that both sense with active acoustics, synchronized with egocentric and exocentric video and the watch&#x27;s audio and IMU, with 4,019 verb-noun action annotations in 11.4 hours. The second is a study of what the wearables add to egocentric video. On verb recognition, they add at least as much as an exocentric camera for participants seen in training, and even more for new participants, for whom the exocentric camera does not help. Active acoustics alone provides most of this gain, and helps most where the camera does not see the hands. Trimmed action recognition, detection, and anticipation remain open. We will release the data, our data collection and annotation tools, and pre-trained models.</p>
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
          <strong>VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors</strong>
          <small>Ying Jiang, Donglai Xiang, Anita Hu, Masha Shugrina</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">3D Priors</span>
<span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Video Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2611.33591</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33591">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 3 very closely: a long-horizon video world model with compositional 3D priors, explicit camera control, and scene exploration for physical AI/embodied reasoning.</p>
        <p class="abstract">Long-horizon video generation is key to interactive world modeling, physical intelligence, and spatial reasoning, yet maintaining geometric consistency and accurate camera control remains challenging without 3D grounding. We introduce \textbf{VivaWorld}, a framework for generating geometry- and view-consistent long videos from an image. We first construct a compositional hybrid 3D representation that combines reconstructed point clouds, which preserve observed scene geometry and appearance, with generated textured meshes, which provide complete object geometry across $360^\circ$ novel views. We also introduce a connected-region filter removing inconsistent floating components for robust cross-view reconstruction and propose a hybrid camera embedding that combines global and object-anchored Pl\&quot;{u}cker rays to capture both scene-level camera motion and camera-object relationships, and inject it together with the visual guidance into a video generation model via a control adapter. Extensive experiments show VivaWorld achieves state-of-the-art visual quality and camera control, while supporting controllable novel-view synthesis, long-horizon scene exploration, and physical AI. Project page is available at: https://research.nvidia.com/labs/sil/projects/vivaworld/</p>
      </div>
    </details>


    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model</strong>
          <small>Zixuan Li, Kangyao Huang, Meng Xu, Wan Tian, Xiaoyu Tang, Jinge Sun, Yingliang Yao, He Chen, Lingzhong Meng, Yunzhi Xue, Jingyu Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Drone Vision</span>
<span class="topic-tag">6-DoF Motion</span>
<span class="topic-tag">Embodied AI</span>
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
          <span>Paper 7 / arXiv:2611.33779</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33779">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 3 closely: an action-conditioned drone world model with dual 6-DoF visual flows for trajectory following and scene dynamics, directly aimed at spatial/embodied understanding.</p>
        <p class="abstract">Action-conditioned video world models generate future observations from an initial frame and a camera trajectory, but often fail to align camera commands with visual dynamics or represent full 6-DoF scene transformations. We present DuoWM, a first-person drone video world model with two complementary visual conditions. Action flow projects future camera positions and orientations into each target frame, while Object flow forward-warps the initial observation and overlays local 6-DoF transformations to ground the induced scene motion. We further introduce transform-aware pretraining, which pairs object appearance with explicit transformation axes before standard RGB video training. On Sekai-drone dataset, DuoWM achieves the best results across video quality, 3D consistency, and trajectory following. Compared with Captain Safari, the state-of-the-art method, our approach reduces real-domain FVD and LPIPS by 17.2\% and 21.6\%, respectively, while improving game-domain AUC@30 from 0.5003 to 0.5719 and AUC@15 from 0.3088 to 0.3747.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Control</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>SPARC: Geometry-Guided Attention Pruning for Long-Horizon Camera-Controlled Video Generation</strong>
          <small>Zesong Yang, Weikai Chen, Liyuan Cui, Yuan Li, Jiaxin Huang, Lutao Jiang, Runze Zhang, Yingda Yin, Xiaoyang Huang, Kai Yan, Keyang Luo, Xin Wang, Hujun Bao, Zhaopeng Cui</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Control</span>
<span class="topic-tag">Video Diffusion</span>
<span class="topic-tag">Attention Pruning</span>
<span class="topic-tag">Camera-Conditioned Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2611.34064</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.34064">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: it proposes a geometry-guided attention pruning method for camera-controlled video generation with persistent scene memory, directly improving spatial control and spatial understanding in embodied/video generation settings.</p>
        <p class="abstract">We present SPARC, a geometry-guided attention pruning framework that turns the native self-attention of pretrained video diffusion transformers into a unified mechanism for camera control and persistent scene memory. Our key insight is that attention connectivity can simultaneously serve as geometric conditioning for camera control and spatial addressing for historical memory retrieval. Motivated by the asymmetric contextual requirements of reconstructing observed content and synthesizing novel regions, SPARC restricts observed tokens to geometrically corresponding historical tokens and local spatiotemporal context, while preserving dense attention for unobserved regions. Correspondence-aware attention biasing and order-invariant historical positioning further enable stable retrieval across long temporal gaps. Without introducing additional learnable control or memory modules, SPARC achieves precise camera adherence and faithful scene revisitation while substantially reducing attention computation. Extensive experiments demonstrate the effectiveness of aggressive attention pruning in improving camera adherence, revisit consistency, and visual fidelity, with an inference speedup of over 50x when combined with four-step distillation. Project page is available at https://zju3dv.github.io/SPARC.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied 3D Perception</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Revisiting Monocular In-Hand Object Scanning: Dataset, Pose Estimation, and Surface Reconstruction</strong>
          <small>Di Wu, Jeeeun Kim, Shu Kong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied 3D Perception</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Surface Reconstruction</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.GR</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2611.33824</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33824">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it builds a new embodied/3D scanning benchmark and a new method for monocular in-hand object scanning with pose estimation and reconstruction.</p>
        <p class="abstract">In-Hand Object Scanning (IHOS) from monocular video captured by a commodity smartphone holds immense potential to democratize 3D digitization for non-expert users, facilitating applications in digital archiving, augmented reality, and custom fabrication. Yet, IHOS remains largely understudied due to a lack of realistic datasets and systematic benchmarks. To bridge this gap, we introduce ToysRUs, a high-quality dataset featuring diverse figurines captured by 4K Ultra High-Definition (UHD) monocular videos. Studying IHOS from first principles, we examine structure-from-motion (SfM) for camera pose estimation, which is key to IHOS. We identify two key challenges: small baselines between consecutive frames, and sparse feature matches across large-view, long-range frames, further exacerbated by dynamic hand occlusions. Guided by these insights, we propose performing SfM on video sub-sequences sampled at sufficient angular intervals, and iteratively stitches the corresponding sub-trajectories into a unified global trajectory. Furthermore, for high-fidelity surface reconstruction, we introduce occlusion-aware 2D Gaussian Splatting, which incorporates opacity rendering and omits the opacity loss on hand regions. Quantitative and qualitative evaluations demonstrate that our framework significantly outperforms existing approaches, including neural implicit representations and 3D foundation models, in both geometric accuracy and photometric fidelity.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Articulated Objects</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>ArtLang-4D: Articulation-Aware Dynamic Language Fields from Monocular Videos</strong>
          <small>Sylvia Yuan, Dan Wang, Ravi Ramamoorthi, Xinrui Cui</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Articulated Objects</span>
<span class="topic-tag">3D Language Fields</span>
<span class="topic-tag">Monocular Reconstruction</span>
<span class="topic-tag">State-Aware Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2611.33511</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33511">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 partially: it introduces articulation-aware dynamic language fields for articulated objects, improving state-aware spatial understanding of object motion from monocular video.</p>
        <p class="abstract">Language that describes an articulated object is often about its state: the drawer pulled out the furthest, the door opened halfway, push the drawer all the way in. Existing 3D language fields attach one feature to each point and cannot tell these descriptions apart, and 4D language fields condition on video time, which has no kinematic meaning and cannot be set by a user. We present ArtLang-4D, which reconstructs an articulated object from a single monocular RGB-D video and equips it with a dynamic language field indexed by articulation time t, the normalized state of its joints, instead of video time. The geometry is a canonical triangle field whose triangles follow typed screw joints, discovered from the video without any joint initialization. The language field is supervised by a t-tagged caption bank that describes each part with comparative state phrases in a whitened open-vocabulary text space. A free-form query is answered by maximizing part relevance jointly over parts and states, which returns both the part and the articulation state it describes; a command is then executed by moving only that part along its recovered joint. On the 100 objects of Articulate-100, ArtLang-4D recovers more accurate joints and part geometry than reconstruction and articulation baselines, retrieves the queried state far more reliably than a state-agnostic language field, and executes language commands with lower motion error.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Matting</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>X-Matte: VAE-Free Pixel-Space Flow Matching for Single-Step Image Matting</strong>
          <small>Zanyi Wang, Jiaang Li, Dengyang Jiang, Ziru Wang, Chengzu Li, Davit Abrahamyan, Harry Yang, Serge Belongie, Mengmeng Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Matting</span>
<span class="topic-tag">Flow Matching</span>
<span class="topic-tag">Generative Vision Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2611.33874</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33874">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: a generative-model-based vision application (matting) with a VAE-free flow-matching design, relevant to vision foundation model adaptation.</p>
        <p class="abstract">Pre-trained generative models offer rich visual priors for image matting, but their adaptation often relies on variational autoencoders (VAEs), whose spatial compression can degrade fine alpha details and introduce additional inference overhead. To address these limitations, we propose X-Matte, a VAE-free pixel-space flow matching framework for single-step image matting. By eliminating latent compression, X-Matte formulates the RGB-to-alpha transition as a continuous flow directly in pixel space. We adopt trajectory-wide x-prediction with transition-aware alpha supervision, enabling the model to learn from intermediate states while directly predicting the target alpha matte in a single forward pass. This design avoids both VAE encoding and decoding and iterative sampling. Extensive experiments demonstrate performance competitive with state-of-the-art trimap-free matting methods on P3M benchmarks, together with promising zero-shot generalization to RWP-636 and AIM-500. Moreover, X-Matte achieves up to a 9.4x inference speedup over a constructed single-step latent counterpart at high resolution, demonstrating the effectiveness of VAE-free pixel-space modeling for accurate and efficient image matting.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Geospatial Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>geo-eval-harness: An Evaluation Harness for Geospatial Foundation Models</strong>
          <small>Nils Lehmann, Caleb Robinson, Isaac Corley, Jennifer Marcus, Inbal Becker-Reshef, Juan M. Lavista Ferres, Hannah Kerner</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Geospatial Foundation Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Remote Sensing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2611.33990</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33990">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a controlled evaluation harness for geospatial foundation models, focused on benchmarking vision foundation models and their applications.</p>
        <p class="abstract">Geospatial foundation model (GFM) research papers are plagued by inconsistent evaluation settings (e.g., different pre-processing and probes), making it difficult to separate performance from evaluation choices. We propose geo-eval-harness}, an open-source framework for controlled model comparisons. We use this harness to evaluate 100 GFMs and general vision models on 6 classification and 14 segmentation datasets, using multiple probes on frozen or low-rank-adapted encoders. We show that under controlled evaluation, general vision backbones are competitive on RGB classification and high-resolution segmentation, but GFMs shine on multispectral tasks. When we compare any two of the top-ten classification models on a single dataset, their 95% confidence intervals overlap 73% of the time. We show that bigger models are not always better: inference FLOPs correlate weakly with segmentation performance. Moreover, translating inference compute into large-area mapping workloads shows how small accuracy differences have outsized deployment cost differences: with frozen encoders on SpaceNet2, a 0.9-point mIoU difference corresponds to 5.9x the compute and days of additional projected GPU time. Our findings stress the importance of comparing models under explicit and fixed settings, and reporting uncertainty and deployment compute alongside accuracy. Our geo-eval-harness makes controlled experiments easy, fast, and fully reproducible. We release the code, configurations, and results at https://github.com/torchgeo/geo-eval-harness.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Text-to-Image Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>What Does RL Post-Training Teach Text-to-Image Models? A Skill-Wise Analysis of Flow-GRPO</strong>
          <small>Cheng Zhang, Jiesong Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Image Generation</span>
<span class="topic-tag">RL Post-Training</span>
<span class="topic-tag">Empirical Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 20 / arXiv:2611.33316</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33316">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: it analyzes RL post-training behavior in text-to-image models, giving an insightful empirical study of spatial relation skills in generative vision-language modeling.</p>
        <p class="abstract">Reinforcement learning (RL) post-training has become a standard way to improve text-to-image flow models: Flow-GRPO lifts the GenEval score of SD3.5-M from 0.63 to 0.95, a gain read as the model having learned compositional generation. We ask how much of that gain the base model&#x27;s own samples already contained, by measuring pass@k over shared noise seeds, one skill at a time, before and after RL, on prompts never used in training. The answer differs by skill. On four of GenEval&#x27;s six skills, where 32 base samples already solve almost every prompt, the gain is sharpening: one post-trained sample is worth 4 to 10 base samples, and pass@32 barely moves. On spatial relations it is unlocking: pass@32 rises from 0.69 to 1.00, 128 base samples do not match one post-trained sample, and prompts the base model never solved in 32 samples are solved 93% of the time, as often as those it solved. The benchmark average, 31 base samples per post-trained sample, describes no skill. Relations carry 35% of the gain; of the other 65%, selecting among 8 base samples with the judge behind the reward recovers nine tenths. We propose an account of when each occurs: within a prompt, a group-relative update re-weights only the outcomes its samples contain, and a flow policy cannot widen the noise that produces them; across prompts, shared parameters let successes on some prompts repair a deficit common to many. The same anatomy applies to a text-rendering checkpoint. The account&#x27;s predictions are tested with a checkpoint trained without KL, within-prompt diversity, and controlled training that holds object classes out, where sharpening comes first and transfers, and unlocking follows, on practised objects before unseen ones.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link20">
      <summary class="paper-row-summary">
        <span class="queue-index">21</span>
        <span class="paper-row-copy">
          <strong>Agentic Reinforcement Learning with Immediate and Prospective Credit Assignment for Medical Visual Reasoning</strong>
          <small>Yuqi Cheng, Rui Meng, Yijin Li, Chandra Sekhar Reddy Edula, Xiuwei Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Reinforcement Learning</span>
<span class="topic-tag">Medical VQA</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 21 / arXiv:2611.33777</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33777">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 weakly: it is a visual reasoning agent that learns where to look next, but it is medical VQA rather than spatial understanding or embodied spatial intelligence.</p>
        <p class="abstract">Medical visual question answering (VQA) requires acquiring useful evidence and deciding where to look next. Yet final-answer rewards do not reveal which observations support answering or guide subsequent inspection. We introduce MedPACT, an agentic reinforcement learning framework that learns selective observation policies through immediate answer support and prospective guidance. Our content-controlled estimator compares next actions induced by real and matched alternative observations under a shared real-observation history, isolating how observed content improves subsequent decisions. We combine both forms of credit within GRPO, assigning observation credit to the corresponding tool-call tokens alongside trajectory-level outcome supervision. MedPACT uses a single vision-language model and image-question-answer supervision, with credit estimation confined to training. Experiments with 4B and 8B backbones on six medical VQA benchmarks demonstrate improved accuracy, strong out-of-distribution generalization, and substantially lower inference costs. Case studies further illustrate how MedPACT avoids repeated observations and uses acquired evidence to guide subsequent inspection, demonstrating real-world practice potential.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Aerial Navigation</summary>
      <div class="queue">

    <details class="paper-row" id="link21">
      <summary class="paper-row-summary">
        <span class="queue-index">22</span>
        <span class="paper-row-copy">
          <strong>A Simple Yet Effective Agent for Open-World Aerial Object Search</strong>
          <small>Jitai Hao, Liangxing Yang, Zhenyang Li, Fan Liu, Qiang Huang, Jun Yu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Aerial Navigation</span>
<span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Agentic Search</span>
<span class="topic-tag">Training-Free Methods</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 22 / arXiv:2611.34115</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.34115">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 partially: it studies open-world aerial object search with a frozen VLM agent, which is embodied/navigation-related and uses a novel training-free setup, though it is more of a strong baseline than a new benchmark or deep methodological leap.</p>
        <p class="abstract">Open-world aerial object search methods often rely on persistent spatial maps, learned world models, or task-specific policy training. To examine how far a minimal, training-free design can go, we introduce SimpleUAV, an agent built around a frozen, off-the-shelf vision-language model (VLM). SimpleUAV separates current-view target assessment from history-conditioned action selection, combining fresh candidate evidence with lightweight search context. Local geometry converts visual selections into bounded straight-line movements, depth-based checks halt blocked segments, and measured execution feedback guides subsequent decisions. This closed loop sustains search without persistent spatial maps or task-specific training. SimpleUAV achieves 41.61% Success Rate (SR) on UAV-ON and 11.98% on AerialDojo-200K, compared with 23.80% and 3.20% for the strongest prior baselines, respectively. With limited benchmark-specific adaptation, the same core agent transfers to aerial Vision-and-Language Navigation (VLN) on TravelUAV, improving Full SR by at least 19.66% across all three splits under L1 assistance. These results establish a strong baseline for evaluating when additional architectural complexity benefits aerial search.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link22">
      <summary class="paper-row-summary">
        <span class="queue-index">23</span>
        <span class="paper-row-copy">
          <strong>Teaching Students to Stand on Their Own: Distilling Vision Foundation Models for Fine-Grained Few-Shot Class-Incremental Learning</strong>
          <small>Junsu Kim, Seungryul Baek</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Knowledge Distillation</span>
<span class="topic-tag">Few-Shot Learning</span>
<span class="topic-tag">Class-Incremental Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 23 / arXiv:2611.33749</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.33749">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 partially: it is about distilling vision foundation models for fine-grained incremental learning, so it is VFMs-related but not about a new foundation model or a core vision-language/embodied method.</p>
        <p class="abstract">Fine-grained few-shot class-incremental learning (FG-FSCIL) aims to incrementally learn visually similar new classes from limited images without catastrophic forgetting. Prior work typically learns strong representations on base classes or leverages vision foundation models (VFMs) directly as backbones or via knowledge distillation. However, VFM backbones incur high computational costs and do not guarantee fine-grained recognition. Although knowledge distillation reduces inference cost, our preliminary experiments reveal that distilled students still lag substantially behind their VFM teachers, particularly on new classes. To address this limitation, we propose STAND, a systematic VFM-to-student distillation design tailored for FG-FSCIL. Specifically, STAND connects the teacher and student by equipping the student with a fixed copy of the teacher&#x27;s classifier, aligning their outputs via projectors, and feeding both models composite images that combine different training images. On these composite images, relation distillation matches how the teacher and the student relate each image to other images, while difference distillation matches how this relation changes between two composite images. Finally, we freeze the student and classify new classes using length-calibrated prototypes, which restore the reduced similarity of few-shot prototypes. Extensive evaluations demonstrate that STAND achieves state-of-the-art performance across FG-FSCIL datasets at low computational cost, while generalizing across student backbones and broader datasets.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Human Mesh Recovery</summary>
      <div class="queue">

    <details class="paper-row" id="link23">
      <summary class="paper-row-summary">
        <span class="queue-index">24</span>
        <span class="paper-row-copy">
          <strong>ScaleCurve: From Constant Scale to Consistent Motion for World-Space Human Mesh Recovery</strong>
          <small>Sanghyeon Lee, Jong Taek Lee</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Human Mesh Recovery</span>
<span class="topic-tag">Spatial Consistency</span>
<span class="topic-tag">Camera Trajectory</span>
<span class="topic-tag">3D Vision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 24 / arXiv:2611.34005</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.34005">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 partially: it improves world-space human mesh recovery by fixing time-varying scale consistency along camera paths, which is relevant to spatial understanding but narrower than the main embodied-agent focus.</p>
        <p class="abstract">World-space human mesh recovery can lose spatial consistency even when camera-space body estimates are accurate. A single sequence-wide scale resolves global scale ambiguity but cannot correct local scale distortion along a reconstructed camera path. We present ScaleCurve, a framework that estimates time-varying metric corrections from human-ground geometry. We construct scale observations by comparing predicted foot geometry with locally fitted ground planes. Joint temporal optimization downweights inconsistent observations and couples neighboring scale estimates, allowing calibration to adapt along the camera path without freely following measurement noise. We scale camera translation increments and integrate them into a calibrated trajectory. With this camera fixed, we refine the lifted body motion using 2D image evidence and pretrained 3D dynamics, while restricting global trajectory rescaling. ScaleCurve achieves state-of-the-art performance on most evaluated metrics on both EMDB-2 and SLOPER4D. Consistent gains across three HMR backbones demonstrate its compatibility with diverse body estimates without retraining. Code will be made publicly available.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>7 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Navigation</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>PoseVLN: Learning Geometric State Evolution for Vision-Language Navigation</strong>
          <small>Pengyu Hou, Mingfei Han, Haihong Hao, Xiaolong Wu, Bo Dong, Xiaojun Chang, Salman Khan, Bin Shi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Navigation</span>
<span class="topic-tag">Geometric Reasoning</span>
<span class="topic-tag">Embodied AI</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2611.32218</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.32218">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: it proposes a geometric-state formulation for vision-language navigation, explicitly modeling pose evolution for embodied agents.</p>
        <p class="abstract">Vision-Language Navigation (VLN) requires an embodied agent to relate past experience, current spatial state, and future motion while following natural-language instructions. Recent approaches improve these capabilities through long-horizon memory, state-aware reasoning, and future prediction, yet these components are often modeled separately, leaving navigation state evolution insufficiently connected across time. We argue that camera pose provides a natural geometric representation for bridging past, present, and future states. Based on this insight, we propose PoseVLN, a pose-aware VLN framework that jointly learns navigation decisions and geometric state evolution. PoseVLN organizes visual memory and the current observation in an episode-relative coordinate frame, and jointly predicts the next K navigation actions together with a local $\Delta$Pose over the same horizon. The predicted $\Delta$Pose is composed with the current trajectory-level pose to obtain the future pose state, which is recursively propagated throughout navigation, forming a continuous geometric state evolution from past memory to future motion. Experiments on the R2R-CE and RxR-CE Val-Unseen splits demonstrate the effectiveness of explicitly modeling geometric state evolution, with PoseVLN outperforming the strongest compared baselines by 2.6 and 2.9 percentage points in success rate, respectively, using only single RGB observations.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Robot Manipulation</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>EffectWAM: Learning Action-Grounded Effects for Robot Manipulation</strong>
          <small>Yuan Zhang, Hao Cui, Jingfei Ni, Meiyi Wang, Xin Nie, Chi Liu, Wenjie Xu, Lin Gao, Hao Li, Xianhe Zhang, Jiajia Wu, Diyuan Liu, Jia Pan, Chao Ji</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Robot Manipulation</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Embodied AI</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2611.32053</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.32053">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: new method for embodied robot manipulation with action-grounded world-action modeling and executable control.</p>
        <p class="abstract">World-action models connect visual prediction with executable robot control. We present EffectWAM, which develops this connection through three complementary components: Effect, camera positional encoding (CaPE), and Action Grounding. Effect represents visual change as the difference between independently encoded future observations and a shared current-observation anchor. CaPE conditions endpoint pooling on relative camera pose when reliable extrinsics are available, while sharing the same learned parameters with pose-free pooling for uncalibrated trajectories. Action Grounding trains the visual representation to retain measured changes in end-effector pose and gripper state. An exponential moving average of the observation encoder supplies Effect targets. A shared generation expert learns to jointly predict Effect and an executable action chunk through flow matching, and reuses the sampled pair to generate future video on demand. This allows the controller to execute actions without waiting for video synthesis. We train on more than 20,000 hours of heterogeneous embodied data, excluding unused chain-of-thought data, and accommodate dataset-specific joint, end-effector, and hand-pose representations. Our evaluation uses the Small (8B) configuration on all five benchmarks and additionally evaluates the Large (26B) configuration on RoboDojo. Experiments examine closed-loop manipulation across complementary benchmarks, and comparisons across multiple baseline policies show consistent improvements from Action Grounding.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal LLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>MOZAIC: An Audio-Video Deepfake Benchmark for Telling What Is Fake</strong>
          <small>Shaina Raza, Mohamed Hafez, Ahmed Y. Radwan, Khalid Elgazzar, Kathryn Hume</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Deepfake Detection</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
<span class="category-tag">cs.SD</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2611.31301</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.31301">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and partly criterion 4: evaluates multiple audio-video MLLMs on a new deepfake benchmark and studies multimodal foundation-model behavior.</p>
        <p class="abstract">Audio-video (AV) deepfakes can fake the face, the voice, or both. Most benchmarks only ask whether a clip is real or fake, so they cannot show whether a detector relies on the picture, the voice, or encoding traces. We present MOZAIC, a paired benchmark with a 4-way label in which every source clip is released in all four combinations of real or fake video and real or fake audio so each modality contribution can be measured directly. Fakes cover inner-face swapping, whole-frame video diffusion and voice conversion. MOZAIC has 137,745 clips from 15,014 source pairs and four tasks: T1 AV authenticity, T2 manipulation type, T3 identity verification and T4 explanation. We evaluate 12 AV multimodal LLMs (MLLMs), train four detectors and fine-tune MLLMs with LoRA. Overall, the best MLLM reaches only 35.6% on the four-way T1 and catches far more video-only fakes than voice-only fakes (43.6% vs 7.5%). Trained detectors reach 98.4% on T1, and LoRA fine-tuning raises explanation scores (OmniVinci 4.17 to 7.40, Qwen2.5-Omni 4.42 to 6.98), but the best T1 detector falls to 78.3% when the face-swap generator is held out of training, so generalization and explanation remain open. We release the dataset, the compact MOZAIC-SMALL split, the code and the prompts. https://vectorinstitute.github.io/mozaic/</p>
      </div>
    </details>


    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>More Powerful, Less Verifiable? Mitigating Hard-to-Verify Hallucinations in MLLM&#x27;s Reinforcement Learning</strong>
          <small>Jianhong Pang, Ziyi Ye, Qiuxia Hou, Yanhao Zhang, Zuxuan Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Hallucination Detection</span>
<span class="topic-tag">RLHF/RLAIF</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2611.32055</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.32055">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: it studies reinforcement learning for MLLMs and introduces a dataset focused on hallucination verifiability in multimodal outputs.</p>
        <p class="abstract">Reinforcement learning (RL) strengthens model capabilities through feedback from humans and environments. However, emerging evidence suggests that reward optimization can produce outputs whose errors are harder for humans to detect. To address this issue, we construct ITHV (the Image-Text Hallucination Verifiability Dataset), comprising 2,728 visually grounded instances that distinguish between obvious hallucinations, which humans readily detect, and elusive hallucinations, which humans struggle to identify. We then propose DAPO-V, an extension of DAPO that maximizes correctness subject to a budget on verifiability-aware risk. Specifically, DAPO-V combines a verifiability-aware reward with adaptive dual control, where larger penalties are assigned to incorrect responses on questions with lower human verification accuracy. An adaptive multiplier further adjusts the penalty strength according to risk-budget violations. Across three MLLM base models, DAPO-V improves overall accuracy while substantially improving accuracy on elusive hallucination questions by 5.78--9.72 percentage points over accuracy-only DAPO. We further test DAPO-V with a blinded human study, which shows that hallucinations are more readily detected in DAPO-V than those of the base model.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>FigmaEval: A Benchmark for Evaluating AI Agents in Professional UI Design</strong>
          <small>Xinyue Huang, Yongyong Gao, Zhengyuan Pan, Zheng Wei, Xinya Liu, Duanyi Yan, Zhiyu Hang, Zheng Ma, Lewei Lu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">UI Agents</span>
<span class="topic-tag">Human Evaluation</span>
<span class="topic-tag">Multimodal Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2611.32321</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.32321">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it introduces a new benchmark for evaluating AI agents on professional UI design, focusing on a task-setting and evaluation angle that prior work largely ignored.</p>
        <p class="abstract">Recent advances in AI agents have enabled autonomous UI design using professional tools such as Figma, yet evaluating their design capabilities remains challenging due to the open-ended nature of design tasks and the absence of unique ground truths. We introduce FigmaEval, a benchmark for evaluating AI agents on professional UI design tasks, comprising 84 tasks and 783 screens derived from real-world Figma design files. FigmaEval adopts a constrained-specification, open-solution paradigm, standardizing task requirements and design resources while allowing agents to independently determine layouts, visual hierarchies, component composition, and visual presentation. To assess design quality beyond reference similarity, we develop 22 expert-grounded evaluation rubrics across six dimensions and introduce a human evaluation arena where professional designers compare agent-generated designs through blinded pairwise judgments. Evaluating eleven models under a unified Figma agent setup, we find substantial agreement between rubric-based assessments and human preferences, alongside distinct differences in design practices and quality--efficiency trade-offs. FigmaEval provides a framework for systematically assessing professional UI design capabilities and understanding the strengths and limitations of current AI agents.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language-Action</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning</strong>
          <small>Simin Huang, Jiawei Chen, Shaolong Zhu, Qiwei Liang, Zhaoxia Yin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Safety &amp; Backdoors</span>
<span class="topic-tag">Robotics</span>
<span class="topic-tag">Multimodal Security</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2611.32304</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.32304">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 partially: it targets Vision-Language-Action models and real-robot trajectory-level backdoor attacks, which is an embodied AI method paper but focused on safety rather than new spatial intelligence or benchmarks.</p>
        <p class="abstract">Vision-Language-Action (VLA) models advance robotic manipulation, but their reliance on demonstrations exposes them to backdoor threats. Among these threats, trajectory-level targeted backdoors are particularly challenging and may pose greater safety risks than behavior-disrupting attacks: rather than merely causing task failures or local action deviations, they must sustain closed-loop redirection to complete an attacker-specified multi-step task. To reliably induce such behaviors, existing methods typically rely on high poisoning rates to obtain sufficient target-trajectory supervision. However, high poisoning rates may compromise clean-task performance, whereas low rates leave target-trajectory supervision scarce and backdoor learning vulnerable to interference from dominant clean-task updates. To resolve this trade-off at low poisoning rates, we propose a two-stage co-optimization framework guided by vision, language, and action. Stage I freezes the policy and uses differentiable rendering and multimodal supervision to optimize a 3D trigger&#x27;s texture, translation, and scale, strengthening trigger-target associations from limited poisoned demonstrations. Building on the optimized trigger, Stage II applies source-selective dual-LoRA adaptation to decouple clean and backdoor updates and mitigate their interference, followed by learned column-wise calibration and analytic fusion into a unified policy. Experiments on OpenVLA, OpenVLA-OFT, $\pi_0$, and $\pi_{0.5}$ across four LIBERO suites show consistent gains over all evaluated attack baselines. With only 1% poisoned data, our method achieves 86.4% target success and 95.2% clean-task success on OpenVLA-OFT in LIBERO-Spatial. Real-robot trials also demonstrate trajectory-level hijacking.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>What People Choose Not to Say: A Multimodal Benchmark for Fine-Grained Information Manipulation in Conversations</strong>
          <small>Yuhan Bian, Zhaokai Liang, Jia Wang, Haoyu Liu, Yu Chen, Jianfeng Qu, Zhixu Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Benchmark</span>
<span class="topic-tag">MLLM Evaluation</span>
<span class="topic-tag">Conversational Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2611.31346</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.31346">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 weakly: it is a new multimodal benchmark for conversational information manipulation, evaluating MLLMs on fine-grained social reasoning rather than vision-grounded tasks.</p>
        <p class="abstract">Recent advances in MLLMs have improved social understanding, enabling models to recognize emotions and distinguish truthful from deceptive behaviors. However, existing benchmarks largely focus on coarse-grained emotion recognition or binary truth-deception detection, overlooking the diverse ways people manipulate information in conversations, such as withholding, leakage, fabrication, evasion, and defensive counterclaim. Understanding these behaviors requires reasoning about underlying facts, participant knowledge, and conversational context, making them difficult to evaluate reliably. To address this gap, we introduce InfoCon, a multimodal benchmark for fine-grained information manipulation in conversations. InfoCon identifies six fine-grained strategies and derives a coarse consistency label from their factual and interactional relations. We develop an evidence-grounded multi-agent annotation framework to construct and verify reliable labels from rich contextual evidence. We benchmark representative multimodal models and systematically analyze their fine-grained information manipulation understanding, providing a testbed beyond binary truth-deception judgments.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

        <a class="archive-link" href="past_arxiv/2026-11-24.html">
          <span>November 24, 2026</span>
        </a>


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
