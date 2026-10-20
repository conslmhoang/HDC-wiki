---
type: concept
slug: fiber-geometry
aliases: [fiber length, fiber diameter, aspect ratio, fiber reinforcement index, embedment length, critical fiber length, fiber content]
tags: [design-variable]
sources: [su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances, li1992-steady-state-multiple-cracking, yu2018-ecc-direct-tensile-review, zhang2022-hshdcc-review, gao2020-hdcc-recycled-fine-aggregate, zhao2022-ecc-tension-damage-model, deng2018-hdc-compressive-constitutive, zhong2019-ecc-freeze-thaw, mohammed2020-cr-ecc-elevated-temperature, homma2009-frcc-self-healing, kunieda2010-uhp-shcc-steel-reinforcement, ivaniuk2022-printable-shcc-design, ozbay2013-ecc-self-healing-sustained-load, wang2023-ecc-frost-damage, sui2018-uhp-ecc-flexural-fatigue, jin2019-hvfa-shcc-structural, yang2008-ecc-fiber-bridging-law]
updated: 2026-10-20
---

# Fiber Geometry & Content (length, diameter, Vf)

## Key points
- **Fiber length** ([[su2023-rubber-modified-hshdc]], PE 20 µm, 2%):
  - The maximum embedment length is L/2.
  - **6 mm PE** (3 mm maximum embedment) is below the critical length. All fibers pull out and the
    mix fails brittle (single crack), even though the PSH indices are met (p. 9–10).
  - At PR0, 12 mm and 18 mm PE give **7.1× and 9.5×** the ε of 6 mm PE (p. 9).
- **Fiber diameter / reinforcement index** ([[yang2024-hshdc-uniaxial-tension]], PE 12 mm, 2%):
  - Going from d = 40 µm to 22 µm raises the index Vf·Lf/df from 6.00 to 10.91 and raises εp
    from 0.345% to 3.839% (p. 8).
  - Fits:
    - εp = 0.61(Vf·Lf/df) − 2.45, R² 0.750
    - σp = 0.50(Vf·Lf/df) + 1.90, R² 0.770 (Fig. 8)
- **Fiber content:**
  - PE22 at 1.5 / 2.0 / 2.5%: εp 3.56 / 3.84 / 4.65% ([[yang2024-hshdc-uniaxial-tension]], Table 6).
  - UHDC at 1% / 2% PE: 4.31 / 9.45% ([[ye2021-uhdc-flexural-size-effect]], p. 3).
  - PVA optimum of 1.5 vol.% (Said 2020, as cited in [[he2024-hdc-research-advances]], p. 2).
  - 1.5% PE gave the best 3D-printed UHDC (p. 5).
- Longer PVA fibers lower f'c (as cited in [[he2024-hdc-research-advances]], p. 2).

## Conflicts & open questions
- ⚔️ Literature conflict on PVA fiber length, as cited in [[su2023-rubber-modified-hshdc]], p. 2:
  Feng et al. 2022 found longer PVA gave lower ductility; Lee et al. 2023 found 18 mm better than
  12 mm. → [[gaps]]
- A very high aspect ratio may hurt dispersion. The ingested sources have no dispersion data
  to check this. → [[fiber-dispersion]]

## Theory and further data (2026-10-16 ingest)
- **Critical fiber volume** V_f^crit ∝ (Lf/df)⁻³, so doubling Lf cuts the needed fiber by 87.5%.
  A smaller df raises σ_fc and lowers V_f^crit ([[li1992-steady-state-multiple-cracking]], Eq. 17, p. 2255, 2259).
  → [[steady-state-cracking]]
- **Tongji PE-ECC:** 3 fibers × 7 Vf (1.25–3.0%), giving Vf·Lf/df 7.5 → 18; σ_tu 10.29 → 17.86 MPa and
  ε 2.20 → 7.91%, with narrower crack spacing and width ([[yu2018-ecc-direct-tensile-review]], Fig. 2).
  The authors suggest a higher Lf/df with a lower Vf (p. 360).
  - > Synthesis: ε about 2.2% at an index of 7.5 is roughly consistent with the Yang 2024 fit
    (about 2.1%).
- **PE in HSHDCC:** typical L/d is 300–900 at 2 vol.% ([[zhang2022-hshdcc-review]], Table 3).
- **Hybrid PE + steel** (as cited in [[zhang2022-hshdcc-review]], p. 9–14):
  - At 2% total fiber, 2% PE gives 23× the ε_tu of 2% steel, and 81% higher σ_tu (Zhou 2018).
  - Adding steel narrows cracks (235 → 80 µm) and raises f'c by up to 51%.


## Round 4 evidence (2026-10-20)
### Fiber content (Vf)
| Source | Term / fiber | Vf series | Effect |
|---|---|---|---|
| [[gao2020-hdcc-recycled-fine-aggregate]] §3.3–3.4, Table 6 | PVA-HDCC 12 mm × 40 µm | 0 / 0.5 / 1.0 / 1.5 / 2.0% | no deflection hardening at 0.5%; tensile SH only at ≥ 1.5% (RFA mixes). R-HDCC ε_tp +260.6% from 0.5 to 2.0%. Fits: σ_bp/f_c = 0.036 Vf + 0.069; σ_tp/f_c = 0.025 Vf + 0.026 (Eqs. 5–6, Vf in % assumed ⚠️) |
| [[zhao2022-ecc-tension-damage-model]] Table 3 | PVA-ECC, W/B 0.28 | 1 / 1.5 / 2% | σ_p flat (3.10 / 2.96 / 3.23 MPa); ε_p 0.51 / 0.80 / 2.00%; tensile fracture energy +217% |
| [[deng2018-hdc-compressive-constitutive]] Table 3 | PVA-HDC (compression) | 1 / 1.5 / 2% | σ0 50.28 / 56.85 / 62.25 MPa; post-peak strain indices ε0.85 / ε0.5 / ε0.2 +33 / +40 / +63% (1 → 2%) |
| [[zhong2019-ecc-freeze-thaw]] §3.5, Tables 6–7 | PVA 13 mm (flexure, F–T) | 0–2% | frost resistance improves to 1.5%, slightly drops at 2.0% (dispersion); Taguchi optimum 1.5% |
| [[mohammed2020-cr-ecc-elevated-temperature]] Fig. 2 | CR-ECC (compression) | 0 / 1 / 2% | PVA a significant RSM term for f'c; optimum 2% PVA with 2.5% CR |

- ⚔️ **Vf vs peak tensile stress:** Zhao found σ_p flat from 1 to 2% PVA, while bridging models predict σ0 ∝ Vf
  ([[jin2019-hvfa-shcc-structural]], Fig. 1a; [[yang2008-ecc-fiber-bridging-law]]). The matrix differs; σ_p may be
  flaw- or rupture-controlled. → [[gaps]]

### Fiber length and size
- **Short PE (6 mm × 12 µm, 1.5 vol.%):** strain softening in a W/B 0.45 FRCC ([[homma2009-frcc-self-healing]], p. 224), but
  strain hardening in W/B 0.20 UHP-SHCC dumbbells ([[kunieda2010-uhp-shcc-steel-reinforcement]], §3.2) and in printed
  PE-SHCC (6 mm Dyneema, [[ivaniuk2022-printable-shcc-design]]). Su 2023's 6 mm × 20 µm PE was brittle
  ([[su2023-rubber-modified-hshdc]], p. 9–10).
  > Synthesis: a 6 mm PE fiber can work when it is thin (12 µm, L/d 500) and the matrix is strong enough to bond it.
  > At 20 µm (L/d 300) it fell below the critical length. Length alone does not set the outcome; the aspect ratio and the
  > matrix both matter.
- **Shorter PVA (8 mm)** is used in [[ozbay2013-ecc-self-healing-sustained-load]] ⚠️ and [[wang2023-ecc-frost-damage]];
  13 mm in [[zhong2019-ecc-freeze-thaw]]. No study isolates PVA length.
- **PE aspect ratio:** L/d 480 (25 µm) in UHP-ECC ([[sui2018-uhp-ecc-flexural-fatigue]], Table 3).
- **Hybrids:** steel + PE and PVA + steel combinations are collected in [[hybrid-fiber]].

## Related
- [[fiber-bridging]] · [[tensile-strain-capacity]] · [[pe-fiber]] · [[pva-fiber]] · [[hybrid-fiber]] · [[strain-hardening]]
