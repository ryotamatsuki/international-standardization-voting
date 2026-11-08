# P1 Institutional-Validity & Prior-Art Audit (2026-11-08)

**Purpose:** Does the assumption that country-level market interests drive formal ISO voting fall inside acceptable theoretical abstraction, and is the proposed mechanism incrementally novel?

**Bottom line:** A *stylized national-position game* grounded in domestic economic interests is acceptable economic modeling and has direct institutional motivation. A literal ISO **FDIS valid-negative-ballot** mechanism based exclusively on lost exporter profits is **not** faithful to current formal rules. Furthermore, the assumed **ISO approval → implementation cost drop** is not itself microfounded. Theorem novelty remains unverified.

## 1. Exact primary institutional evidence

1. **ISO/IEC Directives, Part 1, 21st ed. (2026), §0.7(c) and §1.7.1:** National Bodies must take account of all relevant national interests and establish national technical positions early in the process. This supports national-interest aggregation, not strict national social-welfare maximization. Source: https://www.iso.org/sites/directives/current/consolidated/
2. **ISO/IEC Directives, Part 1, §§2.6.3–2.6.4:** DIS uses P-member two-thirds and valid negative-quarter thresholds, and can proceed directly to publication if approved without subsequent technical changes. Consequently FDIS is not mandatory for every project; drafts are available and commented on at DIS.
3. **ISO/IEC Directives, Part 1, §§2.7.2–2.7.3:** An FDIS national-body rejection must state technical reasons. Negative votes lacking technical comments are excluded from ballot counts. A political-economic loss alone does not establish a valid official negative vote.
4. **ISO/IEC Directives, Part 1, §2.7.7:** Rejection can trigger redrafting, Technical Specification publication, or termination; it is not necessarily a permanent prohibition on technical interoperability.
5. **ANSI, International Procedures, January 2025:** U.S. technical advisory groups and domestic stakeholders collectively determine U.S. national positions; national position formation seeks balanced participation, without domination by a single interest. https://ansi.org/iso/us-representation-in-iso/international-procedures
6. **ISO, Developing standards:** industry, researchers, consumers, NGOs, and governments participate as experts; standard creation is a consensus process, not simply a cabinet-level governmental decision. https://committee.iso.org/developing-standards.html

## 2. Primary scholarly comparisons

| Source | What is established | Implication for P1 |
|---|---|---|
| Gandal & Shy (2001), JIE, https://doi.org/10.1016/S0022-1996(00)00067-2 | Governments weigh domestic consumption and owned firms' earnings from international price competition; existing standard-union incentives and population asymmetry. | National-welfare optimization is standard **for governments**, but does not empirically describe ISO National Bodies. The distributional mechanism is partly inherited. |
| Barrett & Yang (2001), JIE, https://doi.org/10.1016/S0022-1996(00)00082-9 | Existing national technology can yield rational noncompliance with an international standard; governments may support noncompliance. | Incumbent opposition and national welfare tradeoffs are known; P1 must distinguish *network-intensity voting reversal* and the committee threshold. |
| Klimenko (2009), JIE, https://doi.org/10.1016/j.jinteco.2008.08.005 | Cross-border network effects and noncooperative standards/compatibility trade policies can create excess or insufficient compatibility. | Strategic technical compatibility due to national trade incentives is known, and some network comparative statics are known. |
| Goerke & Holler (1995), Public Choice | Voting rules can generate welfare divergence in network standardization decisions. | Supermajority-driven mismatch is not by itself novel. |
| Spulber (2019), Economic Journal, Proposition 6, https://doi.org/10.1111/ecoj.12606 | Voter interests and market power can align in a vertically connected SSO; some votes select efficient standard. | P1 uses horizontally competing firms and national representatives, so it does not contradict Spulber's theorem. The combination voting+market is already known. |
| Mattli & Büthe (2003), World Politics, https://doi.org/10.1353/wp.2004.0006; Büthe & Mattli (2011), book https://doi.org/10.23943/princeton/9780691144795.001.0001 | Global standards choices reflect national institutions and strategic domestic industry coordination, not solely neutral technical optimization; large national power is not identical to standard-setting influence. | Provides strong **motivation** for national-interest formation, not evidence that all ISO votes use the specific \(CS+\Pi\) objective. |
| Blind & von Laer (2022), Journal of Technology Transfer, https://doi.org/10.1007/s10961-021-09871-4 | Panel of 12 countries: ISO secretariat participation related to sector patenting/R&D; sector exports not a significant explanatory factor in their models. | This concerns *secretariat activity*, not final ballot votes. It warns against asserting that GDP/export size alone determines standardization influence. |
| Fiedler, Larrain & Prüfer (2023), Research Policy, article https://ideas.repec.org/a/eee/respol/v52y2023i6s0048733323000458.html | SSO participation, governance and lobbying; industry interests and membership incentives modeled. | Modeling industry-favoring voting rules is not inherently novel; treat domestic aggregation as robustness, not a main breakthrough. |

## 3. Separate national economic preferences from procedurally admissible ballots

**National preference:** \(U_i=\alpha_i CS_i+\beta_i\Pi_i\) with \(\alpha_i,\beta_i>0\), not necessarily social welfare; separate social evaluator \(W=\sum_i(CS_i+\Pi_i)-K\).

**Ballot admissibility:** Let \(t_i=1\) when a National Body opposing a proposal provides an admissible *technical* objection, and \(t_i=0\) otherwise. Under the P1 high-\(d\) candidate preferences, countries 1 and 3 vote yes and countries 0 and 2 prefer no. With \(m=t_0+t_2\) admissible negative votes, exclude unsupported negative votes per §§2.7.2–2.7.3, yielding \(2\) valid yes and \(m\) valid no ballots (4 P-members). The official dual ballot test becomes:
\[
\frac{2}{2+m}\ge\frac23,\qquad \frac{m}{2+m}\le\frac14.
\]
This **passes for \(m=0\)** and **fails for \(m=1,2\)**. Thus an ISO-specific failure requires at least **one genuine technically supported negative vote** among those two incumbents in this particular simple case. The current model provides *no technical reason* for their opposition: all brands' compatible-brand network quality increases and incumbents face no implementation cost. It only provides **competitive loss**. This is a major institutional validity gap, not a cosmetic wording issue.

Possible honest modeling remedies:
- **A: institutionally modest** — label the result "ISO-style one-country-one-vote approval game under economically motivated national preferences"; do not claim to fully explain actual FDIS voting.
- **B: technical-objection microfoundation** — introduce a substantive engineering-performance constraint/legacy-interface loss or a technically valid incompatibility issue, then prove a valid negative ballot can coexist with the P1 competition mechanism without trivializing it. Do not simply assume "profit loss is a technical objection".
- **C: earlier decision stage** — endogenize technical specification amendments and national positions at CD/DIS; recognize that comments/consensus and final-ballot admissibility differ. This is more realistic but a larger model.

## 4. A second major issue: approval-to-implementation cost discontinuity

P1-A assumes publication lowers implementation costs from \(k_H\) to \(k_L\), and then derives a *firm's endogenous adoption choice*. The firm's response is endogenous; the publication-induced cost change is an **exogenous primitive**.

ISO/IEC draft specifications are already developed, circulated and commented on at CD/DIS before formal issuance; a DIS satisfying approval criteria may bypass FDIS and proceed straight to publication. Hence the strong claim "technical interface information first becomes available after the final vote" is not institutionally valid as a general fact.

Better economic interpretation is that *final specification stability, adoption expectations, shared reference implementations, conformance tooling, or procurement coordination* changes expected returns to investment after formal standardization. But those changes are not automatic. The model must either (a) defend a reduced-form implementation-cost technology with institutional examples, or (b) endogenize investment/tool provision through fixed costs, scale economies and beliefs.

If \(k_L=k_H\) and the selected equilibrium is unchanged, ISO's vote can have **no structural causal effect** on adoption; do not claim otherwise.

## 5. Weighted-stakeholder robustness — closed form

For \(i=0,2\), generalize national delegate preferences:
\[
\Delta U_i=\alpha_i\Delta CS_i+\beta_i\Delta\Pi_i
=\frac{Nd}{144}\big[\alpha_i w_i(216-13d)-4\beta_i(d+6)\big].
\]
An incumbent supports the proposal iff
\[
\boxed{w_i\ge r_i\tau_o(d),\quad r_i=\beta_i/\alpha_i>0,\quad
\tau_o(d)=\frac{4(d+6)}{216-13d}.}
\]
Thus the original \(CS+\Pi\) voting is only \(r_i=1\), and the sign-reversal mechanism persists on an *open* range of market-share and stakeholder-weight configurations.

### Asymmetric countries (not necessarily the same sizes)

At \(w=(.12,.42,.13,.33)\), network intensities \(d_L=1/5\) and \(d_H=4/5\), a **common** \(r=\beta/\alpha\) in
\[
\frac{3341}{3400}<r<\frac{3201}{3100}
\]
ensures countries 0 and 2 switch from yes at \(d_L\) to no at \(d_H\). Country 1 supports at both values, and country 3 supports with the original strict private implementation-cost condition \(k_L<G_3<k_H\). This interval contains \(r=1\), showing robustness against small departures from national welfare aggregation. **The interval is finite but relatively narrow**; do not present it as proof of robustness for arbitrary lobbying weights.

### Symmetric countries: an additional conditional result

For \(w=(1/4,1/4,1/4,1/4)\) and \(r=\beta/\alpha=2\) (equal for every national delegate), with \(N=1,\ k_L=1/20,\ k_H=3/10\), the sincere approval votes are:

| \(d\) | countries supporting | official simplified 3-of-4 vote | actual world welfare gain if full interoperability |
|---|---|---|---|
| 1/5 | 0,1,2,3 | accepted | \(853/3600>0\) |
| 2/5 | 0,1,2,3 | accepted | \(112/225>0\) |
| 4/5 | 1,3 | rejected **only if technical negative comments qualify** | \(847/900>0\) |

The reversal holds for all \(r\) in
\[
\boxed{\frac{257}{136}<r<\frac{1067}{496}}
\]
at those two endpoints. This is not a population-asymmetry artifact: a delegate who puts relatively more emphasis on national exporters can oppose even when all national product markets are equal. But there is **no direct evidence** that ISO national positions systematically have \(r=2\), and the effect is a mechanically available extension of a known preference aggregation model. Treat as a *robustness result*, not confirmed innovation.

## 6. Assumption audit

| Current assumption | Economic modeling admissibility | Institutional fidelity | Disposition |
|---|---|---|---|
| Four nations, one national vote each | Normal reduced-form benchmark | Only the four-valid-vote final-ballot special case | Keep, clearly qualify |
| Market shares \(w_i\) arbitrary and sum to one | Strong and explicit | Use **sector-specific domestic demand** rather than total population | Keep, relabel |
| National delegate maximizes \(CS_i+\Pi_i\) | Standard benevolent national-representative benchmark, closely related to Gandal–Shy governments | Exact ISO body preference formation not guaranteed | Keep as benchmark; add \(\alpha_i,\beta_i\) as robustness |
| National no votes motivated solely by lost exporter profit | Rational positive economic model | **Insufficient for valid ISO technical negative vote** | **Must fix or narrow claims** |
| ISO approval alone reduces interface implementation cost | Valid explicitly conditional structural comparison | No automatic technical secrecy/cost decline at final vote; drafts already available | **Needs microfoundation or explicit limitation** |
| Three incumbent firms have existing interoperability, one isolated | Standard coordination / installed-base simplification | Requires credible historical/proprietary origins | Keep with motivation |
| Network gain equals compatible **brand count** | Valid variety/network-scope effect | Not a standard installed-base user-count externality | Keep but do not overgeneralize |
| Strict equilibrium exists after each ballot outcome | Theoretically valid existence statement | Multiple potential coordination equilibria can coexist | Keep; do not claim unique prediction |
| Three-of-four votes is “ISO” | Correct only under four P-member valid yes/no ballots | NP participation, CD consensus, DIS other ballots, FDIS technical reasons omitted | Say **ISO-style final ballot**, not full institutional replication |

## 7. Novelty and publishing decision

- **Mathematical consistency:** Existing P1 price and vote derivations remain credible, conditional on price-adoption continuation and institutional primitives. Weighted-preference extensions are algebraic and verified in Python.
- **Institutional validity:** The *core interest-driven preferences* are reasonably motivated, but the final-ballot mechanism is **materially underspecified** when negative votes require technical comments. This is the most important factual limitation.
- **Novelty:** Interest aggregation, strategic regulatory national policy, rational incumbent incompatibility, voting/market interaction, and SSO lobbying are all known separately. P1's country-specific network-intensity cutoffs are not yet confirmed to add a general new mechanism. A theorem-level first-in-literature conclusion cannot be asserted.
- **Publication:** Current result is suitable for a research working paper and a continued specialist-journal feasibility test. An actual **ISO-FDIS-motivated RIO paper** needs a valid-negative-vote channel and credible cost implementation mechanism; not just more market-share algebra.

## 8. Minimum revision recommendation

Do **not** rebuild a many-country model immediately. Instead:
1. Retain baseline welfare objectives but describe them as national-representative preferences, not literal governmental control of ISO.
2. Recast \(n_i\) as sector-level product-market size.
3. Formalize the technical grounds for negative votes, or expressly restrict the paper to an ISO-inspired approval institution.
4. Replace "ISO approval reveals interface" by an issuance-dependent *investment or credibility* story, backed by sources.
5. Retain the fully closed-form population and stakeholder-weight robustness theorems as supplemental results.
6. Compare the exact theorem with Goerke–Holler, Spulber, Gandal–Shy, Barrett–Yang, and Klimenko; do not present a mere symbolically new threshold as proof of intellectual originality.

**Verdict:** The market-interest-to-national-preference abstraction is defensible. The national-preference-to-valid-final-ISO-vote mapping remains the central institutional gap. The source-to-adoption-cost mapping is the second gap. Solve these before declaring RIO-level publishability.
