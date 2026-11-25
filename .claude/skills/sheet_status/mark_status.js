// Sets the "Estado" dropdown of jobs in the "Vacantes para Mario" Sheet, finding each job by its link.
// Run with mcp__playwright__browser_run_code_unsafe on a copy of this file in which TARGETS and STATUS are filled in.
// STATUS = null only reports where each link is and its current Estado (dry run).
async (page) => {
  const TARGETS = ['https://www.linkedin.com/jobs/view/4422927194'];
  const STATUS = 'Aplicado'; // Por aplicar | Aplicado | Entrevista | Oferta | Descartado | Por referir | Referido | null
  const SHEET_URL = 'https://claude.ai/artifact/8onQyXHwM6TVVm9x8bVuxz';

  // A job's id: the LinkedIn job id, otherwise the URL without protocol, www, query, hash and trailing slash.
  const idOf = (u) => {
    const s = String(u || '').trim();
    const li = s.match(/linkedin\.com\/jobs\/view\/(?:[^/?#]*-)?(\d{6,})/i) || s.match(/currentJobId=(\d{6,})/i);
    if (li) return 'li-' + li[1];
    return s.toLowerCase().replace(/^https?:\/\//, '').replace(/^www\./, '').replace(/[?#].*$/, '').replace(/\/+$/, '');
  };
  const wanted = new Map(TARGETS.map((t) => [idOf(t), t]));
  const results = [];

  if (!page.url().startsWith(SHEET_URL)) await page.goto(SHEET_URL);
  let f = null;
  for (let i = 0; i < 40 && !f; i++) {
    f = page.frames().find((x) => x.url().includes('frame.claudeusercontent.com/_f/'));
    if (!f) await page.waitForTimeout(500);
  }
  if (!f) return { error: 'Sheet frame not found (sign-in wall or bot check?)', title: await page.title() };
  await f.waitForSelector('[role=grid] [role=gridcell]', { timeout: 30000 });

  const active = () => f.evaluate(() => {
    const g = document.querySelector('[role=grid]');
    const c = document.getElementById(g.getAttribute('aria-activedescendant'));
    return c ? { row: Number(c.getAttribute('aria-rowindextext')), col: c.getAttribute('aria-colindextext'), text: c.innerText.trim() } : null;
  });
  const press = async (key, n = 1) => { for (let i = 0; i < n; i++) await page.keyboard.press(key); };
  const toA1 = async () => { await f.locator('[role=grid]').focus(); await page.keyboard.press('Control+Home'); };

  const tabs = await f.locator('[role=tab]:has(.sheet-tab-name)').allInnerTexts();
  for (const tabName of tabs.map((t) => t.trim()).filter(Boolean)) {
    await f.getByRole('tab', { name: tabName, exact: true }).click();
    await page.waitForTimeout(1200);
    await toA1();

    // Header row: find the Estado and Link columns (they differ per tab).
    const header = [];
    for (let i = 0; i < 25; i++) {
      const a = await active();
      header.push(a.text);
      await press('ArrowRight');
    }
    const estado = header.indexOf('Estado');
    const link = header.findIndex((h) => /^link\b/i.test(h)); // "Link", or "Link de referido" on the Mercor tab
    if (estado < 0 || link < 0) { results.push({ tab: tabName, error: 'no Estado or Link header', header }); continue; }

    // Walk down the Link column.
    await toA1();
    await press('ArrowRight', link);
    let blanks = 0;
    for (let i = 0; i < 1000 && blanks < 5; i++) {
      await press('ArrowDown');
      const a = await active();
      if (!a || !a.text) { blanks++; continue; }
      blanks = 0;
      const id = idOf(a.text);
      if (!wanted.has(id)) continue;

      await press('ArrowLeft', link - estado);
      const cell = await active();
      const r = { target: wanted.get(id), found: true, tab: tabName, row: cell.row, before: cell.text, after: cell.text };
      if (STATUS && cell.text !== STATUS) {
        // Enter doesn't always open the dropdown: click the cell's chip, then pick from that cell's own listbox.
        const addr = cell.col + cell.row;
        const gc = f.locator(`[role=gridcell][aria-rowindextext="${cell.row}"][aria-colindextext="${cell.col}"]`);
        const list = f.getByRole('listbox', { name: `Options for ${addr}` });
        await gc.locator('.sheet-chip').click().catch(() => gc.click());
        // The listbox takes a moment to open. Pressing Enter while it opens closes it again, so Enter is only a fallback.
        const opened = await list.waitFor({ timeout: 4000 }).then(() => true, () => false);
        if (!opened) { await press('Enter'); await list.waitFor({ timeout: 4000 }); }
        await page.waitForTimeout(300);
        await list.getByRole('option', { name: STATUS, exact: true }).click();
        await page.waitForTimeout(1000);
        r.after = (await gc.innerText()).trim();
        if (r.after !== STATUS) r.error = `Estado still reads "${r.after}"`;
        await toA1(); // the chip click moves focus; walk back to this row's Link cell
        await press('ArrowDown', cell.row - 1);
        await press('ArrowRight', estado);
      }
      results.push(r);
      await press('ArrowRight', link - estado);
    }
  }
  for (const [id, t] of wanted) if (!results.some((r) => r.target === t && r.found)) results.push({ target: t, found: false });
  return results;
}
