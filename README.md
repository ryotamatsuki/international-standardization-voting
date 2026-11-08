# International Standardization Voting

**Research repository — preliminary theory (2026-11-08).**

This project studies how an ISO-style one-country/one-vote approval stage interacts with international product-market rivalry, network externalities, and voluntary compatibility adoption. The baseline is **Gandal & Shy (2001), _Standardization Policy and International Trade_**.

**Research status: exploratory; no journal submission or confirmed novelty claim.** The main candidate result (P1, *Network-Driven Voting Reversal*) has symbolic calculations and a conditional voluntary-adoption mechanism. A complete multi-stage ISO process, general equilibrium uniqueness, and independence from prior results remain open.

## Repository map

- [Literature history (Japanese)](literature/history_1985_2026_ja.md): chronological development and connection to this project
- [Bibliography and novelty matrix](literature/bibliography_and_novelty.md): verifiable sources, direct comparison, open checks
- [Model and hypotheses](theory/model_and_hypotheses.md): P1/P2/P3, definitions, equations, statuses
- [P1 proof and adoption note](proofs/p1_conditional_adoption.md): conditions, derivations, limitations
- [Numerical and symbolic scripts](code/): reproducible SymPy scripts
- [Research log](research_log/2026-11-08_initial_assessment.md): achievements, caveats, journal strategy, next gates

## What is established, and what is not

- **Established algebraically in the specified candidate-price model:** a voting reversal threshold (d^*=48/139) for a four-country market-size vector ((0.12,0.50,0.12,0.26)), while conditional full compatibility raises world welfare.
- **Conditional continuation:** publication reduces a firm's implementation cost from (k_H) to (k_L); the firm then privately chooses compatibility when (k_L<G_3(d)<k_H). Cost reduction is an **assumption**, not proved from ISO institutional rules.
- **Not yet independently certified:** complete global price-game proof, uniqueness/selection of all adoption subgames, exact ISO NP/CD process, novelty relative to Spulber (2019), Barrett & Yang (2001), and Klimenko (2009).

**Institutional scope:** final DIS/FDIS-style ballot with four P-members and four valid yes/no votes (3 yes required). This is **not** a faithful full reproduction of ISO's project-initiation and consensus process.

## Reproduction

Requires Python 3.12+ and SymPy.

```bash
python -m pip install sympy
python code/p1_iso_verification.py
python code/p1_iso_endogenous_adoption.py
```

These are symbolic checks and scenario tests, **not** formal machine-checked proofs of all assumptions.

## Source and attribution

Cite the underlying journal articles, not this working repository, for established literature results. Original analyses herein are provisional research notes. No publisher PDFs are redistributed.

Primary sources:
- [Gandal & Shy (2001)](https://doi.org/10.1016/S0022-1996(00)00067-2)
- [ISO/IEC Directives Part 1 (2026)](https://www.iso.org/sites/directives/current/consolidated/)
- [Spulber (2019)](https://doi.org/10.1111/ecoj.12606)

See the dated research log for the next tests and publication-tier criteria.
