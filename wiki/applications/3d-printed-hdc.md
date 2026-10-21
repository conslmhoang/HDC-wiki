---
type: application
slug: 3d-printed-hdc
aliases: [3DP-UHDC, 3D printing, additive manufacturing, printable SHCC, printed ECC, 3DCP]
tags: [application, construction, 3d-printing]
sources: [he2024-hdc-research-advances, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design]
updated: 2026-10-21
---

# 3D-Printed HDC / SHCC / UHDC

> Status (2026-10-20): two primary printed-SHCC studies (TU Delft/Eindhoven PVA-SHCC; TU Dresden PE-SHCC) plus
> review data on Chinese 3DP-UHDC.

## Primary studies compared
| | [[chavesfigueiredo2020-printed-shcc]] | [[ivaniuk2022-printable-shcc-design]] |
|---|---|---|
| Term | SHCC (PVA) | printable SHCC (PE) |
| Fibre | PVA, 2 mixes (X, Y) | PE (Dyneema) 6 mm, 1.5 vol.% |
| Rheology modifiers | HPMC | starch + cellulose ether (SE-CE) vs Ref → [[viscosity-modifying-admixtures]] |
| Printing | TU/e gantry, layers 10 × 50 mm, 100 mm/s (Section 2.1) | ACDC project: printed contours of shell modules with SCC infill and carbon-yarn mesh (Fig. 1) |
| Tension along print path | X: σ_tu 2.4 MPa, **ε 0.26%**; Y: 1.64 MPa, **0.15%** (35 d, at peak) (Table 5, p. 12) | σ_tu 5.4 (Ref) / 4.1 MPa (SE-CE), **ε 2–3%** (text, p. 14; ≈ strain at onset of softening per Fig. 17, p. 15; not defined ⚠️); first crack ≈ 3 MPa (read from Fig. 17) |
| Tension ⟂ in-plane | X still strain-hardens: 2.41 MPa, 0.31% (Table 5) | n.r. |
| Across layers | brittle, no strain hardening, but interface strength **≥** bulk first-crack strength ("comparable to or slightly more", Section 3.5; "in the same range", Conclusions p. 20); bond ≈ 2.4 (X2T), 1.9 (X2TT), 1.4 (Y2T), 1.2 MPa (Y2TT) (read from Fig. 14, p. 16) | 3PB flexure lower across interlayer: 18.5 (D3) vs 22.0 MPa (D1), 28 d Ref (Table 3) |
| Compression anisotropy | nearly isotropic, 5–15%, close to cast (Table 2, p. 8) | lowest parallel to print direction: 73.0 vs 82–83 MPa, 28 d Ref (Table 2) |
| Fibre orientation | mainly **diagonal** to print path (µCT): histogram peaks ≈ 40° (≈ 9% X, ≈ 8% Y) and ≈ 170°, minimum ≈ 90° (≈ 1.5–2%), 0/180° ≈ 2.5–3.5% (read from Fig. 17, p. 19) | assumed predominantly along print direction (citing Li et al. 2020) |
| Other | layer interval 3 vs 36 min: no significant effect on interface; interface has the lowest air-void content (void area ≈ 12–14% in X layers vs ≈ 10% at the X interface; Y ≈ 2–7%; Figs. 15–16, pp. 17–18); thicker printed beams → fewer cracks, lower deflection at MOR: X ≈ 2.75 (1 layer) → ≈ 1.0 mm (3–4 layers), Y ≈ 1.6 → ≈ 1.0–1.25 mm, while MOR stays ≈ 7.0–7.5 (X) / ≈ 3.3–3.9 MPa (Y), 28 d (read from Fig. 6, p. 11) → [[flexural-strength]] | surface roughness Sa 772 µm (Ref) vs 411 µm (SE-CE) (Fig. 15) |

- Chaves Figueiredo: printed SHCC lost strain capacity relative to the cast originals; the authors blame high air
  voids, lower water and HPMC (Sections 3.4.1, 3.6). HPMC = 0.30% (X) and 0.40% (Y) of total dry solids (computed in the
  source page; matches the "VA3"/"VA4" names). The fibre L/d for this study's mixes is not reported (p. 2 quotes 12 mm × 40 µm
  only for a cited mix). Strain ≤ 0.31% is far below the ECC > 3% convention and below
  the JC/T 2461 bar of 0.5% (as cited in [[chai2023-hdc-ambient-temperature]]), although multiple cracking and strain
  hardening occur. → [[terminology-hdc-ecc-shcc]]
- Test methods: sawn one-layer plates with glued ends, DIC (Ncorr2) ([[chavesfigueiredo2020-printed-shcc]], Section 2.2.4);
  printed prisms embedded in dumbbell formwork with freshly cast ends ([[ivaniuk2022-printable-shcc-design]], Section 2.3.3).
  → [[dogbone-uniaxial-tension]], [[digital-image-correlation]]
- As cited in [[chavesfigueiredo2020-printed-shcc]] (Section 1): Soltan & Li 2018 printable ECC about 4% strain with HPMC
  and CAC; Ogura 2018 HDPE 0.3–1.5 vol.% printed SHCC; Zhu 2019 printable PE-ECC with sulphoaluminate cement.

## Chinese 3DP-UHDC (as cited in [[he2024-hdc-research-advances]], p. 4–5)
- 3DP-UHDC performed best at 1.5% PE (Ye et al. 2021, as cited).
- Anisotropy is quantified with an index (Eqs. 1–2 in the review).
- ⚠️ The review's sentence about compressive strength of 3DP-UHDC contradicts itself.
- **Stated gaps** (p. 20–21):
  - anisotropy and interlayer bond;
  - bionic and special-shaped components (bamboo-like columns, honeycomb panels);
  - shotcrete printing.

> Synthesis: printed PE-SHCC (2–3%) reaches roughly 10× the strain of printed PVA-SHCC (0.15–0.31%). Fibre type,
> matrix strength and the rheology package differ, so the gap cannot be assigned to one factor. Whether the
> interlayer is the weak plane depends on the study and test (direct tension of the interface vs 3PB across layers).

## Conflicts & open questions
- ⚔️ **Interlayer weakness:** interface ≥ bulk first-crack strength ([[chavesfigueiredo2020-printed-shcc]], Section 3.5)
  vs weaker across layers in flexure ([[ivaniuk2022-printable-shcc-design]], Table 3; also Wolfs 2019 and Feng 2015, as
  cited by Chaves Figueiredo). Different mix, nozzle and test. → [[gaps]], [[interface-bond]]
- ⚔️ **Fibre orientation:** measured mainly diagonal, peaks ≈ 40° / ≈ 170° ([[chavesfigueiredo2020-printed-shcc]], Fig. 17, p. 19) vs assumed along
  print direction ([[ivaniuk2022-printable-shcc-design]]; earlier printing papers cited by Chaves Figueiredo). → [[fiber-dispersion]]
- Refinement: Ivaniuk cites Chaves Figueiredo 2020 for "reduced compressive strength in the direction of printing",
  but Chaves Figueiredo's Table 2 shows only 5–15% (within SD for X).
- Stated gaps: ductile composites for thick printed elements, reinforcement compatible with 3DCP
  ([[chavesfigueiredo2020-printed-shcc]], Conclusions, Section 1); adhesiveness tests free of bleeding effects and the
  effect of starch / cellulose ether on shrinkage ([[ivaniuk2022-printable-shcc-design]], Section 3.1.3, Conclusions).

## Related
- [[uhdc]] · [[unreinforced-hdc-structures]] · [[fiber-dispersion]] · [[fresh-properties]] · [[viscosity-modifying-admixtures]] · [[pe-fiber]] · [[pva-fiber]]
