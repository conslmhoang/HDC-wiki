---
type: test-method
slug: digital-image-correlation
aliases: [DIC, crack counting]
tags: [measurement]
sources: [su2023-rubber-modified-hshdc, ye2021-uhdc-flexural-size-effect, chavesfigueiredo2020-printed-shcc, sui2018-uhp-ecc-flexural-fatigue]
updated: 2026-10-20
---

# Digital Image Correlation (DIC)

## Key points
- **Crack counting** on dumbbells: resolution 0.03 mm/px. A crack is counted when the displacement
  jump exceeds 9 µm ([[su2023-rubber-modified-hshdc]], p. 7, Fig. 10). → [[multiple-cracking]]
- **Crack-pattern evolution** in notched beams ([[ye2021-uhdc-flexural-size-effect]]).

## Setups compared
| Source | Test | Software | Resolution / settings | Use |
|---|---|---|---|---|
| [[su2023-rubber-modified-hshdc]] | dumbbell tension | n.r. | 0.03 mm/px; crack if jump > 9 µm | crack counting |
| [[ye2021-uhdc-flexural-size-effect]] | notched 3PB | n.r. | n.r. | crack-pattern evolution |
| [[chavesfigueiredo2020-printed-shcc]] (Section 2.2.4) | tension of printed SHCC plates | Ncorr2 | subset radius 57, about 48 µm/px, 0.5 Hz | crack pattern parallel / perpendicular to print path |
| [[sui2018-uhp-ecc-flexural-fatigue]] (Figs. 6b, 9, 14) | 4-point bending, static and fatigue | VIC-3D | n.r. | crack sequencing: first crack at 58% of peak, 18 cracks at 72%, saturation near span/30 (static) |

## Conflicts & open questions
- Crack-detection thresholds differ (9 µm in Su 2023; not stated elsewhere), so crack counts are not
  directly comparable.

## Related
- [[multiple-cracking]] · [[dogbone-uniaxial-tension]] · [[four-point-bending-inverse-analysis]] ·
  [[3d-printed-hdc]] · [[fatigue]]
