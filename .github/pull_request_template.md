## Summary

- what changed
- why it changed

## Validation

- [ ] `python3 -m py_compile skill/data-science-cv-repro-lab/scripts/*.py skill/sota-agent/scripts/*.py`
- [ ] `python3 -m pytest -q`
- [ ] `python3 -m codex_harness audit . --strict --min-score 90` run locally, or the reason it could not be run is explained
- [ ] Public helper smoke path run locally or equivalent verification explained
- [ ] Docs or templates updated if the public surface changed
- [ ] Security, leak, bleed, and evidence-discipline review completed
- [ ] No secrets, private notebook URLs, local paths, browser profile names, or customer identifiers were introduced

## Notes

- tradeoffs, assumptions, or follow-up work
