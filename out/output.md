

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
      <p class="eyebrow">Daily ArXiv / August 28, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>17</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>17</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>12.4</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.01rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 61%, var(--accent))" title="13 mentions">action</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">active</span><span class="cloud-word" style="font-size:1.89rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 55%, var(--accent))" title="12 mentions">agent</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">clinical</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">competitive</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">construct</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">control</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">detection</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">dynamic</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="8 mentions">encoder</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">evidence</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">fusion</span><span class="cloud-word" style="font-size:2.13rem;opacity:0.84;color:color-mix(in srgb, var(--accent-2) 67%, var(--accent))" title="14 mentions">generation</span><span class="cloud-word" style="font-size:1.63rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="10 mentions">generative</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">geometric</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">interaction</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">keypoint</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">language</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">material</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">mllm</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">mode</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">motion</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">multimodal</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">observation</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">perception</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">pipeline</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">policy</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">proxy</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">question</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="20 mentions">reasoning</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">response</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">reward</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">scene</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">spatial</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">support</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">surgical</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="8 mentions">target</span><span class="cloud-word" style="font-size:2.01rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 61%, var(--accent))" title="13 mentions">textbf</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">textsc</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="9 mentions">token</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">trajectory</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="11 mentions">video</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">view</span><span class="cloud-word" style="font-size:2.36rem;opacity:0.89;color:color-mix(in srgb, var(--accent-2) 79%, var(--accent))" title="16 mentions">visual</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.27rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="134 mentions">action</span><span class="cloud-word" style="font-size:1.70rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="211 mentions">agent</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="96 mentions">alignment</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="72 mentions">attention</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="87 mentions">change</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="77 mentions">condition</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="77 mentions">consistency</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="87 mentions">control</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="118 mentions">detection</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="99 mentions">diffusion</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="85 mentions">dynamic</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="81 mentions">editing</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="80 mentions">environment</span><span class="cloud-word" style="font-size:1.85rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 53%, var(--accent))" title="241 mentions">evidence</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="105 mentions">fine-grained</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="114 mentions">frame</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="77 mentions">fusion</span><span class="cloud-word" style="font-size:1.83rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="236 mentions">generation</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="78 mentions">generative</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="112 mentions">inference</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="118 mentions">interaction</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="129 mentions">language</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="118 mentions">latent</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="136 mentions">memory</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="93 mentions">mllm</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="80 mentions">modality</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="96 mentions">motion</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="220 mentions">multimodal</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="85 mentions">multiple</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="173 mentions">object</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="85 mentions">observation</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="73 mentions">perception</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="83 mentions">pipeline</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="111 mentions">point</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="76 mentions">policy</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="75 mentions">query</span><span class="cloud-word" style="font-size:1.79rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="228 mentions">reasoning</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="81 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="77 mentions">region</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="102 mentions">retrieval</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="93 mentions">reward</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="72 mentions">same</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="123 mentions">scene</span><span class="cloud-word" style="font-size:1.97rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 59%, var(--accent))" title="267 mentions">semantic</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="105 mentions">space</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="139 mentions">spatial</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="97 mentions">structure</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="101 mentions">supervision</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="96 mentions">support</span><span class="cloud-word" style="font-size:1.33rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="144 mentions">target</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="112 mentions">temporal</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="173 mentions">token</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="138 mentions">trajectory</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="111 mentions">understanding</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="81 mentions">unified</span><span class="cloud-word" style="font-size:2.10rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 66%, var(--accent))" title="298 mentions">video</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="75 mentions">view</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="90 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="476 mentions">visual</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="88 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>4 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>GameWAM: A World Action Model for Video Games</strong>
          <small>Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Weijia Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Game Agents</span>
<span class="topic-tag">Action Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-high">17</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2608.26200</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26200">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 3: it introduces a new world-action model for video games, combining future visual prediction with executable action generation in a closed-loop embodied setting.</p>
        <p class="abstract">Modern video games combine first-person perception, rapid visual changes, persistent world state, and heterogeneous native controls. Existing game agents map visual and task context directly to actions but lack explicit world dynamics modeling, whereas interactive game world models predict visual futures from supplied actions but do not serve as task policies. World-Action Models (WAMs) unify these objectives, but remain largely unexplored under the dynamics and open-ended interaction of video games. We introduce GameWAM, to our knowledge the first WAM for native closed-loop gameplay and GUI control. GameWAM jointly generates future visual observations and executable keyboard-mouse trajectories through parallel visual and action generative processes with block-causal conditioning and flow matching. To support joint world-action learning, we construct synchronized gameplay and GUI trajectories. To handle heterogeneous native control, GameWAM predicts a gameplay/GUI mode at each action step and generates actions with mode-specific prediction distributions and continuous-action normalization. For long-horizon interaction, block-cycle control predicts beyond the committed horizon, executes only a short action prefix, and replans from new observations, while fine-grained within-cycle context and hierarchical cross-cycle history preserve temporal continuity. Experiments demonstrate competitive task success with fewer executed native actions than the compared agents. We further uncover Low-Frequency Action Source Imprinting (LASI), in which low-frequency components of the sampled action source systematically steer coarse generated camera motion under fixed conditioning, revealing a source-sensitivity failure mode in generative control. Project page is available at https://yunncheng.github.io/GameWAM/.</p>
      </div>
    </details>


    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Decoupling Planning and Control for Instructable Agents</strong>
          <small>Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Planning-Control Separation</span>
<span class="topic-tag">Vision-Language-Action</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.MA</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2608.26788</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26788">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it proposes a new embodied-agent method that decouples planning and control, with evaluation across multiple embodied environments and multi-agent settings.</p>
        <p class="abstract">Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but lack open-ended task guidance. In this work, we combine these strengths into a single system, Instruct-to-Act, where we train a world-model controller to act autonomously at high frequency when conditioned on sparse, higher-latency, and high-level text instructions generated by a VLM planner. To train controllers to be language-instructable, we relabel segments of controller policy rollouts with synthetic instructions and jointly optimize a behavior-cloning objective along with existing reward-maximizing and world-modeling objectives. We evaluate our proposed approach across seven embodied environments, including three multi-agent environments where VLM planners coordinate through language while trained controllers serve as their actuators. Under matched observation and action spaces, our decoupled approach consistently outperforms controller-only and direct VLM action-generation variants, preserves fast control, and lets us swap in different pretrained VLM planners without fine-tuning, while remaining competitive with strong vision-language-action and multi-agent RL baselines on six of seven tasks.</p>
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
          <strong>From Atomic to Agentic: Towards Interpretable Evaluation of LLMs&#x27; Agentic Mathematical Capabilities</strong>
          <small>Jiayi Kuang, Yinghui Li, Yunze Song, Keyu Chen, Zhifeng Shen, Yangning Li, Yidong Wang, Di Yin, Ruizhi Qiao, Xing Sun, Kai Jin, Ying Shen, Liang Lin, Philip S. Yu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Agentic Reasoning</span>
<span class="topic-tag">Multimodal Math</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2608.26950</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26950">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: benchmark/evaluation for agentic mathematical capabilities, including multimodal contexts and process-level diagnostics.</p>
        <p class="abstract">Large Language Models (LLMs) are evolving from performing end-to-end mathematical reasoning to integrating agentic intelligence. However, most existing math benchmarks evaluate only final answers. This outcome-oriented evaluation provides limited diagnostic value for identifying process-level failures or rigorous logic, failing to guide the transformation of LLMs into robust agents. To bridge this gap, we present a process-level benchmark designed to evaluate the inherent agentic mathematical reasoning abilities of LLMs. Our framework aligns problem-solving agentic behaviors with a structured taxonomy of reusable mathematical atomic capabilities. We design a comprehensive suite of planning, action, and feedback tasks across both textual and multimodal contexts, supported by an automated pipeline that synthesizes high-quality trajectories and produces fine-grained annotations via controlled LLM rewriting. Experiments reveal that models with similar end-to-end accuracy can exhibit markedly different agentic capability profiles. This demonstrates that process-level evaluation is crucial for interpreting the true potential of LLMs and guiding the development of next-generation mathematical agents.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Agentic AI</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents</strong>
          <small>Yang Xiao, Yusong Sun, Haoyi Wu, Wenyang Hui, Wen Da, Zhaokai Luo, Mu Chuan, Yao Hu, Wenjie Li, Chengyue Jiang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agentic AI</span>
<span class="topic-tag">Long-Horizon Planning</span>
<span class="topic-tag">Self-Improvement</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2608.26530</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26530">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: an embodied/agentic long-horizon agent method focused on live self-improvement during execution, a novel angle compared with post-hoc self-correction.</p>
        <p class="abstract">Long-horizon agent runs generate experience that can improve both the current run and future work. Most self-improvement methods process this experience only after execution ends, so they cannot redirect the active run or immediately apply and validate lessons learned from it. We argue that self-improvement should instead be live, using emerging experience both to redirect the active run and to update the persistent harness. Existing agent architectures do not fully support this goal. Single-agent self-correction combines task execution and trajectory assessment within one context, while subagent delegation separates execution but typically cannot redirect an active subagent. We present PILOT, a supervisor-worker harness for live self-improvement through two coupled mechanisms: (1) live steering lets a separate supervisor redirect or abort the active worker during execution; and (2) live self-evolution distils procedures and failure modes revealed during execution into reusable skills and memory. Across two frozen backbones and three benchmarks, PILOT ranks first in five of six configurations. On Terminal-Bench 2.0, PILOT outperforms counterpart harnesses by up to 9.8 percentage points. In the self-improvement setting, PILOT gains 14.6 points with GLM-5.1 and 12.4 points with Kimi-K2.6. Mean output tokens fall by 42.9% and 47.4%, while successful evaluations per million output tokens rise by 110.3% and 134.0%, respectively.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>13 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City</strong>
          <small>Tianjie Ju, Zheng Wu, Yueqing Sun, Yuhan Cui, Bobo Li, Shengqiong Wu, Pengzhou Cheng, Haodong Zhao, Zongru Wu, Xinbei Ma, Doris Zhang, Kunling Li, Mong-Li Lee, Wynne Hsu, Hao Fei, Qi Gu, Gongshen Liu, Zhuosheng Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Benchmark &amp; Simulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">17</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2608.27456</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.27456">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it introduces UrbanGround, a new real-scale embodied/urban navigation sandbox for studying spatial agency and closed-loop MLLM behavior.</p>
        <p class="abstract">Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investigate how far current MLLM agents can turn local urban perception into reliable action in a complicated real-scale city. We propose UrbanGround, the first sandbox to make this question testable in a physically constrained replica of Hong Kong built from territory-wide 3D geospatial data. UrbanGround supports closed-loop interaction from a first-person view and provides an interactive map for navigation. Agents can directly enter the 3D city and explore from a first-person view. Our analysis follows the growth of the spatial problem through three research questions. We first test whether an agent can ground a local scene well enough to answer spatial questions after active observation. Then we ask whether that grounding supports navigation as destinations become farther away and less explicit. Finally, we examine whether the resulting behavior survives changes in route availability and pedestrian motion. Contemporary MLLM agents usually show useful atomic abilities in visual recognition and short-range spatial reasoning, while orientation and pedestrian-aware movement remain unreliable. Their central failure emerges over extended exploration, where local abilities do not compose into sustained goal-directed behavior and errors accumulate without effective correction. We hope UrbanGround will support broader study of how far current MLLM agents can explore reliably in complex, open-ended urban environments.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical MLLM</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation</strong>
          <small>Haowen Gu, Gensheng Pei, Junzhu Mao, Qiong Wang, Mingwu Ren, Yazhou Yao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical MLLM</span>
<span class="topic-tag">Grounded Reasoning</span>
<span class="topic-tag">Segmentation</span>
<span class="topic-tag">Vision-Language Grounding</span>
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
          <span>Paper 3 / arXiv:2608.26856</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26856">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 2: it is a grounded medical MLLM that tightly couples multimodal reasoning with pixel-level segmentation and evidence masks.</p>
        <p class="abstract">Although Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in Medical Visual Question Answering (Med-VQA), their reliance on global image features often lacks precise pixel-level grounding, thereby limiting clinical trustworthiness. To bridge the semantic gap between high-level clinical reasoning and spatial localization, we propose \textsc{\textsc{MedREAL}} (\textbf{Med}ical \textbf{RE}asoning-driven \textbf{A}nswering and \textbf{L}ocalization), a unified framework that seamlessly aligns linguistic reasoning with spatial grounding. Specifically, \textsc{MedREAL} introduces \textbf{S}eg \textbf{A}nchored \textbf{R}easoning \textbf{P}ooling (SARP) to distill task-relevant semantic evidence directly from \texttt{[SEG]} tokens within the MLLM&#x27;s hidden states. Furthermore, a \textbf{R}easoning-to-\textbf{V}isual (R2V) fusion mechanism is proposed to effectively inject these reasoning-aware features into a segmentation pipeline for accurate mask decoding. To facilitate this paradigm, we construct MedRAVS-13K, a comprehensive dataset comprising 13,824 expertly validated samples across four diverse imaging modalities. Extensive experiments demonstrate that \textsc{MedREAL} significantly outperforms state-of-the-arts, achieving 68.49\% gIoU and 70.47\% cIoU on benchmark evaluations. By generating evidence masks that are strictly consistent with textual diagnoses, \textsc{MedREAL} provides a robust, interpretable framework for reasoning-driven medical image analysis.</p>
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
          <strong>LeVJEPA: Efficient &amp; Scalable Video Pretraining without the Heuristics</strong>
          <small>Lukas Kuhn, Lucas Maes, Giuseppe Serra, Quentin Le Lidec, Yann LeCun, Randall Balestriero, Florian Buettner</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Video Pretraining</span>
<span class="topic-tag">Representation Learning</span>
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
          <span>Paper 4 / arXiv:2608.27395</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.27395">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Good match to criterion 4: this is a vision foundation model-style self-supervised video pretraining method with strong emphasis on efficient scalable representation learning.</p>
        <p class="abstract">Video carries the temporal structure of the physical world, yet learning representations from it has remained computationally expensive: prevailing self-supervised methods either prevent representation collapse through architectural asymmetries, coupling an exponential-moving-average target encoder, a stop-gradient, and a capacity-limited predictor, or circumvent it by reconstructing masked content in pixel space. We introduce LeVJEPA, the first video encoder trained under LeJEPA&#x27;s collapse-free objective, which dispenses with both. A single encoder is trained with an invariance loss over global and local views of a clip, regularized by SIGReg, which excludes collapse with a provable guarantee. The architecture reduces to an encoder and a projector, and the objective to a single hyperparameter. This formulation admits two properties. First, the cost of pretraining is governed by the number of tokens the encoder observes; uniform random token dropping renders this number small while simultaneously improving downstream accuracy. At matched epochs on identical data, LeVJEPA matches or surpasses V-JEPA 2 across ViT-S/B/L at 5.6 to 20.8x less pretraining compute, and at matched total FLOPs it exceeds the strongest video baseline by 7.6 points on ImageNet-1K while remaining competitive on motion-centric benchmarks. Second, since no asymmetry between branches is required, the encoder can be trained with block-causal attention at no measurable accuracy cost: temporal ordering becomes a property of the encoder itself. Against a compute-matched DINOv2 trained on frames of the same videos, LeVJEPA approaches the image-pretrained encoder on appearance-centric evaluation while nearly doubling its motion-centric accuracy. These results indicate that, once its computational overhead is removed, video becomes a viable and in several respects preferable substrate for general-purpose visual pretraining.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Scene Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>SpatialCrafter: Single Image World Modeling with Generative 3D Proxies</strong>
          <small>Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Scene Generation</span>
<span class="topic-tag">3D Consistency</span>
<span class="topic-tag">Video Diffusion</span>
<span class="topic-tag">Dataset Construction</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2608.27073</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.27073">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criterion 3: it proposes a new embodied/scene-generation method with a newly constructed large-scale dataset for explorable image-to-scene generation, focusing on 3D consistency and long-horizon drift.</p>
        <p class="abstract">Explorable image-to-scene generation is essential for applications in gaming, robotics, and virtual reality. Existing methods based on video diffusion model (VDM) commonly rely on incomplete conditioning signals such as sparse point clouds or 2D panoramas, leading to stochastic hallucinations, long-term drifts and suboptimal 3D consistency. We present SpatialCrafter, a novel two-stage framework that addresses these issues by introducing a global 3D proxy for high-fidelity image-to-scene generation. Specifically, we decompose the generation process into global proxy generation and appearance refinement. For proxy generation, we propose a Point-anchored Sparse Structure~(PaSS) Flow module that predicts a spatially aligned and geometrically consistent 3D proxy. For appearance refinement, we re-frame the VDM as a Generative Deferred Refiner which synthesizes high-frequency photorealistic details upon proxy-defined scene geometry. To better integrate the proxy with the pre-trained VDM, we introduce Parallel Geometry Injection and Proxy-Aware Corruption training strategies, which improve robustness to proxy artifacts without disrupting the pretrained generative manifold. Furthermore, as no suitable dataset exists for this explorable scene generation task, we construct a new large-scale dataset of 115K scenes. To the best of our knowledge, it is the first hybrid dataset for image-to-scene generation. Extensive experiments on both synthetic and real-world datasets show that SpatialCrafter outperforms state-of-the-art methods, mitigates long-term drift, and remains robust and consistent under rapid camera motion and extreme viewpoint changes. Code, models, and the newly constructed dataset will be publicly released. See more at https://fangchuan.github.io/SpatialCrafter/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video VLM</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Video-FLAIR: Not Whether to Reason, But How</strong>
          <small>Yogesh Kulkarni, Pooyan Fazli</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video VLM</span>
<span class="topic-tag">Adaptive Reasoning</span>
<span class="topic-tag">RL Training</span>
<span class="topic-tag">Multimodal QA</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2608.26495</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26495">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Good match to criterion 2: it studies a VLLM-style adaptive reasoning framework for video queries, learning when to reason perceptually vs. deliberatively.</p>
        <p class="abstract">Multimodal queries can require different types of reasoning. Some can be answered via perceptual reasoning, extracting information directly from the visual signal, while others require compositional reasoning that combines observations or deliberative reasoning that evaluates competing hypotheses. However, many existing methods apply a uniform reasoning strategy across queries, leading to unnecessary computation on simple tasks and insufficient reasoning on complex ones. We introduce Video-FLAIR, a training framework that learns to select the appropriate reasoning mode for each query using reinforcement learning. During training, the model generates responses under all three modes for the same prompt, enabling direct comparison. A composite reward compares these responses to favor the most effective one based on correctness, grounding, and cost, while discouraging unsupported or misaligned deliberation. This yields a supervision signal for learning adaptive reasoning without per-query annotations. Video-FLAIR improves accuracy over the Qwen2.5-VL base model by +5.4 on MathVista, +4.8 on Video-Holmes, and +4.8 on Video-MMMU, while reducing average token usage to 95 compared to 417 for always-thinking baselines.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">VideoLLM</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs</strong>
          <small>Ji Soo Lee, Jinyoung Park, Seohyun Lee, Jongha Kim, Joonmyung Choi, Jinsung Yoon, Hyunwoo J. Kim</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">VideoLLM</span>
<span class="topic-tag">Reasoning Distillation</span>
<span class="topic-tag">RL Fine-Tuning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2608.26684</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26684">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 moderately well: it is a VideoLLM reasoning/distillation paper with a new RL-style training framework aligned to multimodal model policies.</p>
        <p class="abstract">Recent large language models achieve strong performance on complex reasoning tasks, where reinforcement learning with Group Relative Policy Optimization (GRPO) has emerged as a leading paradigm for optimizing models on self-generated trajectories. However, the on-policy nature of GRPO bounds the model to the reasoning skills it can already produce, restricting to learn more advanced capabilities. Prior works inject privileged reasoning traces from a stronger teacher policy to guide training, yet these traces are inherently out of distribution with respect to the student policy. We observe that this mismatch between on-policy and off-policy causes gradient clipping on semantically critical reasoning tokens, ultimately rewarding correct answers while leaving the reasoning that justifies them unlearned. Hence, we propose \textbf{Echo-GRPO}, a framework that lets the model reason in the words it speaks. Rather than imitating low-probability privileged traces from the teacher model, Echo-GRPO rewrites them into the student policy&#x27;s own \textit{idiolect}, that is, its own characteristic vocabulary and expression patterns, while preserving their semantics via Dual-Reference Decoding. We instantiate this framework as \textbf{VideoEcho-R1} for video reasoning distillation, achieving consistent improvements across three multimodal LLM backbones and five benchmarks. Finally, we show that our idiolectal paraphrasing is a plug-in module that consistently improves both RL and supervised fine-tuning frameworks for reasoning distillation, demonstrating that policy-aligned supervision extends beyond GRPO.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multi-View Perception</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>GeoMAD: Geometry-Aware Multi-View Anomaly Detection via Deformable Fusion and Distributional Alignment</strong>
          <small>Shang-Fu Chen, Jhih-Ciang Wu, Kuan-Chuan Peng, Wen-Huang Cheng, Kai-Lung Hua</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multi-View Perception</span>
<span class="topic-tag">Geometric Fusion</span>
<span class="topic-tag">Anomaly Detection</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2608.26724</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26724">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: geometry-aware spatial understanding for multi-view embodied/3D perception, with deformable cross-view fusion and distributional alignment.</p>
        <p class="abstract">Multi-view anomaly detection (MvAD) detects defects by exploiting complementary observations from multiple camera viewpoints. The central challenge is to fuse views with sufficient geometric awareness while remaining scalable to multi-class industrial settings. Existing methods typically fall into two extremes: voxel-based fusion provides explicit geometric alignment but requires costly 3D construction and class-specific assumptions, whereas lightweight patch-based fusion is efficient but relies on discrete candidate matching and lacks continuous cross-view correspondence. In this paper, we propose GeoMAD, a unified multi-view, multi-class AD framework that addresses both geometric correspondence deficiency and distributional inconsistency. Our \textit{Cross-view Deformable Fusion Module} (CDFM) learns content-adaptive, view-pair-specific sampling offsets directly on 2D feature maps and arranges them across a multi-scale window pyramid with image-global reference sampling, enabling hierarchical cross-view correspondence without camera calibration, voxel construction, or class-specific 3D supervision. We further introduce \textit{Distributional View Alignment} (DVA), a self-supervised cross-view regularization loss that aligns each view&#x27;s bottleneck distribution against a per-instance view-centric target, enforcing global consistency without pixel-level correspondence. Together, CDFM and DVA bridge local geometric correspondence and global distributional consistency, providing geometry-aware and distribution-consistent fusion while preserving the efficiency of 2D feature-space learning. Extensive experiments on Real-IAD and MANTA-Tiny show that GeoMAD achieves strong detection and localization performance in unified MvAD.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Gaussian Splatting</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>KnockGS:interaction-Grounded Calibrationof Physical Gaussian Representations</strong>
          <small>Chenchen Ge, Hanwen Shen, Bowen Jing, Jiyuan Cai, Xiaofeng Wang, Hongsen Lei, Weitao Zhou, Dandan Zhang, Haibao Yu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Gaussian Splatting</span>
<span class="topic-tag">Physical Simulation</span>
<span class="topic-tag">System Identification</span>
<span class="topic-tag">Interaction Grounding</span>
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
          <span>Paper 10 / arXiv:2608.27365</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.27365">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Moderate match to criterion 3: it is an interaction-grounded simulation/calibration method for physical Gaussian representations, relevant to embodied/interactive 3D scene dynamics.</p>
        <p class="abstract">Physics-integrated 3D Gaussian representations now allow reconstructed deformable objects to be simulated and rendered under explicit material models. Existing pipelines, however, assume that material parameters are known or manually specified, limiting their applicability when these parameters must be inferred from observed object dynamics. We propose KnockGS, an interaction-response PhysicalGS framework that estimates the elasticity and density scales of a 3D Gaussian object from its dynamics under a known applied force. Rather than treating physical simulation only as a forward process, we turn the force-induced response into a calibration signal: temporal response features are xtracted from the observed dynamics, the two material scales are estimated from those features, and the estimate is then frozen and written back into the same simulator so that it can be tested on an interaction it was never fitted to.We evaluate the framework on both parameter recovery and response-level fidelity. The estimated scales are compared against hidden ground truth, and the re-simulated object is measured against the target using 3D particle trajectories, response-curve statistics, and rendered-frame quality. Across five held-out material targets, our method recovers the scales substantially more accurately than response retrieval, global regression, or a fixed default material, and the frozen estimate remains predictive under interactions that differ in direction and in magnitude. Interaction response therefore carries enough information to calibrate material scales in physically grounded 3D Gaussian representations.Our study is a first step toward interactive PhysicalGS systems that calibrate a Gaussian asset whose rendered appearance and simulated response are consistent.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Generative Retrieval</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>PailitaoGR: Latent Think-with-Images for Generative Image Retrieval</strong>
          <small>Xiaomeng Fan, Yueran Liu, Shengyu Zhou, Chenghan Fu, Wanxian Guan, Feng Li, Chuan Yu, Jian Xu, Bo Zheng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Generative Retrieval</span>
<span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Image Search</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.IR</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2608.26658</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26658">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: vision foundation model application for generative image retrieval, with a new latent think-with-images mechanism.</p>
        <p class="abstract">Generative retrieval has demonstrated strong performance by directly generating product semantic identifiers (SIDs).   Extending this paradigm to image search, however, is nontrivial because real-world query images contain diverse information, including the search target, useful auxiliary evidence, and irrelevant visual content.   This requires the model to identify and focus on the search target while selectively utilizing auxiliary evidence. In this paper, we propose \textbf{PailitaoGR}, a \emph{Latent Think-with-Images} method for generative image retrieval, which internalizes target-focused perception and selective auxiliary-evidence utilization into a the generative retrieval model, enabling \textit{Zooming without Cropping} and \textit{Reading without OCR}. Specifically, we design a target-focused perception mechanism that identifies and enhances visual tokens of the search target, consisting of a target Enhancer and a learning strategy based on on-policy distillation and attention guidance loss, enabling the model to focus on search-target regions. We also design a selective auxiliary-evidence utilization mechanism that identifies and enhances visual tokens of auxiliary evidence, including an auxiliary enhancer and an in-capacity incremental contrastive distillation strategy, enabling the model to exploit auxiliary evidence. We construct training and validation sets sampled from real-world online image-search logs. Experiments show that our method outperforms existing baselines by an average of 13.8\%, validating its effectiveness.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Local Feature Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>SSMB: Self-Supervised Local Feature Detection under Motion Blur</strong>
          <small>Zhenjun Zhao, Fabio Bellavia, Wenting Wang, Fan Zhu, Jiajun Wu, Suryansh Kumar, Mingqiang Wei, Haoang Li, Javier Civera</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Local Feature Detection</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Motion Blur</span>
<span class="topic-tag">Visual Localization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2608.27181</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.27181">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Partial match to criterion 4: it is a vision feature/keypoint method with self-supervised learning under motion blur, useful for visual localization and matching, but not a foundation model paper.</p>
        <p class="abstract">Keypoint detection under motion blur remains a significant challenge, as blur distorts local image structure and degrades the repeatability of feature localization. Existing approaches either rely on computationally expensive deblur-then-detect pipelines that may introduce restoration artifacts, or learn to regress the image positions of handcrafted keypoints extracted on sharp images, which reflects the assumptions of the handcrafted detector rather than what is truly repeatable under blur. We present SSMB, a deblur-free, self-supervised keypoint detector for motion-blurred images that requires neither handcrafted detectors nor external pseudo-labels. SSMB introduces the Local Discriminability Enhancement (LDE) module, which restores fine-grained local discriminability after global feature mixing. Training is performed in two stages. First, geometric pretraining on synthetic shapes bootstraps spatially discriminative keypoint detection without any external detector, just from the rendered geometry. Second, blur-aware training on real sharp-blur image pairs learns blur-invariant detection through a multi-component self-supervised objective that enforces cross-domain consistency, geometric alignment, and spatial coverage. Extensive evaluations on keypoint detection, image matching, relative pose estimation, and visual localization under motion blur demonstrate that SSMB establishes a new state-of-the-art among sparse keypoint detectors, consistently outperforming both supervised and self-supervised baselines across all tasks. Code, models, and datasets will be publicly available upon paper acceptance.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Reward Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>RubricRM: Generative Reward Modeling via Dynamic Rubrics for Image Generation and Editing</strong>
          <small>Zijian Kan, Wei Wang, Long Luo, Bing Zhao, Xuan Ren, Weixu Qiao, Wenbo Li, Hu Wei, Lin Qu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Reward Modeling</span>
<span class="topic-tag">Image Generation</span>
<span class="topic-tag">Image Editing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2608.26956</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26956">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 loosely: it builds a generative reward model for image generation/editing, which is adjacent to MLLMs but not itself a new VLLM/MLLM.</p>
        <p class="abstract">Reward models play an essential role in aligning visual generative models, yet most existing visual reward models use a single scalar score or rely on fixed criteria that cannot adapt to different instructions. This limits both interpretability and task sensitivity, especially for text-to-image generation and instruction-based image editing, where different inputs require different evaluation dimensions. We propose RubricRM, a pairwise generative reward modeling framework that first produces an input-specific rubric with evaluation dimensions, weights, and scoring criteria, and then applies the rubric to score candidate images. We train dedicated RubricRM models for text-to-image generation and image editing using a two-stage training pipeline: supervised fine-tuning teaches the model the rubric-based scoring paradigm, while GRPO further improves scoring through fine-grained dimension-level rewards. Experiments on multiple generation and editing benchmarks show that RubricRM outperforms existing specialized reward models and remains competitive with strong proprietary MLLM judges despite using smaller backbones. Our models, data, and code are available at https://github.com/zijiankan/RubricRM.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical VQA</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>MedFG-VQA: Low-Frequency Memory and Graph Attention for Lightweight Medical VQA</strong>
          <small>Haowen Gu, Gensheng Pei, Zeren Sun, Mingwu Ren, Xiangbo Shu, Yazhou Yao, Fumin Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical VQA</span>
<span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Cross-Attention</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2608.26848</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26848">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 only loosely: it is a vision-language medical application built around lightweight VQA, but it is not a foundation-model paper in the usual sense.</p>
        <p class="abstract">Medical Visual Question Answering (Med-VQA) holds significant promise for clinical decision support, yet faces challenges due to limited annotated data and the high computational demands of existing large vision-language models. We propose MedFG-VQA, a lightweight framework that leverages a memory bank to augment DCT-based low-frequency features and employs graph-enhanced cross-attention for effective visual-textual alignment. Specifically, our approach features two key components: Frequency-Memory Fusion (FMF), which enhances low-frequency features by retrieving from a learnable memory bank built on DCT decomposition, and Graph-Aware Cross-Attention (GACA), which aligns visual-textual features via cross-attention and refines them through graph-convolutional aggregation. To address data scarcity, we construct SynMed-VQA, a large-scale synthetic dataset comprising over 2 million question-answer pairs across 9 imaging modalities and 10 major organs, generated with GPT-4o. Extensive experiments on SynMed-VQA and three other standard biomedical VQA benchmarks demonstrate that MedFG-VQA achieves competitive or superior performance compared to much larger models while maintaining significantly lower computational costs, highlighting its efficiency and potential for clinical deployment.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical AI</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Surgical Video Generation From Diffusion to World Models: A Survey</strong>
          <small>Fuxiang Huang, Chenxu Zhang, Liang Han, Lei Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical AI</span>
<span class="topic-tag">Video Generation</span>
<span class="topic-tag">World Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2608.26214</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.26214">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>3</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only indirectly as a survey on surgical video generation and world models; it is more of a review than a new embodied method or benchmark.</p>
        <p class="abstract">Surgical video data provides the primary training resource for models of intraoperative perception, surgical workflow understanding, and robotic decision-making. However, clinical data acquisition remains constrained by privacy, cost, and class imbalance. Surgical video generation has emerged as a transformative approach to addressing data scarcity and as a foundation for surgical simulation, training, and robotic policy learning. The field has developed rapidly without a clear conceptual framework. This survey organizes the 2024-2026 literature into three categories: unconditional generation, conditional generation, and world modeling generation, revealing a fundamental shift in how the task is defined from synthesizing visually plausible frames to modeling the causal dynamics of surgical scenes. We examine the persistent gap between pixel-level fidelity and clinical plausibility, and identify generalization, physical realism, controllability, and interpretability as bottlenecks. We further summarize experimental results of representative methods on public datasets to provide a quantitative reference for the field. This survey provides a structured overview of the current state and open challenges, offering a reference for researchers working at the intersection of intelligent perception, multi-modal fusion, generative AI, and surgical data science.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-08-14.html">
          <span>August 14, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-13.html">
          <span>August 13, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-12.html">
          <span>August 12, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-11.html">
          <span>August 11, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-10.html">
          <span>August 10, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-07.html">
          <span>August 07, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-06.html">
          <span>August 06, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-05.html">
          <span>August 05, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-04.html">
          <span>August 04, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-08-03.html">
          <span>August 03, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-31.html">
          <span>July 31, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-30.html">
          <span>July 30, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-29.html">
          <span>July 29, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-28.html">
          <span>July 28, 2026</span>
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
