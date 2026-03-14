# Publication Security

Use this reference before publishing the skill to OpenClaw or ClawHub.

## ClawHub fact

ClawHub is public. Published skills and their `SKILL.md` content are visible to everyone.

Source:
- https://docs.openclaw.ai/tools/clawhub

## What must not ship

- secrets, tokens, API keys, passwords
- private browser profile names
- private notebook URLs
- internal hostnames or VM names
- absolute local filesystem paths
- private dataset slugs or customer identifiers
- command examples that embed credentials in flags

## OpenClaw-specific safety rules

- Keep secrets out of prompts and logs.
- Treat third-party skills as untrusted code.
- Prefer sandboxed runs for risky tools.
- Keep skill config secrets in `skills.entries.*.env` or `apiKey`, not in the skill files.

Source:
- https://docs.openclaw.ai/tools/skills

## Review checklist

1. Search for absolute paths.
2. Search for usernames, profile names, and internal URLs.
3. Search for notebook ids and dataset ids that are not intended to be public.
4. Search for token-like strings and secret-shaped env vars.
5. Ensure bundled scripts do not combine env harvesting with network exfiltration.
6. Ensure the skill uses `{baseDir}` for bundled file references.
7. If private specialization is still needed, keep it in a local override skill instead of the public bundle.

## Practical audit commands

Run these before publishing:

```bash
rg -n "/Users/|/home/|localhost|127\\.0\\.0\\.1|token|api[_-]?key|secret|password" ./skill
python3 -m py_compile ./skill/*/scripts/*.py
diff -r ./skill/data-science-cv-repro-lab ~/.codex/skills/data-science-cv-repro-lab
```
