---
type: source
slug: ranade2017-hshdc-impact-resistance
title: "Impact resistance of high strength-high ductility concrete"
authors: [Ravi Ranade, Victor C. Li, William F. Heard, Brett A. Williams]
year: 2017
venue: "Cement and Concrete Research 98 (2017) 24–35 (received 14 Jan 2016, revised 5 Dec 2016, accepted 27 Mar 2017, online 18 Apr 2017)"
doi: "10.1016/j.cemconres.2017.03.013"
raw_file: "raw/papers/Ranade2017_Impact resistance of high strength-high ductility concrete.pdf"
material_term: "HSHDC (High Strength-High Ductility Concrete), described as a fiber-reinforced cementitious composite; compared with Cor-Tuf, which the authors call a tension-softening, deflection-hardening FR-UHPC (Fiber-Reinforced Ultra-High Performance Concrete)"
study_type: "experimental (drop-weight impact on thin slabs) + numerical (3D rate-dependent FE, LS-Dyna)"
tags: [hshdc, pe-fiber, impact, drop-weight, slab, uhpc, cor-tuf, fe-analysis, extreme-loading]
ingested: 2026-10-06
updated: 2026-10-06
---

# Impact Resistance of HSHDC (Ranade, Li, Heard & Williams, 2017)

## One-paragraph summary
Unreinforced thin slabs (300 × 300 × 25 mm) of [[hshdc]] (PE fiber 2 vol.%, f'c 166 MPa,
ε_tu 3.4%) and of Cor-Tuf (hooked steel fiber 3.26 vol.%, f'c 201 MPa, tension-softening) are
hit repeatedly by a 16.04 kg drop weight with a 75 mm flat cylindrical head. Impact velocities are
2.30, 3.25 and 4.60 m/s, with up to 20 impacts or until failure (2 slabs per case).
Results:
- At 2.30 m/s, the peak contact force (PCF) of both materials stays roughly constant over 20 impacts.
- At 3.25 and 4.60 m/s, the Cor-Tuf PCF drops sharply after about 6 impacts and the slabs fail in
  flexure before the 20th impact. The exception is C3.25-1, which survives but with a much lower PCF.
- The HSHDC PCF stays almost constant at all velocities. The HSHDC slabs survive 20 impacts with
  many fine radial cracks and almost no spalling.

With a smaller 50 mm head, Cor-Tuf fails by punching shear at impact 15, while HSHDC still bends
in a ductile way without failure. A 3D rate-dependent LS-Dyna model reproduces the maximum
displacements within 13% but over-predicts PCF by 34–75%. The model shows a diffuse tensile strain
field (< 1%) on the HSHDC back face, against localised strains up to 3% in Cor-Tuf. The authors
conclude that the better impact resistance comes from HSHDC's tensile ductility, combined with
its high compressive strength. → [[extreme-loading-applications]], [[impact-test]]

## Objective / research question
- Test the hypothesis that the combination of high compressive strength and tensile ductility
  (HSHDC) gives better impact resistance than a strong but tension-softening FR-UHPC (Cor-Tuf) (p. 25).
- The study compares two high-performance concretes directly, unlike most earlier studies that
  compared one of them with normal concrete (p. 25, "Research significance").
- Use FE analysis to explain failure modes, crack patterns and stress/strain fields that are hard
  to measure (p. 25, 31).
- HSHDC vs SHCC/ECC (the effect of compressive strength) is deferred to a future study (p. 25).

## Materials & mix design
Table 1 (p. 26). Mass ratio to cement, with kg/m³ in parentheses. Fibers from Table 2.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| HSHDC | 1 (907), Class H, 30–80 µm | 0 | silica fume 0.389 (353), 0.1–1 µm; silica flour 0.277 (251), 5–100 µm | silica sand 0.700 (635), 100–600 µm | 0.15 (w/cm, by mass); water/c 0.208 (189 kg/m³ tap water) | HRWRA 0.0176 (16), total | UHMWPE ("PE"), 3000 MPa, 100 GPa | 12.7 | 28 | 2 (fiber 0.0214, 19 kg/m³) |
| Cor-Tuf | 1 (817), Class H | 0 | silica fume 0.389 (318); silica flour 0.277 (226) | silica sand 0.967 (791), 100–600 µm | 0.15 (w/cm, by mass); water/c 0.208 (170) | HRWRA 0.0151 (12), total | hooked steel, 1300 MPa, 210 GPa | 30 | 550 | 3.26 (fiber 0.313, 256 kg/m³) |

Units of binder quantities: mass ratio to cement plus kg/m³ (Table 1).
- The HSHDC mix is **identical** to the final HSHDC (HSHDC-S0.70) in Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source)
  and [[ranade2015-hshdc-tensile-rate-effects]]. The HRWRA is 0.0176 here vs the rounded 0.018 in the wiki rows.
- Fresh state (p. 25):
  - matrix viscosity / yield stress: HSHDC 6.0 Pa·s / 186.2 Pa; Cor-Tuf 5.5 Pa·s / 170 Pa;
  - slump about 190 mm for both (ASTM C143, with fibers). → [[fresh-properties]]
- Curing (p. 27):
  - demould at 2 d;
  - 7 d in water at room temperature;
  - 5 d in water at 90 °C;
  - 3 d in air at 90 °C. → [[heat-curing]]

## Test methods
- Specimen geometry:
  - **Impact:** unreinforced square slabs, 300 × 300 × 25 mm (Fig. 2, p. 27). Cast by pouring at
    the mould centre, then moderate table vibration.
  - **Tension (material characterisation, from [33,36]):** dogbone 330 mm long, 12.7 mm thick,
    30 mm wide over an 80 mm narrow section, 90 mm LVDT gauge length (Fig. 1b–c).
  - **Compression:** 51 mm and 76 mm cubes.
- Loading / rate:
  - Drop-weight tower (Fig. 3). The impact head is mounted under an adjustable loading tray that
    slides on two 25 mm guide shafts and is released by an electromagnet.
  - Instrumented series: 75 mm cylindrical steel head, 16.04 kg, drop heights 0.35 / 0.70 / 1.40 m,
    giving measured impact velocities 2.30 / 3.25 / 4.60 m/s (Table 3).
    - The kinetic energy at 3.25 and 4.60 m/s is 2× and 4× that at 2.30 m/s (p. 29).
    - KE = ½mv² gives about 42, 85 and 170 J (computed here).
  - Non-instrumented series: 50 mm head, 16.11 kg, 0.70 m, 3.25 m/s.
  - Repeat until 20 impacts or "slab failure" (almost zero rebound, from flexural failure or head
    penetration), whichever comes first. 2 slabs per material per case (p. 28).
  - The strain rates in moderate-velocity impact are stated as **0.1–10 s⁻¹** (p. 26).
  - Support: steel specimen holder on a heavy steel base (Fig. 3c). The exact boundary condition
    is shown only in the figure.
- Measurement:
  - 3 dynamic load cells (44.5 kN each; 133.5 kN total capacity) between head and tray, pre-compressed;
  - 2 accelerometers (±1500 g), averaged;
  - DAQ 1 MHz total, so 200 kHz per channel;
  - displacement found by integrating acceleration twice;
  - impact velocity from 30 fps video plus equations of motion, assuming constant guide friction (p. 28).
- FE analysis: 3D non-linear, rate-dependent, in LS-Dyna, with a plasticity-based material model
  from Ranade et al. [44] (RILEM SHCC3, 2014).
  - The HSHDC tensile input was computed analytically for coupon-like fiber orientation (2D/3D
    mixed distribution), then increased for the rate effects of [[ranade2015-hshdc-tensile-rate-effects]].
  - The compressive rate effects were assumed to be like those of UHPCs of similar strength (p. 26).
- Curing & test age: heat-curing as above. **The test age is not stated.** The curing regime ends
  at about 17 d after casting (computed here).
→ [[impact-test]] (NEW), [[dogbone-uniaxial-tension]]

## Key results
Material properties (quasi-static, p. 26–27; HSHDC values cited from [33], Cor-Tuf from [36]):

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HSHDC | 166 (51 mm cube, n = 8, CV 6.1%); 159 (76 mm cube, n = 6, CV 4.4%) | not reported here | 14.5 (CV 6%) | 3.4 (CV 11%), n = 8, 0.5 mm/min | not reported | 2 vol.% PE; dynamic: σ_tu +42%, σ_fc +53%, ε_tu 2.9% at ≥ 0.1 s⁻¹ (citing [35]) |
| Cor-Tuf | 201 (51 mm cube, n = 6, CV 3.7%) | not reported | 11.2 (CV 9%), small dogbone; 7.6 (76 × 76 mm dogbone) | 0.12 (CV 27%), small dogbone; 0.09 (large dogbone) | not reported (1–2 macro-cracks) | softens beyond about 0.15% strain (p. 25); 3.26 vol.% hooked steel |

Table 4 (p. 33): first impact, FE vs experiment.

| Material | v (m/s) | PCF FEA (kN) | PCF Exp (kN) | Error | δmax FEA (mm) | δmax Exp (mm) | Error |
|---|---|---|---|---|---|---|---|
| HSHDC | 2.30 | 100 | 57 | 75.4% | 1.04 | 1.15 | −9.6% |
| HSHDC | 3.25 | 121 | 77 | 57.1% | 1.64 | 1.66 | −1.2% |
| HSHDC | 4.60 | 146 | 103 | 41.7% | 2.59 | 2.78 | −6.8% |
| Cor-Tuf | 2.30 | 107 | 64 | 67.2% | 1.05 | 1.10 | −4.5% |
| Cor-Tuf | 3.25 | 134 | 87 | 54.0% | 1.82 | 1.62 | 12.3% |
| Cor-Tuf | 4.60 | 141 | 105 | 34.3% | 3.31 | 3.49 | −5.2% |

Main findings (with Table/Fig. location):
- **Single impact** (H4.60-1, Fig. 4, p. 29) has three stages:
  - S1: impulse, with PCF about 110 kN at 0.04 ms;
  - S2: depression to maximum displacement, with slab and head oscillations up to about 0.8 ms;
  - S3: rebound.
  The PCF depends on surface roughness and on DAQ sampling (200 kHz).
  - ⚠️ The text gives about 110 kN for this impact, but Table 4 gives 103 kN (Exp, 4.60 m/s).
- **Multiple impacts** (Fig. 5, p. 29–30):
  - At 2.30 m/s, PCF is about constant for both materials over 20 impacts (about 45–68 kN, read
    from Fig. 5a). The back faces show only a few cracks.
  - At 3.25 and 4.60 m/s, the Cor-Tuf PCF falls once its deflection-hardening capacity is
    exceeded, faster at 4.60 m/s.
    - Read from Fig. 5b–c: from about 85–110 kN down to about 25–35 kN.
    - The decline starts after about 6 impacts at 3.25 m/s and after about 5–8 at 4.60 m/s.
  - Cor-Tuf slabs fail before 20 impacts, except C3.25-1.
  - HSHDC PCF stays about constant (about 65–80 kN at 3.25 m/s; about 85–110 kN at 4.60 m/s, from
    Fig. 5). All HSHDC slabs survive 20 impacts and keep rebounding the weight.
- **Initial PCF:** Cor-Tuf's first-impact PCF is equal to or slightly higher than HSHDC's
  (Table 4: 64 vs 57, 87 vs 77, 105 vs 103 kN). HSHDC's advantage is the **retained** capacity
  from about 6 impacts on (p. 30).
- **Damage, 75 mm head, 3.25 m/s** (Fig. 6–7, p. 30–31):
  - Cor-Tuf C3.25-1 after 19 impacts: 4 large flexural cracks from the centre toward the slab edge
    thirds (yield lines). Large chunks break away, cracks reach the front face, and the slab breaks
    into 4 pieces at the next impact.
  - HSHDC H3.25-1 after 20 impacts: many fine radial cracks with one relatively larger central
    crack, no significant front-face damage, and almost no spalling.
- **Head size** (Fig. 8–9, p. 30):
  - With the 50 mm head at 3.25 m/s, Cor-Tuf fails by **punching shear at the 15th impact**,
    5 impacts fewer than its flexural failure with the 75 mm head.
  - HSHDC shows no punching on either face and no failure after 20 impacts.
  - The authors link this to the improved shear behaviour of strain-hardening materials, as in SHCC (citing [45]).
- **FE verification** (p. 31–32):
  - The impulse (area under the F–t curve) is about the same in FE and experiment.
  - Displacement error is < 13% for all cases.
  - The experimental δmax is mostly larger than FE, attributed to crushing of surface asperities
    of about 100 µm.
  - The PCF over-prediction is attributed to the 200 kHz sampling and the surface texture.
- **FE stress and strain fields** (Fig. 10–12, p. 32–33):
  - The hydrostatic pressure profile is like a beam in flexural vibration. The neutral axis is
    high, which indicates inelastic deformation.
  - The compressive stress at the front face is higher in HSHDC, because of its greater tensile
    resistance.
  - At δmax the maximum principal strain on the back face is **< 1% everywhere in HSHDC** (diffuse)
    and **up to 3% in Cor-Tuf** (localised along 2 branches per quadrant). Cor-Tuf's tensile strain
    capacity is an order of magnitude lower, which leads to back-face spalling.
  - In rebound, Cor-Tuf sees tension over a larger front-face area, which leads to front-face spalling.

## Mechanisms / explanations offered by authors
- **Tensile ductility spreads the damage:** strain hardening with multiple cracking turns the
  impact into distributed flexural damage. Tension softening concentrates all the strain at the
  yield lines (p. 30, 33). → [[multiple-cracking]], [[strain-hardening]]
- **A ductile tensile response improves shear and punching resistance,** so the failure mode does
  not depend on head size (p. 30).
- **Tensile resistance in the inelastic stage lets the compression zone carry higher stress,** so
  the high f'c is actually used (p. 33).
- **Limits of tension-softening FR-UHPC under impact** (literature review, p. 25):
  1. back-face spalling and scabbing;
  2. localised damage along yield lines;
  3. performance scales with f'c and needs ≥ 3% fibers;
  4. strain incompatibility with rebar.
  **SHCC** limits: front-face crushing (f'c less than half that of FR-UHPC) and larger permanent
  deformation (lower E).
- **Fiber dispersion and orientation** govern the impact performance:
  - Thin planar slabs likely give a 2D orientation, and therefore higher bridging capacity than
    a 3D orientation in beams or columns.
  - Layered casting can leave fiber-poor interlayers (p. 30–31). → [[fiber-dispersion]]
- **Rate effects** of PE fiber and interface: the PE fiber's strength and modulus rise with rate,
  while the frictional bond is relatively insensitive (citing [35], p. 26). → [[strain-rate-effects]]

## Limitations (stated + observed)
- PCF is limited by the 200 kHz sampling per channel. Tests at higher sampling rates are needed
  to confirm the FE–experiment discrepancy (stated, p. 34).
- The FE material input comes from dogbones cast separately, not from specimens sawn out of the
  slabs. Future work should use sawn specimens (stated, p. 35).
- Weapon impacts and blasts produce strain rates 2–3 orders of magnitude higher than those tested
  here. Kolsky bar and shock tube tests are underway (stated, p. 35).
- Only unreinforced slabs were tested. Reinforced members and criteria such as penetration depth,
  crater, perforation, mass loss and frangibility are future work (stated, p. 35).
- PE melts at about 150 °C, which matters for blast fireballs. A study is ongoing (stated, p. 31).
- *Observed:*
  - n = 2 slabs per case.
  - The 50 mm head series is qualitative only (no instrumentation).
  - The impact velocity was found from 30 fps video assuming constant friction.
  - There is no energy-absorption quantity. "Energy" is inferred from rebound and PCF retention.
  - Only one HSHDC mix, and no comparison with SHCC/ECC or a strain-hardening UHPC.
  - The test age is not stated.
  - The strain-rate range 0.1–10 s⁻¹ is asserted, not measured.
  - All data come from one research group.

## Relation to other work
- Agrees with:
  - Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source): same mix and the same quasi-static values
    (166 / 159 MPa, 14.5 MPa, 3.4%, CV values).
  - [[ranade2015-hshdc-tensile-rate-effects]]: rate effects quoted consistently (+42% σ_tu,
    +53% σ_fc, ε_tu plateau at about 2.9% above 0.1 s⁻¹).
  - Yang & Li 2012 (CCR) and Zhang et al. 2007 (as cited [28,29]): SHCC/ECC improves impact
    resistance compared with concrete.
- Contradicts: ⚔️
  - Quasi-static ε_tu is quoted as 3.4% (from [33]). The 2015 paper measured 4.2% at 10⁻⁴ s⁻¹.
    This is the existing conflict, now repeated by a third paper from the same group.
  - The intro (p. 25) says HSHDC keeps "about 3%" ductility up to 10 s⁻¹, while 2015 Table 2 gives
    2.7% at 10 s⁻¹. This is a minor rounding difference.
  - Cor-Tuf vs "VHSC" in Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source) (Table 1). Both have
    f'c 201 MPa, the same Class H/SF/silica flour/silica sand ratios (0.389/0.277/0.967) and hooked
    steel 30 mm × 550 µm, so they are probably the same material. But the values differ:

    | Quantity | This paper (Cor-Tuf) | 2013 paper (VHSC) |
    |---|---|---|
    | ε_tu | 0.12% | 0.18% |
    | σ_tu | 11.2 MPa | 10.4 MPa |
    | Vf | 3.26% | 3.6% |
    | SP | 0.0151 | 0.009 |

    ⚠️ The identity is not stated by either paper.
  - Fig. 1 caption: "gauge length of 980 mm" is printed, but the photo (Fig. 1b) shows 90 mm.
    This is a typo in the source.
  - The single-impact text says PCF about 110 kN (H4.60-1), but Table 4 gives 103 kN.
- Extends:
  - This is the first member-level (slab) impact evidence for HSHDC. It fills the "no member-level
    tests" gap in [[extreme-loading-applications]].
  - It links the rate effects of [[ranade2015-hshdc-tensile-rate-effects]] to structural response
    through FE.

## Pages updated from this source
- [[hshdc]] · [[extreme-loading-applications]] · [[strain-rate-effects]] · [[uhpc-vhsc]] ·
  [[multiple-cracking]] · [[strain-hardening]] · [[fiber-dispersion]] · [[tensile-strain-capacity]] ·
  [[compressive-strength]] · [[fresh-properties]] · [[heat-curing]] · [[pe-fiber]] ·
  [[dogbone-uniaxial-tension]] · [[mix-designs]] · [[mechanical-results]] · [[gaps]]
- Proposed NEW: [[impact-test]] (drop-weight impact on slabs), [[impact-resistance]] (property page),
  [[uhpc-vhsc]] (or fold into [[uhpc-vhsc]]), [[tensile-constitutive-model]]

## To verify
- [ ] Test age of the slabs is not stated (curing ends at about 17 d). Confirm against Ranade [36] / [33].
- [ ] ⚠️ unverified: PCF ranges and the impact number where Cor-Tuf starts to decline are read
      from Fig. 5. They are approximate, not tabulated.
- [ ] ⚠️ unverified: is Cor-Tuf the same material as the "VHSC" reference in
      Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source)? Vf (3.26 vs 3.6%) and SP differ.
- [ ] The single-impact PCF of about 110 kN (text, p. 29) vs 103 kN (Table 4) for H4.60-1. Possibly
      different specimens or a reading of the peak from Fig. 4.
- [ ] Fig. 1 caption "980 mm" gauge length is a source typo (90 mm in Fig. 1b). Confirmed from the
      rendered page image.
- [ ] Support conditions of the slab (clamped or simply supported, span) are shown only in Fig. 3c,
      not in the text.
- [ ] Kinetic energies (about 42 / 85 / 170 J) and the about 17 d curing end are computed here, not stated.
