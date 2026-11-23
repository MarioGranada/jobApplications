# Workspace setup (2026-11-21)

- `AGENTS.md` holds the rules; `CLAUDE.md` is just `@AGENTS.md`, so Claude Code and other agents share one file.
- `Mario_Granada_Senior_Software_Engineer_CV.md` was created from the final docx and is the CV source of truth. `cv_development/CV_MarioGranada_Nov2026_v2.md` is superseded.

# Cover letter skill (added 2026-11-22)

- `.claude/skills/cover_letter_writer/SKILL.md`: job URL → `jobs/<Company>-<Role>/cover_letter.md` + `job_posting.md`. Trigger: "create the cover letter for job <url>".
- Folder names drop hyphens inside the company or role, so only the separator hyphen remains (e.g. `Restream-Software_Engineer_Frontend_Studio_Team`).
- LinkedIn reading that works: navigate, wait about 2.5 s, click the description's "… more" button, then read `main.innerText` and cut it at "Set alert for similar jobs". "Meet the hiring team" shows the named person when there is one.

# Banned technologies (added 2026-11-22)

- WebdriverIO is never mentioned; Playwright replaces it. The CV `.md` (Yolo bullet) and the LinkedIn `.md` still contain it because they mirror the docx and live profile. Update both only after Mario changes the doc and LinkedIn.

# Greeting and relocation (updated 2026-11-23)

- Letters greet the named hiring manager, then the job poster or recruiter, and use "Hiring Team" only when no one is named (first applied to eDreams ODIGEO: "Dear Elisabet Abad,").
- Mario is willing to relocate. On-site or hybrid roles outside Tallinn get "I'm based in Tallinn, willing to relocate to <city> and available to start immediately."

# Colombian Spanish (added 2026-11-23)

- All Spanish output uses Colombian Spanish: "usted", "ustedes", "hoja de vida", "Cordial saludo"; no Spain-only forms. Rule lives in `AGENTS.md`.

# Application answers (2026-11-22 to 2026-11-23)

- Glia: the AI-workflow answer is based on the portfolio repo's agent setup (constitution, AGENTS.md, MEMORY.md, SDD specs, coordinator/planner/implementer/reviewer agents, worktrees).
- Block Labs: the four answers in `application_answers.md` are Mario's own final wording. Keep them verbatim. Q3 uses the Coursy `NEXT_LOCALE` cookie-scope fix (commit "COUR-10495 language cookie fix"); Mario asked not to cite the portfolio there.

## Mistakes to avoid (learned here)

- **Don't paraphrase a posting's numbers.** The Wolt letter first said the chat app "handles" 20M+ conversations; the posting says it's "built to serve" them.
- **Check authorship before citing repo work.** In Coursy, the skins and translation skill notes and the asset-version hotfix were written by Kaupo, not Mario.
- **An Estonian permit doesn't cover Spain.** Spain-only roles (CONVOTIS, Inetum) need remote B2B from Estonia or sponsorship.
- **Gaps go in chat, not in the text.** Microfrontends, Vite, Redux Toolkit, RAG and MCP aren't on the CV. Next.js App Router isn't either; it's used in the CONVOTIS message at Mario's request, pending a CV update.
- On LinkedIn, clicking every "… more" link can open a feed post. Target only the job description's button.

# Applications log

| Date | Company | Role | Location | Folder | Status |
|---|---|---|---|---|---|
| 2026-11-22 | Wolt | FullStack Engineer | Remote | `jobs/Wolt-FullStack_Engineer/` | Applied: letter + top-choice message |
| 2026-11-22 | Restream | Software Engineer - Frontend - Studio Team | Remote | `jobs/Restream-Software_Engineer_Frontend_Studio_Team/` | Applied: letter |
| 2026-11-22 | Wise | Senior Fullstack Engineer, Customer Risk Assessment | Tallinn | `jobs/Wise-Senior_Fullstack_Engineer_Customer_Risk_Assessment/` | Applied: letter |
| 2026-11-22 | Stripe | Frontend Engineer, UI Platform | Barcelona | `jobs/Stripe-Frontend_Engineer_UI_Platform/` | Applied: letter |
| 2026-11-22 | Glia | Senior Software Engineer, Media | Tartu (hybrid) | `jobs/Glia-Senior_Software_Engineer_Media/` | Applied: answers |
| 2026-11-23 | Block Labs | Staff Software Engineer, Frontend | | `jobs/Block_Labs-Staff_Software_Engineer_Frontend/` | Applied: final answers (Mario's wording) |
| 2026-11-23 | eDreams ODIGEO | Frontend Lead Engineer + AI | Barcelona or Madrid (hybrid) | `jobs/eDreams_ODIGEO-Frontend_Lead_Engineer_plus_AI/` | Applied: letter |
| 2026-11-23 | CONVOTIS Iberia | Senior Frontend Developer (React / Next.js) | Spain (remote, Spain residents) | `jobs/CONVOTIS_Iberia-Senior_Frontend_Developer_React_Next.js_Migracion_de_ecommerce/` | Applied: LinkedIn message to Cristina Izquierdo |
| 2026-11-23 | Inetum | AI FrontEnd Engineer | Madrid (on-site) | `jobs/Inetum-AI_FrontEnd_Engineer/` | Applied: letter + top-choice message |
