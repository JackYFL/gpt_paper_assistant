

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
      <p class="eyebrow">Daily ArXiv / November 16, 2026</p>
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
      <strong>14</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>10.5</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="23 mentions">agent</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">agentic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">alone</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">annotation</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">answer</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="9 mentions">attention</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">auxiliary</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">behavior</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">brain</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">control</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">detection</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">diffusion</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">direct</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">error</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">future</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">gaussian</span><span class="cloud-word" style="font-size:2.26rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 74%, var(--accent))" title="17 mentions">generation</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">grounding</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="10 mentions">imitation</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">knowledge</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">label</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">multi-view</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">multimodal</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">object</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">path</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">perception</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">perform</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="9 mentions">policy</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">pose</span><span class="cloud-word" style="font-size:1.86rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="13 mentions">question</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">reasoning</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">reconstruction</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">region</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">relative</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">resource</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">same</span><span class="cloud-word" style="font-size:2.52rem;opacity:0.94;color:color-mix(in srgb, var(--accent-2) 87%, var(--accent))" title="20 mentions">semantic</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="10 mentions">spatial</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">structural</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">structure</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">supervision</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="6 mentions">support</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">transformation</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="7 mentions">video</span><span class="cloud-word" style="font-size:2.16rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 69%, var(--accent))" title="16 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="79 mentions">action</span><span class="cloud-word" style="font-size:2.49rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 86%, var(--accent))" title="146 mentions">agent</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="40 mentions">alignment</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="44 mentions">answer</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="38 mentions">attention</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="41 mentions">camera</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="38 mentions">change</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="49 mentions">control</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="52 mentions">detection</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="46 mentions">diffusion</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="35 mentions">domain</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="35 mentions">embedding</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="43 mentions">environment</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="43 mentions">error</span><span class="cloud-word" style="font-size:1.54rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="72 mentions">evidence</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="34 mentions">execution</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="36 mentions">foundation</span><span class="cloud-word" style="font-size:2.09rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 65%, var(--accent))" title="112 mentions">generation</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="34 mentions">generative</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="37 mentions">geometric</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="37 mentions">geometry</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="44 mentions">inference</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="48 mentions">interaction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="33 mentions">jointly</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="52 mentions">language</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="41 mentions">latent</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="65 mentions">memory</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="57 mentions">multimodal</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="40 mentions">multiple</span><span class="cloud-word" style="font-size:1.51rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="70 mentions">object</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="37 mentions">observation</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="35 mentions">perception</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="49 mentions">physical</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="61 mentions">point</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="54 mentions">policy</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="35 mentions">produce</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="49 mentions">prompt</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="47 mentions">question</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="74 mentions">reasoning</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="35 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="35 mentions">region</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="40 mentions">reward</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="56 mentions">same</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="65 mentions">scene</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="34 mentions">segmentation</span><span class="cloud-word" style="font-size:1.79rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="89 mentions">semantic</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="37 mentions">space</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="49 mentions">spatial</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="49 mentions">structure</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="37 mentions">supervision</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="53 mentions">support</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="37 mentions">target</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="53 mentions">token</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="41 mentions">trajectory</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="36 mentions">user</span><span class="cloud-word" style="font-size:1.98rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="103 mentions">video</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="36 mentions">view</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="44 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="173 mentions">visual</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="54 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>5 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">MLLM Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding</strong>
          <small>Haolin Yang, Wenshan Wu, Jin Jiang, Yu Cheng, Yan Xia, Ting Song, Yangyu Huang, Zhiliang Peng, Wenhui Wang, Hangbo Bao, Yuzhe Zhang, Wen-Da Wei, Tengchao Lv, Li Dong, Lei Cui, Furu Wei</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM Agents</span>
<span class="topic-tag">Visual Tool Use</span>
<span class="topic-tag">Multimodal Coding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2611.17797</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17797">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it proposes a new MLLM/VLM usage paradigm (Vision-as-a-Tool) and a unified multimodal agent framework.</p>
        <p class="abstract">Multimodal agentic coding requires robust visual reasoning to analyze observations and evaluate generated artifacts. Current frameworks largely rely on a Thinking-with-Images paradigm, where agents depend on their intrinsic vision to execute visually grounded tasks. However, this architectural coupling introduces a fundamental bottleneck. Agent performance remains strictly bounded by internal perceptual limitations. Furthermore, text-only agents lack native perception. Without specialized tools, they cannot perform visual reasoning. To overcome these constraints, we introduce the Vision-as-a-Tool (VaaT) paradigm. Prior visual tool-use merely manipulates images for an agent&#x27;s intrinsic vision to read. In contrast, VaaT reframes general-purpose multimodal large language models (MLLMs) as callable external utilities. As a result, text-only agents can completely offload visual reasoning during agentic execution. Meanwhile, vision-capable agents can dynamically augment their native perception on demand. We instantiate this paradigm in VHarness, a unified framework driven by five atomic actions. We comprehensively evaluate VHarness across Image-to-HTML, Image-to-SVG, and Image-to-3D generation tasks. Experimental results demonstrate that VHarness consistently improves visual fidelity and geometric accuracy across both text-only and multimodal coding agents. These findings highlight that modularizing visual reasoning into callable utilities provides a flexible and scalable foundation for future agentic coding systems.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Web Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents</strong>
          <small>Imene Kerboua, Fatemeh Pesaran Zadeh, Xing Han L\`u, Weijian Qi, Alexander Miller, Junyi Song, Yunjia Tian, Dongjin Kang, Seyeon Choi, Marzia Nouri, Ewen Gueguen, Matteo Boglioni, Fengyuan Liu, Zeyi Liao, Mengqi Yuan, Yue Li, Alexandre Lacoste, Alexandre Drouin, Spandana Gella, Huan Sun, Gunhee Kim, Siva Reddy</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Web Agents</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multimodal Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2611.17955</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17955">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3, and also fits criterion 2 in spirit: it introduces a new reproducible multimodal benchmark for web agents with audio/video observations and actions.</p>
        <p class="abstract">Web agents powered by large language and vision-language models are increasingly applied to realistic browser work that spans heterogeneous applications, multimodal content, and stateful workflows. However, existing reproducible web-agent benchmarks cover only a small number of web applications drawn from a few software categories, and restrict modality to text and vision. Live benchmarks broaden site coverage but sacrifice reproducibility, since pages and data drift between runs. Moreover, existing benchmarks do not meaningfully evaluate whether agents can understand and use audio and video content embedded within web tasks. To address these gaps, we introduce WebArena-Pro, a benchmark comprising 300 tasks across 20 self-hosted web applications in six domain categories, spanning distinct interface conventions, workflows, and data models. Across the evaluated agents, the best performance is achieved by both Codex with GPT 6.1 Sol and Claude Code with Claude Opus 5.5 at 62.3%, followed by OpenCode with Kimi 3.1 Pro at 60.7%. The strongest GenericAgent configurations, Gemini 3.1 Pro omni and Gemma4 31B, both achieve 30.3%. Among reproducible, human-curated web agent benchmarks, WebArena-Pro provides the broadest application coverage and the most comprehensive multimodal support to date. The benchmark treats audio and video as core observations alongside text and vision, with dedicated actions for extracting information from each. WebArena-Pro runs each task in isolation and supports reproducible, parallel evaluation. Tasks are authored through a dedicated annotator interface, filtered by LLM-assisted triage, and finally validated by humans before release. Project page: https://webarena-pro.github.io</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>OmniScore-Bench: Evaluating Vision-Language Models on Musical Score Reading</strong>
          <small>Congren Dai, Zhancheng Guo, Danni Zhao, Wenchu Wang, Xiaobing Li, Maosong Sun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Document Understanding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2611.17870</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17870">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: a benchmark for evaluating vision-language models on musical score reading, i.e. a new VLM evaluation setup.</p>
        <p class="abstract">Vision-language models (VLMs) can answer questions about musical scores, but their ability to recognise notation, recover its structure and interpret its musical meaning requires separate evaluation. Existing optical music recognition (OMR) resources establish detection and transcription measurements; a transcription score alone leaves the strengths and bottlenecks of a VLM score reader unresolved. We introduce OmniScore-Bench, an evaluation of OMR capabilities in VLMs through 3,000 questions spanning six aspects and 24 task subtypes. Each question specifies a visible scope, reference annotations and an answer schema, enabling automatic evaluation from symbol localisation to musical consistency and evidence-linked question answering. Our assessment of twelve VLMs reveals operation-specific capability profiles and different transcription leaders across excerpt, single-page and multipage tasks. Controlled analyses examine the roles of score images, auxiliary givens and additional page context. On the tested subset, image removal exposes visual dependence in pitch and repeat interpretation while measuring how much performance remains with public context alone. Separate format and content analyses distinguish answer-format violations from musical errors. OmniScore-Bench supports diagnosing which score-reading operations VLMs perform reliably and which require improvement.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multi-Agent RL</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Imitation Bootstrapped Multi-Agent Reinforcement Learning</strong>
          <small>Tony H. Zhang, Connor Mattson, Daniel S. Brown</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multi-Agent RL</span>
<span class="topic-tag">Imitation Learning</span>
<span class="topic-tag">Demonstration Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.MA</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2611.18543</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.18543">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new method for multi-agent reinforcement learning with demonstrations, though it is not specifically embodied/simulator-focused.</p>
        <p class="abstract">Demonstrations are an effective way to accelerate single-agent reinforcement learning (RL), but extending this idea to multi-agent reinforcement learning (MARL) is non-trivial as it is difficult and often impossible for a single person to teleoperate multiple agents simultaneously. Round-Robin Behavior Cloning (R2BC) addresses this by letting a single demonstrator control one agent at a time while the others execute their current policies. However, the resulting imitation policies are limited by the quality of the demonstrations. We propose Imitation Bootstrapped Multi-Agent Reinforcement Learning (IBMARL), a framework that extends Imitation Bootstrapped Reinforcement Learning (IBRL) to cooperative teams and uses R2BC to train the imitation policies. At each time step, every agent receives one action proposal from its imitation policy and one from its RL policy, and an ensemble of centralized critics selects among the per-agent combinations of the two. A gated imitation penalty, a soft Q-filtered behavior cloning loss, regularizes each RL policy toward its imitation policy only where the critics value the imitation action more, so that after training each agent executes its RL policy alone, without the centralized critics. On four cooperative multi-agent RL benchmarks, IBMARL surpasses its imitation policies $2.6$-$4.2\times$ faster than demonstration-based baselines on two tasks, is the only method to surpass it on the other two, and exceeds the demonstrator itself on two of the four. With real human demonstrations IBMARL still surpasses imitation learning alone, and does so more than twice as fast as the best baseline.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LLM Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination</strong>
          <small>Jie Huang, Yuecheng Hong, Yao Chen, Shengding Jiao, Xudong Liu, Qiang Ye</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LLM Agents</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Long-Horizon Planning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2611.17933</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17933">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only loosely: it is a new benchmark for long-horizon LLM agents, but not embodied AI or simulator-based.</p>
        <p class="abstract">In many long-horizon settings, an agent&#x27;s own choices create future constraints: committing finite capacity establishes future obligations and forecloses later opportunities. Sustaining performance therefore requires both keeping evolving plans feasible and comparing the value of resource allocations with the alternatives they displace. Recent benchmarks increasingly evaluate LLM agents in continuing operations, but give less attention to how agents keep their own commitments feasible while reassessing resource allocations as opportunities change. We introduce OutfitterBench, where agents manage an outdoor-equipment rental business for 200 days, purchasing from a 46-product catalog and handling roughly 1,100 reservation requests. Under a fixed capital ceiling, reservations and uncertain walk-in demand compete for reusable equipment whose availability changes over time. Experiments with seven frontier LLMs show that several agents underperform a simple rule-based baseline, while only the leading agent consistently surpasses it. Trajectory analysis shows that some agents apply known constraints inconsistently and make new decisions that conflict with existing commitments. Agents with more reliable fulfillment can still secure low returns from comparable commitments or delay resource reallocation. The leading agent better connects preparation with economic choices but also misses opportunities for more profitable asset use. These findings highlight limitations in sustaining coherent resource plans and reassessing their value over time. The benchmark code is publicly available at https://github.com/adminblackjack/OutfitterBench.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>14 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">3D Object Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>See and Detect: Image-Driven Open-Vocabulary Multi-View 3D Object Detection</strong>
          <small>Yating Xu, Na Zhao, Chenhan Jiang, Qingwen Zhang, Jiankang Deng, Jifei Song</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Object Detection</span>
<span class="topic-tag">Open-Vocabulary</span>
<span class="topic-tag">Multi-View Perception</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2611.17897</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17897">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it is an embodied/3D perception method with a new open-vocabulary multi-view 3D detection pipeline that uses images as the primary evidence, a novel angle compared with point-cloud-driven work.</p>
        <p class="abstract">Recent open-vocabulary multi-view indoor 3D detection methods typically follow a point-cloud-driven pipeline, where pseudo 3D boxes are generated from reconstructed or estimated geometry and semantic labels are inferred from projected regions. However, such a design makes box generation dependent on the completeness of point clouds and restricts semantic learning to local appearance, causing inferior 3D object localization and open-vocabulary classification. In this paper, we present See and Detect, an image-driven framework that uses multi-view images as the primary evidence for 3D box and semantic label generation. For box generation, we first discover object candidates from individual images, enabling objects missing in point clouds to be recovered from visual evidence. However, single-view predictions are often noisy and redundant. To address this, we propose multi-view consensus box consolidation to fuse spatially consistent predictions across views, and box quality assessment to reduce the impact of boxes with partial object coverage. For semantic label generation, we introduce context-aware semantic learning, where semantic labels are queried from full image context, enabling more accurate semantic prediction. Extensive experiments on ScanNet and ARKitScenes demonstrate that our method achieves state-of-the-art open-vocabulary multi-view 3D detection performance while running over 500$\times$ faster than the previous state-of-the-art method.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Unified Multimodal Models</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>Structural Self-Teaching for Compositional Generation in Unified Multimodal Models</strong>
          <small>Jaeyoo Park, Bohyung Han</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Unified Multimodal Models</span>
<span class="topic-tag">Compositional Generation</span>
<span class="topic-tag">Grounding Signals</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2611.18261</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.18261">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: this is a new unified multimodal model training method for compositional generation in UMMs, with internal grounding used as supervision.</p>
        <p class="abstract">We propose Structural Self-Teaching (SST), a novel framework that enhances compositional image generation in diffusion-based unified multimodal models (UMMs) by leveraging their internal understanding path as a source of structural supervision. The generation path of UMMs often struggles with dense compositional prompts, leading to missing objects, attribute binding failures, and spatial errors. In contrast, their understanding path localizes the same phrases in images that satisfy these prompts. SST converts this phrase-level grounding into training-time structural signals for the generation path. Specifically, we extract phrase-conditioned support masks from internal attention maps derived from the understanding path and employ them through two mechanisms. Phrase-local contrastive alignment uses these masks as pooling regions and aligns each generated phrase region with the same region of the target image. A structural scaffold builds a phrase-level layout from the same masks and modulates an intermediate spatial state of the generation path during training. The scaffold is phased out during training and removed at inference. SST requires no external structural annotations for training and no additional input at test time. Extensive experiments across multiple UMMs demonstrate that SST improves compositional fidelity over LoRA fine-tuning on the same data, with no inference-time cost. Project page is available at https://bellos1203.github.io/sst</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Text-to-Image Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>KnowVis: Dual-View Evaluation and Diagnosis of World-Knowledge Grounding in Text-to-Image Models</strong>
          <small>Yonghang Yu, Ruoyu Wang, Haoyu Zhang, Lin Qi, Yawei Zhou, Changqian Yu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Image Evaluation</span>
<span class="topic-tag">Benchmark &amp; Diagnosis</span>
<span class="topic-tag">World Knowledge Grounding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2611.18101</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.18101">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it builds a new benchmark/evaluation protocol for world-knowledge grounding in text-to-image models, which is directly tied to vision foundation models.</p>
        <p class="abstract">Text-to-image (T2I) models have made substantial progress in visual realism, aesthetic quality, and instruction following. However, real-world prompts often go beyond explicit visual descriptions and require implicit facts, structured knowledge, and domain-specific commonsense. Existing evaluations mainly focus on explicit prompt-to-image semantic alignment or specific knowledge subdomains, lacking unified evaluation and diagnosis of world-knowledge grounding in T2I models. We introduce KnowVis for dual-view evaluation and diagnosis of world-knowledge grounding in T2I generation. Built on a hierarchical knowledge taxonomy with case-level annotations, KnowVis combines two complementary benchmark views with a structured MLLM-based VQA judge protocol. The Skill-Tree Benchmark supports fine-grained atomic knowledge evaluation, while the Generalized Benchmark examines open-ended knowledge composition and expression. The protocol uses Required VQAs to assess atomic knowledge correctness in the Skill-Tree Benchmark, and combines Required, Optional, and dynamically discovered knowledge expressions with human-judge collaborative evaluation in the Generalized Benchmark. We validate the protocol&#x27;s reliability on the Skill-Tree validation split, enabling scalable evaluation and diagnostic error attribution. Experiments show that KnowVis reveals notable gaps in world-knowledge grounding across existing T2I models and provides structured diagnostic signals for knowledge-intensive image generation.</p>
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
          <strong>AmbiSteer: Selectively Eliciting Ambiguity-Aware Responses in Vision-Language Models</strong>
          <small>Monica Riedler, Samuele Antonelli, Barbara Plank, Raffaella Bernardi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Ambiguity Detection</span>
<span class="topic-tag">Activation Steering</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2611.17900</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17900">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: this is a VLM inference-time method for ambiguity-aware responses, directly probing and steering VLM behavior.</p>
        <p class="abstract">Vision-language models (VLMs) often exhibit overconfidence, providing firm answers even when visual evidence is insufficient. A prominent case is referential ambiguity in Visual Question Answering (VQA), where multiple entities in an image are plausible referents of a question. Addressing such cases requires recognizing when ambiguity is present: ambiguous questions can be handled by asking for clarification or enumerating plausible referents, while unambiguous questions should receive a direct answer. Current VLMs struggle with this distinction, often defaulting to a single interpretation. To investigate whether activation steering can serve as an inference-time mechanism to elicit such behaviors, we introduce AmbiSteer, a lightweight framework to selectively elicit ambiguity-aware behavior. Across three VLMs, we find that steering alone has limited and model-dependent effects, while prompting is generally more effective. Combining prompting and steering substantially increases clarification and enumeration behaviors, but also elicits them on unambiguous cases. AmbiSteer addresses this using a linear classifier to predict input ambiguity and condition the steering direction accordingly, increasing the proportion of inputs handled appropriately from 59.0% to 77.0% on average across models. Our work sets the ground for lightweight approaches to reduce model overconfidence in uncertain multimodal settings.</p>
      </div>
    </details>


    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>From Images to Grounded Edits: A Real-World Benchmark for Chinese Grammatical Error Correction in Handwritten Essays</strong>
          <small>Weiru Zhang, Yuzhong Hong, Junwei Bao, Lemao Liu, Dejing Dou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Grounded Editing</span>
<span class="topic-tag">Handwriting Understanding</span>
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
          <span>Paper 12 / arXiv:2611.17966</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17966">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 somewhat: a vision-language benchmark/workflow for grounded edits on handwritten essay images, which is a grounded VLM application.</p>
        <p class="abstract">Chinese Grammatical Error Correction (CGEC) is typically formulated as a text-to-text problem. While suitable for digital texts, this formulation falls short in real-world K-12 education, where AI-assisted corrections are expected directly on essay images, which are primarily handwritten and exhibit many irregularities. To bridge this gap, we introduce Grounded Chinese Grammatical Error Correction (G-CGEC), an image-to-grounded-edit task requiring systems to predict both corrections and their positions on essay images. We propose G-CGEC-Eval, a benchmark comprising real-world images of K-12 Chinese essays with fine-grained annotations. For evaluation, we adapt IoU-based metrics from object detection and propose a more tolerant alternative based on center-distance matching. Using this benchmark, we evaluate open-source and proprietary vision-language models under a direct single-pass setting, as well as settings with auxiliary components (OCR and character grounding) coordinated via pipelining or agentic harnessing. Results show that even top-tier proprietary models perform surprisingly poorly in the single-pass setting, while pipelining and agentic harnessing yield meaningful improvements. Notably, an error-type-based multi-agent workflow achieves the best performance, establishing it as the strongest baseline for future G-CGEC research. Through ablations and fine-grained analysis, we find the task remains far from solved, with linguistic error discovery and character-level grounding as the primary bottlenecks. This underscores the need for models that better integrate visual perception with linguistic reasoning and visual grounding.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Diffusion</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>JVT: Just Video Transformer makes pixel-space video diffusion simple</strong>
          <small>Jianjun Zhou, Hua Geng, Haoyu Guo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Diffusion</span>
<span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Multimodal Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2611.18549</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.18549">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it is a vision/generative modeling paper with a pixel-space video diffusion Transformer and multimodal camera-conditioned generation.</p>
        <p class="abstract">Direct diffusion modeling of high-dimensional raw video data is challenging, and existing pixel-space methods often rely on specialized architectures. We introduce JVT (Just Video Transformer), a simple large-patch DiT-style Transformer for pixel-space video diffusion, without a pretrained autoencoder, auxiliary detailers, cascaded stages, or U-Net-style skip connections. We systematically examine video patch embeddings, register tokens, and adaptive layer normalization to identify design choices that balance generation quality and computational efficiency. The resulting JVT design achieves generation quality competitive with latent diffusion baselines in both class-conditioned and unconditional settings. The pixel-space formulation of JVT also naturally supports joint generation of pixel-aligned modalities. We demonstrate this capability through camera-conditioned RGB-disparity generation, which improves camera following relative to RGB-only baselines and yields explicit scene geometry without an additional reconstruction model at inference. These results highlight the potential of simple DiT-style Transformers for pixel-space video diffusion, and we hope our findings offer useful insights and practical guidance for future research.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Collaborative Perception</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>RSSA: Robust Semantic and Spatial Aligner for Collaborative Perception</strong>
          <small>Zhihao Yang, Zhiyu Xiang, Peng Xu, Tianyu Pu, Kai Wang, Eryun Liu, Dongping Zhang, Yong Ding</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Collaborative Perception</span>
<span class="topic-tag">Spatial Alignment</span>
<span class="topic-tag">V2X Perception</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2611.18023</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.18023">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 moderately well: it improves spatial alignment for collaborative perception, which is a spatial understanding problem in embodied/agentic perception settings.</p>
        <p class="abstract">V2X collaborative perception improves single-vehicle perception by aggregating multi-view features from collaborative agents. However, existing methods typically rely on simple spatial warping to align the collaborative features, which can cause semantic misalignment during fusion. Meanwhile, these deterministic warping-based methods are highly sensitive to the positional noises. In this paper, we propose a plug-in module called Robust Semantic and Spatial Aligner (RSSA), which performs semantic and probabilistic spatial transformations for robust feature alignment. Specifically, a Semantic Transformation (SemT) block modulates feature channels based on the observed relative pose to correct semantic inconsistencies. Subsequently, a Probabilistic Spatial Transformation (P-SpaT) block performs probabilistic warping by sampling from the Gaussian-modeled relative pose space. A Relative Transformation Augmentation (RT-Aug) strategy is further introduced to augment the relative poses and facilitate the training of the RSSA. Extensive experiments on both simulated and real-world datasets demonstrate that RSSA improves the state-of-the-art methods by a large margin under the configuration of both clean and noisy positions.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Hand-Object Interaction</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>VACO: Vertex-Aligned Decoding for Dense Hand Contact Estimation from a Single Image</strong>
          <small>Binhong Ye, Jin-Chuan Shi, Tao Liu, Xin Wang, Hao Chen, Chunhua Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Hand-Object Interaction</span>
<span class="topic-tag">Dense Perception</span>
<span class="topic-tag">Embodied Manipulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2611.17755</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17755">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: embodied manipulation-related vision method for dense hand contact estimation from a single image, relevant to spatial understanding for interaction analysis.</p>
        <p class="abstract">Dense hand contact estimation from a single RGB image is a foundational primitive for dexterous manipulation and 3D interaction analysis. Direct predictors typically decode the entire per-vertex contact map from one shared query, leaving individual vertices ungrounded in the image and smearing contact across adjacent, non-touching surfaces. We present VACO, a vertex-aligned decoder in which each MANO vertex samples local image features at its projected location. A hand-reconstruction backbone, jointly trained for reconstruction and contact, predicts these locations at inference without an auxiliary reconstructor. Training uses noise-perturbed ground-truth projections and end-to-end feature adaptation to improve robustness and contact-sensitive features. A single VACO checkpoint sets a new state of the art on five benchmarks spanning hand-object, hand-human, hand-scene, and bimanual interactions. It improves F1 by +20.7 pp over the strongest prior direct predictor on Hi4D and generalizes to the held-out HOT3D and HOCap, with gains of +5.5 and +2.7 pp. The resulting contact predictions also improve downstream HOI reconstruction.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Robotic Perception</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>Real-Time Diffusion Relighting as a Neural Sensor: Closing the Low-Light Domain Gap for Robotic Perception</strong>
          <small>Shengjie Xu, Alexander Gao, Anshul Rai, Dae Yeol Lee, Guan-Ming Su, Ming C. Lin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Robotic Perception</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Simulation / CARLA</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2611.17438</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17438">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 and 4 partially: it integrates a generative diffusion model into robotic perception and validates on a simulator task, but the main contribution is low-light perception rather than a new embodied benchmark.</p>
        <p class="abstract">Low-light conditions severely degrade robotic perception: object detectors trained on daylight imagery are prone to failure under dark and adverse weather conditions that fall outside of their training distribution. Furthermore, from an efficiency standpoint, existing Low-Light Image Enhancement (LLIE) methods are designed for offline processing and are therefore impractical to integrate into live control loops. To address these issues, we propose to embed a Generative Neural Sensor within the control loop that treats illumination as a generative prior rather than a signal processing problem, enabling task-relevant semantic recovery. We further propose an Real-Time Perceptual Architecture that decouples high-latency semantic recovery from low-latency robotic control. Rather than blocking the control loop, our system runs a large-scale image-to-image diffusion model in a background thread, and is activated only when a drop in detection confidence signals a perceptual uncertainty event, significantly reducing computational overhead. Our method sets a new state-of-the-art performance on the ExDark low-light benchmark with 87.1% mAP, and under adverse weather conditions, significantly boosts detection rates over competing methods. On a navigation task in a closed-loop autonomous driving simulator (CARLA), we achieve a 100% lap completion rate, establishing a simulation-based proof-of-concept for integrating high-latency generative models with standard robotic control autonomy stacks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Generative Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Vessel2Brain: Edge-Aware Multi-Scale Flow Matching for 3D Brain Image Generation from Vessel Masks</strong>
          <small>Zhi Chen, Tianyang Zhang, Theodoros N. Arvanitis, Le Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Medical Imaging</span>
<span class="topic-tag">Conditional Flow Matching</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2611.17919</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17919">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: vision foundation/generative modeling style application, using conditional flow matching for 3D brain image generation.</p>
        <p class="abstract">Generating realistic 3D brain MRI volumes from sparse anatomical priors is a highly ill-posed yet clinically valuable problem, with important applications in data augmentation, simulation, and downstream neuroimaging analysis. In this work, we investigate the challenging task of synthesising full 3D brain MRI volumes conditioned solely on vascular label maps. While vascular structures provide strong anatomical and topological cues, they occupy only a small fraction of the brain volume and offer no direct information about surrounding tissue appearance. To address this challenge, we propose Vessel2Brain, an edge-aware multi-scale conditional flow matching framework that explicitly incorporates vascular structure information into the generative process. Our approach formulates vessel-guided brain image synthesis as a conditional continuous flow, enabling stable training and flexible generation while preserving structural correspondence. A multi-scale flow matching strategy is introduced to jointly model global anatomical coherence and fine-grained local details, with auxiliary velocity predictions providing additional supervision across spatial resolutions. Furthermore, we design an edge-aware objective that emphasises vascular boundaries during training, encouraging anatomically faithful tissue synthesis around vessel structures. We evaluate Vessel2Brain on two public 3D brain MRI datasets with paired vascular annotations. Extensive quantitative and qualitative experiments demonstrate that our method consistently outperforms state-of-the-art generative models in terms of reconstruction accuracy, structural consistency, and distributional realism.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical VQA</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>QCAP-VQA: Question-Conditioned Capped Prior-Mass Supervision for Medical Visual Question Answering</strong>
          <small>Yining Zhao, Catarina Moreira, Mukesh Prasad, Ali Braytee</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical VQA</span>
<span class="topic-tag">Spatial Grounding</span>
<span class="topic-tag">Attention Supervision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2611.17708</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17708">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 in a narrow way: it studies spatial supervision/attention grounding in medical VQA, but it is not about embodied agents or general spatial intelligence.</p>
        <p class="abstract">Medical visual question answering models can answer correctly without attending to the anatomy that the question names. Automatic region priors allow spatial supervision without expert masks, but they are noisy, and it is unclear how strongly they should shape attention and how their effect should be verified. We present QCAP-VQA, which supervises a subset of cross-attention heads with a question-conditioned prior built from ranked segmentation proposals. Its capped prior-mass objective penalizes insufficient attention inside the prior only below a threshold. We evaluate attention against SLAKE structure boxes that play no role in training, separating attention on the named anatomy from how attention shifts between questions about the same image. QCAP-VQA matches the accuracy of a baseline without spatial supervision (84.26% vs. 84.23%), and every evaluated prior-supervised model places more attention on the annotated structures. Over a 64-fold range of regularization strength, the capped objective keeps prior mass between 0.67 and 0.77, whereas a pooled region-mass objective drives it to 0.97 and loses accuracy. The cost lies in question conditioning: as the constraint widens or strengthens, attention shifts agree less with the expert-defined contrast. Across 13 configurations, prior-referenced and expert-referenced evaluation rank the models in largely opposite order (Spearman correlation of -0.87), and the capped models it favors track the prior&#x27;s own errors. Because clinical use of medical visual question answering requires answers grounded in the queried anatomy, supervision from automatic priors should be judged against independent anatomical references.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Reconstruction</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>Stage-wise Lineage-aware Dropout for Sparse-View 3D Gaussian Splatting</strong>
          <small>Yan Xing, Zhi Chen, Fanglue Zhang, Junhong Zhao, Bing Xue, Mengjie Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Gaussian Splatting</span>
<span class="topic-tag">Sparse-View Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2611.17752</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.17752">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 only indirectly: vision-based 3D reconstruction for sparse-view Gaussian splatting, a vision foundation-model-adjacent representation method.</p>
        <p class="abstract">Sparse-view 3D Gaussian Splatting (3DGS) is prone to overfitting because only a limited number of images are available to constrain scene geometry. Dropout is one regularization strategy for alleviating this problem. We introduce the concept of a lineage family to describe a set of Gaussian primitives derived from the same founder through cloning or splitting operations. The founder Gaussians refer to all Gaussian primitives generated during initialization. Descendants within the same family often jointly contribute to the refinement of adjacent local regions. However, dropping individual Gaussians can be less effective due to the compensation effect from neighboring Gaussians for the dropped ones. To address this issue, we propose Stage-wise Lineage-aware Dropout(SLD), which applies lineage-family dropout during the structural regularization stage and switches to individual dropout during the later refinement stage. We further propose Lineage-Balanced Densification(LBD), which operates during densification by constructing an expanded candidate pool and reallocating the densification budget according to the mean gradient scores and existing descendant sizes of different families. Experiments on the LLFF, MipNeRF360, and Blender datasets show that the proposed framework achieves competitive performance in sparse-view reconstruction</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Sign Language Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>SemRAG: Semantic-Guided Sentence-Level Retrieval-Augmented Sign Language Production</strong>
          <small>Xiao Liu, Shiwei Gan, Yafeng Yin, Peishuo Liu, Bowen Guo, Kuizhuang Liu, Cong Wang, Lei Xie</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Sign Language Generation</span>
<span class="topic-tag">Retrieval Augmentation</span>
<span class="topic-tag">Sequence Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2611.18189</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.18189">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; it is a retrieval-augmented sign language production method, which is multimodal but not one of the requested categories.</p>
        <p class="abstract">Sign language production (SLP) aims to generate sign pose sequences that faithfully express spoken-language text while preserving the rhythm and coordination patterns of signing. Common SLP methods learn text-to-pose mappings from training data but often suffer from semantic inaccuracies in long or complex sentences. Retrieval augmentation offers a way to introduce realistic signing priors to provide more explicit guidance for text-to-pose generation. However, existing retrieval-based SLP methods typically operate at the gloss or word level, relying on gloss-pose dictionaries or isolated sign segments that require costly annotations and fail to preserve continuous sentence-level dynamics. To bridge this gap, we propose SemRAG, a semantic-guided sentence-level retrieval-augmented framework that retrieves full-sentence signing templates as priors without constructing gloss/word-level sign dictionaries. While such templates preserve local motion patterns and global rhythm, they also introduce a semantic mismatch problem: irrelevant motions in the retrieved sentence may interfere with the target semantics. To address this issue, we introduce an SLT-guided template semantic localization module that identifies target-relevant temporal regions within the retrieved template while suppressing irrelevant signing content. To adaptively incorporate the template features into the generator, we further introduce layer-specific learnable gates that regulate their contribution across generator layers. Extensive experiments show that SemRAG improves semantic consistency and motion quality over baselines under both back-translation and motion accuracy metrics.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">6DoF Tracking</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>Toward On-Device Markerless 6DoF Tracking of a Physical Manipulative on a Mixed-Reality Headset: A Preliminary Study</strong>
          <small>Guangxi Feng, Philip Yasskin, Wei Yan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">6DoF Tracking</span>
<span class="topic-tag">Mixed Reality</span>
<span class="topic-tag">Pose Estimation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.HC</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2611.18438</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.18438">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>3</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 somewhat: it is an embodied/AR spatial tracking system for 6DoF pose estimation on a headset, but it is a preliminary application rather than a benchmark or major new method.</p>
        <p class="abstract">AR-Classroom uses physical models and virtual overlays to help learners explore spatial transformations. To align these overlays on a standalone headset, we developed a markerless six-degree-of-freedom(6DoF) tracker for a LEGO airplane on the Meta Quest 3. A compact YOLO model trained on synthetic Unity renders predicts 20 keypoints from dynamic RGB crops resized to 128 by 128 pixels. A perspective-n-point solver estimates the airplane&#x27;s pose from these predictions and the corresponding 3D landmarks. In a paired evaluation on 1,000 synthetic validation images, cropping guided by ground-truth boxes increased the detection rate on annotated images from 32.5 to 46.2 percent. Mean keypoint F1 increased from 42.9 to 44.6 percent, with lower keypoint precision in the cropped view. In preliminary headset tests, 2 Hz was the highest tested tracking target at which the application maintained approximately 72 frames per second. A headset demonstration illustrates virtual overlay alignment with the physical airplane before and after a manual rotation. Quantitative 6DoF pose accuracy on real headset footage will be measured in future work.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-10-16.html">
          <span>October 16, 2026</span>
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
