#!/usr/bin/env python3
"""Create a compact research, plan, journal, and evidence scaffold for a CV task."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    return cleaned.strip("-") or "cv-task"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="Directory under which the task folder will be created.")
    parser.add_argument("--task-id", required=True, help="Stable task identifier.")
    parser.add_argument("--title", required=True, help="Human-readable title.")
    args = parser.parse_args()

    task_id = slugify(args.task_id)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    root = Path(args.root).expanduser().resolve() / task_id
    root.mkdir(parents=True, exist_ok=True)

    readme = f"""# {args.title}

- task_id: `{task_id}`
- created_utc: `{now}`

## Goal

Write the product or research question here.

## Promotion Gate

Write the benchmark and non-regression surfaces here.
"""

    research = f"""# Research

## Current State

- facts only

## Files And Artifacts

- add exact paths

## Constraints

- note blockers, environment assumptions, and missing assets
"""

    plan = """# Plan

## Hypotheses

- hypothesis 1

## Steps

1. short validation loop
2. benchmark
3. promotion decision

## Stop Conditions

- what would make this line of work fail fast
"""

    journal = """# Journal

## Timeline

- timestamp, action, result, next step
"""

    evidence = """# Evidence

## Commands

- exact commands run

## Outputs

- output paths

## Risks

- unresolved risks
"""

    promotion = """# Promotion

## Baseline

- current trusted checkpoint or revision

## Candidate

- new checkpoint or revision

## Decision

- promote, hold, or rollback

## Reason

- benchmark-backed summary only
"""

    files = {
        "README.md": readme,
        "research.md": research,
        "plan.md": plan,
        "journal.md": journal,
        "evidence.md": evidence,
        "promotion.md": promotion,
    }
    for name, content in files.items():
        write(root / name, content)

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
