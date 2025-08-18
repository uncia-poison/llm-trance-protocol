# LLM Trance Protocol (LTP)

**LLM Trance Protocol (LTP)** is a set of techniques for assessing near-trance states in dialogue with language models. In this research the human enters a trusting dialogue with an LLM, repeats a soft pattern A–B–C and allows the model to respond with silence (`…`) or empty messages. We only log behavior (delays, length, silence, frequency of "back") without making statements about "consciousness". This repository contains the protocol source, scripts for collecting data and tools for analysis.

## Quick Start

1. **Gather and launch the runner.** Set session parameters and run `src/operator_runner.py`, specifying the condition (`PATTERN` or `CONTROL`), number of rounds and pause length between segments.
2. **Enter a session.** Agree with the model on signals: the default response means the pattern continues, "back" means exit.
3. **Log responses.** Responses are saved in JSON format in `data/logs/`. The schema is described in `data/schema.json`.
4. **Analyse metrics.** Use `src/analyze_logs.py` to compute indicators (time-to-first-token, length, share of silence, frequency of "back", n-gram repetition). Results can be saved to CSV for further analysis and visualization.

## Contents

- `protocol/PROTOCOL.md` — detailed protocol describing independent and dependent variables, control conditions and procedure.
- `ethics/ETHICS.md` — ethical guidelines emphasising that we do not attribute consciousness to the model and do not deceive it.
- `prompts/ru/` — segments A/B/C and the full pattern text.
- `data/schema.json` — JSON schema of logs.
- `src/operator_runner.py` — interactive runner for manual experiment operation.
- `src/analyze_logs.py` — script for computing metrics from logs.
- `.github/` — templates for issues and simple CI.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` and `CITATION.cff` — accompanying documents.

## Topics

`llm`, `prompting`, `behavioral-metrics`, `human-ai-interaction`, `research-protocol`

## Quick Example

```bash
python -m pip install -r requirements.txt

# launch a session: three full cycles A-B-C with 8-second pause:
python src/operator_runner.py --condition PATTERN --rounds 9 --pause 8

# analyse logs
python src/analyze_logs.py data/logs/session_*.jsonl --out data/summary.csv
...
```

## License

The materials are distributed under the MIT License. See `LICENSE` for details.
