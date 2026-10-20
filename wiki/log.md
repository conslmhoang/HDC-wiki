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


## 2026-10-21 — ingest new — 34 sources (round 4, toward the 50-paper target)
- **How sources were obtained:**
  - Wiley/Hindawi PDFs (incl. the 3 Deng/XAUAT papers) downloaded through the human's Chrome with university access.
  - 13 JACT PDFs from J-STAGE.
  - 18 MDPI papers as full-text XML from Europe PMC (CC BY).
  - ScienceDirect was blocked by a CAPTCHA loop (not bypassed), so the 10 ScienceDirect/ACI papers on the reading
    list are still missing.
- **New sources (34):**
  - Chinese HDC/HDCC and XAUAT: deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive,
    deng2018-hdc-short-columns, chai2019-hdcc-freeze-thaw-carbonation-flexure, gao2020-hdcc-recycled-fine-aggregate.
  - Korea Univ. HSDC/NSHSDC: yuan2020-nshsdc-beam-strengthening, lee2021-hsdc-wall-emi-impact.
  - JACT: kanda2003-sprayed-ecc, kanakubo2006-dfrcc-tensile-test-method, kunieda2006-hpfrcc-japan-applications,
    qian2007-shcc-inverse-tensile-strain, homma2009-frcc-self-healing, kunieda2010-uhp-shcc-steel-reinforcement,
    vanzijl2010-shcc-durability, mechtcherine2011-shcc-high-strain-rate, ozbay2013-ecc-self-healing-sustained-load,
    paul2014-r-shcc-chloride-corrosion, wang2023-ecc-frost-damage, zhou2023-hsecc-elevated-temperature.
  - MDPI and others: herbert2013-ecc-self-healing-natural-environment, sui2018-uhp-ecc-flexural-fatigue,
    jin2019-hvfa-shcc-structural, sun2019-modified-pva-fiber-ecc, wang2019-rc-beam-ecc-shear-strengthening,
    zhong2019-ecc-freeze-thaw, chavesfigueiredo2020-printed-shcc, mohammed2020-cr-ecc-elevated-temperature,
    bu2022-ecc-chloride-crack-width, ivaniuk2022-printable-shcc-design, shumuye2022-slag-fa-pe-ecc,
    tabrizikahou2022-masonry-ecc-sma-retrofit, zhang2022-ecc-carbonation-sustained-load,
    zhao2022-ecc-tension-damage-model, xue2023-shcc-structural-review.
- **New pages (10):**
  - properties: freeze-thaw, carbonation, chloride-and-corrosion, compressive-constitutive-model, shear-behaviour
  - materials: recycled-fine-aggregate, hybrid-fiber, viscosity-modifying-admixtures
  - test methods: four-point-bending-inverse-analysis
  - concepts: interface-bond
- **Restructured/rewritten:** durability (now a hub), crack-width; about 40 other topic pages updated by the
  theory, materials, mechanical, durability and tests-apps integration groups.
- **Key corrections:**
  - Chloride crack-width threshold is **exposure-dependent**: 100 µm ≈ uncracked under immersion (Bu 2022), but
    50–100 µm (and < 50 µm) cracks carry chloride to rebar within hours under wet–dry cycles (Paul 2014); the
    55–80 µm value is second-hand.
  - Repair page: field crack-width data now exist, but only second-hand (Kunieda & Rokugo 2006: ≤ 50 µm at
    10 months, ≤ 120 µm at 24 months on an ASR wall).
  - PVA melting: onset 230 °C by primary TG (Zhou 2023); "273 °C" has no support.
  - Fourth HSHDC-type lineage: Korea Univ. steel + PE hybrid (HSDC/NSHSDC, ≈ 122–123 MPa); its tensile ductility
    is not shown in the ingested papers.
  - Kanakubo 2006 JCI round robin: the same PVA-DFRCC gives 2.70% strain at peak (thin plate) down to 0.07%
    (Ø70 dogbone); thickness effects conflict with Rokugo 2007 (as cited). Bending inverse methods depend on the
    chosen tension reference.
  - "ε_tu" naming: some papers report post-peak strain; the wiki compares strain at peak only.
  - Several "ECC/HDC" papers report no tension test (labelled on their source pages, not relabelled).
- **Datasets:** +202 rows: mix-designs 22 → 91 (+69), mechanical-results 54 → 180 (+126),
  micromechanical-parameters 17 → 24 (+7). Fatigue S–N, field crack widths and member results stay on source pages.
- **gaps:** 51 conflict rows (was 19): 32 new after merging duplicates across groups (e.g. chloride threshold,
  Kanakubo vs Rokugo thickness effect, JSCE 2008 vs JC/T 2461, delamination, printed SHCC interlayer and fiber
  orientation); 3 rows refined (strain-rate ε and failure mode by mechtcherine2011; F-T citation note); PVA
  melting partly resolved. Under-studied areas rewritten for the 50-source corpus.
- Updated index (34 sources + 10 pages, grouped by lineage) and review-outline (scope 50 papers).

## 2026-10-21 — ingest new — 10 sources (round 5, reaching 60)
- **How sources were obtained:** the human downloaded 9 ScienceDirect PDFs by hand (a CAPTCHA blocked automated
  download and was not bypassed). Choi 2016 was added as a replacement for Wang 2007 (ACI), which is paywalled.
- **New sources (10):**
  - XAUAT structures and TR-HDC: deng2017-rc-column-hdc-jacket, deng2019-urm-shaking-table-hdc,
    deng2020-aac-wall-hdc-retrofit, li2021-hdc-beam-shear, zhang2022-hdc-basalt-textile-tension.
  - Durability and temperature: yang2009-ecc-self-healing-wet-dry, lepech2009-ecc-water-permeability,
    yun2013-shcc-freeze-thaw, pourfalah2018-ecc-high-temperature.
  - Cementless composite: choi2016-pe-alkali-activated-slag-composite.
- **New pages (2):** materials/textile-reinforced-hdc, materials/alkali-activated-binder.
- **Updated:** about 40 topic pages by the structures and durability-materials integration groups (applications,
  shear, tension, crack width, self-healing, permeability, freeze–thaw, high temperature, fibres, binders, W/B).
- **Key corrections:**
  - Permeability: reinforced mortar at ≈ 500 µm is **4.46 × 10⁻⁴ m/s** (Lepech & Li 2009, Table 5), not 10⁻⁵ m/s as
    quoted via ma2021; 10⁻⁵ (2.58 × 10⁻⁵) is the 300 µm value. The "0.10–0.15 mm" threshold attributed to Lepech & Li
    2009 is a mis-citation; their 100 µm is a design target from concrete (Wang 1997), not measured on ECC.
  - Healing thresholds: Yang 2009's < 50 / 50–150 / > 150 µm limits were measured on a 0.5% PVA tension-softening
    mortar, not ECC; the "< 60 µm" value is Reinhardt & Jooss (via ma2021), not Yang 2009.
  - Yun citation resolved: Yun 2013 (Compos. B 52) and Yun 2011 (Cold Reg. Sci. Technol. 67) are two different papers.
  - "Deng & Zhang 2018" row: he2024 most likely refers to Deng, Zhang & Li 2018 (Eng. Struct. 160, ECC-jacketed short
    columns, not ingested), not to deng2018-hdc-short-columns; probably resolved.
  - XAUAT PVA-HDC strain spread: ≈ 3.0% (Japanese PVA, Deng 2017) vs ≈ 1.0% (Deng 2018, 2019; Li 2021) vs
    0.34–0.45% (plain HDC in Zhang 2022, below the 0.5% bar), same nominal fibre; raised by both groups, merged into
    one conflict row.
  - Deng 2019 shake-table test is now primary; masonry retrofit and RC column jacketing now have primary data.
- **Datasets:** +60 rows: mix-designs 91 → 113 (+22), mechanical-results 180 → 216 (+36),
  micromechanical-parameters 24 → 26 (+2). Dataset conflicts: M45 HRWR 7.51 (lepech2009) vs 17 kg/m³ (yang2009);
  li2021 σ_tu 5.83 vs 5.68 MPa (internal).
- **gaps:** 64 conflict rows (was 51): 13 new after merging duplicates (XAUAT strain spread, permeability at 500 µm,
  0.10–0.15 mm mis-citation, origin of 100 µm, static vs flowing water, ε_tu and stiffness after F-T, code
  conservatism, shear design philosophy, PVA modulus, PVA at 200 °C, M45 HRWR, li2021 σ_tu); 12 rows updated, incl.
  Yun 2011/2013 resolved and Deng & Zhang 2018 probably resolved. Under-studied areas updated for the 60-source corpus.
- Updated index (10 sources + 2 pages; new groups for XAUAT structures and cementless composites) and review-outline
  (scope 60 papers; applications chapter now ✅).
