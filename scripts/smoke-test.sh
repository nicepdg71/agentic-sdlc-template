#!/usr/bin/env bash

set -euo pipefail

ENVIRONMENT="${1:-}"

if [[ -z "${ENVIRONMENT}" ]]; then
  echo "::error::Environment argument is required."
  exit 1
fi

echo "::error::Smoke test adapter is not configured for ${ENVIRONMENT}."
exit 1
