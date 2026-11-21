# Context: CV and LinkedIn overhaul (Nov 2026)

Summary of the working session from 21 Nov 2026, for use as context in new conversations. **The "Final agreements" section takes priority over anything else.**

---

## Files (in `jobApplications/`)

| File | What it is |
|---|---|
| `CV_MarioGranada_Nov2026_v2.md` | **Source of truth for the CV text.** It matches `Copy of CV_MarioGranada_Nov2026 (7).docx` word for word. Bullets use `•` with a blank line between each, so they paste cleanly into Google Docs and LinkedIn. |
| `Copy of CV_MarioGranada_Nov2026 (7).docx` | Latest CV layout (Google Docs export), ATS-checked. Earlier versions are (5) and (6). |
| `LinkedIn_Profile_Nov2026.md` | **Source of truth for the LinkedIn text**, organised by field (Headline, About, each position, Education) in copyable code blocks. It matches the live profile. |
| `CV_MarioGranada_Nov2026.md` | First markdown conversion of the new CV. Superseded by v2. |
| `CV_MarioGranada_Nov2026_old.md` / `_old.docx` | Old CV with "Main functions / Keywords / Impact and Achievements" paragraphs. Use for reference only. |
| `CV_MarioGranada_Nov2026.docx` / `.pdf` | Earlier new-format CV. Do not edit. |
| Claude Doc "Perfil de LinkedIn de Mario – mejoras" | Spanish checklist and recruiter notes for LinkedIn: https://claude.ai/artifact/LTmbyvBLZyKH3yPBfR4RGs |

Rule: **never modify any .docx or .pdf.** Only the .md files are edited.

---

## Final agreements (latest decisions)

### CV
- **Format:** single column; sections SUMMARY / WORK EXPERIENCE / EDUCATION (no roman numerals, and "Education" instead of "Academic Formation"); Arial; real Word bullets with no zero-width characters; contact details in the body.
- **Headline (CV and LinkedIn, word for word):** `Senior Software Engineer | Product Engineer | Full-Stack · Frontend & Design Systems | AI-Assisted Development`. No technologies in the headline.
- **Degree:** *B.Sc. Telematics Engineering — Universidad ICESI, Cali, Colombia | 2013*. Use "Telematics", never "Telecommunications".
- **Summary:** first person, "Telematics Engineer with 14+ years", followed by the client list and one line of soft skills. Mario's soft-skills line stays as it is.
- **Technical Skills:** Mario trimmed these on purpose (AngularJS, PHP, jQuery, plain "Playwright", WebdriverIO, Jira and Confluence were removed from the list because they still appear in the bullets). HTML, CSS, REST APIs, Responsive design and Accessibility were added. Final list: see v2.md.
- **Keyword spellings for ATS:** Phoenix LiveView, Redux-Saga, "Playwright and Playwright Test Agents", Spec-Driven Development, REST APIs.
- **Client attribution:** SpotOn → Encora. IntelePeer → DevSavant, tied to the **AWS API Gateway** bullet only (not React or Angular). Mack Weldon and Effie.org → Razorfish.
- **Yolo** is **one entry** on the CV, opening with the Moon Design System.
- **Razorfish (formerly Intersect & Crown Partners)** is **one entry** on the CV, Sep 2012 – Feb 2015.
- **Dates:** Globant starting **Aug 2016** is intentional, even though Grability ends Aug 2016.
- **Headline length** is fine as it is.
- **Gap Feb 2015 – Apr 2016:** leave it off the CV and have a one-line verbal explanation ready.
- **Metrics:** none yet. Mario will add real numbers later. Don't invent any.
- **PDF export:** rename the Google Doc (e.g. "Mario Granada - Senior Software Engineer CV") before File → Download → PDF so the PDF Title metadata is correct. Alternative: `exiftool -Title=...`.

### LinkedIn
- **Bullets only.** No "Main functions / Keywords / Impact" paragraphs, and **no per-position "Skills:" lines** (removed at Mario's request).
- **Yolo** is **two positions**: "Software Engineer at Design System team" (Oct 2024 – Nov 2025) and "Software Engineer at Casino team" (Sep 2022 – Sep 2024). **Mario keeps the friendly titles.** The doc's "– Design System / – Bitcasino" suggestion was declined.
- **Intersect** (Sep 2012 – May 2013), **Crown Partners** (Jun 2013 – Jul 2014) and **Razorfish** (Jul 2014 – Feb 2015) are **separate positions**, all with bullets.
- **No acquisition disclaimer lines.** Declined as clutter. The Razorfish bullet "staying with the same team and clients through the company's acquisitions" covers it.
- **Mack Weldon and Effie.org** are deliberately under **both Crown Partners and Razorfish**, but not Intersect. This shows how the role and stack evolved. It's consistent with the CV's single Razorfish entry.
- **About:** the new version is live (senior software engineer, 14+ years, React/Next.js/TypeScript plus Elixir/Phoenix LiveView, Moon Design System, Bitcasino, Coursy, career in Colombia, Telematics degree, open to roles). It's mirrored in `LinkedIn_Profile_Nov2026.md`.
- **Top 5 skills (live):** React.js • Next.js • TypeScript • Node.js • AI for Product Development. Recommendation: keep Node.js rather than the generic "Software Development".
- **Skills list:** TypeScript, Node.js, Vue.js, Redux.js, Jest, React Testing Library, Docker, CI/CD, AWS, Express.js, Apollo GraphQL, REST APIs, Accessibility/WCAG and Playwright test agents have all been added. LinkedIn has no "GitHub Actions" skill, so CI/CD covers it.
- **Endorsed old skills** (.NET, C#, Java, duplicate CSS entries, etc.) **stay**. Mario won't remove skills endorsed by former colleagues.
- **Certifications:** LiveView Pro, Developing with Elixir & OTP, Next.js 14 & React – The Complete Guide (Academind, with credential), React Day Berlin 2023, FoCUS. "Nextjs-React The complete guide" was the **attached certificate file** of the Academind entry, not a duplicate. Mario renamed it to match the course name.
- **Featured:** Variables Management Figma plugin and the Moon Design System Phoenix LiveView library (Hex). The npm link (`npmjs.com/package/@moondesignsystem/react`) doesn't generate a LinkedIn preview because npm blocks scrapers. Workarounds: mention the npm URL in the Hex item's description, or feature the GitHub repo or Storybook site, or add it as media.
- **Languages:** English (full professional), German (elementary), Spanish (native).
- **Open to Work:** recruiters only.

### Final check of the live profile against the doc (21 Nov 2026)
Every item on the doc's checklist is either done on the live profile or declined on purpose. Declined: the Yolo title change and the acquisition lines. Changed: top skills went with Node.js and AI for Product Development instead of Elixir and Design Systems. The "Spec-Driven Software Development" duplicate is gone from Skills. The only item left open is the Coursy end date on 30 Nov. The checkboxes in the doc itself aren't ticked.

### Pending
1. **30 Nov 2026:** add an end date to Coursy on LinkedIn, and change "Present" on the CV. The "Most recently…" wording in the About section still works.
2. Add real **metrics** to two or three bullets (Moon brands and components, release time, team size, onboarding speed).
3. Optional: work around the npm link in Featured (see above).

---

## Working notes for the assistant
- The user reviews everything and pushes back on ideas that add clutter. Keep suggestions minimal and concrete.
- When validating LinkedIn with Playwright, **scroll to the end** of the lazy-loaded lists (Experience, Skills) before drawing conclusions. A first pass once missed Intersect and TypeScript.
- On LinkedIn's certifications page, an attached file's title shows up as if it were a separate entry. Don't report it as a duplicate.
- Delete any `.playwright-mcp/` or scraped temporary files from the workspace afterwards.
