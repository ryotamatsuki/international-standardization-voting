# Empirical implementation and ISO data feasibility audit
Checked 2026-11-09; **verification of public metadata/schema only, not an extracted firm microdata panel and not an empirical causal study**.

## Outcome tiers must remain distinct
1. International technical specification created/published (ISO stage).
2. Domestic national standards adoption/transposition (national catalogue).
3. Private implementation and specific OPTIONAL certification profile obtained (OCA firms/products).
4. Actual functional cross-vendor interoperability (pairwise vehicle x charger, messaging network-to-network).
5. Ultimate trade/entry/volume/consumer welfare.
Neither 1 nor 2 is a substitute for 3 or 4.

## Official sources checked
**ISO Open Data:** https://www.iso.org/open-data.html offers deliverables and technical committee metadata in CSV/Parquet/JSONL. Deliverables fields: unique id, reference, publicationDate, edition, currentStage, replaces/replacedBy, ICS, ownerCommittee, and scope. TC fields include P-/O-member country standard bodies and secretariat. **No project-by-country DIS/FDIS ballots or vendor implementation** in published documented schemas. CSV link confirmed, however the tool returned an unsupported octet-stream and independent container download failed; therefore **raw rows were not extracted/verified**. Metadata licensed ODC-By with attribution; proprietary full ISO standards texts are not covered by the same license.

**ISO/IEC Directives 2026:** https://assets.iec.ch/sd/ISO-IEC_Directives_Part-1_2026.html ; valid negative ballot, committee P-members and all-member thresholds must not be collapsed into government vote. Formal consensus is not identical to 100% yes and FDIS may be skipped. Publication and implementation separate.

**Open Charge Alliance OCPP 2.0.1 certification:** https://openchargealliance.org/certificationocpp/certification-ocpp-2-0-1/ . Mandatory Core; optional Advanced Security, Smart Charging and ISO 15118 Support. Expanded full certification announced April 2, 2025: https://openchargealliance.org/ocpp-2-0-1-full-certification-is-now-available/ . Actual posted certification fees differ by membership and charging-system versus station type: high-certification cost microfoundation is grounded as a margin but **engineering compliance costs cannot be equated with OCA fees**.

**Public certified products index:** https://openchargealliance.org/certified-companies/ . Page publicly displays organization, certificate number, country, product designation, product type, software version, date of registration, and certification profile flags S,L,C,D,R,U,I (I=ISO 15118 support). "Export to Excel" control is visible. The web text view exposes schema but dynamically loaded actual product rows and binary export were not returned; **not yet a certified reproducible dataset**. Need check export usability, terms and exact temporal history; repeated certificates for product families and brands create selection/composition bias. This is an OCA (industry consortium) source with an optional ISO-related feature, NOT an ISO national ballot sample.

**OCA version-compatibility:** official https://openchargealliance.org/faq/ : OCPP 1.6 and 2.0.1 incompatible; 2.1 backward compatible with 2.0.1. Dates and versions matter for any study. OCA certification is of a specific protocol version, not proof of cross-version interoperability.

**ISO 15118:** ISO/PAS 15118-23:2026 test case framing distinguishes compliance/conformance and pairwise interoperability involving application logic. ISO 15118-20 is core EV/EVSE communication, but not all charging vendors have the corresponding optional certified OCPP support. Official ISO OBP https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso%3Apas%3A15118%3A-23%3Aed-1%3Av1%3Aen .
**VOLTS:** https://www.energy.ca.gov/publications/2025/vehicle-interoperability-testing-symposium-volts . 2023 industry cross-vendor EV/EVSE testing event and 2025 public California report. It confirms that tests occurred; micro-level pairwise pass/fail outcomes and participant identifiers have not been shown public.

**Cross-border outcomes:** WTO ePing regulatory notices https://data.wto.org/en/dataset/ext_eping ; national trade data UN Comtrade https://comtradeapi.un.org/ ; standards-type ICS↔trade HS mapping many-to-many and often noisy. Cannot infer ISOballot behavior from WTO TBT notice.

## Observable implications derived from the diagnostic optional profile model
Defined on an actual optional-profile universe; not automatic causal implications:
- Conditional on firms' implementation cost distribution and market benefits, more technically demanding profiles may show a **lower fraction of support-certified products**, despite greater functionality conditional on full support.
- If the independent-pair assumption is valid, the predicted effective cross-vendor *profile* coverage is proportional to profile breadth *square* of certified support share, not the count of Core-compliant products.
- Near a dense cluster of engineering cost thresholds, profile coverage can decline sharply with breadth; in settings with low density at the relevant cost cutoff it need not.
- A prospective test: compare *within protocol version and product subtype* profile incidence over revisions, accounting for product family certification, vendor, country, certification type, market demand, safety regulations and rollout. Merely plotting share versus s does not identify a causal effect.
- **Negative control:** mandatory Core alone is insufficient proxy for advanced feature interoperability. Certified profile flags may not guarantee successful pairwise functional operation.

## Counterfactual threats and feasibility status
1. Vendor certification decisions jointly influenced by buyer demand/mandates; no exogenous choice of s. Causal inference needs credible shock to optional module breadth or accreditation rules, and difference-in-differences/event-study is NOT justified until treatment and pretrends verified.
2. Actual breadth/complexity s must be objectively constructed from feature dependencies/conformance test counts and licensing; proprietary technical source copyright may limit automated parsing.
3. OCA publicly lists certificates, not installed product shares or deployed base; equal-weight vendor certificate fraction ≠ market interoperability.
4. Public CEC event summary cannot yet estimate pairwise success without case-level data.
5. More recent Bonani (2026), Bianchi et al (2026), Lessmann–Yao (2026) already cover important innovation/usage outcomes; simple standards adoption-trade association not new.

## Feasibility conclusion
**Potential proxy verified: optional-profile certification schema [YES]. Raw OCA rows/export [NOT TESTED]. Direct interoperability dependent variable [NOT VERIFIED]. ISO TC and deliverables data schema [YES]; raw downloadable bytes [NOT TESTED].** Therefore a credible observational descriptive pilot is possible in principle but not presently complete; causal empirical implementation not yet established.
