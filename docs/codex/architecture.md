# Architecture

## Boundaries

- `skill/data-science-cv-repro-lab/`: run cards, manifests, capture helpers, and promotion-oriented evidence tooling for CV execution.
- `skill/sota-agent/`: benchmark framing, candidate tracking, validation scorecards, and claim-review helpers for SOTA decisions.
- `docs/codex/`: durable repo guidance for OSS packaging, evaluation, and cleanup.
- `.github/`: workflow automation and PR template for public review.
- `.codex/agents/`: narrow repo-specific roles for planning, implementation, review, iteration, and cleanup.

## Shared design rules

- Keep each skill independently installable and reviewable.
- Keep repo-level release rules in top-level docs and templates instead of scattering them through both skills.
- Public text must stay honest about evidence quality, reruns, and claim limits.
- Anything published to GitHub or ClawHub must be safe to expose publicly.

## Do-not-break list

- Public skill folder names: `data-science-cv-repro-lab`, `sota-agent`
- Install and positioning statements in `README.md`
- Validation path in `.github/workflows/validate-skills.yml`
- Release-facing docs in `README.md`, `docs/codex/`, `SECURITY.md`, `CONTRIBUTING.md`, and `.github/pull_request_template.md`
