# Cross-Repo CV Patterns

Use this reference when one CV program is split across multiple repos.

## Common Split

One program often ends up split like this:

- benchmark or decision repo
- trainer or experimentation repo
- deploy or service repo

That split is acceptable only if provenance survives the boundaries.

## Required shared identity

Every candidate should carry enough metadata to reconnect all repos:

- benchmark repo commit
- trainer repo commit
- deploy repo commit
- dataset manifest id
- checkpoint id
- export id
- promotion decision id

## Best practice

Create one canonical run card that joins:

- training config
- output roots
- benchmark table
- runtime export result
- user-facing gate result
- final decision

Generate human-readable markdown from that run card instead of hand-writing the whole story each time.

## Failure pattern to avoid

Avoid this state:

- training details live in repo A docs
- deployment details live in repo B docs
- screenshots live in a temp folder
- final promotion decision lives only in chat history

That state does not survive future agent turns.
