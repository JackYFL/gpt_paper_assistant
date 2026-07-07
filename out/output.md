

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
      <p class="eyebrow">Daily ArXiv / July 07, 2026</p>
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
      <strong>13</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">action</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">adversarial</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="6 mentions">ai-generated</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="6 mentions">alignment</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">attack</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">backbone</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">bidirectional</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">causal</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">co-training</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="6 mentions">construct</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="6 mentions">denoising</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">dense</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">detection</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">diffusion</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">dynamic</span><span class="cloud-word" style="font-size:2.47rem;opacity:0.92;color:color-mix(in srgb, var(--accent-2) 85%, var(--accent))" title="26 mentions">generation</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="9 mentions">generator</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">impairment</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="6 mentions">improving</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="9 mentions">inference</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="6 mentions">language</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">latent</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">layout</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">lighting</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">low-light</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="10 mentions">medical</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">memory</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">motor</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="8 mentions">multimodal</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">produce</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">prompt</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">relation</span><span class="cloud-word" style="font-size:1.95rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="17 mentions">scene</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="6 mentions">semantic</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">sequence</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">step</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">structural</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">supervision</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">support</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">temporal</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="5 mentions">token</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="6 mentions">trajectory</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">unified</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="32 mentions">video</span><span class="cloud-word" style="font-size:1.82rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="15 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="76 mentions">action</span><span class="cloud-word" style="font-size:1.59rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="117 mentions">agent</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="62 mentions">alignment</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="62 mentions">attention</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="50 mentions">concept</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="53 mentions">consistency</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="53 mentions">control</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="55 mentions">detection</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="56 mentions">diffusion</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="58 mentions">domain</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="66 mentions">driving</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="101 mentions">dynamic</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="55 mentions">event</span><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="114 mentions">evidence</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="71 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="52 mentions">foundation</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="56 mentions">frame</span><span class="cloud-word" style="font-size:1.93rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="157 mentions">generation</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="62 mentions">geometric</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="53 mentions">geometry</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="48 mentions">identity</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="61 mentions">inference</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="57 mentions">interaction</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="51 mentions">knowledge</span><span class="cloud-word" style="font-size:1.48rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="105 mentions">language</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="61 mentions">latent</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="62 mentions">mechanism</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="91 mentions">memory</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="79 mentions">motion</span><span class="cloud-word" style="font-size:1.80rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="141 mentions">multimodal</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="110 mentions">object</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="53 mentions">paradigm</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="69 mentions">pipeline</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="53 mentions">policy</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="59 mentions">pose</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="64 mentions">real-world</span><span class="cloud-word" style="font-size:2.24rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 73%, var(--accent))" title="198 mentions">reasoning</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="70 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="54 mentions">reference</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="54 mentions">region</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="53 mentions">reward</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="115 mentions">scene</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="133 mentions">semantic</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="59 mentions">space</span><span class="cloud-word" style="font-size:1.48rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="105 mentions">spatial</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="49 mentions">structured</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="57 mentions">supervision</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="48 mentions">support</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="48 mentions">synthesis</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="70 mentions">target</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="95 mentions">temporal</span><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="119 mentions">token</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="68 mentions">trajectory</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="79 mentions">understanding</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="66 mentions">unified</span><span class="cloud-word" style="font-size:2.35rem;opacity:0.89;color:color-mix(in srgb, var(--accent-2) 79%, var(--accent))" title="215 mentions">video</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="50 mentions">view</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="67 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="281 mentions">visual</span><span class="cloud-word" style="font-size:1.25rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="83 mentions">world</span></div>
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
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation</strong>
          <small>Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Francesco Nex, Hao Cheng, Michael Ying Yang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">World Action Models</span>
<span class="topic-tag">Video-Action Planning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2607.05133</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.05133">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: this is an embodied-AI/autonomous-driving paper proposing a new unified video-action model with a novel modality-decoupling mask for planning.</p>
        <p class="abstract">World Action Models (WAMs) have shown strong potential for improving action generalization in autonomous driving by using future video prediction as dense supervision for scene dynamics and temporal causality. However, it remains unclear which architecture better transfers video-modeling benefits to trajectory generation. Existing cascaded or dual-DiT designs separate video imagination from action prediction, weakening the transfer of video-learned world dynamics to the trajectory branch: the action model may still overfit dataset-specific driving priors, while the video model only indirectly regularizes planning. We propose UNIVERSE, a unified video-action model built upon a single mask-modulated Diffusion Transformer. By co-training future video latents and ego-trajectory tokens within shared generative parameters, UNIVERSE allows dense video supervision to directly shape trajectory denoising, leading to stronger cross-domain action generalization. To ensure causal validity and efficient deployment, we introduce a Modality-Decoupling Visibility Mask, which shares historical context across modalities while blocking mutual attention between future video and trajectory tokens. This prevents future-target leakage and enables trajectory-only inference by removing future-video denoising at test time, achieving a $4.3\times$ speedup over joint video-action rollout while maintaining comparable planning accuracy. The same model also supports video-only and joint video-action rollouts. Experiments show that UNIVERSE achieves 91.0 PDMS on NAVSIM (vs. 89.6 for the Two-DiT variant), and demonstrates strong zero-shot transfer to nuScenes and Bench2Drive without fine-tuning, while ablations confirm the importance of single-DiT unification, video co-training, and mask-based modality decoupling.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation</strong>
          <small>Haozhe Wang, Weijia Feng, Jinpeng Yu, Che Liu, Ping Nie, Fangzhen Lin, Jiaming Liu, Ruihua Huang, Jimmy Lin, Wenhu Chen, Cong Wei</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Agentic Visual Generation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
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
          <span>Paper 2 / arXiv:2607.05382</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.05382">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it builds a benchmark and method for agentic visual generation with tool/search augmentation, a novel angle on vision foundation models.</p>
        <p class="abstract">Visual generators excel at rendering, but they confidently fabricate what they do not know. User requests are unbounded, evolving, and deeply long-tailed: new characters, trending entities, post-cutoff events, and more. This world-knowledge bottleneck is structural: generators are trained on fixed corpora, but the visual world is open-ended. We construct SearchGen-20K and SearchGen-Bench, with 20,839 prompts spanning twelve failure categories and twenty-two domains, paired with a pre-executed multimodal SearchGen-Corpus-1M to support offline, reproducible research. On SearchGen-Bench, frontier open generators score only 21 to 28 out of 100, a 40-point collapse invisible to existing benchmarks. The natural remedy is to employ search tools, enabling agentic visual generation. However, we find that naive search fails: it retrieves indiscriminately, injecting noise into prompts the generator already handles. We trace the root cause to a generator-specific, evolving knowledge boundary: the divide between what a generator can internalize through training and what must remain in external context. Although this boundary is hard to specify in advance, we show that it is discoverable through a teach-then-search co-training framework. Even a minimal version of this co-training recipe produces monotonic improvement, laying the foundation for recursive self-improvement in visual generation that can meet world-knowledge-grounded requests. We release the full dataset, co-training corpus, and search corpus as a replayable harness for tool-augmented, world-knowledge-grounded visual generation.</p>
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
          <strong>Aura: Consistent Multi-Subject Video Generation via VLM-Grounded Semantic Alignment</strong>
          <small>Zixiang Zhou, Zhentao Yu, Yifeng Ma, Hongmei Wang, Wenqing Yu, Cong Wang, Zilin Yang, Rui Chen, Jiarong Ou, Yezhou Liu, Yuan Zhou, Qinglin Lu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Video Generation</span>
<span class="topic-tag">Controllable Synthesis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2607.04311</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.04311">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it proposes a VLM-grounded framework for controllable multi-subject video generation with explicit VLM-to-DiT alignment.</p>
        <p class="abstract">Subject-driven and multi-element video generation are central to controllable video synthesis, but existing methods still struggle to preserve identity consistency and model complex relationships among multiple subjects. In this paper, we propose Aura, a unified framework for high-fidelity and identity-consistent video generation. To better capture scene dynamics and subject interactions, we introduce AI director-level captions that provide dense and structured descriptions of video content. We further leverage a vision-language model (VLM) with learnable queries to extract multimodal semantic features from textual and visual references, covering both global semantics and fine-grained visual cues. To bridge the representational gap between the VLM and the Diffusion Transformer (DiT), we design a two-stage alignment strategy that progressively maps VLM features into the DiT feature space. For visual conditioning, we adopt token concatenation to inject reference information directly into the generation process. To distinguish heterogeneous subject types and reduce common copy-paste artifacts, we develop a subject-aware RoPE-Shift mechanism. To further differentiate reference images of different categories, we introduce subject-aware learnable tokens. In addition, we introduce Memory Tokens to balance the training signal across examples with different numbers of reference subjects. During inference, Progressive-APG (Adaptive Prompt Guidance) further alleviates oversaturation and improves semantic alignment with user prompts. Finally, we build a high-quality video-subject image dataset through a dedicated data construction pipeline. Extensive experiments show that our method achieves state-of-the-art performance on both single-subject generation and more challenging multi-element scenarios.</p>
      </div>
    </details>


    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Solve the Missing First Step: Can VLMs Standardize Raw Heterogeneous Medical Data?</strong>
          <small>Xin Chen, Dongliang Xu, Cunhao Zhu, Xudong Luo, Haoyang Lyu, Xiaoxiao Sun, Serena Yeung-Levy, Yue Yao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Medical AI</span>
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
          <span>Paper 5 / arXiv:2607.04694</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.04694">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: it evaluates VLMs on a new real-world standardization task for raw heterogeneous medical data, revealing a surprising bottleneck.</p>
        <p class="abstract">As vision-language models (VLMs) are increasingly applied to medical AI, existing benchmarks mainly focus on evaluating their diagnosis ability over given medical images and texts, implicitly assuming that standardized medical images, texts or question-answer pairs are already prepared. However, this assumption does not hold when we apply VLMs in real clinical practice, where medical data is often raw, heterogeneous, and fragmented across different sources. In this paper, we study this missing step, i.e., raw medical data standardization. Specifically, models are given raw dataset folders and evaluated on their ability to identify source formats, convert raw medical images into VLM-compatible visual inputs, extract relevant textual information, and organize the results into structured image-text pairs. To construct this Medical Data Standardization Benchmark (MDS-Bench), we manually annotate 1,939 raw medical data standardization tasks covering diverse clinical practice, radiology modalities, annotation formats, and directory layouts. Extensive experiments show that even the best performing VLMs, i.e., Gemini 3 Flash, achieve only 48.6% end-to-end success rate. Our research highlights raw medical data standardization as a critical bottleneck for medical AI diagnosis in real practice.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>Homer: Understanding Long-form Videos with Hierarchical Memory and Agentic Reasoning</strong>
          <small>Yixin Ji, Fanghua Ye, Juntao Li, Bo Zhao, Zexuan Qiu, Zhaopeng Tu, Liefeng Bo, Min Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Reasoning</span>
<span class="topic-tag">Long-Video Understanding</span>
<span class="topic-tag">Agentic Memory</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2607.02588</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.02588">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 3: it proposes an online memory and agentic reasoning framework for long-form video understanding, relevant to embodied/temporal multimodal reasoning.</p>
        <p class="abstract">Multimodal large language models excel on short clips but struggle on hour-long videos in an online setting, where frames are processed incrementally under limited memory. Existing online methods either retain compact visual representations that lack semantic structure, or build higher-level memory stores organized around temporal proximity rather than explicit causal links, leaving multi-hop narrative reasoning to be reconstructed by the LLM at every query. We bridge this gap with \textsc{Homer}, a Hierarchical Online Memory Exploration and Reasoning framework. \textsc{Homer}&#x27;s memory mirrors the multi-scale structure of long videos, ranging from raw perception, to recurring entities, to events connected by explicit temporal and causal relations. Its agentic reasoner then explores this memory the way humans do, locating the relevant scene, looking up details, and composing the answer through multi-round memory retrieval, with a harness that verifies and corrects each step. \textsc{Homer} outperforms the previous best agent method by $+5.5$, $+10.8$, and $+4.4$ points on M3-Bench-robot, M3-Bench-web, and Video-MME-Long, and consistently lifts three various LLM backbones, indicating a model-agnostic structural capability for grounded retrieval over long videos.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">AI-Generated Image Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Ghosts Beneath Textures: Texture-Relation Cues for Cross-Paradigm AI-Generated Image Detection</strong>
          <small>Haoyu Wang, Yiming Qin, Zhongjie Ba, Ziping Dong, Jishen Zeng, Peng Cheng, Kui Ren</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">AI-Generated Image Detection</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Texture Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2607.03862</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.03862">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it introduces a new benchmark and detection method built around texture relations for generalized AI-generated image detection.</p>
        <p class="abstract">AI-generated images have proliferated rapidly, motivating extensive research. Most existing AI-generated image detectors are developed and evaluated under image-free generation paradigms, such as noise-based or text-guided generation. However, image-conditioned generation has become increasingly important in practical applications, as it enables more fine-grained control over generated content. Detecting AI-generated images across these two paradigms creates a critical cross-paradigm detection problem that has long been overlooked. To study this problem, we construct ConImageGen, a benchmark for cross-paradigm AI-generated image detection. Evaluations on ConImageGen show that existing detectors fail to generalize reliably across image-free and image-conditioned generation. To address this failure, this paper identifies a cross-paradigm forensic cue and provides a new perspective for generalized AI-generated image detection. Specifically, by suppressing semantic interference, we visualize, for the first time, semantics-irrelevant texture patterns across generation paradigms. These patterns exhibit structured local-global texture relations, indicating a generalizable form of forensic evidence. Motivated by this finding, we shift the focus from directly exploiting explicit artifacts to modeling texture relations and propose DTS-Det, a detection framework that captures and leverages such relations for generalized AI-generated image detection. Extensive experiments validate the effectiveness of our method. DTS-Det achieves state-of-the-art performance across diverse evaluation settings, reaching 99.6% ACC on ConImageGen with a 10.5% gain over the best baseline. It also achieves 93.2%/94.1% ACC in cross-dataset evaluation on PicoBanana/RAID and maintains detection rates of 95.2%/88.1% under reconstruction attacks and black-box adversarial attacks, respectively.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Reward Lightning: Fast Video Generation via Homologous Preference Distillation</strong>
          <small>Jiaxiang Cheng, Bing Ma, Xuhua Ren, Kai Yu, Peng Zhang, Tianxiang Zheng, Qinglin Lu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Preference Optimization</span>
<span class="topic-tag">Latent Reward Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2607.03960</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.03960">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 and also strongly fits your interest in generative multi-modal learning: it is a new method for fast video generation with preference alignment and latent reward modeling.</p>
        <p class="abstract">Achieving simultaneous preference alignment and distillation acceleration in video diffusion models remains an open challenge. Existing methods optimize the two objectives over mismatched representation spaces, where improving one objective often compromises the other. To overcome this, we propose Reward Lightning, a unified framework that aligns and accelerates a video diffusion model within a single shared representation. Its central principle is homology: both objectives are evaluated on identical latent features, which mitigates the gradient conflicts that arise when they are optimized over disjoint representations. As a foundational component, we first introduce a latent reward model (LRM) that scores videos directly in the latent space, without decoding back to the pixel space. Building on the LRM, homologous preference distillation (HPD) reuses this shared backbone to perform adversarial distillation and preference alignment jointly, yielding few-step generators that remain faithful and well aligned. Extensive experiments demonstrate that the LRM surpasses pixel-level and latent-level reward baselines by $11.0\%$ and $14.7\%$ in preference accuracy, and that Reward Lightning generates high-fidelity videos in merely $1$ to $4$ steps, improving the average VBench score by $2.1\%$ while leading in text alignment, motion quality, and visual quality. Project page: https://reward-lightning.github.io.</p>
      </div>
    </details>


    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Video Generation Models Are Inherent Lighting Estimators</strong>
          <small>Ziqi Cai, Shuchen Weng, Kaiqi Liu, Zifeng Wang, Zhiquan Zhang, Minggui Teng, Han Jiang, Boxin Shi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Intrinsic Lighting Estimation</span>
<span class="topic-tag">HDR Environment Maps</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2607.04674</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.04674">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it uses video generation models as a lighting estimation tool, turning a generative foundation model into a physical-scene inference system.</p>
        <p class="abstract">Recovering dynamic environment maps from a single in-the-wild video is crucial for photorealistic rendering, yet remains a challenge. Recent video generation models can produce photorealistic scenes with complex lighting, possessing an inherent understanding of lighting. In this paper, we introduce V-LITE (Video generation models are inherent lighting estimators), a framework that unlocks this internal knowledge by reframing lighting estimation as a guided video inpainting task. Inspired by VFX industry practices, we insert a synthetic chrome ball into the scene to compel the model to generate physically plausible reflections from the surrounding spatio-temporal context. To bridge the gap from LDR-native models to the HDR domain, we design an HDR-aware VAE and employ an efficient LoRA-based fine-tuning strategy. We then construct a mixed dataset comprising high-fidelity HDR images to provide realistic HDR priors, and in-the-wild HDR videos to provide dynamic spatio-temporal context. Extensive experiments demonstrate that V-LITE produces temporally coherent HDR environment maps, revealing that modern video diffusion models are not merely synthesizers but also powerful, inherently capable estimators of physical scene lighting.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Scene Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>SynCity 3000: Bootstrapping Scene-Scale 3D Diffusion</strong>
          <small>Paul Engstler, Iro Laina, Christian Rupprecht, Andrea Vedaldi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Scene Generation</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Layout Control</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2607.05392</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.05392">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately: scene-scale 3D scene generation is simulator-adjacent and relevant to embodied environments, though it is more generative 3D synthesis than a benchmark or embodied agent method.</p>
        <p class="abstract">We present SynCity 3000, a framework for generating 3D scenes that are globally coherent while enabling fine-grained layout control. Building on the ability of current image-to-3D generators to produce complex 3D assets from a single image, we extend this capability to the scale of entire scenes by adapting the generator to be applicable as a convolutional operator. We achieve this by fine-tuning the model on scene-like data generated by a new synthetic data engine, which we propose to address the scarcity of 3D scene data for training. The convolutional generator is then applied to a dimetric image of the entire scene, generated from the user prompt, resulting in 3D scenes of arbitrary size and complexity. Across diverse prompts and layouts, SynCity 3000 produces large, coherent, and detailed scenes, addressing the shortcomings of prior approaches to 3D scene generation.</p>
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
          <strong>Wan-Streamer v0.2: Higher Resolution, Same Latency</strong>
          <small>Lianghua Huang, Zhi-Fan Wu, Yupeng Shi, Wei Wang, Mengyang Feng, Junjie He, Chen-Wei Xie, Yu Liu, Jingren Zhou, Ang Wang, Bang Zhang, Baole Ai, Chen Liang, Cheng Yu, Chongyang Zhong, Jinwei Qi, Kai Zhu, Pandeng Li, Peng Zhang, Wenyuan Zhang, Xinhua Cheng, Yitong Huang, Yun Zheng, Yuxiang Bao, Yuzheng Wang, Zoubin Bi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Real-Time Interaction</span>
<span class="topic-tag">Audio-Visual Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.GR</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2607.04443</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.04443">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and partially criterion 4: it is a new native-streaming audiovisual model with higher-resolution interactive output, i.e., an MLLM-style real-time embodied interaction system.</p>
        <p class="abstract">We present Wan-Streamer v0.2, a latency-preserving upgrade of the native-streaming, end-to-end audio-visual interaction model. v0.2 keeps the v0.1 modeling formulation, but raises the interactive output stream from 192x336 to 640x368 while preserving approximately 200 ms model-side signal-to-signal latency at 25 FPS. The higher-resolution stream supports scene-grounded mid-shot agents whose posture, gaze, hands, nearby objects, and local scene layout remain legible during real-time conversation. To support the larger visual stream without adding user-visible delay, v0.2 keeps the thinker as a single-GPU low-latency path for streaming perception, the short language/state Transformer pass that builds the generation cache, and final decoding. The performer becomes a multi-GPU Ulysses-style context-parallel group for the expensive next-unit latent generation. Each performer rank writes incoming K/V into a pre-sharded local cache. The long high-resolution latent video sequence is split across ranks for denoising and gathered through Ulysses communication, while the much shorter audio latent sequence is generated without sequence sharding. In this split, the thinker&#x27;s language/state computation reaches the performer only as K/V conditioning, so no separate language sequence has to be communicated inside the performer group. This concentrates additional hardware on visual generation while preserving the compact thinker-performer boundary, keeping total remote interaction latency at approximately 550 ms when a 350 ms bidirectional network budget is included.</p>
      </div>
    </details>


    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>Enhancing Large Multimodal Models in Key Information Extraction via Scene-Aware Document Synthesis</strong>
          <small>Zhipeng Xu, Zulong Chen, Qing Liu, Junhao Ji, Jinxin Hu, Yipeng Yu, Jianqiang Wan, Jun Tang, Zhao Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Key Information Extraction</span>
<span class="topic-tag">Synthetic Data</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2607.04636</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.04636">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 4: it proposes scene-aware document synthesis to improve a multimodal model for KIE, which is a practical VLM application.</p>
        <p class="abstract">Key Information Extraction (KIE) converts visually rich documents into structured data, but practical deployment remains challenging: strong performance often relies on costly on-server Large Multimodal Models (LMMs), while compact locally deployable models lack sufficient KIE supervision. We present SAYRE, a scene-aware document synthesis framework for generating scalable KIE training data without hand-crafted template design. Given a few exemplar documents, SAYRE captures category-specific content patterns and layout conventions to synthesize document-schema-annotation triples. It further introduces error-driven generation, which expands real-world failure cases into hard training examples while preserving their structural patterns. Experiments on constrained- and open-category KIE show that SAYRE consistently improves Qwen3-VL backbones and achieves the strongest overall performance among on-device LMMs. Data scaling experiments show an overall upward trend as more synthesized data is introduced, especially for smaller models and open-category extraction. Error analysis further shows that synthesized training reduces field-level errors by improving schema-aware extraction over dense tables, business identifiers, and contract clauses. These results establish scene-aware synthesis as an effective data-centric approach for improving practical multimodal KIE.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>GeoSelect: Spatial-Program Execution for Training-Free Referring Remote Sensing Image Segmentation</strong>
          <small>Yuhang Jiang, Guohui Deng, Miaozhong Xu, Chao Ruan, Jinling Zhao, Linsheng Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Referring Segmentation</span>
<span class="topic-tag">Program Execution</span>
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
          <span>Paper 12 / arXiv:2607.03869</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.03869">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 loosely: it is a spatial-reasoning method for referring segmentation with explicit spatial-program execution, but it is not embodied-agent spatial intelligence.</p>
        <p class="abstract">Referring remote sensing image segmentation isolates the object named by a natural-language expression in an aerial image. Existing training-free methods resolve the expression through implicit vision-language activations or region-text similarity, which gives weak control over the spatial, comparative, and ordinal relations that dominate aerial referring: they cannot represent constructions such as the largest ship or the second court from the left. We propose GeoSelect, a training-free pipeline that reframes referring as the execution of a typed spatial program. A frozen, text-only language model synthesises the expression into a small domain-specific language, a well-formedness checker accepts the program, and a deterministic executor runs it. The central abstraction is a single scored candidate set type under which every operator composes: continuous geometric fields realise position and proximity as dense pixel-level maps, while discrete set and order operators add the extremum, ordinal, counted-union, and relational constructions that fields alone cannot express. Because execution is explicit, every intermediate program, field, and ranking is inspectable, and a reliability ladder degrades any failing program to a field-only special case, so every expression returns an answer. GeoSelect attains 58.86 mIoU on RRSIS-D test and 55.27 mIoU on RISBench test, more than twice the best prior training-free method on RRSIS-D, with no referring supervision and on a single GPU. A controlled comparison with candidates and segmenter fixed attributes the gain to explicit execution, not the backbone; an oracle decomposition localises the residual gap to detection recall on RRSIS-D and selection on RISBench, and an exposure audit confirms robustness to pretraining leakage. Code will be released upon acceptance at the project page https://avalon-s.github.io/GeoSelect/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Diffusion</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model</strong>
          <small>Xinyin Ma, Julius Berner, Chao Liu, Arash Vahdat, Weili Nie, Xinchao Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Diffusion</span>
<span class="topic-tag">Autoregressive Generation</span>
<span class="topic-tag">Bidirectional Inference</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2607.03509</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.03509">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately: it is a new generative video foundation model formulation, though the contribution is mainly an inference/training regime rather than a broader vision foundation model application.</p>
        <p class="abstract">Recent progress in large-scale generative models has substantially advanced video generation, yet existing methods remain constrained by a rigid inference paradigm. Bidirectional diffusion models excel at global coherence and visual fidelity but suffer from slow inference, while autoregressive models offer efficient and streaming generation at the cost of long-range consistency and exposure bias. We introduce Flex-Forcing, a unified training and inference framework that enables a video diffusion model to seamlessly operate under both bidirectional and autoregressive generation regimes. The core idea is a flexible chunking mechanism jointly defined over the temporal axis and denoising steps. This design allows the model to (1) perform flexible chunking according to different device budgets, (2) perform bidirectional inference across chunks for global structure planning, while generating frames autoregressively within each chunk for efficient and fine-grained synthesis, and (3) perform any-order, any-timestep autoregressive generation without the strict causal constraint. Extensive experiments on multiple video generation benchmarks demonstrate that Flex-Forcing achieves consistently better video quality, long-video stability than strong baselines with a rigid inference schedule, while offering faster inference.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Egocentric Vision</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>EgoInertia-MI: A Multimodal Egocentric Vision and IMU Benchmark for Motor Impairment Assessment</strong>
          <small>Fatemah Alhamdoosh, Pietro Pala, Abduallah Mohamed, DK Arvind</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Egocentric Vision</span>
<span class="topic-tag">Wearable Sensing</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2607.03934</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.03934">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it is a new benchmark for egocentric vision plus IMU in a motor-impairment assessment setting, an embodied sensing angle.</p>
        <p class="abstract">Motor impairments, including tremor, bradykinesia, gait abnormalities, and postural instability, are common across many neurological and movement-related conditions. Conventional clinical assessments are often intermittent and may fail to capture subtle temporal variations in motor behavior. While wearable IMUs and third-person video have shown promise for objective motor assessment, third-person recordings raise privacy concerns and require constrained acquisition setups. In contrast, egocentric vision provides a more naturalistic and privacyaware alternative. In this work, we introduce EgoInertia-MI, a multimodal benchmark dataset combining synchronized egocentric video and wearable IMU signals for motor impairment analysis. The dataset contains 19 upper- and lower-body activities performed by healthy volunteers simulating varying levels of motor impairment severity levels: no impairment, mild impairment, and severe impairment. We establish two benchmark tasks: action recognition and motor impairment severity estimation, and evaluate multiple unimodal and multimodal baselines. Experimental results show that egocentric video provides strong cues for motor impairment assessment, while multimodal fusion achieves the best overall performance, reaching 0.78 Macro-F1 for severity estimation and 0.93 Macro-F1 for action recognition. These findings highlight the potential of combining egocentric vision and wearable sensing for ecologically valid and privacy-aware motor assessment. Code and data are available at:https://fatemah-alh.github.io/EgoInertia-MI-Page/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Text-to-Image Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>RADIANCE: Relative Adaptive Denoising with IP-Adapter for Novel Concept Enhancement</strong>
          <small>Zi-Xiang Ni, Bo-Lun Huang, Teng-Fang Hsiao, Bo-Kai Ruan, Hong-Han Shuai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Image Generation</span>
<span class="topic-tag">Compositional Generation</span>
<span class="topic-tag">Training-Free Guidance</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2607.05088</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.05088">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to the listed criteria; it is a clever training-free guidance method for compositional text-to-image generation, fitting the friend&#x27;s interest in generative modeling but not a specific criterion.</p>
        <p class="abstract">Text-to-image (T2I) diffusion models have achieved striking progress but still struggle to synthesize rare concepts involving unusual attribute-object pairings, often resulting in concept omission or semantic drift where a dominant entity overwhelms the generation. Tracing these failures to a lack of compositional balance during the denoising trajectory, we propose RADIANCE, a training-free framework that treats inference as a closed-loop feedback process. RADIANCE augments pretrained backbones with three modular components: (1) a Compositional Similarity Monitor (CSM) that tracks the emergence of objects and attributes in intermediate latents via CLIP-based feedback; (2) a Bidirectional Scale Controller (BSC) that applies a reactive &quot;restoring force&quot; using positive and negative IP-Adapter scales to rebalance biased trajectories; and (3) a Feedback Guidance Scheduler (FGS) that coordinates these updates across timesteps without additional training. We further extend the framework to multi-object prompts via Delayed Adapter Activation (DAA) and Layer-wise Alternating Guidance (LAG) to prevent premature concept fusion. By overlapping monitoring and denoising through pipelined execution, RADIANCE maintains competitive latency while significantly enhancing the per-sample success rate and effective throughput. Experiments on RareBench and T2I-CompBench demonstrate that RADIANCE consistently enhances compositional alignment and perceptual quality over state-of-the-art baselines.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Low-Light Enhancement</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>Geometry-aware Depth-guided Representation Learning for Structure-preserving Low-light Image Enhancement</strong>
          <small>Fang Gao, Jiongkai Qin, Jiabao Wang, Jingfeng Tang, Ming Cheng, Hanbo Zheng, Qingbao Huang, Cheng Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Low-Light Enhancement</span>
<span class="topic-tag">Depth Priors</span>
<span class="topic-tag">Structure Preservation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2607.05005</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.05005">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately: it applies geometry-aware depth priors to low-light enhancement, which is a vision foundation model-style downstream application but not a core foundation-model paper.</p>
        <p class="abstract">Low-light degradation reduces image visibility and weakens structural cues that are important for visual representation and scene understanding. Existing low-light image enhancement methods mainly focus on appearance restoration, while insufficiently exploiting scene geometry to preserve structural consistency. To address this limitation, this paper proposes a Depth-guided Multi-scale Attention Network (DMSA-Net) for geometry-aware low-light image enhancement. DMSA-Net introduces depth-related structural priors into low-light representation learning through reflectance-geometry interaction. A Retinex-based decomposition module is first used to obtain illumination-invariant reflectance representations, from which depth cues are inferred to characterize scene structure under degraded illumination. A multi-scale depth-guided fusion strategy is then embedded into a hierarchical encoder-decoder architecture, where depth-aware attention adaptively integrates geometric and appearance features. Experiments on several benchmark datasets show that DMSA-Net achieves effective low-light restoration while improving structural preservation. Moreover, we construct LOL-D, a depth-augmented low-light dataset, to facilitate research on geometry-aware low-light vision.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Adversarial Attacks</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Defending from GeoLocalization through Adversarial Road Trips</strong>
          <small>Niccol\`o Niccoli, Federico Becattini, Lorenzo Seidenari</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Adversarial Attacks</span>
<span class="topic-tag">Geo-Localization</span>
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
          <span>Paper 17 / arXiv:2607.03277</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.03277">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 only weakly: it is about adversarial geolocalization, which touches spatial understanding, but it is not a new embodied spatial-intelligence method.</p>
        <p class="abstract">Retrieval-based image geolocalization has emerged as a powerful technique for determining the location of a query image by matching it against a large, geotagged database. The success of deep learning based approaches has raised concerns regarding privacy and safety. A way to protect users from geolocalization is to design adversarial attacks for such methods. In this paper, we introduce RoadTrip Attack (RTA), a novel and highly effective targeted adversarial attack for geolocalization. RTA conceptualizes the adversarial process as finding an optimal distractor journey to a specific, attacker-chosen location. It employs a beam search algorithm to iteratively construct a sequence of incorrect geographic locations that form a path to the target. At each step, the attack generates subtle perturbations to the query image, guiding the geolocalization model toward the next location in this deceptive path. We show that our method is also strong in black-box settings, obtaining highly transferable attacks with less perceptible image artifacts.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
