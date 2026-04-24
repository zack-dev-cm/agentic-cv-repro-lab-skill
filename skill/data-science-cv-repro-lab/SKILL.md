---
name: data-science-cv-repro-lab
description: Data Science CV Repro Lab is a public ClawHub CV repro-lab skill. Use it when the user says "cv repro lab", "computer vision reproducibility", "CV experiment evidence", or wants execution-grade CV experiments and evidence capture across Colab, Kaggle, browser automation, and GPU VMs.
version: 1.9.2
homepage: https://zack-dev-cm.github.io/
user-invocable: true
metadata: {"openclaw":{"homepage":"https://zack-dev-cm.github.io/","skillKey":"data-science-cv-repro-lab","requires":{"anyBins":["python3","python"]}}}
---

# Data Science CV Repro Lab

Search intent: `cv repro lab`, `computer vision reproducibility`, `cv experiment evidence`, `colab kaggle cv workflow`

## Goal

Turn CV work into a reproducible decision loop:

- fixed inputs
- explicit metrics
- durable artifacts
- bounded browser automation
- long-run health monitoring
- promotion only on verified benchmark wins

This skill is the execution and evidence layer, not the full score-improvement stack.
If the real ask is "beat the baseline", "escape a plateau", or "find a better recipe",
pair it with `sota-agent` and a fixed improvement harness before spending more compute.

## Use This Skill When

- the user asks to debug CV training, segmentation, detection, or runtime behavior
- the workflow includes OpenClaw, Colab, Kaggle, or browser-only notebook actions
- you need preprocessing, augmentation, or label-alignment review
- the task requires checkpoint comparisons, export comparisons, or promotion gating
- the user wants VM or GPU watchdog logic, heartbeat files, or auto-stop behavior
- the user wants a general third-party CV workflow, not only repo-specific advice

If the primary goal is benchmark improvement rather than clean execution, route the search loop
through `sota-agent` and use this skill as the execution lane.

## Quick Start

1. Lock the objective before touching code.
   - Write the product problem in one sentence.
   - Name the primary metric.
   - Name the non-regression surfaces.
   - State what blocks promotion.

2. Initialize the durable records immediately.
   - Use `python3 {baseDir}/scripts/init_cv_dataset_manifest.py --out <json> --dataset-id <id>`.
   - Use `python3 {baseDir}/scripts/init_cv_run_card.py --out <json> --candidate-id <id> --task-id <task> --baseline-id <baseline>`.
   - If the task is plateau recovery or benchmark improvement, use `python3 {baseDir}/scripts/init_cv_improvement_harness.py --out <json> --task-id <task> --candidate-family <family>`.
   - If the workflow mixes runtime sweeps, QA runs, benchmark panels, or synced VM artifacts, use `python3 {baseDir}/scripts/init_cv_review_dashboard_manifest.py --out <json> --dashboard-id <id> --title <title>`.
   - If a browser lane matters, use `python3 {baseDir}/scripts/init_cv_browser_run_card.py --out <json> --target-url <url>`.
   - If browser-visible overlays or prompt variants are part of the hypothesis, use `python3 {baseDir}/scripts/init_cv_validation_scorecard.py --out <json> --scorecard-id <id> --surface <surface>`.
   - If a long VM run is involved, use `python3 {baseDir}/scripts/init_cv_vm_bootstrap_manifest.py --out <json> --output-root <run_root> --model-family <name> --command python train.py --epochs 40`.

3. Capture the current state immediately.
   - Use `python3 {baseDir}/scripts/capture_cv_run_context.py --repo-root <repo> --out <json> --markdown-out <md> --param key=value`.
   - Record git state, module versions, GPU state, and experiment params before launch.
   - Use the dataset, artifact, and browser manifest helpers for any additional evidence instead of broad host inspection.

4. Pick the right orchestration lane.
   - Local debug lane: tiny overfit, transform audits, shape and dtype checks.
   - Browser notebook lane: Colab or Kaggle steps that must happen in a real browser or notebook UI.
   - Colab GPU lane: runtime selection, smoke validation, artifact export, and browser evidence.
   - Custom VM or cluster lane: long runs with heartbeats, watchdogs, stall detection, sync, and auto-stop.
   - Review dashboard lane: one local or synced surface for runtime sweeps, QA runs, curated comparisons, and benchmark panels.
   - Promotion lane: fixed benchmark matrix plus customer-facing surface checks.

5. Work the debug ladder in order.
   - `Harness review`: fixed split, primary metric, slice table, rerun rule, and stop condition.
   - `Validation scorecard`: browser or notebook visual QA with per-image pass or fail notes when the UI is part of the release story.
   - `Data audit`: split integrity, label normalization, image-mask pairing, resize geometry.
   - `Preview audit`: at least one augmentation preview and one transformed batch preview.
   - `Failure-set review`: keep 20-50 representative overlays with short notes instead of trusting one scalar metric.
   - `Tiny overfit`: 4-16 shared samples with `no_aug`.
   - `Short resumed run`: continue from the best trusted checkpoint.
   - `Long run`: only after the short loop is healthy.

6. Keep agentic work bounded.
   - External browser LLM output is hypothesis generation, not release evidence.
   - Keep the main thread on the benchmark contract and improvement harness.
   - Use bounded Codex subagents for scouting, data audits, patch proposals, and per-case review.
   - For repeated case review, batch over a manifest or CSV instead of free-form chat drift.
   - Browser steps must emit screenshots, machine-readable scores, and explicit success markers.
   - Hard-fail on unavailable browser modes, dead CDP sessions, or ambiguous notebook state.
   - Keep planner, executor, reviewer, and promoter responsibilities distinct even if one agent performs more than one role.

7. Promote only on full-surface wins.
   - Raw checkpoint quality
   - Exported or runtime quality
   - User-facing render, service, or product surface
   - Runtime cost or throughput if deployment matters
   - Adjacent-seed or rerun stability if the claimed delta is small
   - Generate a promotion bundle with `python3 {baseDir}/scripts/init_cv_promotion_bundle.py --out <json> --candidate-id <id>` before the final decision.

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
- When the hypothesis depends on visible overlays, grids, or prompt variants, capture a validation scorecard before the long run.
- Capture at least two screenshots when the browser UI is part of the validation path.
- Pull artifacts back locally as files, not only screenshots.
- Use explicit timeout and marker logic; do not rely on visual guesswork.
- Record browser profile aliases and session aliases in durable artifacts; keep raw CDP URLs in ephemeral local debug logs only.

### Colab GPU rules

- Select the accelerator explicitly before running expensive cells.
- Verify GPU readiness from inside the notebook before the long run.
- Use a smoke cell that proves the runtime, imports, and data mounts all work.
- Export all required artifacts to one stable bundle directory.
- Create an artifact manifest for that export bundle before pulling it back locally.
- Pull the artifact manifest plus at least one preview image back to local storage.

### Custom VM and cluster rules

- Create a named run root before launch.
- Write a machine-readable bootstrap manifest with commit, dataset, env, and command details.
- Run long jobs under a session, heartbeat, or supervisor so liveness is explicit.
- Track GPU utilization, epoch movement, and log freshness.
- Sync summaries and checkpoints back to local storage on a schedule.
- Auto-stop or downgrade to a debug path when the run is clearly unhealthy.

### Review dashboard rules

- Use one review dashboard manifest when the program spans runtime sweeps, QA runs, benchmark panels, and synced VM artifacts.
- Track summary roots, benchmark roots, allowed roots, and sync targets explicitly instead of relying on memory.
- Keep source-audit, leakage-audit, progress-snapshot, and comparison-summary paths next to the dashboard manifest.
- Count runtime groups, QA runs, curated comparisons, and benchmark panels so the review surface stays legible as the program grows.
- Promote from synced artifacts and run cards, not from a live dashboard alone.

### CV training rules

- Do not change architecture first.
- Prove learning on a tiny shared subset before scaling.
- Save previews in the same run folder as metrics and summaries.
- Do not compare candidates on different benchmark sets.

### Plateau recovery rules

- If Dice or another primary metric is stuck, freeze the benchmark contract and write the improvement harness before another long run.
- Require per-slice metrics, a short failure taxonomy, and a rerun rule before claiming a real win.
- Keep a small, reviewable change set for each serious candidate. If several knobs move together, mark it as a package change instead of an ablation.
- Cut a recipe family after a few non-winning serious candidates instead of rerunning the same idea with cosmetic churn.

### Derm and segmentation rules

- Before architecture changes, audit mask geometry, resize policy, interpolation, empty-mask prevalence, and overlay alignment.
- For derm or lesion segmentation, slice the benchmark by lesion size, border difficulty, artifact-heavy images, and background-dominant images.
- Global Dice is not enough. Keep boundary-sensitive or slice-specific diagnostics so a hidden failure mode does not look like a flat plateau.
- Preserve a 20-50 case review set with saved overlays and short reviewer notes.

### Codex and auth rules

- Use ChatGPT or Codex OAuth-backed sessions as the default and preferred path.
- Prefer Codex multi-agent or app-server workflows over third-party orchestrators that require paid API keys.
- Do not require or recommend `OPENAI_API_KEY`, other vendor API keys, or paid inference APIs as the default runtime path.
- If a third-party framework only works through paid API keys, treat it as reference material unless you can run it fully through local tools and OAuth-backed Codex sessions.

### Promotion rules

- Keep the last trusted baseline intact until the candidate clears agreed gates.
- Separate semantic, runtime, and product-surface gates when deployment or export changes are involved.
- If the semantic model improves but the deployed overlay or service output regresses, fix the downstream path before promotion.
- Prefer a machine-readable run card plus a short markdown summary.
- Initialize that run card before or at launch time so later steps append to one canonical record.
- Render the markdown summary from the run card instead of hand-writing it when possible.
- Keep the default redacted-public markdown rendering in place.

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
- `references/improvement-harness-and-oauth-stack.md`
  - What to reuse from Codex subagents, harness engineering, OpenEvolve, Symphony, Paperclip, and OptiLLM under an OAuth-only rule.
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
- `references/runtime-serving-change-gates.md`
  - How to separate semantic, runtime, and product-surface gates for deployment-shaped releases.

## Bundled Scripts

- `scripts/capture_cv_run_context.py`
  - Capture a compact git, module, GPU, and experiment-param snapshot.
- `scripts/init_cv_task_scaffold.py`
  - Create a reusable research, harness, ablation, agent, plan, journal, and evidence scaffold for a new CV task.
- `scripts/init_cv_run_card.py`
  - Create a machine-readable candidate run card for training, benchmark, and promotion evidence.
- `scripts/init_cv_improvement_harness.py`
  - Create a machine-readable benchmark, slice, rerun, and auth contract for plateau recovery and score-improvement work.
- `scripts/init_cv_review_dashboard_manifest.py`
  - Create a machine-readable review dashboard manifest for runtime sweeps, QA runs, benchmark panels, sync targets, and audit surfaces.
- `scripts/init_cv_dataset_manifest.py`
  - Create a reusable dataset identity manifest for shared CV benchmarks and training runs.
- `scripts/init_cv_browser_run_card.py`
  - Create a sanitized browser evidence record for Colab, Kaggle, or other notebook UI runs.
- `scripts/init_cv_validation_scorecard.py`
  - Create a machine-readable pre-training QA scorecard for browser or notebook hypothesis checks.
- `scripts/render_cv_run_summary.py`
  - Render a concise markdown release summary from the machine-readable run card with public-release redaction.
- `scripts/init_cv_artifact_manifest.py`
  - Create a machine-readable export-bundle manifest for Colab, Kaggle, or VM artifact pulls with redacted public path metadata.
- `scripts/init_cv_vm_bootstrap_manifest.py`
  - Create a machine-readable bootstrap manifest for long VM or cluster training runs with public-release command redaction.
- `scripts/init_cv_promotion_bundle.py`
  - Create one promotion entry point that joins semantic, runtime, browser, and product-surface evidence.
