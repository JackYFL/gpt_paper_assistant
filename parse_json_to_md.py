import configparser
import glob
import html
import json
import math
import os
import re
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path


def clean_abstract(abstract: str) -> str:
    return re.sub(r"^.*?Abstract:", "", abstract, flags=re.DOTALL).strip()


def esc(value) -> str:
    return html.escape(str(value), quote=True)


def strip_trailing_whitespace(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.splitlines()) + "\n"


ARCHIVE_DIR = "past_arxiv"


WORD_CLOUD_RE = re.compile(r"[a-zA-Z][a-zA-Z'-]{2,}")

# Generic English + academic filler words that carry no topical signal.
WORD_CLOUD_STOPWORDS = {
    "the", "and", "for", "are", "but", "not", "you", "all", "can", "her",
    "was", "one", "our", "out", "has", "have", "had", "his", "they", "this",
    "that", "with", "from", "their", "these", "those", "such", "than", "then",
    "them", "been", "being", "into", "over", "under", "also", "more", "most",
    "much", "many", "some", "any", "each", "other", "which", "while", "where",
    "when", "what", "who", "whom", "whose", "how", "why", "via", "per", "use",
    "used", "using", "uses", "based", "show", "shows", "shown", "showing",
    "propose", "proposed", "proposes", "present", "presents", "presented",
    "introduce", "introduces", "introduced", "result", "results", "method",
    "methods", "approach", "approaches", "paper", "papers", "work", "works",
    "task", "tasks", "however", "thus", "therefore", "moreover", "furthermore",
    "between", "across", "within", "without", "among", "given", "due", "both",
    "two", "three", "first", "second", "new", "novel", "various", "different",
    "several", "existing", "compared", "comparison", "achieve", "achieves",
    "achieved", "achieving", "demonstrate", "demonstrates", "demonstrated",
    "leverage", "leverages", "leveraging", "enable", "enables", "enabling",
    "provide", "provides", "provided", "study", "studies", "studied", "able",
    "well", "high", "low", "large", "small", "good", "better", "best", "may",
    "we", "it", "its", "by", "to", "of", "in", "on", "as", "an", "or", "is",
    "be", "at", "do", "does", "set", "non", "etc", "e.g", "i.e",
}

# Generic ML/research terms that appear in almost every abstract, so they drown
# out the words that actually distinguish each day's topics.
WORD_CLOUD_GENERIC_TERMS = {
    "model", "models", "modeling", "modelling",
    "framework", "frameworks", "performance",
    "data", "dataset", "datasets", "benchmark", "benchmarks",
    "evaluation", "evaluate", "evaluated", "evaluating",
    "experiment", "experiments", "experimental", "experimentally",
    "baseline", "baselines", "accuracy", "metric", "metrics",
    "training", "train", "trained", "trains",
    "learning", "learn", "learned", "learns",
    "network", "networks", "system", "systems",
    "algorithm", "algorithms", "problem", "problems",
    "application", "applications", "analysis", "analyses",
    "feature", "features", "function", "functions", "functional",
    "parameter", "parameters", "output", "outputs", "input", "inputs",
    "sample", "samples", "sampling", "setting", "settings",
    "scenario", "scenarios", "representation", "representations",
    "information", "process", "processes", "processing",
    "design", "designs", "designed", "state", "states",
    "number", "value", "values", "level", "levels",
    "type", "types", "case", "cases", "scale", "scales",
    "size", "sizes", "rate", "rates", "score", "scores",
    "test", "tests", "testing", "validation", "module", "modules",
    "component", "components", "objective", "objectives",
    "strategy", "strategies", "capability", "capabilities",
    "ability", "abilities", "challenge", "challenges",
    "improvement", "improvements", "improve", "improves", "improved",
    "effectiveness", "efficiency", "efficient", "quality",
    "quantitative", "qualitative", "empirical", "empirically",
    "significantly", "significant", "extensive", "respectively",
    "general", "specific", "overall", "potential", "effective",
    # common adverbs / connectives that slip past the short stoplist
    "through", "further", "often", "only", "toward", "towards", "address",
    "addresses", "addressed", "addressing", "available", "become", "becomes",
    "make", "makes", "making", "allow", "allows", "including", "include",
    "includes", "included", "particular", "particularly", "especially",
    "recent", "recently", "prior", "current", "currently", "main", "simple",
    "simply", "directly", "fully", "highly", "widely", "largely", "mainly",
    "typically", "generally", "commonly", "finally", "additionally",
    "specifically", "namely", "moreover", "whether", "either", "neither",
    "single", "strong", "remains", "remain", "explicit", "explicitly",
    "implicit", "leading", "leads", "lead", "respective",
    "state-of-the-art", "sota",
    # more plain-English adverbs / connectives
    "even", "still", "yet", "already", "although", "though", "despite",
    "hence", "whereas", "indeed", "rather", "instead", "around", "along",
    "upon", "nonetheless", "besides", "unless", "until", "before", "after",
    "during", "throughout", "every", "anything", "everything", "something",
    "nothing", "someone", "everyone", "anyone", "here", "there", "always",
    "never", "sometimes", "perhaps", "maybe", "likely", "unlikely", "almost",
    "nearly", "quite", "very", "too", "enough", "less", "least", "fewer",
    "former", "latter", "worse", "higher", "lower", "larger", "smaller",
    "greater", "faster", "slower", "stronger", "weaker",
    # research boilerplate verbs ("our method outperforms ...", "we show ...")
    "outperform", "outperforms", "outperformed", "outperforming",
    "surpass", "surpasses", "surpassed", "surpassing", "exceed", "exceeds",
    "boost", "boosts", "boosted", "boosting", "enhance", "enhances",
    "enhanced", "enhancing", "obtain", "obtains", "obtained", "yield",
    "yields", "yielded", "observe", "observes", "observed", "find", "finds",
    "found", "reveal", "reveals", "revealed", "validate", "validates",
    "validated", "verify", "verifies", "verified", "conduct", "conducts",
    "conducted", "consider", "considers", "considered", "develop", "develops",
    "developed", "build", "builds", "built", "apply", "applies", "applied",
    "exploit", "exploits", "exploited", "utilize", "utilizes", "utilized",
    "incorporate", "incorporates", "integrate", "integrates", "integrated",
    "employ", "employs", "employed", "adopt", "adopts", "adopted", "require",
    "requires", "required", "suggest", "suggests", "suggested", "indicate",
    "indicates", "indicated", "report", "reports", "reported", "describe",
    "describes", "contain", "contains", "consist", "consists", "involve",
    "involves", "involved", "focus", "focuses", "focused", "aim", "aims",
    "aimed", "seek", "seeks", "tackle", "tackles", "solve", "solves",
    "solved", "handle", "handles",
    # generic / over-broad technical nouns
    "image", "images", "code", "codes", "text", "texts", "prediction",
    "predictions", "large-scale", "small-scale", "limited", "limitation",
    "limitations", "global", "local", "diverse", "context", "contexts",
    # url / repository boilerplate from "code available at ..." sentences
    "https", "http", "github", "gitlab", "arxiv", "html", "doi",
}

WORD_CLOUD_SKIP = WORD_CLOUD_STOPWORDS | WORD_CLOUD_GENERIC_TERMS

ABSTRACT_FIELD_KEYS = ("abstract", "Abstract", "ABSTRACT")


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


def markdown_field(block: str, label: str) -> str:
    match = re.search(
        rf"\*\*{re.escape(label)}:\*\*\s*(.*?)(?=\n+\*\*[\w\s]+:\*\*|\n+---|\Z)",
        block,
        flags=re.DOTALL,
    )
    if not match:
        return ""
    return " ".join(match.group(1).strip().split())


def parse_archive_markdown_papers(markdown_text: str) -> dict[str, dict]:
    heading_pattern = re.compile(
        r"^##\s+\d+\.\s+\[(?P<title>.*?)\]\((?P<url>https://arxiv\.org/abs/(?P<arxiv_id>[^)]+))\).*?$",
        flags=re.MULTILINE,
    )
    headings = list(heading_pattern.finditer(markdown_text))
    papers = {}

    for idx, heading in enumerate(headings):
        block_start = heading.end()
        block_end = (
            headings[idx + 1].start()
            if idx + 1 < len(headings)
            else len(markdown_text)
        )
        block = markdown_text[block_start:block_end]

        title = heading.group("title").strip()
        arxiv_id = markdown_field(block, "ArXiv ID") or heading.group("arxiv_id")
        authors = markdown_field(block, "Authors")
        abstract = markdown_field(block, "Abstract")
        comment = markdown_field(block, "Comment")
        relevance = markdown_field(block, "Relevance")
        novelty = markdown_field(block, "Novelty")

        if not title or not abstract:
            continue

        paper = {
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": [
                author.strip()
                for author in authors.split(",")
                if author.strip()
            ],
            "abstract": abstract,
            "COMMENT": comment or "Selected by configured paper filters.",
            "primary_category": "ArXiv",
            "categories": [],
        }
        if relevance:
            paper["RELEVANCE"] = relevance
        if novelty:
            paper["NOVELTY"] = novelty
        papers[str(len(papers))] = paper

    return papers


def render_archive_digest(papers_dict: dict) -> str:
    scores = [paper_score(paper) for paper in papers_dict.values()]
    scores = [score for score in scores if score is not None]
    avg_score = f"{sum(scores) / len(scores):.1f}" if scores else "n/a"
    top_score = str(max(scores)) if scores else "n/a"
    grouped_papers = group_indexed_papers(papers_dict)
    queue = "\n".join(
        render_queue_group(category, papers)
        for category, papers in grouped_papers.items()
    )

    return f"""
    <h2 class="section-title" id="paper-content">Reading Queue</h2>
    <nav class="category-groups" aria-label="archived papers by category">
      {queue}
    </nav>
    <section class="archive-summary">
      {render_metric("Archived papers", str(len(papers_dict)))}
      {render_metric("Top score", top_score)}
      {render_metric("Average score", avg_score)}
    </section>
    """


def render_archive_page(archive_date: datetime, markdown_text: str) -> str:
    archived_papers = parse_archive_markdown_papers(markdown_text)
    archive_body = (
        render_archive_digest(archived_papers)
        if archived_papers
        else f"""
    <article class="archive-content">
      {markdown_to_archive_body(markdown_text)}
    </article>
        """
    )

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
    {archive_body}
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
        </a>
        """
        for archive_date, _path in entries
    )
    return f"""
  <section class="archive-block">
    <h2>Past ArXiv</h2>
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
    score_html = ""
    if score is not None:
        tier = "high" if score >= 14 else "mid" if score >= 10 else "low"
        score_html = f'<span class="score-pill score-{tier}">{score}</span>'
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
"""


def render_markdown_paper(paper_entry: dict, idx: int) -> str:
    arxiv_id = paper_entry["arxiv_id"]
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
    abstract = clean_abstract(paper_entry["abstract"])
    authors = ", ".join(paper_entry["authors"])
    title = paper_entry["title"]

    paper_string = f'## {idx}. [{title}]({arxiv_url}) <a id="link{idx}"></a>\n'
    paper_string += f"**ArXiv ID:** {arxiv_id}\n"
    paper_string += f"**Authors:** {authors}\n\n"
    paper_string += f"**Abstract:** {abstract}\n\n"
    if "COMMENT" in paper_entry:
        paper_string += f"**Comment:** {paper_entry['COMMENT']}\n"
    if "RELEVANCE" in paper_entry and "NOVELTY" in paper_entry:
        paper_string += f"**Relevance:** {paper_entry['RELEVANCE']}\n"
        paper_string += f"**Novelty:** {paper_entry['NOVELTY']}\n"
    return paper_string + "\n---\n"


def render_markdown_digest(papers_dict, output_date=None) -> str:
    """Plain-markdown digest used for the dated archive sources and the email
    attachment. The `## N. [title](url)` layout is what `write_archive_pages`
    parses back into archive pages, so keep it in sync with
    `parse_archive_markdown_papers`."""
    output_date = output_date or datetime.today()
    with open("configs/paper_topics.txt", "r") as f:
        criterion = f.read()

    header = (
        "# Personalized Daily ArXiv Papers "
        + output_date.strftime("%m/%d/%Y")
        + f"\nTotal relevant papers: {len(papers_dict)}\n\n"
        + "Paper selection prompt and criteria at the bottom\n\n"
        + "Table of contents with paper titles:\n\n"
    )
    toc = "\n".join(
        f"{i}. [{paper['title']}](#link{i})\n"
        f"**Authors:** {', '.join(paper['authors'])}\n"
        for i, paper in enumerate(papers_dict.values())
    )
    papers = "\n".join(
        render_markdown_paper(paper, i)
        for i, paper in enumerate(papers_dict.values())
    )
    return (
        header
        + toc
        + "\n---\n"
        + papers
        + "\n\n---\n\n"
        + f"## Paper selection prompt\n{criterion}"
    )


def _paper_abstract(paper: dict) -> str:
    for key in ABSTRACT_FIELD_KEYS:
        if paper.get(key):
            return clean_abstract(paper[key])
    return ""


def _singularize(word: str) -> str:
    # lightweight plural folding so e.g. agent/agents count as one word
    if "-" in word or len(word) <= 3:
        return word
    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"
    if word.endswith(("ches", "shes", "sses", "xes", "zes")) and len(word) > 4:
        return word[:-2]
    if word.endswith("s") and not word.endswith(("ss", "us", "is")):
        return word[:-1]
    return word


def abstract_word_counts(papers: list[dict]) -> Counter:
    counts = Counter()
    for paper in papers:
        for word in WORD_CLOUD_RE.findall(_paper_abstract(paper).lower()):
            word = _singularize(word.strip("'-"))
            if len(word) < 4 or word in WORD_CLOUD_SKIP:
                continue
            counts[word] += 1
    return counts


def render_word_cloud(papers: list[dict], max_words: int = 45) -> str:
    # take the most frequent words, then show them alphabetically so the big and
    # small ones interleave into a cloud (deterministic, unlike a shuffle)
    cloud = sorted(abstract_word_counts(papers).most_common(max_words))
    if not cloud:
        return '<p class="cloud-empty">No abstracts available yet.</p>'

    counts = [count for _, count in cloud]
    lo, hi = math.sqrt(min(counts)), math.sqrt(max(counts))
    span = hi - lo
    words = []
    for word, count in cloud:
        weight = 0.5 if span == 0 else (math.sqrt(count) - lo) / span
        size = 0.82 + weight * 1.95
        # smooth, theme-aware colour ramp from accent (rare) to accent-2 (frequent)
        mix = round(weight * 100)
        opacity = round(0.5 + 0.5 * weight, 2)
        style = (
            f"font-size:{size:.2f}rem;"
            f"opacity:{opacity};"
            f"color:color-mix(in srgb, var(--accent-2) {mix}%, var(--accent))"
        )
        words.append(
            f'<span class="cloud-word" style="{style}"'
            f' title="{count} mentions">{esc(word)}</span>'
        )
    return f'<div class="word-cloud">{"".join(words)}</div>'


def collect_recent_papers(output_date=None) -> list[dict]:
    papers = []
    for _archive_date, path in get_recent_archive_entries(output_date):
        try:
            markdown_text = Path(path).read_text()
        except OSError:
            continue
        papers.extend(parse_archive_markdown_papers(markdown_text).values())
    return papers


def render_word_cloud_section(papers_dict, output_date=None) -> str:
    today_papers = list(papers_dict.values())
    month_papers = today_papers + collect_recent_papers(output_date)
    return f"""
  <h2 class="section-title">Abstract word clouds</h2>
  <div class="cloud-grid">
    <article class="cloud-card">
      <h3>Today</h3>
      {render_word_cloud(today_papers)}
    </article>
    <article class="cloud-card">
      <h3>Past month</h3>
      {render_word_cloud(month_papers, max_words=60)}
    </article>
  </div>
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

  {render_word_cloud_section(papers_dict, output_date)}

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
            f.write(render_markdown_digest(output))

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
