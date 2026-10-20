---
type: source
slug: deng2019-urm-shaking-table-hdc
title: "Shaking table tests of a half-scale 2-storey URM building retrofitted with a high ductility fibre reinforced concrete overlay system"
authors: [Mingke Deng, Zhifang Dong, Xuesong Wang, Yangxi Zhang, Tiegang Zhou]
year: 2019            # vol. 197 (2019); received 2 Jan 2019, available online 30 Jul 2019
venue: "Engineering Structures, vol. 197, Article 109424 (Elsevier)"
doi: "10.1016/j.engstruct.2019.109424"
raw_file: raw/papers/Deng2019_URM-shaking-table-HDC.pdf
material_term: "HDC = high ductility fibre reinforced concrete (FRCC 'like' ECC and HPFRCC)"
study_type: experimental (structural, shaking table, 17 runs, three phases on one model)
tags: [structural, seismic, masonry, urm, shaking-table, overlay, retrofit, pva, xauat, deng-group]
ingested: 2026-10-21
updated: 2026-10-21
---

# Shaking-table test of a URM building with an HDC overlay (Deng et al., 2019)

## One-paragraph summary
XAUAT built a **half-scale two-storey unreinforced masonry (URM) building** (3.42 × 3.42 × 3.3 m, 120 mm walls
of half-size fired bricks, open ground-floor front with three RC columns), typical of village shop-houses in SW
China (p. 2, Figs. 1–4). The **same model** was tested in three phases (17 runs, El Centro, Wenchuan and an
artificial record, nominal PGA 0.094–1.171 g; Table 5):
- **M1**: unretrofitted, to near local collapse (stopped at M1-8.5, actual PGA 0.362 g);
- **M2**: cracks grouted, pier rebuilt, **welded wire reinforcement (WWR) + 25 mm mortar** on the north walls,
  tested to "9-degree rare" (1.171 g);
- **M3**: WWR removed, cracks grouted again, **15 mm PVA-HDC overlay** (north walls double/single-sided, plus
  first-floor east and west walls single-sided), tested to 1.171 g (p. 4, Fig. 9).

M3 showed only fine, grouped cracks with **no main crack and no overlay detachment**, frequency loss 10.9% / 8.1%
(E-W / S-N) vs 27.5% / 30.0% for M2 (p. 9), smaller E-W drifts than M2 at every level (Table 7), and reached
Level 1 performance under a 9-degree earthquake (p. 14). The HDC strain-hardens in direct tension (Fig. 6a):
σ_tu 5.83 MPa, ultimate strain 1.0%.

## Objective / research question
- Dynamic response and seismic behaviour of URM buildings retrofitted with an HDC overlay, compared with a WWR
  (ferrocement-type) overlay; backbone curve, torsion and performance-level evaluation (p. 1–2).
- Motivation: ferrocement and FRP retrofits are too costly and slow for village buildings (p. 1).

## Terminology (rule §3)
- Authors' exact term: **"high ductility fibre reinforced concrete (HDC)"**, "a class of fibre-reinforced cementitious
  composite like ... ECC ... and HPFRCC, which exhibits a strain-hardening behavior in tension and a high toughness in
  compression" (p. 1).
- **Tensile strain hardening is measured** (Fig. 6a): three plate specimens, first cracking at about 5.2–5.8 MPa,
  stress rising with load drops to about 6.4–6.6 MPa, failure at about 0.86–1.0% (read from figure ⚠️).
  Text: "ultimate tensile strain reached 1.0% with clear strain-hardening behavior" (p. 3).
- Test method named: **DBJ61/T112-2016**, "Technical specification for application of high ductile concrete"
  (Shaanxi provincial standard, ref. [20]), 15 mm thick plates (p. 3). Not ingested.
- Strain capacity 1.0% is above the 0.5% HDC threshold (JC/T 2461-2018, see [[chai2023-hdc-ambient-temperature]])
  but below the ECC convention (> 3%). See [[terminology-hdc-ecc-shcc]].

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| HDC | 1 | 1 (FA/C 1.0, by mass) | none | 0.72 (type and max size not reported) | 0.29 (computed: 0.58/2, by mass) | HRWR 8 kg/m³ | PVA (σ_f 1600 MPa, E 32 GPa, elong. 7%, SG 1.3) | 12 | 39 | 2 |

Units of binder quantities: mass ratio cement : FA : sand : water = 1 : 1 : 0.72 : 0.58 (p. 3); fiber data Table 2.
> Synthesis: with cement 593 kg/m³ the ratios reproduce the XAUAT base mix 593 / 593 / 427 / 344 of
> [[deng2017-rc-column-hdc-jacket]] and [[deng2018-hdc-short-columns]] (computed here).

Other materials (p. 3, Table 3): MU10 fired clay bricks 13.0 MPa (10 samples, GB 5101-2003); M5 mortar 6.1 MPa
(70.7 mm cubes, 28 d); masonry f_c 4.01 MPa, f_t 0.35 MPa, E 2971 MPa, initial shear strength 0.31 MPa (GB 50003-2011);
concrete 37.89 MPa (100 mm cubes); HPB300 428.62 MPa, HRB400 493.84 MPa.

## Test methods
- **HDC material:** 6 cubes 100 mm at 28 d (f_cu, E); tension on 3 plates 15 mm thick per DBJ61/T112-2016 (plate
  length/width, gauge length, rate not reported ⚠️) (p. 3). Curing of HDC specimens not reported.
- **Model:** half-scale (S_L 0.5, S_E 1, S_m 0.136, S_a 1.838, S_T 0.522; Table 1); "model ignoring gravity" with
  1.11 t added mass; total mass 19.8 t (p. 2). Out-and-in bond brickwork; no ties between walls and columns or ring
  beams (p. 3).
- **Retrofits:**
  - WWR (M2): Ø4 horizontal / Ø6 vertical mesh, Ø4 ties, 25 mm mortar; north walls only (Fig. 8).
  - HDC (M3): 15 mm overlay; Ø8 bars at wall corners against junction failure; wall surface cleaned of dust and loose
    material only (p. 4, Fig. 9). No mesh in the HDC overlay; no special anchorage reported.
- **Shaking table:** MTS 4 × 4 m, 6 DOF, 300 kN (Table 6); bi-directional inputs EQ1 (El Centro 1940), EQ2
  (Wenchuan 2008), EQ3 (artificial, GB 50011-2010) scaled to the nominal PGA; 0.05 g white noise between runs (p. 4).
  M3 was only tested at 0.189, 0.378, 0.756 and 1.171 g, with EQ1 only at the first two.
- **Instrumentation:** 22 accelerometers, 10 LVDTs (4 roof-corner LVDTs for torsion, M3 only) (p. 5, Figs. 11–12).
- **Indices:** stiffness degradation η = (f² − f0²)/f0²; inter-storey drift; acceleration amplification K;
  base shear from floor masses × accelerations (Eqs. 1–4); torsion angle (Eq. 5); wall shear capacity
  V = V_ME + 0.7 f_dt·b·h, i.e. URM capacity per GB 50003-2011 plus 0.7 × HDC tensile strength × overlay thickness ×
  wall length (Eq. 8).
→ [[masonry-wall-retrofit]], [[dogbone-uniaxial-tension]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HDC | f_cu 61.15 (100 mm cube, 28 d, 6 cubes) | about 5.2–5.8 (Fig. 6a ⚠️) | 5.83 (mean of 3 plates, Table 3) | 1.0 "ultimate" (p. 3); individual curves end about 0.86–1.0% (Fig. 6a ⚠️) | not reported | E 9789 MPa (Table 3) |

Model results:

| Quantity | M1 (URM) | M2 (WWR) | M3 (HDC) | Location |
|---|---|---|---|---|
| Initial period E-W / S-N (s) | 0.12 / 0.08 | 0.08 / 0.06 | 0.09 / 0.07 | p. 5 |
| Frequency drop after phase, E-W / S-N | 26.1% / 14.5% | 27.5% / 30.0% | **10.9% / 8.1%** | p. 9 |
| Stiffness degradation η, E-W / S-N | 45.4% / 27.0% | 47.4% / 50.9% | **20.6% / 15.6%** | p. 9 |
| Max storey-1 drift E-W at 0.378 g | 1/463 | 1/239 | 1/361 | Table 7 |
| Max storey-1 drift E-W at 1.171 g | — (stopped) | 1/76 | 1/84 | Table 7 |
| Damage after phase | near local collapse at 0.362 g actual | overlay mortar heavily cracked, needs repair | slight; fine grouped cracks, no detachment | p. 7–8 |
| Performance level (GB 50011) | Level 4 at 8-degree | Level 4 at 9-degree | **Level 1** at 9-degree | p. 14 |

Main findings (with Table/Fig. location):
- **Damage:** M3 showed no cracks up to 0.387 g; fine cracks grew into "grouped cracks" without a main crack at 0.756
  and 1.171 g; south, west and east walls had no significant cracks (p. 8, Fig. 16).
- **Drift:** M3 drifts are smaller than M2 at every level in E-W; about the same in S-N (Table 7, p. 10).
  First-storey drift dominates because the ground-floor south wall is absent (p. 10).
- **Backbone (M3, EQ1):** base shear rose roughly linearly to about ±200 kN at a global roof drift of 0.155%
  (Test M3-9R) without significant stiffness degradation (p. 12, Fig. 20 ⚠️ read from figure).
- **Base shear / weight** (Fig. 21, E-W, read from figure ⚠️): M1 peaks at about 0.8 at 0.19 g nominal, then drops;
  M2 and M3 rise almost linearly to about 1.5 at 1.171 g, with M2 slightly above M3 at the highest levels.
- **Acceleration amplification:** M3's K rises smoothly with height; M1 shows a sharp out-of-plane peak at 0.9 m;
  M2's K drops abruptly at M2-9R (p. 11, Fig. 19).
- **Torsion (M3):** max torsion angle 1/4352, 1/2289, 1/980, 1/328 at M3-7 to M3-9R; mass–stiffness eccentricity
  up to 964 mm; torsion shear in wall QY1 = 50.9 kN (storey 1) and 24.4 kN (storey 2), 34.4% and 41.6% of the
  horizontal force; all walls had capacity/demand γ = 1.19–8.12 (> 1) at M3-9R (Table 8, p. 13).
- **Proposed drift limits for HDC-retrofitted masonry:** intact 1/400, slight damage 1/170, moderate 1/90
  (Conclusion 5). ⚠️ Table 10 lists M3 intactness as 1/370, not 1/400.

## Mechanisms / explanations offered by authors
- The overlay's "high tensile strength" and "collaborative work with the masonry" control cracking and keep overlay
  damage small (p. 10, Conclusion 2).
- The HDC overlay raises global stiffness and damage tolerance, delaying stiffness degradation (p. 9–11).
- Shear contribution of the overlay is modelled as 0.7 f_dt·b·h, i.e. through HDC tensile strength (Eq. 8).

## Limitations (stated + observed)
- Stated: serious-damage and near-collapse states were not reached in M3, so their drift limits could not be found;
  the "moderate damage" limit is conservative (p. 14–15).
- Observed:
  - **One model tested three times.** M2 and M3 are repaired, pre-damaged structures; M3 inherits damage from
    phases I and II. The comparison is not between identical virgin specimens.
  - **Retrofits are not equivalent:** WWR on north walls only (25 mm mortar); HDC on north walls plus first-floor
    east and west walls (15 mm). Retrofit area and thickness differ.
  - M3 was tested in fewer runs (4 levels, EQ1 only at two of them), so it saw less cumulative excitation than M2.
  - Fig. 21 does not show a higher base shear for M3 than M2, though the text says HDC improved shear capacity more.
  - No bond or pull-off test of HDC on brick; no overlay crack widths; HDC curing not reported; tension plate
    geometry not given.
- Internal inconsistencies:
  - "serious damage occurred after Test M1-8 (PGA = 0.189 g)" (p. 12), but M1-8 is 0.376 g in Table 5.
  - Mean σ_tu 5.83 MPa (Table 3) is below the peaks of all three curves in Fig. 6a (about 6.4–6.6 MPa) ⚠️.
  - Fig. 19d legend labels M3 curves as "M1-7 … M1-9R".
  - Conclusion 5 intactness drift 1/400 vs Table 10 1/370.

## Relation to other work
- Agrees with:
  - [[deng2017-rc-column-hdc-jacket]] and [[deng2018-hdc-short-columns]] (same group, same mix): HDC prevents
    spalling and spreads damage into fine cracks.
  - [[he2024-hdc-research-advances]] (p. 9) summarises this paper correctly: 2% PVA HDC overlay on a half-scale
    2-storey URM building outperformed the WWR overlay. The review's "high-strength, high-modulus PVA" is not stated
    here (σ_f 1600 MPa, E 32 GPa in Table 2).
- Contradicts / refines: ⚔️
  - The HDC tensile curves in Fig. 6a (first crack ≈ 5.2–5.8, peaks ≈ 6.4–6.6 MPa, ≈ 1.0%) closely resemble those
    reported for [[deng2018-hdc-short-columns]] (cracking 5.73, σ_tu 6.14 MPa, ≈ 1.0%); the same data may have been
    reused ⚠️. Both are below the ≈ 3.0% ultimate strain of the same nominal mix in [[deng2017-rc-column-hdc-jacket]].
  - Fiber modulus here 32 GPa for a 1600 MPa PVA, vs 40 GPa for the 1600 MPa (Japanese) PVA in
    [[deng2017-rc-column-hdc-jacket]] and [[deng2018-hdc-short-columns]] ⚠️.
- Extends:
  - **First primary experimental masonry-retrofit study in the wiki** (until now only FE:
    [[tabrizikahou2022-masonry-ecc-sma-retrofit]]). Unlike that FE model, the HDC here is shown to strain-harden.
  - Cites a Deng & Zhang ECC-jacket short-column paper: **Deng M, Zhang Y, Li Q. "Shear strengthening of RC short
    columns with ECC jacket: cyclic behavior tests", Eng. Struct. 2018;160:535–45** (ref. [17]). This is very likely the
    "Deng & Zhang 2018" jacketing study cited by [[he2024-hdc-research-advances]], i.e. a different paper from
    [[deng2018-hdc-short-columns]] (not ingested; "cross-shaped" still unverified).
  - Also cites XAUAT masonry work not in the corpus: ECC splints on brick walls (Deng, Gao & Liang 2013; Deng et al.
    2015) and confined masonry walls with a single HDC layer (Deng, Yang & Liang 2018).

## Pages updated from this source
- [[masonry-wall-retrofit]]
- [[interface-bond]]
- [[terminology-hdc-ecc-shcc]]
- [[tensile-strain-capacity]]
- [[pva-fiber]]
- [[dogbone-uniaxial-tension]]
- [[repair-and-field-applications]]
- [[he2024-hdc-research-advances]]
- [[deng2018-hdc-short-columns]]
- [[deng2017-rc-column-hdc-jacket]]
- [[mix-designs]]
- [[mechanical-results]]
- [[gaps]]

## To verify
- [ ] Fig. 6a readings (first crack 5.2–5.8 MPa, peaks 6.4–6.6 MPa, ultimate 0.86–1.0%) and why mean σ_tu is 5.83 MPa ⚠️ unverified.
- [ ] Whether Fig. 6a reuses the tension data of [[deng2018-hdc-short-columns]] Fig. 1.
- [ ] DBJ61/T112-2016 plate dimensions, gauge length and loading rate (standard not ingested).
- [ ] HDC curing regime (cube age 28 d stated; curing not).
- [ ] PVA modulus 32 GPa (Table 2) vs 40 GPa in the 2017/2018 XAUAT papers.
- [ ] Fig. 20 / Fig. 21 values (±200 kN; BS/W ≈ 1.5) read from figures.
- [ ] "M1-8 (PGA = 0.189 g)" on p. 12 vs Table 5; intactness drift 1/400 vs 1/370.
- [ ] Ref. [17] Deng, Zhang & Li 2018 (Eng. Struct. 160:535–45) as the He 2024 "Deng & Zhang 2018" jacketing citation; obtain the paper.
