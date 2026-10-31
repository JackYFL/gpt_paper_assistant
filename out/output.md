

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
      <p class="eyebrow">Daily ArXiv / October 31, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>11</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>19</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="26 mentions">agent</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">alfworld</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">answer</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="8 mentions">change</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">dynarev</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">emph</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">encoder</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">environment</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">envo</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">error</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">estimation</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">evidence</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">experience</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">harmonic</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">interaction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">interface</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">jepa</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="6 mentions">language</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">modality</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">next-token</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">observation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">online</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">pair</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">percentage</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">platonic</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">point</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">policy</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">positive</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">qwen</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">real</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="8 mentions">reinforcement</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">revision</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="9 mentions">reward</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">rotation</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="6 mentions">same</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">scope</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">seed</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">separately</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">social</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">success</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="6 mentions">trajectory</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">unseen</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">update</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="3 mentions">user</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="4 mentions">view</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.74rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="121 mentions">action</span><span class="cloud-word" style="font-size:2.33rem;opacity:0.89;color:color-mix(in srgb, var(--accent-2) 77%, var(--accent))" title="187 mentions">agent</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="67 mentions">alignment</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="48 mentions">answer</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="56 mentions">attention</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="51 mentions">backbone</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="51 mentions">camera</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="56 mentions">change</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="67 mentions">control</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="51 mentions">dense</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="49 mentions">diffusion</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="50 mentions">domain</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="64 mentions">dynamic</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="63 mentions">environment</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="51 mentions">error</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="125 mentions">evidence</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="50 mentions">execution</span><span class="cloud-word" style="font-size:2.03rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 62%, var(--accent))" title="152 mentions">generation</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="65 mentions">geometric</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="56 mentions">geometry</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="61 mentions">inference</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="94 mentions">interaction</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="50 mentions">jointly</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="76 mentions">language</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="61 mentions">latent</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="80 mentions">memory</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="76 mentions">motion</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="82 mentions">multimodal</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="61 mentions">multiple</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="75 mentions">object</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="61 mentions">observation</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="60 mentions">physical</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="95 mentions">point</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="71 mentions">policy</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="50 mentions">question</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="142 mentions">reasoning</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="52 mentions">reconstruction</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="59 mentions">reference</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="54 mentions">region</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="61 mentions">reward</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="87 mentions">same</span><span class="cloud-word" style="font-size:1.72rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 46%, var(--accent))" title="119 mentions">scene</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="98 mentions">semantic</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="49 mentions">skill</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="51 mentions">source</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="47 mentions">space</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="105 mentions">spatial</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="58 mentions">structure</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="73 mentions">supervision</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="77 mentions">support</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="60 mentions">target</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="46 mentions">temporal</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="74 mentions">token</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="93 mentions">trajectory</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="53 mentions">understanding</span><span class="cloud-word" style="font-size:2.37rem;opacity:0.9;color:color-mix(in srgb, var(--accent-2) 79%, var(--accent))" title="192 mentions">video</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="66 mentions">view</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="51 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="246 mentions">visual</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="102 mentions">world</span></div>
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
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>Proving and Improving the Platonic Representation Hypothesis with JEPAs</strong>
          <small>Randall Balestriero, Yann LeCun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">JEPA</span>
<span class="topic-tag">Cross-Modal Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
<span class="category-tag">stat.ML</span>
    </div>

        </span>
        <span class="score-pill score-high">19</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2610.39302</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.39302">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>10</strong></span>
          <span>Novelty <strong>9</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it is a vision foundation-model paper on JEPAs, representation alignment across modalities, and applications to image/text alignment.</p>
        <p class="abstract">Whether models trained on different modalities converge to the same representation of the world is central to AI. The Platonic Representation Hypothesis (PRH) conjectures that they do as they scale, but without a proof it offers neither a guarantee nor a recipe. We turn the hypothesis into a theorem. First, we prove a \emph{Platonic Representation Theorem}: Joint-Embedding Predictive Architectures (JEPAs) trained separately on any number of modalities learn the same representation up to one rotation whenever their positive pairs are two observations of one scene--\emph{good views}--and their misalignment is bounded otherwise. Second, we show that next-token prediction is a JEPA with \emph{bad views}, parts of a single document, which explains why language models align with vision only through scale. Third, we validate the theory from 145k captions to the texts of 940M web images, and uncover a scaling law of alignment that predicts unseen runs within seed noise. Good views need 42 times fewer training samples than next-token prediction on the same corpus to reach the same alignment, and a 109M-parameter text JEPA aligns with DINOv2 and CLIP&#x27;s image encoders better than every language model we evaluated, up to 72B parameters, and than CLIP&#x27;s text encoder: next-token prediction is a remarkably inefficient route to platonic representations. As a showcase, one rotation turns separately trained encoders into an image captioner (CIDEr .838 on COCO). Even that rotation needs no pair: on the latest pair-free benchmark, our text JEPA beats every zero-shot accuracy reported with language models up to 8B parameters, e.g., 64\% against at most 56\% top-5 on ImageNet-100. Positive views, and not scale alone, are thus the lever to build platonic representations.</p>
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
          <strong>Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps</strong>
          <small>Peitong Duan, Khashayar Gatmiry, Jeffrey Nichols, Samy Bengio, Emmanuel Abbe</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">UI Navigation</span>
<span class="topic-tag">Online Reinforcement Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2610.39264</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.39264">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: this is an embodied AI paper on UI navigation with a new online RL method and live-iOS training infrastructure, which is a novel simulator/live-environment angle.</p>
        <p class="abstract">While frontier vision-language models demonstrate strong capabilities in user interface (UI) navigation, their high inference costs prohibit everyday use. Conversely, smaller models trained via supervised fine-tuning (SFT) or offline reinforcement learning often memorize static trajectories, leading to brittle execution and an inability to recover from errors. To address these limitations, we propose a novel online reinforcement learning framework that trains UI navigation agents directly on live iOS applications. Our framework decouples the agent into two specialized components: a Planning agent and a UI Grounding model. We rely on an LLM-as-a-Judge to provide comprehensive reward signals, combining dense, step-level feedback to evaluate intermediate progress with a terminal reward for overall task completion. To effectively leverage this dual reward structure, we optimize the agent using Proximal Policy Optimization (PPO) with step-level advantage estimation. Furthermore, we introduce GiGPPO, a novel neighbor-conditioned value estimation method that improves critic stability by leveraging reward signals from visually similar states across concurrent trajectories. To support this online training paradigm at scale, we introduce an efficient infrastructure that orchestrates hundreds of concurrent virtual iOS devices. Evaluations on rigorous benchmarks, including UINavBench, iOSWorld, and AndroidWorld, demonstrate that our online RL trained agents substantially outperform both SFT and terminal-only RL baselines while accelerating training convergence. Notably, our 8B RL agents achieve nearly a sevenfold improvement over the SFT baseline in out-of-distribution generalization to Android environments, while outperforming Gemini-3.5-Flash and tying with Gemini-3.1-Pro on real iOS applications.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>Timbre: Reliability-aware harmonic consensus for label-free multimodal test-time rexinforcement learning</strong>
          <small>Haotian Lyu, Haoyu Wang, Ru Wang, Feng Ji, Ziwen Li, Jiaxian Guo, Mingming Gong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Test-Time Adaptation</span>
<span class="topic-tag">Multimodal Reinforcement Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2610.39439</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.39439">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it is a multimodal test-time adaptation/reinforcement method for VLMs, with explicit multimodal consensus and Qwen3-VL experiments.</p>
        <p class="abstract">Label-free test-time reinforcement learning adapts vision--language models using rewards derived from their own predictions. However, misinterpreted visual evidence and sensitivity to textual formulation can produce a consistent but incorrect consensus that majority voting reinforces. Cross-view aggregation can expose such errors, but image and text transformations may themselves degrade task-relevant evidence to different extents. We introduce \method, a reliability-aware harmonic consensus framework for multimodal test-time reinforcement learning. \method constructs a $2\times2$ grid combining original and perturbed images with direct-solving and reframing modes, selects pseudo-labels through weighted harmonic aggregation, and adapts modality-level weights using batch-averaged, temporally smoothed shifts in pseudo-label confidence as a heuristic reliability signal. We formulate consensus as a weighted $\chi^2$-barycenter problem whose unique minimizer is the normalized weighted harmonic aggregate, without requiring correct-answer invariance. An exact support--dispersion decomposition characterizes when harmonic aggregation preserves or corrects arithmetic rankings, while a sensitivity analysis establishes how modality reweighting changes pairwise ranking margins, informing interpretation of the heuristic updates. Across six benchmarks and three Qwen3-VL model scales, \method outperforms TTRV in 16 of 18 benchmark--model settings on adaptation instances and 17 of 18 settings on held-out instances under matched estimation and optimization rollout counts. These results demonstrate improved target-task adaptation and transfer to unseen instances without further updates.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied/Agent Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation</strong>
          <small>Ankush Kadu, Athira Gopal, Niharika Singh, Arpit Jain, Aswanth Krishnan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied/Agent Evaluation</span>
<span class="topic-tag">Benchmark Construction</span>
<span class="topic-tag">Computer-Use Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.HC</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2610.40246</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.40246">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it builds a benchmark/evaluation framework for computer-use agents in changing environments, with a simulator-like task construction and auditing setup.</p>
        <p class="abstract">Computer-use agents built on large language models (LLMs) work in software that can change while they act: an appointment moves, a policy is revised, a record is updated. Testing agents under such changes is harder than it looks. When an agent fails, the cause may be the agent, but it may also be a change that did not fire as intended, an update the agent never received, or a grader that scored the episode wrongly. We introduce EnvOS, a framework for building and certifying environments that change mid-task. Before any agent runs, EnvOS checks that each change fires correctly, that the task remains solvable, and that the grader separates correct from incorrect behavior; after each run, separate code re-checks the verdict from archived evidence. We apply it to stale information, where a value the agent has already seen changes before the agent acts on it. In clinic booking, Claude Opus 5 succeeds on 0/16 tasks when nothing extra is shown, 2/16 when reminded to re-check the source, and 15/16 when the updated value is shown; the gain over the reminder holds after correcting for all tests (p = 0.00293). In insurance-claim approval, Opus 5 re-checks on its own and succeeds on 10/10, whereas Claude Sonnet 5 rises from 1/10 to 9/10 when the current policy is shown again, a gain significant in its pre-registered test but not after correcting for all tests. Whether an agent caught a change thus varied with the model and the interface. We also stress-test the grading itself: on corrupted episodes designed blind from the rules, the EnvOS pipeline accepted none of 26 as clean, and on an externally generated set it caught 25 of 39, against 4 for simple log checks. Because every EnvOS environment is generated from a seed and graded by an audited automatic verifier, the same environments are natural candidates for training agents with reinforcement learning from verifiable rewards.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Web Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>WebAnything: From the Wild Web to Scalable Agent Environments</strong>
          <small>Tianci Xie, Zikun Cai, Chaoyun Zhang, Pinxue Guo, Bingxuan Li, Rui Zheng, Hang Yan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Web Agents</span>
<span class="topic-tag">Environment Construction</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2610.37786</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.37786">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately well: it builds scalable web-agent environments, which is an embodied/web-interaction benchmark and simulator-style infrastructure with a novel environment-construction angle.</p>
        <p class="abstract">Web agents require diverse, executable, and resettable website environments for reproducible training and evaluation. Human-assisted mirrors demand per-site engineering, while generative construction can diverge from specified real websites. Capture-and-replay preserves observations, with interaction coverage constrained by captured content and replay capabilities.   We present WebAnything, a fully automated framework that reconstructs source-grounded, reusable Web environments from real URLs without per-site manual implementation or repair after initial setup and authorization. An Explorer-Builder collects browser-observable structures, resources, and interaction outcomes; an independent verifier checks frozen candidates and guides local repair or targeted source recapture.   We construct 244 website artifacts across 14 application domains and 53 categories, supporting 12,984 executed and accepted tasks. Compared with human-assisted WebHarbor, WebAnything achieves higher aggregate scores on three fidelity metrics, with 12 wins, two ties, and no losses in a blind audit. Fine-tuning Qwen3.5-9B on 5,856 interaction trajectories improves REAL success by 9.9 percentage points, Odysseys-Easy Rubric Avg and Task Avg by 6.25 and 6.32 percentage points, and WebArena-Verified Overall success by 13.33 percentage points under the fixed harness. Code: https://github.com/china-qijizhifeng/Web-Anything</p>
      </div>
    </details>


    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>DynaRev: Benchmarking Web Agents under Dynamic Goal Revision</strong>
          <small>Shiqi Zhang, Guochen Zhou, Zesheng Wei, Hai Zhao, Zhisong Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Web Agents</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Interactive Planning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2610.40133</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.40133">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately well: it introduces a new benchmark for web agents under dynamic goal revision, focusing on a previously underexplored interaction setting.</p>
        <p class="abstract">Web agents are typically evaluated with goals fully specified before execution and fixed thereafter, whereas real users often revise their requirements during interaction. To study such interactions, we introduce DynaRev, a benchmark of 181 tasks to evaluate web agents under dynamic goal revision. DynaRev uses semantic milestones to deliver revisions at task-defined stages, covers additive revisions, unconditional overrides, and runtime-conditioned overrides, and evaluates correctness, responsiveness, and efficiency through trajectory-grounded evaluation. Five-model evaluations show that agents often satisfy only part of the task requirements, with performance varying across task sources, revision types, and models. Further analyses reveal varied milestone timing, mixed effects of dynamic delivery, and contrasting revision-handling outcomes, with gains from instruction rewriting while preserving browser state and losses from browser resets. DynaRev provides a testbed for studying how web agents adapt to evolving user goals. The code and data are available at https://github.com/zsq259/DynaRev.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Scientific Discovery</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World</strong>
          <small>Yusheng Zhao, Bowei He, Xue Liu, Mingxiao Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Scientific Discovery</span>
<span class="topic-tag">Agent Benchmark</span>
<span class="topic-tag">Counterfactual Evaluation</span>
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
          <span>Paper 7 / arXiv:2610.37919</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.37919">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 in a broad way: it is a new benchmark/testbed for scientific discovery agents, but it is not embodied AI or a vision-language model paper.</p>
        <p class="abstract">Large language model agents are increasingly used for scientific discovery. However, existing benchmarks mix law inference with programming, score data fitting instead of prediction on unseen inputs, and do not separate empirical evidence from pretrained priors. We introduce SciGame, a controlled benchmark that converts scientific literature into structured scientific cards. Each card yields a pair of Original and dimensionally consistent Counterfactual environments with the same task interface. SciGame contains a Historical collection of canonical laws and a live Temporal collection curated from papers published after model knowledge cutoffs. It evaluates agents in candidate-guided Identification and open-ended Discovery settings. Each setting runs under Prior-only, Fixed, and Adaptive protocols. Experiments on five frontier models yield three findings. First, familiar priors hurt performance once the governing relation is altered. Second, adaptive experimentation helps the strongest models but harms weaker ones under limited budgets. Third, good explanations can hide quantitative failures. Recovering the exact symbolic form remains the main bottleneck, even when agents interpret evidence correctly. Current agents can investigate systems actively, but inducing exact laws in unfamiliar settings remains an open challenge.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LLM Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>SocialArena: Evaluating Social Intelligence in Large Language Models</strong>
          <small>Zongqi Wang, Rui Wang, Yuchuan Wu, Hua Yang, Bingxue Qiu, Tianle Gu, Bing Zhao, Yujiu Yang, Jieping Ye, Yongbin Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LLM Evaluation</span>
<span class="topic-tag">Social Reasoning</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2610.39247</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.39247">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only in a loose sense: it is a new benchmark for social intelligence in LLMs, but it is not embodied AI, spatial intelligence, or a vision-language model paper.</p>
        <p class="abstract">We introduce SocialArena, a benchmark for systematically defining and evaluating the social intelligence of large language models (LLMs). Although LLMs are increasingly deployed in socially interactive applications such as mental health counseling, companionship chatbots, and educational tutoring, existing evaluations remain fragmented focusing on isolated capabilities or single scenarios and evaluation reliability is largely unverified. This work makes three main contributions to address these limitations. (1) We first propose a unified three-tier framework that defines social intelligence along three capability dimensions: role-playing ability, mental state reasoning, and behavioral reasoning. To operationalize this definition, we design a role-playing dialogue paradigm with explicit character thinking for evaluation, enabling simultaneous assessment of these capabilities in a manner that mirrors realistic human interactions. (2) To ensure diversity across social scenarios and thereby prevent evaluation conclusions from being confined to specific scenarios, we introduce the U-TRIMF framework, which guides us in synthesizing social contexts with broad coverage. (3) To obtain reliable evaluation, we invest $132.4K to recruit and train human annotators and adopt a human-annotated arena-style protocol, where annotators compare model responses and provide preference labels along with natural-language critiques. We hope that SocialArena can provide valuable insights and guidance for future LLM improvements.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Reinforcement Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information</strong>
          <small>Daniel Strauss, Nikolaos Sotirakis, Zhenshan Bing, Alois Knoll</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Reinforcement Learning</span>
<span class="topic-tag">Memory Retrieval</span>
<span class="topic-tag">Credit Assignment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2610.40030</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.40030">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Only a loose fit for criterion 3: it touches memory and retrieval credit assignment for reinforcement learning/robots, but it is not clearly an embodied-AI benchmark or a spatial understanding method.</p>
        <p class="abstract">Memory in reinforcement learning raises two problems. Attention finds the relevant item by scoring the whole store, which is costly for robots under latency and energy limits. When a retrieved memory pays off, credit for acquiring it must cross the whole sequence. We argue that both are governed by one quantity, the value of information, and propose to estimate it from archived rollouts with a learned world model. We obtain that, when read at the observation, it yields a provable lower bound on the optimal value of the acquiring action, which floors its TD target and attributes this floor to the observation that earned it. Read at the decision, it defines the optimal retrieval set. A pilot retrieval system, to be trained and improved with this signal, solves a memory task with reduced context.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>A-RSI: Adaptive Task Refresh for Zero-Data Multimodal Self-Improvement</strong>
          <small>Yu Liu, Youxing Li, Yuedong Tan, Zhiwei Yang, Zihan Su, Hanqi Feng, Shaojie Zhang, Libin Liao, Zihao Wan, Chenxu Wu, Cong Cao, Fangfang Yuan, Yanbing Liu, Ziheng Chen, Pei Fu, Radu Timofte, Zongwei Wu, Nicu Sebe, Barnabas Poczos, Jian Luan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Learning</span>
<span class="topic-tag">Self-Improvement</span>
<span class="topic-tag">Data Curation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2610.38568</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.38568">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is self-improvement for multimodal models, but it is not specifically a new VLLM/MLLM architecture or a vision foundation model application.</p>
        <p class="abstract">Recursive self-improvement requires models not only to acquire useful training experience, but also to decide when their current experience has ceased to be useful. Existing methods often focus on what experience to generate next, while paying less attention to when fresh experience should be introduced. Many also construct training targets through self-consistency or majority voting, making supervision depend on the model&#x27;s own uncertain predictions. We address these two questions separately: training dynamics determine when to acquire new experience, while the answers to new tasks remain independently checkable. A-RSI monitors reward variation and accuracy in training logs to refresh a task pool when its learning signal declines, without consulting validation or test scores. A static library of model-authored programs produces multimodal questions and derives their reference answers; we specify the task-generation contract, automatically verify chosen properties of the reward and refresh rules, and separately audit the generated answers. The training loop uses no external training examples or human-written answer labels. On the primary eleven-benchmark suite, A-RSI raises the performance average from 57.77 to 61.05 with 800 fresh tasks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Agentic Reinforcement Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>SCOPE: Selective Critical-Step On-Policy Self-Distillation for Agentic Reinforcement Learning</strong>
          <small>Qirui Liu, Wei Cao, Yu Mi, Yichen Sun, Xuekun Zhang, Lei Liu, Yue Shen, Zhixuan Chu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agentic Reinforcement Learning</span>
<span class="topic-tag">Self-Distillation</span>
<span class="topic-tag">Web/Embodied Tasks</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2610.38391</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.38391">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is agentic RL for web/ALFWorld-style tasks, but not a novel embodied spatial method or benchmark.</p>
        <p class="abstract">Outcome-based reinforcement learning provides coarse supervision for long-horizon LLM agents: failed trajectories may contain correct steps, while successful trajectories can contain errors. Trajectory-level skills can also shift teacher preferences at unrelated steps, introducing off-target distillation signals. We introduce SCOPE, a framework for Selective Critical-Step On-Policy Self-Distillation. After a supervised warm-up, the policy analyzes its own trajectories, generates step-specific hindsight skills, and distills their guidance only at selected error steps. A bounded signed teacher-student coefficient stabilizes auxiliary updates while preserving positive reinforcement and negative correction. A success-relative pairwise length reward further encourages efficient task completion. Experiments on ALFWorld and WebShop demonstrate consistent improvements across multiple model backbones. With Qwen2.5-3B, SCOPE achieves 97.7% success on ALFWorld and 85.2% on WebShop, outperforming SEED by 5.9 and 6.3 percentage points, respectively. On unseen ALFWorld tasks, SCOPE reaches 89.6% success, improving over GRPO by 23.2 percentage points with 46.7% fewer interactions. Scaling to Qwen3-32B, SCOPE achieves 99.2% success on seen ALFWorld tasks and 94.0% on unseen tasks.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-10-16.html">
          <span>October 16, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-15.html">
          <span>October 15, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-13.html">
          <span>October 13, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-12.html">
          <span>October 12, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-09.html">
          <span>October 09, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-08.html">
          <span>October 08, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-07.html">
          <span>October 07, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-05.html">
          <span>October 05, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-02.html">
          <span>October 02, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-01.html">
          <span>October 01, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-30.html">
          <span>September 30, 2026</span>
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
