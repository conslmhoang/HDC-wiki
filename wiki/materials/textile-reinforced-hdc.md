---
type: material
slug: textile-reinforced-hdc
aliases: [TR-HDC, TR-ECC, textile-reinforced ECC, TRC, TRM, textile-reinforced concrete, textile-reinforced mortar, basalt textile grid, FRCM]
tags: [material, textile, composite-reinforcement, strengthening, basalt]
sources: [zhang2022-hdc-basalt-textile-tension, he2024-hdc-research-advances]
updated: 2026-10-21
---

# Textile-Reinforced HDC (TR-HDC)

## Definition
HDC with built-in textile grids (continuous resin-impregnated fibre rovings) placed in layers. XAUAT calls it
**"TR-HDC"**; the same specimens without short PVA fibres are called **"TRC"** (textile-reinforced concrete); the
HDC matrix is described as "also called ECC" ([[zhang2022-hdc-basalt-textile-tension]], §1–2).
It is a hybrid reinforcement: the textile carries the main tensile force, and the short fibres control cracking and
yarn–matrix bond. Not to be confused with short-fibre hybrids on [[hybrid-fiber]].

> Note: the plain HDC matrix in the only primary source barely strain-hardens (peak strain 0.12–0.45%); strain
> hardening with multiple cracking is shown for the textile-reinforced specimens
> ([[zhang2022-hdc-basalt-textile-tension]], Table 8). → [[tensile-strain-capacity]]

## Key points
- **Why:** textile-reinforced mortar (TRM/TRC) is less effective than FRP and fails by textile slip; its matrix has
  low elongation and large cracks and stops carrying load after cracking. HDC as the bonding matrix is meant to raise
  textile utilisation ([[zhang2022-hdc-basalt-textile-tension]], §1; [[he2024-hdc-research-advances]], p. 20).
- **Failure mode switches with PVA content:** TRC (0% PVA) and ≤ 1% PVA fail mainly by textile slip and matrix
  spalling, crack spacing ≈ grid spacing (25 mm); 1.5–2% PVA gives **textile rupture**, denser multiple cracking up
  to peak and no spalling ([[zhang2022-hdc-basalt-textile-tension]], §3.1, Tables 6–7, Conclusion 1). → [[multiple-cracking]]
- **Roles:** peak stress is set mainly by textile level; cracking stress mainly by PVA content (§3.2, Table 8).
- **Peak strain falls when PVA is added** (e.g. B3M1: 2.65% → 1.96–2.13%), because PVA suppresses textile slip (§4.2, Fig. 8).
- **Utilisation α falls with more layers** (M1-2: 1.10 → 0.60 → 0.59 for 1 → 3 layers): capacity is not a simple
  superposition of rovings; α > 1 at one layer + 2% PVA (1.10 / 1.07) shows the short fibres carry load too (§4.1, Table 8).
- **Matrix:** a high-volume-fly-ash matrix (FA/C 3.25) gives higher TRC strain and lower peak stress than FA/C 1.1; at
  1.5–2% PVA the two matrices give similar capacity (§4.3, Table 8). → [[fly-ash]]
- **Bond mechanism (claimed, not measured):** PVA fibres on the yarn surface add "connecting points" and improve
  yarn–matrix bond (§4.2). → [[interface-bond]]

## Quantitative evidence ([[zhang2022-hdc-basalt-textile-tension]], Tables 3–4, 8; 28 d, standard curing)
Basalt grid 25 × 25 mm; single roving 1285 MPa, 2.9% rupture strain, E 44 GPa (Table 4). Grid level ν = 0.42 / 0.84 /
1.26% for 1 / 2 / 3 layers in a 50 × 15 mm dogbone section. PVA 12 mm × 39 µm, 1600 MPa, 40 GPa.

| Group (matrix) | 0% PVA (TRC) σ_u (MPa) / ε_u (%) / mode | 1.5% PVA | 2% PVA |
|---|---|---|---|
| plain M1 (Type I, f_cu 52–58 MPa) | 3.41 / 0.11 | 3.89 / 0.12 | 5.44 / 0.34 |
| B1M1 (1 layer) | 4.20 / 2.22 / slip + clamp | 4.78 / 1.20 / rupture | 6.11 / 1.51 / rupture |
| B3M1 (3 layers) | 7.79 / 2.65 / slip | 9.68 / 1.96 / rupture | 9.73 / 2.13 / rupture |
| plain M2 (Type II, f_cu 30–38 MPa) | 2.23 / 0.024 | 3.45 / 0.28 | 4.23 / 0.45 |
| B1M2 | 3.32 / 2.71 / rupture + slip | 4.75 / 1.53 / rupture | 5.83 / 1.64 / rupture |
| B3M2 | 6.82 / 3.79 / slip | 9.94 / 2.41 / clamp + rupture | 10.02 / 2.48 / rupture |

ε_u = strain at peak stress. Test: XAUAT dogbone 350 mm, clevis grips, 0.2 mm/min, one extensometer (gauge n.s. ⚠️).
→ [[dogbone-uniaxial-tension]]

## Design formulas
- Peak stress: σ_T = α·f_t,b·A_t/A_m, α = 0.005·e^(2.2√(β/ν)) + 0.53 (β = PVA vol.% 0–2, ν = 0.42–1.26%; 25 mm basalt grids;
  68 data sets; exponent printed "2..2" ⚠️) ([[zhang2022-hdc-basalt-textile-tension]], Eqs. 1–2).
- σ–ε model: ACK trilinear for ≤ 1% PVA; bilinear for 1.5–2% PVA with σ_cr = 0.896·E1·σ_t/E_HDC and a Eurocode-2-type
  peak-strain relation (Eqs. 3–17); "roughly matched", no error statistics. → [[tensile-constitutive-model]]

## Applications (second-hand)
- TR-HDC slabs for strengthening (Song 2023/2024, as cited in [[he2024-hdc-research-advances]], p. 19–20).
- Carbon/glass TR-HDC (Dong et al. 2020, ref. 23 in [[zhang2022-hdc-basalt-textile-tension]]) — not ingested.
- TRM for URM walls is less effective than FRP (refs 8, 12–15 in [[zhang2022-hdc-basalt-textile-tension]]). → [[masonry-wall-retrofit]]
- No member-level TR-HDC test is in the corpus. → [[rc-member-strengthening]]

> Synthesis: in TR-HDC the textile, not the HDC, sets capacity, and the HDC's job is to change failure from slip to
> rupture and to spread cracks. About 1.5% PVA is the threshold for that switch in the one primary study. Because the
> plain matrix there barely hardens (≤ 0.45%), the benefit comes from fibre bridging and yarn bond, not from HDC
> tensile ductility; whether a more ductile HDC (≈ 1–3%) would change the picture is untested.

## Conflicts & open questions
- ⚔️ Plain XAUAT PVA-HDC strain in this study (0.34–0.45% at 2% PVA) is far below other XAUAT reports (≈ 1.0–3.0%).
  → [[tensile-strain-capacity]], [[gaps]]
- Empirical α and σ–ε model; need validation for other textiles (carbon, glass), grid spacings, layer positions and fibre
  contents ([[zhang2022-hdc-basalt-textile-tension]], §5, §6.2, Conclusion 3).
- No yarn pull-out test in HDC, no crack widths, no durability or long-term data, hand lay-up only (observed).
- "Mineral powder" in the matrix is undefined; W/B not stated (computed 0.30 / 0.32).

## Related
- [[rc-member-strengthening]] · [[masonry-wall-retrofit]] · [[hshdc]] · [[hybrid-fiber]] · [[pva-fiber]] ·
  [[tensile-constitutive-model]] · [[multiple-cracking]] · [[terminology-hdc-ecc-shcc]]
