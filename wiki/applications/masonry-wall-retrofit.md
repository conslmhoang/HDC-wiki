---
type: application
slug: masonry-wall-retrofit
aliases: [URM strengthening, HDC overlay, masonry retrofit, seismic retrofit, ECC sheets, SMA retrofit]
tags: [application, seismic, strengthening]
sources: [he2024-hdc-research-advances, tabrizikahou2022-masonry-ecc-sma-retrofit, yang2024-hshdc-uniaxial-tension]
updated: 2026-10-20
---

# Seismic Retrofit of Masonry with HDC Overlays

> Status (2026-10-20): one primary source, but it is **numerical only** ([[tabrizikahou2022-masonry-ecc-sma-retrofit]],
> Abaqus). No experimental masonry test is in the corpus. Primary source still to obtain: Deng et al. 2019,
> Eng. Struct. 197:109424 (shake table).

## Experimental evidence (second-hand)
- A PVA-HDC overlay (2% high-strength, high-modulus PVA) on a half-scale 2-storey URM building
  outperformed a welded-wire-mesh overlay in shake-table tests (Deng 2019, as cited in
  [[he2024-hdc-research-advances]], p. 9).
- The Xi'an group (Deng Mingke, XAUAT) is the main source for this application lineage.
  See also [[yang2024-hshdc-uniaxial-tension]] and [[deng2018-hdc-short-columns]] (same group).
- **Out-of-plane tests (as cited in [[tabrizikahou2022-masonry-ecc-sma-retrofit]], Sect. 1, Sect. 3):**
  - ECC-strengthened URM walls: +440% load capacity (Munjal & Singh 2020);
  - walls with openings: about 6× capacity (Singh & Munjal 2020);
  - optimum ECC sheet thickness 20–50 mm (Singh & Munjal).

## Numerical study: Tabrizikahou et al. 2022
Abaqus FE, concrete-damaged-plasticity macro-model; in-plane cyclic URM wall 1720 × 1500 × 195 mm under 0.2 MPa
vertical pressure; precast "ECC" sheets bonded to both faces; Ni–Ti shape-memory-alloy (SMA) strips as an alternative
or hybrid ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], Sect. 2, Fig. 1).

| Retrofit | Peak lateral force (kN) | Note | Location |
|---|---|---|---|
| URM | not stated numerically (Fig. 25) | ≈ 89% of masonry elements yielded; energy 1.52 × 10⁷ J | Figs. 14, 26 |
| ECC 20 / 25 / 30 mm both faces (cohesive) | 113 / — / 135 | yielded elements 27 / 24 / 18%; energy 25.1 / 26.9 / 29.3 MJ | Conclusions, Table 8, Figs. 19, 25 |
| Ni–Ti SMA only, 1.0 / 1.5 / 2.0 mm | 155 / — / 214 | ≈ 89% yielded; energy 21.5 / 23.4 / 25.1 MJ (ECC-only slightly higher) | Table 7, Fig. 16 |
| Ni–Ti X-strips (1.5 mm) inside 25 mm ECC | **246** (highest) | ≈ 68% yielded; energy 4.74 × 10⁷ J vs URM 1.52 × 10⁷ J (about 3.1×; paper says "+318%" ⚠️) | Fig. 26 |

- **Interface assumption controls the result:** dissipated energy 25–29 MJ (cohesive), 24–28 MJ (tied), 14 MJ (hard
  contact, µ = 0.4) (Table 8). → [[interface-bond]]
- ⚠️ **Caveat:** the "ECC" input softens in tension from 1.45 MPa (Table 5). The model therefore does **not** exercise
  tensile strain hardening; results describe a tension-softening overlay, not HDC/ECC as defined in
  [[terminology-hdc-ecc-shcc]].
- ⚔️ The 1.45 MPa softening input conflicts with the strain-hardening ECC definition (σ_tu about 3–5 MPa, e.g.
  4.84 MPa in [[wang2019-rc-beam-ecc-shear-strengthening]]). → [[gaps]]

> Synthesis: the masonry case for HDC in the corpus rests on one second-hand shake-table test (Deng 2019) and one FE
> study whose ECC model is not strain-hardening. The overlay effect in the FE model is driven mainly by added section
> and by the interface law. Claims about the benefit of HDC ductility for masonry are therefore not yet supported by
> primary evidence in this wiki.

## Conflicts & open questions
- No experimental in-plane test of HDC/ECC-retrofitted masonry in the corpus. No experimental validation of the
  hybrid ECC + SMA system ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], observed).
- Bond between overlay and masonry is a first-order parameter (about 2× in energy), but no bond tests exist. → [[gaps]]

## Related
- [[rc-member-strengthening]] · [[pva-fiber]] · [[interface-bond]] · [[review-outline]]
