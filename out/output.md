

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
      <p class="eyebrow">Daily ArXiv / September 22, 2026</p>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.24rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 73%, var(--accent))" title="13 mentions">action</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">agent</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">annotation</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">answer</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">behavior</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="10 mentions">candidate</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">causal</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">causalwm</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">chart</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">detection</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">distribution</span><span class="cloud-word" style="font-size:2.24rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 73%, var(--accent))" title="13 mentions">dynamic</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="10 mentions">embedding</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">embodied</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">evidence</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">fixed</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">forest</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">geometry</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="9 mentions">latent</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">model&#x27;</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">multimodal</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">object</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">occupancy</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">onlinewm</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">predict</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">pretraining</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">reasoning</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">region</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">risk</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">risk-aware</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">room</span><span class="cloud-word" style="font-size:2.09rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 65%, var(--accent))" title="12 mentions">scene</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">self-supervised</span><span class="cloud-word" style="font-size:2.09rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 65%, var(--accent))" title="12 mentions">semantic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">spatial</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">structure</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="6 mentions">supervised</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">target</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="9 mentions">temporal</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="8 mentions">trajectory</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="7 mentions">unified</span><span class="cloud-word" style="font-size:2.38rem;opacity:0.9;color:color-mix(in srgb, var(--accent-2) 80%, var(--accent))" title="14 mentions">video</span><span class="cloud-word" style="font-size:2.09rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 65%, var(--accent))" title="12 mentions">visual</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="17 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.69rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="136 mentions">action</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="144 mentions">agent</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="59 mentions">alignment</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="70 mentions">annotation</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="71 mentions">attention</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="57 mentions">backbone</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="62 mentions">camera</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="66 mentions">consistency</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="61 mentions">control</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="57 mentions">dense</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="66 mentions">detection</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="56 mentions">driving</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="108 mentions">dynamic</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="59 mentions">environment</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="146 mentions">evidence</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="55 mentions">foundation</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="58 mentions">future</span><span class="cloud-word" style="font-size:2.30rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="215 mentions">generation</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="64 mentions">geometry</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="66 mentions">grounding</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="69 mentions">inference</span><span class="cloud-word" style="font-size:1.25rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="90 mentions">interaction</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="98 mentions">language</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="63 mentions">latent</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="66 mentions">memory</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="62 mentions">mllm</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="108 mentions">motion</span><span class="cloud-word" style="font-size:1.79rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="148 mentions">multimodal</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="66 mentions">multiple</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="122 mentions">object</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="99 mentions">observation</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="63 mentions">optimization</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="60 mentions">perception</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="56 mentions">pipeline</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="78 mentions">point</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="61 mentions">query</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="61 mentions">question</span><span class="cloud-word" style="font-size:1.87rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="158 mentions">reasoning</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="55 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="63 mentions">region</span><span class="cloud-word" style="font-size:1.69rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="136 mentions">scene</span><span class="cloud-word" style="font-size:1.87rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="157 mentions">semantic</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="67 mentions">space</span><span class="cloud-word" style="font-size:1.48rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="113 mentions">spatial</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="55 mentions">structure</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="55 mentions">structured</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="67 mentions">supervision</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="76 mentions">support</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="88 mentions">target</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="94 mentions">temporal</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="54 mentions">textbf</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="93 mentions">token</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="106 mentions">trajectory</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="75 mentions">understanding</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="59 mentions">unified</span><span class="cloud-word" style="font-size:2.23rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 72%, var(--accent))" title="205 mentions">video</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="63 mentions">view</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="73 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="289 mentions">visual</span><span class="cloud-word" style="font-size:1.39rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="103 mentions">world</span></div>
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
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>Look Where It Counts: A Free, Label-Free Visual Evidence Signal for Fine-Grained Vision-Language Reasoning</strong>
          <small>Santi Ram Tiwari, Nihal Naik, Devbrat Pandey, Nishant Sinha</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">MLLM</span>
<span class="topic-tag">Visual Evidence Localization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">eess.IV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2609.24244</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.24244">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: a new MLLM/VLM reasoning method centered on label-free visual evidence localization and fine-grained vision-language reasoning.</p>
        <p class="abstract">Multimodal large language models (MLLMs) fail at fine-grained visual questions less because they cannot reason than because they never see the evidence: high-resolution images are downsampled before encoding, so the model answers from linguistic priors. The standard remedies are expensive: annotated answers (SFT), hand-engineered verifiers (RLVR), or a large external teacher (on-policy distillation). We ask whether the visual evidence itself can supply the signal for free. We formalize the contrastive evidence gap, the per-token log-likelihood ratio that a model assigns to its own output when conditioned on a question-relevant region versus an irrelevant one, and study it across Qwen2.5-VL-7B, Qwen3-VL-8B, and Qwen3-VL-30B-A3B on V*Bench. Our main positive result is training-free: selecting the candidate crop under which the model&#x27;s answer distribution is most peaked, using a single-view, label-free criterion, discovers the answer-bearing region with no bounding boxes, training, or labels. It localizes the target 4.4 to 5.1 times better than chance and raises fine-grained accuracy from 70 percent to 85 percent at inference. We further show that the gap is complementary to the model&#x27;s own confidence. Combining them predicts correctness better than either alone, with AUC up to 0.99, and flags confidently wrong answers, with AUC ranging from 0.97 to 1.00 within the high-confidence subset. All effects concentrate on perception-bottleneck questions and vanish on a global-context control. Finally, we report an honest negative result: converting the same signal into a training method, gated self-distillation (SEG-Distill), does not outperform the base model at pilot scale across three gate designs, while more aggressive gating degrades accuracy. The signal is real, but converting it into training gains remains an open problem.</p>
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
          <strong>CausalWM: Causal Chain-of-Thought Reasoning for Embodied World Model</strong>
          <small>Ziming Xu, Shuang Liang, Ruobing Han, Ziqiao Xi, Mingxing Rao, Kun Zhou, Zijun Zhang, Yuchen Yan, Yufan Wei, Junbo Huang, Yifei Shao, Fang Nan, Biwei Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied World Models</span>
<span class="topic-tag">Causal Reasoning</span>
<span class="topic-tag">Future Video Prediction</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2609.23184</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.23184">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: an embodied world model with explicit causal reasoning for future video prediction and improved physical dynamics understanding; also fits criterion 3 as a new embodied AI method.</p>
        <p class="abstract">Embodied world models learn to predict future physical dynamics from visual observations and control signals, where physical knowledge is implicitly entangled within latent representations. We introduce CausalWM, a 16B embodied world model that performs explicit causal chain-of-thought reasoning before future video prediction. CausalWM organizes useful variables into a reasoning trajectory, allowing the model to progressively capture causal dependencies underlying physical evolution. To train CausalWM, we collect 31K hours embodied data and develop a three-stage paradigm consisting of large-scale video pre-training, causal CoT mid-training, and multi-objective RL post-training. Despite using only a limited set of supervised CoT variables, CausalWM exhibits emergent in-context learning capabilities, enabling contextual visual feature guidance and efficient few-step generation. CausalWM achieves state-of-the-art performance across language-conditioned, action-conditioned, single-view and multi-view benchmarks, including Top-1 performance on TriWorldBench leaderboard.</p>
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
          <strong>HappyWorld-Bench</strong>
          <small>Zhiqi Bai, Junai Cai, Yixin Chen, Jingrun Du, Tao Feng, Wei Gong, Siyuan Huang, Xiao Lin, Jiaheng Liu, Jun Luo, Yongzhe Lyu, Liya Ma, Zenan Meng, Lin Qu, Wenbo Su, Jiaming Wang, Qinghe Wang, Shaofei Wang, Yanghai Wang, Zequn Wang, Ziming Wang, Hu Wei, Jiangtao Wu, Ruiqi Wu, Jiaxin Xie, Yuchi Xu, Ze Xu, Chengting Yu, Liangyu Yuan, Gang Zeng, Yawen Zeng, Xingyao Zhang, Zizheng Zhang, Bo Zheng, Jiancheng Zhu, Song-Chun Zhu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Embodied AI</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2609.24308</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.24308">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a benchmark for world models, including spatial and embodied world-model evaluation with new metrics and human comparisons.</p>
        <p class="abstract">Evaluating world models requires assessing both the quality of the worlds they generate and their consistency and responsiveness under exploration, interaction, and modification. We introduce HappyWorld-Bench, a comprehensive benchmark that evaluates whether generated worlds remain reliable as agents interact with them. Our design is built on a hierarchical capability framework of six world capabilities (W1-W6), from generative construction to unified world modeling, instantiated across three independent evaluation tracks: video world models, spatial world models, and embodied world models. HappyWorld-Bench comprises 1,138 video prompts, 300 spatial scenes, and 254 embodied test cases. Across all three tracks, we build and operate HappyWorld-Arena to organize human A/B comparisons and derive model-level Elo ratings, which complement newly designed automated metrics that capture behavioral correctness. We evaluate 14 video world models, 9 spatial systems, and 8 embodied candidates under this unified framework. Results reveal remaining reliability gaps across all three tracks: video models exhibit reduced consistency during extended rollouts and revisits, spatial models achieve at best 70.14% placement accuracy and 73.33% edit execution, and embodied models struggle to preserve state across multi-step actions and respond precisely to altered action conditions and physical rules. These findings highlight the need to evaluate world models not only by visual quality, but also by state consistency and the correctness of their responses to actions and interventions.</p>
      </div>
    </details>


    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>OnlineWM: Causality-Aware Active Online Learning for Effective World Modeling</strong>
          <small>Yikun Miao, Fangqi Zhu, Quanxin Shou, Xiaoyi Pang, Zhengyang Yan, Junhao Li, Haodong Wang, Zicong Hong, Song Guo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Simulator Learning</span>
<span class="topic-tag">Causal Representation Learning</span>
<span class="topic-tag">Active Learning</span>
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
          <span>Paper 7 / arXiv:2609.23753</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.23753">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it proposes a new simulator-in-the-loop method for world modeling with active online learning and causality-aware optimization, targeting a novel embodied/world-model training angle.</p>
        <p class="abstract">Generative world models aim to predict future states conditioned on actions, where action controllability is fundamental for reliable dynamics modeling. While recent efforts leverage simulator-generated data to enhance this capability, existing training pipelines face two fundamental limitations. First, static offline data collection leads to a distribution misalignment between training sets and the model&#x27;s evolving error patterns, failing to resolve critical long-tail scenarios where dynamics predictions remain unreliable. Second, the standard objective of minimizing observational discrepancy often encourages the model to exploit spurious correlations instead of capturing the underlying action-effect causality. To address these limitations, we propose OnlineWM, an online training framework that continuously improves world modeling through active simulator interaction and causality-aware optimization. OnlineWM introduces two key innovations: (1) Active Online Learning: Instead of using fixed datasets, OnlineWM adaptively queries the simulator for new interaction sequences that target the model&#x27;s current predictive weaknesses, ensuring high-utility data acquisition. (2) Causality-Aware Fine-Tuning: We propose a counterfactual learning strategy that contrasts the outcomes of different actions from identical states, forcing the model to attribute state transitions to specific actions rather than ambient environmental evolution, thereby grounding its predictions in reliable causal mechanisms. By integrating active data acquisition with causal optimization, OnlineWM establishes a closed-loop refinement process that ensures the model is both robust to diverse scenarios and precise in its causal attribution. Extensive experiments demonstrate that OnlineWM significantly enhances action controllability and generalizes effectively to unseen domains.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language-Action</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>MaskVLA: Visual Masking Against Trajectory Overfitting of Vision-Language-Action Model</strong>
          <small>Yuxuan Jiang, Jiaying Huang, Ge Wang, Shenhao Yan, Jiahao Yang, Chengsi Yao, Qi Liu, Qing Zhao, Shuguang Cui, Yiming Zhao, Yatong Han, Zhen Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Robot Manipulation</span>
<span class="topic-tag">Generalization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2609.23565</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.23565">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: a new VLA method for embodied robot manipulation, with a clear new training trick aimed at improving generalization and reducing trajectory overfitting.</p>
        <p class="abstract">Vision-Language-Action (VLA) models integrate vision-language understanding with executable robot actions, enabling end-to-end learning for robot control. However, our empirical analysis reveals that existing models exhibit severe trajectory overfitting when finetuned on limited datasets. To guide the model in effectively utilizing wrist camera information, we propose MaskVLA, a masking-based fine-tuning strategy. By randomly masking a small portion of the main camera&#x27;s visual information, the model is guided to autonomously learn more fine-grained, task-relevant, and effective visual features. This process leads to the emergence of robust policies, thereby enhancing the model&#x27;s capability to tackle complex manipulation tasks and improving its generalization performance. Our method has been comprehensively evaluated on RoboTwin 2.0, achieving an average success rate improvement of 23.2% and 16.8% compared to $\pi_0$ and OpenVLA-OFT, respectively. Furthermore, experiments on real-world ALOHA robots also demonstrate the effectiveness of our approach.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>CE$^4$L: Continual Ego, Exo, and Ego-Exo Learning</strong>
          <small>Hongwei Yan, Kanglei Zhou, Yuchen Liu, Qingyu Shi, Yi Zhong, Liyuan Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Continual Learning</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multi-view Video Understanding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2609.23492</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.23492">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it introduces a new embodied/continual learning benchmark for multi-view perception with novel ego/exo and ego-exo settings, plus a new baseline method.</p>
        <p class="abstract">Perception for embodied agents is video-based, often multi-view (ego, exo, or both), and inherently continual, with simultaneous task and viewpoint shifts. Yet continual learning (CL) remains dominated by exo-only recognition tasks, obscuring behavior under these real-world coupled shifts. We introduce Continual Ego, E}xo, and Ego-Exo Learning (CE$^4$L), a unified multi-view CL benchmark spanning four representative tasks: cross-view referenced skill assessment, temporal action segmentation, cross-view association, and action anticipation &amp; planning. CE$^4$L highlights challenges largely absent in prior CL benchmarks, including cross-view correspondence, view-dependent asynchrony, and heterogeneous semantic objectives. To this end, we propose Video Incremental Subspace-routed Task Adapters (VISTA), a parameter-efficient baseline method that stores task-specific updates in lightweight adapters and performs training-free routing via residual distance to task-specific whitened subspaces estimated from second-order statistics. Extensive experiments demonstrate the significantly varied efficacy of representative CL methods across CE$^4$L settings, while VISTA is consistently competitive and achieves state-of-the-art overall performance. Our source code for benchmarks and methods is available at https://github.com/AnAppleCore/CE4L .</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Simulation</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Semi-automated reconstruction of indoor geometry from 360-degree video for CFD-based airflow analysis in classrooms</strong>
          <small>Dhruv Gamdha, James Afful, Shambhavi Joshi, Ulrike Passe, Adarsh Krishnamurthy, Baskar Ganapathysubramanian</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Simulation</span>
<span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Indoor Geometry</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CE</span>
<span class="category-tag">physics.flu-dyn</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2609.23425</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.23425">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: embodied/simulator-related geometry reconstruction for CFD and reconfigurable indoor-environment simulation from 360° video.</p>
        <p class="abstract">Computational Fluid Dynamics (CFD) is widely used to evaluate ventilation and contaminant transport in occupied buildings, but deployment at scale is limited by three bottlenecks: acquiring room geometry without costly scanning hardware or manual CAD modeling, decomposing the scene into individually manipulable objects, and reconfiguring those objects for alternative layouts without re-capturing the room. We present a semi-automated workflow that converts a single 360-degree video of a room into individually editable, simulation-ready geometry assets. A dense point cloud is reconstructed using Neural Radiance Fields (NeRF), and 2D instance masks from text-prompted SAM 3 segmentation are lifted to 3D using multi-view consensus and depth-band filtering. Points are separated into object instances with an octree, and occlusion gaps are healed with a connectivity graph. Chair templates are fitted by Iterative Closest Point (ICP) alignment, and table geometry is generated procedurally. A browser-based editor supports quality assurance and rapid construction of alternative layout configurations. A steady Reynolds-averaged OpenFOAM solution then drives transient passive-scalar transport; the setup is verified using a mesh-sensitivity study and validated against an IEA Annex 20 benchmark. We apply the workflow to two university classrooms and a tiered lecture-hall auditorium. The capture-to-geometry pass takes two to five hours per room on a consumer workstation. In a controlled obstruction sequence in one classroom, the modeled half-clearance time varies non-monotonically as furniture is added, and a cross-room comparison indicates that clearance behavior cannot be reliably extrapolated between rooms, motivating per-room geometry acquisition. By making that acquisition low-cost, the workflow makes geometry-resolved comparative ventilation studies practical for spaces such as classrooms.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Relationally Grounded Latent World Models for Autonomous Driving</strong>
          <small>Fabian Schmidt, Markus Enzweiler, Abhinav Valada</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Latent World Models</span>
<span class="topic-tag">Scene Graphs</span>
<span class="topic-tag">Relational Representation Learning</span>
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
          <span>Paper 8 / arXiv:2609.24626</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.24626">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it proposes a new latent world-model training method for autonomous driving using relational scene-graph supervision, which is a novel embodied/simulator-related modeling angle.</p>
        <p class="abstract">Latent world models learn predictive representations for autonomous driving, but the relational semantics these states preserve often remain implicit. We investigate whether traffic scene graphs can serve as privileged semantic supervision for latent world representations. Building on LAW, we construct actor-centric scene graphs from nuScenes 3D annotations, encode their serialized relational structure using a frozen text embedding model, and align the visual latent representations with this semantic target during training. We remove the supervision branch at inference, so it requires neither scene graphs nor 3D annotations and adds no test-time computation. On nuScenes, our method reduces average trajectory L2 error from 0.661 to 0.622 (5.9%) and collision rate from 0.456 to 0.217 (52.4%) relative to our retrained LAW baseline. It also outperforms an unstructured caption-style semantic target, supporting the benefit of explicit relational structure for latent world-model representation learning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Chart Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Monitorable Chart Reasoning Agents via Verifiable Process Rewards</strong>
          <small>Sanchit Sinha, Oana Frunza, Kashif Rasul, Aidong Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Chart Reasoning</span>
<span class="topic-tag">LVLM</span>
<span class="topic-tag">Process Verifiability</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2609.24071</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.24071">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 only loosely: an LVLM-based chart reasoning agent with verifiable process rewards, more about trustworthy multimodal reasoning than a new foundation model.</p>
        <p class="abstract">Chart reasoning agents are increasingly used to extract actionable insights in critical domains, achieving state-of-the-art performance on multiple benchmarks. Yet, high benchmark accuracy alone is insufficient for deployment, where stakeholders must be able to audit and verify how a model reaches its answer. Existing LVLM-based chart agents produce either answer-only predictions or free-form rationales that are hard to verify, obscuring whether an error arose from misreading the chart, extracting a wrong value, or miscomputing. We propose Chart-RVR, a reinforcement learning framework for training monitorable chart agents with verifiable process rewards. Chart-RVR decomposes chart reasoning into three auditable blocks: Structure, identifying the chart type; Evidence, reconstructing the underlying data table in JSON; and Derivation, exposing the stepwise trace that computes the answer. Across six in-domain and out-of-domain benchmarks, Chart-RVR attains state-of-the-art accuracy among comparable-sized LVLMs. Beyond accuracy, we assess monitorability using a triangulated protocol that combines ground-truth surrogate metrics, an oracle information-gain measure, and an LLM-as-auditor scoring Process Verifiability and Evidence Localization, showing that Chart-RVR yields rationales that are markedly more verifiable and evidence-grounded than those from CoT prompting, SFT, and existing chart-specific baselines.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>AniPrO: Interpretable Anime Image Provenance Detection via Multi-Dimensional Semantic Reasoning</strong>
          <small>Yan Liu, Baoxiang Huang, Zi&#x27;an Wang, Wenbo Xie</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Provenance Detection</span>
<span class="topic-tag">Multimodal Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2609.23345</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.23345">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: vision foundation model-style multimodal semantic reasoning applied to anime image provenance detection, with new benchmarks and interpretable detection.</p>
        <p class="abstract">As generative AI becomes increasingly used in anime-style image creation, distinguishing human-drawn, AI-inpainted, and text-to-image images is important for copyright attribution, visual provenance, and content governance. Existing AI-generated image detectors mainly target real-world photographs and often overlook anime-specific cues such as flat coloring, exaggerated structures, and artistic line control. To address this gap, we propose AniPrO, a multi-dimensional description-enhanced framework for interpretable anime image provenance. Built upon AnimeDL-2M, AniPrO contains 15,000 balanced samples from a 35,000-image candidate pool, covering Real, Inpainting, and Text2Image categories with structured five-dimensional descriptions. We further introduce AniPrO-SFD-Bench and AniPrO-MFR-Bench to evaluate provenance detection from statistical feature discrimination and multimodal fusion reasoning perspectives. Experiments show that structured semantic guidance reveals systematic AI-generation biases, such as the gap between global visual plausibility and local detail coherence, and improves the detection of challenging inpainting samples. The dataset and code will be released at: https://github.com/YAN-LIU05/AniPrO.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">JEPA</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>MotionJEPA: Preventing Temporal Feature Collapse by Capturing Visual Changes in Latent Space</strong>
          <small>Markus Karmann, Shile Li, Christian Intern\`o, Bruno Andreis, David Klindt, Randall Balestriero, Jindong Gu, Philip Torr, Qi Zhang, Peng-Tao Jiang, Hao Zhang, Bo Li, Onay Urfalioglu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">JEPA</span>
<span class="topic-tag">Latent World Models</span>
<span class="topic-tag">Planning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2609.23881</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.23881">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Partially matches criterion 1: a latent world-model/JEPA-style method that improves temporal feature learning and planning, but it is less directly about embodied spatial intelligence than the strongest matches.</p>
        <p class="abstract">Joint Embedding Predictive Architectures (JEPAs) are a promising paradigm for learning task-agnostic latent world models without visual reconstruction. However, standard JEPA training exhibits a strong inductive bias towards slow features, causing feature suppression and the collapse of latent representation. While inverse dynamics provides temporal anti-collapse, it relies on action labels and offers little incentive to embed general, unlabeled dynamics. We introduce Difference Image and Single image embedding Regularization (DISReg), a novel regularizer that builds on an inverse-dynamics-style module that predicts temporal difference image embeddings without any pixel reconstruction loss, encouraging balanced static and dynamic feature learning. DISReg consists of a static term that shapes the distribution of the image embedding and encourages slow features, and a dynamic term, which, unlike direct regularization on the embedding, imposes no constraint on the image embedding&#x27;s shape or distribution and instead only incentivizes that dynamic features be present. By integrating this regularizer into a standard JEPA, we establish our new architecture, MotionJEPA. Latent probing demonstrates that MotionJEPA produces more complete representations than other methods, and our trajectory analysis shows it maintains geometrically simple latent embeddings with low curvature. We further show that MotionJEPA improves downstream planning success under static-background distractors across four environments.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">4D Gaussian Splatting</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>Dynamic Thermal Gaussians: Multimodal 4D Gaussian Splatting</strong>
          <small>Rongfeng Lu, Lifeng Lin, Xiaobao Wei, Quan Chen, Ming Lu, Yitian Xue, Yaoqi Sun, Yuhan Gao, Anke Xue, Chenggang Yan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">4D Gaussian Splatting</span>
<span class="topic-tag">RGB-Thermal Reconstruction</span>
<span class="topic-tag">Multimodal 3D Vision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2609.24531</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.24531">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Partially matches criterion 3 and 4: introduces a new multimodal 4D Gaussian splatting method and a benchmark dataset for dynamic RGB-thermal reconstruction, though it is more application-specific than broadly foundational.</p>
        <p class="abstract">Thermography plays a vital role in military and broader thermal analysis applications. Recent progress in 3D thermal reconstruction has extended temperature analysis from 2D to 3D space, yet most existing works assume static temperature distributions, neglecting the temporal dynamics of heat transfer in real-world environments. To address this limitation, we propose the first dynamic RGB-Thermal reconstruction framework for complex scenes. Our method jointly models RGB appearance, thermal observations, and scene geometry as they change over time. Specifically, we introduce a multimodal dynamic scene representation that anchors both the color and thermal modalities to a shared geometric substrate, ensuring their consistency under spatiotemporal deformations. We further design multimodal embeddings to enhance the motion expressiveness for each modality, and propose a multimodal routing mechanism that retains a unified set of shared multimodal Gaussians as the geometric backbone while adaptively spawning modality-specific Gaussians to strengthen the representational capacity in detail-rich regions of each individual modality. In addition, we contribute a novel benchmark dataset featuring high-frequency temperature variations to facilitate the evaluation of 4D reconstruction. Extensive experiments demonstrate that our method achieves high-fidelity spatiotemporal reconstruction of both appearance and temperature. Our code and dataset are available at: https://github.com/LinLif1869/DTG.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Point Clouds</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>Toward a foundation model for forest point clouds</strong>
          <small>Yuanwen Yue, Stefano Puliti, Damien Robert, Atakan Topalo\u{g}lu, Binbin Xiang, Maciej Wielgosz, Jan Dirk Wegner, Rasmus Astrup, Christian Rupprecht, Konrad Schindler</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Point Clouds</span>
<span class="topic-tag">Foundation Models</span>
<span class="topic-tag">Self-Supervised Learning</span>
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
          <span>Paper 16 / arXiv:2609.24787</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.24787">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a foundation-model-style pretraining study for 3D forest point clouds with transferable representations across downstream vision tasks.</p>
        <p class="abstract">Forest inventories increasingly rely on artificial intelligence (AI) models to derive forest attributes from large-scale 3D point clouds. Current models are typically specialized to a single task, sensor, and forest type, making adaptation expensive in terms of annotations, computation, and expertise. We ask whether a single pretrained model can instead learn transferable representations across diverse forest inventory settings. Inspired by recent developments in language modelling and computer vision, we take a step toward a foundation model (FM) for 3D forestry. Using LitePT as backbone, we first establish a strong supervised baseline that sets a new state of the art on forest semantic and instance segmentation, tree species classification, and age regression benchmarks. We then curate a large-scale unlabelled corpus spanning airborne, UAV, and mobile laser scanning across diverse forest ecosystems, and pretrain the same backbone using self-supervised learning. We systematically evaluate representation learning strategies by comparing training from scratch, supervised pretraining, and self-supervised pretraining across four representative forestry tasks, under varying annotation budgets. Compared with training from scratch, self-supervised pretraining accelerates model convergence and consistently improves performance when annotations are scarce. Compared with task-specific supervised pretraining, self-supervised pretraining yields more transferable representations across downstream forestry tasks. These findings identify the practical regime in which pretrained representations are most valuable and suggest that instance discrimination, rather than forest semantics, is the main remaining obstacle to a general-purpose 3D forest foundation model. Code and models are available at: https://github.com/prs-eth/ForPT.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Open-Vocabulary Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>InterHier: Learning Interconnected Hierarchical Semantics for Open-Vocabulary Object Detection</strong>
          <small>Yeong-Jin Kim, Ho-Joong Kim, Seong-Whan Lee</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Open-Vocabulary Detection</span>
<span class="topic-tag">Hierarchical Semantics</span>
<span class="topic-tag">Vision-Language Alignment</span>
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
          <span>Paper 17 / arXiv:2609.24026</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.24026">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Relevant to criterion 4 in a broad sense: open-vocabulary object detection with improved hierarchical semantic prompting, though it is not a foundation model paper.</p>
        <p class="abstract">In this paper, we investigate the limitations of fixed, hand-crafted connectors in hierarchical semantic representations for open-vocabulary object detection. Existing methods establish semantic relationships between base categories and unseen novel categories by placing a fixed connector between adjacent super-/sub-categories. However, such fixed connectors may not optimally capture the relationships within a semantic hierarchy. To address this limitation, we propose interconnected hierarchical semantic representations (InterHier), which utilize a prepended learnable context to globally guide the interpretation of prompts containing hierarchical relationships. InterHier operates in two main stages. First, it constructs a hierarchy-aware prompt by integrating super-/sub-categories and prepending a learnable context. Second, it optimizes this learnable context to align visual region embeddings and textual embeddings. InterHier consistently improves performance over methods that rely on fixed connectors and can be seamlessly integrated into existing open-vocabulary object detection models. Experiments on open-vocabulary object detection benchmarks demonstrate that InterHier achieves competitive performance against state-of-the-art methods.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Synthesis</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>TReViS: Temporal Repetition Structure Aware Video Synthesis for Self-supervised Repetitive Action Counting</strong>
          <small>Fanqi Yu, Shengming Ma, Stefano Fiorini, Vito Paolo Pastore, Xuan Qi, Vittorio Murino, Cigdem Beyan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Synthesis</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Action Counting</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2609.24367</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.24367">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Only loosely related to the friend&#x27;s broader CV interests; it is a self-supervised video synthesis method for repetitive action counting, but not a direct match to the requested criteria.</p>
        <p class="abstract">Fully supervised repetitive action counting (RAC) has achieved strong performance, but requires dense temporal annotations that are costly and difficult to scale. We propose TReViS, a self-supervised video synthesis framework that enables training RAC models without any repetition labels. TReViS estimates the underlying temporal repetition structure of an unlabeled video via a Temporal Self-Similarity Matrix, infers its cycle statistics, and synthesizes new training sequences that preserve realistic repetition patterns while introducing controlled temporal variability. These synthesized videos are paired with pseudo-labels and used to train existing RAC architectures from scratch. Across multiple datasets and backbones, TReViS consistently outperforms prior self-supervised methods and achieves performance competitive with several supervised baselines, while remaining fully label-free, demonstrating the effectiveness of structure-aware video synthesis for label-free RAC. The source code is available at https://github.com/yfqi/TReViS.</p>
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
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Risk-Aware Occupancy for Safety-Oriented End-to-End Autonomous Driving</strong>
          <small>Jiaxing Chen, Hengduo Zou, Yiren Zhao, Bolin Gao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Safety &amp; Planning</span>
<span class="topic-tag">Benchmark Dataset</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2609.21470</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21470">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a new safety-oriented end-to-end autonomous driving method plus a new risk-aware occupancy benchmark derived from nuScenes.</p>
        <p class="abstract">Sparse representation formulates the environment perception for the end-to-end driving system as a set of discrete elements like objects and lane lines. This formulation meets safety risks in crowded, occluded scenes dealing with unstructured obstacles, uncertain regions, and intricate interactions. In this paper, we propose a dense representation, risk-aware occupancy, to characterize planning-relevant risks in an explicit and uniform manner. It jointly encodes global scene occupancy, map-derived traffic constraints, and future dynamic agent occupancy into a unified BEV map. The unified BEV map captures the risk evidence for trajectory planning in both spatial and temporal dimensions. We design an E2E network, ROIDrive, to realize risk-aware occupancy. It predicts risk-aware occupancy with an independent branch and injects it into planning queries for safety-oriented trajectory generation. In addition, to quantify the safety problem, we introduce RiskOcc4D-nuScenes built upon nuscenes and occ3d-nuscenes. Our risk-aware occupancy yields relative open-loop collision reductions of 52.9% under the UniAD metric and 35.0% under the ST-P3 metric on nuScenes.</p>
      </div>
    </details>


    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Driving on Registers, Reasoning on Risk: Risk-Aware Occupancy for Register-Based End-to-End Autonomous Driving</strong>
          <small>Jiaxing Chen, Hengduo Zou, YuKai Qin, Yiren Zhao, Lidong Yu, Bolin Gao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Occupancy Representation</span>
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
          <span>Paper 10 / arXiv:2609.21486</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21486">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a new embodied autonomous driving method with a novel risk-aware occupancy representation and a new simulator-related benchmark/annotation pipeline.</p>
        <p class="abstract">Multimodal trajectory prediction improves behavioral coverage in end-to-end autonomous driving, but existing methods remain limited by sparse scene representations. Incomplete evidence leads to low-quality candidate generation and unreliable ranking among geometrically similar trajectories. On a register-based baseline, bad and poor candidates constitute 19.74% of the candidate set, while the oracle-best candidate ranks only 33.9th on average. We propose RRDrive, which introduces risk-aware occupancy as a dense, temporally aligned, and trajectory-queryable representation. Its global structure guides high-quality multimodal generation, while candidate-conditioned risk queries support fine-grained selection. We further construct RiskOcc4D-NAVSIM with automatic risk annotations. RRDrive achieves a selected-trajectory PDMS of 0.951, representing a 1.5% relative improvement over the baseline (0.937), and improves the average candidate PDMS by 7.7%. In challenging scenes, it improves candidate PDMS by 30.2% and increases the Spearman correlation among good candidates by 0.41, from 0.26 to 0.67. To move beyond this oracle setting, we further develop an external RiskOcc predictor, a perception module that estimates risk-aware occupancy directly from sensor inputs. The competitive performance validates the representation&#x27;s feasibility.</p>
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
          <strong>CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition</strong>
          <small>Lance Ying, Jinzhou Wu, Yingshan Susan Wang, Shivam Aarya, Luca M. Schulze Buschoff, Harry Chen, Katherine M. Collins, Andrea de Varda, Shuhao Fu, Sean Dae Houlihan, Akshay K. Jagadish, Guangyuan Jiang, Samuel Kiegeland, Tetsu Kurumisawa, Rongzhi Liu, Ryan Liu, Ningshan Ma, Kathryn McGregor, Younes Strittmatter, Polina Tsvilodub, Jacob Hoover Vigly, Sarah Wu, Enjie Xu, Yiling Yun, Kelsey Allen, Tyler Brooke-Wilson, Brian Christian, Evelina Fedorenko, Michael C. Frank, Michael Franke, Tao Gao, Samuel J. Gershman, Robert D. Hawkins, Jennifer Hu, Julian Jara-Ettinger, Max Kleiman-Weiner, Sydney Levine, Tal Linzen, Hongjing Lu, Timothy O&#x27;Donnell, Desmond C. Ong, Steven T. Piantadosi, Rebecca Saxe, Eric Schulz, Tianmin Shu, Felix A. Sosa, Ilia Sucholutsky, Tan Zhi-Xuan, Tomer Ullman, Fei Xu, Ilker Yildirim, Jian-Qiao Zhu, Thomas L. Griffiths, Tobias Gerstenberg, Kevin Smith, Joshua B. Tenenbaum</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Human-AI Comparison</span>
<span class="topic-tag">Multimodal Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2609.21259</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21259">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only: it is a new benchmark/framework for large-scale human-machine comparison, with video/image/text experiment evaluation and a strong embodied-/multimodal-eval flavor.</p>
        <p class="abstract">Understanding and modeling human intelligence are parallel goals shared by artificial intelligence (AI) and cognitive science. As AI systems grow increasingly capable, in what ways do model responses resemble human responses, and where do they systematically diverge? The sheer breadth and diversity of the tasks humans can perform and think about pose a challenge for scalable and rigorous comparison between humans and models. We introduce CogGym, a scalable, unified framework grounded in cognitive science for systematically comparing model and human behavior on matched experimental trials. CogGym uses a semi-automated, human-in-the-loop pipeline to standardize diverse experimental paradigms into a task-agnostic Experiment Markup Language (EML), enabling reproducible and faithful comparison at scale. For initial release, we curate and standardize 258 cognitive experiments from 100 papers that focuses on human commonsense reasoning, and evaluate 50 large language models against human responses. We find a clear scaling trend where larger and more recent AI models better reproduce human judgments. Yet AI models&#x27; improvement on such common reasoning tasks is considerably slower than the gains observed on formal-reasoning benchmarks like math and coding, and model--human fit remains well below human splithalf reliability ($R^2 = 0.93$ on text, $0.95$ on image, and $0.92$ on video) with the best models achieving $R^2 = 0.59$ on text, $0.58$ on image, and $0.43$ on video experiments. We intend for CogGym to provide a living evaluation framework that continually incorporates new cognitive science experiments to characterize where model behavior resembles human behavior, where it systematically diverges, and how those patterns change as models and experiments evolve.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
