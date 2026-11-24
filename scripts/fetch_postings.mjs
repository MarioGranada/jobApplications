// Read job postings from jobs/queue.csv with Playwright and save each one as
// jobs/triage/postings/<key>.md, so triage can read them without a browser.
//
// Usage: node scripts/fetch_postings.mjs [--gate ok,check] [--priority 1,2] [--limit 30] [--keys li-123,li-456]
//
// - Uses the signed-in browser state in ~/.playwright-auth/linkedin.json (LinkedIn needs it).
// - Skips jobs already fetched, and jobs whose status isn't "todo".
// - Waits 20-40 s between postings so the pace stays human (about 50 a day is the target).

import { chromium } from "playwright";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const QUEUE = path.join(ROOT, "jobs/queue.csv");
const OUT_DIR = path.join(ROOT, "jobs/triage/postings");
const STATE = path.join(os.homedir(), ".playwright-auth/linkedin.json");
const END_MARKERS = ["Set alert for similar jobs", "About the company", "Similar jobs", "People also viewed"];

function arg(name, fallback) {
  const i = process.argv.indexOf(`--${name}`);
  return i > -1 ? process.argv[i + 1] : fallback;
}

function parseCsv(text) {
  const rows = [];
  let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (quoted) {
      if (c === '"' && text[i + 1] === '"') { field += '"'; i++; }
      else if (c === '"') quoted = false;
      else field += c;
    } else if (c === '"') quoted = true;
    else if (c === ",") { row.push(field); field = ""; }
    else if (c === "\n") { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += c;
  }
  if (field || row.length) { row.push(field); rows.push(row); }
  const [header, ...body] = rows;
  return body.filter(r => r.length > 1).map(r => Object.fromEntries(header.map((h, i) => [h, r[i] ?? ""])));
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function readPosting(page, url) {
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await sleep(3000);
  if (/linkedin\.com/.test(url)) {
    if (/authwall|login|checkpoint/.test(page.url())) return { error: "LinkedIn sign-in wall: refresh ~/.playwright-auth/linkedin.json" };
    const more = page.locator("main button").filter({ hasText: /^(…|\.\.\.)?\s*(see\s+)?more$/i }).first();
    if (await more.count()) await more.click().catch(() => {});
    await sleep(800);
    let text = await page.locator("main").innerText().catch(() => "");
    for (const m of END_MARKERS) { const i = text.indexOf(m); if (i > 500) text = text.slice(0, i); }
    return { text };
  }
  const frames = page.frames().filter(f => /greenhouse|lever|workday|ashby|smartrecruiters/.test(f.url()));
  const text = frames.length ? await frames[0].locator("body").innerText() : await page.locator("body").innerText();
  return { text };
}

const gates = arg("gate", "ok,check").split(",");
const priorities = arg("priority", "1,2,3").split(",");
const keys = arg("keys", "") ? arg("keys").split(",") : null;
const limit = Number(arg("limit", "30"));

fs.mkdirSync(OUT_DIR, { recursive: true });
const jobs = parseCsv(fs.readFileSync(QUEUE, "utf8"))
  .filter(j => keys ? keys.includes(j.key) : j.status === "todo" && gates.includes(j.gate) && priorities.includes(j.priority))
  .filter(j => j.link && !fs.existsSync(path.join(OUT_DIR, `${j.key}.md`)))
  .slice(0, limit);

console.log(`Fetching ${jobs.length} postings`);
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ storageState: fs.existsSync(STATE) ? STATE : undefined, locale: "en-US" });
const page = await context.newPage();

for (const [n, job] of jobs.entries()) {
  const today = new Date().toISOString().slice(0, 10);
  let result;
  try { result = await readPosting(page, job.link); } catch (e) { result = { error: String(e.message).split("\n")[0] }; }
  if (result.error) {
    console.log(`[${n + 1}/${jobs.length}] ${job.company}: ERROR ${result.error}`);
    if (/sign-in wall/.test(result.error)) break;
  } else {
    const closed = /No longer accepting applications|no longer available|job has expired/i.test(result.text);
    const md = [
      `# ${job.company}: ${job.role}`, "",
      `- Key: ${job.key}`, `- URL: ${job.link}`, `- Read: ${today}`,
      `- Sheet: priority ${job.priority}, gate ${job.gate}, ${job.country} · ${job.location} · ${job.modality}`,
      `- Permit note: ${job.permit}`, `- Salary (Sheet): ${job.salary || "—"}`,
      closed ? "- **CLOSED: no longer accepting applications**" : "", "",
      "## Posting text", "", result.text.trim(), "",
    ].join("\n");
    fs.writeFileSync(path.join(OUT_DIR, `${job.key}.md`), md);
    console.log(`[${n + 1}/${jobs.length}] ${job.company}: ${closed ? "CLOSED" : "ok"} (${result.text.length} chars)`);
  }
  if (n < jobs.length - 1) await sleep(20000 + Math.random() * 20000);
}

await context.storageState({ path: STATE }).catch(() => {});
await browser.close();
