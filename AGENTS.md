# AGENTS.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Mario Granada's job-search workspace (Tallinn, Estonia). It holds no application code. It contains the CV, the LinkedIn profile text, cover letters, an analysis of contract rates and taxes, and LinkedIn thumbnail images. Most tasks involve writing, auditing for ATS and recruiters, and keeping the CV and LinkedIn consistent with each other.

## Layout

- `Mario Granada - Senior Software Engineer CV.docx` / `.pdf` (root): the **current, final CV** as exported from Google Docs. The file name is also the PDF Title metadata.
- `cv_development/`
  - `CV_MarioGranada_Nov2026_v2.md`: **source of truth for the CV text.** It mirrors the final docx word for word. Bullets use `• ` with a blank line between each, so they paste cleanly into Google Docs and LinkedIn.
  - `LinkedIn_Profile_Nov2026.md`: **source of truth for the LinkedIn text.** Each field (Headline, About, each position, Education) is in a copyable code block. It mirrors the live profile at linkedin.com/in/mariogranadacolombia.
  - `CV_MarioGranada_Nov2026_old.docx`, `Copy of CV_MarioGranada_Nov2026 (7).docx`: older iterations, kept for reference only.
- `cover_letter_template.md`: base cover letter with `[Company]`, `[Role]` and `[date]` placeholders. Tailored letters go per company, e.g. a `Loka/` folder.
- `<Company>/`: material for one specific application (e.g. `Loka/`).
- `rate/`: contract-rate analysis for Estonia (individual vs FIE vs OÜ "Munbuh Corp OÜ"). `calc_rates.py` holds the model. `rate-analysis.md` and `ou-tax-guide.md` are the write-ups built from its output.
- `linkedin-thumbnails/`: standalone HTML cards (1200×627 body, LinkedIn link-preview size) that are screenshotted at 2× to make the matching PNGs. `plugin-ui.png` is a source screenshot that `figma-plugin.html` embeds.

## Commands

- Rate model: `cd rate && python3 calc_rates.py`. Edit the `ASSUMPTIONS` block at the top, re-run, then update the numbers in `rate-analysis.md` / `ou-tax-guide.md` by hand. Tax rates are marked as assumptions to verify before relying on them.
- Read a docx: `textutil -convert txt -stdout file.docx`, or `unzip -p file.docx word/document.xml` to inspect its structure.
- Read a PDF and check for hidden characters: `pdftotext file.pdf -`. Google Docs exports can contain U+200B. Check the metadata with `pdfinfo file.pdf`.

## Hard rules

- **Never modify any `.docx` or `.pdf`.** Mario edits those in Google Docs himself. Only edit the `.md` files, then tell him what to change in the doc.
- The CV `.md` and the LinkedIn `.md` must stay in sync with the final docx and the live profile. When one changes, check whether the other needs the same change.
- **Don't invent metrics.** Mario will add real numbers later.
- Mario pushes back on clutter. Keep suggestions minimal and concrete, and don't re-propose ideas he has already declined (listed below).

## Settled decisions (don't re-litigate)

**CV (ATS-oriented):** single column, Arial, real Word bullets, no zero-width characters. Sections are `SUMMARY / WORK EXPERIENCE / EDUCATION`, with no roman numerals.

- Headline (identical on the CV and LinkedIn): `Senior Software Engineer | Product Engineer | Full-Stack · Frontend & Design Systems | AI-Assisted Development`. No technologies in the headline.
- Degree: "B.Sc. Telematics Engineering — Universidad ICESI, Cali, Colombia | 2013". Always "Telematics", never "Telecommunications".
- ATS keyword spellings: Phoenix LiveView, Redux-Saga, Spec-Driven Development, REST APIs, Playwright Test Agents. Avoid slash-joined tokens.
- Client attribution: SpotOn → Encora. IntelePeer → DevSavant, on the AWS API Gateway bullet only. Mack Weldon and Effie.org → Razorfish.
- Yolo is **one** CV entry, opening with the Moon Design System. Razorfish (formerly Intersect & Crown Partners) is **one** CV entry, Sep 2012 – Feb 2015.
- Leaving the gap from Feb 2015 to Apr 2016 off the CV is intentional. So is Globant starting in Aug 2016, the same month Grability ends.
- Technical Skills was trimmed on purpose (AngularJS, PHP, jQuery, WebdriverIO, Jira and Confluence appear only in the bullets). Don't add them back.

**LinkedIn:** bullets only, with no per-position "Skills:" lines.

- Yolo is **two** positions with friendly titles: "Software Engineer at Design System team" and "Software Engineer at Casino team".
- Intersect, Crown Partners and Razorfish are separate positions. Mack Weldon and Effie.org appear under both Crown Partners and Razorfish on purpose, to show how the role evolved.
- Declined ideas: acquisition disclaimer lines, renaming the Yolo titles, removing old skills that colleagues endorsed.
- Top skills: React.js, Next.js, TypeScript, Node.js, AI for Product Development.
- On the certifications page, an attached certificate file can look like a duplicate entry. It isn't one.

**PDF export:** rename the Google Doc to `Mario Granada - Senior Software Engineer CV` before File → Download → PDF. The PDF Title comes from the doc name. Don't put dates or "v2" in names.

## Pending (as of 21 Nov 2026)

- 30 Nov 2026: Coursy ends. Add the end date on LinkedIn and replace "Present" on the CV.
- Add real metrics to 2–3 bullets once Mario provides them.

## Tooling notes

- Validating LinkedIn with Playwright needs Mario's signed-in browser. Scroll to the end of the lazy-loaded Experience and Skills lists before drawing conclusions. Delete `.playwright-mcp/` and any scraped files from the workspace afterwards.
- The Spanish recruiter checklist lives in a Claude Doc, "Perfil de LinkedIn de Mario – mejoras" (claude.ai/artifact/LTmbyvBLZyKH3yPBfR4RGs). If the Docs connector refuses to read it, read it through a Playwright snapshot instead.
