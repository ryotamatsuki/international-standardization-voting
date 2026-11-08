# Independent adversarial novelty audit — International Standardization Voting
Date: 2026-11-08
Reviewed source branch at start: `research/p1-proof-novelty-gate-20261108` / `b50f6596c36689f97a6b7a9f8fb40f7cfae67d6f`; main base `8feb4a242eaa7cb8c186a7e0f82fe76ba003cb02`.
Reviewer stance: independent, critical, not a proof of first-in-literature. Do not quote this assessment as an external peer review.

## Overall decision
**Substantive novelty NOT YET DEMONSTRATED.** The particular symbolic Salop threshold and open-set example are valid conditional computations, but the mechanism "incumbents preserve competitive/network rents at the expense of compatibility" is established in network-effects literature, while the aggregation of national payoffs under a 3-of-4 rule is an immediate voting-game consequence. No exact mathematical theorem subsumption by any of the checked original four papers has been demonstrated. Current best description: **tier 3 (easy application) for the ballot aggregation; tier 4 (partial novelty) for the specific derived international industry/committee configuration, conditional on stronger originality proof**. **Tier 5 is not substantiated.** Do not submit to IJIO on P1 alone; Journal of Economics or RIO require particular attention to the near-prior 2023 and 2025 articles below.

## Literature provenance matrix
| Source | Evidence verified | Theorem-specific findings | Equivalence verdict / limits |
|---|---|---|---|
| Gandal & Shy (2001), *JIE* 53:363–383 | **Uploaded final published PDF, all 21 pages** | §2 price equations (2)-(4), welfare (10)-(11); Proposition 1 mutual recognition dominant with conversion costs; Propositions 2–3 exclusionary two-state union when high conversion costs; §3.3 asymmetric country size; Proposition 4 network-effect mutual recognition dominant without unions; Proposition 5 and §4.2.2 no profitable exclusionary network union | Same home CS + owned-firm global-profit aggregation, network compatibility, Salop pricing and country sizes. BUT 3-country recognition/unions not automatically a special case of 4-country 3+1 legacy network and vote; no formal full embedding asserted. Mechanism rent diversion inherited; different conditional payoff effects in full vs no recognition. |
| Barrett & Yang (2001), *JIE* 54:171–191 | Published abstract; **August 1999 revised WP** full PDF at https://ageconsearch.umn.edu/record/14597/files/wp9909.pdf | WP version gives established installed-base incentive to maintain local standards; government may value deviations; propositions concerning incumbent incompatibility, network size and national trade | Strong mechanistic overlap with rational incompatibility. WP not proven identical to final publication; exact published theorem inclusion unknown. No 4-country ISO ballot in identified WP. |
| Klimenko (2009), *JIE* 77:151–166 | Publisher abstract + preview only https://doi.org/10.1016/j.jinteco.2008.08.005 | Governments' strategic compatibility rules can create excessive or low compatibility, depending on network intensity | Strong comparative-static conceptual overlap. **Full text propositions unavailable**, theorem inclusion unresolved; never say the phenomenon is absent there. |
| Spulber (2019), *Economic Journal* 129:1477–1509 | **Final published full-text Wiley HTML** https://doi.org/10.1111/ecoj.12606 | **Published Proposition 6:** with no SEPs vertical adopter groups elect welfare-efficient standard by majority; **published Corollary 2:** votes for efficient standard nondecreasing in innovation quality | No direct subsumption: vertically related users vs four countries horizontally competing firms, and technology quality parameter not equal to P1 network strength. Not a contradiction of Spulber; voting plus post-vote market competition already known. **Do not confuse with numbering in Spulber's 2016 WP.** |
| Goerke & Holler (1995), *Public Choice*, Voting on Standardisation | Publication abstract; no complete proof audit | Standards with voting and supermajority in network economy | Majority rule and possible welfare divergence cannot be declared novel. |
| Farrell & Simcoe (2012), *RAND*; Simcoe (2012), *AER* | Previous repository audit uses pre-publication author versions (2009/2010) | Committee bargaining, delay, incumbent interests, strategic consensus | A technical-objection bargaining/delay innovation must beat this prior art. Published version theorem numbers not imported from WPs. |
| Diekmann (1985), *JCR* | Earlier Gate 4 audit + direct normal-form mapping | Two-person Volunteer's Dilemma | Exact strategic equivalence: Gate 4 two-opponent filing game is volunteer's dilemma after adding a player-specific constant. **Tier 2: mathematically equivalent.** |
| Buccella, Fanti & Gori (2023), *Journal of Economics* 140:141–168 | Open access published article https://doi.org/10.1007/s00712-023-00834-x | Cournot compatibility-decision game; with fixed costs endogenous compatibility generates distinct and multiple SPNE, welfare comparison | Voluntary company adoption/compatibility cannot alone be claimed original; not identical to country ballots / four-firm Salop. |
| Cheng & Huang (2025), *Journal of Economics* 145:31–57, online 2024-12-30 | Published **abstract only** https://doi.org/10.1007/s00712-024-00896-5 | With firms holding veto power over compatibility, *high network externalities lead to incompatibility*, whereas without veto compatibility emerges | **Major additional novelty threat:** same direction of network-intensity effect despite different primitive and firm veto vs country vote; full propositions/proofs **not yet checked**, so no exact theorem subsumption claim. |
| Buccella et al. (2026 issue), *Economics of Innovation and New Technology* | Title/abstract from publication listing, no full proof | Compatibility decisions with variable costs and alternative competition regimes including Bertrand | Additional obstacle to treating Gate 2 as new. |

## Direct theoretical comparison
Gandal–Shy (§4, benchmark) has the gross quality boost shared equally across brands on switching all-recognize vs no-recognize and, with c=0, firm price/shares/profits unchanged. P1 moves from a 3+1 asymmetrically compatible group to a common four-brand network, thereby **changing relative quality and product-market rents**. The meaningful analytical difference is Δπ_incumbent<0 while ΔCS_domestic>0, not 3 vs 4 countries in itself. Yet §3.2 Gandal–Shy already models discriminatory unions altering competition and rents, and §3.3 sizes.
P1's critical country size threshold is obtained mechanically from ΔW_i=w_i ΔCS_local+(owned world Δπ_i), not from an original voting equilibrium construction. Given any ordered single-crossing payoffs ΔW_i(d), a 3/4 ballot with country 3 certain yes accepts exactly when d is below the **median** of three incumbent cutoffs. This is an order statistic; no new median-voter theorem.

## Generalized P1 formula (for reference)
For N>0, w_i>0, sum(w)=1, d in (0,6/7), conditional on selected voluntary adoption continuations and sincere weak-dominance-refined votes:
- ΔCS_circle=d(216-13d)/36
- Δπ_circle=(-d(d+6)/9,-d(d+12)/36,-d(d+6)/9,d(60-25d)/36)
- ΔW_i=N/4 [w_i ΔCS_circle+Δπ_circle_i] and for entrant country additionally minus resource cost k_L.
- τ_outer(d)=4(d+6)/(216-13d), τ_center(d)=(d+12)/(216-13d), with τ'_outer=1176/(216-13d)^2 and τ'_center=372/(216-13d)^2.
- d*_{0,2}=(216w_i-24)/(13w_i+4); d*_1=(216w_1-12)/(13w_1+1); approval iff d <= median(d*_0,d*_1,d*_2).
- G_3=Nd(60-25d)/144 and k_L<G_3<k_H is a **selection/technology** condition, not implied by ISO vote itself.
- Gross global welfare gain Nd(216-47d)/144, actual conditional net welfare subtract k_L.
- Price Nash equilibrium for specified game proven in the repository for 0<d<6/7 (existence, **not uniqueness**).
A local independently executed SymPy script verified symbolic identities and 1,536 exact rational sufficient-condition inequalities across 16 product-market technology configurations and endpoints 1/5,4/5; min exact slack 1/30. The independent script is saved separately.

## Hypothesis audits H0-A..G
| Null | Status | Why |
|---|---|---|
| A: merely G&S relabeled | **Not demonstrated / reject literal identity** | Their §4 no-vs-all price effect zero, whereas P1 old-vs-full relative quality drives profit changes; no rigorous global game embedding. But core union rents known. |
| B: rational incumbent incompatibility alone | **Supported as close economic-mechanism overlap** | Barrett–Yang and Cheng–Huang; not a proof of exactly equal games. |
| C: Klimenko directly implies P1 comparative static | **Unresolved** | Publisher shows strong externality-dependent compatibility regimes; full proposition-level proof inaccessible. |
| D: Spulber simply implies P1 | **No exact inclusion shown** | Vertical vs horizontal original payoffs distinct; supermajority plus differentiated national welfare is easily adapted. |
| E: generic voting game suffices | **Supported for ballot/median theorem** | Once ΔW_i(d) are fixed, vote pattern is deterministic threshold-counting, independent of Salop. Salop matters only to derive ΔW_i, not ballot aggregation. |
| F: voluntary adoption is mathematically redundant for vote reversal | **Supported for vote/welfare comparative static** | If approval is forced to result in universal compatibility and failure in legacy network, same threshold math; adoption stage needed only to explain feasibility/implementation. |
| G: ISO unique voting institutions necessary | **Not supported for core reversal** | 3/4 matches generic 75% majority; original equal critical sizes also reverse under unanimity. Asymmetry can produce differing 4->3->2 cutoffs, where 3/4 vs unanimity differ in reversal location. ISO technical-negative admissibility and abstentions change official outcomes, but this is not solved in baseline P1. |

## Institution caveats
ISO/IEC Directives Part 1 (2026) §§2.6–2.7: abstentions excluded, >=2/3 P-member positive votes **and** <=1/4 negatives of all valid votes, negative ballots require technical comments. With exactly 4 P-members and all four Yes/No valid, rule is 3-of-4; when abstentions are allowed, 2 Yes and 2 abstentions **pass**, contrary to a fixed 3-vote requirement. Economically motivated opposition is **not equivalent to an admissible technically justified negative vote**. FDIS may be skipped, and a rejection may return for revised drafting; ISO publication does not command corporate adoption. Publication-induced cost drop k_H->k_L is assumed, not a demonstrated consequence of ISO rules. Gate5A complementary-tool entry is a conditional microfoundation, but extra published-standard demand R and contractability remain primitives.

## Editorial destination
- IJIO: **not yet at evidenced journal-level novelty**; new independent endogenous institutional mechanism is needed.
- RIO: investigate if a sharply focused institutional-distortion theorem survives full proof and direct prior art, with real-world relevance and ISO validity.
- Journal of Economics: potentially best technical note only **after** reading Cheng–Huang (2025) full results and explaining how P1 adds more than veto-induced incompatibility; 2023 Buccella et al. is directly relevant.
Any acceptance probability would be a subjective conjecture without data and is not provided.

## Minimal next research agenda
1. **First priority, not model inflation:** obtain Cheng–Huang final full text; Barrett–Yang 2001 final (1999 WP differs potentially); Klimenko 2009 full; check theorem/assumption/parameter mapping. A rigorous exact-subsumption test must compare best responses and parametrizations.
2. Derive a **genuinely endogenous proposal amendment / standard scope** and adoption-investment response with a joint equilibrium sensitive to ISO ballot eligibility/threshold, rather than calculating national payoffs then counting votes. Test whether the same result survives replacing 3/4 with majority, unanimity and removing actual publication-related demand; where impossible, report failure.
3. If mechanism remains, test **user-installed-base** rather than compatible-brand-count externalities, n-country voting and continuation-equilibrium selection; do not label a numerical stress test a general theorem.

All claims explicitly limited by available publication versions and baseline primitive conditions.
