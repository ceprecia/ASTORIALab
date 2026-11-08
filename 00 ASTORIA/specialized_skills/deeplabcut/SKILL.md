---
name: deeplabcut
description: >-
  Implements one approved animal-behavior pose-estimation or tracking checkpoint
  through an already available verified environment while preserving video
  identity, keypoints, labeling, splits, confidence, occlusion, outputs, and
  behavioral-claim boundaries. Triggers: track animal pose with DeepLabCut,
  DeepLabCut project checkpoint.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: software-adapter
  modality: behavior
  dependencies: ""
  requires: Python, DeepLabCut, video files
  gates: installing software, running on real data, accepting QC
  created: "2026-07-24"
  updated: "2026-10-29"
---

# DeepLabCut

Implement one approved pose-estimation checkpoint without silently choosing
keypoints, labels, thresholds, training data, or behavioral interpretation.

## Purpose

This conditional Part 4 animal-behavior software adapter audits video and
animal identity, camera and frame metadata, keypoint schema, labels, train/test
split, augmentation, model, confidence, occlusion, smoothing, identity
tracking, checkpoint, and output provenance. It does not choose the behavior,
keypoints, model, threshold, or claim.

The user owns the scientific behavior measure, animals, keypoints, labels, model,
split, and claim. [experimental-design](../../skills/experimental-design/SKILL.md) owns task and behavior design;
[pytorch-lightning](../pytorch-lightning/SKILL.md) owns selected training orchestration.

Activate only for exact `deeplabcut` or an approved handoff naming one pose or
tracking checkpoint. Do not trigger from generic behavior, video, pose, or
animal requests. Out of scope: automatic behavior classification, downloads,
installs, and interpretation of pose as an unvalidated behavior measure.

## Inputs

Obtain or mark missing: video and animal identity, camera and frame rate,
keypoints and labeling protocol, occlusion, train/validation/test split,
model and checkpoint, confidence and smoothing, environment, output, and claim.
If animal identity, keypoint schema, or split is missing, return **DeepLabCut
intake incomplete**.

## Steps

### Gate 1: approve the pose checkpoint

Show video, animal, camera, keypoints, labels, split, model, confidence,
occlusion, output, validation, and claim. Gate 1 authorizes a method plan.

### Gate 2: approve one bounded action

Ask the user to select the exact operation, environment, output, and verification.
Gate 2 authorizes one action only; it does not authorize installs, downloads,
unbounded training, or behavioral interpretation.

Return:

```text
DeepLabCut Operation Record
Video, animal, camera, frame, and keypoint identity:
Labels, occlusion, split, model, checkpoint, and confidence:
Output, validation, smoothing, and provenance:
Behavioral-measure and interpretation limits:
Permitted claim and stop point:
```

## Boundaries

Method rules:

- Split by animal, session, or recording as scientifically required; do not
  let adjacent frames leak across train and test.
- Preserve frame, animal, camera, keypoint, confidence, occlusion, and missing
  data metadata. Do not infer keypoints from filenames.
- Record labeling agreement, held-out error, confidence policy, interpolation,
  smoothing, and sensitivity. A high-confidence point is not necessarily valid.
- Pose coordinates require a separate behavioral definition and validation;
  they are not automatically actions, welfare states, or biological traits.

Stop for missing animal or keypoint identity; frame leakage; unreviewed labels
or confidence thresholds; unavailable environment; a request to install,
download, train unboundedly, classify behavior automatically, or interpret pose
as a biological or welfare conclusion.

## References

- Adapted from: NeuroAIHub. (2026). *awesome_cognitive_and_neuroscience_skills* [Computer software]. GitHub. https://github.com/NeuroAIHub/awesome_cognitive_and_neuroscience_skills (MIT License)
- DeepLabCut developers. (n.d.). *DeepLabCut user guide*. https://deeplabcut.github.io/DeepLabCut/docs/standardDeepLabCut_UserGuide
