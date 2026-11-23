# Job Applications

Mario Granada's job-search workspace (Tallinn, Estonia): CV, LinkedIn profile text, cover letters, application answers, a contract-rate analysis and LinkedIn thumbnails. There's no application code here.

## What's here

| Path | What it is |
|---|---|
| `Mario_Granada_Senior_Software_Engineer_CV.md` | Source of truth for the CV text. Mirrors the final docx word for word. |
| `Mario Granada - Senior Software Engineer CV.docx` / `.pdf` | The final CV, edited and exported from Google Docs. |
| `cover_letter_template.md` | Approved cover letter template. |
| `jobs/<Company>-<Role>/` | One folder per application: `cover_letter.md`, `job_posting.md`, and sometimes `application_answers.md` or `linkedin_message.md`. |
| `cv_development/` | LinkedIn profile text (source of truth) and older CV iterations. |
| `minimum_salary.md` | Minimum net pay (€4,400/month) and the gross salary or invoice it requires in each setup. |
| `rate/` | Contract-rate and tax model for Estonia. |
| `spain/` | Relocation plan to Spain and the official digital nomad visa (DNV) requirements. |
| `linkedin-thumbnails/` | HTML cards screenshotted into LinkedIn link-preview images. |
| `.claude/skills/cover_letter_writer/` | Claude Code skill that writes a tailored cover letter from a job URL. |

## Write a cover letter

In Claude Code, from this folder:

```
create the cover letter for job https://www.linkedin.com/jobs/view/<id>/
```

The skill reads the posting with Playwright (LinkedIn needs the signed-in browser), writes `jobs/<Company>-<Role>/cover_letter.md` and `job_posting.md`, and flags any requirement the CV doesn't cover.

Then paste `cover_letter.md` into a copy of the Google Docs template, rename the doc to `Mario Granada - Cover Letter - <Company>` and use File → Download → PDF. The doc name becomes the PDF's Title metadata.

## Export the CV

Rename the Google Doc to `Mario Granada - Senior Software Engineer CV`, then File → Download → PDF. No dates or version numbers in the name.

## Rate model

```bash
cd rate && python3 calc_rates.py
```

Edit the `ASSUMPTIONS` block at the top, re-run, then update `rate-analysis.md` and `ou-tax-guide.md` by hand.

## For AI agents

- `AGENTS.md`: rules, settled decisions and conventions (`CLAUDE.md` imports it).
- `constitution.md`: the principles behind every piece of writing in this repo.
- `MEMORY.md`: dated decisions, lessons learned and the applications log.
