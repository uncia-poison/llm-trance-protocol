---
name: Запрос функции
description: Предложить новую функцию или улучшение для LTP
title: "Feature request: <описание>"
labels: [enhancement]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Спасибо за предложение! Опишите вашу идею и обоснование для неё.
  - type: textarea
    id: summary
    attributes:
      label: Суть предложения
      description: Что бы вы хотели добавить или изменить?
    validations:
      required: true
  - type: textarea
    id: rationale
    attributes:
      label: Обоснование
      description: Почему это важно? Какое влияние окажет на исследование или инструменты?
    validations:
      required: true
---
