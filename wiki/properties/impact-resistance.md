---
type: property
slug: impact-resistance
aliases: [drop-weight impact, repeated impact, punching resistance, peak contact force, PCF]
tags: [dynamic, extreme-loading]
sources: [ranade2017-hshdc-impact-resistance, he2024-hdc-research-advances, lee2021-hsdc-wall-emi-impact, mechtcherine2011-shcc-high-strain-rate, xue2023-shcc-structural-review]
updated: 2026-10-20
---

# Impact Resistance

## Quantitative evidence
Unreinforced 300 × 300 × 25 mm slabs, 16.04 kg drop weight, 75 mm head, up to 20 impacts,
2 slabs per case ([[ranade2017-hshdc-impact-resistance]], Table 3–4, p. 28–31):

| Velocity (m/s) | HSHDC | Cor-Tuf (FR-UHPC) | First-impact PCF (kN), HSHDC / Cor-Tuf |
|---|---|---|---|
| 2.30 | survived 20 impacts | survived | 57 / 64 |
| 3.25 | survived 20; PCF about constant | flexural failure before 20 (one slab survived with low PCF) | 77 / 87 |
| 4.60 | survived 20 | flexural failure | 103 (the text says about 110 ⚠️) / 105 |

- **50 mm head:** Cor-Tuf failed by punching shear at impact 15. HSHDC showed no punching (p. 30).
- **Damage pattern:** HSHDC showed fine radial cracks and almost no spalling. Cor-Tuf formed 4
  yield-line cracks, spalled, and broke into 4 pieces. → [[multiple-cracking]]
- **FE model** (LS-Dyna): displacement error below 13%; PCF over-predicted by 34–75%; impulse matches
  (Table 4). → [[tensile-constitutive-model]]
- **Moderate-velocity impact** gives strain rates of about 0.1–10 s⁻¹ (stated, not measured, p. 26).
  → [[strain-rate-effects]]
- **EDGC tensile impact:** 8 mm PVA outperformed 13 mm PVA (as cited in
  [[he2024-hdc-research-advances]], p. 9).

> Synthesis: In these tests, the first-impact peak force is similar for both materials, but
> **damage tolerance** (repeated impacts, no punching or spalling) comes from tensile ductility,
> not from compressive strength.

## Strengthening skins on concrete panels ([[lee2021-hsdc-wall-emi-impact]])
Korea Univ. "HSDC" (hybrid steel + PE fiber, 1.5 vol.%, f'c about 122–123 MPa, σ_t 9.7 MPa, room-cured;
strain hardening not shown in this paper ⚠️) as 5 / 10 / 20 mm layers on 100 mm NC panels; 100 kg drop
weight, height 200 mm + 100 mm per blow (§3.2.1, Figs. 8–11):

| Panel | Layers | Result |
|---|---|---|
| H5S / H10S / H20S | single (one face) | failed at blow 2 / 4–5 / 4–5 by scabbing of the unstrengthened bottom face |
| H5D / H10D / H20D | double (both faces) | H20D total reaction force 2.2× H5D and 1.6× H10D |

- Total imparted energy to failure rises with HSDC thickness; H20D > 5× H5S (Fig. 11).
- Crack widths in H20D: about 0.05 mm after blow 1, 0.70 / 1.10 mm after blows 4 / 5; H5D and H10D 5.0 / 5.5 mm
  (crack-width units printed inconsistently ⚠️). → [[crack-width]]
- These are composite panels with HDC-type skins, not reinforced members; they partly address the
  "members under impact" gap.

## As cited
- SHCC under projectile impact: nearly no scabbing or spalling and better energy absorption than NSC/HSC
  (Maalej 2005, as cited in [[mechtcherine2011-shcc-high-strain-rate]], p. 52). The primary high-rate
  tension data of that paper (10–50 s⁻¹) are on [[strain-rate-effects]].
- An SHCC layer improves RC slab impact resistance (Mahmoud 2020, as cited in [[xue2023-shcc-structural-review]], Table 1).

> Synthesis: with Lee 2021, the "damage tolerance from tensile ductility" reading now also holds for
> HDC-type skins on ordinary concrete, but only when **both faces** are covered: a single
> layer did not prevent scabbing of the unstrengthened bottom face.

## Conflicts & open questions
- No energy-absorption value is quantified for the Michigan slabs. Only 2 slabs per case. Slabs are unreinforced.
- Strain rates of 10²–10³ s⁻¹ (blast, projectiles) are untested. → [[gaps]]

## Related
- [[impact-test]] · [[extreme-loading-applications]] · [[uhpc-vhsc]] · [[hshdc]]
