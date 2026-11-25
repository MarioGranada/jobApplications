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

- 2026-11-24: Mario decided on one global answers bank, `application_answers_bank.md` at the root, filled only from answers already in the repo (Glia, Block Labs) plus the Ketryx stack answer (draft). Skill: `.claude/skills/application_answers/`.

- Glia: the AI-workflow answer is based on the portfolio repo's agent setup (constitution, AGENTS.md, MEMORY.md, SDD specs, coordinator/planner/implementer/reviewer agents, worktrees).
- Block Labs: the four answers in `application_answers.md` are Mario's own final wording. Keep them verbatim. Q3 uses the Coursy `NEXT_LOCALE` cookie-scope fix (commit "COUR-10495 language cookie fix"); Mario asked not to cite the portfolio there.
- Block Labs (2026-11-23): Mario asked €6,250–7,050/month gross. Ask for an employee contract with a non-Spanish entity on Spanish Social Security, not B2B (B2B at that figure nets less than Coursy). A Spanish entity or Spanish EOR is ruled out because it would require changing the visa (PAC). In the recruiter call, open as Tallinn-based and raise Spain only at the end. Details: `jobs/Block_Labs-Staff_Software_Engineer_Frontend/relocation_and_contract.md`.

## Mistakes to avoid (learned here)

- **Don't paraphrase a posting's numbers.** The Wolt letter first said the chat app "handles" 20M+ conversations; the posting says it's "built to serve" them.
- **Check authorship before citing repo work.** In Coursy, the skins and translation skill notes and the asset-version hotfix were written by Kaupo, not Mario.
- **An Estonian permit doesn't cover Spain.** Spain-only roles (CONVOTIS, Inetum) need remote B2B from Estonia or sponsorship.
- **Gaps go in chat, not in the text.** Microfrontends, Vite, Redux Toolkit, RAG and MCP aren't on the CV. Next.js App Router isn't either; it's used in the CONVOTIS message at Mario's request, pending a CV update.
- On LinkedIn, clicking every "… more" link can open a feed post. Target only the job description's button.

# Minimum pay (set 2026-11-23)

- Absolute minimum: €4,400 net/month. Gross and company-cost floors per setup are in `minimum_salary.md`. Block Labs' €6,250/month (€75,000/year) asked is the floor with Beckham.

# Job queue and triage (added 2026-11-24)

- Own tool instead of ai-job-search, which would replace the fixed Google Docs CV and the Playwright reading of LinkedIn. Borrowed ideas: the fit rubric with vetoes (`/rank`) and follow-ups after 10+ days (`/outcome followup`).
- `vacantes.xlsx` lives at the repo root and is re-exported whenever the Sheet changes (Mario's rule). The Sheet is shared from another organization, so the Docs connector can't read it. Export it through the Playwright browser instead.
- Playwright MCP now runs `--isolated` with `~/.playwright-auth/linkedin.json`. That file now also holds the claude.ai sign-in (saved 2026-11-24, backup at `linkedin.json.bak`).
- First export: 479 rows → 456 unique jobs, 415 to do. To do by gate: ok 49, check 37, spain_permit 43, eu_permit 127, visa_sponsored 6, visa 125, blocked 28.
- Submitting stays manual (LinkedIn's terms). Pace postings at about 50 a day.
- The Sheet is the source of truth for jobs and status (rule in `constitution.md`), updated twice a day, morning and afternoon.
- Headless: claude.ai shows a bot check ("Just a moment...") to headless browsers. A standalone script in a visible browser loaded the Sheet, but its menu said "You can't export this artifact", while the MCP browser got the Excel/CSV dialog. So the Sheet export runs through the visible `playwright-sheet` MCP server and everything else is headless.
- First triage batch (49 postings): 13 apply, 21 maybe, 11 skip, 4 closed.
- Afternoon export (2026-11-24): 519 rows → 495 unique jobs, 39 new (none removed), 36 Aplicado in the Sheet. The five jobs marked by `sheet_status` today all read Aplicado in the export.
- 2026-11-24: Mario asked us to set the Estado dropdown when he says he applied (or reports another change), so that column is now the one exception to the Sheet being read-only. The Docs connector refuses the Sheet ("access", shared from another org), so `sheet_status` edits it through the page in Playwright: keyboard navigation over the virtualized DOM grid (Control+Home, arrows, Enter opens the dropdown). Jobs are matched by link, because rows move between updates (Ketryx went from Remoto global row 43 in the morning export to row 2 that afternoon). Estado options: Por aplicar, Aplicado, Entrevista, Oferta, Descartado, Por referir, Referido.
- Morning export (2026-11-25): 557 rows → 532 unique jobs, 32 new (none removed), 40 Aplicado. New Mercor tab (talent pools that train AI, USD/h, referral links, no Empresa column): `build_queue.py` now uses the tab name as the company and reads "Link de referido", "Pago (USD/h)", "Ubicación / dedicación" and "Ojo / requisitos". Its 5 rows come in as `referral` (Estado Por referir). HappyRobot and Nortal (2026-11-25) are still not in the Sheet. Triage: 10 postings fetched and 9 scored. New apply: Langfuse (ClickHouse), Kraken Consumer Frontend (Estonia posting li-4437058590; the letter in `jobs/Kraken-…` was written for li-4437052825) and Carla. Maybe: Hack The Box Elixir. edenity's posting loaded without a description, so it's still pending.

# Applications log

| Date | Company | Role | Location | Folder | Status |
|---|---|---|---|---|---|
| 2026-11-22 | Wolt | FullStack Engineer | Remote | `jobs/Wolt-FullStack_Engineer/` | Applied: letter + top-choice message |
| 2026-11-22 | Restream | Software Engineer - Frontend - Studio Team | Remote | `jobs/Restream-Software_Engineer_Frontend_Studio_Team/` | Applied: letter |
| 2026-11-22 | Wise | Senior Fullstack Engineer, Customer Risk Assessment | Tallinn | `jobs/Wise-Senior_Fullstack_Engineer_Customer_Risk_Assessment/` | Applied: letter |
| 2026-11-22 | Stripe | Frontend Engineer, UI Platform | Barcelona | `jobs/Stripe-Frontend_Engineer_UI_Platform/` | Applied: letter |
| 2026-11-22 | Glia | Senior Software Engineer, Media | Tartu (hybrid) | `jobs/Glia-Senior_Software_Engineer_Media/` | Applied: answers |
| 2026-11-23 | Block Labs | Staff Software Engineer, Frontend | | `jobs/Block_Labs-Staff_Software_Engineer_Frontend/` | Applied: final answers (Mario's wording). Recruiter intro call Thu 26 Nov 2026, 11:00 |
| 2026-11-23 | eDreams ODIGEO | Frontend Lead Engineer + AI | Barcelona or Madrid (hybrid) | `jobs/eDreams_ODIGEO-Frontend_Lead_Engineer_plus_AI/` | Applied: letter |
| 2026-11-23 | CONVOTIS Iberia | Senior Frontend Developer (React / Next.js) | Spain (remote, Spain residents) | `jobs/CONVOTIS_Iberia-Senior_Frontend_Developer_React_Next.js_Migracion_de_ecommerce/` | Applied: LinkedIn message to Cristina Izquierdo |
| 2026-11-23 | Inetum | AI FrontEnd Engineer | Madrid (on-site) | `jobs/Inetum-AI_FrontEnd_Engineer/` | Applied: letter + top-choice message |
| 2026-11-23 | Yapily | Senior Front End Developer | Málaga (hybrid) | `jobs/Yapily-Senior_Front_End_Developer/` | Letter + headline |
| 2026-11-23 | Mecalux | FrontEnd Developer | Cornellà de Llobregat, Barcelona (hybrid) | `jobs/Mecalux-FrontEnd_Developer/` | Letter |
| 2026-11-23 | IKEA | Senior Software Engineer - IKEA for Business, Group Digital | San Sebastián de los Reyes, Madrid (on-site) | `jobs/IKEA-Senior_Software_Engineer_IKEA_for_Business_Group_Digital/` | Letter |
| 2026-11-24 | 011h | Product Engineer | Barcelona (hybrid) | `jobs/011h-Product_Engineer/` | Applied: letter (marked Aplicado in the Sheet) |
| 2026-11-24 | Ashby | Design Engineer - EU | Estonia / España / UE | `jobs/Ashby-Design_Engineer_EU/` | Applied: letter (marked Aplicado in the Sheet) |
| 2026-11-24 | Ashby | Senior Software Engineer, Product Engineering - EU | 🇪🇺 Remoto en Europa (publicado para España) | `jobs/Ashby-Senior_Software_Engineer_Product_Engineering_EU/` | Applied: letter + form answers (marked Aplicado in the Sheet) |
| 2026-11-24 | Ashby | Staff Design Engineer - EU | 🇪🇺 Remoto en Europa | `jobs/Ashby-Staff_Design_Engineer_EU/` | Letter (maybe, fit 3) |
| 2026-11-24 | Ashby | Staff Software Engineer, Product Engineering - EU | 🇪🇺 Remoto en Europa (publicado para Italia) | `jobs/Ashby-Staff_Software_Engineer_Product_Engineering_EU/` | Letter (maybe, fit 3) |
| 2026-11-24 | BairesDev | Backend Engineer (Elixir) | 🌎 Cualquier lugar | `jobs/BairesDev-Backend_Engineer_Elixir/` | Letter (maybe, fit 3) |
| 2026-11-24 | BairesDev | Design Systems Engineer | 🌎 Cualquier lugar ("100% remote, from anywhere") | `jobs/BairesDev-Design_Systems_Engineer/` | Letter (apply, fit 4) |
| 2026-11-24 | BairesDev | Senior Frontend Developer | 🌎 Cualquier lugar | `jobs/BairesDev-Senior_Frontend_Developer/` | Letter (maybe, fit 4) |
| 2026-11-24 | BairesDev | Senior React Engineer | 🌎 Cualquier lugar | `jobs/BairesDev-Senior_React_Engineer/` | Letter (maybe, fit 4) |
| 2026-11-24 | BairesDev | Senior React & TypeScript Engineer | 🌎 Cualquier lugar | `jobs/BairesDev-Senior_React_and_TypeScript_Engineer/` | Letter (maybe, fit 4) |
| 2026-11-24 | BairesDev | Senior React + TypeScript Developer | 🌎 Cualquier lugar | `jobs/BairesDev-Senior_React_plus_TypeScript_Developer/` | Letter (maybe, fit 3) |
| 2026-11-24 | BairesDev | UI Engineer (Analytics) | 🌎 Cualquier lugar | `jobs/BairesDev-UI_Engineer_Analytics/` | Letter (maybe, fit 3) |
| 2026-11-24 | Betsson Group | Senior Frontend Engineer - Brand Experience | Grecia · Atenas | `jobs/Betsson-Senior_Frontend_Engineer_Brand_Experience/` | Letter (maybe, fit 3) |
| 2026-11-24 | Canonical | Senior Web Engineer | 🌍 Remoto EMEA | `jobs/Canonical-Senior_Web_Engineer/` | Letter (maybe, fit 3) |
| 2026-11-24 | Checkly | Senior Product Engineer (Incident Response, remote) | Zonas horarias UTC-3 a UTC+3 | `jobs/Checkly-Senior_Product_Engineer_Incident_Response_remote/` | Applied: letter + 3 form answers (marked Aplicado in the Sheet) |
| 2026-11-24 | ClickHouse | Senior Full Stack Engineer - ClickStack | 🌎 Remote-friendly, 25+ países (publicado en Ámsterdam) | `jobs/ClickHouse-Senior_Full_Stack_Engineer_ClickStack/` | Applied: letter + form answer (marked Aplicado in the Sheet) |
| 2026-11-24 | ClickHouse | Senior Software Engineer (Typescript / Front-end) - AI/ML | 🌎 Remote-friendly, 25+ países | `jobs/ClickHouse-Senior_Software_Engineer_Typescript_Front_end_AI_ML/` | Letter (maybe, fit 3) |
| 2026-11-24 | ClickUp | Senior Frontend Engineer | Hungría (remoto UE) | `jobs/ClickUp-Senior_Frontend_Engineer/` | Letter (maybe, fit 3) |
| 2026-11-24 | Customer.io | Senior Software Engineer, Product/AI | Remoto · EMEA | `jobs/Customer.io-Senior_Software_Engineer_Product_AI/` | Letter (maybe, fit 3) |
| 2026-11-24 | Deel | Senior Design Engineer | Reino Unido | `jobs/Deel-Senior_Design_Engineer/` | Letter (maybe, fit 3) |
| 2026-11-24 | Deel | Senior Full Stack Engineer - EMEA | Estonia / EMEA | `jobs/Deel-Senior_Full_Stack_Engineer_EMEA/` | Applied: letter (marked Aplicado in the Sheet) |
| 2026-11-24 | Elastic | Senior Full Stack Software Developer - Observability | 🇪🇸 Remoto España | `jobs/Elastic-Senior_Full_Stack_Software_Developer_Observability/` | Letter (apply, fit 4) |
| 2026-11-24 | Kake | Senior Full Stack Engineer (Node/React) | 🌎 Publicado en 10+ países (LATAM, Europa, Asia, África) | `jobs/Kake-Senior_Full_Stack_Engineer_Node_React/` | Letter (maybe, fit 4) |
| 2026-11-24 | Ketryx | Full Stack Software Engineer | Remoto en la UE (o híbrido en Viena) | `jobs/Ketryx-Full_Stack_Software_Engineer/` | Applied: letter (marked Aplicado in the Sheet) |
| 2026-11-24 | Kraken | Senior Software Engineer - Frontend - Consumer | Eslovenia (remoto UE) | `jobs/Kraken-Senior_Software_Engineer_Frontend_Consumer/` | Letter (maybe, fit 3) |
| 2026-11-24 | Motion (Creative Analytics) | Senior / Staff Software Engineer | 🌍 Equipo 100% remoto (publicado en Reino Unido) | `jobs/Motion-Senior_Staff_Software_Engineer/` | Letter (apply, fit 4) |
| 2026-11-24 | Nebius | Senior Fullstack Engineer | Remoto · Europa e Israel | `jobs/Nebius-Senior_Fullstack_Engineer/` | Letter (maybe, fit 3) |
| 2026-11-24 | Productboard | Staff Full-stack Product Engineer, Growth | Chequia · Praga | `jobs/Productboard-Staff_Full_stack_Product_Engineer_Growth/` | Applied: letter (marked Aplicado in the Sheet) |
| 2026-11-24 | Proxify | Senior Frontend Developer (React.js + Next.js) | 🌎 Remoto (red global de contractors; publicado para Brasil) | `jobs/Proxify-Senior_Frontend_Developer_React.js_plus_Next.js/` | Letter (maybe, fit 3) |
| 2026-11-24 | Social Discovery Group | Senior Frontend Developer | 🌎 Cualquier país (equipo de nómadas digitales) | `jobs/Social_Discovery_Group-Senior_Frontend_Developer/` | Letter (maybe, fit 4) |
| 2026-11-24 | Spotify | Senior Web Engineer – Subscriptions | Remoto · EMEA | `jobs/Spotify-Senior_Web_Engineer_Subscriptions/` | Applied: letter + form answers (marked Aplicado in the Sheet) |
| 2026-11-24 | Toggl | Senior Full Stack Engineer | 🌎 Cualquier zona horaria (≥4 h de solape con Europa central) | `jobs/Toggl-Senior_Full_Stack_Engineer/` | Applied: letter + 4 form answers (marked Aplicado in the Sheet) |
| 2026-11-24 | Toptal | Senior Fullstack Engineer | Estonia / Grecia / remoto | `jobs/Toptal-Senior_Fullstack_Engineer/` | Discarded: no longer accepting applications (marked Descartado in the Sheet) |
| 2026-11-24 | Triple | Product Engineer | 🌍 100% remoto (publicado en Reino Unido) | `jobs/Triple-Product_Engineer/` | Letter (maybe, fit 3) |
| 2026-11-24 | Upvest | Senior Fullstack Engineer | Hubs en Berlín, Londres o Tallin (híbrido) o remoto en Europa, según el rol | `jobs/Upvest-Senior_Fullstack_Engineer/` | Letter (maybe, fit 3) |
| 2026-11-25 | HappyRobot | Forward Deployed Engineer | Madrid (híbrido) | none (not in the Sheet) | Applied: 1 form answer (not in the Sheet, no Estado to mark) · https://www.linkedin.com/jobs/view/4318435019/ |
| 2026-11-25 | Nortal | AI-Driven Software Engineer | Tallinn (híbrido) | `jobs/Nortal-AI-Driven_Software_Engineer/` | Applied: letter (not in the Sheet, no Estado to mark; Java and Estonian required, senior cap €6,000 gross/month) · https://www.linkedin.com/jobs/view/4423101698/ |
