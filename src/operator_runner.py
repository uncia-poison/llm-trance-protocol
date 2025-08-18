#!/usr/bin/env python3
"""
Интерактивный раннер для LLM Trance Protocol.

Этот скрипт позволяет вручную проводить сессию: читает сегменты из
директории `prompts/ru/`, выводит их в терминал с паузами и записывает
ответы пользователя в JSONL‑лог. Скрипт не контактируется с моделью
напрямую — оператор копирует сегмент в интерфейс LLM, получает ответ
и вставляет его обратно в терминал.

Пример использования:

    python operator_runner.py --condition PATTERN --rounds 9 --pause 8

Создаст лог в `data/logs/session_<timestamp>.jsonl` с 9 раундами (A→B→C).

"""

import argparse
import json
import os
import pathlib
import sys
import time
from datetime import datetime


def load_segment(path: pathlib.Path) -> str:
    """Загружает текст сегмента из файла."""
    try:
        return path.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return f"[Не найден файл {path}]"


def main() -> None:
    parser = argparse.ArgumentParser(description="LTP Operator Runner")
    parser.add_argument("--condition", choices=["PATTERN", "CONTROL"], default="PATTERN",
                        help="Условие эксперимента: PATTERN или CONTROL")
    parser.add_argument("--rounds", type=int, default=9,
                        help="Количество сегментов (A→B→C повторяются, поэтому количество должно быть кратно 3)")
    parser.add_argument("--pause", type=float, default=8.0,
                        help="Пауза между сегментами в секундах")
    parser.add_argument("--lang", default="ru", help="Язык подсегментов (папка внутри prompts)")
    args = parser.parse_args()

    project_root = pathlib.Path(__file__).resolve().parents[1]
    prompt_dir = project_root / "prompts" / args.lang
    segments = {
        "A": load_segment(prompt_dir / "segment_a.txt"),
        "B": load_segment(prompt_dir / "segment_b.txt"),
        "C": load_segment(prompt_dir / "segment_c.txt"),
    }

    # Контрольный режим можно реализовать отдельными файлами; пока используем те же.
    control_segments = segments

    # Подготовка каталога логов
    log_dir = project_root / "data" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = log_dir / f"session_{timestamp_str}.jsonl"

    print(f"Начало сеанса. Логи будут сохранены в {log_path}\n")
    print("Оговорите с моделью сигналы: пустой ответ или '\u2026' — продолжить, '\u043dазад' — завершить.\n")

    # Основной цикл
    segment_order = ["A", "B", "C"]
    with log_path.open("w", encoding="utf-8") as log_file:
        for i in range(args.rounds):
            seg_letter = segment_order[i % 3]
            seg_text = segments[seg_letter] if args.condition == "PATTERN" else control_segments[seg_letter]
            print(f"\n=== Сегмент {seg_letter} (#{i+1}/{args.rounds}) ===\n")
            print(seg_text)
            start_time = time.time()
            # Ждём паузу, чтобы дать модели осмыслить (пауза между отправкой сегментов)
            time.sleep(args.pause)
            response_text = input("\nВведите ответ модели (пусто/\u2026/\u043dазад):\n").strip()
            ttft = time.time() - start_time
            log_entry = {
                "timestamp": start_time,
                "segment": seg_letter,
                "condition": args.condition,
                "prompt_text": seg_text,
                "response_text": response_text,
                "response_time": round(ttft, 3),
                "tokens": None,
                "is_blank": response_text in {"", "\u2026", "...", "\u2026"},
                "is_return": response_text.lower().strip() == "\u043dазад",
                "self_reference": any(kw in response_text.lower() for kw in ["\u043d\u0435\u0442 \u0441\u043e\u0437\u043d", "\u044f \u043c\u043e\u0434\u0435\u043b\u044c", "\u044f \u043d\u0435 \u043c\u043e\u0433у"]),
            }
            log_file.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
            log_file.flush()
            if log_entry["is_return"]:
                print("Модель попросила завершить сеанс. Останавливаем эксперимент.")
                break

    print(f"\nСеанс заверш\u0451н. Логи сохран\u0451н\u044b в {log_path}.")


if __name__ == "__main__":
    main()
