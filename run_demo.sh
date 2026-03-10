#!/usr/bin/env bash
set -e

echo "🔧 Installing dependencies..."
pip install -r requirements.txt -q

echo "🚀 Running demo agent..."
python demo_agent.py

echo ""
echo "🔍 Verifying RunProof..."
pip install substr8 -q
substr8 proof verify runproof.json
