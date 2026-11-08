# Gate 4 — ISO technical objections, abstention, and the endogenous cost of opposition

**Status:** Analytical, conditional theorem for a minimal ISO-type final ballot; 2026-11-08. This extends the P1 national-preference model but **does not** claim that economic protectionism alone constitutes a valid technical objection.

## 1. Exact institutional mapping (ISO/IEC Directives Part 1, 2026)

FDIS approval under §§2.7.2–2.7.3 uses (a) at least two-thirds *yes* among P-member votes and (b) no more than one-quarter *negative* among all nonabstention votes. Negative votes without technical comments are excluded. The protocol permits yes, no, or abstention. If rejected, §§2.7.7–2.7.8 specify possible return, revised drafts, publication as Technical Specification, or abandonment; the *one-shot* game below conditions on a specific final draft and does not model these future steps.

For **exactly four P-member countries, all votes valid and all potential eligible voters**, define \(Y\) positive votes, \(B\) negative votes containing technical comments, and \(A=4-Y-B\) abstentions. With all voters being P-members, the two inequalities reduce to:
\[
\frac{Y}{Y+B}\ge\frac23,\quad
\frac{B}{Y+B}\le\frac14
\quad\Longleftrightarrow\quad
Y\ge3B
\quad (Y+B>0).
\]
This differs from a fixed 3-of-4 threshold as soon as abstentions are allowed.

| \(Y\) | \(B\) | \(A\) | FDIS passes? |
|---:|---:|---:|---|
| 4 | 0 | 0 | yes |
| 3 | 1 | 0 | yes |
| 2 | 2 | 0 | no |
| 2 | 1 | 1 | no |
| 2 | 0 | 2 | **yes** |

The formula is *not* general for P-members and non-P-members mixed together; the two ISO criteria then have different denominators.

## 2. The national-body preference reduced form

Let firm/country \(i\) be as in P1, national product-market share \(w_i=n_i/N>0\), \(\sum_i w_i=1\), network strength \(d>0\). Let the national standardization body have a reduced-form objective \(B_i=CS_i+\lambda_i \Pi_i\) with constant \(\lambda_i>0\). For \(i=0,2\),
\[
\Delta B_i(d)=
\frac{Nd}{144}\left[w_i(216-13d)-4\lambda_i(d+6)\right].
\]
For \(i=1\),
\[
\Delta B_1(d)=
\frac{Nd}{144}\left[w_1(216-13d)-\lambda_1(d+12)\right].
\]
Country 3 supports a published, implemented standard whenever the private joining profit strictly exceeds implementation cost, subject to positive consumer surplus. In the following region assume countries 1 and 3 strictly support publication, and countries 0 and 2 strictly prefer rejection.

Define the two opponents' losses from publication:
\[
\boxed{
L_i(d):=-\Delta B_i(d)
=\frac{Nd}{144}\{(4\lambda_i+13w_i)d+24\lambda_i-216w_i\}>0,\quad i\in\{0,2\}.
}
\]
Their losses are increasing in \(d\) in the region \(L_i>0\) and \(d>0\), since the derivative of \(d(ad+b)\), with \(a>0\) and \(ad+b>0\), is \(2ad+b>0\).

## 3. Legitimate technical-comment opportunity — what is assumed

**Independent eligibility condition:** a country may submit a valid technical negative ballot only if it can substantiate a genuine unresolved technical concern about the draft (e.g., a demonstrable interoperability or conformance defect); denote this feasibility by \(e_i=1\). If \(e_i=0\), *No with a technical comment* is not available. Financial loss does **not** imply \(e_i=1\), and the model does not authorize fabricated objections.

When \(e_i=1\), preparing the technical assessment and evidence requires a real, country-specific administrative/technical resource cost \(c_i>0\). The cost is incurred if the country submits *No*. Otherwise, the country may abstain without cost. Positive countries 1 and 3 choose *Yes* without a ballot preparation cost.

This is a **new, testable modeling assumption**, not an assertion that ISO charges filing fees. It represents the scarce specialist time and engineering evidence required for substantiated technical comments. It is appropriate for an illustrative reduced-form participation game but needs empirical or institutional justification for publication.

## 4. Closed-form "documented objection" theorem

With countries 1 and 3 voting Yes, consider eligible countries 0 and 2 choosing either Abstain \(A_i\) or No \(N_i\) with technical documentation.

- If both Abstain, the ballot has \(Y=2,B=0,A=2\), and passes. Opponent \(i\)'s payoff, relative to rejection, is \(-L_i\).
- If **either** submits an eligible negative vote, there are at most \(Y=2,B\ge1\) and the final draft fails. Any submitting country incurs \(-c_i\); an abstainer pays zero.

The resulting normal-form game is
\[
\begin{array}{c|cc}
 & A_2 & N_2\\ \hline
A_0 & (-L_0,-L_2) & (0,-c_2)\\
N_0 & (-c_0,0) & (-c_0,-c_2)
\end{array}.
\]

**Proposition 4.1 (two eligible challengers).** Assume \(e_0=e_2=1\), \(0<c_i<L_i\) for both countries, and the selected continuation payoffs and country 1/3 yes votes specified above.

1. There are two pure-strategy Nash equilibria: \((N_0,A_2)\) and \((A_0,N_2)\). Both reject the proposed standard, despite *only one technical negative vote*.
2. There is a mixed-strategy equilibrium with each country independently submitting No with probabilities
\[
\boxed{
\Pr(N_0)=1-\frac{c_2}{L_2(d)},\qquad
\Pr(N_2)=1-\frac{c_0}{L_0(d)}.
}
\]
3. Consequently, the mixed-equilibrium probability of **ISO approval** is
\[
\boxed{\Pr(\mathrm{approve})=
\frac{c_0c_2}{L_0(d)L_2(d)}}.
\]
On any interval where \(L_i(d)>c_i\) and \(c_i\) are constant, approval probability is **strictly decreasing** in \(d\).

*Proof.* Each player’s No yields \(-c_i\) independently of the other’s choice; abstaining yields \(-(1-p_j)L_i\), where \(p_j\) is the other’s No probability. The best-response cutoff is \(c_i\le(1-p_j)L_i\). Under \(0<c_i<L_i\), the two asymmetric pure profiles meet these strict best responses, while (No,No) is not an equilibrium because each agent could abstain and save \(c_i\). In a mixed equilibrium, indifference gives \(1-p_j=c_i/L_i\), yielding the two probabilities and the approval probability above. Because both losses strictly increase in \(d\) on the specified interval, the approval probability strictly falls. QED.

**Boundary cases.** If one country is ineligible to provide substantiated technical grounds, \(e_i=0\), that country must abstain. If the other eligible country satisfies \(c_j<L_j\), it submits the single No, and approval fails; if neither can/will submit No, **the two-Yes, two-Abstain ballot passes** even though both countries prefer rejection. If one filing cost exceeds its avoided loss, that country never files unilaterally. This formalizes why *political economic opposition alone* need not translate to ISO rejection.

### Filing threshold

For an opposing incumbent \(i=0,2\), let \(a_i=4\lambda_i+13w_i>0\) and \(b_i=24\lambda_i-216w_i\). The cost of a unilateral objection is privately worthwhile once
\[
L_i(d)\ge c_i.
\]
The unique positive threshold is
\[
\boxed{
d_i^{\rm doc}=
\frac{-b_i+\sqrt{b_i^2+576a_i c_i/N}}{2a_i}.
}
\]
When the baseline country-switch threshold is positive, this documents-needed threshold lies strictly above the costless switching threshold for every \(c_i>0\).

**Important:** if one of countries 0,2 still supports the draft and votes Yes, then three countries vote Yes and one documented No is *insufficient* to defeat the draft; both incumbent opponents must first prefer rejection to reach the two-Yes configuration. If both prefer rejection but neither files a technically valid comment, the draft passes.

## 5. Symmetric closed-form worked case (the original P1)

Take \(N=1,\ w_0=w_2=3/25,\ \lambda_0=\lambda_2=1,\ d=3/8\). Then the two opponents' financial losses are exactly
\[
L_0=L_2=\frac{11}{25600}.
\]
Take real technical-documentation cost \(c_0=c_2=1/10000\) and suppose both genuinely possess valid technical grounds. Both have \(0<c_i<L_i\). Two pure equilibria reject the draft. In the mixed equilibrium,
\[
\Pr(N_0)=\Pr(N_2)=\frac{211}{275},\quad
\Pr(\mathrm{approve})=\frac{4096}{75625}\approx0.05416.
\]
At \(d=1/3<48/139\), both incumbents favor approval; all four vote Yes and it passes. Thus the original reversal survives under a nonempty set of positive documentation costs, while the **mixed-strategy equilibrium gives a continuous, strictly decreasing approval probability** above the filing threshold.

For larger cost or no valid technical grounds, this conclusion no longer follows.

## 6. Social welfare impact

Let the hypothetical net world welfare improvement **if approved and implemented** be
\[
S(d)=\frac{Nd(216-47d)}{144}-k_L>0
\]
per P1. Suppose the evidence preparation costs \(c_i\) are real economic resources. Relative to no standard and no objection costs, expected realized welfare in the mixed voting equilibrium is
\[
\mathbb E[\Delta W]=
\Pr(\mathrm{approve})S(d)-
c_0\Pr(N_0)-c_2\Pr(N_2).
\]
The efficient-approval benchmark exceeds this by
\[
\underbrace{(1-\Pr(\mathrm{approve}))S(d)}_{\text{lost coordination gain}}+
\underbrace{c_0\Pr(N_0)+c_2\Pr(N_2)}_{\text{resources spent on objections}}.
\]
This expression does not claim that all technical comments are socially wasteful in the real world; model comments are documentation costs and unmodeled future design improvements could make criticism valuable.

## 7. Interpretation, limits, and novelty

This result adds an **ISO-rule-sensitive endogenous objection stage**, not just a vote against a standard that hurts domestic profits:
- technology-related evidence is an eligibility condition, rather than assumed automatically from private commercial loss;
- abstentions change the approval threshold through the dual ISO FDIS conditions;
- with costly documentation and two opponents, a **volunteer's dilemma** emerges;
- a higher network effect raises documented-objection incentives and decreases approval probability in the mixed equilibrium.

**This uses a familiar volunteer’s-dilemma strategic form. It is not sufficient on its own to claim a new general game-theoretic mechanism.** Its potential contribution is the sharp connection to the *ISO dual threshold*, endogenous technological objections and the underlying international Bertrand-welfare calculation. This is not an empirical account of actual ISO ballots.

### Scope boundaries

- Four P-members (no non-P ballots), no other valid voters, final stage reached, firm 3’s adoption continuation as selected in Gate 2.
- Technical feasibility \(e_i=1\) is imposed for the theorem; it is not explained by negative welfare.
- The cost of producing a technical report is not an ISO filing charge.
- Stage-specific costs and one-shot rejection; the feedback/revision dynamics prescribed in the actual ISO Directives are not yet included.
- Existing reliance on the acceptance-to-adoption implementation-cost differential remains; a separate no-go note and proposed microfoundation are necessary.

## Sources

- [ISO/IEC Directives Part 1 (2026), §§2.7.2–2.7.8](https://assets.iec.ch/sd/ISO-IEC_Directives_Part-1_2026.html): eligibility of negative votes with technical comments, abstentions and dual thresholds.
- [Farrell & Simcoe (2012), RAND Journal, *Choosing the rules for consensus standardization*](https://doi.org/10.1111/j.1756-2171.2012.00164.x): related bargaining and standard-setting delay mechanisms; **not** a source for this specific volunteer’s-dilemma result.
- [P1 population generalization](p1_population_generalization.md) and [Gate 2 adoption continuations](gate2_voluntary_adoption_equilibria.md).
