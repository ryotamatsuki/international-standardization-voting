# P1 全継続ゲームの後ろ向き帰納法による解 — Game-Form Freeze

**Date:** 2026-11-08  
**Evaluated branch:** `research/p1-proof-novelty-gate-20261108`  
**Scope:** 4-country, 4-firm ISO-*style* four valid yes/no votes, Gate 2 implementation-cost benchmark. Gate 4 (technical negative ballots), Gate 5A (tool supply), and P2 endogenous proposals are **different games**, not automatically part of the core game.

## I. Game form fixed before solving

There are four national bodies and four nationally owned firms i=0,1,2,3. Markets k=0,1,2,3 have sizes n_k=Nw_k>0, sum w_k=1. They are segmented; firms can independently price in each market; marginal cost=0. All consumers buy one unit, transport disutility is squared circular distance on a length-four Salop circle, and utility in location z for firm i is V+a_i(s)-p_i^k-dist(z,i)^2 with V sufficiently large at relevant prices. Network quality is a **compatible-brand-count bonus**: a_i(s)=d(number of other L-users if i uses L), otherwise 0; each private X_i and M is distinct.

**Stage 1:** all four national standardization bodies cast valid Yes/No simultaneously on a fixed draft. Publication A=1 iff at least 3/4 votes Yes. This is the restricted game with four valid ballots, NOT actual DIS/FDIS with abstentions and technical eligibility. All players know the primitives.

**Stage 2:** after observing A, four firms choose standards simultaneously. Incumbents i=0,1,2 choose L or their unique X_i, and firm 3 chooses L or M. Their 4-bit action profile is s, 1=L. Incumbents have zero additional investment cost (existing rights/access are assumed); firm 3 pays real resource joining cost k_A>0 if s_3=1, with k_1=k_L and k_0=k_H.

**Stage 3:** following every one of 16 possible s, firms simultaneously choose nonnegative prices in each national market. Consumers pick maximum utility. Firms receive worldwide operating profit minus individual adoption costs. National body i receives its domestic CS plus firm-i worldwide profit, minus its own nationally borne implementation cost if incurred. The game is solved by subgame perfect backward induction, first fixing an explicit pricing continuation.

The benchmark regular region is d in [1/3,3/8], N=1, k_L=1/20, k_H=1/5 for numerical examples. The symbolic welfare and voting statements allow arbitrary w_i>0, sum1 and N>0.

## II. Stage-3 product-market Bertrand equilibrium — all 16 adoption profiles

Let a=(a0,a1,a2,a3) be quality. Under regular adjacent-market boundaries, FOCs in any segmented country are
2 p_i-(p_{i-1}+p_{i+1})/2 = 1+a_i-(a_{i-1}+a_{i+1})/2 .
The unique solution **within the interior adjacent-boundary class** is
p_i(s)=1+(5/12)a_i-(1/6)(a_{i-1}+a_{i+1})-(1/12)a_{i+2}.
Candidate unit-density per-country q_i=p_i and firm i worldwide operating profit Pi_i(s)=N p_i(s)^2/4. Rotating players changes which price belongs to which firm.

All 16 configurations fall into five structural classes (number of states):
- 0 or 1 L member (5): a=(0,0,0,0), all p=1.
- Exactly two adjacent L members (4): p of two L members=1+d/4, others=1-d/4.
- Exactly two opposite L members (2): p of two L members=1+d/3, others=1-d/3.
- Exactly three L members (4): rotate (1+d/3,1+d/6,1+d/3,1-5d/6), with the last component for the excluded/isolated brand when it occupies slot 3.
- All four L members (1): all p=1.

Exact-rational SymPy verification reran **1536 inequalities** from a sufficient-condition family for the written global-price-deviation lemma over all 16 s, at d=1/5,4/5; minimum slack 1/30. The sufficient functions are affine or concave endpoint-testable, thus positive throughout [1/5,4/5] and in particular on [1/3,3/8]. **This proves existence of a specific pure pricing Nash equilibrium (along with the written global best-response bound), not uniqueness among arbitrary noninterior/nonadjacent price equilibria.** The latter is an unsolved mathematical question, so the full-game exhaustive result below is **conditional on choosing these verified price continuation equilibria in every stage-3 subgame**.

## III. Stage-2 adoption subgames solved — all Nash equilibria, including mixed strategies

The key identity can be derived directly from the price formula: for any player i currently isolated, write m_adj=number of its two adjacent players already at L, and m_opp=1 if the opposite player already at L, 0 otherwise. If i joins L alone, holding other technology choices fixed, its **equilibrium price** changes by exactly
Δp_i = (d/12)(3 m_adj+4 m_opp) >= 0.
If at least one other player already uses L, this price gain is strictly positive. Since p_i>0 in the verified domain and operating profit is N p_i^2/4, any incumbent (no entry fee) **weakly prefers L to its private standard for every rivals' strategy combination** and **strictly prefers L whenever at least one other firm uses L**. In the 0000 state an isolated incumbent is indifferent to joining L alone.

Firm 3 has a real joining fee k_A and, when all incumbents use L, gains
G_3(d)=N d(60-25d)/144
in worldwide operating profit upon joining.

**Complete adoption Nash correspondence, for k_A>0 and 0<d in verified domain, using the selected price continuation:** 
- k_A>G_3: exactly two Nash profiles, I=0000 and O=1110.
- 0<k_A<G_3: exactly two Nash profiles, I=0000 and F=1111.
- k_A=G_3>0: I=0000 and the entire continuum s0=s1=s2=1, with firm3 indifferent and allowed any mixed probability of L.

**Proof of completeness incl. mixed:** If any player uses L with positive probability, then every incumbent must put probability one on L: with some rival-L chance the payoff advantage of L is strictly positive. In particular an incumbent with positive isolated probability cannot coexist with any other firm using L with positive probability; a hypothetical sole incumbent with mixed use of L forces other incumbents to join, contradicting the hypothesis. Hence any NE is either I=0000 (where entrant prefers M because k_A>0), or all incumbents use L for sure and firm3 chooses according to k_A vs G_3. No further mixed NE are possible except at the entrant indifference boundary.

**Refinement:** Each incumbent's X_i is weakly dominated by L, with strict inequality against some other-firm profiles. Therefore the all-isolated Nash equilibrium I is **not trembling-hand perfect** in the finite adoption game, as infinitesimal full-support trembles make L strictly better. Since the incumbent L choices are enforced, the sole trembling-hand perfect adoption equilibrium is O after rejection when k_H>G_3, and F after approval when k_L<G_3. This result does **not** establish perfection or uniqueness for the entire continuous-price extensive game without resolving possible alternate price Nash equilibria.

For the benchmark N=1, k_L=1/20, k_H=1/5, d∈[1/3,3/8], k_L<G_3(d)<k_H. Thus rejection's pure adoption NE = {I,O}, approval's = {I,F}; each has only **one** adoption-stage trembling-hand perfect equilibrium.

## IV. Stage-1 voting solved for all four continuation-selection pairs

Define three feasible adoption outcomes I=0000, O=1110, F=1111. At the stage-3 price equilibrium, representative-country **consumer surplus (excluding common 4V)** per unit-density circle is:
C_I=-13/3,
C_O=-13/3+6d+13d²/36,
C_F=-13/3+12d.
In I and F every firm has worldwide gross profit N/4; in O the four firm price levels are as above, hence firm i has worldwide profit N[p_i(O)]²/4. Publication and choosing F requires the real joining cost k_L in firm3's national payoff.

There are exactly FOUR pairs of Nash continuation choices for the two separate voting outcomes:
1. reject O, approve F;
2. reject I, approve F;
3. reject O, approve I;
4. reject I, approve I.

A national representative's approval gain is δ_i = W_i(s^A)-W_i(s^R), and all-stage-1 voting equilibria can be characterized for each δ vector:

Case 1, O→F (P1 intended branch):
δ_0=Nd[w0(216-13d)-4(d+6)]/144,
δ_1=Nd[w1(216-13d)-(d+12)]/144,
δ_2=Nd[w2(216-13d)-4(d+6)]/144,
δ_3=Nd[w3(216-13d)+60-25d]/144-k_L.

Case 2, I→F:
δ_i=3Nw_i d for i=0,1,2; δ_3=3Nw3d-k_L.

Case 3, O→I:
for i=0,2, δ_i= -Nd[w_i(216+13d)+4(d+6)]/144;
for i=1, δ_1=-Nd[w1(216+13d)+(d+12)]/144;
for i=3, δ_3=-Nd[w3(216+13d)+25d-60]/144.
No adoption cost incurred in I.

Case 4, I→I: δ_i=0 for every i.

**Complete pure-ballot Nash rule**, given any fixed δ and threshold 3 yes out of 4:
- With <=1 Yes: always a Nash equilibrium (no single voter can change the rejection result).
- With exactly 2 Yes: Nash iff each of the 2 No voters has δ_i<=0.
- With exactly 3 Yes: Nash iff each of the 3 Yes voters has δ_i>=0.
- With 4 Yes: always a Nash equilibrium (no single voter can overturn passage).
The proof is checking unilateral pivotality: only exactly 2 or 3 affirmative votes make individual actions pivotal. Thus **both approval and rejection are always supported by some pure voting Nash equilibrium**, independent of δ; this is the standard nonpivotal voting indeterminacy.

**Voting refinement:** With strict approval preferences δ_i≠0, the sincere vote Yes iff δ_i>0 is weakly dominant; because in a fully mixed opponent tremble every voter has positive pivotal probability, its sincere vote is the unique trembling-hand perfect choice in the finite voting game. In the P1 O→F continuation case, country3 strictly supports, and approval iff d<=median{d*_0,d*_1,d*_2}, where:
d*_0=(216w0-24)/(13w0+4), d*_1=(216w1-12)/(13w1+1), d*_2=(216w2-24)/(13w2+4).
At a crossing, indifferent national votes are not pinned down by this strict-preference refinement.

### Exact numerical example and exhaustive SPNE counts in the selected-price reduced game
Choose w=(3/25,1/2,3/25,13/50), N=1, k_L=1/20,k_H=1/5.
At d=1/3, the four continuation pairs O→F, I→F, O→I, I→I generate respectively **10,10,12,16** pure voting Nash equilibria, totaling **48** pure SPNE plans, conditional on the selected stage-3 price equilibria. Of the first-case 10, 5 approve and 5 reject. The sincere-refined case O→F yields all 4 Yes and approval.
At d=3/8, the four continuation pairs give respectively **7,10,12,16**, totaling **45** pure SPNE plans. In the first case there is 1 approval equilibrium (all 4 Yes) and 6 rejection equilibria. The sincere-refined case O→F yields votes (No,Yes,No,Yes) and rejection.

Therefore **unrefined SPNE does not uniquely predict the voting reversal**. Only the explicitly stated stage-2 adoption refinement + the stage-1 sincere/weak-dominance refinement selects the intended sequence in the selected-price continuation model.

The unconditional statement 'the game has a unique SPNE in which d↑ causes rejection' is FALSE in the current game.

## V. Welfare and final economic content

For O→F, total world welfare gain when full interoperability is implemented is
ΔW_world= Nd(216-47d)/144-k_L>0
on the maintained window. With independent adoption selection, the realized gain can differ if the all-isolated continuation is played in some ballot-result subgame. Under the finite-stage trembling-hand refinement just established, rejection selects O and approval selects F, making this welfare comparison the relevant one.

Original country's vote threshold for 0 and 2 at w_i=3/25:
d*=48/139. For d<d* (inside [1/3,3/8]), sincere refined votes YYYY; for d>d*, NYNY; at d=d* countries 0 and2 are indifferent and approved/rejected outcome depends on the ballot tie choice. Under the original zero-cost valid-vote simplification, this is a complete characterization of the **refined reduced game**, not the full ISO procedural game.

## VI. Remaining proof gap that prevents a claim of 'all equilibria of the full original extensive game'

The existence and globally optimal unilateral price responses for the displayed stage-3 price vector have a rigorous candidate proof and exact checks. **There is no independent proof excluding additional asymmetric, noninterior, or nonadjacent Bertrand equilibria** for all 16 technology profiles, and the normal-form adoption payoff correspondence might differ if such other equilibria exist. An unconditional statement about every SPNE of the full game must first establish pricing equilibrium uniqueness or handle all pricing correspondences; this audit does not infer it from endpoint checks.

The present theorem is a **complete solution of the finite voting/adoption game with the audited pricing equilibrium selection in each product-market subgame**. Any attempt to claim more must supply a new theorem addressing that remaining continuous price-game correspondence. ISO actual technically justified No ballots, abstention denominators and later negotiation also constitute separate models and are excluded from this exact baseline.

## VII. Reproduction
The independent executable SymPy checker evaluates all 16 states, the strict/weak incumbent dominance price difference, all three relevant consumer surplus formulas, the four continuation-pair national payoff differences, all 16 vote profiles and their pure Nash characterization, plus 1,536 exact sufficient-condition inequalities. See companion code `code/solve_p1_full_backward_20261108.py`, and original proof `proofs/gate1_closed_form_global_bertrand.md`.

**Result:** pricing Nash *existence* yes, adoption all pure and mixed Nash *conditional on pricing selection* characterized completely, all pure ballot Nash characterized, pure SPNE plans for example counted completely, finite-stage trembling-hand refinement produces the desired equilibrium path. The global all-price-equilibrium uniqueness question remains open.
