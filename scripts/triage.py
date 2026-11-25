"""Record triage results in jobs/queue.csv and rebuild jobs/triage.md.

Usage:
  python3 scripts/triage.py set <key> <fit 1-5> <apply|maybe|skip|closed> "<notes>"
  python3 scripts/triage.py status "<Estado>" <url> [<url> ...]   # mirror a Sheet Estado change
  python3 scripts/triage.py report
"""

import csv
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / "jobs" / "queue.csv"
REPORT = ROOT / "jobs" / "triage.md"
POSTINGS = ROOT / "jobs" / "triage" / "postings"
VERDICTS = ["apply", "maybe", "skip", "closed"]
# Status comes from the Sheet's Estado column (the source of truth), shown in the Sheet's own words.
STATUS_LABELS = {"todo": "Por aplicar", "applied": "**Aplicado**", "discarded": "Descartado",
                 "referral": "Por referir", "referred": "Referido", "interview": "**Entrevista**",
                 "offer": "**Oferta**", "letter_ready": "Por aplicar (carta lista)"}
ESTADOS = {"Por aplicar": "todo", "Aplicado": "applied", "Descartado": "discarded", "Por referir": "referral",
           "Referido": "referred", "Entrevista": "interview", "Oferta": "offer"}


def job_id(url):
    """LinkedIn job id, otherwise the URL without protocol, www, query, hash and trailing slash."""
    s = url.strip()
    m = re.search(r"linkedin\.com/jobs/view/(?:[^/?#]*-)?(\d{6,})", s, re.I) or re.search(r"currentJobId=(\d{6,})", s, re.I)
    if m:
        return "li-" + m.group(1)
    s = re.sub(r"^https?://", "", s.lower())
    s = re.sub(r"^www\.", "", s)
    return re.sub(r"[?#].*$", "", s).rstrip("/")


def load():
    with QUEUE.open() as fh:
        reader = csv.DictReader(fh)
        return reader.fieldnames, list(reader)


def save(fields, rows):
    with QUEUE.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def report(rows):
    triaged = [r for r in rows if r["verdict"]]
    fetched = {p.stem for p in POSTINGS.glob("*.md")} if POSTINGS.exists() else set()
    pending = [r for r in rows if r["key"] in fetched and not r["verdict"]]
    lines = [
        "# Triage", "",
        f"_Generated {date.today().isoformat()} by `scripts/triage.py report` from `jobs/queue.csv`. "
        "Fit is 1–5. Sheet (tab, row) points to the job's row in the Sheet, and Status is the Sheet's Estado "
        "at the last export. Mark a job \"Aplicado\" in the Sheet after you submit it._", "",
        f"Triaged: {len(triaged)} · Fetched, not triaged yet: {len(pending)}", "",
    ]
    for verdict in VERDICTS:
        group = sorted((r for r in triaged if r["verdict"] == verdict),
                       key=lambda r: (-int(r["fit"] or 0), r["priority"]))
        if not group:
            continue
        lines += [f"## {verdict.capitalize()} ({len(group)})", "",
                  "| Sheet (tab, row) | Status | Fit | Company | Role | Where | Notes | Link |",
                  "|---|---|---|---|---|---|---|---|"]
        for r in group:
            where = r["location"] or r["country"]
            notes = r["triage_notes"].replace("|", "/")
            refs = r["sheet_refs"].replace("; ", "<br>")
            status = STATUS_LABELS.get(r["status"], r["status"])
            lines.append(f"| {refs} | {status} | {r['fit']} | {r['company']} | {r['role']} | {where} | {notes} | "
                         f"[posting]({r['link']}) |")
        lines.append("")
    REPORT.write_text("\n".join(lines))
    print(f"{REPORT.relative_to(ROOT)}: {len(triaged)} triaged, {len(pending)} pending")


def main():
    fields, rows = load()
    if sys.argv[1:2] == ["set"]:
        key, fit, verdict, notes = sys.argv[2:6]
        assert verdict in VERDICTS, f"verdict must be one of {VERDICTS}"
        row = next(r for r in rows if r["key"] == key)
        row.update(fit=fit, verdict=verdict, triage_notes=notes)
        save(fields, rows)
    elif sys.argv[1:2] == ["status"]:
        # Mirrors an Estado change already made in the Sheet, until the next export.
        estado, urls = sys.argv[2], sys.argv[3:]
        assert estado in ESTADOS, f"Estado must be one of {list(ESTADOS)}"
        wanted = {job_id(u): u for u in urls}
        for r in rows:
            ids = {job_id(r["link"])} | {job_id(u) for u in r["duplicate_links"].split()}
            if r["key"] in wanted or ids & wanted.keys():
                r["status"] = ESTADOS[estado]
                print(f"{r['key']}: {r['company']} · {r['role']} -> {estado}")
                wanted = {k: v for k, v in wanted.items() if k != r["key"] and k not in ids}
        for u in wanted.values():
            print(f"not in queue: {u}")
        save(fields, rows)
    report(rows)


if __name__ == "__main__":
    main()
