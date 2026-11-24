# AGENTS.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Mario Granada's job-search workspace (Tallinn, Estonia). It holds no application code. It contains the CV, the LinkedIn profile text, cover letters, an analysis of contract rates and taxes, and LinkedIn thumbnail images. Most tasks involve writing, auditing for ATS and recruiters, and keeping the CV and LinkedIn consistent with each other.

## Before you start

- Read `constitution.md` before writing anything for Mario (letters, answers, messages). It holds the principles behind these rules.
- Check `MEMORY.md` for dated decisions, lessons learned and the applications log. When a decision is made or an application is added, record it there with the date.
- `README.md` is the human-facing overview. Keep it in sync when the layout or workflow changes.

## Layout

- `Mario_Granada_Senior_Software_Engineer_CV.md` (root): **source of truth for the CV text.** It mirrors the final docx word for word. Bullets use `• ` with a blank line between each, so they paste cleanly into Google Docs and LinkedIn.
- `Mario Granada - Senior Software Engineer CV.docx` / `.pdf` (root): the current, final CV as exported from Google Docs. Their names keep spaces because the Google Doc name becomes the PDF Title metadata (see the naming rule below).
- `cv_development/`
  - `LinkedIn_Profile_Nov2026.md`: **source of truth for the LinkedIn text.** Each field (Headline, About, each position, Education) is in a copyable code block. It mirrors the live profile at linkedin.com/in/mariogranadacolombia.
  - `CV_MarioGranada_Nov2026_v2.md`, `CV_MarioGranada_Nov2026_old.docx`, `Copy of CV_MarioGranada_Nov2026 (7).docx`: older iterations, superseded by the root CV `.md`. Keep for reference only and don't edit them.
- `cover_letter_template.md`: base cover letter with `[Company]`, `[Role]` and `[date]` placeholders. Every paragraph except "What draws me to…" is approved and stays word for word.
- `jobs/<Company>-<Role>/`: one folder per application (e.g. `jobs/Wrike-Senior_AI_Product_Builder/`), holding `cover_letter.md` (ready to paste into the Google Docs template) and `job_posting.md` (the posting as read). `Loka/` predates this convention.
- `.claude/skills/cover_letter_writer/`: skill that reads a job posting URL with Playwright and writes the tailored cover letter into `jobs/`. Trigger it with "create the cover letter for job <url>".
- `vacantes.xlsx` (root): the latest Excel export of Mario's vacancies Sheet ("Vacantes para Mario – Nov 2026", claude.ai/artifact/8onQyXHwM6TVVm9x8bVuxz). **Always keep it at the root, and export it again whenever the Sheet is updated** (steps in `.claude/skills/job_triage/`). The Sheet is the source of truth for jobs and their status (see `constitution.md`). It's updated twice a day and is read-only for us. Never edit it.
- `jobs/queue.csv`: one row per unique job from the export, with work-rights `gate`, `status` and triage results. Rebuild it with `python3 scripts/build_queue.py` after every new export. `jobs/triage/postings/` holds postings read by `scripts/fetch_postings.mjs`, and `jobs/triage.md` is the ranked shortlist written by `scripts/triage.py`.
- `.claude/skills/job_triage/`: skill that refreshes the export, rebuilds the queue, fetches postings and ranks them. Trigger it with "triage the queue".
- `minimum_salary.md` (root): Mario's minimum net pay (€4,400/month), with the gross salary, company cost and contractor invoice needed in each setup (Spain or Estonia, employee or contractor).
- `rate/`: contract-rate analysis for Estonia (individual vs FIE vs OÜ "Munbuh Corp OÜ"). `calc_rates.py` holds the model. `rate-analysis.md` and `ou-tax-guide.md` are the write-ups built from its output. `tax_calculator.xlsx` is an editable spreadsheet (Employee and B2B tabs, live formulas) for Google Sheets.
- `spain/`: relocation to Spain. `spain_relocation_dnv_context.md` is Mario's visa, tax and relocation plan. `dnv_requirements_tallinn.md` holds the official DNV requirements and procedure from the Spanish Embassy in Tallinn.
- `linkedin-thumbnails/`: standalone HTML cards (1200×627 body, LinkedIn link-preview size) that are screenshotted at 2× to make the matching PNGs. `plugin-ui.png` is a source screenshot that `figma-plugin.html` embeds.

## Commands

- Job queue: `python3 scripts/build_queue.py` (export → `jobs/queue.csv`), `node scripts/fetch_postings.mjs --gate ok,check --priority 1,2 --limit 50` (postings → `jobs/triage/postings/`, run in the background, at about 50 a day), `python3 scripts/triage.py set <key> <fit> <verdict> "<notes>"` or `python3 scripts/triage.py report`. Run `npm install` once for Playwright.
- Rate model: `cd rate && python3 calc_rates.py`. Edit the `ASSUMPTIONS` block at the top, re-run, then update the numbers in `rate-analysis.md` / `ou-tax-guide.md` by hand. Tax rates are marked as assumptions to verify before relying on them.
- Read a docx: `textutil -convert txt -stdout file.docx`, or `unzip -p file.docx word/document.xml` to inspect its structure.
- Read a PDF and check for hidden characters: `pdftotext file.pdf -`. Google Docs exports can contain U+200B. Check the metadata with `pdfinfo file.pdf`.

## Hard rules

- **Never modify any `.docx` or `.pdf`.** Mario edits those in Google Docs himself. Only edit the `.md` files, then tell him what to change in the doc.
- The root CV `.md` and the LinkedIn `.md` must stay in sync with the final docx and the live profile. When one changes, check whether the other needs the same change.
- **Naming:** always use `_` instead of spaces in every file and folder name you create or rename. The only exceptions are `Mario Granada - Senior Software Engineer CV.docx` and `Mario Granada - Senior Software Engineer CV.pdf`. In `jobs/<Company>-<Role>/`, the single hyphen separates the company from the role. (Google Doc titles used for the PDF Title metadata, e.g. `Mario Granada - Cover Letter - <Company>`, live in Google Drive, not in this repo, so they keep spaces.)
- **Cover letters:** Mario is available to start immediately and willing to relocate from Tallinn. For on-site or hybrid roles elsewhere, the letter says "willing to relocate to <city>". Address the letter to the person named in the posting (hiring manager first, then job poster or recruiter), and use "Hiring Team" only when no one is named. Every claim must come from the root CV `.md`.
- **Relocation timeline:** Tallinn until mid-December 2026, Colombia until 22 Jan 2027 (a family visit only), Alicante (Spain) from 23 Jan 2027. The full plan is in `spain/spain_relocation_dnv_context.md`. For contracts, tax, social security and employer setup, treat the Colombia weeks exactly as working from Estonia. Don't raise Colombia as a separate case or complication.
- **Digital nomad visa (DNV):** whenever the Spanish DNV (*visado de teletrabajo* / *nómada digital*, COLELETEL) comes up, read `spain/dnv_requirements_tallinn.md` (the official requirements and procedure from the Spanish Embassy in Tallinn) together with `spain/spain_relocation_dnv_context.md` (Mario's own visa and plan). Base any visa advice on them.
- **Minimum pay:** Mario's absolute minimum is **€4,400 net/month**. Never suggest, accept or draft a salary or rate below the floors in `minimum_salary.md` (e.g. €75,000/year gross as an employee in Spain with Beckham). Contractor floors are break-even only; the ask stays €480–500/day.
- **Banned technologies:** never mention these in any output, whether a skill, a cover letter, a message or a suggestion. Use the replacement instead:

  | Never mention | Use instead |
  |---|---|
  | WebdriverIO | Playwright |

- **Spanish:** whenever you write in Spanish (messages, answers, cover letters, any output), use Colombian Spanish. Use "usted" in professional messages and "ustedes", never "vosotros". Avoid Spain-only forms such as "valoráis", "os", "vale" and "ordenador". Write "hoja de vida" instead of "CV" or "currículum", and sign off with "Cordial saludo".
- **Don't invent metrics.** Mario will add real numbers later.
- Mario pushes back on clutter. Keep suggestions minimal and concrete, and don't re-propose ideas he has already declined (listed below).

## Settled decisions (don't re-litigate)

**CV (ATS-oriented):** single column, Arial, real Word bullets, no zero-width characters. Sections are `SUMMARY / WORK EXPERIENCE / EDUCATION`, with no roman numerals.

- Headline (identical on the CV and LinkedIn): `Senior Software Engineer | Product Engineer | Full-Stack · Frontend & Design Systems | AI-Assisted Development`. No technologies in the headline.
- Degree: "B.Sc. Telematics Engineering — Universidad ICESI, Cali, Colombia | 2013". Always "Telematics", never "Telecommunications".
- ATS keyword spellings: Phoenix LiveView, Redux-Saga, Spec-Driven Development, REST APIs, Playwright Test Agents. Avoid slash-joined tokens.
- Client attribution: SpotOn → Encora. IntelePeer → DevSavant, on the AWS API Gateway bullet only. Mack Weldon and Effie.org → Razorfish.
- Yolo is **one** CV entry, opening with the Moon Design System. Razorfish (formerly Intersect & Crown Partners) is **one** CV entry, Sep 2012 – Feb 2015.
- Leaving the gap from Feb 2015 to Apr 2016 off the CV is intentional. So is Globant starting in Aug 2016, the same month Grability ends.
- Technical Skills was trimmed on purpose (AngularJS, PHP, jQuery, Jira and Confluence appear only in the bullets). Don't add them back.

**LinkedIn:** bullets only, with no per-position "Skills:" lines.

- Yolo is **two** positions with friendly titles: "Software Engineer at Design System team" and "Software Engineer at Casino team".
- Intersect, Crown Partners and Razorfish are separate positions. Mack Weldon and Effie.org appear under both Crown Partners and Razorfish on purpose, to show how the role evolved.
- Declined ideas: acquisition disclaimer lines, renaming the Yolo titles, removing old skills that colleagues endorsed.
- Top skills: React.js, Next.js, TypeScript, Node.js, AI for Product Development.
- On the certifications page, an attached certificate file can look like a duplicate entry. It isn't one.

**PDF export:** rename the Google Doc to `Mario Granada - Senior Software Engineer CV` before File → Download → PDF. The PDF Title comes from the doc name. Don't put dates or "v2" in names.

## Pending (as of 21 Nov 2026)

- 30 Nov 2026: Coursy ends. Add the end date on LinkedIn and replace "Present" on the CV.
- Add real metrics to 2–3 bullets once Mario provides them.

## Tooling notes

- Playwright runs from `.mcp.json` with `--isolated`, so several sessions can each have their own browser. The `playwright` server is `--headless`: use it for LinkedIn and everything else. The `playwright-sheet` server is visible and is used only to export the Sheet, because claude.ai's bot check blocks headless browsers. A standalone Playwright script was tried and claude.ai disabled Export there, so export only through `playwright-sheet`. The LinkedIn login is loaded from `~/.playwright-auth/linkedin.json`, which is kept outside the repo because it holds live cookies. When LinkedIn shows a sign-in wall, refresh the file with `npx playwright codegen --save-storage=$HOME/.playwright-auth/linkedin.json https://www.linkedin.com/login`, sign in, close the window, then restart the session.
- Validating LinkedIn with Playwright needs Mario's signed-in browser. Scroll to the end of the lazy-loaded Experience and Skills lists before drawing conclusions. Delete `.playwright-mcp/` and any scraped files from the workspace afterwards.
- The Spanish recruiter checklist lives in a Claude Doc, "Perfil de LinkedIn de Mario – mejoras" (claude.ai/artifact/LTmbyvBLZyKH3yPBfR4RGs). If the Docs connector refuses to read it, read it through a Playwright snapshot instead.
