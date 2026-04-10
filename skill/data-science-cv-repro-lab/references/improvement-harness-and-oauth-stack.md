# Improvement Harness And OAuth Stack

Use this reference when the real goal is to beat a baseline, recover from a plateau, or run a
multi-branch research loop instead of only preserving clean execution artifacts.

## Why The Base Skill Plateaus

`data-science-cv-repro-lab` is strong at provenance, browser evidence, run cards, and promotion
discipline. That is necessary, but it is not enough to improve a model.

Plateaus happen when the loop has:

- no fixed evaluator contract
- no slice table or failure taxonomy
- no bounded subagent decomposition
- no controlled ablation queue
- no rerun rule for small deltas
- no explicit auth rule, so the workflow drifts toward API-key-based tooling

For derm and segmentation work, that usually means global Dice stays flat while the team keeps
spending compute on the same hidden failure buckets.

## What To Reuse From The External Stack

### `karpathy/autoresearch`

Reuse the structure, not the exact repo:

- one investigation workspace per topic
- one fixed file or contract that the agent is allowed to mutate
- short, cheap experiments with keep or discard decisions
- a journal that records why each run existed

CV adaptation:

- keep one benchmark contract per investigation
- keep one ablation queue per candidate family
- keep one failure-review set with saved overlays

Source:
- https://github.com/karpathy/autoresearch

### Codex multi-agent and customization guidance

Use Codex subagents for bounded work, not vague roleplay:

- main thread owns the benchmark contract and final decision
- scout subagents inspect papers, repos, or previous runs
- executor subagents make bounded code or config changes
- reviewer subagents audit hard cases, regressions, and artifact completeness

For repeated audits, fan out over a manifest or CSV instead of asking one agent to hold the whole
review set in context.

Sources:
- https://developers.openai.com/codex/multi-agent/
- https://developers.openai.com/codex/concepts/customization/

### OpenAI harness engineering

The evaluator must become the center of the loop.

Adapt these ideas:

- humans steer, agents execute
- increase application legibility before adding more autonomy
- make tests, validators, and operational checks part of the harness, not a later cleanup step

For CV, that means:

- frozen split and metric contract
- saved slice metrics
- saved per-case failure review
- rerun policy for small wins
- promotion gates that separate semantic, runtime, and product-surface outcomes

Source:
- https://openai.com/index/harness-engineering/

### `algorithmicsuperintelligence/openevolve`

Reuse the evaluator-centered search pattern:

- mutate small code or config changes
- score every candidate with the same harness
- keep search state and candidate diffs
- use Pareto thinking when quality, latency, memory, or cost all matter

Do not copy the "autonomous discovery" rhetoric into CV work without the evaluator discipline.
OpenEvolve is valuable because the evaluator stays in charge.

Source:
- https://github.com/algorithmicsuperintelligence/openevolve

### `openai/symphony`

Reuse the workflow contract and workspace isolation:

- workspace per issue, candidate family, or research branch
- one workflow contract that says what the agent can do
- persistent logs and observability for long-running work

This is especially useful when several long-running CV branches must be supervised at once.
Symphony's reference implementation also shows a Codex app-server flow that can work from local
Codex auth instead of paid API keys.

Source:
- https://github.com/openai/symphony

### `paperclipai/paperclip`

Reuse the management concepts when the work expands beyond one branch:

- heartbeats for recurring work
- ticket or task lineage
- goal alignment
- auditability across multiple agents

For a single plateau investigation this is optional. For a portfolio of ongoing experiments, it
becomes useful.

Source:
- https://github.com/paperclipai/paperclip

### `algorithmicsuperintelligence/optillm`

What is useful here is selective:

- plan search
- self-consistency
- best-of-n or candidate selection ideas
- optional reasoning-time compute for research notes or patch review

What is not a good default here:

- making an API-key-based inference proxy a required dependency of the skill

OptiLLM assumes OpenAI-compatible API endpoints and environment variables such as
`OPENAI_API_KEY`. Under an OAuth-only ChatGPT or Codex constraint, treat it as inspiration for
search and selection strategies, not as a mandatory runtime dependency.

Source:
- https://github.com/algorithmicsuperintelligence/optillm

## OAuth-Only Rule

Default allowed paths:

- ChatGPT OAuth-backed sessions
- Codex OAuth-backed sessions
- Codex app-server workflows backed by local auth state
- local Python, shell, notebook, and browser tools

Default forbidden requirements:

- `OPENAI_API_KEY`
- provider-specific paid API keys
- "works only if you buy API access" as a prerequisite for the skill

If a third-party framework cannot run inside the user's local ChatGPT or Codex-authenticated
workflow, keep the idea and drop the dependency.

## Plateau Protocol For Derm Segmentation

If Dice is stuck around a local ceiling:

1. Freeze the contract.
   - dataset version
   - split
   - primary metric
   - non-regression surfaces
   - rerun rule
2. Build slices before another long run.
   - lesion size buckets
   - border difficulty
   - artifact-heavy images
   - background-dominant or empty-mask images
3. Build a failure taxonomy.
   - missed small lesions
   - border leakage
   - background false positives
   - low-contrast misses
4. Save a review set with overlays.
   - 20-50 representative images
   - one short note per case
5. Audit geometry before architecture.
   - resize policy
   - interpolation
   - mask pairing
   - crop policy
   - augmentation alignment
6. Change one meaningful thing at a time.
   - data
   - loss
   - sampler
   - model
   - postprocess
7. Demand rerun evidence for small gains.
   - adjacent seed
   - short rerun
   - same harness, same slices

## Recommended Composition

For real score-improvement work:

- `sota-agent` owns scouting, ablation design, and candidate prioritization
- `data-science-cv-repro-lab` owns execution lanes, evidence capture, and promotion discipline
- the improvement harness owns acceptance or rejection

That split is the simplest way to avoid "cleanly reproduced stagnation".
