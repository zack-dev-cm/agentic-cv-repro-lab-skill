# Contributing

This repository is a public skill bundle, not a generic ML framework. Contributions should improve one of the two shipped skills or the release scaffolding around them without weakening evidence discipline.

## Contribution bar

- the change solves a real public-use problem
- the public story stays honest about what the repo does and does not guarantee
- validation stays cheap enough to run locally
- docs, templates, and manifests remain safe to publish

## Local setup

This repo does not require an install step for the baseline checks. Use Python 3.11 or newer and run:

```bash
python3 -m py_compile \
  skill/data-science-cv-repro-lab/scripts/*.py \
  skill/sota-agent/scripts/*.py

python3 -m pytest -q

tmpdir="$(mktemp -d)"
python3 skill/data-science-cv-repro-lab/scripts/capture_cv_run_context.py \
  --repo-root . \
  --out "$tmpdir/cv-run-context.json" \
  --markdown-out "$tmpdir/cv-run-context.md" \
  --label local \
  --module pip \
  --param lane=local
python3 skill/data-science-cv-repro-lab/scripts/init_cv_artifact_manifest.py \
  --out "$tmpdir/cv-artifact-manifest.json" \
  --bundle-root skill/data-science-cv-repro-lab \
  --item skill=skill/data-science-cv-repro-lab/SKILL.md
python3 skill/sota-agent/scripts/init_sota_artifact_manifest.py \
  --out "$tmpdir/sota-artifact-manifest.json" \
  --bundle-root skill/sota-agent \
  --item skill=skill/sota-agent/SKILL.md
```

Before a public release, also run `python3 -m codex_harness audit . --strict --min-score 90` when the release-audit helper is available locally.

## Typical contribution types

- tighter helper scripts, manifests, and summaries inside a skill bundle
- docs or template updates that improve OSS review readiness
- leak and evidence-discipline hardening for public examples
- clearer release guidance for GitHub or ClawHub users

## Guidelines

1. Keep the change small and legible.
2. Keep `data-science-cv-repro-lab` and `sota-agent` clearly separated unless shared behavior is truly necessary.
3. Update docs or templates when the public surface changes.
4. Add or expand validation when behavior changes.
5. Do not commit secrets, private notebook URLs, local paths, browser profile names, or customer identifiers.
6. If a change affects evaluation claims, explain what evidence should now exist to support the claim.
