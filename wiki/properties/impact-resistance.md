---
type: property
slug: impact-resistance
aliases: [drop-weight impact, repeated impact, punching resistance, peak contact force, PCF]
tags: [dynamic, extreme-loading]
sources: [ranade2017-hshdc-impact-resistance, he2024-hdc-research-advances, lee2021-hsdc-wall-emi-impact, mechtcherine2011-shcc-high-strain-rate, xue2023-shcc-structural-review]
updated: 2026-10-21
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
weight, height 200 mm + 100 mm per blow up to 1100 mm (blow 10), then repeated at 1100 mm (§3.2.1, pp. 9–11; Figs. 8–11; Fig. 9 x-axis, p. 10):

| Panel | Layers | Result |
|---|---|---|
| H5S / H10S / H20S | single (one face) | text: failed at blow 2 / 4–5 / 4–5 by scabbing of the unstrengthened bottom face (p. 9). Figures disagree: Fig. 8 plots H10S to blow 5 and H20S to blow 6; Figs. 11/12 label other counts ⚠️ |
| H5D / H10D / H20D | double (both faces) | H20D total reaction force 2.2× H5D and 1.6× H10D (p. 10); peak reaction ≈ 38.5 kN (H20D) vs ≈ 26 kN (H5D) (read from Fig. 9) |
| D1-HSDC (full 100 mm HSDC) | — | ≈ 57 kN peak reaction, survived 16–17 blows, ≈ 515 J (read from Figs. 9, 11) |

- Total imparted energy to failure rises with HSDC thickness (printed labels, Fig. 11, p. 12): H5S 19.0, H10S 68.3, H20S 96.8,
  H5D 86.7, H10D 90.2, H20D 114.9 J; H20D = 6.0× H5S and +32.5% over H5D (the text's "3.5% larger" is a typo). "Total imparted
  energy" is not defined; 19 J is far below the ≈ 196 J potential energy of one 200 mm drop ⚠️ ([[lee2021-hsdc-wall-emi-impact]]).
- Crack widths in H20D: about 0.05 mm after blow 1, 0.70 / 1.10 mm after blows 4 / 5; H5D and H10D 5.0 / 5.5 mm
  (units are mm per the Fig. 9d axes; the text's "m" is a typo; pp. 10–11). → [[crack-width]]
- Post-impact SE decrease (Fig. 12, p. 12): H20S ≈ 7%, H20D 24.7%, H10S ≈ 16%, H10D ≈ 26%, H5D ≈ 28%, H5S ≈ 44%.
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
