---
type: concept
slug: fiber-geometry
aliases: [fiber length, fiber diameter, aspect ratio, fiber reinforcement index, embedment length, critical fiber length, fiber content]
tags: [design-variable]
sources: [su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances]
updated: 2026-10-06
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

## Related
- [[fiber-bridging]] · [[tensile-strain-capacity]] · [[pe-fiber]] · [[strain-hardening]]
