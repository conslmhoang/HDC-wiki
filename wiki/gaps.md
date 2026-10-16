---
type: hub
updated: 2026-10-16
---

# Research Gaps, Conflicts & Open Questions

This page feeds the "Research gaps and future directions" chapter of [[review-outline]].

## ⚔️ Conflicts between sources
| Topic | Source A says | Source B says | Possible reason | Status |
|---|---|---|---|---|
| Meaning of "HDC" / "HSHDC" | HSHDC = Michigan PE + VHSC matrix, 166 MPa, heat-cured ([[ranade2017-hshdc-impact-resistance]]) | HSHDC = Xi'an ambient-cured, about 100 MPa ([[yang2024-hshdc-uniaxial-tension]]); GDUT ([[su2023-rubber-modified-hshdc]]); umbrella HSHDCC > 100 MPa and > 3% ([[zhang2022-hshdcc-review]]) | Same name used by different groups | open: always state the lineage, see [[terminology-hdc-ecc-shcc]] |
| Class thresholds | HSHDCC: > 100 MPa, > 3% ([[zhang2022-hshdcc-review]]) | > 55 MPa and > 4%, or > 80 MPa and > 2% (other reviews, as cited there); normal HDC 30–80 MPa ([[su2023-rubber-modified-hshdc]]) vs normal ECC 40–70 MPa ([[zhang2022-hshdcc-review]]) | No standard | open |
| HDC vs ECC | "HDC stands for ECC" (p. 2) | "HDC developed on the basis of ECC" (p. 10), both in [[he2024-hdc-research-advances]] | Internal inconsistency | treat HDC ≈ ECC/SHCC |
| Quasi-static ε_tu of Michigan HSHDC | 3.4% (as quoted in [[ranade2017-hshdc-impact-resistance]]) | 4.2% ([[ranade2015-hshdc-tensile-rate-effects]]); 3.5% for the 2011 version ([[zhang2022-hshdcc-review]]) | Batch and fiber version (38 vs 28 µm) | open: report 3.4–4.2% |
| Strength–ductility trade-off | ε_tu falls as f'c rises across the primary sources (UHDC 9.45% → Michigan 3.4–4.2%) | f'c > 210 MPa with ε > 5%, and 122 MPa with 8.5% (as cited in [[zhang2022-hshdcc-review]]) | Interface and fiber design, not f'c alone | resolved: the trade-off is **not fundamental** |
| PSH criteria vs behaviour | 6 mm PE mixes meet both PSH thresholds but fail brittle ([[su2023-rubber-modified-hshdc]]) | In PVA-ECC the energy index (> 3) predicts saturation well ([[li2002-pva-ecc-interface-tailoring]]) | Missing flaw-size and embedment terms ([[li1992-steady-state-multiple-cracking]]) | open |
| β of ECC | about 0.6 (Wang & Li 2007, as cited in [[ranade2015-hshdc-tensile-rate-effects]]) | 1.15–2.31 ([[li2002-pva-ecc-interface-tailoring]]) | Different fiber, oiling and matrix | refinement |
| PVA-ECC ε vs strain rate (as cited) | decreases (Yang & Li 2014; Mechtcherine) | no significant change (Boshoff & van Zijl 2007), both in [[yu2018-ecc-direct-tensile-review]] | Test method and rate range | open |
| PVA failure mode at high rate (as cited) | pull-out dominates in composite tests | rupture dominates in single-fiber tests ([[yu2018-ecc-direct-tensile-review]], p. 350) | Scale effect | open |
| Shrinkage vs W/B (as cited) | rises with W/B (Gao 2018) | falls with W/B (Ye 2019), both in [[ma2021-ecc-durability-review]] | Strength class | open |
| Freeze–thaw citation | Yun 2013, hybrid PVA+PE ([[he2024-hdc-research-advances]]) | Yun 2011, PVA loses more ε than PE ([[ma2021-ecc-durability-review]]) | Possibly two papers or a mis-citation | verify |
| PE fiber melting point | about 150 °C ([[ranade2017-hshdc-impact-resistance]]; [[yu2018-ecc-direct-tensile-review]]) | 124–138 °C ([[he2024-hdc-research-advances]]); 135–145 °C ([[su2023-rubber-modified-hshdc]]) | Different products | minor |
| PVA fiber length effect (as cited) | longer gives lower ductility (Feng 2022) | 18 mm better than 12 mm (Lee 2023), both in [[su2023-rubber-modified-hshdc]] | Matrix and test | open |
| UHPC flexural size effect (as cited) | significant | reduced, both in [[ye2021-uhdc-flexural-size-effect]] | Size range and method | open |

## Under-studied areas
- **Durability of HSHDC/UHDC.** All durability data concern normal ECC. Reviews explicitly flag that
  high-strength / high-ductility ECC lacks data ([[ma2021-ecc-durability-review]], p. 9–10).
  → [[durability]]
- **Crack width of PE-based HSHDC** (80–200 µm) exceeds the thresholds for chloride (55–90 µm) and
  fast self-healing (< 60 µm). PVA-ECC (43–88 µm) does not. → [[crack-width]], [[self-healing]]
- **Fire:** PE-ECC loses strain hardening between 100 and 140 °C; PVA-ECC at about 150–200 °C. No fire design data. → [[high-temperature-behaviour]]
- **Chinese PVA-HDC primary data** (Deng group, Xi'an) for normal-strength HDC are still missing.
  The PVA reference is Michigan ECC. → [[pva-fiber]]
- **No standard** test method or definition for HDC tension and flexure ([[zhang2022-hshdcc-review]];
  [[yu2018-ecc-direct-tensile-review]]). → [[dogbone-uniaxial-tension]]
- **No field deployment** of HSHDCC ([[zhang2022-hshdcc-review]], p. 2). Structural applications are
  known only second-hand. → [[masonry-wall-retrofit]], [[rc-member-strengthening]]
- **Long-term ageing:** almost all data are at 28 d. Ductility and self-healing fall with age.
  → [[durability]]
- **Extreme rates** above 10 s⁻¹ for HSHDC, and reinforced members under impact. → [[strain-rate-effects]], [[impact-resistance]]
- **Interface data** exist only for the Michigan PE matrix and the Michigan PVA-ECC. → [[fiber-matrix-interface]]
- **Effect of curing regime** on PSH indices and ductility is unclear ([[zhang2022-hshdcc-review]]). → [[heat-curing]]
- **Size-independent tensile constitutive model** ([[yu2018-ecc-direct-tensile-review]]). → [[size-effect]]

## Open questions
- Can PSH indices be extended to include embedment length and flaw size (as in Li & Leung 1992)?
- Can PE-HSHDC crack widths be brought below 60–80 µm, e.g. with hybrid steel, SF or rubber, to gain
  self-healing and chloride resistance?
- Does ambient-cured HSHDC keep its ductility after long-term ageing?
