---
type: concept
slug: interface-bond
aliases: [substrate bond, overlay bond, ECC-concrete interface, slant shear, interlayer bond, interlayer strength, rebar-ECC bond, bond-slip, delamination, debonding]
tags: [interface, repair, strengthening, 3d-printing, rebar, structural]
sources: [yuan2020-nshsdc-beam-strengthening, wang2019-rc-beam-ecc-shear-strengthening, xue2023-shcc-structural-review, tabrizikahou2022-masonry-ecc-sma-retrofit, kunieda2006-hpfrcc-japan-applications, li2003-ecc-review, yang2024-hshdc-uniaxial-tension, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, wang2023-ecc-frost-damage, lee2021-hsdc-wall-emi-impact, kunieda2010-uhp-shcc-steel-reinforcement]
updated: 2026-10-20
---

# Interface Bond (HDC/ECC to substrate, interlayer, and rebar)

## Definition
The bond across a **macroscopic interface** between an HDC/ECC/SHCC and another body. Three cases appear in the corpus:
1. **Substrate bond:** an ECC overlay, jacket or repair layer on existing concrete or masonry.
2. **Interlayer bond:** between successive layers of 3D-printed SHCC.
3. **Rebar bond:** between a steel bar and the surrounding ECC.

This is different from the micro-scale fiber/matrix bond (τ0, Gd), which is covered in [[fiber-matrix-interface]].

## Key points
- **Bond is a first-order design parameter for overlays.** All 40 mm sprayed ECC side layers on RC beams debonded,
  and some 20 mm layers peeled off after failure ([[wang2019-rc-beam-ecc-shear-strengthening]], §3.3.3, Fig. 7).
  The authors cover this with an empirical efficiency factor η (0.6 for 20 mm, 0.4 for 40 mm) in their shear model (§4.3.1)
  and advise limiting layer thickness (Conclusions). → [[rc-member-strengthening]], [[shear-behaviour]]
- **In FE, the assumed interface law changes the result about 2×.** The dissipated energy of ECC-retrofitted masonry
  walls was 25–29 MJ with a cohesive interface, 24–28 MJ tied, and 14 MJ with hard contact (µ = 0.4)
  ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], Table 8). The cohesive stiffness was K = 28,000 MPa (Eq. 12).
  ⚠️ The energy magnitudes look implausibly large (see that source page). → [[masonry-wall-retrofit]]
- **Strengthening layers end in debonding:** 10 and 30 mm SHCC layers on RC beams failed by crack localisation, then
  debonding; thicker layers and a roughened interface are said to reduce delamination (Wang 2020, as cited in
  [[xue2023-shcc-structural-review]], §4.1, Table 1). Substrates were roughened by retarder wash-out (§4.2).
- **Good bond can restrict ductility.** A bonded HPFRCC overlay is constrained by the substrate and may concentrate
  cracking over an existing crack; an unbonded zone spreads the cracking (Kunieda 2004, as cited in
  [[kunieda2006-hpfrcc-japan-applications]], p. 22–23, Fig. 9). → [[multiple-cracking]]
- **Earlier claim:** ECC repairs absorb interface defects without spalling or delamination (Lim & Li 1997, as cited in
  [[li2003-ecc-review]], p. 225). The structural tests above qualify this. → [[repair-and-field-applications]]
- **Gap noted by the Xi'an group:** the bond between HSHDC and existing concrete "still needs study"
  ([[yang2024-hshdc-uniaxial-tension]], p. 14). [[yuan2020-nshsdc-beam-strengthening]] is the first primary
  bond test in the wiki.

## Quantitative evidence

### Substrate bond: slant shear, NSHSDC on normal concrete
ASTM C882, 100 × 100 × 300 mm prisms, 28 d, mean of 3; LS = as-cast (low roughness), HS = chiselled (high roughness)
([[yuan2020-nshsdc-beam-strengthening]], Table 7):

| Interface angle | LS τ (MPa) | HS τ (MPa) | Failure (LS / HS) |
|---|---|---|---|
| 30° | 16.4 | 20.9 | concrete crushing / – |
| 45° | 14.5 | 21.4 | near-interface concrete cracking / concrete crushing |
| 60° | 6.1 | 13.2 | near-interface cracking / interface sliding |
| 75° | 3.1 | 5.3 | near-interface cracking / interface sliding |

- Chiselling raises slant shear strength by about 27% (§3.1.1, Fig. 6).
- High-roughness interfaces meet the ACI 546 range (14–21 MPa at 28 d) except at 75°; low-roughness ones only at
  30–45° (Fig. 7).
- Codes are conservative: mean τ/τ_pred 22.5 (ACI 318-19), 1.5 (AASHTO), 3.6 (CSA), 1.7 (MC2010) (Table 7).
  ⚠️ The conclusion gives 1.27–2.17, which does not match Table 7.
- In the beam tests, no NSHSDC jacket delaminated (substrate chiselled 40 mm bottom / 20 mm sides and top) (§3.2.1).
- The same Korea Univ. group cast 5–20 mm HSDC skins on chiselled NC panels for impact tests
  ([[lee2021-hsdc-wall-emi-impact]], §2.1). → [[impact-resistance]], [[hshdc]]

### Substrate preparation reported
| Source | Substrate | Preparation | Outcome |
|---|---|---|---|
| [[wang2019-rc-beam-ecc-shear-strengthening]], §3.1 | RC beam sides | chiselled, saturated-surface-dry, interface agent (0.85 cement + 0.05 SF + 0.1 expansive agent + 0.3 water, by mass); ECC sprayed | 40 mm layers all debonded; 20 mm partly |
| [[yuan2020-nshsdc-beam-strengthening]], §2.2.2 | NSC beams | chiselled | no delamination |
| [[xue2023-shcc-structural-review]], §4.2 | RC beams | retarder wash-out roughening | debonding after layer crack localisation (10, 30 mm) |
| [[tabrizikahou2022-masonry-ecc-sma-retrofit]] | URM wall (FE) | epoxy/resin-bonded precast sheets (modelled) | interface law dominates energy |

### Interlayer bond in 3D-printed SHCC
| Source | Material | Test | Result |
|---|---|---|---|
| [[chavesfigueiredo2020-printed-shcc]], §3.5, Fig. 14 | printed PVA-SHCC (2 vol.%), 28 d | direct tension on 10 × 10 × 20 mm prisms across the interface; 3 vs 36 min interval | brittle, no strain hardening (few fibers cross the interface), but interface strength comparable to or above the bulk first-crack strength; interval had no significant effect; interface had the **lowest** air-void content (Figs. 15–16) |
| [[ivaniuk2022-printable-shcc-design]], Table 3, §3.2.2 | printed PE-SHCC (1.5 vol.% 6 mm PE), 28 d | 3PB across the interlayer (D3) vs along layers (D1) | Ref: 18.5 (D3) vs 22.0 MPa (D1); lower D3 attributed to a weaker interlayer |

⚔️ **Conflict:** the interlayer is *not* the weak zone in [[chavesfigueiredo2020-printed-shcc]] (which also cites
Wolfs 2019 and Feng 2015 reporting weaker interfaces), but *is* weaker in [[ivaniuk2022-printable-shcc-design]].
Mix, fiber, nozzle and test differ (direct tension vs bending). → [[3d-printed-hdc]], [[gaps]]

### Rebar–ECC bond
Central pull-out, HRB335 Ø12 mm, bond length 7d (84 mm), 0.5 mm/min ([[wang2023-ecc-frost-damage]], §2.6, Tables 6–7):

| Material | Freeze–thaw cycles | τu (MPa) | Peak slip (mm) | Failure |
|---|---|---|---|---|
| PVA-ECC | 0 | 18.22 | 0.665 | pull-out |
| PVA-ECC | 100 | 17.30 | 0.569 | pull-out |
| PVA-ECC | 300 | 16.14 | 0.387 | pull-out |
| Normal concrete (W/C 0.5) | 0 / 25 / 50 | 14.38 / 9.03 / 6.51 | rises with cycles | splitting |

- ⚠️ The text gives ECC bond losses of −19.1% / −24.5%, but Table 7 gives −5.0% / −11.4% (computed by the ingest).
- The authors state that bond-slip laws for concrete do not apply to ECC and that steel–ECC bond after frost damage
  is little studied (§1). → [[freeze-thaw]], [[durability]]
- **Composite action of steel and SHCC in tension:** D6 bars at ρs 0.3% restore strain hardening in 50 mm-thick
  UHP-SHCC tension members (119 vs 43 cracks) ([[kunieda2010-uhp-shcc-steel-reinforcement]], Table 3). Rebar bond
  is assumed, not measured, there. → [[multiple-cracking]]

> Synthesis:
> - Splitting does not occur around bars in ECC (pull-out failure, [[wang2023-ecc-frost-damage]]), so rebar bond is
>   governed by the ECC's tensile ductility, not by cover cracking.
> - For overlays, the evidence points two ways. Thin, well-bonded layers are restrained and crack only over the
>   substrate crack ([[kunieda2006-hpfrcc-japan-applications]]; [[xue2023-shcc-structural-review]]). Thick layers
>   (≥ 30–40 mm) tend to debond ([[wang2019-rc-beam-ecc-shear-strengthening]]; [[xue2023-shcc-structural-review]]).
>   Chiselled NSHSDC jackets did not debond ([[yuan2020-nshsdc-beam-strengthening]]). Roughness and layer thickness
>   both matter, but no study varies them together.
> - The only quantitative substrate-bond data are slant shear values for one Korean steel + PE mix. Direct-tension
>   (pull-off) or shear bond tests for PVA-ECC/HDC on concrete are absent from the corpus.

## Conflicts & open questions
- ⚔️ Printed SHCC interlayer: stronger than bulk first crack ([[chavesfigueiredo2020-printed-shcc]]) vs weaker in
  flexure ([[ivaniuk2022-printable-shcc-design]]).
- ⚔️ "ECC repairs avoid delamination" (Lim & Li 1997 via [[li2003-ecc-review]]) vs debonding of all 40 mm sprayed
  layers ([[wang2019-rc-beam-ecc-shear-strengthening]]) and of 10/30 mm layers ([[xue2023-shcc-structural-review]]).
  Different loading (repair under shrinkage vs structural shear/flexure).
- Open: no pull-off or direct-shear bond data for PVA-ECC/HDC on concrete; no bond-slip law for rebar in HDC;
  no test of bond durability (wet–dry, freeze–thaw) for overlays.

## Related
- [[fiber-matrix-interface]] · [[rc-member-strengthening]] · [[repair-and-field-applications]] · [[masonry-wall-retrofit]] ·
  [[3d-printed-hdc]] · [[multiple-cracking]] · [[freeze-thaw]] · [[hshdc]] · [[gaps]]
