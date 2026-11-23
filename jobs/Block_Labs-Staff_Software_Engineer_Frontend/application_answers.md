# Block Labs: Staff Software Engineer, Frontend

- URL: https://www.linkedin.com/jobs/view/4478406396/
- Location: Málaga, Andalusia, Spain · Remote · Full-time (apply off LinkedIn)
- Sources: coursy-analytics, coursy, coursy-intra, coursy-marketplace repos; portfolio-mario-hernandez repo
- Status: final answers, in Mario's own wording (2026-11-23)

## Name one frontend you took from a rough brief to production and owned after launch. What was yours, what was your team's and what was your agents'?

From my most recent job role (Coursy - a B2B Learning Management System provider that helps to create tailored courses and trainings for customers employees): 
The Coursy analytics portal: a dashboard and trackers (course and training completions, compliance, certificate expiry) that managers open from the admin portal. The brief was a ticket with mock data and a design prototype. I started the repo in March 2026 and wrote about 124 of its roughly 130 commits.

Mine: the architecture and conventions (Next.js App Router and TypeScript in a pnpm monorepo, with a shared @repo/ui package on Tailwind and shadcn), the layouts, sidebar, charts and drawers, the middleware that trusts the admin portal's JWT cookie, the server-side language switch, and the bug-fix rounds after launch. Later I added the Playwright E2E suite and its CI pipeline.

My team's: My Team Lead built the backend side (a slim analytics token, the privileges endpoint and the link from the admin sidebar) and the initial repo setup. The data comes from the admin's Yii API, which another part of the team owns.

My agents': the E2E tests, written through Playwright Test Agents (planner, generator and healer) under rules I wrote in AGENTS.md: log in only through one page object, never inline, and assert only what both prelive and the ephemeral CI environment guarantee, since the CI data has no courses and every widget shows zeros there.

## What is in your agent setup right now? Context files, design system rules, and what runs before agent-written code ships.

Context files: every repo has a short AGENTS.md that the agent reads first, with a trigger table that loads skill files only when the task needs them (deployments, translations, Playwright tests, test fixtures, customer skins). App-level files override the root. They hold the rules agents get wrong without them: no N+1 queries in Yii2, keep the API backward compatible because the admin and learner portals deploy separately, bump the portal's asset version when its JS changes, never use SSH. I use to add a constitution.md (principles and stack) and a MEMORY.md with past decisions and mistakes, and run a coordinator with planner, implementer and reviewer agents that each have limited tools, mirrored for either Claude Code or OpenCode.

Design system rules: colors, spacing and type come from semantic tokens (chart colors as Tailwind tokens in analytics), with no hardcoded values like text-white, and shared components come from the design system (@repo/ui). Every user-facing string goes through next-intl, in every locale file.

Before agent-written code ships: I approve the spec and plan first. The implementer writes tests first and does one task at a time; lint, build and node --test must pass; visual changes are checked with the Chrome DevTools MCP, mobile included; a read-only reviewer checks each functional requirement, with at most two fix rounds. At Coursy particularly, Playwright E2E runs in a Bitbucket pipeline against an ephemeral environment, and every change goes through a pull request.

## The last time an agent produced UI that looked right but was wrong, how did you catch it, and what did you change so it does not happen again?

At Coursy, the language switch in the analytics portal. The agent's version looked right: picking a language in the sidebar re-rendered the page in that language, and it worked every time on localhost. On prelive it didn't hold. The admin portal writes the NEXT_LOCALE cookie on the shared .coursy.io domain, while the new code wrote a host-only cookie with the same name, so the browser kept both and the page could come back in the old language. Locally there is only one host, so the bug could not show up there.

I caught it by testing the switch on prelive across both apps, moving between the admin portal and analytics instead of staying inside analytics. The fix deletes the cookie in both scopes and writes it with the admin's scope from one shared helper. Then I made it hard to repeat: the app's AGENTS.md now says cookies are written only with the admin's scope, because a different scope survives as a stale duplicate; the language switch is documented step by step for agents; and every Playwright test logs in through one page object that sets the cookies with that scope and checks that html[lang] matches the expected language.

## Which parts of your job should agents take over completely, and which should stay with you? Why?

Agents can take over completely where a check decides when it's done and where tasks are automated. For instance: writing and healing E2E tests, translation keys across every locale file, refactors that mirror an existing pattern, migrations, and documentation such as runbooks and handoff notes. Hence, a wrong result fails a test, a lint rule or a build.

What stays with me is the criteria on what should be done by an agent and what not, where exactly and how (Backend, Server Side, Client side to name some) As well, it stays with me the work is plausible but wrong, expensive and also when nothing automatic could catch it: deciding what to build and the trade offs, architecture and conventions, design system decisions like consistency versus flexibility, contracts between apps that deploy separately, the final visual and UX judgement across themes and breakpoints, etc. Agents are fast and accurate at producing output that looks finished. However, I'm accounted for how it behaves in production and the final output overall.
