# Glia: Senior Software Engineer, Media

- URL: https://www.linkedin.com/jobs/view/4485012250/
- Location: Tartu, Tartumaa, Estonia · Hybrid · Full-time (apply off LinkedIn)

## Describe your current AI-assisted development workflow and which tools you use (e.g., Claude Code, Cursor). What have you learned or changed in your workflow recently?

I use Claude Code and OpenCode every day, set up to share the same rules. On my portfolio (Next.js, TypeScript, Supabase), the repo has a constitution.md with the project's principles and stack, an AGENTS.md with commands and conventions, and a MEMORY.md where decisions and past mistakes are written down so the agent doesn't repeat them.

My workflow is spec-driven. Every feature, enhancement or bug fix gets a numbered folder under specs/ with a spec (requirements in EARS notation), a plan and a task list, and the folder name tracks its state. A coordinator agent runs the flow through three subagents with limited tools: a planner that only writes specs, an implementer that does one task at a time with tests first, and a read-only reviewer that checks each functional requirement. I approve the spec and the plan before any code is written. Each feature runs in its own git worktree, and visual changes are checked with the Chrome DevTools MCP, including the mobile view. At Coursy.io I also configured Playwright Test Agents.

Recently I moved from open-ended prompting to this spec and approval flow, and I keep the agent configs for both tools in sync. I also learned to check external constraints before building: an agent built a full Spotify integration that turned out to be unusable under the API's Premium requirement, so I removed it and recorded the rule in MEMORY.md. Small rules like that, plus requiring finished specs to be marked completed before merging, are what keep the agents reliable over time.
