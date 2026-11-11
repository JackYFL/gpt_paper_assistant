

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
      <p class="eyebrow">Daily ArXiv / November 11, 2026</p>
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
      <strong>15</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>10.9</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">action</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">adaptation</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">camera</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">combine</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">computational</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">control</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">decoder</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">diagnosis</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="8 mentions">diagnostic</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">diffusion</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">disaster</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">distribution</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">domain</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="14 mentions">earth</span><span class="cloud-word" style="font-size:2.29rem;opacity:0.88;color:color-mix(in srgb, var(--accent-2) 76%, var(--accent))" title="11 mentions">embedding</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">evidence</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">fine-grained</span><span class="cloud-word" style="font-size:2.46rem;opacity:0.92;color:color-mix(in srgb, var(--accent-2) 84%, var(--accent))" title="12 mentions">foundation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">full</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">generation</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">imagery</span><span class="cloud-word" style="font-size:1.54rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="7 mentions">imaging</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">interface</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">landslide</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">landslidefm</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">language</span><span class="cloud-word" style="font-size:2.12rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 67%, var(--accent))" title="10 mentions">latent</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">location</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">matching</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">medical</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">multiple</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="8 mentions">observation</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="9 mentions">perception</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="9 mentions">pretrained</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">question</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">reasoning</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">reconstruction</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="8 mentions">segmentation</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="9 mentions">space</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">spatial</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">structure</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="5 mentions">support</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="6 mentions">video</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">view</span><span class="cloud-word" style="font-size:2.12rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 67%, var(--accent))" title="10 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.61rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="85 mentions">action</span><span class="cloud-word" style="font-size:2.12rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 67%, var(--accent))" title="126 mentions">agent</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="50 mentions">alignment</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="39 mentions">answer</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="43 mentions">attention</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="40 mentions">backbone</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="42 mentions">camera</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="43 mentions">change</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="48 mentions">control</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="45 mentions">detection</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="41 mentions">diffusion</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="41 mentions">domain</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="40 mentions">editing</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="45 mentions">embedding</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="49 mentions">environment</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="38 mentions">error</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="76 mentions">evidence</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="43 mentions">execution</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="49 mentions">foundation</span><span class="cloud-word" style="font-size:1.87rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="105 mentions">generation</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="40 mentions">geometric</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="46 mentions">geometry</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="42 mentions">inference</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="54 mentions">interaction</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="59 mentions">language</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="52 mentions">latent</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="74 mentions">memory</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="49 mentions">motion</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="60 mentions">multimodal</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="43 mentions">multiple</span><span class="cloud-word" style="font-size:1.37rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="68 mentions">object</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="42 mentions">observation</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="47 mentions">physical</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="71 mentions">point</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="49 mentions">policy</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="39 mentions">produce</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="51 mentions">prompt</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="38 mentions">question</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="95 mentions">reasoning</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="49 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="38 mentions">reference</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="37 mentions">region</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="53 mentions">reward</span><span class="cloud-word" style="font-size:1.40rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="70 mentions">same</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="76 mentions">scene</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="79 mentions">semantic</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="43 mentions">space</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="74 mentions">spatial</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="49 mentions">structure</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="46 mentions">supervision</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="58 mentions">support</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="41 mentions">target</span><span class="cloud-word" style="font-size:1.17rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="56 mentions">token</span><span class="cloud-word" style="font-size:1.21rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="58 mentions">trajectory</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="38 mentions">user</span><span class="cloud-word" style="font-size:2.01rem;opacity:0.8;color:color-mix(in srgb, var(--accent-2) 61%, var(--accent))" title="116 mentions">video</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="45 mentions">view</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="41 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="190 mentions">visual</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="60 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>16 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>ZoomGain: Mining Global-to-Zoom Perception Gaps for Fine-Grained Visual Supervision</strong>
          <small>Haozhan Shen, Liangbo He, Jun Lan, Huijia Zhu, Weiqiang Wang, Tiancheng Zhao, Jianwei Yin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Fine-Grained Perception</span>
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
          <span>Paper 1 / arXiv:2611.14076</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.14076">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: it studies VLM fine-grained perception gaps, creates a benchmark, and improves VLM training with new supervision.</p>
        <p class="abstract">Fine-grained visual perception requires Vision-Language Models (VLMs) to locate and interpret subtle evidence within complex scenes. Constructing supervision for this ability is challenging: questions must have correct, unambiguous answers that depend on actual fine-grained visual details rather than coarse cues or language priors. Verifying these properties makes manual annotation labor-intensive and automatic generation difficult for models that themselves struggle with fine-grained perception. Yet the same models can often recognize such details once the region is zoomed in. We exploit this global-to-zoom perception gap and introduce ZoomGain, a data construction pipeline that constructs questions about the full image from visual information gained only by zooming in. It verifies each answer on the zoomed view with multiple models, ensures that each question remains unambiguous in the full image and cannot be answered from language priors, and specifically generates high-quality distractors for multiple-choice questions. With this pipeline and human-only screening (no manual QA editing), we build ZoomGainBench, a 1,000-question bilingual benchmark on which the best of 28 VLMs achieves only 61.08. Failure analysis reveals that models favor a particular type of distractor when answering multiple-choice questions incorrectly. Beyond evaluation, training on just 9K ZoomGain samples substantially improves the visual perception capabilities of our 4B/9B models, enabling them to outperform several hundred-billion-parameter models across various perception benchmarks. The trained 9B model achieves SoTA performance on several benchmarks, such as 90.25 on HR-Bench 4K. These results establish global-to-zoom perception gaps as a practical basis for scaling fine-grained visual supervision for both evaluation and training. Our code is available at https://github.com/inclusionAI/ZoomGain.</p>
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
          <strong>GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning</strong>
          <small>Jiajun Chen, Shicheng Fang, Jiahao Lu, Yuxin Wang, Xipeng Qiu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Game Simulation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2611.13028</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13028">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it builds a new embodied-AI benchmark/environment for GTA V tasks and supports evaluation plus RL in a simulator-like setting.</p>
        <p class="abstract">AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA games is challenging and often human-annotated because task outcomes are often difficult to verify automatically, let alone applying it for Reinforcement Learning (RL). We introduce GTAGym, an environment and framework for evaluation and RL on GTA V tasks. Its evaluation benchmark, GTAVBench, derived from GTA V main-story missions, contains 103 online tasks reconstructed across nine task families, alongside 47 image-based shooting and sniping tasks using GTA V imagery. A web server provides access to the online environment and evaluation interface, supporting parallel testing through screenshots and keyboard-mouse actions with automatic engine-state outcome checks. We evaluate six frontier LLMs on GTAVBench with textual task instructions and on its GTAVBench-AGI branch, where instructions appear only in the first screenshot and a harness automatically compresses interaction history. The best configuration achieves 70.9% overall accuracy in GTAVBench-AGI, yet aerial navigation, evasion and interception remain difficult. GTAGym also provides a scalable generator that samples task parameters within user-specified ranges and option sets under fixed templates, creating batches of 3D and image-based shooting environments for RL with automatic reward and termination signals. LoRA RL of Qwen3.8-27B on generated on-foot navigation tasks improves the in-domain performance and transfers to out-of-domain task categories, and native GTA V tasks from 15% to 23%.</p>
      </div>
    </details>


    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models</strong>
          <small>Guoqiang Liang, Yiqi Lin, Yanzhe Chen, Kevin Yuchen Ma, Mike Zheng Shou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Video Diffusion</span>
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
          <span>Paper 3 / arXiv:2611.14365</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.14365">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: an embodied AI world-action model with a new latent interface for robot action/observation modeling, using pretrained video diffusion models.</p>
        <p class="abstract">Pretrained video diffusion models (VDMs) offer a powerful foundation for World Action Models (WAMs), which jointly predict robot actions and future observations. Building such models requires injecting low-dimensional robot signals (e.g. proprioception, actions, and values) into a latent space shaped by natural videos, and a key design choice is the interface through which these signals enter: existing schemes treat it as a formatting detail, spending a separate latent frame on each signal or bolting on dedicated encoders and decoders. We argue that signal injection is instead a distribution-alignment problem: how well a representation matches the prior of the pretrained VDMs during denoising. Using the relative reconstruction error of a frozen VDM denoiser as a probe, we find that conventional spatial encodings sit far off this prior, whereas frequency-domain packing yields latents that the denoiser corrects far less. Motivated by this diagnostic result, we propose MetaWAM, which folds all robot signals into a single unified meta-frame: each signal is assigned to a disjoint frequency-domain channel band and lifted to the spatial latent by an inverse DCT, yielding a decodable interface aligned with the pretrained VDM prior without any added module or architectural change. A fixed band layout together with slot-aware routing lets the same meta-frame support policy, world-model, and value prediction over a shared set of robot variables. On RoboCasa, MetaWAM reaches 68.9% success while collapsing the per-signal frames into one and cutting inference latency by 39%, and attains 85.0% success on three real-world Franka tasks. Code and models are available at https://github.com/showlab/MetaWAM</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Intelligence</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>X Marks the Spot: Diffusion for Image Geolocalization with Location Representations</strong>
          <small>Brian Wei, Chih-Chuan Hsu, Tianyi Gao, Daniel Cher, Eric Xing, Danielle Beaulieu, Nathan Jacobs</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Intelligence</span>
<span class="topic-tag">Image Geolocalization</span>
<span class="topic-tag">Diffusion Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2611.13180</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13180">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: it targets spatial understanding via image geolocalization and introduces a new latent representation for location prediction.</p>
        <p class="abstract">Image geolocalization predicts the location at which a photo was taken. Accurate geolocalization requires discriminating between both physically and semantically adjacent areas on Earth. However, prior diffusion-based approaches predict locations by generating coordinates, which are semantically unstable over space. We avoid this limitation by learning geolocalization behavior in the pretrained representation spaces of location encoders, which provide both positional and semantic understanding. To make this space usable for coordinate prediction, we introduce a Location Autoencoder (LAE), which pairs a frozen location encoder with a learned decoder mapping embeddings back to coordinates with kilometer-level accuracy worldwide. In the LAE space, we train DIG, a latent diffusion model that transports noise to location embeddings conditioned on image features. DIG consistently outperforms coordinate-based generative models and sets a new state of the art for parametric geolocalization on three benchmarks: OSV-5M, Im2GPS3k, and YFCC4k. Notably, DIG is the first generative model to outperform retrieval-based methods, and further improves retrieve-and-rerank systems when used as a prior. Code and models will be released.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multi-Modal Large Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Evidence-Grounded Iterative Reasoning for the Diagnosis of Diffuse Cystic Lung Diseases</strong>
          <small>Haoqing Li, Jun Shi, Tou Li, Xianmeng Chen, Rui Wang, Yating Peng, Qiwei Jia, Li Gao, Qianyi Chen, Hong An, Ruoyun Ouyang, Xiaowen Hu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multi-Modal Large Language Models</span>
<span class="topic-tag">Medical Diagnosis</span>
<span class="topic-tag">Evidence-Grounded Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2611.12981</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.12981">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2: it uses an MLLM-style evidence-grounded iterative reasoning framework for multimodal diagnosis.</p>
        <p class="abstract">Overlapping imaging manifestations complicate the differential diagnosis of Diffuse Cystic Lung Diseases (DCLDs), while limited annotated data constrain supervised model development. Multimodal Large Language Models (MLLMs) can integrate imaging and clinical information, but their diagnostic reasoning remains limited by incomplete volumetric perception and insufficient grounding in disease-specific evidence. We propose DCLDs-EIR, an evidence-grounded iterative reasoning framework coupling diagnostic hypothesis refinement with multimodal evidence acquisition and verification. Multiview renderings of predicted lung and cyst segmentations characterize global cyst distributions and initialize the differential diagnosis. Competing hypotheses guide axial CT inspection to identify local findings that, together with clinical context, inform retrieval from a disease-specific knowledge graph. Accumulated patient observations and retrieved knowledge are jointly assessed for diagnostic support and refutation to revise the diagnostic state. Updated hypotheses and unresolved distinctions guide subsequent inspection, forming a feedback loop between evidence acquisition and hypothesis verification. Multicenter evaluation demonstrates that DCLDs-EIR consistently improves diagnostic accuracy over baselines and enables traceable differential diagnosis through explicit links between diagnostic hypotheses, patient observations, and disease-specific knowledge.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Camera3R: Feed-Forward 3D Reconstruction from Heterogeneous Camera Models</strong>
          <small>Ruxiao Duan, Yunwen Zhou, Erin Hong, Dongxu Zhao, Eric Turner, Federico Tombari, Alex Wong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Camera Adaptation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2611.13453</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13453">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it extends a foundation-style 3D reconstruction model to heterogeneous camera models, an application of vision foundation models.</p>
        <p class="abstract">Feed-forward 3D reconstruction (3R) from unconstrained multi-view images has recently emerged as a prominent research direction in 3D computer vision. Various foundational reconstruction models have been proposed with different architectures and reconstruction paradigms. Despite being trained on large-scale perspective datasets with substantial computational resources, these models generally struggle to generalize to non-perspective images. This limitation hinders their deployment in applications involving arbitrary, unknown, and potentially heterogeneous camera models. To build on the capabilities of existing reconstruction models with minimal retraining, we propose Camera3R, a low-rank adaptation framework that efficiently extends perspective-pretrained 3R networks to any other camera models. Extensive experiments demonstrate that, with only 0.5% additional parameters and less than a day of training, Camera3R adapts a foundational 3D reconstruction model to non-perspective cameras while fully preserving its original performance on perspective inputs. Code is available at https://github.com/android-xr/camera3r.</p>
      </div>
    </details>


    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Adapting a Vision Foundation Model for Fracture Characterization in Acoustic Image Logs</strong>
          <small>Guangyu Wang, Xiaodong Ma, Xinming Wu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Geoscience Imaging</span>
<span class="topic-tag">Few-Shot Fine-Tuning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2611.13911</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13911">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: it adapts a pretrained vision foundation model to a specialized geoscience imaging task, but the contribution is mainly a downstream application.</p>
        <p class="abstract">Natural fractures (NFs) and drilling-induced tensile fractures (DITFs) in acoustic image logs provide insights into rock mass structure and in situ stress, but manual characterization is time-consuming. Deep learning can automate this task, although expert-labeled data are scarce. We investigate whether adapting a pretrained vision foundation model (VFM) outperforms task-specific models trained from scratch with limited annotations. Using 80 annotated acoustic image samples, we fine-tuned DINOv3, pretrained on satellite imagery, and evaluated it on four boreholes excluded from fine-tuning. The adapted model estimated NF and DITF parameters comparably to human interpretation. Relative to U-Net, YOLOv8, and Swin Transformer models trained from scratch, it yielded fewer false positives and negatives and more accurate fracture counts and orientations. However, its performance advantage generally narrowed as training sample size decreased. We also assessed decoder architecture, fine-tuning strategy, and image enhancement. A progressive upsampling decoder with full fine-tuning performed best among the DINOv3 configurations tested, while fracture-focused image enhancement did not consistently improve accuracy. These results demonstrate the potential of VFM adaptation for fracture characterization in acoustic image logs with limited labeled data and suggest a transferable workflow for other annotation-scarce geoscientific imaging tasks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Open-World Segmentation</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>MEOW: Medical Open-World Interactive Segmentation</strong>
          <small>Philip Matthias Winter, Maria Wimmer, Bernhard Sch\&quot;{a}fl, David Major, Dimitrios Lenis, Astrid Berg, Theresa Neubauer, Ariharasudhan Muthusami, Johannes Novotny, Georg Zotti, Katja B\&quot;{u}hler</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Open-World Segmentation</span>
<span class="topic-tag">Interactive Learning</span>
<span class="topic-tag">Medical AI</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">stat.ML</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2611.13935</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13935">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: an embodied/interactive segmentation method with open-world continual learning behavior, though in medical imaging rather than robotics or simulation.</p>
        <p class="abstract">In open-world recognition, machine learning models not only make predictions on unknown structures (&quot;generalized open-set&quot;), but also continually learn and improve from those predictions over time. Interactive segmentation, despite its access to user feedback, has so far remained confined to the open-set setting. In this work we introduce MEOW, the first framework that turns non-interactive segmentation backbones into interactive open-world learners without updating learnable model parameters. MEOW combines parameter-free transductive reasoning with memory consolidation to accumulate knowledge and thereby improve future performance. Focusing on medical data, we show that MEOW consistently improves its own predictions on classes never seen during training, and transfers zero-shot to unfamiliar domains, including micro-CT data and other imaging modalities.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Just Image Transformers with Late-Stage Pixel Refinement</strong>
          <small>Denis Lukovnikov, Andreas M\&quot;uller, Asja Fischer</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Generation</span>
<span class="topic-tag">Diffusion Transformers</span>
<span class="topic-tag">Vision Foundation Models</span>
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
          <span>Paper 9 / arXiv:2611.13120</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13120">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a vision foundation/model-generation paper on latent-free image generation with improved pixel refinement; strong fit for generative modeling in vision.</p>
        <p class="abstract">Recent work on latent-free diffusion transformers has demonstrated the feasibility of training image generators without a latent VAE. This avoids compression artifacts from the VAE and simplifies the training pipeline. In particular, JiT showed that even a standard transformer can be trained to generate images when the model is trained to predict the final image ($x$-prediction). Even though JiT unlocks training efficiency comparable to latent models, it still suffers from reduced image quality likely arising from modeling the image as a collection of large patches. In this work, we revisit JiT and show that adding simple convolutional pixel-pathway layers in a post-training phase significantly improves generation quality. Moreover, we show that the added pixel-pathway does not need to be active in the early denoising stages, and can be activated as late as in the last $20\%$ of the denoising process. Our experiments on ImageNet@256 show improvements compared to the original JiT results, achieving an FID of $1.78$ (from $2.34$ with corrected sampling), without using additional losses.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Referring Segmentation</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>DroneSegEdit: Adapting Pretrained Generative Editors for UAV Segmentation with Language-Grounded Verification</strong>
          <small>Dehua Chen, Long Xin, Jiangtao Wei</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Referring Segmentation</span>
<span class="topic-tag">UAV Perception</span>
<span class="topic-tag">Vision-Language Grounding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2611.13890</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13890">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: UAV referring segmentation with a novel grounding-rendering gap fix and language-grounded verification; also touches criterion 2 via an MLLM-backed verifier.</p>
        <p class="abstract">Recent work has shown that pretrained image generators can support diverse visual tasks. Yet directly applying them to language-guided unmanned aerial vehicle (UAV) segmentation exposes a key limitation: a plausible mask may correspond to the wrong instance among small and repeated objects. We call this mismatch between mask rendering and expression-level target selection the Grounding-Rendering Gap. We present DroneSegEdit, which combines RGB proposal rendering with language-grounded, proposal-constrained verification to select supported foreground while retaining rendered geometry. DroneSegEdit adapts the open-weight LongCat-Image-Edit model using task-specific LoRA and fixed color-to-label decoding. For referring segmentation, a Language-Grounded Spatial Verifier (LGSV) reads hierarchical states from the frozen multimodal large language model backbone to derive expression-conditioned spatial evidence, which is mapped back to the rendered proposal without introducing foreground outside it. On RIS-LAD, DroneSegEdit reaches a new state of the art at 52.78 mIoU, 7.16 points above the previous best. It remains competitive overall on UAVid-RIS and VDD-RIS, with its clearest class-wise gains on compact, application-relevant categories, notably vehicles and humans. A separate verifier-free experiment extends the RGB interface to full-scene parsing: a task-specific adapter jointly renders all classes from one task-level instruction without enumerating class names or palette colors.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Toward Foundation Detection Models via Example-Based Grounding in EM-DETR</strong>
          <small>Sheethal Bhat, Bogdan Georgescu, Awais Mansoor, Florin C. Ghesu, Sasa Grbic, Andreas Maier</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Detection</span>
<span class="topic-tag">Foundation Models</span>
<span class="topic-tag">Multi-Domain Learning</span>
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
          <span>Paper 12 / arXiv:2611.14518</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.14518">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: explicitly about building a foundation detection model across heterogeneous medical datasets, with multi-domain training and example-based grounding.</p>
        <p class="abstract">DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by integrating diverse medical image datasets annotated for both anatomical structures and abnormalities. We first propose a student-teacher training strategy to effectively combine datasets with heterogeneous label spaces, mitigating catastrophic forgetting, and im proving feature learning. In addition, building on our previously pro posed example-based EM-DETR framework, we adapt it to jointly learn from multiple domain-specific datasets, enabling fine-grained, example driven detection across modalities. Our model achieves state-of-the-art (SOTA) results, with image-level AUC scores exceeding previous SOTA by 1% point on four key findings in CXRs. We achieve a leading mAP50 in CXRs and mammography, surpassing EM-DETR trained on a single dataset by 2-3% points. This approach paves the way for scalable foundation models in medical imaging that leverage heterogeneous data while maintaining robust and generalizable performance.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Medical Imaging</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Prompt2Echo (P2Echo): Text-Prompted Multi-View Echocardiography Segmentation with One Model</strong>
          <small>Moein Heidari, Alvin Kimbowa, Mahdi Tabatabaei, Afshin Bozorgpour, Sina Ghorbani Kolahi, River Jiang, Wenjin Chen, David J. Foran, Jasmine Grewal, Dorit Merhof, Ilker Hacihaliloglu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Medical Imaging</span>
<span class="topic-tag">Prompted Segmentation</span>
<span class="topic-tag">Foundation Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2611.13425</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13425">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a controllable segmentation framework built around structured text prompts and dynamic image-text alignment, using foundation-model-style adaptation for medical imaging.</p>
        <p class="abstract">Automated segmentation in multi-view echocardiography is essential for comprehensive cardiac assessment, yet remains challenging due to substantial anatomical and appearance variability across standard acoustic windows. In this paper, we present P2Echo, a unified framework capable of segmenting diverse cardiac structures across multiple standard echocardiographic views using a single model controlled by structured view-aware text prompts. Unlike recent foundation model adaptations that rely on implicit latent priors, P2Echo explicitly conditions the segmentation process via a novel Dynamic Image-Text Alignment (DyITA) module. DyITA integrates a differentiable routing mechanism and token differential operators to dynamically modulate decoder features according to the requested view and target structure. This allows the network to adaptively switch its processing pathways for different views without architectural changes. Extensive experiments on a large-scale internal dataset (seen during training) and held-out evaluation on three external datasets demonstrate that P2Echo matches or exceeds both view-specific specialists and state-of-the-art universal models at a fraction of their computational cost, offering an efficient, controllable solution for multi-plane cardiac analysis. Code is available at: https://github.com/moeinheidari7829/P2Echo.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Diffusion Models</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>Stylization as Geodesic Navigation on Diffusion Manifolds</strong>
          <small>Yan Li, Zehao Li, Xinlong Sun, Fuchen Long, Xi Chen, Wenhan Luo, Yike Guo</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Image Stylization</span>
<span class="topic-tag">Geometric Optimization</span>
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
          <span>Paper 15 / arXiv:2611.14097</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.14097">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; it is a diffusion-manifold stylization method, relevant to vision/generative modeling but not one of the target criteria.</p>
        <p class="abstract">Facial stylization asks for a delicate transformation: the image should look unmistakably artistic, yet the person should remain unmistakably the same. Existing training-free and instruction-driven methods often fail to expose such control, either drifting away from identity or producing only weak stylization. We introduce Stylus, a training-free framework that treats facial style transfer as navigation on the curved latent manifold of a pretrained diffusion model. Rather than interpolating in flat Euclidean space, \method refines the interpolated content--style point by lowering a ratio-weighted discrete geodesic energy under the pullback metric, made tractable by a rank-one power-iteration approximation of the Jacobian. This principle drives two complementary controls: content--style latent interpolation for smooth semantic fusion, and self-attention query optimization for spatially adaptive style injection. The resulting dual-control mechanism provides continuous, fine-grained control over stylization strength while preserving identity-critical facial structure, all without additional training. Experiments show that Stylus achieves the strongest identity and content preservation at competitive stylization strength.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Generative Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>Trajectory-Regularized Distribution Distillation for One-Step Generation</strong>
          <small>An Zhao, Yixiang Zhou, Zejian Li, Yi Guo, Pei Chen, Lingyun Sun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Diffusion Distillation</span>
<span class="topic-tag">One-Step Generation</span>
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
          <span>Paper 16 / arXiv:2611.12978</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.12978">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; it is a generative-model distillation method, but not specifically a VLLM/MLLM, embodied AI, or vision foundation model paper.</p>
        <p class="abstract">Distilling flow matching models for one-step generation generally follows two paradigms. Trajectory alignment supervises the student with the teacher&#x27;s probability flow ODE, but its performance degrades under very small sampling budgets. Distribution matching directly optimizes the generated distribution, but estimating its reverse Kullback-Leibler gradient typically requires a separate network to track the evolving student score. We propose trajectory-regularized distribution distillation (TRD), which combines distribution-level and trajectory-level supervision through a momentum-mixture policy predicted in a single student forward pass. This policy serves simultaneously as a one-step generator, an estimator of the student&#x27;s marginal velocity that removes the need for a second trainable network in distribution matching, and a closed-form time-dependent velocity field supervised along the teacher ODE trajectory. Experiments on SANA-1.6B and Stable Diffusion 3.5 show that TRD outperforms representative consistency and distribution matching baselines in generation quality and training efficiency for both one-step and few-step generation, with a trade-off in sample diversity.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>Domain adaptation of a video Foundation model for Heart Failure Diagnosis from Echocardiography</strong>
          <small>Mahyar Bolhassani, Tijana Geroski, Narayana S. Singam, Amir Amini</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Foundation Models</span>
<span class="topic-tag">Medical Imaging</span>
<span class="topic-tag">Domain Adaptation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2611.13297</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13297">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: it adapts a video foundation model for a medical video task, but this is an application rather than a broadly new foundation-model method.</p>
        <p class="abstract">The rapid advancement of foundation models has transformed computer vision, yet their adaptation to medical imaging, particularly purpose built foundation models for spatio temporal echocardiography videos, remains limited. In this work, we explore the feasibility of fine tuning a pretrained foundation model for video (TimeSformer) for automated diagnosis of reduced ejection fraction heart failure (HFrEF) from apical four chamber videos. The model is finetuned on the publicly available RVENet A4C dataset with a phase aware clip generation strategy that captures complementary systolic and diastolic dynamics. We employ divided space time attention, layer wise learning rate decay, and multi clip inference to enhance robustness under limited data. Experimental results show that full fine tuning of the proposed model outperforms classifier only tuning and a 3D CNN baseline. These findings highlight the potential of leveraging foundation video models for echocardiography based heart failure diagnosis and motivates further domain adaptation studies in medical imaging.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">UAV Vision</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>picoEmergencyNet : Attention-Enhanced Ultra-Small Deep Learning Model for Aerial Image Classification in Emergency Monitoring</strong>
          <small>Christos Kyrkou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">UAV Vision</span>
<span class="topic-tag">TinyML</span>
<span class="topic-tag">Aerial Image Classification</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">6</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2611.13638</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13638">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>3</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 only loosely: an embodied/UAV deployment-oriented method for aerial disaster monitoring, but it is mainly a lightweight classifier rather than a novel embodied benchmark or spatial method.</p>
        <p class="abstract">Real-time disaster recognition from aerial imagery requires deep learning models that operate under strict memory, compute, and latency constraints. While recent approaches achieve high accuracy, their computational cost limits deployment on resource-constrained UAV platforms. This work introduces picoEmergencyNet, an ultra-lightweight convolutional neural network designed for aerial image disaster classification. The proposed architecture combines depthwise dilated convolutions with efficient channel attention and channel shuffling to enable multi-scale feature extraction at minimal computational cost. picoEmergencyNet has 23k parameters and 7M FLOPs, requiring only 0.1 MB of model storage. Evaluated on the AIDER and AIDERv2 disaster datasets, it achieves up to 96.1% accuracy, matching or exceeding state-of-the-art lightweight models that are orders of magnitude larger. Deployment experiments on the NVIDIA Jetson AGX Orin show that, without hardware-specific optimizations, picoEmergencyNet achieves 258 FPS on GPU and 46 FPS on CPU with a 7x lower activation memory footprint compared to competing models. These results demonstrate that careful architectural specialization, rather than model scaling, enables highly efficient and accurate TinyML-ready disaster recognition for real-time UAV-based emergency monitoring.</p>
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
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>LandslideFM: A Foundation Model Towards Unified Landslide Perception and Understanding</strong>
          <small>Shanwen Wang, Sirui Wang, Xin Sun, Jungong Han</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Foundation Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2611.12936</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.12936">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it proposes a landslide foundation model plus a new benchmark for landslide perception and reasoning, combining vision and language.</p>
        <p class="abstract">Intelligent landslide detection is essential for disaster prevention. However, existing models primarily focus on isolated visual tasks, require extensive labeled data, and lack deep analytical and scene-understanding capabilities. To address these limitations, we propose LandslideFM, the first unified foundation model that connects visual perception tasks with contextual interpretation of landslides. Specifically, LandslideFM adapts to multiple visual tasks via a Source-Agreement Graduated Trust semi-supervised learning framework that leverages limited labeled data alongside abundant unlabeled data. Furthermore, predicted landslide regions provide explicit spatial guidance to a Vision-Language Model adapted through parameter-efficient fine-tuning, enabling comprehensive landslide reasoning. To support training and evaluation in this domain, we also present LandslideVL, the first benchmark for intelligent landslide analysis, combining visual imagery and newly introduced textual prompts. Comprehensive experiments across public datasets and LandslideVL demonstrate that LandslideFM achieves superior quantitative and qualitative performance. Most importantly, LandslideFM surpasses general-purpose VLMs in specialized landslide reasoning and scene analysis. Our code is released at https://github.com/wangshanwen001/LandslideFM.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Autonomous Experimentation</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>Auditable Human-Agent Teams for Autonomous X-ray Experimentation</strong>
          <small>Gunik Luthra, Ronald J. Pandolfi, Benjamin T. Diroll, Ricky Ronquillo, Ruipeng Li, Christopher B. Murray, Marcus M. Noack, Kevin G. Yager, Esther H. R. Tsai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Experimentation</span>
<span class="topic-tag">Human-Agent Collaboration</span>
<span class="topic-tag">Scientific Agents</span>
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
          <span>Paper 11 / arXiv:2611.12933</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.12933">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: autonomous scientific experimentation with human-agent teams, focusing on a new operational/audit angle for embodied/agentic systems.</p>
        <p class="abstract">Closed-loop autonomous experimentation can accelerate scientific discovery, but implementation effort limits accessibility. Agentic systems may lower this barrier, although sustained operation on physical instruments remains largely unexplored. Here, using coding-agent infrastructure grounded in validated scientific methods, we demonstrate autonomous synchrotron X-ray experiments on nanoparticle superlattices under evolving, human-defined objectives. Complete human-agent and agent-agent transcripts enable an audit that reconstructs decision provenance and characterizes the division of cognitive labor. Across three experiments, 61-67% of messages involved interpretation or judgment, while the share of methodological and scientific contributions increased from 46% in the setup-focused first experiment to 56-61% in later experiments. Provenance showed that 59-68% of error corrections involved multiple participants and that about half of all decisions incorporated the input of another participant. These results may guide design principles for multi-agent scientific systems and inform future agent harnesses, model training, and accessible autonomous experimentation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Earth Embeddings in Environmental Remote Sensing</strong>
          <small>Yuchi Ma, Jiaqi Yang, Mengyu Liang, Ivan Higuera-Mendieta, Caleb Robinson, Anthony Ortiz, Min Chen, David B. Lobell, Inbal Becker-Reshef, Juan M. Lavista Ferres</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2611.13612</span>
          <a class="paper-action" href="https://arxiv.org/abs/2611.13612">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it is explicitly about Earth embeddings as a vision foundation model representation and evaluates downstream applications.</p>
        <p class="abstract">Earth observations from satellite platforms have profoundly transformed research and applications across numerous domains. However, uneven observation coverage and frequent data gaps continue to limit their ability to capture Earth&#x27;s surface dynamics. Moreover, processing multi-modal Earth observations requires substantial computational resources and sophisticated data harmonization frameworks, which may not be readily accessible to many remote sensing practitioners. Earth embeddings have emerged as promising solutions to these challenges. As general-purpose representations converted from multi-source Earth observations, Earth embeddings can support a wide range of downstream tasks with no requirement of task-specific feature design and preprocessing. In this study, we first introduce the theoretical foundations of Earth embeddings. Then, we review several representative Earth embedding products. We next examine the applications of Earth embeddings across six major domains of environmental remote sensing. Finally, we systematically assess the performance of Earth embeddings in four downstream tasks, including hyperspectral image classification, individual tree crown segmentation, crop yield prediction, and aboveground biomass mapping. Our review and case studies suggest that, despite several advantages over conventional Earth observation data, current Earth embeddings do not always outperform remote sensing imagery or hand-crafted features. Earth embeddings should not be viewed as a direct replacement for conventional EO data, but rather as representations that provide stable information across space and time. Remote sensing practitioners may consider evaluating Earth embeddings&#x27; suitability for specific tasks and using them strategically, rather than assuming superior performance by default.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

        <a class="archive-link" href="past_arxiv/2026-11-09.html">
          <span>November 09, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-06.html">
          <span>November 06, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-05.html">
          <span>November 05, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-03.html">
          <span>November 03, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-11-02.html">
          <span>November 02, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-31.html">
          <span>October 31, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-28.html">
          <span>October 28, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-27.html">
          <span>October 27, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-26.html">
          <span>October 26, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-23.html">
          <span>October 23, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-22.html">
          <span>October 22, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-21.html">
          <span>October 21, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-19.html">
          <span>October 19, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-16.html">
          <span>October 16, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-15.html">
          <span>October 15, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-13.html">
          <span>October 13, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-12.html">
          <span>October 12, 2026</span>
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
