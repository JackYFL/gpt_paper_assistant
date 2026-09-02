

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
      <p class="eyebrow">Daily ArXiv / September 02, 2026</p>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="9 mentions">action</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">adversarial</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">agent</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">architecture</span><span class="cloud-word" style="font-size:2.09rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 65%, var(--accent))" title="12 mentions">attention</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">attribute</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">camera</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">diagnostic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">discovery</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">environment</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">error</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">exact</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">feedback</span><span class="cloud-word" style="font-size:2.24rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 73%, var(--accent))" title="13 mentions">figure</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">finding</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="9 mentions">generation</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">hallucination</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">hyperedge</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">mllm</span><span class="cloud-word" style="font-size:2.09rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 65%, var(--accent))" title="12 mentions">multimodal</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">object</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">observation</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">pair</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">pathology</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">pattern</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">perturbation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">qwen</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">reasoning</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">refinement</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="10 mentions">region</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">relative</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">robot</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">scaffold</span><span class="cloud-word" style="font-size:2.51rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 87%, var(--accent))" title="15 mentions">scientific</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">semantic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">slide</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">spatial</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">structured</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">targeted</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">temporal</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">trajectory</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">video</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="9 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="17 mentions">visual</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.23rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="122 mentions">action</span><span class="cloud-word" style="font-size:1.67rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="191 mentions">agent</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="100 mentions">alignment</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="86 mentions">attention</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="78 mentions">change</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="72 mentions">complementary</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="92 mentions">consistency</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="86 mentions">control</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="74 mentions">dense</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="117 mentions">detection</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="86 mentions">diffusion</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="74 mentions">distribution</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="95 mentions">dynamic</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="75 mentions">editing</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="75 mentions">environment</span><span class="cloud-word" style="font-size:1.85rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 53%, var(--accent))" title="223 mentions">evidence</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="84 mentions">fine-grained</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="99 mentions">frame</span><span class="cloud-word" style="font-size:1.86rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 53%, var(--accent))" title="225 mentions">generation</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="73 mentions">generative</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="75 mentions">geometric</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="99 mentions">inference</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="115 mentions">interaction</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="105 mentions">language</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="112 mentions">latent</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="126 mentions">memory</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="79 mentions">mllm</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="97 mentions">motion</span><span class="cloud-word" style="font-size:1.70rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="195 mentions">multimodal</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="83 mentions">multiple</span><span class="cloud-word" style="font-size:1.54rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="169 mentions">object</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="89 mentions">observation</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="73 mentions">perception</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="77 mentions">pipeline</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="104 mentions">point</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="77 mentions">policy</span><span class="cloud-word" style="font-size:1.83rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="219 mentions">reasoning</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="82 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="81 mentions">region</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="86 mentions">retrieval</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="87 mentions">reward</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="149 mentions">scene</span><span class="cloud-word" style="font-size:2.04rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 63%, var(--accent))" title="260 mentions">semantic</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="93 mentions">space</span><span class="cloud-word" style="font-size:1.39rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="145 mentions">spatial</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="98 mentions">structure</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="72 mentions">structured</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="106 mentions">supervision</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="84 mentions">support</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="134 mentions">target</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="106 mentions">temporal</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="151 mentions">token</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="141 mentions">trajectory</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="94 mentions">understanding</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="79 mentions">unified</span><span class="cloud-word" style="font-size:2.09rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 65%, var(--accent))" title="270 mentions">video</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="81 mentions">view</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="101 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="428 mentions">visual</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="94 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>11 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving</strong>
          <small>Xin Zhou, Zongchuang Zhao, Zhibo Yang, Mingsheng Li, Humen Zhong, Shuai Bai, Du Chu, Ruizhe Chen, Zhaohai Li, Jun Tang, Qiuyue Wang, Mingkun Yang, Jiazhao Zhang, Dayiheng Liu, Dingkang Liang, Xiang Bai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Vision-Language Foundation Models</span>
<span class="topic-tag">3D Perception</span>
<span class="topic-tag">Motion Planning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2609.00111</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00111">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 2: a vision-language foundation model for autonomous driving with explicit 3D perception and motion planning in a unified framework.</p>
        <p class="abstract">We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving. Qwen-Drive-1.0 retains the architecture of the pretrained vision-language model (VLM) and integrates 3D perception, visual question answering, and motion planning within a unified framework. An external bird&#x27;s-eye-view (BEV) perception head jointly performs 3D object detection, semantic occupancy prediction, and BEV map segmentation. It serves as a probe of the 3D information accessible from the shared representations and provides an explicit, inspectable interface to 3D scene structure. A Planning Expert conditions on shared VLM representations to generate future ego trajectories. A staged training recipe combines driving supervision with general-purpose vision-language data to acquire driving-specific competence while helping preserve broad visual understanding and instruction-following capabilities. Experiments demonstrate strong 3D perception and driving scene understanding while largely preserving general vision-language capability. Comprehensive evaluations across open-loop, pseudo-closed-loop, and closed-loop settings further show highly competitive motion-planning performance.</p>
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
          <strong>ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training</strong>
          <small>Xionghao Wu, Yijun Yang, Shiyang Zhou, Haoze Sun, Jianhui Liu, Songsong Yu, Jiyao Zhang, Wenbo Li, Bo Wang, Guoqing Ma, Lin Song, Renjie Liao, Shenghe Zheng, Wei Tang, Xiaojuan Qi, Yanwei Li, Yuan Zhang, Zhuotao Tian, Haoyang Huang, Nan Duan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Robot Manipulation</span>
<span class="topic-tag">Video Pretraining</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2609.00188</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00188">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: this is an embodied AI method for learning world action models from large-scale video, aimed at robot control and generalization.</p>
        <p class="abstract">Robotic manipulation faces a fundamental scaling challenge: robust generalization demands broad physical experience, yet action-labeled robot trajectories are expensive to collect and inherently limited in diversity. Egocentric videos offer a far more scalable source of embodied experience, capturing object interactions, contact dynamics, tool use, and long-horizon behaviors across diverse environments. The central challenge is how to convert this abundant but action-free experience into effective robot control. We introduce ZimaBlue, a scalable framework for learning generalizable World Action Models (WAMs) from large-scale video. ZimaBlue follows a three-stage training curriculum: it first performs causal embodied video pre-training on large-scale human and robot egocentric videos, then grounds the learned visual dynamics in heterogeneous robot trajectories through video-action mid-training with a unified action representation, and finally specializes the model to a target robot for deployment. To make generative WAMs practical for real-time control, ZimaBluefurther adopts an asynchronous Slow-Fast dual-system architecture, where a high-capacity Slow world model provides generalizable spatiotemporal representations and a lightweight Fast branch enables 30 Hz action prediction on NVIDIA RTX 4090. On real-robot zero-shot evaluations, scaling from target-robot data alone to over 120,000 hours of embodied video improves success from 36.1% to 77.8%. ZimaBlue further delivers strong performance across multiple benchmarks, with particularly pronounced gains on unseen tasks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal LLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>Beyond Language Priors: Diagnosing and Fixing Visual-Origin Hallucinations in Multimodal LLM</strong>
          <small>Peiyang Xu, Xiaopei Zhu, Jun Zhu, Xiaolin Hu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Hallucination</span>
<span class="topic-tag">Model Diagnosis</span>
<span class="topic-tag">Contrastive Fine-Tuning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2609.00231</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00231">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: it is a multimodal LLM paper focused on diagnosing and fixing hallucinations in MLLMs, with a concrete method and empirical analysis.</p>
        <p class="abstract">Existing research on object hallucination in multimodal large language models (MLLMs) predominantly attributes the problem to language priors such as over-reliance on textual co-occurrence statistics. We challenge this view by presenting quantitative evidence for a complementary, under-explored cause: visual-origin hallucination, where hallucinations arise from incorrect visual feature extraction and misalignment between image and text embeddings. Through cosine similarity analysis and Smooth Grad-CAM entropy measurements, we show that hallucinated samples exhibit systematically lower image-text similarity (average 0.158 vs. -0.122) and inverted attention patterns, where attention is dispersed when the target object is present but wrongly concentrated when it is absent. Guided by this diagnosis, we propose Adversarial Contrastive Fine-Tuning (ACFT). ACFT uses an Adversarial Hallucination Attribute Flipping (AHAF) procedure, involving minimal, targeted adversarial perturbations that flip an image&#x27;s hallucination attribute, to construct perfectly aligned positive-negative pairs, which are then used for contrastive fine-tuning. AHAF simultaneously serves as a diagnostic probe, revealing that MLLM visual representations lie dangerously close to hallucination decision boundaries. Requiring only 0.9% of the COCO dataset and adding zero inference overhead, ACFT achieves state-of-the-art performance on POPE, MME, and four description-level hallucination benchmarks across LLaVA, MiniGPT-4, and Qwen2.5-VL. Code is available at https://github.com/zxp555/ACFT_MM</p>
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
          <strong>Benchmarking Vision-Language Models for Automated Pathology Diagnosis and Report Generation</strong>
          <small>Yumi Lee, Harim Oh, Hyoryung Kim, Minji Kim, Eunsu Kim, Hyeseong Lee, Junya Fukuoka, Andrey Bychkov, Jijgee Munkhdelger, Rajiv Kumar Kaushal, Ayushi Sahay, Rajni Yadav, Bharathi Prabakaran, Sulen Sarioglu, Serdar Balc{\i}, Ilknur Turkmen, Yuri Tolkach, Christian Harder, Julian Westerdorf, Reinhard Buettner, Audun Ljone Henriksen, Sepp De Raedt, Byung Hyun Lee, Sungjin Lim, Joohoon Lee, Gwanghyun Kim, Se Young Chun, Suryakant Singh, Saarthak Kapse, Prateek Prasanna, Kyung A Kim, Yousun Kang, Sehwan Yoo, Sungman Hong, Shubham Innani, Michael Feldman, Spyridon Bakas, Ujjwal Baid, Prasad Dutande, Suhas Gajare, Bhakti Baheti, Serkan S\&quot;okmen, Ece Tu\u{g}ba Cebeci, Ahmet Hal{\i}c{\i}, Musa Balc{\i}, Kardelen Pe\c{c}enek, Srividhya Sainath, Kyongseok Jang, Messi H. J. Lee, Noorul Wahab, Bodong Du, Jiaming Zhang, Qixiang Zhang, Jang-Hwan Choi, Sangjeong Ahn</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Medical AI</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Report Generation</span>
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
          <span>Paper 4 / arXiv:2609.00866</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00866">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 3: a benchmark paper for vision-language models in pathology report generation, with systematic evaluation and analysis of model failures.</p>
        <p class="abstract">The rapid advancement of vision-language models (VLMs) has accelerated progress in computational pathology; however, whole-slide image (WSI)-based pathology report generation remains limited by the scarcity of large-scale WSI--report datasets and the complexity of mapping spatially distributed visual patterns to structured clinical text. To address this, we introduce a clinically curated Pan-Asia WSI--report dataset of approximately 10,500 pairs from five institutions and establish the REG 2025 benchmark through a MICCAI challenge for systematic evaluation of multimodal models. We analyze submitted methods spanning pretrained VLMs, multiple-instance learning frameworks, hierarchical expert models, retrieval-augmented generation, and cross-modal Transformers. Rather than indicating that VLM use alone was sufficient for superior performance, the results suggest that top-performing methods benefited from structured report representations, hierarchical diagnostic decomposition, and effective multimodal grounding. We identify key limitations, including instability in quantitative attribute estimation (e.g., numeric hallucination) and a tendency toward diagnostic overspecification, with some errors resembling known diagnostic pitfalls in routine pathology. These findings establish REG 2025 as a benchmark for evaluating WSI-based structured report generation and vision-language understanding in computational pathology, providing insights for the design of clinically grounded multimodal pathology models.</p>
      </div>
    </details>


    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>Visual Attention Faithfulness in Vision-Language Models is Heterogeneous</strong>
          <small>Xurui Song, Weishi Wang, Zhongqi Yue, Kuluhan Binici, Tao Bai, Hongxin Shao, Daniel Dahlmeier, Jun Luo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Attention Faithfulness</span>
<span class="topic-tag">Causal Analysis</span>
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
          <span>Paper 16 / arXiv:2609.00830</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00830">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: an analysis paper on visual attention faithfulness in vision-language models, with surprising empirical findings about heterogeneity.</p>
        <p class="abstract">Whether attention weights faithfully reflect model reasoning has been actively debated in NLP, yet this question remains largely unexplored for the visual modality in Vision-Language Models (VLMs). We address this gap through causal perturbation analysis on current VLMs, evaluating both the comprehensiveness and sufficiency gap of attention-ranked visual tokens. Our analysis reveals that visual attention faithfulness is heterogeneous, manifesting in three distinct processing modes: Faithful-Sufficient, where top-$k$ attention tokens are both necessary and sufficient for prediction; Faithful-Distributed, where they are necessary but broader visual context remains required; and Non-Focal, where no localized attention region is individually necessary while visual information remains an essential trigger for prediction. Furthermore, human-annotated ground-truth regions satisfy comprehensiveness in only $\sim 60$% of cases compared with model attention rankings, revealing systematic divergence between model visual reliance and human intuition. We demonstrate these patterns across both general VQA on VQAv2 and document tasks on VRDU and ChartQA, showing that visual attention faithfulness varies systematically with processing demands and model architectures rather than being uniformly faithful or unfaithful.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Self-Supervised Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison</strong>
          <small>Thibaut Loiseau, Guillaume Bourmaud, Vincent Lepetit</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">3D Vision</span>
<span class="topic-tag">Cross-View Pretraining</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2609.01530</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.01530">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: it is a vision pretraining method for cross-view completion and 3D understanding, with a useful self-supervised co-visibility signal.</p>
        <p class="abstract">Self-supervised pre-training via cross-view completion learns strong features for 3D vision from co-visible regions of image pairs. However, the reference view provides little information for reconstructing non-co-visible patches, implicitly yielding a monocular training signal in these regions. We introduce Gekko, which turns this limitation into a useful signal. The relative improvement of the cross-view reconstruction error over a masked-autoencoder error is a self-supervised proxy for co-visibility: large improvements indicate co-visible regions, negligible ones non-co-visible areas. Gekko is a network, trained from scratch, that jointly performs cross-view completion, masked autoencoding, and per-pixel prediction of this relative improvement, providing an additional binocular signal for all masked regions without any ground-truth 3D annotation. Under identical architectures and training data, Gekko consistently outperforms CroCo on zero-shot correspondence estimation, relative pose estimation, and pointmap regression, with up to 6 times higher accuracy at the strictest relative-pose threshold and a 22% drop in end-point error on ETH3D. The extra channel it learns is itself a strong co-visibility detector on unseen scenes, and Gekko&#x27;s frozen features outperform released cross-view backbones of comparable or larger size. It can also be trained directly from raw videos with a simple stride-based curriculum, removing the cumbersome 3D preprocessing prior methods require while matching models trained on curated data. Code and pre-trained models are publicly available.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>ViTAL-X: Video-Text Alignment with Cross-Modal Temporal Edits</strong>
          <small>Sethuraman T V, Savya Khosla, Onkar Kishor Susladkar, Aditi Tiwari, Seoung Wug Oh, Kushal Kafle, Joon-Young Lee, Derek Hoiem, Simon Jenni</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video-Language Models</span>
<span class="topic-tag">Temporal Reasoning</span>
<span class="topic-tag">Self-Supervised Learning</span>
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
          <span>Paper 10 / arXiv:2609.00505</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00505">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: a video-text alignment method and benchmark diagnostic for temporal reasoning, relevant to vision foundation model applications.</p>
        <p class="abstract">Video-text models adapted from image-text architectures (e.g., CLIP) frequently exhibit temporal blindness, the inability to perceive fundamental cues like order, direction, and motion dynamics. Standard datasets mask this limitation by enabling models to exploit static spatial shortcuts. To systematically evaluate this, we introduce XTE-Bench, a diagnostic probe revealing that even large-scale video-language models struggle with basic temporal reasoning, indicating that parameter scaling alone is insufficient to resolve this flaw. To address this, we propose Cross-Modal Temporal Edits (XTE), a self-supervised framework that injects precise temporal supervision. By performing synchronized video-text transformations, XTE generates hard temporal negatives without manual annotation. We instantiate this with ViTAL-X, a lightweight model that equips frozen image-text backbones with temporal awareness while preserving their foundational spatial knowledge. Across six temporal benchmarks, ViTAL-X achieves state-of-the-art performance. Utilizing only 0.4B parameters and 1M training clips, ViTAL-X outperforms 7B-parameter models and surpasses baselines trained on 600x more data. These results demonstrate that targeted, high-quality temporal alignment provides a highly efficient alternative to pure scaling.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>MeRoPE: Metric Rotary Position Embedding for Camera-Controlled Video Generation</strong>
          <small>Zhijian Qiao, Xinjiang Wang, Jiajie Chen, Haoming Huang, Meng Li, Chih-Chung Chou, Jing Wang, Shaojie Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Camera Control</span>
<span class="topic-tag">Positional Encoding</span>
<span class="topic-tag">3D Geometry</span>
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
          <span>Paper 11 / arXiv:2609.01252</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.01252">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Partial match to criterion 1: introduces a new positional encoding for camera-controlled video generation that improves geometry-aware spatial conditioning.</p>
        <p class="abstract">In camera-controlled video generation, geometry-aware positional encodings condition tokens on camera extrinsics and per-token viewing rays. Existing schemes, however, have a scale-dependent failure mode on real-world metric camera trajectories: homogeneous projective encodings cause attention logits and feature norms to grow unbounded with physical translation baselines. We propose MeRoPE (Metric Rotary Position Embedding), a norm-preserving relative camera encoding for attention. MeRoPE encodes relative orientations between calibrated viewing rays with orthogonal rotation blocks, maps raw metric displacements into multi-frequency rotary phases, and adds a disparity-anchored correspondence prior along the epipolar arc. This design strictly preserves feature norms, bounds pre-softmax attention logits regardless of the physical translation scale, and maintains exact invariance to global rigid coordinate changes. Across nuScenes and PanShot, which cover large-baseline trajectories and diverse camera optics, respectively, MeRoPE achieves stronger camera control than prior encodings, with the best consistency between generated camera motion and conditioning poses in both rotation and translation. Code will be made publicly available.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical AI</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Instance-Guided Report Anchoring for Text-Free 3D Abnormality Segmentation in Chest CT</strong>
          <small>Zhenyu Bu, Haoyan Ding, Chushu Shen, Xinyuan Zheng, Peiyu Duan, Xueqi Guo, Sepehr Farhand, Yoshihisa Shinagawa, Gerardo Hermosillo, Chaowei Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical AI</span>
<span class="topic-tag">Vision-Language Grounding</span>
<span class="topic-tag">3D Segmentation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2609.00447</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00447">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely in the medical vision-language setting: it uses report anchoring for 3D segmentation and removes text at inference, which is a neat multimodal grounding trick.</p>
        <p class="abstract">Accurate 3D abnormality segmentation in chest CT requires dense spatial supervision, but obtaining expert voxel-level labels is costly. Radiology reports, however, are routinely generated during clinical interpretation and contain instance-specific descriptions that can provide additional guidance without new dense annotation. Existing vision-language grounding methods typically require report-derived findings at inference, making localization dependent on paired text and limiting each forward pass to a queried finding. We propose Instance-Guided Report Anchoring (IGRA), a model-agnostic module that preserves the correspondence between each annotated abnormality instance and the report finding that describes it. IGRA pools each instance representation and anchors it to the corresponding finding embedding during training; all text-related components are discarded at inference. We further reformulate free-text grounding on ReXGroundingCT as multi-label volumetric segmentation by merging same-category instances, allowing all abnormality categories to be predicted in one image-only forward pass. IGRA improves Dice by 22.5% over the strongest image-only baseline (30.93 vs. 25.25) and is comparable to VoxTell on the single-finding subset (30.29 vs. 30.43). Applied unchanged to four standard 3D segmentation backbones, IGRA improves Dice and hit rate across all architectures. Zero-shot evaluation on LIDC-IDRI, PleThora, and a private in-house dataset further shows consistent gains over image-only baselines.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>ExBind: A Controlled Diagnostic Benchmark for Visual-to-Executable Correspondence</strong>
          <small>Ziqian Wang, Yuxiao Cheng, Tingxiong Xiao, Jinli Suo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multimodal Agents</span>
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
          <span>Paper 13 / arXiv:2609.01344</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.01344">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately well: a new benchmark for visual-to-executable correspondence, which is relevant to embodied/interactive agents and tool-use localization.</p>
        <p class="abstract">Multimodal coding and editing systems must map a visible or semantic referent to the exact executable object that can be edited. A wrong reference may select a valid but incorrect DOM node, SVG element, graph endpoint, hierarchy member, or table cell, while final execution success alone does not reveal the source of the failure. ExBind isolates this visual-to-executable correspondence layer as a controlled diagnostic benchmark between semantic localization and action execution. It samples representation-independent latent binding instances and compiles them into SVG, DOM, canvas, tree, graph, and table cases with deterministic mappings to executable references. Models output only a strict reference; the evaluator maps predictions back to latent structure and scores structural constraints without requiring reasoning traces. The release contains a 250-case broad suite, a disjoint 240-case targeted suite, and 50 paired latent groups. Qwen2.5-VL-3B achieves 98.4% candidate validity but 76.4% exact accuracy, while Qwen3-VL-4B achieves 100.0% validity and 98.8% exact accuracy. In the targeted table suite, all Qwen2.5-VL-3B residual errors are valid correct-row/wrong-column selections. Candidate-order perturbations change case-level outcomes while preserving this error pattern. ExBind is designed for controlled diagnosis rather than population-scale ranking or end-to-end editing evaluation. Code and benchmark records are available at https://github.com/Daerwang2020/Exbind and https://huggingface.co/datasets/Ziqianwwww/ExBind.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Large Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>Forbid Your Attention: Fooling Multimodal Large Language Models by Selectively Removing Intrinsic Focus in Spectral Domain</strong>
          <small>Daizong Liu, Junhao Dong, Zhiyuan Ma, Xiaoye Qu, Xiang Fang, Runwei Guan, Keke Tang, Jianfeng Dong, Yew-Soon Ong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Large Language Models</span>
<span class="topic-tag">Adversarial Attacks</span>
<span class="topic-tag">Robustness</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2609.00788</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00788">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Only a partial fit: it studies MLLMs, but the paper is about adversarial attacks rather than a new VLLM/MLLM capability or embodied/spatial method.</p>
        <p class="abstract">Multimodal large language models (MLLMs) have extended the capability of large language models (LLMs) to process more contextual multimodal information, showing remarkable progress in diverse realistic multimodal applications. Despite their strong perception and reasoning abilities, recent studies reveal that MLLMs remain highly vulnerable to adversarial inputs, especially those targeting visual components. However, existing attacks mainly focus on global perturbations, lacking an understanding of how MLLMs internally interpret visual structures. In this paper, we make the attempt to investigate the intrinsic focus of MLLMs in the frequency domain and discover that their predictions are particularly sensitive to phase information, which encodes essential structural and semantic cues. Based on this observation, we propose a novel phase-aware adversarial attack framework that explicitly restricts adversarial perturbations to structure-relevant phase regions to suppress the MLLMs&#x27; focus for effective and imperceptible attacks. To further amplify the structural influence, we also introduce an auxiliary adversarial prompt learning module to guide multimodal misalignment around phase-sensitive regions, misleading the MLLM&#x27;s attention toward targeted structural patterns. Extensive experiments on multiple representative MLLM models and datasets demonstrate the superior effectiveness of our method compared to existing attacks.</p>
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
      <summary class="topic-heading">Document Layout</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>ReDeck: Step-Level Render-Grounded Refinement for Document-to-Slide Generation</strong>
          <small>Muzhao Tian, Zezi Zeng, Yifan Yang, Xin Gao, Yan Li, Zisu Huang, Xiaohua Wang, Changze Lv, Mingxi Cheng, Bei Liu, Kai Qiu, Qi Dai, Dong Chen, Yue Dong, Xiaoqing Zheng, Ji Li, Chong Luo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Document Layout</span>
<span class="topic-tag">Agentic Generation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Spatial Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2609.00194</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00194">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: an embodied-style agentic system for document-to-slide generation with render-grounded refinement and a new benchmark emphasizing spatial correctness.</p>
        <p class="abstract">Document-to-slide generation is challenging because slides are dense editable artifacts that require both faithful content selection and precise spatial layout. Recent slide agents adopt iterative reflection, but typically follow a monolithic &quot;one version, one feedback&quot; loop: a slide or deck is rewritten, rendered afterward, and critiqued only at the turn boundary. This delayed feedback makes local failures such as overflow, overlap, clipping, and off-canvas placement difficult to attribute and repair. We propose ReDeck, a step-level render-grounded refinement framework that decomposes slide revision into atomic edit actions and returns renderer-derived observations after each step, turning refinement into &quot;one edit, one observation.&quot; To balance local repair with global quality, ReDeck uses multi-granular feedback: step-level render feedback for spatial errors, a turn-level adaptive critic for semantic and design guidance, and a submission-level gate for hard layout validation. We further introduce DeckQuiz, a benchmark that decouples content fidelity, spatial correctness, and design quality. Across GPT-5.4, Claude-4.6, and Gemini-3.1, ReDeck consistently outperforms existing slide-generation agents, and ablations confirm that feedback timing and granularity are critical for reliable slide refinement.</p>
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
          <strong>UI-Venus-2 Technical Report</strong>
          <small>Venus Team, Zhuohan Cai, Haoxing Chen, Jiaxuan Chen, Weizhi Chen, Changlong Gao, Zhangxuan Gu, Yuan Guo, Yusong Hu, Jianrong Jiang, Jianguo Li, Runze Li, Jinzhen Lin, Zhenyu Ma, Changhua Meng, Han Peng, Xinyu Qiu, Shuheng Shen, Zhongyi Shui, Weiqiang Wang, Ming Wen, Zhuoer Xu, Hang Yan, Kaiwen Yang, Ruilin Yao, Nanjun Yu, Zhengwen Zeng, Lianrui Zhang, Yunzhu Zhang, Zhe Zhao, Beitong Zhou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Agents</span>
<span class="topic-tag">GUI Automation</span>
<span class="topic-tag">Foundation Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2609.00028</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00028">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: this is a technical report for a general-purpose multimodal GUI agent/foundation model with closed-loop reasoning and action.</p>
        <p class="abstract">Multimodal GUI agents have emerged as a promising paradigm for digital task automation, yet transitioning from benchmark-oriented models to dependable real-world applications remains challenging due to limited environment coverage, brittle task construction, and unreliable reward verification. In this work, we present UI-Venus-2, a general-purpose foundation GUI agent designed to operate across mobile, web, and desktop environments through a unified closed-loop reasoning-action framework. To bridge the gap toward practical deployment, we jointly scale three critical dimensions: (1) Environments, expanding coverage to more than 170 multilingual mobile apps and native desktop operating systems; (2) Tasks, employing a deep-research pipeline for function-grounded instruction generation; and (3) Verification, adopting trace-level and sample-level evaluators with visual keypoints and multi-model voting to ensure reliable RL signals for training. Furthermore, we integrate safety-aware mechanisms to ensure controlled execution of consequential actions. By offering a capable, efficient, and open-source foundation, UI-Venus-2 advances the field toward more generalizable, verifiable, and self-reflective agents for real-world applications.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Can LLMs Discover Scientific Laws in Real and Parallel Worlds?</strong>
          <small>Yiming Huang, Ziche Liu, Zhuohang Wu, Yiqian Wang, Junxia Cui, Xinkai Zou, Linjun Mao, Nan Huang, Naicheng Yu, Kaijie Zhu, Yue Ma, Kun Zhou, Letian Peng, Jingbo Shang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Scientific Discovery</span>
<span class="topic-tag">LLM Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2609.01552</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.01552">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely as a new benchmark for scientific-law discovery with an active &#x27;parallel worlds&#x27; setting; also likely to appeal for its empirical findings on memorization and selection bottlenecks.</p>
        <p class="abstract">Scientific equation discovery has long been central to scientific progress, proceeding through iterative cycles of hypothesis generation, observational testing, and refinement under scientific constraints. As LLM capabilities advance and their role in AI for Science expands, it remains an open problem whether they can genuinely discover scientific laws and how this ability should be evaluated. Existing evaluations, however, often either simplify discovery through synthetic settings or reuse published targets that may already be familiar to LLMs. We therefore introduce SCILAWS-BENCH, a benchmark for scientific law discovery built from published research and real scientific data. It comprises 118 problems drawn from 381 scientific papers, covering 291 candidate laws and roughly 8M real data points across six scientific disciplines. Each problem is instantiated in two complementary settings: (1) SCILAWS-REAL asks models to propose laws from fixed real observations and evaluates held-out predictive fit and scientific validity derived from the source literature, and (2) SCILAWS-PARALLEL asks models to actively query residual-calibrated worlds and recover synthesized hidden laws derived from published forms. This two-setting task design preserves each problem&#x27;s scientific context while separately evaluating fixed-record law discovery and active recovery of a newly synthesized hidden law. We find that predictive fit can diverge from scientific validity, memorization shapes whether models reproduce or move beyond published formulas, and our best-of-N study reveals a selection bottleneck. Our work provides a paper-grounded benchmark and new empirical perspectives for evaluating AI for scientific discovery. Project page: https://yiyihum.github.io/SciLaws-Bench</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Figures as Programs: Recursive Generation of Editable Scientific Figures</strong>
          <small>Yepeng Liu, Dasen Dai, Chengzhi Liu, Yiren Song, Hai Ci, Yu Zhang, Qi Zhang, Mike Zheng Shou, Xin Eric Wang, Yuheng Bu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Scientific Figure Generation</span>
<span class="topic-tag">Multi-Agent Systems</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.GR</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2609.01006</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.01006">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it is a vision/foundation-model-style system for generating editable scientific figures, with recursive multimodal figure construction and repair.</p>
        <p class="abstract">Scientific methodology figures are essential for communicating complex methods clearly, yet creating them remains labor-intensive and typically requires multiple rounds of refinement. Recent image-generation models can synthesize visually appealing raster figures, but producing a human-satisfactory result in a single generation step remains difficult. Moreover, precise edits to raster figures are challenging for both humans and models. We formulate scientific figure generation as recursive SVG program construction and propose \textsc{FigTree}, a \textit{multi-agent} system that automatically transforms a scientific paper into a structured vector figure. \textsc{FigTree} grounds figure content in the source paper, decomposes a figure into a hierarchy of local regions, generates each region as a short SVG program, and assembles the resulting fragments. A render-critic refinement loop jointly inspects the rendered figure and its underlying program, enabling visual defects to be traced to specific statements and accurately repaired. We conduct extensive evaluations of \textsc{FigTree} on figure quality and editability, showing that \textsc{FigTree} produces high-quality figures, while also enabling more effective editing than existing raster-based methods.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Data</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>SCAFFOLD: A Large-Scale Structured Dataset of Computer Science Research Figures with Diagram QA and Chain-of-Thought Reasoning Traces</strong>
          <small>Ranjit Raut, Aarav Subedi, Sagun Rai, Sudan Jha</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Data</span>
<span class="topic-tag">Diagram QA</span>
<span class="topic-tag">Dataset Construction</span>
<span class="topic-tag">Scientific Figures</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2609.00018</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00018">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 4 loosely: a new structured dataset for diagram QA and CoT reasoning aimed at training vision-language models on scientific figures.</p>
        <p class="abstract">Computer science papers rely heavily on diagrams: architecture drawings, system flowcharts, and pipeline schematics that often carry more information than the text around them. There is currently no public dataset that pairs this specific kind of figure with captions, context, questions, answers, and step-by-step reasoning, which is exactly what is needed to train a vision-language model to understand them. We present \textbf{SCAFFOLD}\footnote{https://github.com/theranjitraut/scaffold}, a large-scale structured dataset of computer science research figures with diagram QA and Chain-of-Thought reasoning traces. This dataset consists of (image, caption, context, question-answer, chain-of-thought) tuples from arXiv computer science papers prepared using layout detection and PDF parsing, with an AI-assisted question-generation step. The resulting large-sized SCAFFOLD-157K dataset spans 3,058 papers with 29,887 figures (157,387 pairs), a medium-sized SCAFFOLD-37K dataset (36,797 pairs), and a small-sized SCAFFOLD-12K dataset (12,000 pairs). We used SCAFFOLD-12K for baseline experiments on Qwen2.5-VL-3B-Instruct.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>HyperWorld: Hypergraph-Structured State Serialization Improves Learned Textual World Models</strong>
          <small>Yun-Jian Zhang, Chen-Wei Liang, Tian-Yi Zhang, Jian Ding, Yi-Lun Wu, Ao-Bo Li, Wei-Cong Su, Saifullah, Hong-Yu An, Mu-Jiang-Shan Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Embodied Agents</span>
<span class="topic-tag">State Serialization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2609.00002</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00002">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a new method study for textual world models in embodied/agentic settings, focusing on state serialization as an underexplored design choice.</p>
        <p class="abstract">World models enable language-model agents to predict environment dynamics and plan before acting. In text environments, the model must learn symbolic action effects from serialized state descriptions, but the role of serialization structure remains underexplored. We present HyperWorld, a controlled study of state serialization for learned textual world models. We compare raw observations with three symbolic serializations of the same ground-truth state: independent sentences, pairwise triples, and entity-centered hyperedge units that group multiple related facts around entities and relations. All variants use the same training objective: given a state and an action, predict symbolic effects or judge the action infeasible. Across model scales, data budgets, and in-distribution and out-of-distribution test worlds, hyperedge serialization gives the clearest gains for 0.5B--1.5B models and under distribution shift. Larger models reduce the gap, and pairwise triples can match or slightly exceed hyperedges on in-distribution exact match, but hyperedges achieve the strongest out-of-distribution fact F1 and the best small-to-medium scale trade-off between feasibility detection and effect prediction. In downstream greedy planning, the hyperedge world model also attains the highest success rate among the tested representations. These results show that higher-order state organization is a simple but effective inductive bias for learned symbolic world models, especially when model capacity is limited or test environments differ from training.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning</strong>
          <small>Yuanjun Zhang, Fuzel Ahamed Shaik, Suvojit Acharjee, Fahad Khalid, Mourad Oussalah</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Preference Optimization</span>
<span class="topic-tag">Multimodal Disaster Assessment</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2609.00879</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.00879">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: a new multimodal system built on vision-language reasoning with SFT+DPO alignment for disaster assessment.</p>
        <p class="abstract">Reliable disaster damage assessment requires models that provide both accurate predictions and transparent explanations. However, existing multimodal approaches are limited by scarce annotated data and insufficient evaluation of reasoning quality. This study proposes a two-stage training framework that integrates Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) within a unified data construction pipeline. From a single Human-in-the-Loop (HITL) annotation workflow, two complementary datasets are derived, namely ReasoningSet, which contains validated rationales for SFT, and PreferenceSet, which comprises paired rationales for DPO-based alignment. The framework evaluates both classification performance and explanation quality using automatic metrics, model-based scoring, and human ranking. Experimental results show that SFT improves accuracy from 73.64% to 78.29% and increases Macro-F1 by 29% compared to the baseline, while explanation quality improves by approximately 25%. Subsequent DPO alignment further enhances interpretability on the PreferenceSet. Cross-model validation on InternVL-3-8B and LLaVA-1.5-7B demonstrates the robustness and generalizability of the approach. The proposed framework improves detection of underrepresented mild damage cases, reduces high-risk misclassifications, and strengthens alignment between model reasoning and human judgment. Overall, it provides a reproducible pathway to develop reliable multimodal systems that deliver auditable, actionable disaster insights for emergency management.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
