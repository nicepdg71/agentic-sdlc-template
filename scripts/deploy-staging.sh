#!/usr/bin/env bash

set -euo pipefail

echo "::error::Staging deployment adapter is not configured."
echo "Configure scripts/deploy-staging.sh for the selected deployment target."

exit 1
