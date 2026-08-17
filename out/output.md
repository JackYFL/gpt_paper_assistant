

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
      <p class="eyebrow">Daily ArXiv / August 17, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>16</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>15</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>11.0</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="11 mentions">anomaly</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">architecture</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">asymmetry</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">auxiliary</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">change</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">control</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">cpi-bench</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="9 mentions">detection</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">diffusion</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="8 mentions">domain</span><span class="cloud-word" style="font-size:1.80rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 50%, var(--accent))" title="14 mentions">editing</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">event</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="7 mentions">evidence</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">experience</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">fine-grained</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">generation</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">instance</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">latent</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">localization</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="9 mentions">mask</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">memory</span><span class="cloud-word" style="font-size:1.56rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="11 mentions">mllm</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="8 mentions">multimodal</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">observation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">on-policy</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">original</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">predicted</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">property</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="8 mentions">reasoning</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">reference</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">same</span><span class="cloud-word" style="font-size:2.33rem;opacity:0.89;color:color-mix(in srgb, var(--accent-2) 77%, var(--accent))" title="22 mentions">semantic</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">should</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">source-domain</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">spatial</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">structural</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">structure</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="9 mentions">target</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">teacher</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="9 mentions">token</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="7 mentions">trajectory</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="10 mentions">video</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="30 mentions">visual</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">world</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="5 mentions">zero-shot</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="110 mentions">action</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="202 mentions">agent</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="90 mentions">alignment</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="69 mentions">attention</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">challenging</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="81 mentions">change</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="71 mentions">condition</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="84 mentions">consistency</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="68 mentions">consistently</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">control</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="110 mentions">detection</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="92 mentions">diffusion</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">distribution</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">domain</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="83 mentions">dynamic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="68 mentions">editing</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="69 mentions">environment</span><span class="cloud-word" style="font-size:1.82rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="216 mentions">evidence</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="89 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="75 mentions">foundation</span><span class="cloud-word" style="font-size:1.18rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="111 mentions">frame</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="72 mentions">fusion</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="239 mentions">generation</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="100 mentions">inference</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="129 mentions">interaction</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="135 mentions">language</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="87 mentions">latent</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="130 mentions">memory</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="95 mentions">mllm</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="89 mentions">modality</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="117 mentions">motion</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="202 mentions">multimodal</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="93 mentions">multiple</span><span class="cloud-word" style="font-size:1.45rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="152 mentions">object</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="69 mentions">optimization</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="75 mentions">pipeline</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="89 mentions">point</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">real-world</span><span class="cloud-word" style="font-size:1.67rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="189 mentions">reasoning</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="99 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="85 mentions">region</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="93 mentions">retrieval</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="70 mentions">reward</span><span class="cloud-word" style="font-size:1.28rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="126 mentions">scene</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="239 mentions">semantic</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="88 mentions">space</span><span class="cloud-word" style="font-size:1.27rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 23%, var(--accent))" title="124 mentions">spatial</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">structure</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="81 mentions">supervision</span><span class="cloud-word" style="font-size:1.06rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="96 mentions">support</span><span class="cloud-word" style="font-size:1.39rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="142 mentions">target</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="114 mentions">temporal</span><span class="cloud-word" style="font-size:1.55rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="168 mentions">token</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="95 mentions">trajectory</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="131 mentions">understanding</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="86 mentions">unified</span><span class="cloud-word" style="font-size:2.33rem;opacity:0.89;color:color-mix(in srgb, var(--accent-2) 77%, var(--accent))" title="323 mentions">video</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="84 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="433 mentions">visual</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="77 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>13 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>SSP: An Event-Matched Syn2Sim2Phy Cross-Domain Evaluation Framework for Autonomous Driving VLA Models</strong>
          <small>Haojie Feng, Peizhi Zhang, Xinrui Zhang, Zhuoren Li, Junpeng Huang, Xiurong Wang, Dongxiao Yin, Yuxiang Zhang, Junfan Zhu, Lu Xiong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI Benchmark</span>
<span class="topic-tag">Autonomous Driving VLA</span>
<span class="topic-tag">Cross-Domain Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2608.14024</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14024">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it proposes a new embodied AI evaluation benchmark/framework for autonomous driving VLA models, with an event-matched Syn2Sim2Phy setup that targets a novel cross-domain comparison angle.</p>
        <p class="abstract">Vision-language-action (VLA) models for autonomous driving jointly produce scene interpretation, language-based reasoning, and driving trajectories. Existing evaluations often use independently selected synthetic, simulated, and physical data, so measured performance gaps can be confounded by changes in scenario content rather than genuine domain sensitivity. We propose SSP (Synthetic-Simulation-Physical), an event-matched Syn2Sim2Phy evaluation framework that anchors cross-domain comparison to the same safety-critical interaction. Starting from a synthetic long-tail video, SSP builds a validated event specification that preserves road topology, participant roles, relative motion, conflict evolution, passing order, response constraints, and event phases. Platform-specific realizations are then constructed in CARLA and on a closed proving ground and are evaluated only after transfer audits confirm preservation of mandatory event properties. SSP maps heterogeneous outputs from OpenEMMA, LLaViDA, and Alpamayo-R1 into common semantic slots and a 1 s trajectory window to assess output validity, semantic accuracy, critical-interaction recognition, trajectory quality, and risk response. Across Cut-in and vulnerable-road-user crossing cases, the macro-averaged Integrated VLA Capability Scores are 0.259, 0.291, and 0.325 in the Synthetic, Simulation, and Physical domains, respectively, while the best domain varies by scenario. Alpamayo-R1, OpenEMMA, and LLaViDA obtain scores of 0.405, 0.338, and 0.131. SSP provides a reproducible scene-transfer chain and an evidence-qualified evaluation of VLA behavior without assuming that the Physical domain is universally superior.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">VLM Distillation</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>Self-Supervised Visual On-Policy Distillation</strong>
          <small>Yijiang Li, Yijun Liang, Yunjie Tian, Bingyang Wang, Ke Zhang, Zhenfei Yin, Di Fu, Philip Torr, Nuno Vasconcelos</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">VLM Distillation</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Fine-Grained Vision-Language Reasoning</span>
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
          <span>Paper 2 / arXiv:2608.14144</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14144">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 very closely: it studies self-supervised distillation for a visual large multimodal model and reports strong empirical gains on fine-grained perception benchmarks.</p>
        <p class="abstract">Visual on-policy distillation relies heavily on an informative teacher-student asymmetry, through either a larger, stronger teacher or privileged supervision, such as reference answers or ground-truth regions of interest. This raises a fundamental question: where can informative asymmetry come from when nothing privileged is available? We answer this by inverting where the asymmetry comes from. Rather than adding privileged information to the teacher, we subtract information from the student. This asymmetry creates the same effective learning signal for free as a teacher with access to information unavailable to the student, without ground-truth annotations, rewards, or a separate stronger teacher model. Building on this principle, we introduce Self-Supervised Visual On-Policy Distillation (S$^2$VOPD), a simple yet effective method that constructs on-policy learning signals from asymmetric augmented views. S$^2$VOPD distills the teacher&#x27;s distribution conditioned on the original image on-policy into the student distribution conditioned on a strongly augmented view of the same image. We systematically explore a broad design space of visual augmentations and uncover that (1) asymmetry matters: all four augmentation families improve performance, while symmetric self-distillation degrades it; (2) strength matters: performance peaks at a moderate strength; and (3) the gap must remain task-consistent: augmentations that completely remove the question-relevant evidence can induce large but uninformative discrepancies. Across six fine-grained perception benchmarks, S$^2$VOPD improves Qwen3.5-4B from 70.7% to 77.4%, above all open-source models compared, up to Qwen3-VL at 235B, and surpasses GPT-5.4. While holding training data the same, it recovers 96% of the improvement achieved by methods with privileged information. Website is at https://williamium3000.github.io/s2vopd</p>
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
          <strong>Marionette: Predicting World States, Rendering Geometry, Painting Appearance</strong>
          <small>Zian Meng, Zhen Li, Chuanhao Li, Qiang Li, Kaipeng Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Video Generation</span>
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
          <span>Paper 3 / arXiv:2608.14530</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14530">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it builds an explicit world model for interactive games with articulated characters, focusing on structured state prediction and rendering for embodied settings.</p>
        <p class="abstract">Interactive game world models typically autoregress visual observations directly in pixel or latent space, forcing structured properties such as pose, geometry, and occlusion to be implicitly maintained by the same generative sequence. Over long horizons, errors in these latent world properties accumulate, making consistency and controllability fragile. We explicitly model the evolving world state, delegate exact geometric computation to a fixed, zero-parameter renderer, and leave the neural model to synthesize appearance. We instantiate this idea as Marionette, a world model for interactive games with articulated characters. First, a two-stage autoregressive dynamics model predicts an explicit and interpretable 276-dimensional 3D world state comprising multi-entity articulated skeletons, metric root trajectories, and rotations. Second, a zero-parameter graphics bridge converts the predicted state into pose-control videos, computing world-space geometry and occlusion in closed form. Third, a control-conditioned video-diffusion observation model synthesizes photorealistic RGB observations from the resulting structured controls. Our experiments establish two properties of Marionette. First, the predicted world state is directly controllable. Forcing a mismatched action stream changes root-aligned joint error by 31% across 48 held-out segments. Second, long-horizon behaviour is determined in the state, and can be repaired there. Left free, the two generated characters drift to 21.2 m apart (recorded sessions stay near 5 m) and a third of frames show ground penetration. Two rules imposed on the explicit state, a terrain collider and a separation cap, cut penetration by 66% and keep the pair engaged, with no change to the observation model. Routing appearance through the predicted state costs no fidelity we can detect, at an FVD of 831 against 799 for recorded pose.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Editing</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>InstructVVT: Instruction-Driven Video Virtual Try-On without Auxiliary Spatial Priors</strong>
          <small>Dingbao Shao, Song Wu, Xinyu Chen, Qian Wang, Jiahang Li, Kuai Jiang, Jiang Lin, Yuhang Liu, Ziyu Chen, Duo Li, Jiaxin Hu, Shengrong Gu, Ziheng Tang, Rongrong Liu, Yanlun Peng, Liang Li, Junlan Feng, Lujia Jin, Ting Zhang, Jian Yang, Zili Yi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Editing</span>
<span class="topic-tag">MLLM Conditioning</span>
<span class="topic-tag">Generative Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2608.14070</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14070">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it introduces an MLLM-driven, instruction-based video virtual try-on method and removes the need for auxiliary spatial priors.</p>
        <p class="abstract">Video virtual try-on is a highly constrained editing task requiring the precise replacement of a target person&#x27;s clothing while strictly preserving the original video&#x27;s spatial structure and temporal dynamics. Existing methods heavily rely on auxiliary handcrafted spatial priors (e.g., masks, poses) for editing control. However, these priors are prone to failure in unconstrained real-world videos and often compress rich visual context into incomplete structural signals. Furthermore, standard reconstruction objectives fail to fully capture try-on-specific human preferences. To address these challenges, we propose InstructVVT, an instruction-driven and reference-guided video virtual try-on framework based on a Diffusion Transformer (DiT) that operates without inference-time spatial priors. Our core insight is to recover fine-grained control directly from the input triplet (source video, reference garment, and instruction) via a dual-level reference conditioning scheme. Specifically, an MLLM infers semantic edit tokens for target disambiguation and structural preservation, while a lightweight conditioning pathway explicitly injects fine-grained visual garment details. Finally, we design a try-on-specific reward and utilize the DiffusionNFT algorithm to align the model with human preferences. Extensive experiments on ViViD-S and TripVVT-Bench demonstrate that InstructVVT outperforms state-of-the-art open-source methods in garment fidelity, structural preservation, and temporal consistency, despite requiring fewer inference-time controls.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM Segmentation</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>FIRM: Fine-Grained Intra-Token Representation of Masks for Remote Sensing Reasoning Segmentation</strong>
          <small>Weidong Tang, Kaiyu Li, Yikai Wang, Yanan Wu, Haotian Gan, Shihong Wang, Xiangyong Cao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM Segmentation</span>
<span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Remote Sensing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2608.13980</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.13980">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 3: an MLLM-based reasoning segmentation method with a novel fine-grained spatial mask representation for remote sensing.</p>
        <p class="abstract">Reasoning segmentation requires multimodal large language models (MLLMs) to translate implicit instructions into precise pixel-level masks. MLLMs encode an image as visual tokens, each of which merges a group of image patches. In remote sensing images, small targets, thin structures, and adjacent instances can occupy different parts of the same visual token. Assigning a single binary mask label to such a token loses its internal spatial structure, causing nearby targets to merge and object boundaries to become coarse. To bridge this representational gap, we introduce FIRM, a Fine-grained Intra-token Representation of Masks. For each visual token, FIRM predicts a mask code that specifies an $r\times r$ binary sub-cell pattern rather than a single foreground/background label. Given a target identified by the MLLM, the complete grid of mask codes is predicted in one mask pass. Fixed lookup converts the predicted codes into a discrete sub-cell mask, while marginalizing the code distribution yields a soft structural field. To further recover fine-grained boundaries within each sub-cell, we introduce a lightweight continuous renderer that refines this field using pre-merge visual features and image details. Across five reasoning and referring segmentation benchmarks on satellite and UAV images, FIRM achieves leading results, including $70.5/80.5$ gIoU/cIoU on LaSeRS and a $3.0$-point average gain on EarthReason. These results demonstrate the value of explicitly representing intra-token mask patterns for fine-grained MLLM segmentation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>SCVIB: Editable State-Conditioned Visual Instance Binding forMulti-Turn Personalized Localization</strong>
          <small>Xiongtai Yang, Ziyan He, Tao Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Referring Localization</span>
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
          <span>Paper 6 / arXiv:2608.14148</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14148">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: introduces a new embodied-style localization benchmark with multi-turn, state-conditioned instance binding and a method for it.</p>
        <p class="abstract">We introduce editable state-conditioned visual instance binding, a multi-turn localization setting in which several support-defined instances are introduced across turns and protocol-defined state events determine the final target. We instantiate this setting as SCVIB, comprising 1,050 manually verified support--query base pairs and 1,500 episodes spanning five visual domains, three difficulty levels, and four target-state dependency groups. Direct Seq-free inference reaches only 60.13\% Joint@0.5, indicating that resolving the final reference does not ensure effective use of the corresponding visual evidence for query-side localization. We address this gap with TT-VG (Transition-Tree Visual Grounding), which combines a Target-State Transition Tree (TSTT) with Visual Evidence Grounding Adaptation (VEGA). TSTT compiles the visible interaction into protocol-defined events, executes them over versioned target states, and resolves the final-query reference to the corresponding support evidence. Adapted on trajectory-derived same-instance pairs, VEGA performs support-conditioned grounding of the resolved instance using a Visual Evidence Package. TT-VG reaches 70.27\% Joint@0.5; under matched target resolution, VEGA exceeds the strongest comparison method by 16.20 points. Gains over direct inference are largest on Counter-Recency and Rollback, which require routing to non-latest or restored support evidence. Together, these results establish SCVIB as a controlled testbed and highlight the effective use of resolved support evidence for query-side same-instance localization as a central challenge in multi-turn personalized localization.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Beyond Text Conditioning: A Systematic Study of MLLM-DiT Fusion for Video Generation</strong>
          <small>Yanbo Ding, Yijia Fan, Caihua Shan, Yifan Yang, Yifei Shen, Weijie Wang, Xirui Hu, Dongsheng Li, Lili Qiu, Yuqing Yang, Yali Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM</span>
<span class="topic-tag">Video Generation</span>
<span class="topic-tag">Diffusion Transformers</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2608.14043</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14043">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: proposes a new MLLM-DiT hybrid for video generation and studies how to fuse MLLMs with diffusion transformers.</p>
        <p class="abstract">Diffusion Transformers (DiTs) have become the dominant paradigm for high-fidelity video generation, yet their ability to perform high-level semantic planning remains limited. While hybrid architectures integrating MLLMs with diffusion backbones have shown strong advantages in image synthesis, such designs remain underexplored in video generation, where existing approaches often treat MLLMs primarily as frozen feature encoders rather than semantic generators. To fill this gap, we systematically study how an MLLM should be integrated with a DiT for video generation by answering three questions: what intermediate representation should bridge the MLLM and DiT, how the MLLM should generate it, and how the DiT should incorporate it during diffusion rendering. Our analysis reveals three key findings: (1) discrete semantic visual tokens produced by an EMA-based tokenizer provide a stable and expressive interface, (2) autoregressive causal modeling is effective for generating these tokens, and (3) explicit visual-token conditioning is more effective than prompt refinement or latent bridging. Based on these findings, we propose BiVidGen, a hybrid framework where an MLLM first generates semantic visual tokens and a DiT renders videos conditioned on both text and these tokens via multi-layer cross-attention. Extensive experiments show that BiVidGen improves semantic alignment and temporal coherence over a fine-tuned DiT baseline, achieving stronger performance on VBench-Long. These results demonstrate that explicit MLLM-based visual planning provides an effective intermediate interface for text-to-video generation beyond text-only conditioning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LiDAR Self-Supervision</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>GhostPoint: Self-Supervised Representation Learning by Hallucinating Occluded LiDAR Structure</strong>
          <small>Mohamed Abdelsamad, Bin Yang, Michael Ulrich, Miao Zhang, Yakov Miron, Alexandru Paul Condurache, Abhinav Valada</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LiDAR Self-Supervision</span>
<span class="topic-tag">3D Spatial Reasoning</span>
<span class="topic-tag">Autonomous Driving</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2608.14428</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14428">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 closely: it improves spatial understanding for embodied/autonomous systems by hallucinating occluded LiDAR structure to better model missing 3D geometry.</p>
        <p class="abstract">3D object detection from LiDAR point clouds is a core problem in autonomous driving. Recent advances in self-supervised learning (SSL) enable scalable pretraining and transfers well to per-point tasks such as semantic and panoptic segmentation, but transfer to 3D detection remains weaker. We analyze recent SSL methods and find that most objectives are defined only on measured LiDAR returns from visible surfaces, leaving occluded and unobserved regions unconstrained. This visible-surface bias can be sufficient for point-wise prediction, but 3D detection requires robustness to missing structure. To address this gap, we propose GhostPoint, an SSL framework that hallucinates latent features in local neighborhoods around discovered instances, generated via a novel instance voxel dilation. In GhostPoint, an encoder processes observed returns, and an additional predictor infers neighborhood representations from observed context. In addition to standard encoder-level supervision, we introduce a predictor-level supervision scheme on sampled voxels from generated neighborhoods. Specifically, observed (visible/masked) voxels match teacher-encoder targets, while unobserved voxels match teacher-predictor hallucinations. This design encourages the learned representation to explicitly model structure beyond observed returns. Extensive evaluations on nuScenes and Waymo demonstrate that our method achieves state-of-the-art performance, consistently improving downstream 3D detection, especially under sparse scans and limited labels.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Image Editing</strong>
          <small>Qinye Zhou, Jun Zheng, Yongchao Du, Yuan Wang, Zhengrui Chen, Zuan Gao, Taihang Hu, Chao Lin, Yefeng Shen, Xingjian Wang, Zhao Wang, Zhengtao Wu, Xiaoli Xu, Zhengze Xu, Hao Yan, Denghui Yang, Yuhang Yu, Huayu Zhang, Mingzhou Zhang, Mengting Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Image Editing</span>
<span class="topic-tag">Reasoning-based Editing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2608.14546</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14546">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: a new benchmark for real-world image editing, including multi-image editing, practical deployment scenarios, and reasoning-based editing.</p>
        <p class="abstract">With the rapid advancement of image editing models and their widespread application across various domains, there is an increasingly urgent need to deploy these model capabilities directly into real-world scenarios. However, existing benchmarks remain confined to simple single-image tasks, suffering from limited coverage dimensions and an inability to effectively differentiate performance among diverse models. Consequently, they fail to reliably evaluate model performance in complex multi-image editing, highly demanding reasoning instructions, and practical deployment settings. To address these limitations, we propose CPI-Bench, a Comprehensive, Practical andIntelligent benchmark for real-world image editing. CPI-Bench comprises three core subsets: CPI-General-Bench, which comprehensively covers diverse editing tasks and pioneers the inclusion of multi-image editing evaluation; CPI-Practical-Bench, which focuses on high-frequency real-user application scenarios; and CPI-Intelligent-Bench, which is dedicated to evaluating capabilities in highly demanding reasoning-based editing. Evaluation results of mainstream image editing models based on CPI-Bench demonstrate that CPI-Bench enhances performance differentiation among models. It provides a comprehensive and reliable quantification of gaps in general editing capabilities, practical deployment efficacy, and advanced reasoning-based editing, offering invaluable guidance for the future optimization of image editing models. Crucially, our ranking analysis reveals that CPI-Bench achieves the highest alignment with the Arena Image Edit Leaderboard, indicating it faithfully captures the preferences and perceptual judgments of human evaluators, serving as a robust proxy for real-world user experience.</p>
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
          <strong>Rethinking Auxiliary Modalities in Multimodal Zero-shot Anomaly Detection: From Semantic Fusion to Conditional Modulation</strong>
          <small>Peng Wu, Xin Ge, Yujia Sun, Guansong Pang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Anomaly Detection</span>
<span class="topic-tag">Multimodal Fusion</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2608.13973</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.13973">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a multimodal anomaly detection method built around foundation-model-based RGB image-text matching and auxiliary modality conditioning.</p>
        <p class="abstract">Recent foundation model-based methods have endowed RGB images with strong zero-shot anomaly detection (ZSAD) through vision-language pretraining. However, RGB observations alone remain limited in perceiving anomalies dominated by geometric deformation, depth variation, or subtle surface changes. Auxiliary modalities can provide complementary structural information, but existing multimodal methods typically fuse them directly into a shared semantic space, which may disturb the text-aligned anomaly semantics established by RGB foundation models and often requires modality-specific architectures. To address this issue, we propose a plug-and-play auxiliary-conditioned enhancement framework for zero-shot anomaly detection. Instead of reconstructing a joint multimodal anomaly semantic space, our framework preserves the original RGB image-text anomaly matching pathway and uses auxiliary observations as conditional signals for RGB feature refinement, allowing auxiliary modalities to seamlessly enhance existing RGB-based zero-shot anomaly detectors. Specifically, a lightweight meta-learning module takes global RGB and auxiliary representations as input and generates sample-adaptive low-rank residual updates to determine how RGB features should be refined. We further construct uncertainty-aware spatial modulation from the initial RGB anomaly response and auxiliary reliability, which determines where local residual updates are strengthened or suppressed. This global-to-local conditional modulation enables selective multimodal enhancement while preserving the original RGB anomaly semantics. Extensive experiments on MVTec 3D-AD and Eyecandies demonstrate that our framework consistently improves multiple popular RGB-based zero-shot anomaly detectors, achieving state-of-the-art performance for multimodal zero-shot anomaly detection.</p>
      </div>
    </details>


    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>RankT2I: A Submodular Framework for Discovering Interpretable and Diverse Semantics in Text-to-Image Models</strong>
          <small>Ritika Allada, Pinar Yanardag</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Text-to-Image</span>
<span class="topic-tag">Semantic Discovery</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2608.14226</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14226">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: uses a multimodal vision-language model to discover editable semantics in text-to-image models, a neat application of foundation models.</p>
        <p class="abstract">Recent advances in text-to-image (T2I) models have revolutionized the field of image generation and editing. However, identifying semantics that a T2I model can successfully edit in an image continues to be a challenging task. Most existing approaches require users to manually specify semantics to modify a particular image, a time-consuming process that often involves extensive trial and error. In this paper, we present RankT2I, a novel, training-free, and model-agnostic framework that automates the discovery of editable semantics in diffusion and FLUX-based models. Given a visual domain, we first utilize a multimodal vision-language model to gather a broad set of candidate semantics. We then frame semantic discovery as a set selection problem and use a submodular objective to identify semantics that are relevant, editable, and diverse. Our method helps users efficiently identify a wide range of semantics for text-to-image editing models across several domains while outperforming existing methods.</p>
      </div>
    </details>


    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>PISA: A Pseudo-Individual Source-Domain Feature Adaptation Framework for Test-Time Open-Vocabulary Object Detection</strong>
          <small>Ziyan He, Xiongtai Yang, Tao Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Open-Vocabulary Detection</span>
<span class="topic-tag">Test-Time Adaptation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2608.14142</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14142">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a CLIP/open-vocabulary detection adaptation method that leverages foundation-model visual features under test-time shift.</p>
        <p class="abstract">Open-vocabulary object detection test-time adaptation (OVOD-TTA) aims to address the performance degradation that pre-trained base models suffer when encountering image-domain shifts. Existing source-free OVOD-TTA methods rely either on refined test-time information for re-scoring or on pseudo-labels for self-training, leading to significant accuracy degradation when initial predictions are poor. Meanwhile, most conventional source-domain estimation methods recover abstract, sparse representations suitable for the classification task, but fail to capture the dense, concrete features required for detection. To address these issues, we propose PISA, a novel source-free OVOD-TTA method that can be seamlessly integrated into open-vocabulary visual backbones. The core components of our method are the Corruption-Invariant Feature Extractor (CIFE), the Feature Alignment Module (FAM), and a multi-scale alignment framework (BAA). To capture detection-suitable features, we develop CIFE to exploit the invariance of CLIP&#x27;s visual features across corrupted images, ensuring robustness against various corruptions. We further develop FAM and BAA for the pre-training and adaptation to transform the corruption-invariant features into pseudo-individual source-domain features that are close to the original source-domain features. In this way, dense and concrete pseudo-individual source-domain features are used for supervision instead of unreliable pseudo-label signals. Experiments on the corrupted VOC-C, COCO-C, and LVIS-C benchmarks across three base models demonstrate that PISA substantially improves both the localization precision and the category recognition accuracy of the original models. Notably, PISA achieves state-of-the-art performance without requiring access to source-domain data, surpassing existing methods by 3.92% in AP@50% on COCO-C.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">VLM Analysis</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>Seeing Red, Thinking Bad: Color Bias in Vision Language Models</strong>
          <small>Kohsuke Ide, Ryousuke Yamada, Yoshihiro Fukuhara, Hirokatsu Kataoka, Yutaka Satoh</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">VLM Analysis</span>
<span class="topic-tag">Bias &amp; Fairness</span>
<span class="topic-tag">Visual Prompting</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2608.14286</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14286">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No direct match to the listed criteria, but it is relevant to your friend&#x27;s interest in vision-language model behavior and surprising empirical findings about bias.</p>
        <p class="abstract">Vision language models (VLMs) are increasingly used in industrial decision-making systems, such as recruitment support and recommendation. This motivates careful analysis of how VLMs process visual and textual information. In this work, we study how VLMs interpret text rendered as an image, and investigate the influence of visual styling biases. To this end, we introduce Stealth Visual Prompts, which subtly change visual styling of text, such as color and contrast, while preserving semantic content. Using these prompts, we systematically control the visual styling of words in text and measure their impact on the analysis performed by VLMs. We further analyze how such visual perturbations affect the latent representations of the vision encoder. From our experiments, we observed that coloring positive words in green consistently shifts sentiment predictions toward a positive direction. As a result, VLMs often fail to properly account for negative words present in the text. Our analysis suggests that this behavior is correlated with changes in the latent representations of the vision encoder induced by color variations. In addition, we show that reducing text--background contrast increases reliance on visually salient cues and leads to more incorrect Visual Question Answering (VQA) outputs. These results suggest that the visual styling of rendered text can guide VLMs&#x27; interpretation in ways that diverge from human semantic understanding.   Project page: https://github.com/KohsukeIde/color-bias-vlm</p>
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
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities in LLM Agents</strong>
          <small>Zhizhao Guan, Chen Huang, Ziming Liu, Hongru Liang, Wenqiang Lei, See-Kiong Ng, Tat-Seng Chua, Anthony G Cohn</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">LLM Agents</span>
<span class="topic-tag">Exploration Policies</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2608.14339</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14339">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it targets proactive exploration in LLM agents, which is an embodied-agent capability and proposes a new training method for it.</p>
        <p class="abstract">We study proactive exploration in LLM agents, i.e., the ability to explore an environment to acquire information that improves future decision-making. In this regard, we first identify two fundamental bottlenecks that hinder this capability and then propose \ours, a novel method designed to instill and refine proactive exploration. Specifically, \ours\ consists of two components: (1) Exploratory Data Construction, which synthesizes exploration-rich trajectories to mitigate the hindsight bias of standard demonstrations; and (2) RL Optimization with Contrastive Signal Guidance, which leverages contrastive trajectory pairs to distinguish productive exploration from redundant wandering. Extensive experiments demonstrate the effectiveness of \ours\ and provide insights into the characteristics of proactive exploration. Our code is available at: https://github.com/GuanZhizhao/SAFARI.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Agent Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>MobileMem: Learning from a Year of Mobile Experiences</strong>
          <small>Xinle Deng, Yida Xue, Xiangyuan Ru, Haoming Xu, Shuofei Qiao, Mengru Wang, Yijun Chen, Buqiang Xu, Chen Jiang, Yuchen Eleanor Jiang, Lizhong Wang, Jianfeng Wang, Li Zeng, Haofen Wang, Guilin Qi, Huajun Chen, Ningyu Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agent Benchmark</span>
<span class="topic-tag">Long-Term Memory</span>
<span class="topic-tag">Multimodal Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.LG</span>
<span class="category-tag">cs.MA</span>
<span class="category-tag">cs.MM</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2608.13606</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.13606">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> A partial match to criterion 3 only in the broad sense of building a benchmark for agent memory, but it is not an embodied AI/simulator paper and is more about long-term personal/mobile memory.</p>
        <p class="abstract">The next generation of AI agents is increasingly moving beyond systems that answer isolated questions toward persistent personal assistants that can understand, remember, and continuously learn from users&#x27; experiences. Such assistants require long-term memory to accumulate and leverage user-specific experiences over time, yet existing benchmarks remain inadequate for realistic mobile settings, where experiences are heterogeneous, multimodal, evolving, and deeply personal. We introduce MobileMem, a benchmark and framework for studying on-device long-term memory, grounded in a year-scale collection of mobile experiences. MobileMem employs a knowledge-grounded synthesis pipeline to construct coherent and temporally consistent long-horizon trajectories from user-app sessions. It provides complementary text and multimodal settings covering multi-hop and temporal reasoning, knowledge updating, and implicit preference inference. Specifically, MobileMem enables agents to remember the past, understand the present, and adapt to the future. By modeling experiences rather than isolated facts, MobileMem moves memory beyond information retrieval toward experiential intelligence for continuous personal learning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning</strong>
          <small>Kai Chen, Jifeng Ding, Ning Ding, Jiaye Ge, Lixin Gu, Yicheng Gu, Qipeng Guo, Ermo Hua, Haian Huang, Haozheng Hou, Jie Hou, Xiangyu Hong, Che Jiang, Minxi Jin, Cheng Liang, Dahua Lin, Dawei Liu, Kuikun Liu, Chengqi Lv, Haijun Lv, Han Lv, Ningsheng Ma, Biqing Qi, Jianmin Qian, Shiya Su, Youbang Sun, Huanze Tang, Zhongbo Tian, Hanjing Wang, Rui Wang, Ting Wang, Yi Wang, Baiting Wu, Jun Xu, Bowen Yang, Hui Wang, Weida Wang, Haochen Ye, Jiashuo Yu, Shan Yu, Xiaoyi Yu, Qirui Zeng, Qi Zhang, Ming Zhang, Wenwei Zhang, Bowen Zhou, Xinyu Zhou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Foundation Models</span>
<span class="topic-tag">Reasoning Efficiency</span>
<span class="topic-tag">Architecture</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2608.14290</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.14290">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No direct match to the listed criteria, though it is a foundation model architecture paper that may interest you for efficiency and reasoning design.</p>
        <p class="abstract">We introduce Mobius-v0, an architecture that comprises a globally shared Memory (FFN) that stores knowledge vectors and multiple Reasoners (Self-Attn) that iteratively achieve compositional reasoning. Using hidden states as cache and carrier, reasoners repeatedly query memory for required knowledge-vectors, while the knowledge is transmitted back to reasoning operators. Through this knowledge-reasoning-separation architecture, Mobius achieves better knowledge compression and reasoning efficiency. Built upon Mobius-v0 architecture: 1) Our 7B model trained-from-scratch achieves similar downstream score as a 7B Transformer baseline with 62.6% of baseline&#x27;s training data. 2) Our Intern-S2-Mobius, continually-pretrained from Qwen3.5-35B, achieves similar downstream score while delivering nearly 4x end-to-end inference speedup.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
