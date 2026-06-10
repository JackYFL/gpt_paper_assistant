# Daily ArXiv: Personalized paper assistant

A daily ArXiv scanner that finds papers you actually want to read. Every day it pulls new
papers from your chosen ArXiv categories, scores them with a GPT model against your research
interests (plus author matches via Semantic Scholar), and delivers a ranked digest to:

- 🌐 **A static website** published on GitHub Pages — [live demo](https://jackyfl.github.io/gpt_paper_assistant/)
- 📧 **Your inbox** — a daily email digest with the paper list and a Markdown attachment
- 💬 **Slack** (optional) — pushed to a channel via a bot

Everything runs unattended on GitHub Actions; no server needed.

This repo is a fork of [tatsu-lab/gpt_paper_assistant](https://github.com/tatsu-lab/gpt_paper_assistant)
with an email pipeline, a redesigned web page, and daily archives added.

## Features

- **Two-stage filtering**
  1. *Author match*: papers by authors you follow (matched by Semantic Scholar author ID) are
     kept automatically with a configurable score.
  2. *GPT scoring*: remaining papers (pre-filtered by author h-index to control cost) are
     batched and scored by a GPT model for **relevance** and **novelty** (1–10 each) against
     the criteria you write in `configs/paper_topics.txt`. Papers below your cutoffs are dropped.
- **A polished daily web page** (`out/index.html`)
  - Reading queue grouped by ArXiv category and fine-grained topic tags, with collapsible sections
  - Score badges color-coded by tier, expandable rows with abstract and a "why selected" note
  - Automatic dark mode, responsive layout
  - **Past ArXiv archives**: the last month of digests is preserved as browsable pages
- **Email digest**: a daily HTML email listing the selected papers, with the full Markdown
  digest attached, sent to a configurable recipient list via SMTP (Gmail supported).
- **Fully automated**: a GitHub Actions cron job runs the scanner daily at 13:00 UTC, commits
  the outputs back to the repo, publishes the site to GitHub Pages, and sends the email.

## How it works

```text
ArXiv RSS feeds ──> new papers (UPDATED entries filtered out)
        │
        ├─ author match via Semantic Scholar ──────────────┐
        │                                                  ▼
        └─ h-index prefilter ──> GPT relevance/novelty ──> ranked paper set
                                                           │
                       ┌───────────────┬───────────────────┤
                       ▼               ▼                   ▼
                 out/index.html   email digest        Slack (optional)
                 (GitHub Pages)   (+ .md attachment)
```

Papers are ranked by the max of their author-match score and the sum of GPT relevance +
novelty scores, then rendered to JSON, Markdown, and HTML in `out/`.

## Quickstart (GitHub Actions)

1. **Fork this repo** and [enable scheduled workflows](https://docs.github.com/en/actions/using-workflows/disabling-and-enabling-a-workflow).
2. **Define your interests**: copy `configs/paper_topics.template.txt` to
   `configs/paper_topics.txt` and describe the topics you want to follow (see
   [writing the topic prompt](#writing-the-topic-prompt) below).
3. **Follow authors**: copy `configs/authors.template.txt` to `configs/authors.txt` and list
   authors as `Name, <semantic scholar author ID>`. The ID is the number at the end of an
   author's Semantic Scholar URL.
4. **Pick categories**: set `arxiv_category` in `configs/config.ini` (e.g. `cs.AI, cs.CV`).
5. **Set secrets** ([repo secrets guide](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)):
   - `OAI_KEY` (required) — OpenAI API key
   - `EMAIL_KEY` (for email) — sender's SMTP app password (for Gmail, an [app password](https://support.google.com/accounts/answer/185833))
   - `S2_KEY` (recommended) — Semantic Scholar API key, makes author lookup much faster
   - `SLACK_KEY`, `SLACK_CHANNEL_ID` (optional) — for Slack push
6. **Configure email**: in `configs/config.ini` set `send_email` (sender address) and
   `receive_emails` (comma-separated recipients) under `[EMAIL]`, or set
   `push_to_email = false` to disable.
7. **Enable GitHub Pages**: in repo settings, set the Pages build source to
   [GitHub Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow).

Trigger the `Run daily arxiv` workflow manually once to test; after that it runs daily.
Tip: keep the repo active (GitHub disables scheduled workflows in repos with
[no activity for 60 days](https://docs.github.com/en/actions/using-workflows/disabling-and-enabling-a-workflow)).

## Configuration

All knobs live in `configs/config.ini`:

| Section | Key | What it does |
| --- | --- | --- |
| `SELECTION` | `model` | GPT model used for scoring (don't use small/cheap models except for debugging — quality matters here) |
| | `batch_size` | papers per GPT call; larger is cheaper but less accurate |
| | `author_match_score` | score assigned to author-matched papers |
| `FILTERING` | `arxiv_category` | comma-separated ArXiv categories to scan |
| | `force_primary` | ignore papers only cross-listed into your categories |
| | `hcutoff` | drop papers with no author above this h-index before GPT scoring (cost control) |
| | `relevance_cutoff`, `novelty_cutoff` | minimum GPT scores to keep a paper |
| | `author_match` | enable/disable the author-match stage |
| `OUTPUT` | `dump_json`, `dump_md`, `push_to_slack` | output endpoints |
| `EMAIL` | `push_to_email`, `send_email`, `receive_emails` | email digest settings |

### Writing the topic prompt

`configs/paper_topics.txt` is the heart of the filter — it tells GPT what you care about.
Be specific, and spell out both what *is* and *is not* relevant:

```text
1. New methodological improvements to RLHF or instruction-following.
   - Relevant: papers proposing or analyzing specific methods like RLHF or
     instruction-tuning datasets.
   - Not relevant: papers that merely apply instruction-following to a task.
2. Shows new test set contamination or membership inference methods for language models.
   - Relevant: statistics that detect benchmark contamination; general membership
     inference methods applicable to LMs.
   - Not relevant: papers that do not consider language models.
```

Ending with a short description of your general taste also helps, e.g. *"Your friend enjoys
statistical ML and generative modeling in NLP, and surprising empirical results in language
models; he does not want application-only papers."*

## Running locally

```bash
pip install -r requirements.txt
export OAI_KEY=...            # required
export S2_KEY=...             # recommended
export EMAIL_KEY=...          # if push_to_email is enabled
python main.py                # scan, filter, render out/index.html + out/output.md
python send_emails.py         # send the email digest for today's output
```

The scanner only looks at the last day's RSS feed, so run it daily (e.g. via crontab:
`0 13 * * * python ~/gpt_paper_assistant/main.py`) to avoid missing papers.

## Testing and improving the GPT filter

`filter_papers.py` can run standalone: it reads a batch of papers from
`in/debug_papers.json`, applies your current config and prompts, and writes results to
`out/filter_paper_test.debug.json`. When the bot misjudges a paper, copy the corresponding
batch from `out/gpt_paper_batches.debug.json` into `in/debug_papers.json` to build a small
benchmark for prompt iteration.

## Repo layout

```text
main.py              # daily pipeline: scrape -> filter -> render -> push
arxiv_scraper.py     # ArXiv RSS scraping
filter_papers.py     # author matching + GPT scoring (standalone-runnable)
parse_json_to_md.py  # renders the web page, Markdown digest, and monthly archives
send_emails.py       # email digest via SMTP
push_to_slack.py     # optional Slack push
configs/             # config.ini, topic prompt, author list, GPT prompt templates
out/                 # generated outputs (index.html, output.md, past_arxiv/ archives)
.github/workflows/   # daily cron run + GitHub Pages publishing
```

## Contributing

This repo uses [ruff](https://github.com/astral-sh/ruff): `ruff check .` and `ruff format .`.
Install the pre-commit hook with `pre-commit install`.

## Credits and license

Originally built by Tatsunori Hashimoto ([tatsu-lab/gpt_paper_assistant](https://github.com/tatsu-lab/gpt_paper_assistant)),
licensed under Apache 2.0. Thanks to Chenglei Si for testing and benchmarking the GPT filter.
