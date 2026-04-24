# Cleanup

Codex can create entropy quickly in a public skills repo. This file defines the cleanup cadence.

## Weekly sweep

- Remove stale release notes, copied notebooks, temporary manifests, and generated artifacts that do not belong in source control.
- Refresh docs and templates that drifted from `README.md` or `.github/workflows/validate-skills.yml`.
- Re-check public wording for unsupported claim language or stale package-version references.
- Re-run the baseline compile and smoke checks after meaningful script cleanup.

## Promote a rule when

- The same leak or bleed issue appears more than once.
- Review repeatedly asks for the same public metadata or validation detail.
- A stale doc or template creates a false first-run path.

## Do not do

- Opportunistic rewrites under the label of cleanup.
- Private note dumps, notebook links, or environment details in public docs.
- Cross-skill abstractions that blur the product boundaries without a clear maintenance win.
