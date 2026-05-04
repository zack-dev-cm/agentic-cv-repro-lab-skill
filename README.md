# CV Repro Lab Skills

**Run CV experiments reproducibly across Colab, Kaggle, browser workflows, and GPU VMs, then decide whether a result is strong enough to promote.**

CV Repro Lab Skills packages two public OpenClaw/Codex skills:

- `data-science-cv-repro-lab`: run experiments, capture browser and notebook evidence, and bundle results for review
- `sota-agent`: define the benchmark, rank candidates, and decide whether a claimed gain is real

Use both together when you want one planning lane and one execution lane:

- `sota-agent` freezes the benchmark, candidate list, rerun policy, and claim rules before more compute gets spent
- `data-science-cv-repro-lab` executes runs across Colab, Kaggle, browser-heavy workflows, or VMs and captures the evidence needed to promote or reject the result

## Which Skill Should I Use?

### `data-science-cv-repro-lab`

Use it when you need:

- Colab, Kaggle, or VM execution discipline
- browser evidence and validation scorecards
- dataset manifests, run cards, and promotion bundles
- reproducible artifact capture for a real training or export lane

### `sota-agent`

Use it when you need:

- a fixed benchmark before spending more compute
- literature triage and candidate ranking
- ablation discipline and rerun policy for small deltas
- an honest claim decision instead of benchmark theater

## Quick Start

Install from ClawHub or copy the skill folders into `$CODEX_HOME/skills/`.

```bash
mkdir -p "$CODEX_HOME/skills"
rsync -a skill/data-science-cv-repro-lab/ "$CODEX_HOME/skills/data-science-cv-repro-lab/"
rsync -a skill/sota-agent/ "$CODEX_HOME/skills/sota-agent/"
```

## Live Packages

- [CV Repro Lab on ClawHub](https://clawhub.ai/zack-dev-cm/data-science-cv-repro-lab) (`v1.9.1`)
- [SOTA Agent on ClawHub](https://clawhub.ai/zack-dev-cm/sota-agent) (`v1.4.4`)
- [Portfolio entry](https://zack-dev-cm.github.io/projects/cv-repro-lab-skills.md)

## What Changed In This Release

- added an explicit improvement harness for plateau recovery and score-improvement work
- added a review-dashboard manifest for synced QA runs, benchmark panels, runtime sweeps, and audit surfaces
- expanded run cards and candidate/program records with reruns, slices, agent threads, and auth policy
- added explicit dashboard, source-audit, and leakage-audit references to the SOTA claim surface
- added redacted public summary rendering for the richer machine-readable records
- made local-first planning and public artifact review the default public story instead of API-key-first tooling

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

Report security issues privately using the contact path in [SECURITY.md](SECURITY.md) instead of filing a public issue with sensitive details.

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
