# Independent counterfactual and strategic-reduction audit for P1
Date: 2026-11-08. Frozen analysis input: branch `research/p1-proof-novelty-gate-20261108` as of `b50f6596c36689f97a6b7a9f8fb40f7cfae67d6f`.

## A. Model and derived primitives
Four vertically segmented national markets indexed i=0,1,2,3, with total population N and positive shares w_i. Four horizontally located products at successive points on a Salop circle of circumference four, quadratic distance disutility and covered demand. Initial a^0=(2d,2d,2d,0); all-compatible a^1=(3d,3d,3d,3d). A national decision maker values domestic consumer surplus plus its resident producer's *worldwide* operating profit. This reproduces the profit ownership criterion in Gandal & Shy (2001), not a new government-objective invention.

P1 price candidates verified from the 4-firm linear first-order price system and against the supplied proof's deviation-bound sufficient conditions:
p^0=q^0=(1+d/3, 1+d/6, 1+d/3, 1-5d/6), p^1=q^1=(1,1,1,1).
For the specified market, these form Nash prices on the proven domain 0<d<6/7; uniqueness of all equilibria unproven. The independent SymPy reproduction checked all 1,536 rational end-point inequalities for 16 technology profiles on [1/5,4/5] with strictly positive minimum slack 1/30; passing a finite sufficient-condition family supports the **written conditional proof**, not automatic uniqueness.

On moving from a^0 to a^1:
C(d)=ΔCS_circle=d(216-13d)/36,
Δπ_circle=(-d(d+6)/9,-d(d+12)/36,-d(d+6)/9,d(60-25d)/36).
Consequently, for incumbent i, ΔW_i=N/4 [w_i C(d)+Δπ_circle_i]. Country 3 additionally subtracts implementation real resource cost k_L.
Total gross welfare gain (provided all four implement) is Nd(216-47d)/144.

## B. Aggregation equivalence (a genuine reduction)
Given the three independently specified incumbent critical network values
d*_0=(216w_0-24)/(13w_0+4);
d*_1=(216w_1-12)/(13w_1+1);
d*_2=(216w_2-24)/(13w_2+4),
and assuming strict support of country 3 and a sincere ballot for all, let a<=b<=c be the sorted three critical values. In the region where these are valid comparisons:
- a generic 2-of-4 approval rule accepts iff d<=c (at least one incumbent yes);
- a generic 3-of-4 approval rule accepts iff d<=b (at least two incumbent yes);
- a generic unanimous 4-of-4 rule accepts iff d<=a.
Proof: at a network intensity d each incumbent says yes iff d<=its own critical value, country 3 always says yes, and at least (k-1) of the three incumbent yes votes are needed under a k-of-4 quota. This is an **elementary voting order statistic, not an original economic theorem**. ISO's supermajority has no distinct implication when all four cast valid votes; the proper dual-denominator ISO rule matters if abstentions or technically invalid negatives exist.

## C. Asymmetric and original symmetric counterfactuals (exact)
Case w=(3/25,21/50,13/100,33/100), N=1,k_L=1/20,k_H=3/10:
 d*_0=48/139, d*_1=3936/323, d*_2=408/569; sorting gives a=48/139, b=408/569, c=3936/323 (c lies outside the proven d<6/7 range).
 d=1/5: Y,Y,Y,Y; 2/4,3/4,4/4 all accept; ΔW_world_net=853/3600.
 d=2/5: N,Y,Y,Y; 2/4,3/4 accept, 4/4 reject; ΔW_world_net=112/225.
 d=4/5: N,Y,N,Y; 2/4 accepts, 3/4 and 4/4 reject; ΔW_world_net=847/900.
This demonstrates the **voting quota changes timing**. It does not establish uniquely ISO-specific economics.
Original w=(3/25,1/2,3/25,13/50) has d*_0=d*_2=48/139. Hence going 4 yes to 2 yes at a single threshold reverses under **both 3/4 and unanimity**, and does not reverse under 2/4. Thus the original case does not identify any distinctive positive explanatory contribution of the 75%-vs-unanimous criterion.

## D. Remove or change one primitive at a time
1. Remove the vote, retain the private adoption game: no institutional outcome can be inferred without specifying which cost/technology/adoption opportunity is available; the old-vs-new comparison remains a product-market comparative static.
2. Force adoption on acceptance, no adoption on rejection, rather than allowing voluntary private choice: **the national ΔW and voting cutoff formulas do not change**. Hence adoption endogeneity is not needed to obtain the *reversal equation*, only to justify its realizability in sequential equilibrium.
3. Change only voting quota: results in B, same ΔW and same continuation.
4. Set each incumbent's owned-profit welfare weight β_i=0 and α_i>0 on CS_i: because C(d)>0 for 0<d<6/7, each incumbent strictly supports full compatibility; reversal disappears. Ownership/weighting of worldwide firm profits is essential **within this reduced-form model**, but already appears in Gandal–Shy.
5. Equalize population w_i=1/4 and maintain α=β=1: incumbents all strictly support full compatibility on proven domain, because the outer countries' welfare change is Nd(120-29d)/576>0 and country1 also positive. Reversal requires either smaller pivotal consumer markets or different producer weights. An alternate population-symmetric β/α=2 case is already in the institutional audit; that is a different *preference primitive*, not a contradiction.
6. Change network benefit from d times **compatible brand count** to the number of installed users: the current algebra is no longer valid, since demand and anticipated network size enter an additional fixed point. NOT SOLVED. No general-network claim.
7. Remove all approval-conditional feasible actions, costs, information changes and systematic equilibrium selection: the postballot game in both outcomes is identical; the equilibrium correspondence is equal. The ballot cannot uniquely cause adoption change. **Sunspot selection in a multiple-equilibrium game is a separate possibility**, not ruled out without a selection condition.
8. Add actual ISO abstention and technical-negative admissibility: if only countries 1,3 cast valid yes votes, while 0 and2 abstain, actual 2026 DIS/FDIS dual conditions give Yes=2, No=0 -> PASSES. If one eligible negative is valid and the other abstains, Yes=2, No=1 -> FAILS because 1/3 negatives exceeds 1/4. With all four valid votes, Yes=3,No=1 passes; Yes=2,No=2 fails. Financial loss alone is not a technical comment, so this is an institutional constraint not derived from ΔW.
9. Gate 4 voluntary technical-objection submission: add each player's player-specific loss constant to transform u_i=-L_i 1{no filing by either}-c_i 1{i files} into the two-person **Volunteer's Dilemma** payoff u'_i=L_i 1{someone files}-c_i 1{i files}. This is exact strategic identity, not just similar verbal framing. Its mixed approval probability c_0 c_2/(L_0 L_2) is **selection dependent**; both pure equilibria reject with probability one.

## E. Institutional microfoundation and welfare caveat
A conditional cost interval k_L<G_3(d)<k_H selects both an approved state with a voluntarily joining outsider and a rejected state with a nonjoining outsider (the shown technology profiles can be strict Nash adoption continuations); existence is distinct from uniqueness across the whole game. Gate5A replaces k_L,k_H by a supplier fixed cost F, third-party customer revenues R and stand-alone cost K with G<F<G+R and K>G. This offers a feasible two-sided contract after publication but relies on additional published-standard-specific demand R. It does not make compatibility unconditionally efficient, nor resolve all adoption-stage equilibrium selection. Welfare is measured conditional on implementation, net of **real** implementation/tool development resource costs; licence fees internal to a country are transfers.

## F. Mathematical and editorial interpretation
The derivation `ΔW_i -> individual single-crossing -> median critical value` is a mathematically explicit, instructive example of an internationally inefficient supermajority vote. It is **not a new voting equilibrium concept** and could be reproduced from any reduced form with single-crossing payoffs. The specific ΔW_i is derived from horizontal oligopoly, but analogous rent-preserving incompatibility mechanisms are already in Gandal–Shy, Barrett–Yang, Klimenko and more recent compatibility-veto work. Proving a genuinely new institution-dependent equilibrium requires an endogenous interaction affecting incentives on both sides of the ballot, not a renamed order statistic.

## Reproducible check
`python code/test_independent_novelty_counterfactuals_20261108.py`
This script verifies price and welfare formulas and selected exact population voting/quota counterfactuals. Full 1,536 sufficient-condition screen in `code/test_p1_population_generalization.py`, independently recomputed in this audit; both are symbolic/auditable checks, not formal automated proof assistants.

## Original primary sources
- User-provided published PDF: Gandal & Shy (2001) §2–4; compare §3.3 country size and §4 recognition and standardization unions.
- ISO/IEC Directives Part 1 (2026): https://assets.iec.ch/sd/ISO-IEC_Directives_Part-1_2026.html, §§2.6–2.7.
- Published full Spulber (2019): https://onlinelibrary.wiley.com/doi/10.1111/ecoj.12606.
- Barrett & Yang 1999 revised WP, not assured final version: https://ageconsearch.umn.edu/record/14597/files/wp9909.pdf.
- Klimenko (2009): https://doi.org/10.1016/j.jinteco.2008.08.005; published full proof unavailable in audit.
- Buccella et al. (2023): https://doi.org/10.1007/s00712-023-00834-x.
- Cheng & Huang (2025): https://doi.org/10.1007/s00712-024-00896-5; published abstract only.
