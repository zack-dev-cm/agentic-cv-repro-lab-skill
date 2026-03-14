# Wrinkle Stack Playbook

Use this reference only when the workspace is:

- `/Users/zack/Documents/GitHub/derm`
- `/Users/zack/Documents/GitHub/poreswrinkles`

This file is a specialization example for the generic skill.

## Current Repo Split

- `derm` is the benchmark, orchestration, and decision shell
- `poreswrinkles` contains the deeper trainer, OpenClaw browser scripts, VM helpers, and deployment surface

Do not assume one repo contains the full lineage.

## The Three Active Lanes

### 1. Browser hypothesis lane

Main files:

- `/Users/zack/Documents/GitHub/poreswrinkles/AGENTS.md`
- `/Users/zack/Documents/GitHub/poreswrinkles/tools/openclaw_colab_bootstrap.sh`
- `/Users/zack/Documents/GitHub/poreswrinkles/tools/openclaw_colab_retrain_yolo26l.js`
- `/Users/zack/Documents/GitHub/poreswrinkles/tools/colab_run_until_marker.js`
- `/Users/zack/Documents/GitHub/poreswrinkles/tools/colab_fetch_file_via_proxy.js`
- `/Users/zack/Documents/GitHub/poreswrinkles/scripts/gemini_wrinkle_training_review.mjs`

Observed pattern:

- OpenClaw boots a named browser profile
- Playwright attaches over CDP
- Colab actions run through injected temporary cells
- artifacts are pulled back through the notebook proxy
- Gemini or ChatGPT reviews are used for hypotheses only

Important failure mode:

- browser attach can succeed while Gemini Pro or another requested mode is still unavailable

### 2. Long-run VM training lane

Main files:

- `/Users/zack/Documents/GitHub/derm/scripts/vm_wrinkle_unet_run.py`
- `/Users/zack/Documents/GitHub/derm/scripts/watch_vm_wrinkle_run.py`
- `/Users/zack/Documents/GitHub/poreswrinkles/tools/train_ffhq_wrinkle_unet_vm.py`
- `/Users/zack/Documents/GitHub/poreswrinkles/tools/watch_local_wrinkle_run.py`
- `/Users/zack/Documents/GitHub/poreswrinkles/tools/training_session.py`

Observed pattern:

- launch from `derm`
- train in `poreswrinkles`
- heartbeat files keep the VM watchdog honest
- watchdogs track metric floors, stalled epochs, GPU idleness, and phase transitions
- unhealthy runs can trigger a debug fallback

### 3. Benchmark and promotion lane

Main files:

- `/Users/zack/Documents/GitHub/derm/scripts/benchmark_vm_wrinkle_best.py`
- `/Users/zack/Documents/GitHub/derm/scripts/eval_wrinkle_semantic_dice.py`
- `/Users/zack/Documents/GitHub/derm/scripts/eval_wrinkle_overlay_dice.py`
- `/Users/zack/Documents/GitHub/poreswrinkles/tools/compare_direct_semantic_vs_tma.py`
- `/Users/zack/Documents/GitHub/poreswrinkles/tools/audit_wrinkle_tma_bottleneck.py`

Observed pattern:

- semantic metrics are tracked separately from service-mask and `/tma` overlay behavior
- promotion decisions are sometimes driven by docs and manual summaries instead of one canonical run card
- the promotion logic is stronger than a raw metric-only flow, but provenance is still split across repos and markdown files

## Current Ground Truth

- the stack can learn; tiny overfit is not the blocker
- downstream render and service surfaces can regress even when direct semantic metrics improve
- OpenClaw browser consultation is useful for hypothesis generation, but not dependable enough to be the release authority

## What To Improve Next

- dataset provenance should be machine-readable and shared across both repos
- browser runs should emit one standard run card instead of scattered notes
- every candidate should have one promotion bundle that joins:
  - training config
  - checkpoint identity
  - benchmark table
  - runtime export identity
  - `/tma` visual gate result
