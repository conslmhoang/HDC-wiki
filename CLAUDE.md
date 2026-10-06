# HDC LLM Wiki — Schema

This repository is an **LLM-maintained wiki** on **High Ductile Concrete (HDC)** and closely
related strain-hardening cementitious composites (ECC, SHCC, SHGC). Its purpose is to support a
**literature review** for a master's thesis in the Smart Concrete course.

You (the LLM) write and maintain everything under `wiki/`. The human curates sources, asks
questions, and verifies. Read this file fully before any operation.

---

## 1. Layers

| Path | Role | Rule |
|---|---|---|
| `raw/` | Original sources (PDF papers, standards, theses, datasets) | **Never edit, rename, or delete.** Read only. |
| `wiki/` | Compiled knowledge as Markdown pages | You create and update these pages. |
| `templates/` | Page templates | Copy a template when you create a new page. |
| `CLAUDE.md` | This schema | Edit only when the human agrees to a convention change. |

Raw file naming (the human does this, and you suggest it when files arrive badly named):
`raw/papers/<FirstAuthorSurname><Year>_<short-keyword>.pdf`, e.g. `raw/papers/Li2001_ECC-micromechanics.pdf`.

## 2. Wiki structure

```
wiki/
├── index.md          # Catalogue of every page with a one-line summary. Read this first.
├── log.md            # Append-only history of ingests, queries saved, and lint passes.
├── gaps.md           # Research gaps, contradictions, open questions.
├── sources/          # One page per raw source.        slug: <firstauthor><year>-<keyword>
├── concepts/         # Mechanisms and theory.          e.g. strain-hardening, fiber-bridging
├── materials/        # Constituents.                   e.g. pva-fiber, fly-ash
├── properties/       # Measured behaviours.            e.g. tensile-strain-capacity
├── test-methods/     # Testing procedures.             e.g. dogbone-uniaxial-tension
├── applications/     # Structural uses.                e.g. masonry-wall-retrofit
├── datasets/         # Aggregated tables across sources (mix designs, results)
└── synthesis/        # Thematic syntheses = draft chapters of the literature review
```

- Filenames: lowercase kebab-case, `.md`, no spaces. One topic per page.
- Links: Obsidian wikilinks `[[page-slug]]` (no folder, no extension). Every page must have
  at least one inbound and one outbound link.
- Every page starts with YAML frontmatter (see templates). Keep `updated:` current.

## 3. Terminology and units (follow strictly)

- **HDC**: High Ductile Concrete, the term used mainly in the Chinese literature
  (e.g. the Xi'an University of Architecture and Technology group). **ECC**: Engineered
  Cementitious Composites (V.C. Li). **SHCC**: Strain-Hardening Cementitious Composites (RILEM).
  These terms overlap but are **not** automatically interchangeable. On each source page, record
  the term the authors use **and** the actual performance they report. Never relabel a material.
- Do not treat UHPC/UHPFRC, ordinary FRC, or SFRC as HDC unless the source shows
  tensile strain hardening. They may be pages of their own for comparison.
- Units: SI. Stress in MPa, strain in % (state whether it is **tensile strain capacity** at
  peak stress or ultimate), crack width in µm, fiber length in mm, diameter in µm,
  fiber content in **vol.%** (convert from kg/m³ only if density is given, and say so).
- Binder ratios: write `W/B` (water/binder) and `FA/C` (fly ash/cement) explicitly. Say whether a
  ratio is by mass.
- Ages: always state curing age (e.g. 28 d) for a reported property.

## 4. Evidence rules (most important)

1. **Every quantitative claim must carry a citation** to a source page, plus location when
   possible: `(see [[li2001-ecc-micromechanics]], Table 3)`.
2. **Never invent numbers, authors, years, DOIs or titles.** If you are unsure of something
   in a PDF, write `⚠️ unverified` and add it to the "To verify" list on the source page.
3. Distinguish clearly between:
   - **Reported**: what the source states.
   - **Interpreted**: your synthesis across sources. Mark it `> Synthesis:`.
4. When sources disagree, keep **both** values with citations, add a `⚔️ Conflict` note, and
   add the conflict to `wiki/gaps.md`. Do not average them or pick one silently.
5. Background knowledge not taken from a source in `raw/` may appear only with the tag
   `[general knowledge — needs source]`. The human will replace it with a real citation.

## 5. Operations

### 5.1 Ingest — triggered when the human says "ingest <file>"
1. Read the whole source (text, tables, and figure captions).
2. Create `wiki/sources/<slug>.md` from `templates/source.md`. Fill **every** field. Write
   `n/a` or `not reported` where appropriate, and never leave a field blank.
3. Add the source's mix designs and key results as rows in the relevant tables in `wiki/datasets/`.
4. Update or create the concept, material, property, test-method and application pages that the
   source touches (typically 5–15 pages). Add new facts with citations, and do not delete earlier
   content without noting why.
5. Check for contradictions with existing pages, then apply rule 4.4.
6. Update `wiki/index.md` (new pages plus revised summaries) and append an entry to `wiki/log.md`.
7. Report to the human: pages created, pages updated, conflicts found, and items to verify.

Batch ingest: process one source at a time and run the full steps for each.

### 5.1b Ingest new — triggered when the human says "ingest new" (or "ingest all")
1. List every file under `raw/` (except README and `.gitkeep`). A file is **new** if no page in
   `wiki/sources/` has it as its `raw_file:` value.
2. Order the new files so that foundational or companion papers come first (e.g. composite
   properties before applications). If there is no clear order, use year then name.
3. Run the full 5.1 procedure for each file, one at a time. Do not stop between files to ask.
4. At the end, give **one combined report**: per source, the pages created or updated; then all
   conflicts and all "To verify" items together.

### 5.2 Query — triggered when the human asks a question
1. Read `wiki/index.md`, then the relevant pages. Read `raw/` only if the wiki is insufficient.
2. Answer with citations to source pages.
3. If the answer is a reusable synthesis (a comparison, trend, or table), offer to save it as a
   page in `wiki/synthesis/` or `wiki/datasets/`, and log it.

### 5.3 Lint — triggered when the human says "lint"
Check for and report:
- orphan pages (no inbound links) and broken `[[links]]`
- claims without citations, `⚠️ unverified` items, `[general knowledge — needs source]` tags
- conflicts that are not listed in `gaps.md`
- concepts mentioned in 3 or more pages that lack their own page
- stale `index.md` entries
- dataset rows with missing key fields
Then propose fixes, apply the ones the human approves, and log the pass.

### 5.4 Draft review section — triggered when the human says "draft <chapter>"
Use `wiki/synthesis/review-outline.md` as the outline. Write academic prose that cites
**source pages**. At the end, list the references in full using the bibliographic data from
the source pages. Do not cite any source that lacks a source page.

## 6. Style

- Wiki pages: concise, factual, in English. Use bullet lists and tables over long prose
  (except in `synthesis/`).
- Chat replies to the human may be in Vietnamese if the human writes in Vietnamese.
- Keep each page focused. Split a page once it exceeds roughly 400 lines.
