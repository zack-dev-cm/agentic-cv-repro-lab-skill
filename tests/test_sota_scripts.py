from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from conftest import REPO_ROOT


def run_script(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def test_init_sota_artifact_manifest_redacts_bundle_and_external_items(tmp_path: Path) -> None:
    bundle_root = tmp_path / "bundle"
    bundle_root.mkdir()
    review_packet = bundle_root / "review" / "packet.json"
    review_packet.parent.mkdir()
    review_packet.write_text("{}", encoding="utf-8")
    out_path = tmp_path / "sota-artifact-manifest.json"
    script = REPO_ROOT / "skill" / "sota-agent" / "scripts" / "init_sota_artifact_manifest.py"

    run_script(
        script,
        "--out",
        str(out_path),
        "--bundle-root",
        str(bundle_root),
        "--item",
        f"review_packet={review_packet}",
        "--item",
        "scoreboard=/tmp/private-scoreboard.json",
    )

    payload = json.loads(out_path.read_text(encoding="utf-8"))

    assert payload["bundle_root"] == "$BUNDLE_ROOT"
    assert payload["artifacts"][0]["path"] == "$BUNDLE_ROOT/review/packet.json"
    assert payload["artifacts"][1]["path"] == "<external>/private-scoreboard.json"


def test_init_sota_program_redacts_frontier_sources_and_sets_defaults(tmp_path: Path) -> None:
    out_path = tmp_path / "sota-program.json"
    script = REPO_ROOT / "skill" / "sota-agent" / "scripts" / "init_sota_program.py"

    run_script(
        script,
        "--out",
        str(out_path),
        "--campaign-id",
        "demo-campaign",
        "--task",
        "lesion-segmentation",
        "--metric",
        "dice",
        "--baseline",
        "baseline=0.87",
        "--paper",
        "https://github.com/example/paper-repo",
        "--paper",
        "/tmp/private-notes.md",
    )

    payload = json.loads(out_path.read_text(encoding="utf-8"))

    assert payload["program_id"] == "demo-campaign"
    assert payload["problem"] == "lesion-segmentation"
    assert payload["benchmark"]["primary_metric"] == "dice"
    assert payload["frontier_sources"] == ["github.com", "<external>/private-notes.md"]
    assert payload["agents"]["subagent_roles"] == ["scout", "reproducer", "reviewer"]


def test_init_sota_vm_bootstrap_manifest_redacts_sensitive_command_tokens(tmp_path: Path) -> None:
    out_path = tmp_path / "sota-vm-bootstrap.json"
    output_root = tmp_path / "runs"
    output_root.mkdir()
    script = REPO_ROOT / "skill" / "sota-agent" / "scripts" / "init_sota_vm_bootstrap_manifest.py"

    run_script(
        script,
        "--out",
        str(out_path),
        "--output-root",
        str(output_root),
        "--model-family",
        "demo-trainer",
        "--command",
        "--notebook-url=https://example.com/run?token=secret123",
        r"--dataset-root=D:\private-data\private-dataset",
    )

    payload = json.loads(out_path.read_text(encoding="utf-8"))
    command = payload["runtime"]["command"]

    assert command[0] == "--notebook-url=<redacted:credential-url>"
    assert command[1] == "--dataset-root=<external>/private-dataset"


def test_init_sota_browser_run_card_redacts_private_targets_and_aliases(tmp_path: Path) -> None:
    out_path = tmp_path / "sota-browser-run-card.json"
    script = REPO_ROOT / "skill" / "sota-agent" / "scripts" / "init_sota_browser_run_card.py"

    run_script(
        script,
        "--out",
        str(out_path),
        "--target-url",
        "http://127.0.0.2:8501/private/notebook?token=abc",
        "--browser-alias",
        "personal-chrome",
        "--session-alias",
        "client-session",
    )

    payload = json.loads(out_path.read_text(encoding="utf-8"))

    assert payload["browser"]["browser_alias"] == "<redacted:browser-alias>"
    assert payload["browser"]["session_alias"] == "<redacted:session-alias>"
    assert payload["target"]["url"] == ""
    assert payload["target"]["target_host"] == ""
    assert payload["target"]["target_label"] == "private-notebook-target"
