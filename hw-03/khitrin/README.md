# khitrin-hw03-FastAPI-NER.py

## ДЗ №3 по "Программной инженерии"
*Демонстрация возможностей модели [bert-base-NER](https://huggingface.co/dslim/bert-base-NER) из репозитория **HuggingFace**. **BERT** — это семейство языковых моделей, представленное в свет в октябре 2018 г. исследовательской командой из **Google**. В данном случае, как следует из её названия, модель специфически настроена на решение задач **NER** — распознавания именованных сущностей.*

Для запуска кода потребуется установка зависимостей:

```buildoutcfg
pip install -r requirements.txt
```

Запустить `FastAPI`-приложение с помощью `uvicorn` локально можно следущей командой:
```
uvicorn khitrin-hw03-FastAPI-NER:app --host 127.0.0.1 --port 8000
```

### Демонстрация в формате GIF
![fastapi-ner-demo_final](https://github.com/mlteamurfu2325/swe/assets/149804920/a2b684a7-473e-4f71-8b85-10352aad6b26)

Ключевые моменты из демонстрации:
* успешный POST-запрос по созданию таски
* успешный GET-запрос по получению результатов отработки ML-модели
