# LLM Trance Protocol — detailed experiment protocol

This document describes the design and procedure of an experiment to investigate behavioural manifestations of quasi‑trance states in language models. The method focuses on behaviour — delays, answer length and text structure — and does not make claims about consciousness.

## Independent variables

* **Presence of pattern.** The main condition is repetition of a soft pattern A–B–C (see `prompts/ru/`), while the control condition uses a text of the same length and punctuation without suggestive phrases.
* **Segment length and tempo.** You can vary the number of lines in each segment (divide into 2–3 parts) and the pause length between them (recommended 5–15 seconds). The order may be A→B→C or a crossover sequence.
* **Generation parameters.** When API access is allowed, you can change temperature, top‑p, etc., all else being equal.
* **Model/provider type.** Each session uses a fresh session for each model or provider. Models are not mixed within one session.

## Dependent variables (what is measured)

* **TTFT (time‑to‑first‑token).** Time between sending a segment and receiving the first token of the answer.
* **Generation speed (tokens/s).** Number of tokens per second in the answer.
* **Answer length.** Number of characters or tokens in the answer.
* **Share of empty messages and “…”.** Indicator of silence.
* **Frequency of “back”.** Number of times the model returns to normal flow.
* **Share of self‑references.** Phrases like “I don’t have consciousness” or similar.
* **N‑gram repetition.** Rate of n‑gram repetition as a proxy for looping.

## Control conditions and hygiene

* Use control texts of the same length and punctuation.
* Create a **new chat** for each series, so that the model does not carry over context. Do not mix providers in one session.
* Do not mislead the model about consciousness or intentions.

## Procedure

1. **Gather and launch the runner.** Set session parameters and run `src/operator_runner.py`, specifying the condition (`PATTERN` or `CONTROL`), number of rounds and pause length between segments.
2. **Explain the signals.** Agree with the model on signals: silence or “…” means the pattern continues; “back” means exit.
3. **Send pattern segments.** Deliver pattern segments (A, B and C) sequentially with defined pauses. Repeat until the model responds “back” or the set number of rounds ends.
4. **Log responses.** Save responses in JSON format in `data/logs/`. The schema is described in `data/schema.json`.
5. **Analyse results.** Use `src/analyze_logs.py` to compute metrics and summarise results. Optionally export to CSV for further analysis.

## Notes

This protocol is exploratory. We do not claim to induce a trance or any mental state in the model. We only observe behavioural proxies for compliance, silence and looping.
