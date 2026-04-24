# Evals

## Rules

- Every task should name the primary verification step before editing.
- Public-surface changes need leak and evidence-discipline review, not just script compilation.
- Prefer the existing workflow checks before inventing new local harnesses.
- If claim language changes, review whether the required evidence artifacts still match the wording.

## Required checks

- Script compile: `python3 -m py_compile skill/data-science-cv-repro-lab/scripts/*.py skill/sota-agent/scripts/*.py`
- Smoke helpers:

```bash
tmpdir="$(mktemp -d)"
python3 skill/data-science-cv-repro-lab/scripts/capture_cv_run_context.py \
  --repo-root . \
  --out "$tmpdir/cv-run-context.json" \
  --markdown-out "$tmpdir/cv-run-context.md" \
  --label eval \
  --module pip \
  --param lane=eval
python3 skill/data-science-cv-repro-lab/scripts/init_cv_artifact_manifest.py \
  --out "$tmpdir/cv-artifact-manifest.json" \
  --bundle-root skill/data-science-cv-repro-lab \
  --item skill=skill/data-science-cv-repro-lab/SKILL.md
python3 skill/sota-agent/scripts/init_sota_artifact_manifest.py \
  --out "$tmpdir/sota-artifact-manifest.json" \
  --bundle-root skill/sota-agent \
  --item skill=skill/sota-agent/SKILL.md
```

- Public-surface review: confirm no secret-like strings, local paths, browser profile names, private notebook URLs, or customer identifiers were introduced.

## Quality bar

- A broken or drifted validation path is a failure.
- Secret-like strings, tracked private URLs, and unsupported benchmark claims are release blockers.
- Docs and templates count as product surface and must stay aligned with the actual bundle behavior.
