import configparser
import glob
import html
import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path


def clean_abstract(abstract: str) -> str:
    return re.sub(r"^.*?Abstract:", "", abstract, flags=re.DOTALL).strip()


def esc(value) -> str:
    return html.escape(str(value), quote=True)


def strip_trailing_whitespace(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.splitlines()) + "\n"


ARCHIVE_DIR = "past_arxiv"


TOPIC_TAG_RULES = [
    (
        "Vision-Language Reasoning",
        r"vision-language|visual language|vlm|rotated|spatial",
    ),
    ("Multimodal LLM", r"mllm|multimodal large language|multi-modal|multimodal"),
    ("Benchmark & Evaluation", r"benchmark|challenge|evaluation|diagnostic|dataset"),
    ("Embodied Interaction", r"embodied|agentic|agent|co-pilot|robot|simulator|dyadic"),
    ("Knowledge Editing", r"knowledge editing|reasonedit|edit fact|crane"),
    ("Medical AI", r"pathology|medical|brain|mri|neuroimaging|mci|diagnosis"),
    ("Generative Modeling", r"generation|synthesis|diffusion|flow matching|generative"),
    ("Safety & Backdoors", r"backdoor|safety|mitigation|detection"),
    (
        "LLM Interpretability",
        r"interpretability|inference|latent|interaction|consistency",
    ),
    ("Time-Series LLM", r"time series|forecasting|temporal"),
    ("Retrieval & Grounding", r"retrieval|grounded|evidence|knowledge"),
]


def paper_score(paper_entry: dict) -> int | None:
    if "RELEVANCE" not in paper_entry or "NOVELTY" not in paper_entry:
        return None
    return int(paper_entry["RELEVANCE"]) + int(paper_entry["NOVELTY"])


def get_paper_categories(paper_entry: dict) -> list[str]:
    categories = paper_entry.get("categories") or []
    primary_category = paper_entry.get("primary_category")
    if primary_category:
        categories = [primary_category, *categories]

    seen = set()
    unique_categories = []
    for category in categories:
        if not category or category in seen:
            continue
        seen.add(category)
        unique_categories.append(category)
    return unique_categories


def normalize_tags(tags) -> list[str]:
    if not tags:
        return []
    if isinstance(tags, str):
        tags = re.split(r"[,;/]", tags)

    seen = set()
    normalized_tags = []
    for tag in tags:
        tag = str(tag).strip()
        if not tag or tag in seen:
            continue
        seen.add(tag)
        normalized_tags.append(tag)
    return normalized_tags


def infer_topic_tags(paper_entry: dict) -> list[str]:
    text = " ".join(
        [
            paper_entry.get("title", ""),
            paper_entry.get("abstract", ""),
        ]
    ).lower()
    tags = [
        tag
        for tag, pattern in TOPIC_TAG_RULES
        if re.search(pattern, text, flags=re.IGNORECASE)
    ]
    if tags:
        return tags[:4]

    primary_category = get_primary_category(paper_entry)
    if primary_category == "cs.CV":
        return ["Computer Vision"]
    if primary_category == "cs.AI":
        return ["AI Methods"]
    return ["General ML"]


def get_topic_tags(paper_entry: dict) -> list[str]:
    tags = normalize_tags(paper_entry.get("topic_tags") or paper_entry.get("TAGS"))
    if tags:
        return tags[:4]
    return infer_topic_tags(paper_entry)


def get_primary_topic_tag(paper_entry: dict) -> str:
    return get_topic_tags(paper_entry)[0]


def get_primary_category(paper_entry: dict) -> str:
    if paper_entry.get("primary_category"):
        return paper_entry["primary_category"]
    categories = get_paper_categories(paper_entry)
    if categories:
        return categories[0]
    return "Uncategorized"


def group_papers_by_topic(
    papers: list[tuple[int, dict]],
) -> dict[str, list[tuple[int, dict]]]:
    topic_groups = {}
    for idx, paper in papers:
        topic_groups.setdefault(get_primary_topic_tag(paper), []).append((idx, paper))
    return topic_groups


def group_indexed_papers(papers_dict: dict) -> dict[str, list[tuple[int, dict]]]:
    grouped_papers = {}
    for idx, paper in enumerate(papers_dict.values()):
        grouped_papers.setdefault(get_primary_category(paper), []).append((idx, paper))
    for papers in grouped_papers.values():
        papers.sort(key=lambda item: paper_score(item[1]) or -1, reverse=True)
    return grouped_papers


def render_topic_tags(paper_entry: dict) -> str:
    tags = "\n".join(
        f'<span class="topic-tag">{esc(tag)}</span>'
        for tag in get_topic_tags(paper_entry)
    )
    return f"""
    <div class="topic-tags" aria-label="fine-grained topic tags">
      {tags}
    </div>
    """


def render_category_tags(paper_entry: dict) -> str:
    categories = get_paper_categories(paper_entry)
    if not categories:
        return ""

    tags = "\n".join(
        f'<span class="category-tag">{esc(category)}</span>' for category in categories
    )
    return f"""
    <div class="category-tags" aria-label="arXiv categories">
      {tags}
    </div>
    """


def render_metric(label: str, value: str) -> str:
    return f"""
    <div class="metric">
      <span>{esc(label)}</span>
      <strong>{esc(value)}</strong>
    </div>
    """


def archive_filename(output_date: datetime) -> str:
    return f"{ARCHIVE_DIR}/{output_date.strftime('%Y-%m-%d')}.html"


def archive_title_from_date(output_date: datetime) -> str:
    return output_date.strftime("%B %d, %Y")


def parse_archive_date(path: str) -> datetime | None:
    match = re.search(r"output_(\d{4})_(\d{2})(\d{2})\.md$", path)
    if not match:
        return None
    year, month, day = match.groups()
    return datetime(int(year), int(month), int(day))


def get_recent_archive_entries(output_date=None, days=31) -> list[tuple[datetime, str]]:
    output_date = output_date or datetime.today()
    output_day = output_date.date()
    start_day = (output_date - timedelta(days=days)).date()
    entries = []
    for path in glob.glob("out/output_*.md"):
        archive_date = parse_archive_date(path)
        if archive_date is None:
            continue
        archive_day = archive_date.date()
        if start_day <= archive_day < output_day:
            entries.append((archive_date, path))
    return sorted(entries, reverse=True)


def inline_markdown_to_html(text: str) -> str:
    text = html.escape(text)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2">\1</a>',
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(
        r"&lt;a id=&quot;([^&]+)&quot;&gt;&lt;/a&gt;",
        r'<a id="\1"></a>',
        text,
    )
    return text


def markdown_to_archive_body(markdown_text: str) -> str:
    html_lines = []
    paragraph_lines = []

    def flush_paragraph():
        if paragraph_lines:
            paragraph = "<br>".join(
                inline_markdown_to_html(line) for line in paragraph_lines
            )
            html_lines.append(
                f"<p>{paragraph}</p>"
            )
            paragraph_lines.clear()

    for line in markdown_text.splitlines():
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            continue
        if stripped == "---":
            flush_paragraph()
            html_lines.append("<hr>")
            continue
        if stripped.startswith("## "):
            flush_paragraph()
            html_lines.append(f"<h2>{inline_markdown_to_html(stripped[3:])}</h2>")
            continue
        if stripped.startswith("# "):
            flush_paragraph()
            html_lines.append(f"<h1>{inline_markdown_to_html(stripped[2:])}</h1>")
            continue
        paragraph_lines.append(stripped)

    flush_paragraph()
    return "\n".join(html_lines)


def render_archive_page(archive_date: datetime, markdown_text: str) -> str:
    return strip_trailing_whitespace(f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Past ArXiv / {esc(archive_title_from_date(archive_date))}</title>
  {render_styles()}
</head>
<body>
  <main class="daily-arxiv">
    <section class="hero archive-hero">
      <div>
        <p class="eyebrow">Past ArXiv / {esc(archive_title_from_date(archive_date))}</p>
        <h1>Daily archive</h1>
        <p class="hero-copy">A preserved paper digest from the previous month.</p>
      </div>
      <div class="metrics">
        {render_metric("Archive date", archive_date.strftime("%m/%d/%Y"))}
        {render_metric("Source", "ArXiv")}
      </div>
    </section>
    <p class="archive-nav"><a href="../index.html">Back to current digest</a></p>
    <article class="archive-content">
      {markdown_to_archive_body(markdown_text)}
    </article>
  </main>
</body>
</html>
""")


def render_archive_links(output_date=None) -> str:
    entries = get_recent_archive_entries(output_date)
    if not entries:
        return ""

    links = "\n".join(
        f"""
        <a class="archive-link" href="{esc(archive_filename(archive_date))}">
          <span>{esc(archive_title_from_date(archive_date))}</span>
          <small>{esc(Path(path).name)}</small>
        </a>
        """
        for archive_date, path in entries
    )
    return f"""
  <section class="archive-block">
    <h2>Past ArXiv</h2>
    <p>Previous daily digests from the last month.</p>
    <div class="archive-links">
      {links}
    </div>
  </section>
    """


def write_archive_pages(output_date=None):
    out_dir = Path("out") / ARCHIVE_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    for archive_date, path in get_recent_archive_entries(output_date):
        markdown_text = Path(path).read_text()
        archive_path = Path("out") / archive_filename(archive_date)
        archive_path.write_text(render_archive_page(archive_date, markdown_text))


def render_paper_row(paper_entry: dict, idx: int) -> str:
    arxiv_id = paper_entry["arxiv_id"]
    title = paper_entry["title"]
    authors = ", ".join(paper_entry["authors"])
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
    abstract = clean_abstract(paper_entry["abstract"])
    comment = paper_entry.get("COMMENT", "Selected by configured paper filters.")
    relevance = paper_entry.get("RELEVANCE")
    novelty = paper_entry.get("NOVELTY")
    score = paper_score(paper_entry)
    score_html = f'<span class="score-pill">{score}</span>' if score is not None else ""
    categories_html = render_category_tags(paper_entry)
    topic_tags_html = render_topic_tags(paper_entry)

    score_detail_html = ""
    if relevance is not None and novelty is not None:
        score_detail_html = f"""
        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>{esc(relevance)}</strong></span>
          <span>Novelty <strong>{esc(novelty)}</strong></span>
        </div>
        """

    return f"""
    <details class="paper-row" id="link{idx}">
      <summary class="paper-row-summary">
        <span class="queue-index">{idx + 1}</span>
        <span class="paper-row-copy">
          <strong>{esc(title)}</strong>
          <small>{esc(authors)}</small>
          {topic_tags_html}
          {categories_html}
        </span>
        {score_html}
      </summary>
      <div class="paper-row-detail">
        <div class="paper-row-meta">
          <span>Paper {idx + 1} / arXiv:{esc(arxiv_id)}</span>
          <a class="paper-action" href="{esc(arxiv_url)}">Open arXiv</a>
        </div>
        {score_detail_html}
        <p class="comment"><strong>Why selected:</strong> {esc(comment)}</p>
        <p class="abstract">{esc(abstract)}</p>
      </div>
    </details>
    """


def render_queue_group(category: str, papers: list[tuple[int, dict]]) -> str:
    topic_sections = "\n".join(
        render_topic_queue_group(topic, topic_papers)
        for topic, topic_papers in group_papers_by_topic(papers).items()
    )
    label = "paper" if len(papers) == 1 else "papers"
    return f"""
    <details class="category-section" open>
      <summary class="category-heading">
        <h3>{esc(category)}</h3>
        <span>{len(papers)} {label}</span>
      </summary>
      {topic_sections}
    </details>
    """


def render_topic_queue_group(topic: str, papers: list[tuple[int, dict]]) -> str:
    paper_rows = "\n".join(
        render_paper_row(paper, idx) for idx, paper in papers
    )
    return f"""
    <details class="topic-section" open>
      <summary class="topic-heading">{esc(topic)}</summary>
      <div class="queue">
        {paper_rows}
      </div>
    </details>
    """


def render_styles() -> str:
    return """
<style>
:root {
  color-scheme: light;
  --paper-bg: #f6f7f4;
  --ink: #1f2a2e;
  --muted: #647071;
  --line: #d9dfda;
  --panel: #ffffff;
  --accent: #276e6a;
  --accent-2: #a63d40;
  --soft: #e6efe8;
  --soft-2: #f4e8df;
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
  text-decoration-color: rgba(39, 110, 106, 0.35);
  text-underline-offset: 0.18em;
}

.daily-arxiv {
  max-width: 1180px;
  margin: 0 auto;
  padding: 40px 20px 72px;
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
  font-size: clamp(2.2rem, 7vw, 5.8rem);
  line-height: 0.95;
  letter-spacing: 0;
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
  font-size: 1.65rem;
  line-height: 1;
}

.section-title {
  margin: 34px 0 14px;
  font-size: 1.35rem;
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
  border: 1px solid rgba(39, 110, 106, 0.2);
  border-radius: 999px;
  background: #f8fbf9;
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

.comment {
  padding: 12px 14px;
  border-left: 4px solid var(--accent);
  background: #f8fbf9;
}

.prompt-block {
  margin-top: 30px;
  padding: 22px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fbfaf7;
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
  background: #fbfaf7;
  text-decoration: none;
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

.archive-content {
  padding: 24px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
}

.archive-content h1,
.archive-content h2 {
  line-height: 1.2;
}

.archive-content h2 {
  margin-top: 26px;
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
"""


def render_md_string(papers_dict, output_date=None):
    with open("configs/paper_topics.txt", "r") as f:
        criterion = f.read()

    output_date = output_date or datetime.today()
    paper_count = len(papers_dict)
    dated = output_date.strftime("%B %d, %Y")
    scores = [paper_score(paper) for paper in papers_dict.values()]
    scores = [score for score in scores if score is not None]
    avg_score = f"{sum(scores) / len(scores):.1f}" if scores else "n/a"
    top_score = str(max(scores)) if scores else "n/a"
    grouped_papers = group_indexed_papers(papers_dict)

    queue = "\n".join(
        render_queue_group(category, papers)
        for category, papers in grouped_papers.items()
    )

    return strip_trailing_whitespace(f"""
{render_styles()}

<main class="daily-arxiv">
  <section class="hero">
    <div>
      <p class="eyebrow">Daily ArXiv / {esc(dated)}</p>
      <h1>Personalized paper radar</h1>
      <p class="hero-copy">
        A focused reading queue selected from today's ArXiv feed, ranked by topic fit,
        novelty, and configured author matches.
      </p>
    </div>
    <div class="metrics">
      {render_metric("Relevant papers", str(paper_count))}
      {render_metric("Top score", top_score)}
      {render_metric("Average score", avg_score)}
      {render_metric("Source", "ArXiv")}
    </div>
  </section>

  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">
    {queue}
  </nav>

  {render_archive_links(output_date)}

  <section class="prompt-block">
    <h2>Paper selection prompt</h2>
    <pre>{esc(criterion)}</pre>
  </section>
</main>
""")


def render_html_string(papers_dict, output_date=None):
    return strip_trailing_whitespace(f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Daily ArXiv Paper Radar</title>
</head>
<body>
{render_md_string(papers_dict, output_date)}
</body>
</html>
""")


if __name__ == "__main__":
    with open("out/output.json", "r") as f:
        output = json.load(f)

    with open("out/output.md", "w") as f:
        f.write(render_md_string(output))
    with open("out/index.html", "w") as f:
        f.write(render_html_string(output))
    write_archive_pages()

    from send_emails import send_email

    config = configparser.ConfigParser()
    config.read("configs/config.ini")
    if len(output) != 0:
        email = config["EMAIL"]
        sender_email = email["send_email"]
        sender_password = os.environ.get("EMAIL_KEY")
        recipient_email_list = email["receive_emails"].split(", ")

        today_str = datetime.today().strftime("%Y_%m%d")
        subject = f"Daily ArXiv: {datetime.today().strftime('%m/%d/%Y')}"
        paper_len = len(output)

        title_authors = ""
        for i, paper_id in enumerate(output):
            paper_entry = output[paper_id]
            title = paper_entry["title"]
            authors = ", ".join(paper_entry["authors"])
            title_authors += f"{i}: {title}. {authors}. \n"

        body = (
            "Hi, \n\n"
            "This is Daily ArXiv: https://jackyfl.github.io/gpt_paper_assistant/. "
            f"There are {paper_len} relevant papers on "
            f"{datetime.today().strftime('%m/%d/%Y')}:\n\n"
            f"{title_authors}\n"
            "Reading papers everyday, keep innocence away! \n\n"
            "Best,\nDaily ArXiv"
        )
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        attachment_path = f"out/output_{today_str}.md"
        with open(attachment_path, "w") as f:
            f.write(render_md_string(output))

        send_email(
            sender_email,
            sender_password,
            recipient_email_list,
            subject,
            body,
            smtp_server,
            smtp_port,
            attachment=attachment_path,
        )
