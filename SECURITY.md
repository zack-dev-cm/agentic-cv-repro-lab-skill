# Security Policy

This repository publishes two local-first skills and their helper scripts. It does not run a hosted service, but the public bundle can still create security exposure if private material or unsafe defaults are committed.

## Supported versions

Security fixes are applied to the latest release line and default branch only.

## What to report

Treat these as security issues:

- committed secrets, tokens, or credential-bearing files
- leaked absolute paths, browser profile names, private notebook URLs, or customer identifiers
- helper scripts that capture or emit sensitive material by default
- public docs that instruct unsafe credential or evidence handling

## Reporting a vulnerability

Do not open a public GitHub issue first.

Send a private report with:

- affected files or versions
- reproduction steps
- impact assessment
- any proposed mitigation

Use a private GitHub security advisory if the repository has that feature enabled. If it does not, contact the maintainer directly through the GitHub profile associated with the repository.
