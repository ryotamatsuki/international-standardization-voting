# Gate 5A — Can publication influence voluntary adoption without assuming lower implementation costs?

**Date:** 2026-11-08. **Status:** conditional *supply-side investment microfoundation*, independently derived. This is a feasible contract-and-investment continuation under explicit ancillary-demand primitives, not yet a unique SPE of the unrestricted four-firm technology-choice game.

## 1. An impossibility/null benchmark

**Lemma 5A.1 (no automatic publication effect).** If publication \(A\in\{0,1\}\) does not change the post-ballot feasible actions, information, preferences/payoff functions, timing, or equilibrium selection rule, then the corresponding continuation game is identical in the two states. Its equilibrium set is unchanged; if the selected continuation is unique or the same selection function is applied, realized adoption and price outcomes are unchanged.

**Proof.** The game forms are identical, so all best-response inequalities are identical, hence the equilibrium sets coincide. Any selected unique equilibrium or a state-invariant selection yields the same action profile. QED.

**Important limit:** a publicly observed ballot outcome can itself serve as a *sunspot / equilibrium-selection signal* when multiple equilibria exist, even without payoff change. Thus the null benchmark does **not** rule out signaling via equilibrium selection. A claimed causal adoption result must specify which payoff, feasibility, information, expectation, or selection primitive changes.

This is a diagnostic lemma; it is not itself new economics.

## 2. Complementary-tool supply mechanism with fixed cost unchanged

Previously P1 assumed \(k_L< G_3(d)<k_H\), a reduction in the entrant's own implementation cost caused by publication. We instead keep the **same technical development cost** in both states and let publication affect the viability of a **third-party compatibility-tool market**.

- The main four-product-market continuation is unchanged; firm 3's worldwide gross operating-profit gain from joining the three incumbents' \(L\) network is
\[
G(d)=\frac{Nd(60-25d)}{144}>0.
\]
- Firm 3 may independently reverse-engineer the \(L\) adapter at real cost \(K>G(d)\) throughout the selected interval, hence does not join without outside help.
- One independent technology supplier can develop a reusable \(L\)-compatible, independently testable adapter toolkit at a **fixed real cost** \(F>0\), identical whether ISO-type publication is approved or rejected.
- If the standard is officially issued, other third-party users purchase conformity-test/implementation services from this provider and generate **additional commercial receipts** \(R>0\) conditional on production of the toolkit. Their gross willingness to pay is at least \(R\), with total value \(V_C\ge R\). They are a separate ancillary market and do not change the four differentiated brands' prices.
- If publication is rejected, that specific independent third-party demand is absent (\(R_0=0\)); this is the **substantive institutional primitive**. It may arise from buyers who demand an independently verifiable *published* interoperability reference. It is **not** a general fact that ISO approval mechanically produces customers, and is not ISO's own certification service. ISO does not certify products.
- The toolkit supplier is assumed to be resident in country 3, and the ancillary customers likewise reside there, preserving the country-0/2/1 comparisons.
- The supplier and firm 3 may negotiate a **binding contract before** the supplier incurs \(F\). Fees are pure transfers within country 3. At this stage, firms 0–2 are using the incumbent interface \(L\). This is a conditional construction, not the full endogenized four-firm strategy game.

### Proposition 5A.2 (supplier entry can implement publication-dependent adoption)

Suppose the fixed-cost window
\[
\boxed{R<F,\qquad G(d)<F<G(d)+R,\qquad K>G(d)}
\]
holds over some nonempty interval of \(d\).

**Following rejection**, the supplier has at most the firm-3 customer's willingness to pay \(G<F\), no ancillary revenue, and therefore cannot cover real development cost \(F\). Firm 3 does not independently implement because \(K>G\). The market stays at \((L,L,L,M)\).

**Following publication**, total jointly appropriable revenue from firm 3 and third-party customers is \(G+R>F\). A binding contract can set a license fee \(t\) satisfying
\[
\boxed{F-R<t<G}.
\]
The supplier invests (net commercial profit \(t+R-F>0\)) and firm 3 voluntarily joins L (incremental profit \(G-t>0\)). Therefore all four firms are interoperable.

A symmetric Nash bargaining *solution* over the ex-ante surplus \(G+R-F\) gives the closed-form fee
\[
\boxed{t^*=\frac{G+F-R}{2}}
\]
and both parties gain
\[
G-t^*=t^*+R-F=\frac{G+R-F}{2}>0.
\]
This bargaining solution is **not** falsely labeled a unique noncooperative bargaining equilibrium; it is an explicit feasible strictly individually rational contracting allocation. Noncooperative implementation can use an explicitly selected positive-surplus bargaining protocol.

**Proof.** The rejection state's maximum toolkit receipts are \(G\), below production cost \(F\); self-adaptation is privately dominated by not joining. In the approval state, the inequalities \(F-R<t<G\) are jointly satisfiable iff \(G+R>F\). They imply positive supplier and entrant incremental profits; the toolkit is produced and adopted voluntarily. Solving equal surplus shares yields \(t^*\). QED.

### Induced national welfare and the ISO pivotal threshold

The original four-brand demand and price equilibria remain the same. For opponents \(i=0,2\),
\[
\Delta B_i=\frac{Nd}{144}\left[w_i(216-13d)-4\lambda_i(d+6)\right].
\]
Country 1 also retains its original consumer/profit terms. Country 3 internalizes firm 3, the supplier, and ancillary users. Its incremental combined real benefit (aside from its home-market consumer gain) is
\[
G(d)+V_C-F>0,
\]
so it strictly supports publication in the specified region, even after accounting for real tooling costs. With nationally resident provider/users, the opponent countries' price/consumer market incentives and **their closed-form vote thresholds do not change**.

For total world welfare, when compatibility is implemented the improvement is
\[
\Delta W_{\rm World}=
\frac{Nd(216-47d)}{144}+V_C-F
\ \ge\
\frac{Nd(216-47d)}{144}+R-F.
\]
The addition is *real ancillary value* \(V_C\) less *real investment cost* \(F\), not the license fee \(t\), which is a transfer.

Thus P1's inefficient rejection can arise **without postulating different exogenous costs of self-implementation after publication/rejection**. The crucial remaining assumption is that standard publication elicits a side market for third-party conformance tools and that this demand can be contracted for.

## 3. Rational-number, non-knife-edge example

Take
\[
N=1,\qquad d\in[1/3,3/8],\qquad F=1/5,\quad R=1/10,\quad K=1/4.
\]
Then
\[
G(1/3)=155/1296,\quad G(3/8)=135/1024,
\]
so throughout the interval
\[
0<R<F,\quad G(d)<F,\quad F<G(d)+R,\quad K>G(d).
\]
The contract's total surplus is
\[
G(d)+R-F=G(d)-1/10>0
\]
and increases over this interval. For instance,

| \(d\) | \(G(d)\) | supplier/firm-3 joint surplus | Nash fee \(t^*\) | lower bound on net world welfare |
|---|---|---|---|---|
| \(1/3\) | \(155/1296\) | \(127/6480\) | \(1423/12960\) | \(2357/6480>0\) |
| \(3/8\) | \(135/1024\) | \(163/5120\) | \(1187/10240\) | \(2133/5120>0\) |

The original P1 government-0/2 crossing at \(d^*=48/139\) remains intact under the conditional supplier mechanism. This is a nonempty interval of \(d\) and a strict, open set of \(F,R,K\) nearby.

## 4. How faithful is the institutional interpretation?

**Supported by primary materials:**
- ISO explicitly distinguishes a published international standard from the third-party certification/conformity-assessment services that might use that standard. ISO itself provides **no certification**.
- Independent labs and third-party tooling can implement conformity tests; whether that market exists is industry-specific.
- Network effects involving complementary product/tool investment are standard in industrial organization; this **mechanism family is not original**.

**Still assumed, not demonstrated from ISO's charter:**
- Publication creates sufficient **incremental** complementary-tool demand \(R_1-R_0>0\), whereas an unsuccessful draft does not. This depends on users valuing published normative test criteria and cannot be asserted universally.
- Supplier and side customers share a country with firm 3; this is a tractable distributional assumption.
- Supplier and entrant can commit to ex-ante licensing; IP rights, access and procurement specifics are not modeled.
- Existing firms do not strategically undermine the standard/toolkit relationship after signing. Full simultaneous standard choice plus supplier contracting and all continuation selection equilibria is not solved.
- The technically valid basis for ISO negative votes is handled separately in [Gate 4](gate4_technical_objections_and_abstention.md); this mechanism does not automatically make a negative vote technically valid.

**Assessment:** This is a preferable *economically explicit alternative* to an unexplained \(k_H-k_L\), but **not** a unique institutional microfoundation or proof that every ISO approval creates a new conformity market.

## 5. Related literature and documentary anchors

- [ISO: Conformity assessment](https://www.iso.org/conformity-assessment.html) — third-party conformity activity; ISO does not certify.
- [NIST: Conformance testing](https://www.nist.gov/itl/ai/applied-ai-research-group/conformance-testing) — labs and test-suite provision are separate from standard-setting.
- [Farrell & Saloner (1988), *Coordination through Committees and Markets*, RAND Journal](https://ideas.repec.org/a/rje/randje/v19y1988isummerp235-252.html) — standard-setting coordination and irreversible market choices.
- [Katz & Shapiro (1994), *Systems Competition and Network Effects*, JEP](https://doi.org/10.1257/jep.8.2.93) — network effects involving complementary technologies.
- [Church & Gandal (1993), *Complementary network externalities and technological adoption*, IJIO](https://doi.org/10.1016/0167-7187(93)90006-X) — complementary production and adoption.
- [Existing implementation-cost version](gate2_voluntary_adoption_equilibria.md).
