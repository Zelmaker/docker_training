## Задание 1. Dockerfile

Создайте простое python-приложение, которое в бесконечном цикле запрошивает от пользователя арифметическое выражение, например, 2+2, и выдает его решение. Если пользователь ввел `Stop` или `stop`, приложение останавливается.

<aside>
💡 Можно пользоваться функцией eval()

</aside>

```powershell
>>>2+2
4
>>>stop

```

Напишите Dockerfile. Создайте образ приложения и запустите контейнер.


Внутри контейнера проведите ряд арифметических выражений.


# Решение:
Создаем app.py
```
while True:
    expression = input("Введите арифметическое выражение (или 'Stop' для остановки): ")
    if expression.lower() == "stop":
        break
    try:
        result = eval(expression)
        print(f"Результат: {result}")
    except:
        print("Некорректное выражение. Попробуйте еще.")
```

Создаем Dockerfile
```
FROM python:3.8-alpine

COPY app.py /app/app.py

RUN apk add --no-cache build-base

RUN pip install --upgrade pip

CMD ["python", "/app/app.py"]
```
Команда для создания образа:

~~~
docker build -t arithmetic-calculator .
~~~
Команда для запуска контейнера:
~~~
docker run -it arithmetic-calculator
~~~