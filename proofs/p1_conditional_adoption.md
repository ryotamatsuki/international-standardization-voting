# P1: ISO-style approval, voluntary implementation, and network-driven voting reversal

Research proof note — 2026-11-08. **Conditional existence result; not a claim of unconditional ISO effects or established publication novelty.**

## Institution and timing

Four P-member national bodies each cast one valid yes/no vote on an already-developed interface standard. At least 3 yes votes are required. This is a stylized final ballot, not the complete NP/CD/DIS/FDIS procedure. Firms 0, 1, 2 already use interoperable legacy L; firm 3 uses incompatible M. Four firms price-compete in a length-four Salop circle.

ISO approval makes a settled interface/test specification available. Adapting to legacy interoperability costs firm 3 \(k_L\) if issued and \(k_H\) otherwise, with \(k_L<k_H\). The publication-to-cost channel is an explicit assumption **not derived from the voting rules**. The costs are real resource costs.

Game: final ballot → firm 3's voluntary adoption decision → Bertrand price competition. Existing three firms are committed to continuing L.

Set total market density \(N=1\), network strength \(d\in[1/3,3/8]\), and market shares
\[
(w_0,w_1,w_2,w_3)=(3/25,1/2,3/25,13/50).
\]

## Candidate Bertrand continuation

With squared travel costs on the circle, the legacy quality increments are \(a^0=(2d,2d,2d,0)\). The candidate equilibrium prices and per-unit-circle demands are
\[
p^0=q^0=(1+d/3,1+d/6,1+d/3,1-5d/6).
\]
After full compatibility \(a^1=(3d,3d,3d,3d)\),
\[
p^1=q^1=(1,1,1,1).
\]

These candidates satisfy the interior first-order conditions. Prior analysis presented an interval-specific argument for global deviations, but a full written partition-by-partition proof has **not yet been independently audited**. The Python scripts verify symbolic identities and finitely sampled deviations; they are not mechanized continuous-strategy proofs.

The privately captured increment to firm 3's world profit is:
\[
G_3(d)=\frac14\left[1-(1-5d/6)^2\right]=\frac{d(60-25d)}{144}.
\]

On the interval \(G_3'(d)=(60-50d)/144>0\), and
\[
G_3(1/3)=155/1296,\qquad G_3(3/8)=135/1024.
\]
Hence, under
\[
 k_L<155/1296,\qquad k_H>135/1024,
\]
firm 3 **strictly** implements L if ISO issues the interface, and strictly retains M if not, conditional on the three incumbent firms maintaining L. This is chosen by the firm's profit maximization, not dictated by the ballot.

For example choose \(k_L=1/20=0.05,\ k_H=1/5=0.20\).

## Government voting and welfare

Gross welfare changes from the legacy network to full compatibility:
\[
\Delta W_0^{gross}=\Delta W_2^{gross}=\frac{d(48-139d)}{3600},
\]
\[
\Delta W_1^{gross}=\frac{d(64-5d)}{96},
\]
\[
\Delta W_3^{gross}=w_3\frac{d(216-13d)}{144}+G_3(d).
\]
Country 3 also bears implementation cost \(k_L\) if passage induces entry. Thus \(\Delta W_3=\Delta W_3^{gross}-k_L>0\); other countries' changes are gross values.

Marginal states 0 and 2 switch at
\[
d^*=\frac{48}{139}.
\]
For \(1/3\le d<d^*\): all four vote yes. For \(d^*<d\le3/8\): only countries 1 and 3 vote yes, and the 3-vote rule rejects the proposal.

Sincere binary approval voting is weakly dominant when continuation payoffs for pass/fail are fixed; this is a weak-dominance-refined voting result, not uniqueness of all Nash voting profiles.

World welfare **if approved and implemented** (including implementation resources) changes by:
\[
\Delta W_{\text{world}}(d)=\frac{d(216-47d)}{144}-k_L>0
\]
throughout the region. The exact two endpoints are:
\[
\Delta W_{\text{world}}(1/3)=2681/6480,\qquad
\Delta W_{\text{world}}(3/8)=2389/5120.
\]

Thus the stronger network effect raises the *potential world welfare gain from compatibility*, while shifting two marginal national votes against the proposal.

## Optional bilateral implementation-tool contracting

After publication, an independent provider may build a reference compatibility toolkit at real resource cost \(f=1/20\), and sell it to firm 3 via payment \(t\). Joint surplus is \(S=G_3(d)-f>0\). An equal-surplus Nash bargaining solution gives
\[
t=(f+G_3(d))/2,
\]
provider profit \(t-f=S/2>0\) and adopter incremental profit \(G_3-t=S/2>0\). If both agents belong to country 3, the transfer cancels in national welfare. This is a bargaining-solution illustration, **not** a full noncooperative bargaining subgame.

## Parameter robustness claim and limits

Strict inequalities at the displayed parameter values imply continuity of the symbolic welfare/payoff comparisons under sufficiently small perturbations. **They do not by themselves establish** existence, uniqueness, or continuity of a price-market Nash equilibrium under every nearby perturbation. Those are separate proof obligations.

Major assumptions that remain:
1. ISO issuance reduces compatibility implementation cost, a plausible but unverified exogenous institution-to-market mechanism.
2. Firms 0–2 retain L; no unrestricted simultaneous 4-firm standard-choice equilibrium is claimed.
3. No model of NP expert pledges, CD consensus, the technical grounds for negative votes, post-rejection revision, or complete ISO standard development.
4. Technology access and patent licensing rights are assumed feasible on specified terms.
5. If passage and failure leave feasible actions, payoff primitives, and equilibrium selection all unchanged, the ballot has no causal market effect.
6. Novelty versus Spulber (2019), Barrett & Yang (2001), and Klimenko (2009) remains unresolved.

## Reproduction

\`\`\`bash
python code/p1_iso_verification.py
python code/p1_iso_endogenous_adoption.py
\`\`\`

See [model](../theory/model_and_hypotheses.md), [research status log](../research_log/2026-11-08_initial_assessment.md), and [primary bibliography](../literature/bibliography_and_novelty.md).

Primary external references: [ISO/IEC Directives Part 1 (2026)](https://www.iso.org/sites/directives/current/consolidated/), [Gandal & Shy (2001)](https://doi.org/10.1016/S0022-1996(00)00067-2), [Spulber (2019)](https://doi.org/10.1111/ecoj.12606).
