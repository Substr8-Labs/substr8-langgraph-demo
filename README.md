# Substr8 LangGraph Demo

**Generate and verify a cryptographically signed receipt for an AI agent in under 60 seconds.**

## Quick Start

```bash
git clone https://github.com/Substr8-Labs/substr8-langgraph-demo
cd substr8-langgraph-demo
./run_demo.sh
```

Or with make:

```bash
make demo
```

## Expected Output

```
🔧 Installing dependencies...
🚀 Running demo agent...

============================================================
Substr8 LangGraph Demo - Verifiable Agent Execution
============================================================

🔧 Instrumenting graph with Substr8...
🚀 Running agent...

📋 Execution Steps:
   • Searched for: AI agent governance
   • Analyzed 3 sources
   • Generated summary

============================================================
✅ RunProof generated: runproof.json

   Proof ID:  proof_ccfe7c4abd014eab
   Run ID:    run_ade859b400e24d09
   Agent:     demo/research-agent
   Events:    6
   Status:    verified
============================================================

🔍 Verifying RunProof...

╭──────────────────────────── Verification Result ─────────────────────────────╮
│ ✓ RunProof: VALID                                                            │
╰──────────────────────────────────────────────────────────────────────────────╯

Checks:
  ✓ schema
  ✓ hash_chain
  ✓ merkle_root
  ✓ signature
```

## Verify Without Running

A sample proof is included. Test verification immediately:

```bash
pip install substr8
substr8 proof verify sample_runproof.json
```

## What This Demo Does

1. **Builds a LangGraph agent** — Research agent with search → analyze → summarize flow
2. **Wraps it with Substr8** — `instrument_graph()` captures every event
3. **Generates a RunProof** — Cryptographic receipt with hash chain + Merkle root + signature
4. **Verifies the proof** — CLI confirms the proof is valid and untampered

## Files

| File | Description |
|------|-------------|
| `demo_agent.py` | LangGraph agent with Substr8 instrumentation |
| `runproof.json` | Generated proof (created when you run the demo) |
| `sample_runproof.json` | Pre-generated proof for immediate testing |
| `run_demo.sh` | One-command demo script |
| `Makefile` | `make demo` target |

## Verify in Browser

Upload `runproof.json` to [verify.substr8labs.com](https://verify-ui-gamma.vercel.app)

## Learn More

- [Docs](https://docs.substr8labs.com)
- [How Verification Works](https://docs.substr8labs.com/verification)
- [RunProof Schema](https://docs.substr8labs.com/runproof)
- [GitHub](https://github.com/Substr8-Labs)

---

**Agents with receipts.** 🧾
