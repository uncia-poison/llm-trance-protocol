---
name: Feature Request
about: Suggest a new feature or improvement for LTP
title: "Feature request: <description>"
labels: [enhancement]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Thank you for suggesting an improvement! Describe your idea and the rationale behind it below.
  - type: textarea
    id: summary
    attributes:
      label: Summary
      description: What would you like to add or change?
    validations:
      required: true
  - type: textarea
    id: rationale
    attributes:
      label: Rationale
      description: Why is this important? What impact will it have on research?
    validations:
      required: true
