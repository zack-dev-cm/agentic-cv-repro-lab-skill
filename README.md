# CV Repro Lab Skills

**Benchmark-gated CV skills for execution lanes and SOTA campaigns.**

Two public OpenClaw/Codex skills for CV and data-science experimentation:

- `data-science-cv-repro-lab`: execution lane for browser evidence, Colab/Kaggle runs, VM runs, and promotion bundles
- `sota-agent`: benchmark lane for paper triage, candidate ranking, ablation discipline, and claim review

Use both together when the real task is plateau recovery or a benchmark push: `sota-agent` freezes the
campaign contract and ranks candidates; `data-science-cv-repro-lab` executes the runs and captures the
evidence needed to promote or reject a result.

## Live Packages

- [CV Repro Lab on ClawHub](https://clawhub.ai/zack-dev-cm/data-science-cv-repro-lab) (`v1.9.1`)
- [SOTA Agent on ClawHub](https://clawhub.ai/zack-dev-cm/sota-agent) (`v1.4.1`)
- [Portfolio entry](https://zack-dev-cm.github.io/projects/cv-repro-lab-skills.md)

## Quick Start

Install from ClawHub or copy the skill folders into `$CODEX_HOME/skills/`.

```bash
mkdir -p "$CODEX_HOME/skills"
rsync -a skill/data-science-cv-repro-lab/ "$CODEX_HOME/skills/data-science-cv-repro-lab/"
rsync -a skill/sota-agent/ "$CODEX_HOME/skills/sota-agent/"
```

## What Changed In This Release

- added an explicit improvement harness for plateau recovery and score-improvement work
- added a review-dashboard manifest for synced QA runs, benchmark panels, runtime sweeps, and audit surfaces
- expanded run cards and candidate/program records with reruns, slices, agent threads, and auth policy
- added explicit dashboard, source-audit, and leakage-audit references to the SOTA claim surface
- added redacted public summary rendering for the richer machine-readable records
- made OAuth-backed ChatGPT/Codex paths the default public story instead of API-key-first tooling

## When To Use Which Skill

### `data-science-cv-repro-lab`

Use it when you need:

- Colab, Kaggle, or VM execution discipline
- browser evidence and validation scorecards
- dataset manifests, run cards, and promotion bundles
- reproducible artifact capture for a real training or export lane

### `sota-agent`

Use it when you need:

- a fixed benchmark contract before spending more compute
- literature triage and candidate ranking
- ablation discipline and rerun policy for small deltas
- an honest claim decision instead of benchmark theater

## Good Public Fit

These skills are strongest when the user already has a real CV or DS workflow and wants a drop-in
research harness around it. Good fits include:

- derm or segmentation plateau recovery
- browser-heavy notebook workflows
- benchmark campaigns that need stronger promotion gates
- public or reusable experiment-management patterns across repos

## Public Safety

ClawHub is public. Keep the published skill bundles free of:

- absolute local paths
- browser profile names
- private notebook URLs
- secrets, tokens, and customer identifiers
- internal hostnames or VM labels

Private specializations should stay in local override skills, not in the public package.

## Local Validation

```bash
python3 -m py_compile \
  skill/data-science-cv-repro-lab/scripts/*.py \
  skill/sota-agent/scripts/*.py

python3 skill/data-science-cv-repro-lab/scripts/init_cv_improvement_harness.py \
  --out /tmp/cv-harness.json \
  --task-id demo \
  --candidate-family baseline-recovery

python3 skill/data-science-cv-repro-lab/scripts/init_cv_review_dashboard_manifest.py \
  --out /tmp/cv-dashboard.json \
  --dashboard-id demo-dashboard \
  --title "Demo review dashboard"

python3 skill/sota-agent/scripts/init_sota_program.py \
  --out /tmp/sota-program.json \
  --campaign-id demo \
  --task demo \
  --metric score
```

## References

The public bundle is informed by:

- [karpathy/autoresearch](https://github.com/karpathy/autoresearch)
- [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve)
- [algorithmicsuperintelligence/optillm](https://github.com/algorithmicsuperintelligence/optillm)
- [openai/symphony](https://github.com/openai/symphony)
- [OpenAI harness engineering](https://openai.com/index/harness-engineering/)
- [OpenClaw skills docs](https://docs.openclaw.ai/tools/skills)
