#!/usr/bin/env python3
"""Validate example_knowledge_graph.ttl with SHACL shapes.

Usage::
    python validate_example_graph.py [data] [shapes]

If arguments are omitted, the script defaults to:
    data   = Example/example_knowledge_graph.ttl
    shapes = Example/example_knowledge_graph_shapes.ttl

Exit status is non-zero when validation fails.
"""
from pathlib import Path
import sys
import argparse

from rdflib import Graph
from pyshacl import validate


def main():
    parser = argparse.ArgumentParser(description="Validate a Turtle knowledge graph using SHACL shapes.")
    parser.add_argument("data", nargs="?", default="Example/example_knowledge_graph.ttl",
                        help="Path to the data graph (TTL/RDF file)")
    parser.add_argument("shapes", nargs="?", default="Example/example_knowledge_graph_shapes.ttl",
                        help="Path to the SHACL shapes graph")
    args = parser.parse_args()

    data_path = Path(args.data).resolve()
    shapes_path = Path(args.shapes).resolve()

    if not data_path.exists():
        print(f"[ERROR] Data graph not found: {data_path}", file=sys.stderr)
        sys.exit(2)
    if not shapes_path.exists():
        print(f"[ERROR] SHACL shapes file not found: {shapes_path}", file=sys.stderr)
        sys.exit(2)

    print("[INFO] Loading data graph …")
    data_graph = Graph().parse(str(data_path))
    print(f"        Loaded {len(data_graph):,} triples from {data_path.name}")

    print("[INFO] Loading SHACL shapes graph …")
    shapes_graph = Graph().parse(str(shapes_path))
    print(f"        Loaded {len(shapes_graph):,} triples from {shapes_path.name}")

    print("[INFO] Running SHACL validation …")
    conforms, results_graph, results_text = validate(
        data_graph,
        shacl_graph=shapes_graph,
        advanced=True,
        inplace=True,
        debug=True,  # Enable debug for detailed tracing of new UCO shapes
    )

    if conforms:
        print("\n✅ Validation passed – data graph conforms to all SHACL shapes.")
        # Add quick UCO-specific check (query for actions without performers)
        uco_action_query = """
        PREFIX uco-action: <https://ontology.unifiedcyberontology.org/uco/action#>
        SELECT ?action WHERE {
            ?action a uco-action:Action .
            FILTER NOT EXISTS { ?action uco-action:performer ?performer }
        }
        """
        missing_performers = list(data_graph.query(uco_action_query))
        if missing_performers:
            print("⚠️ Warning: All shapes passed, but some UCO actions lack performers (check narrative mappings).")
        sys.exit(0)
    else:
        print("\n❌ Validation FAILED – data graph does not conform. Details:\n")
        print(results_text)
        # Also save detailed results report
        report_file = data_path.with_suffix(".shacl-report.ttl")
        results_graph.serialize(destination=str(report_file), format="turtle")
        print(f"Detailed report written to {report_file}")
        sys.exit(1)


if __name__ == "__main__":
    main() 