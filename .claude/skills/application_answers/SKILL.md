---
name: application_answers
description: Answers a job application form question for Mario, reusing the root answers bank, and records the answer there. Use when the user pastes a question from an application form ("question for <Company>:", "they ask...", "answer this", "Q/A", "form question").
---

# Application answers

Writes answers to application form questions and keeps every answer in one bank, so each new form takes less typing.

## Inputs

- The question as asked, and the company. If the company isn't clear, take it from the open file or the latest `jobs/<Company>-<Role>/` folder in the conversation.
- `application_answers_bank.md` (root): every answer written so far, grouped by topic.
- `Mario_Granada_Senior_Software_Engineer_CV.md`, `constitution.md`, `AGENTS.md`, and the job's `job_posting.md`.

## Steps

1. **Look in the bank first.** If the same or a similar question exists, reuse it. Answers marked verbatim are Mario's own wording: keep them as they are, and only trim them to a character limit if he asks. Otherwise adapt the answer to the posting's terms.
2. **Write the answer** if nothing fits:
   - Facts only from the CV, or from repos Mario authored (check the git author first). No invented metrics.
   - Lead with what overlaps with the posting, in the posting's own words.
   - Plain first person, short sentences, no hype words, no em dashes. Never mention a banned technology (see `AGENTS.md`).
   - Colombian Spanish if the form is in Spanish.
   - Respect any character or word limit the form states.
3. **Reply in chat** with the answer ready to paste, its word count (or character count, with `wc -m`, when there's a limit), and gaps, such as a technology the posting uses that the CV doesn't show. Gaps stay in chat, never in the answer.
4. **Record it in the bank** under the right topic, or add a topic: `### <question as asked>`, then `- Asked by: <Company>, <Role> (<date>) · <folder>`, `- Status: Draft, waiting for Mario's approval`, an optional `- Note:`, then the answer. When the same question comes back from another company, add that company to "Asked by" instead of duplicating the entry.
5. When Mario approves, rewrites or submits an answer, update its status. If he rewrites it, save his wording verbatim and mark it **Mario's own final wording: keep verbatim**.
