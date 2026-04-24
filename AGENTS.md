# AGENTS.md

This repository packages two public skills: `data-science-cv-repro-lab` and `sota-agent`. Use this file as the index, not as the full manual.

## Operating rules

- Restate the user goal and name the verification step before editing files.
- Keep diffs surgical. Do not refactor adjacent surfaces unless the task needs it.
- Preserve the split between the two skills and the top-level release scaffolding. Shared rules belong in repo docs and templates, not duplicated ad hoc.
- Treat public-surface review as part of the default loop. New docs, examples, manifests, and templates must clear leak, bleed, and evidence-discipline checks.
- Do not publish absolute local paths, browser profile names, private notebook URLs, secrets, customer identifiers, or unsupported claim language.
- Put durable repo knowledge in `docs/codex/`. Keep this file short.

## Repo map

- [Overview](docs/codex/overview.md)
- [Architecture](docs/codex/architecture.md)
- [Workflow](docs/codex/workflow.md)
- [Evals](docs/codex/evals.md)
- [Cleanup](docs/codex/cleanup.md)

## Main code paths

- `skill/data-science-cv-repro-lab/`: execution-lane skill for reproducible CV runs, evidence capture, and promotion bundles.
- `skill/sota-agent/`: planning and review-lane skill for benchmark freeze, candidate triage, and claim decisions.
- `docs/codex/`: durable OSS packaging and review guidance for this repository.
- `.github/`: public-release workflow and pull request template.
- `.codex/agents/`: focused repo-local agent prompts.

## Default verification

1. Run `python3 -m py_compile skill/data-science-cv-repro-lab/scripts/*.py skill/sota-agent/scripts/*.py`.
2. Run `python3 -m pytest -q`.
3. Run the public helper smoke path from `.github/workflows/validate-skills.yml`.
4. If `codex_harness` is available locally, run `python3 -m codex_harness audit . --strict --min-score 90`.
5. Review changed public files for secrets, private paths, private URLs, customer data, and evidence drift.

## Project-scoped custom agents

- `.codex/agents/architect.toml`
- `.codex/agents/implementer.toml`
- `.codex/agents/reviewer.toml`
- `.codex/agents/evolver.toml`
- `.codex/agents/cleanup.toml`
