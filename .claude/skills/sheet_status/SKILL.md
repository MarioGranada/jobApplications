---
name: sheet_status
description: Sets a job's "Estado" dropdown in Mario's "Vacantes para Mario" Sheet (Aplicado, Entrevista, Descartado...), finding each job by its link. Use when Mario says he applied to a job or a batch ("applied to job <url>", "applied to these", "applied to all the apply ones"), or reports another change (interview, rejected, offer, referred, discarded).
---

# Sheet status

Mario submits applications himself. When he says he did, this skill marks the job in the Sheet, so the Sheet stays the source of truth (see `constitution.md`).

## Rules

- **The only cell this skill changes is a job's `Estado` dropdown, and only when Mario says so.** Every other cell, row, tab and dropdown option stays as it is. Never add, edit or remove dropdown options.
- **Find jobs by link, never by row number.** Rows move with every morning and afternoon update. `mark_status.js` reads each tab's `Link` column and matches the LinkedIn job id (or the URL without query, hash and trailing slash). It marks every row with that link, in any tab.
- The Docs connector can't reach this Sheet: it's shared from another organization, and the connector refuses it. Edit it through its page in the Playwright browser, which is signed in to claude.ai (`~/.playwright-auth/linkedin.json`).
- Use the visible `playwright-sheet` MCP server (`mcp__playwright-sheet__*`), because claude.ai shows a bot check to headless browsers. If those tools aren't loaded, use whichever Playwright browser loads the Sheet. Never try to get past a bot check.

## What Mario says → Estado

| Mario says | Estado |
|---|---|
| applied, submitted, sent | Aplicado |
| interview, call, screening | Entrevista |
| offer | Oferta |
| rejected, discarded, not a fit, closed, skip it | Descartado |
| needs a referral | Por referir |
| referred | Referido |
| undo, not applied yet | Por aplicar |

If the words fit none of these, ask.

## Which jobs

- **One or more URLs**: those jobs.
- **A group** ("all the apply ones", "this round", "the BairesDev ones", "the 34 letters"): resolve it to URLs from `jobs/triage.md`, `jobs/queue.csv` or the `jobs/` folders, list the jobs (company, role, link) and wait for Mario's yes before marking anything.
- **A company or role named without a link**: find the URL in `jobs/queue.csv`. If more than one job matches, ask which.

## Steps

1. Copy `mark_status.js` to `.playwright-mcp/mark_status_run.js` (Playwright can only read files inside the workspace), setting `TARGETS` to the URLs and `STATUS` to the Estado label.
2. Navigate to `https://claude.ai/artifact/8onQyXHwM6TVVm9x8bVuxz`, then run `browser_run_code_unsafe` with `filename: ".playwright-mcp/mark_status_run.js"`. It returns one result per target: `tab`, `row`, `before`, `after`, or `found: false`. Scanning all the tabs takes a few minutes.
3. If a sign-in wall shows, ask Mario to sign in to that browser window, then save the state with `page.context().storageState({path:'/Users/mariogranada/.playwright-auth/linkedin.json'})`.
4. **Check**: reload the page and run the copy again with `STATUS = null`. That's a read-only pass, and every target must read the new Estado.
5. **Keep the repo in step** until the next export:
   - `python3 scripts/triage.py status "<Estado>" <url> [<url> ...]` sets `status` in `jobs/queue.csv` and rebuilds `jobs/triage.md`.
   - Update the job's row in the Applications log in `MEMORY.md`. For Aplicado, use "Applied: letter (marked Aplicado in the Sheet)", or say what else was sent. Add a dated row if the job has none.
6. **Commit the job folders** once the Sheet check passes, for every changed job that has a `jobs/<Company>-<Role>/` folder (from the `folder` column of `jobs/queue.csv`):
   - `git add <folder>` for each one, then a single `git commit -m "<Estado>: <Company> - <Role>"` (for a batch: `"<Estado>: <n> jobs"`, with one `- <Company> - <Role>` line per job in the body), ending with the attribution lines from the system reminder.
   - Stage only those folders, never `git add .` or other files. Don't push.
   - If a folder has nothing new to commit, skip it and say so. A job without a folder gets no commit.
7. Delete `.playwright-mcp/` and reply with a short table: company, role, tab and row, before → after. List any link that wasn't found. Never guess its row.
