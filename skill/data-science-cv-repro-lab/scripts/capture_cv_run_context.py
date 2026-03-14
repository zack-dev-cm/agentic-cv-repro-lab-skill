#!/usr/bin/env python3
"""Capture a compact, reproducible snapshot of a CV experiment context."""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_MODULES = [
    "torch",
    "torchvision",
    "numpy",
    "albumentations",
    "cv2",
    "onnx",
    "onnxruntime",
    "ultralytics",
    "mmseg",
    "mmcv",
    "timm",
    "segmentation_models_pytorch",
    "wandb",
    "mlflow",
]

DEFAULT_ENV_PREFIXES = [
    "CUDA",
    "CUDNN",
    "PYTHON",
    "TORCH",
    "WANDB",
    "MLFLOW",
    "DVC",
    "OMP",
    "MKL",
]


def run(cmd: list[str], cwd: Path | None = None) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError as exc:
        return 127, "", str(exc)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def sha256_file(path: Path, block_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            chunk = fh.read(block_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def parse_key_value(items: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise SystemExit(f"invalid --param value: {item!r}, expected key=value")
        key, value = item.split("=", 1)
        out[key.strip()] = value.strip()
    return out


def git_info(repo_root: Path) -> dict[str, Any]:
    info: dict[str, Any] = {"is_git_repo": False}
    code, _, _ = run(["git", "rev-parse", "--is-inside-work-tree"], cwd=repo_root)
    if code != 0:
        return info
    info["is_git_repo"] = True
    info["repo_root"] = str(repo_root)
    for key, cmd in {
        "head": ["git", "rev-parse", "HEAD"],
        "short_head": ["git", "rev-parse", "--short", "HEAD"],
        "branch": ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        "describe": ["git", "describe", "--always", "--dirty", "--tags"],
    }.items():
        _, out, _ = run(cmd, cwd=repo_root)
        info[key] = out or None
    _, status_out, _ = run(["git", "status", "--short"], cwd=repo_root)
    status_lines = [line for line in status_out.splitlines() if line.strip()]
    info["dirty"] = bool(status_lines)
    info["status_short"] = status_lines[:200]
    info["modified_count"] = sum(1 for line in status_lines if not line.startswith("??"))
    info["untracked_count"] = sum(1 for line in status_lines if line.startswith("??"))
    return info


def module_versions(names: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for name in names:
        try:
            module = importlib.import_module(name)
        except Exception as exc:
            data[name] = {"installed": False, "error": type(exc).__name__}
            continue
        version = getattr(module, "__version__", None)
        record: dict[str, Any] = {"installed": True, "version": version}
        if name == "torch":
            record["cuda"] = getattr(getattr(module, "version", None), "cuda", None)
            try:
                record["cudnn_version"] = module.backends.cudnn.version()
            except Exception:
                record["cudnn_version"] = None
            try:
                record["cuda_available"] = bool(module.cuda.is_available())
                record["device_count"] = int(module.cuda.device_count())
            except Exception:
                record["cuda_available"] = None
                record["device_count"] = None
        data[name] = record
    return data


def env_snapshot(prefixes: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for key, value in sorted(os.environ.items()):
        if any(key.startswith(prefix) for prefix in prefixes):
            out[key] = value
    return out


def path_record(path_str: str, hash_files: bool, recursive_dir_count: bool) -> dict[str, Any]:
    path = Path(path_str).expanduser()
    record: dict[str, Any] = {"path": str(path), "exists": path.exists()}
    if not path.exists():
        return record
    stat = path.stat()
    record["type"] = "dir" if path.is_dir() else "file"
    record["size_bytes"] = stat.st_size
    record["mtime_utc"] = datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat()
    if path.is_file():
        if hash_files:
            record["sha256"] = sha256_file(path)
    elif path.is_dir():
        children = list(path.iterdir())
        record["child_count"] = len(children)
        if recursive_dir_count:
            record["recursive_file_count"] = sum(1 for p in path.rglob("*") if p.is_file())
    return record


def pip_freeze_hash() -> dict[str, Any]:
    code, out, err = run([sys.executable, "-m", "pip", "freeze"])
    if code != 0:
        return {"available": False, "error": err or "pip freeze failed"}
    lines = sorted(line.strip() for line in out.splitlines() if line.strip())
    digest = hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()
    return {
        "available": True,
        "count": len(lines),
        "sha256": digest,
        "sample": lines[:40],
    }


def gpu_snapshot() -> dict[str, Any]:
    code, out, err = run(
        [
            "nvidia-smi",
            "--query-gpu=name,driver_version,memory.total,memory.used,utilization.gpu",
            "--format=csv,noheader,nounits",
        ]
    )
    if code != 0:
        return {"available": False, "error": err or "nvidia-smi unavailable"}
    rows = []
    for line in out.splitlines():
        parts = [chunk.strip() for chunk in line.split(",")]
        if len(parts) != 5:
            continue
        rows.append(
            {
                "name": parts[0],
                "driver_version": parts[1],
                "memory_total_mib": int(parts[2]),
                "memory_used_mib": int(parts[3]),
                "utilization_gpu_pct": int(parts[4]),
            }
        )
    return {"available": True, "gpus": rows}


def to_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# CV Run Context: {payload.get('label') or 'unnamed'}",
        "",
        f"- captured_utc: `{payload['captured_utc']}`",
        f"- cwd: `{payload['cwd']}`",
        f"- python: `{payload['python']['version']}`",
        f"- platform: `{payload['platform']['platform']}`",
    ]
    git = payload.get("git") or {}
    if git.get("is_git_repo"):
        lines.extend(
            [
                f"- git branch: `{git.get('branch')}`",
                f"- git head: `{git.get('short_head')}`",
                f"- git dirty: `{git.get('dirty')}`",
            ]
        )
    gpu = payload.get("gpu") or {}
    if gpu.get("available") and gpu.get("gpus"):
        first = gpu["gpus"][0]
        lines.append(
            f"- gpu0: `{first['name']}`, util `{first['utilization_gpu_pct']}%`, "
            f"mem `{first['memory_used_mib']}/{first['memory_total_mib']} MiB`"
        )
    if payload.get("params"):
        lines.append("")
        lines.append("## Params")
        for key, value in sorted(payload["params"].items()):
            lines.append(f"- `{key}`: `{value}`")
    if payload.get("tracked_paths"):
        lines.append("")
        lines.append("## Tracked Paths")
        for item in payload["tracked_paths"]:
            extra = ""
            if item.get("sha256"):
                extra = f", sha256 `{item['sha256'][:12]}`"
            lines.append(f"- `{item['path']}` ({item.get('type', 'missing')}){extra}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--out", required=True)
    parser.add_argument("--markdown-out")
    parser.add_argument("--label")
    parser.add_argument("--path", action="append", default=[])
    parser.add_argument("--param", action="append", default=[])
    parser.add_argument("--module", action="append", default=[])
    parser.add_argument("--env-prefix", action="append", default=[])
    parser.add_argument("--hash-files", action="store_true", default=False)
    parser.add_argument("--recursive-dir-count", action="store_true", default=False)
    parser.add_argument("--skip-pip-freeze", action="store_true", default=False)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve()
    md_path = Path(args.markdown_out).expanduser().resolve() if args.markdown_out else None

    payload: dict[str, Any] = {
        "label": args.label,
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "cwd": str(Path.cwd()),
        "python": {
            "executable": sys.executable,
            "version": sys.version.replace("\n", " "),
        },
        "platform": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        },
        "git": git_info(repo_root),
        "params": parse_key_value(args.param),
        "tracked_paths": [
            path_record(path_str, args.hash_files, args.recursive_dir_count) for path_str in args.path
        ],
        "modules": module_versions(args.module or DEFAULT_MODULES),
        "env": env_snapshot(args.env_prefix or DEFAULT_ENV_PREFIXES),
        "gpu": gpu_snapshot(),
    }
    if not args.skip_pip_freeze:
        payload["pip_freeze"] = pip_freeze_hash()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if md_path:
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(to_markdown(payload), encoding="utf-8")
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
