

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
      <p class="eyebrow">Daily ArXiv / September 15, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>18</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="6 mentions">action</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">ai-generated</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">aligned</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">answering</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="6 mentions">backbone</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">camera</span><span class="cloud-word" style="font-size:1.92rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="8 mentions">change</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">continuous</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="7 mentions">document</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="6 mentions">embedding</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">encode</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="7 mentions">fine-tuning</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="12 mentions">generation</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">hyper-llava</span><span class="cloud-word" style="font-size:2.37rem;opacity:0.9;color:color-mix(in srgb, var(--accent-2) 79%, var(--accent))" title="10 mentions">interaction</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">interactive</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="7 mentions">language</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">matching</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">medical</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="12 mentions">mllm</span><span class="cloud-word" style="font-size:1.92rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="8 mentions">modality</span><span class="cloud-word" style="font-size:2.57rem;opacity:0.95;color:color-mix(in srgb, var(--accent-2) 90%, var(--accent))" title="11 mentions">motion</span><span class="cloud-word" style="font-size:2.37rem;opacity:0.9;color:color-mix(in srgb, var(--accent-2) 79%, var(--accent))" title="10 mentions">multimodal</span><span class="cloud-word" style="font-size:1.92rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="8 mentions">multiple</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">observation</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">open-source</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">optimization</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">pixel</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="7 mentions">question</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="7 mentions">radiologist</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">real-world</span><span class="cloud-word" style="font-size:1.92rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="8 mentions">reasoning</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="7 mentions">region</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">response</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="6 mentions">routing</span><span class="cloud-word" style="font-size:2.57rem;opacity:0.95;color:color-mix(in srgb, var(--accent-2) 90%, var(--accent))" title="11 mentions">semantic</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">similarity</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="7 mentions">space</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="6 mentions">spatial</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="7 mentions">transition</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="7 mentions">understanding</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">unified</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">user</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="12 mentions">video</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="5 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="110 mentions">action</span><span class="cloud-word" style="font-size:1.72rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 46%, var(--accent))" title="155 mentions">agent</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="66 mentions">alignment</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="60 mentions">annotation</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="64 mentions">attention</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="62 mentions">camera</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="67 mentions">consistency</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="63 mentions">control</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="61 mentions">dense</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="68 mentions">detection</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="78 mentions">diffusion</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="59 mentions">driving</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="85 mentions">dynamic</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="73 mentions">editing</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="66 mentions">environment</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="130 mentions">evidence</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="62 mentions">fine-grained</span><span class="cloud-word" style="font-size:2.13rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 67%, var(--accent))" title="213 mentions">generation</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="64 mentions">geometric</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="71 mentions">geometry</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="60 mentions">grounding</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="80 mentions">inference</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="60 mentions">instruction</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="94 mentions">interaction</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="86 mentions">language</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="74 mentions">latent</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="66 mentions">memory</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="72 mentions">mllm</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="94 mentions">motion</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="163 mentions">multimodal</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="68 mentions">multiple</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="104 mentions">object</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="82 mentions">observation</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="72 mentions">optimization</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="69 mentions">pipeline</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="90 mentions">point</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="59 mentions">question</span><span class="cloud-word" style="font-size:1.84rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="171 mentions">reasoning</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="61 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="66 mentions">region</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="66 mentions">reward</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="107 mentions">scene</span><span class="cloud-word" style="font-size:1.88rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="176 mentions">semantic</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="84 mentions">space</span><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="134 mentions">spatial</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="67 mentions">structure</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="60 mentions">structured</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="81 mentions">supervision</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="71 mentions">support</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="94 mentions">target</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="88 mentions">temporal</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="70 mentions">textbf</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="98 mentions">token</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="127 mentions">trajectory</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="68 mentions">understanding</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="60 mentions">unified</span><span class="cloud-word" style="font-size:2.13rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 67%, var(--accent))" title="214 mentions">video</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="75 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="324 mentions">visual</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="91 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>15 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models</strong>
          <small>DeepCybo Team, Yu Bin, Haipeng Cao, Zheng Chang, Kai Chen, Youning Chen, Kailin Deng, Yichao Du, Xiaotong Fu, Haoyang Ge, Yunlong Guo, Chenliu Hao, Jiyan He, Xuguo He, Yakun Hou, Kai Hu, Cong Huang, Tuopusen Huang, Yu Huang, Hong Li, Peize Li, Shijie Lian, Xiaopeng Lin, Yun Lin, Haibao Liu, Haochen Liu, Qiuzhi Liu, Shengcai Liu, Zhiqiang Liu, Tao Luo, Peng Ren, Shuo Ren, Chaoyi Ruan, Zhaolong Shen, Yukun Shi, Qiyuan Su, Yuxuan Tian, Yining Wang, Changti Wu, Hao Wu, Xueyin Xu, Ruoqi Yang, Zhaoyang Yang, Hang Yuan, Zhaoyang Zeng, Hanwen Zhang, Ruimeng Zhang, Yao Zhang, Yibo Zhang, Yuxiang Zhang, Zhirui Zhang, Ziyi Zhang, Zubin Zheng, Zishen Zhuang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Physical Foundation Models</span>
<span class="topic-tag">Vision-Language Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2609.14973</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.14973">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 4 very closely: it is a physical foundation model built from a vision-language model, aimed at understanding physical environments, generating actions, and predicting future states for embodied settings.</p>
        <p class="abstract">We present PhysBrain 1.5, a unified model for understanding physical environments, generating actions, and predicting future states. Motivated by the physical loop of observation, interaction, and environmental change, we bring these capabilities into a common learning framework. Starting from a general vision--language model, we encode language responses, end-effector motion, and dense visual targets as discrete sequences and jointly optimize them with autoregressive next-token prediction. Pre-training draws its embodied supervision entirely from human interaction videos, using task-centered episodes to pair semantic and spatial context with recovered motion and subsequent observations. We then adapt the model through supervised fine-tuning on a mixture of human demonstrations, robot trajectories, and simulated experience. Across 28 embodied understanding benchmarks, our 8B model achieves an average score of 72.5, setting a new open-source state of the art and performing on par with leading proprietary models such as GPT-6-Astra and Gemini 3.6 Flash. It achieves the best open-source results on 14 benchmarks while retaining general multimodal capabilities. Beyond these understanding evaluations, qualitative examples show the model&#x27;s ability to produce end-effector trajectories and predict future scenes through spatially aligned RGB, depth, and robot-mask outputs.</p>
      </div>
    </details>


    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>DiVA: Enabling Interactive Digital Life Simulation via Video Models</strong>
          <small>Cheng Chen, Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Wen Wang, Yihao Meng, Hanlin Wang, Yixuan Li, Jiacheng Wei, Zhenshan Tan, Yanhong Zeng, Yujun Shen, Guosheng Lin, Fayao Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Interactive Video Generation</span>
<span class="topic-tag">MLLM Orchestration</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2609.13830</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.13830">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied/digital-life simulation system built around an MLLM router and interactive video generation, with explicit focus on long-term simulation, spatial grounding, and stable transitions.</p>
        <p class="abstract">We present DiVA, a deeply interactive digital life simulator pioneering a new paradigm for long-term, open-ended interactive experiences within digital character worlds. DiVA&#x27;s architecture pairs a Multimodal Large Language Model (MLLM) as a router with a meticulously designed stacked video pipeline for seamless, multi-turn interactions with action and audio response. To maintain continuity and avoid degradation, we model generation as a three-part coupled system: waiting video, action video, and the transitions between them. These transitions are critically handled by our Anchored Video Continuation (AVC) module, which returns the character to stable states to prevent degradation. By encoding information from the preceding action video segment, AVC ensures smooth transitions, significantly reducing camera jitter and inconsistencies common in current video transition methods. This design also enables complex pose changes (e.g., sitting to standing) typically difficult for audio-driven models. These system designs together ensure high-fidelity identity, coherence, and dynamics for extended experiences. To validate our pipeline design, we comprehensively compare our system against alternatives by replacing our core generation module with mainstream long-video, continuation, and interpolation methods. We further analyze the necessity of the three-stage design, anchor-state selection, transition naturalness, spatial grounding, and the quality-latency trade-off, and we expand the comparison to additional long-form audio-driven avatar models. Results confirm DiVA is markedly superior in maintaining long-term visual quality and realism, validating its effectiveness as a sustainable, interactive simulation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>Concept-Grounded Reasoning with Prompt-Driven Localization for Interpretable Structured Report Generation</strong>
          <small>Xinyue Xu, Hongbin Lin, Juangui Xu, Hualiang Wang, Lehan Wang, Lijie Hu, Weiyang Liu, Adrian Weller, Xiaomeng Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM</span>
<span class="topic-tag">Medical Vision-Language</span>
<span class="topic-tag">Spatial Grounding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2609.15334</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.15334">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and also criterion 1 in a medical-imaging setting: it uses an MLLM with prompt-driven localization and concept-grounded reasoning for spatially grounded report generation.</p>
        <p class="abstract">Medical imaging modalities such as ultrasound and X-ray are widely used in clinical practice, where diagnosis follows a structured, evidence-driven workflow aligned with standardized criteria. While multimodal large language models (MLLMs) show promise for automated medical report generation, most existing systems rely on end-to-end multimodal fusion without modeling clinically defined intermediate attributes, leading to limited grounding and interpretability. To address this issue, we propose CORAL (COncept-grounded ReAsoning with Localization), a multimodal framework that integrates spatial grounding and concept-level supervision into a unified reasoning process. CORAL employs a prompt-driven medical segmentation model to localize lesions and predicts multi-class clinical attributes through a Concept Bottleneck module. The resulting textual concept tokens are combined with mask-modulated visual features within an MLLM to enable structured report generation and diagnostic prediction. Experiments on BUS-CoT and IU X-ray datasets demonstrate consistent improvements in diagnostic accuracy, concept consistency, and report quality over strong general-purpose and medical MLLMs, indicating that concept-grounded reasoning better aligns generation with clinical decision processes.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">View Synthesis</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>ConeGaussian: Anti-Aliased Gaussian Ray-Tracing for Generic Central Cameras</strong>
          <small>Deheng Zhang, Letian Shi, Runyi Yang, Zhendong Li, Lei Sun, Kanzhi Wu, Ajad Chhatkuli, Danda Pani Paudel, Luc Van Gool</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">View Synthesis</span>
<span class="topic-tag">Gaussian Rendering</span>
<span class="topic-tag">Anti-Aliasing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2609.13397</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.13397">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: this is a vision/rendering method for generic central cameras, improving camera-model-agnostic Gaussian ray tracing with anti-aliasing for distorted and fisheye imagery.</p>
        <p class="abstract">In rendering, a camera is a sampling operator that maps each finite pixel to a bundle of rays. Different camera models change the geometry of this bundle, thus making a unified and faithful rendering formulation challenging. Consequently, Gaussian ray tracing supports generic cameras (with optical center) through their inverse ray mappings, yet typically reduces every pixel to a single center ray. This ignores the camera-dependent pixel footprint, causing aliasing under minification, while unconstrained Gaussians expose unsupported frequencies under magnification. We present ConeGaussian, a camera-model-agnostic anti-aliasing framework for Gaussian ray-based rendering. Instead of defining the pixel filter on a camera-specific image plane, ConeGaussian constructs an anisotropic footprint directly from neighboring rays produced by the camera&#x27;s native inverse mapping. We derive a closed-form response under a locally linear, depth-local, moment-matched approximation of the finite pixel footprint, while the same geometry defines a per-Gaussian training-frequency floor. Notably, by construction, our filtering principle can be used unmodified across calibrated central camera models and multiple Gaussian ray-rendering backbones. Additionally, unlike in mip-splatting, our scene-space frequency floor and filtering enable trivial composition at render time, allowing us to remove excess blurring. On pinhole and strongly distorted fisheye captures, ConeGaussian consistently improves two distinct ray-based backbones, by up to 4.3 dB at 1/8 resolution, and reduces fisheye LPIPS by 30% where perspective screen-plane footprint formulations are not directly applicable.</p>
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
          <strong>Selective Tool Use for Agentic Change Visual Question Answering in Remote Sensing</strong>
          <small>Yakoub Bazi, Mohamad M. Al Rahhal, Mohamed A. Mekhtiche, Mansour Zuair</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Tool Use</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2609.14523</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.14523">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 3 moderately well: it introduces a tool-augmented VLM pipeline for change VQA in remote sensing, with selective tool use and a new tool-augmented benchmark extension.</p>
        <p class="abstract">Change visual question answering (Change VQA) requires understanding semantic changes across bi-temporal remote sensing images. Although vision language models (VLMs) have shown promising performance on this task, they remain unreliable when answering questions that require explicit transition statistics, area measurements, or spatial information. To address this limitation, we propose a selective tool use framework in which a single VLM either answers directly or invokes a deterministic change analysis tool to obtain question specific evidence. Specifically, the selected tool operates on bi-temporal semantic maps and returns a structured observation, which the same VLM uses to generate its final answer. To support this framework, we construct a tool augmented extension of CDVQA covering eight question families and three tools for transition, spatial, and temporal analysis. Tool use supervision and observations are derived automatically from the original semantic annotations, without additional manual labeling. We then adapt Qwen3.5-4B using Low Rank Adaptation (LoRA) to jointly learn direct answering, tool invocation, and evidence conditioned answering. Experiments on 7,164 test questions show that selective tool use with reference semantic maps improves overall accuracy from 73.77% to 88.79% and average family accuracy from 69.11% to 89.65%. When the semantic maps are predicted automatically, the framework achieves 77.47% overall accuracy and 75.06% average family accuracy. These results demonstrate the benefit of question-specific semantic evidence for Change VQA, while highlighting the influence of semantic prediction quality on the resulting performance. Code and tool-augmented annotations will be made publicly available at https://github.com/yakoubbazi/ToolChangeVQA.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Instruction Tuning</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Hyper-LLaVA: Hyperbolic Uncertainty-aware Modality-Balanced Routing for Multimodal Continual Instruction Tuning</strong>
          <small>Kunlun Xu, Yanqin Zhang, Wenwen Qiang, Jiahuan Zhou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Instruction Tuning</span>
<span class="topic-tag">Parameter Routing</span>
<span class="topic-tag">Continual Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2609.13742</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.13742">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: Hyper-LLaVA is a multimodal continual instruction-tuning method for an MLLM, with a new routing strategy.</p>
        <p class="abstract">Multimodal Continual Instruction Tuning (MCIT) aims to exploit the incrementally accumulated knowledge to process multimodal inputs of diverse tasks, where parameter routing plays an important role. State-of-the-art methods rely on sample-to-task center similarity and cross-modal fusion with equal weight during routing. However, such solutions face two fundamental flaws: (1) Within each modality, the sample-to-task center distance is sub-optimal for routing since the abundant intra-task diversity information is underleveraged. (2) Different modalities exhibit varying reliability across tasks, where the modality with inter-task ambiguity can easily misguide the routing result. To address these problems, we propose Hyperbolic Uncertainty-aware Modality-Balanced Routing (Hyper-LLaVA) to improve parameter routing capacity based on cross-modality task feature uncertainty modeling. Specifically, to improve intra-modality task matching, Hyper-LLaVA accesses the sample-to-task distribution similarity in the Hyperbolic space. Besides, to alleviate the degradation brought by unreliable modalities, Hyper-LLaVA quantifies the task matching ambiguity within each modality to achieve adaptive balancing between task matching across modalities. Based on the complementary intra- and inter-modality task matching enhancement, our Hyper-LLaVA outperforms state-of-the-art approaches by large margins. Our source code is available at https://github.com/zhoujiahuan1991/ICML2026-Hyper-LLaVA</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Realtime-Venus: A full-duplex interaction system with asynchronous delegation</strong>
          <small>Ruixiang Zhao, Hualei Wang, Renhe Sun, Enzhi Zhou, Jincenzi Wu, Xujie Song, Kexin Shi, Zihang Liu, Pengcheng Zhu, Jiayi Zhou, Baoyue Zhang, Changhao Zhang, Zitong Wang, Jinhong Wang, Tong Niu, Jingjing Liu, Junan Lin, Haolin He, Hengshuo Chu, Yuhui Chen, Jian Liu, Yuge Huang, Junliang Xing, Yuntao Wang, Weiqiang Wang, Chun Yu, Yuanchun Shi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Modeling</span>
<span class="topic-tag">Audio-Visual Interaction</span>
<span class="topic-tag">Full-Duplex Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">eess.AS</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2609.13814</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.13814">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 reasonably well: it presents an audio-visual interaction model with online video understanding and proactive dialogue, i.e. a VLLM/MLLM-style system.</p>
        <p class="abstract">Natural interaction in digital and physical environments requires continuous perception and timely responses. Spoken dialogue relies on acoustic and linguistic cues, while video interaction also requires grounding the conversation in evolving visual context. We present Realtime-Venus, a proactive full-duplex interaction system with two separately trained 9B models: Realtime-Venus-Omni for audio-visual interaction and Realtime-Venus-Audio for spoken interaction. Each model serves as a complete conversational frontend, integrating continuous perception, conversational control, and native speech generation through a shared causal timeline for user inputs, model outputs, and delegation events.   A dual-loop runtime coordinates live interaction with background reasoning and tool execution. Foreground interaction continues while Realtime-Venus-Harness executes tasks asynchronously and returns results for integration into the ongoing dialogue.   Both models follow a common post-training recipe combining offline understanding, proactive full-duplex trajectories, and delegation workflows.   Among the evaluated online models, Realtime-Venus-Omni achieves the highest scores on six of eight video benchmarks, including StreamingBench (70.2%), OVO-Bench (64.7%), and Daily-Omni (81.3%). Across eight audio understanding and spoken question answering benchmarks, Realtime-Venus-Audio leads the compared models on MMAU (78.0%), MMAU-Pro (63.2%), Llama Questions (83.8%), and Speech CMMLU (67.8%), while matching the best VoiceBench AlpacaEval score of 4.81. On Full-Duplex-Bench v1.5, Realtime-Venus-Audio responds to 75% of user interruptions and achieves continuation rates of 97%, 88%, and 86% under backchannels, other-directed speech, and background speech, respectively, exceeding Gemini 3.1 Live and GPT-4o on all three continuation metrics.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Diffusion Models</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>DNF-SR: Dual-Input and Negative-Aware Feature Fine-Tuning for Real-World Image Super-Resolution</strong>
          <small>Shuhao Han, Wenjie Liao, Hayden Vance, Hang Dong, Rui Zhang, Chun-Le Guo, Chongyi Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Super-Resolution</span>
<span class="topic-tag">Image Restoration</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2609.15120</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.15120">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: it is a diffusion-model-based image super-resolution method, using generative priors and feature fine-tuning for real-world restoration.</p>
        <p class="abstract">Benefiting from the powerful generative priors of diffusion models, diffusion-based real-world image super-resolution (Real-ISR) methods have demonstrated impressive performance.To achieve efficient Real-ISR, several recent works have designed one-step diffusion-based models.Howerver, unmediatedly feeding LR into a diffusion model creates a distributional gap with the model&#x27;s original input.A straightforward approach to reduce the distribution gap is to introduce noise to the LR latents. However, directly adding noise inevitably corrupts the content of the LR images.In this study, we propose DNF-SR, a Dual-input and Negative-aware Feature fine-tuning method for Real-ISR.Specifically, we use a dual-input strategy that concatenates the original LR image with the noisy LR input and feeds them into a diffusion-based image editing model, ensuring both high-fidelity one-step super-resolution and improved perceptual and content consistency.Additionally, the noise present in the noisy LR input introduces randomness and diversity into the outputs. We exploit this property and propose a post-training optimization method, Negative-aware Feature Fine-Tuning (NF2T), which guides the model toward producing higher-quality results.NF^2T classifies multiple outputs into positive and negative subsets and then defines implicit policy improvement directions in both the image and feature spaces, thereby further enhancing the stability of the optimization.Extensive experiments show that DNF-SR outperforms other methods.Code will be released.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Beyond Natural Images: Rethinking AI-Generated Image Detection in Documents</strong>
          <small>Zhangjie Fu, Jiazhen Yan, Yuanwen Chen, Xinquan Yu, Yanzhe Li, Hui Jiang, Lei Gao, Chenfu Bao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">AI-Generated Image Detection</span>
<span class="topic-tag">Document Intelligence</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2609.14352</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.14352">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: it is a vision foundation model application for AI-generated image detection in document images, with a new benchmark and document-specific analysis.</p>
        <p class="abstract">AI-generated image detection has attracted increasing attention, but existing evaluations mainly focus on natural images, leaving AI-generated document images largely underexplored. This omission is concerning because documents often appear in sensitive real-world scenarios, such as invoices, expense reports, certificates, and medical records. In this paper, we first construct a controlled diagnostic benchmark, AIGDoc-Pilot, and reveal that existing detectors suffer substantial performance degradation on AI-generated document images, with the mean AUC dropping by more than 7%. Based on this, we further reveal two document-specific properties behind this gap: generation artifacts exhibit strong spatial inconsistency across local regions, and text density significantly affects real-synthetic separability, where text-dense regions offer stronger discriminative evidence. Motivated by these findings, we construct AIGDoc, a larger document-centric dataset containing diverse real-world documents and AI-generated counterparts produced by multiple advanced generation and editing models. Extensive experiments on AIGDoc demonstrate that existing detectors still struggle to reliably identify AI-generated documents, while document-based training partially narrows the gap. Together, these results offer valuable insights for developing dependable and generalizable detectors in document-centric scenarios. The code and datasets will be made publicly available upon acceptance of the paper.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Restoration</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>LIMODENet: Attention-Free Compact Encoders for Information-Preserving Onboard Satellite Image Restoration</strong>
          <small>Thanh-Dung Le, Vu Nguyen Ha, Ti Ti Nguyen, Symeon Chatzinotas</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Restoration</span>
<span class="topic-tag">Efficient Vision Models</span>
<span class="topic-tag">Satellite Imaging</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2609.14690</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.14690">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: it is a vision restoration backbone for onboard satellite imaging, centered on compact attention-free encoders and deployment-constrained visual foundation-style design choices.</p>
        <p class="abstract">Onboard satellites must restore a channel-degraded image on a few watts, using neuromorphic accelerators (e.g., BrainChip Akida, Intel Loihi-2) that support no softmax or attention. We ask which encoder restores best under that constraint and introduce LIMODENet (LinearMix-ODENet), a 0.69M softmax-/QKV-free backbone whose residual stages read as ODE discretizations and which is empirically information-preserving (probe accuracy rises 79.9% -&gt; 98.4% from stem to head). At iso-parameters it restores 1 dB DVB-S2X-degraded EuroSAT better than a CNN autoencoder (+1.75 dB PSNR) and a skip-connection U-Net (+1.07 dB), three seeds, non-overlapping. Unconstrained modern restorers (NAFNet, Restormer) win on fidelity; we decompose that gap: spiking-legal additive skips recover about half, and the rest traces to attention and channel gating. LIMODENet then converts end-to-end to a spiking network with zero blocked operations, versus 22-24 for the competitors: not the best restorer available, but the best verified deployable within a real power budget.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Virtual Try-On</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>TryOnReward: Learning Foveated Consistency for Reinforcement Fine-Tuning of Virtual Try-On</strong>
          <small>Xueheng Li, Yong Liu, Xiaolong Fu, Wen Xue, Chengjun Xie, Yipeng Sun, Yan Li, Simiu Gu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Virtual Try-On</span>
<span class="topic-tag">Reward Modeling</span>
<span class="topic-tag">Human Preference Learning</span>
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
          <span>Paper 12 / arXiv:2609.13259</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.13259">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; it is a reward model and benchmark for virtual try-on, which is a multimodal application but not specifically spatial intelligence, embodied AI, or foundation models.</p>
        <p class="abstract">Virtual Try-On (VTON) aims to dress a person with the reference garment, producing visually reasonable results aligned with human preferences. Turning this preference-oriented goal into an actionable objective relies on a scoring function aligned with human taste. However, classic fidelity metrics exhibit weak correlation with human judgments, and generic VLMs fail to provide the discriminative granularity demanded by try-on quality evaluation, which hinges on faithfully preserving garment and person details. This shortcoming is further exacerbated in the reinforcement fine-tuning (RFT) optimization and leads to severe reward hacking. To this end, we present TryOnReward, a fine-grained reward model tailored for VTON. Built on a vision-language backbone, it adopts a foveation calibration objective that grounds each quality dimension in the relevant region to avoid global shortcut learning. Meanwhile, TryOnReward jointly optimizes pairwise preferences and per-dimension quality scores via margin-aware supervision, leveraging both relative and absolute quality signals. For model training and evaluation, we build TryOnReward-100K, a human-annotated per-dimension rating dataset, alongside TryOn-Bench and TryOnRewardBench, two benchmarks covering diverse real scenarios. Extensive experiments confirm that TryOnReward significantly outperforms generic judges in human preference alignment, and when serving as the RFT reward function, it consistently yields human-preferred try-on results across multiple baselines.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Large Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>From Density to Biopsy Decisions and Malignancy Prediction: A Benchmark Study of Multimodal Large Language Models Against Radiologists in Digital and Contrast-Enhanced Mammography</strong>
          <small>Ali Abbasian Ardakani, Afshin Mohammadi, Taha Yusuf Kuzan, Beyza Nur Kuzan, Alisa Mohebbi, Masume Behruzi, Hamid Khorshidi, Ashkan Ghorbani, Elham Asadiara, Zeinab Khorshidi Lotfi, Ansar Rahman, Nedim Christoph Beste, U. Rajendra Acharya, Sepideh Hatamikia</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Large Language Models</span>
<span class="topic-tag">Medical Vision-Language</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">physics.med-ph</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2609.14676</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.14676">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it benchmarks multiple MLLMs on mammography tasks and compares them against radiologists.</p>
        <p class="abstract">Purpose: To compare four multimodal large language models (MLLMs) with radiologists of varying expertise in breast density assessment, BI-RADS assessment, biopsy candidacy determination, and continuous malignancy probability estimation using digital mammography (DM) and contrast-enhanced mammography (CEM). Methods: This study included 179 women with paired DM/CEM examinations and reference standards. Four MLLMs (ChatGPT-5.2, Gemini-3.1 Pro, Sonnet-4.6, Muse Spark) interpreted images with and without masks; three radiologists interpreted non-masked images. Results: For binary density classification on DM, radiologist accuracies ranged from 55.81% to 78.60%, exceeding most MLLM values (62.33%-71.63%), while masks added limited benefit. Five-category BI-RADS accuracies were higher for radiologists on DM (56.74-67.44%) and CEM (62.33-82.79%) compared with MLLMs (DM 31.16-45.12%; CEM 40.00-55.81%). Binary biopsy-candidacy accuracies were likewise higher for radiologists (DM 85.12-89.77%; CEM 86.98-92.09%) than for MLLMs (DM 61.39-75.35%; CEM 69.30-82.79%), although CEM improved performance across all readers. Lesion masks substantially improved MLLM continuous malignancy-probability accuracies from 64.65%-71.63% to 72.56-78.60% on DM and from 67.91%-77.21% to 72.56%-81.86% on CEM, approaching radiologist ranges (DM 63.72-82.79%; CEM 81.86-88.84%). The corresponding AUCs for the top masked models overlapped those of the human readers. Overall, Muse Spark, followed by Sonnet-4.6, demonstrated the strongest performance among the MLLMs across domains. Conclusion: Radiologists generally outperformed MLLMs in categorical tasks, while selected masked models approached human performance for continuous malignancy probability estimation, suggesting a potential adjunctive role.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Robust Estimation</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>Robust Multi-Model Fitting through Learning Neighbor Regions</strong>
          <small>Chang Nie, Guangming Wang, Zhe Liu, Hesheng Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Robust Estimation</span>
<span class="topic-tag">Geometric Vision</span>
<span class="topic-tag">Model Fitting</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2609.15348</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.15348">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to the criteria; it is a computer vision optimization method for multi-model fitting, which is related to vision/geometry but not specifically spatial intelligence, VLLMs, embodied AI, or foundation models.</p>
        <p class="abstract">Multi-model fitting involves fitting multiple models accurately in a noisy environment. It is the basis for computer vision tasks such as scene reconstruction and mixed reality. However, its performance is often limited by insufficient feature utilization, inefficient optimization, model overlap, and the non-differentiable pipelines. To overcome these limitations, we introduce a robust coarse-to-fine framework called Learning Neighbor Regions (LNR). Recognizing that substantial computational resources are wasted on numerous bad minimum sets, we propose the coarse-level module. This module utilizes a neural network to extract and analyze geometric feature of both local point-wise relationships and global contextual information in minimum sets, outputting confidence to pre-select a small number of good minimum sets, thereby enhancing overall efficiency before solving hypotheses. To address model overlap, LNR encodes neighbor region features for each hypothesis in its fine-level module. These region features consist of geometric features of neighboring data points, which can be used by multiple regions simultaneously. This design allows the neural network to individually refine and score each hypothesis. Importantly, LNR is trained to learn directly from data point features rather than from the hypothesis parameters, thus avoiding differentiating the sampling process and the model solvers. Extensive experiments on four classic multi-model fitting tasks demonstrate that LNR achieves state-of-the-art performance. The analysis suggests that LNR can be easily adapted to various robust multi-model fitting tasks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Text-to-Motion</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>MoVT: Video-Augmented Motion Tokenizer for Text-to-Motion Generation</strong>
          <small>Beibei Jing, Tianle Guo, Youjia Zhang, Zikai Song, Yawei Luo, Junqing Yu, Tao Guan, Wei Yang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Motion</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Cross-Modal Tokens</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2609.14965</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.14965">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; it is a generative text-to-motion method using video augmentation, but not an embodied AI benchmark or VLLM/MLLM paper.</p>
        <p class="abstract">Text-driven 3D human motion generation models face significant challenges in responding to diverse and unconstrained textual prompts, primarily due to the limited availability of 3D motion training data. To address this, we introduce MoVT, a novel framework that effectively leverages the extensive range of human action videos to enhance text-to-motion generation. At the core of our approach is the cross-modal augmented motion tokenizer, which projects discrete 3D motion tokens into the 2D domain. This projection allows us to enrich the motion codebook with complex, real-world motion patterns derived from videos. The enriched discrete tokens are then mapped back to the 3D domain, resulting in aligned 3D and 2D codebooks with an enhanced capacity to represent intricate motions. These enhanced codebooks are integrated into a generative masked transformer, which predicts masked motion token indices in a modality-agnostic manner. This enables the use of text-index pairs, generated from the 2D codebook and annotated motion videos, to further enhance the generator. Extensive empirical evaluations show that MoVT performs favorably against prior state-of-the-art methods across multiple key metrics.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Embeddings</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>PACE: Progressive Angular-to-Norm Contrastive Embedding</strong>
          <small>Yanping Li, Wei Zhou, Yawen Liu, Yibo Wang, Ke Zhu, Guangda Huzhang, Qing-Guo Chen, Zhao Xu, Jun Zhang, Wei Wei</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Embeddings</span>
<span class="topic-tag">Contrastive Learning</span>
<span class="topic-tag">Metric Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2609.15152</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.15152">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; it is a multimodal embedding method, but not a VLLM/MLLM, embodied AI, or vision foundation model application in the intended sense.</p>
        <p class="abstract">Multimodal embedding models encode heterogeneous inputs into a shared embedding space, enabling efficient similarity computation across modalities and tasks. Most existing methods optimize cosine-based contrastive objectives, which promote stable training but restrict semantic compatibility to angular geometry, precluding embedding norms from serving as an additional semantic signal. However, directly optimizing the more expressive dot-product similarity, which leverages both angular and norm information, underperforms cosine-based training and exhibits unstable training dynamics. We attribute this discrepancy to premature optimization-space expansion, manifested as angular--norm entanglement and directional anisotropy in the representation space and further compounded by full-parameter fine-tuning. In this paper, we propose PACE, a two-stage framework that progressively expands both the representation and trainable parameter spaces. Stage I combines cosine-based objective with low-rank adaptation to establish a reliable angular geometry within constrained optimization spaces. Stage II switches to dot-product similarity and full-parameter fine-tuning, enabling embedding directions and norms to jointly encode semantic information. We further introduce Focal Embedding Loss, a confidence-adaptive objective that downweights queries with high positive retrieval confidence while emphasizing ambiguous queries with competitive negatives. Experiments across multiple backbone scales and diverse multimodal embedding tasks consistently validate the effectiveness of PACE.</p>
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

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>VisInteract: Towards Dynamic Interactive Text-to-Visualization under Imperfect Queries</strong>
          <small>Wenxin Xu, Jinwei Lu, Hwanhee Kim, Chen Jason Zhang, Xiao-Yong Wei, Haoyang Li, Yuanfeng Song</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Interactive LLM Agents</span>
<span class="topic-tag">Text-to-Visualization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2609.15182</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.15182">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it builds a new embodied-like benchmark and method for dynamic interactive Text-to-Visualization, with a novel simulator-style user agent and MCTS-based interaction loop that previous work largely ignored.</p>
        <p class="abstract">Real-world visualization requests are routinely ambiguous, incomplete, or factually incorrect, yet existing Text-to-Visualization (Text-to-Vis) systems assume well-specified inputs and produce charts in a single pass. When queries are imperfect, a system must \emph{interact} with the user to recover the true intent, but no benchmark or method supports this dynamic process. We introduce \textbf{VisInteract}, a new paradigm that reframes Text-to-Vis as interaction-driven intent recovery, and \textbf{VisInteract-Bench}, to our knowledge, that is the first benchmark for dynamic interactive Text-to-Vis, featuring controlled imperfection injection, a leakage-controlled User Agent for realistic multi-turn feedback, and dual-perspective (code and chart) automated evaluation. On the algorithmic side, we propose \textbf{Vis-MCTS}, a Monte Carlo Tree Search (MCTS) enhanced method, introducing improvements over classical MCTS, that \emph{Progressive Widening} to tame the unbounded tool-argument space in tree search, \emph{cross-rollout information sharing} so clarifications and critiques benefit the entire search tree, and \emph{Dimension-Aware Reward Decomposition} that routes scalar user feedback along data-fidelity, visual-design, and intent-alignment dimensions to resolve credit assignment across heterogeneous actions. Extensive Experiments across two LLM backbones show that Vis-MCTS consistently outperforms all Text-to-Vis baselines, improving end-to-end task success by $13.40\%$--$16.27\%$ over the strongest interactive baseline and by more than $5\times$ over non-interactive ones.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Beyond Accuracy: Robustness, Cost, and Governance Trade-offs for Vision-Language Models in Templated Document Extraction</strong>
          <small>Kushal Patel, Pushkal Shrivastava, Mackenzie Lees, Qirui Lu, Bhargobjyoti Saikia, Liying Li, Junlin Jiang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Document AI</span>
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
          <span>Paper 13 / arXiv:2609.15706</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.15706">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 only indirectly: it studies vision-language models for document extraction and gives a measurement-grounded evaluation framework, but it is not really about a new VLLM/MLLM or embodiment/spatial understanding.</p>
        <p class="abstract">Vision-language models (VLMs) are increasingly used to extract structured fields from business documents, yet most evaluations report accuracy on clean benchmarks and offer little guidance to practitioners choosing an approach for a given task complexity. We address this gap with a measurement-grounded study and an open-source release. Across eleven systems (three commercial, two reasoning, five open-source VLMs in pretrained and fine-tuned form, and a non-LLM OCR-&gt;regex floor) scored on a 750-document held-out pool of synthetic checks, fine-tuning on 3K samples lifts the best open-source VLMs above F1 0.98-above every zero-shot commercial system on this task-while GPT-5 leads the commercial pool on F1 and Claude Sonnet 4.5 collapses on Date. To turn these measurements into actionable choices, we introduce a practitioner-oriented selection framework that maps a task profile (quality, latency, governance, volume) to a recommended approach via filtering and total-cost minimization, illustrated on a hypothetical mid-volume document-extraction scenario.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Retrieval-Augmented Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>CWM: Controllable White-Box Meta-Prompting for Adaptive Retrieval-Augmented Generation and Reasoning Ability</strong>
          <small>Keuntae Kim, Eunhye Jeong, Yong Suk Choi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Retrieval-Augmented Generation</span>
<span class="topic-tag">Prompting</span>
<span class="topic-tag">Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2609.15234</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.15234">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is an LLM method for adaptive RAG and reasoning, but not a visual or multimodal model.</p>
        <p class="abstract">Recently, Large Language Models (LLMs) have gained significant attention due to their strong language understanding and generation capabilities, demonstrating impressive reasoning abilities as well as effective utilization of external knowledge. Many studies have proposed methods that specialize in improving performance for individual tasks. However, ironically, only a limited number of attempts have explored general-purpose, task-agnostic methods. In this work, we present a unified framework integrating reasoning and Retrieval-Augmented Generation (RAG) tasks. We further propose Controllable White-Box Meta-Prompting (CWM), a low-cost white-box method for adaptive RAG tasks previously dominated by black-box approaches, without requiring external decision modules or multi-sampling. CWM achieves state-of-the-art performance on three adaptive RAG benchmarks across recent LLMs, including GPT-oss-20b, Qwen3-14b, and Llama3.1-8b, while also demonstrating strong generality by extending to reasoning tasks. In addition, CWM provides controllability by enabling retrieval decisions to be regulated through the manipulation of internal model signals. Our code is available at https://github.com/JeongEunhye00/CWM.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-08-28.html">
          <span>August 28, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-27.html">
          <span>August 27, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-26.html">
          <span>August 26, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-25.html">
          <span>August 25, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-24.html">
          <span>August 24, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-21.html">
          <span>August 21, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-20.html">
          <span>August 20, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-19.html">
          <span>August 19, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-18.html">
          <span>August 18, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-17.html">
          <span>August 17, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-15.html">
          <span>August 15, 2026</span>
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
