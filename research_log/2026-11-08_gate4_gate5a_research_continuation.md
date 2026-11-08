# Research continuation — ISO-specific technical voting and voluntary tool supply (2026-11-08)

## Why this continuation was undertaken

Previous audit found that national population-market weights and welfare-derived voting thresholds are acceptable conditional model primitives, but three problems remained:
1. National bodies' negative ballots require technical comments, rather than mere economic opposition.
2. Abstentions make ISO DIS/FDIS's double-threshold rule different from a generic fixed supermajority.
3. The baseline assumption \(k_L<G_3(d)<k_H\) directly assigns publication a lower implementation cost, without an investment mechanism.

This branch now contains two **optional analytical extensions**; they should not both be treated as part of the core paper until the argument is streamlined.

## Gate 4 — Verifiable technical objections and endogenous documentation

New proof: [gate4_technical_objections_and_abstention.md](../proofs/gate4_technical_objections_and_abstention.md)

When all four voters are P-members and all negative votes provide the necessary technical comments, the ISO FDIS approval rule becomes \(Y\ge3B\), with \(Y\) Yes and \(B\) No, excluding abstentions.

With two pro-publication Yes voters (countries 1 and 3), two opposing but technically eligible countries 0 and 2, and nonzero costs \(c_i\) of preparing genuine supporting technical analyses, the opponents face a volunteer's dilemma:
\[
\begin{array}{c|cc}
& A_2&N_2\\\hline
A_0&(-L_0,-L_2)&(0,-c_2)\\
N_0&(-c_0,0)&(-c_0,-c_2)
\end{array}
\]
where \(L_i=-\Delta B_i>0\) is the national-body loss from approval. For \(0<c_i<L_i\), the game has two asymmetric pure equilibria, each rejecting the draft, and a mixed equilibrium:
\[
\Pr(N_0)=1-c_2/L_2,\quad
\Pr(N_2)=1-c_0/L_0,\quad
\boxed{\Pr(\mathrm{approve})=c_0c_2/(L_0L_2)}.
\]
The approval probability decreases strictly as network effects grow in the region where the losses \(L_i(d)>c_i\) increase.

For the original symmetric size example at \(d=3/8\), costs \(c_i=10^{-4}\), losses \(L_i=11/25600\), mixed approval probability \(4096/75625\). The choice of technical-documentation cost is an illustrative resource cost, **not a legal filing fee**.

**Limit:** having a financial incentive to reject does not automatically imply genuine technically defensible comments. Technical eligibility is an explicit separate assumption. The structure is a standard volunteer's dilemma, not a standalone novel game-theory solution.

## Gate 5A — Investment-based alternative to publication-induced low costs

New proof: [gate5a_endogenous_tool_supply_channel.md](../proofs/gate5a_endogenous_tool_supply_channel.md)

Replace differential implementation costs by an unchanged supplier's fixed engineering cost \(F\), independent of the ISO outcome. Without issued standard, a toolkit supplier has at most entrant's private willingness-to-pay \(G(d)\). With a published normative interface, a separate third-party conformity/implementation market additionally provides supplier receipts \(R>0\); the additional potential buyers are assumed to value the **published verifiable reference**, not a certification service offered by ISO.

If
\[
0<R<F,\quad G(d)<F<G(d)+R,\quad K>G(d),
\]
a toolkit is unprofitable to produce without approval, but can be developed and sold by a third-party supplier after approval through an ex-ante fee \(F-R<t<G(d)\) while preserving strictly positive gains for both supplier and adopter. Symmetric ex-ante Nash bargaining yields
\[
t=(G+F-R)/2.
\]
This is a feasible contracting/bargaining solution, **not** a proof of the entire unrestricted adoption/price game having a unique SPNE. Adoption still depends on a substantive institution-to-market primitive: publication must create *additional independent third-party demand* \(R\). If it does not, publication cannot automatically induce the change.

A nonempty exact example:
\[
N=1,\quad F=1/5,\ R=1/10,\ K=1/4,\quad d\in[1/3,3/8].
\]
The private entrant gain \(G(d)=Nd(60-25d)/144\) lies between \(155/1296\) and \(135/1024\), so the inequalities are strict throughout. Net global welfare gain is bounded below by \(Nd(216-47d)/144+R-F\), which is positive, and the original opponent-country voting threshold \(48/139\) is unaffected if all tool suppliers/customers are in country 3.

**Novelty:** Complementary-investment network effects are established in Church & Gandal (1993), Katz & Shapiro (1994), and Farrell & Saloner (1988). The supply mechanism should therefore be described as an economically credible supporting mechanism, not first-in-literature.

## Strictly bounded institutional interpretation

- ISO itself **does not certify**. Independent external conformity-assessment organizations may use published standards: [ISO official](https://www.iso.org/conformity-assessment.html).
- FDIS technical comments and abstention are directly from [ISO/IEC Directives Part 1 (2026), §2.7](https://assets.iec.ch/sd/ISO-IEC_Directives_Part-1_2026.html).
- Approval at FDIS presupposes previous NP/CD stages, which are not modeled.
- The full equilibrium after failed draft revision, external side markets across countries, and unrestricted standard switching are not solved.
- Neither new mechanism's first-in-literature novelty is established.

## Verification and reproducibility

- [Gate 4 exact SymPy tests](../code/test_gate4_iso_technical_objections.py): all 81 possible Y/N/A ballot profiles for 4 countries, 2x2 Nash equilibria, mixed probabilities, strict filing thresholds.
- [Gate 5A exact SymPy tests](../code/test_gate5a_tool_supply.py): no-tool/with-tool conditions, license fee, real global welfare, inequalities across the original P1 interval.
- [GitHub Actions successful run](https://github.com/ryotamatsuki/international-standardization-voting/actions/runs/42471600556): previous gates, national preference weight and ballot constraints, plus both new test modules have PASS status.

## Editorial judgment

**Advance research but do not merge into main as a publication-ready theorem.** Gate 4 is a sharper ISO-specific extension and Gate 5A replaces an especially fragile institutional cost assumption by an explicit private-investment incentive. Both introduce new primitives that must be defended empirically or institutionally.

Best next task: choose which extension offers a genuinely *novel* economic result once compared carefully with voting-participation, volunteer's-dilemma, and indirect-network-effect papers. Then incorporate only the strongest contribution into the main theorem; keep the other as optional robustness/microfoundation.
