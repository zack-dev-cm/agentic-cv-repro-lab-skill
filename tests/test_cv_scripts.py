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


def run_script_in_dir(script: Path, cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )


def test_capture_cv_run_context_sanitizes_params_and_paths(tmp_path: Path) -> None:
    out_path = tmp_path / "cv-run-context.json"
    md_path = tmp_path / "cv-run-context.md"
    script = REPO_ROOT / "skill" / "data-science-cv-repro-lab" / "scripts" / "capture_cv_run_context.py"

    run_script(
        script,
        "--repo-root",
        str(REPO_ROOT),
        "--out",
        str(out_path),
        "--markdown-out",
        str(md_path),
        "--label",
        "ci",
        "--module",
        "pip",
        "--param",
        "dataset_root=/tmp/private-dataset",
        "--param",
        "api_token=secret-value",
    )

    payload = json.loads(out_path.read_text(encoding="utf-8"))
    markdown = md_path.read_text(encoding="utf-8")

    assert payload["cwd"] == "$REPO_ROOT"
    assert payload["git"]["repo_root"] == "$REPO_ROOT"
    assert payload["params"]["dataset_root"] == "<external>/private-dataset"
    assert payload["params"]["api_token"] == "<redacted:sensitive-key>"
    assert str(REPO_ROOT) not in out_path.read_text(encoding="utf-8")
    assert "/tmp/private-dataset" not in markdown


def test_capture_cv_run_context_redacts_git_branch_and_status(tmp_path: Path) -> None:
    repo_dir = tmp_path / "throwaway-repo"
    repo_dir.mkdir()
    subprocess.run(["git", "init"], cwd=repo_dir, check=True, capture_output=True, text=True)
    subprocess.run(["git", "config", "user.name", "Codex"], cwd=repo_dir, check=True, capture_output=True, text=True)
    subprocess.run(
        ["git", "config", "user.email", "codex@example.com"],
        cwd=repo_dir,
        check=True,
        capture_output=True,
        text=True,
    )
    (repo_dir / "README.md").write_text("# Temp\n", encoding="utf-8")
    subprocess.run(["git", "add", "README.md"], cwd=repo_dir, check=True, capture_output=True, text=True)
    subprocess.run(["git", "commit", "-m", "init"], cwd=repo_dir, check=True, capture_output=True, text=True)
    subprocess.run(
        ["git", "checkout", "-b", "customer-acme-rollout"],
        cwd=repo_dir,
        check=True,
        capture_output=True,
        text=True,
    )
    (repo_dir / "private-client-notes.md").write_text("secret\n", encoding="utf-8")

    out_path = tmp_path / "git-context.json"
    script = REPO_ROOT / "skill" / "data-science-cv-repro-lab" / "scripts" / "capture_cv_run_context.py"
    run_script_in_dir(
        script,
        repo_dir,
        "--repo-root",
        str(repo_dir),
        "--out",
        str(out_path),
        "--module",
        "pip",
    )

    payload = json.loads(out_path.read_text(encoding="utf-8"))

    assert payload["git"]["branch"] == "<redacted:branch>"
    assert payload["git"]["status_short"] == ["?? <untracked-path>"]
    assert "customer-acme-rollout" not in out_path.read_text(encoding="utf-8")
    assert "private-client-notes.md" not in out_path.read_text(encoding="utf-8")


def test_init_cv_artifact_manifest_redacts_bundle_and_external_items(tmp_path: Path) -> None:
    bundle_root = tmp_path / "bundle"
    bundle_root.mkdir()
    item_path = bundle_root / "notes" / "summary.md"
    item_path.parent.mkdir()
    item_path.write_text("# Summary\n", encoding="utf-8")
    out_path = tmp_path / "cv-artifact-manifest.json"
    script = REPO_ROOT / "skill" / "data-science-cv-repro-lab" / "scripts" / "init_cv_artifact_manifest.py"

    run_script(
        script,
        "--out",
        str(out_path),
        "--bundle-root",
        str(bundle_root),
        "--item",
        f"summary={item_path}",
        "--item",
        "dataset=/tmp/private-dataset",
    )

    payload = json.loads(out_path.read_text(encoding="utf-8"))

    assert payload["bundle_root"] == "$BUNDLE_ROOT"
    assert payload["artifacts"][0]["path"] == "$BUNDLE_ROOT/notes/summary.md"
    assert payload["artifacts"][0]["exists"] is True
    assert payload["artifacts"][1]["path"] == "<external>/private-dataset"
    assert payload["artifacts"][1]["exists"] is False


def test_init_cv_improvement_harness_emits_expected_shape(tmp_path: Path) -> None:
    out_path = tmp_path / "cv-improvement-harness.json"
    script = (
        REPO_ROOT
        / "skill"
        / "data-science-cv-repro-lab"
        / "scripts"
        / "init_cv_improvement_harness.py"
    )

    run_script(
        script,
        "--out",
        str(out_path),
        "--task-id",
        "segmentation-recovery",
        "--candidate-family",
        "baseline-recovery",
    )

    payload = json.loads(out_path.read_text(encoding="utf-8"))

    assert payload["task_id"] == "segmentation-recovery"
    assert payload["candidate_family"] == "baseline-recovery"
    assert payload["agents"]["subagent_roles"] == ["scout", "executor", "reviewer"]
    assert payload["oauth_policy"]["allowed_auth"][0] == "chatgpt_oauth"


def test_init_cv_browser_run_card_redacts_private_targets_and_aliases(tmp_path: Path) -> None:
    out_path = tmp_path / "cv-browser-run-card.json"
    script = REPO_ROOT / "skill" / "data-science-cv-repro-lab" / "scripts" / "init_cv_browser_run_card.py"

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
