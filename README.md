# Substr8 LangGraph Demo

Generate cryptographically verifiable RunProofs from LangGraph workflows.

## Quick Start

```bash
git clone https://github.com/Substr8-Labs/substr8-langgraph-demo
cd substr8-langgraph-demo
./run_demo.sh
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Run the demo agent
python demo_agent.py

# Verify the generated proof
substr8 proof verify runproof.json

# Inspect proof details
substr8 proof inspect runproof.json --events
```

## RunProof v2.1 Features

This demo generates RunProof v2.1 artifacts with:

- **Claims** — Policy, model, environment metadata
- **Lineage** — Chainable proofs for workflows
- **Expanded Issuer** — Name, version, runtime info

See `sample_runproof.json` for an example.

## Verification

[![RunProof Verified](https://runproof.substr8labs.com/badge/proof_demo_v21_001)](https://runproof.substr8labs.com/proof/proof_demo_v21_001)

## Links

- [Documentation](https://docs.substr8labs.com)
- [RunProof Specification](https://docs.substr8labs.com/spec)
- [Cookbook](https://docs.substr8labs.com/cookbook)

## License

MIT
