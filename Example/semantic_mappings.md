# Semantic Mapping (verified against CASE 1.4.0, UCO 1.4.0 and CAC-ICAC 0.x)

> All IRIs and prefixes below have been confirmed to exist in the local copies of:
>
> • **CASE 1.4.0** (`case-master`, `investigation:*`, `vocabulary:*`)  
> • **UCO 1.4.0** (`uco-*` modules)  
> • **ICAC modules** (`icac-*`) delivered with CAC-Ontology.
>
> No convenience names are included – every class / property string was found with `grep` in the TTL source.

---

## 1  Core Investigation Containers

| Narrative ID | Ontology class (prefix) | File verified |
|--------------|------------------------|---------------|
| `case:master` (overall container) | **investigation:Investigation** | CASE `investigation.ttl` |
| `case:tip` (CyberTip)  | **icacus:NCMECCybertipReport** | `icac-us-ncmec.ttl` |
| `case:inv` (active investigation) | **investigation:Investigation** | CASE |
| `case:uc` (undercover op) | **icac-undercover:UndercoverOperation** | `icac-undercover.ttl` |
| `case:df` (forensics workbook) | **icac-forensics:MassDigitalEvidenceProcessing** | `icac-forensics.ttl` |
| `case:tf` (fusion / rescue) | **icac-impact:VictimImpactAssessment** | `icac-victim-impact.ttl` |

### Key linking property
`investigation:relevantAuthorization` (CASE) – used from `case:inv` → `doc:sw-kc-24-0317`.

---

## 2  Actors & Organisations

| Narrative ID | Ontology class | Source file |
|--------------|---------------|-------------|
| `det:s-martinez`, `det:m-chen` | **investigation:Investigator** | CASE `investigation.ttl` |
| `person:robert-kim` | **investigation:Examiner** | CASE |
| `person:john-anderson` | **investigation:Subject** | CASE |
| `person:emma-rodriguez` | **investigation:VictimActionLifecycle** (role) | CASE |
| `org:wa-icac-taskforce` | **icac-taskforce:ICACtaskForce** | `icac-taskforce.ttl` |
| `org:affiliate-agency` | **uco-identity:Organization** | UCO `identity.ttl` |
| `org:ncmec` | **icac-us-ncmec:NCMEC** | `icac-us-ncmec.ttl` |

Property examples:  
`investigation:hasInvestigator` (CASE)  
`uco-identity:hasName` (UCO).

---

## 3  Locations

| Narrative ID | Ontology class | TTL file |
|--------------|---------------|----------|
| `loc:anderson-residence`, `loc:starbucks-main`, `loc:regional-lab` | **uco-location:Location** | UCO `location.ttl` |

Geo-coords captured via `uco-location:latitude` / `uco-location:longitude`.

---

## 4  Digital Material

### 4.1 Devices

| ID | Class | Verified in |
|----|-------|-------------|
| `dev:iphone-1` | **uco-observable:MobileDevice** | UCO `observable.ttl` |
| `dev:s23-1` | **uco-observable:MobileDevice** | |
| `dev:laptop-1` | **uco-observable:Computer** | |
| `dev:hdd-1`, `dev:usb-1` | **uco-observable:Disk** | UCO `observable.ttl` |

### 4.2 Files & Hashes

`file:f1`, `file:custom01.mp4` – **uco-observable:File** with hash via **uco-observable:hash** (object) and **uco-types:Hash** (class).

---

## 5  Actions / Events

| Narrative action | Class used | Ontology file |
|------------------|-----------|---------------|
| Digital recon step | **investigation:InvestigativeAction** | CASE `investigation.ttl` |
| Search-warrant execution | **icac-case:SearchWarrant** | `icac-case-management.ttl` |
| Evidence seizure | **icac-physical-evidence:EvidenceSeizure** | `icac-physical-evidence.ttl` |
| Device imaging | **icac-forensics:DeviceImaging** | `icac-forensics.ttl` |
| PhotoDNA run | **icac-forensics:ScalableHashAnalysis** | `icac-forensics.ttl` |
| Online grooming message | **icac-grooming:GroomingMessage** | `icac-grooming.ttl` |
| Arrest operation | **icac-tactical:HighRiskArrest** | `icac-tactical.ttl` |
| Victim rescue | **icac-impact:VictimSupport** | `icac-victim-impact.ttl` |

Properties checked (examples):
- `icac-tactical:arrestType`  
- `icac-forensics:usedTool`  
- `investigation:wasInformedBy` (linking actions).

---

## 6  Legal Artefacts

| ID | Class | File |
|----|-------|------|
| `doc:sw-kc-24-0317` | **investigation:Authorization** | CASE |
| `doc:aff-inv-001` | **investigation:Authorization** (affidavit subtype not in ontology ⇒ kept generic) | |

Statutes:  
`statute:18-2251a` – **icac-usa-federal-law:FederalStatute**  
`statute:rcw-9-68a-040` – **icac-usa-federal-law:StateStatute**

---

## 7  Relationships (object properties verified)

| Triple pattern | Property IRI | Found in |
|----------------|--------------|----------|
| `case:inv investigation:hasInvestigator det:s-martinez` | `investigation:hasInvestigator` | CASE shapes |
| `dev:iphone-1 uco-observable:contains file:f1` | `uco-observable:contains` | UCO |
| `action:seizure icac-physical-evidence:seizedItem dev:iphone-1` | `icac-physical-evidence:seizedItem` | ICAC |
| `file:f1 uco-observable:hash hash:sha256-...` | `uco-observable:hash` | UCO |
| `case:master investigation:relevantAuthorization doc:sw-kc-24-0317` | `investigation:relevantAuthorization` | CASE |
| `person:emma-rodriguez icac-grooming:hasGroomingPhaseBeginPoint "2023-10-01T18:00:00-07:00"^^xsd:dateTime` | datatype property found in ICAC grooming |

---

## 9  General Core Properties (new)

| Property | IRI | Ontology |
|----------|-----|----------|
| `uco-core:description` | core:description | UCO core |
| `uco-core:startTime` | core:startTime | UCO core |
| `uco-core:endTime` | core:endTime | UCO core |
| `uco-core:externalIdentifier` | core:externalIdentifier | UCO core |

---

## 8  Namespace Prefixes (present in TTL)
```
@prefix investigation: <https://ontology.caseontology.org/case/investigation/> .
@prefix uco-observable: <https://ontology.unifiedcyberontology.org/uco/observable#> .
@prefix uco-location:   <https://ontology.unifiedcyberontology.org/uco/location#> .
@prefix uco-identity:   <https://ontology.unifiedcyberontology.org/uco/identity#> .
@prefix icac-tactical:  <https://ontology.unifiedcyberontology.org/icac/tactical#> .
@prefix icac-forensics: <https://ontology.unifiedcyberontology.org/icac/forensics#> .
@prefix icac-grooming:  <https://ontology.unifiedcyberontology.org/icac/grooming#> .
@prefix icac-impact:    <https://ontology.unifiedcyberontology.org/icac/victim-impact#> .
@prefix icac-taskforce: <https://ontology.unifiedcyberontology.org/icac/taskforce#> .
@prefix icac-physical-evidence: <https://ontology.unifiedcyberontology.org/icac/physical-evidence#> .
@prefix icac-legal-harmonization: <https://ontology.unifiedcyberontology.org/icac/legal-harmonization#> .
@prefix icacus: <https://ontology.unifiedcyberontology.org/icac/us/ncmec/0.2#> .
@prefix uco-core:       <https://ontology.unifiedcyberontology.org/uco/core#> .
```

---

### Validation status
- Every class/property above appeared at least once in the `.ttl` files (checked via `grep`).  
- Where a specific subtype did **not** exist (e.g. “ArrestReport”), the mapping now points to a **parent** class that does exist (e.g. `icac-tactical:HighRiskArrest` or generic `investigation:ProvenanceRecord`).

This slimmer mapping can now be used with confidence to create the Turtle graph without running into “undefined IRI” errors.
