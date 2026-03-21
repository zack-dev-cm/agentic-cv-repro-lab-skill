# Agentic CV Repro Lab Skills

This repo packages two public Codex skills for DS and CV work:

- `data-science-cv-repro-lab`: execution-grade browser, notebook, VM, and promotion workflows for CV experimentation
- `sota-agent`: benchmark-governance and OpenClaw execution workflows for pushing DS and CV work toward defensible SOTA claims across browser notebooks and GPU VMs

The first skill handles execution and evidence capture. The second handles frontier targeting, paper triage, ablations, scoreboard discipline, and claim review.

Both skills were generalized from a real multi-repo CV training stack, then scrubbed so they can be published safely and reused without leaking local paths, internal profile names, or private infrastructure details.

## Live Packages

- [Agentic CV Repro Lab on ClawHub](https://clawhub.ai/zack-dev-cm/data-science-cv-repro-lab) (`v1.7.2`)
- [SOTA Agent on ClawHub](https://clawhub.ai/zack-dev-cm/sota-agent) (`v1.2.3`)
- [Portfolio entry](https://zack-dev-cm.github.io/projects/agentic-cv-repro-lab-skill.md)

## What Is Included

- `skill/data-science-cv-repro-lab/SKILL.md`
- `skill/data-science-cv-repro-lab/references/official-repro-guidance.md`
- `skill/data-science-cv-repro-lab/references/agentic-research-patterns.md`
- `skill/data-science-cv-repro-lab/references/openclaw-browser-lane.md`
- `skill/data-science-cv-repro-lab/references/colab-vm-operations.md`
- `skill/data-science-cv-repro-lab/references/kaggle-2026-practices.md`
- `skill/data-science-cv-repro-lab/references/cross-repo-cv-patterns.md`
- `skill/data-science-cv-repro-lab/references/publication-security.md`
- `skill/data-science-cv-repro-lab/references/runtime-serving-change-gates.md`
- `skill/data-science-cv-repro-lab/scripts/capture_cv_run_context.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_task_scaffold.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_run_card.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_dataset_manifest.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_browser_run_card.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_validation_scorecard.py`
- `skill/data-science-cv-repro-lab/scripts/render_cv_run_summary.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_artifact_manifest.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_vm_bootstrap_manifest.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_promotion_bundle.py`
- `skill/sota-agent/SKILL.md`
- `skill/sota-agent/references/sota-campaign-playbook.md`
- `skill/sota-agent/references/sota-program-rules.md`
- `skill/sota-agent/references/benchmark-discipline.md`
- `skill/sota-agent/references/paper-triage.md`
- `skill/sota-agent/references/openclaw-research-lane.md`
- `skill/sota-agent/references/openclaw-browser-lane.md`
- `skill/sota-agent/references/colab-vm-operations.md`
- `skill/sota-agent/references/claim-safety.md`
- `skill/sota-agent/references/public-safety.md`
- `skill/sota-agent/scripts/init_sota_browser_run_card.py`
- `skill/sota-agent/scripts/init_sota_validation_scorecard.py`
- `skill/sota-agent/scripts/init_sota_artifact_manifest.py`
- `skill/sota-agent/scripts/init_sota_vm_bootstrap_manifest.py`
- `skill/sota-agent/scripts/init_sota_campaign.py`
- `skill/sota-agent/scripts/init_sota_program.py`
- `skill/sota-agent/scripts/init_sota_leaderboard_snapshot.py`
- `skill/sota-agent/scripts/init_sota_paper_triage.py`
- `skill/sota-agent/scripts/init_sota_candidate_card.py`
- `skill/sota-agent/scripts/init_sota_candidate.py`
- `skill/sota-agent/scripts/init_sota_ablation_queue.py`
- `skill/sota-agent/scripts/update_sota_scoreboard.py`
- `skill/sota-agent/scripts/init_sota_review_packet.py`
- `skill/sota-agent/scripts/render_sota_claim_summary.py`
- `skill/sota-agent/scripts/render_sota_program_summary.py`
- `skill/sota-agent/scripts/sota_public_safety.py`

## Install Into Codex

Install from ClawHub or copy the skill you want into `$CODEX_HOME/skills/`.

Example:

```bash
mkdir -p "$CODEX_HOME/skills"
rsync -a skill/data-science-cv-repro-lab/ "$CODEX_HOME/skills/data-science-cv-repro-lab/"
rsync -a skill/sota-agent/ "$CODEX_HOME/skills/sota-agent/"
```

## Operating Model

1. Initialize the dataset manifest, candidate run card, and browser run card when the notebook UI matters.
2. If the hypothesis depends on browser-visible overlays, grids, or prompt variants, create a validation scorecard before long training.
3. Treat the short smoke loop as mandatory:
   - preview audit
   - tiny subset run
   - short resumed run
   - only then full training
4. Separate release truth into three surfaces:
   - semantic checkpoint quality
   - runtime or staged-service quality
   - product-surface quality
5. Capture the run context before touching training.
6. Pick the right lane:
   - local debug lane
   - browser-only Colab or Kaggle lane
   - explicit Colab GPU lane
   - custom VM or cluster long-run lane
   - benchmark or promotion lane
7. Keep every step backed by artifacts:
   - dataset manifests
   - previews
   - validation scorecards
   - metrics CSV or JSON
   - screenshots
   - browser run cards
   - run cards
   - promotion bundles
8. Treat browser LLM advice as hypothesis generation only.
9. Promote only on fixed benchmark wins across every required surface.

## Built-In Helpers

- `capture_cv_run_context.py`: capture git, module, GPU, and experiment-param state
- `init_cv_task_scaffold.py`: create research, plan, journal, evidence, and promotion docs
- `init_cv_run_card.py`: create a machine-readable candidate run card for benchmark and release review
- `init_cv_dataset_manifest.py`: create a reusable dataset manifest shared across training and evaluation repos
- `init_cv_browser_run_card.py`: create a sanitized browser evidence record for Colab, Kaggle, or other notebook UIs
- `init_cv_validation_scorecard.py`: create a per-image browser or notebook scorecard for pre-training QA and short smoke checks
- `render_cv_run_summary.py`: generate markdown release notes directly from the run card
- `init_cv_artifact_manifest.py`: capture the artifact bundle contents for Colab, Kaggle, or VM export pulls
- `init_cv_vm_bootstrap_manifest.py`: capture the launch metadata for long VM or cluster runs
- `init_cv_promotion_bundle.py`: join semantic, runtime, browser, and product-surface artifacts into one promotion entry point

## Public Positioning

This bundle is meant to be public and reusable. The OpenClaw skill is exposed as a user-invocable command, so it can be discovered both by model routing and by explicit user invocation.

Recommended GitHub repository topics:

- `openclaw`
- `clawhub`
- `llm-agents`
- `computer-vision`
- `data-science`
- `reproducibility`
- `google-colab`
- `kaggle`
- `browser-automation`
- `benchmarking`
- `gpu-training`
- `mlops`
- `agentic-workflows`

ClawHub tags in the live listings:

- `data-science-cv-repro-lab`: `latest`, `computer-vision`, `data-science`, `reproducibility`, `colab`, `kaggle`, `gpu-training`, `openclaw`, `mlops`, `agentic-workflows`
- `sota-agent`: `latest`, `computer-vision`, `data-science`, `benchmarking`, `reproducibility`, `colab`, `kaggle`, `gpu-training`, `openclaw`, `mlops`, `agentic-workflows`

## OpenClaw And ClawHub Publication

OpenClaw skill format and gating details:

- [Skills](https://docs.openclaw.ai/tools/skills)
- [Creating skills](https://docs.openclaw.ai/tools/creating-skills)
- [ClawHub](https://docs.openclaw.ai/tools/clawhub)

ClawHub is public by default. Before publishing, keep the bundle free of:

- absolute local filesystem paths
- usernames and browser profile names
- private notebook URLs
- internal hostnames and VM names
- secrets, tokens, dataset credentials, or account IDs

If you need a private specialization for one company or repo, keep it as a local override in `~/.openclaw/skills` or `<workspace>/skills`, not in the public bundle.

Recommended release checklist:

1. Complete the publication review checklist from `references/publication-security.md`.
2. Confirm the skill still exposes the public-friendly slash command and UI metadata.
3. Apply the GitHub repository topics listed above and keep the repo homepage pointed at the public portfolio page.
4. Publish to ClawHub with the tag set listed above.
5. Review the changelog text one more time for customer names, private infra labels, or leaked URLs.

## Repository Validation

This repo is prepared to be public:

- the public skill bundles avoid repo-specific absolute paths and raw notebook or CDP endpoints
- the GitHub Actions workflow compiles all bundled scripts and runs basic smoke tests
- `.gitignore` blocks local env files, logs, and Python bytecode from being committed
- the repo README, GitHub topics, and ClawHub listings are kept aligned to the live public skill versions

Recommended publish flow:

```bash
clawhub login
export CLAWHUB_DISABLE_TELEMETRY=1
clawhub publish ./skill/data-science-cv-repro-lab \
  --slug data-science-cv-repro-lab \
  --name "Agentic CV Repro Lab" \
  --version 1.7.2 \
  --changelog "Stop importing ML packages for version capture and reduce public artifact metadata" \
  --tags latest,computer-vision,data-science,reproducibility,colab,kaggle,gpu-training,openclaw,mlops,agentic-workflows

clawhub publish ./skill/sota-agent \
  --slug sota-agent \
  --name "SOTA Agent" \
  --version 1.2.3 \
  --changelog "Make the public redaction helper explicit and tighten workspace path guidance" \
  --tags latest,computer-vision,data-science,benchmarking,reproducibility,colab,kaggle,gpu-training,openclaw,mlops,agentic-workflows
```

## Why This Exists

The common failure mode in agentic CV work is not lack of model ideas. It is loss of provenance:

- no stable benchmark set
- no dataset or model version pinning
- no screenshots from browser-only flows
- no heartbeat or watchdog on long runs
- no clean separation between research notes and promotion evidence

This skill encodes guardrails for those failure modes.

## References

This skill is not a verbatim port of any single project. It is a practical synthesis of public references, official tooling guidance, and a real multi-repo CV operating model.

Research lineage and direct references:

- Andrej Karpathy, [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch)
  - cited here because the skill adapts its planner/searcher/reviewer separation into DS and CV experiment management
- [OpenClaw Skills](https://docs.openclaw.ai/tools/skills)
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills)
- [OpenClaw ClawHub](https://docs.openclaw.ai/tools/clawhub)
- [KaggleHub README](https://github.com/Kaggle/kagglehub)
- [Kaggle docker-python releases](https://github.com/Kaggle/docker-python/releases)
- [Kaggle dataset metadata docs](https://github.com/Kaggle/kaggle-api/blob/main/docs/datasets_metadata.md)
- [Kaggle model metadata docs](https://github.com/Kaggle/kaggle-api/blob/main/docs/models_metadata.md)
- [Kaggle kernel metadata docs](https://github.com/Kaggle/kaggle-api/blob/main/docs/kernels_metadata.md)
- [PyTorch reproducibility notes](https://docs.pytorch.org/docs/stable/notes/randomness.html)
- [Albumentations segmentation guidance](https://albumentations.ai/docs/3-basic-usage/semantic-segmentation/)
- [MLflow tracking quickstart](https://mlflow.org/docs/latest/ml/tracking/quickstart/)
