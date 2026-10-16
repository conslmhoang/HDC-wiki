---
type: source
slug: li1992-steady-state-multiple-cracking
title: "Steady-State and Multiple Cracking of Short Random Fiber Composites"
authors: [Victor C. Li, Christopher K. Y. Leung]
year: 1992
venue: "Journal of Engineering Mechanics (ASCE), Vol. 118, No. 11, November 1992, pp. 2246–2264 (Paper No. 2500; submitted 21 Aug 1991)"
doi: "not reported in PDF"
raw_file: "raw/papers/Li1992_STEADY-STATE AND MULTIPLE CRACKING OF SHORT RANDOM FIBER COMPOSITES.pdf"
material_term: "short (discontinuous) random fiber composites / brittle-matrix composites; fiber reinforced cementitious composites (FRC); behaviour called 'pseudostrain hardening'. The terms ECC, SHCC and HDC are not used."
study_type: "analytical (fracture mechanics + micromechanics), with literature data used for comparison"
tags: [micromechanics, steady-state-cracking, multiple-cracking, pseudo-strain-hardening, critical-fiber-volume, snubbing, fracture-mechanics, design-theory]
ingested: 2026-10-16
updated: 2026-10-16
---

# Steady-State and Multiple Cracking of Short Random Fiber Composites (Li & Leung, 1992)

## One-paragraph summary
This is a foundational analytical paper for what later became ECC/SHCC design theory. It treats fiber
bridging as a cohesive traction on the flanks of a penny-shaped matrix crack. It balances stress-intensity
factors (K_L + K_B = K_tip) to derive the **first-crack strength** of a composite with 3-D random,
discontinuous, flexible fibers that pull out by friction. The bridging law includes the
**snubbing effect** of inclined fibers. Two nondimensional parameters control the tensile failure mode:
- **K̃**: a ratio of crack-tip toughness to fiber-bridging toughness. It equals (10/(3√π))·(G_tip/G_r).
- **c̃**: a normalized flaw size.

**Steady-state (flat) cracking** needs K̃ ≤ K̃_crit = 1/(3√π) ≈ 0.188. This is equivalent to
G_r ≥ 10 G_tip and gives a closed-form **critical fiber volume fraction V_f^crit** (Eq. 17).
**Multiple cracking** also needs the flaw size to exceed a minimum c̃_mc (Eq. 24). A K̃–c̃
**failure-mechanism map** (Fig. 7) shows four tensile behaviours (modes A–D). The authors match these
modes to published curves for Spectra-PE, steel, PP and glass FRC (Table 2, Fig. 8). The paper calls
steady-state cracking a prerequisite of pseudo strain-hardening (p. 2247). → [[strain-hardening]],
[[multiple-cracking]], [[fiber-bridging]]

## Objective / research question
- Under what conditions can a discontinuous, randomly oriented short-fiber brittle-matrix composite show
  the ductile features of a continuously reinforced composite: a higher first-crack strain, steady-state
  cracking and multiple cracking (p. 2246)?
- How can these conditions be stated with nondimensional micromechanical parameters, so that
  composites can be designed for pseudo strain-hardening (p. 2246, p. 2259)?

## Materials & mix design
This is an analytical paper with no mixes of its own. The table below lists the **parameter cases** the
authors use (Tables 1 and 2, Fig. 6). Mix proportions are not reported for any case.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| T1-Steel (Table 1) | OPC matrix (proportions n/a) | n/a | n/a | not reported | not reported | not reported | steel, Ef 200 GPa, τ 7 MPa | 25 (computed here: Lf/df 100 × 250 µm) | 250 | V_f^crit = 3.6 (output) |
| T1-Glass (Table 1) | OPC matrix | n/a | n/a | not reported | not reported | not reported | glass, Ef 80 GPa, τ 0.3 MPa | 36 (computed here: 3000 × 12 µm) | 12 | V_f^crit = 0.4 (output) |
| T1-Carbon (Table 1) | OPC matrix | n/a | n/a | not reported | not reported | not reported | carbon (pitch), Ef 40 GPa, τ 8 MPa | 3 (computed here: 200 × 15 µm) | 15 | V_f^crit = 0.6 (output) |
| T1-PP (Table 1) | OPC matrix | n/a | n/a | not reported | not reported | not reported | PP, Ef 6 GPa, τ 0.7 MPa | 13 (computed here: 186 × 70 µm) | 70 | V_f^crit = 2.9 (output) |
| Fig6-steel | not reported | n/a | n/a | not reported | not reported | not reported | steel, Ef 200 GPa, τ 7 MPa | 10 | 20 / 50 / 70 | 0–25 (varied) |
| T2-Glass (Ali et al. 1975) | OPC paste | n/a | n/a | none (paste) | not reported | not reported | glass, Ef 76 GPa | not reported | not reported | 8.2 |
| T2-PP (Baggott 1983) | lightweight mortar | n/a | n/a | lightweight (not specified) | not reported | not reported | PP, Ef 2 GPa | not reported | not reported | 5.0 |
| T2-Spectra (Green 1989) | high-strength concrete | n/a | n/a | not reported | not reported | not reported | Spectra (high-modulus PE), Ef 120 GPa | not reported | not reported | 0.6 |
| T2-Steel (Shah et al. 1979) | OPC mortar | n/a | n/a | not reported | not reported | not reported | steel, Ef 200 GPa | not reported | not reported | 1.73 |

Units of binder quantities: not applicable (analytical paper; no mix proportions are given).
- Table 1 matrix: Em = 20 GPa, Gm = 100 × 10⁻⁶ MPa·m (= 100 J/m², converted here) (Table 1 note, p. 2254).
- The fiber lengths for Table 1 are computed here from Lf/df × df. They are not stated in the paper.

### Model assumptions (p. 2247–2250, App. I)
- Fibers are held by **friction only**: little or no elastic bond, with a constant frictional bond
  strength τ.
- Fibers are short enough, or τ low enough, that **all fibers pull out without rupture**.
- Fibers are **flexible**, so snubbing is active. For stiff, brittle fibers, fiber rupture or matrix
  spalling may make snubbing unusable (Leung & Li 1992, as cited, p. 2248).
- Fiber distribution is **uniform 3-D random**: p(φ) = sin φ and p(z) = 2/Lf (p. 2248).
- The elastic stretch of the fiber after full debonding is neglected (p. 2247).
- The prepeak bridging law (Eq. 4) drops higher-order terms in δ̃/δ̃* (p. 2248).
- The crack is penny-shaped, with radius c.
- The **crack profile is parabolic**, as under uniform bridging (Eq. 11). Marshall et al. (1985, as
  cited) found that this overestimates the first-crack strength by about 20% for continuous fibers (p. 2250).
- K_tip = Km for small Vf; otherwise K_tip = (Ec/Em)·Km (p. 2250).
- Ec comes from the rule of mixtures. This is an upper bound, with errors under 10% for Vf below
  about 10% (p. 2260).
- The matrix-deformation term η(1 − e^{fθ}cos θ) is dropped from Eq. 34. This causes less than 5% error
  when η < 0.1 and f ≤ 1. Eq. 34 must be used for Vf about 10% with f about 1 (p. 2262).

### Governing equations (transcribed from page images)
- **Single-fiber pullout, debonding stage** (Eq. 1, p. 2247):
  P(δ) = (π/2)·√[(1+η)·Ef·df³·τ·δ]·e^{fφ}, for δ ≤ δ0
  - δ0 = 4l²τ / [(1+η)·Ef·df], with l = embedment length.
  - η = Vf·Ef / (Vm·Em).
- **Slippage stage** (Eq. 2): P(δ) = π·τ·l·df·(1 − δ/l)·e^{fφ}, for l/2 ≥ δ > δ0.
- **Composite bridging stress** (Eq. 3, Li, Wang & Backer 1991, as cited):
  σ_B(δ) = (4Vf/(π·df²)) ∫_{φ=0}^{π/2} ∫_{z=0}^{(Lf/2)cosφ} P(δ)·p(φ)·p(z) dz dφ
- **Normalized prepeak bridging law** (Eq. 4):
  σ̃_B(δ̃) = g·[2(δ̃/δ̃*)^{1/2} − δ̃/δ̃*], for δ̃ ≤ δ̃*
  - σ̃_B = σ_B/σ0, with **σ0 = Vf·τ·(Lf/df)/2** (the peak bridging stress when g = 1).
  - δ̃ = δ/(Lf/2).
  - δ̃* = [2τ/((1+η)Ef)]·(Lf/df).
  - The peak bridging stress is therefore g·σ0, at δ̃ just below δ̃* (p. 2248).
- **Snubbing factor** (Eq. 5): g = [2/(4 + f²)]·(1 + e^{πf/2}). f is the snubbing coefficient,
  measured at 0.5–1 for three fiber types in cement (Li et al. 1990; Li 1992, as cited, p. 2247).
- **Prepeak bridging fracture energy** (Eq. 6): G_r = (5/24)·g·τ·Vf·df·(Lf/df)²·δ̃*. This is the
  area **under** the prepeak σ_B–δ curve, from 0 to δ*.
- **Stress-intensity balance** (Eq. 7): K_L + K_B = K_tip.
- **Applied load** (Eqs. 8–9): K̃_L = K_L/(σ0√c0) = 2√(c̄/π)·σ̃.
  - c0 = (Lf·Ec/(2K_tip))²·π/[16(1−ν²)²].
  - c̄ = c/c0.
- **Bridging** (Eq. 10): K̃_B = −2√(c̄/π) ∫₀¹ σ̃_B(δ̃)·R dR/√(1−R²).
- **Crack profile** (Eq. 11): δ̃ = √[c̄(1−R²)].
- **First-crack strength** (Eq. 12): σ̃_fc/g = (√π/2)·(K̃/c̃) + (4/3·√c̃ − c̃/2).
  - K̃ ≡ (K_tip/(σ0√c0))/(g·δ̃*).
  - c̃ ≡ √c̄/δ̃*.
  - The first term is the strength from matrix toughness. The second term is the strength from
    fiber bridging.
- **Steady-state onset** (Eqs. 13–14): σ̃_m = σ̃_B(δ̃_m = √c̄) = σ̃_fc. This gives
  K̃ = (2/√π)·c̃_s·(2/3·√c̃_s − c̃_s/2), for 0 ≤ c̃_s ≤ 1.
- **Critical K̃** (p. 2251): at c̃_s = c̃_p = 1, **K̃_crit = 1/(3√π) ≈ 0.188**.
- **Energy form of K̃** (Eq. 15): K̃ = [10/(3√π)]·(G_tip/G_r).
- **Steady-state requirement** (Eqs. 16–17):
  - **G_r ≥ 10·G_tip** (Eq. 16).
  - **V_f ≥ V_f^crit = 48·G_tip / [g·τ·df·(Lf/df)²·δ̃*]** (Eq. 17).
- **Steady-state cracking strength** (Eq. 18): σ̃_ss = g·(2√c̃_s − c̃_s). With Eq. 14, this gives a
  parametric pair in c̃_s.
- **Steady-state strain**: ε_ss = σ_ss/Ec, assuming the composite is linear up to steady-state cracking (p. 2254).
- **Long-fiber (ACK) limit** (Eqs. 19–21): σ̃_ss = g·(6√π·K̃)^{1/3}.
  - ε_ss = [3g²·Vf²·τ·Gm·Ef / (Ec·Em²·rf·Vm)]^{1/3}.
  - Gm/Em = (1/Ec)·((1−ν²)K_tip²/Ec).
- **ACK theory** (Eq. 22, Aveston et al. 1971, as cited): ε_mu = [12·Vf²·τ·γm·Ef / (Ec·Em²·rf·Vm)]^{1/3}.
  - Eq. 20 is equivalent to Eq. 22 when Gm = 2γm and g = 1.
  - A factor of 2 remains because Eq. 20 is for 3-D random fibers and Eq. 22 is for aligned
    continuous fibers (p. 2254–2255).
- **Multiple-cracking condition** (Eq. 23a/b): σ_fc(c) ≤ g·σ0, i.e. σ̃_fc(c̃)/g ≤ 1.
- **Minimum flaw size for multiple cracking** (Eq. 24): (√π/2)·(K̃/c̃_mc) + (4/3·√c̃_mc − c̃_mc/2) = 1.
- **Complete multiple-cracking criteria** (Eq. 25a/b): **K̃ ≤ K̃_crit** and **c̃_mc ≤ c̃**.
- **Small-specimen condition** (p. 2259): when K̃ > K̃_crit, a small rise in load is possible before full
  separation if s/2 < c0·δ̃*², where s is the specimen cross-section size.
- **Appendix I** (Eqs. 26–35): shear-lag derivation, following Leung & Li (1991, as cited).
  - Eq. 32 is identical to Marshall et al. (1985, as cited).
  - Inclined fiber (Eq. 34): P(δ) = (π/2)√[(1+η)Ef·df³·τ·δ]·e^{fθ} / [1 + η(1 − e^{fθ}cos θ)].
  - Eq. 35 is Eq. 34 without the denominator.

## Test methods
- Specimen geometry: not applicable (analytical paper). The model is a penny-shaped matrix crack of
  radius c in a uniaxially tensioned body. Table 2 gives specimen half-widths s/2 = 25 mm (Spectra) and
  100 mm (steel), taken from the cited experiments.
- Loading / rate: quasi-static uniaxial tension (implied by the model); rate not reported.
- Measurement (LVDT, DIC, ...): not applicable. The comparison curves in Fig. 8 come from the literature
  (Green 1989; Shah et al. 1979; Baggott 1983; Ali et al. 1975, as cited); their instrumentation is not reported.
- Curing & test age: not reported.
→ [[dogbone-uniaxial-tension]] (the type of test the model predicts), [[single-fiber-pullout-test]] (the source of τ and f)

## Key results
These are model outputs; no test is reported.

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| T1-Steel | not reported | not reported | not reported | not reported | not reported | V_f^crit = 3.6% (Table 1) |
| T1-Glass | not reported | not reported | not reported | not reported | not reported | V_f^crit = 0.4% |
| T1-Carbon | not reported | not reported | not reported | not reported | not reported | V_f^crit = 0.6% |
| T1-PP | not reported | not reported | not reported | not reported | not reported | V_f^crit = 2.9% |
| Fig6-steel, df 20/50/70 µm | not reported | rises with Vf, up to about 350 MPa at Vf 25% for 20 µm (read from Fig. 6 ⚠️) | not reported | not reported | not reported | V_f^crit marked on each curve; it falls as df falls (p. 2255) |
| T2-Glass | not reported | not reported | not reported | not reported | not reported | K̃ 0.00027, c̃ 0.0055, c̃_s 0.0053, c̃_mc 0.001: **mode D** |
| T2-PP | not reported | not reported | not reported | not reported | not reported | K̃ 0.0016, c̃ 0.018, c̃_s 0.02, c̃_mc 0.011: **mode C** |
| T2-Spectra (PE) | not reported | not reported | not reported | not reported | not reported | K̃ 0.65, c̃ 0.38, s/2 25 mm, c_p 246 mm: **mode A** |
| T2-Steel | not reported | not reported | not reported | not reported | not reported | K̃ 0.91, c̃ 0.65, s/2 100 mm, c_p 71 mm: **mode B** |

Table 2 inputs:
- τ, Gm and Km are assumed values. The flaw size c is an assumed effective value.
- The values are set so that the measured matrix tensile strength and the composite first-crack
  strength are matched (p. 2259).
- τ: 0.3 / 0.5 / 1.0 / 2.5 MPa for glass / PP / Spectra / steel.
- Gm: 1.5 / 4.5 / 20.0 / 18.0 × 10⁻⁶ MPa·m. Converted here, this is 1.5 / 4.5 / 20 / 18 J/m².
- Km: 0.2 / 0.1 / 0.63 / 0.6 MPa√m.
- Em: 26 / 2.2 / 20 / 20 GPa. The Spectra and steel values carry an asterisk mark.
- c: 6 / 6 / 20 / 30 mm.
- Check: Gm ≈ Km²/Em holds for all four rows (computed here).

Main findings (with Table/Fig. location):
- **Steady-state cracking is a prerequisite for multiple cracking and pseudo strain-hardening.** It occurs
  when rising bridging stress during debonding reaches the applied load. The crack flanks then flatten,
  and the crack spreads at constant load σ_ss (p. 2247, p. 2251).
- **Two conditions for steady-state cracking** (p. 2251, Fig. 2):
  1. The midpoint bridging stress σ_m must equal σ_fc.
  2. The midpoint opening δ_m must be below δ_p, the opening at peak bridging stress.
- **K̃_crit = 1/(3√π) ≈ 0.188** (p. 2251, Eq. 14).
  - Composites with K̃ > K̃_crit fail at σ_fc, which depends on flaw size. They stay **notch-sensitive**,
    like a Griffith material.
  - Composites with K̃ < K̃_crit fail at σ_ss. They are **notch-insensitive** when c̃ > c̃_s (Fig. 3).
  - c̃_s → ∞ as K̃ → K̃_crit (Fig. 4).
- **G_r ≥ 10 G_tip** (Eq. 16).
  - G_r scales linearly with Vf and g, with τ², and with (Lf/df)³ (p. 2252–2253).
  - Raising any of these lowers K̃.
- **V_f^crit for typical FRCs is 0.5–4%** (p. 2253; Table 1 gives 0.4–3.6%).
  - Higher matrix fracture energy needs more fiber.
  - Small-diameter fibers (carbon, glass) need less fiber (p. 2254).
- **Doubling the aspect ratio through Lf cuts the fiber needed by 87.5%** (p. 2259). This follows from
  V_f^crit ∝ (Lf/df)⁻³.
- **The long-fiber (ACK) formula, Eq. 19, has more than 10% error for K̃ > 0.05**, so Eqs. 14 and 18
  should be used for short fibers (p. 2255, Fig. 5).
- **Smaller fiber diameter raises the first-crack strength and lowers V_f^crit** (steel, Lf = 10 mm,
  c = 20 mm, Gm = 100 × 10⁻⁶ MPa·m; Fig. 6, p. 2255).
- **Failure-mechanism map (K̃–c̃)** (Fig. 7, p. 2256–2257). The shaded region (low K̃, high c̃) gives
  pseudo strain-hardening.
  - **D** (K̃ < K̃_crit, c̃ > c̃_s): steady-state cracking at σ_ss, then multiple cracking until the load
    rises to σ0 (pseudo strain-hardening).
  - **C** (K̃ < K̃_crit, c̃_mc < c̃ < c̃_s): multiple cracking with an initial load drop at first crack,
    then a rising load.
  - **Left of c̃_mc**: σ_fc can be much higher than σ0. The load drops suddenly, rises to σ0, then
    softens on a single crack.
  - **A** (K̃ > K̃_crit, s < c_p): first-crack drop, then a small rise before separation.
  - **B** (K̃ > K̃_crit, s > c_p): catastrophic, Griffith-type failure.
  - In all cases fiber pullout gives R-curve behaviour (p. 2259).
- **Model modes match published curves** (Fig. 8, Table 2):
  - Spectra-PE FRC in high-strength concrete (Vf 0.6%): A.
  - Steel FRC: B.
  - PP in lightweight mortar: C.
  - Glass FRC in OPC paste: D.
  - The Spectra FRC strength was below the matrix strength. This needs a very large effective flaw
    size, which the authors attribute to poor workability (p. 2259).
- **Snubbing raises bridging** (Fig. 1). The normalized peak is about 1.0 at f = 0, about 1.3 at
  f = 0.4 and about 1.7 at f = 0.8 (read from Fig. 1 ⚠️). It also raises the steady-state strength,
  though the strength stays below that of a continuous-fiber system (p. 2260).

## Mechanisms / explanations offered by authors
- Fiber bridging acts as a **growing fracture resistance** (an R-curve) with crack extension. It raises
  the first-crack strength. If the stress-transfer capability is adequate, it also produces steady-state
  cracking (p. 2247).
- **Load transfer back to the matrix:** after the first crack, the fibers must carry their own load plus
  the load the matrix sheds. If they can, they pass load back to the matrix through interfacial shear and
  form a new crack. This repeats until a set of periodic, subparallel cracks forms. If they cannot, they
  pull out (p. 2255).
- **Snubbing:** a fiber inclined at angle φ gets extra pullout force e^{fφ} from local fiber/matrix
  friction at the exit point. This partly offsets the efficiency loss of random, discontinuous fibers
  (p. 2246–2247). → [[fiber-matrix-interface]]
- **Design levers** (p. 2259): tailor τ/Ef, Lf/df and Gm/(g·τ·df) to reduce V_f^crit, lower cost and
  ease processing. If c̃_s is below the fabrication flaw size, the composite becomes notch-insensitive and
  more reliable. For multiple cracking, c̃_mc must be below the fabrication flaw size. → [[fiber-geometry]],
  [[matrix-fracture-toughness]]

## Limitations (stated + observed)
- Stated:
  - The parabolic crack profile is an approximation; it gives about 20% overestimation for continuous
    fibers (p. 2250).
  - Rule-of-mixtures Ec is an upper bound, with errors under 10% for Vf < 10% (p. 2260).
  - Eq. 35 is accurate only for small η and f ≤ 1 (p. 2262).
  - One-way debonding is accurate up to 90% of peak pullout load for weakly bonded fibers. Two-way
    debonding needs iteration and is not used (p. 2261).
  - The model holds only where friction-dominated pullout without fiber rupture describes the
    composite (p. 2260).
- Observed:
  - **No chemical bond (G_d) and no slip-hardening** are included. Both later proved important for
    PVA-ECC.
  - Fiber rupture is excluded, so the model does not apply to high-strength matrices where PE or PVA
    fibers rupture.
  - **Matrix tension-softening is ignored.**
  - Table 2 τ, Gm, Km and c are back-fitted assumptions, so the mode predictions are consistency checks,
    not blind predictions.
  - There is no strain-capacity or crack-width prediction beyond ε_ss = σ_ss/Ec at first crack.
  - The paper does **not** use the J-integral energy criterion (J_tip ≤ σ0δ0 − ∫σdδ) that is used in
    later ECC papers.

## Relation to other work
- Agrees with:
  - The strength-type multiple-cracking condition σ_fc ≤ g·σ0 (Eq. 23a) is the 1992 form of the strength
    criterion that later sources cite from Kanda & Li 1998 ([[ranade2015-hshdc-tensile-rate-effects]];
    [[su2023-rubber-modified-hshdc]]).
  - Eq. 3 is the same scale-linking integral cited in [[fiber-bridging]].
- Contradicts: ⚔️ none directly. Refinement: this paper's energy condition is
  **G_r (area under the prepeak σ–δ curve) ≥ 10·G_tip**, written in stress-intensity and K̃ form.
  The wiki's [[strain-hardening]] page states the later energy criterion with the **complementary**
  energy J′b ≥ J_tip. The two are not the same expression and should not be merged.
- Extends:
  - The ACK theory (Aveston et al. 1971) and Marshall et al. (1985) / Marshall & Cox (1987), as cited:
    from aligned continuous fibers to 3-D random discontinuous fibers with snubbing.
  - It recovers ACK in the long-fiber limit (Eqs. 19–22).

## Pages updated from this source
- [[strain-hardening]] · [[multiple-cracking]] · [[fiber-bridging]] · [[fiber-matrix-interface]] ·
  [[fiber-geometry]] · [[matrix-fracture-toughness]] · [[micromechanical-parameters]] · [[pe-fiber]] ·
  [[size-effect]] · [[terminology-hdc-ecc-shcc]]
- (This list gives the intended updates. Only this source page was written in this pass.)

## To verify
- [ ] DOI is not printed in the PDF. A DOI of the form 10.1061/(ASCE)0733-9399(1992)118:11(2246) is
  likely but ⚠️ unverified.
- [ ] Table 1 V_f^crit values could not be reproduced here from Eq. 17 with g = 1, η = 0 and
  G_tip = Gm. That calculation gives about 3.9 / 0.66 / 1.25 / 6.5% against the printed
  3.6 / 0.4 / 0.6 / 2.9%. The snubbing coefficient f (g) and any η or Ec correction used for Table 1 are
  not stated ⚠️ unverified.
- [ ] Table 2 Em values for Spectra and steel carry a "*" mark that differs from the "a" (assumed)
  footnote. Its meaning is unclear ⚠️ unverified.
- [ ] Text (p. 2259) says "computed c value (246 mm)" for Spectra, but Table 2 column 15 lists this as
  c_p. This is probably a typo in the text.
- [ ] Fig. 1 peak values (about 1.3 at f = 0.4, about 1.7 at f = 0.8) and the Fig. 6 strength (about
  350 MPa) are read from plots ⚠️ unverified.
- [ ] Table 2 Gm values (1.5–20 J/m²) are much lower than the Table 1 value (100 J/m²). This is
  consistent with Km²/Em as printed, but the large difference is worth noting.
- [ ] The Spectra fiber length and diameter for the Green (1989) data are not given in this paper.
