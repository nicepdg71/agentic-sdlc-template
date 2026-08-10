#!/usr/bin/env bash

set -euo pipefail

echo "Agentic SDLC project CI adapter"

# Master Template 자체에서는 project.name이 비어 있다.
if grep -Eq '^[[:space:]]*name:[[:space:]]*""[[:space:]]*$' project.yaml; then
  echo "Template mode detected."
  echo "Project-specific CI is not required for the master template."
  exit 0
fi

echo "::error::Project-specific CI is not configured."
echo "Configure scripts/ci.sh for this project."
echo ""
echo "Required categories should normally include:"
echo "- lint/static analysis"
echo "- unit tests"
echo "- build"
echo "- project-specific verification"

exit 1
