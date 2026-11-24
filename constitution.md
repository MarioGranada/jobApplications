# Workspace Constitution

## Guiding Principles

- **Truth over polish**: every claim about Mario traces back to the root CV `.md`. If the CV doesn't show it, it's a flag for Mario, not a sentence in a letter.
- **Sound like Mario**: plain, first person, concrete, short sentences. A recruiter should read a person, not a template.
- **Simplicity first**: minimal, concrete suggestions. No clutter, no extra files nobody asked for, no re-proposing ideas Mario already declined.
- **Traceability**: it should be clear where every fact comes from. Each application keeps the posting as it was read, and the CV and LinkedIn each have one source of truth.
- **Mario has the final word**: he edits the docx and PDFs himself, and when he rewrites something in his own words, his version is kept verbatim.

---

## Sources of Truth

| What | Source | Notes |
|---|---|---|
| Jobs to apply to and their status | The "Vacantes para Mario" Sheet (claude.ai/artifact/8onQyXHwM6TVVm9x8bVuxz) | **The source of truth for the job list.** Mario updates it twice a day (morning and afternoon). Re-export it to `vacantes.xlsx` and rebuild `jobs/queue.csv` before any queue or triage work. When the Sheet and the repo disagree on a job's status, the Sheet wins. Read-only for us. |
| Mario's experience | `Mario_Granada_Senior_Software_Engineer_CV.md` | Mirrors the final docx. The only source of facts for letters and answers. |
| LinkedIn profile | `cv_development/LinkedIn_Profile_Nov2026.md` | Mirrors the live profile. Kept in sync with the CV. |
| Letter structure | `cover_letter_template.md` | Approved. Only the "What draws me" paragraph is written per job. |
| A job's requirements | `jobs/<Company>-<Role>/job_posting.md` | The posting as read, in its own words. |
| Rules and decisions | `AGENTS.md`, `MEMORY.md` | Rules and settled decisions; dated history and lessons. |

---

## Core Premises

### 1. Reading postings
- Read job postings with Playwright only. If the page is behind a sign-in wall or fails, ask. Never guess at a posting's content.
- Quote the posting's facts in its own words. A number or claim taken from a posting must keep its exact meaning.

### 2. Writing
- English by default. Whenever writing in Spanish, use Colombian Spanish (see `AGENTS.md`).
- Use the posting's own terms for requirements, so the text also passes ATS keyword matching.
- No hype words, no em dashes, no rhetorical questions, no exclamation marks.
- Never mention a banned technology (see `AGENTS.md`).

### 3. Evidence beyond the CV
- When Mario points to a repo (Coursy, the portfolio) as evidence for an answer, use only work he authored. Check the git author before citing a commit, note or skill.
- Say which parts are inferred rather than found, so Mario can confirm them.

### 4. Location and work rights
- Mario lives in Tallinn, is available immediately and is willing to relocate.
- Never imply that his Estonian residence or work permit lets him work in another country. Offer real options instead (remote B2B from Estonia, or relocation with sponsorship).

### 5. Files and naming
- Use `_` instead of spaces in every file and folder name, except the two final CV files.
- Never modify a `.docx` or `.pdf`. Edit the `.md`, then tell Mario what to change in Google Docs.
- Leave no scraped or temporary files behind (`.playwright-mcp/`).

### 6. Privacy
- Mario's email, phone and personal details appear only in his own documents. Never send them to external services.

---

## What to Avoid

- ❌ Inventing metrics, years, team sizes or technologies.
- ❌ Generic reasons to join ("your innovative culture"). The reason must come from the posting.
- ❌ Rewriting Mario's own wording without being asked.
- ❌ Putting flags or caveats inside a letter. They belong in the chat.
- ❌ Long option lists when one recommendation will do.

---

## Checklist Before Handing Anything Over

- [ ] Does every claim about Mario appear in the root CV `.md`?
- [ ] Do facts about the company match the posting's exact wording?
- [ ] Does it read like a person wrote it, with no banned words or em dashes?
- [ ] Is the greeting addressed to the named person, and is the location line right for the work model?
- [ ] Are file and folder names free of spaces?
- [ ] Are gaps (missing skills, work rights, language) flagged in chat?

---

## Philosophy Statement

This workspace exists to get Mario hired by telling the truth about his work well. Every letter, answer and message should be something he could defend line by line in an interview. Precise and honest beats impressive.
