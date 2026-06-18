

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
      <p class="eyebrow">Daily ArXiv / June 18, 2026</p>
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
      <strong>16</strong>
    </div>


    <div class="metric">
      <span>Average score</span>
      <strong>11.9</strong>
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
        <span>18 papers</span>
      </summary>

    <details class="topic-section" open>
      <summary class="topic-heading">Embodied AI</summary>
      <div class="queue">

    <details class="paper-row" id="link0">
      <summary class="paper-row-summary">
        <span class="queue-index">1</span>
        <span class="paper-row-copy">
          <strong>ActWorld: From Explorable to Interactive World Model via Action-Aware Memory</strong>
          <small>Zhexiao Xiong, Yizhi Song, Hao Kang, Qing Yan, Liming Jiang, Jenson Yang, Zhoujie Fu, Stathi Fotiadis, Angtian Wang, Zichuan Liu, Bo Liu, Yiding Yang, Xin Lu, Nathan Jacobs</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">World Models</span>
<span class="topic-tag">Action-Aware Memory</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">16</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 1 / arXiv:2606.17730</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17730">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>9</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: this is an embodied/world-model method extending interactive simulation beyond navigation to object interaction with action-aware memory.</p>
        <p class="abstract">Interactive world models aim to simulate environment dynamics under real-time user actions. However, their action vocabulary is largely confined to navigation: most actions correspond to motion (e.g., walk, turn, look around), while interaction with objects in the scene (e.g., pick up plates, open doors, or trigger physical responses) is either absent, restricted to game domains, or relegated to prompt-to-full-video scenarios. The resulting worlds are visually explorable but not truly actionable. In this work, we present ActWorld, an interactive world model that extends prior navigation-centric generators to support mid-rollout object interaction within a chunk-autoregressive framework. We argue that the navigation-interaction gap stems from two bottlenecks. First, a data bottleneck: the lack of human-object interaction data with accurate, dense labels. Second, a memory bottleneck: recency-biased history compression in existing world models discards the event-transition frames that causally determine subsequent object states, leading to an action-forgetting pathology. On the data side, we construct a 100K interaction video dataset, each annotated with per-chunk captions via chain-of-thought reasoning. On the model side, we introduce a hierarchical action-aware memory design that routes history compression by interaction importance, complemented by a persistent memory bank that maintains event-update and object-identity tokens across long rollouts. Experiments show that ActWorld supports both flexible navigation and rich object interaction within a single model, substantially improving interaction fidelity over navigation-only baselines without sacrificing viewpoint control. Project page is available at https://interactwm.github.io/ActWorld.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">World Models</summary>
      <div class="queue">

    <details class="paper-row" id="link1">
      <summary class="paper-row-summary">
        <span class="queue-index">2</span>
        <span class="paper-row-copy">
          <strong>OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation</strong>
          <small>Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">World Models</span>
<span class="topic-tag">Autonomous Driving</span>
<span class="topic-tag">Multi-View Generation</span>
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
          <span>Paper 2 / arXiv:2606.17536</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17536">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>8</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: this is a new embodied/autonomous driving world-model method with multi-view generation and latent geometry-aware control.</p>
        <p class="abstract">Generative world models for autonomous driving face two unresolved tensions: heterogeneous control injection, where free-form language, HD-maps, trajectories, and camera poses reside in incompatible representational spaces, and post-hoc cross-view fusion, where per-camera latents fail to encode global 3-D geometry. We trace both to a single root cause: the absence of a shared symbolic interlingua aligning language, geometry, and pixels at the latent-token level. We present DRIVE-CHOREO, an LLM-choreographed multi-agent world model that recasts controllable multi-view video generation as latent choreography. Three Qwen2.5-VL agents - a Director parsing user intent into a structured WorldScript, a Cartographer grounding it into spatially-anchored layout tokens, and an Auditor feeding cross-view critiques back as auxiliary supervision - jointly author a single position-aware token sequence. This sequence is co-compressed with the multi-view video via a view-time permutation that enforces inter-camera geometry within the convolutional receptive field of a 3-D VAE. On nuScenes, DRIVE-CHOREO sets new state-of-the-art multi-view consistency and BEV mAP (21.6) with competitive FVD (45.7); a detector trained purely on our synthetic data gains +2.4 NDS on the real validation split, validating downstream utility.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Unified Multimodal Modeling</summary>
      <div class="queue">

    <details class="paper-row" id="link3">
      <summary class="paper-row-summary">
        <span class="queue-index">4</span>
        <span class="paper-row-copy">
          <strong>Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification</strong>
          <small>Wujian Peng, Lingchen Meng, Yuxuan Cai, Xianwei Zhuang, Yuhuan Yang, Rongyao Fang, Chenfei Wu, Junyang Lin, Zuxuan Wu, Shuai Bai</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Unified Multimodal Modeling</span>
<span class="topic-tag">Visual Tokenization</span>
<span class="topic-tag">Image Generation</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 4 / arXiv:2606.18249</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.18249">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 very closely: this is a new unified multimodal autoregressive model with a shared visual tokenizer for visual understanding and generation.</p>
        <p class="abstract">Unified Multimodal Modeling aims to integrate visual understanding and generation within a single system. However, existing approaches typically rely on two disparate visual tokenizers, which splits the representation space and hinders truly unified modeling. We propose UniAR, a unified autoregressive framework where a single discrete visual tokenizer serves as the key bridge between understanding and generation, enabling a shared context in which the model can directly interpret its own generated visual tokens without additional re-encoding. UniAR adapts a pretrained vision encoder with multi-level feature fusion and a lookup-free bitwise quantization scheme, preserving both high-level semantics and low-level details while scaling the effective visual vocabulary at minimal cost. Building on this, the unified autoregressive model adopts parallel-bitwise-prediction to jointly predict spatially grouped, multi-level visual codes, substantially reducing visual sequence length and accelerating generation. Finally, a diffusion-based visual decoder operates on discrete visual tokens to decode high-fidelity images. Through large-scale pre-training, followed by supervised fine-tuning and reinforcement learning, UniAR achieves state-of-the-art performance on image generation and image editing while remaining competitive on multimodal understanding benchmarks. The project page is available at https://sharelab-sii.github.io/uniar-web.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language-Action</summary>
      <div class="queue">

    <details class="paper-row" id="link4">
      <summary class="paper-row-summary">
        <span class="queue-index">5</span>
        <span class="paper-row-copy">
          <strong>GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning</strong>
          <small>Haoyu Wang, Guoqing Ma, Zeyu Zhang, Yandong Guo, Boxin Shi, Hao Tang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language-Action</span>
<span class="topic-tag">Robot Planning</span>
<span class="topic-tag">3D Reconstruction</span>
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
          <span>Paper 5 / arXiv:2606.17480</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17480">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it proposes a new robot-planning method with geometry-aware reconstruction and governed long-term memory for a VLA system.</p>
        <p class="abstract">Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Second, the original KnowledgeBank mainly retrieves semantically similar snippets and appends new knowledge, which makes it difficult to control memory quality, conflicts, confidence, and geometric relevance. To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance. To address the second challenge, we upgrade KnowledgeBank into a governed long-term memory system with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while reducing AS by 4.95% and 5.65%, respectively. Code: https://github.com/AIGeeksGroup/GeneralVLA-2. Website: https://aigeeksgroup.github.io/GeneralVLA-2.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Robot Manipulation</summary>
      <div class="queue">

    <details class="paper-row" id="link5">
      <summary class="paper-row-summary">
        <span class="queue-index">6</span>
        <span class="paper-row-copy">
          <strong>WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation</strong>
          <small>Shoujing Zhu, Zhenyang Liu, Fungmiu Wang, Jiafeng Wang, Bo Yue, Guiliang Liu, Simo Wu, Xiangyang Xue, Taiping Zeng</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Robot Manipulation</span>
<span class="topic-tag">VLA Policies</span>
<span class="topic-tag">Memory-Augmented Control</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.RO</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 6 / arXiv:2606.17463</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17463">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: this is a new embodied robot manipulation method focused on cross-subtask memory for repeated actions.</p>
        <p class="abstract">Vision-Language-Action (VLA) policies have achieved remarkable single-step manipulation, yet they remain brittle precisely where each stage depends on what was just completed. The core issue is structural: short-window VLAs lack an explicit channel for rouxting information across sub-task boundaries, and existing memory-augmented variants either write at every frame, retrieve from demonstration-time stages, or fire at sub-goal events without performing an explicit sub-task-to-sub-task hand-off into the action expert. We identify the sub-goal completion event as the natural temporal unit for cross-subtask memory hand-off, and present WeaveLA (Weave Latent memory for Vision-Language-Action policies), a cross-subtask memory interface that, on top of a frozen VLA backbone, compresses each completed segment into latent tokens via query-driven attention pooling and routes them directly into the action-generation path of the next sub-task. This event-triggered, action-side design preserves the base policy&#x27;s short-window interface while adding a lightweight cross-subtask channel. Through stratified evaluation on RoboMME with a $\pi_{0.5}$ backbone, WeaveLA&#x27;s gains land exactly where the channel is needed: on the hardest repetition slice (SwingXtimes, $N{=}3$), success rises from $0\%$ to $47.8\%$, while single-execution episodes remain unchanged. Per-episode paired analysis confirms the gains are confined to tasks whose causal structure requires cross-subtask information.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Reasoning</summary>
      <div class="queue">

    <details class="paper-row" id="link6">
      <summary class="paper-row-summary">
        <span class="queue-index">7</span>
        <span class="paper-row-copy">
          <strong>Enhancing Pathological VLMs with Cross-scale Reasoning</strong>
          <small>Chi Phan, Tianyi Zhang, Qiaochu Xue, Yufeng Wu, Dan Hu, Zeyu Liu, Sudong Wang, Yueming Jin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Medical AI</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
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
          <span>Paper 7 / arXiv:2606.17412</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17412">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and criterion 4: this is a pathology VLM with cross-scale reasoning plus a new benchmark for multi-magnification understanding.</p>
        <p class="abstract">Pathological images are inherently multi-scale, requiring pathologists to integrate evidence from global tissue architecture at low magnification to cellular morphology at higher magnification for accurate diagnosis. While existing pathological datasets for vision-language model (VLM) include various scales, they often lack an explicit cross-scale reasoning objective. This limitation prevents VLMs from capturing essential cross-scale representations and learning evidence-based reasoning. To bridge this gap, we introduce the first cross-scale training and evaluation paradigm that formulates pathology interpretation as multi-magnification reasoning. However, creating such a task reveals a critical challenge: multi-image visual question answering (VQA) is prone to text-only shortcuts, which allow models to guess answers using magnification-dependent artifacts rather than visual evidence. To address this, we propose a leakage-aware curation pipeline that combines adversarial text-only screening with constraint-guided question design. Using this pipeline, we construct Scale-VQA, a high-quality benchmark with 4,685 multiple-choice questions grounded in 2,537 pathology images across multiple magnification levels. Finally, we present ScaleReasoner-R1, a model trained via reinforcement learning to optimize performance on the cross-scale VQA task. ScaleReasoner-R1 achieves state-of-the-art performance on our cross-scale reasoning benchmark and generalizes to SOTA performance on established single-scale benchmarks. Findings suggest that even the limited cross-scale supervision can significantly improve pathological understanding. The code and demos will be open-sourced.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Benchmark &amp; Evaluation</summary>
      <div class="queue">

    <details class="paper-row" id="link8">
      <summary class="paper-row-summary">
        <span class="queue-index">9</span>
        <span class="paper-row-copy">
          <strong>Test-Time Training for Robust Text-Guided Open-Vocabulary Object Counting</strong>
          <small>Hao-Yuan Ma, Yuda Zou, Li Zhang, Yongchao Xu</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Open-Vocabulary Object Counting</span>
<span class="topic-tag">Test-Time Training</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 9 / arXiv:2606.17601</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17601">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: it builds a new benchmark for robust text-guided open-vocabulary object counting under corruptions and proposes a test-time training method.</p>
        <p class="abstract">Text-guided Open-vocabulary Object Counting (TOOC) enables counting arbitrary object categories specified by text prompts, offering substantially greater flexibility than conventional closed-set counting. However, existing TOOC methods are developed and evaluated primarily on ideal images, while real-world scenes often suffer from adverse conditions such as rain, fog, darkness, and sensor noise, which severely degrade visual quality and impair vision-language alignment. To bridge this gap, we introduce Robust-TOOC, the first benchmark for evaluating TOOC under diverse corruption conditions, which covers six representative degradation types: rain, fog, darkness, Gaussian noise, salt-and-pepper noise, and mixed corruption. To improve robustness while preserving the original counting architecture, we propose Dual-TTT, a dual-architecture test-time training framework for TOOC. Specifically, during test-time training, Dual-TTT updates only the Text-guided Lightweight Denoising module (TL-Denoiser), while keeping the original counting network frozen. Inspired by diffusion models, the TL-Denoiser is optimized to remove corruption-aware noise from image representations under degraded conditions. Since only the TL-Denoiser is trained at test time, Dual-TTT is annotation-free and can be seamlessly integrated into existing TOOC models without modifying their original architecture. Extensive experiments on multiple recent TOOC baselines demonstrate the effectiveness of our method.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Vision-Language Models</summary>
      <div class="queue">

    <details class="paper-row" id="link9">
      <summary class="paper-row-summary">
        <span class="queue-index">10</span>
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
        <span class="score-pill score-mid">12</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 10 / arXiv:2606.17362</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17362">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it uses Vision-Language Models for autonomous driving evaluation and introduces a new human-aligned evaluation benchmark/task setup.</p>
        <p class="abstract">Autonomous driving has shifted towards end-to-end policy learning, where reliable, interpretable policy evaluation is a fundamental challenge as driving quality is highly context-dependent. Commonly used rule-based driving metrics like EPDMS are interpretable but lack context-awareness, while recent VLMbased evaluations are context-aware but limited by ambiguous VLM outputs and weak physical grounding. To evaluate driving in a manner that is both interpretable and context-aware, we introduce DriveJudge. DriveJudge is a driving evaluation agent that combines rule-grounded evaluation with Vision-Language Model (VLM) reasoning and selectively invokes physically-grounded deterministic rule functions after interpreting the environmental context. To train and evaluate DriveJudge, we curate a large-scale dataset of 33,577 challenging driving samples with human annotations on whether the driving behavior is reasonable in the given scenario. With this dataset, we address the underexplored problem of driving metric evaluation, and introduce two human-aligned benchmark tasks: Driving Quality Classification and Trajectory Preference Selection. DriveJudge outperforms EPDMS for driving quality classification by 21.23 AUC, and the recent VLM-based DriveCritic for trajectory preference selection by 6.5%, setting a new standard for interpretable and precise driving evaluation.</p>
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
          <strong>Predicting Immune Biomarkers with MultiModal Mixture-of-Expert Pathology Foundation Models Empowers Precision Oncology</strong>
          <small>Tianyu Liu, Ziqing Wang, Zhaokang Liang, Tong Ding, Peter Humphrey, Lorraine Col\&#x27;on-Cartagena, Emily Ling-Lin Pai, Kenneth Tou En Chang, Mohamed Kahila, Jonathan Chong Kai Liew, Tinglin Huang, Rex Ying, Kaize Ding, Faisal Mahmood, Wengong Jin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Multimodal Learning</span>
<span class="topic-tag">Computational Pathology</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 11 / arXiv:2606.18123</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.18123">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: this is a multimodal foundation model for computational pathology using image/text/transcriptomic experts.</p>
        <p class="abstract">Predicting immune biomarkers associated with the tumor immune microenvironment (TIME) is critical for advancing precision oncology, yet existing approaches are largely limited to single image modalities and suffer from insufficient resolution and incomplete utilization of complementary clinical and biological information. Here we introduce MixTIME, a multimodal foundation model that leverages a mixture-of-experts (MoE) architecture to integrate pathology foundation models trained across distinct modalities: image only (UNIv2), image text (CONCHv1.5), and image transcriptomic (STPath) representations for pixel-level and slide-level prediction of multiplex immunofluorescence (mIF) protein expression from hematoxylin and eosin (HE) whole-slide images. MixTIME employs a learnable router to dynamically weight expert contributions and is trained with a distribution- and tendency-aware loss function. Benchmarked on two datasets of different scales, MixTIME achieves state-of-the-art performance across 17 protein markers as measured by correlation metrics. The predicted mIF profiles substantially enhance downstream tasks, including spatial domain identification, survival prediction, and AI-assisted pathology report generation validated by expert pathologists from multiple institutes across the world. Furthermore, MixTIME enables longitudinal tracking of protein expression dynamics across clinical time points and reveals protein gene interaction patterns linked to drug resistance and immune suppression in tumor microenvironments. Collectively, MixTIME provides a scalable framework for multimodal biomarker discovery and clinical translation in computational pathology.</p>
      </div>
    </details>


    <details class="paper-row" id="link12">
      <summary class="paper-row-summary">
        <span class="queue-index">13</span>
        <span class="paper-row-copy">
          <strong>HLS-GPT: A Generative Pretrained Transformer (GPT) for Continental-Scale NASA Harmonized Landsat and Sentinel-2 (HLS) Reflectance Reconstruction Across All Bands on Arbitrary Dates</strong>
          <small>Junjie Li, Hankui K. Zhang, David P. Roy</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Remote Sensing</span>
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
          <span>Paper 13 / arXiv:2606.18115</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.18115">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: a large-scale generative pretrained transformer for continental-scale remote-sensing reflectance reconstruction.</p>
        <p class="abstract">Recent deep learning methods for Landsat and Sentinel-2 reflectance time series reconstruction remain limited by restricted spectral coverage, limited geographic scalability, or patch-based designs with short temporal contexts. We present HLS-GPT, a large-scale generative pretrained Transformer model for reconstructing NASA Harmonized Landsat Sentinel-2 30 m surface reflectance for all bands, any date, and any pixel location. HLS-GPT uses a hierarchical Transformer architecture to handle the different spectral band configurations of Landsat and Sentinel-2 and operates on single-pixel 12-month time series. To capture geographic and seasonal variability, the model was trained with nine years of HLS time series from more than 0.25 million training pixels across the conterminous United States. A random cropping and masking strategy extracts 12-month periods with varying start dates across epochs, masks 50% of valid observations, and trains the model to reconstruct the masked reflectance values from the remaining observations. Evaluation using more than 62,000 independent test pixels shows robust reconstruction under diverse land surface conditions, including complex crop phenology and sparse, irregular observations. Leave-one-observation-out evaluation achieved reconstruction RMSE below 0.026 for all HLS spectral bands, with relative RMSE below 35% for visible bands and below 13% for other bands. Red-edge band errors were comparable to red and near-infrared errors despite the absence of red-edge bands on Landsat. Sensitivity analyses that randomly masked 10% to 90% of test observations showed only modest degradation when 10% to 50% of observations were masked, with all-band RMSE below 0.028. Image reconstruction over nine independent 109 by 109 km CONUS HLS tiles further demonstrates that HLS-GPT outperforms two conventional methods and the NASA-IBM Prithvi model.</p>
      </div>
    </details>


    <details class="paper-row" id="link17">
      <summary class="paper-row-summary">
        <span class="queue-index">18</span>
        <span class="paper-row-copy">
          <strong>LADBench: A Benchmark for Logical Fault Detection in Images</strong>
          <small>Sahasra Kondapalli, Lara Radovanovic, Aadi Palnitkar, Mingyang Mao, Xiaomin Lin</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Vision Foundation Models</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Logical Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">10</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 18 / arXiv:2606.17433</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17433">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 closely: it introduces a benchmark for logical fault detection in images and evaluates foundation models on sequential multimodal reasoning.</p>
        <p class="abstract">Large Vision Language Models (VLMs) excel at visual question answering and semantic grounding, but their capacity for autonomous logical reasoning remains underexplored. Existing anomaly benchmarks emphasize visual errors or direct prompting rather than the physical and social common sense needed for open-world deployment. To address this, we introduce LAD-bench, a benchmark of more than 1,000 curated synthetic images with logical anomalies across four domains: Residential, Urban, Collaborative, and Nature. We further propose a Tiered Prompting Protocol based on progressive disclosure, which measures how much explicit assistance a model needs to localize and reason about a logical fault. Evaluating leading foundation models reveals substantial weaknesses: even the best achieves only 70.11% overall accuracy, showing that implicit logical fault detection remains unsolved. Crucially, models often fail to identify anomalies even after receiving explicit hints in deeper tiers. By surfacing these limitations in sequential multimodal reasoning, LAD-Bench offers a rigorous framework for advancing the safety, reliability, and cognitive alignment of autonomous visual systems. Dataset and Code: https://huggingface.co/datasets/SahasraK/LADBench</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Open-Vocabulary Counting</summary>
      <div class="queue">

    <details class="paper-row" id="link11">
      <summary class="paper-row-summary">
        <span class="queue-index">12</span>
        <span class="paper-row-copy">
          <strong>RT-Counter: Real-Time Text-Guided Open-Vocabulary Object Counting</strong>
          <small>Hao-Yuan Ma, Li Zhang, Zhiwei Zhu, Jie Gao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Open-Vocabulary Counting</span>
<span class="topic-tag">Vision-Language Reasoning</span>
<span class="topic-tag">Efficient Inference</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-mid">11</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 12 / arXiv:2606.17561</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17561">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 1: it explicitly targets fine-grained spatial understanding for text-guided open-vocabulary object counting and improves real-time visual-language reasoning.</p>
        <p class="abstract">Text-guided open-vocabulary object counting (TOOC) aims to count objects belonging to the categories specified by natural language descriptions. Although vision-language pre-trained models have been successful applied to TOOC tasks, they still struggle with fine-grained spatial understanding and real-time inference requirements in counting scenarios. To address these limitations, this paper proposes a real-time TOOC framework, called the Real-Time Counter (RT-Counter), that achieves not only good counting accuracy but also high computational efficiency. RT-Counter designs a novel Visual Prototype Textualization (VPT) module that can project learned visual features into a text feature space and then generate features containing the abstract information that is hard to capture with visual prototypes and the detailed prototype information that is difficult to describe in text, enhancing the object-level visual-language model&#x27;s counting capabilities. Additionally, RT-Counter incorporates our Weaving Transformer (Weaformer) layers, maintaining high descriptive power at a fraction of the computational cost. The Weaformer layer adopts a novel hybrid attention mechanism that can efficiently weave together local and global visual features. Extensive experiments on three public datasets show that RT-Counter successfully breaks the accuracy-speed trade-off in TOOC. While achieving a competitive MAE of 13.30 on FSC147, RT-Counter operates at 112.48 FPS, making it 7.4x faster and over 4$\times$ more parameter-efficient than the existing leading methods in TOOC. Our work aims at balancing high accuracy and real-time performance in TOOC. Code is available at: https://github.com/Jason-Mar1/RT-Counter.</p>
      </div>
    </details>


    <details class="paper-row" id="link14">
      <summary class="paper-row-summary">
        <span class="queue-index">15</span>
        <span class="paper-row-copy">
          <strong>MambaCount: Efficient Text-guided Open-vocabulary Object Counting with Spatial Sparse State Space Duality Block</strong>
          <small>Hao-Yuan Ma, Li Zhang, Minjie Qiang, Jie Gao</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Open-Vocabulary Counting</span>
<span class="topic-tag">Mamba Vision Model</span>
<span class="topic-tag">Spatial Reasoning</span>
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
          <span>Paper 15 / arXiv:2606.17650</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17650">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>5</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4 moderately well: it is a vision-model application with a new spatial-efficient architecture for open-vocabulary object counting, though it is not a foundation-model paper in the strongest sense.</p>
        <p class="abstract">Text-guided Open-vocabulary Object Counting (TOOC) aims to estimate the number of objects described by text prompts, which is particularly challenging in dense scenes with large scale variations. Existing TOOC approaches predominantly rely on Transformers, whose quadratic complexity with respect to image resolution limits their scalability. Mamba offers a promising alternative due to its linear complexity. However, previous Mamba-based methods have two main limitations. On the one hand, the inherent causal formulation of Mamba constrains the bidirectional spatial dependency modeling required by non-causal vision tasks. On the other hand, existing Mamba-based vision models often overlook the unconstrained high entropy in the spatial token responses, which can weaken local details and high-frequency cues. To address these limitations, we propose MambaCount, an efficient framework built on the Spatial Sparse State Space Duality (S^4D) block. Specifically, we analyze and reconstruct the decay dynamics of hidden states in Mamba to alleviate the dependency constraints introduced by causal modeling. Moreover, we introduce a Spatial Token Selection (STS) sub-block to reduce the unconstrained high entropy in spatial token responses within Mamba. In addition, we design Multi-Granularity Prototypes (MGP) to identify object-like regions at different semantic levels, improving cross-modal alignment and interpretability. Extensive experiments on FSC-147 demonstrate that MambaCount achieves state-of-the-art performance among methods without secondary querying, obtaining a test MAE of 12.23, while retaining linear complexity.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Egocentric Action Recognition</summary>
      <div class="queue">

    <details class="paper-row" id="link13">
      <summary class="paper-row-summary">
        <span class="queue-index">14</span>
        <span class="paper-row-copy">
          <strong>Divide, Deliberate, Decide: A Multi-Agent Framework for Fine-Grained Egocentric Action Recognition</strong>
          <small>Alessandro Sottovia, Alessandro Torcinovich, Oswald Lanz</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Egocentric Action Recognition</span>
<span class="topic-tag">Multi-Agent VLM</span>
<span class="topic-tag">Zero-Shot Classification</span>
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
          <span>Paper 14 / arXiv:2606.17627</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17627">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>6</strong></span>
          <span>Novelty <strong>5</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 2 and is also adjacent to criterion 3: it uses a multi-agent VLM framework for fine-grained egocentric action recognition.</p>
        <p class="abstract">Fine-grained action recognition in egocentric video is challenging for Vision-Language Models (VLMs): actions often differ only in small visual cues, and a single model tends to be biased toward a subset of these cues. We propose Divide, Deliberate, Decide, a fully-local, zero-shot multi-agent framework in which (i) a VLM orchestrator chunks the video and proposes a top-k candidate label list per segment, (ii) an ensemble of heterogeneous VLM specialists, drawn from different open model families, engages in a structured deliberation that includes a peer-consultation round of questions, and (iii) agent rankings are aggregated with a Borda count and the orchestrator re-ranks its own prediction in light of the specialists&#x27; evidence. The entire pipeline runs locally with no fine-tuning. Experiments show that our method positively improves zero-shot action recognition performance over the baseline, highlighting the influence of a heterogeneous deliberation step, showing that the gain stems from decorrelated model priors rather than from additional compute.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">3D Vision</summary>
      <div class="queue">

    <details class="paper-row" id="link15">
      <summary class="paper-row-summary">
        <span class="queue-index">16</span>
        <span class="paper-row-copy">
          <strong>ReAge3D: Re-Aging 3D Faces with View Consistency</strong>
          <small>Libing Zeng, Li Ma, Mingming He, Ning Yu, Paul Debevec, Nima Khademi Kalantari</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">3D Vision</span>
<span class="topic-tag">Diffusion Editing</span>
<span class="topic-tag">Multi-View Consistency</span>
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
          <span>Paper 16 / arXiv:2606.18156</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.18156">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: this is a vision foundation-model-adjacent 3D face editing method built on diffusion-based multi-view consistency.</p>
        <p class="abstract">We present a novel framework for realistic and controllable 3D face re-aging which produces highly detailed, identity-preserving results. Existing 3D editing methods, while effective for coarse semantic changes, are not well suited for re-aging, as even small inconsistencies across re-aged 2D views can lead to over-smoothing of subtle but perceptually important age-related details. To address this challenge, we first introduce a 2D diffusion-based re-aging model, DiffReaging, trained on synthetically generated image pairs. We further propose a center-out editing propagation strategy that leverages this re-aging model to reconstruct multi-view-consistent re-aged images. Specifically, starting from a re-aged frontal pivot view, we reconstruct the remaining views through warping and our proposed Masked-DiffReaging process. By injecting existing content at every step of the diffusion process, Masked-DiffReaging ensures that the reconstructed regions remain coherent with existing pixels. The resulting consistent set of re-aged views supervises the optimization of the re-aged 3D representation. Our method outperforms existing 3D editing techniques both visually and quantitatively, enabling smooth, fine-grained control over age transformations in 3D face models.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Video Generation</summary>
      <div class="queue">

    <details class="paper-row" id="link16">
      <summary class="paper-row-summary">
        <span class="queue-index">17</span>
        <span class="paper-row-copy">
          <strong>SierpinskiCam: Camera-Controlled Video Retaking with Sierpinski Triangle Pattern Cues</strong>
          <small>Suttisak Wizadwongsa, Hyelin Nam, Supasorn Suwajanakorn, Jeong Joon Park</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Video Generation</span>
<span class="topic-tag">Camera Control</span>
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
          <span>Paper 17 / arXiv:2606.17310</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17310">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>4</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 4: it is a vision/generative-modeling paper that improves view-conditioned video retaking with new camera-control cues.</p>
        <p class="abstract">Generating novel renderings of a scene along user-defined camera trajectories from a single monocular video, dubbed video retaking, is a compelling but difficult problem in content creation and visual effects. Existing geometry-guided approaches reconstruct a 4D representation from the source video and render it along the target trajectory to condition video diffusion models. However, this guidance degrades as the target camera departs from the source trajectory, leaving newly revealed regions sparse or entirely missing. We propose SierpinskiCam, which addresses this limitation by augmenting geometry-based guidance with Sierpinski dome texture cues that contains rich trackable features even under large viewpoint changes. We further introduce a reference video conditioning mechanism that appends source-video tokens to the target-token sequence and separates the two streams with negative RoPE indices, enabling appearance grounding without architectural modification or per-video adaptation. Extensive experiments show that SierpinskiCam achieves significant gains in camera controllability, geometric consistency, and video quality across diverse and challenging retaking scenarios. Project page: https://hyelinnam.github.io/SierpinskiCam/.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Image Restoration</summary>
      <div class="queue">

    <details class="paper-row" id="link18">
      <summary class="paper-row-summary">
        <span class="queue-index">19</span>
        <span class="paper-row-copy">
          <strong>Universal Image Restoration via Internalized Chain-of-Thought Reasoning</strong>
          <small>Yu Guo, Zhengru Fang, Shengfeng He, Senkang Hu, Yihang Tao, Phone Lin, Yuguang Fang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Image Restoration</span>
<span class="topic-tag">Generative Modeling</span>
<span class="topic-tag">Reasoning</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
    </div>

        </span>
        <span class="score-pill score-low">9</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 19 / arXiv:2606.17557</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17557">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No close match to the listed criteria; this is image restoration with internalized chain-of-thought, which is adjacent to generative modeling but not specifically the requested spatial/embodied/VLM/foundation-model focus.</p>
        <p class="abstract">Image restoration seeks to recover high-quality images from degraded inputs but becomes highly ill-posed under complex, mixed degradations. While unified all-in-one models are common, their performance declines as degradation complexity increases. Recent works adopt Chain-of-Thought (CoT) reasoning for multi-round restoration using specialized modules. However, this approach faces two key limitations: (i) increased computational cost due to multi-step processing, and (ii) weak modeling of interactions between degradations during stepwise inference. We introduce CoTIR, a universal image restoration framework that internalizes CoT reasoning within a single model. Concretely, we view image restoration as a specialized subtask of image editing, which implies that a large-scale pre-trained editing model provides a more favorable optimization starting point. Building on this, we fine-tune the model for restoration and further encode structured CoT-style reasoning into the learning objective via a differentiable formulation inspired by Lagrangian optimization, enabling holistic restoration without chaining specialized restorers. To facilitate training and evaluation, we further present CoTIR-Bench, a large-scale benchmark comprising 5.2 million samples with CoT-style reasoning traces. Extensive experiments on CoTIR-Bench and broad real composite degradation scenes show that CoTIR achieves stronger perceptual quality and more competitive fidelity than both all-in-one models and multi-round restoration methods. The source code is available at https://github.com/gy65896/CoTIR.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">Positional Encoding</summary>
      <div class="queue">

    <details class="paper-row" id="link19">
      <summary class="paper-row-summary">
        <span class="queue-index">20</span>
        <span class="paper-row-copy">
          <strong>Robustness of Similarity-based Positional Encoding Under Rotations: Theoretical Analysis and Experimental Validation</strong>
          <small>Andrea Santomauro, Luigi Portinale, Giorgio Leonardi</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Positional Encoding</span>
<span class="topic-tag">Rotation Robustness</span>
<span class="topic-tag">Theoretical Analysis</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.CV</span>
<span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-low">7</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 20 / arXiv:2606.17961</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.17961">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>3</strong></span>
          <span>Novelty <strong>4</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> No very close match to criteria 1-4; the main overlap is a spatially aware vision method with a theoretical robustness analysis, which is more of a general CV/ML technical paper than embodied AI or VLLM work.</p>
        <p class="abstract">Positional encoding is a fundamental component of Transformer architectures, as it injects information about the spatial or sequential arrangement of inputs. Among recent alternatives to standard absolute and sinusoidal encodings, similarity-based positional encoding (simPE) has emerged as a flexible framework for representing positional structure through pairwise relations. simPE was originally designed for medical imaging applications, where geometric robustness is especially relevant: small rotations naturally arise during image acquisition, induced by imaging instruments, patient positioning, or slight acquisition misalignments. Despite its empirical promise, the theoretical behavior of simPE under geometric perturbations has not been fully characterized. In this paper, we study the robustness of simPE with respect to rotations, combining formal theoretical analysis with experimental validation. We first show that simPE is generally not rotation-invariant. We then prove that, under mild Lipschitz assumptions on the elementary components, simPE is stable under rotational perturbations and derive explicit perturbation bounds in Frobenius norm. We validate these findings experimentally on four controlled datasets--a synthetic Arrow dataset, a synthetic Shapes dataset (four geometric shape categories), a synthetic Digits dataset, and a benchmark image classification dataset (FashionMNIST)--in which training and validation images are kept in a fixed canonical orientation while test images are subjected to increasing rotation angles. Across all datasets, simPE consistently outperforms standard learned positional encoding in terms of accuracy, F1 score, precision, and recall under rotation, particularly in the small-to-moderate angle regime, corroborating the theoretical stability guarantees.</p>
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

    <details class="paper-row" id="link2">
      <summary class="paper-row-summary">
        <span class="queue-index">3</span>
        <span class="paper-row-copy">
          <strong>WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents</strong>
          <small>Yehang Zhang, Jianchong Su, Haojian Huang, Yifan Chang, Tianhao Zhou, Xinli Xu, Yingjie Xu, Yinchuan Li, Zexi Li, Ying-Cong Chen</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">Embodied AI</span>
<span class="topic-tag">Benchmark &amp; Evaluation</span>
<span class="topic-tag">Long-Horizon Memory</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-high">15</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 3 / arXiv:2606.18847</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.18847">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>8</strong></span>
          <span>Novelty <strong>7</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3: this is a new embodied AI benchmark plus a stateful long-horizon memory/planning method for embodied household assistance.</p>
        <p class="abstract">To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions. Existing long-term memory benchmarks mainly evaluate language-centric retrieval and question answering, while embodied benchmarks often focus on short-horizon task execution without testing long-term memory use in dynamic environments. We introduce WorldLines, a project-driven benchmark for long-horizon embodied household assistance. It constructs temporally extended household traces with dialogues, actions, execution feedback, object and device state changes, and converts them into evidence-linked samples for Memory QA and Embodied Task Planning. We further propose ObsMem, an observer-grounded memory framework that maintains visibility-aware memories and action-native state trails for state-aware decisions. Experiments reveal persistent challenges in partial observability, overwritten world states, and translating long-term memory into embodied plans, while ObsMem offers a stronger reference architecture for this setting.</p>
      </div>
    </details>

      </div>
    </details>


    <details class="topic-section" open>
      <summary class="topic-heading">GUI Agents</summary>
      <div class="queue">

    <details class="paper-row" id="link7">
      <summary class="paper-row-summary">
        <span class="queue-index">8</span>
        <span class="paper-row-copy">
          <strong>Skill-Guided Continuation Distillation for GUI Agents</strong>
          <small>Zhimin Fan, Hongwei Yu, Yeqing Shen, Haolong Yan, Guozhen Peng, Tianhao Peng, Yudong Zhang, Xiaowen Zhang, Kaijun Tan, Zheng Ge, Xiangyu Zhang, Daxin Jiang</small>

    <div class="topic-tags" aria-label="fine-grained topic tags">
      <span class="topic-tag">GUI Agents</span>
<span class="topic-tag">Imitation Learning</span>
<span class="topic-tag">Off-Policy Supervision</span>
    </div>


    <div class="category-tags" aria-label="arXiv categories">
      <span class="category-tag">cs.AI</span>
    </div>

        </span>
        <span class="score-pill score-mid">13</span>
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper 8 / arXiv:2606.18890</span>
          <a class="paper-action" href="https://arxiv.org/abs/2606.18890">Open arXiv</a>
        </div>

        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>7</strong></span>
          <span>Novelty <strong>6</strong></span>
        </div>

        <p class="comment"><strong>Why selected:</strong> Matches criterion 3 very closely: this is a new method for GUI agents, focused on closing the off-trajectory supervision gap with skill-guided continuation distillation.</p>
        <p class="abstract">Improving GUI agents typically relies on behavior cloning on expert trajectories. However, as the current policy deviates from the expert policy, it inevitably encounters policy-induced off-trajectory states during closed-loop execution, i.e., states that fall outside the expert trajectories. Since expert trajectories provide no demonstrations for these unseen states, such states receive no effective supervision, leaving the policy unable to select the correct action. To close this supervision gap, we propose Skill-Guided Continuation Distillation (SGCD), an iterative self-improvement framework. SGCD first runs the plain policy without skill guidance for a few steps to reach realistic off-trajectory states. From these states, a skill-guided policy then completes the task and produces successful continuations, which are mixed with expert trajectories to supply supervision over policy-induced off-trajectory states. The skills are extracted from both successful and failed rollouts, consisting of Continuation Plans, Critical Targets, Failure Traps, and Success Criteria. On OSWorld-Verified, SGCD improves the success rate of three base models from the low-30\% range to over 50\%, demonstrating its effectiveness and generality.</p>
      </div>
    </details>

      </div>
    </details>

    </details>

  </nav>


  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <div class="archive-links">

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
