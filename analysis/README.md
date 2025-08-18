# Results analysis

This folder is intended for reports, notebooks and charts obtained after processing logs using `src/analyze_logs.py`.

Suggested workflow:

1. Collect data by running several sessions under PATTERN and CONTROL conditions. Make sure the log files (`.jsonl`) are located in `data/logs/`.
2. Run the aggregator:

```bash
python src/analyze_logs.py data/logs/session_*.jsonl --out analysis/summary.csv
...
```

3. Open `analysis/summary.csv` in a spreadsheet or use pandas/matplotlib to build charts. For example you can build a box plot for `avg_ttft` comparing PATTERN vs CONTROL.
4. Document your observations in this folder: place your Jupyter notebooks (`.ipynb`), scripts or Markdown reports that describe the differences and conclusions.

Remember that interpretation of data should be based on strict correlations and should not attribute mental states to the model.
