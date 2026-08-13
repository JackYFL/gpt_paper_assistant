

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
      <p class="eyebrow">Daily ArXiv / August 13, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>21</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>15</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>11.5</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.11rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 66%, var(--accent))" title="11 mentions">action</span><span class="cloud-word" style="font-size:1.92rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="10 mentions">agent</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">annotation</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">architecture</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">attribute</span><span class="cloud-word" style="font-size:1.92rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="10 mentions">branch</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="8 mentions">change</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">complementary</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">condition</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">consistently</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">counterfactual</span><span class="cloud-word" style="font-size:1.92rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="10 mentions">detection</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">diagram</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">distribution</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="9 mentions">driving</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">expert</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">foundation</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="9 mentions">frame</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">frozen</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">fusion</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="9 mentions">generation</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="9 mentions">generative</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="8 mentions">hierarchical</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="9 mentions">judge</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">latent</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="9 mentions">mllm</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">modality</span><span class="cloud-word" style="font-size:2.11rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 66%, var(--accent))" title="11 mentions">multimodal</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">navigation</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="9 mentions">object</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">pipeline</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="8 mentions">planning</span><span class="cloud-word" style="font-size:1.92rem;opacity:0.78;color:color-mix(in srgb, var(--accent-2) 57%, var(--accent))" title="10 mentions">reasoning</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">response</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="9 mentions">scene</span><span class="cloud-word" style="font-size:2.45rem;opacity:0.92;color:color-mix(in srgb, var(--accent-2) 84%, var(--accent))" title="13 mentions">semantic</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="6 mentions">structure</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">supervision</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">thermal</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">token</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="8 mentions">trajectory</span><span class="cloud-word" style="font-size:1.73rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="9 mentions">understanding</span><span class="cloud-word" style="font-size:2.11rem;opacity:0.83;color:color-mix(in srgb, var(--accent-2) 66%, var(--accent))" title="11 mentions">video</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="15 mentions">visual</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="7 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="112 mentions">action</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 48%, var(--accent))" title="218 mentions">agent</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="92 mentions">alignment</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="79 mentions">attention</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="83 mentions">challenging</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="73 mentions">change</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="71 mentions">condition</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="99 mentions">consistency</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="76 mentions">consistently</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="71 mentions">control</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="113 mentions">detection</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="89 mentions">diffusion</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="79 mentions">distribution</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="77 mentions">domain</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="102 mentions">dynamic</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="77 mentions">environment</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="205 mentions">evidence</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="98 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="85 mentions">foundation</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="102 mentions">frame</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="70 mentions">fusion</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="259 mentions">generation</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="71 mentions">geometry</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="99 mentions">inference</span><span class="cloud-word" style="font-size:1.33rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="141 mentions">interaction</span><span class="cloud-word" style="font-size:1.41rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 30%, var(--accent))" title="154 mentions">language</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="86 mentions">latent</span><span class="cloud-word" style="font-size:1.23rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="125 mentions">memory</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="88 mentions">mllm</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="88 mentions">modality</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="139 mentions">motion</span><span class="cloud-word" style="font-size:1.71rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 46%, var(--accent))" title="211 mentions">multimodal</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="99 mentions">multiple</span><span class="cloud-word" style="font-size:1.51rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="172 mentions">object</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="78 mentions">perception</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="88 mentions">pipeline</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="94 mentions">point</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="84 mentions">real-world</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="198 mentions">reasoning</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="111 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="83 mentions">region</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="78 mentions">retrieval</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="70 mentions">robust</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="149 mentions">scene</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="73 mentions">segmentation</span><span class="cloud-word" style="font-size:1.83rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="235 mentions">semantic</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="98 mentions">space</span><span class="cloud-word" style="font-size:1.31rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="138 mentions">spatial</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="91 mentions">structure</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="86 mentions">support</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="124 mentions">target</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="124 mentions">temporal</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="185 mentions">token</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="81 mentions">trajectory</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="144 mentions">understanding</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="104 mentions">unified</span><span class="cloud-word" style="font-size:2.28rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 75%, var(--accent))" title="339 mentions">video</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="87 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="475 mentions">visual</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="88 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.AI</h3>
        <span>3 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>HUGIN: Enhancing Vision-Language Planning for Autonomous Logistics Sorting</strong>
          <small>Xikai Sun, Cangtian Zhou, Kebin Liu, Ke Ma, Xu Wang, Zaishu Chen, Haotian Wang, Li Liu, Yunhao Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Vision-Language Planning</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multi-Scene Understanding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2608.11692</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11692">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: embodied AI paper building a new simulator-related benchmark (SortingBench) and proposing a new VLM planning method for spatially disjoint multi-scene understanding.</p>
        <p class="abstract">Autonomous logistics sorting systems (ALSS) are an important industrial application of embodied AI, which requires joint planning over spatially disjoint camera views. We formulate this setting as Joint Multi-Scene Understanding (JMSU). With open-world visual understanding and task-planning capabilities, vision-language models (VLMs) are promising candidates for JMSU. However, directly applying existing VLMs to JMSU is non-trivial due to scarce cross-scene supervision and attention dispersion caused by long visual context in JMSU. To address these challenges, we propose HUGIN, a training framework with two complementary components. Endogenous Data Augmentation recombines verified atomic facts under operating constraints, while Global Context Ranking aligns the instruction representation more strongly with the complete visual context than with a partial visual context. To support ongoing research, we construct a high-quality industrial sorting dataset and benchmark named SortingBench from four layouts of autonomous logistics sorting systems. Across five open VLMs, HUGIN consistently outperforms matched baselines; for example, the accuracy on SortingBench of Qwen3-VL-8B increases from 63.6% to 78.8%. Additional experiments verify the effectiveness of each component and JMSU&#x27;s spillover benefits in embodied tasks. Deployment tests involving more than 15,000 packages support the practical viability of VLM-based planning for autonomous logistics sorting.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>Apodex Discovery: Reality Benchmarks and Environments for Evaluating and Building Discoverative Artificial Intelligence</strong>
          <small>Brian Wang, Bin Feng, Xiaoman Pan, Chenyang An, Felix Liu, Tangqi Fang, Gongbo Sun, Lingfeng Shen, Ning Wang, Handuo Zhang, Feng Chen, Fuchao Yang, Xiang Wang, Jiacheng Lin, Siting Li, Zixuan Liu, Chi Han, Zhenhailong Wang, Kunlun Zhu, Lawrence Zhao, Yueqi Guo, Kailong Wen, Feng Xing, Yiling Guo, Lidong Bing, David Tan, Bo An, Heng Ji, Sheng Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Evaluation</span>
<span class="topic-tag">Benchmark &amp; Environment</span>
<span class="topic-tag">Tool Use</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2608.11341</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11341">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it builds new benchmarks/environments for discoverative AI with explicit simulation, verification, and tool use.</p>
        <p class="abstract">Apollo did not reach the Moon merely because its engineers could solve difficult equations. It succeeded by turning a distant ambition into a mission architecture of explicit objectives, simulation, verification, and repeated correction. AI now faces a similar transition: frontier models can solve difficult tasks once the problem, tools, and success criteria are specified, yet consequential real-world challenges rarely arrive in an executable or verifiable form.   We introduce Apodex Discovery, a framework for building and evaluating discoverative AI through the heavy-duty solver, a system comprising a foundation model, harness, tools, and control policies that pursues extended, stateful, verifiable investigations. It has three core components. First, a problem-scouting process surveyed 561 industries across 16 sectors, assembled 423 high-value real-world problems, and selected 20 for the initial release. Second, a common environment-task-episode abstraction provides data, tools, constraints, feedback, trajectory recording, and verification of intermediate artifacts and final submissions. Third, HDS6 evaluates Tools, Repair, Alternatives, Coherence, Evidence, and Scope independently of final-task success.   In AAV capsid design, Apodex surpassed the published state of the art by 7% across viability, tropism, structure prediction, and generative design. In drug repurposing and reformulation, a task-specific biomedical environment improved the mean normalized prediction score of GPT-5.5 and GPT-5.6-sol by 2.5 and 7.6 points over the same closed-book backbone. Controlled ablations show that the fixed TRACES episode interface enables attribution of performance differences to specific solver components. Apodex Discovery moves AI evaluation beyond predefined benchmarks toward verifiable investigations aimed at genuine discovery.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Mobile Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>Benchmarking LLM Judges for Mobile Agent Evaluation</strong>
          <small>Ziqiang Wan, Li Gu, Zhixiang Chi, Zhi Liu, Seyed Mehdi Ayyoubzadeh, Yuanhao Yu, Yang Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Mobile Agents</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">LLM-as-Judge</span>
<span class="topic-tag">Trajectory Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2608.11434</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11434">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 loosely: benchmark for evaluating LLM-as-judge methods on mobile agent trajectories, relevant to embodied agent evaluation rather than new agent methods.</p>
        <p class="abstract">Mobile agent benchmarks increasingly rely on LLM-based judges to evaluate task completion, yet the reliability of these judges on mobile agent trajectories remains largely unexamined. We introduce MobileJudgeBench, a benchmark for systematically evaluating LLM-as-judge methods on mobile agent trajectories. Our benchmark comprises 931 human-annotated trajectories spanning 6 mobile agent benchmarks, 4 agent models, and 68 apps. We evaluate 6 judge methods (five adapted from SPA-Bench, A3 with two modes, AndroidArena, and AgentRewardBench, plus a simple baseline we design) across multiple LLM backends. Our experiments reveal three key findings. First, a simple baseline judge with sampled screenshots is competitive with, and often exceeds, purpose-built methods, indicating that more elaborate judge pipelines do not consistently improve judge quality; among competitive methods, the LLM backbone is the primary driver. Second, benchmark quality metrics reliably predict real-world judge utility: they correlate with both agent ranking fidelity for evaluation and downstream performance when judges serve as reward signals for on-policy reinforcement learning. Third, failure analysis across two LLM backends uncovers qualitatively opposite failure profiles, one conservative and the other permissive, linked to the backbone&#x27;s precision-recall characteristics.</p>
      </div>
    </details>

      </div>
    </details>

    </details>


    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>18 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">MLLM</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>GeoBridge: Decoupled Semantic Conditioning for Generative Image Geolocalization</strong>
          <small>Zhiyang Dou, Xumeng Han, Fengde Peng, Zipeng Wang, Moxuan Zhao, Zhipei Huang, Zhenjun Han</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM</span>
<span class="topic-tag">Image Geolocalization</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Sphere Geometry</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2608.11838</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11838">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: a new MLLM-based generative geolocalization pipeline with a frozen semantic MLLM and geometry-aware decoding.</p>
        <p class="abstract">Multimodal large language models (MLLMs) have advanced image geolocalization mainly by improving how they reason about geographic cues. How that reasoning isdecoded into coordinates, however, has lagged behind. Predicting a place name for a geocoding API is discrete and lossy: it ignores image evidence and collapses multi-granular semantics into a coarse lookup. We argue that the bottleneck has shifted from what a model reasons to how that reasoning is represented for a continuous, geometry-aware decoder. We present GeoBridge, a role-decoupled conditioning mechanism that connects a frozen semantic MLLM to a frozen Riemannian flow-matching head that generates coordinates on the sphere. The central obstacle is arole conflict: supervising the condition with discrete semantic labels biases its representation toward class-discriminative geometry, at odds with the smooth manifold the generative head requires. GeoBridge keeps the semantic supervision decoupled from the condition interface: a separate projection forms the continuous condition the frozen head expects, injecting geographic priors without disturbing the spherical decoder. On IM2GPS3K, GeoBridge reaches 38.67/52.89/70.37 at the 25/200/750 km thresholds, improving over a place-name-to-API pipeline and reasoning-augmented direct prediction at these precision-relevant scales. GeoBridge is a decode-side algorithmic contribution, orthogonal and complementary to chain-of-thought reasoning. Code will be made publicly available.</p>
      </div>
    </details>


    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>Motion-as-Prompt: Enhancing Motion Reasoning in Multimodal Large Language Models via Motion-Guided Cross-Frame Visual Prompting</strong>
          <small>Xikai Sun, Kebin Liu, Haotian Wang, Li Liu, Xu Wang, Yunhao Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM</span>
<span class="topic-tag">Motion Reasoning</span>
<span class="topic-tag">Video Understanding</span>
<span class="topic-tag">Visual Prompting</span>
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
          <span>Paper 11 / arXiv:2608.11655</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11655">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and criterion 1: a new MLLM prompting method that improves motion reasoning in video understanding, especially for movement and interaction reasoning.</p>
        <p class="abstract">Motion-centric video reasoning is fundamental to interactive applications such as robotic manipulation and autonomous navigation. However, multimodal large language models (MLLMs) typically process videos through sparse uniform sampling to control visual-token and attention costs. This strategy may discard critical transitions between sampled frames, limiting reasoning about object movement, collisions, and causal interactions. To mitigate this issue, we propose Motion-as-Prompt (MaP), a track-guided cross-frame visual prompting framework. MaP recovers dense point trajectories, selects motion-informative frames, and marks the trajectories accumulated between consecutive sampled frames directly onto the visual inputs, making otherwise hidden displacement, direction changes, and interactions observable to frozen MLLMs. Experiments on CLEVRER and Something-Something-v2 show that MaP consistently improves average motion-reasoning accuracy, yielding gains of 4.2% and 8.9% for GPT-5.5, respectively. Notably, these improvements are obtained without degrading non-motion understanding, highlighting the robustness of MaP. These results demonstrate that MaP provides a simple and effective solution for enhancing motion-centric video reasoning without model training or architectural modification. Project page:https://github.com/SunVictor23/MaP.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation</strong>
          <small>Yan Deng, Fei Xu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Vision-Language Navigation</span>
<span class="topic-tag">Diffusion Planning</span>
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
          <span>Paper 4 / arXiv:2608.12308</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.12308">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied AI navigation method for aerial vision-language navigation with new memory, planning, and stop prediction components.</p>
        <p class="abstract">Aerial vision-language navigation (VLN) requires an embodied agent to integrate visual evidence over time, plan future actions, and determine when it has reached a navigation goal under partial observability. Although recent VLA models offer a promising perception-to-action paradigm, adapting them to aerial navigation remains challenging due to limited historical context, short planning horizons, and unreliable implicit termination. To address these challenges, we propose DreamFly, a diffusion-based aerial VLN framework built on Dream-VLA. DreamFly introduces a causally aligned historical memory that augments the current visual representation using only observations preceding the current decision step, enabling temporal reasoning without future information leakage. We further formulate navigation as receding-horizon diffusion planning, where the policy predicts a $K$-step action chunk but executes only the first action before replanning. This plan-$K$, execute-one strategy uses future actions as auxiliary planning targets while preserving closed-loop visual feedback. Finally, LiteStop estimates the stop probability directly from action logits at the initial all-mask state, decoupling explicit termination from action generation. Experiments on the OpenFly benchmark demonstrate consistent improvements in seen and unseen environments. DreamFly achieves 32.04%/29.46% SR and 28.22%/23.54% SPL on the test-seen/test-unseen splits, respectively, outperforming all compared methods on both metrics while attaining the lowest navigation error. These results demonstrate the effectiveness of jointly modeling historical context, future action structure, and explicit termination for aerial VLN.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>VOLA: Improving Open-World Driving by VLM-Based Semantic Attribute Prediction</strong>
          <small>Yuchen Zhang, Yuan Gao, Sebastian Schmidt, Johannes Betz</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Driving</span>
<span class="topic-tag">Spatial Understanding</span>
<span class="topic-tag">Vision-Language Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2608.11777</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11777">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: it proposes a new spatially dense, action-relevant representation for open-world driving using VLM image-token features, aimed at embodied driving intelligence.</p>
        <p class="abstract">Driving in the real world is open-world: a car may encounter a fallen mattress, a deer, or other objects outside its training data. Naming them is not enough. The system must know how to treat each region: can it drive over it, and how severe would a collision be? We therefore shift scene perception from category labels to dense action-relevant attributes, where each pixel is labeled by how it should affect motion rather than by object name. We instantiate this general formulation with two ordered attributes: 7-rank drivability and 5-rank vulnerability. We read Qwen3.5 image-token hidden states directly as a spatial semantic representation. A lightweight boundary-aware decoder then turns this coarse token grid into sharp full-resolution attribute maps. The whole process requires neither autoregressive text generation nor an external mask model such as SAM. We train on dense attribute labels built in CARLA and test transfer to real scenes and to novel obstacles never seen in training. We compare with vision-only segmenters trained on the same attributes and prompted VLM segmenters. Our model matches strong vision-only segmenters on familiar categories and improves transfer to real open-world anomalies, reaching 69.4% mean vulnerability-rank recall versus 57.1% for the best vision-only baseline and 53.9% for the best prompted VLM baseline. These results show that VLM image tokens provide useful semantic cues for transferring driving attributes to objects outside the training vocabulary.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LVLM Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>LookBack: Where and How to Score LVLM Responses via Visual Reference Usage</strong>
          <small>Beomsik Cho, Jinhyeong Kim, Dongseok Lee, Jaehyung Kim</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LVLM Evaluation</span>
<span class="topic-tag">Hallucination Detection</span>
<span class="topic-tag">Visual Grounding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2608.11847</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11847">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: a new training-free LVLM response scoring method that specifically measures visual reference usage in the model’s outputs.</p>
        <p class="abstract">Large Vision-Language Models (LVLMs) integrate visual perception with language generation, enabling responses that span image understanding and complex reasoning. However, LVLMs do not just inherit the text-level hallucinations; they also hallucinate against the image, producing fluent responses ungrounded in what they see. This makes LVLM response scoring inherently harder, and our diagnostics show that existing confidence-based metrics adopted from LLMs are insufficient for LVLMs. Specifically, removing the input image barely changes confidence-based selection, suggesting that output-space confidence primarily captures textual plausibility rather than agreement with the image. To address this gap, we propose LookBack, a training-free LVLM response scoring method that augments token likelihood with visual lookback score, a lightweight measure of how strongly each response token refers to image tokens. Across four benchmarks and three models, LookBack consistently improves Best-of-$N$ selection over existing baselines with negligible additional overhead.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Do You See What You Draw? A Semantic Closed-Loop Framework for Holistic Evaluation of Unified Multimodal Models</strong>
          <small>Hao Zhang, Jiaxin Qi, Zhijiang Tang, Jianqiang Huang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Evaluation</span>
<span class="topic-tag">Unified Multimodal Models</span>
<span class="topic-tag">Vision-Language Generation</span>
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
          <span>Paper 7 / arXiv:2608.11907</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11907">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: it introduces a new evaluation framework for unified multimodal models that combines understanding and generation in a closed loop.</p>
        <p class="abstract">As Large Vision-Language Models increasingly aim to integrate visual generation and understanding within a single parameter space, evaluating such structural unification in a cohesive manner remains a critical challenge. Current evaluation protocols predominantly treat generative and discriminative capabilities as separate tasks, leaving a gap in system-level evaluation for unified multimodal models (UMMs). In this work, we propose Self-Generative-Understanding (SGU), a novel, annotation-free evaluation framework that probes the integrated capabilities of unified models through a semantic closed-loop challenge. Without requiring new annotations, SGU leverages the dual understanding-and-generation abilities of UMMs by asking them to first perceive an image and produce a textual description, subsequently reconstruct a visual context based on that description, and finally perform reasoning over the self-generated output. This pipeline provides a zero-cost testbed that yields an integrated performance score specifically tailored for evaluating UMMs as unified systems. Extensive experiments show that even high-performing UMMs often struggle to reason over their own generated contexts, revealing limitations that are not captured by separate evaluations of understanding or generation alone. Our work provides a complementary holistic evaluation framework and offers a foundation for benchmarking the development of next-generation unified multimodal models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">MLLM Benchmark</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams</strong>
          <small>Weihao Bo, Shan Zhang, Yanpeng Sun, Jie Liu, Yongke Yao, Jinhao Du, Wei He, Kai Zou, Zechao Li, Jingdong Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">MLLM Benchmark</span>
<span class="topic-tag">Diagram Understanding</span>
<span class="topic-tag">Diagram-to-Code</span>
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
          <span>Paper 8 / arXiv:2608.12262</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.12262">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 closely: it is a new multi-modal benchmark for evaluating MLLMs on scientific diagram parsing, editing, and diagram QA.</p>
        <p class="abstract">Multimodal Large Language Models (MLLMs) have been growing the capability for scientific writing and collaboration. For example, OpenAI Prism is a free workspace for scientific writing and collaboration. One important feature in Prism is turning scientific diagrams directly into LaTeX TikZ code. In this paper, we build a benchmark, Diagram-MMU, a multi-modal benchmark designed to assess MLLMs&#x27; ability for scientific diagram parsing and understanding. Diagram-MMU features 3.7k curated diagrams and 18.3k human-validated questions across six domains. It evaluates MLLMs on three tasks common in vibe writing workspaces: diagram-to-code parsing, diagram-to-code editing, and diagram question answering, alongside agentic settings per task. The evaluation of 12 MLLMs reveals that diagram-to-code tasks are more challenging than diagram question answering: models can reason well over diagrams but struggle to parse and edit them, underscoring the need for methods to enhance MLLMs&#x27; capability in diagram-to-code generation. Under agentic settings, most models improve parsing and editing performance but degrade on question answering, while Claude-4.6 Opus consistently improves across all three tasks. Project Page: https://vi-ocean.github.io/projects/diagram-mmu.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Scene Understanding</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>STAR: A Spatial-Topology Aware Routing Framework for Generalizable 3D Scene Understanding</strong>
          <small>Mingwei Xing, Xinliang Wang, Yifeng Shi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Scene Understanding</span>
<span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Mixture-of-Experts</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2608.11699</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11699">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 closely: it introduces a spatial-topology aware framework for generalizable 3D scene understanding, explicitly targeting cross-domain spatial reasoning in 3D.</p>
        <p class="abstract">Constructing a unified 3D scene understanding model has long been hindered by the topological discrepancies across sensor modalities. While applying the Mixture-of-Experts (MoE) architecture is a flexible approach for multi-domain 3D understanding, we observe that conventional feature-only MoE routers may underrepresent local sampling topology under semantic supervision, making expert allocation difficult when semantic consistency coexists with geometric heterogeneity. To overcome this challenge, we propose STAR (Spatial-Topology Aware Routing Framework). Specifically, we introduce a multi-attribute self-supervised pre-training branch, covering topological and textural variations, to anchor cross-domain structural priors. Building upon this, we design a domain-aware expert branch with two mechanisms: Domain-Spatial-Guided Routing (DSR), which captures local topological variations from spatial context, and Entropy-controlled Dynamic Allocation (EDA), which adjusts the number of activated experts according to routing uncertainty. Together, these branches combine stable cross-domain representation learning with adaptive expert allocation. Extensive experiments across various tasks, encompassing both indoor and outdoor scenes, demonstrate the effectiveness of STAR. It achieves 80.1% mIoU on the ScanNet validation set and 77.2% mIoU on S3DIS, consistently improving over strong baselines. Code is available at our project page (https://xmw666.github.io/STAR/).</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Object Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs</strong>
          <small>Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bul\`o, Sunghwan Hong, Denis Rozumny, Johannes Sch\&quot;onberger, Zuria Bauer, Hermann Blum, Peter Kontschieder, Marc Pollefeys</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Object Detection</span>
<span class="topic-tag">Metric Reconstruction Priors</span>
<span class="topic-tag">Embodied Perception</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2608.12179</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.12179">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 closely: it proposes a new method for metric 3D reconstruction priors to improve online multi-view 3D object detection for embodied agents, with a clear spatial understanding angle.</p>
        <p class="abstract">Metric 3D object detection is a core capability for embodied agents, yet most reliable systems lean on depth sensors, trading away cost, power, and integration simplicity. This motivates monocular 3D detection, which avoids additional constraints, yet it faces a major obstacle: from a single image, depth, and especially absolute scale, are underconstrained. As a result, the prevailing pattern of detecting in 2D and then predicting 3D attributes is often brittle, since modest range errors can dominate 3D localization, and the learned scale prior can fail when cameras, motion, or environments undergo domain shifts. To address this, we propose Map-Det3D, an online multi-view 3D object detection model that brings detection directly into a 3D space reconstructed from RGB. We map a short temporal window into multiple views and repurpose a feed-forward metric 3D reconstruction model as our geometric backbone while tuning its object-aware capabilities. Building on this representation, Map-Det3D directly predicts boxes in metric 3D space, without the widely used 2D-to-3D lifting. Experiments across different benchmarks show that this design supports strong online performance and robust transfer without adaptation, suggesting that training reconstruction priors for detection is a practical route to stable metric 3D detection from monocular video. Code and models are available at https://royyang0714.github.io/Map-Det3D.</p>
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
          <strong>Repurposing RGB-based Foundation Model for Depth Estimation on Thermal Images Using Hierarchical Supervision</strong>
          <small>Jie Hong, Tingtian Li, Xuesong Li, Xiao Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Depth Estimation</span>
<span class="topic-tag">Thermal Imaging</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2608.11564</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11564">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it repurposes an RGB foundation model for thermal depth estimation using hierarchical supervision.</p>
        <p class="abstract">Depth estimation from thermal images is highly valuable for robotic applications in adverse conditions, such as nighttime and rainy weather. Recent studies have sought to transfer knowledge from RGB-based foundation models to thermal modalities, yet the rich hierarchical representations these models encode remain underutilized. To address this limitation, we propose RGB-HS, a novel framework for thermal-image depth estimation that leverages hierarchical supervision from an RGB-based foundation model. Specifically, we first replace the baseline thermal encoder with a foundational model and introduce a parallel RGB branch that also employs a foundational model as an encoder of the same architecture, taking RGB images as input. The alignment is then performed across multiple levels between the tokens of the two encoders, allowing the thermal student branch to capture both structural precision and semantic abstraction from the RGB teacher branch. Furthermore, we introduce verification to refine the alignment process by weighting tokens from the RGB branch based on RGB image quality. Extensive experiments on the popular benchmark demonstrate that RGB-HS achieves competitive performance and more effectively exploits the representational capacity of RGB-based foundation models for depth estimation on thermal images.</p>
      </div>
    </details>


    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Zero-OVCD: Bridging Training-Free Foundation Models and Pseudo-Label Learning for Open-Vocabulary Change Detection</strong>
          <small>Daifeng Peng, Yuanke Peng, Haiyan Guan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Open-Vocabulary Detection</span>
<span class="topic-tag">Remote Sensing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2608.11663</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11663">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it uses foundation-model-based pseudo-labeling for open-vocabulary change detection, a clear vision foundation model application.</p>
        <p class="abstract">Open-vocabulary change detection (OVCD) enables the identification of user-specified land-cover changes in bitemporal remote sensing images, but existing training-free pipelines remain vulnerable to inaccurate candidate masks, ambiguous semantic assignments, and accumulated inference errors. To address these issues, we propose Zero-OVCD, a two-stage framework that requires no pixel-level annotations from the target domain. In the first stage, high-quality change pseudo-labels are generated through complementary candidate-mask refinement, multiscale semantic similarity fusion with margin-based reliability filtering, and response-guided mask correction and completion. These components jointly suppress noisy candidates, enhance mask-level semantic discrimination, and recover missed change regions. In the second stage, a change detector is trained using the generated pseudo-labels, while checkpoint voting and high-agreement sample selection are introduced to mitigate residual pseudo-label noise. On LEVIR-CD, WHU-CD, and S2Looking, Stage I achieves F1 scores of 86.25%, 85.82%, and 50.48%, while Stage II further improves them to 88.65%, 88.85%, and 57.96%, respectively. On SECOND, the macro-average F1 across six category-wise one-vs-rest tasks increases from 47.91% to 50.92%. These results demonstrate that bridging training-free foundation-model inference with noise-aware pseudo-label learning provides an effective solution for open-vocabulary change detection without target-domain pixel-level annotations. Code will be available at https://github.com/1321663019/Zero-OVCD.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Driving World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>How Can Driving World Models Do Counterfactual Prediction?</strong>
          <small>Jiaru Zhang, Can Cui, Yi Xu, Xin Ye, Ruqi Zhang, Ziran Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Driving World Models</span>
<span class="topic-tag">Counterfactual Prediction</span>
<span class="topic-tag">Simulation Benchmark</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2608.11601</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11601">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 somewhat: it builds a controlled benchmark for counterfactual prediction in driving world models and exposes a failure mode in current approaches.</p>
        <p class="abstract">Driving world models are often interpreted as counterfactual simulators for observed driving episodes: given a factual driving log, they are asked what would have happened under an alternative ego action. In this paper, we identify a fundamental mismatch between this goal and direct action-conditioned prediction. The direct prediction uses the shared history and the alternative action but not the factual continuation observed after that history. It can therefore generate a plausible future without preserving what actually happened in this episode. We formalize this gap using the causal recipe of abduction, action, and prediction and study it in a setting with a short time horizon, where the alternative ego action does not alter how surrounding agents evolve. To make the gap measurable, we construct a controlled simulation benchmark with factual outcomes and matched counterfactual outcomes. Across two representative world models, direct predictions fail to match the counterfactual ground truth, supporting our analysis. As a constructive check of this analysis, we introduce a deliberately simple, training-free pipeline that moves observed evidence into the counterfactual view and lets the frozen model complete what remains unknown. Even this simple construction raises the overall recovered fraction substantially and reduces perceptual distance to the matched counterfactual on both models. We hope this work draws attention to this gap and motivates better counterfactual prediction methods for driving world models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Remote Sensing</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>Warping Earth Observations for better ice labeling in the Marginal Marginal Ice Zone</strong>
          <small>Tom Kelly, Martin S. J. Rogers</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Multimodal Alignment</span>
<span class="topic-tag">Segmentation Benchmark</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2608.11883</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11883">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it develops a multimodal satellite image alignment method and a sparse expert-labeled benchmark for dense segmentation under modality misalignment.</p>
        <p class="abstract">Multimodal satellite imagery provides complementary information for Earth Observation, but accurately combining heterogeneous sensors remains challenging in dynamic environments. Fast-changing regions, such as the Antarctic marginal ice zone, cannot fully exploit multimodal information from different satellite sensors because surface features move between image acquisitions. This spatial and temporal mismatch challenges effective perceptual grounding, violating the assumption of pixel-level correspondence that underpins most multimodal reasoning and downstream classification pipelines. Antarctic sea ice provides a challenging benchmark due to the rapid, heterogeneous drift of individual ice floes and the differing responses of sea ice to radar, visible and thermal sensing modalities. Accurate, dense supervision of sea ice remains scarce because generating pixel-wise labels requires time-consuming expert interpretation of noisy data, leading to historical reliance on coarse-resolution maritime ice charts for model training. This paper presents a novel architecture based on mutual information warping to align multi-satellite (Sentinel-1 and MODIS platforms) multimodal (visible, thermal, radar) satellite scenes. To demonstrate the approach, we introduce a sparse expert-labeled dataset of 2,088 pixel-wise annotations (7,046 expert point classifications) located at the ice-water margin interface across 43 scenes. Our results demonstrate that spatially grounding and aligning modalities prior to segmentation improves classification accuracy, and enables accurate, dense sea ice segmentation from sparse point-wise supervision.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors</strong>
          <small>Jiazheng Liu, Hang Li, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Shengyin Fan, Jin Zheng, Xiao Bai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Driving Scenes</span>
<span class="topic-tag">Flow Matching</span>
<span class="topic-tag">Geometric Priors</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2608.12203</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.12203">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately: vision foundation/generative modeling applied to driving video generation with geometry-aligned priors, though it is more a domain-specific generative method than a foundation model advance.</p>
        <p class="abstract">Generative models like Diffusion Models and Flow Matching have demonstrated remarkable capabilities in synthesizing high-fidelity driving videos, but are severely constrained by high inference latency due to the requirement of extensive sampling steps. We argue that this inefficiency stems from the prevailing reliance on a standard Gaussian source distribution, where consecutive frames are initialized as independent Gaussian noise. This paradigm disregards the rich spatiotemporal correlations inherent in driving videos, compelling the model to regenerate deterministic scene structures existing in previous frames from noise, which is both computationally redundant and prone to geometric inconsistency. To address this problem, we propose GeoFlow, a novel framework designed to achieve efficient driving video generation by harnessing explicit geometric priors. Instead of sampling from standard Gaussian noise, we leverage multi-view geometry and spatially-adaptive noise injection to construct a Geometry-Aligned Prior (GAP) distribution as starting point. This initialization bridges the gap between source distribution and data distribution, yielding a significantly straighter and shorter sampling trajectory. Extensive experiments demonstrate that GeoFlow can achieve remarkable efficiency of both training and inference: merely several hours of fine-tuning on baseline models can significantly boost few-step generation quality, while fully converged training drastically reduces number of inference steps required for state-of-the-art video generation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>Better Slots, Better Worlds: Representation Quality &amp; Robustness in Object-Centric World Models</strong>
          <small>Shukrullo Nazirjonov, Sai Prasanna, Anna Manasyan, Georg Martius</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Object-Centric Representation</span>
<span class="topic-tag">Robustness</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2608.12078</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.12078">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 somewhat and criterion 4 indirectly: it studies object-centric world models for visual planning, robustness, and the role of pretrained features in scene understanding.</p>
        <p class="abstract">Learning world models from offline trajectories enables agents to accomplish different tasks through planning. Object-centric (OC) representations, which decompose a scene into a set of slots that bind to its objects, have been proposed as an inductive bias for world models that are more sample-efficient and generalize better. Yet prior object-centric world models (OCWMs) take the slot encoder as given and evaluate only in-distribution, leaving open whether the object-centric bias actually delivers for planning and what within the OCWM drives it. We conduct a controlled study of OCWMs for visual model-predictive control along two axes: object-centric representation quality and generalization under distribution shift relative to scene-centric models. We find that (i) planning success correlates positively with unsupervised slot-quality metrics (FG-ARI, mBO), though the gains saturate at high slot quality; (ii) with well-bound slots, the auxiliary proprioception inputs and masking inductive bias that prior methods relied on become unnecessary; and (iii) under unseen distribution shifts, the OCWM with well-bound slots is more robust overall than the end-to-end trained scene-centric LeWM, while DINO-WM, built on similar frozen pretrained features, remains competitive -- pointing to pretrained features as a key contributor to robustness.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Fusion</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>EGM-Det: Entropy-Guided Multimodal Adaptive Fusion for UAV RGB-IR Object Detection</strong>
          <small>Cunzheng Fan, Dawei Yan, Guanlin Wang, Xingshuo Yang, Yupeng Jia, Jing Yang, Haokui Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Fusion</span>
<span class="topic-tag">UAV Perception</span>
<span class="topic-tag">RGB-IR Detection</span>
<span class="topic-tag">Adaptive Attention</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2608.11685</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11685">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 moderately: methodological improvement for spatially varying multimodal fusion in UAV RGB-IR perception, which is spatial understanding for embodied/robotic sensing but not a direct embodied-agent paper.</p>
        <p class="abstract">Joint use of RGB and infrared (IR) imagery can improve UAV-view object detection, but most existing methods fuse multimodal features with static or fixed weights and therefore overlook spatially varying modality reliability. We propose EGM-Det, an entropy-guided multimodal adaptive fusion framework for RGB-IR object detection. EGM-Det employs a dual-stream architecture to preserve modality-specific representations and introduces an Entropy Offset Gate Fusion module for adaptive multi-scale fusion. The module derives shallow entropy priors from input intensity, local entropy, and cross-modal discrepancy, and uses them to guide local offset alignment and spatial-channel gated fusion. It therefore selectively aggregates reliable RGB and infrared cues instead of uniformly combining heterogeneous features. We further introduce cross-modal distillation to regularize the learned fusion gates and reduce fusion degradation. Each student branch extracts complementary knowledge from the cross-modality teacher branch matched to the main branch, while entropy-adaptive supervision emphasizes uncertain modality decisions. Experiments on DroneVehicle, LLVIP, and VEDAI demonstrate state-of-the-art performance across all three benchmarks; in particular, EGM-Det outperforms prior approaches by more than 10 percentage points on VEDAI.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Generative Video Compression</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>Generative Video Compression Based on Hierarchical Referencing</strong>
          <small>Daowen Li, Ding Ding, Zifu Zhang, Kai Li, Ying Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Generative Video Compression</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Video Representation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 20 / arXiv:2608.11618</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11618">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: diffusion-based generative video compression is a vision/generative-model application, though not a core foundation-model paper.</p>
        <p class="abstract">Diffusion-based generative video compression has emerged as a promising paradigm to improve perceptual quality, where latent frames are required to be encoded efficiently while serving as denoising conditions. However, existing methods neither carefully design reference and quality structures during latent coding nor account for the impact of frame-level quality variation on denoising procedure, which limits coding efficiency and aggravates artifact propagation during generative reconstruction. In this paper, we propose GVCHR, Generative Video Compression based on Hierarchical Referencing. The key idea is to organize latent frames hierarchically, where the selected high-quality references benefit both latent coding and generative reconstruction. In latent coding, GVCHR couples a hierarchical reference structure with a hierarchical quality structure, assigning more bits to lower-layer frames that are reused more frequently as references. Built on this design, we introduce Hierarchical Temporal Context Mining to exploits complementary short- and long-term temporal context for effective latent coding. In generative reconstruction, the coding-side hierarchy is incorporated into a Hierarchical Attentive Adapter which is attached to a video diffusion transformer. This adapter uses hierarchical attention to restrict each latent frame to attend only to the same- or lower-layer references, thereby reducing artifact propagation during denoising. Experiments validate GVCHR on multiple benchmarks. Compared with the previous state-of-the-art method, GVCHR achieves 50.5% and 54.0% BD-rate gains in terms of LPIPS and DISTS, respectively, while also delivering clearly improved visual quality.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Text-to-Image</summary>
      <div class="queue">

    <details class="paper-row" id="link20">
      <summary class="paper-row-summary">
        <span class="queue-index">21</span>
        <span class="paper-row-copy">
          <strong>TangPoetryBench: A Multi-Dimensional Benchmark and Rubric-Conditioned Evaluator for Poetry-to-Image Generation</strong>
          <small>Haoqi Hu, Tongji Luo, Li Zhang, Boning Zhou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Image</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multimodal Evaluation</span>
<span class="topic-tag">Cultural Generation</span>
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
          <span>Paper 21 / arXiv:2608.11452</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11452">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: vision foundation model application in text-to-image generation and evaluation, but centered on a literary benchmark rather than a foundation-model method.</p>
        <p class="abstract">Text-to-image (T2I) models are increasingly asked to illustrate literary and cultural content, yet we cannot measure how well an image renders the meaning of a poem. The task is many-sided: a good illustration must be visually sound, faithful to the poem&#x27;s imagery and scene, culturally and stylistically apt, free of spurious text, and true to its emotion, and its deepest requirements, imagery and especially implicit emotion, are never stated in the words. Existing metrics (CLIPScore, BLIPScore, VQAScore) reward literal text-image correspondence and so cannot tell whether an illustration succeeds, let alone why, or even separate the best model from the worst. We introduce TangPoetryBench, a multi-dimensional benchmark of 1,280 images (320 classical Chinese Tang poems x 4 state-of-the-art T2I models) with quality-controlled human annotations across ten dimensions. Analyzing this data, we reveal the shared and model-specific strengths and weaknesses of current T2I models, including their ability to evoke a poem&#x27;s implicit emotion. We further introduce PoemAutoEvaluator (PAE), an open, rubric-conditioned evaluator that reaches parity with a strong proprietary judge (Claude), generalizes to an unseen generator and a second poetic tradition (Song Ci), and lets the benchmark scale to new images without fresh human annotation. We release the benchmark, annotations, and evaluator.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
