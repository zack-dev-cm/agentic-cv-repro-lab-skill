# Agentic CV Repro Lab Skill

This repo packages a Codex skill for reproducible, agentic computer-vision work:

- browser-driven hypothesis checks in Colab or Kaggle
- explicit Google Colab GPU management
- long-running VM or cluster training with watchdogs and heartbeats
- custom GPU VM lifecycle management
- machine-readable experiment context capture
- promotion decisions gated by benchmark evidence instead of intuition

The skill was generalized from a real multi-repo CV training stack, then scrubbed so it can be published safely and reused by third parties without leaking local paths, internal profile names, or private infrastructure details.

## What Is Included

- `skill/data-science-cv-repro-lab/SKILL.md`
- `skill/data-science-cv-repro-lab/references/official-repro-guidance.md`
- `skill/data-science-cv-repro-lab/references/agentic-research-patterns.md`
- `skill/data-science-cv-repro-lab/references/openclaw-browser-lane.md`
- `skill/data-science-cv-repro-lab/references/colab-vm-operations.md`
- `skill/data-science-cv-repro-lab/references/kaggle-2026-practices.md`
- `skill/data-science-cv-repro-lab/references/cross-repo-cv-patterns.md`
- `skill/data-science-cv-repro-lab/references/publication-security.md`
- `skill/data-science-cv-repro-lab/scripts/capture_cv_run_context.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_task_scaffold.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_run_card.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_dataset_manifest.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_browser_run_card.py`
- `skill/data-science-cv-repro-lab/scripts/render_cv_run_summary.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_artifact_manifest.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_vm_bootstrap_manifest.py`

## Install Into Codex

Copy `skill/data-science-cv-repro-lab` into `$CODEX_HOME/skills/`.

Example:

```bash
mkdir -p "$CODEX_HOME/skills"
rsync -a skill/data-science-cv-repro-lab/ "$CODEX_HOME/skills/data-science-cv-repro-lab/"
```

## Operating Model

1. Initialize the dataset manifest, candidate run card, and browser run card when the notebook UI matters.
2. Capture the run context before touching training.
3. Pick the right lane:
   - local debug lane
   - browser-only Colab or Kaggle lane
   - explicit Colab GPU lane
   - custom VM or cluster long-run lane
   - benchmark or promotion lane
4. Keep every step backed by artifacts:
   - dataset manifests
   - previews
   - metrics CSV or JSON
   - screenshots
   - browser run cards
   - run cards
5. Treat browser LLM advice as hypothesis generation only.
6. Promote only on fixed benchmark wins across every required surface.

## Built-In Helpers

- `capture_cv_run_context.py`: capture git, environment, GPU, and tracked-path state
- `init_cv_task_scaffold.py`: create research, plan, journal, evidence, and promotion docs
- `init_cv_run_card.py`: create a machine-readable candidate run card for benchmark and release review
- `init_cv_dataset_manifest.py`: create a reusable dataset manifest shared across training and evaluation repos
- `init_cv_browser_run_card.py`: create a sanitized browser evidence record for Colab, Kaggle, or other notebook UIs
- `render_cv_run_summary.py`: generate markdown release notes directly from the run card
- `init_cv_artifact_manifest.py`: capture the artifact bundle contents for Colab, Kaggle, or VM export pulls
- `init_cv_vm_bootstrap_manifest.py`: capture the launch metadata for long VM or cluster runs

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

Recommended publish flow:

```bash
clawhub login
export CLAWHUB_DISABLE_TELEMETRY=1
clawhub publish ./skill/data-science-cv-repro-lab \
  --slug data-science-cv-repro-lab \
  --name "Agentic CV Repro Lab" \
  --version 1.4.0 \
  --changelog "Add artifact-manifest and VM-bootstrap helpers for full train-management coverage" \
  --tags latest,computer-vision,reproducibility
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
