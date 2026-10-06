---
type: source
slug: ranade2015-hshdc-tensile-rate-effects
title: "Tensile Rate Effects in High Strength-High Ductility Concrete"
authors: [Ravi Ranade, Victor C. Li, William F. Heard]
year: 2015
venue: "Cement and Concrete Research 68 (2015) 94–104 (received 12 Jun 2014, accepted 10 Nov 2014, online 25 Nov 2014)"
doi: "10.1016/j.cemconres.2014.11.005"
raw_file: "raw/papers/Ranade2014_Tensile Rate Effects in High Strength-HDC.pdf"
material_term: "HSHDC (High Strength-High Ductility Concrete); described as a strain-hardening FRCC"
study_type: "experimental (composite + micro-scale) + analytical (scale-linking)"
tags: [hshdc, pe-fiber, strain-rate, dynamic-tension, micromechanics, fiber-pullout, fracture-toughness]
ingested: 2026-10-06
updated: 2026-10-06
---

# Tensile Rate Effects in HSHDC (Ranade, Li & Heard, 2015)

## One-paragraph summary
The paper tests [[hshdc]] in direct tension at six strain rates from 10⁻⁴ to 10 s⁻¹ (6 dogbones per
rate, 36 in total). It measures the micro-scale properties at the matching displacement rates:
150 single-fiber pullouts, and notched-beam Km at four rates.

From the slowest to the fastest rate:
- σ_fc rises by about 53% (8.1 → 12.4 MPa) and σ_tu by about 42% (14.5 → 20.6 MPa).
- σ_tu/σ_fc stays about 1.8.
- ε_tu falls from 4.2% to 2.9% up to 0.1 s⁻¹, then plateaus. This tracks the drop in residual
  crack width from 160 to 120 µm.

At the micro-scale:
- τ0 barely changes (+14%), because PE has no chemical bond.
- PE fiber modulus rises +85% and strength +21%, and these changes dominate.
- f rises +27% and µ +43%.
- Km rises from 1.10 to 1.31 MPa√m.

A scale-linking model explains the composite rate effects quantitatively up to about 0.1–1 s⁻¹.
J′b/J_tip stays about 6 or more, so multiple cracking persists at all rates. → [[strain-rate-effects]]

## Objective / research question
1. Effect of strain rate (10⁻⁴–10 s⁻¹) on the composite direct-tension behaviour of HSHDC.
   Compression is out of scope.
2. Effect of rate on fiber/matrix interaction, fiber properties, and matrix toughness.
3. Whether the micro-scale rate effects explain the composite-scale rate effects through
   scale-linking.

## Materials & mix design
Table 1 is identical to the final HSHDC of Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source):

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| HSHDC | 1 (907 kg/m³), Class H | 0 | SF 0.389 (353); silica flour 0.277 (251) | silica sand 0.700 (635), 100–600 µm | 0.15 (w/cm); water/c 0.208 | 0.018 (16) | UHMWPE | 12.7 (per companion papers) | 28 (per companion papers) | 2 (19 kg/m³) |

Units: mass ratio to cement plus kg/m³. Curing follows Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source) → [[heat-curing]].

## Test methods
- **Direct tension at rate** ([[dogbone-uniaxial-tension]]):
  - dogbones as in the 2013 paper, gauge length 90 mm;
  - strain rates 10⁻⁴, 10⁻³, 10⁻², 10⁻¹, 1, 10 s⁻¹ via displacement rates of 9 µm/s, 90 µm/s,
    0.9 mm/s, 9 mm/s, 90 mm/s, 0.9 m/s;
  - 10 kN electro-mechanical system, dynamic load cell (25 kN);
  - **lost-motion grip** above 1 mm/s;
  - 2 LVDTs; data sampled at 10⁴ × the strain rate.
  - Stress oscillations at ≥ 0.01 s⁻¹ (ringing of the test system) are removed by local averaging.
- **Single-fiber pullout** at the same 6 rates, 25 per rate:
  - 10 aligned;
  - 5 at 27° and 5 at 45°;
  - 5 with Le > 15 mm to measure the in-situ fiber strength and modulus.
  → [[single-fiber-pullout-test]]
- **Matrix Km:** 4 notched beams per rate, on a 100 kN hydraulic system at 20 µm/s, 0.2, 2 and
  10 mm/s. These correspond to notch-tip strain rates of about 10⁻⁴, 10⁻³, 10⁻² and about 0.05 s⁻¹.
  The 10 s⁻¹ rate was not reachable. → [[matrix-fracture-toughness]]
- Curing & test age: HSHDC heat-curing regime. The test age is **not stated explicitly** (presumably
  28 d, as in the companion papers).

## Key results
Table 2 averages (6 dogbones per rate):

| Strain rate (s⁻¹) | σ_fc (MPa) | σ_tu (MPa) | σ_tu/σ_fc (PSH_strength) | ε_tu (%) | Avg residual crack width (µm) |
|---|---|---|---|---|---|
| 10⁻⁴ | 8.1 (COV 11%) | 14.5 (8%) | 1.8 | 4.2 (10%) | 160 |
| 10⁻³ | 7.6 (14%) | 15.3 (7%) | 2.05 | 3.9 (16%) | 150 |
| 10⁻² | 8.9 (16%) | 16.3 (7%) | 1.87 | 3.3 (23%) | 140 |
| 10⁻¹ | 9.7 (21%) | 17.5 (9%) | 1.87 | 2.9 (23%) | 120 |
| 1 | 11.1 (24%) | 19.3 (12%) | 1.82 | 2.9 (28%) | 110 |
| 10 | 12.4 (22%) | 20.6 (12%) | 1.71 | 2.7 (26%) | 110 |

- The minimum ε_tu over all 36 specimens is 1.7% (specimen #31 at 10 s⁻¹) (p. 99).
- Variability of all properties grows with rate (Fig. 4–5).
- For individual specimens, PSH_strength correlates positively with ε_tu at every rate (Fig. 6).

Micro-scale rate effects (0.009 → 900 mm/s):

| Parameter | Quasi-static | Highest rate | Change | Location |
|---|---|---|---|---|
| τ0 | (about 1.5 MPa per companion) | — | +14% | Fig. 8 |
| β | 0.003 | 0.006 | ×2 (ECC β ≈ 0.6 for comparison) | p. 98, Fig. 8 |
| f | 0.59 | 0.75 | +27% | p. 98, Fig. 9 |
| µ (N/(m·rad)) | 386 | 553 | +43% | p. 99, Fig. 9 |
| PE fiber strength | — | — | +21% | Fig. 10 |
| PE fiber modulus | — | — | +85% | Fig. 10 |
| Km (MPa√m) | 1.10 (0.02 mm/s) | 1.31 (10 mm/s) | +19% (computed here) | p. 100, Fig. 11 |
| J′b (J/m²) | 969 | about 600 | −38% (computed here) | p. 103 |
| J_tip (J/m²) | 25 | ≤ 100 (assumes Km doubles) | — | p. 103 |

Scale-linking: at 0.9 mm/s, σ0 = 15.2 MPa; min(Vf) = 0.80 × 2%, so min(σ0) = 12.2 MPa at δ = 112 µm
(p. 101). Quasi-static analytical σ_tu is 11.3 MPa and crack width 140 µm, against experimental
values of 14.5 MPa and 160 µm. The comparison is therefore made with ratios relative to the
quasi-static values. Prediction errors:
- crack width: < 5% up to 1 s⁻¹;
- σ_tu: < 7% up to 0.1 s⁻¹;
- larger errors at 1–10 s⁻¹ (Fig. 15).

## Mechanisms / explanations offered by authors
- **No chemical bond, so a rate-insensitive interface.** In hydrophilic-fiber FRCC (e.g. PVA),
  the chemical bond is highly rate-sensitive. Hydrophobic PE has only friction, so τ0 changes little
  (p. 94–95, 98). → [[fiber-matrix-interface]]
- **Viscoelastic PE fiber:** strength and modulus rise with rate. A higher fiber modulus makes
  the σ–δ curve steeper, which narrows cracks and lowers ε_tu. A higher fiber strength raises σ0
  and therefore σ_tu (p. 101–102). → [[pe-fiber]], [[fiber-bridging]]
- **f and µ rise** with rate, possibly because a stronger, tougher matrix gives a larger normal
  reaction. The µ effect adds at most about 4.3% to the bridging stress (p. 99).
- **σ_fc follows Km**, consistent with Irwin's fracture criterion for the same flaw population (Fig. 16).
- **ε_tu falls even though PSH_strength stays constant**, because the crack count stays about the same
  while each crack becomes narrower (p. 97).
- **Scatter at high rates** may come from greater variability of the micro-properties, and unknown
  hardening mechanisms at very high rates "cannot be ruled out" (p. 102).

## Limitations (stated + observed)
- Elastic modulus at each rate was underestimated because of LVDT slippage; strain gauges are needed (stated).
- Km was not measured at 1–10 s⁻¹ (equipment limit); J_tip at the highest rate is assumed (Km doubled).
- Compression rate effects are out of scope.
- The model under-predicts absolute σ_tu (11.3 vs 14.5 MPa), so only relative changes are compared.
- *Observed:* the maximum rate is 10 s⁻¹. Real blast or impact rates (above 10² s⁻¹) were not tested.
  One mix only.

## Relation to other work
- Agrees with:
  - Ranade et al. 2013 "Micromechanics of HSHDC" (ACI MJ 110(4); not a wiki source): same model, and the same quasi-static f = 0.59 and µ = 386.
  - Yang & Li 2005 and Maalej et al. 2005 (as cited): τ0 depends only weakly on rate.
- Contradicts: ⚔️
  1. **ε_tu at quasi-static rate is 4.2%** here (10⁻⁴ s⁻¹, about 0.54 mm/min over a 90 mm gauge),
     but **3.4%** in Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source) (0.5 mm/min). The rates are about
     the same, so this is likely batch-to-batch variation.
  2. σ_fc 8.1 MPa here vs 8.3 MPa (2013).
  3. min(Vf) = 0.80 × 2% = 1.6% here vs 1.7% in Ranade et al. 2013 "Micromechanics of HSHDC" (ACI MJ 110(4); not a wiki source).
- Context (as cited, p. 94):
  - For plain concrete, the tensile strength increases with rate 2–3× faster than compressive strength.
  - The rate effect is smaller in high-strength concrete than in normal concrete (CEB-FIP / MC2010 bilinear forms).
  - Matrix Km: UHPC about 1.31 MPa√m (Orange et al. 2000); ECC about 0.5 MPa√m (Yang 2008).

## Pages updated from this source
- [[strain-rate-effects]] · [[hshdc]] · [[pe-fiber]] · [[fiber-matrix-interface]] · [[fiber-bridging]] ·
  [[matrix-fracture-toughness]] · [[strain-hardening]] · [[tensile-strain-capacity]] · [[crack-width]] ·
  [[fiber-dispersion]] · [[dogbone-uniaxial-tension]] · [[single-fiber-pullout-test]] ·
  [[extreme-loading-applications]] · [[mix-designs]] · [[mechanical-results]] · [[micromechanical-parameters]]

## To verify
- [ ] Test age is not stated. Confirm whether it is 28 d.
- [ ] The absolute τ0 values at each rate are only in Fig. 8 (not in the text). Read them off the figure if needed.
- [ ] The fiber strength and modulus absolute values are only in Fig. 10.
- [x] Raw file renamed by the human to `Ranade2014_...` (2026-10-06).
