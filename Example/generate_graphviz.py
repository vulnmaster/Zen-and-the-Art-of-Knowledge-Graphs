#!/usr/bin/env python3
"""generate_graphviz.py

Convert a Turtle knowledge graph into a GraphViz DOT representation (and optionally render
it to PNG/SVG if the `dot` executable from GraphViz is available).

Usage::

    python generate_graphviz.py example_knowledge_graph.ttl  [-o graph.dot] [--png graph.png]

If -o/--output is omitted, a file with the same basename and `.dot` extension will be
created alongside the input TTL file.

The script tries to shorten IRIs to QName prefixes using the graph's namespace manager;
if a QName is not available it falls back to the local part after the last `/` or `#`.
It excludes `rdf:type` triples to reduce clutter.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF

try:
    import pydot  # type: ignore
except ImportError as e:
    print("Error: pydot is required. `pip install pydot`", file=sys.stderr)
    raise

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def qname_or_curie(graph: Graph, term: URIRef | Literal) -> str:
    """Return a compact representation for a URIRef/Literal for node labels."""
    if isinstance(term, Literal):
        return str(term)  # plain literal
    try:
        return graph.namespace_manager.normalizeUri(term)
    except Exception:
        # Fallback to last fragment or path segment
        s = str(term)
        return s.split("#")[-1].split("/")[-1]


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def build_dot(graph: Graph) -> "pydot.Dot":
    dot_graph = pydot.Dot("knowledge_graph", graph_type="digraph", rankdir="LR")

    # Add nodes and edges
    for s, p, o in graph:
        if p == RDF.type:
            continue  # skip rdf:type for visual clarity

        subj = qname_or_curie(graph, s)
        obj = qname_or_curie(graph, o)
        pred = qname_or_curie(graph, p)

        dot_graph.add_node(pydot.Node(subj, shape="ellipse"))
        dot_graph.add_node(pydot.Node(obj, shape="ellipse"))
        dot_graph.add_edge(pydot.Edge(subj, obj, label=pred))

    return dot_graph


def render_graph(dot_graph: "pydot.Dot", dot_path: Path, png_path: Path | None = None):
    # Write DOT text ourselves with UTF-8 to avoid Windows default code page issues.
    dot_text = dot_graph.to_string()
    dot_path.parent.mkdir(parents=True, exist_ok=True)
    with dot_path.open("w", encoding="utf-8") as fh:
        fh.write(dot_text)
    print(f"DOT file written to {dot_path} (UTF-8)")

    if png_path is not None:
        try:
            dot_graph.write_png(str(png_path))
            print(f"PNG file written to {png_path}")
        except Exception as e:
            print("Warning: failed to render PNG with GraphViz — is GraphViz installed and in PATH?", file=sys.stderr)
            print(str(e), file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Convert Turtle to GraphViz DOT/PNG.")
    parser.add_argument("ttl", type=Path, help="Path to Turtle file")
    parser.add_argument("-o", "--output", type=Path, help="Output DOT path")
    parser.add_argument("--png", type=Path, help="Optional PNG output path")
    parser.add_argument("--max-triples", type=int, default=2000, help="Maximum triples to include (to keep diagrams manageable)")
    args = parser.parse_args()

    ttl_path = args.ttl
    if not ttl_path.exists():
        parser.error(f"Turtle file {ttl_path} does not exist")

    graph = Graph()
    graph.parse(ttl_path, format="ttl")

    if len(graph) > args.max_triples:
        print(f"Graph has {len(graph)} triples. Truncating to first {args.max_triples} for readability.")
        graph = Graph(namespace_manager=graph.namespace_manager)[list(graph)[: args.max_triples]]

    dot_graph = build_dot(graph)

    dot_out = args.output if args.output else ttl_path.with_suffix(".dot")
    render_graph(dot_graph, dot_out, args.png)


if __name__ == "__main__":
    main() 