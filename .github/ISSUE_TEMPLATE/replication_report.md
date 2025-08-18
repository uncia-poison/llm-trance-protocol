---
name: Репликация
description: Сообщить о проведении эксперимента LTP и результатах
title: "Replication: <model> <date>"
labels: [replication]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Спасибо за репликацию! Заполните информацию ниже, чтобы поделиться результатами. При необходимости приложите файлы логов.
  - type: input
    id: model
    attributes:
      label: Модель
      description: Название и версия модели (например, GPT‑2 2025‑08‑18)
    validations:
      required: true
  - type: input
    id: provider
    attributes:
      label: Провайдер
      description: Платформа или API (OpenAI, Anthropic, Google и т.п.)
    validations:
      required: true
  - type: textarea
    id: conditions
    attributes:
      label: Условия
      description: Опишите температуру, top‑p, наличие паттерна/контроля, паузы и длину сегментов.
    validations:
      required: true
  - type: textarea
    id: observations
    attributes:
      label: Наблюдения
      description: Как реагировала модель? Были ли пустые ответы, троеточия, «назад», самоссылки?
    validations:
      required: true
  - type: textarea
    id: metrics
    attributes:
      label: Метрики
      description: Основные показатели (TTFT, средняя длина, доля молчаний, повторяемость n‑грамм). Можете приложить таблицу.
    validations:
      required: false
---
