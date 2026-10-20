---
type: source
slug: zhang2022-hdc-basalt-textile-tension
title: "Uniaxial tensile performance of high ductile fiber-reinforced concrete with built-in basalt textile grids"
authors: [Wei Zhang, Mingke Deng, Yagang Han, Ruizhe Li, Shuo Yang]
year: 2022            # Construction and Building Materials 315 (2022) 125716; available online 23 Nov 2021 (received 22 Sep, accepted 13 Nov 2021)
venue: "Construction and Building Materials 315 (2022) 125716"
doi: "10.1016/j.conbuildmat.2021.125716"
raw_file: raw/papers/Zhang2022_HDC-basalt-textile-tension.pdf
material_term: "HDC ('high ductile fiber-reinforced concrete', 'also called' ECC), PVA 0–2 vol.% (12 mm × 39 µm), two matrices (Type I FA/C 1.1, f_cu 52–58 MPa; Type II FA/C 3.25, f_cu 30–38 MPa); with basalt textile grids = 'TR-HDC'; without PVA = 'TRC'. Plain HDC reached only 0.12–0.45% peak strain (below the JC/T 2461 0.5% bar); strain hardening with multiple cracking is shown for the textile-reinforced specimens. Standard curing, 28 d"
study_type: experimental + analytical (strength formula, bilinear σ–ε model)
tags: [hdc, tr-hdc, textile-reinforced-concrete, trc, trm, basalt-textile, pva-fiber, xauat, uniaxial-tension, dogbone, fly-ash, strength-utilization, ack-model, strengthening-material]
ingested: 2026-10-21
updated: 2026-10-21
---

# Uniaxial tension of HDC with built-in basalt textile grids (TR-HDC) (Zhang et al., 2022)

## One-paragraph summary
**Experimental + analytical** study from XAUAT (Deng Mingke group, Xi'an) with the Shanghai Research Institute of Building
Sciences. 32 groups (96 dogbones, 3 per group) of plain matrix, TRC (basalt textile grid, no PVA) and **TR-HDC** (basalt
textile grid + PVA-HDC) were tested in uniaxial tension at 28 d. Variables: PVA short-fibre volume fraction (0 / 0.5 / 1 /
1.5 / 2%), matrix type (Type I, cement-rich; Type II, high-volume fly ash) and textile grid level (0–3 layers, ν = 0.42–1.26%)
(§2, Table 5). The textile level mainly set the peak stress (up to 10.02 MPa for B3M2-2), while PVA governed the cracking
stress and the failure mode: with ≤ 1% PVA the grids slipped (failure pattern C), with 1.5–2% PVA the grids **ruptured**
(pattern B) and specimens showed multiple cracking up to peak (§3, Table 8). Adding PVA **reduced** the peak strain of
textile specimens (e.g. B3M1: 2.65% without PVA → 1.96–2.13% with 1.5–2%), because it suppressed textile slip (§4.2, Fig. 8).
Matrix type mattered little at 1.5–2% PVA (§4.3). The authors propose σ_T = α·f_t,b·A_t/A_m with α = 0.005·e^(2.2√(β/ν)) + 0.53
(68 data sets) and a bilinear σ–ε model for TR-HDC with 1.5–2% PVA, using a cracking stress of 0.896σ_t and a Eurocode-2-type
crack-width relation (Eqs. 1–17).

> Synthesis: this paper is a primary source for **TR-HDC**, which [[he2024-hdc-research-advances]] cites (via Song 2023/2024)
> as a slab-strengthening material (see [[rc-member-strengthening]]). Its plain HDC dogbones, however, barely harden
> (peak strain 0.12–0.45%, σ_tu/σ_cr ≈ 1.25–1.36), far below other XAUAT PVA-HDC (≈ 1.0%, [[deng2018-hdc-short-columns]];
> 0.968%, [[li2021-hdc-beam-shear]]) — record it as "HDC label, weak hardening in plain dogbones".

## Objective / research question
- Overcome the brittleness and textile slip of TRC/TRM by replacing the mortar with HDC (TR-HDC) (§1).
- Quantify the effect of PVA volume fraction, matrix type and textile grid level on cracking, peak stress, peak strain,
  failure mode and textile strength utilisation (§1, §4).
- Propose an ultimate-tensile-strength formula and a σ–ε model for TR-HDC (§5–6).

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| Type I HDC (M1) | 447 | 494 | "mineral powder" 177 ⚠️ (GGBFS?) + silica fume 59 | fine silica sand 424, max size not reported | 0.30 (computed: 353 / 1177) | water-reducing agent 8 | PVA (σ_f 1600 MPa, E 40 GPa, elong. 7%, 1.3 g/cm³, L/d ≈ 310) | 12 | 39 | 0 / 1.5 / 2 |
| Type II HDC (M2) | 235 | 764 | "mineral powder" 177 ⚠️; no SF | same, 424 | 0.32 (computed: 376 / 1176) | 8 | same PVA | 12 | 39 | 0 / 0.5 / 1 / 1.5 / 2 |

Units of binder quantities: kg/m³ (Table 1). FA/C (by mass) = 1.1 (Type I; the text says "0.9" for cement/FA = 447/494) and
3.25 (Type II; text "0.31" cement/FA) (§2.1.1). W/B computed by the wiki with binder = cement + FA + mineral powder (+ SF);
the paper gives no W/B. "Mineral powder" is not defined (often GGBFS in Chinese usage ⚠️).

Textile: basalt-fibre grid of resin-impregnated rovings, 25 × 25 mm spacing; single roving: rupture force 2.03 kN, area
1.58 mm², rupture stress 1285 MPa, rupture strain 2.9%, E 44 GPa, density 2.7 g/cm³ (Table 4, Fig. 1; 200 mm free length,
1 mm/min, after EN ISO 10618). Grid levels ν = 0.42 / 0.84 / 1.26% for 1 / 2 / 3 layers (§5; consistent with 2 rovings ×
1.58 mm² per layer over a 50 × 15 mm section, computed).

## Test methods
- **Specimen geometry:** dogbone 350 mm long (100 mm end zones with carbon-fibre fabric glued on both faces), 15 mm thick,
  measured region 50 mm wide, ends 80 mm wide; narrow region ≈ 230 mm, extensometer on one face (gauge length not stated ⚠️)
  (§2.2, Fig. 2). Textile layers placed by hand between matrix lifts (Figs. 3–4).
- **Loading / rate:** clevis grips, 100 kN machine, displacement control 0.2 mm/min; stop at 50% post-peak or abrupt yarn
  rupture; the clevis set-up allows textile slip at the grips (after Arboleda et al.) (§2.3, Fig. 5).
- **Measurement:** load cell; one extensometer on one side (out-of-plane bending neglected) (§2.3). Crack patterns
  photographed (Tables 6–7); no crack widths reported.
- **Compression:** three 100 mm cubes per PVA content (Table 3).
- **Curing & test age:** standard curing, tested at 28 d (§2.2).
→ [[dogbone-uniaxial-tension]]

## Key results
Plain matrices (no textile, B0) (Table 8, Table 3):
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| M1-0 (Type I, 0% PVA) | f_cu 58.2 | – | 3.41 | 0.11 (peak) | n.r. | matrix only |
| M1-1.5 | f_cu 56.2 | 3.07 | 3.89 | 0.12 (peak) | n.r. | σ_tu/σ_cr 1.27 (computed) |
| M1-2 | f_cu 52.0 | 4.35 | 5.44 | 0.34 (peak) | n.r. | σ_tu/σ_cr 1.25 (computed) |
| M2-0 (Type II) | f_cu 30.2 | – | 2.23 | 0.024 | n.r. | — |
| M2-0.5 | f_cu 33.8 | – | 1.16 ⚠️ | 0.15 | n.r. | lower than M2-0 |
| M2-1 | f_cu 32.0 | 2.04 | 2.35 | 0.29 | n.r. | — |
| M2-1.5 | f_cu 38.1 | 2.75 | 3.45 | 0.28 | n.r. | — |
| M2-2 | f_cu 33.3 | 3.10 | 4.23 | 0.45 | n.r. | σ_tu/σ_cr 1.36 (computed) |

All f_cu are 100 mm cubes at 28 d. Strain values are "peak strain ε_u" (strain at peak stress).

Textile-reinforced specimens (Table 8; σ_u = peak stress, ε_u = strain at peak, α = strength utilisation; failure patterns:
A = at clamps, B = textile rupture, C = textile slip):
| Group | 0% PVA (TRC) σ_u / ε_u / α / mode | 1.5% PVA | 2% PVA |
|---|---|---|---|
| B1M1 | 4.20 / 2.22 / 0.75 / AC | 4.78 / 1.20 / 0.85 / B | 6.11 / 1.51 / 1.10 / B |
| B2M1 | 5.64 / 2.35 / 0.53 / BC | 6.30 / 1.46 / 0.57 / B | 6.69 / 1.72 / 0.60 / B |
| B3M1 | 7.79 / 2.65 / 0.46 / C | 9.68 / 1.96 / 0.59 / B | 9.73 / 2.13 / 0.59 / B |
| B1M2 | 3.32 / 2.71 / 0.60 / BC | 4.75 / 1.53 / 0.89 / B | 5.83 / 1.64 / 1.07 / B |
| B2M2 | 5.68 / 2.85 / 0.51 / C | 6.83 / 1.90 / 0.64 / B | 7.12 / 2.32 / 0.66 / B |
| B3M2 | 6.82 / 3.79 / 0.41 / C | 9.94 / 2.41 / 0.62 / AB | 10.02 / 2.48 / 0.61 / B |

Type II with 0.5% / 1% PVA: B1–B3M2-0.5 σ_u 3.58–7.78 MPa, ε_u 3.41–3.71%; B1–B3M2-1 σ_u 3.95–9.15 MPa, ε_u 1.87–2.75%
(Table 8). Cracking stress of TR specimens 1.5–4.6 MPa, cracking strain 0.018–0.105% (Table 8). COVs up to 0.9 (Table 8 notes).

Main findings (with Table/Fig. location):
- **Failure mode:** TRC (0% PVA) failed by textile slip and matrix spalling, with crack spacing ≈ grid spacing (25 mm);
  ≤ 1% PVA mostly pattern C (slip); 1.5–2% PVA failed by **textile rupture** (pattern B) with denser multiple cracking and no
  spalling (§3.1, Tables 6–7).
- **Peak stress** rises mainly with textile level (B1 → B3: e.g. 6.11 → 9.73 MPa at M1-2) and modestly with PVA (§3.2, Fig. 8).
- **Cracking stress** is governed by PVA content; textile level has little effect (§3.2, Table 8).
- **Peak strain falls when PVA is added** to textile specimens (slip suppressed), then rises slightly from 1.5% to 2% PVA (§4.2, Fig. 8).
- **Strength utilisation α** falls as layers are added (e.g. M1-2: 1.10 → 0.60 → 0.59), i.e. capacity is not a superposition of
  rovings; PVA raises α (§4.1, Table 8). α > 1 at B1 with 2% PVA (1.10, 1.07): fibres carry part of the load.
- **Matrix:** Type II (high FA) TRC has higher strain and lower peak stress than Type I; with 1.5–2% PVA the two matrices give
  similar capacity at the same textile level (§4.3, Table 8).
- **Strength formula** (Eqs. 1–2, Fig. 9): σ_T = α·f_t,b·A_t/A_m; α = 0.005·e^(2.2√(β/ν)) + 0.53 (printed "2..2" ⚠️), β = PVA
  vol. fraction, ν = textile grid level; valid for 25 × 25 mm basalt grids, β 0–2%, ν 0.42–1.26%; 68 data sets.
- **σ–ε model** (§6, Eqs. 3–17, Figs. 10–12):
  - ≤ 1% PVA: ACK trilinear model as for TRC (E_e = E_t·ν_t + E_c·ν_c; ε_mu = (1 + 0.666α_m)σ_tu/E_c), with E_c from GB 50010
    (E_c = 10⁵/(2.2 + 34.7/f_cu)).
  - 1.5–2% PVA: bilinear; E1 = E_t·ν_t + E_HDC·ν_HDC; σ_cr = 0.896·E1·σ_t/E_HDC; ε_cr = 0.896σ_t/E_HDC (HDC cracking stress
    taken as 89.6% of its tensile strength); peak strain ε_u = (σ_T − k_t·σ_t(1 + α_e·ν_f))/(μ·E_f·ν_f) + ε_u,HDC with
    k_t = 0.6 and μ = 1 / 0.85 / 0.65 for 1 / 2 / 3 layers (Eq. 15, adapted from Eurocode 2 crack-width formula Eq. 14).
  - The model "roughly matched" the test curves (Fig. 12); no error statistics given.

## Mechanisms / explanations offered by authors
- PVA fibres bridge cracks, reduce matrix relaxation near cracks and allow new cracks at shorter spacing → more multiple
  cracking, no spalling (§3.1).
- PVA fibres lying on the yarn surface add "connecting points" to the matrix and improve yarn–matrix bond ("chemical
  adhesion"); at ≥ 1.5% PVA the yarn–matrix interface is strong enough that the grid ruptures instead of slipping (§4.2,
  Conclusion 1).
- High FA lowers chemical bond and raises frictional bond at fibre–matrix interfaces (citing Wang & Li 2007; Şahmaran & Li 2009),
  favouring pull-out and strain capacity; a similar effect is assumed at the yarn–matrix interface (§4.3).
- Laying textile in the middle plane reduces bond and causes premature slip (citing Caggegi 2017) (§4.1).

## Limitations (stated + observed)
- Stated: the α formula and σ–ε model are empirical and need validation with more tests, textile types, levels and fibre
  contents (§5, §6.2, Conclusion 3).
- Plain HDC dogbones show very low peak strains (0.12–0.45%), so the "HDC" matrix does not meet the JC/T 2461 0.5% bar in this
  test; the reason (thick 15 mm section with long 230 mm narrow length? matrix? dispersion?) is not discussed.
- M2-0.5 peak stress (1.16 MPa) is lower than M2-0 (2.23 MPa) without explanation; COVs up to 0.5–0.9 for cracking values.
- W/B not stated; "mineral powder" undefined; sand maximum size not reported; extensometer gauge length not stated.
- §4.3 refers to Table 8 for compressive strength, which is in Table 3.
- Hand lay-up only; no crack-width data, no bond (pull-out) test of yarn in HDC, no long-term/durability data.

## Relation to other work
- Agrees with: [[he2024-hdc-research-advances]] (p. 20, as cited there) that textile-reinforced mortar has low matrix
  elongation, large cracks and textile slip, motivating TR-HDC.
- Contradicts: ⚔️ Plain XAUAT PVA-HDC with 2% PVA reaches 0.34–0.45% peak strain here (Table 8), vs ≈ 1.0% in
  [[deng2018-hdc-short-columns]] (Fig. 1) and 0.968% in [[li2021-hdc-beam-shear]] (§2.1), all XAUAT-type PVA (12 mm × 39 µm,
  1600 MPa). Possible reasons: different matrix (W/B ≈ 0.30–0.32 with SF/"mineral powder" vs W/B 0.29 with FA only),
  specimen (350 mm XAUAT dogbone, 50 × 15 mm, here vs geometry n.r. in Deng 2018), strain basis (peak here vs n.s.).
- Extends: [[rc-member-strengthening]] (TR-HDC was second-hand only); [[tensile-constitutive-model]] (bilinear model for a
  hybrid textile + short-fibre composite with σ_cr = 0.896σ_t); [[dogbone-uniaxial-tension]] (same 350 mm, 50 × 15 mm,
  CFRP-wrapped XAUAT dogbone as [[yang2024-hshdc-uniaxial-tension]]).

## Pages updated from this source
- [[rc-member-strengthening]] · [[tensile-constitutive-model]] · [[tensile-strain-capacity]] · [[dogbone-uniaxial-tension]] ·
  [[multiple-cracking]] · [[pva-fiber]] · [[fly-ash]] · [[hybrid-fiber]] · [[terminology-hdc-ecc-shcc]] · [[mix-designs]] ·
  [[mechanical-results]] · [[masonry-wall-retrofit]]

## To verify
- [ ] Exponent in Eq. 2 (printed "2..2"; assumed 2.2).
- [ ] Extensometer gauge length (Fig. 2 shows a 230 mm narrow region; Yang 2024 used 150 mm on the same geometry).
- [ ] Identity of "mineral powder" (GGBFS?) and the W/B (computed 0.30 / 0.32).
- [ ] M2-0.5 peak stress 1.16 MPa < M2-0 2.23 MPa (Table 8).
- [ ] Why plain 2% PVA-HDC reaches only 0.34–0.45% peak strain here.
- [ ] Number of data sets for Eq. 2 (68) vs 72 TR specimens (24 groups × 3).
