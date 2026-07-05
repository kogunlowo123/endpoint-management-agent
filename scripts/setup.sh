#!/bin/bash
set -euo pipefail
echo "Setting up Endpoint Management Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
