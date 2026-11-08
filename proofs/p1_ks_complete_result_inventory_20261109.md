# P1-KS｜結果の網羅的棚卸し：命題・補題・系・未証明仮説
Date: 2026-11-09 (Asia/Tokyo)
Research branch: research/p1-proof-novelty-gate-20261108
Scope: new *user-count* network externality model, not the earlier exogenous compatible-brand-count P1.
Version status: **research inventory, not a finished theorem manuscript or external referee report**.

## 0. Status labels and strict boundary

- **A**: symbolic identity / exact finite-game classification **for the chosen interior fulfilled-expectations (FE) price continuation**.
- **B**: analytic sign or parameter-range result checked with rational polynomial/Bernstein sign certificates on beta in [1/10,1/2] under B_j/N=1.
- **C**: candidate full-game equilibrium proposition **conditional** on proving every chosen price continuation is a global price-Nash equilibrium and on specified selection/refinement.
- **D**: limited counterfactual or existence construction, verified algebraically, not a general theorem.
- **U**: genuinely open/untested proposition. Do not present as proved.
- **LIT**: method or generic effect substantially covered in preceding literature; not an originality claim.
All algebra below uses N=1 and normalized firm installed bases h=B_j/N unless otherwise indicated. Corporate world operating profit is p_i q_i/4, as countries' market masses sum to one. General N multiplies flow revenues and consumer surplus by N, not real joining costs k.

### Game

Four brands at 0,1,2,3 on a length-4 quadratic Salop circle; four country markets, national shares w_i>0, sum w_i=1; segmented pricing allowed. Existing firms 0–2 initially interoperable on L, firm 3 isolated on M; incumbents may each select unique X_i (free), firm 3 may join L at k_A (k_L on approval; k_H on rejection). Four national bodies simultaneously vote valid Yes/No; at least 3 Yes for acceptance. Price/quantity are decided after standards; expectations of current network sizes must be fulfilled. National welfare = own domestic CS + worldwide profit of its owned firm - local resource cost of implementation.

Let the adoption vector s in {0,1}^4 record L-membership. Let H(s) be the 4x4 same-network indicator, including 1 on the diagonal and singleton groups. Let lambda be the symmetric circle operator with diagonal 1, adjacency -1/2 and opposite zero. Let global expected share per-market density vector be qbar=sum_k w_k q^k.

User network utility for firm j is a_j=beta sum_{l in same network as j}(h_l+Q_l/N). For uniform normalized installed bases h_l=h, this is a=beta H(h*1+qbar/4). **Historic installed bases of different firms are assumed mergeable when technologies become compatible.** In the main checked instance h=1 for every firm and beta in [1/10,1/2]. Default costs N=1, k_L=1/100, k_H=2/5.

Define I=0000 (all singleton), O=1110 (incumbent three compatible), and F=1111 (full compatibility). Price continuation results below are interior FOCs, not yet proven global price Nash for every s.

## I. Demand / technology / pricing lemmas — 11 items

**KS-L01 — Installed-base and current-user aggregation [A; LIT].**
\(a=\beta H(s)(h{\bf1}+\bar q/4)\). When h=1, O's historical installed base is 3N against M's N; F merges all four installed bases. This is K–S/Stadler-style network utility rather than compatible *brand count*. Independent base scaling must be distinguished from platform user counts.

**KS-L02 — Interior rational-expectations demand fixed point [A].**
\(q^k={\bf1}-\Lambda p^k+\Lambda a\),
\(C(s)=I-\beta\Lambda H(s)/4\),
\(\bar q=C^{-1}({\bf1}-\Lambda\bar p+\beta h\Lambda H{\bf1})\), when C invertible.
Important: C uniqueness is only for the locally adjacent **interior demand branch**.

**KS-L03 — Interior demand invertibility for all sixteen adoption states [A].**
Exact spectrum of \(\Lambda H(s)\) across structural classes: singleton network {2,1,1,0}; two adjacent {3/2,3/2,0,0}; two opposite {3,1,0,0}; three compatible {2,0,0,0}; four compatible {0,0,0,0}. Thus max eigenvalue=3 and C is invertible for \(0\le\beta<4/3\), including entire tested [1/10,1/2]. Does not exclude non-interior alternative FE selections.

**KS-L04 — Endogenous network demand-price feedback [A].**
Let \(T=C^{-1}\Lambda\). In interior regime, \(\partial Q_i^k/\partial p_i^\ell\) reflects both immediate local sales and feedback via average worldwide network size. Price FOC in each country is \(q_i^k-p_i^k-(T_{ii}-1)\bar p_i=0\).

**KS-L05 — Endogenous symmetry of destination-specific price candidates [A].**
Subtracting cross-market FOCs and demand equations implies \((I+\Lambda)(p^k-p^\ell)=0\). Since I+Lambda is invertible, all candidate national prices coincide despite *permission* for discrimination. Population shares affect country objectives, not these interior price vectors.

**KS-L06 — Compact matrix formula for all 16 interior price solutions [A].**
\(p=(T+\operatorname{diag}(T_{ii}))^{-1}C^{-1}({\bf1}+\beta h\Lambda H{\bf1})\), \(q=C^{-1}({\bf1}-\Lambda p+\beta h\Lambda H{\bf1})\). Equal-B choice yields five compatibility topology classes totaling 16 states: 5 with L size 0/1, 4 with 2 adjacent, 2 with 2 opposite, 4 with 3, 1 with 4. Exact symbolic candidates verified for all 16 states at both endpoints; positivity and adjacent boundary regularity checked on interval using polynomial certificates.

**KS-L07 — Fully compatible prices and network benefit [A].**
For F and h=1, \(p_i=q_i=1\), \(a_i=5\beta\), and consumer surplus per full unit-density circle (without 4V) \(C_F=(60\beta-13)/3\). For general h, common bonus is \(\beta(4h+1)\) and same prices.

**KS-L08 — All-singletons price and network benefit [A].**
For I and h=1, \(p_i=(4-\beta)(2-\beta)/(8-3\beta)\), \(q_i=1\), \(a_i=5\beta/4\). Unlike old brand-count P1, singleton products retain *own-user* network benefits and prices need not equal 1.

**KS-L09 — Three-plus-one interior prices [A].**
For O and h=1:
\(p_0=p_2=(12-\beta)/[4(3-\beta)]\),
\(p_1=(24-5\beta)/[8(3-\beta)]\),
\(p_3=(12\beta^2-41\beta+24)/[8(3-\beta)]\).
On tested interval, \(p_0=p_2>p_1>1>p_3>0\). F prices equal 1.

**KS-L10 — Three-plus-one fulfilled demands [A].**
\(q_0=q_2=(8-3\beta)(12-\beta)/[16(3-\beta)(2-\beta)]\), \(q_1=p_1\), \(q_3=(12\beta^2-41\beta+24)/[4(3-\beta)(2-\beta)]\). The network-dependent regime does **not** generally satisfy the old Salop identity p=q.

**KS-L11 — World operating profits [A].**
\(\Pi_i=Np_i q_i/4\) for the common price continuation, including when country populations differ; firms sell in all four markets. With h=1, F has \(\Pi_i=N/4\). This distinction is the source of country-size/ownership wedge.

## II. Welfare and pricing comparative statics — 8 items

**KS-L12 — Exact consumer-surplus gain [A,B].**
For O->F (h=1), unit-circle CS gain:
\[
\Delta C(\beta)=\frac{\beta(7\beta-16)(128\beta^3-1023\beta^2+2556\beta-1944)}
{128(\beta-3)^2(\beta-2)^2}.
\]
Both \(\Delta C>0\) and \(\Delta C'>0\) verified symbolically on [1/10,1/2].

**KS-L13 — Outer incumbent operating-profit losses [A,B].**
\[
\Delta\Pi_{0,2}=\frac{N\beta(61\beta^2-432\beta+720)}
{256(\beta-3)^2(\beta-2)}<0,
\quad \Delta\Pi'_{0,2}<0.
\]
The magnitude of the incumbent's lost global rent grows with beta on tested interval.

**KS-L14 — Middle incumbent operating-profit loss [A,B].**
\[
\Delta\Pi_1=\frac{3N\beta(13\beta-48)}
{256(\beta-3)^2}<0.
\]
Further, \(\Delta\Pi_1>\Delta\Pi_0=\Delta\Pi_2\), hence the central incumbent bears a strictly smaller profit loss than the outer incumbents.

**KS-L15 — Isolated entrant's merger gain [A,B].**
\[
G_3(\beta)=\Delta\Pi_3
=\frac{N\beta(144\beta^3-952\beta^2+2001\beta-1296)}
{128(\beta-3)^2(\beta-2)}>0.
\]
Also \(G_3'(\beta)>0\) on the range. Hence \(k_L<G_3(\beta)<k_H\) is the strict voluntary joining/nonjoining window.

**KS-L16 — Country-specific welfare decomposition [A].**
\(\Delta W_i=(Nw_i/4)\Delta C+\Delta\Pi_i-\mathbf1_{i=3}k_L\).
The first term scales with *domestic population*, second with *global corporate profits*. This is the essential political-economy wedge already conceptually related to Gandal–Shy.

**KS-L17 — World potential welfare gain [A,B].**
\[
S(\beta)=N\Delta C/4+\sum_i\Delta\Pi_i-k_L
\]
is strictly positive and strictly increasing in beta over [1/10,1/2] for N=1,k_L=1/100. Stronger sufficient condition: \(N\Delta C/4+\sum_i\Delta\Pi_i-G_3>0\) on this interval. Hence whenever k_L<G_3, full adoption has positive world net gain even without fixing k_L=1/100.

**KS-L18 — Profit erosion vs benefit expansion [B].**
\(\Delta C'>0\), \(\Delta\Pi_{0,2}'<0\), \(G_3'>0\). Network size can simultaneously increase consumer welfare and exacerbate existing standard owners' private opposition. The pure sign pattern is not novel by itself.

**KS-L19 — Incumbent-price ordering [B].**
In the O state, \(p_0=p_2>p_1>p_i^F=1>p_3\). The outside network player cuts prices to offset its disadvantage; incumbent pricing depends on both installed-base asymmetry and endogenously fulfilled network sales.

## III. Endogenous firm adoption — 6 items

**KS-P01 — Incumbent L action weakly dominates private standard [A,B].**
All 24 incumbent comparisons across 16 standards choices were evaluated symbolically. Of the 24 cases with s_i=0, three yield exactly zero improvement (all other firms singleton); the remaining **21 yield strictly positive** worldwide profit gain from adopting L on beta in [1/10,1/2] for h=1. All positive signs passed rational polynomial/Bernstein checks.

**KS-P02 — All-singletons coordination equilibrium [A].**
I=0000 is a pure adoption Nash equilibrium for any positive firm3 L fee, because a unilateral incumbent joining a network of size one obtains no compatibility gain, and firm3 would incur positive entry cost.

**KS-P03 — Strict rejection continuation [A,B].**
When \(k_H>G_3\), O=1110 is a *strict* pure adoption NE: incumbents strictly prefer L and firm3 strictly prefers M. Verified symbolically over [1/10,1/2] for k_H=2/5.

**KS-P04 — Strict approval continuation [A,B].**
When \(0<k_L<G_3\), F=1111 is a *strict* pure adoption NE: incumbents strictly prefer L, firm3 strictly prefers joining. Verified symbolically over [1/10,1/2] for k_L=1/100.

**KS-P05 — Exhaustive adoption Nash correspondence [A,B].**
With h=1 and beta in tested interval, weak dominance implies, under a chosen interior price continuation:
- if \(k_A>G_3\), pure NE exactly {I,O};
- if \(0<k_A<G_3\), pure NE exactly {I,F};
- if \(k_A=G_3>0\), I plus incumbents all L with firm3 allowed to mix;
- no additional mixed NE under strict inequalities.
This is stronger than mere enumeration at two endpoint beta values.

**KS-P06 — Adoption-stage trembling-hand refinement [A,C].**
Private-standard choice by each incumbent is weakly dominated with strict advantage somewhere, so I fails trembling-hand perfection. The unique perfect equilibrium of the *finite adoption game under selected price payoffs* is O if k_A>G3 and F if k_A<G3. This does **not** establish full extensive continuous-price trembling-hand perfection or price equilibrium uniqueness.

## IV. International voting — 9 items

**KS-P07 — Outer-incumbent population threshold [A,B].**
For i=0,2, define
\[
\tau_o(\beta)=-4\Delta\Pi_0/(N\Delta C)
=-\frac{2(\beta-2)(61\beta^2-432\beta+720)}
{(7\beta-16)(128\beta^3-1023\beta^2+2556\beta-1944)}.
\]
Country i sincerely supports iff \(w_i\ge\tau_o(\beta)\) (indifference requires a voting tie rule).

**KS-P08 — Center-incumbent population threshold [A,B].**
\(\tau_c(\beta)=-4\Delta\Pi_1/(N\Delta C)\), in explicit terms
\[
\tau_c(\beta)=
-\frac{6(\beta-2)^2(13\beta-48)}
{(7\beta-16)(128\beta^3-1023\beta^2+2556\beta-1944)}.
\]
Country1 votes yes iff \(w_1\ge\tau_c\). On tested interval, \(0<\tau_c<\tau_o\).

**KS-P09 — Rising vote-support thresholds [B].**
Exact Bernstein sign certificates verify \(\tau_o'(\beta)>0\) and \(\tau_c'(\beta)>0\) on [1/10,1/2]. Thus increasing network intensity weakly lowers the number of strictly supporting incumbent countries *for fixed populations* in the maintained price/adoption regime.

**KS-P10 — Unique incumbent reversal threshold [A,B].**
For w0=w2=3/25, each country's welfare difference is
\[
\Delta W_{0,2}=
\frac{\beta(2688\beta^4-24577\beta^3+75080\beta^2-84312\beta+21312)}
{12800(\beta-3)^2(\beta-2)^2}
\]
when N=1. Exactly one root within beta in [1/10,1/2], \(\beta^*\approx0.349670283323148\); signs positive below and negative above, holding interior continuation fixed.

**KS-P11 — ISO-type ballot reversal [B,C].**
For w=(.12,.50,.12,.26), k_L=.01,k_H=.4, sincere ballots: YYYY at beta=.1; NYNY at beta=.5; thus 4 Yes->2 Yes and approval->rejection, despite potential positive world gains. The result is a conditional SPNE path only after justifying the chosen price continuations and refining the adoption/voting games.

**KS-P12 — Unequal-country sequential defections and median voter [A,B,C].**
For unequal w0=.115,w2=.125,w1=.50,w3=.26, threshold crossings are approx beta0*=.298406804 and beta2*=.396781347. Consequently sincere vote counts 4->3->2 as beta increases. With country3 Yes, approval under 3/4 rule requires two incumbent Yes votes, so the *median of the three incumbent critical beta values* is pivotal. More generally 2-of-4 requires at least one incumbent yes (max threshold); 4-of-4 requires all three (min threshold). This is voting arithmetic, **not an originality claim**.

**KS-P13 — Entrant country's strict pro-approval condition [A,B].**
For i=3, \(\Delta W_3=Nw_3\Delta C/4+G_3-k_L\). Since \(\Delta C>0\) and \(k_L<G_3\), country3 always strictly supports full compatibility in the checked region, regardless of its positive w3.

**KS-P14 — Full pure ballot Nash characterization [A].**
Given fixed approval vs rejection continuation payoffs \(\delta_i\), a valid Yes/No profile is Nash iff:
- 0 or 1 Yes: always (any unilateral ballot is nonpivotal);
- 2 Yes: both No voters weakly prefer rejection;
- 3 Yes: all three Yes voters weakly prefer approval;
- 4 Yes: always (nonpivotal).
Thus unrefined ballot Nash outcomes are not unique; sincerity is weakly dominant and can be selected by trembling-hand perfection where preferences are strict.

**KS-P15 — Multiplicity of reduced-game SPNE [A,C].**
With {I,O} as rejection adoption NE and {I,F} as approval NE, four adoption-continuation pairs are available. With country weights as baseline and fixed selected price continuations, direct 16-ballot enumeration gives **45 pure SPNE plans at beta=.1 and 45 at beta=.5**. For O->F pair, ballot-Nash counts are respectively 10 and 7. The sincere outcome follows reversal, but alternative unrefined equilibrium paths exist. These are **reduced selected-price game** counts, not unconditional full-game counts.

## V. Installed-base and null-model counterfactuals — 7 items

**KS-C01 — No inherited users eliminates incumbent profit-loss channel [D,B].**
When each installed base h=0 while current sales still contribute to user network size, exact O->F calculations give \(\Delta\Pi_i>0\) for all four i on beta in [1/10,1/2], and \(\Delta C>0\). Thus all incumbent countries with w_i>0 strictly favor approval conditional on F vs O. This is a *within-model counterfactual*, not a general impossibility theorem for all network games.

**KS-C02 — A strictly positive inherited-user threshold for outer-incumbent rent loss [A,D].**
With arbitrary identical h=B_j/N, the O-world price and demand for i=0,2 are
\(p_o=(12-5\beta+4\beta h)/[4(3-\beta)]\),
\(q_o=(8-3\beta)(12-5\beta+4\beta h)/[16(3-\beta)(2-\beta)]\).
Full compatibility has p=q=1. Outer profit loss (\(\Pi_o^O>N/4\)) occurs iff
\[
h>h_o^{\rm profit}(\beta)=
\frac{8(3-\beta)\sqrt{(2-\beta)/(8-3\beta)}-12+5\beta}{4\beta}
\]
*within the interior regularity range*. h*~.0610729 at beta=.1, ~.0538446 at beta=.5. This threshold is NOT the government's approval/objection threshold (domestic consumer welfare must also be counted).

**KS-C03 — Center-incumbent's different inherited-user threshold [A,D].**
For O and common h, \(p_1=q_1=(24-9\beta+4\beta h)/[8(3-\beta)]\). At positive beta, the center incumbent loses profits under full compatibility iff \(h>1/4\). Hence topology produces distinct individual rent-loss thresholds, without choosing w.

**KS-C04 — Genuine open set of asymmetric country sizes [A,B,C].**
For beta_low=.1,beta_high=.5, take w0,w2 strictly between tau_o(.1) and tau_o(.5), w1>tau_c(.5), and w3=1-w0-w1-w2>0. All strict inequalities define a nonempty relative open population-simplex set where approval can switch to rejection under sincere voting. It is not dependent on w0=w2.

**KS-C05 — Equal-size countries do not reverse in the checked h=1 interval [B,D].**
With all w_i=1/4, incumbent national welfare effects are positive throughout beta in [1/10,1/2], based on rational sign checks. Hence the particular mechanism relies on mismatch between equal national votes and asymmetric domestic markets.

**KS-C06 — Null publication-effect lemma [A; LIT].**
If formal approval leaves technology options, information, adoption/payoff parameters and equilibrium-selection device unchanged, continuation equilibrium *sets* are the same in accepted/rejected states. With a unique or consistently selected continuation, publication has no implementation effect. Multiple equilibria might still allow a public signal/sunspot to coordinate selection, so not an absolute impossibility claim.

**KS-C07 — Scale and fixed-cost comparative statics [A,D].**
At fixed normalized installed bases h and beta, the incumbent population support thresholds are invariant to total N; entrant adoption gain scales as N while fixed k_L,k_H do not. The inequality k_L<G3<k_H can therefore change as N changes even though voting preferences conditional on full-vs-old do not change for incumbent countries.

## VI. Numerically grounded illustrative endpoints (not separate independent mechanisms)

At N=1, h=1, k_L=1/100, k_H=2/5, w=(.12,.50,.12,.26):
- beta=.1: ΔW=(+.003501535475,+.077082682508,+.003501535475,+.087506282892), net world gain +.171592036351, sincere YYYY, passes.
- beta=.5: ΔW=(-.013828125,+.354214409722,-.013828125,+.409214409722), net world gain +.735772569444, sincere NYNY, fails.
- On the *whole interval*, exact polynomial sign checks show ΔC>0, ΔC'>0, ΔΠ0<0, ΔΠ1<0, ΔΠ3>0, ΔΠ3'>0, τ_o'>0, τ_c'>0, net world gain>0 and increasing.
- At both endpoints, all 16 adoption profiles have verified positive interior candidate prices and adjacent demand boundaries; 2,928 exploratory nonlocal **uniform worldwide-price** deviations uncovered no profitable switch. **This does not prove worldwide differentiated-price global Nash optimality**.

## VII. Unresolved result candidates (explicitly NOT established)

**KS-U01:** General proof that the selected price vector is a global price-Nash equilibrium in every one of 16 subgames with network expectations re-solved after any country-specific nonlocal price deviation. A short sufficient-condition proof is sufficient; all-equilibrium uniqueness is NOT needed for a selected-SPNE existence theorem.

**KS-U02:** Exhaustive uniqueness of noninterior FE demand fixed points and price equilibria. This is not a necessary baseline paper theorem unless asserting all-SPNE uniqueness.

**KS-U03:** A tractable *general h / arbitrary installed-base distribution* characterization of country preference, not just common h=1 and h=0.

**KS-U04:** Robustness of reversal to actual utilization rather than brand-user counts, rival network multi-homing, consumer heterogeneity, unequal purchase volumes, country-specific network effects and non-normalized installed bases.

**KS-U05:** Fully endogenous linkage between ISO publication and implementation expense kL<kH rather than a reduced-form institutional primitive.

**KS-U06:** Full normative analysis of endogenous voting thresholds, optimal voting quotas, inter-country transfers and mechanism design. Quota order statistics alone are trivial; welfare/implementation tradeoffs may be substantive but unproven.

**KS-U07:** Microfoundation for availability of technical No votes, abstention, legitimate objections, and revision after rejection. The Gate4 volunteer-dilemma game pertains to the *old brand-count model* and is not automatically proved for the KS extension.

**KS-U08:** Integration of third-party interoperability toolkit supply from Gate5A into the user-count model, including installed-base migration and financing. Gate5A was developed for a different pricing continuation.

**KS-U09:** Theorem-level novelty audit versus Gandal & Shy (2001), Katz & Shapiro (1985), Barrett & Yang (2001), Klimenko (2009), Spulber (2019), Stadler et al. (2022), Buccella et al. (2023), Cheng & Huang (2025). No inference of first-in-literature novelty from an algebraically new quartic.

**KS-U10:** General perturbations of country-specific prices, asymmetric installed bases, cost heterogeneity of incumbents, and a mathematically closed *all-16-price-subgame* existence region.

## VIII. Legacy and optional extensions: deliberately excluded from the current theorem count

The original exogenous compatible-brand-count P1 has exact price p0=(1+d/3), p1=(1+d/6), p2=(1+d/3), p3=(1-5d/6) in O and country reversal at d=48/139 for w0=w2=3/25. The original median-population-threshold theorem, Gate4 ISO-technical-comment/abstention volunteer dilemma, Gate5A ancillary toolkit-supply model, and the P2 variable-compatibility proposal game each have their own distinct primitives. Do NOT merge their formulas as theorems in the user-count KS model without rederivation.

## IX. Evidence map / reproduction

- Existing exact primary program: verify_ks_userbase_vote_reversal.py (executed in the ChatGPT container on 2026-11-09; originally created 2026-11-08).
- New independent exact checks during this inventory: 21 strict incumbent L-improvement signs; 3 zero signs; 16 fixed point spectra; β0=.1, β1=.5 reduced-game SPNE counts; beta=0-installed-base CS and all-four profit gains; threshold hcrit; derivative of center support threshold; gross world benefit above G3.
- Existing repository note: proofs/p1_ks_userbase_network_reversal_20261108.md.
- Original brand-count P1: proofs/p1_complete_backward_induction_gameform_20261108.md.
- Literature verification: Stadler, Tobler Trexler & Unsorg (2022), Network and Spatial Economics 22, 903–913, https://doi.org/10.1007/s11067-022-09572-x; Katz & Shapiro (1985), AER 75, 424–440; Gandal & Shy (2001), Journal of International Economics 53, 363–383.
- These results are a *structured backlog* not an exhaustive mathematical enumeration of every possible theorem. The 2026-11-08 selected-interior-price-status caveat persists.

## X. Research sequencing — without selecting a main result

(1) Freeze demand expectations, prices and the small-β parameter region; prepare minimum sufficient global-price best-response verification.
(2) Present KS-L12–L18, P07–P13 and C01–C05 side by side in result-logic diagram with assumptions and exact signs.
(3) Judge which insights are first-in-literature at theorem level; only afterward choose a main proposition. The same facts can be support lemmas or corollaries depending on narrative priorities.
