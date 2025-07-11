# Ontology Cheatsheet for DFRWS USA 2025 Forensic Rodeo

This cheatsheet summarizes key classes and properties from UCO, CASE, and CAC ontologies. Use it to map your narrative to RDF/Turtle quickly. For full details, check the TTL files in `/UCO-Official`, `/CASE`, and `/CAC-Ontology`.

## UCO (Unified Cyber Ontology) – Foundational Cyber Elements
- **Key Modules**: `core.ttl` (basics), `observable.ttl` (digital artifacts), `action.ttl` (events), `role.ttl` (actors).
- **Common Classes**:
  - `uco-core:Role`: For actors (e.g., Investigator, Victim).
  - `uco-observable:File`: Represents files/devices with hashes.
  - `uco-action:Action`: Tracks actions with provenance (who/what/when).
- **Example**: Link a file to an action: `<file1> a uco-observable:File ; uco-core:hasFacet [ a uco-action:ActionResult ] .`

## CASE (Cyber-investigation Analysis Standard Expression) – Evidence Provenance
- **Key Modules**: `investigation.ttl` (lifecycle), `vocabulary.ttl` (terms).
- **Common Classes**:
  - `case-investigation:InvestigativeAction`: Models steps like evidence collection.
  - `case-investigation:ProvenanceRecord`: Tracks chain-of-custody.
- **Example Integration**: Combine with UCO: `<action1> a case-investigation:InvestigativeAction ; uco-action:instrument <tool1> .`

## CAC (Crimes Against Children) Ontology – ICAC-Specific
- **Key Modules**: `icac-core.ttl` (basics), `icac-investigation-coordination.ttl` (task forces), `icac-physical-evidence.ttl` (artifacts), `icac-temporal-gufo.ttl` (timelines), and specialized ones like `icac-sextortion.ttl`.
- **Common Classes**:
  - `icac:HotlineReport`: For tips (e.g., NCMEC CyberTips).
  - `icac:Investigation`: Full case with phases.
  - `icac:VictimImpactAssessment`: For assessing harm.
- **Example Integration**: With UCO/CASE: `<report1> a icac:HotlineReport ; case-investigation:performer <investigator1> ; uco-location:location <usa> .`

## Tips for Interconnections
- Start with CAC for scenario specifics, layer in CASE for provenance, and UCO for cyber details.
- Common Pattern: `<entity> a cac:Class ; uco-core:role [ a uco-core:Role ] ; case-investigation:instrument <tool> .`
- Temporal: Use CAC's GUFO integration for events over time (e.g., `gufo:participatesIn`).

For more, explore examples in `/CAC-Ontology/ontology/icac/examples/`.
