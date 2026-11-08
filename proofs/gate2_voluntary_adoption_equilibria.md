# Gate 2 — Voluntary adoption: strict continuation equilibria and ISO approval

2026-11-08. **Status: closed-form existence of strict adoption Nash equilibria under an explicit publication-to-implementation-cost assumption.** This is not a unique-implementation theorem and not a claim that ISO automatically reduces implementation costs.

## 1. Complete finite adoption subgame

Four companies price-compete in the Salop markets of [Gate 1](gate1_closed_form_global_bertrand.md). There is a pre-existing interoperable network of firms \(0,1,2\), standard \(L\), and an independent firm \(3\), standard \(M\).

After the yes/no final-ballot outcome \(A\in\{0,1\}\):

- Firms \(0,1,2\) each independently choose **stay with L** or **disconnect** to its own distinct private standard \(X_i\) (zero exit cost, so stability is nontrivial).
- Firm 3 chooses **join L** or **stay with M**.
- All firms compete in Bertrand prices within each country's market.
- A brand's quality increment is \(d\) multiplied by the **number of other brands** adopting the same compatible network.
- If firm 3 joins L it incurs real resource cost \(k_A\), where \(k_1=k_L\) if the standard is officially issued and \(k_0=k_H\) if rejected. Assume \(0\le k_L<k_H\).
- For firms \(0,1,2\), the cost of staying with their installed standard is sunk; joining/rejoining L has no fee in the current-period game. No firm can force another to cease being compatible; technical access for firm 3 is feasible at the stated fee.

The 16 possible technology-choice profiles produce 16 market quality vectors. **Each is followed by a properly specified price-game Nash equilibrium**, with the candidate price profile
\[
p_i= \left(M^{-1}v(a)\right)_i,\quad
M_{ij}=
\begin{cases}
2& i=j\\[-2pt]
-1/2& j=i\pm1\pmod 4\\
0& \text{otherwise}
\end{cases},
\quad
v_i(a)=1+a_i-\frac{a_{i-1}+a_{i+1}}2.
\]
For \(d\in[1/3,3/8]\), all 16 candidate price vectors satisfy the neighbor-demand upper-bound sufficient conditions in the [Gate 1 lemma](gate1_closed_form_global_bertrand.md): positive candidate prices; zero-price left and right bounds in \((0,3/2)\); candidate boundaries in \((0,1)\); opposite brand inferior at candidates and dominates beyond \(3/2\); local neighbor-difference bounds hold. See [exact Python assertions](../code/test_gate123_closed_form.py).

## 2. Continuation equilibria

Normalise world population to \(N=1\) for the following adoption-cost example; the same algebra scales revenues by \(N\).

### Rejection, \(A=0\)

Consider \(s^0=(L,L,L,M)\). Every incumbent is strictly better off keeping L than becoming an isolated brand:

\[
\Pi_i(X_i,L_{-i})-\Pi_i(s^0)=
\begin{cases}
-\dfrac{7Nd(d+24)}{576}<0,&i=0,2,\\[6pt]
\dfrac{Nd(d-12)}{48}<0,&i=1.
\end{cases}
\]
Firm 3's incremental world gross operating profit from joining L is
\[
G_3(d)=\frac{Nd(60-25d)}{144}.
\]
If \(k_H>G_3(d)\), firm 3 strictly prefers M over joining L. Thus \(s^0\) is a **strict Nash equilibrium** of the adoption subgame.

### Approval, \(A=1\)

Consider \(s^1=(L,L,L,L)\). If any single firm isolates itself while the other three remain on L, its gross world profit falls by exactly
\[
G_3(d)=\frac{Nd(60-25d)}{144}>0
\]
(the isolated-firm price equilibrium is a rotation of the benchmark three-versus-one quality vector). Each incumbent \(0,1,2\) thus strictly prefers to stay with L.

Firm 3 strictly joins if \(k_L<G_3(d)\).

Thus \(s^1\) is a **strict Nash equilibrium** of the adoption subgame if \(k_L<G_3(d)\).

### Concrete nonempty region

Choose
\[
N=1,\quad k_L=1/20,\quad k_H=1/5,\quad
d\in[1/3,3/8].
\]
On that entire interval,
\[
G_3(1/3)=155/1296,\quad
G_3(3/8)=135/1024,\quad
\frac1{20}<G_3(d)<\frac15.
\]
Hence the rejection profile \(s^0\) and the approval profile \(s^1\) are each strict Nash equilibria in their respective adoption subgames, and publication changes the **endogenously chosen** adoption outcome along these continuation equilibria.

**Multiplicity warning:** the full 16-profile adoption game can also have weaker coordination equilibria (e.g., all firms isolated, with indifferent incumbent deviations). **Strictness of \(s^0,s^1\) does not prove they are unique or that adoption occurs under every equilibrium selection rule.** If a single-price equilibrium is selected in each price subgame and \(s^0\) following rejection and \(s^1\) following approval are selected, they form the relevant continuation profile in a subgame-perfect equilibrium. A separate selection refinement would be needed to call this an unavoidable prediction.

## 3. Voting backward from the two strict continuations

With the national population vector
\[
w=(.12,.50,.12,.26)
\]
government \(i\)'s objective is home-market consumer surplus plus its owned firm's **worldwide operating profit**, less the firm's domestic implementation resource cost, if incurred.

Governments 0 and 2 have
\[
\Delta W_0=\Delta W_2=\frac{Nd(48-139d)}{3600}.
\]
Government 1 has
\[
\Delta W_1=\frac{Nd(64-5d)}{96}>0.
\]
Government 3 has
\[
\Delta W_3^{gross}
=\frac{11Nd(176-43d)}{2400},
\qquad
\Delta W_3=\Delta W_3^{gross}-k_L>0
\]
for the above cost interval.

The vote reversal threshold for governments 0 and 2 is \(d^*=48/139\). With four valid yes/no ballots, approval requires 3 yes votes. In the sincere/weak-dominance-refined voting profile, passage moves from 4-to-0 to rejection by 2-to-2 at \(d^*\).

With implementation cost \(k_L\) as a real resource cost, world welfare **conditional on the adopted compatibility** improves by
\[
\Delta W_{\mathrm{world}}(d)
=\frac{Nd(216-47d)}{144}-k_L>0.
\]
Therefore a network-effect increase can shift voting against a world-welfare-improving standard, in **an SPNE with the stated strict continuation equilibria**.

### Important equilibrium concept caveat

A final binary vote can have Nash equilibria with nonpivotal, weakly dominated or outcome-irrelevant ballots; sincere voting is a weakly dominant action but not generally the unique Nash strategy. The voting outcome claims here use a specified sincere/weak-dominance refinement. Approval after \(A=1\) is **not** assumed to force adoption — firms choose it because it is strictly privately advantageous in the selected subgame equilibrium.

## 4. Microfoundation of the implementation-cost channel (illustration)

The simplest valid structural interpretation is *coordination and verification overhead*: before a public interoperable reference specification is issued, adapting the isolated technology requires private engineering, bilateral interface discovery, and testing at cost \(k_H\); after issuance it can be implemented with a reusable interface toolkit at cost \(k_L\). The difference is a structural **primitive** that must be defended with institutional facts. ISO itself does not grant patents, force adoption, or automatically waive licensing fees.

A complementary technology-supply story: after approval, a third-party developer can invest real cost \(f\) in a reference toolkit and bargain over a transfer \(t\) with firm 3. A Nash bargaining solution with symmetric surplus shares has
\[
t=\frac{G_3(d)+f}{2},\quad
t-f=G_3(d)-t=\frac{G_3(d)-f}{2}>0
\]
when \(G_3(d)>f\). This establishes *voluntary investment and transfer feasibility* given access to the adopted interface; it does **not** endogenously explain why issuance enables the toolkit.

If \(k_H=k_L\), and approval leaves all feasible technologies, payoffs, and equilibrium selection rules identical, then approval itself cannot change economic adoption outcomes. This *null-institution benchmark* is necessary for credible causal interpretation.

## 5. Assessment

- **Proved in closed form (conditional model):** price-game best-response lemma; gross/private adoption gains; strict continuation adoption equilibria for both ballot outcomes; country votes and world welfare; SPNE existence under specified continuation selection and sincere voting.
- **Not proved:** all-SPNE uniqueness, sophisticated dynamic standard-development procedure, endogenous reduction of implementation costs *by the ISO voting rule itself*, or intellectual-property feasibility without additional assumptions.
- **Next challenge:** develop either an institutional microfoundation with internal investment/verification choices, or a credible equilibrium-selection refinement that survives a less restrictive adoption strategy space. The novelty obstacle is separate (see Gate 3).
