# DFRWS USA Forensic Rodeo 2024
## Challenge Track: “Zen and the Art of Knowledge Graphs for Law Enforcement Investigations, Operations, and Digital Forensics”

### 1  Objective
Model a complete child-protection investigation—from hotline tip to final technical findings—using semantic ontologies.
Participants will:

1. **Represent the investigation** in a Turtle (`.ttl`) knowledge graph that captures:
   • people, tools, artefacts, locations, legal instruments, and procedures;  
   • every lifecycle phase:
     – hotline receipt (e.g., NCMEC CyberTip),  
     – ICAC task-force intake and investigation,  
     – phased undercover operation,  
     – digital-forensics examination, and  
     – presentation of results.
2. **(Bonus)** Build a simple UI that auto-generates the undercover-operation plan.

### 2  Permitted Technologies
• Ontologies  
  – Unified Cyber Ontology (UCO)  
  – CASE Ontology  
  – Experimental Crimes Against Children (CAC) ontology family  
• Any additional tooling you need is allowed

### 3  What to Submit
1. **Knowledge graph** — single Turtle file (`your_team.ttl`).  
   • Must be readable by any RDF-compliant tool.  
   • Should support ChatGPT (or similar) reconstructing the narrative in plain English.  
   • Perfection is not required; clarity and correct ontology usage matter most.
2. **(Bonus) UI demo** — lightweight app that produces the undercover-operation plan from your graph.  
   Show it to a Forensic Rodeo judge for extra points.

### 4  Scoring Highlights
• Coverage of all investigative phases and entities  
• Correct, consistent ontology usage  
• Readability of the graph (can another team query it and understand the story?)  
• Bonus points for the UI generator

### 5  Background References
#### Unified Cyber Ontology (UCO)
Community-developed foundation for cyber-security information. Sub-domain models (threat intel, incident response, etc.) extend UCO so data can flow seamlessly across tools and teams.

#### CASE Ontology
Specifies how to represent digital-evidence information during investigations. Tracks provenance (who, what, when, where) and enables automated combination and validation of heterogeneous tool outputs.

#### Crimes Against Children (CAC) Ontology Family
Experimental framework for Internet Crimes Against Children (ICAC) and child-sex-trafficking investigations. Modules cover:
• production cases,  
• custodial relationships,  
• victim-impact assessment,  
• ICAC task-force operations, and  
• international coordination (leveraging ICMEC partnerships with 120 + countries).

The CAC family supplies standard vocabularies so agencies, researchers, and technology partners can share, analyse, and coordinate child-protection data worldwide.

---

### 6  Walk-through Example (`/Example` folder)
The `Example/` directory contains a fully-worked reference that shows the **minimum deliverables** working together.  Review it, then replace it with your own artefacts:

| File | Purpose |
| ---- | ------- |
| `wa_icac_2024_master_001_narrative.md` | A prose narrative (~9 000 words) describing every step of an ICAC investigation.  Use it as a template to write **your own original scenario** (it can be shorter). |
| `semantic_mappings.md` | A human-readable table that links narrative entities (people, devices, warrants …) to IRIs and ontology classes.  Start here after you draft your narrative. |
| `example_knowledge_graph.ttl` | RDF/Turtle implementation of the narrative using UCO, CASE and CAC ontologies.  Build your own graph from your narrative + mappings. |
| `example_knowledge_graph_shapes.ttl` | SHACL shapes that define the **minimum semantic constraints** (e.g., every `File` needs a hash).  Adapt or extend this for your domain. |
| `validate_example_graph.py` | Python script that runs `pyshacl` to validate the graph against the shapes.  Use it—or your own variant—to test your submission. |

#### Recommended Workflow for Participants
1. **Draft a unique narrative** (or adapt an existing case) that covers the required investigation phases.
2. **Create a semantic-mapping document** that enumerates all IDs and ontology classes you will use.
3. **Build the knowledge graph** in Turtle, conforming to UCO/CASE/CAC terms.
4. **Write a SHACL shapes file** that encodes the rules your graph must satisfy.
5. **Develop a validation script** (Python, Bash, Makefile …​) to run the SHACL check automatically.
6. Iterate until your script reports that the graph **conforms**.

Feel free to borrow patterns from the example files, but your final submission should be based on **your own narrative and data**.