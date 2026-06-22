# CLAUDE.md

Guidance for AI assistants working in this repository.

## What this project is

A daily ArXiv paper assistant. Each day it scrapes new papers from chosen ArXiv
categories, scores them with an OpenAI model against the user's research
interests (plus author matches via Semantic Scholar), and publishes a ranked
digest to three endpoints: a static website on GitHub Pages, an email digest,
and (optionally) Slack. It runs unattended on GitHub Actions; there is no
server.

This is a fork of [tatsu-lab/gpt_paper_assistant](https://github.com/tatsu-lab/gpt_paper_assistant)
that adds an email pipeline, a redesigned web page, and daily archives.

## Pipeline overview

`main.py` is the daily entry point and orchestrates everything in this order:

1. **Scrape** — `arxiv_scraper.get_papers_from_arxiv_rss_api` pulls the last
   day's RSS feed for each category in `arxiv_category`. Only entries with
   `arxiv_announce_type == "new"` are kept (updates are dropped). Each becomes
   a `Paper` dataclass.
2. **Author lookup** — every paper author is resolved to Semantic Scholar
   metadata (h-index, author IDs) via batched API calls.
3. **Author match** (`filter_papers.filter_by_author`) — papers by a followed
   author (from `configs/authors.txt`) are auto-selected with
   `author_match_score`.
4. **GPT scoring** (`filter_papers.filter_by_gpt`) — remaining papers are:
   - prefiltered by author h-index (`hcutoff`) to control cost,
   - title-filtered by an LLM call that drops obviously-irrelevant papers,
   - batched (`batch_size`) and scored for **RELEVANCE** and **NOVELTY**
     (1–10 each); papers below `relevance_cutoff` / `novelty_cutoff` are dropped.
5. **Rank** — papers are sorted by `max(author_match_score, relevance + novelty)`.
6. **Render & push** — `parse_json_to_md.py` writes `out/output.json`,
   `out/output.md`, `out/index.html`, a dated digest `out/output_YYYY_MMDD.md`,
   and monthly archive pages under `out/past_arxiv/`. Then optionally Slack
   (`push_to_slack.py`); email is sent separately by `send_emails.py`.

## Files

| File | Role |
| --- | --- |
| `main.py` | Daily orchestrator: scrape → author lookup → filter → render → push. Contains Semantic Scholar batch helpers. |
| `arxiv_scraper.py` | ArXiv RSS/API scraping; defines the `Paper` dataclass and `EnhancedJSONEncoder`. |
| `filter_papers.py` | Author matching, h-index prefilter, GPT title filter, GPT scoring, and cost calculation. **Standalone-runnable** for prompt iteration. |
| `parse_json_to_md.py` | Largest file. Renders the HTML site (with inline CSS), Markdown digest, topic/category grouping, word cloud, and `past_arxiv/` archive pages. |
| `send_emails.py` | SMTP email digest (Gmail). Reads `out/output.json` + today's dated `.md` attachment. **Standalone-runnable.** |
| `push_to_slack.py` | Optional Slack push via `slack_sdk`. |
| `configs/` | `config.ini` plus the prompt and list text files (see below). |
| `in/debug_papers.json` | Input batch for the standalone `filter_papers.py` benchmark. |
| `out/` | Generated outputs, **committed back to the repo** by the cron job. |
| `.github/workflows/` | `cron_runs.yaml` (daily run + commit + email) and `publish_md_test.yml` (GitHub Pages deploy). |

## Configuration (`configs/`)

All knobs live in `configs/config.ini` (read with `configparser`):

- **`[SELECTION]`** — `model` (OpenAI model id), `reasoning_effort`,
  `batch_size`, `author_match_score`, `run_openai`.
- **`[FILTERING]`** — `arxiv_category` (comma-separated), `force_primary`,
  `hcutoff`, `relevance_cutoff`, `novelty_cutoff`, `author_match`.
- **`[OUTPUT]`** — `debug_messages`, `dump_debug_file`, `output_path`,
  `dump_json`, `dump_md`, `push_to_slack`.
- **`[EMAIL]`** — `push_to_email`, `send_email` (sender), `receive_emails`
  (comma-space-separated recipients).

Prompt/list files, all plain text:

- `paper_topics.txt` — the heart of the filter: the user's numbered research
  criteria, fed to GPT as the matching rubric. Has a `.template.txt` companion.
- `authors.txt` — followed authors as `Name, <semantic scholar author ID>`;
  `#` lines are comments. Has a `.template.txt` companion.
- `base_prompt.txt` — system framing prepended to every GPT call.
- `postfix_prompt.txt` — output-format instructions (JSONL with
  `ARXIVID, COMMENT, RELEVANCE, NOVELTY, TAGS`).

`configs/keys.ini` is gitignored and only used by the standalone
`filter_papers.py` path. The main pipeline reads keys from **environment
variables**, not `keys.ini`.

## Secrets / environment variables

The main pipeline and GitHub Actions read keys from the environment:

- `OAI_KEY` — OpenAI API key (**required**; `main.py` raises if missing).
- `S2_KEY` — Semantic Scholar API key (recommended; without it author lookup
  sleeps 1s/request instead of 20ms to avoid rate limits).
- `EMAIL_KEY` — sender SMTP app password (for email).
- `SLACK_KEY`, `SLACK_CHANNEL_ID` — optional Slack push.

In Actions these come from repo secrets; locally, `export` them.

## Running locally

```bash
pip install -r requirements.txt
export OAI_KEY=...            # required
export S2_KEY=...             # recommended
export EMAIL_KEY=...          # only if push_to_email is enabled
python main.py               # scrape, filter, render out/
python send_emails.py        # send today's digest (reads out/output.json)
```

`main.py` only looks at the last day of RSS, so it must run daily to avoid
missing papers.

### Iterating on the GPT filter

`filter_papers.py` runs standalone: it reads `in/debug_papers.json`, applies the
current config and prompts, and writes `out/filter_paper_test.debug.json`. To
build a benchmark, copy a batch from `out/gpt_paper_batches.debug.json` (emitted
when `dump_debug_file = true`) into `in/debug_papers.json`. Note this path reads
keys from `configs/keys.ini`, unlike `main.py`.

## GitHub Actions

- **`cron_runs.yaml`** (`Run daily arxiv`) — runs daily at 13:00 UTC (and on
  manual dispatch). Installs deps, runs `python main.py`, commits the `out/`
  changes back to `main` via `GITHUB_TOKEN`, runs `send_emails.py`, and uploads
  `out/` as an artifact.
- **`publish_md_test.yml`** — deploys to GitHub Pages on push to `main` that
  touches `out/index.html`, `out/past_arxiv/**`, or `out/output.md`, and after
  the daily workflow completes. Prefers the prebuilt `index.html`.

The daily run commits generated outputs into the repo, so `out/` churns
constantly on `main`. Treat those as machine-generated.

## Conventions

- **Python 3.10** (matches CI). Code uses 3.10+ syntax (e.g. `int | None`).
- **Formatting/linting: ruff.** Run `ruff check .` and `ruff format .` before
  committing. A pre-commit hook is configured (`pre-commit install`); the hook
  pins ruff `v0.1.5`.
- Papers flow as the `Paper` dataclass (in `arxiv_scraper.py`); serialize with
  `EnhancedJSONEncoder`. Papers are keyed by `arxiv_id` throughout.
- OpenAI calls go through `filter_papers.call_chatgpt`, which prefers the
  Responses API (`responses.create` with `reasoning.effort`) and falls back to
  chat completions. New models need a price entry in `MODEL_PRICES_PER_MTOK`
  for cost reporting, but pricing only affects logging, not behavior.
- Don't commit secrets. `configs/keys.ini` is gitignored; real keys belong in
  env vars / repo secrets.

## Working on this repo

- The development branch for this work is `claude/claude-md-docs-568r9k`.
- Commit and push only when asked; never open a PR unless explicitly requested.
- When changing the GPT scoring behavior, keep `base_prompt.txt`,
  `postfix_prompt.txt`, and the parsing in `run_and_parse_chatgpt` /
  `filter_by_gpt` in sync — the code expects exactly the JSONL fields the
  postfix prompt requests.
- When editing rendering, remember both HTML (`render_html_string`) and Markdown
  (`render_md_string` / `render_markdown_digest`) outputs exist and the archive
  pages are re-parsed from saved Markdown.
