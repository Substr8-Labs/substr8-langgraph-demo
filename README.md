# Substr8 LangGraph Demo

**Verifiable AI Agent Execution in 60 Seconds**

This demo shows how to generate cryptographically verifiable execution proofs (RunProof) for LangGraph agents using Substr8.

## Quick Start

```bash
# Install dependencies
pip install substr8-langgraph langgraph

# Run the demo agent
python demo_agent.py

# Verify the proof
substr8 proof verify runproof.json
```

## What This Demo Does

1. **Builds a LangGraph agent** - A simple research agent with search → analyze → summarize flow
2. **Wraps it with Substr8** - `instrument_graph()` adds event capture and proof generation
3. **Generates a RunProof** - Cryptographic receipt of everything that happened

## Output

After running, you'll see:

```
✅ RunProof generated: runproof.json

   Proof ID:  proof_abc123...
   Run ID:    run_xyz789...
   Agent:     demo/research-agent
   Events:    6

🔍 Verify with:
   substr8 proof verify runproof.json

🌐 Or upload to:
   https://verify-ui-gamma.vercel.app
```

## Verify the Proof

### CLI Verification
```bash
pip install substr8-cli
substr8 proof verify runproof.json
```

### Web Verification
Upload `runproof.json` to [verify.substr8labs.com](https://verify-ui-gamma.vercel.app)

## What's in a RunProof?

A RunProof contains:

- **Header** - Agent ID, timestamps, status
- **Trace** - Every event with cryptographic hash chain
- **Commitments** - Merkle root + Ed25519 signature
- **Outputs** - Hashed results

```json
{
  "schema_version": "runproof/v2",
  "header": {
    "proof_id": "proof_...",
    "agent_id": "demo/research-agent",
    "status": "completed"
  },
  "trace": [
    {"type": "run_started", "entry_hash": "sha256:..."},
    {"type": "node_started", "entry_hash": "sha256:..."},
    ...
  ],
  "commitments": {
    "event_root": "sha256:...",
    "signature": {"algorithm": "ed25519", "value": "..."}
  }
}
```

## Why RunProof?

- **Auditability** - Know exactly what your agent did
- **Tamper Evidence** - Hash chain detects any modification
- **Provenance** - Cryptographic signature proves origin
- **Compliance** - Verifiable execution for regulated industries

## Learn More

- [Substr8 Docs](https://docs.substr8labs.com)
- [RunProof Spec](https://github.com/Substr8-Labs/substr8-core)
- [Substr8 Labs](https://substr8labs.com)

---

**Agents with receipts.** 🧾
