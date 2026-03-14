# Colab And VM Operations

Use this reference when the workflow depends on Google Colab GPUs or a custom GPU VM.

## Google Colab GPU Management

### Required operating pattern

1. Open the target notebook through a stable URL.
2. Select the accelerator explicitly.
3. Run a smoke cell before any expensive training.
4. Export artifacts to one stable directory.
5. Pull the artifact manifest and previews back locally.

### Colab smoke checklist

Before a long run, verify from inside the notebook:

- Python version
- GPU presence
- CUDA visibility to the framework
- dataset mount or download success
- write access to the export directory

Minimum smoke checks:

- `nvidia-smi`
- `torch.cuda.is_available()` or framework equivalent
- one tiny batch through the dataloader
- one tiny forward pass

### Colab artifact discipline

Keep one export root such as:

- `/content/export`
- `/kaggle/working/export`

Write at least:

- `run_context.json`
- `artifact_manifest.json`
- `metrics.csv` or `metrics.json`
- `train_strategy.json`
- one preview image
- one final checkpoint or checkpoint pointer

### Colab browser evidence

When browser automation is part of the task, preserve:

- runtime type selected
- notebook URL
- screenshots
- marker or completion signal
- local artifact pull results

## Custom GPU VM Management

### Bootstrap

Every long-run VM job should start with a machine-readable bootstrap manifest:

- git commit
- dataset id or manifest hash
- command line
- output root
- model family
- threshold or loss settings
- GPU type
- start time

### Liveness

Do not rely on PID existence alone.

Use at least one of:

- heartbeat file
- session json
- tmux session plus heartbeat
- supervisor status
- epoch-progress polling

### Health policy

Track:

- epoch progression
- best metric so far
- GPU utilization
- GPU memory
- heartbeat age
- log freshness

A healthy long run should have explicit stall and failure rules.

### Recovery

When a run goes unhealthy, the workflow should define one of:

- kill and relaunch
- kill and fall back to a tiny debug run
- sync artifacts and stop the VM
- hold the VM for human review

### Artifact sync

Do not leave the only copy of a useful candidate on the VM.

Sync back:

- summary json
- history csv
- checkpoint path or exported model
- benchmark snapshot
- preview boards

### Shutdown

When the work is complete:

- stop the training session
- flush remaining artifacts
- stop the VM automatically if policy allows
- record the final state in the run card
