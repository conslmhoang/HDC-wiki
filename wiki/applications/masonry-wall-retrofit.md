---
type: application
slug: masonry-wall-retrofit
aliases: [URM strengthening, AAC wall retrofit, shaking table, HDC overlay, masonry retrofit, seismic retrofit, ECC sheets, SMA retrofit]
tags: [application, seismic, strengthening]
sources: [he2024-hdc-research-advances, tabrizikahou2022-masonry-ecc-sma-retrofit, yang2024-hshdc-uniaxial-tension, deng2019-urm-shaking-table-hdc, deng2020-aac-wall-hdc-retrofit, zhang2022-hdc-basalt-textile-tension]
updated: 2026-10-21
---

# Seismic Retrofit of Masonry with HDC Overlays

> Status (2026-10-21): **two primary experimental studies** by the XAUAT group now exist — a shake-table test of a
> half-scale URM building ([[deng2019-urm-shaking-table-hdc]]) and in-plane cyclic tests of AAC block walls
> ([[deng2020-aac-wall-hdc-retrofit]]) — plus one numerical study ([[tabrizikahou2022-masonry-ecc-sma-retrofit]]).
> Both experimental papers use an XAUAT PVA-HDC with **measured** tensile strain hardening (≈ 1.0–1.2%).

## Materials used in the experimental studies
| Source | Authors' term | Overlay mix | f_cu (MPa) | σ_tu (MPa) | ε_tu (%) | Location |
|---|---|---|---|---|---|---|
| [[deng2019-urm-shaking-table-hdc]] | "high ductility fibre reinforced concrete (HDC)" | C : FA : sand : W = 1 : 1 : 0.72 : 0.58 (mass), 2 vol.% PVA 12 mm × 39 µm | 61.15 (100 mm cube, 28 d) | 5.83 (mean of 3 plates, DBJ61/T112-2016) | ≈ 1.0 ultimate (Fig. 6a ⚠️ read) | p. 3, Table 3, Fig. 6a |
| [[deng2020-aac-wall-hdc-retrofit]] | "HDC, also referred to as ECC" | 593 C / 593 FA / 427 silica sand kg/m³, 1.7 vol.% PVA | 49.80 (100 mm cube, air-cured ≈ 2 months) | 3.89 (dogbone 15 × 50 mm) | ≈ 1.2 at peak (Fig. 3 ⚠️ read) | Tables 2–3, Fig. 3 |

## Shake-table test: Deng et al. 2019 (primary)
Half-scale 2-storey URM building (3.42 × 3.42 × 3.3 m, 120 mm half-brick walls), 17 runs in three phases on **one**
model ([[deng2019-urm-shaking-table-hdc]], p. 2–4, Table 5):
M1 unretrofitted → M2 cracks grouted + welded-wire reinforcement (WWR) + 25 mm mortar on north walls → M3 WWR removed,
re-grouted, **15 mm PVA-HDC overlay** (north walls double/single-sided, first-floor E/W walls single-sided; Ø8 corner bars;
brick surface only cleaned of dust and loose material) (p. 4, Figs. 8–9).

| Quantity | M1 (URM) | M2 (WWR + mortar) | M3 (HDC overlay) | Location |
|---|---|---|---|---|
| Highest input | near local collapse at 0.362 g (actual) | 1.171 g nominal ("9-degree rare") | 1.171 g nominal | p. 7–8, Table 5 |
| Damage after phase | near local collapse | overlay mortar heavily cracked | slight: fine grouped cracks, **no main crack, no overlay detachment** | p. 7–8 |
| Frequency drop after phase (E-W / S-N) | — | 27.5 / 30.0% | 10.9 / 8.1% | p. 9 |
| Equivalent damping η (E-W / S-N) | — | 47.4 / 50.9% | 20.6 / 15.6% | p. 9 |
| Max first-storey drift E-W at 1.171 g | — | 1/76 | 1/84 | Table 7 |
| Performance level at 9-degree (GB 50011) | Level 4 | Level 4 | Level 1 | p. 14 |

- Proposed drift limits for HDC-overlaid masonry: 1/400 intact, 1/170 slight, 1/90 moderate (Concl. 5; ⚠️ Table 10 gives
  1/370 for intact); serious-damage and near-collapse limits not reached ([[deng2019-urm-shaking-table-hdc]]).
- Design shear capacity of an overlaid wall: V = V_ME + 0.7 f_dt·b·h (URM capacity per GB 50003 + 0.7 × HDC tensile
  strength × overlay thickness × wall length) ([[deng2019-urm-shaking-table-hdc]], Eq. 8).
- Torsion: mass–stiffness eccentricity up to 964 mm; torsion shear 34–42% of storey force in wall QY1; all walls had
  capacity/demand γ = 1.19–8.12 at M3-9R ([[deng2019-urm-shaking-table-hdc]], Table 8).
- Motivation: low-cost, fast retrofit for village URM shop-houses in SW China; ferrocement and FRP judged too costly (p. 1).
- ⚠️ **Caveats (observed):** M2 and M3 are repaired, pre-damaged states of the same model; retrofit area and thickness
  differ (WWR on north walls only vs HDC also on E/W walls); M3 saw fewer runs (4 levels); base shear / weight of M3 is
  not above M2 (Fig. 21 ⚠️ read, ≈ 1.5 for both at 1.171 g), although the text says HDC improved shear capacity more;
  no bond test and no overlay crack widths ([[deng2019-urm-shaking-table-hdc]], Limitations).
- The earlier second-hand bullet (Deng 2019, as cited in [[he2024-hdc-research-advances]], p. 9) is correct in substance;
  the review's "high-strength, high-modulus PVA" is given in the primary as 1600 MPa / 32 GPa (Table 2).

## In-plane cyclic tests of AAC walls: Deng et al. 2020 (primary)
5 half-scale autoclaved aerated concrete (AAC) block walls 2400 × 1400 × 190 mm, 0.3 MPa vertical stress, reversed
cyclic lateral load ([[deng2020-aac-wall-hdc-retrofit]], Table 1, Fig. 1).

| Retrofit | Peak load vs URM | Other result | Location |
|---|---|---|---|
| 15 mm HDC edge strips, unanchored | **+17%** | strips debonded at the wall base; ductility not improved | Table 4, p. 4, §4.2 |
| 15 mm HDC strips + steel bars anchored into wall/foundation | **+28%** | matched a confined (tie-column) wall in ultimate displacement (+75% vs URM) and ductility (2.05× URM); +32% strength and +125% energy vs the confined wall | §4.1–4.3, Concl. 4 |
| 15 mm single-sided HDC layer | **+31%** | failure mode shifted from diagonal shear to bed-joint sliding; energy +308%; little degradation up to 14 mm displacement | §3.1, §4.3 |

- Design formulas: diagonal-shear contribution V_HDC = 0.44·α_HDC·f_tu·t′·x with α_HDC = 0.53; sliding capacity
  V = µN + µ f_tu t (0.5 l), µ = 0.7 ([[deng2020-aac-wall-hdc-retrofit]], Eqs. 12–14). → [[shear-behaviour]]
- Bond: spalled face shells carried AAC fragments, so the HDC–AAC bond exceeded the block tensile strength; strip
  debonding was driven by compression concentration at the base (p. 4). → [[interface-bond]]
- ⚠️ Limited specimens (one per case); no crack widths; no bond tests on AAC; W-4 not taken to failure (§5, observed).

## Second-hand evidence
- **Out-of-plane tests (as cited in [[tabrizikahou2022-masonry-ecc-sma-retrofit]], Sect. 1, Sect. 3):**
  - ECC-strengthened URM walls: +440% load capacity (Munjal & Singh 2020);
  - walls with openings: about 6× capacity (Singh & Munjal 2020);
  - optimum ECC sheet thickness 20–50 mm (Singh & Munjal).
- Textile-reinforced mortar (TRM) is less effective than FRP for URM walls and RC members (refs 8, 12–15, as cited in
  [[zhang2022-hdc-basalt-textile-tension]], §1) — motivation for [[textile-reinforced-hdc]].
- SHCC bonds to masonry without bonding agents (Mechtcherine et al. 2011, as cited in [[deng2020-aac-wall-hdc-retrofit]], p. 2).
- The Xi'an group (Deng Mingke, XAUAT) is the main source for this application lineage; its earlier masonry papers use
  the term "ECC" (Deng & Yang 2018, 2020, as cited in [[deng2020-aac-wall-hdc-retrofit]]). See also
  [[yang2024-hshdc-uniaxial-tension]] and [[deng2018-hdc-short-columns]] (same group).

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

> Synthesis: the masonry case now rests on two primary XAUAT experiments with a strain-hardening HDC (ε ≈ 1.0–1.2%):
> a whole-building shake-table test and five AAC wall tests. Both show that a thin (15 mm) HDC layer raises capacity
> moderately (+17% to +31% in-plane) and, more clearly, reduces damage (no main crack, smaller stiffness loss) and
> raises energy dissipation. Anchorage, not the HDC itself, controlled the strip retrofits. The size of the HDC
> benefit over conventional overlays is still uncertain: the shake-table comparison is confounded by repeated testing
> of one model and unequal retrofit areas, and no study measures overlay bond or crack width. The FE study
> (Tabrizikahou 2022) models a tension-softening overlay, so it does not test HDC ductility at all.

## Conflicts & open questions
- "No experimental in-plane test of HDC/ECC-retrofitted masonry in the corpus" — superseded 2026-10-21 by
  [[deng2020-aac-wall-hdc-retrofit]] (in-plane cyclic, AAC) and [[deng2019-urm-shaking-table-hdc]] (shake table).
  No experimental validation of the hybrid ECC + SMA system ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], observed).
- Bond between overlay and masonry is a first-order parameter in FE (about 2× in energy), but still no bond test of HDC
  on brick or AAC exists; the experiments give only visual evidence (no detachment to 1.171 g; AAC fragments on
  spalled strips). → [[interface-bond]], [[gaps]]
- No virgin-specimen comparison of HDC vs other overlays on identical walls; no out-of-plane test with HDC; no
  overlay crack-width data ([[deng2019-urm-shaking-table-hdc]], [[deng2020-aac-wall-hdc-retrofit]], observed).
- Serious-damage and near-collapse drift limits for HDC-overlaid masonry are not established
  ([[deng2019-urm-shaking-table-hdc]], p. 14–15).

## Related
- [[rc-member-strengthening]] · [[pva-fiber]] · [[interface-bond]] · [[shear-behaviour]] · [[textile-reinforced-hdc]] ·
  [[repair-and-field-applications]] · [[review-outline]]
