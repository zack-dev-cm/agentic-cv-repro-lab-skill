#!/usr/bin/env python3
"""Create a machine-readable review dashboard manifest for CV execution surfaces."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_sync_target(raw: str) -> dict[str, object]:
    name, sep, remote_label = raw.partition("=")
    if not name.strip():
        raise SystemExit(f"invalid --sync-target value: {raw!r}, expected name=remote-label")
    return {
        "name": name.strip(),
        "remote_label": remote_label.strip() if sep else "",
        "local_parent": "",
        "auto_sync_minutes": 0,
        "last_sync_utc": "",
        "status": "",
        "notes": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, help="Path to the output JSON file.")
    parser.add_argument("--dashboard-id", required=True, help="Stable dashboard identifier.")
    parser.add_argument("--title", default="", help="Human-readable dashboard title.")
    parser.add_argument("--port", type=int, default=0, help="Optional local dashboard port.")
    parser.add_argument("--dashboard-url", default="", help="Optional local or remote dashboard URL.")
    parser.add_argument("--summary-root", action="append", default=[], help="Repeatable summary root.")
    parser.add_argument("--benchmark-root", action="append", default=[], help="Repeatable benchmark root.")
    parser.add_argument("--allowed-root", action="append", default=[], help="Repeatable allowed file root.")
    parser.add_argument(
        "--sync-target",
        action="append",
        default=[],
        help="Repeatable sync target in name=remote-label form.",
    )
    args = parser.parse_args()

    out_path = Path(args.out).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "schema_version": "1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "dashboard_id": args.dashboard_id,
        "title": args.title,
        "server": {
            "port": args.port,
            "dashboard_url": args.dashboard_url,
            "status": "",
        },
        "surfaces": {
            "summary_roots": args.summary_root,
            "benchmark_roots": args.benchmark_root,
            "allowed_roots": args.allowed_root,
        },
        "sync_targets": [parse_sync_target(item) for item in args.sync_target],
        "observed_counts": {
            "runtime_groups": 0,
            "runtime_runs": 0,
            "qa_runs": 0,
            "curated_comparisons": 0,
            "benchmark_panels": 0,
            "tracked_datasets": 0,
        },
        "curated_samples": [],
        "audits": {
            "progress_snapshot_paths": [],
            "comparison_summary_paths": [],
            "source_audit_paths": [],
            "leakage_audit_paths": [],
            "eda_report_paths": [],
            "overfit_summary_paths": [],
        },
        "decision": {
            "status": "review",
            "reason": "",
        },
        "notes": [],
    }

    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
