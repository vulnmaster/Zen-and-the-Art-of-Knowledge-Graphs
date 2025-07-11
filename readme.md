# DFRWS USA Forensic Rodeo 2025
## Challenge Track: “Zen and the Art of Knowledge Graphs for Law Enforcement Investigations, Operations, and Digital Forensics”

### 0  Getting Started
To begin, clone this template repository and set up a Python virtual environment:

```bash
# 1) Clone the repo (use your own fork or clone directly)
 git clone https://github.com/vulnmaster/Zen-and-the-Art-of-Knowledge-Graphs.git
 cd Zen-and-the-Art-of-Knowledge-Graphs

# 2) Create a virtual environment (optional but recommended)
 python -m venv .venv
 source .venv/bin/activate       # Windows: .venv\Scripts\activate

# 3) Install the minimal dependencies
 pip install -r requirements.txt

# 4) Run the validator on the example graph
 python Example/validate_example_graph.py
```

You should see a ✅ **Validation passed** message.  This confirms your environment is ready.  From here you can begin replacing the example artefacts with your own.

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

### Quick Start Tutorial
If you're new to RDF/Turtle or these ontologies, try this mini-example to model just the "hotline receipt" phase before tackling the full challenge.

1. **Draft a Simple Narrative**: Create a file `my_mini_narrative.md` with: "A hotline receives a CyberTip from NCMEC about suspected CSAM on a device."
2. **Map to Ontologies**: In a file `my_mini_mappings.md`, note: Entity "CyberTip" → IRI `<http://example.org/cybertip1>`, Class `icac:HotlineReport` (from CAC).
3. **Build a Mini Graph**: Create `my_mini_graph.ttl`:
   ```
   @prefix icac: <http://example.org/icac-core#> .
   @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

   <http://example.org/cybertip1> a icac:HotlineReport ;
       icac:reportDate "2025-01-01"^^xsd:date ;
       icac:source "NCMEC" .
   ```
4. **Validate It**: Use SHACL (adapt from `Example/example_knowledge_graph_shapes.ttl`) and run a script like `validate_example_graph.py` on your mini files. If it passes, you've captured your first "flag"!

This warm-up covers basics—scale it up for the full investigation.

### 2  Permitted Technologies
• Ontologies  
  – Unified Cyber Ontology (UCO)  
  – CASE Ontology  
  – Experimental Crimes Against Children (CAC) ontology   
• Any additional tooling you **think** you need is allowed

### 3  What to Submit
1. **Knowledge graph** — single Turtle file (`your_team.ttl`).  
   • Must be readable by any RDF-compliant tool.  
   • Should support ChatGPT (or similar) reconstructing the narrative in plain English.  
   • Perfection is not required; clarity and correct ontology usage matter most.

### 4  Scoring Highlights
• Coverage of all investigative phases and entities  
• Correct, consistent ontology usage  
• Readability of the graph (can another team query it and understand the story?)  

**Scoring Checklist** (aim for 100 points):
- [ ] Covers all phases (hotline, intake, operation, forensics, presentation) – 20 points
- [ ] Uses at least one class/property from UCO, CASE, and CAC – 20 points
- [ ] Graph supports 3+ SPARQL queries (e.g., "List forensic tools" – see examples in `/Example/example_SPARQL_queries/`) – 20 points
- [ ] Passes SHACL validation with no errors – 20 points
- [ ] Includes a custom "flag" (e.g., a hashed value modeled in the graph) – 20 points (bonus for creativity)

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
The `Example/` directory contains a fully-worked reference that shows the **minimum deliverables** working together.  Review it, then replace it with your own artifacts:

| File | Purpose |
| ---- | ------- |
| `wa_icac_2024_master_001_narrative.md` | A prose narrative (~9 000 words) describing every step of an ICAC investigation.  Use it as a template to write **your own original scenario** (it can be shorter). |
| `semantic_mappings.md` | A human-readable table that links narrative entities (people, devices, warrants …) to IRIs and ontology classes.  Start here after you draft your narrative. |
| `example_knowledge_graph.ttl` | RDF/Turtle implementation of the narrative using UCO, CASE and CAC ontologies.  Build your own graph from your narrative + mappings. |
| `example_knowledge_graph_shapes.ttl` | SHACL shapes that define the **minimum semantic constraints** (e.g., every `File` needs a hash).  Adapt or extend this for your domain. |
| `validate_example_graph.py` | Python script that runs `pyshacl` to validate the graph against the shapes.  Use it—or your own variant—to test your submission. |
| `generate_graphviz.py` | Utility to convert a Turtle graph to GraphViz DOT/PNG for interactive visual exploration. |

#### Recommended Workflow for Participants
1. **Draft a unique narrative** (or adapt an existing case) that covers the required investigation phases.
2. **Create a semantic-mapping document** that enumerates all IDs and ontology classes you will use.
3. **Build the knowledge graph** in Turtle, conforming to UCO/CASE/CAC terms.
4. **Write a SHACL shapes file** that encodes the rules your graph must satisfy.
5. **Develop a validation script** (Python, Bash, Makefile …​) to run the SHACL check automatically.
6. Iterate until your script reports that the graph **conforms**.

Feel free to borrow patterns from the example files, but your final submission should be based on **your own narrative and data**.

### Troubleshooting Common Issues
- **Namespace Conflicts**: Ensure prefixes match ontology files (e.g., CAC uses `icac:` – check `icac-core.ttl`).
- **Validation Fails**: If SHACL reports errors, verify required properties (e.g., every `uco-observable:File` needs a `uco-types:Hash`).
- **Querying the Graph**: Use tools like rdflib in Python; if stuck, load into GraphDB for visual queries.
- **Overwhelmed by Ontologies?**: See `ontology_cheatsheet.md` for summaries.

### Visualizing the example knowledge graph

You can export `Example/example_knowledge_graph.ttl` to GraphViz (DOT) – and optionally PNG – using the helper script:

```bash
# Activate venv first
. .venv/Scripts/activate  # Windows PowerShell

python Example/generate_graphviz.py Example/example_knowledge_graph.ttl \
  --png Example/example_knowledge_graph.png
```

* A `.dot` file is always produced (same basename by default).
* If GraphViz’s `dot` executable is on your PATH, a PNG (or SVG) is rendered automatically; otherwise you can open the DOT file in any graph viewer.

The script truncates very large graphs to the first 2,000 triples for readability – use `--max-triples` to change that.

> **Tip – GraphViz install**  
> • Windows: Download from https://graphviz.org/download/ and ensure `dot.exe` is in your `PATH`.  
> • macOS: `brew install graphviz`  
> • Linux: `sudo apt install graphviz` (or distro equivalent).
>
> After installation you can also render manually:
>
> ```bash
> dot -Tsvg Example/example_knowledge_graph.dot -o graph.svg
> ```
>
> – Use SVG for scalable, zoom-friendly diagrams; PNG for quick screenshots.
>
> **Viewing options**  
> • Any browser opens the generated `.svg` directly.  
> • VS Code has a built-in DOT preview extension.  
> • Gephi or yEd can import the `.dot` file for interactive exploration.