---
name: job_triage
description: Refreshes the job queue from the "Vacantes para Mario" Sheet, reads postings with Playwright and ranks them by fit against Mario's CV. Use when the user asks to "triage", "refresh the queue", "update vacantes", "rank the jobs" or "what should I apply to next".
---

# Job triage

Turns the Sheet of vacancies into a ranked shortlist, so Mario only spends time on jobs he can get and wants.

## Inputs

- `vacantes.xlsx` (repo root): the latest export of the Sheet. **Always keep it at the root.** Refresh it whenever the Sheet changes (step 1).
- `jobs/queue.csv`: one row per unique job, built from the export.
- `Mario_Granada_Senior_Software_Engineer_CV.md`, `constitution.md`, `minimum_salary.md`, `AGENTS.md`.

## Step 1: Refresh the export (when the Sheet changed or the file is missing)

The Sheet is the source of truth and changes twice a day, so do this at the start of every queue or triage session. Use the **`playwright-sheet`** MCP server (visible, because claude.ai blocks headless browsers), never the headless `playwright` one. Open https://claude.ai/artifact/8onQyXHwM6TVVm9x8bVuxz. If claude.ai asks for a sign-in, ask Mario to sign in in that window and wait with `page.waitForURL`. Then, in `browser_run_code_unsafe`:

1. Save the sign-in: `await page.context().storageState({ path: '/Users/mariogranada/.playwright-auth/linkedin.json' })`.
2. Click the title button (`Vacantes para Mario – Nov 2026`), then `Export` (`.click().catch(() => {})`), which opens a dialog with Excel and CSV. Then wait for `page.waitForEvent('download')` while clicking `Excel`.
3. `download.saveAs('<repo>/vacantes.xlsx')`, overwriting the old copy.

Never edit the Sheet. It's read-only for us.

## Step 2: Rebuild the queue

`python3 scripts/build_queue.py`. It keeps triage results already in the CSV. Columns that matter:

- `status`: `todo`, `letter_ready` (a `jobs/` folder exists), `applied`, `discarded`, `referral`.
- `gate`: work-rights pre-filter from the Sheet's permit column. `ok` and `check` can be applied to now. `spain_permit` means a Spanish employer contract, which the DNV doesn't cover. `eu_permit` means another EU country's permit. `visa` means UK, US, Canada or Switzerland. `blocked` means the posting rules Mario out.

## Step 3: Fetch postings

`node scripts/fetch_postings.mjs --gate ok,check --priority 1,2 --limit 50` (run it in the background). It saves each posting to `jobs/triage/postings/<key>.md` and waits 20–40 s between them. Stay at about 50 postings a day. If it reports a LinkedIn sign-in wall, follow the refresh steps in `AGENTS.md`.

## Step 4: Score each fetched posting

Read each posting file that has no verdict yet. Score fit from 1 to 5 against the CV only:

- **Stack**: how many of the must-haves the CV shows (React, Next.js, TypeScript, Node.js, design systems, Elixir and Phoenix LiveView, testing, AI-assisted development).
- **Level**: senior, staff or lead roles fit his 14+ years. Penalize junior roles and hard people-management roles.
- **Product**: product engineering, design systems or frontend architecture count most.
- **Work rights**: remote from Estonia now, and from Spain under the DNV from 23 Jan 2027 (a non-Spanish employer). Read `spain/` before deciding on anything Spain-related.
- **Pay**: if the posting states pay, it must reach the floors in `minimum_salary.md`.

Vetoes (verdict `skip`, or `closed` when the posting is closed): closed posting; residence or a visa Mario doesn't have and the company doesn't sponsor; a required language other than English or Spanish; stated pay below the floor; a core must-have the CV doesn't show (e.g. Unity, native iOS, Java backend).

Record each result: `python3 scripts/triage.py set <key> <fit> <apply|maybe|skip|closed> "<one line: why, and the gaps>"`. Notes are short, and the gaps are named plainly. It rebuilds `jobs/triage.md`.

## Step 5: Reply

Link `jobs/triage.md` and list the `apply` jobs with fit 4–5. Mario picks which ones get an application pack (cover letter through `cover_letter_writer`, which can reuse the saved posting instead of fetching it again, plus answers from `application_answers_bank.md`). Never submit anything for him.
