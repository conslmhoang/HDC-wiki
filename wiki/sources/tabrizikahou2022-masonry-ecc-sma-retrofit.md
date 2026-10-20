---
type: source
slug: tabrizikahou2022-masonry-ecc-sma-retrofit
title: "Cyclic Behavior of Masonry Shear Walls Retrofitted with Engineered Cementitious Composite and Pseudoelastic Shape Memory Alloy"
authors: [Alireza Tabrizikahou, Mieczysław Kuczma, Magdalena Łasecka-Plura, Ehsan Noroozinejad Farsangi]
year: 2022            # Sensors 22(2), January 2022 issue; published online 10 Jan 2022 (received 14 Dec 2021, accepted 7 Jan 2022)
venue: "Sensors (MDPI) 22(2) (2022) 511"
doi: "10.3390/s22020511"
raw_file: raw/papers/Tabrizikahou2022_masonry-ECC-SMA-retrofit.xml
material_term: "ECC (engineered cementitious composite), used as epoxy/resin-bonded (precast) sheets. No fiber type, mix or tensile strain capacity reported; ECC properties are taken second-hand from Munjal & Singh (refs 33, 34) and are modelled with a tension-SOFTENING CDP law (Table 5), i.e. strain hardening is not represented"
study_type: numerical   # Abaqus FE only; no new experiments. Model validated against experiments of others (Singh & Munjal, ref. 35; wall geometry from Karimi et al., ref. 36)
tags: [ecc, masonry, urm, seismic-retrofit, in-plane-cyclic, shape-memory-alloy, ni-ti, hybrid-retrofit, finite-element, abaqus, concrete-damaged-plasticity, cohesive-interface, energy-dissipation, poznan-university-of-technology]
ingested: 2026-10-20
updated: 2026-10-20
---

# FE study of URM shear walls retrofitted with ECC sheets and Ni–Ti SMA strips (Tabrizikahou et al., 2022)

## One-paragraph summary
A purely **numerical (Abaqus) study** from Poznan University of Technology (with Kerman, Iran).
A URM wall 1720 × 1500 × 195 mm (L × H × t) under a constant 0.2 MPa vertical pressure was pushed
by in-plane, displacement-controlled cyclic loading, each amplitude repeated three times (Sect. 2,
Fig. 1). Eight cases were modelled (Table 2):
- an unretrofitted reference wall (URM);
- X-shaped pseudoelastic Ni–Ti strips, 120 mm wide and 1.0, 1.5 or 2.0 mm thick, on both faces;
- ECC sheets 20, 25 or 30 mm thick, bonded with epoxy/resin to both faces;
- a hybrid: 1.5 mm Ni–Ti strips embedded in 25 mm ECC sheets.

The masonry and the ECC are homogenised macro-models with the Concrete Damaged Plasticity (CDP) law.
The ECC–wall bond is a cohesive surface with a stiffness of 28,000 MPa (Eq. 12, Sect. 2.2).

Main results:
- **Energy dissipation:** hybrid 4.74 × 10⁷ J vs URM 1.52 × 10⁷ J (Sect. 3, Fig. 26).
- **Peak lateral force:** hybrid 246 kN; Ni–Ti 155 → 214 kN for 1.0 → 2.0 mm; ECC 113 → 135 kN for
  20 → 30 mm (Sect. 4, Fig. 25).
- **Yielded wall elements:** about 89% for the URM and for every Ni–Ti case, but only 27/24/18% with
  20/25/30 mm ECC sheets (Figs. 14, 16, 19).
- **Interface assumption:** a cohesive bond dissipates roughly twice the energy of hard contact
  (friction 0.4) (Table 8).

> Synthesis: this is the wiki's first **primary** masonry-retrofit source, but it is **numerical, not
> experimental**. The "ECC" in the model has a peak tensile stress of 1.45 MPa that softens to 0.43 MPa at
> 1.38% cracking strain (Table 5). It therefore behaves as a softening quasi-brittle material and does
> **not** reproduce tensile strain hardening. The results speak to "a stiff bonded cementitious overlay",
> not specifically to ECC/HDC ductility.

## Objective / research question
- How do Ni–Ti SMA strips, ECC sheets and their combination change the in-plane cyclic behaviour
  (hysteresis, energy dissipation, reaction force, yielded area) of URM shear walls (Sect. 1, last paragraph)?
- What are the effects of Ni–Ti thickness (1–6 mm, Table 7), ECC thickness (20–30 mm), and the ECC–wall
  interaction model (cohesive, hard contact, tied; Table 8)?

## Materials & mix design
No mix design. ECC is defined only by FE input parameters taken from the literature.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| ECC sheet (FE input) | not reported | not reported | not reported | not reported | not reported | not reported | not reported | not reported | not reported | not reported |

Units of binder quantities: n/a (no mix given)

FE material inputs (Sect. 2.1; Tables 3–5):
- **Masonry (homogenised):** E = 1450 MPa; Poisson's ratio 0.2 (assumed); tensile strength = 10% of
  compressive (assumed, ref. 51). Compression yield stress 0.95 → 2.83 MPa at inelastic strain 0 → 0.0006.
  Tension 0.28 MPa → 0.05 MPa at cracking strain 0.00022 (Table 5).
- **ECC sheet:** E = 17,500 MPa (from Munjal & Singh, ref. 33).
  - Compression: yield stress 19.62 → 62.78 MPa at inelastic strain 0 → 0.0170 (Table 5).
  - Tension: 1.45 MPa at cracking strain 0, then 1.06 MPa at 0.0057 and 0.43 MPa at 0.0138, i.e.
    monotonic softening (Table 5).
- **CDP parameters** (Table 4):

  | Material | Dilation angle | Eccentricity | σb0/σc0 | Kc | Viscosity |
  |---|---|---|---|---|---|
  | Masonry | 30° | 0.1 | 1.16 | 0.667 | 1 × 10⁻⁵ |
  | ECC | 37° | 0.1 | 1.16 | 0.667 | 1 × 10⁻⁵ |

- **Ni–Ti (Pereiro-Barceló & Bonet, ref. 43; Auricchio model):**
  - E (austenite) 64,647 MPa; E (martensite) 28,125 MPa; Poisson's ratio 0.33.
  - Transformation temperatures: Mf −49.15, Ms −31.23, As −20.75, Af −7.70 °C (Table 3).
- ⚠️ Table 5's caption cites ref. [34] (Singh, Patil & Munjal 2017). The text attributes the ECC modulus
  to ref. [33] (Munjal & Singh 2020) and the material characterisation to "Munjal and Singh [34]". The
  attribution is inconsistent.

## Test methods
- **Specimen geometry:** FE wall 1720 × 1500 × 195 mm, geometry from the tests of Karimi et al. (ref. 36).
  Ni–Ti strips 120 mm wide in an X pattern on both faces. ECC sheets cover both full faces (Table 2, Figs. 3–4).
- **Loading / rate:** 0.2 MPa constant vertical pressure through a rigid top surface. Lateral in-plane
  cyclic displacement at a top reference point, rising amplitude, 3 cycles per amplitude (Fig. 1b).
  Quasi-static. The base is fixed.
- **Elements and mesh:** C3D8R solids for masonry and ECC with a 100 mm mesh, chosen from a 25–200 mm
  sensitivity study (Figs. 10–12). The C3D20 alternative raised run time from 0.5 to 10.8 min with no
  benefit (Sect. 2.3). Ni–Ti strips are S4R shells.
- **Interfaces:**
  - Ni–Ti to wall: "mortar-bonded", full transfer.
  - ECC to wall: cohesive, Knn = Kss = Ktt = 28,000 MPa (Eqs. 11–12). Alternatives compared: hard contact
    with friction 0.4 (ref. 54), and a tie constraint (Sect. 3, Table 8).
- **Validation** against tests by Singh & Munjal (ref. 35), Table 6:
  - Masonry: max load 15,480 N tested vs 15,710 N FE (+1.47%); max displacement 1.02 vs 1.01 mm.
  - ECC: 2620 vs 2850 N (+8.8%); 15.87 vs 15.25 mm (3.91%).
  - The validation tests are not in-plane wall tests; the paper does not describe their configuration
    (Fig. 9) ⚠️.
- **Measurement:** n/a (numerical). Outputs: hysteresis, Mises stress, equivalent plastic strain, AC-yield
  fraction, reaction force, dissipated energy.
- **Curing & test age:** n/a (numerical); not reported for the borrowed ECC data.
→ [[masonry-wall-retrofit]] · [[tensile-constitutive-model]]

## Key results
No material tests. The ECC row restates the FE inputs taken second-hand from the literature.

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| ECC sheet (FE input, from refs 33/34) | max yield stress in Table 5: 62.78 | 1.45 (tension yield, Table 5) | 1.45 (softening after) | not represented (softening law; cracking strain up to 1.38% at 0.43 MPa) | not reported | E = 17,500 MPa |

Structural results:

| Model | Peak force (kN) | Dissipated energy | Yielded masonry elements | Location |
|---|---|---|---|---|
| URM | not stated numerically (Fig. 25) | 1.52 × 10⁷ J | ≈ 89% | Fig. 14, 26 |
| URM-SMA-1.0 / 1.5 / 2.0 mm | 155 / — / 214 | 21.5 / 23.4 / 25.1 MJ | ≈ 89% (all) | Sect. 4; Table 7; Fig. 16 |
| URM-ECC-20 / 25 / 30 mm (cohesive) | 113 / — / 135 | 25.1 / 26.9 / 29.3 MJ | 27 / 24 / 18% | Sect. 4; Table 8; Fig. 19 |
| URM-SMA-ECC (1.5 mm + 25 mm) | 246 | 4.74 × 10⁷ J | ≈ 68% | Sect. 3–4; Figs. 22, 26 |

Main findings (with Table/Fig. location):
- **Energy:** the hybrid dissipated about 3.1× the URM energy. The authors call this "+318%" (Sect. 3,
  Conclusions), but 4.74/1.52 = 3.12, i.e. +212% ⚠️. The ECC-only walls dissipated slightly more energy than
  the SMA-only walls (Fig. 26).
- **Yielding:** ECC sheets cut the yielded fraction of masonry from ≈ 89% to 18–27%, and thicker sheets cut
  it more (Fig. 19). Ni–Ti strips did not change the yielding of the masonry (Fig. 16).
- **Thickness effects:**
  - ECC 20 → 30 mm raised peak force from 113 to 135 kN.
  - Ni–Ti 1.0 → 2.0 mm raised it from 155 to 214 kN (Conclusions).
  - The authors say ECC thickness has a "small effect" on hysteresis, yet also report +117% for
    20 → 30 mm and +116% for Ni–Ti 1.0 → 2.0 mm (Conclusions) ⚠️ internally inconsistent.
- **Interaction model** (Table 8):
  - Cohesive dissipates 25.1–29.3 MJ; tied 23.9–27.7 MJ; hard contact 13.9–14.2 MJ.
  - With hard contact, the 30 mm sheet doubled the maximum displacement (6.765 → 13.120 mm).
- **Ni–Ti 1–6 mm** (Table 7): dissipated energy rose from 21.5 to 35.1 MJ, but not monotonically
  (it dipped at 4.0 mm). The maximum Mises stress in the wall stayed between 3.7 and 4.2 MPa.
- **Hybrid stress transfer:** the ECC sheets carried higher stresses than the masonry but had low plastic
  strain because of their higher modulus. The Ni–Ti carried the highest stresses with the lowest residual
  strain (Figs. 23–24).

## Mechanisms / explanations offered by authors
- **Ni–Ti:** pseudoelasticity (stress-induced martensitic transformation) gives high stress capacity with
  low residual strain, and adds stiffness and damping (Sect. 1, Figs. 15, 24).
- **ECC sheets:** spread the damage and reduce the yielded masonry volume. A higher Young's modulus than
  masonry means lower plastic strain under higher stress (Sect. 3, Fig. 23).
- Energy dissipation scales with lateral stiffness and residual displacement (Sect. 3).
- **Literature cited** (refs 31–35, as cited):
  - ECC on URM out-of-plane gave +440% load capacity (Munjal & Singh 2020).
  - Walls with openings gave about 6× capacity (Singh & Munjal 2020).
  - ECC columns gave +110% stiffness, +65% strength, +45% ductility and +100% energy absorption vs RC
    (Gencturk & Hosseini 2015).

## Limitations (stated + observed)
- **Stated:**
  - The macro-model cannot capture local crack growth in the masonry; it was used for computational
    efficiency (Sect. 2).
  - Ni–Ti cost limits the practical thickness, so 1.5 mm was adopted (Sect. 3).
- **Observed: no new experiments.**
  - All material data are borrowed.
  - The validation compares only peak load and displacement against tests of a different configuration
    (Table 6).
  - The FE model of the hybrid system was not validated.
- **Observed: ECC is modelled with tension softening** (1.45 → 0.43 MPa). The peak tensile stress (1.45 MPa)
  is far below typical ECC values (e.g. 4.84 MPa in [[wang2019-rc-beam-ecc-shear-strengthening]]).
  Multiple cracking and strain hardening are therefore absent.
- **Observed: ECC not characterised.** Fiber type, Vf, mix, age and curing of the ECC are not reported.
- **Observed: unrealistic bond.** The interface is an epoxy/resin cohesive bond with no damage or failure law.
  The paper shows that the interaction assumption changes the dissipated energy about 2× (Table 8).
- **Observed: internal inconsistencies.**
  - "+318%" vs a 3.1× ratio.
  - "small effect" vs "+117%".
  - "1.48%" in the text vs 1.47% in Table 6.
  - Ref. [33] vs [34] for the ECC data.
- **Observed: unrealistic energy values.** Dissipated energy is in MJ (≈ 10⁷ J) for a 1.7 m wall with forces
  of ≈ 100–250 kN. That needs tens of metres of cumulative displacement, which looks implausible ⚠️.

## Relation to other work
- **Agrees with:** the general claim that ECC overlays improve URM seismic response (Deng 2019
  shake-table test, as cited in [[he2024-hdc-research-advances]], p. 9; see [[masonry-wall-retrofit]]).
- **Contradicts:** ⚔️ the ECC tension input here (softening from 1.45 MPa) is inconsistent with the
  strain-hardening ECC defined elsewhere in the wiki (σ_tu ≈ 3–5 MPa, ε_tu > 1%; e.g.
  [[li2003-ecc-review]], [[wang2019-rc-beam-ecc-shear-strengthening]]). This is a modelling-input issue,
  not a measured conflict.
- **Extends:**
  - First FE treatment in the wiki of the ECC–masonry interface.
  - First combination of ECC with SMA.
  - Introduces the in-plane cyclic URM wall configuration (the Deng 2019 test was a shake table).

## Pages updated from this source
- [[masonry-wall-retrofit]]
- [[tensile-constitutive-model]]
- [[rc-member-strengthening]]
- [[gaps]]

## To verify
- [ ] "Energy increased by 318%" (Sect. 3, Conclusions) vs 4.74/1.52 × 10⁷ J = 3.12× (+212%). Check the PDF and Fig. 26.
- [ ] Units of dissipated energy (MJ, Tables 7–8; 10⁷ J, Fig. 26) look physically too large for the forces and displacements reported.
- [ ] Source of the ECC inputs: ref. [33] (Munjal & Singh 2020, JSIM) vs ref. [34] (Singh, Patil & Munjal 2017, Eng. Struct.). What fiber, Vf and test gave σt = 1.45 MPa?
- [ ] Configuration of the validation tests in Table 6 (out-of-plane wallets? prisms?) and why the ECC max load is only 2620 N.
- [ ] URM peak force value (Fig. 25 only; not stated in text).
- [ ] Peak forces for the 1.5 mm Ni–Ti and 25 mm ECC models (Fig. 25 only).
- [ ] "Hysteresis raised by 116% / 117%" (Conclusions): which metric?
