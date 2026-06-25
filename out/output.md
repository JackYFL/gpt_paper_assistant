

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
      <p class="eyebrow">Daily ArXiv / June 25, 2026</p>
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
      <strong>13</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.70rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="10 mentions">action</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">adversarial</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">annotation</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="6 mentions">anomaly</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">content</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="6 mentions">detection</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="9 mentions">detector</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">end-to-end</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="9 mentions">error</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="6 mentions">foundation</span><span class="cloud-word" style="font-size:1.81rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="11 mentions">generation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">interaction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">interactive</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="8 mentions">knowledge</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">language</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">latency</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">logical</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">mllm</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">multi-modal</span><span class="cloud-word" style="font-size:2.03rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 62%, var(--accent))" title="13 mentions">multimodal</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="6 mentions">multiple</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="9 mentions">normal</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">pair</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">physical</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="9 mentions">pipeline</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="6 mentions">pqsg</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">progress</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">proxy</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">question</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">reasoning</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="6 mentions">reward</span><span class="cloud-word" style="font-size:1.70rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="10 mentions">safety</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">separate</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">sequence</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">ssmnbench</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">structural</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="6 mentions">supervision</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">support</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">surgatla</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="9 mentions">surgical</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="6 mentions">token</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">try-on</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="21 mentions">video</span><span class="cloud-word" style="font-size:1.70rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="10 mentions">visual</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="5 mentions">wan-streamer</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="97 mentions">action</span><span class="cloud-word" style="font-size:2.23rem;opacity:0.86;color:color-mix(in srgb, var(--accent-2) 72%, var(--accent))" title="278 mentions">agent</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="78 mentions">alignment</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="73 mentions">architecture</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="91 mentions">attention</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="72 mentions">consistency</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="70 mentions">control</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="88 mentions">detection</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="82 mentions">diffusion</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="91 mentions">domain</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="70 mentions">driving</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="113 mentions">dynamic</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="157 mentions">evidence</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="84 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="77 mentions">foundation</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="76 mentions">frame</span><span class="cloud-word" style="font-size:1.87rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="212 mentions">generation</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="78 mentions">geometry</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="102 mentions">inference</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="105 mentions">interaction</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="90 mentions">knowledge</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="167 mentions">language</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">latent</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="90 mentions">mechanism</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="159 mentions">memory</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="85 mentions">mllm</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="84 mentions">motion</span><span class="cloud-word" style="font-size:1.76rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="193 mentions">multimodal</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="84 mentions">multiple</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="134 mentions">object</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="84 mentions">optimization</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="77 mentions">paradigm</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="88 mentions">pipeline</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">point</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="82 mentions">policy</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="69 mentions">prompt</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">question</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="80 mentions">real-world</span><span class="cloud-word" style="font-size:2.58rem;opacity:0.95;color:color-mix(in srgb, var(--accent-2) 90%, var(--accent))" title="352 mentions">reasoning</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="78 mentions">retrieval</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="78 mentions">reward</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="156 mentions">scene</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="73 mentions">search</span><span class="cloud-word" style="font-size:1.64rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="174 mentions">semantic</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="97 mentions">skill</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">space</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="145 mentions">spatial</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="78 mentions">structure</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="82 mentions">supervision</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="89 mentions">target</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="127 mentions">temporal</span><span class="cloud-word" style="font-size:1.66rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="177 mentions">token</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="108 mentions">trajectory</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="112 mentions">understanding</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="76 mentions">unified</span><span class="cloud-word" style="font-size:2.42rem;opacity:0.91;color:color-mix(in srgb, var(--accent-2) 82%, var(--accent))" title="316 mentions">video</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="77 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="395 mentions">visual</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="70 mentions">world</span></div>
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
      <summary class="topic-heading">Multimodal Foundation Model</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models</strong>
          <small>Lianghua Huang, Zhifan Wu, Wei Wang, Yupeng Shi, Mengyang Feng, Junjie He, Chenwei Xie, Yu Liu, Jingren Zhou, Ang Wang, Bang Zhang, Baole Ai, Chen Liang, Cheng Yu, Chongyang Zhong, Jinwei Qi, Kai Zhu, Pandeng Li, Peng Zhang, Wenyuan Zhang, Xinhua Cheng, Yitong Huang, Yun Zheng, Zoubin Bi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Foundation Model</span>
<span class="topic-tag">Real-Time Interaction</span>
<span class="topic-tag">Audio-Visual Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.GR</span>
<span class="category-tag">cs.SD</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2606.25041</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25041">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: a new end-to-end interactive foundation model that unifies audio, video, and text for real-time streaming interaction.</p>
        <p class="abstract">We present Wan-Streamer, a native-streaming, end-to-end interactive foundation model designed from the ground up for real-time, low-latency, full-duplex audio-visual interaction. Wan-Streamer seamlessly models language, audio, and video as both input and output within a single Transformer, where the sequence is represented as interleaved visual, audio, and text input tokens together with visual, audio, and text output tokens, coordinated by block-causal attention for incremental streaming. Unlike cascaded interactive systems that rely on separate VAD, ASR, language, TTS, audio-driven animation, or video-generation modules, Wan-Streamer does not rely on external language, speech, avatar, or video-generation modules: perception, reasoning, generation, response timing, turn management, and cross-modal synchronization are learned jointly within one unified model, reducing pipeline latency and error accumulation. To support natural audio-visual responsiveness, we redesign the entire stack around streamability, including causal encoders, causal decoders, block-causal attention, and low-latency multimodal token scheduling, enabling streaming units as short as 160 ms at 25 fps. Wan-Streamer achieves approximately 200 ms model-side response latency and approximately 550 ms total interaction latency when combined with 350 ms bidirectional network latency, supporting sub-second duplex audio-visual communication. These results position Wan-Streamer as a unified, end-to-end, multimodal interactive foundation model for low-latency streaming interaction.</p>
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
          <strong>TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy</strong>
          <small>Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Video Generation</span>
<span class="topic-tag">3D/4D Representation</span>
<span class="topic-tag">Virtual Try-On</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2606.26092</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.26092">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it proposes a new embodied/video generation benchmark and method for camera-controllable video virtual try-on with a 4D proxy.</p>
        <p class="abstract">While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time&#x27;&#x27; effects, and $360$-degree orbital viewing.</p>
      </div>
    </details>


    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>ESTANet: Efficient Online Error Detection in Procedural Videos via Prediction Inconsistency</strong>
          <small>Shih-Po Lee, Reza Ghoddoosian, Faizan Siddiqui, Enna Sachdeva, Behzad Dariush</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Procedural Video Understanding</span>
<span class="topic-tag">Online Error Detection</span>
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
          <span>Paper 11 / arXiv:2606.25317</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25317">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately: an embodied/procedural-video method for online error detection in action sequences, but it is not a new benchmark or simulator paper.</p>
        <p class="abstract">An efficient and accurate system for detecting errors in procedural tasks is crucial for supporting human needs in daily life, as it can provide instant notifications and guide people to correct mistakes. In this work, we study real-time online error detection in procedural videos from a simple but overlooked perspective: the prediction behavior of action detectors themselves. Instead of designing complex architectures or specialized supervision, we observe that action detectors naturally exhibit different prediction characteristics depending on their sensitivity to input dynamics and temporal context. We therefore propose ESTANet (Error-Sensitive and Temporally-vArying Network), a lightweight framework that detects errors by exploiting inconsistencies among action predictions produced by a small set of action detectors. We construct standard and error-sensitive action detectors that behave similarly on correct executions but respond differently when errors occur. Meanwhile, detectors operating with different temporal contexts further amplify prediction inconsistencies when the procedure deviates from the intended sequence. During inference, we detect errors by aggregating mismatches between standard and error-sensitive predictions through majority voting to flag frames that contain errors. Extensive experiments on EgoPER, Assembly-101-O, and EPIC-Tent-O demonstrate that ESTANet achieves state-of-the-art performance in online error detection while maintaining real-time efficiency with a lightweight architecture. Our results highlight that leveraging the intrinsic properties of action detectors can yield a powerful and practical solution for online error detection without increasing architectural design complexity.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>SSMNBench: Diagnosing Image-based Cross-View Human-Object Understanding via Single-View Sufficiency and Multi-View Necessity</strong>
          <small>Tianchen Guo, Chen Liu, Ling Chen, Xin Yu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM Benchmark</span>
<span class="topic-tag">Cross-View Reasoning</span>
<span class="topic-tag">Human-Object Understanding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2606.25634</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25634">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: a new benchmark for cross-view human-object understanding in MLLMs, with a diagnostic angle on single-view sufficiency vs multi-view necessity.</p>
        <p class="abstract">Multimodal Large Language Models (MLLMs) have shown remarkable progress in single-image perception, yet their ability to reason about complex cross-view human-centric scenes remains largely unverified. Current multi-view benchmarks evaluate models using a fixed &quot;bag of frames&quot; and thus conflate a model&#x27;s robustness to visual distraction with its genuine ability to fuse fragmented cross-view evidence. To address this issue, we introduce SSMNBench, a diagnostic benchmark comprising 3,300 curated QA pairs for cross-view human and human-object understanding. SSMNBench uniquely categorizes tasks into Single-View Sufficiency (SVS) and Multi-View Necessity (MVN). By systematically perturbing view availability across 17 state-of-the-art MLLMs, critical limitations are revealed: models suffer from severe &quot;distraction degradation&quot; when presented with redundant views (SVS), and fail to integrate fragmented geometric evidence across cameras (MVN). Our evaluations demonstrate that modern MLLMs rely on multiple single-image semantic averaging and view preference rather than genuine cross-view synthesis. By exposing these fundamental vulnerabilities, SSMNBench provides a rigorous diagnostic framework to drive the advancement of future cross-view-aware multimodal architectures. The code is available at: $ \href{https://github.com/gtc-gh/SSMNBench}{\text{SSMNBench}} $</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video-Language Dataset</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>SurgAtlas: A Large-Scale Surgical Video-Language Dataset with 2,391 Hours of Open and Minimally Invasive Surgery</strong>
          <small>Filippos Bellos, Andre S. Gala-Garza, Miaowei Wang, Alyssa M. Hardin, Ahmad M. Hider, Yayuan Li, Jing Bi, Susan Liang, Chenliang Xu, Donald S. Likosky, Jason J. Corso</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video-Language Dataset</span>
<span class="topic-tag">Medical Foundation Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Surgical AI</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2606.25905</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25905">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 well: it builds a large-scale surgical video-language dataset and benchmarks, supporting foundation-model style multimodal learning in a new domain.</p>
        <p class="abstract">We introduce SurgAtlas, the largest surgical video-language dataset to date, comprising 15,291 videos (2,391 hours) spanning 18 surgical specialties and over 5,000 procedure types, sourced entirely from publicly available YouTube content. SurgAtlas is also the first surgical video-language dataset to include open surgery at scale, with 6,182 open procedure videos alongside over 9,000 minimally invasive recordings, and the first to establish standardized benchmarks for open-surgery video understanding. We additionally provide an expert-validated subset with verified visual question-answer pairs across diverse open and minimally invasive procedures, serving as a clinically grounded benchmark for surgical reasoning. Compared with existing surgical video-language datasets, SurgAtlas provides one of the most diverse annotation schemas, combining segment-level captions, step- and phase-level descriptions, video-level surgical descriptions, and reasoning-oriented question-answer pairs organized within a hierarchical taxonomy. These annotations are constructed through an automated multi-tier pipeline with LLM-based enrichment and a staged VQA generation framework with explicit groundedness verification. The scale and diversity of SurgAtlas enable training surgical foundation models with broad procedural coverage: we finetune Qwen3-VL-8B through a two-stage captioning-then-instruction pipeline and achieve competitive or state-of-the-art results on multiple established surgical benchmarks, including phase recognition, triplet detection, and reasoning question answering. More broadly, SurgAtlas provides a large native public video corpus that can support future large-scale pretraining of multimodal surgical AI systems and contribute to the development of next-generation foundation models for surgery.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal LLM</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Yuvion VL: A Multimodal Foundation Model for Adversarial Content and AI Safety</strong>
          <small>Shikai Qiu, Xiaowen Xu, Benlei Cui, Ting Ma, Xiufeng Huang, Wenjing Jiang, Shaoxuan He, Haolei Xu, Chunyang Chai, Yujian Li, Yiliang Zhang, Guanghui Wang, Ziheng Wang, Ziwen Xu, Zhaoyu Fan, Jinhao Chen, Ruijie Jian, Hongxing Li, Chuxi Xiao, Xinyue Chen, Wenxuan Liu, Libin Dong, Yupeng Cao, Xiaoqian Xia, Jing Wang, Zhe Jiang, Zhenan Ye, Guang Yang, Bin Liu, Wei Peng, Ziqiang Zhu, Meihui Lian, Kaiwen Lv Kacuila, Haidong Ding, Dongjie Zhang, Yangfan Zhou, Bingyu Zhu, Yan Wang, Hai Zhao, Xuan Jin, Wei Zhao, Pengfei Sun, Huiming Zhang, Wei Wang, Xipeng Cao, Bin Li, Chengwen Yao, Meng Huang, Xianfeng Li, Bin Tang, Chao Liu, Hui Xue, Longtao Huang, Haiwen Hong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal LLM</span>
<span class="topic-tag">AI Safety</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Adversarial Robustness</span>
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
          <span>Paper 5 / arXiv:2606.25034</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25034">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 well: it presents a new multimodal foundation model (Yuvion VL) and a benchmark for adversarial content and AI safety.</p>
        <p class="abstract">General-purpose models often struggle to reliably identify and understand real-world multimodal risks, largely due to the inherent multimodal adversarial nature of content and AI safety. We present Yuvion VL, a family of multimodal large language models purpose-built for content and AI safety, with both instruction-tuned and reasoning-oriented variants. Yuvion VL addresses this gap by treating safety as an inherently adversarial and multimodal problem and designing the entire pipeline around adversarial robustness. For data construction, we develop an automated pipeline integrating adversarial-aware data synthesis with multi-stage quality control, producing large-scale, high-quality multimodal samples augmented with domain knowledge and reasoning annotations. For training, we adopt a three-stage pipeline that includes continued pretraining for risk-concept cross-modal alignment, instruct post-training for production-grade safety tasks, and reasoning post-training for enhanced interpretability and performance in complex tasks. We further introduce Confuse-then-Contrast Fine-Tuning, a contrastive framework that mines model-specific confusions and constructs multi-image contrastive groups to enforce explicit discrimination of fine-grained visual-semantic elements, enabling the model to distinguish between visually similar cases with different safety implications in adversarial safety tasks. To support rigorous evaluation, we further introduce Yuvion VL RiskEval (YVRE), a collection of benchmarks covering diverse open and internal evaluations, with a focus on content and AI safety, adversarial robustness, and real-world capability requirements. Experiments show that Yuvion VL-32B achieves industry-leading safety performance, surpassing comparably sized open-source models and best closed-source commercial models, while maintaining comparable general capabilities.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Visual Anomaly Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Hypergraph Normal World Models for Logical Visual Anomaly Detection</strong>
          <small>Weizhi Nie, Zibo Xu, Weijie Wang, Yuting Su</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Visual Anomaly Detection</span>
<span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Hypergraphs</span>
<span class="topic-tag">Foundation Vision Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2606.25368</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25368">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 well: it introduces a new method for logical visual anomaly detection that explicitly models spatial relations and hypergraph structure.</p>
        <p class="abstract">Visual anomaly detection is often deployed with only normal training images. Most one-class detectors map test patches or features to a normal reference distribution. This works well for local structural defects. Logical anomalies are different. Each visible part may look normal, while the whole image violates a normal count, co-occurrence, or spatial relation. This paper studies whether a model can learn such a category-specific normal world from nominal images alone. We propose the Hypergraph Normal World Model, a normal-only detector that distills frozen DINOv2 patch tokens into patch, relation, and hypergraph statistics. It builds spatial hyperedges over token groups. It then scores each test image with an information quotient that separates local, relational, hyperedge, and hyperedge-relation evidence. On the available MVTec LOCO breakfast-box validation data, the full hypergraph model improves logical anomaly AUROC from 0.8434 for DINOv2 patch-kNN to 0.9279. It also improves over the non-hypergraph variant, from 0.9013 to 0.9279. Few-shot experiments show that the model remains effective with very limited normal images. We also test whether the score reflects normal-world knowledge rather than a shallow mapping. t-SNE separates logical anomalies in the learned energy space. Relation counterfactuals increase the information quotient by 83.13 on average. Random hypergraphs reduce logical AUROC, and hyperedge attribution is much larger on logical anomalies. Qualitative examples show that high scores are driven by relation-bearing terms. These results suggest that logical visual anomaly detection should model normal relations, not only normal local patches.</p>
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
          <strong>Physics Question Scene Graph: Fine-grained Evaluation of Physical Plausibility in Text-to-Video Generation</strong>
          <small>Atin Pothiraj, Jaemin Cho, Yue Zhang, Elias Stengel-Eskin, Mohit Bansal</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Physical Reasoning</span>
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
          <span>Paper 7 / arXiv:2606.25306</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25306">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it builds a fine-grained evaluation method for physical plausibility in text-to-video generation using a VLM-guided question graph.</p>
        <p class="abstract">Video generation models are increasingly capable of producing realistic videos, but they still struggle to generate videos that follow basic physical laws. Compounding this is a lack of reliable granular evaluation methods for localizing and specifying physical law violations in videos. We address this by introducing Physics Question Scene Graph (PQSG), a hierarchical question-based evaluation pipeline. PQSG evaluates generated videos by checking their faithfulness to a prompt across objects, actions, and adherence to physical laws using a graph-based hierarchy of questions generated by a vision-language model (VLM), guided by high-quality in-context examples. By representing questions as a graph, PQSG introduces logical dependencies within questions, ensuring that each query is contextually valid. Moreover, PQSG provides granular assessments of which qualities of the video violate physical plausibility constraints. We validate PQSG by creating FinePhyEval, a dataset with physics-based prompts and corresponding generated videos from diverse state-of-the-art video generation models (Sora 2, Veo 3, and Wan 2.1), with each video annotated across multiple categories by humans. Using FinePhyEval, we measure the correlation between PQSG&#x27;s fine-grained scores and human judgments, showing higher overall correlations than prior work. We also find that PQSG ranks closed-source models higher than Wan 2.1 on physical realism. Lastly, we show that the annotations we provide in FinePhyEval can also be used for subtask evaluation: we benchmark two strong VLMs on generating and answering questions, finding that while models can create human-like questions, they still fall short of human performance in answering them.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Structuring Sparsity: Block-Sparse Featurizers Capture Visual Concept Manifolds</strong>
          <small>Thomas Fel, Matthew Kowal, Mozes Jacobs, Dron Hazra, Usha Bhalla, Lee Sharkey, Lucius Bushnaq, Satchel Grant, Tal Haklay, Thomas Icard, Can Rager, Michael Pearce, Daniel Wurgaft, Aiden Swann, Fenil Doshi, Siddharth Boppana, Curt Tigges, Nick Cammarata, Thomas Serre, Vasudev Shyam, Owen Lewis, Thomas McGrath, Jack Merullo, Ekdeep Singh Lubana, Atticus Geiger</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Interpretability</span>
<span class="topic-tag">Generative Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2606.25234</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25234">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: it studies vision foundation model representations and shows interpretability/control applications in diffusion models, but it is not an application-centric VFM paper.</p>
        <p class="abstract">What is the geometry of a visual percept? The most widely used protocols for decomposing neural network representations into interpretable parts treat concepts as isolated directions, yet recent work shows that concepts are often realized as geometric structures in low dimensional regions of activation space. We turn to the literature of Structured sparsity to close this gap, and show that block sparsity, which groups directions into blocks, is the prior matched to a generative model in which a representation is a sparse sum of low-dimensional manifolds: the modern, learned form of a classical idea in visual neuroscience, where a visual feature is carried by a coordinated group of neurons rather than a single tuned one. We implement three variants of block-sparse featurizers (BSFs) and, through a minimum-description-length analysis, show that all three describe activations more compactly than direction-based featurizers, with the recovered concepts typically two- to four-dimensional. We then use BSFs to (i) recontextualize prior work, showing that curve detectors in InceptionV1 actually read from a single continuous curve manifold, (ii) discover novel manifolds including shadows and lighting in DINOv3, and (iii) support interpretable control of image generation in diffusion models (SDXL) via manifold steering.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM Adaptation</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Curvature-Guided Mixing for MLLM Adaptation</strong>
          <small>Jinglong Yang, Jiaxuan He, Wenjian Huang, Zhan Zhuang, Jianguo Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM Adaptation</span>
<span class="topic-tag">Model Merging</span>
<span class="topic-tag">Curvature/Hessian Methods</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2606.24963</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24963">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: adaptation/merging method for MLLMs, with a mathematically grounded curvature-based mixing rule.</p>
        <p class="abstract">Fine-tuning Multimodal Large Language Models (MLLMs) on specialized tasks often leads to catastrophic forgetting of their general capabilities. Existing model merging methods to combat this are often heuristic or use sub-optimal objectives. We propose CurvatureGuided Mixing (CGM), a theoretically grounded framework that merges pre-trained and fine-tuned models. CGM formulates a joint optimization objective and uses a second-order (Hessian) approximation of the loss landscapes to analytically derive an optimal, closed-form &quot;soft mixing&quot; ratio. This ratio intelligently blends parameters based on their relative task-specific curvatures. We also introduce CGM$\dagger$, a robust &quot;hard mixing&quot; variant that performs sparse parameter selection guided by a novel, curvature-aware score. Experiments on LLaVA-1.5 and Qwen2.5VL across multiple downstream tasks show that CGM and CGM$\dagger$ consistently improve the trade-off between task specialization and general knowledge retention over existing methods. Code is available at github.com/zzsyjl/CGM-ECCV-2026.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical VLM</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>MRI2Rep: Autoregressive Structured Report Generation for 3D Liver MRI</strong>
          <small>Xinran Li, Junlin Yang, Annabella Shewarega, Zongwei Zhou, Julius Chapiro, James S. Duncan, Lawrence H. Staib</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical VLM</span>
<span class="topic-tag">Report Generation</span>
<span class="topic-tag">3D Medical Imaging</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2606.25279</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25279">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 only weakly: medical vision-language report generation for 3D MRI, but this is a specialized application rather than a foundation-model advance.</p>
        <p class="abstract">Manual reporting of 3D MRI studies is time-consuming, yet end-to-end structured report generation for 3D liver MRI remains underexplored due to volumetric complexity and scarce paired data. We propose MRI2Rep, an autoregressive framework for liver MRI report generation. From 3,929 real-world MRI-report pairs acquired over a 10-year single-institution cohort, a Report-to-Label Canonicalization (RLC) module converts free-text reports into structured, closed-vocabulary diagnostic sequences without lesion-level annotations. On a held-out test set, MRI2Rep achieves 76.0% case-level sensitivity, 29.4% lesion-level F1, compared with no more than 8.3% for adapted medical vision-language baselines, and 82.4% liver-level accuracy. In a blinded reader study, two radiologists rated 75% and 70% of AI-generated reports as clinically acceptable, compared with 95% and 100% for original reports. Our automated LLM-based judge, LLM-Eval, rated 61.8% of AI-generated reports as acceptable, applying a stricter standard and supporting its use as a conservative proxy. To our knowledge, this is the first end-to-end LI-RADS-structured reporting system for 3D liver MRI.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Semantic Segmentation</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Heterogeneous and Adept Snapshot Distillation for 3D Semantic Segmentation</strong>
          <small>Xiaopei Wu, Yuenan Hou, Junkai Xu, Wenxiao Wang, Binbin Lin, Yu Li, Ping Li, Haifeng Liu, Deng Cai, Wanli Ouyang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Semantic Segmentation</span>
<span class="topic-tag">Knowledge Distillation</span>
<span class="topic-tag">Multi-Modal Fusion</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2606.25278</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.25278">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 only indirectly: new knowledge-distillation method for 3D semantic segmentation, but it is not about spatial intelligence for embodied agents.</p>
        <p class="abstract">Multi-modal fusion and multi-model ensembling are prevalent in enhancing the performance of 3D semantic segmentation. Despite the impressive performance, these methods either rely on auxiliary input signals or suffer from costly computational expense. To efficaciously enhance the segmentation performance without introducing intolerable costs, we propose to transfer the rich knowledge from the multi-modal model (i.e., point clouds and images) and multiple model experts to the point-cloudbased network through knowledge distillation. Specifically, we present Information-oriented Heterogeneous Distillation (IHD) to help the uni-modal model absorb the complementary knowledge from the multi-modal teacher. We design the Information-Oriented Filtering (IOF) strategy to select informative images from the continuous image sequence for multi-modal fusion. This practice can boost the performance of the multi-modal teacher, thus benefiting the learning of the student. Besides, as opposed to vanilla model ensembling that requires the separate training of each expert, we propose Adept Snapshot Distillation (ASD). ASD treats the freely available model snapshots generated during the training phase as multiple experts, which significantly reduces the training cost for model ensembling. For each expert teacher, it only provides supervision to the student in the class where it is adept. The resulting Heterogeneous and Adept Snapshot Knowledge Distillation, dubbed HAS-KD, attains state-of-the-art results on ScanNetV2 and S3DIS datasets. HAS-KD can be seamlessly integrated into contemporary 3D segmentation algorithms and bring considerable gains without introducing extra inference burdens. The code will be made publicly available upon publication.</p>
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

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning</strong>
          <small>Xirui Li, Zhe Liu, Xiaoqing Ye, Wenhua Han, Yifeng Pan, Junyu Han, Hengshuang Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Generative Planning</span>
<span class="topic-tag">Reward Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2606.24231</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24231">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately: it is an embodied driving-planning method for simulation-based reward-conditioned action generation, though not a new benchmark.</p>
        <p class="abstract">Multimodal driving planning faces a long-standing tension between two paradigms: scoring-based methods benefit from dense reward supervision but are confined to a fixed action vocabulary, while anchor-based methods generate proposals dynamically yet suffer from sparse supervision constrained to a single ground-truth trajectory. In this work, we propose FlowR2A, which resolves this tension by reframing simulation-based rewards from discriminative targets into generative conditions. By learning the reward-conditioned action distribution from dense trajectory-reward pairs with a flow-matching decoder, FlowR2A unifies the dense supervision of scoring-based methods with the proposal generation of anchor-based methods in a single generative model, forcing the model to internalize the correlation between an action and its outcomes in safety, progress, comfort, and rule compliance. To balance hard safety constraints against soft progress objectives, we introduce fine-grained per-timestep reward conditioning and reward noise augmentation. The generative formulation naturally supports controllable test-time sampling via reward guidance and anchored sampling, producing high-quality proposals. FlowR2A achieves state-of-the-art results on the NAVSIM v1 and v2 benchmarks, with multimodal proposals of substantially higher quality than prior methods.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Personalized Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Navigating User Behavior toward Personalized Multimodal Generation</strong>
          <small>Hengji Zhou, Yufeng Liu, Ye Liu, Yong Xu, Lianghao Xia, Liqiang Nie</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Personalized Generation</span>
<span class="topic-tag">Multimodal Recommendation</span>
<span class="topic-tag">Image/Video Synthesis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2606.24196</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24196">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 only loosely: personalized multimodal generation with instruction synthesis for images/videos, but it is not a vision foundation model paper in the usual sense.</p>
        <p class="abstract">Modern AIGC pipelines deliver high-fidelity images and videos but presuppose a well-formed creation instruction, while end users rarely articulate visual details, leaving generators misaligned with user demand. We study personalized content generation, which turns a user&#x27;s interaction history into an executable instruction for downstream synthesis, and identify two obstacles: behavior must be encoded in a form legible to language reasoning, and the model must acquire instruction-writing skill absent from both pretraining and behavior data. We propose NaviGen, which represents each item with a dual identifier coupling a collaborative code and a textual code as a behavioral substrate and a semantic bridge in one token stream. On this representation, a two-stage SFT+RL pipeline first distills preference reasoning and instruction writing from evolutionarily searched supervision, then aligns generation with user intent through hierarchical and self-consistent rewards. Experiments across product, game, and short-video domains show that NaviGen improves personalized image and video generation, strengthens next-item prediction, and yields more specific, relevant, and visually generatable instructions. Our code is released at: https://github.com/iLearn-Lab/NaviGen.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-05-29.html">
          <span>May 29, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-05-28.html">
          <span>May 28, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-05-27.html">
          <span>May 27, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-05-26.html">
          <span>May 26, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-05-25.html">
          <span>May 25, 2026</span>
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
