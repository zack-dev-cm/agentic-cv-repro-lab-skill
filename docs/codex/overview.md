# Overview

This repository packages two public skills for reproducible computer-vision work and honest benchmark review.

## Products

- `data-science-cv-repro-lab`: execution-lane skill for Colab, Kaggle, browser-heavy, and VM-backed CV runs with evidence capture.
- `sota-agent`: planning and review-lane skill for benchmark freeze, candidate triage, rerun discipline, and claim decisions.

## Repo landmarks

- Skill bundles: `skill/data-science-cv-repro-lab/`, `skill/sota-agent/`
- Docs: `README.md`, `docs/codex/`, `SECURITY.md`, `CONTRIBUTING.md`
- GitHub automation: `.github/workflows/`, `.github/pull_request_template.md`
- Repo-local agents: `.codex/agents/`

## Standard checks

- Compile bundled scripts: `python3 -m py_compile skill/data-science-cv-repro-lab/scripts/*.py skill/sota-agent/scripts/*.py`
- Smoke test the public helpers using the commands from `.github/workflows/validate-skills.yml`
- Review public docs and manifests for leaks, unsupported claims, and stale release guidance

## Non-goals

- This repo is not a hosted training platform or experiment tracker.
- It does not guarantee benchmark gains by itself.
- It should not ship private notebook links, credential workflows, or customer-specific playbooks as part of the public bundle.
