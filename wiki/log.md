---
type: log
---

# Log

Append-only. Format: `## YYYY-MM-DD — <operation> — <subject>`, followed by bullet points.

## 2026-10-06 — setup — wiki skeleton
- Created the schema (`CLAUDE.md`), templates, hub pages, and empty dataset tables.
- No sources ingested yet.

## 2026-10-06 — ingest — Ranade et al. 2013a, Micromechanics of HSHDC
- Raw file: `raw/papers/Ravi2013_Micromechanics of High Strength, HDC.pdf` (14 pp. incl. appendix)
- Created (15 pages):
  - source: ranade2013-hshdc-micromechanics
  - concepts: hshdc, strain-hardening, multiple-cracking, fiber-bridging, fiber-matrix-interface,
    fiber-dispersion, heat-curing
  - materials: pe-fiber, pva-fiber (stub), silica-fume
  - properties: matrix-fracture-toughness
  - test methods: single-fiber-pullout-test, single-crack-test
  - dataset: micromechanical-parameters
- Updated: terminology-hdc-ecc-shcc (two meanings of HDC), mix-designs (+1 row), gaps, index
- Conflicts: HDC terminology ambiguity; microspalling vs clamping (matrix-dependent)
- µm/mm extraction errors resolved (page image confirms "600 µm"; µ glyph was lost in text extraction)
- Still to verify: τ0 1.52 vs 1.53 MPa; DOI missing

## 2026-10-06 — schema — added "ingest new" command (CLAUDE.md §5.1b)
- Requested by the human: batch-ingest all unprocessed raw files with one message.

## 2026-10-06 — ingest — Ranade et al. 2013b, Composite Properties of HSHDC
- Raw file: `raw/papers/Ravi2013_Composite Properties of Hight-Strength, HDC.pdf` (10 pp.)
- Created (10 pages):
  - source: ranade2013-hshdc-composite-properties
  - properties: tensile-strain-capacity, compressive-strength, crack-width, flexural-strength,
    fresh-properties
  - concepts: uhpc-vhsc
  - test methods: dogbone-uniaxial-tension, split-tension-test, third-point-flexure-test
- Updated: hshdc, fiber-dispersion, multiple-cracking, strain-hardening, heat-curing,
  matrix-fracture-toughness, mix-designs (+6 rows), mechanical-results (+6), gaps
- Conflicts: σ_fc 8.3 (primary) vs 8.4 MPa (quoted in the companion paper)
- To verify: HRWRA basis (1.8% of cement vs 1.26% of cementitious); DOI missing

## 2026-10-06 — ingest — Ranade, Li & Heard 2015, Tensile Rate Effects in HSHDC
- Raw file: `raw/papers/Ravi2014_Tensile Rate Effects in High Strength-HDC.pdf` (11 pp.)
- Slug uses the publication year 2015 (CCR 68). Replaced the placeholder link
  `ranade2014-...` in ranade2013-hshdc-micromechanics.
- Created (3 pages):
  - source: ranade2015-hshdc-tensile-rate-effects
  - concept: strain-rate-effects
  - application: extreme-loading-applications
- Updated: hshdc, pe-fiber, fiber-matrix-interface, matrix-fracture-toughness, strain-hardening,
  tensile-strain-capacity, crack-width, fiber-dispersion, dogbone-uniaxial-tension,
  single-fiber-pullout-test, mix-designs (+1), mechanical-results (+6),
  micromechanical-parameters (+2), gaps, index
- Conflicts:
  - quasi-static ε_tu 4.2% vs 3.4% (2013)
  - J′b 969 vs 682 J/m²
  - min Vf 1.6% vs 1.7%
- To verify: test age not stated; absolute τ0 and fiber properties only in figures

## 2026-10-06 — maintenance — raw folder changed by the human
- Renamed raw file: `Ravi2014_...` → `Ranade2014_...` (text identical); raw_file path updated.
- **Removed at the human's request:** Ranade et al. 2013 (Micromechanics; Composite Properties).
  - Deleted both source pages and all dataset rows (14).
  - Rewrote every topic page from the remaining sources.
  - Deleted the pages split-tension-test and third-point-flexure-test (no remaining source).
  - Links to them inside other source pages were converted to plain "as cited" text.

## 2026-10-06 — ingest new — 5 sources (parallel drafting of source pages, sequential integration)
- New sources:
  - he2024-hdc-research-advances
  - ranade2017-hshdc-impact-resistance
  - su2023-rubber-modified-hshdc
  - yang2024-hshdc-uniaxial-tension
  - ye2021-uhdc-flexural-size-effect (raw file "Ye2020"; slug uses volume year 2021)
- New pages:
  - concepts: uhdc, fiber-geometry, water-binder-ratio, size-effect, fracture-process-zone,
    tensile-constitutive-model
  - materials: fly-ash, crumb-rubber, ggbfs
  - properties: impact-resistance, tensile-toughness, durability, high-temperature-behaviour
  - test methods: impact-test, notched-beam-three-point-bending, digital-image-correlation
  - applications: masonry-wall-retrofit, rc-member-strengthening, unreinforced-hdc-structures,
    3d-printed-hdc
- Rewritten: all remaining concept, material, property, test-method and application pages;
  the datasets; gaps; review-outline; index.
- Key findings:
  - "HSHDC" has 3 lineages (Michigan, GDUT, Xi'an).
  - HDC ≈ ECC/SHCC in the Chinese usage; fiber type does not define it.
  - Heat curing is not required.
  - There is a strength–ductility trade-off across lineages.
