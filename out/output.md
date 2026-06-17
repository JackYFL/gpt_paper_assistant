

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
      <p class="eyebrow">Daily ArXiv / June 17, 2026</p>
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
      <strong>17</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>11.1</strong>
    </div>


    <div class="metric">
      <span>Source</span>
      <strong>ArXiv</strong>
    </div>

    </div>
  </section>

  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">

    <details class="category-section" open>
      <summary class="category-heading">
        <h3>cs.CV</h3>
        <span>14 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Event Cameras</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>EventDrive: Event Cameras for Vision-Language Driving Intelligence</strong>
          <small>Dongyue Lu, Rong Li, Ao Liang, Lingdong Kong, Wei Yin, Lai Xing Ng, Benoit R. Cottereau, Camille Simon Chane, Wei Tsang Ooi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Event Cameras</span>
<span class="topic-tag">Vision-Language Driving</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">17</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2606.18242</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.18242">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 3: it presents an event-camera vision-language driving benchmark plus a VLM for driving intelligence.</p>
        <p class="abstract">Event cameras sense the world through asynchronous brightness changes with microsecond latency and high dynamic range, offering motion fidelity far beyond frame-based sensors and capturing temporal structure that conventional exposures often miss. These properties make events a powerful complement to RGB in autonomous driving, especially under blur, glare, and rapid motion, where frame-based perception can become unreliable. However, existing event-aware vision-language models remain limited to generic perception and do not reveal how event sensing contributes to reasoning and decision-making across the full driving loop. We present EventDrive, a large-scale benchmark and model suite that unifies event streams, RGB frames, and language supervision across four core dimensions: Perception, Understanding, Prediction, and Planning, covering captions, structured QA, grounding, motion-state recognition, trajectory forecasting, and planning tasks. Building on this foundation, EventDrive-VLM introduces a multi-horizon event pyramid and a temporal-horizon mixture-of-experts module to adaptively encode and fuse asynchronous and frame-based information for downstream reasoning. Comprehensive evaluation across diverse tasks shows that event streams provide substantial gains in temporal precision, motion awareness, and robustness, bringing event sensing into the center of driving intelligence.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>DriveJudge: Rethinking Autonomous Driving Evaluation with Vision-Language Models</strong>
          <small>Xinglong Sun, Kevin Xie, Jenny Schmalfuss, Despoina Paschalidou, Xiuming Zhang, Sanja Fidler, Kashyap Chitta, Jose M. Alvarez</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Models</span>
<span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.LG</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 2 / arXiv:2606.17362</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17362">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and 3: it introduces a vision-language model-based driving evaluation agent and a new human-aligned benchmark for autonomous driving evaluation.</p>
        <p class="abstract">Autonomous driving has shifted towards end-to-end policy learning, where reliable, interpretable policy evaluation is a fundamental challenge as driving quality is highly context-dependent. Commonly used rule-based driving metrics like EPDMS are interpretable but lack context-awareness, while recent VLMbased evaluations are context-aware but limited by ambiguous VLM outputs and weak physical grounding. To evaluate driving in a manner that is both interpretable and context-aware, we introduce DriveJudge. DriveJudge is a driving evaluation agent that combines rule-grounded evaluation with Vision-Language Model (VLM) reasoning and selectively invokes physically-grounded deterministic rule functions after interpreting the environmental context. To train and evaluate DriveJudge, we curate a large-scale dataset of 33,577 challenging driving samples with human annotations on whether the driving behavior is reasonable in the given scenario. With this dataset, we address the underexplored problem of driving metric evaluation, and introduce two human-aligned benchmark tasks: Driving Quality Classification and Trajectory Preference Selection. DriveJudge outperforms EPDMS for driving quality classification by 21.23 AUC, and the recent VLM-based DriveCritic for trajectory preference selection by 6.5%, setting a new standard for interpretable and precise driving evaluation.</p>
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
          <strong>ActWorld: From Explorable to Interactive World Model via Action-Aware Memory</strong>
          <small>Zhexiao Xiong, Yizhi Song, Hao Kang, Qing Yan, Liming Jiang, Jenson Yang, Zhoujie Fu, Stathi Fotiadis, Angtian Wang, Zichuan Liu, Bo Liu, Yiding Yang, Xin Lu, Nathan Jacobs</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Interactive Generation</span>
<span class="topic-tag">Memory Systems</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2606.17730</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17730">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: embodied/world-model paper introducing action-aware memory and a new interaction-focused benchmark-like dataset for interactive world modeling.</p>
        <p class="abstract">Interactive world models aim to simulate environment dynamics under real-time user actions. However, their action vocabulary is largely confined to navigation: most actions correspond to motion (e.g., walk, turn, look around), while interaction with objects in the scene (e.g., pick up plates, open doors, or trigger physical responses) is either absent, restricted to game domains, or relegated to prompt-to-full-video scenarios. The resulting worlds are visually explorable but not truly actionable. In this work, we present ActWorld, an interactive world model that extends prior navigation-centric generators to support mid-rollout object interaction within a chunk-autoregressive framework. We argue that the navigation-interaction gap stems from two bottlenecks. First, a data bottleneck: the lack of human-object interaction data with accurate, dense labels. Second, a memory bottleneck: recency-biased history compression in existing world models discards the event-transition frames that causally determine subsequent object states, leading to an action-forgetting pathology. On the data side, we construct a 100K interaction video dataset, each annotated with per-chunk captions via chain-of-thought reasoning. On the model side, we introduce a hierarchical action-aware memory design that routes history compression by interaction importance, complemented by a persistent memory bank that maintains event-update and object-identity tokens across long rollouts. Experiments show that ActWorld supports both flexible navigation and rich object interaction within a single model, substantially improving interaction fidelity over navigation-only baselines without sacrificing viewpoint control. Project page is available at https://interactwm.github.io/ActWorld.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Open-Vocabulary Counting</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>RT-Counter: Real-Time Text-Guided Open-Vocabulary Object Counting</strong>
          <small>Hao-Yuan Ma, Li Zhang, Zhiwei Zhu, Jie Gao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Open-Vocabulary Counting</span>
<span class="topic-tag">Spatial Understanding</span>
<span class="topic-tag">Efficient Vision-Language Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2606.17561</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17561">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: it targets fine-grained spatial understanding for text-guided open-vocabulary object counting and proposes an efficiency-oriented method.</p>
        <p class="abstract">Text-guided open-vocabulary object counting (TOOC) aims to count objects belonging to the categories specified by natural language descriptions. Although vision-language pre-trained models have been successful applied to TOOC tasks, they still struggle with fine-grained spatial understanding and real-time inference requirements in counting scenarios. To address these limitations, this paper proposes a real-time TOOC framework, called the Real-Time Counter (RT-Counter), that achieves not only good counting accuracy but also high computational efficiency. RT-Counter designs a novel Visual Prototype Textualization (VPT) module that can project learned visual features into a text feature space and then generate features containing the abstract information that is hard to capture with visual prototypes and the detailed prototype information that is difficult to describe in text, enhancing the object-level visual-language model&#x27;s counting capabilities. Additionally, RT-Counter incorporates our Weaving Transformer (Weaformer) layers, maintaining high descriptive power at a fraction of the computational cost. The Weaformer layer adopts a novel hybrid attention mechanism that can efficiently weave together local and global visual features. Extensive experiments on three public datasets show that RT-Counter successfully breaks the accuracy-speed trade-off in TOOC. While achieving a competitive MAE of 13.30 on FSC147, RT-Counter operates at 112.48 FPS, making it 7.4x faster and over 4$\times$ more parameter-efficient than the existing leading methods in TOOC. Our work aims at balancing high accuracy and real-time performance in TOOC. Code is available at: https://github.com/Jason-Mar1/RT-Counter.</p>
      </div>
    </details>


    <details class="paper-row" id="link10">
      <summary class="paper-row-summary">
        <span class="queue-index">11</span>
        <span class="paper-row-copy">
          <strong>MambaCount: Efficient Text-guided Open-vocabulary Object Counting with Spatial Sparse State Space Duality Block</strong>
          <small>Hao-Yuan Ma, Li Zhang, Minjie Qiang, Jie Gao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Open-Vocabulary Counting</span>
<span class="topic-tag">Spatial Modeling</span>
<span class="topic-tag">Mamba</span>
<span class="topic-tag">Efficient Vision Models</span>
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
          <span>Paper 11 / arXiv:2606.17650</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17650">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: a methodological improvement for spatial understanding in open-vocabulary object counting, with explicit spatial token selection and bidirectional spatial modeling.</p>
        <p class="abstract">Text-guided Open-vocabulary Object Counting (TOOC) aims to estimate the number of objects described by text prompts, which is particularly challenging in dense scenes with large scale variations. Existing TOOC approaches predominantly rely on Transformers, whose quadratic complexity with respect to image resolution limits their scalability. Mamba offers a promising alternative due to its linear complexity. However, previous Mamba-based methods have two main limitations. On the one hand, the inherent causal formulation of Mamba constrains the bidirectional spatial dependency modeling required by non-causal vision tasks. On the other hand, existing Mamba-based vision models often overlook the unconstrained high entropy in the spatial token responses, which can weaken local details and high-frequency cues. To address these limitations, we propose MambaCount, an efficient framework built on the Spatial Sparse State Space Duality (S^4D) block. Specifically, we analyze and reconstruct the decay dynamics of hidden states in Mamba to alleviate the dependency constraints introduced by causal modeling. Moreover, we introduce a Spatial Token Selection (STS) sub-block to reduce the unconstrained high entropy in spatial token responses within Mamba. In addition, we design Multi-Granularity Prototypes (MGP) to identify object-like regions at different semantic levels, improving cross-modal alignment and interpretability. Extensive experiments on FSC-147 demonstrate that MambaCount achieves state-of-the-art performance among methods without secondary querying, obtaining a test MAE of 12.23, while retaining linear complexity.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning</strong>
          <small>Haoyu Wang, Guoqing Ma, Zeyu Zhang, Yandong Guo, Boxin Shi, Hao Tang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Robot Planning</span>
<span class="topic-tag">3D Reconstruction</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 5 / arXiv:2606.17480</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17480">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: embodied AI / robot planning with a new VLA-style system, new geometry-aware 3D reconstruction, and governed memory for manipulation planning.</p>
        <p class="abstract">Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Second, the original KnowledgeBank mainly retrieves semantically similar snippets and appends new knowledge, which makes it difficult to control memory quality, conflicts, confidence, and geometric relevance. To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance. To address the second challenge, we upgrade KnowledgeBank into a governed long-term memory system with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while reducing AS by 4.95% and 5.65%, respectively. Code: https://github.com/AIGeeksGroup/GeneralVLA-2. Website: https://aigeeksgroup.github.io/GeneralVLA-2.</p>
      </div>
    </details>


    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>TerraTransfer: Learning End-to-End Driving Policies Without Expert Demonstrations</strong>
          <small>Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Simulation</span>
<span class="topic-tag">Imitation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2606.17386</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17386">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 closely: embodied AI / driving policy learning in simulation, with a novel self-play-to-vision-alignment setup that avoids expert demonstrations.</p>
        <p class="abstract">End-to-end autonomous driving has achieved state-of-the-art performance on benchmarks and real-world deployments. Its standard training recipe, however, is expensive across all stages: collecting and labeling millions of driving frames is costly, and closed-loop RL on images is bottlenecked by the per-step cost of photorealistic rendering plus a forward pass through a large vision backbone. Self-play in vectorized simulators changes the economics: millions of rollout steps per second, and a state distribution naturally rich in collisions, near-misses, and recoveries that no driving log contains. Our approach exploits this asymmetry by decoupling learning to drive from learning to see. We pretrain a single policy by self-play, then align its latent space with a pretrained vision backbone, through the action KL divergence and a batch-relational low-rank structural loss. The action target comes from the self-play policy, so alignment never supervises against a logged trajectory: a paired dataset of (image, scene-state) frames suffices, with no need for the curated expert demonstrations that imitation pretraining is built on. On photorealistic 3D Gaussian splatting closed-loop scenarios, the resulting end-to-end policy matches or exceeds prior end-to-end methods.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Generative Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics</strong>
          <small>Junfeng Xia, Wenhao Ye, Junxiang Zhang, Xuanye Pan, Mo Wang, Quanying Liu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Neuroimaging</span>
<span class="topic-tag">Multimodal Foundation Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">q-bio.NC</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2606.17742</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17742">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it is a generative foundation-model-style method for whole-brain 4D fMRI dynamics with multimodal conditioning.</p>
        <p class="abstract">Whole-brain 4D fMRI generation is valuable for modeling functional brain dynamics, yet existing fMRI foundation models mainly target representation learning and downstream prediction rather than conditional predictive generation. We introduce BrainWorld, a structural-prior-conditioned generative model for whole-brain 4D fMRI dynamics. BrainWorld uses sMRI as subject-level anatomical context to guide future fMRI generation, integrating structural information into the denoising process rather than treating it as a parallel modality. Evaluated on 22 datasets spanning diverse cohorts and brain states, BrainWorld generates stable 4D fMRI trajectories up to 400 frames, improves downstream performance through generated-example augmentation, and learns transferable multimodal representations that outperform baselines. Together, these results establish BrainWorld as a condition-aware generative framework for long-horizon brain dynamics modeling and multimodal representation learning.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Foundation Models</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Predicting Immune Biomarkers with MultiModal Mixture-of-Expert Pathology Foundation Models Empowers Precision Oncology</strong>
          <small>Tianyu Liu, Ziqing Wang, Zhaokang Liang, Tong Ding, Peter Humphrey, Lorraine Col\&#x27;on-Cartagena, Emily Ling-Lin Pai, Kenneth Tou En Chang, Mohamed Kahila, Jonathan Chong Kai Liew, Tinglin Huang, Rex Ying, Kaize Ding, Faisal Mahmood, Wengong Jin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Foundation Models</span>
<span class="topic-tag">Computational Pathology</span>
<span class="topic-tag">Biomarker Prediction</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 7 / arXiv:2606.18123</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.18123">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: this is a multimodal pathology foundation model with MoE experts and downstream applications in biomarker discovery.</p>
        <p class="abstract">Predicting immune biomarkers associated with the tumor immune microenvironment (TIME) is critical for advancing precision oncology, yet existing approaches are largely limited to single image modalities and suffer from insufficient resolution and incomplete utilization of complementary clinical and biological information. Here we introduce MixTIME, a multimodal foundation model that leverages a mixture-of-experts (MoE) architecture to integrate pathology foundation models trained across distinct modalities: image only (UNIv2), image text (CONCHv1.5), and image transcriptomic (STPath) representations for pixel-level and slide-level prediction of multiplex immunofluorescence (mIF) protein expression from hematoxylin and eosin (HE) whole-slide images. MixTIME employs a learnable router to dynamically weight expert contributions and is trained with a distribution- and tendency-aware loss function. Benchmarked on two datasets of different scales, MixTIME achieves state-of-the-art performance across 17 protein markers as measured by correlation metrics. The predicted mIF profiles substantially enhance downstream tasks, including spatial domain identification, survival prediction, and AI-assisted pathology report generation validated by expert pathologists from multiple institutes across the world. Furthermore, MixTIME enables longitudinal tracking of protein expression dynamics across clinical time points and reveals protein gene interaction patterns linked to drug resistance and immune suppression in tumor microenvironments. Collectively, MixTIME provides a scalable framework for multimodal biomarker discovery and clinical translation in computational pathology.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Enhancing Pathological VLMs with Cross-scale Reasoning</strong>
          <small>Chi Phan, Tianyi Zhang, Qiaochu Xue, Yufeng Wu, Dan Hu, Zeyu Liu, Sudong Wang, Yueming Jin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Medical AI</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Multi-Scale Vision</span>
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
          <span>Paper 8 / arXiv:2606.17412</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17412">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and criterion 4: a new pathological VLM training/evaluation setup with cross-scale reasoning and a new model trained for it.</p>
        <p class="abstract">Pathological images are inherently multi-scale, requiring pathologists to integrate evidence from global tissue architecture at low magnification to cellular morphology at higher magnification for accurate diagnosis. While existing pathological datasets for vision-language model (VLM) include various scales, they often lack an explicit cross-scale reasoning objective. This limitation prevents VLMs from capturing essential cross-scale representations and learning evidence-based reasoning. To bridge this gap, we introduce the first cross-scale training and evaluation paradigm that formulates pathology interpretation as multi-magnification reasoning. However, creating such a task reveals a critical challenge: multi-image visual question answering (VQA) is prone to text-only shortcuts, which allow models to guess answers using magnification-dependent artifacts rather than visual evidence. To address this, we propose a leakage-aware curation pipeline that combines adversarial text-only screening with constraint-guided question design. Using this pipeline, we construct Scale-VQA, a high-quality benchmark with 4,685 multiple-choice questions grounded in 2,537 pathology images across multiple magnification levels. Finally, we present ScaleReasoner-R1, a model trained via reinforcement learning to optimize performance on the cross-scale VQA task. ScaleReasoner-R1 achieves state-of-the-art performance on our cross-scale reasoning benchmark and generalizes to SOTA performance on established single-scale benchmarks. Findings suggest that even the limited cross-scale supervision can significantly improve pathological understanding. The code and demos will be open-sourced.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Tokenization</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
        <span class="paper-row-copy">
          <strong>TivTok: Broadcasting Time-Invariant Tokens for Scalable Video Tokenization</strong>
          <small>Weiliang Chen, Yuanhui Huang, Xuebo Wang, Yueqi Duan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Tokenization</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Efficient Video Modeling</span>
<span class="topic-tag">Representation Learning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2606.17590</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17590">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 and is also relevant to generative modeling: a new video tokenization method for scalable video generation, centered on reusable time-invariant tokens.</p>
        <p class="abstract">Video tokenization is fundamental to scalable video generation, as the number of tokens directly determines the computational cost and the length of videos that can be modeled. Existing tokenizers mainly improve scalability by compressing videos into fewer tokens, but they often continue to represent persistent content, such as static backgrounds and consistent object appearances, repeatedly across frames and chunks. In this paper, we propose \textbf{TivTok} (\textit{Time-Invariant Tokenizer}), a reuse-aware video tokenizer that makes persistent information reusable across time. TivTok represents a clip with Time-Invariant (TIV) tokens that encode information shared across frames and Time-Variant (TV) tokens that encode frame-specific residuals. To obtain this factorization, we introduce Scope-Induced Factorization (SIF), which assigns different attention scopes to the two token groups: TIV tokens attend to the full clip, whereas each TV token only accesses its corresponding frame together with the TIV tokens. In the decoder, Invariant Broadcasting (IB) reuses the same TIV tokens across frames and chunks for parallel reconstruction and long-video tokenization. Experiments show that TivTok achieves an rFVD of 12.65 on the standard $16{\times}256{\times}256$ benchmark and improves compression efficiency by 2.91$\times$ for 128-frame videos compared with the evaluated baselines, while using only 1.1\% of the tokens required by downsample-based tokenizers in our evaluation.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Model Interpretability</summary>
      <div class="queue">

    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>PhaseWin: An Efficient Search Algorithm for Faithful Visual Attribution</strong>
          <small>Zihan Gu, Ruoyu Chen, Junchi Zhang, Li Liu, Xiaochun Cao, Hua Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Model Interpretability</span>
<span class="topic-tag">Visual Attribution</span>
<span class="topic-tag">Vision-Language Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 13 / arXiv:2606.18008</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.18008">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 loosely: this is a method for faithful visual attribution in vision/vision-language models, which is a useful vision foundation model application.</p>
        <p class="abstract">Visual attribution is a fundamental tool for interpreting modern vision and vision-language models, particularly when their decisions must be inspected, diagnosed, or audited. Its goal is to explain how a model&#x27;s decision depends on local regions of the visual input, typically by assigning an importance ordering over candidate image regions. Given an image partitioned into $n$ regions, faithful attribution can be cast as an ordered subset-search problem, in which progressively inserting the selected regions should recover the target model response as early as possible. Exhaustive search over region subsets incurs exponential cost, while the widely used greedy search still requires a quadratic number of model evaluations, because every selection step rescores all remaining candidates. We propose PhaseWin, an efficient subset-search algorithm for faithful visual attribution. PhaseWin reorganizes greedy region selection into a phased window-search procedure: rather than re-evaluating the full candidate set at every step, it alternates between global candidate screening, adaptive pruning, and localized window refinement, while preserving the essential region-ranking behavior of greedy search. We analyze PhaseWin under monotone evidence-accumulation conditions and show that, under feature-level structural assumptions, it attains controllable linear evaluation complexity together with near-greedy faithfulness guarantees. Extensive experiments on image classification, object detection, visual grounding, and image captioning show that, among all compared attribution methods, PhaseWin reaches high faithfulness with the fewest forward passes, empirically realizing the predicted reduction from $O(n^2)$ to $O(n)$. The code is available at https://github.com/Qihuai27/phasewin-va.</p>
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
          <strong>SegDINO: Introducing Multi-Scale Structure into DINO for Efficient Medical Image Segmentation</strong>
          <small>Sicheng Yang, Hongqiu Wang, Zhaohu Xing, Sixiang Chen, Qiuxia Yang, Yize Mao, Guang Yang, Lei Zhu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Medical Image Segmentation</span>
<span class="topic-tag">Self-Supervised Learning</span>
<span class="topic-tag">Multi-Scale Representation</span>
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
          <span>Paper 14 / arXiv:2606.17972</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17972">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: uses a vision foundation model (DINOv3) for efficient downstream segmentation with a new multi-scale adaptation method.</p>
        <p class="abstract">Self-supervised DINO models provide strong transferable visual representations, yet applying them directly to image segmentation remains challenging. Existing approaches commonly rely on heavy decoders with complex upsampling, introducing substantial parameter and computational overhead. We observe that introducing scale into DINO features is far more critical than increasing decoder capacity. In this work, we present SegDINO, an efficient segmentation framework that integrates a DINOv3 backbone with lightweight scale modeling. SegDINO introduces Token Pyramid Adaptation (TPA) to reorganize intermediate DINO features into a pseudo multi-scale hierarchy, and Scale-Aware Decoding (SAD) for efficient intra-scale refinement and top-down multi-scale propagation. We further curate PanCT, a new CT dataset containing 284 patients with expert-annotated pancreatic tumors, to assess SegDINO&#x27;s ability to handle difficult small-lesion cases. Extensive experiments on PanCT and three public benchmarks demonstrate that SegDINO achieves state-of-the-art results with high efficiency. The code is available at https://github.com/script-Yang/segdino_v2.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Captioning</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>CIAN: Multi-Stage Framework for Event-Enriched Image Captioning via Retrieval-Augmented Generation</strong>
          <small>Trinh Thi Thu Hien, Trung-Nghia Le</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Captioning</span>
<span class="topic-tag">Retrieval-Augmented Generation</span>
<span class="topic-tag">Vision-Language Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">6</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 16 / arXiv:2606.17430</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17430">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>3</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 only loosely: retrieval-augmented image captioning with a vision-language generation pipeline, but it is more of an application than a core foundation-model advance.</p>
        <p class="abstract">Event-enriched image captioning describes not only visible content but also the broader context of events, including timing, location, and participants, capabilities missing in most pixel-bound models. We propose the Contextual Image-Article Narrator (CIAN), a multi-stage framework that enriches captions with external narratives. CIAN retrieves relevant articles using SigLIP, summarizes them to guide a Narrative Generation stage with a LoRA-fine-tuned Qwen model, and applies N-Gram-based Refinement for fluency and coherence. On the OpenEvents-V1 benchmark, CIAN achieves high retrieval performance (mAP 0.979) and improves caption quality, increasing CIDEr from 0.030 to 0.094. These results highlight the effectiveness of retrieval-augmented reasoning combined with linguistic refinement for generating context-aware, human-like captions.</p>
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
      <summary class="topic-heading">Text-to-Image</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>STAR: SpatioTemporal Adaptive Reward Allocation for Text-to-Image RL Post-Training</strong>
          <small>Jinjie Shen, Wei Deng, Xian Hu, Daiguo Zhou, Jian Luan</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Text-to-Image</span>
<span class="topic-tag">RL Post-Training</span>
<span class="topic-tag">Diffusion Models</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2606.17979</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17979">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; this is a text-to-image RL post-training method, relevant to generative modeling but not specifically to embodied AI, VLLMs, or vision foundation model applications.</p>
        <p class="abstract">Existing RL post-training methods for text-to-image generation usually convert the final-image reward into a single scalar advantage and apply it with the same strength to the entire generative trajectory. However, text-to-image generation naturally has temporal and spatial structure: different denoising steps are responsible for different generation stages, and the content that truly determines text alignment often appears only in part of the image. This granularity mismatch makes it difficult for policy updates to focus on the generative components that actually affect the reward. To address this issue, we propose \textbf{SpatioTemporal Adaptive Reward (STAR) Allocation} for RL post-training of text-to-image diffusion and flow models. STAR uses text-image attention inside the generative model and starts from the core content that the user truly cares about in the prompt. It constructs spatial allocation maps that dynamically vary across denoising steps and rollouts, and allocates the same group-relative advantage to more relevant latent regions with almost no additional computational overhead. STAR then applies stronger policy updates to these regions through a spatially resolved policy objective. We use Stable Diffusion 3.5 Medium as the base model and evaluate on three tasks: GenEval, OCR text rendering, and PickScore. Experimental results show that STAR improves compositional semantic alignment, text rendering, and preference optimization without changing the external reward source, achieving $\mathbf{0.9759}$, $\mathbf{0.9757}$, and $\mathbf{23.60}$ on GenEval, OCR, and PickScore, respectively.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Multimodal Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>MathVis-Fine: Aligning Visual Supervision with Necessity via Progressive Dependency-Guided Training for Multimodal Mathematical Reasoning</strong>
          <small>Wanshi Xu, Haokun Zhao, Haidong Yuan, Songjun Cao, Long Ma</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Multimodal Reasoning</span>
<span class="topic-tag">Visual Grounding</span>
<span class="topic-tag">Math VQA</span>
<span class="topic-tag">Training Strategy</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 15 / arXiv:2606.17888</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17888">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 loosely: it is a multimodal reasoning paper for math with progressive visual supervision, but not really a new VLLM/MLLM architecture.</p>
        <p class="abstract">Chain-of-Thought (CoT) reasoning has extended from purely linguistic domains to multimodal scenarios; however, existing approaches often treat visual inputs as homogeneous or auxiliary signals, failing to capture the intricate and sample-specific dependencies between text and images in mathematical problem-solving. This gives rise to two core issues: first, the supervisory signals for visual content are generalized and coarse-grained, lacking adaptation to the actual necessity of visual information in each sample; second, training feedback becomes inaccurate when visual rewards are uniformly applied without distinguishing the complementary relationships among inputs. These limitations hinder models from achieving precise multimodal reasoning. In this work, we propose a framework for modeling fine-grained visual dependencies in mathematical reasoning. We first construct the MathVis-Fine dataset, augmenting fine-grained visual annotations with visual dependency ratings. Building upon this dataset, we introduce a two-stage progressive visual enhancement training paradigm that balances answer correctness rewards and visual grounding rewards according to the intrinsic visual dependency level of each sample, thereby mitigating reward bias and improving supervision accuracy. Extensive experiments demonstrate that the MathVis-Fine framework effectively enhances visual perception progressively based on visual dependency, offering a more precise training framework for multimodal mathematical reasoning. We will release the dataset upon acceptance.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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


        <a class="archive-link" href="past_arxiv/2026-05-22.html">
          <span>May 22, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-05-21.html">
          <span>May 21, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-05-20.html">
          <span>May 20, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-05-19.html">
          <span>May 19, 2026</span>
        </a>


        <a class="archive-link" href="past_arxiv/2026-05-18.html">
          <span>May 18, 2026</span>
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
