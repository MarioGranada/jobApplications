# Application answers bank

Answers to questions that application forms ask, reused across jobs. **This file is the single place for form answers:** new answers go here, not in per-job files. The `application_answers.md` files in Glia and Block Labs are kept as the record of what was submitted there.

## How to use it

- Before writing a new answer, look here for the same or a similar question, and reuse or adapt it to the posting's terms.
- Every fact must come from the root CV `.md` (or from repos Mario authored, checked by git author). Don't invent metrics.
- Answers marked **verbatim** are Mario's own wording. Reuse them as they are, and only trim to fit a character limit when asked.
- Add every new answer under the right topic: the question as asked, who asked, the date, its status (draft, approved or submitted) and the answer. Flag gaps in chat, never inside the answer.
- Skill: `.claude/skills/application_answers/`.

## Tech stack and experience

### Which stack have you used in production?

- Asked by: Ketryx, Full Stack Software Engineer (2026-11-24) · `jobs/Ketryx-Full_Stack_Software_Engineer/`
- Status: Draft, waiting for Mario's approval.
- Note: Left out because they aren't on the CV: PostgreSQL, Prisma, Redis, Vitest, Cucumber. For a stack-matching question, lead with the overlap with the company's stack.

Most recently at Coursy.io: Next.js, React, TypeScript and Tailwind for new features across all products, plus legacy Angular, PHP and Less, shipped to production through Bitbucket CI/CD pipelines and Docker. At Yolo Group: React, TypeScript, Tailwind and Next.js with server-side rendering, GraphQL (Apollo), Node.js with Express and MongoDB on Bitcasino, and React plus Elixir/Phoenix LiveView component libraries for Moon Design System, released to npm and Hex.pm through GitHub Actions. Earlier: AWS (Lambda, S3, API Gateway) for an API gateway, Vue.js, Nuxt.js and Angular, and Sentry for monitoring. For testing I've used Jest, React Testing Library and Playwright, including Playwright Test Agents.

### What's your day-to-day tech stack? (Frontend: JavaScript, TypeScript, React, state management. Backend: strongest language, Golang? Database: SQL yourself or mainly an ORM?)

- Asked by: Toggl, Senior Full Stack Engineer (2026-11-24) · `jobs/Toggl-Senior_Full_Stack_Engineer/`
- Status: Submitted (as drafted, unless Mario says otherwise).
- Note: Years are from the CV dates. The SQL sentence ("through the framework's data layer") is our guess: Mario must confirm whether he wrote SQL himself (MySQL at Razorfish, the Yii API at Coursy).

Frontend: JavaScript in production since 2012, React since 2016 and as my main framework since 2019 (Truelogic, DevSavant, Encora, Yolo Group, Coursy.io), and TypeScript for about four years, at Yolo Group and Coursy.io. For state I've used Redux with Redux-Saga (I built the first version of an app on it at Truelogic), Vuex on Vue.js, and Apollo's cache with GraphQL on Bitcasino, where server data lived in the cache instead of a store. I haven't used Zustand or TanStack Query in production; the closest is Apollo, which handles the same server-cache problem.

Backend: my strongest is Node.js with Express, which I've used in several jobs since 2016, most recently full-stack on Bitcasino with MongoDB. I've also built on AWS (Lambda, S3, API Gateway) for an API gateway at DevSavant, and earlier worked with Ruby on Rails and PHP. No Golang yet, but I'm ready to pick it up.

Database: I've worked with MySQL at Razorfish, with Ruby on Rails and PHP, and with MongoDB on Bitcasino. Most of my relational work went through the framework's data layer, and my recent backend work has been on a document database, so Postgres query plans are something I'd be building up.

### What's your preferred approach to state management in React and why?

- Asked by: ClickHouse, Senior Full Stack Engineer, ClickStack (2026-11-24) · `jobs/ClickHouse-Senior_Full_Stack_Engineer_ClickStack/`
- Status: Submitted (approved by Mario).
- Note: The approach is an opinion, so Mario should confirm it's his. Facts used: Bitcasino (GraphQL with Apollo, Next.js SSR) and Truelogic (React, Redux, Redux-Saga). Left out because they aren't on the CV: React Query, Zustand and other state libraries.

I start with as little state as possible and keep each piece where it belongs. Data that comes from the server isn't app state, so I let the data layer own it. On Bitcasino we used GraphQL with Apollo, whose cache handled fetching and updates, and with Next.js server-side rendering much of the data arrived already rendered, so the client held less. UI state that one component needs stays in useState. I lift it only as far as the components that share it, and use context for a few app-wide values such as the theme or the current user.

I reach for a global store like Redux only when a lot of client state is shared across distant parts of the app and changes in complex ways. At Truelogic I built the first version of an app with React, Redux and Redux-Saga for side effects. It pays off there because every change is explicit and easy to trace, but for most features it adds code without adding clarity. The reason behind all of it is the same: fewer copies of the same data mean fewer bugs where two parts of the UI disagree.

## AI-assisted development and agents

### Describe your current AI-assisted development workflow and which tools you use (e.g., Claude Code, Cursor). What have you learned or changed in your workflow recently?

- Asked by: Glia, Senior Software Engineer, Media (2026-11-22) · `jobs/Glia-Senior_Software_Engineer_Media/`
- Status: Submitted.
- Note: Based on the portfolio repo's agent setup (constitution, AGENTS.md, MEMORY.md, SDD specs, coordinator, planner, implementer and reviewer agents, worktrees).

I use Claude Code and OpenCode every day, set up to share the same rules. On my portfolio (Next.js, TypeScript, Supabase), the repo has a constitution.md with the project's principles and stack, an AGENTS.md with commands and conventions, and a MEMORY.md where decisions and past mistakes are written down so the agent doesn't repeat them.

My workflow is spec-driven. Every feature, enhancement or bug fix gets a numbered folder under specs/ with a spec (requirements in EARS notation), a plan and a task list, and the folder name tracks its state. A coordinator agent runs the flow through three subagents with limited tools: a planner that only writes specs, an implementer that does one task at a time with tests first, and a read-only reviewer that checks each functional requirement. I approve the spec and the plan before any code is written. Each feature runs in its own git worktree, and visual changes are checked with the Chrome DevTools MCP, including the mobile view. At Coursy.io I also configured Playwright Test Agents.

Recently I moved from open-ended prompting to this spec and approval flow, and I keep the agent configs for both tools in sync. I also learned to check external constraints before building: an agent built a full Spotify integration that turned out to be unusable under the API's Premium requirement, so I removed it and recorded the rule in MEMORY.md. Small rules like that, plus requiring finished specs to be marked completed before merging, are what keep the agents reliable over time.

### How do you leverage AI in your day to day work?

- Asked by: Checkly, Senior Product Engineer (Incident Response, remote) (2026-11-24) · `jobs/Checkly-Senior_Product_Engineer_Incident_Response_remote/`
- Status: Submitted (as drafted, unless Mario says otherwise).
- Note: Adapted from Glia's AI workflow answer (above), in Checkly's terms ("coding agents are how you work").

Coding agents are how I work every day. I use Claude Code and OpenCode, set up to share the same rules: a constitution.md with the project's principles and stack, an AGENTS.md with commands and conventions, and a MEMORY.md where decisions and past mistakes are written down so the agent doesn't repeat them.

My workflow is spec-driven. Every feature or bug fix gets a spec, a plan and a task list, and I approve the spec and the plan before any code is written. A coordinator agent runs three subagents with limited tools: a planner that only writes specs, an implementer that does one task at a time with tests first, and a read-only reviewer that checks each functional requirement. Each feature runs in its own git worktree, and visual changes are checked with the Chrome DevTools MCP, mobile view included. At Coursy.io I configured Playwright Test Agents to write and heal our E2E tests, which run in a Bitbucket pipeline against an ephemeral environment.

What I've learned is that agents are fast at producing output that looks finished, so the value is in the checks around them. When an agent gets something wrong, I turn it into a written rule or a test so it doesn't happen again. For example, after an agent built a full Spotify integration that turned out to be unusable under the API's Premium requirement, I removed it and added a rule to check external constraints before building.

### What is in your agent setup right now? Context files, design system rules, and what runs before agent-written code ships.

- Asked by: Block Labs, Staff Software Engineer, Frontend (2026-11-23) · `jobs/Block_Labs-Staff_Software_Engineer_Frontend/`
- Status: Submitted. **Mario's own final wording: keep verbatim.**

Context files: every repo has a short AGENTS.md that the agent reads first, with a trigger table that loads skill files only when the task needs them (deployments, translations, Playwright tests, test fixtures, customer skins). App-level files override the root. They hold the rules agents get wrong without them: no N+1 queries in Yii2, keep the API backward compatible because the admin and learner portals deploy separately, bump the portal's asset version when its JS changes, never use SSH. I use to add a constitution.md (principles and stack) and a MEMORY.md with past decisions and mistakes, and run a coordinator with planner, implementer and reviewer agents that each have limited tools, mirrored for either Claude Code or OpenCode.

Design system rules: colors, spacing and type come from semantic tokens (chart colors as Tailwind tokens in analytics), with no hardcoded values like text-white, and shared components come from the design system (@repo/ui). Every user-facing string goes through next-intl, in every locale file.

Before agent-written code ships: I approve the spec and plan first. The implementer writes tests first and does one task at a time; lint, build and node --test must pass; visual changes are checked with the Chrome DevTools MCP, mobile included; a read-only reviewer checks each functional requirement, with at most two fix rounds. At Coursy particularly, Playwright E2E runs in a Bitbucket pipeline against an ephemeral environment, and every change goes through a pull request.

### The last time an agent produced UI that looked right but was wrong, how did you catch it, and what did you change so it does not happen again?

- Asked by: Block Labs, Staff Software Engineer, Frontend (2026-11-23) · `jobs/Block_Labs-Staff_Software_Engineer_Frontend/`
- Status: Submitted. **Mario's own final wording: keep verbatim.**
- Note: Uses the Coursy NEXT_LOCALE cookie-scope fix (commit "COUR-10495 language cookie fix"). Mario asked not to cite the portfolio here.

At Coursy, the language switch in the analytics portal. The agent's version looked right: picking a language in the sidebar re-rendered the page in that language, and it worked every time on localhost. On prelive it didn't hold. The admin portal writes the NEXT_LOCALE cookie on the shared .coursy.io domain, while the new code wrote a host-only cookie with the same name, so the browser kept both and the page could come back in the old language. Locally there is only one host, so the bug could not show up there.

I caught it by testing the switch on prelive across both apps, moving between the admin portal and analytics instead of staying inside analytics. The fix deletes the cookie in both scopes and writes it with the admin's scope from one shared helper. Then I made it hard to repeat: the app's AGENTS.md now says cookies are written only with the admin's scope, because a different scope survives as a stale duplicate; the language switch is documented step by step for agents; and every Playwright test logs in through one page object that sets the cookies with that scope and checks that html[lang] matches the expected language.

### Which parts of your job should agents take over completely, and which should stay with you? Why?

- Asked by: Block Labs, Staff Software Engineer, Frontend (2026-11-23) · `jobs/Block_Labs-Staff_Software_Engineer_Frontend/`
- Status: Submitted. **Mario's own final wording: keep verbatim.**

Agents can take over completely where a check decides when it's done and where tasks are automated. For instance: writing and healing E2E tests, translation keys across every locale file, refactors that mirror an existing pattern, migrations, and documentation such as runbooks and handoff notes. Hence, a wrong result fails a test, a lint rule or a build.

What stays with me is the criteria on what should be done by an agent and what not, where exactly and how (Backend, Server Side, Client side to name some) As well, it stays with me the work is plausible but wrong, expensive and also when nothing automatic could catch it: deciding what to build and the trade offs, architecture and conventions, design system decisions like consistency versus flexibility, contracts between apps that deploy separately, the final visual and UX judgement across themes and breakpoints, etc. Agents are fast and accurate at producing output that looks finished. However, I'm accounted for how it behaves in production and the final output overall.

## Ownership and projects

### Name one frontend you took from a rough brief to production and owned after launch. What was yours, what was your team's and what was your agents'?

- Asked by: Block Labs, Staff Software Engineer, Frontend (2026-11-23) · `jobs/Block_Labs-Staff_Software_Engineer_Frontend/`
- Status: Submitted. **Mario's own final wording: keep verbatim.**

From my most recent job role (Coursy - a B2B Learning Management System provider that helps to create tailored courses and trainings for customers employees): 
The Coursy analytics portal: a dashboard and trackers (course and training completions, compliance, certificate expiry) that managers open from the admin portal. The brief was a ticket with mock data and a design prototype. I started the repo in March 2026 and wrote about 124 of its roughly 130 commits.

Mine: the architecture and conventions (Next.js App Router and TypeScript in a pnpm monorepo, with a shared @repo/ui package on Tailwind and shadcn), the layouts, sidebar, charts and drawers, the middleware that trusts the admin portal's JWT cookie, the server-side language switch, and the bug-fix rounds after launch. Later I added the Playwright E2E suite and its CI pipeline.

My team's: My Team Lead built the backend side (a slim analytics token, the privileges endpoint and the link from the admin sidebar) and the initial repo setup. The data comes from the admin's Yii API, which another part of the team owns.

My agents': the E2E tests, written through Playwright Test Agents (planner, generator and healer) under rules I wrote in AGENTS.md: log in only through one page object, never inline, and assert only what both prelive and the ephemeral CI environment guarantee, since the CI data has no courses and every widget shows zeros there.

### Describe a role you were in or a project you led that brought out your absolute best work? What setup or attributes of the role/project enabled that?

- Asked by: Ashby, Senior Software Engineer, Product Engineering - EU (2026-11-24) · `jobs/Ashby-Senior_Software_Engineer_Product_Engineering_EU/`
- Status: Draft, waiting for Mario's approval.
- Note: Facts from the Block Labs "rough brief to production" answer and the CV. The "setup" paragraph is our reading of why it worked; Mario should confirm it. Moon Design System is the alternative story if a design-system angle fits better.

My best work so far is the Coursy analytics portal: a dashboard and trackers (course and training completions, compliance, certificate expiry) that managers open from Coursy's admin portal. The brief was a ticket with mock data and a design prototype. I started the repo in March 2026 and wrote about 124 of its roughly 130 commits.

I owned the frontend end to end: the architecture and conventions (Next.js App Router and TypeScript in a pnpm monorepo, with a shared @repo/ui package on Tailwind and shadcn), the layouts, sidebar, charts and drawers, the middleware that trusts the admin portal's JWT cookie, and the server-side language switch. After launch I kept owning it through the bug-fix rounds, and later added a Playwright E2E suite with its own CI pipeline so the next changes would ship safely.

What brought out my best work was the setup. It was a new codebase, so I could set the conventions once and every later screen reused them, starting with the shared UI package. The brief described the problem with mock data and a prototype, and left the technical decisions to me. The split with my Team Lead was clear: he built the backend side (a slim analytics token, the privileges endpoint and the link from the admin sidebar) while I built the frontend, so we worked in parallel. And ownership didn't stop at launch, so I stayed close to how it behaved after release.

### Tell us about an engineering project you're particularly proud of, in no more than 5 sentences.

- Asked by: Checkly, Senior Product Engineer (Incident Response, remote) (2026-11-24) · `jobs/Checkly-Senior_Product_Engineer_Incident_Response_remote/`
- Status: Submitted (as drafted, unless Mario says otherwise).
- Note: 5 sentences. Condensed from the Block Labs and Ashby analytics portal answers.

I'm most proud of the Coursy analytics portal, a dashboard and trackers (course and training completions, compliance, certificate expiry) that managers open from the admin portal. The brief was a ticket with mock data and a design prototype, and I started the repo in March 2026 and wrote about 124 of its roughly 130 commits. I owned the architecture and conventions (Next.js App Router and TypeScript in a pnpm monorepo, with a shared @repo/ui package on Tailwind and shadcn), the layouts, charts and drawers, the middleware that trusts the admin portal's JWT cookie, and the server-side language switch. After launch I stayed on it through the bug-fix rounds and added a Playwright E2E suite, written with Playwright Test Agents, that runs in a Bitbucket pipeline against an ephemeral environment. I'm proud of it because I took it from a rough brief to a product in managers' hands, and kept owning how it behaved after release.

### Briefly tell us about your full-stack engineering experience, especially where you've owned something end to end. (What you built, what you owned versus handed off, and one decision a reasonable person could disagree with.)

- Asked by: Toggl, Senior Full Stack Engineer (2026-11-24) · `jobs/Toggl-Senior_Full_Stack_Engineer/`
- Status: Submitted. **Mario's own final wording: keep verbatim.**
- Note: New facts from Mario: he built an E2E suite for each Coursy repo (admin, analytics, learner portal), asserting mock data created in the ephemeral Bitbucket CI environment, except analytics, which asserts prelive data. This differs from the Block Labs answer ("assert only what both prelive and the ephemeral CI environment guarantee"); keep the story consistent in interviews.

The most complete and recent end to end ownership project I have had is the Coursy analytics portal, which is a dashboard and a set of trackers for customers managers (training completions, compliance, etc.) routed from an admin portal. I started a mono repo from scratch in March 2026 and wrote most of its commits (around 130) : the architecture I thought for it was: Next.js App Router and TypeScript in a pnpm monorepo with a shared ui package (for general shadcn components, utilities and services) , a single layout, and tailored components (charts and drawers), a middleware to use the aforementioned admin portal's auth token as a cookie and a Playwright e2e suite with its respective CI/CD pipeline. However, for sure the data layer was made by my Team Lead where all the data comes from an Yii API, already owned by the team. Where I owned part of the backend too was on Bitcasino, working mostly as a full stack with both Express and MongoDB.

On the other hand, one call a reasonable person could disagree with is: for Coursy repos (admin, analytics, leaner portal, etc.) I built a e2e suite for each where I decided to assert mock data created specifically on a CI/CD ephemeral env (living only during bitbucket pipeline) except for analytic. For which, I decided particularly to assess data from a prelive env directly instead of an ephemeral env. Why? Because The CI/CD data has no courses, so every rendered widget would show only zeros, which means the tests check that each view loads and renders in the right language, but not actual or significant numbers. I chose a suite that is green for the right reasons in every environment instead of one that checks null data.

## Curiosity and initiative

### What's something, in a professional context, that you've gone deep on purely because you couldn't let it go?

- Asked by: Ashby, Senior Software Engineer, Product Engineering - EU (2026-11-24) · `jobs/Ashby-Senior_Software_Engineer_Product_Engineering_EU/`
- Status: Draft, waiting for Mario's approval.
- Note: Ashby's form asks for exactly one of three questions (four paragraphs at most; answering more than one is rejected). The other two were not answered: "a choice you made that didn't come from a PM or EM, how you advocated for it and its impact on end users" and "a time you challenged and changed a product request". Facts from the Block Labs cookie answer and the Glia workflow answer.

What I couldn't let go of is agent-written work that looks finished but is wrong. At Coursy, the language switch in the analytics portal looked right and worked every time on localhost, but on prelive the page could come back in the old language. The admin portal writes the NEXT_LOCALE cookie on the shared .coursy.io domain, while the new code wrote a host-only cookie with the same name, so the browser kept both. Locally there is only one host, so the bug could not show up there. I fixed it with one shared helper that deletes the cookie in both scopes and writes it with the admin's scope.

Fixing the bug wasn't enough, because the pattern was the real problem: the agent had no way to know that rule, and neither would the next person. So I pulled the thread. I wrote the rule into the app's AGENTS.md, documented the language switch step by step, and made every Playwright test log in through one page object that sets the cookies with that scope and checks that html[lang] matches the expected language.

That led me to rethink how I work with agents in general. On my portfolio I moved from open-ended prompting to a spec-driven flow: every change gets a spec, a plan and a task list that I approve before any code is written, and a coordinator runs a planner, an implementer that writes tests first, and a read-only reviewer. A MEMORY.md records past decisions and mistakes. One entry came from an agent that built a full Spotify integration that turned out to be unusable under the API's Premium requirement. I removed it and wrote down the rule to check external constraints before building.

What I took from it: agents are fast at producing output that looks done, so the leverage is in the rules and checks around them. Each mistake becomes a written rule, a test or a review step, so the next one is caught by the system and not by luck.

## Product impact and metrics

### Tell us about a product initiative you led that improved user engagement, conversion, or monetization. How did you identify the opportunity, what was your specific contribution, and what measurable impact did you achieve?

- Asked by: Spotify, Senior Web Engineer – Subscriptions (2026-11-24, via Jobicy) · `jobs/Spotify-Senior_Web_Engineer_Subscriptions/`
- Status: Draft, waiting for Mario's approval. Needs Mario's input before submitting.
- Note: The CV has no metrics and doesn't say Mario led the SSR work or how the opportunity was spotted. The opening paragraph explains why SEO matters for a casino, not how Mario found it; "the move to SSR" is inferred from the CV's "Improved SEO and performance with Next.js server-side rendering (SSR) and GraphQL (Apollo)". Add a real number (Lighthouse, Core Web Vitals, organic traffic, sign-ups) and who started it, if Mario has them.

On Bitcasino, one of the first cryptocurrency online casinos, I worked on SEO and performance. For a casino brand, both drive player acquisition and conversion: players find a brand through search, and slow or poorly indexed pages lose them before they sign up.

My contribution was the move to server-side rendering (SSR) with Next.js, with data fetched through GraphQL (Apollo), so pages reached search engines and players already rendered instead of being built in the browser. Alongside it, I built new components and features with React, TypeScript and Tailwind across several brands, and shipped them through staging and controlled releases so changes reached production safely.

The impact was better SEO and faster pages on Bitcasino and the other brands that shared the work.

## Incidents and reliability

### Tell us about the most painful incident-response, on-call, alerting, or status-page workflow you've personally experienced. What was broken, what did you build or change, and how did you know it improved? Please answer in no more than 5 sentences.

- Asked by: Checkly, Senior Product Engineer (Incident Response, remote) (2026-11-24) · `jobs/Checkly-Senior_Product_Engineer_Incident_Response_remote/`
- Status: Submitted (as drafted, unless Mario says otherwise).
- Note: 5 sentences. The CV shows no on-call rotation or incident or status-page product, so this uses the Coursy NEXT_LOCALE cookie bug (caught on prelive, not a production incident). Swap in a real production incident or on-call story if Mario has one.

The most painful one I've owned was a language bug in the Coursy analytics portal that only existed outside localhost: switching language worked every time locally, but on prelive the page could come back in the old language, and nothing on my machine could reproduce it. What was broken was the cookie: the admin portal writes NEXT_LOCALE on the shared .coursy.io domain, while the new code wrote a host-only cookie with the same name, so the browser kept both. I found it by testing the switch on prelive across both apps, and fixed it with one shared helper that deletes the cookie in both scopes and writes it with the admin's scope. To stop it coming back, I wrote the rule into the app's AGENTS.md and made every Playwright test log in through one page object that sets the cookies with that scope and checks that html[lang] matches the expected language. I knew it improved because that check runs in our Bitbucket pipeline against an ephemeral environment, so a regression fails the build instead of reaching a user.

## Fit for the role

### What makes you the right hire for this position? Please take a few moments to briefly describe what qualifies you for this role.

- Asked by: HappyRobot, Forward Deployed Engineer (Madrid, hybrid) (2026-11-25) · no folder (not in the Sheet or the queue) · https://www.linkedin.com/jobs/view/4318435019/
- Status: Submitted (as drafted, unless Mario says otherwise).
- Note: The posting's must-haves include Python and building LLM apps (prompting, voice and transcriber tuning). The CV shows neither, so the answer leaves them out. The Brave Search proxy comes from custom-search (Mario's own repo, git author checked).

I've spent 14 years building full-stack products with React, TypeScript and Node.js, and I do my best work when I own something from a rough brief to production. At Coursy I started the analytics portal from scratch, set its architecture in Next.js and TypeScript, and kept owning it after launch, through the bug-fix rounds and a Playwright E2E suite in CI. At Truelogic I set up the development team from scratch and built the first version of the app.

Integrations and APIs run through my work. At DevSavant I helped build an API gateway from scratch on AWS (Lambda, S3, API Gateway) for IntelePeer, and wrote the API and onboarding documentation that sped up new developers' ramp-up. On a personal project I moved the search to the Brave Search API behind a serverless proxy, with a Postgres quota guard and caching, after the search APIs it used were retired.

I'm used to working close to clients: at Encora I resolved long-standing tickets for TripAdvisor and SpotOn, and at Team International I was the link between a team in California and one in Medellín. AI is part of my daily work. I run coding agents under written rules, specs and reviews, and I configured Playwright Test Agents at Coursy.

I'm willing to relocate to Madrid and available to start immediately.

## Motivation and personal

### What about Toggl and this role made you apply? And why now?

- Asked by: Toggl, Senior Full Stack Engineer (2026-11-24) · `jobs/Toggl-Senior_Full_Stack_Engineer/`
- Status: Submitted. **Mario's own final wording: keep verbatim.**
- Note: Mario's answer leaves out the "why now" (Coursy ending, the move to Alicante) and leads with the analytics portal as a reporting tool that matters, plus wanting to learn Go.

I love to provide solutions to problems. For instance, the analytics portal I built at Coursy and mentioned above is a dashboard with charts, filters and trackers for customers managers, which in practice is a more meaningful reporting tool rather than a sober and meaningless tables as reports with raw data. In the job post you say "You own significant parts of that experience end-to-end, working hands-on with product and design to ship work that matters" and that's precisely what I aimed to when I built Coursy Analytics, a tool that is meaningful and matters. Thus, it's very interesting we have a similar conception for a product and that's what caught my attention and that's what makes me want to work at Toggle and help with toggl 2.0. Besides, I have always been keen to learn Golang as a next step on my career which is what you mention the backend is written on so it looks like a match of interests at both sides.

### Beyond any AI-polished application answer, is there something about you that you'd like us to know?

- Asked by: Toggl, Senior Full Stack Engineer (2026-11-24) · `jobs/Toggl-Senior_Full_Stack_Engineer/`
- Status: Submitted. **Mario's own final wording: keep verbatim.**
- Note: Reusable for any "tell us about yourself / something personal" question: F1, the F1-style portfolio (still under construction), SDD and harness engineering.

Well, I'm passionate about many things but specially at both F1 and technology. In fact, I'm writing my own portfolio on a F1 style following f1. official website design system. Yet under construction so it's coming soon. Now, on AI era I'm particularly interested in SDD and harness engineering which I started to integrate actually in my portfolio website and of course eager to implement it on more personal projects and work related ones..

## Video answers

### Send a short Loom video that covers: something you built that you're proud of (and which parts you personally wrote), how AI fits into your day-to-day workflow, and why Motion

- Asked by: Motion (Creative Analytics), Senior / Staff Software Engineer (2026-11-24) · `jobs/Motion-Senior_Staff_Software_Engineer/`
- Status: Draft, waiting for Mario's approval.
- Note: The script is in `jobs/Motion-Senior_Staff_Software_Engineer/loom_script.md` (about 3 minutes). Project: custom-search (personal, chosen by Mario over Coursy). 2022 hand-written (config-driven engines, Redux, MUI, react-intl, tests); Nov 2026 backend rebuilt with Claude Code (Vercel proxy for Brave, Postgres quota guard, CDN cache, 83 tests). Commits checked: all by Mario. The parts can be reused for other video questions.

