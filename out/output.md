

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
      <p class="eyebrow">Daily ArXiv / June 24, 2026</p>
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
      <strong>10.3</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">answer</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">attention</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="6 mentions">boundary</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="8 mentions">city</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">consistent</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">detection</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">driving</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="6 mentions">dynamic</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="6 mentions">edit</span><span class="cloud-word" style="font-size:2.03rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 62%, var(--accent))" title="10 mentions">evidence</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">foundation</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="7 mentions">frame</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">garment</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">generation</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="7 mentions">geometric</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="7 mentions">geometry</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">grounding</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="6 mentions">language</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">mesh</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">motion</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">multimodal</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">neuenahrflood</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">object</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">paired</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">patterngsl</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">pipeline</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">pretrained</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">realistic</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="6 mentions">reasoning</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">reconstruction</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">rgb-d</span><span class="cloud-word" style="font-size:1.68rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="8 mentions">scene</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="6 mentions">semantic</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">sewing</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="6 mentions">spatial</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="4 mentions">structured</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">target</span><span class="cloud-word" style="font-size:2.03rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 62%, var(--accent))" title="10 mentions">temporal</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 34%, var(--accent))" title="7 mentions">token</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">understanding</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">unidrive</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">unified</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="15 mentions">video</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="6 mentions">visual</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="5 mentions">water</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="87 mentions">action</span><span class="cloud-word" style="font-size:2.26rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 74%, var(--accent))" title="278 mentions">agent</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="77 mentions">alignment</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="70 mentions">architecture</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="89 mentions">attention</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="72 mentions">consistency</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="68 mentions">control</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="82 mentions">detection</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="81 mentions">diffusion</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="89 mentions">domain</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="69 mentions">driving</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="110 mentions">dynamic</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="154 mentions">evidence</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="81 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="71 mentions">foundation</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">frame</span><span class="cloud-word" style="font-size:1.84rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="201 mentions">generation</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="77 mentions">geometry</span><span class="cloud-word" style="font-size:1.12rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="100 mentions">inference</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="101 mentions">interaction</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="82 mentions">knowledge</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="160 mentions">language</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">latent</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="90 mentions">mechanism</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 38%, var(--accent))" title="159 mentions">memory</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="81 mentions">mllm</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="83 mentions">motion</span><span class="cloud-word" style="font-size:1.71rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="180 mentions">multimodal</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="78 mentions">multiple</span><span class="cloud-word" style="font-size:1.38rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="133 mentions">object</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="83 mentions">optimization</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="75 mentions">paradigm</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="79 mentions">pipeline</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="72 mentions">point</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="82 mentions">policy</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="72 mentions">question</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="77 mentions">real-world</span><span class="cloud-word" style="font-size:2.59rem;opacity:0.95;color:color-mix(in srgb, var(--accent-2) 91%, var(--accent))" title="345 mentions">reasoning</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="68 mentions">region</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="78 mentions">retrieval</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="72 mentions">reward</span><span class="cloud-word" style="font-size:1.53rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 37%, var(--accent))" title="154 mentions">scene</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="73 mentions">search</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="171 mentions">semantic</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="96 mentions">skill</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="77 mentions">space</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="143 mentions">spatial</span><span class="cloud-word" style="font-size:0.91rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="77 mentions">structure</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="76 mentions">supervision</span><span class="cloud-word" style="font-size:1.01rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="88 mentions">target</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="125 mentions">temporal</span><span class="cloud-word" style="font-size:1.65rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="171 mentions">token</span><span class="cloud-word" style="font-size:1.16rem;opacity:0.59;color:color-mix(in srgb, var(--accent-2) 18%, var(--accent))" title="105 mentions">trajectory</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 20%, var(--accent))" title="110 mentions">understanding</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="73 mentions">unified</span><span class="cloud-word" style="font-size:2.35rem;opacity:0.89;color:color-mix(in srgb, var(--accent-2) 78%, var(--accent))" title="295 mentions">video</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="75 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="385 mentions">visual</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="68 mentions">world</span></div>
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
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving</strong>
          <small>Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth, Stephen Law, Yun Ye</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Grounded Vision-Language</span>
<span class="topic-tag">Spatial Reasoning</span>
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
          <span>Paper 1 / arXiv:2606.24759</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24759">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and criterion 3 closely: it is a grounded multimodal framework for autonomous driving that combines temporal reasoning with precise spatial evidence.</p>
        <p class="abstract">Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and spatial precision. Models that rely on single-frame or low-resolution inputs often miss small, distant, or partially occluded hazards, while language-centric driving models frequently provide limited grounded evidence for their explanations. To address this gap, we propose UniDrive, a unified visual-language and grounding framework for interpretable risk understanding in autonomous driving. UniDrive combines a temporal reasoning branch that models scene dynamics from multi-frame visual input with a high-resolution perception branch that preserves fine-grained spatial details from the latest frame. The two branches are integrated through a gated cross-attention fusion module, enabling dynamic context to be aligned with precise spatial evidence. Based on the fused representation, UniDrive jointly generates natural-language risk descriptions and grounded bounding-box outputs for risk objects. Experiments on the DRAMA-Reasoning benchmark show that UniDrive outperforms representative image-based and video-based baselines in both captioning and risk-object grounding. In particular, UniDrive achieves the best overall performance on the validation split and demonstrates clear advantages in small-object localization, zero-shot generalization to NuScenes and BDD100K, and human-rated interpretability and trustworthiness. These results suggest that explicitly combining temporal semantics and high-resolution perception provides a stronger foundation for interpretable and safety-oriented autonomous driving systems. The code is available at https://github.com/pixeli99/unidrive-dev.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>PatternGSL: A Structured Specification Language for Template-Free and Simulation-Ready 3D Garments</strong>
          <small>Zhenyang Li, Lutao Jiang, Yizhou Zhao, Ying-Cong Chen, Xin Wang, Weikai Chen, Yifan Peng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Modeling</span>
<span class="topic-tag">3D Garments</span>
<span class="topic-tag">Simulation-Ready Representation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2606.24564</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24564">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 and also criterion 2 somewhat closely: it proposes a new simulation-ready structured garment representation and a VLM pipeline for predicting it.</p>
        <p class="abstract">Reconstructing realistic, physically plausible garments from a single image remains a fundamental challenge. Template-free methods capture surface geometry but lack explicit sewing structure for simulation; while programmatic systems are simulation-ready but constrained by predefined templates. This reveals a fundamental representation gap between geometric reconstruction and structured garment construction. We present PatternGSL, a structured garment representation in the form of a template-free and learnable specification language that encodes complete sewing patterns, including panel boundaries, parameterized seams, and explicit stitch topology, in a compact and standardized form. PatternGSL preserves the physical rigor of pattern-based models while removing template dependence, elevating sewing structure as a first-class target for generative modeling. We further propose a vision-language framework that predicts PatternGSL specifications directly from a single image and decodes them into garments using lightweight deterministic validity handling, without optimization-based refinement or manual cleanup. In addition, we introduce PatternGSLData, the first large-scale image-to-GSL paired dataset comprising 300K samples with complete sewing pattern annotations, enabling supervised VLM training for structured garment reconstruction. Experiments demonstrate improved pattern accuracy over prior baselines, explicit sewing-structure recovery, reliable cloth simulation, and pattern-level editing through the same deterministic decoding pipeline. Code and data-processing scripts will be released at https://github.com/PatternGSL/PatternGSL.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>Sat2City v2: Native 3D City Asset Generation from a Single Satellite Image</strong>
          <small>Tongyan Hua, Dongli Wu, Jinjing Zhu, Yinrui Ren, Zhongcheng Hong, Ying-Cong Chen, Hui Xiong, Wufan Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Generation</span>
<span class="topic-tag">Geospatial AI</span>
<span class="topic-tag">Foundation Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2606.24138</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24138">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criteria 3 and 4 closely: it builds a new satellite-mesh paired dataset and proposes a 3D city asset generation method from satellite imagery, with a foundation-model angle.</p>
        <p class="abstract">Generating explicit 3D city assets from a single satellite image is important for digital twins, urban simulation, and geospatial intelligence. Unlike satellite-to-street-view synthesis, the task requires a reusable textured mesh with plausible geometry and controllable appearance rather than a 3D proxy optimized only for rendering a small set of images or videos. The ICCV Sat2City framework made a first step by conditioning cascaded sparse-voxel latent diffusion on satellite-derived height maps, but its appearance was random, its training data were synthetic, and its task-specific VAE did not scale well to noisy real-world reconstructions. We present Sat2City v2, a journal extension that adapts a pretrained native structured-latent 3D foundation model to weakly aligned satellite images and textured meshes. We build a real-world dataset with 16,241 satellite-mesh pairs across 24 regions in 9 cities. Instead of learning a 3D representation from noisy city meshes, Sat2City v2 encodes each mesh into a pretrained native 3D latent space, fine-tunes a satellite-conditioned geometry flow, and uses the decoded shape to anchor satellite-conditioned texturing. This retains Sat2City&#x27;s geometry-to-appearance cascade while enabling appearance-controllable generation from the satellite input. Experiments on metric-scale DSM reconstruction and generative city-asset benchmarks for geometry and appearance show that Sat2City v2 achieves the best overall performance among evaluated baselines. Overall, Sat2City v2 advances satellite-to-city generation from rendering-oriented 3D proxies to explicit textured mesh assets, supported by, to the best of our knowledge, the first documented satellite-mesh paired dataset collected from matched geographic crops for this asset-level task. Project page: https://ai4city-hkust.github.io/Sat2City-v2/</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video LLM</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>video-SALMONN-R$^3$: Learning to ReWatch, ReAsk, and ReAnswer for Efficient Video Understanding</strong>
          <small>Yixuan Li, Guangzhi Sun, Yudong Yang, Wei Li, Zejun MA, Chao Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video LLM</span>
<span class="topic-tag">Efficient Inference</span>
<span class="topic-tag">Reinforcement Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.SD</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2606.24477</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24477">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a new method for efficient video understanding in video-LLMs using re-watch/re-ask/re-answer, with a novel training strategy.</p>
        <p class="abstract">Video large language models (LLMs) are often constrained by computation and memory budgets, leading them to use reduced frame rates and spatial resolutions, which may cause them to miss critical information for question answering (QA). A practical and efficient solution is a two-stage paradigm: first perform coarse video understanding to localize relevant segments, and then re-watch these segments at higher temporal or spatial fidelity. In this paper, we present video-SALMONN-R$^3$, the first end-to-end video-LLM that enables re-watch through reinforcement learning without relying on chain-of-thought (CoT) cold-start. This design removes the need for costly CoT data annotations and avoids CoT-based supervised fine-tuning (SFT), which can otherwise degrade the pretrained video understanding abilities. To address the mismatch between the reasoning-first behavior induced by re-watch and the answer-first tendency of pretrained video-LLMs, we propose a re-answer strategy, in which the model first produces a direct answer in the first watch and then refines it after re-watching. Finally, to improve question adherence during re-watching, we propose a re-ask mechanism that re-injects the query when revisiting localized segments. Experimental results show that video-SALMONN-R$^3$ consistently outperforms both the base model and the QA-SFT baseline, while surpassing prior re-watch-based approaches with significantly lower computational cost. Code, models, and data will be publicly released upon acceptance.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video MLLM</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>SER: Learning to Ground Video Reasoning with Semantic Evidence Rewards</strong>
          <small>Sheng Xia, Zhengqin Lai, Tianxiang Jiang, Kanghui Tian, Shoujun Zhou, Bin Li, Yi Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video MLLM</span>
<span class="topic-tag">Evidence Grounding</span>
<span class="topic-tag">Reinforcement Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2606.24726</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24726">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied/video reasoning method that improves spatio-temporal evidence grounding with a new reward design for video MLLMs.</p>
        <p class="abstract">Video MLLMs often struggle with fine-grained spatio-temporal reasoning, sometimes generating correct answers based on irrelevant frames or objects. Although outputting spatio-temporal evidence during reasoning is a promising direction, existing RL frameworks typically rely on geometry-only (IoU) rewards, which can be sensitive to boundary perturbations and overlook semantic alignment. To address this, we propose Semantic Evidence Reward (SER), which reformulates spatio-temporal evidence grounding as a constrained verification task. Instead of computing pixel-level overlap, SER uses a referee VLM as a local checker to evaluate model-generated evidence claims across two dimensions: relevance and localization quality, combined with a temporal penalty. This design reduces the reliance on dense box annotations and enables training directly on standard video QA data. On the V-STAR benchmark, SER achieves 49.6% mLGM, improving by 3.0 points over the strong evidence-grounded baseline Open-o3-Video, demonstrating its potential in enhancing both answer accuracy and evidence grounding.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>Advancing WordArt-Oriented Scene Text Recognition: Datasets and Methods</strong>
          <small>Xingsong Ye, Yongkun Du, Jiaxin Zhang, Haojie Zhang, Chong Sun, Chen Li, Jing Lyu, Zhineng Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Scene Text Recognition</span>
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
          <span>Paper 6 / arXiv:2606.24484</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24484">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and criterion 4 closely: it introduces a new vision-language method and large-scale synthetic dataset for WordArt-oriented text recognition.</p>
        <p class="abstract">WordArt (artistic text) features highly customized fonts, textures, and layouts, making WordArt-oriented scene TExt Recognition (WATER) substantially more challenging than general Scene Text Recognition (STR). Existing STR datasets and methods, typically built around regular scene text and fixed-template inputs, struggle to scale to WATER. Thus, we aim to advance this task from both data and model perspectives. On the data side, we construct a 2M synthetic dataset, WATER-S, with the scale improved by hundreds of times compared to existing artistic text data. WATER-S consists of two complementary subsets. One rendered by an upgraded rendering pipeline (SynthWordArt), which provides highly accurate and controllable synthetic WordArt data. The other is generated by combining Qwen3-VL for prompt mining and Z-Image for image synthesis, which improves the coverage of realistic and diverse data. On the model side, we propose WATERec. It adopts an visual encoder supporting arbitrary-shaped inputs and an autoregressive decoder to model complex layouts, structurally breaking the bottleneck of fixed-template STR on WordArt. Experiments show that this architecture outperforms prior STR methods, achieving state-of-the-art performance on irregular texts such as WordArt. Together with WATER-R, carefully reorganized from existing real STR data, our strong baseline with the new synthetic data and model design reaches 90.40% accuracy on WordArt-Bench, surpassing both general-purpose and OCR-specialized vision-language models by a large margin. Code and data are available at https://github.com/YesianRohn/WATER.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Visual Tracking</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>SENTRY: SAM2-Enhanced Neighbor-Aware and Temporally Reasoned Memory for Visual Tracking</strong>
          <small>Mohamad Alansari, Yonathan Michael, Hasan AlMarzouqi, Muzammal Naseer, Naoufel Werghi, Sajid Javed</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Visual Tracking</span>
<span class="topic-tag">Temporal Reasoning</span>
<span class="topic-tag">Memory Modules</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2606.24449</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24449">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 closely: it improves memory update and temporal reasoning for visual object tracking, which is a spatial understanding problem for embodied/interactive perception.</p>
        <p class="abstract">We revisit the memory update mechanism in SAM2-based visual object tracking and identify confidence-only mask selection as the dominant cause of drift under occlusion, rapid motion, and distractors. We introduce SENTRY, a training-free, plug-and-play, refine-before-write module that validates each memory update for short-horizon temporal consistency before committing it. SENTRY aggregates diverse segmentation hypotheses per frame, backtracks them into short tracklets, and uses neighbor-aware cycle-consistent matching against recent trajectories to favor temporally and geometrically consistent masks. It leaves the base architecture untouched, replacing confidence-driven writes with consistency-validated ones. For fair evaluation, we re-evaluate major open-source SAM2-based trackers across all available scales and datasets, filling gaps in prior reports. Integrated into five strong baselines, SENTRY delivers consistent gains across nine benchmarks, achieving new zero-shot SOTA on LaSOT, LaSOT_ext, GOT-10k, VOT20, VOT22, and DiDi. Despite these checks, the SAM2-L version runs at 32.8 FPS on an A100, and across compatible hosts adds only about 0.4--0.6 GB VRAM. Our results provide the first unified all-scale evaluation of SAM2-based trackers and show that enforcing temporal validity at write time stabilizes memory-augmented tracking without retraining.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">VLM Forensics</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Revealing Training Data Exposure in Vision Language Large Models via Parameter Gradients</strong>
          <small>Zhihao Zhu, Hongyi Tang, Yi Yang, Ahmed Abbasi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">VLM Forensics</span>
<span class="topic-tag">Data Provenance</span>
<span class="topic-tag">Model Auditing</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2606.24774</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24774">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is a training-data auditing/forensics paper for VLLMs, relevant to VLMs but not a new model or embodied/spatial method.</p>
        <p class="abstract">Vision-Language Large Models (VLLMs) trained on massive crawled corpora raise pressing copyright and data-provenance concerns. These concerns are particularly acute in healthcare, where patient medical images paired with clinical reports demand rigorous privacy safeguards. However, existing training data detection methods either fail in cross-modal scenarios or rely on superficial output signals with insufficient discriminative power. We introduce GradAudit, a gradient-based auditing framework that examines internal optimization dynamics rather than treating VLLMs as black boxes. Our approach builds on a key observation: model parameters converge to regions where gradients on training samples become stable and well-aligned, whereas gradients on non-training samples remain noisy and inconsistent. By analyzing these gradient signatures, GradAudit achieves strong separability and detects genuine image-text associations learned during training, not merely individual modality membership. Empirically, across both medical and general-domain datasets, GradAudit substantially outperforms state-of-the-art baselines in both pretraining and fine-tuning VLLMs. In a case study employing copyrighted content, we show that existing training data detection methods not only underestimate the extent of unauthorized data usage, but that this underestimation becomes more pronounced as models become more recent and more advanced.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Model</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>Flood Mapping from RGB imagery using a Vision Foundation Model</strong>
          <small>Vladyslav Polushko, Tilman Bucher, Ronald R\&quot;osch, Thomas M\&quot;arz, Markus Rauhut, Andreas Weinmann</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Model</span>
<span class="topic-tag">Remote Sensing</span>
<span class="topic-tag">Flood Segmentation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">eess.IV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2606.24120</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24120">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it adapts a vision foundation model for flood mapping from RGB imagery and studies transfer/generalization across flood events.</p>
        <p class="abstract">Timely, high-resolution maps of flood extent around settlements are essential for emergency response and damage assessment. We consider airborne RGB imagery for flood mapping as it can be collected rapidly at low cost. To produce flood maps, deep learning models for water segmentation are often used. CNN based and small vision transformer models are used. However, they need much data for adaptation to a change of scenery, i.e., another flooding event. Vision foundation models or large vision transformers are known to generalize across domains. Recently, foundation models for Earth observation became available. They are pretrained on satellite data, whose spatial resolution, viewing geometry, and radiometry differ from nadir RGB imagery. Thus, adaptation is required. We investigate how a satellite-pretrained Earth observation foundation model can be adapted to centimeter-scale floodwater mapping from RGB imagery. Specifically, we fine-tune a model we call Prithvi-2.0-UPN consisting of the Prithvi-EO-2.0-600M Vision Transformer combined with a UPerNet decoder for binary water segmentation on two RGB datasets (BlessemFlood21, NeuenahrFlood). In a first experiment we observe that Prithvi-2.0-UPN reaches state-of-the-art results on BlessemFlood21 and NeuenahrFlood, when trained on their datasets. In a second experiment we show that Prithvi-2.0-UPN performs better than state-of-the-art baseline models for transfer to a new flood event (trained on BlessemFlood21, tested on NeuenahrFlood) in a zero-shot setting. However, the performance indicates room for improvement. In this respect, we investigate in a third experiment how performance improves when further fine-tuning the models with small shares of NeuenahrFlood training data: Prithvi-2.0-UPN improves the fastest and reaches almost the performance level when fully trained on NeuenahrFlood, indicating transfer capabilities.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Interpolation</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>UniRED: Unified RGB-D Video Frame Interpolation with Event Guidance</strong>
          <small>Yinuo Zhang, Guangshun Wei, Yuanfeng Zhou, Yiran Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Interpolation</span>
<span class="topic-tag">RGB-D</span>
<span class="topic-tag">Event Cameras</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2606.24282</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24282">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; it is a multimodal video interpolation method with a new RGB-D-Event dataset, which is adjacent to vision foundations but not a direct fit.</p>
        <p class="abstract">High frame-rate RGB-D videos are crucial for a variety of downstream tasks, including motion analysis, dynamic scene understanding, and 3D reconstruction. However, due to hardware and sensing constraints, practical RGB-D cameras are typically limited to low frame rates, making it difficult to capture rapid scene dynamics. Existing video interpolation methods have achieved strong performance on RGB data, but they are not readily applicable to RGB-D scenarios, where they often yield blurry boundaries, visible artifacts, and degraded geometric consistency. Furthermore, motion estimation from only two boundary frames is inherently under-constrained in complex dynamic scenes. Event cameras, by contrast, provide asynchronous measurements with ultra-high temporal resolution, offering dense motion cues. In this paper, we propose a unified multimodal framework for RGB-D video interpolation that jointly exploits RGB appearance, depth geometry, and event-based temporal cues. Specifically, it first extracts and fuses RGB, depth and event cues, then estimates bidirectional flow with motion basis refinement for RGB and Z-axial refinement for depth, and finally synthesizes the target RGB-D frame via bidirectional warping and soft blending. In addition, we construct a new RGB-D-Event dataset to alleviate the scarcity of tri-modal training data. Extensive experiments on a public benchmark and the proposed dataset demonstrate that our method achieves superior photometric fidelity for RGB interpolation and stronger geometric accuracy for depth interpolation than existing approaches.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Listening makes Vision Clear for VLMs</strong>
          <small>Yiyang Chen, Yixin Tan, Binrui Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Interpretability</span>
<span class="topic-tag">Attention Analysis</span>
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
          <span>Paper 13 / arXiv:2606.23763</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.23763">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 weakly: it studies VLM attention/activation maps and introduces a consistency evaluation method, but it is not a new VLLM/MLLM model.</p>
        <p class="abstract">Recent work typically assesses vision--language consistency using attention distributions of answer-side tokens. However, we observe that highest attention regions are not always consistent with the intended semantic token. This probably stems from decoding drift, where language priors from previously generated answer tokens accumulate and mismatch with visual attention. Besides the priors from previous answer tokens, we find that structural tokens, e.g., modality boundary markers, may encompass the entire context and generate high attention to areas unrelated to the target. To avoid these distortions and provide consistency evaluation for large VLMs, we adopt prompt-side semantics and propose Prompt-Vision Token Activation Map (PV-TAM). PV-TAM further incorporates a filter to remove systematic bias induced by modality boundary markers. Unlike traditional methods that evaluate overlap solely through masks while ignoring activation intensity, our metrics leverage the peak distribution of attention to measure the alignment between prompts and visual regions. In experiments, PV-TAM consistently improves both attention-based and IoU-style localization metrics over answer-side baselines on various datasets.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Editing</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Geometry-Instructed Video Editing</strong>
          <small>Chirui Chang, Xiaoyang Lyu, Yi-Hua Huang, Haoru Tan, Shizhen Zhao, Yikang Ding, Jianmin Bao, Xin Tao, Pengfei Wan, Xiaojuan Qi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Editing</span>
<span class="topic-tag">Geometry Conditioning</span>
<span class="topic-tag">Generative Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2606.24225</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24225">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 loosely: it is a new method for geometry-aware video editing, but it is not an embodied AI benchmark/simulator paper and not a VLLM/MLLM paper.</p>
        <p class="abstract">Object-level geometric edits, including translating, rotating, scaling, duplicating, or removing an object, are routine operations in digital content creation (DCC) workflows, yet they remain unreliable in generative video editing. The key challenge lies in specifying the target object&#x27;s 3D state change unambiguously across viewpoint and time, while consistently updating geometry-dependent secondary effects such as shadows and reflections. We introduce GIVE, a geometry-instructed video editing framework that represents edits through a unified object-state formulation. Two video-aligned geometry streams describe the target object before and after editing: a depth-box encoding coarse 3D placement and extent, and an orientation-box providing an appearance-agnostic orientation cue. Together, these streams provide a compact pre/post geometric specification for object-state transitions. To provide paired supervision for learning these edits, we build a scalable graphics-engine pipeline that executes object-level edit programs and renders controlled before/after pairs, isolating the intended geometric edit while keeping secondary effects consistent with the transformation. Experimental results demonstrate that GIVE produces faithful geometric edits with temporal coherence and consistent secondary effects across operators in a unified framework, and shows promising transfer to in-the-wild videos. Project page: https://geometry-instructed-video-editing.github.io/give/</p>
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
      <summary class="topic-heading">Multimodal Verification</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal Misinformation Detection</strong>
          <small>Chenhao Dang, Dantong Zhu, Jun Yang, Conghui He, Weijia Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Verification</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Agentic Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2606.24112</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24112">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 loosely: it introduces a new multimodal misinformation benchmark and an agentic verifier, but it is not embodied AI or a vision foundation model paper.</p>
        <p class="abstract">Multimodal misinformation detection is increasingly important because viral posts now combine long multilingual narratives, several images, mixed provenance, and subtle text--image framing errors. Existing benchmarks and methods remain poorly matched to this setting: they usually isolate short captions, single images, binary labels, or one manipulation source, while agentic verification remains costly under realistic evidence search. We present ReMMD, a realistic multilingual multi-image agentic verification framework for multimodal misinformation detection. ReMMD includes ReMMDBench, a real-world multimodal misinformation detection benchmark with 500 samples, 2,756 images, five monolingual languages, two cross-lingual settings, three text-length tiers, multi-image posts, five-way veracity labels, eight distortion labels, evidence provenance, and rationales. It also includes ReMMD-Agent, a persistent-memory verifier that decomposes posts into atomic points, builds a reusable evidence set, and predicts structured L1/L2/L3 outputs. Across proprietary systems, open LVLMs, MMD-Agent, and T2-Agent, ReMMD-Agent obtains the best five-way veracity performance, with 41.80% accuracy and 39.12% macro-F1 using GPT-5.2, while reducing cost by 17.5% relative to MMD-Agent and 79.9% relative to T2-Agent. The project is available at https://dang-ai.github.io/ReMMD.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Personalized Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Navigating User Behavior toward Personalized Multimodal Generation</strong>
          <small>Hengji Zhou, Yufeng Liu, Ye Liu, Yong Xu, Lianghao Xia, Liqiang Nie</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Personalized Generation</span>
<span class="topic-tag">Multimodal Learning</span>
<span class="topic-tag">Recommendation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2606.24196</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.24196">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to criteria 1-4; this is about personalized multimodal generation from user behavior, which is related to generative multimodal learning but not one of the specified focuses.</p>
        <p class="abstract">Modern AIGC pipelines deliver high-fidelity images and videos but presuppose a well-formed creation instruction, while end users rarely articulate visual details, leaving generators misaligned with user demand. We study personalized content generation, which turns a user&#x27;s interaction history into an executable instruction for downstream synthesis, and identify two obstacles: behavior must be encoded in a form legible to language reasoning, and the model must acquire instruction-writing skill absent from both pretraining and behavior data. We propose NaviGen, which represents each item with a dual identifier coupling a collaborative code and a textual code as a behavioral substrate and a semantic bridge in one token stream. On this representation, a two-stage SFT+RL pipeline first distills preference reasoning and instruction writing from evolutionarily searched supervision, then aligns generation with user intent through hierarchical and self-consistent rewards. Experiments across product, game, and short-video domains show that NaviGen improves personalized image and video generation, strengthens next-item prediction, and yields more specific, relevant, and visually generatable instructions. Our code is anonymously released at: https://github.com/iLearn-Lab/NaviGen.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
