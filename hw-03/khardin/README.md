# Практическое задание №3
___

## Описание приложения
В скрипте **get_answer.py** реализовано приложение, которое позволяет получить ответ на вопрос по контексту с помощью REST API.
Реализация выполнена с использованием модели *Deepset Roberta Base Squad2*, которая представляет собой модель обработки естественного языка (NLP), реализованную в библиотеке Transformer, на языке программирования Python.
Более подробную инофрмацию по модели можно получить по ссылке [https://huggingface.co/deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2).

## Использование модели
Вы можете легко найти модель Deepset Roberta Base Squad2 в библиотеке Python Transformers. 
Чтобы загрузить и использовать любую из предварительно обученных моделей для решения вашей задачи, вам потребуется установить пакеты. Список необходимых зависимостей указан в файле **requirements.txt**
Для быстрой установки зависимостей используйте:
```
$ pip install -r requirements.txt
```
Для демонстрации работы приложения на localhost:
```
$ uvicorn get_answer:app
```

## Демонстрация решения
![Screenshot from 2023-11-27 01-06-02](https://github.com/mlteamurfu2325/swe/assets/73106199/a02fd295-1ed2-4521-9e31-23062fe07211)
![Screenshot from 2023-11-27 01-06-33](https://github.com/mlteamurfu2325/swe/assets/73106199/7e3fd410-7c5a-4d4f-b0c5-b2af48492668)
