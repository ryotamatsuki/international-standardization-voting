# P1-KS: uniform installed bases h and arbitrary national populations — exact two-dimensional theorem
Date: 2026-11-09 (JST)
Branch: research/p1-proof-novelty-gate-20261108
**Status:** analytically certified conditional results under **selected interior fulfilled-expectations price FOC continuation**. This is **not** a global Bertrand best-response proof or a full SPNE existence theorem. No assertion of novelty against prior art.

## 1. Scope and definitions

Retain the four-brand (firms at 0,1,2,3) length-four quadratic Salop circle, four segmented national markets, country weights \(w_i>0,\sum_iw_i=1\), home consumer surplus plus home firm's worldwide operating profits, four valid Yes/No national votes and a 3-of-4 quota. Three old firms choose old standard L or their own singleton \(X_i\), while firm 3 chooses L or singleton M. Following the ballot A, the entrant's L adaptation costs are \(k_L\) on publication, \(k_H\) after rejection; these are **exogenous institutional primitives**.

Generalize the earlier fixed historical base \(B_j=N\) to **\(B_j=hN\) for every firm j**, with \(h\ge0\). This is a common but variable installed base, **not arbitrary heterogeneous firm-specific bases \(h_j\)**. On technology state \(s\), groups of interoperable products merge their historic bases:

\[
a(s)=\beta H(s)\{h{\bf1}+\bar q/4\},\qquad
q^k={\bf1}-\Lambda p^k+\Lambda a,\quad
\bar q=\sum_k w_kq^k.
\]

With \(\Lambda_{ii}=1,\Lambda_{i,i\pm1}=-1/2\), let \(C(s)=I-\beta\Lambda H(s)/4\), \(T=C^{-1}\Lambda\). Interior FE fulfilled demands and differentiated-price FOCs yield \(p^k=p^\ell=p(s)\) at all destinations, independent of \(w\), and

\[
p(s)=[T+\operatorname{diag}(T_{ii})]^{-1}C^{-1}({\bf1}+\beta h\Lambda H{\bf1}),\qquad
q(s)=C^{-1}({\bf1}-\Lambda p+\beta h\Lambda H{\bf1}).
\]

All statements below are algebraic results *within these candidate interior continuation solutions*. They are not a proof of global strategic optimality outside the interior region.

Normalize the total current market to \(N=1\) for the rectangle theorem and costs \(k_L=1/100,k_H=2/5\). For general N, scale operating profits and consumer surplus by N, and evaluate the cost thresholds in units \(k_A/N\).

## 2. Closed-form price and profit for O=1110 vs F=1111

Define

\[
A=12-5\beta+4\beta h,\quad
J=24-9\beta+4\beta h,\quad
E=24-21\beta+4\beta^2+(8\beta^2-20\beta)h.
\]

At \(O=(L,L,L,M)\),

\[
\begin{aligned}
p_0=p_2&=\frac A{4(3-\beta)},&
q_0=q_2&=\frac{(8-3\beta)A}{16(3-\beta)(2-\beta)},\\
p_1=q_1&=\frac J{8(3-\beta)},&
p_3&=\frac E{8(3-\beta)},&
q_3&=\frac E{4(3-\beta)(2-\beta)}.
\end{aligned}
\]

At \(F=(L,L,L,L)\), \(p_i=q_i=1\) for all firms and each consumer's network bonus is \(\beta(4h+1)\). Unit-density circle consumer surplus without the common \(4V\) is \(C_F=4\beta(4h+1)-13/3\).

Normalized firm worldwide profits (\(N=1\)) in O:

\[
\pi_o^O=\frac{(8-3\beta)A^2}{256(3-\beta)^2(2-\beta)},\quad
\pi_c^O=\frac{J^2}{256(3-\beta)^2},\quad
\pi_3^O=\frac{E^2}{128(3-\beta)^2(2-\beta)}.
\]

All have \(\pi_i^F=1/4\). Define \(\Delta C=C_F-C_O\), \(\Delta\pi_i=1/4-\pi_i^O\), \(G_3=\Delta\pi_3\). With normalized costs, national gains are

\[
\begin{aligned}
\Delta W_{0,2}&=w_{0,2}\Delta C/4+\Delta\pi_o,\\
\Delta W_1&=w_1\Delta C/4+\Delta\pi_c,\\
\Delta W_3&=w_3\Delta C/4+G_3-k_L.
\end{aligned}
\]

World welfare improvement **if full adoption actually occurs** is \(\Delta W_{\rm World}=\Delta C/4+\sum_i\Delta\pi_i-k_L\).

## 3. Theorems on a genuinely two-dimensional parameter rectangle

Let

\[
\boxed{R=\{(\beta,h):1/10\le\beta\le1/2,\;3/4\le h\le5/4\}.}
\]

Exact rational **bivariate Bernstein coefficient certificates** (including positive denominators) establish all the following over the *entire closed rectangle*, rather than at sampled points:

**KS-GH-L1 (positive, growing consumer benefit):** \(\Delta C>0\), \(\partial_\beta\Delta C>0\).

**KS-GH-L2 (heterogeneous incumbent losses):** \(\Delta\pi_0=\Delta\pi_2<0,\;\Delta\pi_1<0,\;\partial_\beta\Delta\pi_0<0\).

**KS-GH-L3 (strict voluntary adoption):** \(1/100<G_3(\beta,h)<2/5\) across R. Thus entrant 3 strictly joins on approval and strictly refuses on rejection, provided firms 0–2 stay on L.

**KS-GH-L4 (all 16 adoption configurations):** All 16 interior FE price candidates have positive prices and demands and strictly interior neighboring consumer boundaries. Using five rotation classes, 80 positivity/interior inequalities are certified across R. All 24 isolated-incumbent-to-L adoption comparisons, across all 16 states, have 21 **strict** increases in own price-equilibrium operating profit and 3 exact indifferences (when no rival is on L), throughout R. Hence L weakly dominates a singleton for every incumbent. In the *selected-price finite adoption game*, I=0000 is an unrefined Nash equilibrium while O=1110 (rejection) and F=1111 (approval) are strict Nash equilibria. The incumbent weak-dominance refinement removes I.

**KS-GH-P1 (arbitrary country-population thresholds):** For \(\Delta C>0\), each outer incumbent country \(i=0,2\) sincerely supports the standard precisely when

\[
\boxed{w_i\ge\tau_o(\beta,h)=\frac{4(\pi_o^O-1/4)}{\Delta C}}.
\]

For the central incumbent \(i=1\),

\[
\boxed{w_1\ge\tau_c(\beta,h)=\frac{4(\pi_c^O-1/4)}{\Delta C}}.
\]

These are *closed-form* rational functions since \(\pi_o^O,\pi_c^O,\Delta C\) are rational. Exact certificates on R prove

\[
\partial_\beta\tau_o>0,\quad \partial_\beta\tau_c>0,\quad
\partial_h\tau_o>0.
\]

Thus the outer-country **critical network strength** \(\beta_i^*(h,w_i)\) exists and is unique whenever \(\tau_o(1/10,h)<w_i<\tau_o(1/2,h)\). Implicit derivatives give
\(\partial_h\beta_i^*=-\tau_{o,h}/\tau_{o,\beta}<0\)
and \(\partial_{w_i}\beta_i^*=1/\tau_{o,\beta}>0\).
Larger inherited installed base makes the country reverse at *lower* network intensity, whereas a larger domestic market requires *higher* intensity to trigger opposition.

**KS-GH-P2 (uniform open-population-set reversal):** For **every** \(h\in[3/4,5/4]\), and country shares satisfying

\[
\boxed{0.104<w_0,w_2<0.125,\quad w_1>0.06,\quad
w_3=1-w_0-w_1-w_2>0,}
\]

the 3-of-4 sincere ballot is **YYYY** at \(\beta=0.1\) and **NYNY** at \(\beta=0.5\), under selected O-after-rejection/F-after-approval adoption continuations. Bounds were certified by \(\max_h\tau_o(.1,h)<0.104\), \(\min_h\tau_o(.5,h)>0.125\), \(\max_h\tau_c(.5,h)<0.06\); country 3 strictly supports because \(k_L<G_3\) and \(\Delta C>0\). This is a nonempty open population region and nonzero-width installed-base interval, not a special-case \(h=1,w_0=w_2=.12\) numerical example. For unequal \(w_0,w_2\) their two crossing points differ; with country 1 and 3 always in favor, approval ceases when both outer-country votes have switched (the later of the two unique threshold crossings).

**KS-GH-P3 (opposition despite increasing world efficiency):** On R,
\[
\Delta W_{\rm World}>0,\quad\partial_\beta\Delta W_{\rm World}>0,\quad
\Delta C/4+\sum_i\Delta\pi_i>G_3.
\]
Thus the world gross compatibility gain exceeds the entrant's private joining gain, and *any* normalized joining fee \(0<k_L<G_3\) makes full compatibility potentially world-welfare improving. The specific \(k_L=1/100\) ensures adoption.

**KS-GH-P4 (sincere-vote critical point with benchmark national weights):** For \(w_0=w_2=3/25\), \(w_1=1/2,w_3=13/50\), the unique critical \(\beta^*(h)\) in the tested interval **decreases** with h, and:

| h | unique critical beta |
|---|---:|
| 3/4 | 0.446161163849873 |
| 1 | 0.349670283323148 |
| 5/4 | 0.286262300037029 |

The decimals locate roots of the exact implicit equation \(\tau_o(\beta,h)=3/25\); they are **not** stand-alone numerical proof of uniqueness (the derivative certificate proves uniqueness).

## 4. Distinct firm vs country thresholds

The outer firm loses operating profits upon full interoperability iff (on the interior branch with positive prices)

\[
h>h_o^{\rm profit}(\beta)
=\frac{8(3-\beta)\sqrt{(2-\beta)/(8-3\beta)}-12+5\beta}{4\beta}.
\]

The **central firm** loses gross operating profit iff \(h>1/4\).

A country with \(w_0=0.12\) loses national welfare at \(\beta=1/2\) only if
\[
h>h_0^{\rm national}(.5,.12)
=-115/244+\sqrt{4681}/61\approx0.6502923595
\]
on the positive interior branch. In contrast, the outer firm's *private* profit-loss threshold at \(\beta=.5\) is only \(h_o^{\rm profit}(.5)\approx0.0538446142\).

This separates a firm's private rejection incentive from the national welfare criterion: home-market consumer surplus can outweigh the industry's worldwide profit loss over a large h range. The separating threshold and economic implication are more substantive than merely listing a country vote count, but **their novelty is not established** against earlier installed-base/international-compatibility theories.

## 5. Scope of the result and publication implication

- **Actually verified:** exact algebra and rational signs in the selected interior continuation; all 16 candidate prices are strictly interior; incumbent L weak-dominance; strict O/F adoption continuations and country-support threshold signs on a two-dimensional region.
- **Not verified:** global price-Nash optimality against arbitrary nonlocal or different-national-market-price deviations; all possible alternative FE/price branches; unconditional SPNE existence; country-specific heterogeneity \(h_i\); endogenous institutional \(k_L<k_H\); theorem-level novelty.
- **Do not claim:** general N countries or all market-demand forms. Here four firms/four countries remain, while scalar common installed base h and the full national population simplex are generalized.
- **Editorial recommendation:** These results strengthen P1-KS from a single installed-base/population calibration to an open *joint* parameter region and a novel-to-this-calculation comparative statics \(\partial_h\beta^*<0\). But it is still anchored in a specific Salop topology, and the standard old installed-base mechanism may contain the economic insight. First perform theorem-level prior-art comparisons; then consider general K-country *voting-aggregation* extension separately, without unnecessarily expanding the product-market player count.

## 6. Reproduction and relation to legacy inventory

Script: [code/verify_ks_general_hw_20261109.py](../code/verify_ks_general_hw_20261109.py).
- 15 analytic inequalities on the beta–h rectangle, each with exact rational polynomial/Bernstein certificate.
- 5 rotation classes covering 16 technology profiles: 80 price/demand/interior-boundary checks.
- 21 strict and 3 indifferent incumbent adoption comparisons.
- 3 uniform ballot threshold bounds and root calculations.

This **extends** KS-C02, C03, P07, P08, P09, P11 and C04 in [41-result inventory](p1_ks_complete_result_inventory_20261109.md); it does not replace that inventory or alter the exogenous compatible-brand-count original P1. The core epistemic caveat about selected interior price equilibria remains unchanged.
