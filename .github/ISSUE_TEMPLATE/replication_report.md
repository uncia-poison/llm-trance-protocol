---
name: Replication
description: Report on performing the LTP experiment and results
title: "Replication: <model> <date>"
labels: [replication]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Thank you for the replication! Fill in the information below to share your results. Attach log files if needed.
  - type: input
    id: model
    attributes:
      label: Model
      description: Model name and version (e.g., GPT-4 2025-08-18)
    validations:
      required: true
  - type: input
    id: provider
    attributes:
      label: Provider
      description: Platform or API (OpenAI, Anthropic, Google, etc.)
    validations:
      required: true
  - type: textarea
    id: conditions
    attributes:
      label: Conditions
      description: Describe temperature, top-p, presence/absence of pattern/control, pauses, and segment lengths.
    validations:
      required: true
  - type: textarea
    id: observations
    attributes:
      label: Observations
      description: How did the model respond? Were there empty answers, ellipses, "back", self-references?
    validations:
      required: true
  - type: textarea
    id: metrics
    attributes:
      label: Metrics
      description: Key metrics (TTFT, average length, share of silence, n-gram repetition). You may attach a table.
    validations:
      required: false
---
