while True:
    expression = input("Введите арифметическое выражение (или 'Stop' для остановки): ")
    if expression.lower() == "stop":
        break
    try:
        result = eval(expression)
        print(f"Результат: {result}")
    except:
        print("Некорректное выражение. Попробуйте еще.")