---
name: cover_letter_writer
description: Writes a tailored, ready-to-send cover letter for a job posting URL, using Mario's CV and cover letter template. Use when the user asks for something like "create the cover letter for job https://...", "write a cover letter for this job: <url>" or "cover letter for <url>".
---

# Cover letter writer

Turns a job posting URL into a cover letter Mario can paste straight into his Google Docs template and download as a PDF, with no further editing.

## Inputs

- **Job posting URL**: taken from the user's prompt. If the prompt has no URL, ask for one and stop.
- **`AGENTS.md`** (repo root): rules, settled decisions and naming conventions. Follow them.
- **`Mario_Granada_Senior_Software_Engineer_CV.md`** (repo root): the only source of facts about Mario's experience.
- **`cover_letter_template.md`** (repo root): the letter's structure and tone.

Read all three files before writing anything.

## Step 1: Read the job posting (Playwright only)

Use only the Playwright MCP tools (`mcp__playwright__*`) to read the posting. Don't use WebFetch, curl, the web-fetch agent or any other browser tool. If the Playwright tools are deferred, load them with ToolSearch first.

1. `browser_navigate` to the URL.
2. Dismiss any cookie or consent banner that hides the content (`browser_click` on "Accept" or "Reject"). Expand "Show more" or "See full description" if the description is truncated.
3. Get the text with `browser_snapshot`, or with `browser_evaluate` returning `document.body.innerText` if the snapshot is too noisy. If the posting sits in an iframe (Greenhouse, Lever, Workday and similar embeds), read the iframe's content.
4. If the page shows a sign-in wall (LinkedIn, for example) or an error, tell the user and ask them to sign in to the Playwright browser or send a direct link to the company's careers page. Never guess at the posting's content.

Extract:
- **Company name**, as the company writes it (e.g. "Wrike", not "Wrike Inc.").
- **Role title**, exactly as posted.
- **Hiring manager or recruiter name**, if the posting gives one.
- **Location and work model** (remote, hybrid, on-site, which city or country).
- **What the company or product does**, plus anything specific: the mission, a product, a technical challenge, the team's setup.
- **Key requirements**: must-haves and nice-to-haves, in the posting's own words.

## Step 2: Fill in the template

Keep every paragraph of `cover_letter_template.md` word for word, except for these changes:

- `[Company]`: the company name. `[Role]`: the role title as posted.
- **Greeting**: if the posting names a person, use `Dear <First name> <Last name>,`. A hiring manager comes first; otherwise use the job poster or recruiter (LinkedIn's "Meet the hiring team" section). Use `Dear [Company] Hiring Team,` only when no one is named.
- **Availability**: Mario is available immediately. Replace `and available from [date]` with `and available to start immediately`.
- **The "What draws me" paragraph** (the only paragraph you write). It has two sentences:
  1. `What draws me to <Company> is <one specific reason>.` The reason must come from the posting: a concrete product, mission, challenge or way of working that the posting actually mentions. Nothing generic like "your innovative culture" or "your growth".
  2. One sentence linking a key requirement of the role to a **real** fact from the CV: a project, client, stack or responsibility. Choose the requirement where Mario's match is strongest and most specific. Design systems, React/Next.js/TypeScript, Elixir/Phoenix LiveView, leading frontend across products, CI/CD releases and AI-assisted development are the usual strong points.
- **Location line**: Mario is willing to relocate. If the role is on-site or hybrid outside Tallinn, write `I'm based in Tallinn, willing to relocate to <city> and available to start immediately.` (e.g. "to Barcelona or Madrid" when the posting offers both). For remote roles or roles in Tallinn, keep `I'm based in Tallinn and available to start immediately.`

Don't touch the other paragraphs, the sign-off or the contact block. The template has already been approved.

## Step 3: Humanize

The new paragraph must sound like the rest of the letter and the CV: plain, first person, concrete, short sentences, no hype. Before saving, check it against these rules:

- Use only facts from the CV. No invented metrics, years, team sizes or technologies (see `AGENTS.md`).
- Don't claim experience with anything the CV doesn't show, even if the posting asks for it.
- Never mention any technology on the "Banned technologies" list in `AGENTS.md`. Use its replacement instead (e.g. Playwright, never WebdriverIO).
- Avoid these words and phrases: passionate, excited, thrilled, eager, leverage, synergy, cutting-edge, innovative, dynamic, fast-paced, "I believe", "I am confident", "align with", "resonates with", "perfect fit", "unique opportunity".
- No em dashes, no rhetorical questions, no exclamation marks, no lists of three adjectives.
- Use the posting's own terms for the requirement, so the letter also works for ATS keyword matching.
- The whole paragraph is two sentences, about 40 to 70 words.
- Read the full letter once from top to bottom. It should flow as one voice.

## Step 4: Save

Folder: `jobs/<Company>-<Role>/`. A hyphen separates the company from the role. Inside each part, spaces become `_`. Remove characters that are unsafe in file names (`/ \ : * ? " < > | , ( ) '`), replace `&` with `and`, drop any hyphens inside the company or role (so only the separator hyphen remains), and strip accents to plain ASCII. For example, "Software Engineer - Frontend - Studio Team" at Restream becomes `jobs/Restream-Software_Engineer_Frontend_Studio_Team/`. For example, Wrike's "Senior AI Product Builder" goes in `jobs/Wrike-Senior_AI_Product_Builder/`.

Write two files in that folder:

1. **`cover_letter.md`**: only the letter text, from the greeting to the contact block. No headings, front matter or notes, so the whole file can be copied and pasted into the Google Docs template as it is.
2. **`job_posting.md`**: the URL, the date it was read, and the extracted posting (company, role, location, description, requirements). Keep it for interview prep and in case the posting is taken down.

If the folder already exists, show the user what's there and ask before you overwrite anything.

After saving, delete any `.playwright-mcp/` folder or scraped temporary files from the workspace.

## Step 5: Reply in chat

Keep the reply short:

- Where the files are, as links.
- The new "What draws me" paragraph, so the user can review it without opening the file.
- **Google Doc name for the PDF download**: `Mario Granada - Cover Letter - <Company>`. Rename the copy of the template to this before File → Download → PDF, so the PDF's Title metadata is correct (same convention as the CV in `AGENTS.md`).
- **Flags**, only if any apply: requirements the CV doesn't cover (e.g. a language, a technology, years of experience), location or relocation conflicts, or anything unclear in the posting. Keep these in chat. Never put them in the letter.
