---
name: data-science-cv-repro-lab
description: Run reproducible, agentic computer-vision experiments end to end. Use when the task involves CV training or inference debugging, OpenClaw or browser-driven Colab/Kaggle workflows, preprocessing and augmentation audits, checkpoint comparisons, benchmark-gated deployment decisions, GPU or VM training monitoring, or turning an ad hoc DS/CV workflow into a repeatable playbook.
homepage: https://github.com/zack-dev-cm/agentic-cv-repro-lab-skill
user-invocable: false
metadata: {"openclaw":{"homepage":"https://github.com/zack-dev-cm/agentic-cv-repro-lab-skill","skillKey":"data-science-cv-repro-lab","requires":{"anyBins":["python3","python"]}}}
---

# Data Science CV Repro Lab

## Goal

Turn CV work into a reproducible decision loop:

- fixed inputs
- explicit metrics
- durable artifacts
- bounded browser automation
- long-run health monitoring
- promotion only on verified benchmark wins

## Use This Skill When

- the user asks to debug CV training, segmentation, detection, or runtime behavior
- the workflow includes OpenClaw, Colab, Kaggle, or browser-only notebook actions
- you need preprocessing, augmentation, or label-alignment review
- the task requires checkpoint comparisons, export comparisons, or promotion gating
- the user wants VM or GPU watchdog logic, heartbeat files, or auto-stop behavior
- the user wants a general third-party CV workflow, not only repo-specific advice

## Quick Start

1. Lock the objective before touching code.
   - Write the product problem in one sentence.
   - Name the primary metric.
   - Name the non-regression surfaces.
   - State what blocks promotion.

2. Initialize the durable records immediately.
   - Use `python3 {baseDir}/scripts/init_cv_dataset_manifest.py --out <json> --dataset-id <id>`.
   - Use `python3 {baseDir}/scripts/init_cv_run_card.py --out <json> --candidate-id <id> --task-id <task> --baseline-id <baseline>`.
   - If a browser lane matters, use `python3 {baseDir}/scripts/init_cv_browser_run_card.py --out <json> --target-url <url>`.

3. Capture the current state immediately.
   - Use `python3 {baseDir}/scripts/capture_cv_run_context.py --repo-root <repo> --out <json> --markdown-out <md> --path <dataset_or_checkpoint> --param key=value`.
   - Record git state, environment, tracked paths, GPU state, and experiment params before launch.

4. Pick the right orchestration lane.
   - Local debug lane: tiny overfit, transform audits, shape and dtype checks.
   - Browser notebook lane: Colab or Kaggle steps that must happen in a real browser or notebook UI.
   - Colab GPU lane: runtime selection, smoke validation, artifact export, and browser evidence.
   - Custom VM or cluster lane: long runs with heartbeats, watchdogs, stall detection, sync, and auto-stop.
   - Promotion lane: fixed benchmark matrix plus customer-facing surface checks.

5. Work the debug ladder in order.
   - `Data audit`: split integrity, label normalization, image-mask pairing, resize geometry.
   - `Preview audit`: at least one augmentation preview and one transformed batch preview.
   - `Tiny overfit`: 4-16 shared samples with `no_aug`.
   - `Short resumed run`: continue from the best trusted checkpoint.
   - `Long run`: only after the short loop is healthy.

6. Keep agentic work bounded.
   - External browser LLM output is hypothesis generation, not release evidence.
   - Browser steps must emit screenshots, machine-readable scores, and explicit success markers.
   - Hard-fail on unavailable browser modes, dead CDP sessions, or ambiguous notebook state.
   - Keep planner, executor, reviewer, and promoter responsibilities distinct even if one agent performs more than one role.

7. Promote only on full-surface wins.
   - Raw checkpoint quality
   - Exported or runtime quality
   - User-facing render or product surface
   - Runtime cost or throughput if deployment matters

## Operating Rules

### Research before edits

- Keep separate files or sections for `research`, `plan`, `journal`, and `evidence`.
- Summaries are not evidence. Preserve the artifact paths.
- If a workflow uses both code changes and browser actions, record both.

### Agentic orchestration rules

- Planner: defines the question, benchmark, stop condition, and chosen execution lane.
- Executor: runs the browser, notebook, local, or VM steps and preserves artifacts.
- Reviewer: checks whether the evidence actually answers the question and catches regressions.
- Promoter: makes the final hold or promote decision from the run card, not from memory.
- If one agent performs all roles, keep the outputs separated anyway.

### Browser automation rules

- Prefer stable URLs over uploads.
- Start with a short smoke run before full training.
- Capture at least two screenshots when the browser UI is part of the validation path.
- Pull artifacts back locally as files, not only screenshots.
- Use explicit timeout and marker logic; do not rely on visual guesswork.
- Record browser profile aliases and session aliases in durable artifacts; keep raw CDP URLs in ephemeral local debug logs only.

### Colab GPU rules

- Select the accelerator explicitly before running expensive cells.
- Verify GPU readiness from inside the notebook before the long run.
- Use a smoke cell that proves the runtime, imports, and data mounts all work.
- Export all required artifacts to one stable bundle directory.
- Pull the artifact manifest plus at least one preview image back to local storage.

### Custom VM and cluster rules

- Create a named run root before launch.
- Write a machine-readable bootstrap manifest with commit, dataset, env, and command details.
- Run long jobs under a session, heartbeat, or supervisor so liveness is explicit.
- Track GPU utilization, epoch movement, and log freshness.
- Sync summaries and checkpoints back to local storage on a schedule.
- Auto-stop or downgrade to a debug path when the run is clearly unhealthy.

### CV training rules

- Do not change architecture first.
- Prove learning on a tiny shared subset before scaling.
- Save previews in the same run folder as metrics and summaries.
- Do not compare candidates on different benchmark sets.

### Promotion rules

- Keep the last trusted baseline intact until the candidate clears agreed gates.
- If the semantic model improves but the deployed overlay or service output regresses, fix the downstream path before promotion.
- Prefer a machine-readable run card plus a short markdown summary.
- Initialize that run card before or at launch time so later steps append to one canonical record.

### Public distribution rules

- Use `{baseDir}` when pointing at bundled scripts or references.
- Keep secrets, tokens, private dataset identifiers, browser profile names, and internal URLs out of the skill bundle.
- Do not publish repo-specific absolute paths.
- Keep private specialization in a local override skill, not the public package.

## References

Read only the reference that matches the task:

- `references/official-repro-guidance.md`
  - Official PyTorch, Albumentations, MLflow, and DVC guidance.
- `references/agentic-research-patterns.md`
  - How to adapt `karpathy/autoresearch` style loops to DS and CV work.
- `references/openclaw-browser-lane.md`
  - OpenClaw, CDP, Colab, screenshot, artifact-pull, and timeout patterns.
- `references/colab-vm-operations.md`
  - Google Colab GPU management and custom VM lifecycle guidance.
- `references/kaggle-2026-practices.md`
  - Current Kaggle platform habits for reproducibility, versioning, and notebook execution.
- `references/cross-repo-cv-patterns.md`
  - Generic patterns for benchmark, trainer, and deploy repos split across one program.
- `references/publication-security.md`
  - Publication checklist for OpenClaw or ClawHub and leak-prevention rules.

## Bundled Scripts

- `scripts/capture_cv_run_context.py`
  - Capture a compact environment, git, GPU, and artifact snapshot.
- `scripts/init_cv_task_scaffold.py`
  - Create a reusable research, plan, journal, and evidence scaffold for a new CV task.
- `scripts/init_cv_run_card.py`
  - Create a machine-readable candidate run card for training, benchmark, and promotion evidence.
- `scripts/init_cv_dataset_manifest.py`
  - Create a reusable dataset identity manifest for shared CV benchmarks and training runs.
- `scripts/init_cv_browser_run_card.py`
  - Create a sanitized browser evidence record for Colab, Kaggle, or other notebook UI runs.
