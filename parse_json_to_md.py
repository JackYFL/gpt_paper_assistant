import configparser
import html
import json
import os
import re
from datetime import datetime


def clean_abstract(abstract: str) -> str:
    return re.sub(r"^.*?Abstract:", "", abstract, flags=re.DOTALL).strip()


def esc(value) -> str:
    return html.escape(str(value), quote=True)


def strip_trailing_whitespace(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.splitlines()) + "\n"


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


def get_primary_category(paper_entry: dict) -> str:
    if paper_entry.get("primary_category"):
        return paper_entry["primary_category"]
    categories = get_paper_categories(paper_entry)
    if categories:
        return categories[0]
    return "Uncategorized"


def group_indexed_papers(papers_dict: dict) -> dict[str, list[tuple[int, dict]]]:
    grouped_papers = {}
    for idx, paper in enumerate(papers_dict.values()):
        grouped_papers.setdefault(get_primary_category(paper), []).append((idx, paper))
    for papers in grouped_papers.values():
        papers.sort(key=lambda item: paper_score(item[1]) or -1, reverse=True)
    return grouped_papers


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


def render_title_and_author(paper_entry: dict, idx: int) -> str:
    title = paper_entry["title"]
    authors = ", ".join(paper_entry["authors"])
    score = paper_score(paper_entry)
    score_html = f'<span class="score-pill">{score}</span>' if score is not None else ""
    categories_html = render_category_tags(paper_entry)
    return f"""
    <a class="queue-item" href="#link{idx}">
      <span class="queue-index">{idx + 1}</span>
      <span class="queue-copy">
        <strong>{esc(title)}</strong>
        <small>{esc(authors)}</small>
        {categories_html}
      </span>
      {score_html}
    </a>
    """


def render_queue_group(category: str, papers: list[tuple[int, dict]]) -> str:
    queue_items = "\n".join(
        render_title_and_author(paper, idx) for idx, paper in papers
    )
    label = "paper" if len(papers) == 1 else "papers"
    return f"""
    <section class="category-section">
      <header class="category-heading">
        <h3>{esc(category)}</h3>
        <span>{len(papers)} {label}</span>
      </header>
      <div class="queue">
        {queue_items}
      </div>
    </section>
    """


def render_paper_group(category: str, papers: list[tuple[int, dict]]) -> str:
    paper_cards = "\n".join(render_paper(paper, idx) for idx, paper in papers)
    return f"""
    <section class="paper-category-section">
      <h3>{esc(category)}</h3>
      <div class="paper-list">
        {paper_cards}
      </div>
    </section>
    """


def render_paper(paper_entry: dict, idx: int) -> str:
    arxiv_id = paper_entry["arxiv_id"]
    title = paper_entry["title"]
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
    abstract = clean_abstract(paper_entry["abstract"])
    authors = ", ".join(paper_entry["authors"])
    comment = paper_entry.get("COMMENT", "Selected by configured paper filters.")
    relevance = paper_entry.get("RELEVANCE")
    novelty = paper_entry.get("NOVELTY")

    score_html = ""
    if relevance is not None and novelty is not None:
        score_html = f"""
        <div class="paper-scores" aria-label="model scores">
          <span>Relevance <strong>{esc(relevance)}</strong></span>
          <span>Novelty <strong>{esc(novelty)}</strong></span>
        </div>
        """

    return f"""
    <article class="paper-card" id="link{idx}">
      <header class="paper-head">
        <div>
          <p class="paper-kicker">Paper {idx + 1} / arXiv:{esc(arxiv_id)}</p>
          <h2><a href="{esc(arxiv_url)}">{esc(title)}</a></h2>
        </div>
        <div class="paper-actions">
          <a class="paper-action" href="{esc(arxiv_url)}">Open arXiv</a>
          <a class="paper-action secondary" href="#paper-content">Back to queue</a>
        </div>
      </header>
      <p class="authors">{esc(authors)}</p>
      {render_category_tags(paper_entry)}
      {score_html}
      <p class="comment"><strong>Why selected:</strong> {esc(comment)}</p>
      <p class="abstract">{esc(abstract)}</p>
    </article>
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

.category-groups,
.paper-category-groups {
  display: grid;
  gap: 24px;
}

.category-section,
.paper-category-section {
  scroll-margin-top: 18px;
}

.category-heading,
.paper-category-section h3 {
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin: 0 0 10px;
}

.category-heading h3,
.paper-category-section h3 {
  color: var(--ink);
  font-size: 1rem;
  margin: 0;
}

.category-heading span {
  color: var(--muted);
  font-size: 0.86rem;
  font-weight: 700;
}

.queue {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 10px;
}

.queue-item {
  display: grid;
  grid-template-columns: 36px minmax(0, 1fr) auto;
  gap: 12px;
  align-items: start;
  min-height: 96px;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  text-decoration: none;
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

.queue-copy strong {
  display: block;
  line-height: 1.28;
}

.queue-copy small {
  display: block;
  margin-top: 7px;
  color: var(--muted);
  line-height: 1.35;
}

.category-tags {
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

.paper-list {
  display: grid;
  gap: 18px;
  margin-top: 14px;
}

.paper-card {
  padding: 24px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
}

.paper-head {
  display: flex;
  gap: 18px;
  justify-content: space-between;
}

.paper-head h2 {
  max-width: 900px;
  margin: 0;
  font-size: 1.45rem;
  line-height: 1.2;
}

.paper-actions {
  display: flex;
  flex: 0 0 auto;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: flex-end;
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

.paper-action.secondary {
  border-color: var(--line);
  color: var(--muted);
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

  .paper-card {
    padding: 18px;
  }

  .paper-head {
    display: block;
  }

  .paper-actions {
    justify-content: flex-start;
    margin-top: 14px;
  }

  .paper-action {
    display: inline-block;
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
    paper_groups = "\n".join(
        render_paper_group(category, papers)
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
      {render_metric("Source", "ArXiv RSS")}
    </div>
  </section>

  <h2 class="section-title" id="paper-content">Reading Queue</h2>
  <nav class="category-groups" aria-label="selected papers by category">
    {queue}
  </nav>

  <h2 class="section-title">Paper Notes</h2>
  <section class="paper-category-groups">
    {paper_groups}
  </section>

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
