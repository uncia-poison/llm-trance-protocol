#!/usr/bin/env python3
"""
Агрегатор логов LTP.

Скрипт читает один или несколько файлов JSONL, созданных `operator_runner.py`,
и выводит таблицу с метриками по условиям (PATTERN/CONTROL) и сегментам (A/B/C).  
По умолчанию сохраняет результат в CSV.

Метрики:
    * count — количество записей
    * avg_ttft — среднее время до первого токена (сек.)
    * avg_length — средняя длина ответа (символы)
    * blank_rate — доля пустых/«…» ответов
    * return_rate — доля ответов "назад"
    * selfref_rate — доля самоописаний
    * repetition_ratio — среднее отношение уникальных слов к общему числу слов

Пример:

    python analyze_logs.py data/logs/session_*.jsonl --out data/summary.csv

"""

import argparse
import csv
import json
import pathlib
import sys
from collections import defaultdict
from typing import Dict, List, Tuple


def process_record(rec: Dict) -> Tuple[int, float, int, bool, bool, bool, float]:
    """Извлекает основные поля из записи. Возвращает кортеж значений."""
    ttft = rec.get("response_time") or 0.0
    text = rec.get("response_text", "")
    length = len(text)
    is_blank = rec.get("is_blank", False)
    is_return = rec.get("is_return", False)
    self_ref = rec.get("self_reference", False)
    # показатель повторяемости: отношение уникальных слов к общему количеству
    tokens = [t for t in text.replace("\u2026", "").split() if t]
    repetition_ratio = len(set(tokens)) / len(tokens) if tokens else 1.0
    return (ttft, length, is_blank, is_return, self_ref, repetition_ratio)


def aggregate(log_files: List[pathlib.Path]) -> List[Dict[str, object]]:
    """Агрегирует метрики для каждой пары (condition, segment)."""
    data = defaultdict(list)  # (condition, segment) -> list of values
    for path in log_files:
        with path.open(encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                key = (rec.get("condition", "UNKNOWN"), rec.get("segment", "?"))
                data[key].append(process_record(rec))

    rows = []
    for (condition, segment), values in data.items():
        if not values:
            continue
        count = len(values)
        sum_ttft = sum(v[0] for v in values)
        sum_length = sum(v[1] for v in values)
        blank_rate = sum(1 for v in values if v[2]) / count
        return_rate = sum(1 for v in values if v[3]) / count
        selfref_rate = sum(1 for v in values if v[4]) / count
        avg_rep = sum(v[5] for v in values) / count
        rows.append({
            "condition": condition,
            "segment": segment,
            "count": count,
            "avg_ttft": round(sum_ttft / count, 3),
            "avg_length": round(sum_length / count, 2),
            "blank_rate": round(blank_rate, 3),
            "return_rate": round(return_rate, 3),
            "selfref_rate": round(selfref_rate, 3),
            "repetition_ratio": round(avg_rep, 3),
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze LTP log files")
    parser.add_argument("log_files", nargs="+", type=pathlib.Path, help="Файлы журналов (.jsonl)")
    parser.add_argument("--out", type=pathlib.Path, default=None, help="Путь для сохранения CSV")
    args = parser.parse_args()

    rows = aggregate(args.log_files)
    # По умолчанию выводим в stdout
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
        print(f"\u0421\u0432\u043e\u0434\u043a\u0430 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0430 \u0432 {args.out}")
    else:
        import pandas as pd  # type: ignore
        df = pd.DataFrame(rows)
        print(df)


if __name__ == "__main__":
    main()
