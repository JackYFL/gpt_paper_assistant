

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
      <p class="eyebrow">Daily ArXiv / September 21, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>14</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>17</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>13.1</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="9 mentions">action</span><span class="cloud-word" style="font-size:1.91rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="11 mentions">candidate</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">causal</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">consistency</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">control</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">dense</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">driving</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">environment</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">evidence</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">expert</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">future</span><span class="cloud-word" style="font-size:1.91rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 56%, var(--accent))" title="11 mentions">generation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">geometric</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">gesture</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">interaction</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">language</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">latent</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">mapping</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">memory</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">motion</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="10 mentions">object</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">observation</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">occupancy</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">perception</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">persistent</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">pipeline</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">query</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="8 mentions">reference</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">risk</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="6 mentions">risk-aware</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">scalable</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="19 mentions">scene</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">scenelm</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">semantic</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">sign</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">streaming</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">support</span><span class="cloud-word" style="font-size:2.37rem;opacity:0.9;color:color-mix(in srgb, var(--accent-2) 79%, var(--accent))" title="15 mentions">tactile</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">teacher</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="9 mentions">trajectory</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">unified</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="7 mentions">video</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="5 mentions">view</span><span class="cloud-word" style="font-size:1.78rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 49%, var(--accent))" title="10 mentions">visual</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="129 mentions">action</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="146 mentions">agent</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="61 mentions">alignment</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="68 mentions">annotation</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="71 mentions">attention</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="55 mentions">backbone</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="66 mentions">camera</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="56 mentions">challenging</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="68 mentions">consistency</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="58 mentions">control</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="62 mentions">detection</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="55 mentions">driving</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="97 mentions">dynamic</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="68 mentions">environment</span><span class="cloud-word" style="font-size:1.69rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="139 mentions">evidence</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="55 mentions">foundation</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="60 mentions">future</span><span class="cloud-word" style="font-size:2.28rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 75%, var(--accent))" title="220 mentions">generation</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="64 mentions">geometry</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="65 mentions">grounding</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="71 mentions">inference</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="94 mentions">interaction</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="95 mentions">language</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="64 mentions">latent</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="68 mentions">memory</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="61 mentions">mllm</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="111 mentions">motion</span><span class="cloud-word" style="font-size:1.72rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 46%, var(--accent))" title="143 mentions">multimodal</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="68 mentions">multiple</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="117 mentions">object</span><span class="cloud-word" style="font-size:1.33rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="99 mentions">observation</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="66 mentions">optimization</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="54 mentions">pair</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="64 mentions">perception</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="64 mentions">pipeline</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="83 mentions">point</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="59 mentions">query</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="61 mentions">question</span><span class="cloud-word" style="font-size:1.89rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 55%, var(--accent))" title="164 mentions">reasoning</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="59 mentions">region</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="59 mentions">reward</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="128 mentions">scene</span><span class="cloud-word" style="font-size:1.82rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="155 mentions">semantic</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="75 mentions">space</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="112 mentions">spatial</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="56 mentions">structured</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="72 mentions">supervision</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="76 mentions">support</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="89 mentions">target</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="90 mentions">temporal</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="59 mentions">textbf</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="96 mentions">token</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="111 mentions">trajectory</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="78 mentions">understanding</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="59 mentions">unified</span><span class="cloud-word" style="font-size:2.20rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 71%, var(--accent))" title="207 mentions">video</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="63 mentions">view</span><span class="cloud-word" style="font-size:1.10rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="77 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="300 mentions">visual</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="86 mentions">world</span></div>
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
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>A Scene Language Model for Open-Vocabulary Scene Mapping</strong>
          <small>Adam Lilja, Fabio H\&quot;ubel, Siming He, Junsheng Fu, Claire Tomlin, Lars Hammarstrand, Jitendra Malik, Jonas Frey, Marco Pavone</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">3D Scene Mapping</span>
<span class="topic-tag">Vision-Language Model</span>
<span class="topic-tag">Open-Vocabulary Perception</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">17</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2609.21400</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21400">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 2 very closely: it proposes a new Scene-Language Model for open-vocabulary 3D scene mapping, giving a novel method for spatial understanding in embodied settings and a new VLM-style system.</p>
        <p class="abstract">Open-vocabulary 3D scene mapping aims to build a persistent representation of the objects in an environment. Existing systems typically rely on engineered mapping pipelines to associate observations, merge information across views, and maintain a consistent scene representation over time. Many additionally store feature-rich object representations, such as embeddings or image crops, increasing the size and complexity of the persistent memory. We introduce SceneLM, a Scene-Language Model that directly maintains a textual scene map. The full scene is represented as a structured text list of objects, which serves as the model&#x27;s only persistent memory. For each input image, the model reads the current scene state and updates the map by adding, editing, and removing objects. To learn this behavior, we introduce supervision tasks for iterative scene map maintenance together with an automatic annotation pipeline that generates training data from images without human labels. We evaluate SceneLM on both a language-grounded retrieval benchmark and a localization benchmark. Across both benchmarks, the model produces a scene map that achieves competitive performance with complete mapping systems built from dedicated perception and geometric modules while producing a scene representation that is 6-12x more compact. We further show that SceneLM can be run online on an edge device through experiments on a quadruped. These results show that a persistent open-vocabulary 3D scene map can be maintained directly by a single vision-language model using only a lightweight text representation. Training and inference code is available on https://goldengait.github.io/scenelm/.</p>
      </div>
    </details>


    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>VideoReloc: Long-Term Indoor Video Relocalization against a Kilobyte-Scale Semantic Scene Graph</strong>
          <small>Qianru Li, Xuyang Chen, Xuqin Wang, Zhenghao Zhang, Hongyi Luo, Tao Wu, Daniel Cremers, Lu Liu, Yanfeng Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Indoor Relocalization</span>
<span class="topic-tag">Scene Graphs</span>
<span class="topic-tag">Spatial Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2609.21804</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21804">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 3 very closely: it targets long-term indoor relocalization with a compact semantic scene graph, introducing a new embodied spatial method and a simulator/benchmark-style evaluation setting.</p>
        <p class="abstract">Given a compact semantic scene graph, long-term indoor video relocalization estimates a map-frame trajectory after lighting and furniture changes. Visual methods rely on appearance and become unreliable under these changes; localizing one frame at a time from object classes and geometry instead leaves sparse, ambiguous evidence. We introduce VideoReloc, whose adaptive clips use odometry to gather spatial evidence until object and motion criteria are met, adapting query length to the observed scene. Its run-level decision rechecks conflicting placements using evidence accumulated across connected clips, stabilizing the trajectory beyond adjacent-clip tracking. Hypothesis-first registration proposes poses from object triplets and verifies each using clip-wide object centers and box surfaces. Orientation-aware refinement uses box faces, gravity and wall directions to resolve ambiguity in camera orientation and refine the full pose. This reframes sparse-map relocalization as verification of spatially extended video queries, moving discriminative support from stored appearance to temporal context and permitting a 100 kB map of class-labelled boxes. On RIO10 and ReplicaCAD, the all-frame localization success rate at 1 m/10$^\circ$ is 73.5% and 61.1% under causal evaluation, rising to 90.6% and 74.8% with clip closure. The evaluated per-frame scene coordinate regressors reach up to 47.6% and 49.8%, respectively, with maps of 12.6-42 MB. Project page: https://videoreloc.github.io</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Model</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>MintAct: A Unified Visual Agent for Digital Environments</strong>
          <small>Mingfei Gao, Rui Tian, Haiming Gang, Bohan Zhai, Le Zhang, Yuanzheng Gong, Di Feng, Ege \&quot;Ozsoy, Kaixin Ma, Vishwesh Kirthivasan, O\u{g}uzhan Fatih Kar, Roman Bachmann, Anders Boesen Lindbo Larsen, Afshin Dehghan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Model</span>
<span class="topic-tag">GUI Agent</span>
<span class="topic-tag">Reinforcement Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2609.22083</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.22083">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and criterion 3 very strongly: a unified visual agent / VLM for UI grounding, multi-step navigation, and visual tool use across digital environments.</p>
        <p class="abstract">We present MintAct, a family of vision-language models that unifies UI grounding, multi-step navigation across mobile, desktop, and web, and visual tool use, trained at 2B, 4B, and 8B scales. Through careful design of our environments, data, and training recipes, MintAct models match the performance of per-domain specialists across all of these capabilities. To enable this, we develop a scalable environment and reinforcement learning (RL) infrastructure. On the environment side, we host hundreds of concurrent instances across heterogeneous per-domain backends, serving both trajectory data collection and online RL. To enable efficient and scalable RL training, an asynchronous framework keeps explicit control over the cross-domain training distribution and remains stable under noisy environment feedback and off-policy drift. Experimental results show that MintAct achieves state-of-the-art performance (48.9 on OSWorld-Verified) across a wide range of benchmarks at comparable model sizes.</p>
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
          <strong>ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation</strong>
          <small>Boni Hu, Xiong Wei, Haoming Huang, Yong Huang, Chenbo Wang, Yi Yang, Jiancheng Wang, Ruicheng Zhu, Zhimin Yang, Guanglai Liu, Qiaowan Jin, Dongzhuo Wang, Haiwei Kuang, Jiajun Fan, Yue Wu, Jiaxin Wei, Hao Sun, Feihong Yan, Wei Bi, Kaixuan Wang, Zichao Guo, Xiaozhi Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Autonomous Driving Simulation</span>
<span class="topic-tag">Closed-Loop Rollouts</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2609.21712</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21712">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Strong match for criterion 3: a new real-time controllable world model for closed-loop autonomous-driving simulation, with simulator-style long-horizon rollout and memory handling.</p>
        <p class="abstract">Generative world models offer controllable and repeatable closed-loop simulation for end-to-end and vision-language-action driving policies, but production deployment exposes three unresolved requirements: faithfully reproducing a mixed fisheye-pinhole rig at native resolutions; reconciling causal, per-timestep interaction with long-horizon stability and low latency; and preserving scene identity when a location is revisited. We present ZYT-World, a single architecture that natively generates four fisheye views with field of view &gt; 180{\deg} and three pinhole views. Projection-specific Plucker adapters encode camera geometry, ego-motion adaptive layer normalization provides global motion control, and a lightweight pixel-aligned layout conditions traffic participants and signals through instance-level boxes, headings and colors. Heterogeneous training combines full-rig geometric coverage with high-resolution detail. Teacher forcing, causal consistency distillation, self-rollout distribution matching distillation, and RigCritic transform a 40-step bidirectional teacher into a one-step, per-latent streaming generator, with RigCritic evaluating the seven-view rig jointly. A 19M-parameter variational autoencoder decoder (TinyVAE), W8A8 quantization, and our inference engine reduce decoding, backbone, and incremental-execution costs, respectively. Finally, cross-trajectory pairs derived from real captures train a plug-in implicit-memory module that preserves place-specific evidence. On the internal multi-view test set, the one-step model retains more than 90% of the teacher&#x27;s PSNR and SSIM, while FID, FVD, and LPIPS stay within 11% of the teacher. Under the generator-only timing in Figure 2, it is 107.7 times faster than the 40-step bidirectional teacher. TinyVAE decodes 59.8 times faster than Wan. 30s rollouts and cross-trajectory revisits show the intended long-horizon and memory behavior.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">SLAM</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Cube-Splat: High-Fidelity 360{\deg} Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization</strong>
          <small>Xiangfei Guo, Hao Shi, Yufan Zhang, Zhonghua Yi, Yongqi Mao, Xiaoting Yin, Kaiwei Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">SLAM</span>
<span class="topic-tag">3D Gaussian Splatting</span>
<span class="topic-tag">Synthetic Benchmark</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2609.21347</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21347">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new panoramic GS-SLAM framework plus a synthetic benchmark dataset for 360° SLAM evaluation.</p>
        <p class="abstract">Recent progress in 3D Gaussian Splatting (3DGS) has enabled dense visual SLAM with pinhole cameras, yet most pipelines are not designed for panoramic imagery. We present Cube-Splat, the first panoramic GS-SLAM framework that factorizes each 360{\deg} frame into a cubemap of four fixed-orientation virtual pinhole views sharing a single optical center. By designating the front face as the primary pose state, we accumulate gradients from all faces via an adjoint mapping, thereby enabling multi-face observations to coherently update a single state while strictly preserving cross-view geometric consistency. Concurrently, our mapping module densifies and optimizes anisotropic Gaussians using aggregated cubemap rays for high-fidelity, dense reconstruction. Furthermore, to rigorously evaluate panoramic SLAM under diverse and challenging conditions, we introduce SynPano, a highly scalable, photorealistic synthetic dataset featuring parameterized complex trajectories and multi-modal ground truth. Extensive evaluations on two public benchmarks (PALVIO and OmniBlender) and our SynPano dataset, collectively encompassing both indoor and outdoor scenes, demonstrate that Cube-Splat achieves state-of-the-art (SOTA) performance in tracking accuracy and reconstruction fidelity. Both the source code and the SynPano dataset are available at https://github.com/guoxf304/CubeSplat.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Manipulation</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling</strong>
          <small>Xuancheng Zhang, Xuetao Liu, Qianying Tang, Jizhe Wang, Zhijing Cheng, Bochen Lin, Haoran Wen, Ming Li, Kun Zhan, Yu Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Manipulation</span>
<span class="topic-tag">Tactile Sensing</span>
<span class="topic-tag">World Action Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2609.21449</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21449">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very well: an embodied manipulation method that brings tactile sensing into world-action modeling, with a new heterogeneous tactile data engine and simulator-based evaluation.</p>
        <p class="abstract">World Action Models bring the predictive capabilities of video models into robot action generation, providing a rich foundation for modeling future visual states. Tactile sensing complements this foundation with direct measurements of physical interaction. Some existing methods use tactile features as conditioning inputs without jointly predicting future tactile states, visual observations, and actions. Our key insight is that tactile signals, like video, provide observations of the evolving world state and should be modeled as future observations alongside video. We present ME-Dex-1.0 (MachEmbodied-Dex-1.0), a unified World Action Tactile Model for joint visual, tactile, and action learning. ME-Dex-1.0 adopts a Mixture-of-Transformers architecture comprising a Video Expert, a Tactile Expert, and an Action Expert, all trained with flow matching. We use shared attention connects the experts in intermediate layers, allowing action generation to draw on learned representations of visual and tactile dynamics during joint denoising. To support multi-source heterogeneous tactile inputs, a Canonical Hand Model and a Unified Tactile Autoencoder map tactile observations from different embodiments and sensing layouts into shared spatial and latent spaces. To address the limited availability of paired visual, tactile, and action data, we develop the Agentic Tactile Data Engine, an agent-based data production platform. It supplements RoboTwin and DexJoCo with tactile data recorded directly from force sensors during trajectory replay in simulation. Experiments on the RoboTwin, DexJoCo, and ManiFeel simulation platforms, together with real robot evaluations, demonstrate improved manipulation performance using both grippers and dexterous hands equipped with tactile sensing.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video Generation</strong>
          <small>Wenxue Li, Peiyan Guan, Haoyang Jiang, Junxian Cai, Hualuo Liu, Chunjie Zhang, Chong Guan, Songlian Li, Taiyi Wu, Yongjian Yu, Xiaotong Zhao, Alan Zhao, Eric Liu, Xi Chen, Yu Liu, Lei Zhu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multimodal Generative Modeling</span>
<span class="topic-tag">Reference Control</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2609.22069</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.22069">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 partially and is also a strong benchmark paper: it builds a new large-scale benchmark/dataset for reference-to-video generation, which may interest someone following multimodal generative modeling and evaluation.</p>
        <p class="abstract">Reference-to-video (R2V) generation is evolving toward increasingly general and versatile reference control, giving rise to the emerging paradigm of omni R2V generation. However, existing benchmarks fall short of these emerging capabilities: their test cases cover limited reference types and compositions, and their evaluation protocols largely assess holistic reference consistency, overlooking whether reference factors are properly preserved, disentangled, and routed. Meanwhile, the high cost of constructing omni R2V training data makes suitable training resources scarce. To address these gaps, we introduce OmniVBench and the Omni-R2V Dataset for evaluating and training omni R2V models. OmniVBench expands R2V evaluation across broader reference types, fine-grained control tasks, and richer reference compositions, covering 7 task families and 18 fine-grained tasks spanning content, motion, style, structure, narrative, and multi-reference settings. We introduce factor-grounded evaluation with 12,172 case-specific checklist items, assessing whether intended reference factors are faithfully preserved, correctly disentangled and bound to their targets, and properly realized according to the instruction. We further introduce the Omni-R2V Dataset, bringing industrial-grade training resources for diverse R2V tasks to the broader research community. Drawing primarily on a large-scale corpus of professional video footage, it comprises 340K processed training samples spanning diverse reference types and multi-reference compositions. We develop task-specific pipelines for reference-target pair construction, offering a practical and scalable recipe for omni R2V data construction. Extensive evaluation of advanced open- and closed-source R2V models reveals clear performance gaps across task families and evaluation dimensions on OmniVBench, highlighting remaining limitations of current R2V models.</p>
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
          <strong>VeriFuse: Bounded Vision-Language Arbitration and Reason-Guided Refinement for Cooperative 3D Perception</strong>
          <small>Hongyi Lin, Yiyao Liu, Qi Kang, Heye Huang, Yang Liu, Haris Koutsopoulos, Jinhua Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Cooperative 3D Perception</span>
<span class="topic-tag">VLM Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2609.21323</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21323">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 and criterion 2: it uses a frozen VLM for bounded arbitration in cooperative 3D perception, a clear vision-foundation-model application.</p>
        <p class="abstract">Vision-language models (VLMs) have demonstrated strong scene understanding and semantic judgment across diverse tasks, but their appropriate role in cooperative perception remains unclear. Directly asking a VLM to regress 3D detections is unreliable and computationally expensive, whereas using it to select the output of a single source discards useful information from other agents. We introduce VeriFuse, a bounded arbitration framework for vehicle-infrastructure cooperative 3D detection. Each agent first produces detections independently. Around each vehicle and roadside proposal, VeriFuse generates source-conditioned geometric candidates and combines the original detections, their perturbations, and cross-source hypotheses into a unified candidate pool. A frozen VLM then chooses among three admissible actions: SELECT an adequate candidate; REFINE an existing anchor when an object is supported but all candidates are geometrically inadequate; or REJECT an unsupported infrastructure-only proposal. Experiments on the DAIR-V2X dataset show that VeriFuse achieves 0.494/0.357 cooperative 3D AP50/AP70 and limits the relative vehicle-side BEV AP50 drop under a 300 ms delay to 1.7%. Overall, VeriFuse assigns the VLM a clear and constrained role in cooperative perception: semantic reasoning resolves ambiguity among cross-agent hypotheses, while deterministic constraints determine the final 3D geometry.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language-Action</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>PRIME: Perception Feedback with Situational Memory Embeddings in VLA Models</strong>
          <small>Erik Deinzer, Naya Baslan, Luca Paparusso, Narunas Vaskevicius, Peter Knott, Luigi Palmieri</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Perception Feedback</span>
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
          <span>Paper 11 / arXiv:2609.22040</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.22040">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new VLA driving method that adds perception feedback via situational memory, improving closed-loop autonomous driving behavior.</p>
        <p class="abstract">Current Vision-Language-Action (VLA) models for autonomous driving operate primarily through feedforward inference across the perception--reasoning--planning hierarchy. While modern architectures maintain temporal recurrence within the perceptual module, early perception remains blind to downstream reasoning and navigation goals, processing visual inputs agnostically without prioritizing cues informed by prior decisions. To bridge this gap, this paper introduces PRIME, a learned feedback mechanism that conditions the VLA perceptual queries on a novel Situational Memory. By aggregating latent representations of past perception, reasoning, navigation goals, and predicted behaviors across an L-step window via cross-attention, PRIME enables intent-driven perceptual attention at minimal computational cost, adding only a maximum of 29.7M parameters (0.41% of the 7.3B-parameter base model). Evaluated on the Bench2Drive closed-loop benchmark, PRIME achieves a state-of-the-art Driving Score of 82.47 (+4.73 over ORION) and a Success Rate of 60.00% (+5.38 percentage points), the highest reported Driving Score among published VLAs trained on Think2Drive demonstrations.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Sign Language</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>SignGPT: Toward LLM-Mediated Sign Language Interaction through Gloss-Free Translation and Generation</strong>
          <small>Ronghui Li, Jun Dong, Zhongyuan Hu, Zunnan Xu, Jun Zhou, Liyuan Chen, Shuoling Liu, Jiangpeng Yan, Jie Guo, Xiu Li, Linchao Bao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Sign Language</span>
<span class="topic-tag">Multimodal Translation</span>
<span class="topic-tag">Pose-Based Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2609.21709</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21709">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: unified sign-language translation and generation with a new pose-based framework, which is an embodied interaction setting with a novel bidirectional formulation.</p>
        <p class="abstract">Large language models (LLMs) provide limited support for sign language interaction. Unifying sign language translation (SLT) and generation (SLG) to enable sign language as both input and output can reduce switching between separate models during sign-text interaction. We present SignGPT, a unified, pose-based framework for gloss-free SLT and SLG. SignGPT integrates part-aware hierarchical representations of body, hand, and facial motion into a shared language model and employs asymmetric multi-token prediction and progressive training for bidirectional modeling. We evaluate SignGPT on How2Sign (ASL) and Phoenix-2014T (DGS) through benchmark comparisons, qualitative analyses, and component ablations. An exploratory study with 12 Deaf ASL signers assesses an LLM-mediated sign-to-sign response pipeline, highlighting the potential of unified modeling to support sign language conversation (SLC).</p>
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
          <strong>PrismAlign: Prior-Steered Multi-View VLM Alignment for Hallucination-Robust Table OCR</strong>
          <small>Guangyi Liu, Qianjun Huang, Boyu Hou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">OCR</span>
<span class="topic-tag">Hallucination Reduction</span>
<span class="topic-tag">Bayesian Inference</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2609.21351</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21351">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 partially: it uses multiple VLMs in a new alignment framework for OCR, but the paper is mainly about document/table extraction rather than a new general VLLM or embodied method.</p>
        <p class="abstract">Table extraction suffers from frequent structural errors and semantic hallucinations. We propose PrismAlign, a multi-VLM framework aligning diverse visual perspectives to resolve ambiguity. It integrates priors of table logic to assess output plausibility, decoupling structural alignment from cell content alignment. A Bayesian decision strategy maximizes alignment accuracy by exploiting the correlation between extraction errors and computable rule violations. Evaluated on open-source and custom VLMs, PrismAlign reduces hallucinations and achieves state-of-the-art performance on OmniDocBench 1.5, as well as on the table category of CC-OCR and PureDocBench.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Gesture Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>GestureFAR: Streaming Co-Speech Gesture Generation with Flow Autoregression</strong>
          <small>Pinxin Liu, Haiyang Liu, Jiahao Luo, Junhua Huang, Chunhao Zou, Luchuan Song</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Gesture Generation</span>
<span class="topic-tag">Flow Matching</span>
<span class="topic-tag">Embodied Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.GR</span>
<span class="category-tag">cs.HC</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2609.21576</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21576">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only very loosely: it is an embodied conversational agent method, but the focus is co-speech gesture generation rather than a new embodied AI benchmark or spatial intelligence method.</p>
        <p class="abstract">Generating natural co-speech gestures from streaming speech is essential for embodied conversational agents, where motion must be produced while a user is still speaking. Recent streaming gesture systems make online generation possible by autoregressing over discrete motion tokens, but this design compresses high-dimensional continuous motion into finite codebooks and can limit the realism and diversity of generated gestures. To preserve both causality and continuous expressiveness, we propose \textbf{GestureFAR}, a flow-autoregressive framework for streaming co-speech gesture generation. First, GestureFAR autoregresses over causal continuous motion latents, using a transformer to model streaming audio-motion context and a per-token flow-matching head to sample the next latent from a continuous distribution. Second, we introduce a head-only flow distillation strategy that freezes the causal backbone and distills the multi-step per-token flow head into a single network evaluation using consistency and distribution-matching objectives. This keeps the model token-causal while removing the main latency bottleneck for live interaction. Experiments on BEAT2 show that GestureFAR significantly improves the quality--latency trade-off among streaming-capable methods, preserving strong gesture quality while enabling real-time token-causal generation. Project Page: https://andypinxinliu.github.io/GestureFAR</p>
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
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Driving on Registers, Reasoning on Risk: Risk-Aware Occupancy for Register-Based End-to-End Autonomous Driving</strong>
          <small>Jiaxing Chen, Hengduo Zou, YuKai Qin, Yiren Zhao, Lidong Yu, Bolin Gao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Trajectory Prediction</span>
<span class="topic-tag">Risk-Aware Occupancy</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2609.21486</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21486">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new register-based driving method with risk-aware occupancy and a new risk-annotated benchmark for trajectory selection.</p>
        <p class="abstract">Multimodal trajectory prediction improves behavioral coverage in end-to-end autonomous driving, but existing methods remain limited by sparse scene representations. Incomplete evidence leads to low-quality candidate generation and unreliable ranking among geometrically similar trajectories. On a register-based baseline, bad and poor candidates constitute 19.74% of the candidate set, while the oracle-best candidate ranks only 33.9th on average. We propose RRDrive, which introduces risk-aware occupancy as a dense, temporally aligned, and trajectory-queryable representation. Its global structure guides high-quality multimodal generation, while candidate-conditioned risk queries support fine-grained selection. We further construct RiskOcc4D-NAVSIM with automatic risk annotations. RRDrive achieves a selected-trajectory PDMS of 0.951, representing a 1.5% relative improvement over the baseline (0.937), and improves the average candidate PDMS by 7.7%. In challenging scenes, it improves candidate PDMS by 30.2% and increases the Spearman correlation among good candidates by 0.41, from 0.26 to 0.67. To move beyond this oracle setting, we further develop an external RiskOcc predictor, a perception module that estimates risk-aware occupancy directly from sensor inputs. The competitive performance validates the representation&#x27;s feasibility.</p>
      </div>
    </details>


    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Risk-Aware Occupancy for Safety-Oriented End-to-End Autonomous Driving</strong>
          <small>Jiaxing Chen, Hengduo Zou, Yiren Zhao, Bolin Gao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Occupancy Prediction</span>
<span class="topic-tag">Safety Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2609.21470</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.21470">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new safety-oriented end-to-end driving method based on risk-aware occupancy, plus a new risk benchmark for autonomous driving.</p>
        <p class="abstract">Sparse representation formulates the environment perception for the end-to-end driving system as a set of discrete elements like objects and lane lines. This formulation meets safety risks in crowded, occluded scenes dealing with unstructured obstacles, uncertain regions, and intricate interactions. In this paper, we propose a dense representation, risk-aware occupancy, to characterize planning-relevant risks in an explicit and uniform manner. It jointly encodes global scene occupancy, map-derived traffic constraints, and future dynamic agent occupancy into a unified BEV map. The unified BEV map captures the risk evidence for trajectory planning in both spatial and temporal dimensions. We design an E2E network, ROIDrive, to realize risk-aware occupancy. It predicts risk-aware occupancy with an independent branch and injects it into planning queries for safety-oriented trajectory generation. In addition, to quantify the safety problem, we introduce RiskOcc4D-nuScenes built upon nuscenes and occ3d-nuscenes. Our risk-aware occupancy yields relative open-loop collision reductions of 52.9% under the UniAD metric and 35.0% under the ST-P3 metric on nuScenes.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-08-21.html">
          <span>August 21, 2026</span>
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
