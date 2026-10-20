---
type: concept
slug: size-effect
aliases: [flexural size effect, Bažant size effect law, SEL, Weibull size effect, Type-I, Type-II]
tags: [fracture, scaling]
sources: [ye2021-uhdc-flexural-size-effect, ranade2017-hshdc-impact-resistance, li1992-steady-state-multiple-cracking, yu2018-ecc-direct-tensile-review, kunieda2010-uhp-shcc-steel-reinforcement, kanakubo2006-dfrcc-tensile-test-method, xue2023-shcc-structural-review, kanda2003-sprayed-ecc]
updated: 2026-10-20
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

## Notch sensitivity (theory) and tension size effects
- [[li1992-steady-state-multiple-cracking]] (p. 2251, Fig. 3):
  - when K̃ > K̃_crit, σ_fc depends on flaw size, so the composite is **notch-sensitive**;
  - when K̃ < K̃_crit, the composite fails at σ_ss independent of flaw size, so it is **notch-insensitive**.
  → [[steady-state-cracking]]
- **In tension:** no conclusive size effect for ECC. Geometry has an "apparent influence", attributed
  to imperfections, fiber orientation, end effects and stress singularities. A size-independent
  constitutive model is needed ([[yu2018-ecc-direct-tensile-review]], p. 348, 359).

## Tension members: a strong thickness / size effect (2026-10-20)
| Source | Material | Small specimen | Large specimen | Change |
|---|---|---|---|---|
| [[kunieda2010-uhp-shcc-steel-reinforcement]] §4.1, Table 3, Fig. 5 | UHP-SHCC (PE 1.5%, f'c 95 MPa) | 13 × 30 mm dumbbell: ε 1.5%, strain hardening | 50 × 200 × 900 mm unreinforced member: ε 0.23–0.24%, brittle | ε about −85%, σ about −30% |
| [[kanakubo2006-dfrcc-tensile-test-method]] Tables 6–9 | PVA-DFRCC, same mix | 30 × 13 mm plate: ε 2.70% | Ø70 dogbone 0.07%; Ø100 cylinder 0.32% | > 30× (shape, casting and end conditions also differ) |

- **Mechanisms proposed** ([[kunieda2010-uhp-shcc-steel-reinforcement]], §2, Fig. 2):
  - strain capacity is set by the overlap between the matrix-cracking-strength and bridging-strength
    distributions along the member; a larger volume widens the bridging distribution and lowers its mean
    (weakest-link view);
  - fiber orientation is about 2-D in 13 mm dumbbells but 3-D in 50 mm members. → [[fiber-dispersion]]
- Small reinforcement (D6, ρs 0.3%) restores distributed cracking and 1.5–1.8% strain (Table 3).
- Similar member-level losses: thin bonded strengthening layers over a substrate crack do not reach dogbone
  ductility ([[xue2023-shcc-structural-review]], Section 4.1.2); cut-outs from 150 mm thick sprayed ECC lose
  deflection capacity vs thin moulded prisms ([[kanda2003-sprayed-ecc]], Fig. 11 ⚠️).

> Synthesis: in **flexure** UHDC-2 shows no size effect up to 150 mm (Ye 2021), but in **direct tension**
> PE UHP-SHCC shows a large thickness effect between 13 and 50 mm (Kunieda 2010). The two are different modes
> and materials; the tension result matters most for design because dogbone ε_tu feeds the constitutive
> models. → [[tensile-strain-capacity]], [[tensile-constitutive-model]]

- ⚔️ "Thickness 13 / 30 / 50 mm has negligible effect" for PVA-ECC (Rokugo 2007, as cited in
  [[yu2018-ecc-direct-tensile-review]], p. 348) vs −85% strain at 50 mm for PE UHP-SHCC
  ([[kunieda2010-uhp-shcc-steel-reinforcement]]). Fiber type, matrix strength and specimen width differ. → [[gaps]]

## Related
- [[flexural-strength]] · [[notched-beam-three-point-bending]] · [[fracture-process-zone]] · [[uhdc]] · [[tensile-strain-capacity]]
