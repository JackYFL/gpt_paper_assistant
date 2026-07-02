

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
      <p class="eyebrow">Daily ArXiv / July 02, 2026</p>
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
      <strong>16</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="7 mentions">action</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">agent</span><span class="cloud-word" style="font-size:2.42rem;opacity:0.91;color:color-mix(in srgb, var(--accent-2) 82%, var(--accent))" title="11 mentions">alignment</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="6 mentions">anchor</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">anomaly</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="7 mentions">boundary</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">challenging</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">consistency</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="7 mentions">defect</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">dense</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="6 mentions">detection</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">dynamic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">encoder</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">endpoint</span><span class="cloud-word" style="font-size:1.83rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="8 mentions">evidence</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="7 mentions">geometric</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">hallucination</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">improving</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">inference</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">instance</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="6 mentions">language</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">localization</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">manipulation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">mobile</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">multimodal</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="6 mentions">object</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="6 mentions">pipeline</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">produce</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">progressively</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">query</span><span class="cloud-word" style="font-size:2.60rem;opacity:0.96;color:color-mix(in srgb, var(--accent-2) 91%, var(--accent))" title="12 mentions">reasoning</span><span class="cloud-word" style="font-size:2.03rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 62%, var(--accent))" title="9 mentions">reconstruction</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">recover</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="6 mentions">segmentation</span><span class="cloud-word" style="font-size:1.83rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="8 mentions">semantic</span><span class="cloud-word" style="font-size:1.83rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="8 mentions">spatial</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">table</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">target</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="6 mentions">temporal</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">textual</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">token</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="5 mentions">trajectory</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="7 mentions">video</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="7 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="13 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="80 mentions">action</span><span class="cloud-word" style="font-size:2.04rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 63%, var(--accent))" title="203 mentions">agent</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="71 mentions">alignment</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="64 mentions">architecture</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="76 mentions">attention</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="58 mentions">camera</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="62 mentions">consistency</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="60 mentions">control</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="63 mentions">detection</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="61 mentions">diffusion</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="65 mentions">domain</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="72 mentions">driving</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="100 mentions">dynamic</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="68 mentions">editing</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="60 mentions">error</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="137 mentions">evidence</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="75 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="65 mentions">foundation</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="63 mentions">frame</span><span class="cloud-word" style="font-size:1.84rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="173 mentions">generation</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="63 mentions">geometric</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="69 mentions">geometry</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="73 mentions">inference</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="74 mentions">interaction</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="65 mentions">knowledge</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="130 mentions">language</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="72 mentions">latent</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="71 mentions">mechanism</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="134 mentions">memory</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="74 mentions">mllm</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="101 mentions">motion</span><span class="cloud-word" style="font-size:1.80rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="168 mentions">multimodal</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="66 mentions">multiple</span><span class="cloud-word" style="font-size:1.48rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="126 mentions">object</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="70 mentions">optimization</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="62 mentions">paradigm</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="82 mentions">pipeline</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="73 mentions">policy</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="75 mentions">real-world</span><span class="cloud-word" style="font-size:2.45rem;opacity:0.92;color:color-mix(in srgb, var(--accent-2) 83%, var(--accent))" title="271 mentions">reasoning</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="84 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="65 mentions">region</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="62 mentions">reward</span><span class="cloud-word" style="font-size:1.54rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="133 mentions">scene</span><span class="cloud-word" style="font-size:1.80rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="167 mentions">semantic</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="73 mentions">space</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="128 mentions">spatial</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="63 mentions">structured</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="79 mentions">supervision</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="59 mentions">support</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="75 mentions">target</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="110 mentions">temporal</span><span class="cloud-word" style="font-size:1.63rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="145 mentions">token</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="85 mentions">trajectory</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="91 mentions">understanding</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="77 mentions">unified</span><span class="cloud-word" style="font-size:2.20rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 71%, var(--accent))" title="228 mentions">video</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="72 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="332 mentions">visual</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="84 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>12 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>OmniView-Space: Reinforcing Spatial Reasoning via Multi-Perspective Spatial Mapping</strong>
          <small>Xudong Li, Mengdan Zhang, Peixian Chen, Jiaxi Tan, Zihao Huang, Jingyuan Zheng, Yan Zhang, Xiawu Zheng, Xing Sun, Rongrong Ji</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Multimodal Large Language Models</span>
<span class="topic-tag">Egocentric Mapping</span>
<span class="topic-tag">Embodied AI</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2607.00881</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00881">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match to criteria 1 and 2: it targets spatial intelligence for MLLMs and proposes a new spatial reasoning framework with multi-perspective mapping and egocentric tool-guided reasoning.</p>
        <p class="abstract">Spatial intelligence remains a persistent challenge for Multimodal Large Language Models (MLLMs), as it requires coherent spatial scene representations beyond basic object recognition. Existing methods typically build such representations through textual reasoning or 3D reconstruction. However, they often falter during multi-step reasoning, particularly when required to dynamically re-anchor evidence to the specific camera-, object-, or direction-centric reference frames demanded by complex queries. To address this, we propose OmniView-Space, a framework designed to maintain spatial consistency through multimodal egocentric evidence. Our approach consists of three core components: (1) Multi-Perspective Spatial Mapping (MPSM), which re-anchors reconstructed geometry into a query-aligned visual cognitive map and a textual spatial graph; (2) Tool-Guided Egocentric Reasoning, an interleaved policy trained to actively select the ego anchor required by the query and request the corresponding MPSM evidence; and (3) Cognitive-Map Distillation, which uses MPSM-generated trajectories and ego-frame rewards to train the model to reason with self-generated cognitive maps. Experiments on single- and multi-image spatial reasoning benchmarks show that OmniView-Space achieves state-of-the-art performance. Furthermore, the distilled model maintains this performance while reducing reliance on external geometry pipelines.</p>
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
          <strong>ABot-M0.5: Unified Mobility-and-Manipulation World Action Model</strong>
          <small>Ronghan Chen, Yandan Yang, Zuojin Tang, Dongjie Huo, Tong Lin, Haoning Wu, Haoyun Liu, Yuzhi Chen, Lulu Zheng, Botai Yuan, Tianlun Li, Mingxin Wang, Dekang Qi, Bin Hu, Wei Mei, Yuze Xuan, Haolong Yang, Yanqing Zhu, Mu Xu, Zhiheng Ma, Xinyuan Chang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Mobile Manipulation</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Robot Control</span>
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
          <span>Paper 2 / arXiv:2607.00678</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00678">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied AI method for mobile manipulation/world action modeling with explicit alignment for long-horizon robot control.</p>
        <p class="abstract">Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics, suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space, and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local visual state transitions and serve as an bridging action space between video latents and embodiment-specific controls. To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent world-action modeling.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Pretraining</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>LeVLJEPA: End-to-End Vision-Language Pretraining Without Negatives</strong>
          <small>Lukas Kuhn, Giuseppe Serra, Randall Balestriero, Florian Buettner</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Pretraining</span>
<span class="topic-tag">Foundation Models</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Dense Representations</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2607.00784</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00784">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it proposes a new vision-language pretraining method without negatives, with direct implications for vision foundation models and dense semantic features.</p>
        <p class="abstract">Vision-language pretraining remains dominated by contrastive objectives, whereas vision-only self-supervised learning has largely adopted non-contrastive methods. At the same time, the role of vision-language encoders has shifted: they are increasingly deployed not as zero-shot classifiers but as the frozen visual backbone of vision-language models and dense prediction systems, which consume the full grid of patch tokens rather than a single pooled embedding. We introduce LeVLJEPA, the first fully non-contrastive end-to-end vision-language pretraining method. LeVLJEPA learns through cross-modal prediction with stop-gradient targets and per-modality distributional regularization, without negatives, temperature, momentum encoder, or teacher-student schedule, and trains stably at large scale. We find that the resulting encoder provides markedly stronger dense semantic features for downstream use: as a frozen vision-language-model backbone, LeVLJEPA is the strongest of the evaluated encoders across GQA, VQAv2, and POPE under two distinct language models, and outperforms contrastive baselines on semantic segmentation, while remaining on par on global readouts such as linear probing. These results establish non-contrastive pretraining as an effective means of producing dense semantic vision features.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Remote Sensing</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>GeoSearcher: Anchor-Guided Progressive Reasoning for Remote Sensing Visual Grounding with Process Supervision</strong>
          <small>Dianyu Wang, Yidan Zhang, Peirong Zhang, Xuyang Li, Xiaoxuan Liu, Lei Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Visual Grounding</span>
<span class="topic-tag">Process Supervision</span>
<span class="topic-tag">Multimodal LLMs</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2607.01050</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.01050">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and criterion 3 closely: an MLLM-based method for remote sensing visual grounding with progressive reasoning and process supervision, emphasizing a novel spatial localization formulation.</p>
        <p class="abstract">Recent multimodal large language models (MLLMs) have shown strong cross-modal understanding and coordinate generation abilities in visual grounding. However, transferring these abilities to remote sensing visual grounding (RSVG) remains challenging. High-resolution remote sensing images usually cover large-scale scenes, where targets are often extremely small and surrounded by numerous visually similar distractors. Meanwhile, queries often contain multiple clues, such as reference objects, spatial relations, and target attributes. Existing MLLM-based methods usually formulate RSVG as one-step coordinate generation, which may lead to unstable predictions for small-object localization and complex queries. To address these challenges, we propose GeoSearcher, which reformulates RSVG as an anchor-guided progressive reasoning process and realizes it through two coupled stages: Anchor-Centric Reasoning Supervised Fine-Tuning (ACR-SFT) and Process-Faithful Group Relative Policy Optimization (PF-GRPO). In ACR-SFT, anchor-centric reasoning data are used to teach the model to represent key visual clues as anchors and progressively integrate location, relational, and attribute clues around them. In PF-GRPO, Process-Aware Reward (PAR) and Reasoning-Informative Sample Selector (RISS) further optimize this reasoning behavior by jointly evaluating key reasoning steps and target localization, while focusing training on samples that are more beneficial for improving progressive reasoning. Through this design, GeoSearcher transforms large-scale visual search into a more constrained local reasoning process. Extensive experiments on DIOR-RSVG, OPT-RSVG, and VRS-Bench show that GeoSearcher outperforms existing state-of-the-art methods. The project will be released at https://github.com/wangdianyu954-xixi/GeoSearcher.</p>
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
          <strong>GenAU: Language-Grounded Industrial Anomaly Understanding with Vision-Language Models</strong>
          <small>Hongkuan Zhou, Tristan Rehm, Nadeem Nazer, Lavdim Halilaj, Jingcheng Wu, Steffen Staab</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Industrial Anomaly Detection</span>
<span class="topic-tag">Grounded Segmentation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2607.01049</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.01049">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 2 quite closely: it is a new VLM-based method for spatial localization/segmentation in industrial anomaly understanding, with language-grounded pixel-level queries.</p>
        <p class="abstract">Industrial inspection requires more than binary anomaly detection: a practical system should determine whether an anomaly exists, localize the defective region, identify the defect type, and provide interpretable visual evidence. Existing CLIP-based methods detect and localize anomalies well but offer limited language-level defect understanding, while instruction-tuned vision-language models can describe defects but do not natively produce pixel-level masks. We introduce GenAU, a Generalist vision-language framework for industrial Anomaly Understanding that unifies image-level detection, pixel-level segmentation, multi-type anomaly detection, and defect analysis in a single instruction-following model. GenAU augments a vision-language model with two segmentation tokens, [SEG_defect] and [SEG_normal], whose hidden states act as language-grounded queries over multi-scale visual features for pixel-level localization; the image-level score fuses this map with the decoder&#x27;s textual normal/defect decision, while the language decoder produces structured defect-aware responses. Trained with a joint language-modeling and segmentation objective, GenAU covers all four tasks within one architecture and recipe, adding zero-shot multi-type detection and language-grounded defect analysis at a quantified cost to detection and segmentation. Across cross-dataset benchmarks, GenAU attains the strongest image-level detection among CLIP-based zero-shot methods on VisA and Real-IAD, with segmentation approaching but not surpassing specialized CLIP baselines.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Inference</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Radial Interaction Tomography: Recognizing Non-Transitive Evolutionary Games from One Range-Expansion Image</strong>
          <small>Faruk Alpay, Baris Basaran</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Inference</span>
<span class="topic-tag">Computational Biology</span>
<span class="topic-tag">Inverse Problems</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">q-bio.PE</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2607.00378</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00378">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 in a novel way: this is a computer-vision inverse problem for spatial/mechanistic inference from a single image, with strong emphasis on observability and statistical testing.</p>
        <p class="abstract">Colored sectors in a microbial range expansion encode more than lineage survival counts. We formulate a computer-vision inverse problem: from one endpoint image of an accretive multi-type expansion, recover the radius-indexed pairwise boundary-flow field and test whether the visual pattern is compatible with a transitive scalar fitness hierarchy. The observable is a geometric signal extracted from sector-boundary curves in log-polar coordinates. We prove endpoint observability and stability for frozen fronts, weighted transitive/cyclic decomposition, contact-complete circular design, physical-clock and mechanism non-identifiability, exact Gaussian cyclicity testing, and Bonferroni-valid interval scanning. The benchmark is deterministic: analytic endpoint images, blurred/noisy pixel round trips, scalar-null stress tests, public-image tracing, multi-resolution mechanistic endpoints, and a non-learning frozen-front simulator. The implementation recovers pairwise edge-flow histories from endpoint images, detects cyclic residuals in a mechanistic four-type expansion, and uses those residuals as forcing signals for a dimensionless active design-control layer covering reaction-diffusion control, phenotype-frontier optimization, protocol synthesis, Monte Carlo robustness, and a downstream population-state bridge.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical AI</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Synergistic Perception-Reasoning Governance: Grounding Medical MLLMs with Verifiable Anatomical Evidence</strong>
          <small>Rui Hao, Qiankun Li, Junyuan Mao, Linghao Meng, Dirui Xie, Dayu Tan, Zhigang Zeng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical AI</span>
<span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Hallucination Mitigation</span>
<span class="topic-tag">Visual Grounding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2607.00060</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00060">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it is a medical MLLM method that directly targets hallucination mitigation in visual-language reasoning with training-free evidence injection.</p>
        <p class="abstract">Multimodal large language models (MLLMs) show strong promise for clinical VQA and radiology report generation, yet inference-time hallucinations still undermine trustworthy use: models can produce fluent conclusions that conflict with imaging evidence. Existing mitigation strategies typically rely on additional training, external retrieval/knowledge bases, or multi-stage post-hoc verification, which increases cost and pipeline complexity and often generalizes poorly across models and tasks.To address this, we propose a holistic, training-free evidence-injection framework that systematically mitigates hallucinations through dual-side evidence injection. By leveraging ROI priors acquired using MedSAM in our implementation, we recalibrate the visual perception trajectory via ROI-guided activation modulation while anchoring the textual reasoning trajectory by mapping anatomical coordinates into discrete semantic tokens as verifiable external memory. Then we introduce a task-aware dynamic router to select modality-specific interventions based on task semantics, balancing perceptual grounding and linguistic fluency. We conduct systematic evaluations on 2 tasks and 5 datasets using \texttt{LLaVA-1.5-7B}, \texttt{LLaVA-Med-1.5-7B}, \texttt{Qwen3-VL-8B/32B}, and \texttt{InternVL-3.5-8B/38B}. Controlled ablations and visualizations further validate the framework, which consistently outperforms baselines across medical benchmarks, improving close-ended accuracy by up to $\sim\mathbf{6}\%\uparrow$ and reducing open-ended hallucinations by $\sim\mathbf{35}\%\downarrow$. The code has been made available on GitHub: \href{https://github.com/Henry991115/SPRG}{\textcolor{blue}{https://github.com/Henry991115/SPRG}}.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Reconstruction</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>LIST3R: Long-sequence Instance-aware 3D Reconstruction</strong>
          <small>Jing Gao, Wei Wang, Feiran Wang, Yan Yan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Scene Memory</span>
<span class="topic-tag">Instance Awareness</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2607.00375</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00375">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 loosely: it is a spatial-memory-inspired 3D reconstruction method with instance-aware long-horizon scene organization, but it is not embodied AI or a VLLM paper.</p>
        <p class="abstract">We present LIST3R, an instance-aware framework for long-sequence 3D reconstruction inspired by the way humans organize spatial memory around stable and recognizable objects. LIST3R organizes long-sequence reconstruction around instance anchors, using them to reconnect fragmented subsequences and consolidate local observations into a coherent global 3D scene. Given a long video, our approach partitions it into overlapping subsequences and builds a structured local instance library for each partial reconstruction, maintaining persistent trackable anchors with semantic and geometric evidence. These anchors are matched across subsequences to recover revisited regions and provide object-aware constraints for fragment alignment, producing a consistent global reconstruction. During this process, the evolving geometric evidence updates the local instance libraries and progressively organizes them into a unified global 3D instance library. Experiments on long-sequence benchmarks show that our method produces more accurate trajectories and higher-quality 3D reconstructions, highlighting the effectiveness of persistent instance anchors for organizing long-horizon 3D reconstruction. Our code is available on the project page: https://yixn965.github.io/LIST3R/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Vision</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Robust 3D Alignment of Generative Reconstructions via Partial Monocular Observations</strong>
          <small>Yuchen Zhang, Luanyuan Dai, Yiwei Wang, Xiwei Xu, Jianing Zhang, Johnny. r. zhang, Xianhui Meng, Yanbiao Ma, Jiayi Ma, Xiaoshuai Hao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Vision</span>
<span class="topic-tag">Generative Reconstruction</span>
<span class="topic-tag">Geometric Alignment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2607.00498</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00498">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 somewhat: it uses generative 3D priors and robust alignment for partial monocular observations, which is relevant to vision foundation model applications, though not a foundation model itself.</p>
        <p class="abstract">Aligning generative 3D reconstructions with partial monocular observations is a critical but under-explored challenge in computer vision. This task is inherently ill-posed due to severe asymmetries between noisy, sparse monocular inputs and dense generative priors, whose scale ambiguity and geometric hallucinations, combined with the lack of initial overlap, render traditional registration pipelines ineffective. To resolve these issues, we propose a training-free and interpretable geometric alignment framework that grounds generative 3D priors via a 3D similarity transformation (Sim(3)), which can recover accurate metric scale and pose. Specifically, we introduce an explicit scale factor to resolve metric ambiguity and employ a coarse-to-fine alignment strategy, leveraging geometry-aware descriptors for robust initialization and a decoupled closed-form solver for precision refinement. In addition, we introduce a Hallucination Filtering operation to effectively suppress outliers caused by hallucinated geometry. To evaluate alignment performance under these extreme conditions, we introduce GenPMOAlign--Where2Place, a rigorous benchmark specifically designed for Generative-to-Partial Monocular Observational Alignment. Experiments demonstrate that our method achieves stable and accurate registration, substantially outperforming both classical geometric pipelines and state-of-the-art learning-based baselines. Code and the benchmark will be publicly released.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video-Text Alignment</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>MoVA: Learning Asymmetric Dual Projections for Modular Long Video-Text Alignment</strong>
          <small>Peiyuan Zhu, Shaoan Xie, Zijian Li, Yifan Shen, Namrata Deka, Harsh Shrivastava, Guangyi Chen, Kun Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video-Text Alignment</span>
<span class="topic-tag">Contrastive Learning</span>
<span class="topic-tag">Representation Learning</span>
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
          <span>Paper 11 / arXiv:2607.00858</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00858">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 weakly: it is a vision-text representation learning paper and could be useful for vision foundation model alignment, but it is not a foundation model itself.</p>
        <p class="abstract">Contrastive pre-training has propelled video-text alignment, yet models often inherit the critical limitations of their image-text predecessors like CLIP, resulting in entangled representations. These challenges are severely exacerbated by two fundamental properties in the video domain: Temporal Misalignment, where textual descriptions often correlate only to specific, constrained temporal windows, leaving other frames text-irrelevant; and Semantic Asymmetry, which dictates a sparse, bidirectional, and non-equivalent relevance between frame-level visual details and caption-level concepts. This failure persists whether captions are short and temporally disjoint, creating ambiguity, or long and detailed, fostering entanglement between static objects and their temporal evolution. In this paper, we establish theoretical conditions that enable flexible alignment between video and text representations across the temporal dimension and at varying levels of granularity. Building on these theoretical insights, we introduce MoVA, Modular Long Video-Text Alignment, which learns dual asymmetric projections: a text-side projection that adaptively selects frame-aware subspaces of the caption, and a video-side projection that disentangles text-relevant visual concepts. Our framework ensures that the model can preserve global cross-modal semantics while disentangling evolving, frame-specific concepts and scale naturally to long captions and videos. Empirical evaluations show that MoVA outperforms existing methods in multiple video-text alignment tasks, demonstrating the effectiveness of our method.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Imaging</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>AnF-DiffPET: Anatomy- and Frequency-Guided Diffusion for PET/CT Denoising</strong>
          <small>Xuepeng Liu, Ruili Li, Zetong Liu, Renyiming Li, Yan Li, Yin Dai, Chao Li, Yueyang Teng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Imaging</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Anatomy Guidance</span>
<span class="topic-tag">Image Denoising</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2607.00509</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00509">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately: a vision-foundation-style anatomical guidance framework applied to PET/CT denoising with diffusion models, though it is a domain-specific medical imaging method.</p>
        <p class="abstract">Positron emission tomography (PET) provides essential functional information for disease assessment, however reducing injected activity or acquisition time produces low-dose (LD) PET with stronger count dependent noise and less reliable uptake quantification. Diffusion models offer a promising solution for PET denoising by progressively recovering high-dose (HD) PET images from LD inputs. However, LD-to-HD PET denoising is still challenging due to insufficient anatomical guidance, unstable multi-scale feature propagation, and uncertain frequency domain uptake recovery. We propose AnF-DiffPET, an anatomy- and frequency-guided diffusion framework for computed tomography (CT) conditioned LD PET denoising. The framework integrates Anatomical-Frequency Guidance (AFG), Multi-Scale Cross-Transformer Reconstruction (MSCTR), and Frequency-Contrastive Hard Mining (FCHM) to enhance anatomy aware feature modulation and frequency domain consistency during denoising. Experimental results across four PET/CT datasets show that the proposed method improves image fidelity, anatomical consistency, and quantitative fidelity over representative CNN-based, GAN-based, transformer-based, and diffusion-based methods. The code and trained models will be publicly released upon acceptance.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Document AI</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>ConRTF: Edge-Constrained Boundary Distribution Refinement for Realtime TransFormer Table Structure Recognition</strong>
          <small>Eliott Thomas, Tri-Cong Pham, Mickael Coustaty, Aurelie Joseph, Gaspar Deloin, Vincent Poulain d&#x27;Andecy, Jean-Marc Ogier, Antoine Doucet</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Document AI</span>
<span class="topic-tag">Table Structure Recognition</span>
<span class="topic-tag">Detection &amp; Localization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">6</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2607.00734</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00734">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>3</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 weakly: it is a new method for table structure recognition in document images, but not an embodied-AI benchmark or spatial-intelligence paper.</p>
        <p class="abstract">Table Structure Recognition (TSR) aims to recover the row and column layout of tables from document images, a key step in document understanding pipelines. Accurate TSR depends on precise boundary localization: small errors in row or column boundaries can propagate into incorrect cell assignments and structural inconsistencies. Yet detection-based approaches treat table elements as generic objects, ignoring a fundamental property of table layout: rows and columns play structurally distinct roles and their boundaries carry unequal importance. We propose an Edge-constrained Fine-grained Localization loss (EFL) that formalizes this structural asymmetry by encoding table-specific geometric priors into the training objective: row-like elements are supervised with emphasis on their horizontal boundaries, while column-like elements prioritize vertical boundaries. Implemented within a real-time detector with distribution-based boundary refinement (D-FINE), EFL operates during training only and guides boundary refinement toward structurally meaningful adjustments with no change to the inference pipeline. The proposed approach, ConRTF, is also data-efficient, maintaining robust accuracy with as few as 2k--3k annotated tables. Experiments on PubTables-1M and two private datasets show consistent improvements over the optimized baseline and several real-time detectors including RT-DETRv2 and YOLOv10-11, with gains of up to +1.6 GriTS points at equal inference speed.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>1 paper</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>PHREEQC-MCQ-200: A Diagnostic Benchmark for Tool-Augmented Scientific Simulator Agents</strong>
          <small>Ke Zhang, Sahchit Chundur, Mohammad Javad Qomi, Maziar Raissi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Tool-Augmented Agents</span>
<span class="topic-tag">Scientific Simulators</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2607.00436</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.00436">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it is a new benchmark for tool-augmented scientific simulator agents, with a diagnostic angle that emphasizes simulator access, failure modes, and protocol sensitivity.</p>
        <p class="abstract">Large language model agents are increasingly connected to scientific software, yet it remains unclear when tool access makes scientific computation more reliable rather than merely more complex. We introduce PHREEQC-MCQ-200, a benchmark for evaluating tool-augmented agents on deterministic aqueous-geochemistry simulations. The benchmark contains 200 multiple-choice questions derived from 21 validated PHREEQC scenarios, requiring agents to construct simulator inputs, execute PHREEQC, inspect structured outputs, and commit to final answers.   Across multiple frontier and mid-tier model families, simulator access substantially improves aggregate accuracy, confirming that grounded execution is necessary for many scientific-computation tasks. However, the gains are not monotonic: tool-augmented agents also lose items they answered correctly without tools, revealing regressions that average accuracy alone hides. We further show that output-access protocol matters. A table-of-contents interface can reduce token cost while preserving or improving accuracy for stronger models, but it degrades performance for mid-tier models that cannot reliably navigate structured simulator outputs.   PHREEQC-MCQ-200 therefore frames scientific tool use as an end-to-end diagnostic problem rather than a simple tool-calling capability. We argue that evaluations of scientific agents should report not only accuracy, but also item-level retention, output-access sensitivity, trajectory failures, and where the computation chain breaks.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-06-18.html">
          <span>June 18, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-17.html">
          <span>June 17, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-16.html">
          <span>June 16, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-15.html">
          <span>June 15, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-12.html">
          <span>June 12, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-11.html">
          <span>June 11, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-10.html">
          <span>June 10, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-09.html">
          <span>June 09, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-08.html">
          <span>June 08, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-06.html">
          <span>June 06, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-05.html">
          <span>June 05, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-04.html">
          <span>June 04, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-03.html">
          <span>June 03, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-02.html">
          <span>June 02, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-06-01.html">
          <span>June 01, 2026</span>
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
