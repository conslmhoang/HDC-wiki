---
type: concept
slug: size-effect
aliases: [flexural size effect, Bažant size effect law, SEL, Weibull size effect, Type-I, Type-II]
tags: [fracture, scaling]
sources: [ye2021-uhdc-flexural-size-effect, ranade2017-hshdc-impact-resistance]
updated: 2026-10-06
---

# Size Effect

## Definition
Nominal strength changes with specimen or member size. Two families of theory are described
([[ye2021-uhdc-flexural-size-effect]], p. 1–2):
- **Weibull** (statistical; Type-I, unnotched members).
- **Bažant SEL** (energetic; Type-II, notched members):
  - σn = B·f′t / √(1 + β), with β = D/D0
  - β < 0.1 means ductile (plastic limit); β > 10 means brittle (LEFM).

## Quantitative evidence
SEL fits, notched three-point bending, d = 40–150 mm ([[ye2021-uhdc-flexural-size-effect]], Table 5):

| Material | α (notch/depth) | B | D0 (mm) | Applicability |
|---|---|---|---|---|
| NC (fiber-free mortar) | 0.23 / 0.10 | 18.57 / 9.76 | 5.80 / 52.50 | SEL holds |
| UHDC-1 (1% PE) | 0.23 / 0.10 | 35.36 / 18.90 | 11.40 / 70.00 | SEL holds |
| UHDC-2 (2% PE) | 0.23 / 0.10 | — | **−620 / −675** | **SEL not applicable** (β < 0) |

- UHDC-2 keeps f_n at about 20 MPa at all sizes and notch depths (Table 3).
- The authors suggest a Type-I (Weibull) approach instead.
- Fiber bridging removes the flexural size effect (as summarised in [[he2024-hdc-research-advances]], p. 7–8).
- Tension specimens of FR-UHPC also show a size effect: a 76 × 76 mm dogbone gave σ_tu 7.6 MPa and
  ε 0.09%, against 11.2 MPa and 0.12% for the standard dogbone
  ([[ranade2017-hshdc-impact-resistance]], p. 27). → [[uhpc-vhsc]]

## Conflicts & open questions
- ⚔️ UHPC flexural size effect is "significant" in refs [38, 39] but "reduced" in refs [40–42]
  (as cited in [[ye2021-uhdc-flexural-size-effect]], p. 3). Lepech & Li 2004 found it inappreciable
  for PVA-ECC.
- Sizes tested only reach 150 mm. A size effect may appear in UHDC at metre scale (stated, p. 9). → [[gaps]]

## Related
- [[flexural-strength]] · [[notched-beam-three-point-bending]] · [[fracture-process-zone]] · [[uhdc]]
