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

## 2026-10-16 — ingest new — 5 sources (parallel source drafting, sequential integration)
- New sources: li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring,
  yu2018-ecc-direct-tensile-review (raw "Yu2017"), ma2021-ecc-durability-review (raw "Ma2020"),
  zhang2022-hshdcc-review. Slug years use the journal volume year.
- New pages:
  - concepts: steady-state-cracking, fiber-surface-treatment
  - properties: self-healing, permeability, shrinkage, fatigue
- Rewritten: pva-fiber, durability, high-temperature-behaviour, crack-width, gaps, review-outline.
- Updated about 20 topic pages; datasets +20 rows.
- Key changes:
  - The PVA gap is filled (Li 2002).
  - The strength–ductility trade-off is revised: it is not fundamental (Zhang 2022).
  - The two PSH indices fail in opposite cases (Li 2002 vs Su 2023).
  - There are two crack-width families: PVA about 40–90 µm, PE about 80–200 µm.
- The human decided the corpus (11 papers) is sufficient.

## 2026-10-20 — ingest — 5 sources (downloaded by the LLM; 13 more still to obtain)
- Downloaded: Kanda 2006, Yang 2008, Li 2003 (J-STAGE PDFs); Chai 2023 and Li 2021 sulfate (Europe PMC
  full-text XML, CC BY, because MDPI/NCBI block scripted PDF download). Hindawi, ScienceDirect and ACI
  blocked automated download; the 13 remaining papers need the human's browser or library access.
- New sources: kanda2006-psh-design-criteria, yang2008-ecc-fiber-bridging-law, li2003-ecc-review,
  chai2023-hdc-ambient-temperature, li2021-hdc-sulfate-dry-wet.
- New page: repair-and-field-applications.
- Corrected: PSH thresholds (1.2 / 3 = pull-out type, Kanda & Li 1998b; 1.3 / 2.7 = rupture type, 2006)
  on strain-hardening and steady-state-cracking; "no standard" → JC/T 2461-2018 (≥ 0.5%, ≤ 200 µm);
  "no primary durability study" and "no Chinese PVA-HDC primary data" statements.
- Updated about 20 topic pages and 3 datasets (+18 rows); gaps: 3 conflicts resolved or refined, 4 new.

