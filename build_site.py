"""Build a static website (docs/) from the LLM wiki (wiki/).

Usage:  python build_site.py
Then commit and push; GitHub Pages serves the docs/ folder.
"""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
WIKI = ROOT / "wiki"
OUT = ROOT / "docs"
TEMPLATE = ROOT / "site_template.html"

FOLDER_TYPE = {
    "sources": "source", "concepts": "concept", "materials": "material",
    "properties": "property", "test-methods": "test-method",
    "applications": "application", "datasets": "dataset", "synthesis": "synthesis",
}


def parse_frontmatter(text):
    meta, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if m:
        body = text[m.end():]
        for line in m.group(1).splitlines():
            kv = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
            if not kv:
                continue
            key, val = kv.group(1), kv.group(2).strip()
            val = re.sub(r"\s+#.*$", "", val) if not val.startswith('"') else val
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip().strip('"') for v in val[1:-1].split(",") if v.strip()]
            else:
                val = val.strip('"')
            meta[key] = val
    return meta, body


def first_paragraph(body, after_heading=None):
    text = body
    if after_heading:
        m = re.search(r"^##\s+" + re.escape(after_heading) + r".*?$", body, re.M | re.I)
        if m:
            text = body[m.end():]
    for block in re.split(r"\n\s*\n", text):
        b = block.strip()
        if not b or b.startswith(("#", "|", ">", "-", "<!--", "```")):
            continue
        b = re.sub(r"\[\[([^\]|]+)\]\]", r"\1", b)
        b = re.sub(r"[*_`]", "", b)
        b = " ".join(b.split())
        return b[:400] + ("…" if len(b) > 400 else "")
    return ""


def main():
    notes = []
    for path in sorted(WIKI.rglob("*.md")):
        slug = path.stem
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        folder = path.parent.name if path.parent != WIKI else ""
        ntype = FOLDER_TYPE.get(folder, "hub")
        if slug == "log":
            ntype = "hub"
        h1 = re.search(r"^#\s+(.+)$", body, re.M)
        title = meta.get("title") if ntype == "source" and meta.get("title") else (h1.group(1).strip() if h1 else slug)
        if ntype == "source":
            summary = first_paragraph(body, "One-paragraph summary")
        else:
            summary = first_paragraph(body, "Definition") or first_paragraph(body)
        links = sorted(set(re.findall(r"\[\[([^\]|#]+)", body)) - {slug})
        notes.append({
            "slug": slug, "type": ntype, "title": title, "summary": summary,
            "links": links, "body": body, "meta": meta,
        })

    slugs = {n["slug"] for n in notes}
    for n in notes:
        n["links"] = [l for l in n["links"] if l in slugs]
    backlinks = {s: [] for s in slugs}
    for n in notes:
        for l in n["links"]:
            backlinks[l].append(n["slug"])
    for n in notes:
        n["backlinks"] = sorted(backlinks[n["slug"]])

    data = {
        "built": date.today().isoformat(),
        "notes": notes,
    }
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/null", payload)
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(html, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    n_links = sum(len(n["links"]) for n in notes)
    print(f"Built docs/index.html: {len(notes)} notes, {n_links} links")


if __name__ == "__main__":
    main()
