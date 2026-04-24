from __future__ import annotations

from pathlib import Path

from cv_public_safety import sanitize_command_tokens, sanitize_metadata_map
from sota_public_safety import sanitize_ref


def test_sanitize_command_tokens_redacts_paths_and_credentials(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    data_file = repo_root / "artifacts" / "metrics.json"
    data_file.parent.mkdir()
    data_file.write_text("{}", encoding="utf-8")

    tokens = [
        "--auth-token=secret-value",
        f"--config={data_file}",
        "REMOTE=https://user:pass@example.com/repo.git",
        str(data_file),
    ]

    sanitized = sanitize_command_tokens(
        tokens,
        alias_roots=[(repo_root, "$REPO_ROOT")],
        allow_absolute_paths=False,
    )

    assert sanitized[0] == "--auth-token=<redacted:sensitive-flag-value>"
    assert sanitized[1] == "--config=$REPO_ROOT/artifacts/metrics.json"
    assert sanitized[2] == "REMOTE=<redacted:credential-url>"
    assert sanitized[3] == "$REPO_ROOT/artifacts/metrics.json"


def test_sanitize_metadata_map_redacts_sensitive_values(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    repo_root.mkdir()

    sanitized = sanitize_metadata_map(
        {
            "dataset_root": r"D:\private-data\private-dataset",
            "api_token": "secret-value",
            "remote_url": "https://example.com/run?token=secret123",
            "lane": "ci",
        },
        alias_roots=[(repo_root, "$REPO_ROOT")],
        allow_absolute_paths=False,
    )

    assert sanitized["dataset_root"] == "<external>/private-dataset"
    assert sanitized["api_token"] == "<redacted:sensitive-key>"
    assert sanitized["remote_url"] == "<redacted:credential-url>"
    assert sanitized["lane"] == "ci"


def test_sanitize_ref_redacts_public_summary_inputs() -> None:
    assert sanitize_ref("https://github.com/example/project") == "github.com"
    assert sanitize_ref("/tmp/private-run/card.json") == "<external>/card.json"
    assert sanitize_ref(r"D:\private-run\card.json") == "<external>/card.json"
    assert sanitize_ref("baseline-v2") == "baseline-v2"
