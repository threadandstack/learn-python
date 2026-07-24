#!/usr/bin/env bash
# Resume helper: activates the venv and shows you where you left off.
# Run this from anywhere with: ./start.sh (from inside LEARN_PYTHON) or
# bash /path/to/LEARN_PYTHON/start.sh from elsewhere.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

if [ ! -d ".venv" ]; then
    echo "No .venv found yet."
    echo "Head to modules/00_setup_and_orientation/LESSON.md and follow the setup steps first."
    exit 1
fi

# shellcheck source=/dev/null
source .venv/bin/activate
python3 tools/status.py
