

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
      <p class="eyebrow">Daily ArXiv / August 03, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>20</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>15</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">action</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="11 mentions">agent</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="7 mentions">alignment</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">consistently</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">constraint</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="8 mentions">cross-modal</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">detection</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">editing</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">embedding</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="11 mentions">encoder</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">encoding</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="30 mentions">evidence</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">final</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="11 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">fine-tuning</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">flow</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">full</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 46%, var(--accent))" title="14 mentions">generation</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="7 mentions">graph</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="8 mentions">hand</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">improving</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="7 mentions">language</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">latent</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="8 mentions">layer</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">modality</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">multi-modal</span><span class="cloud-word" style="font-size:2.03rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 62%, var(--accent))" title="18 mentions">multimodal</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="7 mentions">must</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">neuron</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="10 mentions">page</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">reasoning</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="9 mentions">region</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">resolution</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="7 mentions">reuse</span><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="12 mentions">safety</span><span class="cloud-word" style="font-size:1.80rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="15 mentions">semantic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">shopping</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="7 mentions">source</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">space</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">stream</span><span class="cloud-word" style="font-size:1.88rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="16 mentions">token</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="6 mentions">understanding</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">unified</span><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="12 mentions">video</span><span class="cloud-word" style="font-size:2.30rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="22 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="87 mentions">action</span><span class="cloud-word" style="font-size:1.59rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="151 mentions">agent</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="84 mentions">alignment</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="62 mentions">attention</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="60 mentions">challenging</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="58 mentions">condition</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="78 mentions">consistency</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="58 mentions">consistently</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="60 mentions">cost</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="79 mentions">detection</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="83 mentions">diffusion</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="69 mentions">domain</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="95 mentions">dynamic</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="71 mentions">environment</span><span class="cloud-word" style="font-size:1.26rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="105 mentions">evidence</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="91 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="67 mentions">foundation</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="58 mentions">fusion</span><span class="cloud-word" style="font-size:2.08rem;opacity:0.82;color:color-mix(in srgb, var(--accent-2) 64%, var(--accent))" title="235 mentions">generation</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="60 mentions">geometry</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="88 mentions">inference</span><span class="cloud-word" style="font-size:1.25rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="103 mentions">interaction</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="132 mentions">language</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="59 mentions">latent</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="79 mentions">memory</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="65 mentions">mllm</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="62 mentions">modality</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="115 mentions">motion</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="177 mentions">multimodal</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="71 mentions">multiple</span><span class="cloud-word" style="font-size:1.50rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="138 mentions">object</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="65 mentions">perception</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="58 mentions">physical</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="84 mentions">pipeline</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="68 mentions">point</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="56 mentions">preserving</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="58 mentions">prompt</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="57 mentions">query</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="80 mentions">real-world</span><span class="cloud-word" style="font-size:1.66rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="162 mentions">reasoning</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="96 mentions">reconstruction</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="77 mentions">region</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="62 mentions">robust</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="141 mentions">scene</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="67 mentions">segmentation</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="179 mentions">semantic</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="84 mentions">space</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="124 mentions">spatial</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="57 mentions">structure</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="71 mentions">support</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="93 mentions">target</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="102 mentions">temporal</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="152 mentions">token</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="63 mentions">trajectory</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="124 mentions">understanding</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="87 mentions">unified</span><span class="cloud-word" style="font-size:2.51rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 87%, var(--accent))" title="325 mentions">video</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="66 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="387 mentions">visual</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="70 mentions">world</span></div>
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
      <summary class="topic-heading">Generative Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>WaiT for the Signal: Simple Frequency-Aware Flow-Matching</strong>
          <small>Krunoslav Lehman Pavasovic, Th\&#x27;eophane Vallaeys, St\&#x27;ephane Mallat, Giulio Biroli, Luke Zettlemoyer, Brian Karrer, Jakob Verbeek</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Flow Matching</span>
<span class="topic-tag">Image/Video Synthesis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
<span class="category-tag">stat.ML</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2607.28760</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.28760">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: a vision foundation model–style generative method for image/video generation with a new frequency-aware architecture and evaluation protocol.</p>
        <p class="abstract">As image generation models scale to ever higher resolutions, global coherence, local detail, and texture fidelity become critical axes for generation quality. However, standard flow matching treats all spatial frequencies uniformly, ignoring the natural frequency hierarchy where high-frequency bands become indistinguishable from pure noise far earlier than coarse structures. We introduce WaiT, a Wavelet-aware image Transformer that decomposes generation into coarse and fine bands via lossless wavelets. True to its name, the high-frequency bands wait for the signal: staying pure noise until coarse structure has emerged, then joining the flow for joint refinement. Since standard FID discards fine-grained detail through aggressive downsampling, we introduce a more stringent three-axis evaluation protocol to assess quality at native resolution. On ImageNet 512x512, WaiT achieves a pixel-space FID of 1.43 and is Pareto-optimal across all three axes, reducing sampling compute by up to 50%. With our largest 2B model, we set a new state-of-the-art FID of 1.3 for pixel-space models on ImageNet 512 resolution. Our formulation outperforms even the strongest latent-space models on texture fidelity, and scales seamlessly to high-resolution OpenImages and to video generation, achieving a state-of-the-art FVD of 0.84 on Kinetics-600 with no algorithmic modifications.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Document VQA</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>HierDoc: Hierarchical Page-to-Region Evidence Routing for Long-Document Visual Question Answering</strong>
          <small>Rongjian Gu, Wengang Zhou, Junyu Xiong, Yonghui Wang, Bing Yin, Bei Wang, Houqiang Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Document VQA</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Evidence Routing</span>
<span class="topic-tag">Long-Context Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2607.29638</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29638">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a new benchmark-style method for long-document VQA with hierarchical page-to-region evidence routing, focusing on a previously under-modeled evidence-selection angle.</p>
        <p class="abstract">Multi-page document visual question answering requires locating sparse evidence at both the page and region levels. Existing approaches typically emphasize one level over the other: page-centric methods focus on page acquisition, with region operations serving mainly as navigation aids, whereas region-centric methods assume that the relevant pages have already been supplied. Consequently, page and region selection remain disconnected rather than forming successive evidence decisions. We propose HierDoc, a hierarchical evidence-routing framework that formulates long-document evidence acquisition as two-stage set prediction from pages to regions. A page policy selects evidence pages from the full document; these pages are then parsed for semantic elements, after which a region policy selects the elements passed to a downstream answer model. Both answer-agnostic policies are optimized with stage-wise GRPO using granularity-specific structured-set rewards. The answer model receives selected full pages together with selected region crops and OCR or table text, preserving global context while emphasizing fine-grained evidence. Across the evaluated benchmarks, HierDoc achieves state-of-the-art or competitive performance among open-weight systems, improving LongDocURL by 16.87% relative to the strongest reported open-weight baseline. Controlled ablations further show that selected regional evidence improves the page-only system in accuracy and F1 by 5.51% and 4.82%, respectively. These results demonstrate the benefit of organizing coarse page routing and fine-grained region routing as successive, separately optimized stages of a unified evidence-acquisition process.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM Safety</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>SafeNexus: Discovering and Steering Modality-Universal Safety Neurons in MLLMs</strong>
          <small>Jian Yu, Fei Shen, Cong Wang, Jian Wang, Lu Jin. Xiaoyu Du, Jinhui Tang, Tat-Seng Chua</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM Safety</span>
<span class="topic-tag">Interpretability</span>
<span class="topic-tag">Neuron Steering</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2607.28969</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.28969">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: a new MLLM safety/intervention framework with neuron-level analysis and cross-modal safety alignment.</p>
        <p class="abstract">Although Large Language Models (LLMs) have demonstrated promising safety performance, extending them to Multimodal Large Language Models (MLLMs) exposes a significant gap between expanded multimodal capabilities and existing safety mechanisms. Current defenses remain predominantly confined to specific modal settings, thereby limiting their robustness against broader cross-modal threats. To bridge this gap, we introduce SafeNexus, a cross-modal safety alignment framework that adopts a dedicated neuron-level intervention strategy. First, we formulate a neuron localization paradigm that identifies functionally specialized neurons by characterizing intermediate-layer activation patterns and quantifying their functional salience through importance scoring. Building upon this paradigm, we exploit contrastive data to identify modality-bound safety neurons (BS-Neurons), and validate their role in regulating safety behavior within each modality via targeted suppression. Further cross-modal analysis defines modality-universal safety neurons (US-Neurons) as the shared subset of BS-Neurons identified across individual modalities, serving as the core for defending against harmful cross-modal attacks. We observe that suppressing these neurons substantially degrades safety performance across modalities, while leaving overall utility largely unaffected. Building on these insights, we propose two safety alignment strategies: activation-level safety amplifier and safety neuron calibrator. The proposed strategies enhance model safety through two distinct routes: the former amplifies the activation magnitudes of US-Neurons, while the latter selectively calibrates them via targeted fine-tuning. Extensive experiments demonstrate that our method outperforms prevailing state-of-the-art approaches on safety benchmarks spanning diverse modality combinations, while effectively preserving utility.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Embeddings</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>ReLoop-UME: Recurrent Depth with Learnable Retrieval Registers for Universal Multimodal Embedding</strong>
          <small>Shijie Wang, Xiangzhao Hao, Yueti Li, Guangyu Cao, Xinyu Tang, Haiyun Guo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Embeddings</span>
<span class="topic-tag">Representation Learning</span>
<span class="topic-tag">Retrieval</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2607.28751</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.28751">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a new universal multimodal embedding method with a recurrent depth/retrieval-register design, relevant to vision-language embedding models.</p>
        <p class="abstract">Universal multimodal embedding (UME) maps heterogeneous multimodal inputs into a shared embedding space. Existing UME models either form embeddings through single forward encoding or add computation through explicit rationale tokens and latent autoregressive states. Although token expansion can improve complex matching, serial generation increases retrieval latency and makes the final embedding depend on generated intermediate states. This raises a different question: can useful computation be expanded along model depth while keeping the token workspace fixed? We analyze positive-negative similarity separation at every layer of independently trained UME models and observe a shared progression: early layers contextualize multimodal inputs, a contiguous middle-to-late stage forms retrieval-discriminative features, and the final layers map them into the embedding space. Based on this finding, we propose ReLoop-UME, which executes the early layers once, recurrently reuses a parameter-shared retrieval-forming block, and applies the final mapping layers after the last loop. Learnable Retrieval Registers provide persistent retrieval-specific states that accumulate and exchange evidence across loops, with the final register serving as the embedding readout. On MMEB-V2 and MRMR, ReLoop-UME consistently improves retrieval across different backbones while running 44.9x faster than UME-R1 and 1.5x faster than PLUME.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Text-to-Motion</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>MoRAE: Flow-Friendly Self-Supervised Latents for Text-to-Motion Generation</strong>
          <small>Yifei Zhu, Mingyi Shi, Yangyang Cai, Miao Cheng, Yoshifumi Kitamura, Taku Komura</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Motion</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Latent Representations</span>
<span class="topic-tag">Flow Matching</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2607.29180</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29180">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 in a broad sense: it proposes a new generative latent-space method for text-to-motion, but it is more about motion generation than spatial understanding for embodied agents.</p>
        <p class="abstract">Text-to-motion generation must produce motions that are semantically correct, temporally coherent, and physically plausible. A natural approach is to first project motion data into a structured semantic space and then train a generative model within that space. Such a paradigm has been highly successful in image generation through Representation Autoencoders (RAEs), where a frozen self-supervised encoder provides semantic features for diffusion or flow models to learn from. However, direct transfer of such a paradigm to motion space using Motion-JEPA as the frozen encoder fails dramatically. We diagnose this failure geometrically and identify two motion-specific bottlenecks: (1) the JEPA feature space is spectrally ill-conditioned, making the Gaussian-to-data transport unstable; and (2) even with a well-conditioned spectrum, flow residuals tend to align with decoder-sensitive directions, where small latent errors are amplified into large motion artifacts after decoding. Based on these insights, we propose MoRAE. MoRAE addresses the two bottlenecks separately. A compact bottleneck distills the structured JEPA representation while removing weak and redundant directions, bringing the latent spectrum into a transport-stable regime. Motion-coupled training then aligns the retained latent geometry with the decoder, making characteristic flow errors less costly after decoding. With this flow-friendly latent, a standard non-autoregressive Flow-Matching DiT achieves state-of-the-art performance.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>OSEF: One-Step Evidence Fusion for Cross-Video Scene Procedure Planning</strong>
          <small>Zhentong Ye, Lei Zhang, Sijia Zhou, Yingda Yu, Yuehan Shi, Jiaqi Xuan, Shuaiwu Dong, Guanchao Tong, Meimei Zhang, Bin Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Procedure Planning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2607.29401</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29401">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new embodied/planning benchmark and method for cross-video scene procedure planning, with evidence retrieval plus planning.</p>
        <p class="abstract">Video Scene Procedure Planning (VSPP) supplies the target start-goal observations in advance, leaving open how a planner should act when the evidence must itself be retrieved. We introduce Cross-Video Scene Procedure Planning (CVSPP): given an answer-redacted start-goal query and K candidate videos, a model must retrieve the supporting video, localize the relevant window, and predict the action sequence. Two obstacles couple here. Same-task demonstrations share stages and windows, and an early hard selection passes the wrong scene chain to the planner. We build an eleven-source benchmark with typed negative roles, a fail-closed answer-leakage gate, and separate Evidence- and Plan-axis metrics. On its 14 source-horizon cells we adapt nine planner families against a majority-sequence floor. We then present One-Step Evidence Fusion (OSEF), which scores a query-conditioned cell-and-span lattice over all candidates and feeds the full soft lattice to the planner through a token-global adapter, cropping no window beforehand. OSEF ranks first on all six cells the benchmark certifies as method-rankable. On four matched same-task COIN and CrossTask cells it improves exact-video-and-plan success by 2.9-10.7 points over an enhanced hard-selection SOTA, and a component study assigns the largest single increment to the token-global interface. Five converted-source cells sit at or near the majority-sequence floor, the benchmark&#x27;s remaining headroom. The supplementary package includes model constructors and evaluation code.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>MoRoute: Dynamic Routing for In-Context Multimodal Video Generation</strong>
          <small>Chong Gao, Jie Ma, Zhan Peng, Chongxiao Wang, Haoxue Wu, Jun Liang, Guanbin Li, Jing Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Generation</span>
<span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Video Diffusion</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2607.29545</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29545">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: a new multimodal video generation framework that uses a frozen VLM to guide synthesis.</p>
        <p class="abstract">Multimodal video generation aims to generate and edit videos conditioned on arbitrary combinations of text, images, and videos within a single model, allowing diverse tasks to share complementary data and generative priors. Unifying these tasks requires multimodal understanding of diverse conditions, which is typically provided by a pretrained vision-language model (VLM). A key challenge is how to connect the VLM&#x27;s hierarchical multimodal representations with a pretrained video diffusion transformer (DiT). Existing methods either inject features from only the final or a few manually selected VLM layers, or jointly train architecture-matched understanding and generation streams, making it difficult to reuse heterogeneous pretrained backbones. We introduce MoRoute, a unified multimodal video generation framework that formulates a frozen VLM and a pretrained video DiT with different architectures as heterogeneous experts connected through dynamic layer routing. For each input, a lightweight block-wise router enables every DiT block to select the VLM layer most relevant to its generation stage, thereby learning an adaptive correspondence between multimodal understanding and video synthesis. MoRoute further incorporates reference images and source videos directly into the DiT token sequence through unified in-context conditioning, preserving fine-grained visual details across diverse generation and editing tasks. Experiments on IntelligentVBench, OpenVE-Bench, and RefVIE-Bench show that MoRoute consistently surpasses the best competing method on each benchmark, improving the average score by 0.15, 0.18, and 0.34 on a 1-5 scale, respectively.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Retrieval</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Multi-Modal Object Re-Identification with Dual Semantic Guidance and Global-Local Mutual Modulation</strong>
          <small>Weixiang Zhou, Xingguo Xu, Yuhao Wang, Cong Wang, Yang Yang, Zhixun Su, Jinshan Pan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Retrieval</span>
<span class="topic-tag">Cross-Modal Alignment</span>
<span class="topic-tag">ReID</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2607.29207</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29207">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: a multimodal retrieval model using semantic guidance and global-local modulation, though it is more task-specific than foundation-model oriented.</p>
        <p class="abstract">Multi-modal object Re-Identification (ReID) aims to retrieve target instances by leveraging complementary information across modalities. However, existing methods suffer from two challenges. First, they often fail to exploit well-aligned and reliable semantic priors, making them vulnerable to background clutter and cross-modal misalignment. On the other hand, they typically rely on holistic feature modeling, overlooking the synergy between global and local representations. To overcome these limitations, we propose a robust multi-modal ReID framework with dual semantic guidance and global-local mutual modulation, which mainly consists of three key components, namely the Text-Semantic Injector (TSI), the Masked Global-Local Modulator (MGLM), and the Hierarchical MoE Fusion (HMF). The TSI enhances semantic awareness by integrating clean and coherent textual features into visual tokens. The MGLM enables part-aware cross-modal interaction through joint guidance from soft masks and global context, improving fine-grained feature alignment. Finally, the HMF adaptively aggregates multi-spectral features under local semantic supervision, yielding discriminative and robust representations. Extensive experiments on three multi-modal ReID benchmarks demonstrate the effectiveness of the proposed method. The code will be made publicly available at https://github.com/zw-absin/DSGM upon acceptance.</p>
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
          <strong>VFAD: Variational Semantic Prompting Meets Frequency-Adaptive Representation Learning for Zero-Shot Anomaly Detection</strong>
          <small>Peng Chen, Kaige Li, Wei Wang, Mingbo Yang, Wenqiang Wang, Li Shen, Fangjun Huang, Chao Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Zero-Shot Anomaly Detection</span>
<span class="topic-tag">Prompt Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2607.29370</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29370">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a CLIP-based zero-shot anomaly detection method using visual foundation model representations and prompting.</p>
        <p class="abstract">Zero-shot anomaly detection (ZSAD) aims to detect and localize anomalies in unseen categories without access to target-specific training data. Although recent CLIP-based methods have demonstrated promising generalization through vision-language alignment, they remain limited in capturing diverse anomaly semantics and subtle local variations. To address these limitations, we propose VFAD, a unified framework that combines variational semantic prompting with frequency-adaptive representation learning. Specifically, we introduce a Variational Semantic Prompt Extractor (VSPE), which adaptively aggregates anomaly-relevant local semantics from dense patch tokens and regularizes them through a variational information bottleneck, thereby incorporating fine-grained visual cues and enabling more precise cross-modal alignment. Furthermore, we develop a Frequency-Adaptive Representation Aggregation (FARA) module that leverages wavelet-based frequency decomposition and frequency-specific expert aggregation to enhance anomaly-discriminative visual representations. By jointly strengthening semantic guidance and visual representation learning, VFAD improves both anomaly discrimination and fine-grained localization. Extensive experiments on 13 industrial and medical benchmarks demonstrate that VFAD consistently outperforms existing state-of-the-art ZSAD methods across diverse anomaly scenarios. The code will be publicly available upon publication.</p>
      </div>
    </details>


    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Uncertainty-Aware Deepfake Detection via Multi-View Structural Learning</strong>
          <small>Muhammad Umar Farooq, Kutub Uddin, Awais Khan, Khalid Malik</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Deepfake Detection</span>
<span class="topic-tag">Uncertainty Calibration</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2607.28769</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.28769">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: vision foundation model application for robust deepfake detection, with CLIP-based features and uncertainty calibration.</p>
        <p class="abstract">Security-critical biometric and forensic applications require accurate predictions and reliable confidence estimates, particularly under distribution shift. This challenge is especially acute for deepfake detection, where foundation-model-based detectors often exhibit overconfident predictions on out-of-distribution manipulations, which limits their suitability for operational deployment. We propose an uncertainty-aware deepfake detection framework that identifies manipulations through inconsistencies across complementary evidence sources. The framework integrates three streams: a visual stream based on an adapted CLIP encoder, a semantic stream that models consistency among facial attributes through differentiable constraints, and a structural stream that captures class-dependent dependency patterns between semantic and forensic features. To effectively combine these signals, we introduce Inter-Branch Disagreement Calibration (IBDC), a disagreement-aware uncertainty modeling mechanism that links predictive uncertainty to conflicts among evidence streams. Extensive cross-dataset experiments using FaceForensics++ as the training source demonstrate that the proposed framework achieves state-of-the-art generalization across multiple out-of-distribution benchmarks while consistently improving calibration and selective prediction performance. These results show that combining complementary evidence with disagreement-aware uncertainty provides a robust foundation for trustworthy and well-calibrated deepfake detection under distribution shift.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Reconstruction</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>OASIS: Occlusion-aware Single-image Hand Avatar Reconstruction via 3D Gaussian Splatting</strong>
          <small>Zhisheng Han, Shiyao Wu, Jiayan Qiu, Yakun Ju, Lu Liu, Le Zhang, Pengfei Feng, Huiyu Zhou, Zheheng Jiang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Gaussian Splatting</span>
<span class="topic-tag">Human Avatar Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2607.29633</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29633">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; this is a 3D hand avatar reconstruction method with Gaussian splatting, which is more a specialized 3D vision/generative reconstruction paper than a new spatial-intelligence or VLLM/embodied-AI benchmark paper.</p>
        <p class="abstract">Single-image 3D hand avatar reconstruction is fundamentally ill-posed and particularly challenging due to limited visual evidence under severe self-occlusion and the complex pose-dependent deformation of highly articulated hands. Existing methods predominantly rely on implicit NeRF-style representations, whose volumetric fitting is computationally expensive and often struggles to preserve fine-grained hand details. In this work, we present OASIS, a tailored 3D Gaussian Splatting framework for single-image hand avatar reconstruction. To faithfully encode sparse image-specific appearance cues in single-view reconstruction, we construct geometry-aligned visual evidence tokens by explicitly aligning input image observations with 3D hand geometry and context-adaptively tokenizing the resulting visual evidence. Since severe self-occlusion makes the reliability of image evidence inherently visibility-dependent, we introduce a visibility-conditioned point-image attention to reliably transfer visual evidence to geometric tokens, yielding occlusion-aware Gaussian features for faithful and robust reconstruction. To further capture non-rigid deformation of articulated hands, we introduce a Feature-on-Mesh representation to enable Gaussian deformation to be guided by local surface stretching. Under this framework, we adopt a one-shot adaptation scheme that learns a shared hand prior from multi-identity training data and then fits it to a target image for target-specific reconstruction. Extensive experiments show that OASIS outperforms existing baselines in both visual fidelity and efficiency across challenging poses and in-the-wild scenarios, and further demonstrates strong versatility in downstream applications such as text-to-avatar generation and texture editing.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal LLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>CodeShrink: Adaptive Visual Compression for Efficient Multimodal Code Understanding</strong>
          <small>Wenxin Tang, Jingyu Xiao, Zhenyu Liu, Zipeng Xie, Junliang Liu, Wang Luo, Yuan Jiang, Yintong Huo, Michael Lyu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Visual Compression</span>
<span class="topic-tag">Code Understanding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.SE</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2607.29637</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29637">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 4 moderately well: an efficiency-oriented MLLM application that adapts visual compression for code understanding, but it is not a core embodied or benchmark paper.</p>
        <p class="abstract">Rendering source code as images offers a promising way to reduce the input costs of Multimodal Large Language Models (MLLMs). Adjusting image resolution can trade visual token cost against content fidelity. However, resolution scaling alone overlooks two sources of inefficiency: blank regions created by line breaks and indentation, and code regions irrelevant to the current instruction. Moreover, the best compression setting varies across inputs, tasks, and models, limiting fixed-ratio strategies. We propose CodeShrink, an adaptive visual compression framework with three components. Blank-Free Rendering replaces whitespace-dependent layouts with compact layouts and explicit structural markers, removing layout-induced tokens. Adaptive Compression Configuration uses a lightweight agent trained with reinforcement learning to predict a per-input setting that balances token efficiency and readability. Dominant Token Selection jointly analyzes the instruction and code image to prune task-irrelevant visual tokens during inference. We evaluate CodeShrink on code question answering, clone detection, and code completion. CodeShrink reduces visual token use by up to 71.2\% while matching or exceeding uncompressed text-only inputs, and consistently outperforms text-based and visual compression baselines across all three tasks. These results show that combining layout compaction, adaptive configuration, and instruction-aware pruning can make multimodal code understanding more efficient. Our code is available at https://github.com/vinsontang1/CodeShrink.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>SciFigPlag-Bench: A Benchmark for Provenance-Aware Scientific Figure Plagiarism Detection</strong>
          <small>Zhiying Cui, Minghao Yang, Linlin Gao, Jie Liu, Pengyuan Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Scientific Document Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2607.29124</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29124">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a vision-language benchmark around scientific figure provenance, grounded in fine-grained visual reasoning.</p>
        <p class="abstract">Scientific figures often encode the visual evidence behind scientific findings, yet figure plagiarism remains underexplored as a benchmarked multimodal evaluation problem. We present SciFigPlag-Bench, a benchmark for provenance-aware reasoning over scientific figures in scholarly documents. Unlike general image-similarity or image-forensics benchmarks, SciFigPlag-Bench evaluates whether a suspicious figure reuses evidence from a specific source figure, how the reused content has been transformed, and where the reused evidence appears. We introduce a factorized taxonomy that separates what is reused from how it is transformed, covering material-preserving reuse, such as full-figure and subfigure reuse, as well as abstract-content reuse, such as data re-expression and structural redraw. Guided by this taxonomy, we construct a hybrid benchmark with 2,582 positive pairs and 2,541 negative pairs, combining documented real-world cases, taxonomy-guided synthetic examples, and visually similar negatives. The benchmark supports four diagnostic tasks: pairwise detection, source attribution, hierarchical reuse-type classification, and reuse correspondence localization. Experiments with diverse vision-language models establish initial baselines and reveal persistent challenges in fine-grained provenance reasoning, reuse-type understanding, and spatial evidence grounding.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Editing</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>Evaluation-Verification Reward for Consistent Multi-Reference Image Editing</strong>
          <small>Yingmao Miao, Pengfei Zhang, Xiaochen Lv, Meng Yu, Lei Sun, Xiangxiang Chu, Chao Shen, Chenhao Lin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Editing</span>
<span class="topic-tag">Reward Modeling</span>
<span class="topic-tag">Multimodal Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2607.29025</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29025">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; it is a reward-design paper for multi-reference image editing, which is relevant to generative modeling and MLLM-based evaluation but not a direct criterion match.</p>
        <p class="abstract">While recent image editing models have made rapid progress, multi-reference editing remains challenging, particularly in maintaining visual consistency across references and ensuring overall visual harmony. Reinforcement learning has proven highly effective for text-to-image generation and single-image editing, but its extension to multi-reference editing is hindered by the absence of suitable reward models that capture multi-image relational constraints. Moreover, naively using multimodal large language models(MLLMs) as zero-shot evaluators faces a key tension between hallucination-prone long-form reasoning and the limited deductive power of short-form judgments. We address these issues with a Multi-dimensional Evaluation-Verification Reward(EVR). EVR decomposes evaluation into distinct visual criteria; for each criterion, an MLLM Evaluator generates multiple candidate hypotheses, and a Verifier grounds each claim in concrete visual evidence to accept or reject it, producing reliable and fine-grained reward signals. Together with a scalable data pipeline, our method enables RL fine-tuning of off-the-shelf editors without architectural changes. Extensive experiments show substantial gains over the base Qwen-Image-Edit, improving consistency and harmony to match or surpass NanoBanana.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Vision-Language</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>On the Efficacy of Self-Supervised Point Cloud Encoders for Efficient 3D Large Language Models</strong>
          <small>Yao Zheng, Tian Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Vision-Language</span>
<span class="topic-tag">Point Cloud Encoders</span>
<span class="topic-tag">Self-Supervised Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2607.29136</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29136">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: study of self-supervised point cloud encoders for efficient 3D large language models, relevant to 3D/embodied vision-language systems.</p>
        <p class="abstract">3D point cloud-language models (3D-LLMs) enable 3D understanding by pairing point cloud encoders with large language models, but existing methods rely on costly multi-modal encoders (e.g., ULIP-2) that require image-text-point cloud alignment on 8x A100-scale compute, creating high barriers for research and deployment. In this work, we systematically investigate whether low-cost self-supervised point cloud encoders, specifically PCP-MAE and Point-MAE, can serve as effective alternatives.   Using MiniGPT-3D as our testbed, we evaluate 7 encoder initialization/pre-training setups (1 multi-modal baseline, 5 self-supervised, 1 random init) under frozen and unfrozen fine-tuning (12 total groups), across 2 architectures (MaskTransformer, PointTransformer), 3 objectives (PCP-MAE, Point-MAE, random init), and 2 datasets (Objaverse 660K, ShapeNet55-34 approximately 50K).   Our experiments reveal three key findings: (1) The four-stage MiniGPT-3D pipeline can effectively train a 3D encoder from random initialization: an end-to-end trained random init encoder reaches 52.50% open-vocabulary accuracy and 44.45 captioning score, approaching top pre-trained variants; (2) Architecture and pre-training objective show strong crossover interaction: PCP-MAE + MaskTransformer achieves 59.00% accuracy (best self-supervised), while Point-MAE + MaskTransformer drops to 46.50%, with the pattern reversed for PointTransformer; (3) Closed-set ModelNet40 classification remains a core weakness of purely geometric encoders, reaching only ~13-18% accuracy vs. ~62% for the multi-modal baseline, even after end-to-end fine-tuning.   Our results offer practical guidelines for cost-effective 3D-LLM design and reveal interaction patterns between self-supervised objectives and encoder architectures.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>5 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">GUI Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation</strong>
          <small>Hang Yan, Zhangxuan GU, Beitong Zhou, Jiaxuan Chen, Runze Li, Yusong Hu, Shuheng Shen, Changhua Meng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">GUI Agents</span>
<span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Action Distillation</span>
<span class="topic-tag">Cross-Platform Policies</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2607.29320</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29320">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a GUI-agent paper on multi-platform embodied interaction with a new training/distillation method for action execution.</p>
        <p class="abstract">Graphical user interface (GUI) agents based on large language models are increasingly deployed across mobile, web, and desktop environments. However, existing agents are typically domain-specific, limiting the deployment and user experience. This motivates the consolidation of specialized models into a single cross-environment policy. Weight merging directly merges domain-specific experts but can corrupt executable actions under expert disagreement, while on-policy distillation (OPD) avoids conflicting teacher supervision yet still treats all response tokens equally during distillation, ignoring that action tokens are the only interface between the environment and the agent. To address this, We introduce MAGA that re-allocates training signal according to the structured action. Based on the correctness of the generated action, it suppresses unnecessary or invalid distillation signals and focuses learning on erroneous actions. Besides, a training-only hint optimizes the supervision signal provided by domain-specific teachers without changing the student input. Across two model scales, MAGA achieves the highest mean success rate, outperforming the strongest baseline by 2.0% at 8B and achieves almost the same average performance with teachers.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>MMShopBench: A Real-Log Benchmark for Multimodal, Multi-Turn Shopping Agents</strong>
          <small>Zeying Hao, Hao Guo, Mengtao Xu, Yimin Hu, Yuheng Song, Zesheng Zhou, Jinsong Lan, Xiaoyong Zhu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Agents</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Shopping Assistant</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2607.29002</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.29002">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: this introduces a new real-log benchmark for multimodal, multi-turn shopping agents, which is a novel benchmark angle for embodied-like agent evaluation with image-and-dialogue grounding.</p>
        <p class="abstract">Online shoppers increasingly turn to AI shopping assistants, using images and multi-turn dialogue to express and refine product needs that are difficult to articulate in text alone. However, existing benchmarks largely rely on text-only or synthetic requests, underrepresenting complex real-world shopping requirements jointly expressed through images and language. We introduce MMShopBench, the first real-log benchmark for multimodal, multi-turn shopping agents. Built from carefully cleaned and manually annotated shopping logs, MMShopBench provides ground-truth annotations of each request&#x27;s purchase intent and mandatory product requirements. Agents must infer these requirements jointly from user images and multi-turn dialogue, retrieve candidate products through image and text search, and verify that each candidate satisfies all requirements using its product images and structured attributes. We evaluate representative open-source and proprietary models using an evidence-grounded multimodal protocol and construct a companion training set for fine-tuning an open-source model. To ensure reproducible experimentation, we build an offline shopping sandbox, where fine-tuning substantially narrows the performance gap between our open-source model and leading proprietary models, demonstrating the effectiveness of our training data.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal LLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding</strong>
          <small>Xinkui Zhao, Enbo Chen, Yifan Zhang, Chang Liu, Guanjie Cheng, Naibo Wang, Yueshen Xu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Video Understanding</span>
<span class="topic-tag">Agentic Memory</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2607.28678</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.28678">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and partly criterion 3: this proposes a multimodal agentic memory framework for long-form video understanding, aimed at improving MLLM-style reasoning over long horizons.</p>
        <p class="abstract">Multimodal agents operating in long-horizon environments must build and continually update multimedia memories to support entity-consistent, temporally grounded reasoning. However, existing agentic memory approaches often discard fine-grained dentity cues under aggressive compression and segment-wise processing. They also rely heavily on vector similarity retrieval, which can surface semantically related yet identity-mismatched evidence, leading to entity confusion, error propagation, and hallucinated answers.   We propose ViSAGE, a multimodal agentic memory framework that constructs self-correcting, entity-centric memories. Specifically, ViSAGE anchors entity identity via cross-modal binding over long temporal ranges. It then applies bidirectional memory refinement to propagate delayed identity evidence, retroactively unifying historical records and improving future reasoning. We also introduce multi-agent cross-verification to assess retrieved evidence under an identity-evidence alignment onstraint, enabling abstention instead of unsupported answers when evidence is missing. Extensive results demonstrate that ViSAGE consistently outperforms the strongest baseline, achieving 5.9% higher accuracy.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Multi-Agent Planning with Spatio-Temporal and Topological Constraints using STL-GO</strong>
          <small>Sheryl Paul, Vidisha Kudalkar, Anand Balakrishnan, Lars Lindemann, Alberto Speranzon, Jyotirmoy V. Deshmukh</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Multi-Agent Planning</span>
<span class="topic-tag">Formal Methods</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.MA</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2607.28679</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.28679">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 fairly well: it is a new multi-agent planning method with spatio-temporal and topological constraints, evaluated on a multi-UAV search-and-rescue benchmark, which is closely related to embodied/multi-robot planning in simulated settings.</p>
        <p class="abstract">Multi-agent planning problems arise in a variety of engineering applications, such as multi-robot wildfire fighting and unmanned aerial inspection in factories. A particular challenge is the existence of spatio-temporal (i.e., when and/or where an agent should do what) and topological constraints (i.e., how agents should interact), as typically formalized via the notion of graphs. Over the last years, various frameworks have been proposed that can capture such constraints via spatio-temporal logics. We focus here on spatio-temporal logic with graph operators (STL-GO), a recent formalism that supports reasoning about multiple agents and their topologies, such as sensing, communication, and task topologies. In this paper, we consider the problem of planning multi-agent paths that satisfy constraints written in STL-GO. This problem is particularly challenging due to the need of encoding multiple, potentially time-varying graphs via the graph operators inherent to STL-GO. We present two encodings of this problem, one based on mixed-integer programming (MIP) and another based on satisfiability modulo theory (SMT), with soundness guarantees. We provide a unified interface for specifying agent constraints, their graph topologies, and the STL-GO specification, enabling seamless use of both methods and facilitating direct comparison between them. We evaluate both encodings on a multi-UAV search-and-rescue benchmark, ablating over team size and graph complexity, highlighting the expressiveness of the proposed encodings under dynamic multi- graph interactions.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>EarlyDx: An Admission-Anchored Benchmark for Open-Ended Generation of Evidence-Supported ED-Encounter Diagnoses</strong>
          <small>Jiahui Li, Ruili Fang, Zishuai Liu, Yutong Guo, Nan Yang, Wenzhan Song, Jin Lu, Fei Dou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Medical AI</span>
<span class="topic-tag">LLM-as-Judge</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 20 / arXiv:2607.28788</span>
          <a class="paper-action" href="https://arxiv.org/abs/2607.28788">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new benchmark for open-ended diagnosis generation with evidence support, though it is medical AI rather than embodied AI.</p>
        <p class="abstract">Clinical diagnosis at hospital admission must be made rapidly from limited, incomplete evidence. Existing diagnosis-prediction benchmarks are poorly suited to this setting: they restrict prediction to closed code sets, exclude free-text notes, and supervise with discharge diagnoses that incorporate the full inpatient course. We introduce EarlyDx, a large-scale benchmark for open-ended early diagnosis, built from 154,834 emergency department encounters in MIMIC-IV. Each encounter is restricted to records available at admission time $t_0$ and supervised by the diagnoses recorded during the ED encounter rather than at discharge. An LLM auditor further verifies every free-text label as supported, partially supported, or unsupported by that evidence; the primary evaluation scores only fully supported labels. Under a semantic LLM-as-judge protocol, no evaluated system --- frontier general, medical-specialized, or in-domain post-trained --- synthesizes admission-time evidence reliably. Zero-shot models score largely by extraction, recovering only 3-31% of diagnoses that must be inferred rather than read from the record; post-training raises inference-dependent recall to 56%, but a sizeable margin remains, and on time-critical conditions no system attains a clinician&#x27;s balance of sensitivity and precision. We release the full construction and evaluation pipeline at here.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-07-27.html">
          <span>July 27, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-24.html">
          <span>July 24, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-23.html">
          <span>July 23, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-22.html">
          <span>July 22, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-21.html">
          <span>July 21, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-07-20.html">
          <span>July 20, 2026</span>
        </a>


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
