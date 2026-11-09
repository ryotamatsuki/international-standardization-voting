# R12 minimal game: backward-compatible standard version and strategic legacy/frontier investments
Status: exact **within-model mathematical lemma**, not yet an original economic theory contribution to a journal. Date 2026-11-09.

## 0. Economic meaning and institutional scope
An existing protocol generation has an installed base; a standards consortium decides how much backward compatibility b to preserve when defining the NEXT revision, b∈[0,1]. Legacy vendor invests r≥0 in compatible migration interfaces; frontier vendor invests y≥0 in new generation software/quality. Neither variable is the JPET x_i residual product similarity and neither equals a binary installed-base market share. This is not a national ISO ballot or a complete industrial-organization price equilibrium.

Large L>0 is the legacy installed-base margin for migration support; T>0 is standalone prospective value of new generation innovations; 0<γ<1 is the strength of private cross-generation COMPLEMENTARITY (joint engineering support). Firms' reduced-form private payoffs for fixed b:
\[
 \pi_L(r,y;b)=Lbr+\gamma b r y-\tfrac12r^2,
 \quad
 \pi_F(r,y;b)=T(1-b)y+\gamma b r y-\tfrac12 y^2.
\]
This is a structural *hypothesis* about business benefits, not an estimated demand system. Linear–quadratic costs allow an exact benchmark; note that b=1 eliminates autonomous frontier-feature benefits T(1-b), but frontier innovation can still be profitable because it enhances joint migration value γbr y.

## 1. Exact proposition (mathematical A; economic novelty UNVERIFIED/N2)
For all L,T>0 and 0<γ<1, for every b∈[0,1] the simultaneous private investment game has a unique Nash equilibrium:
\[
 r^*(b)=\frac{Lb+\gamma bT(1-b)}{1-\gamma^2 b^2},\qquad
 y^*(b)=\frac{T(1-b)+\gamma L b^2}{1-\gamma^2 b^2}.
\]
Both objectives are strictly concave in each firm's own effort, and \(\gamma b<1\) guarantees a unique BR intersection; at b=0 boundary r*=0, frontier y*=T; no other nonnegative equilibrium exists.

**Sharp response threshold.** Let
\[
 N(b)= -T+2\gamma Lb+T\gamma^2(2b-b^2).
\]
Then
\[
 \frac{dy^*}{db}=\frac{N(b)}{(1-\gamma^2 b^2)^2},
 \quad N'(b)=2\gamma L+2T\gamma^2(1-b)>0.
\]
Since N(0)=-T<0:
- If \(2\gamma L\le T(1-\gamma^2)\), frontier effort \(y^*(b)\) strictly falls over b∈[0,1) (at equality derivative zero only at b=1).
- If \(2\gamma L>T(1-\gamma^2)\), \(y^*(b)\) is **U-shaped**: it falls for low backwards compatibility, then increases after a unique interior threshold \(b_*\) where N(b*)=0.
- If \(\gamma L>T(1-\gamma^2)\), FULL b=1 backward compatibility gives **more** frontier investment than NO b=0, because \(y^*(1)=\gamma L/(1-\gamma^2)>T=y^*(0)\).

Interpretation: compatibility has TWO effects on frontier effort: direct reduced proprietary new-feature return (the T(1-b) term) and indirect additional complementary return from legacy migration support (γbr y). Relative magnitudes and installed base determine which dominates. In contrast, setting γ=0 yields y=T(1-b), strictly decreasing. This ablation makes cross-generation engineering complementarity necessary for the U-shape **within this specification**.

### Proof
The two global best responses are \(r=Lb+\gamma b y,\ y=T(1-b)+\gamma b r\). As \(\gamma b<1\), their substitution yields the displayed unique positive intersection. Own payoff second derivatives are -1, so every displayed BR is a global best response. Differentiate the rational form of y. The numerator N(b) is strictly increasing in [0,1], proving the exhaustive sign classification. At b=0, y=T; at b=1, y=γL/(1-γ²), yielding the end-point inequality.

### Exact rational benchmark (an illustration, not calibration)
Set \(\gamma=1/2,L=2,T=1\).
| b | r*(b) | y*(b) | b r*(b) (bridge quality index) |
|---|---|---|---|
| 0 | 0 | 1 | 0 |
| 1/4 | 38/63 | 52/63 | 19/126 |
| 1/2 | 6/5 | 4/5 | 3/5 |
| 3/4 | 102/55 | 52/55 | 153/110 |
| 1 | 8/3 | 4/3 | 8/3 |
Unlike a probability, b r* can exceed 1 (it is an effort-weighted interface quality INDEX). No inference about actual interoperable product pair rate is allowed.

## 2. Binary policy diagnostic, NOT full institutional equilibrium
If a hypothetical technical body maximized *aggregate optimized producer profit only* between b=0 and b=1, the result would be:
\[
 \sum\pi^*(0)=T^2/2,\quad
 \sum\pi^*(1)=\frac{L^2(1+\gamma^2)}{2(1-\gamma^2)^2}.
\]
It would select fully backward compatible b=1 iff
\(L/T\ge (1-\gamma^2)/\sqrt{1+\gamma^2}\).
**This is NOT a social welfare optimum**: consumer surplus, price, foreign markets, certification investment, and national standards body aggregation are omitted. This threshold is elementary optimization; do not call it a new SSO voting equilibrium.

## 3. What is NOT yet solved
1. ISO committee choice, voting, proposal revision, country welfare and political aggregation are not endogenous here.
2. A Cournot/Salop or other consumer market continuation is not derived; L and T are reduced-form investment returns.
3. Inter-firm investment complementarity γbr y is technologically plausible but needs microfoundation and direct 2026 prior-art noncontainment.
4. The nominal b requirement is NOT equivalent to actual hardware-level interoperability; b r is a quality proxy and must not be sold as a statistical share of compatible users.
5. Existing published dynamic standards and R&D theory already contains many compatible qualitative results (Farrell–Saloner; Kristiansen; Aoki–Arai; Wang–Buccella). This lemma is mathematical A, economic novelty only N1/N2 provisional.

## 4. Journal gate
**Reject the result as a standalone paper main theorem** pending sharper novel economic prediction that logically REQUIRES institutional standard revision and private complementary investments, with observable market outcomes. More algebraic thresholds will not fix this. Next move should be closest-theorem comparison and identifiable 2026 OCPP version evidence, not add complexity automatically.

Reproduction: code/verify_version_migration_20261109.py and run output. All calculations used SymPy exact symbolic or rational evaluation. No engineering cost/certification data have been estimated.
