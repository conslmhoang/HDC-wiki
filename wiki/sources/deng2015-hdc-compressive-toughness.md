---
type: source
slug: deng2015-hdc-compressive-toughness
title: "Analysis of Compressive Toughness and Deformability of High Ductile Fiber Reinforced Concrete"
authors: [Mingke Deng, Jian Han, Haibo Liu, Meng Qin, Xingwen Liang]
year: 2015            # vol. 2015; received 27 Jun 2015, accepted 11 Oct 2015
venue: "Advances in Materials Science and Engineering, vol. 2015, Article ID 384902, 7 pp. (Hindawi)"
doi: "10.1155/2015/384902"
raw_file: raw/papers/Deng2015_HDC-compressive-toughness.pdf
material_term: "HDC = high ductile fiber reinforced concrete (XAUAT's name for ECC)"
study_type: experimental + analytical (uniaxial compression; Mander-model equivalence)
tags: [compression, toughness-index, pva, xauat, deng-group, confinement-analogy]
ingested: 2026-10-20
updated: 2026-10-20
---

# Compressive toughness and deformability of PVA-HDC (Deng et al., 2015)

## One-paragraph summary
Xi'an University of Architecture and Technology (XAUAT, Deng Mingke group) tested 100 × 100 × 300 mm
prisms in uniaxial compression: a fiber-free mortar matrix and HDC with 1.0, 1.5 and 2.0 vol.% PVA,
three prisms each, at 10 months (p. 2, Tables 2–3). Fiber barely changed the peak load
(640 kN for the matrix vs 503–623 kN for HDC), but it raised the peak strain from 0.0022 to
0.0067–0.0080 and left 10–20% residual capacity at large deformation (Table 3, p. 4). The authors propose
an **equivalent compressive toughness index** W_cu = Ω_u/(A·l), the energy per unit volume up to the
point where the load drops to u = 0.85, 0.50 or 0.20 of the peak (Eq. 3). For u = 0.85 it rises
linearly with fiber volume: W_cu^0.85 = W_cu,0^0.85 + 0.10φ (Eq. 4, Fig. 6). Using Mander's
confined-concrete model, they treat fiber bridging (σ_t = f_t = 5.7 MPa) as lateral confinement.
This gives a predicted peak strain of 0.0079 for 2% PVA, which matches the test. They argue the bridging
is equivalent to a volumetric stirrup ratio of 3.03% in a 500 mm RC column (Eqs. 5–9, p. 5–6).
The paper is in compression only: tensile strain hardening is **asserted, not measured**.

## Objective / research question
- Find a compressive-toughness index for HDC, and quantify how PVA fiber volume affects compressive
  toughness and deformability (p. 1–2).
- Explain the larger compressive deformability through an equivalence between fiber bridging and stirrup
  confinement (p. 5–6).

## Terminology (rule §3)
- The authors' exact term is **"high ductile fiber reinforced concrete (HDC)"**. They say the group adopted this
  name for ECC "to facilitate the application of ECC in concrete structures" (p. 1).
- On p. 5 they also write "high ductility fiber reinforced concrete".
- **Tensile strain hardening:** stated as a property of HDC ("tensile strain hardening effect of HDC",
  p. 5–6). The only tensile value is "HDC tensile strength average f_t = 5.7 MPa" for mix 4 (p. 5). No
  tensile test method, tensile strain or crack width is reported. So **strain hardening is not
  demonstrated in this paper.**

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 (matrix) | type not reported | 50% "by volume" ⚠️ | none | fine river sand; sand–cement ratio 0.36; max size not reported | 0.29 ("water-cement ratio" ⚠️) | used, dosage not reported | none | — | — | 0 |
| 2 | same | 50% | none | same | 0.29 | n.r. | PVA | 12 | 39 | 1.0 |
| 3 | same | 50% | none | same | 0.29 | n.r. | PVA | 12 | 39 | 1.5 |
| 4 | same | 50% | none | same | 0.29 | n.r. | PVA | 12 | 39 | 2.0 |

Units of binder quantities: ratios only, as given in Table 2. The basis of "fly ash (by volume) 50%"
and of the "water-cement ratio" is unclear: probably fly ash as 50% of the binder and water/binder, but
not stated ⚠️.

PVA fiber (Table 1): L 12 mm, d 39 µm, aspect ratio 0.31 × 10³ (about 310), σ_f 1600 MPa, E 40 GPa,
ultimate strain 7%, density 1.3 g/cm³. Manufacturer and oil coating not reported.

## Test methods
- Specimen geometry: prisms 100 × 100 × 300 mm, 3 per mix (p. 2).
- Loading / rate: uniaxial compression, 500 t electro-hydraulic servo machine, 0.5 mm/min displacement
  control (p. 2, Fig. 1).
- Measurement: load and vertical deformation (load–deformation curves, Fig. 3). Transducer type and
  gauge length not reported. Strain = deformation / 300 mm.
- Curing & test age: all specimens made and cured "in the same condition" (regime not reported);
  tested at **10 months** (p. 2).
- Toughness index: f_ce = Ω_u/(δ_u·A) (Eq. 2, modelled on the CECS 13:2009 equivalent flexural
  strength); W_cu = f_ce·δ_u/l = Ω_u/(A·l) (Eq. 3).
→ no dedicated compression test-method page yet; see [[compressive-strength]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| 1 (matrix) | 64.0 prism (computed here from 640.45 kN / 100² mm²); authors quote mean f_c 63.06 (p. 6) | n/a | not reported | not reported | n/a | peak deformation 0.65 mm; peak strain 0.0022 (0.22%); W_cu^0.85 0.065 N/mm² |
| 2 (1.0% PVA) | 50.3 prism (computed from 502.78 kN) | n/a | not reported | not reported | n/a | 2.22 mm; 0.0074; W_cu^0.85/0.50/0.20 0.187/0.209/0.234 |
| 3 (1.5% PVA) | 56.9 prism (computed from 568.50 kN) | n/a | not reported | not reported | n/a | 2.02 mm; 0.0067; W_cu 0.198/0.218/0.276 |
| 4 (2.0% PVA) | 62.3 prism (computed from 622.52 kN) | n/a | 5.7 (mean; method not reported) | not reported | n/a | 2.39 mm; 0.0080; W_cu 0.266/0.323/0.382 |

All at 10 months. Peak load and deformation from Table 3; W_cu (N/mm²), δ_u (mm) and Ω_u (×10⁵ N·mm)
from Table 4.

Main findings (with Table/Fig. location):
- **Fiber barely changes strength but greatly raises deformability.** The peak strain of HDC is
  0.0067–0.0080 vs 0.0022 for the matrix. The authors give this as 3.41–3.67 times (Abstract, p. 4).
  ⚠️ From Table 3, mix 3 gives only 3.1×; see "To verify".
- The matrix peak strain (0.0022) is close to the GB 50010-2010 value for concrete (p. 4).
- Above 1% fiber, the peak strain hardly increases further (p. 4).
- HDC fails gradually through three stages (p. 2):
  - linear elastic, with micro-cracks appearing at 50–60% of peak load;
  - from 80% of peak, cracks widen and the curve bends; a vertical main crack forms, and fiber
    pull-out or rupture can be heard;
  - after the peak, slow load decay; at 10–20% of peak load the faces of the main crack slip
    ("dislocation"), and some residual capacity remains.
  The mortar fails on the appearance of vertical cracks (p. 2, Fig. 2).
- **Toughness index:** W_cu^0.85 of HDC is 2.88–4.09 times that of the matrix (p. 5, Table 4). In the
  worked example, specimen b has 1.60× the δ_0.85 of a and only 1.06× its f_ce, but 1.66× its W_cu. So
  W_cu captures deformability where equivalent strength does not (p. 4–5, Fig. 5).
- Uses proposed for the index: W_cu^0.85 for ductility and energy-dissipation analysis; W_cu^0.50 and
  W_cu^0.20 for residual capacity and progressive-collapse resistance (p. 5).
- **Regression:** W_cu^0.85 = W_cu,0^0.85 + 0.10φ, with φ in vol.% (Eq. 4, Fig. 6). The units of the
  coefficient are implicitly N/mm² per %. A check with Table 4 gives 0.065 + 0.20 = 0.265 vs 0.266 measured.
- **Confinement analogy:** Mander model with ε_co 0.0022, f_c 63.06 MPa and f_t = σ_t = 5.7 MPa gives
  ε_cco = 0.0079, i.e. 3.59× the matrix, against 0.0080 measured for mix 4 (p. 5–6, Eqs. 5–6).
- **Stirrup equivalence:** a 500 × 500 mm column with HRB400 Ø10 two-leg ties (f_yv 360 MPa, 25 mm cover,
  b = 450 mm) would need s = 23 mm to match σ_t = 5.7 MPa, i.e. ρ_v = 3.03% (Eqs. 7–9, p. 6).
  The authors conclude that HDC in plastic-hinge regions could improve deformability and reduce the
  number of ties (p. 6–7).

## Mechanisms / explanations offered by authors
- Fiber bridging across the vertical (splitting) cracks supplies a continuous, stable lateral restraint.
  This puts HDC in a state like actively confined concrete under triaxial compression (p. 5, Fig. 7).
- The authors give the tensile strain hardening of HDC as the reason the lateral force is sustained after
  transverse cracking (p. 5).
- Fibers are pulled out against interfacial friction, which keeps the specimen intact after cracking (p. 1).

## Limitations (stated + observed)
- Stated: conclusions called "preliminary" (p. 7).
- Observed:
  - Only 3 specimens per mix and one matrix. Curing regime, cement type and SP dosage are not reported.
  - The test age (10 months) is unusual, so values are not comparable with 28-d data.
  - The tensile strength (5.7 MPa) has no method, specimen or strain. The confinement analogy assumes
    σ_t = f_t over the whole crack face. It is calibrated against one mix only.
  - The regression uses 4 points (3 fiber levels + matrix).
  - The "3.41–3.67×" peak-strain range does not match mix 3 in Table 3 (3.1×) ⚠️.
  - The basis of the 50% fly ash ("by volume") and of the 0.29 "water-cement" ratio is unclear ⚠️.
  - No lateral strain or Poisson measurement to support the confinement mechanism.

## Relation to other work
- Agrees with:
  - [[chai2023-hdc-ambient-temperature]] and [[li2021-hdc-sulfate-dry-wet]]: Chinese PVA-HDC with high fly
    ash and normal-range f'c (about 45–64 MPa).
  - [[li2021-hdc-sulfate-dry-wet]]: cracked, intact "drum" failure in compression.
- Contradicts: ⚔️ none directly. Fiber reduces prism strength here (64.0 → 50.3–62.3 MPa), as noted for UHDC
  in [[ye2021-uhdc-flexural-size-effect]] (as cited there).
- Extends:
  - the XAUAT (Deng) HDC lineage back to 2015, before [[yang2024-hshdc-uniaxial-tension]];
  - first compression-toughness index for HDC in the wiki.
  - Cites [[li1992-steady-state-multiple-cracking]] as the origin of ECC (ref. [1]).

## Pages updated from this source
- [[compressive-strength]]
- [[pva-fiber]]
- [[terminology-hdc-ecc-shcc]]
- [[fiber-bridging]]
- [[fly-ash]]
- [[rc-member-strengthening]]
- [[mix-designs]]
- [[mechanical-results]]

## To verify
- [ ] Peak-strain ratio: the abstract and p. 4 say 3.41–3.67×, but Table 3 gives 0.0067/0.0022 ≈ 3.0
      (strain) or 2.02/0.65 ≈ 3.1 (deformation) for mix 3. ⚠️ unverified
- [ ] Fly ash "(by volume) 50%" in Table 2: of binder? by mass or by volume? ⚠️ unverified
- [ ] "Water-cement ratio 0.29": water/cement or water/binder? ⚠️ unverified
- [ ] Source and test method of f_t = 5.7 MPa (p. 5); possibly from refs. [7, 8] (Deng 2013, 2014,
      Industrial Construction), not ingested.
- [ ] Curing regime before the 10-month test.
- [ ] f'c values in the Key results table are computed here from peak load / 10 000 mm²; the authors
      report only the matrix mean (63.06 MPa), which differs slightly from 640.45 kN / 10⁴ mm² = 64.0 MPa.
