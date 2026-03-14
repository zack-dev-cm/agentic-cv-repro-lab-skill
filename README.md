# Agentic CV Repro Lab Skill

This repo packages a Codex skill for reproducible, agentic computer-vision work:

- browser-driven hypothesis checks in Colab or Kaggle
- long-running VM or cluster training with watchdogs and heartbeats
- machine-readable experiment context capture
- promotion decisions gated by benchmark evidence instead of intuition

The skill was extracted from the `derm` and `poreswrinkles` wrinkle-training workflow, then generalized so a third party can reuse the same operating model without inheriting repo-specific assumptions.

## What Is Included

- `skill/data-science-cv-repro-lab/SKILL.md`
- `skill/data-science-cv-repro-lab/references/official-repro-guidance.md`
- `skill/data-science-cv-repro-lab/references/agentic-research-patterns.md`
- `skill/data-science-cv-repro-lab/references/openclaw-browser-lane.md`
- `skill/data-science-cv-repro-lab/references/kaggle-2026-practices.md`
- `skill/data-science-cv-repro-lab/references/wrinkle-stack-playbook.md`
- `skill/data-science-cv-repro-lab/scripts/capture_cv_run_context.py`
- `skill/data-science-cv-repro-lab/scripts/init_cv_task_scaffold.py`

## Install Into Codex

Copy `skill/data-science-cv-repro-lab` into `$CODEX_HOME/skills/`.

Example:

```bash
mkdir -p "$CODEX_HOME/skills"
rsync -a skill/data-science-cv-repro-lab/ "$CODEX_HOME/skills/data-science-cv-repro-lab/"
```

## Operating Model

1. Capture the run context before touching training.
2. Pick the right lane:
   - local debug lane
   - browser-only Colab or Kaggle lane
   - VM or cluster long-run lane
   - benchmark or promotion lane
3. Keep every step backed by artifacts:
   - previews
   - metrics CSV or JSON
   - screenshots
   - run cards
4. Treat browser LLM advice as hypothesis generation only.
5. Promote only on fixed benchmark wins across every required surface.

## Why This Exists

The common failure mode in agentic CV work is not lack of model ideas. It is loss of provenance:

- no stable benchmark set
- no dataset or model version pinning
- no screenshots from browser-only flows
- no heartbeat or watchdog on long runs
- no clean separation between research notes and promotion evidence

This skill encodes guardrails for those failure modes.
