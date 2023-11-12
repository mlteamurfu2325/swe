# Домашнее задание №2

---
## 1) ANGorbachev/translator.py
*Переводчик с русского языка на английский. Для перевода используется модель [<u>"opus-mt-ru-en"</u>](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en) от **Language Technology Research Group at the University of Helsinki**. Модель основана на архитектуре Трансформер и показывает неплохие результаты при не очень больших размерах самой модели (307Мб)*

*Для запуска кода потребуется установка зависимостей:*

```buildoutcfg
pip install transformers sentencepiece sacremoses tensorflow
```
---
Также для демостранции модели, приложение запущено в облаке Streamlit:
[Запустить приложение](https://lighttranslator.streamlit.app/)
