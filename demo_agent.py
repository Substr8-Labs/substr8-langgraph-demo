#!/usr/bin/env python3
"""
Substr8 LangGraph Demo - Verifiable AI Agent Execution

This demo shows how to wrap a LangGraph agent with Substr8 instrumentation
to generate cryptographically verifiable execution proofs (RunProof).

Usage:
    pip install substr8-langgraph langgraph
    python demo_agent.py
"""

import json
from datetime import datetime

from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

from substr8_langgraph import instrument_graph


# === Define Agent State ===

class ResearchState(TypedDict):
    """State for our research agent."""
    topic: str
    sources: Annotated[list[str], operator.add]
    summary: str
    steps: Annotated[list[str], operator.add]


# === Define Agent Nodes ===

def search_node(state: ResearchState) -> dict:
    """Simulate searching for sources on a topic."""
    topic = state["topic"]
    
    # Simulated search results
    sources = [
        f"https://arxiv.org/search/?query={topic.replace(' ', '+')}",
        f"https://scholar.google.com/scholar?q={topic.replace(' ', '+')}",
        f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}",
    ]
    
    return {
        "sources": sources,
        "steps": [f"Searched for: {topic}"]
    }


def analyze_node(state: ResearchState) -> dict:
    """Simulate analyzing the sources."""
    num_sources = len(state["sources"])
    
    return {
        "steps": [f"Analyzed {num_sources} sources"]
    }


def summarize_node(state: ResearchState) -> dict:
    """Generate a summary based on the research."""
    topic = state["topic"]
    sources = state["sources"]
    
    summary = f"""Research Summary: {topic}

Based on analysis of {len(sources)} sources, here are the key findings:

1. The topic "{topic}" is an active area of research
2. Multiple academic and reference sources are available
3. Further investigation recommended for specific subtopics

Sources consulted:
{chr(10).join(f'- {s}' for s in sources)}

Generated at: {datetime.now().isoformat()}
"""
    
    return {
        "summary": summary,
        "steps": ["Generated summary"]
    }


# === Build the Graph ===

def build_research_graph() -> StateGraph:
    """Build the research agent graph."""
    
    graph = StateGraph(ResearchState)
    
    # Add nodes
    graph.add_node("search", search_node)
    graph.add_node("analyze", analyze_node)
    graph.add_node("summarize", summarize_node)
    
    # Add edges
    graph.set_entry_point("search")
    graph.add_edge("search", "analyze")
    graph.add_edge("analyze", "summarize")
    graph.add_edge("summarize", END)
    
    return graph


# === Main ===

def main():
    print("=" * 60)
    print("Substr8 LangGraph Demo - Verifiable Agent Execution")
    print("=" * 60)
    print()
    
    # Build the graph
    graph = build_research_graph()
    
    # Compile the base graph first
    compiled = graph.compile()
    
    # Wrap with Substr8 instrumentation
    print("🔧 Instrumenting graph with Substr8...")
    instrumented = instrument_graph(
        compiled,
        agent_id="demo/research-agent",
        project="substr8-demo",
    )
    
    # Run the agent
    print("🚀 Running agent...")
    print()
    
    initial_state = {
        "topic": "AI agent governance",
        "sources": [],
        "summary": "",
        "steps": [],
    }
    
    # invoke() returns result + proof metadata
    result = instrumented.invoke(initial_state)
    
    # Print results
    print("📋 Execution Steps:")
    for step in result.get("steps", []):
        print(f"   • {step}")
    print()
    
    print("📄 Summary:")
    print(result.get("summary", "N/A"))
    print()
    
    # Get the RunProof from result
    if "proof" in result:
        proof = result["proof"]
        
        # Convert to dict if it's a Pydantic model
        if hasattr(proof, 'model_dump'):
            proof_dict = proof.model_dump(mode="json")
        else:
            proof_dict = proof
        
        # Save to file
        with open("runproof.json", "w") as f:
            json.dump(proof_dict, f, indent=2, default=str)
        
        print("=" * 60)
        print("✅ RunProof generated: runproof.json")
        print()
        print(f"   Proof ID:  {result.get('proof_id', 'N/A')}")
        print(f"   Run ID:    {result.get('run_id', 'N/A')}")
        print(f"   Agent:     {proof_dict.get('header', {}).get('agent_id', 'N/A')}")
        print(f"   Events:    {len(proof_dict.get('trace', []))}")
        print(f"   Status:    {result.get('proof_status', 'N/A')}")
        print()
        print("🔍 Verify with:")
        print("   substr8 proof verify runproof.json")
        print()
        print("🌐 Or upload to:")
        print("   https://verify-ui-gamma.vercel.app")
        print("=" * 60)
    else:
        print("⚠️  No RunProof generated (check substr8-langgraph version)")
        print(f"   Result keys: {list(result.keys())}")


if __name__ == "__main__":
    main()
