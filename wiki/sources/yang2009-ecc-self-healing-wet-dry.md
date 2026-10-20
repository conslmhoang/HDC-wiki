---
type: source
slug: yang2009-ecc-self-healing-wet-dry
title: "Autogenous healing of engineered cementitious composites under wet–dry cycles"
authors: [Yingzi Yang, Michael D. Lepech, En-Hua Yang, Victor C. Li]
year: 2009   # Cement and Concrete Research 39 (2009); received 1 Dec 2007, accepted 21 Jan 2009
venue: "Cement and Concrete Research 39 (2009) 382–390. University of Michigan (Y. Yang visiting from Harbin Institute of Technology); corresponding author V.C. Li"
doi: "10.1016/j.cemconres.2009.01.013"
raw_file: raw/papers/Yang2009_ECC-self-healing-wet-dry.pdf
material_term: "ECC (Engineered Cementitious Composites), described as a high-performance fiber-reinforced cementitious composite; PVA fiber (Kuralon-II REC-15). Mix proportions equal M45 (Table 1). A separate 0.5 vol.% PVA tension-softening mortar was used for single-crack tests (not ECC). HDC/SHCC not used."
study_type: "experimental (laboratory wet–dry conditioning of pre-cracked coupons; resonant frequency, uniaxial tension, water permeability, microscopy/EDX)"
tags: [self-healing, ecc, pva-fiber, fly-ash, wet-dry-cycles, resonant-frequency, stiffness-recovery, permeability, crack-width, calcium-carbonate, m45]
ingested: 2026-10-21
updated: 2026-10-21
---

# ECC self-healing under wet–dry cycles (Yang et al., 2009)

## One-paragraph summary
Michigan study of autogenous healing of **PVA-ECC (M45 proportions, FA/C 1.2)** coupons
(230 × 76 × 13 mm) that were air-cured for **6 months**, pre-loaded in uniaxial tension to
**0.3, 0.5, 1, 2 or 3%** strain, and then exposed to **10 wet–dry cycles** of two kinds: CR1 (24 h water
at 20 °C / 24 h lab air at 21 °C) and CR2 (24 h water / 22 h oven at 55 °C / 2 h lab air) (§2.2–2.3).
Healing was tracked by transverse resonant frequency (RF, ASTM C215), tensile reloading and, for a
separate single-crack mortar series (0.5 vol.% PVA, tension-softening), water permeability (§2.1, 2.4).
Single-crack tests showed **full RF recovery and uncracked-level permeability for cracks < 50 µm**,
partial recovery for 50–150 µm, and **no recovery above 150 µm** (Figs. 4–5, p. 387). In ECC, RF ratios
rose from 40–82% to **87–100% (CR1)** and from 31–83% to **77–90% (CR2)**, stabilising after **4–5 cycles**
(Figs. 6–7, p. 387–388). Healed specimens kept tensile strain capacity of **1.7–3.1% (CR1)** and
**0.8–2.2% (CR2)** on reloading, with clear stiffness recovery (Figs. 9–12). The healing product was mainly
**calcium carbonate** (EDX, Fig. 14). Maximum residual crack width in pre-loaded ECC was 50–90 µm
(Table 2); cracks closed about **15%** on unloading (p. 385).

## Objective / research question
- Quantify self-healing of pre-damaged, mature (6-month) ECC under cyclic wetting and drying that
  mimics rain / sun exposure (p. 383).
- Measure recovery of transport (permeability) and mechanical properties (RF, stiffness, tensile
  strength and strain capacity), and the effect of drying temperature (CR1 vs CR2) (§2, §3).

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| ECC (M45 proportions) | 578 | 694 (Class F, Boral) | none | 462 (sand, 110 µm average grain size; max not reported) | 0.25 (computed here: 319 / (578 + 694), by mass) | 17 (polycarboxylate HRWR, ADVA Cast 530) | PVA, Kuralon-II REC-15 (Kuraray) | 12 | not reported | not reported (26 kg/m³; fiber density not given, so not converted; ECC is "typically 2% by volume", p. 382) |
| Single-crack mortar | same as ECC | same | none | same | same | same | PVA | not reported (same fiber assumed ⚠️) | not reported | 0.5 (p. 385) |

Units of binder quantities: kg/m³ (Table 1). FA/C = 694 / 578 = **1.20 by mass** (computed here).
Water 319 kg/m³. Type I portland cement.

## Test methods
- Specimen geometry: coupons 230 × 76 × 13 mm for RF, tension and permeability (p. 384); crack
  counting over a 100 mm gauge (p. 385).
- Loading / rate: servo-hydraulic, displacement control, **0.0025 mm/s**; aluminium plates glued to the
  ends; pre-loading to fixed strains 0.3–3% at 6 months; reloading after conditioning (§2.1.2).
- Measurement (LVDT, DIC, ...): two external LVDTs; RF by ASTM C215 transverse mode; water permeability
  by falling-head (low k) or constant-head (high k) set-ups adapted from Wang et al. 1997 and Cernica
  1982 (Eqs. 1–2, Fig. 3); crack widths measured in the **unloaded** state (p. 385); microscopy and EDX.
- Curing & test age: covered with plastic, demoulded at 24 h, then **air-cured in the lab for 6 months**;
  f'c ≈ 60 MPa at 28 d (p. 385). Conditioning: 10 cycles of CR1 or CR2 (§2.2). RF normalised by
  virgin specimens given the same 10 cycles (p. 386).
→ [[dogbone-uniaxial-tension]] · [[self-healing]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| ECC, virgin (6 months) | ≈ 60 (28 d, p. 385) | ≈ 3.5–4 (Figs. 9–10 ⚠️ read) | ≈ 4.0–4.4 (Figs. 9–10 ⚠️ read) | "about 3" (p. 384; strain at peak or ultimate not stated) | average steady-state ≈ 60 (p. 384); maximum residual 50–90 (Table 2) | — |
| ECC, after 10 × CR1 | — | below virgin first-crack strength (p. 388) | ≈ virgin level (Fig. 9 ⚠️) | **1.7–3.1** on reloading (residual strain excluded) (p. 388) | — | RF 87–100%; stiffness ratio ≈ 74–90% (Fig. 12 ⚠️) |
| ECC, after 10 × CR2 | — | below virgin (p. 388) | higher than pre-loading, esp. 2–3% pre-strain; up to ≈ 5.3 (Fig. 10a ⚠️) | **0.8–2.2** (p. 388) | — | RF 77–90%; stiffness ratio ≈ 54–74% (Fig. 12 ⚠️) |

Crack characteristics of pre-loaded ECC (Table 2, residual, 100 mm gauge):

| Pre-strain (%) | No. of cracks | Maximum crack width (µm) |
|---|---|---|
| 3 | 39 | 90 |
| 2 | 27 | 60 |
| 1 | 15 | 60 |
| 0.5 | 7 | 70 |
| 0.3 | 5 | 50 |

RF ratio before → after 10 cycles (Fig. 7, bar heights ⚠️ read from figure):

| Pre-strain (%) | CR1 before | CR1 after | CR2 before | CR2 after |
|---|---|---|---|---|
| 3 | ≈ 40 | ≈ 87 | ≈ 31 | ≈ 81 |
| 2 | ≈ 45 | ≈ 94 | ≈ 45 | ≈ 76 |
| 1 | ≈ 58 | ≈ 91 | ≈ 59 | ≈ 87 |
| 0.5 | ≈ 71 | ≈ 100 | ≈ 55 | ≈ 87 |
| 0.3 | ≈ 82 | ≈ 97 | ≈ 83 | ≈ 90 |

Main findings (with Table/Fig. location):
- **Crack-width limits for healing** (single-crack mortar, 10 × CR1): RF recovers to 100% for cracks
  < 50 µm; no RF change for > 150 µm (Fig. 4, p. 387). After conditioning, permeability of < 50 µm cracks
  is "essentially identical" to uncracked; it rises exponentially with width, with little or no recovery
  for wider cracks (Fig. 5, p. 387). Conclusion: crack width must be **< 150 µm, preferably < 50 µm**
  (p. 387, Conclusion 1).
- Permeability of single-crack specimens (Fig. 5 ⚠️ read, log scale): ≈ 10⁻¹⁰ m/s uncracked; ≈ 10⁻⁹ m/s at
  50 µm before conditioning; ≈ 10⁻⁸ m/s at 100 µm; ≈ 10⁻⁶ m/s at 200 µm and ≈ 3 × 10⁻⁶ m/s at 300 µm
  with no change after conditioning.
- **RF recovery stabilises after 4–5 wet–dry cycles** (Fig. 6, p. 387; Conclusion 2).
- Higher pre-strain → lower initial and final RF but larger rebound; rebound rises with crack number
  (Fig. 8, p. 388). Authors attribute incomplete healing at high strain to the probabilistic presence
  of wider cracks.
- **Hot drying (CR2, 55 °C) heals less** than CR1 (RF and stiffness), but raises ultimate tensile
  strength and slightly lowers strain capacity (p. 388; Conclusion 5).
- Without healing, reloading a 3%-pre-strained specimen shows a very low initial stiffness (crack
  re-opening) (Fig. 11); stiffness ratio without conditioning ≈ 4–6% vs ≈ 54–90% after conditioning
  (Fig. 12 ⚠️ read).
- First-crack strength after healing is below virgin, because new cracks start in the weaker CaCO₃
  healing product; most new cracks follow old crack paths (Fig. 15), but some form next to healed
  cracks (Figs. 16–17, p. 388).
- Residual crack widths are about **15% smaller** than under load ("crack closure of about 15%" on
  unloading, p. 385).
- RF ratio vs pre-strain is bilinear, with a sharp drop below ≈ 1% strain (crack width and number both
  grow) and a slow decay beyond (crack number only grows) (Fig. 2, from ref. [16], p. 384).

## Mechanisms / explanations offered by authors
- Crack width is the dominant factor for healing (Poiseuille / parallel-plate flow, p. 382).
- Main healing product is **calcium carbonate** (white residue, EDX, Figs. 13–14, p. 388); based on
  "limited EDX study" (Conclusions).
- Higher CR2 temperature may hydrate unreacted cement / fly ash and raise fiber–matrix bond, raising
  ultimate strength; it may also raise matrix toughness, reducing multiple cracking and ductility
  (p. 388–389, citing Wang 2005 PhD). CR2 healing products are less uniform (p. 388). Mechanism not
  confirmed.
- RF tracks dynamic modulus, so RF recovery and stiffness recovery agree (p. 388).

## Limitations (stated + observed)
- Stated: temperature effect on healing needs more study (p. 388); EDX evidence limited (Conclusions);
  only 10 wet–dry cycles.
- Stated: healing was studied in the unloaded state; the authors expect unloading has "only a small
  impact" (p. 385).
- Observed: single-crack tests use a 0.5 vol.% PVA tension-softening **mortar**, not ECC; the < 50 µm /
  < 150 µm limits are therefore from that mortar.
- Observed: one batch, ≥ 2 specimens per level (p. 385–386); air-cured 6 months (mature, high-FA), so
  results may not transfer to young ECC.
- Observed: Table 2 max crack width at 3% is 90 µm, but p. 384 says crack widths stay "below about
  60 µm" even at high strain ⚠️ internal inconsistency.
- Observed: text says 0.5% pre-strain reduced RF by "only 18%" (p. 388), while Fig. 7a shows ≈ 71% RF
  for 0.5% and ≈ 82% for 0.3% ⚠️.
- Observed: the 3% RF recovery is "87%" in the text (p. 388) and "76%" in Conclusion 3 and the abstract;
  strain capacity after healing is "1.7% to 3.1%" (p. 388) vs "1.8% to 3.1%" (Conclusion 6) ⚠️.
- Observed: no fiber diameter, no SP basis, no sand max size reported.

## Relation to other work
- Agrees with: [[ozbay2013-ecc-self-healing-sustained-load]] (CaCO₃ product; small cracks heal fully,
  > 60 µm only partly); [[homma2009-frcc-self-healing]] (CaCO₃; most deposition early); healing range
  "below 100 µm, preferably < 50 µm" attributed to Li & Yang 2007 in Özbay 2013.
- Agrees with: [[herbert2013-ecc-self-healing-natural-environment]] (same group, same RF method; RF
  90–96% after one week outdoors).
- Contradicts: ⚔️ loaded-vs-residual crack width — ≈ 15% closure on unloading here (tension, p. 385) vs
  ≈ 2× under sustained flexural load ([[ozbay2013-ecc-self-healing-sustained-load]]). Confirms the
  second-hand "≈ 15%" in [[herbert2013-ecc-self-healing-natural-environment]].
- Refines: "< 60 µm fast healing" (Reinhardt & Jooss, as cited in [[ma2021-ecc-durability-review]]):
  here < 50 µm gives full RF and permeability recovery in 10 wet–dry cycles; 50–150 µm partial.
- Extends: [[lepech2009-ecc-water-permeability]] (companion paper, same M45 mix and same permeability
  set-ups).

## Pages updated from this source
- [[self-healing]] · [[permeability]] · [[crack-width]] · [[durability]] · [[pva-fiber]] · [[fly-ash]]
- [[dogbone-uniaxial-tension]] · [[tensile-strain-capacity]] · [[multiple-cracking]] · [[heat-curing]]

## To verify
- [ ] Fig. 7 bar values, Fig. 12 stiffness ratios and Fig. 5 permeability values (all read from figures).
- [ ] RF recovery at 3% pre-strain: 87% (text, CR1) vs 76% (abstract, Conclusion 3).
- [ ] Strain capacity after CR1 healing: 1.7–3.1% (p. 388) vs 1.8–3.1% (Conclusion 6).
- [ ] "Reduction of only 18%" for 0.5% pre-strain (p. 388) vs Fig. 7a (≈ 71% RF before CR1).
- [ ] Table 2 max crack width 90 µm at 3% vs "below about 60 µm" (p. 384).
- [ ] Fiber diameter and Vf of the ECC (26 kg/m³ given; not converted).
- [ ] Whether the single-crack mortar used the same REC-15 fiber.
