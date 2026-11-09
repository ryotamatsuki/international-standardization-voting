# No N3/N4 main theorem certified — exact diagnostic proposition on breadth and implementation
Date 2026-11-09. **The file name satisfies requested research artifact layout; it does NOT certify an original journal proposition.** Only reduced-form voluntary adoption is solved. An ISO committee and Cournot/Salop price-stage have NOT been added. Formally novel algebra does not imply economic novelty.

## Specification and precise realized outcome
A continuum (mass 1) of potential optional-interface implementers has heterogeneous compliance engineering cost coefficients c distributed Uniform[0,1]. A standard-setter may propose a breadth/strictness s in (0,1]. Each atomistic firm takes fraction a of other implementers as given and chooses adoption z_i∈{0,1}; incremental private operating payoff from adoption is
\[
\Delta\Pi_i(s,a,c_i)=s(b+\theta a)-c_i s^2
\]
with positive b, nonnegative theta, and 0<b+theta<1. Nonadoption gives zero incremental profit. The first term is a *maintained reduced-form* quality/market-access return, not a derived Bertrand price equilibrium; the cost curvature is another maintained engineering primitive. This game is deliberately diagnostic, NOT an integration of JPET's X and the ISO vote model's H.

Define **effective cross-firm pairwise optional-profile interoperability** in a random independent pair of potential implementers as
\[
\mathcal I(s)=s\,a(s)^2,
\]
where s is the scope-weighted value of pairwise common optional functionality, and both firms must opt in. The square comes from independent firm cost draws; this is **not** the fraction of all technically ISO-compliant products (Core certification etc.). It may not coincide with physical interoperability if optional implementation profiles differ even for two nominal adopters.

## Proposition D1 — unique adoption equilibrium and interior breadth peak (exact)
For b>0, theta>=0 and b+theta<1, each positive s has a unique symmetric atomistic adoption equilibrium
\[
a(s)=\begin{cases}
1 & 0<s\le b+\theta,\\
b/(s-\theta)&b+\theta<s\le1.
\end{cases}
\]
Proof: adopt iff c≤(b+theta*a)/s. Uniform CDF implies \(a=\min\{1,(b+\theta a)/s\}\). The fixed-point expression has a unique interior root a=b/(s-theta) exactly when s>b+theta, and full adoption is consistent exactly when s≤b+theta. No partial equilibrium is feasible at s≤theta, and no other full adoption equilibrium is feasible above the threshold.

Therefore
\[
\mathcal I(s)=\begin{cases}
s,&s\le b+\theta,\\
b^2 s/(s-\theta)^2,&s>b+\theta,
\end{cases}
\quad
\mathcal I'(s)=
\begin{cases}
1,&0<s<b+\theta,\\
-b^2(s+\theta)/(s-\theta)^3,&b+\theta<s\le1.
\end{cases}
\]
Hence **formal technical scope can increase while realized pairwise coverage decreases**. The unique maximizer is \(s^*=b+\theta\). Adoption declines with s on the partial branch. All inequalities are strict away from the kink and boundary under b>0, theta>=0, b+theta<1.

## Proposition D2 — welfare also peaks (exact, within this reduced-form economy)
Take global welfare relative to nonadoption as:
\[
W(s)=V\,\mathcal I(s)+\int_0^{a(s)}
\{s[b+\theta a(s)]-c\,s^2\}\,dc
\]
where \(V\ge0\) is an incremental consumer value of cross-firm functionality; the second term is private operating surplus net of engineering costs. **This is an explicitly chosen separate consumer-value and firm-operating-surplus accounting convention; it is not the welfare formula of the JPET/Salop models.** The firm gain is gross of transfers, with no separately modeled price or intellectual-property royalties.

Exact reduction:
\[
W(s)=\begin{cases}
V s+s(b+\theta)-s^2/2,&s\le b+\theta,\\
b^2 (V s+s^2/2)/(s-\theta)^2,&s>b+\theta.
\end{cases}
\]
On the full-adoption branch \(W'=V+b+\theta-s>0\). On the partial branch
\[
W'(s)=-b^2\{V(s+\theta)+s\theta\}/(s-\theta)^3<0
\]
for V>0 or theta>0. If V=theta=0 the upper branch is flat rather than strictly declining; impose V+theta>0 for a unique welfare maximum at b+theta. The baseline below has V=1, theta>0.

**Exact baseline:** b=theta=1/4, V=1, peak s=1/2. At s=1/2, a=1, I=1/2, W=5/8; at s=1, a=1/3, I=1/9, W=1/6. This is a diagnostic counterexample to "wider formal standard always makes more effective interoperability", NOT a newly discovered empirical regularity.

## Proposition D3 — general cost distribution, conditional
For any differentiable CDF F with positive density f, a stable interior adoption equilibrium obeys \(a=F(z)\), \(z=(b+\theta a)/s\), and \(1-\theta f(z)/s>0\). By implicit differentiation:
\[
a'(s)=-\frac{f(z)z}{s-\theta f(z)},\qquad
\mathcal I'(s)=a^2\left[1-\frac{2zf(z)/a}{1-\theta f(z)/s}\right].
\]
Thus \(\mathcal I'(s)<0\) iff \(2zf(z)/F(z)>1-\theta f(z)/s\). This is a **cutoff-density elasticity condition**, a fairly direct chain-rule identity, not an economic novelty claim. Do not generalize the uniform-cost peak to all heterogeneity distributions.

## Null-model falsification — why D1/D2 FAIL the N3 gate
1. **No national ISO voting is present**. Removing committee governance changes nothing. Hence this cannot substantiate a Gandal–Shy/ISO institutional novelty claim.
2. Setting theta=0 STILL yields a full-coverage-to-partial-coverage reversal with a=b/s and I=b^2/s. Network externalities are not necessary. Hence not a network-specific mechanism.
3. Forcing a=1 eliminates the reversal; voluntary compliance and rising complexity cost are necessary.
4. No prices, entry, royalties or product market competition were solved. Later adding Salop or Cournot without a changed qualitative result would be an empty recombination.
5. Mechanism overlaps prior cost-sensitive adoption and consortium development/adoption results: Zhao–Xia–Shaw (2007), Zhu et al (2006), standards-adoption review (2023), Rosero Abad et al (2026). Full theorem-level noncontainment remains unverified.

**Editorial status: mathematically exact diagnostic [A], economic novelty at most provisional N2, no submission recommendation.**

Reproduction: code/verify_optional_profile_scope.py (SymPy). General F derivative is checked algebraically; numerical values are exact rational.
