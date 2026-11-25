"""Build jobs/queue.csv from vacantes.xlsx (the export of the "Vacantes para Mario" Sheet).

Usage: python3 scripts/build_queue.py

- One row per unique job across all tabs (duplicates are listed in `duplicate_links`).
- `gate` is a work-rights pre-filter read from the Sheet's permit column.
- `status` merges the Sheet's Estado with the job folders in jobs/ (a folder means a letter exists).
- Triage results already in jobs/queue.csv (fit, verdict, triage_notes) are kept on rebuild.
"""

import csv
import re
import unicodedata
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "vacantes.xlsx"
OUT = ROOT / "jobs" / "queue.csv"

LOCATION_COLS = ["País / ciudad", "Ciudad / país", "Desde dónde se puede trabajar", "Ciudad / modalidad",
                 "Ubicación / dedicación"]
MODALITY_COLS = ["Modalidad", "Contrato"]
PERMIT_COLS = ["Permiso de trabajo", "Permiso / nota", "¿Se puede trabajar desde España?"]
NOTE_COLS = ["Restricción / nota", "Nota para Mario", "Verificación", "Relación con la F1", "Ojo / requisitos"]

GATE_ORDER = ["ok", "check", "spain_permit", "eu_permit", "visa_sponsored", "visa", "blocked"]
STATUS_MAP = {"Por aplicar": "todo", "Aplicado": "applied", "Descartado": "discarded",
              "Por referir": "referral", "Referido": "referred", "Entrevista": "interview", "Oferta": "offer"}
TRIAGE_COLS = ["fit", "verdict", "triage_notes"]

FIELDS = ["key", "status", "gate", "priority", "company", "role", "country", "location", "modality",
          "type", "visa", "permit", "salary", "published", "link", "folder", "contact", "why", "note",
          "tab", "row", "sheet_refs", "duplicate_links"] + TRIAGE_COLS


def norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def linkedin_id(url):
    m = re.search(r"linkedin\.com/jobs/view/(\d+)", url or "")
    return m.group(1) if m else None


def first(d, cols):
    return next((str(d[c]).strip() for c in cols if d.get(c) not in (None, "", "—")), "")


def gate(permit, country):
    p = permit.lower()
    if permit.startswith("❌"):
        return "blocked"
    if permit.startswith("✅"):
        return "visa_sponsored" if "visa" in p and "remoto" not in p else "ok"
    if any(k in p for k in ("reino unido", "visa", "ee. uu", "estados unidos", "canad", "suiza")) \
            or any(k in country for k in ("Reino Unido", "Estados Unidos", "Canadá", "Suiza")):
        return "visa"
    if "españa" in p and "permiso" in p:
        return "spain_permit"
    if "permiso" in p:
        return "eu_permit"
    return "check"


def local_folders():
    """Map queue key (li-<LinkedIn id> or saved Key) and normalized company -> jobs/ folder."""
    by_id, by_company = {}, {}
    for f in sorted((ROOT / "jobs").glob("*/job_posting.md")):
        folder = f"jobs/{f.parent.name}/"
        text = f.read_text()
        for jid in re.findall(r"linkedin\.com/jobs/view/(\d+)", text):
            by_id[f"li-{jid}"] = folder
        for key in re.findall(r"^- Key: (\S+)", text, re.M):  # postings saved by fetch_postings.mjs
            by_id[key] = folder
        by_company[norm(f.parent.name.split("-")[0].replace("_", " "))] = folder
    return by_id, by_company


def same_job(a, b):
    if norm(a["company"]) != norm(b["company"]):
        return False
    ra, rb = norm(a["role"]), norm(b["role"])
    return ra.startswith(rb) or rb.startswith(ra)


def main():
    wb = openpyxl.load_workbook(XLSX, read_only=True, data_only=True)
    by_id, by_company = local_folders()
    old = {}
    if OUT.exists():
        with OUT.open() as fh:
            old = {r["key"]: r for r in csv.DictReader(fh)}

    jobs = []
    for ws in wb.worksheets:
        if ws.sheet_state != "visible":
            continue
        # Keep the real Sheet row number (1 = header) so Mario can find each job in the Sheet.
        rows = [(n, r) for n, r in enumerate(ws.iter_rows(values_only=True), start=1) if any(r)]
        header = [str(h).strip() if h else "" for h in rows[0][1]]
        for row_no, r in rows[1:]:
            d = dict(zip(header, r))
            # The Mercor tab has no Empresa column: the tab name is the company.
            if "Empresa" not in header and "Puesto" in header:
                d["Empresa"] = ws.title
            if not d.get("Empresa"):
                continue
            link = first(d, ["Link", "Link de referido"])
            permit = first(d, PERMIT_COLS)
            country = re.sub(r"^\d+ · ", "", str(d.get("País") or "")).strip()
            pub = d.get("Publicado")
            jid = linkedin_id(link)
            job = {
                "key": f"li-{jid}" if jid else norm(f"{d['Empresa']} {d['Puesto']}").replace(" ", "-")[:60],
                "status": STATUS_MAP.get(d.get("Estado"), d.get("Estado") or "todo"),
                "gate": gate(permit, country),
                "priority": str(d.get("Prioridad") or "").split(" · ")[0],
                "company": str(d["Empresa"]).strip(),
                "role": str(d.get("Puesto") or "").strip(),
                "country": country,
                "location": first(d, LOCATION_COLS),
                "modality": first(d, MODALITY_COLS),
                "type": d.get("Tipo") or "",
                "visa": d.get("¿Patrocina visa?") or "",
                "permit": permit,
                "salary": first(d, ["Salario", "Pago (USD/h)"]),
                "published": pub.date().isoformat() if hasattr(pub, "date") else str(pub or ""),
                "link": link,
                "folder": "",
                "contact": first(d, ["Contacto (reclutador)"]),
                "why": first(d, ["Por qué encaja"]),
                "note": first(d, NOTE_COLS),
                "tab": ws.title,
                "row": row_no,
                "sheet_refs": f"{ws.title} {row_no}",
                "duplicate_links": "",
            }
            job["folder"] = by_id.get(job["key"], "")
            if not job["folder"] and job["status"] == "todo" and norm(job["company"]) in by_company:
                job["note"] = (job["note"] + " | " if job["note"] else "") + \
                    f"Same company as {by_company[norm(job['company'])]}"
            if job["folder"] and job["status"] == "todo":
                job["status"] = "letter_ready"
            for c in TRIAGE_COLS:
                job[c] = old.get(job["key"], {}).get(c, "")
            jobs.append(job)

    # Deduplicate: same LinkedIn id, or same company with one role title a prefix of the other.
    unique = []
    for job in jobs:
        dup = next((u for u in unique if u["key"] == job["key"] or same_job(u, job)), None)
        if dup:
            dup["sheet_refs"] += f"; {job['sheet_refs']}"
            if job["link"] != dup["link"]:
                dup["duplicate_links"] = " ".join(filter(None, [dup["duplicate_links"], job["link"]]))
            if job["status"] != "todo" and dup["status"] == "todo":
                dup["status"] = job["status"]
            dup["priority"] = min(dup["priority"], job["priority"])
            continue
        unique.append(job)

    unique.sort(key=lambda j: (j["status"] != "todo", GATE_ORDER.index(j["gate"]), j["priority"],
                               "".join(chr(255 - ord(c)) for c in j["published"])))
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(unique)

    from collections import Counter
    print(f"{len(jobs)} rows -> {len(unique)} unique jobs -> {OUT.relative_to(ROOT)}")
    print("status:", dict(Counter(j["status"] for j in unique)))
    todo = [j for j in unique if j["status"] == "todo"]
    print("todo by gate:", {g: sum(j["gate"] == g for j in todo) for g in GATE_ORDER})
    print("todo ok/check by priority:",
          dict(Counter(j["priority"] for j in todo if j["gate"] in ("ok", "check"))))


if __name__ == "__main__":
    main()
