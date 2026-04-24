# Workflow

## Default loop

1. Clarify which surface is in scope: top-level scaffolding, one skill bundle, or both.
2. Read the smallest relevant set of docs, templates, and helper scripts.
3. Implement the smallest durable change.
4. Review for correctness, regressions, secret leaks, public-surface bleed, and evidence-discipline drift.
5. Run the highest-signal local checks that match the changed surface.
6. Update release-facing docs and templates when the repo now relies on a new durable rule.

## Open-source prep loop

1. Harden metadata: `README.md`, `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, and `docs/codex/`.
2. Harden public packaging: keep install paths, bundle names, and workflow checks aligned.
3. Harden evidence: prefer manifests, scorecards, and rerun rules over screenshot-only claims.
4. Harden examples: remove private notebook URLs, browser profile names, local paths, and customer details.
5. Keep private specializations in local overrides, not in the public repository.

## When to use which agent

- `architect`: scope cuts, repo boundary questions, and acceptance criteria.
- `implementer`: focused doc, template, script, or scaffolding patches.
- `reviewer`: final correctness, security, leak, and public-surface review.
- `evolver`: measured iteration on prompts, helper wording, or evaluation-facing ergonomics.
- `cleanup`: entropy reduction, stale artifact removal, and repeated review-fix consolidation.
