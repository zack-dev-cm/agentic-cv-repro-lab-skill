from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CV_SCRIPTS = REPO_ROOT / "skill" / "data-science-cv-repro-lab" / "scripts"
SOTA_SCRIPTS = REPO_ROOT / "skill" / "sota-agent" / "scripts"

for scripts_path in (CV_SCRIPTS, SOTA_SCRIPTS):
    scripts_text = str(scripts_path)
    if scripts_text not in sys.path:
        sys.path.insert(0, scripts_text)
