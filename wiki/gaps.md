---
type: hub
updated: 2026-10-06
---

# Research Gaps, Conflicts & Open Questions

This page feeds the "Research gaps and future directions" chapter of [[review-outline]].

## ⚔️ Conflicts between sources
| Topic | Source A says | Source B says | Possible reason | Status |
|---|---|---|---|---|
| Meaning of "HDC" / "HSHDC" | HSHDC = Michigan PE + VHSC matrix, 166 MPa, heat-cured ([[ranade2017-hshdc-impact-resistance]]) | HSHDC = Xi'an ambient-cured, about 100 MPa, PE or PVA ([[yang2024-hshdc-uniaxial-tension]]); GDUT HSHDC ([[su2023-rubber-modified-hshdc]]) | Same name used by different groups | open: always state the lineage, see [[terminology-hdc-ecc-shcc]] |
| HDC vs ECC | "HDC stands for ECC" (p. 2) | "HDC developed on the basis of ECC" (p. 10), both in [[he2024-hdc-research-advances]] | Internal inconsistency in the review | treat HDC ≈ ECC/SHCC |
| Quasi-static ε_tu of Michigan HSHDC | 3.4% (as quoted in [[ranade2017-hshdc-impact-resistance]]) | 4.2% ([[ranade2015-hshdc-tensile-rate-effects]], 10⁻⁴ s⁻¹) | Batch variability | open: report a range of 3.4–4.2% |
| PSH criteria vs observed behaviour | 6 mm PE mixes meet PSH > 1.2 and > 3 | …but fail brittle ([[su2023-rubber-modified-hshdc]]) | Fiber embedment length is not in the indices | open: criteria are necessary, not sufficient |
| PE fiber melting point | about 150 °C ([[ranade2017-hshdc-impact-resistance]]) | 124–138 °C ([[he2024-hdc-research-advances]]); 135–145 °C ([[su2023-rubber-modified-hshdc]]) | Different products | minor |
| PVA fiber length effect (as cited) | Longer gives lower ductility (Feng 2022) | 18 mm better than 12 mm (Lee 2023), both in [[su2023-rubber-modified-hshdc]] | Matrix and test differences | open |
| UHPC flexural size effect (as cited) | Significant (refs 38–39) | Reduced (refs 40–42), both in [[ye2021-uhdc-flexural-size-effect]] | Size range and test method | open |

## Under-studied areas
- **Classic PVA-HDC in a normal-strength matrix:** no primary source yet. This is the most important
  gap for a review about Chinese HDC. → [[pva-fiber]]
- **No standard definition of HDC.** Thresholds are uncited (3–5% / 3–7 MPa) and no JGJ/T or CECS
  standard is ingested. → [[terminology-hdc-ecc-shcc]]
- **Durability:** no primary data for any HSHDC or UHDC. Crack widths in PE-HSHDC (80–200 µm) exceed
  chloride thresholds (55–90 µm). → [[durability]], [[crack-width]]
- **Fire and high temperature:** PE melts at about 124–150 °C. → [[high-temperature-behaviour]]
- **Extreme rates:** nothing above 10 s⁻¹, and no reinforced members under impact or blast.
  → [[strain-rate-effects]], [[impact-resistance]]
- **Interface data** (τ0, β) exist only for the Michigan matrix. → [[fiber-matrix-interface]]
- **Size effect at structural scale:** tests only reach 150 mm. → [[size-effect]]
- **Bond between HSHDC and existing concrete** for strengthening ([[yang2024-hshdc-uniaxial-tension]], p. 14).
  → [[rc-member-strengthening]]
- **Tension test methods are not standardised:** gauge length, section and rate differ.
  → [[dogbone-uniaxial-tension]]
- **Structural applications** (masonry retrofit, RC strengthening, 3D printing) are known only
  second-hand through the review. → [[masonry-wall-retrofit]]
- **Cross-lineage comparison:** no study compares Michigan, GDUT, Xi'an and Tongji materials directly.
  → [[hshdc]]

## Open questions
- Is the strength–ductility trade-off (UHDC 9.45% at 37 MPa → Michigan 3.4–4.2% at 166 MPa) a
  fundamental limit, or can it be overcome with fiber or interface tailoring?
- Can PSH indices be extended to include embedment length?
- Does rubber or FA-based ductility enhancement survive long-term exposure?
