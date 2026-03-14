# Kaggle 2026 Practices

Use this reference when the workflow runs in Kaggle or should imitate Kaggle-level reproducibility.

## What The Current Kaggle Platform Encourages

Inference from the current official Kaggle tooling and docs:

- version datasets explicitly
- version models explicitly
- declare notebook sources and runtime metadata in kernel metadata
- prefer environment parity with the current Kaggle Docker image
- pull datasets, models, and notebook outputs programmatically instead of copying loose files by hand

Primary sources:

- KaggleHub README: https://github.com/Kaggle/kagglehub
- Kaggle Docker image: https://github.com/Kaggle/docker-python
- Dataset metadata: https://github.com/Kaggle/kaggle-api/blob/main/docs/datasets_metadata.md
- Model metadata: https://github.com/Kaggle/kaggle-api/blob/main/docs/models_metadata.md
- Kernel metadata: https://github.com/Kaggle/kaggle-api/blob/main/docs/kernels_metadata.md

## Practical Habits

### 1. Pin every data source

Do not say "the Kaggle dataset". Record:

- owner
- slug
- version
- local download path
- any post-download conversion step

### 2. Pin every model artifact

If a run consumes or publishes a model, record:

- owner
- slug
- framework
- version notes
- local exported filename

### 3. Treat notebook metadata as part of the experiment

Kernel metadata should be explicit about:

- accelerator choice
- internet on or off
- source datasets
- source kernels
- source models

If you cannot recreate those settings, your run is not reproducible.

### 4. Match the execution image

Mirror the Kaggle Docker image or at least capture its package stack before debugging local regressions.

### 5. Keep browser-only steps short and artifact-rich

For Kaggle or notebook UIs, use short validation passes first, then long runs.

Required artifacts:

- preview grids
- metrics CSV or JSON
- sample prediction panels
- final checkpoint location
- screenshots from the browser path when the browser path matters

### 6. Favor machine-readable run cards

A good Kaggle-style run card includes:

- problem statement
- notebook URL or identifier
- dataset versions
- model version
- runtime settings
- local benchmark result
- exported artifact paths

## CV-Specific Implication

For CV tasks, the strongest Kaggle habit to copy is this:

do not separate model experimentation from artifact discipline.

The model, preview grids, notebook metadata, and benchmark table should travel together.
