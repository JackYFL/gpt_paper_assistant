

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
      <p class="eyebrow">Daily ArXiv / August 12, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>24</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.55rem;opacity:0.94;color:color-mix(in srgb, var(--accent-2) 89%, var(--accent))" title="17 mentions">agent</span><span class="cloud-word" style="font-size:1.67rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="10 mentions">alignment</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="7 mentions">attention</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="9 mentions">backbone</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">capture</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">complementary</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="7 mentions">content</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="7 mentions">cross-modal</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="9 mentions">diffusion</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="8 mentions">echet</span><span class="cloud-word" style="font-size:2.20rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 71%, var(--accent))" title="14 mentions">event</span><span class="cloud-word" style="font-size:1.67rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 44%, var(--accent))" title="10 mentions">evidence</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="8 mentions">fabric</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">generate</span><span class="cloud-word" style="font-size:2.44rem;opacity:0.92;color:color-mix(in srgb, var(--accent-2) 83%, var(--accent))" title="16 mentions">generation</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">generator</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">geometric</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">grounded</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="8 mentions">historical</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">inference</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="7 mentions">interaction</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="9 mentions">latent</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="19 mentions">memory</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="19 mentions">motion</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="7 mentions">multimodal</span><span class="cloud-word" style="font-size:1.81rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="11 mentions">object</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">perspective</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="8 mentions">query</span><span class="cloud-word" style="font-size:1.95rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="12 mentions">reasoning</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">reduce</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="7 mentions">safety</span><span class="cloud-word" style="font-size:1.81rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="11 mentions">scene</span><span class="cloud-word" style="font-size:1.95rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="12 mentions">semantic</span><span class="cloud-word" style="font-size:2.20rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 71%, var(--accent))" title="14 mentions">space</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">standard</span><span class="cloud-word" style="font-size:2.20rem;opacity:0.85;color:color-mix(in srgb, var(--accent-2) 71%, var(--accent))" title="14 mentions">structure</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="5 mentions">substantially</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="8 mentions">supervision</span><span class="cloud-word" style="font-size:1.20rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="7 mentions">target</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="9 mentions">temporal</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">token</span><span class="cloud-word" style="font-size:1.52rem;opacity:0.68;color:color-mix(in srgb, var(--accent-2) 36%, var(--accent))" title="9 mentions">trajectory</span><span class="cloud-word" style="font-size:1.81rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="11 mentions">video</span><span class="cloud-word" style="font-size:1.02rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 10%, var(--accent))" title="6 mentions">vision-language</span><span class="cloud-word" style="font-size:2.66rem;opacity:0.97;color:color-mix(in srgb, var(--accent-2) 95%, var(--accent))" title="18 mentions">visual</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="101 mentions">action</span><span class="cloud-word" style="font-size:1.74rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="208 mentions">agent</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="89 mentions">alignment</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="75 mentions">attention</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">challenging</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="98 mentions">consistency</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="70 mentions">consistently</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="68 mentions">control</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="67 mentions">cost</span><span class="cloud-word" style="font-size:1.11rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 15%, var(--accent))" title="103 mentions">detection</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="86 mentions">diffusion</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="73 mentions">distribution</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="74 mentions">domain</span><span class="cloud-word" style="font-size:1.09rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 14%, var(--accent))" title="100 mentions">dynamic</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="73 mentions">environment</span><span class="cloud-word" style="font-size:1.70rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="201 mentions">evidence</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="98 mentions">fine-grained</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="80 mentions">foundation</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="93 mentions">frame</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="250 mentions">generation</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="69 mentions">geometry</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="94 mentions">inference</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="139 mentions">interaction</span><span class="cloud-word" style="font-size:1.42rem;opacity:0.65;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="150 mentions">language</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">latent</span><span class="cloud-word" style="font-size:1.25rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="124 mentions">memory</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="79 mentions">mllm</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="82 mentions">modality</span><span class="cloud-word" style="font-size:1.34rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="137 mentions">motion</span><span class="cloud-word" style="font-size:1.70rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="200 mentions">multimodal</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="95 mentions">multiple</span><span class="cloud-word" style="font-size:1.49rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 35%, var(--accent))" title="163 mentions">object</span><span class="cloud-word" style="font-size:0.84rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="69 mentions">optimization</span><span class="cloud-word" style="font-size:0.90rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="76 mentions">perception</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="82 mentions">pipeline</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="89 mentions">point</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="81 mentions">real-world</span><span class="cloud-word" style="font-size:1.63rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="188 mentions">reasoning</span><span class="cloud-word" style="font-size:1.13rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 16%, var(--accent))" title="106 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="80 mentions">region</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="78 mentions">retrieval</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="67 mentions">reward</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="68 mentions">robust</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="140 mentions">scene</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="71 mentions">segmentation</span><span class="cloud-word" style="font-size:1.81rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="222 mentions">semantic</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="95 mentions">space</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="135 mentions">spatial</span><span class="cloud-word" style="font-size:0.97rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="85 mentions">structure</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="83 mentions">support</span><span class="cloud-word" style="font-size:1.24rem;opacity:0.61;color:color-mix(in srgb, var(--accent-2) 22%, var(--accent))" title="122 mentions">target</span><span class="cloud-word" style="font-size:1.22rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 21%, var(--accent))" title="119 mentions">temporal</span><span class="cloud-word" style="font-size:1.58rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="178 mentions">token</span><span class="cloud-word" style="font-size:0.87rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="73 mentions">trajectory</span><span class="cloud-word" style="font-size:1.32rem;opacity:0.63;color:color-mix(in srgb, var(--accent-2) 26%, var(--accent))" title="135 mentions">understanding</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="99 mentions">unified</span><span class="cloud-word" style="font-size:2.28rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 75%, var(--accent))" title="328 mentions">video</span><span class="cloud-word" style="font-size:0.96rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="83 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="460 mentions">visual</span><span class="cloud-word" style="font-size:0.94rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="81 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>20 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>GESTO: Human-Centric Spatio-Temporal Memory for Reasoning in Dynamic Scenes</strong>
          <small>Ermanno Bartoli, Buwei He, Dennis Rotondi, Sebastian Koch, Federico Tombari, Kai O. Arras, Patric Jensfelt, Yixi Cai, Iolanda Leite</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Spatial-Temporal Memory</span>
<span class="topic-tag">Human-Robot Interaction</span>
<span class="topic-tag">Dynamic Scene Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2608.10886</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10886">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it proposes a new human-centric spatio-temporal memory for reasoning in dynamic scenes, aimed at embodied robots in human environments.</p>
        <p class="abstract">Robots operating in human environments need memories that capture not only what objects exist and where, but also how people use them over time and how individual interactions compose into goal-directed activities. Existing 4D scene graphs preserve object and place histories but omit activity structure, whereas activity representations are either not grounded in persistent 3D scenes or rely on externally provided event boundaries and object associations. We present GESTO (Grounded Event and Spatio-Temporal memOry), a spatio-temporal memory that couples a persistent 4D scene graph with a two-level hierarchy of atomic human--object interactions and goal-driven events. From an RGB-D observation stream, GESTO automatically extracts timestamped interactions, grounds them to persistent scene entities, groups them into events, and uses event context to refine uncertain object associations. A relation-aware tool-calling agent queries the resulting memory for activity-centric spatio-temporal reasoning. We evaluate GESTO on the reproducible text, binary, and time categories of an existing benchmark, together with 40 new Space2Event and Event2Space queries. GESTO achieves scores of 0.71, 0.75, and 0.70 on the standard categories, approaching a method supplied with ground-truth event and object grounding, while substantially outperforming the same reasoning framework when these inputs are removed. It further achieves 0.73 and 0.75 on Space2Event and Event2Space queries. Ablations show that hierarchical event structure and context-aware grounding refinement provide complementary benefits, supporting activity-grounded hierarchical memory for retrospective reasoning in dynamic human environments.</p>
      </div>
    </details>


    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>The GENEA Challenge 2026: A Large-Scale Disentangled Evaluation of Speech-Driven Gesture Generation on the Seamless Interaction Dataset</strong>
          <small>Rajmund Nagy, Silvia Arellano Garc\&#x27;ia, Hendric Voss, Mihail Tsakov, Taras Kucherenko, Youngwoo Yoon, Gustav Eje Henter</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Gesture Generation</span>
<span class="topic-tag">Human Studies</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.GR</span>
<span class="category-tag">cs.HC</span>
<span class="category-tag">cs.SD</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2608.10839</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10839">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it builds a new embodied/HCI-style benchmark and evaluation protocol for speech-driven gesture generation, with new semantic-mismatch and dyadic evaluation angles.</p>
        <p class="abstract">This preprint presents the results of the fourth GENEA Challenge, a large-scale human evaluation of five speech-driven gesture-generation systems trained by participating teams on the Seamless Interaction dataset of dyadic conversations. As in the 2023 GENEA Challenge, we used a disentangled evaluation methodology to assess motion quality and speech alignment without confounding between the two, and performed a dyadic mismatching study to isolate the effect of listening and reacting to the interlocutor. We additionally introduce a new semantic gesture-generation task and a text-mismatching evaluation methodology using the Grounded Gestures subset of the data. In total, we ran four large-scale user studies, collecting over 23,000 votes from 869 test-takers.   In the motion-realism study, the dataset&#x27;s filtered segments had substantially higher motion quality than all challenge submissions (68-95% pairwise winrate). In the speech-alignment study, the motion-capture segments provided a conceptual ceiling at 62% alignment score, with the top submission significantly behind at 32% and the rest only slightly above the 0% expected of an input-independent system. In the dyadic study, motion capture again set the ceiling at 65% appropriateness score, but no submission scored substantially above chance, indicating that the systems could not yet respond to the interlocutor. Finally, the semantic mismatching evaluation found highly expressive gestures in the dataset (test-takers identified the matching transcript 79% of the time), yet almost all submissions failed to generate semantically expressive motion, with the best achieving only an 8% appropriateness score.   The collected votes and outputs will be made publicly available at https://genea-workshop.github.io/2026/challenge/ to facilitate reproducibility and further research.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Autonomous Driving</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>4D-WAM: 4D Consistent World Modeling for Autonomous Driving</strong>
          <small>Jiacheng Fu, Yibo Yuan, Meng Tian, Yue Li, Jiangtong Zhu, Jianhua Han, Yueyi Zhang, Jianwu Fang, Jianru Xue, Hang Xu, Zhiwei Xiong</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">4D Scene Consistency</span>
<span class="topic-tag">Geometric Supervision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2608.10107</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10107">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an autonomous-driving world-action model with 4D consistent world modeling and geometry-based supervision for planning.</p>
        <p class="abstract">Emerging World-Action Models (WAMs) have demonstrated promising performance in autonomous driving by jointly modeling future driving scene evolution and trajectory planning. However, existing WAMs are typically trained with video data, which is only 2D projections of the underlying 4D driving scene. Consequently, WAMs fail to understand and capture the structure of 4D scenes and thus generate visually plausible yet 4D inconsistent future predictions that mislead downstream planning. To alleviate this issue, we present 4D-WAM, a model that leverages geometric foundation models for training-time supervision to enable 4D consistent world modeling. Specifically, we feed WAM-predicted future frames into a geometric foundation model, and use 4D-aware responses to define a 4D consistency loss. This loss encourages the model to understand, represent, and predict physically consistent 4D scenes during training, without additional inference cost. Moreover, we identify an early-decision phenomenon in WAMs and propose a decision-oriented timestep sampling strategy that emphasizes supervision at early, high-noise stages, where driving decisions are primarily formed. By propagating 4D supervision to this critical decision-formation phase, the proposed strategy further improves trajectory planning. Extensive experiments demonstrate that 4D-WAM effectively models 4D consistent scene evolution and achieves state-of-the-art performance on challenging NAVSIM-v1 and NAVSIM-v2 benchmarks.</p>
      </div>
    </details>


    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>DriveVLA-M0: Failure-Aware Memory Augmentation for Autonomous Driving</strong>
          <small>Zebin Xing, Yupeng Zheng, Qiang Chen, Linbo Wang, Yichen Zhang, Pengxuan Yang, Junli Wang, Deheng Qian, Xiaoqing Ye, Junyu Han, Yifeng Pan, Qichao Zhang, Dongbin Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Retrieval-Augmented Memory</span>
<span class="topic-tag">Test-Time Adaptation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2608.10413</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10413">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it is an embodied driving VLA method with failure-aware memory augmentation and test-time adaptation for autonomous driving.</p>
        <p class="abstract">Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for end-to-end autonomous driving by enabling unified reasoning across perception, language, and planning. However, existing approaches lack mechanisms to exploit past failures or adapt to distribution shifts, causing the model to persistently underperform on similar scenarios where it has previously failed. In this paper, we propose DriveVLA-M0, a retrieval-augmented VLA with failure-aware latent memory. We construct a latent memory pool that stores failure cases along with their structure scene representations and expert trajectory labels, and design a dedicated Retrieve Model that decouples static road structure and dynamic agent interactions to enable structurally grounded retrieval. At inference time, retrieved cases are injected into the model via a lightweight decoupled LoRA-based test-time training (TTT) mechanism, allowing targeted and scenario-specific correction without modifying the backbone. Extensive experiments on NAVSIMv1 and NAVSIMv2 benchmark demonstrate that our approach consistently outperforms prior methods, achieving 94.1 PDMS on Navtest and 47.0 EPDMS on Navhard with only 26.44 ms TTT backward latency overhead. Furthermore, we show that DriveVLA-M0 scales effectively with additional memory, enabling training-free performance gains through memory expansion. The code is available at https://github.com/ZebinX/DriveVLA-M0.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Hallucination Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations</strong>
          <small>Dvir Samuel, Guy Bar-Shalom, Fabrizio Frasca, Ethan Fetaya, Yftah Ziser, Gal Chechik, Haggai Maron</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Hallucination Detection</span>
<span class="topic-tag">LVLM Interpretability</span>
<span class="topic-tag">Token-Level Verification</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2608.10835</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10835">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: a new token-level detector for LVLM hallucinations, with a structure-aware internal representation design.</p>
        <p class="abstract">Large Vision-Language Models (LVLMs) achieve impressive visual reasoning and dialogue capabilities, yet frequently hallucinate content unsupported by the visual input. Effective mitigation requires token-level localization, enabling targeted intervention without discarding the entire response. Existing detectors require expensive full-model fine-tuning, rely on external verifiers that ignore the model&#x27;s generation process, or reduce internal signals to isolated features and hand-crafted statistics, discarding spatial, sequential, and relational structure. We introduce \textbf{UniProbe}, a lightweight, unified, learnable detector that models a frozen LVLM&#x27;s heterogeneous computational trace from a single forward pass. UniProbe constructs a directed graph over image patches, query tokens, and generated tokens, with attention weights encoding their relations. It processes this trace with alternating structure-aware modules: a GNN for relational evidence, a ViT for 2-D visual geometry, and a GRU for response order. Interleaving them allows spatial, relational, and sequential evidence to interact throughout the detector. We further develop a streaming variant for hallucination-aware decoding, which detects and resamples hallucinated tokens during generation, and a self-adaptation strategy aligning the detector with the LVLM&#x27;s own generations. Across diverse LVLM backbones, UniProbe achieves state-of-the-art token-level and object-hallucination detection. During decoding, it reduces object hallucinations by up to 55\% at $1.06\times$ the latency of standard generation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Streaming Video Understanding</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>StreamFlow: Dynamic Memory Flows for Streaming Video Understanding</strong>
          <small>Muxin Fu, Yifan Zhang, Wentao Zhang, Fangming Guo, Qian Chen, Guibin Zhang, Shuicheng Yan, Bo An</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Streaming Video Understanding</span>
<span class="topic-tag">Visual Memory</span>
<span class="topic-tag">MLLM</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2608.10949</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10949">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and is somewhat relevant to criterion 4: a new MLLM framework for streaming video understanding with dynamic visual memory.</p>
        <p class="abstract">Streaming video understanding requires multimodal large language models (MLLMs) to preserve relevant evidence from continuously evolving streams under strict causality and bounded memory. Yet existing paradigms remain limited: model-based methods require intrusive backbone updates, while memory-based methods expend substantial visual-encoding computation on temporally redundant content and rely on rigid access to visual history. To address these limitations, we introduce StreamFlow, an efficient visual memory framework that enables dynamic, on-demand access to historical visual information. StreamFlow combines a lightweight, dynamics-aware mid-term memory that filters temporal redundancy before visual encoding with a latent long-term memory that consolidates historical video content into visual latents accessible to subsequent reasoning. During generation, an attention-guided retrieval mechanism injects relevant visual latents when the model&#x27;s reliance on visual evidence weakens. StreamFlow achieves state-of-the-art streaming video understanding performance, reaching 67.73% overall accuracy on StreamingBench, while also delivering strong performance on offline long-video benchmarks. Relative to the vanilla setting, it improves the visual attention score (VAS) by 59.1% while reducing end-to-end latency and peak memory by 50.4% and 21.1%, respectively, enabling more visually grounded and efficient reasoning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">LVLM Safety</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning</strong>
          <small>Caoyuan Ma, Wenpu Liu, Weichu Xie, Tian Gu, Shilei Zhao, Lingxi Min, Shuai Dong, Yuqi Xu, Ji Zhao, Ziyue Wang, Wenzheng Chang, Taiqiang Wu, Yongfu Zhu, Wenqi Shao, Yinqiang Zheng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">LVLM Safety</span>
<span class="topic-tag">Reinforcement Learning</span>
<span class="topic-tag">Multimodal Alignment</span>
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
          <span>Paper 6 / arXiv:2608.10513</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10513">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: a new LVLM safety/alignment method for multimodal models, with caption-mediated reinforcement learning.</p>
        <p class="abstract">Large vision-language models (LVLMs) remain vulnerable to jailbreak attacks that exploit visual inputs to bypass safety alignment inherited from their language backbones. We propose SafeCap, a reinforcement-learning framework that aligns LVLMs through learned self-captioning. SafeCap trains a policy model to first generate a safety-relevant image caption and then produce a final answer; the caption is further optimized by whether it enables a frozen LLM to reach a safety-aligned decision. This caption-mediated objective encourages the policy to expose visual cues relevant to safe response generation rather than relying solely on direct refusal supervision. Across five multimodal safety benchmarks and six vision-utility benchmarks, SafeCap substantially improves aggregate safety performance under its intended DirectCap protocol, with gains of 3.7-19.0 points in safety average across four model settings while maintaining comparable or improved vision utility. Under controlled comparisons on matched backbones and data, SafeCap outperforms safety SFT, DPO, and SafeGRPO, demonstrating the effectiveness of caption-mediated reinforcement learning for multimodal safety alignment.</p>
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
          <strong>SapiensID 2.0: Aligning Human Recognition Foundation Models with Human Perception</strong>
          <small>Yiyang Su, Jie Zhu, Feng Liu, Anil K. Jain, Xiaoming Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Person Re-Identification</span>
<span class="topic-tag">MLLM Alignment</span>
<span class="topic-tag">Temporal Modeling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2608.10497</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10497">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it is a human-recognition foundation-model paper that transfers semantic knowledge from MLLMs and adds temporal attention for perception-aware recognition.</p>
        <p class="abstract">While foundation models have significantly advanced human recognition across diverse modalities, they predominantly rely on static, geometric feature extraction. This approach fundamentally diverges from human perception. Consequently, current models often suffer from &quot;semantic blindness,&quot; overfitting to transient noise while failing to leverage invariant soft biometrics, and struggle to capture temporal motion signatures. To bridge this gap, we propose SapiensID 2.0, a human recognition framework enriched with both semantic and temporal awareness. To overcome the lack of soft-biometric annotations, we transfer zero-shot semantic knowledge from Multimodal Large Language Models (MLLMs) into a discriminative embedding space. We resolve the dimensional mismatch between these spaces using Invariant Trait Alignment (ITA) to distill core persistent traits, and Transient Noise Disentanglement (TND) to decouple artifacts like clothing. Furthermore, we design a Kinematic Semantic Attention Head (K-SAH) that extends spatial attention across temporal windows. By tracking semantic patches over time, K-SAH captures rich kinematic signatures without requiring large-scale video datasets. Extensive experiments demonstrate that SapiensID 2.0 achieves state-of-the-art performance across image- and video-based person re-identification and gait recognition, while maintaining robust face recognition capabilities.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">4D Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Beyond Pixels: From Video Priors to 4D Worlds</strong>
          <small>Zihao Liu, Xiaolong Shen, Zhenglin Zhou, Ruijie Quan, Yi Yang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">4D Generation</span>
<span class="topic-tag">Video Diffusion</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">3D/4D Vision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2608.10744</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10744">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it is a generative modeling paper that uses video priors to produce 4D worlds, fitting the vision foundation/generative modeling interest well.</p>
        <p class="abstract">4D generation synthesizes dynamic 3D scenes from conditions such as text or images. Existing methods either reconstruct generated RGB videos with a separate 4D model or adapt a particular video generator to predict geometry directly. The former suffers from distribution mismatch and error propagation, whereas the latter ties 4D prediction to a specific generator and may require retraining when the generator or conditioning regime changes. We ask whether the final denoised latents of video models that share a variational autoencoder (VAE) can instead provide a reusable interface to explicit 4D prediction. Building on this insight, we introduce direct latent-to-4D generation and instantiate it as Latent-to-4D, which bypasses RGB by aligning a video latent with the token grid of a pretrained 4D decoder and refining it through frame-wise and global spatiotemporal attention. Trained on roughly 1K existing reconstruction clips, a single checkpoint transfers unchanged across multiple video diffusion transformers within the same VAE family. On Text4D-200 and I4D-200, Latent-to-4D surpasses matched same-latent Wan+4RC cascades in projection-based DINO-F1 by 2.88--3.45 and 5.81 points, respectively, while also being preferred by human raters for geometry, temporal stability, and overall quality.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Agentic Vision</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>InSight-doc: Agentic Visual Perception for Long-Document Understanding</strong>
          <small>Kaican Li, Weiyan Xie, Lewei Yao, Jiannan Wu, Lanqing Hong, Yongxiang Huang, Nevin L. Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agentic Vision</span>
<span class="topic-tag">Document Understanding</span>
<span class="topic-tag">Multimodal Models</span>
<span class="topic-tag">Active Perception</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2608.10628</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10628">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 and 4 well: it is an agentic visual-perception method for long-document understanding, using adaptive zoom-in perception with a multimodal model.</p>
        <p class="abstract">Long-document understanding often requires reasoning over many visually rich pages, making inference costly and prone to context rot. In this work, we propose InSight-doc, an agentic visual perception framework that treats visual resolution as an adaptive reasoning-time resource. InSight-doc starts from low resolution and selectively zooms into high-resolution regions for finer evidence, without relying on any external retriever. To train such an agent, we construct an active-perception corpus of 17.9K high-quality SFT examples with region-level zoom-in trajectories, accompanied by 19.2K hard RL examples. Through SFT+RL, InSight-doc-8B improves the baseline by 4.3--16.4 accuracy points over document VQA benchmarks. On long documents, it reduces hallucination by more than 40% and inference latency by 41%--68% while maintaining an accuracy lead. Our code, datasets, and model are released at https://github.com/m-Just/InSight-doc .</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Manipulation</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>MAD-HOI: Masked Autoregressive Diffusion for Generating Articulated Hand Object Interactions from Text</strong>
          <small>Ananya Bal, Kartik Sharma, Ethan Lai, Samyak Tiwari, Liza Dahiya, Chaitanya Chawla, Laszlo A. Jeni</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Manipulation</span>
<span class="topic-tag">Hand-Object Interaction</span>
<span class="topic-tag">Motion Generation</span>
<span class="topic-tag">Autoregressive Diffusion</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2608.10162</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10162">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: a new embodied/motion-generation method for articulated hand-object interactions, focused on a novel generation setting rather than a benchmark.</p>
        <p class="abstract">Methods for text-based generation of hand-object interaction (HOI) sequences primarily focus on producing smooth, physically plausible trajectories. A truly utilitarian method should additionally support variable-length generation, composite motion sequences, motion completion and infilling, and reliable termination without compromising physical plausibility. Standard diffusion models for HOI generation are typically trained only for text-to-motion generation on atomic motions and require the motion length to be specified a-priori. Autoregressive (AR) methods provide greater sequence-level flexibility, but commonly depend on discrete motion codes, which can lose contact-sensitive motion detail. To address these key limitations, we present a model performing Masked Autoregression with Diffusion for HOI generation (MAD-HOI). Our method starts by encoding hand and object motions in a continuous latent space while keeping them disentangled to maintain stream-wise control. This is followed by a masked autoregressive transformer to predict context features that condition a flow-matching head. MAD-HOI is capable of motion generation for atomic and composite articulated sequences, conditioned motion completion and infilling, as well as EOM (End of Motion) prediction from a single training objective. We provide comprehensive evaluations for these capabilities and benchmark our method on the ARCTIC and GRAB datasets. Our experiments demonstrate that our method generates more diverse and physically plausible interactions compared to other open-sourced baseline methods.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multi-Modal Detection</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Bridging Severe Cross-Modal Misalignment: End-to-End Visible-Infrared Object Detection via Explicit Feature-Domain Affine Registration</strong>
          <small>Qi Ming, Yuyang Wang, Mingjing Zhao, Yifan Xiao, Zhixin Guo, Zhiqiang Zhou, Peng Sun, Juan Fang, Fuqiang Yang, Xudong Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multi-Modal Detection</span>
<span class="topic-tag">Cross-Modal Alignment</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Registration</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2608.10680</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10680">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it introduces a new benchmark for severe visible-infrared misalignment and a method for explicit feature-domain registration, with a novel spatial-alignment angle.</p>
        <p class="abstract">Visible-infrared object detection relies on complementary RGB and thermal cues, but its performance is often degraded by cross-modal spatial misalignment. Most existing methods rely on implicit feature adaptation to handle weakly misaligned scenarios, while large-offset geometric discrepancies remain insufficiently addressed. In this paper, we propose a Joint Feature-domain Registration and Detection network (JFRDet), an end-to-end visible-infrared oriented object detector tailored for severely cross-modal geometric discrepancies. JFRDet introduces a Cross-Modal Affine Alignment (CMAA) module to estimate an image-level affine transformation for explicit multi-level feature alignment. Note that illumination changes directly affect the reliability of RGB cues, an Illumination-Guided Complementary Fusion (IGCF) module adaptively exploits modality reliability under varying illumination conditions for cross-modal fusion. Then, an Alignment Quality-Consistency Gating (AQCG) strategy stabilizes joint optimization by modulating detection supervision according to alignment reliability and gradient consistency. We further construct DroneVehicle Misaligned (DVMA), a benchmark for evaluating visible-infrared oriented object detection under severe cross-modal geometric misalignment. The proposed JFRDet achieves 69.7\% $\mathrm{mAP}_{50}$ on DVMA, which represents state-of-the-art (SOTA) performance. The code and dataset will be available on GitHub.</p>
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
          <strong>MMArt A Multi-Perspective Multimodal Dataset for Visual Art Understanding</strong>
          <small>Shuai Wang, Wangyuan Ding, Yixian Shen, Jia-Hong Huang, Stevan Rudinac, Monika Kackovic, Nachoem Wijnberg, Marcel Worring</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Dataset</span>
<span class="topic-tag">Art Understanding</span>
<span class="topic-tag">Multimodal Captioning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.MM</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2608.10706</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10706">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: this is a vision foundation model application/dataset paper for art understanding, and it includes multi-perspective multimodal supervision that should be useful for VLM research.</p>
        <p class="abstract">Recent vision-language models demonstrate impressive general visual understanding, yet their art interpretation remains shallow: they describe surface content but struggle with formal analysis, grounded historical interpretation, or affective characterization. We argue this is not only a model but also a dataset limitation. Existing art datasets are single perspective resources, where no dataset provides narrative, formal, emotional, and historical perspectives simultaneously for the same artworks. We introduce MMArt, a large-scale dataset of 74,234 WikiArt paintings, each annotated with four independently annotated perspectives plus a harmonized unified caption, produced by specialized vision-language models or human annotation and validated through complementary quality evaluations. Two complementarity analyses establish that perspectives encode genuinely distinct information. A generative analysis shows that formal analysis descriptions best preserve compositional style, and historical descriptions carry strong affective signal in reconstructed images. A discriminative retrieval analysis reveals task-asymmetry: narrative descriptions drive retrieval (R@1 = 44.0%), while formal descriptions, strongest for reconstruction, are nearly nondiscriminative at retrieval scale (R@1 = 7.8%). Leave-one-out analysis further confirms that historical descriptions are the least replaceable perspective across both tasks. Together, the two analyses establish that no single perspective suffices for all tasks, directly motivating MMArt multi-perspective design. The dataset, code, and additional information are available at https://shuaiwang97.github.io/MMArt/.</p>
      </div>
    </details>


    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>NullEdit: Stealthy Image Protection via VLM Condition Redirection</strong>
          <small>Weiyao Huang, Liqin Wang, Ziqi Sheng, Wei Lu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Image Editing</span>
<span class="topic-tag">Adversarial Defense</span>
<span class="topic-tag">Diffusion Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2608.10870</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10870">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a vision-language model–conditioned application for image editing protection, with a method that redirects VLM representations before the diffusion backbone.</p>
        <p class="abstract">Modern image editors combine vision-language models (VLMs) with diffusion transformer backbones to modify a single reference image according to instructions without fine-tuning. This capability also enables unauthorized manipulation of publicly released images. Existing inference-time defenses either invalidate edits through conspicuous corruption, thereby exposing the protection, or allow them to proceed with identity or reference content drift, thereby failing to prevent the editing behavior itself. We instead target a stealthy and harmless no-op in which the requested edit is suppressed, the output remains natural and source-preserving without conspicuous artifacts or identity replacement, and harmful semantics requested by malicious instructions are absent. We propose NullEdit, which targets the VLM representation jointly formed from the reference image and instruction before it conditions the downstream DiT backbone. Using normal-edit and no-edit anchors, NullEdit redirects this representation, while cross-prompt gradient averaging transfers protection to held out instructions. Across Step1X-Edit and Qwen-Image-Edit on CelebA-HQ and VGGFace2, NullEdit reduces the EditReward IF score by 0.813 on average relative to the SOTA baseline while preserving subject identity and source content.</p>
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
          <strong>AdvFD: Boosting Visual Generation via Adversarial Fr&#x27;echet Distance Loss</strong>
          <small>Mingju Gao, Jingkai Zhou, Kun Gai, Changqian Yu, Hao Tang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Fréchet Distance</span>
<span class="topic-tag">Vision Foundation Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2608.11205</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.11205">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 somewhat: a vision generation method using an adversarial Fréchet-distance objective, relevant to generative modeling and vision foundation model post-training.</p>
        <p class="abstract">Fr\&#x27;echet distance has recently emerged as an effective distribution-level objective for generator post-training, complementing the conventional sample-level diffusion and flow-matching losses. However, directly optimizing Fr\&#x27;echet objectives can cause Fr\&#x27;echet hacking. The target metrics keep improving, but visual quality and Fr\&#x27;echet alignment in other feature spaces may stagnate or deteriorate. We attribute this failure to the static pretrained feature spaces used by existing Fr\&#x27;echet losses. These feature spaces provide incomplete and fixed views of the differences between real and generated distributions. To address this limitation, we propose Adversarial Fr\&#x27;echet Distance (AdvFD), which complements the static representation targets in FD-Loss with a calibrated adversarially learned representation. AdvFD augments the original static Fr\&#x27;echet objective with a learnable representation that adversarially maximizes the Fr\&#x27;echet discrepancy between real and generated samples, while the generator minimizes the same discrepancy in the resulting adaptive feature space. To prevent the adversarial representation from trivially increasing the objective through feature amplification, we further introduce real-feature whitening, which normalizes its scale and covariance geometry and stabilizes the min--max optimization. Extensive experiments show that AdvFD consistently improves one-step generator post-training across both JiT and pMF backbones and across different model scales.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Text-to-Video</summary>
      <div class="queue">

    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>SafeCA: Safe Cross-Attention Localization and Regulation for Text-to-Video Jailbreak Defense</strong>
          <small>Siyuan Liang, Yupeng Qiu, Junfeng Fang, Rong-Cheng Tu, Jiaxing Huang, Dacheng Tao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Video</span>
<span class="topic-tag">Safety &amp; Jailbreak Defense</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Cross-Attention</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2608.10933</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10933">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 in a broad sense: it studies and defends a text-to-video generative model, with an insightful analysis of cross-attention separability during diffusion.</p>
        <p class="abstract">Text-to-Video (T2V) generative models are vulnerable to jailbreak attacks in real-world deployment, leading them to produce harmful or inappropriate content. Existing defense approaches mainly rely on input filtering or reconstruction, which not only incur high computational latency but also tend to distort semantics. To address these issues, we experimentally and systematically analyze the differences between clean and jailbreak samples in the cross-attention feature space, revealing for the first time a cumulative separation effect and a progressively increasing trend of linear separability between the two during the diffusion process. Based on this insight, we propose SafeCA, a feature-level defense mechanism for safe cross-attention localization and regularization. Firstly, we identify key defensive regions and values through attention stability analysis using cross-attention features collected from clean prompts within a single inference. Secondly, SafeCA mitigates anomalous activations via attention masking with energy normalization and introduces a lightweight semantic-space adapter to redirect abnormal semantic flows. Furthermore, we detect and suppress potentially malicious tokens by back-propagating feature anomaly signals to the input cue words, thereby enhancing the deployability of the defense in commercial models. Experimental results show that SafeCA reduces the jailbreak success rate by about 20% on mainstream T2V models, adds almost no inference overhead (+0.1s), and maintains good text-video semantic consistency. Overall, SafeCA provides an architecture-level, deployable protection paradigm for T2V generation models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Colorization</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>Beyond Fixed Luminance: Towards Panchromatic and Orthochromatic Image Colorization</strong>
          <small>Swarnim Maheshwari, Syed Imam Ali, Vineeth N. Balasubramanian</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Colorization</span>
<span class="topic-tag">Foundation Models</span>
<span class="topic-tag">Image Editing</span>
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
          <span>Paper 19 / arXiv:2608.10798</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10798">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it applies a foundation image-editing model to colorization, with a useful robustness angle on panchromatic vs. orthochromatic grayscale formation.</p>
        <p class="abstract">Most image colorization systems operate in $Lab$ space by predicting chroma ($ab$) while preserving an input-derived luminance channel ($L$). While effective on standard benchmarks, this fixed-luminance design restricts brightness changes and becomes unreliable when grayscale formation deviates from natural-image luminance, as in historical orthochromatic photography. We propose a luminance-agnostic colorization framework that formulates colorization as full-RGB image editing using a foundation image-editing model. To bridge modern panchromatic and historical orthochromatic conditions, we introduce a mixed grayscale objective that trains the model under both standard luminance grayscale and a red-insensitive grayscale formation. Experiments on COCO, ImageNet, and a multi-instance benchmark show that our method is competitive on standard grayscale inputs and substantially more robust under orthochromatic inputs, with qualitative comparisons and a human study indicating fewer visible color artifacts.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Pretraining</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>Unlocking the Power of Medical Tabular Data via Semantic-Aware Multimodal Pre-training</strong>
          <small>Yingsheng Liu, Haiming Li, Jingmin Zhu, Jiajun Sun, Victoria Mar, Monika Janda, H. Peter Soyer, Zongyuan Ge, Zhen Yu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Pretraining</span>
<span class="topic-tag">Medical AI</span>
<span class="topic-tag">Tabular Learning</span>
<span class="topic-tag">Representation Learning</span>
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
          <span>Paper 20 / arXiv:2608.10522</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10522">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a multimodal pre-training method for medical tabular data, though it is more medical representation learning than general vision foundation models.</p>
        <p class="abstract">While vision-language models dominate medical representation learning, unstructured text lacks the dense, quantitative diagnostic phenotypes inherent in structured clinical tables. However, existing multimodal pre-training methods underutilize this potential due to semantic-agnostic designs that treat tabular inputs as flat vectors and employ unstable continuous regression objectives. To overcome this, we propose a novel semantic-aware framework explicitly modeling the intrinsic two-dimensional structure of tabular data. First, addressing the inter-feature hierarchy of varying diagnostic importance, we introduce Importance-Aware Adaptive Masking to construct a label-free curriculum prioritizing salient features. Second, addressing the intra-feature continuity-discreteness duality, we propose a Soft-Label Discretized Module that replaces unstable numerical regression with stable distribution matching, thereby mathematically preserving ordinal relationships. Extensive experiments across large-scale dermatology (SLICE-3D, HOP) and ophthalmology (EyePACS) datasets establish a new state-of-the-art (SOTA), demonstrating exceptional robustness and cross-domain generalizability.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Frame Interpolation</summary>
      <div class="queue">

    <details class="paper-row" id="link20">
      <summary class="paper-row-summary">
        <span class="queue-index">21</span>
        <span class="paper-row-copy">
          <strong>Bridging Event Streams and DiT: Event-Guided Video Frame Interpolation</strong>
          <small>Guixu Lin, Yuyang Yu, Xiang Ji, Linyao Chen, Zhengwei Yin, Mengshun Hu, Mingdeng Cao, Shengfeng He, Yinqiang Zheng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Frame Interpolation</span>
<span class="topic-tag">Event Cameras</span>
<span class="topic-tag">Diffusion Models</span>
<span class="topic-tag">Motion Estimation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 21 / arXiv:2608.10479</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10479">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Only a partial fit to criterion 4: it uses event cameras with diffusion-based video interpolation, which is vision-model application but not a foundation-model paper.</p>
        <p class="abstract">Latent diffusion models have recently advanced video frame interpolation by synthesizing intermediate frames between input images. However, handling large temporal gaps and complex motion remains challenging, often resulting in motion blur, structural distortions, and temporal inconsistencies. Event cameras provide high-temporal-resolution motion cues that are well suited for bridging these gaps and improving interpolation quality. To exploit this advantage without training an event-assisted model from scratch, we propose an adapter-based framework that incorporates event-derived cues into a pre-trained image-to-video diffusion model with minimal architectural changes. Specifically, our method leverages Image Warped Events (IWEs) and bidirectional sparse optical flow to provide spatially and temporally aligned guidance during generation. By injecting these event-guided structural and motion cues into the diffusion process, our approach reduces interpolation artifacts and improves both reconstruction fidelity and temporal coherence. Experimental results on real and synthetic benchmarks show that our method consistently outperforms existing state-of-the-art approaches. The project page is at https://joseph-lin-tech.github.io/BridgeEventDiT-VFI/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Robotic Manipulation</summary>
      <div class="queue">

    <details class="paper-row" id="link23">
      <summary class="paper-row-summary">
        <span class="queue-index">24</span>
        <span class="paper-row-copy">
          <strong>Precise Top-Layer Fabric Segmentation for Fabric Destacking with Edge- and Shape-Aware Deep Networks</strong>
          <small>Wenbo Dong, Dipankar Bhattacharya, Akinari Kobayashi, Akira Seino, Fuyuki Tokuda, Xuzhao Huang, Kai Tang, Norman C. Tien, Kazuhiro Kosuge</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Robotic Manipulation</span>
<span class="topic-tag">Segmentation</span>
<span class="topic-tag">Industrial Vision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 24 / arXiv:2608.10648</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10648">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 weakly: an embodied manipulation-related segmentation method for fabric destacking, but it is more a task-specific robotic perception paper than a broader embodied AI benchmark/method angle.</p>
        <p class="abstract">Fabric destacking requires precise segmentation of the topmost fabric layer, a task complicated by subtle fabric boundaries and high visual similarity between fabric layers. Existing semantic and edge-based segmentation approaches often struggle with these complexities, limiting the performance of robotic manipulation for different tasks. In this work, a novel segmentation training architecture tailored for top-layer fabric segmentation in stacked fabrics is proposed. The method extends the classical encoder-decoder framework by introducing two specialized branches - an edge-aware branch and a shape-aware branch - that are used to supervise the backbone network for better tuning. The edge-aware branch enhances boundary delineation, while the shape-aware branch guides the network to capture and align the overall fabric shape with reference masks derived from Computer Aided Design (CAD) models. Experiments on a real-world fabric dataset demonstrate that the training approach outperforms established baselines, verifying the effectiveness of the multi-branch design through both quantitative results and ablation studies.</p>
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
      <summary class="topic-heading">Multimodal Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>VERDICT: Training-Free Step-Wise Verification of Multimodal Reasoning via Disagreement-Aware Consensus</strong>
          <small>Rohit Sinha, Kunal Tilaganji, Tanuja Ganu, Nagarajan Natarajan, Amit Sharma, Vineeth Balasubramanian</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Reasoning</span>
<span class="topic-tag">Verification</span>
<span class="topic-tag">Training-Free Methods</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CV</span>
<span class="category-tag">cs.GT</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2608.10665</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10665">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 reasonably well: training-free verification for multimodal reasoning in MLLMs, with an interesting disagreement-aware consensus trick.</p>
        <p class="abstract">Multimodal large language models often generate reasoning chains containing subtle errors that lead to incorrect answers. Current verification approaches have notable limitations. Existing approaches either require expensive labelled supervision with inconsistent cross-task performance or aggregate scores from multiple sources by simple aggregations, missing a key insight: when these scores disagree, that disagreement itself carries important information about whether a reasoning step is truly valid or not. We formalise this as a coupled scoring problem among disparate, frozen verifiers, interpretable as a coordination game with a unique closed-form equilibrium where agreement signals valid steps while disagreement reveals instability. Towards this end, we propose a training-free domain-agnostic step-wise verification approach we call VERDICT: VERification via Disagreement-Informed Coupled Thresholding. To our knowledge, VERDICT is the first training-free verifier that makes the structure of cross-modal disagreement explicit and actionable. It computes consensus scores through a closed-form solution, enabling both disagreement-aware filtering and stability-conscious ranking of reasoning steps. Evaluated across six benchmarks, \method consistently improves over the base model by up to +5.95%, and performs competitively with domain-specific critics that demand extensive supervision, demonstrating that cross-modal agreement provides robust verification signals without task-specific adaptation and Training-Free Verification</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Agent Memory</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>MESA:Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory</strong>
          <small>Beidi Zhao, Yaoqi Chen, Yuru Feng, Menghao Li, Qianxi Zhang, Baotong Lu, Jianan Lu, Zhirui Wang, Xinjiang Wang, Shusen Xu, Zengzhong Li, Xiaoxiao Li, Qi Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agent Memory</span>
<span class="topic-tag">Long-Horizon Agents</span>
<span class="topic-tag">Evidence Selection</span>
<span class="topic-tag">Planning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2608.10108</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10108">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: proposes a new long-horizon agent memory method with dynamic evidence selection, which is relevant to embodied/agentic AI methods even though it is not a simulator benchmark.</p>
        <p class="abstract">Long-horizon agents accumulate trajectories spanning hundreds of interleaved reasoning, action, and observation steps, where answering a query may depend on evidence buried far back in the history. External memory stores such trajectories as structured representations, yet each structure provides a distinct and incomplete view. Existing multi-memory systems either read a fixed set of structures for every query, inflating context and introducing noise, or route each query to a single structure, preventing the composition of complementary evidence. A controlled analysis on AMA-Bench shows that the optimal memory configuration is typically neither a single structure nor the full union, but a tailored composition of multiple structural memories that varies with query and task demands. Motivated by these findings, we formulate structure-level dynamic selection: selecting and fusing a query-adaptive subset from a library of specialized memory structures. We propose MESA (a Multi-structure Evidence Selection framework for long-horizon Agent), which builds five complementary structure views of each trajectory and learns from end-to-end answer-level feedback to select and fuse a query-specific subset for a frozen answer model. To learn under this weak supervision, MESA employs harness optimization with prior-guided search and UCB-guided scheduling to balance exploration and exploitation. On AMA-Bench, MESA outperforms the strongest baseline by 8.5% while using 41% fewer evidence tokens than the all-structure alternative.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link21">
      <summary class="paper-row-summary">
        <span class="queue-index">22</span>
        <span class="paper-row-copy">
          <strong>ComBodied Agents: a New Paradigm of Human-Centric Agentic AI</strong>
          <small>Qianggang Ding, Xingyao Wang, Rui Feng, Zhibin Wang, Feixiang Wang, Kelong Mao, Hao Sun, Zhiyao Luo, Jiankai Tang, Lei Li, Jiadong Guo, Minheng Ni, Weicong Lin, Chenxi Yang, Hongxiang Gao, Zhenghua Chen, Yang Bai, Min Wu, Jun Cheng, Huazhu Fu, Dacheng Tao, Bang Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Agentic AI</span>
<span class="topic-tag">Human-Centric AI</span>
<span class="topic-tag">Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 22 / arXiv:2608.10915</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10915">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: it is an embodied/agentic AI position paper proposing a new human-centric paradigm and evaluation direction, although it is more conceptual than a concrete benchmark or method.</p>
        <p class="abstract">After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural gap in Agentic AI: Digital Agents primarily transform software states, while Embodied Agents transform physical states; neither makes a person&#x27;s evolving state and agency the primary object of modeling, intervention, and evaluation. We introduce Combodied Agents, a human-centered paradigm that perceives, models, predicts, and supports individual human-state trajectories over time, using software tools, sensors, wearables, robots, and human services as action channels rather than end goals. We unify fragmented capabilities across personal assistants, health agents, AI companions, and adaptive human--AI systems into a closed loop: event-based multimodal perception reconstructs meaningful personal events; longitudinal, correctable memory provides temporal context; Personal World Models estimate future personal states and outcomes under alternative decisions and interventions; and an admissible intervention policy selects proportionate support under consent, uncertainty, safety, reversibility, and user control. Feedback from the person and environment updates the loop. Rather than requiring an exhaustive Human Digital Twin, the framework uses purpose-bounded, uncertainty-aware, user-correctable representations. We organize the design space by human-state targets, relational contexts, and agent roles, and propose scenario-centered evaluation, agency-preservation metrics, benchmark requirements, edge-native personal models, and governance directions. Combodied Agents shift Agentic AI from external task completion toward sustained human benefit.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">AI Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link22">
      <summary class="paper-row-summary">
        <span class="queue-index">23</span>
        <span class="paper-row-copy">
          <strong>Automating and Scaling Behavioral Scientific Research on AI Agents</strong>
          <small>Soo Yong Lee, Jongha Lee, Jaewan Chun, Hyunjin Hwang, Fanchen Bu, Ziv Ben-Zion, Taekwan Kim, Denny Borsboom, Jaemin Yoo, Kijung Shin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">AI Agents</span>
<span class="topic-tag">Behavioral Evaluation</span>
<span class="topic-tag">Simulation Studies</span>
<span class="topic-tag">Statistical Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.MA</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 23 / arXiv:2608.10030</span>
          <a class="paper-action" href="https://arxiv.org/abs/2608.10030">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Only a loose fit: it studies AI agents behavior scientifically, but it is not specifically about embodied AI, VLLMs/MLLLMs, or vision foundation models.</p>
        <p class="abstract">As AI agents are increasingly deployed in complex environments, understanding their behaviors becomes critical. Yet behavioral scientific research on AI agents remains manual and labor-intensive. We introduce AEROBAT, the first multi-agent system to automate behavioral scientific research on AI agents. Given an arbitrary target behavior by its user, AEROBAT automatically executes a full pipeline of behavioral scientific research---generating hypotheses about the behavior, designing and executing controlled experiments, making behavioral assessments, analyzing the results, and writing reports. For 12 target behaviors, we used AEROBAT to generate and test 79 hypotheses: designing 1,240 controlled experiments and executing 23,512 simulation rounds in total. Moderate-to-strong statistical evidence was found for 26 hypotheses, including some novel ones. In sum, our results demonstrate that automated behavioral scientific research on AI agents can complement and extend the reach of manual research.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
