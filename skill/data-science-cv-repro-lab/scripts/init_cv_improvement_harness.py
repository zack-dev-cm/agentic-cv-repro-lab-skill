#!/usr/bin/env python3
"""Create a machine-readable improvement harness for plateau recovery and score-improvement work."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, help="Path to the output JSON file.")
    parser.add_argument("--task-id", required=True, help="Stable task or investigation identifier.")
    parser.add_argument(
        "--candidate-family",
        default="",
        help="Optional recipe or model family identifier for this search branch.",
    )
    args = parser.parse_args()

    out_path = Path(args.out).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "schema_version": "1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "task_id": args.task_id,
        "candidate_family": args.candidate_family,
        "benchmark_contract": {
            "dataset_id": "",
            "dataset_version": "",
            "split": "",
            "primary_metric": "",
            "direction": "maximize",
            "minimum_delta": 0.0,
            "non_regression_surfaces": [],
        },
        "resource_budget": {
            "max_candidates": 0,
            "max_wall_time_hours": 0,
            "max_gpu_hours": 0.0,
        },
        "rerun_policy": {
            "required_for_small_delta": True,
            "small_delta_threshold": 0.0,
            "minimum_reruns": 2,
            "seed_strategy": "adjacent",
            "acceptance_rule": "",
        },
        "agents": {
            "main_thread_role": "planner",
            "subagent_roles": ["scout", "executor", "reviewer"],
            "notes": "",
        },
        "search_policy": {
            "strategy": "bounded_evolution",
            "unit_of_change": "single_meaningful_change",
            "keep_top_k": 5,
            "require_patch_diff": True,
            "require_machine_readable_scores": True,
        },
        "slices": [
            {
                "name": "all",
                "description": "Full benchmark set",
                "metric": "",
                "required": True,
            }
        ],
        "failure_taxonomy": [
            {
                "name": "",
                "definition": "",
                "review_cases": [],
            }
        ],
        "oauth_policy": {
            "allowed_auth": [
                "chatgpt_oauth",
                "codex_oauth",
                "codex_app_server_auth_json",
            ],
            "forbidden_env_vars": [
                "OPENAI_API_KEY",
                "ANTHROPIC_API_KEY",
                "GOOGLE_API_KEY",
                "CEREBRAS_API_KEY",
                "AZURE_OPENAI_API_KEY",
            ],
            "notes": "Third-party frameworks that require paid API keys are reference-only unless reconfigured to run through local tools and OAuth-backed Codex sessions.",
        },
        "evidence_requirements": {
            "required_artifacts": [
                "dataset_manifest",
                "run_card",
                "metrics_json_or_csv",
                "overlay_preview",
                "failure_review_notes",
            ],
            "promotion_bundle_path": "",
        },
    }

    out_path.write_text(f"{json.dumps(payload, indent=2)}\n", encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
