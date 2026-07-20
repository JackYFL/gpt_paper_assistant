

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
      <p class="eyebrow">Daily ArXiv / July 20, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>15</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">action</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">assessment</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="6 mentions">capture</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="6 mentions">challenging</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">consistency</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">construct</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">critical</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">device</span><span class="cloud-word" style="font-size:1.90rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="7 mentions">estimation</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="6 mentions">event</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">evolution</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">expert</span><span class="cloud-word" style="font-size:1.90rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="7 mentions">geometric</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">language</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">long-term</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">meme</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">merging</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">mllm</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">mobile</span><span class="cloud-word" style="font-size:1.90rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="7 mentions">motion</span><span class="cloud-word" style="font-size:2.21rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 71%, var(--accent))" title="8 mentions">multiple</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">natural</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">object</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">perception</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">point</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">pose</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">preserve</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">query</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="6 mentions">real-time</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">reasoning</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="6 mentions">recognition</span><span class="cloud-word" style="font-size:2.50rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 86%, var(--accent))" title="9 mentions">reconstruction</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">reduce</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="6 mentions">reduction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">region</span><span class="cloud-word" style="font-size:1.90rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="7 mentions">risk</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">safety</span><span class="cloud-word" style="font-size:2.50rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 86%, var(--accent))" title="9 mentions">semantic</span><span class="cloud-word" style="font-size:2.21rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 71%, var(--accent))" title="8 mentions">temporal</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="10 mentions">token</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">tracking</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">trajectory</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="6 mentions">unified</span><span class="cloud-word" style="font-size:2.21rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 71%, var(--accent))" title="8 mentions">visual</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="5 mentions">zero-shot</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="89 mentions">action</span><span class="cloud-word" style="font-size:1.71rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 46%, var(--accent))" title="140 mentions">agent</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="72 mentions">alignment</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="52 mentions">attention</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">camera</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">concept</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="66 mentions">consistency</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">dense</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="72 mentions">detection</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="58 mentions">diffusion</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="64 mentions">domain</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="105 mentions">dynamic</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">environment</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="72 mentions">event</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="81 mentions">evidence</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="71 mentions">fine-grained</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="66 mentions">foundation</span><span class="cloud-word" style="font-size:2.09rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 65%, var(--accent))" title="191 mentions">generation</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="68 mentions">geometric</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="58 mentions">geometry</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="65 mentions">inference</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">interaction</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="110 mentions">language</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">latent</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">mechanism</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="67 mentions">memory</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="111 mentions">motion</span><span class="cloud-word" style="font-size:1.64rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="131 mentions">multimodal</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">multiple</span><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="121 mentions">object</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="55 mentions">paradigm</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="62 mentions">perception</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="60 mentions">physical</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="89 mentions">pipeline</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">pose</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="52 mentions">query</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="83 mentions">real-world</span><span class="cloud-word" style="font-size:1.85rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 53%, var(--accent))" title="157 mentions">reasoning</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="89 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">region</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="52 mentions">reward</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="51 mentions">robust</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="145 mentions">scene</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="61 mentions">segmentation</span><span class="cloud-word" style="font-size:1.87rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="160 mentions">semantic</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="70 mentions">space</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="127 mentions">spatial</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="55 mentions">support</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="68 mentions">target</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="99 mentions">temporal</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="101 mentions">token</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="63 mentions">trajectory</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="87 mentions">understanding</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="82 mentions">unified</span><span class="cloud-word" style="font-size:2.58rem;opacity:0.95;color:color-mix(in srgb, var(--accent-2) 90%, var(--accent))" title="268 mentions">video</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">view</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">vision</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="69 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="302 mentions">visual</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="94 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>13 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Model</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>GeoChrono: Benchmarking and Rethinking Long-Term Temporal Understanding in Remote Sensing</strong>
          <small>Yujie Li, Jiancheng Pan, Zhiwei Wei, Jiuniu Wang, Mugen Peng, Wenjia Xu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Model</span>
<span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
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
          <span>Paper 1 / arXiv:2607.15768</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15768">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: this is a remote-sensing MLLM benchmark plus a new model for long-term temporal and spatio-temporal understanding.</p>
        <p class="abstract">Remote sensing offers an unparalleled vantage point for observing the Earth&#x27;s long-term surface evolution, yet it demands that a model not only perceive land cover at isolated moments, but also track changes, memorize evolution histories, and reason across time and space. However, existing studies lack a systematic evaluation that dissects these distinct competencies. To fill this gap, we introduce ChronoBench, a multidimensional benchmark that decomposes this task into four progressive cognitive levels (i.e., Land Cover Perception, Temporal Recognition, Long-Term Memory, and Spatio-Temporal Reasoning). The ChronoBench comprises 12 sub-tasks and 17,689 rigorously validated QA (Question-Answer) pairs. Extensive evaluations reveal that mainstream MLLMs fall drastically behind human experts, with Long-Term Memory emerging as the most critical bottleneck. Motivated by this finding, we further propose GeoChrono, an MLLM with enhanced capabilities for tracing, memorizing, and reasoning about long-term geographic evolution. Leveraging the physical prior that geographic parcels remain spatially fixed while their semantics evolve, we design a Temporal Trajectory Encoder~(TempEnc) that constructs per-location temporal trajectories for dedicated land cover evolution modeling, and we introduce a Coarse-to-Fine Token Compressor~(C2FComp) that adaptively preserves dynamic regions while compressing the static background. To support training, we also construct ChronoInstruct, a 104K-sample instruction-tuning dataset spanning all competency levels for training. GeoChrono achieves state-of-the-art performance on ChronoBench, surpassing the leading commercial MLLMs by over 20%, while C2FComp reduces visual tokens by over 56% while retaining GeoChrono&#x27;s 94.6% performance. The code and data will be available at https://github.com/IntelliSensing/GeoChrono</p>
      </div>
    </details>


    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>When Can Test-Time Adaptation Help Zero-Shot CT Vision-Language Models?</strong>
          <small>Ailar Mahdizadeh, Puria Azadi Moghadam, Xiangteng He, Leonid Sigal</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Model</span>
<span class="topic-tag">Test-Time Adaptation</span>
<span class="topic-tag">Medical Imaging</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2607.15556</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15556">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and somewhat criterion 4: it studies test-time adaptation for zero-shot 3D CT vision-language models and proposes a cardinality-aware method.</p>
        <p class="abstract">3D CT vision-language models (VLMs) classify abnormalities from text prompts in a zero-shot manner, enabling cross-institution deployment where labels are scarce and clinical tasks shift faster than supervised models can be retrained. A real CT scan, however, typically contains several co-occurring abnormalities, and the reliability of zero-shot multi-label prediction under distribution shift remains poorly understood. Test-time adaptation (TTA) updates a model on unlabeled target scans without source data or target annotations, yet existing TTA methods target multi-class softmax prediction on natural images or 2D medical segmentation, and none addresses unsupervised multi-label adaptation for zero-shot 3D CT VLMs. We study when TTA helps zero-shot 3D CT VLMs. A controlled diagnostic analysis shows that TTA is conditional: the volumetric input must preserve the encoder&#x27;s depth structure, and the base representation must transfer to the target cohort, with depth reduction alone lowering internal AUROC by more than 0.12. We then focus on the regime where the base model already separates present from absent abnormalities. We introduce CARVE (Cardinality-Aware Retained-View Entropy), the first TTA method for this setting. CARVE estimates a sample-specific positive-label cardinality $\hat{k}$, optimizes a top-$\hat{k}$ objective to preserve co-occurring abnormalities, and performs memory-efficient multi-view adaptation by scoring weak 3D views without gradients before updating on a retained subset. Across contrastive CT-CLIP and anatomy-aware fVLM, CARVE provides the most consistent improvements across multi-label, three-class, and binary CT tasks when the base model is already discriminative. These results establish multi-label TTA for zero-shot 3D CT VLMs as a distinct problem and CARVE as a cardinality-aware solution.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal LLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>Reasoning-Guided Part-Level Visual Grounding via Reinforcement Learning</strong>
          <small>Kazi Sajeed Mehrab, Hani Alomari, Najibul Haque Sarker, Chia-Wei Tang, Zaber Ibn Abdul Hakim, Anuj Karpatne, Chris Thomas</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Referring Grounding</span>
<span class="topic-tag">Reinforcement Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2607.15374</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15374">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Criterion 2 matches closely: this is a new MLLM-based reasoning-guided grounding method with hierarchical coarse-to-fine localization and RL training.</p>
        <p class="abstract">Multimodal large language models (MLLMs) ground whole objects well from free-form language queries, but they struggle when the query names a part rather than the object. We trace this to a missing object-part hierarchy, since parts are localized in the same single step used for objects. We propose Object-Part Hierarchical Reflective Grounding (OP-HRG), a coarse-to-fine reasoning-guided grounding strategy that first localizes the parent object and then the part within it. A self-check then reflects on the result, with an extension to re-encode the predicted crop to inspect the region it is correcting. We introduce a part-aware GRPO framework to train our pipeline with stage-wise rewards. A 4B model trained this way outperforms 7B grounding LLMs and SAM3 across PascalPart, PartImageNet, and InstructPart, and transfers to reasoning segmentation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>EgoExoMoCap: Distributed Ego-Exo Human Motion Capture</strong>
          <small>Jiaxi Jiang, Bharat Lal Bhatnagar, Nan Yang, Lingni Ma, Sebastian Starke, Robin Kips, Nadine Bertsch, Christian Holz, Federica Bogo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Motion Capture</span>
<span class="topic-tag">Egocentric Vision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.GR</span>
<span class="category-tag">cs.HC</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2607.15868</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15868">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Criterion 3 matches closely: this is an embodied-AI-relevant motion capture method with a novel distributed ego-exo setup and a new in-the-wild capture paradigm.</p>
        <p class="abstract">Human motion capture from head-mounted devices (HMDs) offers a scalable way to acquire real-world human motion and interaction data, which is crucial for applications in embodied AI and VR/AR. Existing approaches focus on either egocentric body tracking, estimating the motion of the subject wearing the device, or exocentric tracking, capturing the movements of people in the wearer&#x27;s surroundings. So far, these two paradigms have largely been explored in isolation. In this paper, we propose a novel distributed framework that jointly leverages ego- and exocentric multi-modal signals for human motion estimation from HMDs. Unlike traditional motion capture systems requiring bulky multi-camera setups or obtrusive mocap suits, our approach, EgoExoMoCap, is as simple as two (or more) people, each wearing a pair of smart glasses. The method leverages head (plus potentially wrist) tracking signals for accurate estimation of global motion in the 3D world and combines context-aware image features based on DINOv3 to achieve robustness in the presence of noise and occlusions. Extensive experiments on two in-the-wild datasets show that our approach can robustly reconstruct motion even in challenging scenarios.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Gaussian Splatting</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>E3DGS: Unified Geometric-Photometric Equivariance for 3D Gaussian Splatting via Color-as-Geometry Embedding</strong>
          <small>Chankyo Kim, Maani Ghaffari</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Gaussian Splatting</span>
<span class="topic-tag">Equivariant Vision</span>
<span class="topic-tag">World Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2607.15536</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15536">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a vision foundation model-style geometric formulation for 3D Gaussian Splatting with equivariance and action-conditioned world modeling applications.</p>
        <p class="abstract">3D Gaussian Splatting (3DGS) captures scenes by coupling explicit geometry (position, covariance) with view-dependent photometry (Spherical Harmonics). However, building $\mathrm{SE}(3)$-equivariant architectures on these primitives presents a fundamental representation bottleneck. Color has been treated as a signal rather than a geometric entity, making it nontrivial to unify symmetry across geometry and appearance as the camera frame changes. While translations are handled by relative coordinates, rotations act heterogeneously across attributes: $\mu\mapsto R\mu$, $\Sigma\mapsto R\Sigma R^\top$, and $f_\ell\mapsto D^\ell(R)f_\ell$. This mismatch complicates strict equivariance, leading existing methods to either discard or flatten SH coefficients, thereby breaking symmetry. We propose a unified solution rooted in representation theory: for SH degrees $\ell\le2$, photometry is algebraically isomorphic to a rank-2 geometric tensor. We prove that the Wigner-$D$ action on these SH coefficients can be exactly reformulated as the conjugation action on $3\times3$ matrices. Leveraging this, we introduce the Unified Matrix Embedding, a lifting that maps all Gaussian attributes into a unified carrier space, $\mathfrak{gl}(3)$. Building on the &quot;Color-as-Geometry&quot; formulation, we present E3DGS, a rigid-body ($\mathrm{SE}(3)$) equivariant architecture that processes 3D Gaussians without Clebsch-Gordan tensor products. Evaluations on object vision and action-conditioned Gaussian world modeling demonstrate that our unified approach yields strong robustness under camera-frame changes and improved data efficiency.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Geo-localization</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Trajectory-aware Cross-view Geo-localization with Sequential Observations</strong>
          <small>Tianyi Gao, Jiayu Lin, Danielle Beaulieu, Nathan Jacobs</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Geo-localization</span>
<span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Multimodal Benchmark</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2607.15491</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15491">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 3 closely: it introduces trajectory-aware cross-view geo-localization and a new dataset/framework for sequential observations with spatially-aware representations.</p>
        <p class="abstract">Cross-view geo-localization matches ground-level observations against geo-tagged satellite imagery. Recent methods show that sequential queries such as video clips yield richer spatiotemporal cues than single images, yet they overlook a complementary sequential modality: route descriptions -- which capture the same trajectory at a higher level of abstraction and are often the only input available (e.g., a user directing an autonomous vehicle to a pickup point). To bridge this gap, we introduce SeqGeo-VL, a dataset of $\sim$39K video-text-satellite triplets, and TrajLoc, a unified framework capable of processing both video clips and route descriptions. By leveraging both dense visual and abstract linguistic semantics, TrajLoc enables these modalities to mutually reinforce cross-view matching. We further propose TrajMod, a lightweight module that conditions query embeddings on trajectory geometry, yielding spatially-aware representations. Experiments show that TrajLoc achieves substantial gains over state-of-the-art methods on both video and text geo-localization. The project page is available at https://humblegamer.github.io/trajloc/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Semantic Communication</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Toward Semantic Communication for Real-time Mobile 3D Reconstruction</strong>
          <small>Fangzhou Zhao, Yao Sun, Xuesong Liu, Runze Cheng, Shang Kai, Yi Sun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Semantic Communication</span>
<span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Pose Estimation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.MA</span>
<span class="category-tag">cs.MM</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2607.16128</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.16128">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Criterion 3 matches closely: it is a new method for real-time mobile 3D reconstruction with semantic communication and confidence-guided geometry estimation, a novel embodied/robotics-relevant angle that prior work often ignores.</p>
        <p class="abstract">Real-time mobile 3D reconstruction is fundamental to many emerging applications such as autonomous navigation and digital twin construction, where a moving platform continuously captures an image stream and transmit to a computing server for scene understanding. Unlike offline reconstruction, camera poses and scene geometry are estimated on-the-fly during acquisition, making multi-view consistency a real-time requirement and rendering geometric estimation highly sensitive to communication-induced distortions. Semantic communication (SemCom) transmits compact semantic information, offering a promising way to preserve task-critical data over unreliable links. However, existing designs are optimized at the image or single-view level and without providing explicit reliability information for geometric estimation, limiting their applicability to real-time mobile 3D reconstruction. In this context, we propose a SemCom framework for real-time mobile 3D reconstruction. The framework includes a semantic transceiver that outputs a reconstructed image alongside a pixel-wise confidence map, quantifying the reliability of each region. We further introduce a confidence-guided geometric estimation method, incorporating confidence into RANSAC-based pose initialization and bundle adjustment to reduce the influence of unreliable regions and enhance robustness under noisy channels. Simulations show that, compared to existing SemCom and traditional seperate source and channel coding, our framework maintains high image quality while significantly improving pose estimation accuracy and 3D structural consistency.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Model Merging for Medical LVLMs: A Benchmark and a Winner-Take-All Approach</strong>
          <small>Lichao Mou, Shilan Zhang, Chunlei Li, Bingcong Yan, Jingliang Hu, Yilei Shi, Shengwu Xiong, Xiao Xiang Zhu, Lei Li, Yaxiong Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Vision-Language Models</span>
<span class="topic-tag">Model Merging</span>
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
          <span>Paper 8 / arXiv:2607.15661</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15661">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 4 closely: it is a benchmark and method for merging medical LVLMs, directly about vision-language models.</p>
        <p class="abstract">Large vision-language models (LVLMs) can be adapted to specialized medical imaging tasks via parameter-efficient fine-tuning approaches such as low-rank adaptation (LoRA), leading to a growing ecosystem of expert models tailored to specific imaging modalities and clinical scenarios. However, deploying multiple expert LVLMs in practice incurs substantial computational and operational overhead. Model merging provides a promising solution by consolidating multiple experts into a single model without retraining, yet it remains largely unexplored in the medical domain. In this work, we present the first systematic study of model merging for medical LVLMs. We introduce MergeMedBench, a comprehensive benchmark spanning eight imaging modalities and diverse clinical task types, comprising 16 LoRA fine-tuned models built upon two mainstream architectures. We conduct an extensive evaluation of existing merging methods and further propose winner-take-all, a simple and hyperparameter-free approach that retains only the most dominant parameters across expert models. By preserving the critical parameters that govern model behavior and discarding weaker ones, our method avoids the information dilution inherent in averaging- or alignment-based strategies. Despite its simplicity, winner-take-all consistently outperforms existing approaches, offering both a new perspective on LoRA merging and a strong practical baseline for future research.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Event Cameras</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation</strong>
          <small>Jian Huang, Haotian Shen, Xinhao Lou, Chengrui Dong, Wenpu Li, Peidong Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Event Cameras</span>
<span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Embodied Perception</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2607.15727</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15727">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied-perception/3D reconstruction method with a new event-camera reconstruction framework and a self-supervised pretraining strategy for a previously underexplored sensor setting.</p>
        <p class="abstract">Robust 3D reconstruction is essential for robotics and embodied perception. Recent feed-forward approaches such as DUSt3R have demonstrated impressive progress in dense 3D reconstruction from RGB images, achieving global geometric consistency and strong generalization. However, extending such dense 3D reconstruction to event cameras remains challenging due to their asynchronous, sparse, and highly dynamic nature, as well as the lack of large-scale, well-labeled datasets. In this work, we introduce Event3R, a feed-forward framework that directly maps asynchronous event streams to globally consistent 3D point clouds. Event3R represents incoming events as spatial-temporal voxels, enabling time-aware feature integration through a temporal attention module that enhances the module&#x27;s temporal feature learning. To further strengthen temporal representation learning and reduce reliance on labeled data, we propose a Masked Bin Modeling (MBM) strategy for self-supervised pre-training, enabling robust temporal representation learning with minimal labeled data, and retain it as an auxiliary fine-tuning objective. In addition, contrastive alignment and consistency regularization losses are incorporated during fine-tuning to reinforce structural correspondence and temporal coherence across views. Extensive experiments on both synthetic and real-world benchmarks demonstrate that Event3R achieves robust, temporally consistent, and globally aligned 3D reconstructions, significantly outperforming existing event-based methods.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Visual Place Recognition</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>Are All Tokens Necessary for Visual Place Recognition? An Empirical Study of Token Reduction for Efficient Inference</strong>
          <small>Tong Jin, Yunpeng Liu, Shuyu Hu, Qinghua Zhang, Ruize Han, Song Wang, Feng Lu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Visual Place Recognition</span>
<span class="topic-tag">Token Pruning</span>
<span class="topic-tag">Efficiency Benchmark</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2607.15563</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15563">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a benchmark study on token reduction for visual place recognition using vision transformer foundation models, with practical efficiency insights.</p>
        <p class="abstract">Recent visual place recognition (VPR) methods based on vision transformers, particularly foundation models, have achieved remarkable recognition performance. However, these models process all visual tokens throughout the entire network, resulting in substantial computational overhead, which hinders their deployment in real-time and resource-constrained scenarios. A natural question thus arises: are all visual tokens necessary for VPR? To answer this question, we present the first systematic benchmark of token reduction for efficient visual place recognition. Our benchmark comprehensively evaluates representative token pruning, token merging, and hybrid pruning-merging methods across multiple state-of-the-art VPR models and diverse benchmark datasets covering urban, suburban, and natural environments. We further investigate token reduction from multiple perspectives, including recognition performance under different reduction configurations, computational complexity, inference speed, qualitative visualization, and deployment efficiency on edge devices. Through extensive experiments and in-depth analysis, our benchmark reveals multiple important characteristics of token reduction in VPR and provides several practical insights into the trade-offs between accuracy and inference efficiency. For example, token reduction can reduce computational cost by up to 29\% and improve throughput by up to 44\%, while incurring less than 1\% degradation in recognition accuracy. Overall, this work establishes a comprehensive foundation for future research on token-efficient VPR and efficient visual retrieval systems. Our codes and models will be available at https://github.com/Tong-Jin01/TokenReduction4VPR</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Bundle Adjustment</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>CSS-BA: Gate-Guided Column Space Search for Bundle Adjustment</strong>
          <small>Ayano Kaneda, Takafumi Taketomi, Shugo Yamaguchi, Shigeo Morishima</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Bundle Adjustment</span>
<span class="topic-tag">3D Vision</span>
<span class="topic-tag">Optimization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2607.15652</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15652">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Criterion 3 matches loosely: it is a new solver-side bundle-adjustment method for weak-geometry reconstruction, but it is not a benchmark or embodied-AI-specific paper.</p>
        <p class="abstract">Bundle adjustment (BA) remains a critical refinement module for image-based 3D reconstruction and continues to improve geometric accuracy even in learning-based pipelines. However, in low-parallax and near-rotational regimes, classical Schur-based Levenberg--Marquardt (LM) often becomes ill-conditioned and yields unreliable pose and calibration estimates. We propose Gate-Guided CSS-BA, a solver-side modification of Schur-LM that preserves the classical BA objective and trust-region framework while constraining each update to a geometrically informed low-dimensional subspace. By integrating Column Space Search (CSS) with geometry-aware gating, the method stabilizes the Schur-LM update without altering the estimation problem. In contrast to keyframe or state-selection approaches, all camera and point parameters remain in the optimization problem; only the update direction is restricted. The method serves as a drop-in replacement for existing BA pipelines. Experiments on both generic and challenging weak-geometry scenarios show more stable optimization, improved relative pose accuracy, and competitive calibration behavior while maintaining reprojection quality.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>StructGen: Disambiguating Multi-Reference Image Generation via Structured Context Modeling</strong>
          <small>Jianing Peng, Mengyu Wang, Henghui Ding, Zixiang Li, Ting Liu, Xiaochao Qu, Luoqi Liu, Yao Zhao, Yunchao Wei</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Generation</span>
<span class="topic-tag">Multimodal Conditioning</span>
<span class="topic-tag">Data-Efficient Training</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2607.15619</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15619">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the requested criteria; this is multi-reference image generation with structured conditioning, which fits generative multimodal learning but not the specific criteria listed.</p>
        <p class="abstract">Multi-reference image generation aims to synthesize images by integrating attributes from multiple reference images under textual instructions. As the number of references increases, the task necessitates complex semantic comprehension, such as correctly associating attributes with the intended subjects and planing out coherent spatial arrangement between subjects and their environments. Existing approaches, which rely solely on natural language instruction, often fail to capture these complex intentions precisely, leading to semantic misalignment and inconsistent generation. We identify two key factors behind these limitations: natural language instructions are often verbose and ambiguous, and high-quality multi-reference data is scarce. To address these issues, we propose StructGen, which employs a structured, dictionary-like format to encode multiple reference images, thereby enabling explicit and unambiguous specification of generation intentions. To support this design, we construct a structured dataset based on high-quality real images and develop a corresponding training framework, along with a dedicated benchmark for challenging multi-reference scenarios. Extensive experiments on both public benchmarks and our proposed benchmark demonstrate that StructGen consistently outperforms existing methods on both semantic alignment and detailed reference-generation consistency, especially under complex instructions with multiple references. The code is available at \href{https://jianingpeng0382.github.io/StructGen/}{https://jianingpeng0382.github.io/StructGen/}.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Sensor Fusion</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>CLIFE: Camera-LiDAR Fusion Framework for Edge-Deployable Roadside VRU Perception</strong>
          <small>Tam Bang, Hoang H. Nguyen, Lei Cheng, Lihao Guo, Siyang Cao, Hussam Abubakr, Tianya Zhang, Austin Harris, Mina Sartipi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Sensor Fusion</span>
<span class="topic-tag">Edge Perception</span>
<span class="topic-tag">Autonomous Driving</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.SY</span>
<span class="category-tag">eess.SY</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2607.16154</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.16154">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 loosely: an embodied/perception-adjacent multi-sensor fusion system for roadside VRU perception, but it is more deployment-focused than a novel embodied AI benchmark or method.</p>
        <p class="abstract">Reliable roadside perception of vulnerable road users (VRUs) remains challenging under occlusions, variable lighting, and diverse weather conditions, particularly under strict edge-computing and latency constraints. Existing multi-sensor fusion systems rely on cloud or server-grade infrastructure, creating a deployment gap at real-world intersections. We present CLIFE, an edge-native camera-LiDAR fusion framework that integrates targetless online calibration and lightweight late-fusion tracking entirely on a single embedded device, without cloud offloading. CLIFE adaptively refines camera-LiDAR alignment on demand and performs multi-sensor fusion and track association with O(N log N) per-frame cost. We deploy CLIFE across 12 signalized intersections in Chattanooga and conduct an in-depth evaluation at a representative intersection using synchronized camera-LiDAR data that spans diverse daytime, nighttime, and weather conditions. Our experiments demonstrate that the fusion architecture substantially enhances the perceptual range and robustness of the individual sensors under varied environmental and traffic conditions. The late-fusion core operates at 53.2 FPS on the Jetson AGX Thor, ensuring high throughput for real-time intersection-scale applications. By centering perception at the edge, CLIFE provides a deployable foundation for downstream safety applications, while reducing bandwidth and calibration overhead for agencies operating multi-intersection corridors.</p>
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
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction</strong>
          <small>Xue Yu, Bo Yuan, Pengshuai Yang, Kailin Zhao, Hong Hu, Junlan Feng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">GUI Agents</span>
<span class="topic-tag">World Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2607.15550</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15550">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Criterion 1 matches closely: this proposes a new safety framework for mobile GUI agents using a learned world model for pre-execution risk assessment, which is an embodied-agent method with spatial/state prediction.</p>
        <p class="abstract">Mobile graphical user interface (GUI) agents have demonstrated remarkable capabilities in automating complex tasks, yet they introduce critical safety risks where a single erroneous action can lead to irreversible consequences. Existing safety mechanisms are primarily reactive, lacking the ability to assess risks before execution. In this paper, we introduce SeerGuard, a consequence-aware safety framework designed to mitigate these risks through pre-execution instruction-level screening and action-level risk assessment. Specifically, the action-level assessment analyzes agent-proposed actions within current GUI states, anticipating likely outcomes to identify risks before they are executed. To enable these capabilities, we construct a unified safety-augmented world model (SAWM) via multi-task learning, integrating semantic next-state prediction with safety risk assessment. Extensive experiments demonstrate that SeerGuard generalizes effectively across diverse mobile GUI agents. On Qwen3-VL-8B-Instruct, it increases the safety-utility score from $0.191$ to $0.596$ at $\omega=0.8$ and reduces the risk-cost score from $0.347$ to $0.130$ at $\alpha=0.8$. Further analyses on our SAWM validate the effectiveness of the instruction-level screening, alongside the capability of action risk assessment and next-state prediction.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Beyond a Joke: Multi-Angle Reasoning for Detecting and Explaining Harmful Humor in Memes</strong>
          <small>Shanhong Liu, Pai Chet Ng, De Wen Soh, Malika Meghjani, Konstantinos N. Plataniotis</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Meme Understanding</span>
<span class="topic-tag">Explainable Multimodal Classification</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2607.15442</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.15442">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the requested criteria; this is a VLM-based meme understanding/explanation paper, but it is not about embodied AI, benchmark building for embodied agents, or vision foundation model applications in the sense of the criteria.</p>
        <p class="abstract">Internet memes intertwine visual cues, textual content, and cultural context, making them particularly challenging to interpret in scenarios where humor, sarcasm, and harmful intent coexist. These complexities highlight the need for explainable meme understanding systems that can provide reliable and structured reasoning to support both accurate classification and human interpretability. However, existing multimodal classifiers either overlook these interdependencies or provide only limited interpretability. In this paper, we introduce MAR-12, a novel framework that leverages Vision Language Models (VLMs) for meme detection and understanding in settings where humorous and hateful elements may coexist. The framework first interprets each meme through twelve structured perspectives derived from humor and hate theories. It then applies a role-aware soft-gated attention mechanism to learn how much each perspective should contribute, followed by a prototype-based classifier for the final prediction. Finally, explanations are synthesized using both perspective-specific reasoning and learned attention weights, ensuring transparent and context-grounded justifications. We evaluate MAR-12 on the PrideMM and Memotion datasets, where it achieves up to 80.3% accuracy for humor detection and 75.9% accuracy for hate detection, outperforming state-of-the-art approaches. Furthermore, both human and GPT-4-based evaluations confirm that MAR-12 produces coherent and persuasive explanations, particularly for memes in which humorous and harmful cues co-occur.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-06-19.html">
          <span>June 19, 2026</span>
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
