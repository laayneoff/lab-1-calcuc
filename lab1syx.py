a = float(input("Введите перевое число:"))
b = float(input("Введите второе число:"))
action = input("Введите дейстивие(+ - / *): ")

if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "/":
    print(a / b)
elif action == "*":
    print(a * b)
else:
    print("Вы ввели неверное действие")
