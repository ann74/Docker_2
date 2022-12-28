expression = input("Введите пример: ").lower().strip()
while expression != 'stop':
    print("Ответ:", eval(expression))
    expression = input("Введите пример: ").lower().strip()
print("Вы завершили программу")
