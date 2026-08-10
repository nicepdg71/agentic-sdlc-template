#!/usr/bin/env bash

set -euo pipefail

echo "::error::Production deployment adapter is not configured."
echo "Configure scripts/deploy-production.sh for the selected deployment target."

exit 1
