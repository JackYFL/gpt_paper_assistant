

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
      <p class="eyebrow">Daily ArXiv / September 04, 2026</p>
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
      <strong>16</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>11.3</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.25rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 73%, var(--accent))" title="15 mentions">action</span><span class="cloud-word" style="font-size:2.67rem;opacity:0.97;color:color-mix(in srgb, var(--accent-2) 95%, var(--accent))" title="19 mentions">agent</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">answer</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">appearance</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">autonomous</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">challenging</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="11 mentions">concept</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">depth</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">diffusion</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">domain</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="8 mentions">driving</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">dynamic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">erasure</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="9 mentions">evidence</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">foreground</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="8 mentions">future</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">gaussian</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="20 mentions">generation</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="11 mentions">geometry</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">inference</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">instruction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">matching</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">mechanism</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">meeting</span><span class="cloud-word" style="font-size:1.63rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="10 mentions">multimodal</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">necessary</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">observation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">paradigm</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">path</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">precise</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">reasoning</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">safety</span><span class="cloud-word" style="font-size:1.63rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="10 mentions">scene</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">segmentation</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">semantic</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="8 mentions">shape</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">sparse</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="8 mentions">spatial</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">success</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">trajectory</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">unified</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="7 mentions">user</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="8 mentions">video</span><span class="cloud-word" style="font-size:2.47rem;opacity:0.92;color:color-mix(in srgb, var(--accent-2) 84%, var(--accent))" title="17 mentions">visual</span><span class="cloud-word" style="font-size:1.89rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 55%, var(--accent))" title="12 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="132 mentions">action</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="205 mentions">agent</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="96 mentions">alignment</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="86 mentions">attention</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="77 mentions">change</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="92 mentions">consistency</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="88 mentions">control</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="78 mentions">dense</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="116 mentions">detection</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="90 mentions">diffusion</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="80 mentions">driving</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="103 mentions">dynamic</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="79 mentions">environment</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="208 mentions">evidence</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="77 mentions">fine-grained</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="103 mentions">frame</span><span class="cloud-word" style="font-size:1.92rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="241 mentions">generation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="74 mentions">generative</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="77 mentions">geometric</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="78 mentions">geometry</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="75 mentions">grounding</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="108 mentions">inference</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="115 mentions">interaction</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="105 mentions">language</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="113 mentions">latent</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="124 mentions">memory</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="80 mentions">mllm</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="113 mentions">motion</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="191 mentions">multimodal</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="82 mentions">multiple</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="177 mentions">object</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="97 mentions">observation</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="75 mentions">perception</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="78 mentions">pipeline</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="108 mentions">point</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="74 mentions">policy</span><span class="cloud-word" style="font-size:1.81rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="220 mentions">reasoning</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="79 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="78 mentions">region</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="83 mentions">retrieval</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="89 mentions">reward</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="156 mentions">scene</span><span class="cloud-word" style="font-size:1.99rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 60%, var(--accent))" title="255 mentions">semantic</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="93 mentions">space</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="154 mentions">spatial</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="100 mentions">structure</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="76 mentions">structured</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="111 mentions">supervision</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="87 mentions">support</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="142 mentions">target</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="113 mentions">temporal</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="135 mentions">token</span><span class="cloud-word" style="font-size:1.39rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="148 mentions">trajectory</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="94 mentions">understanding</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="81 mentions">unified</span><span class="cloud-word" style="font-size:2.09rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 65%, var(--accent))" title="275 mentions">video</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="85 mentions">view</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="106 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="434 mentions">visual</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="106 mentions">world</span></div>
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
      <summary class="topic-heading">Multimodal World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States</strong>
          <small>Kang Liao, Yihang Luo, Xiao-Ming Wu, Linyi Jin, Size Wu, Chunyu Lin, Yao Zhao, Fei Wang, Wei Li, Chen Change Loy</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal World Models</span>
<span class="topic-tag">3D Scene Generation</span>
<span class="topic-tag">Physical Simulation</span>
<span class="topic-tag">Vision-Language Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2609.04196</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.04196">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and criterion 4 very closely: a unified multimodal model with native 3D world states for world generation, reconstruction, and physical understanding.</p>
        <p class="abstract">We propose Puffin-World, a unified multimodal architecture that integrates physical understanding, spatial simulation, and 3D world generation and reconstruction without relying on external offline modules. To reliably construct and interact with 3D worlds, our framework jointly models three native world states: physics (gravity field and latitude), geometry (depth), and appearance (image), together with a unified Omni-Camera representation that supports diverse tasks and flexible motions. Beyond modeling these states, we introduce a strategy for propagating physical dynamics across future frames. By grounding absolute camera properties in the real world, Puffin-World enables physically consistent and visually stable world generation. We further couple appearance and geometry within a single generative process, jointly synthesizing each future view and reconstructing its underlying geometry. This unified paradigm enables interleaved closed-loop applications requiring synergy across multiple tasks, including mimic and self-calibrated world exploration. To scale Puffin-World to complex scenarios, we construct Puffin-16M, comprising 15 million vision-language-camera triplets and 1 million trajectories featuring various and challenging motions. To foster further research in this area, we released the code, models, and datasets.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs</strong>
          <small>Junqing Du, Fernando Ropero, Erkin Turkoz, Yanfeng Zhang, Lu Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">3D Scene Graphs</span>
<span class="topic-tag">Multimodal LLMs</span>
<span class="topic-tag">Embodied AI</span>
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
          <span>Paper 2 / arXiv:2609.03892</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03892">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: it proposes a training-free spatial reasoning framework for MLLMs using 3D scene graphs, BEV rendering, and egocentric grounding.</p>
        <p class="abstract">3D spatial reasoning underpins understanding and acting in the physical world, yet it remains unreliable in current multimodal large language models (MLLMs). These models falter at precise geometric measurement, at transforming between egocentric and allocentric viewpoints, and at grounding fine-grained appearance. The most common remedies fine-tune the model on large-scale curated spatial-reasoning datasets or attach dedicated encoders for 3D geometry, which typically couples the solution to costly supervision and a specific backbone. We instead introduce GraFT, a training-free framework that supplies the missing 3D structure through a compact, easily maintained 3D scene graph (3DSG). From this 3DSG, GraFT provides three spatial reasoning capabilities: (1) deterministic geometry through symbolic tools, (2) allocentric layout through a bird&#x27;s-eye-view (BEV) rendering, and (3) visual-attribute grounding through task-relevant egocentric frames. On ScanQA, GraFT improves every metric over the same-backbone baseline, raising CIDEr by 27%. On VSI-Bench, GraFT improves frozen MLLMs by up to 65%, surpassing every proprietary and general-purpose open-source baseline, and several prominent fine-tuned spatial models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language-Action</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving</strong>
          <small>Ruoyu Yao, Yusen Xie, Qingzhao Liu, Pei Liu, Zewei Yang, Yipeng Zhu, Xiaolong Wang, Jun Ma</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Simulator Evaluation</span>
<span class="topic-tag">Latent Planning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2609.04070</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.04070">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and criterion 3 very closely: a new VLA/VLM-grounded method for end-to-end autonomous driving with closed-loop simulator evaluation.</p>
        <p class="abstract">Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground semantic understanding in precise motion execution. We first design an action tokenizer based on a residual vector-quantized variational autoencoder (VQ-VAE), capturing vehicle kinematics and encoding trajectory features into a structured latent space. Rather than discrete codebook lookups that inevitably introduce quantization errors, LaPla repurposes this representation as a physical prior to bridge the modality gap between high-dimensional semantics and the raw action space. Specifically, given multimodal inputs integrating multi-view images, historical actions, and textual instructions, LaPla incorporates concurrent action queries to causally attend to the multimodal context in a single forward pass, projecting hidden states directly into the pretrained VQ-VAE latent space. The frozen decoder then translates these continuous latents into actions, effectively eliminating quantization errors and ensuring physically plausible trajectories while bypassing time-consuming autoregressive generation. Extensive experiments on the nuScenes benchmark demonstrate that LaPla achieves competitive open-loop performance, reducing long-horizon L2 error by 15.52% compared to state-of-the-art VLA methods. Closed-loop evaluations on the NVIDIA AlpaSim simulator further confirm its superior capability in ensuring smooth driving progress, improving the success rate by 33.34 percentage points with significantly reduced inference latency.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Diffusion</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping</strong>
          <small>Zelong Lv, Sicheng Xu, Jianfeng Xiang, Ruicheng Wang, Yue Dong, Yu Deng, Guangzhong Sun, Jiaolong Yang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Diffusion</span>
<span class="topic-tag">3D Memory</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Spatial Consistency</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2609.03919</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03919">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 and partially criterion 1: it is a generative video/world model with persistent 3D memory for world-consistent scene generation, strongly relevant to vision foundation models and spatial understanding.</p>
        <p class="abstract">We present OctWorld, a video diffusion framework with persistent 3D memory for generating explorable, world-consistent, and high-fidelity visual scenes. Given a single image, OctWorld performs stable autoregressive world generation along user-specified camera trajectories. We focus on long-range generation, characterized by extended camera paths and wide viewpoint coverage, where preserving spatial consistency is particularly challenging when previously generated regions are revisited. To address this problem, we introduce OctMap, an extensible and spatially adaptive 3D memory that progressively fuses generated visual observations and their corresponding depth maps into a global representation. OctMap employs TSDF fusion within a dynamic sparse octree whose spatial resolution adapts to image evidence. This design preserves geometric and appearance details across diverse scene scales while maintaining low memory overhead. Experiments demonstrate that OctWorld generates long-range, spatially consistent videos and outperforms prior methods on both existing benchmarks and challenging long-range generation settings. OctMap also provides clear advantages over point-based caches and fixed-resolution TSDF volumes. Project page: https://maxtirerror.github.io/octworldpage/</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Drive-HWM: Hierarchical World Models for Dynamic-Latent Guided Autonomous Driving</strong>
          <small>Zhaoxin Fan, Tianbao Zhang, Wenjun Wu, Xiaofeng Wang, Yeying Jin, Jian Zhao, Zheng Zhu, Shuicheng Yan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Embodied Decision Making</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2609.03572</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03572">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: an embodied-autonomous-driving world-model method with hierarchical slow-fast planning and multimodal action generation, focusing on a new modeling angle.</p>
        <p class="abstract">World models offer a promising paradigm for autonomous driving by predicting how traffic scenes may evolve and using such predictions to support action generation. However, existing approaches either separate future prediction from action generation or jointly predict them at the same temporal scale, making it difficult to simultaneously achieve long-horizon anticipation and responsive, observation-grounded decision making. We present Drive-HWM, a hierarchical slow--fast world modeling framework that organizes future representation prediction and action generation at complementary temporal scales. The slow world model predicts multi-step future representations to capture extended scene evolution. To explicitly model the abundant motion dynamics in driving environments, we introduce Dynamic-Aware Latents learned through optical-flow prediction. Guided by these future representations, the fast model uses a lightweight multimodal backbone and an autoregressive expert to jointly predict the next frame and the immediate action from the latest observation. Next-frame prediction encourages the fast model to capture imminent scene evolution, while one-step action generation allows decisions to be continuously updated as new observations arrive. Extensive experiments on NAVSIM v1 and v2 demonstrate the strong driving performance of Drive-HWM. Comprehensive ablation studies further validate the effectiveness of the hierarchical slow--fast design, dynamics-aware future representations, and joint next-frame and action prediction.</p>
      </div>
    </details>


    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Understanding Autonomous Driving Datasets by Describing Differences between Image Subsets in Natural Language</strong>
          <small>Julian Truetsch, Felix Hauser, Christoph Stiller, Frank Bieder</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Vision-Language Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.LG</span>
<span class="category-tag">cs.NE</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2609.03677</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03677">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 and 4 somewhat: proposes a benchmark for understanding autonomous driving datasets via natural-language difference captioning, with a novel evaluation setting.</p>
        <p class="abstract">Understanding the composition of large-scale autonomous driving datasets is essential for safety, robustness, and reliable operation across domains. For example, domain shift between locations could lead to the operating environment being misaligned with the training data, resulting in potentially dangerous performance degradation. Yet, existing data analysis pipelines largely rely on metadata, predefined labels, or manual inspection, which provide limited semantic insight or do not scale. This paper studies set difference captioning: given two subsets of images, the goal is to produce a natural-language hypothesis describing differences between the target and reference set. Building on a two-stage formulation, we adapt the method to autonomous driving by focusing on object-centric patches derived from object detection, which simplifies aggregation and enables attribution of differences to specific object instances or categories. To evaluate this setting in-domain, we introduce a new benchmark, AD-Diff Bench. Low-concentration experiments assess the suitability of set-difference-captioning approaches to sparse, real-world differences. We restrict our experiments to open-weight models to support reproducibility and ease of deployment. The proposed benchmark and analysis provide a step towards practical, human-interpretable dataset introspection for autonomous driving datasets. Our implementation and benchmark dataset are available at https://github.com/KIT-MRT/AD-Diff</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Text-to-Video Diffusion</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>EraseSAE: Surgical Concept Erasure in Text-to-Video Diffusion Models via Sparse Autoencoders</strong>
          <small>Xinghao Wang, Dong Li, Wei Yu, Yingwei Pan, Tao Gong, Qi Chu, Nenghai Yu, Ting Yao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Video Diffusion</span>
<span class="topic-tag">Concept Erasure</span>
<span class="topic-tag">Sparse Autoencoders</span>
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
          <span>Paper 6 / arXiv:2609.03629</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03629">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a vision generative-model paper on surgical concept erasure in text-to-video diffusion models using sparse autoencoders.</p>
        <p class="abstract">Recent advances in text-to-video (T2V) diffusion models have demonstrated remarkable generative capabilities, yet their reliance on loosely curated training data raises pressing safety and copyright concerns. Concept erasure offers a principled remedy by removing unwanted semantics from pretrained models while preserving remaining concepts. However, existing approaches typically operate at a coarse granularity misaligned with the fine-grained, distributed nature of concept representations, leading to incomplete removal or degraded generation quality. We argue that surgical erasure fundamentally requires intervention at the level of monosemantic features, where each unit encodes a single interpretable concept. To this end, we propose EraseSAE, a novel framework that leverages sparse autoencoders to achieve surgical concept erasure in DiT-based T2V diffusion models via a principled decompose-attribute-erase pipeline. We first introduce the Partitioned Convolutional Sparse Autoencoder, which decomposes dense spatiotemporal activations into disentangled, interpretable sparse features while preserving spatiotemporal coherence. A contrastive attribution mechanism then contrasts activations from paired prompts to isolate concept-specific feature kernels. At inference, timestep-resolved spatiotemporal masks derived from the identified kernels confine erasure to regions where the target concept is active, leaving unrelated content intact. Extensive experiments across diverse diffusion models and concept erasure tasks demonstrate that EraseSAE achieves precise and robust concept removal with minimal quality degradation, substantially outperforming state-of-the-art methods. The code is available at https://github.com/HiDream-ai/EraseSAE.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>SafeRI: Recognition and Intervention for Token-Level Safety Intervention in Large Vision Language Models</strong>
          <small>Caoyuan Ma, Tian Gu, Wenpu Liu, Weichu Xie, Shuai Dong, Yuqi Xu, Ji Zhao, Ziyue Wang, Wenzheng Chang, Taiqiang Wu, Yongfu Zhu, Wenqi Shao, Zheng Wang, Yinqiang Zheng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Safety Alignment</span>
<span class="topic-tag">LoRA</span>
<span class="topic-tag">Token-Level Intervention</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2609.03544</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03544">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: a new safety intervention method for large vision-language models with token-level gated LoRA control.</p>
        <p class="abstract">Existing safety alignment methods for vision-language models usually modify the model behavior globally: once the safety parameters are trained or loaded, they participate in both unsafe and already-safe generations. This always-on intervention can unnecessarily perturb the model&#x27;s original reasoning path and degrade general multimodal capabilities. We argue that safety alignment should be an on-demand intervention rather than a permanent modification to every decoding trajectory. To this end, we propose a streaming recognition and gated LoRA framework for intrinsic VLM safety. During autoregressive generation, a lightweight recognizer estimates whether the current pre-token generation state is safe or unsafe. Its output updates the LoRA gate for the following decoding step; otherwise, generation follows the frozen-backbone policy. The LoRA module is trained from unsafe prefixes, transition statements, and safe continuations, so that it learns to redirect unsafe generations back to safe responses after activation. Experiments across multiple safety and general-purpose benchmarks demonstrate the effectiveness of our method in post-alignment settings.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">In-Context Segmentation</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>FoRIS: Progressive Foreground Refinement for Training-Free In-Context Segmentation</strong>
          <small>Ming Hu, Jianfu Yin, Mingyu Dou, Miaomiao Zhang, Yao Wang, Cong Hu, Bingliang Hu, Quan Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">In-Context Segmentation</span>
<span class="topic-tag">Training-Free Methods</span>
<span class="topic-tag">Segmentation Refinement</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2609.03384</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03384">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: proposes a new training-free method for in-context segmentation with a coarse-to-fine refinement perspective and foreground consolidation.</p>
        <p class="abstract">In-Context Segmentation (ICS) aims to precisely segment arbitrary semantic concepts, such as objects or parts, given one or a few annotated visual exemplars. In this paper, we revisit ICS from a more classical segmentation perspective, viewing it as a coarse-to-fine progressive refinement process. Rather than directly predicting the final mask through reference-query matching, we progressively refine the segmentation from coarse and ambiguous foreground responses to precise and complete foreground structures. Building upon this perspective, we propose a training-free in-context segmentation framework, termed FoRIS. Specifically, FoRIS consists of three key stages: Foreground Purification, Foreground Localization, and Foreground Consolidation, which progressively suppress background distractions, localize discriminative target regions, and recover complete foreground structures through semantic aggregation. Experimental results demonstrate that FoRIS achieves SOTA performance across semantic and part segmentation tasks, with average improvements of 4.5 and 4.8 mIoU points over existing approaches in the 1-shot and 5-shot settings, respectively. Code: https://github.com/Xi-Mu-Yu/FoRIS.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Editable Visual Design</strong>
          <small>Junyan Ye, Wei Liu, Dongzhi Jiang, Zichen Wen, HaoDong Li, Zhutao Lv, Jiaxin Lin, Jinhua Yu, Jun He, Zilong Huang, Rui Chen, Weijia Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Generative Design</span>
<span class="topic-tag">Coding Agents</span>
<span class="topic-tag">Interactive Editing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2609.04034</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.04034">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it applies VLMs and generative models to editable visual design, with a coding-agent workflow built around image generation and visual editing.</p>
        <p class="abstract">While diffusion base models such as GPT-Image-2 and Nano-Banana exhibit remarkable visual expressiveness, their end-to-end generation inherently yields flattened bitmaps with error-prone text, precluding layer-wise post-editing. Conversely, code-based visual generation via Coding Agents provides precise layout control and decoupled layers, yet remains constrained by a lack of global aesthetic intuition and the difficulty of coding complex visual assets.   To address this, we propose Editable Visual Design, a new paradigm driven by a Coding Agent. We designate the VLM as the ``creative brain&#x27;&#x27; for requirement comprehension, task planning, and aesthetic judgment, while utilizing the image generation model as an on-demand ``visual world simulator&#x27;&#x27; to synthesize standalone visual assets. Operating under an ``imagine first, then act&#x27;&#x27; closed-loop workflow, the agent generates isolated assets, writes native HTML/CSS, and iteratively refines the design against visual rendering feedback.   Furthermore, Agent Design Replay faithfully reproduces the creative and reasoning trajectory akin to that of professional human designers. Ultimately, the system delivers editable artifacts with decoupled layers and real text, enabling users to perform intuitive mouse dragging and layout adjustments on a graphical user interface. Validations on posters, infographics, and other scenarios show that this paradigm successfully achieves both refined aesthetics and production-grade editability.</p>
      </div>
    </details>


    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>KnowVis: Knowledge-Centric Visual Summarization for Video Lectures</strong>
          <small>Yi Xu, Yifan Hou, Xiaoyu Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Video Summarization</span>
<span class="topic-tag">Educational AI</span>
<span class="topic-tag">Multimodal Dataset</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2609.03742</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03742">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: vision foundation models applied to educational video summarization, with a new multimodal dataset and visual summarization framework.</p>
        <p class="abstract">Video lectures are valuable educational resources, but their dense and lengthy formats often overwhelm novice learners. This difficulty stems from a fundamental pedagogical mismatch: while videos deliver transient information linearly, human learning requires constructing interconnected cognitive networks, a task that induces severe cognitive overload for novice learners lacking prior domain knowledge. Existing video summarization methods fail to resolve this mismatch, as they primarily produce text-heavy, linear condensations that still demand high cognitive effort. To bridge this gap, we propose KnowVis, a framework that transforms linear video lectures into pedagogically grounded visual narratives. KnowVis first extracts a detailed concept map from multimodal video content to identify important and challenging threshold concepts, then constructs structured knowledge units, and finally synthesizes engaging visual summaries. Alongside the framework, we introduce a curated dataset of 125 educational videos across 10 academic disciplines, paired with 1,079 generated visual summaries. Extensive automated evaluations and a human study demonstrate that, compared to state-of-the-art baselines, KnowVis generates more accurate and clear visuals that successfully reduce cognitive load and significantly improve student learning effectiveness and knowledge retention.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Gaussian Splatting</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>TruncGradGS: Improved 3D Gaussian Splatting via Truncated Gradient Updates</strong>
          <small>Theo Morales, Nhat-Quynh Le-Pham, Robin Atkins, Binh-Son Hua</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Gaussian Splatting</span>
<span class="topic-tag">Novel View Synthesis</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Optimization</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.GR</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2609.03534</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03534">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: adds a new benchmark dataset for dynamic 3D Gaussian Splatting and a method for improving scene reconstruction.</p>
        <p class="abstract">3D Gaussian Splatting has become a de facto scene representation for novel view synthesis, yet robustly learning 3D Gaussian primitives from visual input remains challenging. Standard optimization relies on gradient-based updates, but a common issue is the gradient vanishing phenomenon: a pixel far from a Gaussian primitive often has diminishing gradient magnitudes to influence primitive attributes, resulting in suboptimal scene reconstruction. In this paper, we propose a method to address gradient vanishing with a piecewise truncated gradient formulation that improves the optimization stability and robustness to initializations. We show that our method consistently improves 3D Gaussian Splatting with random and COLMAP initializations while being generalizable across static and dynamic Gaussian Splatting. As a by-product, we also examine the limitations of current benchmarks for dynamic scenes, and introduce a novel dataset for benchmarking dynamic Gaussian Splatting using synthetic 3D scenes. We demonstrate the effectiveness of our method in both static and dynamic settings for the public benchmarks and our proposed dataset.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Vision</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>TokenMatch: 3D Mesh Correspondence Transformer with Curvature-Guided Tokenisation</strong>
          <small>Adeela Islam, Zorah L\&quot;ahner, Vittorio Murino, Vladislav Golyanik</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Vision</span>
<span class="topic-tag">Shape Correspondence</span>
<span class="topic-tag">Transformer Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2609.04202</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.04202">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: a transformer-based 3D correspondence method for geometric vision, with curvature-guided tokenisation and strong practical results.</p>
        <p class="abstract">While data-driven 3D shape correspondence estimation has recently seen substantial progress, robust matching under partial observations and strong non-isometric deformations remains challenging. Existing learning-based approaches often rely on hand-crafted descriptors or template-based representations, whereas recent generative models over functional maps suffer from high inference cost, limited interpretability, and poor generalisation to partial shapes. In response to these limitations, this paper introduces TokenMatch, a new transformer-based unified model for estimating 3D shape correspondences. Our feed-forward approach trained exclusively on BeCoS, a challenging non-isometric partial-to-partial shape-matching dataset, can generalise to matching full shapes without retraining or fine-tuning. TokenMatch uses self- and cross-attention mechanisms to efficiently learn patch-level and point-level relations as well as dense correspondences between shape pairs. Our core insight is that meshes can be adaptively tokenised into patches using shape curvature guidance, enabling effective learning of shape-specific geometric descriptors for correspondence estimation. We evaluate TokenMatch on standard benchmarks for partial and full shape matching, including CP2P, PSMAL, BeCoS, FAUST, SCAPE, and SHREC&#x27;19. Our method achieves consistently high performance, in most cases outperforming existing methods for partial and full shape matching in the mean geodesic error and intersection-over-union metrics, while also running faster at sub-second inference speeds.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical VLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>MedQA-MM: Shortcuts Behind Medical Visual Reasoning</strong>
          <small>Benlu Wang, Yifan Zhang, Jiaqing Yu, Chin Siang Ong, Juncheng Huang, Zhuohao Li, Zhenyu Zhang, Arman Cohan, Hong Yu, Zonghai Yao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical VLMs</span>
<span class="topic-tag">Benchmark Bias</span>
<span class="topic-tag">Shortcut Learning</span>
<span class="topic-tag">Vision-Language Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2609.03261</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03261">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: it is a vision-language evaluation paper that audits shortcut cues in medical multimodal reasoning, though it is more about benchmark analysis than a new foundation model.</p>
        <p class="abstract">A benchmark score credits final answers, but not the route by which an item can be answered. In medical multimodal multiple-choice questions (MCQs), this distinction matters because a correct answer can be supported by the intended image finding or by benchmark-preserved cues in the wording of answers, non-visual clinical text, visible image text, artificial annotations, or device/context artifacts. We call the resulting score-level overinterpretation reasoning inflation. Here, a route is an observable input path that can support answer selection, not a claim about the model&#x27;s hidden cognition. Across six medical multimodal MCQ datasets, we separate candidate cues from behavioral evidence through prompt- and image-side audits, modality ablations, and matched repairs that preserve the medical target and answer key. In a 13-configuration open-model panel, full-input accuracy is 62.63%, while text-only and options-only settings achieve 53.96% and 29.71%, respectively. Removing length-gap, absolute/conspicuous, and spatial/prepositional cues lowers accuracy by 6.58, 3.50, and 4.77 percentage points. We also construct MedQA-MM, a 1,000-item shortcut-mitigated subset, where text-only and options-only accuracy fall to 5.21% and 12.33%. This does not imply that models never use images; it shows that medical image-reasoning claims require route-level evidence.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">RGB-D Salient Object Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>When Depth Hurts: Reliability-Aware Geometry Distillation for Depth-Free RGB-D Salient Object Detection</strong>
          <small>Xuehao Wang, Jiaxin Hua, Runmei Li, Zhenyu Wu, Chenglizhao Chen, Ke Gu, Aimin Hao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">RGB-D Salient Object Detection</span>
<span class="topic-tag">Knowledge Distillation</span>
<span class="topic-tag">Reliability Estimation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2609.03378</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03378">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to the listed criteria; it is a modality-reliability method for RGB-D salient object detection using depth distillation.</p>
        <p class="abstract">Depth can resolve appearance ambiguity in RGB-D salient object detection (SOD), yet sensor depth is not uniformly reliable. Missing regions, blurred boundaries, and structural artifacts can propagate through multimodal fusion and make an RGB-D detector less accurate than its RGB-only counterpart. Existing quality-aware approaches regulate observed depth but remain dependent on the same potentially defective modality. We propose \method, a reliability-aware geometry distillation framework developed for RGB-D SOD benchmarks without using dataset-provided depth during training or inference. A frozen Depth Anything V2 model serves only as a training-time teacher, transferring dense relative geometry, hierarchical spatial attention, and boundary structure to a compact edge-aware geometry branch. Pooled bidirectional interaction aligns geometry with appearance, and a pixel-wise reliability estimator selectively injects geometry that is compatible with the current RGB representation. The teacher is removed after training, leaving an RGB-only inference network. Trained on 2,985 RGB-mask pairs, \method{} achieves the best or tied-best result in 26 of 36 metric-dataset comparisons against ten recent RGB-D SOD methods, including a 13.4\% relative MAE reduction on ReDWeb-S. When retrained on DUTS-TR, it also improves the strongest prior $F$-measure by 4.2\% on PASCAL-S, showing that the distilled geometry transfers beyond a particular sensor or dataset domain. Code will be released upon publication.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>4 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">LLM Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Speak for Me: Giving LLMs the Situational Awareness to Participate in a Meeting</strong>
          <small>Muneeb Khan, Frederic Kirstein, Terry Ruas, Bela Gipp</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LLM Agents</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Situational Awareness</span>
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
          <span>Paper 9 / arXiv:2609.03923</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03923">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: introduces a new benchmark/protocol and method for online meeting delegation with LLM agents, emphasizing situational awareness and action timing.</p>
        <p class="abstract">In online meeting delegation, LLM agents fail to recognize when to speak. With no structured way to track stances, coverage, and floor, they miss the moments where they should contribute. Prompt-only delegates stay silent on 51.4% of the absent participant&#x27;s talking opportunities on the AMI corpus. We present CAPA (Collaborative Agent Predictive Architecture), an architecture for online meeting delegation. A Perceiver updates the meeting state from each observed turn. A Predictor forecasts how the conversation will continue. A Controller decides whether to speak and which proposition to surface. A Generator phrases the chosen contribution in the participant&#x27;s style. Two judges score the forecast and the action against the next observed turn. A Recalibrator updates the meeting state from those verdicts for future decisions. To evaluate online delegation, we introduce an episode-level protocol that scores whether, when, and what a delegate contributes around the participant&#x27;s actual idea units. The protocol&#x27;s schema-constrained LLM judges align with human annotations at Cohen&#x27;s kappa = 0.71. On 137 AMI meetings, CAPA reduces the silence rate from 51.4% to 2.5%, doubles credited recovery (26.1 --&gt; 52.2), and keeps hallucination at 0.6%. The failure mode shifts from omission to selection, with each residual near-miss attributable to a specific module of the architecture. Mechanism ablations identify the meeting state as the lever that closes the recognition gap, where raw-context scaling alone does not.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Agentic VLMs</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>Making Every Tool Call Count: Necessary Tool-Evidence Path Rewards for Agentic Vision-Language Models</strong>
          <small>Xingming Long, Yu Liu, Zhiwei Yang, Hanqi Feng, Shaojie Zhang, Barnabas Poczos, Chao Jiang, Zhenbo Luo, Lei Jiang, Pei Fu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agentic VLMs</span>
<span class="topic-tag">Tool Use</span>
<span class="topic-tag">Visual Question Answering</span>
<span class="topic-tag">Reward Design</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2609.03493</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03493">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 moderately: it is about agentic vision-language models with structured tool use and evidence-path supervision, which is directly relevant to building stronger VLLM-based agents.</p>
        <p class="abstract">Modern vision-language models (VLMs) can directly answer many image-grounded questions, yet they often struggle with complex queries requiring fine-grained visual details or external knowledge. To acquire this missing evidence, agentic VLMs invoke tools such as image cropping, image search, and text search. However, existing training paradigms primarily evaluate tool-use based on final answer correctness, leaving evidence acquisition and utilization insufficiently supervised. This leads to two critical shortcomings: (i) models frequently issue redundant or off-target tool calls that fail to gather necessary evidence, and (ii) even when appropriate tools are called, models often fail to extract the necessary information from the resulting observations. To address these limitations, we introduce the NTEP (Necessary Tool-Evidence Path), a novel annotation scheme that explicitly specifies the essential external evidence and corresponding tool calls for each query. Building upon this, we propose NTEP-R (NTEP Reward), a supervision mechanism ensuring that each tool invocation strictly advances the reasoning process toward the final solution. Specifically, our approach rewards the agent for aligning its pre-call intent with a necessary evidence-seeking goal, and for ensuring the information summarized from the post-call observation aligns with the necessary evidence. Furthermore, we introduce a non-repeated-goal regularizer to penalize redundant calls that revisit satisfied NTEP goals. Extensive evaluations on seven image-grounded benchmarks demonstrate that our 8B-parameter instantiation, NTEP-8B, significantly improves both search-oriented accuracy and tool-use efficiency within a unified three-tool framework. These results highlight the critical value of fine-grained tool-evidence path supervision for training robust agentic VLMs.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">GUI Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents</strong>
          <small>Zhaoyuan Huang, Tianjie Ju, Pengzhou Cheng, Zheng Wu, Yansi Li, Chuanbiao Song, Jun Lan, Huijia Zhu, Weiqiang Wang, Zhuosheng Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">GUI Agents</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Agent Safety</span>
<span class="topic-tag">Multimodal Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2609.03438</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.03438">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is a new embodied/GUI agent benchmark and method focused on conflict-aware termination, a novel angle that prior GUI-agent work often ignores.</p>
        <p class="abstract">Graphical user interface (GUI) agents are increasingly used to execute natural-language instructions on user interfaces, yet real users may issue infeasible instructions due to benign mistakes. A reliable agent should not only know how to act, but also when not to act. In this work, we introduce CONFLICTGUI, a benchmark covering instruction-internal conflicts and instruction-GUI context conflicts to study conflict-aware termination. Our evaluation reveals severe execution-biased overcompliance: agents that perform well on feasible tasks often continue to execute blindly under conflicting instructions. To mitigate this behavior, we propose CONFLICTGUARD, an inference-time framework that aligns an agent&#x27;s feasibility awareness with its action generation. CONFLICTGUARD contains two coupled components: a feasibility verification protocol that guides the agent to assess instruction logic and GUI-side evidence before acting, and a conditional action modulation mechanism that steers agents from over-compliant execution into termination-oriented behavior. Experiments across five widely-used agents demonstrate that CONFLICTGUARD improves average conflict task success rate significantly, while preserving normal GUI-task performance. These results validate that a lightweight inference-time intervention can substantially boost GUI Agent&#x27;s competence to identify inappropriate execution scenarios and refrain from unnecessary actions.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Test-Time Adaptation</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>Efficient Test-Time Adaptation through Human-AI Interaction</strong>
          <small>Zora Zhiruo Wang, Apurva Gandhi, Rulin Shao, Aspen Chen, Jonas Mueller, Zhiqi Liang, Jett Chen, Michael Ryan, Qianou Ma, Luxi He, Zhoujun Cheng, Andre He, Seungone Kim, Jiayi Geng, Mingqian Zheng, Weiwei Sun, Zheyuan Zhang, Xinran Zhao, Yike Wang, Abe Hou, Liwei Jiang, Pang Wei Koh, Diyi Yang, Graham Neubig, Daniel Fried</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Test-Time Adaptation</span>
<span class="topic-tag">Human-AI Interaction</span>
<span class="topic-tag">Personalized Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2609.04141</span>
          <a class="paper-action" href="https://arxiv.org/abs/2609.04141">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; it is test-time adaptation via human-AI interaction for writing and visual creation, not specifically vision foundation models or embodied AI.</p>
        <p class="abstract">AI agents are trained on population-scale data to encode broad capabilities spanning those of many practitioners. Yet the artifacts they produce rarely meet the personal bar professionals need to stake their reputation on. On realistic, open-ended tasks where success criteria are heterogeneous and insufficiently documented, individual expertise lives precisely in the elevation and departure from the average. In practice, iterative human-agent interaction surfaces criteria that users cannot fully specify up front, yet apply repeatedly across tasks. We argue this cross-session interaction data is a rich, underused signal for closing the gap to individual expertise. In this work, we propose test-time adaptation through human-agent interaction (TAHI), which integrates these signals into agent context and weights, and crystallizes each user&#x27;s training and evaluation criteria via an evolving rubric module. We adapt agents to 30 individuals in two high-utility domains, writing and visual creation, on a total of 600 tasks. Our agents improve solo task success by 4.5-20.9% within only tens of tasks. Meanwhile, our evolving rubric module serves as a scalable annotation tool, creating evaluation rubrics that catch 16.0-22.3% more failures than those from LMs or humans alone. While agents are adapted towards individuals, we show these personalized agents also produce improvements in success of up to 8.8% that generalize across users.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
