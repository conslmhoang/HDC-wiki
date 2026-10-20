---
type: source
slug: yang2008-ecc-fiber-bridging-law
title: "Fiber-Bridging Constitutive Law of Engineered Cementitious Composites"
authors: [En-Hua Yang, Shuxin Wang, Yingzi Yang, Victor C. Li]
year: 2008
venue: "Journal of Advanced Concrete Technology, Vol. 6, No. 1, pp. 181-193, February 2008 (Japan Concrete Institute); scientific paper; received 2 Jul 2007, accepted 31 Oct 2007"
doi: "not printed in PDF; 10.3151/jact.6.181 ⚠️ unverified"
raw_file: raw/papers/Yang2008_fiber-bridging-law.pdf
material_term: "ECC (Engineered Cementitious Composites); PVA-ECC; mix 'M45' (p. 181, 188)"
study_type: analytical (micromechanical bridging model) + experimental validation (notched-coupon single-crack tension, single-fiber pullout)
tags: [ecc, pva-ecc, m45, fiber-bridging, sigma-delta, micromechanics, two-way-pullout, slip-hardening, matrix-spalling, cook-gordon, fiber-rupture, snubbing, fiber-strength-reduction, crack-width, fiber-dispersion, single-crack-test, michigan-group]
ingested: 2026-10-20
updated: 2026-10-20
---

# Fiber-bridging constitutive law of PVA-ECC (Yang et al., 2008)

## One-paragraph summary
University of Michigan (V.C. Li group) with Harbin Institute of Technology. The paper extends the
earlier simplified σ(δ) model of Lin, Kanda & Li (1999, as cited) with **three new fiber/matrix
mechanisms**: (1) **two-way fiber debonding and pull-out** (slip from both embedment sides, driven by
PVA slip hardening), (2) **matrix micro-spalling** at the fiber exit, and (3) the **Cook–Gordon
effect** (premature debonding ahead of the crack tip). Fiber **rupture** (with the inclination
strength reduction f′) and **snubbing** (f) are kept from earlier models. The model is validated
against single-crack notched-coupon tension tests of PVA-ECC M45 at reduced fiber contents of 0.1 and
0.5 vol.% (Fig. 12). For the standard 2 vol.% M45, it predicts a mean peak bridging stress of
**6.7 MPa at about 130 µm** (p. 191), well above the composite σ_tu (about 5 MPa) and crack width
(about 60 µm) of Fig. 1. The authors reconcile this by assuming a **±25% plane-to-plane variation in
bridging fiber volume** (1.5 / 2.0 / 2.5 vol.%): the weakest plane (1.5%) sets σ_tu, and δ at
σ = 5 MPa on the curves gives the crack width (37–133 µm, "mean" 62 µm; Fig. 13). **Two-way pull-out
is the mechanism most responsible** for correcting the earlier under-prediction of crack opening (Fig. 14).
This is the **primary source** for the "min(Vf)" method that the wiki previously cited second-hand
via [[ranade2015-hshdc-tensile-rate-effects]].

## Objective / research question
- Build an analytical σ(δ) model of ECC linking constituent parameters to composite properties, with
  better **crack-opening** prediction than Lin et al. (1999) (p. 182).
- Verify the model against measured σ(δ) curves (p. 182, 188).
- Purpose: design for steady-state crack-width control (durability) and composite tensile properties
  (ultimate limit state) (Abstract; p. 192).

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| M45, Vf 2% | 571 (Type I OPC) | 685 (ASTM Class F) | none | 456; fine silica sand, mean size 110 µm (max not reported) | 0.26 (computed here: 332/(571+685), by mass); FA/C = 1.20 by mass (computed) | 6.8 (polycarboxylate HRWR) | PVA, oil-coated 1.2% by weight (REC-15, p. 189) | 12 | 39 | 2 (26 kg/m³) |
| M45, Vf 0.5% | 571 | 685 | none | 456 | 0.26 (computed) | 6.8 | PVA | 12 | 39 | 0.5 (6.5 kg/m³) |
| M45, Vf 0.1% | 571 | 685 | none | 456 | 0.26 (computed) | 6.8 | PVA | 12 | 39 | 0.1 (1.3 kg/m³) |

Units of binder quantities: kg/m³ (Table 1, p. 189). Water 332 kg/m³. Totals 2076.8 / 2057.3 / 2052.1
kg/m³. The paper does not state W/B; it is computed here from Table 1. The kg/m³ fiber contents are
consistent with Vf × 1300 kg/m³ fiber density (p. 188).

**Fiber properties** (p. 188; Table 2, p. 190):
| Property | Value | Location |
|---|---|---|
| Nominal tensile strength | 1600 MPa | p. 188 |
| Apparent (in-situ) strength σfu | 1060 MPa | Table 2 |
| Ef | 22 GPa | Table 2 |
| Density | 1300 kg/m³ | p. 188 |
| Oil coating | 1.2% by weight | p. 188 |

## Test methods
- **Specimen geometry:** notched coupon, 13 mm thick × 76 mm wide × 90 mm high; 2 mm wide
  circumferential notch; 6 mm deep notches on the two lateral sides, 2 mm on front and back faces
  (Fig. 10, p. 188–189). Fiber content cut to 0.1 and 0.5 vol.% so that a **single crack** forms.
- **Loading / rate:** servohydraulic, deformation control, 0.0001 mm/s (quasi-static); aluminum plates
  glued at the ends for gripping (p. 188).
- **Measurement:** two extensometers, 5 mm gauge, across the notches; elastic deformation outside the
  crack within the gauge subtracted (p. 188; Fig. 11). At least 6 tests per Vf (p. 190).
- **Interface parameters:** single-fiber pullout (Redon et al. 2001 method, as cited) in M45 matrix
  containing 0.1, 0.5 and 2 vol.% PVA (p. 189). σfu and f′ by single-fiber in-situ strength test
  (Kanda & Li 1998, as cited). Em from initial slope of tensile σ–ε; σm by wedge-splitting test plus
  inverse analysis (p. 189).
- **Curing & test age:** demolded at 24 h, air cured at 50 ± 5% RH and 23 ± 2 °C to 28 d; tested at 28 d (p. 188).
- Mixing: 10 L Hobart mixer; dry solids, then water + SP for 3 min, then fibers (p. 188).
→ [[single-crack-test]], [[single-fiber-pullout-test]], [[dogbone-uniaxial-tension]]

## Model (equations transcribed from page images)
**Strain-hardening criteria** (p. 182–183):
- Energy (Marshall & Cox 1988, as cited): J_tip ≤ σ0·δ0 − ∫₀^δ0 σ(δ)dδ ≡ J′b (Eq. 1); J_tip → Km²/Em at small Vf.
- Strength: σc < σ0 (Eq. 2).

**Single fiber** (Lin & Li 1997, as cited):
- Debonding: σ_debonding = 2·√[(τ0·u + Gd)·2Ef(1+η)/df] (Eq. 3)
- Pull-out with slip hardening: σ_pullout = (τ0/df)(Le − u − δc)(1 + β(u − δc)/df) (Eq. 4)
- Full-debond displacement: δc = 2τ0Le²(1+η)/(Ef·df) + √[8Gd·Le²(1+η)/(Ef·df)] (Eq. 5)
- Snubbing: P(φ) = P(0)·e^{fφ} (Eq. 6)
- Fiber strength reduction (Kanda & Li 1998, as cited): σfu(φ) = σfu(0)·e^{−f′φ} (Eq. 7)
- Fiber rupture when load exceeds fiber strength, "often the case in PVA-ECC" because of strong slip hardening (p. 183).

**Two-way pull-out** (p. 184–185; Fig. 5):
- δ = δL + δS (Eq. 8); δL = δS for δ < 2δ0S (Eq. 9);
  Pd(δL) = Pp(δS, LS) for δS > δ0S and δL < δ0L (Eq. 10);
  Pp(δL, LL) = Pp(δS, LS) for δS > δ0S and δL > δ0L (Eq. 11).
- Pd(δ) = π·√[(τ0δ + Gd)·Ef·df³(1+η)/2] (Eq. 12)
- Pp(δ, L) = πτ0(L − δ + δ0)(df + β(δ − δ0)) (Eq. 13)
- δ0(L) = 2τ0L²(1+η)/(Ef·df) + √[8Gd·L²(1+η)/(Ef·df)] (Eq. 14); δ0L = δ0(LL), δ0S = δ0(LS) (Eqs. 15–16)
- Rationale: with β ≈ 0 or < 0 (PE, PP, smooth steel) the long side stays anchored; with strong PVA
  slip hardening the pull-out load exceeds the debond-end load, so the long side also debonds and slips (p. 184).

**Matrix micro-spalling** (p. 185–186):
- s = P·sin(φ/2) / (k·df·σm·cos²(φ/2)) (Eq. 17)
- δ′ = √(4s² + 4sδcosφ + δ²) (Eq. 18); φ′ = sin⁻¹(δ·sinφ/δ′) (Eq. 19); δeff = δ′ − 2s (Eq. 20), replacing δ in Eq. 8.
- Spalling lowers the effective inclination φ → φ′, which delays rupture of inclined PVA fibers.

**Averaging** (Wang et al. 1990, as cited; p. 186–187):
- σ(δ) = (1/(Af·Vf))·∫P(z,φ)p(z,φ)dz dφ (Eq. 21) — ⚠️ unverified: the prefactor prints as 1/(AfVf); the dimensionally expected form is Vf/Af. Transcribed as printed.
- p(z,φ) = p(z)p(φ) (Eq. 22); p(z) = 1/lf for −lf/2 ≤ z ≤ lf/2 (Eq. 23)
- 3-D random: p(φ) = sin φ (Eq. 24); 2-D random: p(φ) = 2/π, 0 ≤ φ ≤ π/2 (Eq. 25)
- Evaluated numerically with small δ increments (p. 187; flow chart Fig. 9).

**Cook–Gordon effect** (Li et al. 1993, as cited; p. 187):
- δcg = 4αP/(π·df²·Ef) (Eq. 26); σ = P·N_B (Eq. 27); N_B = (Af/Vf)·η_B (Eq. 28, prefactor as printed ⚠️ unverified);
  η_B ≡ ∫p(z,φ)dz dφ (Eq. 29); δcg = ασ/(Vf·Ef·η_B) (Eq. 30); δtot = δ + δcg (Eq. 31).

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| M45, 2% PVA ("typical", Fig. 1) | not reported | ≈ 4 (read from Fig. 1) ⚠️ | about 5 (p. 191; Fig. 1) | ≈ 4–4.5 (ultimate, read from Fig. 1) ⚠️ | about 60, constant after 1% strain (p. 181; Fig. 1) | age and specimen of Fig. 1 not reported |
| M45, 0.1% PVA (notched coupon, 28 d) | not reported | n/a (single crack) | peak bridging ≈ 0.25–0.35 (Fig. 12a, read) ⚠️ | n/a | δ at peak ≈ 0.1–0.2 mm (Fig. 12a) ⚠️ | model peak ≈ 0.35 MPa |
| M45, 0.5% PVA (notched coupon, 28 d) | not reported | n/a (single crack) | peak bridging ≈ 1.5–1.85 (Fig. 12b, read) ⚠️ | n/a | δ at peak ≈ 0.15–0.2 mm (Fig. 12b) ⚠️ | model peak ≈ 1.7 MPa |
| M45, 2% PVA (model, 2-D? see To verify) | — | — | predicted σ0 6.7 | — | δ0 130 µm (p. 191) / 133 µm (Fig. 14 text) | J′b not reported |

**Micromechanical inputs** (Table 2, Table 3, p. 190):
| Parameter | Value | How obtained |
|---|---|---|
| df / Lf / Ef | 39 µm / 12 mm / 22 GPa | measured |
| σfu (apparent) | 1060 MPa | single-fiber in-situ strength test |
| f (snubbing) | 0.2 | assumed: low end of 0.2–0.8 measured by Wu (2001) on 0.5%-oiled fiber, as cited (p. 189) |
| f′ (strength reduction) | 0.33 | single-fiber in-situ strength test |
| α (Cook–Gordon) | 78 µm (= 2df) | assumed: low end of Bentur's 2–10 df for steel; Li et al. 1993 used 15df for PP (p. 190) |
| Em | 20 GPa | initial slope of tensile σ–ε |
| σm | 5 MPa | wedge-splitting + inverse analysis |
| k (spalling) | 500 | calibrated: max observed spall 30 µm (p. 189–190) |

| Matrix type | τ0 (MPa) | Gd (J/m²) | β |
|---|---|---|---|
| M45 + 0.1 vol.% PVA | 1.91 | 1.24 | 0.63 |
| M45 + 0.5 vol.% PVA | 1.58 | 1.13 | 0.60 |
| M45 + 2 vol.% PVA | 1.31 | 1.08 | 0.58 |

Main findings (with Table/Fig. location):
- **Model validated:** the predicted mean σ(δ) curves for Vf 0.1 and 0.5% (2-D random orientation,
  coupon 13 mm thick vs 12 mm fiber) "fit well" with ≥ 6 tests each (p. 190; Fig. 12).
- **Experimental scatter:** peak bridging stress varies widely between specimens, but δ at peak stays
  fairly constant; attributed to varying number of bridging fibers (p. 190).
- **Interface bond falls with Vf:** τ0 1.91 → 1.31 MPa, Gd 1.24 → 1.08 J/m², β 0.63 → 0.58 from 0.1 to
  2 vol.%; attributed to higher air content / looser pores at higher Vf (p. 189; Table 3).
- **Mechanism contributions** for M45 2% (Fig. 14, p. 191):

  | Model | Peak σ0 (MPa) | δ at peak (µm) |
  |---|---|---|
  | 1-way pull-out (Lin et al. 1999) | 6.2 | 93 |
  | 2-way | 6.3 | 130 |
  | 2-way + spalling | 6.7 | 131 |
  | 2-way + spalling + Cook–Gordon | 6.7 | 133 |

  Two-way pull-out mainly raises δ0; spalling mainly raises σ0 (delays rupture of inclined fibers);
  Cook–Gordon is negligible for α = 2df (p. 191).
- **Weakest-plane method (the "min(Vf)" idea, primary source):**
  - Predicted mean σ0 (6.7 MPa) is 25% above the observed σ_tu of about 5 MPa (p. 191).
  - Curves for Vf = 1.5 / 2.0 / 2.5 vol.% (±25%) represent plane-to-plane variation (Fig. 13a);
    peaks ≈ 5 / 6.7 / 8.4 MPa (8.4 read from Fig. 13a ⚠️).
  - The weakest plane dominates; localization occurs when it reaches its peak (5 MPa for M45) (p. 191).
  - Crack width = δ on each curve at σ = 5 MPa: **37 to 133 µm, "mean" 62 µm**, matching the ≈ 60 µm
    of Fig. 1 (p. 191; Fig. 13b).
- Single-fiber pullout in M45: Le = 0.597 mm pulled out (peak ≈ 0.53 N); Le = 1.18 mm ruptured
  (≈ 0.96 N); slip-hardening load after debonding exceeds the debond-end load (Fig. 4, p. 184; loads read from figure ⚠️).
- Predicted spall size 0–28 µm for typical PVA loads (k = 500, σm = 5 MPa, df = 39 µm); observed up to
  30 µm; elastic stretch of spall-freed segments < 2 µm at 60 µm crack width, so neglected (p. 185; Fig. 6).
- Average crack spacing in PVA-ECC about 1 mm (p. 188).

## Mechanisms / explanations offered by authors
- σ(δ) governs both PSH criteria: J′b (Eq. 1) and σ0 (Eq. 2) (p. 183). → [[strain-hardening]]
- PVA slip hardening (β > 0) is due to abrasion and jamming in the matrix tunnel (Redon & Li 2001, as
  cited) and causes two-way debonding/pull-out (p. 184).
- Matrix spalling relieves stress concentration and reduces φ, delaying rupture of inclined PVA fibers,
  which have strong inclination strength loss (f′) (p. 185).
- Cook–Gordon effect is small for hydrophilic PVA (strong chemical bond, small α) but may be important
  for hydrophobic PE and PP fibers with near-zero chemical bond and larger α (p. 191).
- Higher fiber content in a crack plane raises the load but crack opening is limited by a stiffer
  averaged fiber "spring", so δ at peak stays nearly constant (p. 190).
- Lower bond at higher Vf: higher air content and looser pore structure (p. 189).

## Limitations (stated + observed)
- Stated: validation used reduced Vf (0.1, 0.5%) because 2% gives multiple cracks with ~1 mm spacing;
  interface properties change with Vf but mechanisms are assumed unchanged (p. 188).
- Stated: f and α are assumed, not measured, "for lack of more precise experimental evidence" (p. 189–190).
- Observed: the ±25% Vf variation is back-calculated from the 5 MPa vs 6.7 MPa gap, not measured
  (no fiber-count or fluorescence data) (p. 191).
- Observed: the reported "mean of 62 µm" does not equal the arithmetic mean of 37 and 133 µm with the
  middle curve's value (≈ 65 µm from Fig. 13b); 62 µm appears to be the δ on the mean (2%) curve. ⚠️
- Observed: δ0 for the 2% model is given as 130 µm (p. 191, para. 1) and 133 µm (Fig. 14 text).
- Observed: Fig. 1 test conditions (age, specimen, rate) not reported.
- Observed: whether Fig. 13–14 (2% curves) use 2-D or 3-D orientation is not stated.
- Single matrix (M45) and single fiber (REC-15 PVA); no PE or high-strength matrix.

## Relation to other work
- Agrees with: [[li2002-pva-ecc-interface-tailoring]] — same Michigan PVA fiber (39 µm, 12 mm, 1.2% oil);
  ≈ 60 µm crack width falls inside the 43–88 µm range there.
- Contradicts: ⚔️ β = 0.58–0.63 here vs 1.15 for the same 1.2%-oiled fiber in a w/c 0.45 non-FA matrix
  ([[li2002-pva-ecc-interface-tailoring]], Table 3). Different matrix (M45 with FA/C 1.2) and test.
  Supports the "β ≈ 0.6" value cited from Wang & Li 2007 in [[ranade2015-hshdc-tensile-rate-effects]].
- Extends: Lin, Kanda & Li 1999 (as cited) by adding two-way pull-out, spalling and Cook–Gordon;
  [[li1992-steady-state-multiple-cracking]] (friction-only pullout and energy criterion).
- Used by: [[ranade2015-hshdc-tensile-rate-effects]] (min σ0 = σ0·min(Vf)/Vf; crack width at min σ0).
  Note that Ranade uses a measured min(Vf) = 0.80·Vf, whereas this paper infers a −25% Vf from σ_tu.

## Pages updated from this source
- [[fiber-bridging]]
- [[fiber-matrix-interface]]
- [[crack-width]]
- [[fiber-dispersion]]
- [[strain-hardening]]
- [[pva-fiber]]
- [[fly-ash]]
- [[single-crack-test]]
- [[single-fiber-pullout-test]]
- [[tensile-constitutive-model]]
- [[micromechanical-parameters]]
- [[mix-designs]]
- [[mechanical-results]]

## To verify
- [ ] DOI 10.3151/jact.6.181 (not printed in the PDF).
- [ ] Eq. 21 and Eq. 28 prefactor printed as 1/(AfVf) and Af/Vf; dimensionally Vf/Af is expected.
- [ ] "Mean of 62 µm" in Fig. 13b: arithmetic mean of three δ values or δ on the 2% curve?
- [ ] δ0 for 2% model: 130 µm (p. 191) vs 133 µm (Fig. 14 discussion).
- [ ] Orientation assumption (2-D vs 3-D) for the 2% predictions in Fig. 13–14.
- [ ] Values read from figures: Fig. 1 first-crack ≈ 4 MPa and ε ≈ 4–4.5%; Fig. 12 experimental peaks; Fig. 13a peak 8.4 MPa for 2.5%; Fig. 4 pullout loads.
- [ ] Fig. 1 specimen type, age and loading rate.
