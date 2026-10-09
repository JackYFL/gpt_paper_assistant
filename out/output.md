

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
      <p class="eyebrow">Daily ArXiv / October 09, 2026</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">

    <div class="metric">
      <span>Relevant papers</span>
      <strong>26</strong>
    </div>


    <div class="metric">
      <span>Top score</span>
      <strong>17</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>11.6</strong>
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
      <div class="word-cloud"><span class="cloud-word" style="font-size:2.06rem;opacity:0.82;color:color-mix(in srgb, var(--accent-2) 64%, var(--accent))" title="15 mentions">action</span><span class="cloud-word" style="font-size:2.68rem;opacity:0.98;color:color-mix(in srgb, var(--accent-2) 95%, var(--accent))" title="21 mentions">agent</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">attention</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="9 mentions">candidate</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">computation</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">downstream</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">dynamic</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="9 mentions">environmental</span><span class="cloud-word" style="font-size:1.94rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="14 mentions">evidence</span><span class="cloud-word" style="font-size:1.70rem;opacity:0.73;color:color-mix(in srgb, var(--accent-2) 45%, var(--accent))" title="12 mentions">feedback</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="8 mentions">flow</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 25%, var(--accent))" title="9 mentions">future</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="8 mentions">gaussian</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="8 mentions">geometric</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">inference</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="11 mentions">interaction</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">jointly</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">language</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">latent</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="10 mentions">motion</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="10 mentions">multimodal</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="10 mentions">observation</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">outcome</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="8 mentions">perception</span><span class="cloud-word" style="font-size:2.58rem;opacity:0.95;color:color-mix(in srgb, var(--accent-2) 90%, var(--accent))" title="20 mentions">point</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="10 mentions">policy</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="22 mentions">reasoning</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">reduce</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="8 mentions">reference</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">retrieval</span><span class="cloud-word" style="font-size:2.48rem;opacity:0.93;color:color-mix(in srgb, var(--accent-2) 85%, var(--accent))" title="19 mentions">scene</span><span class="cloud-word" style="font-size:1.15rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="8 mentions">screen</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">self-distillation</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="11 mentions">semantic</span><span class="cloud-word" style="font-size:2.58rem;opacity:0.95;color:color-mix(in srgb, var(--accent-2) 90%, var(--accent))" title="20 mentions">skill</span><span class="cloud-word" style="font-size:2.06rem;opacity:0.82;color:color-mix(in srgb, var(--accent-2) 64%, var(--accent))" title="15 mentions">spatial</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">structure</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="7 mentions">successful</span><span class="cloud-word" style="font-size:1.57rem;opacity:0.69;color:color-mix(in srgb, var(--accent-2) 39%, var(--accent))" title="11 mentions">token</span><span class="cloud-word" style="font-size:1.83rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="13 mentions">trajectory</span><span class="cloud-word" style="font-size:2.68rem;opacity:0.98;color:color-mix(in srgb, var(--accent-2) 95%, var(--accent))" title="21 mentions">video</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">view</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="6 mentions">vision-language</span><span class="cloud-word" style="font-size:2.28rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 75%, var(--accent))" title="17 mentions">visual</span><span class="cloud-word" style="font-size:1.83rem;opacity:0.76;color:color-mix(in srgb, var(--accent-2) 52%, var(--accent))" title="13 mentions">world</span></div>
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      <div class="word-cloud"><span class="cloud-word" style="font-size:1.86rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 54%, var(--accent))" title="146 mentions">action</span><span class="cloud-word" style="font-size:1.95rem;opacity:0.79;color:color-mix(in srgb, var(--accent-2) 58%, var(--accent))" title="156 mentions">agent</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">alignment</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">backbone</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">candidate</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="55 mentions">change</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="59 mentions">consistency</span><span class="cloud-word" style="font-size:1.04rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="68 mentions">control</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">dense</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">detection</span><span class="cloud-word" style="font-size:1.47rem;opacity:0.67;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="105 mentions">dynamic</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="67 mentions">environment</span><span class="cloud-word" style="font-size:2.01rem;opacity:0.81;color:color-mix(in srgb, var(--accent-2) 61%, var(--accent))" title="163 mentions">evidence</span><span class="cloud-word" style="font-size:0.86rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="55 mentions">foundation</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">future</span><span class="cloud-word" style="font-size:2.28rem;opacity:0.87;color:color-mix(in srgb, var(--accent-2) 75%, var(--accent))" title="196 mentions">generation</span><span class="cloud-word" style="font-size:1.00rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="65 mentions">geometric</span><span class="cloud-word" style="font-size:1.14rem;opacity:0.58;color:color-mix(in srgb, var(--accent-2) 17%, var(--accent))" title="76 mentions">geometry</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="59 mentions">grounding</span><span class="cloud-word" style="font-size:1.08rem;opacity:0.57;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="71 mentions">inference</span><span class="cloud-word" style="font-size:1.60rem;opacity:0.7;color:color-mix(in srgb, var(--accent-2) 40%, var(--accent))" title="118 mentions">interaction</span><span class="cloud-word" style="font-size:1.35rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 27%, var(--accent))" title="94 mentions">language</span><span class="cloud-word" style="font-size:0.95rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 7%, var(--accent))" title="61 mentions">latent</span><span class="cloud-word" style="font-size:1.30rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="89 mentions">memory</span><span class="cloud-word" style="font-size:1.36rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 28%, var(--accent))" title="95 mentions">motion</span><span class="cloud-word" style="font-size:1.75rem;opacity:0.74;color:color-mix(in srgb, var(--accent-2) 47%, var(--accent))" title="133 mentions">multimodal</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="64 mentions">multiple</span><span class="cloud-word" style="font-size:1.66rem;opacity:0.72;color:color-mix(in srgb, var(--accent-2) 43%, var(--accent))" title="124 mentions">object</span><span class="cloud-word" style="font-size:1.44rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 32%, var(--accent))" title="102 mentions">observation</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="69 mentions">perception</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="59 mentions">physical</span><span class="cloud-word" style="font-size:1.43rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 31%, var(--accent))" title="101 mentions">point</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="69 mentions">policy</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">query</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="70 mentions">question</span><span class="cloud-word" style="font-size:2.06rem;opacity:0.82;color:color-mix(in srgb, var(--accent-2) 64%, var(--accent))" title="169 mentions">reasoning</span><span class="cloud-word" style="font-size:0.83rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 1%, var(--accent))" title="53 mentions">reconstruction</span><span class="cloud-word" style="font-size:0.82rem;opacity:0.5;color:color-mix(in srgb, var(--accent-2) 0%, var(--accent))" title="52 mentions">reduce</span><span class="cloud-word" style="font-size:0.99rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 9%, var(--accent))" title="64 mentions">reference</span><span class="cloud-word" style="font-size:0.92rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 5%, var(--accent))" title="59 mentions">region</span><span class="cloud-word" style="font-size:0.98rem;opacity:0.54;color:color-mix(in srgb, var(--accent-2) 8%, var(--accent))" title="63 mentions">same</span><span class="cloud-word" style="font-size:1.89rem;opacity:0.77;color:color-mix(in srgb, var(--accent-2) 55%, var(--accent))" title="149 mentions">scene</span><span class="cloud-word" style="font-size:1.81rem;opacity:0.75;color:color-mix(in srgb, var(--accent-2) 51%, var(--accent))" title="140 mentions">semantic</span><span class="cloud-word" style="font-size:0.85rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 2%, var(--accent))" title="54 mentions">source</span><span class="cloud-word" style="font-size:1.03rem;opacity:0.55;color:color-mix(in srgb, var(--accent-2) 11%, var(--accent))" title="67 mentions">space</span><span class="cloud-word" style="font-size:1.62rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 41%, var(--accent))" title="120 mentions">spatial</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">structure</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="70 mentions">supervision</span><span class="cloud-word" style="font-size:1.39rem;opacity:0.64;color:color-mix(in srgb, var(--accent-2) 29%, var(--accent))" title="97 mentions">support</span><span class="cloud-word" style="font-size:1.07rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 13%, var(--accent))" title="70 mentions">target</span><span class="cloud-word" style="font-size:1.05rem;opacity:0.56;color:color-mix(in srgb, var(--accent-2) 12%, var(--accent))" title="69 mentions">temporal</span><span class="cloud-word" style="font-size:1.29rem;opacity:0.62;color:color-mix(in srgb, var(--accent-2) 24%, var(--accent))" title="88 mentions">token</span><span class="cloud-word" style="font-size:1.46rem;opacity:0.66;color:color-mix(in srgb, var(--accent-2) 33%, var(--accent))" title="104 mentions">trajectory</span><span class="cloud-word" style="font-size:1.19rem;opacity:0.6;color:color-mix(in srgb, var(--accent-2) 19%, var(--accent))" title="80 mentions">understanding</span><span class="cloud-word" style="font-size:0.93rem;opacity:0.53;color:color-mix(in srgb, var(--accent-2) 6%, var(--accent))" title="60 mentions">unified</span><span class="cloud-word" style="font-size:2.55rem;opacity:0.94;color:color-mix(in srgb, var(--accent-2) 89%, var(--accent))" title="233 mentions">video</span><span class="cloud-word" style="font-size:0.88rem;opacity:0.51;color:color-mix(in srgb, var(--accent-2) 3%, var(--accent))" title="56 mentions">view</span><span class="cloud-word" style="font-size:0.89rem;opacity:0.52;color:color-mix(in srgb, var(--accent-2) 4%, var(--accent))" title="57 mentions">vision-language</span><span class="cloud-word" style="font-size:2.77rem;opacity:1.0;color:color-mix(in srgb, var(--accent-2) 100%, var(--accent))" title="266 mentions">visual</span><span class="cloud-word" style="font-size:1.64rem;opacity:0.71;color:color-mix(in srgb, var(--accent-2) 42%, var(--accent))" title="122 mentions">world</span></div>
    </article>
  </div>


  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>21 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>SpaceCast-Bench: Evaluating Predictive Spatial Reasoning in Vision-Language Models</strong>
          <small>Hongxing Li, Jinyue Su, Dingming Li, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Reasoning</span>
<span class="topic-tag">Vision-Language Benchmark</span>
<span class="topic-tag">Predictive Reasoning</span>
<span class="topic-tag">3D Understanding</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-high">17</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2610.12402</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12402">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: a new benchmark for predictive spatial reasoning in vision-language models, going beyond static spatial perception.</p>
        <p class="abstract">Existing spatial reasoning benchmarks mainly test spatial perception: reading off relations already visible in the input. Yet real-world spatial intelligence demands predictive spatial reasoning: constructing a scene from observations, anticipating how an intervention changes it, and reasoning about the unseen outcome. We introduce SpaceCast-Bench, the first benchmark to directly and diagnostically evaluate this capability. Built around an observe-transform-infer framework, its 3,862 questions from 182 real-world scenes span 16 task types at three levels: static perception, local prediction, and global prediction, progressively requiring scene understanding, spatial state updating, and relational inference over unobserved outcomes. Evaluating 21 models exposes a stark gap: the strongest model reaches only 58.0% against 87.2% human performance, while spatially specialized models remain near random chance. Controlled analyses further reveal that bridge views are critical for integrating distributed observations, and that explicit 3D evidence benefits models more reliably than generated outcome images or videos. Fine-tuning on our programmatically generated data lifts Qwen3-VL-4B from 34.0% to 65.7% with macro-average gains across six out-of-domain benchmarks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models</strong>
          <small>Hongxing Li, Yixin Li, Dingming Li, Zixuan Wang, Yuchen Yan, Wenqi Zhang, Weiming Lu, Yongliang Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Spatial Intelligence</span>
<span class="topic-tag">3D Geometry</span>
<span class="topic-tag">Self-Distillation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2610.12355</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12355">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: it targets spatial reasoning in vision-language models by injecting 3D geometric privilege for better spatial understanding.</p>
        <p class="abstract">Spatial reasoning remains a persistent weakness of vision-language models (VLMs), because RGB inputs do not directly provide geometric evidence. Existing remedies either inject 3D into the model at inference, paying architecture and latency costs, or train with outcome rewards that supervise only the final answer. Spatial errors originate in perception: a misjudged depth or direction can be corrected only by the scene&#x27;s true geometry, which the 3D-scanned sources of spatial training corpora already provide. We propose GPD (Geometry-Privileged Distillation), which makes geometric evidence the privilege in on-policy self-distillation (OPSD). For each question, depth, semantic, and bird&#x27;s-eye-view (BEV) cues are rendered as compact text and routed to the teacher alongside the reference answer; a privileged KL, applied only to incorrect trajectories, augments GRPO, and the deployed model remains RGB-only. On the 4B backbone, GPD achieves 57.1 on VSI-Bench and 37.6 average across MindCube, SPARBench, MMSI-Bench, and ViewSpatial, outperforming both GRPO and answer-privileged OPSD across spatial reasoning benchmarks. Ablations confirm the complementarity of 3D and answer privilege, the advantage of question-conditioned routing over full-context injection, and the benefit of restricting distillation to incorrect trajectories.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Agent</summary>
      <div class="queue">

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video</strong>
          <small>Hongyu Li, Manyuan Zhang, Kaituo Feng, Shu Chen, Dian Zheng, Hao Li, Hao Yu, Zhangquan Chen, Zoey Guo, Ray Zhang, Shaofei Huang, Tianrui Hui, Linjiang Huang, Si Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Agent</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Image-Video Reasoning</span>
<span class="topic-tag">Tool-augmented MLLM</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2610.12419</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12419">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 3 very closely: a unified multimodal deep research agent for image/video with new benchmarks and evidence-graph-based supervision.</p>
        <p class="abstract">Single-image, multi-image, and video deep research require different visual operations but share a workflow of visual grounding, external retrieval, and fact composition. A key challenge is to preserve the dependencies linking localized visual anchors, entity relations, source-supported facts, and answer-producing operations. We introduce OneSearch-VL, a unified agent centered on the Visually Grounded Evidence Graph (VGEG), which encodes these dependencies as a shared task-level reference for data construction, process supervision, and operation-level evaluation. Our VGEG-based data engine constructs and verifies multi-image and video questions and filters expert trajectories. Using these data, we assemble OneSearch-VL-SFT-110K and OneSearch-VL-RL-10K for SFT and RL, respectively. We further derive the Evidence-aware Visual-Grounded Rubric reward (EVGR) from VGEG annotations to supervise evidence traceability and visual grounding during RL. For fine-grained evaluation, we construct OneSearch-MI-Bench and OneSearch-Video-Bench, organizing questions by the research operations encoded in their VGEGs. Experiments show that OneSearch-VL-8B improves over Qwen3-VL-8B with tool access by 20.2 and 17.6 percentage points on the two new benchmarks, respectively, while also achieving substantial gains across 7 image benchmarks and VideoDR. Project repository: https://github.com/appletea233/OneSearch-VL</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Spatial Understanding</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding</strong>
          <small>Tianhui Cai, Xinglong Sun, Chao Fang, Zhenxin Li, Rui Song, Jose M. Alvarez, Yunxiang Mao, Jiaqi Ma, Langechuan Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Spatial Understanding</span>
<span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Affordance Prediction</span>
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
          <span>Paper 4 / arXiv:2610.11060</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11060">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 very closely: new spatial understanding for embodied driving via affordance-aware world-action modeling.</p>
        <p class="abstract">World-action models have recently improved autonomous driving by jointly learning future scene prediction and trajectory generation. Most existing approaches model the future primarily through RGB appearance, and recent works have begun to incorporate geometric prediction to improve spatial understanding. However, dense geometry describes the spatial layout of the entire scene without indicating which parts are most relevant to the ego vehicle&#x27;s action. For driving, the model must also identify and anticipate where it can safely move and which regions may pose collision risks. Jointly modeling action-relevant regions and future geometry can provide the policy with both driving-relevant cues and their corresponding spatial structure. We therefore propose AffordDrive3D, an affordance- and geometry-aware world-action model that jointly learns future action-relevant regions and spatial structure. In order to capture the scene semantics and driving context needed for driving affordance prediction, we build AffordDrive3D on a VLM backbone to forecast drivable areas and collision-critical regions that directly affect ego motion, while predicting future geometry from RGB world-model latents. On NAVSIM, AffordDrive3D achieves state-of-the-art performance with 91.3 PDMS and 89.9 EPDMS, demonstrating the effectiveness of jointly modeling future affordances and geometry for trajectory planning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>Mid-Training Language Models on Raw Video</strong>
          <small>Jaedong Hwang, Xiaoqian Shen, Ernie Chang, Changsheng Zhao, Chong Zhou, Saksham Suri, Qi Qian, Zechun Liu, Lemeng Wu, Qinsi Wang, Raghuraman Krishnamoorthi, Wei Wen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Foundation Models</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Multimodal Pretraining</span>
<span class="topic-tag">Raw Video</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-high">14</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2610.11019</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11019">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: self-supervised mid-training on raw video for multimodal foundation models, with clear downstream gains on video and image tasks.</p>
        <p class="abstract">Multimodal large language models learn mostly from paired image-text data or annotated video, and raw web video is rarely used to further train an existing language model. We study whether raw video, with no captions and no text loss, can serve as mid-training data for a pretrained language model. Frames are encoded into continuous visual tokens, and the language model learns to predict the next visual token. We mid-train Qwen3-1.7B on raw clips from YT-Temporal-1B and then apply the same image-text instruction tuning to it and to the model without mid-training, so that the two differ only in mid-training. The mid-trained model scores 2.9 points higher on average across four video benchmarks and 5.1 points higher across ten image benchmarks, spanning perception, document, and chart tasks. Text performance is preserved even though mid-training includes no text, with an average of 48.9 across 14 text benchmarks compared with 48.0 for the model without mid-training. Analyses across training show that the image and video gains emerge within 30% of training and plateau thereafter, varying by less than 0.5 points. Predicting captions fails to outperform next-visual-token prediction, demonstrating that video mid-training can remain purely self-supervised without the computational overhead or labeling noise of automated captioning.</p>
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
          <strong>ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills</strong>
          <small>Hongxing Li, Dingming Li, Yixin Li, Yong Du, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">VLM Agents</span>
<span class="topic-tag">Skill Learning</span>
<span class="topic-tag">Reinforcement Learning</span>
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
          <span>Paper 6 / arXiv:2610.12403</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12403">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: embodied/VLM agents with a new visual-native skill learning method, focusing on action-state structure rather than generic language skills.</p>
        <p class="abstract">Skill-augmented agents improve sample efficiency by distilling successful trajectories into reusable strategies. Yet most existing approaches remain text-centric, linearizing spatial layouts and action-state correspondences into language that loses critical geometric structure. Recent efforts have begun incorporating visual evidence, but construct and update skills separately from policy optimization, leaving their mutual improvement underexplored. We propose ViSkill, a visual-native skill learning framework that encodes successful interactions as composite visual skill cards directly accessible to VLM agents. Retrieved skills guide both inference and reward shaping, while successful trajectories are distilled back into the library, forming a closed feedback loop in which skill accumulation and policy improvement reinforce each other. An optional cold-start mechanism further accelerates early-stage learning. Evaluated on Sokoban, FrozenLake, and PrimitiveSkill, ViSkill achieves an overall success rate of 0.89, rising to 0.91 with cold-start initialization, outperforming all evaluated proprietary and open-source baselines while converging faster than standard PPO. Our code is available at https://github.com/ZJU-REAL/ViSkill.</p>
      </div>
    </details>


    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation</strong>
          <small>Ruicheng Zhang, Kaiwen Shen, Jiaqi Hou, Shuhan Yang, Junchao Huang, Kewei Zhang, Jun Zhou, Li Jiang, Shen Zhao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Referring Expression Segmentation</span>
<span class="topic-tag">Closed-Loop Policy</span>
<span class="topic-tag">Multimodal RL</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2610.12107</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12107">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: an embodied, closed-loop perception-action method for generalized referring expression segmentation with new action-style optimization.</p>
        <p class="abstract">Generalized referring expression segmentation (GRES) requires dynamically balancing high-level semantics for identifying a variable number of language-specified referents with fine-grained visual evidence for precise boundary delineation. This requirement challenges existing cascaded vision-language architectures, which typically rely on static feature interfaces and single-pass mask prediction, limiting adaptive perception and geometric correction. We introduce ContourVLA, a vision-language-action policy that recasts GRES as a closed-loop visuomotor process, in which editable contours serve as explicit policy states that condition multimodal perception and are updated by geometric action chunks. Evolution-Aware Semantic Scheduling (EASS) couples contour-guided bidirectional boundary sampling with state-conditioned routing of multilevel multimodal features, adapting perception to each contour state. Following supervised initialization, Dustbin-Augmented Entropic Credit Transport GRPO (DECT-GRPO) jointly optimizes discrete grounding and continuous contour actions with instance-level credits. Its rollout rewards and credits are derived from soft prediction-target correspondences that account for false positives and missed targets. ContourVLA improves gIoU over the strongest evaluated baselines by 8.7, 2.8, and 2.7 points on gRefCOCO val, testA, and testB, respectively, and achieves the highest mIoU across all eight RefCOCO, RefCOCO+, and RefCOCOg splits.</p>
      </div>
    </details>


    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>What 30,000 Hours of Ego-centric Video Does Not Teach</strong>
          <small>Jiahua Dong, Anurag Bagchi, Yash Jangir, Muhammad Zubair Irshad, Sergey Zakharov, Martial Hebert, Homanga Bharadhwaj, Yu-Xiong Wang, Vitor Campagnolo Guizilini, Pavel Tokmakov</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Egocentric Video</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Empirical Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 14 / arXiv:2610.12464</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12464">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it studies embodied/world-model learning from large-scale egocentric video and highlights an important empirical gap between agent and object modeling.</p>
        <p class="abstract">World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment. We ask how far scaling ego-centric human video takes them, using a dataset of 30,000 hours spanning over 1,000 scene types and 14,000 contributors. Rather than relying on opaque downstream metrics, we directly evaluate agent and object-interaction fidelity on a challenging out-of-distribution benchmark. Increasing training data by 100x improves both, but unevenly: the agent is modeled well, while object fidelity remains far lower and improves slowly. We show that the agent gains need not come from data, and a careful visual conditioning design saturates fidelity with a fraction of it, which lets us measure object fidelity on its own and discover its saturation point. We then introduce a supervision scheme that shifts capacity from scene appearance toward object dynamics, improving object fidelity though a substantial gap remains. Finally, our conclusions transfer to downstream humanoid modeling. Overall, our results suggest that scaling ego-centric data brings agent modeling close to its limit while leaving its effects on the world far behind, and that closing this gap will depend on how models are trained, not only on how much data they see.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Camera Trajectory Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>TKCAM: Text and Keyframe to Camera Trajectory Generation</strong>
          <small>Haozhe Yang, Zhiyang Dou, Zekai Gu, Cheng Lin, Wenping Wang, Yuan Liu, Taku Komura</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Camera Trajectory Generation</span>
<span class="topic-tag">Benchmark &amp; Dataset</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Multimodal Conditioning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2610.11105</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11105">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: builds a new benchmark/dataset and method for text-and-keyframe conditioned camera trajectory generation, relevant to simulator/camera-motion style embodied vision.</p>
        <p class="abstract">Generating high-quality and controllable camera motion is essential for AI-assisted cinematography, video synthesis, and 3D scene understanding. We introduce TKCAM, a Text- and Keyframe-conditioned CAMera-motion synthesis framework based on generative masked modeling. We represent camera dynamics using a 12-dimensional kinematic feature comprising position, velocity, and a continuous rotation representation and discretize them into hierarchical motion tokens via a Residual Vector Quantizer (RVQ). A two-stage masked transformer architecture then learns to reconstruct and refine these tokens, utilizing explicit self- and cross-attention modules for multimodal conditioning. A central feature of our framework is sparse visual keyframe conditioning: users can provide free-form text prompts together with RGB observations at selected timestamps, which provide temporally localized visual guidance for generating coherent in-between trajectories. Furthermore, to advance evaluation standards, we curate RealEstate10K-Cap, a large-scale text-camera dataset, and establish a cross-domain benchmark with a Universal CLaTr Evaluator. Extensive experiments demonstrate that TKCAM surpasses recent state-of-the-art baselines on Fr\&#x27;echet distance (FID), text-motion matching scores, and retrieval metrics (R@K), while additional analyses evaluate temporal smoothness and cross-domain generalization. Code is available at https://github.com/linearalgebrayhz/TKCAM.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Point Cloud Representation</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Point-Focused Attention Meets Context-Scan State Space: Robust Biological Visual Perception for Point Cloud Representation</strong>
          <small>Kanglin Qu, Pan Gao, Qun Dai, Yuanhao Sun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Point Cloud Representation</span>
<span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Biomimetic Attention</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2610.11342</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11342">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a vision foundation-style point cloud representation model with biologically inspired attention/context mechanisms and broad downstream applications.</p>
        <p class="abstract">Synergistically capturing intricate local structures and global contextual dependencies has become a critical challenge in point cloud representation learning. To address this, we introduce PointLearner, a point cloud representation learning network that closely aligns with biological vision which employs an active, foveation-inspired processing strategy, thus enabling local geometric modeling and long-range dependency interactions simultaneously. Specifically, we first design a point-focused attention, which simulates foveal vision at the visual focus through a competitive normalized attention mechanism between local neighbors and spatially downsampled features. The spatially downsampled features are extracted by a pooling method based on learnable inducing points, which can flexibly adapt to the non-uniform distribution of point clouds as the number of inducing points is controlled and they interact directly with point clouds. Second, we propose a context-scan state space that mimics eye&#x27;s saccade inference, which infers the overall semantic structure and spatial content in the scene through a scan path guided by the Hilbert curve for the bidirectional S6. With this focus-then-context biomimetic design, PointLearner demonstrates remarkable robustness and achieves state-of-the-art performance across multiple point cloud tasks.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">GUI Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents</strong>
          <small>Jiaming Zhang, Xuan Wang, Fuyao Zhang, Yang Cao, Lingjuan Lyu, Wei Yang Bryan Lim</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">GUI Agents</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Safety</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2610.11942</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11942">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: it introduces a new embodied/GUI world-model method and a benchmark focused on verification from action-conditioned transitions, a novel angle many prior GUI agents ignore.</p>
        <p class="abstract">A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the transition rather than of the screen, and a monitor that inspects only screens can be defeated by reusing a legitimate one. Judging a transition requires an expectation of what should have followed the action. Existing GUI world models provide one, but they output it as text, code, or images, so checking it against the observed screen requires a second model to judge the two. We argue that a world model meant for verification should instead predict in the space in which observations are encoded, and present LGWM, a decoder-free, action-conditioned world model that predicts the representation of the next screen directly, trained without semantic annotation on 1.85M real GUI transitions. Verification reduces to a vector comparison, and the same signal reveals whether a mismatch is harmful. We evaluate on RSWT-BENCH, a diagnostic where each credential screen appears under both a legitimate and a hijacked transition, so detectors that see only the screen are at chance by construction. The training-free score reaches 0.987 AUC at 17 ms per decision, on par with the strongest closed-source VLMs and about ten AUC points above generative GUI world models at over three orders of magnitude lower latency. The residual direction reaches 0.953 AUC at separating harmful from benign violations, where prompted VLMs are near chance. Further analyses show that the prediction is a usable future state rather than an anomaly score. World models have mostly served as simulators or planners; our results point to a third role, verification, for which predicting in representation space is the natural design.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs</strong>
          <small>You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">3D Generation</span>
<span class="topic-tag">World Modeling</span>
<span class="topic-tag">Multi-View Video</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.GR</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2610.12461</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12461">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it builds on a vision-language model to synthesize dynamic 3D scenes and introduces a new 3D world representation/evaluation for vision foundation model applications.</p>
        <p class="abstract">Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph: a dynamic scene with vivid, diverse motion looping seamlessly from any viewpoint. A vision-language model infers plausible dynamics and guides a video model to synthesize a reference video, which we lift and complete into multi-view videos. To learn from this imperfect supervision, we propose Inconsistency-Robust Periodic 4DGS: a Fourier-series deformation field guarantees looping by construction, while a Grounded Drift Field anchored at the reference view absorbs cross-view inconsistency. Unlike prior Eulerian methods limited to fluid-like motion, we capture general deformation, object motion, and illumination change. We introduce a ground-truth-free evaluation covering vividness, naturalness, loop seam coherence, and scene quality. On 39 reconstructed and generated scenes, OuroWorld outperforms all baselines and wins 70.8%-99.0% of user-study comparisons. Project page: https://ouroworld.userwei.com</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Reconstruction</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>PCAsplat: Gaussian Splatting with Local PCA Regularization</strong>
          <small>Vitor Matias, Filipe Nascimento, Kiyohiro Nakayama, Jo\~ao Paulo Lima, M\&#x27;arcus Lobo, Gordon Wetzstein, Leonidas Guibas, Afonso Paiva, Tiago Novello</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Reconstruction</span>
<span class="topic-tag">Gaussian Splatting</span>
<span class="topic-tag">Geometry Regularization</span>
<span class="topic-tag">Vision Foundation Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.GR</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2610.11011</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11011">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: a vision foundation model/3D reconstruction method that improves Gaussian splatting with geometry-aware regularization.</p>
        <p class="abstract">Gaussian splatting has emerged as a flexible representation for 3D reconstruction from posed images. However, existing methods are optimized primarily using rasterization-based losses, which supervise a splat only when it contributes to sampled camera rays. Gaussians that are occluded or contribute little to the sampled view therefore receive weak or no geometric gradients and may drift away from the underlying surface, producing undesired floaters. We introduce PCAsplat, a geometry-aware regularization framework for Gaussian splatting based on differentiable local principal component analysis (PCA). Our PCA regularizer acts directly on neighborhoods of Gaussian centers and can therefore update Gaussians that do not contribute to the current training view. We regularize the PCA eigenvalues to encourage Gaussians to move to the underlying surface with isotropic tangent-plane coverage. We also align each Gaussian normal with the PCA-estimated neighborhood normal to enforce consistent orientation. Experiments on DTU, Tanks and Temples, and NeRF Synthetic show that the splats produced by PCAsplat better approximate samples of the reference surface while substantially reducing undesired floaters. These surface-aligned splats enable downstream geometry-processing tasks, including point cloud segmentation, and direct Poisson reconstruction. Additionally, PCAsplat remains competitive under conventional novel view synthesis and mesh extraction tasks. Code will be released.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>DiscoVL: Unveiling Disentangled C ross-Modal Representation Learning via Orthogonal Adversarial Regularization for V ision-Language Models</strong>
          <small>Mengping Dong, Jinbao Li, Fei Li</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Representation Learning</span>
<span class="topic-tag">Few-shot Transfer</span>
<span class="topic-tag">Prompt Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 17 / arXiv:2610.11113</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11113">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: vision-language model representation learning and generalization improvement for VLM adaptation.</p>
        <p class="abstract">Pre-trained vision-language models excel across varied perception tasks, but adapting them to novel downstream settings without sacrificing generalization remains non-trivial. Existing parameter-efficient prompt learning method often yields inconsistent representations and fails to account for semantic distribution shifts. In this work, we present DiscoVL, a disentangled cross-modal representation learning framework that couples orthogonal adversarial regularization with structured cross-modal alignment for vision-language models. To address the insufficient cross-modal interaction, our DiscoVL designs a multi-branch low-rank residual aligner that decomposes representations into subspaces and enables bidirectional cross-modal feedback between visual and textual streams at each layer. Furthermore, while conventional triplet constraints overfit features to class centroids, we design an orthogonal regularization for adversarial triplet loss, which prevents centroid collapse and substantially boosts generalization. Evaluations on 15 benchmarks demonstrate that DiscoVL delivers consistent improvements over state-of-the-art methods for base-to-novel generalization, cross-dataset evaluation, and few-shot learning</p>
      </div>
    </details>


    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>V-CoLA: Vision Token Compression with Linear Attention</strong>
          <small>Hao Jiang, Yiru Mao, Tianpeng Bu, Hao Zhou, Hongtao Duan, Wang Jing, Bowen Xu, Xin Chen, Lulu Hu, Bin Yang, Yongliang Tao, Minying Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Token Compression</span>
<span class="topic-tag">Efficient Inference</span>
<span class="topic-tag">Linear Attention</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2610.11251</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11251">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it improves vision token compression for vision-language models, a practical efficiency method for vision foundation model systems.</p>
        <p class="abstract">Vision-language models (VLMs) have demonstrated impressive capabilities but suffer from substantial computational overhead, as vision tokens dominate the input sequence. This motivates vision token compression as a key direction to alleviate the burden. However, with the emergence of hybrid architectures incorporating linear attention (\eg, Qwen3.5), prior methods designed for softmax attention struggle to generalize. Our analysis reveals that both attention- and similarity-based approaches suffer notable performance degradation, underscoring the urgent need for compression methods tailored to this regime. To this end, we propose \textbf{V-CoLA}, an efficient training-free token compression framework specifically designed for linear attention. V-CoLA introduces a novel \textit{uniqueness-aware importance criterion} for identifying critical vision tokens, coupled with an \textit{adaptive token merging strategy} that performs compression. All components are optimized at the implementation level to remain compatible with the chunk-wise parallelism of linear attention, ensuring strong practical value. Extensive experiments across multiple benchmarks demonstrate the superiority of V-CoLA: it achieves 99.5\% of the original performance with only 50.0\% of vision tokens, and over 88.0\% with as few as 12.5\%, while delivering a 1.86$\times$ to 6.15$\times$ prefill speedup.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Interactive Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>Skill-V: Verifiable Self-Evolving Skill Library for Interactive Agents</strong>
          <small>Jie Ma, Zhipeng Qian, Yufei Ma, Zihan Liang, Jiayi Ji, Qingpeng Cai, Ben Chen, Peng Jiang, Xiaoshuai Sun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Interactive Agents</span>
<span class="topic-tag">Skill Learning</span>
<span class="topic-tag">Verification</span>
<span class="topic-tag">Web/ALFWorld</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2610.11781</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11781">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately: it is an embodied/interactive-agent method for building and revising a skill library, though it is less directly about spatial understanding or VLLMs.</p>
        <p class="abstract">Interactive agents can turn experience into reusable skills, yet existing self-evolving skill libraries primarily improve by accumulating new knowledge. Failures may lead to new skills, while previously stored skills are less often revisited as new evidence arrives. However, growth alone does not ensure reliability, as a retrieved skill may be inapplicable under the current task conditions, and an existing skill may encode a mis-specified operational boundary. Reliable skill evolution therefore requires not only adding knowledge, but also testing and revising what is already stored. We introduce Skill-V, a verifiable self-evolving skill library. To make stored knowledge testable, we propose representing skills as versioned, falsifiable contracts that link semantic intent to observable behavioral criteria. We use environment outcomes to drive library evolution. Specifically, task failures motivate skill addition, while disagreements between contract evaluations and task outcomes guide revisions to existing skill boundaries. To validate these revisions, we require them to preserve protected semantic constraints and satisfy non-regression criteria for rubric-outcome metrics on historical replay evidence. Finally, we employ an applicability-aware filter to exclude candidates judged confidently inapplicable to the current task. Across ALFWorld and WebShop, Skill-V achieves success rates of 95.3% and 85.9%, respectively, while maintaining a more compact skill library than growth-oriented baselines. Applicability-aware filtering reduces incorrect skill invocations, and outcome-grounded revisions correct mis-specified skill boundaries without degrading performance on previously observed evidence. These results show that reliable skill evolution requires more than accumulating experience: the library must learn which knowledge to retain, when to revise it, and when it should be applied.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Scene Flow</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting</strong>
          <small>Jiuming Liu, Jianing Li, Mengmeng Liu, Hongyang He, Hesheng Wang, Per Ola Kristensson</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Scene Flow</span>
<span class="topic-tag">Temporal Memory</span>
<span class="topic-tag">3D Motion Estimation</span>
<span class="topic-tag">Autoregressive Forecasting</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 20 / arXiv:2610.10759</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.10759">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1 in the embodied/scene-understanding sense: sequential 3D motion estimation with memory and forecasting, though not a benchmark paper.</p>
        <p class="abstract">Scene flow can capture low-level 3D motion displacements in dynamic scenarios. Early pairwise estimators relying on instantaneous two-frame motion lack long-term temporal correlation and also struggle with poor extrapolation ability in future prediction. Although some recent methods attempt to explore multi-frame scene flow estimation in a sequence-to-sequence manner, they typically suffer from heavy computational overhead with increasing input frames and long-horizon prediction degradation due to ineffective motion propagation. To address these problems, we propose a novel memory-enhanced sequential scene flow pipeline, called MESSENGER. To sufficiently mine long-term temporal dependencies naturally within consecutive sequences, a memory buffer is designed by explicitly storing multiple history flow estimates and latent states. For each input frame, the temporally stored flows and states are correlated and retrieved to predict the current initialized flow in a next-frame forecasting manner. Furthermore, we develop an uncertainty-aware reweighting module to filter unreliable retrievals and mitigate accumulated errors. Extensive experiments on nuScenes and Argoverse 2 demonstrate state-of-the-art performance of our MESSENGER, reducing EPE3D by 71.6% on nuScenes and 67.7% on Argoverse 2 in long-horizon future extrapolation. This superiority can be attributed to our designed autoregressive forecasting paradigm, which naturally forces the network to progressively learn the next-frame distribution based on history observations. Code will be released at https://github.com/liujiuming123/Messenger.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link20">
      <summary class="paper-row-summary">
        <span class="queue-index">21</span>
        <span class="paper-row-copy">
          <strong>Towards Unified Evaluation of Prompt Enhancers for Video Generation</strong>
          <small>Yawen Shao, Yubo Zhu, Ziyun Dai, Zixun Fang, Kai Zhu, Zeyinzi Jiang, Yufeng Ai, Siyang Sun, Haolan Xue, Yu Shang, Yuxiang Bao, Zoubin Bi, Jingming Luo, Jie Xiao, Chaojie Mao, Zhehan Kan, Hongchen Luo, Yu Liu, Sheng Zhong, Wei Tong, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Prompt Engineering</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 21 / arXiv:2610.11736</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11736">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 partially: introduces a benchmark for evaluating prompt enhancers in video generation, which is useful but not directly embodied AI.</p>
        <p class="abstract">Modern video generators can realize increasingly complex visual narratives, positioning the prompt enhancer (PE) as a critical bridge from concise user instructions and multimodal references to structured cinematic plans. However, existing PE evaluation relies on rendered videos, imposing substantial computational and human costs, slowing PE training and iteration, and conflating PE quality with downstream generator behavior. To address this gap, we introduce PEBench, the first unified benchmark for direct PE evaluation across text-to-video, image-to-video, and reference-to-video prompt enhancement. It comprises 1,100 expert-verified cases and 1,005 visual assets, spanning 35 fine-grained tasks with diverse temporal, cinematic, audiovisual, and multi-reference requirements. In addition, we develop PEBench evaluation, an evidence-grounded framework that combines modality-aware fact extraction with rubric-based assessment across 24 criteria. Our systematic evaluation of representative open- and closed-source PE methods reveals an emerging shift from fine-grained descriptive expansion toward intent-preserving cinematic planning, while the caption-reconstruction and forward-refinement methods show complementary strengths in cinematic coverage and semantic fidelity or internal coherence, respectively. Human validation shows that PEBench scores align closely with expert judgments of enhanced prompts and downstream videos from Wan3.0 and MiniMax-H3, indicating that prompt-level evaluation reliably reflects downstream utility.</p>
      </div>
    </details>


    <details class="paper-row" id="link21">
      <summary class="paper-row-summary">
        <span class="queue-index">22</span>
        <span class="paper-row-copy">
          <strong>Parametric Trajectory Distillation for Few-Step Video Generation</strong>
          <small>Lan Feng, Peter Karkus, Maximilian Igl, Julius Berner, Yuxiao Chen, Shuhan Tan, Alexandre Alahi, Boris Ivanovic, Marco Pavone</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Diffusion Distillation</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Few-step Sampling</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 22 / arXiv:2610.11498</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11498">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Relevant to criterion 4 only in a broad generative-modeling sense; it is about few-step video generation, not vision foundation models or embodied AI.</p>
        <p class="abstract">Video diffusion and flow models require many sequential evaluations, making generation computationally expensive. Few-step distillation reduces this cost but poses a capacity allocation problem: a student must match the teacher&#x27;s iterative generation with far less sequential computation. Existing trajectory methods ask the student to reproduce teacher transitions that are highly curved at high noise, which can exceed its capacity and degrade fine detail. We introduce Parametric Trajectory Distillation (PTD), which lets the student parameterize teacher trajectory segments as polynomials and learn from teacher guidance along its own predicted path. PTD is designed to let the learned curvature adapt to the backbone&#x27;s predictive capacity, preserving motion and diversity. The curvature head is used only in training; inference keeps the original backbone architecture. On Wan2.1-14B, four-step PTD sets a new state of the art for trajectory distillation, significantly improving dynamic quality and naturalness over PDD, the best-performing trajectory-only method on this model, under the same training setting. On the 33B audio-video MiniMax-H3, LoRA-trained PTD significantly improves diversity and naturalness over the state-of-the-art LightX2V Turbo. Blinded human votes give PTD 55.1% and 63.4% preference shares against PDD and LightX2V Turbo. Project page: https://alan-lanfeng.github.io/PTD/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Efficient Inference</summary>
      <div class="queue">

    <details class="paper-row" id="link24">
      <summary class="paper-row-summary">
        <span class="queue-index">25</span>
        <span class="paper-row-copy">
          <strong>FastJEV: Understanding Redundancy for Compact JEV Inference</strong>
          <small>Jie Ma, Jie Gao, Yihang Liu, Zhike Qiu, Junle Li, Chongyi Zhuang, Jiayi Ji, Xiaoshuai Sun</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Efficient Inference</span>
<span class="topic-tag">Multimodal Decision Models</span>
<span class="topic-tag">Redundancy Reduction</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 25 / arXiv:2610.11379</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11379">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: it studies compact inference and redundancy reduction in multimodal decision models, but it is more about efficient execution than new spatial understanding.</p>
        <p class="abstract">JEV models make multimodal decisions by directly scoring candidates. Although the common context is encoded once, candidate evaluation can still repeat matching token histories, duplicate inference states, and execute the full backbone. In this paper, we study these sources of redundancy and present FastJEV for compact candidate evaluation. We jointly organize history reuse and state storage, since sharing computation requires preserving states for later branches. We first introduce shared context anchoring to reuse recurrent initial states and omit unused final recurrent caches. We extend this reuse through candidate prefix sharing, retaining the intermediate states needed by subsequent branches. To further reduce the depth of these paths, we apply decision guided pruning based on relative score changes measured on a small unlabeled set. Our method retains full context encoding and all candidates without additional training. We evaluate FastJEV across three OmniJev model sizes on five public benchmarks and reconstructed LIBERO-10 offline questions. At the selected pruning budgets, the complete method reduces candidate depth by 43.75% to 45.83%, while retaining 93.66% to 97.52% of the original task scores on average across the six evaluation sets. Through controlled experiments, we show how candidate overlap and branching structure affect the execution cost of history reuse. In our implementation, candidate prefix sharing can reduce repeated computation while increasing latency. These findings motivate designing sharing granularity and execution schedules together for efficient JEV inference.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video-Text Retrieval</summary>
      <div class="queue">

    <details class="paper-row" id="link25">
      <summary class="paper-row-summary">
        <span class="queue-index">26</span>
        <span class="paper-row-copy">
          <strong>VEDJE: Video-Efficient Discriminative Joint Encoder for Scalable Video-Text Retrieval</strong>
          <small>Shahaf Wagner, Gabriele Serussi, Dan Ben Ami, Tomer Galanti, Chaim Baskin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video-Text Retrieval</span>
<span class="topic-tag">Efficient Encoding</span>
<span class="topic-tag">Cache Compression</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">8</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 26 / arXiv:2610.11850</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11850">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No strong match to the listed criteria; mainly a video-text retrieval efficiency paper, though it is adjacent to vision-language modeling.</p>
        <p class="abstract">Finding the right video often requires distinguishing similar scenes in which different events occur. Joint matching improves retrieval, but processing rich video representations for each query is costly. VEDJE compresses features within sampled frames while keeping their representations separate in a reusable cache. Feature-change prediction supplies an auxiliary training signal that improves retrieval from the compressed cache without adding work at query time. On MSR-VTT, MSVD, DiDeMo, and ActivityNet, VEDJE improves R@1 over matched first-stage retrievers in both retrieval directions. On MSR-VTT, it reaches 59.8 text-to-video R@1 with a fine-tuned VideoCLIP-XL first stage. In the VideoPrism configuration, shrinking the per-video cache fourfold to 12 KiB preserves text-to-video recall within 0.2 points. These results show that accurate video search can operate on compact evidence, encoded once and reused as new queries arrive.</p>
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
      <summary class="topic-heading">Agentic AI</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>Environmental Feedback Modeling Matters: Rethinking Feedback Treatment in Agentic Hindsight Self-Distillation</strong>
          <small>Hangxi Guo, Fengyuan Liu, Yue Wang, Yuhua Qi, Haoyi Xiong, Fei Sun, Mengnan Du</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agentic AI</span>
<span class="topic-tag">Self-Distillation</span>
<span class="topic-tag">Environmental Feedback</span>
<span class="topic-tag">Interactive Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2610.11384</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11384">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately well: a new agentic self-distillation method using environmental feedback modeling for interactive agents.</p>
        <p class="abstract">Reinforcement learning is commonly used to train language agents in interactive environments, but cannot be directly applied when rewards are unavailable. Recent methods use environmental feedback as privileged context for hindsight self-distillation, but our analysis suggests that simply conditioning the teacher on feedback is insufficient, motivating us to rethink how environmental feedback is used in agentic self-distillation. Given that environmental feedback contains rich supervision for modeling how the environment responds to agent actions, we introduce \textit{agentic SElf-distilLation with environmental Feedback modeling} (SELF), a framework that jointly optimizes environmental feedback modeling and hindsight self-distillation. SELF learns to predict environmental responses while distilling guidance from a feedback-conditioned self-teacher into the policy. Our analysis reveals a mutually reinforcing mechanism: environmental feedback modeling strengthens hindsight supervision and policy learning, while self-distillation enhances the model&#x27;s ability to model environmental feedback. With Qwen3-8B, SELF outperforms SDPO and GRPO by 6.4 and 4.1 percentage points in $\tau$-bench success rate, and by 10.71 and 3.57 percentage points in AppWorld task goal completion, respectively. These results show that SELF uses environmental feedback more effectively within agentic self-distillation, improving agent capabilities.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks</strong>
          <small>Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov, Haitham Bou-Ammar, Weilin Luo, Jun Wang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied Reasoning</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Continual Learning</span>
<span class="topic-tag">Agent Memory</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
<span class="category-tag">cs.CV</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2610.11794</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.11794">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 moderately: it proposes a model-based continual learning / world-modeling approach for interactive agents, but it is not specifically centered on spatial understanding or new benchmarks.</p>
        <p class="abstract">Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives. Yet limited observations can support multiple world models that explain past interactions but predict different outcomes in unseen states. We introduce Memento 3, building on the Memento series to enable frozen LLM agents to continually learn explicit world models through external memory. The agent maintains a natural-language rulebook as persistent semantic memory, recording revisable hypotheses about environment dynamics while leaving unknown aspects underspecified. It compiles this rulebook into executable code for prediction and planning. Through a continual loop of observation, reflection, rule revision, compilation, and verification, the agent uses prediction errors to refine both the rulebook and its code. Updated code is accepted only when the LLM judges it faithful to the rulebook and cell-exact replay reproduces the observed transitions. We investigate this process as a model-based route to recursive self-improvement (RSI): the agent autonomously explores the environment, revises its world model, and uses verified updates to guide subsequent interaction and learning, while the underlying LLM remains fixed. A population extension maintains multiple world models in parallel, sharing interaction evidence and using their predictions to guide exploration. On ARC-AGI-3, the single-model agent clears every level of all 25 public games, achieves a mean Relative Human Action Efficiency (RHAE) of 100.0, and uses 44% of the human action count. In an Atari Pong case study, a learned feedback controller wins 21:0 in each of three evaluated episodes with different openings, without further LLM calls.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models</strong>
          <small>Hongyu Shi, Sen Zhao, Zuyu Zhang, Lifeng Shen, Ding Zou, Xinyu He, Xu Zhang, Qinghua Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Robot Control</span>
<span class="topic-tag">Memory Mechanisms</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2610.12090</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12090">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it proposes a new method for vision-language-action embodied control with latent reasoning reuse and closed-loop robot action improvement.</p>
        <p class="abstract">Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions. While existing methods learn to generate or refine such states for each policy query, they discard successful reasoning after execution and therefore reconstruct similar computation from scratch. We present Reasoning and Flow Memory (FLOWMEM), a unified VLA model that turns successful latent computation into reusable reasoning experience. Rather than appending a fixed retrieved context, FLOWMEM dynamically retrieves and recomposes compatible latent fragments as the embodied context evolves, forming a reasoning route that follows the temporal structure and progress of successful computation. The route is then refined using current visual and proprioceptive evidence before it conditions action generation. Experiments on RoboMME and LIBERO-Plus show that FLOWMEM attains 48.0% and 77.3% success, outperforming memory-free policies by 1.7 and 4.1 percentage points, respectively. These results demonstrate the value of reusing successful latent computation for closed-loop VLA control.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Representation Learning</summary>
      <div class="queue">

    <details class="paper-row" id="link22">
      <summary class="paper-row-summary">
        <span class="queue-index">23</span>
        <span class="paper-row-copy">
          <strong>HRIL: Learning Multimodal Synergy via Higher-Order Tensor Modeling</strong>
          <small>Qun Dai, Liangjian Wen, Jiang Duan, Yong Dai, Dongkai Wang, Maolin Wang, Mingjie Wang, Jianzhuang Liu, He Yan, Zhao Kang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Representation Learning</span>
<span class="topic-tag">Higher-order Statistics</span>
<span class="topic-tag">Self-supervised Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 23 / arXiv:2610.12393</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12393">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Relevant to criterion 4 in a general multimodal representation sense, but not specifically vision foundation models or embodied AI.</p>
        <p class="abstract">Self-supervised multimodal representation learning has achieved remarkable success across diverse domains, yet capturing synergistic information remains challenging due to the complexity of cross-modal interactions. Unlike the shared information across individual modalities, synergy arises when task-relevant signals emerge only from the joint configuration of multiple modalities and cannot be recovered from any modality in isolation. This work focuses on how to preserve the information capacity for such synergistic signals in multimodal representations. The key observation is that synergistic information is reflected in higher-order statistical dependence among modalities, which provides a principled target for explicitly modeling joint interactions. Motivated by this insight, we propose Higher-order Representation and Information Learning (HRIL), which constructs an empirical cross-moment tensor over modality embeddings to represent multi-way interactions. HRIL employs Tucker decomposition to obtain a core tensor, complemented by a synergy-aware regularizer that prevents energy concentration and preserves higher-order coupling capacity for synergistic information capture. Experiments on the controlled synergy task and real-world benchmarks demonstrate consistent improvements over existing multimodal contrastive methods, with notable gains on tasks dominated by synergistic interactions. Code is released at https://github.com/brightest66/HRIL.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Agent Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link23">
      <summary class="paper-row-summary">
        <span class="queue-index">24</span>
        <span class="paper-row-copy">
          <strong>When Should Agents Think? Adaptive Reasoning via Cross-Turn Estimation</strong>
          <small>Yiruo Cheng, Shen Huang, Xiaoshuai Song, Jiejun Tan, Guanting Dong, Pengjun Xie, Ji-Rong Wen, Zhicheng Dou</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Agent Reasoning</span>
<span class="topic-tag">Adaptive Computation</span>
<span class="topic-tag">RL for Agents</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
<span class="category-tag">cs.CL</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 24 / arXiv:2610.12061</span>
          <a class="paper-action" href="https://arxiv.org/abs/2610.12061">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Relevant to criterion 3 only indirectly: adaptive reasoning for agents, but not clearly embodied AI, spatial intelligence, or a new simulator/benchmark.</p>
        <p class="abstract">Large language model (LLM)-based agents have demonstrated strong capabilities on complex tasks. They typically perform reasoning before each action throughout an interaction trajectory. However, reasoning may not be necessary at every turn, as reasoning produced earlier can continue to support subsequent actions. A key challenge is therefore to determine when existing reasoning remains sufficient and when a new reasoning step is needed, without relying on costly generation-based verification. We find that decreases in the likelihood of subsequent reference actions after removing additional reasoning closely track whether those actions remain recoverable given earlier reasoning, providing an effective and lightweight signal for estimating cross-turn action support. Based on this observation, we propose Reasoning Adaptation through Cross-Turn Estimation (RACE), a training approach for adaptive agent reasoning. RACE introduces a Likelihood-Guided Progressive Reasoning Cover Detection (LoGiC) procedure that progressively identifies reasoning turns whose removal has limited impact on the current and subsequent reference actions. The resulting removal signals are incorporated into both supervised fine-tuning and agentic reinforcement learning, enabling the policy to learn when to reason and when to act directly. Extensive experiments on four representative agent benchmarks show that RACE substantially reduces reasoning cost while maintaining or improving task performance.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

        <a class="archive-link" href="past_arxiv/2026-10-08.html">
          <span>October 08, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-07.html">
          <span>October 07, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-05.html">
          <span>October 05, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-02.html">
          <span>October 02, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-10-01.html">
          <span>October 01, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-30.html">
          <span>September 30, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-29.html">
          <span>September 29, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-28.html">
          <span>September 28, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-25.html">
          <span>September 25, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-24.html">
          <span>September 24, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-23.html">
          <span>September 23, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-22.html">
          <span>September 22, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-09-21.html">
          <span>September 21, 2026</span>
        </a>


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
