def my_func(x, y):
    if x > 0 and y < 0:
        stepen = x ** y
    else:
        stepen = "'Введены неверные данные!'"
    return stepen


n1 = float(input("Введите положительное число: "))
n2 = int(input("Введите отрицательное число: "))
rez = my_func(n1, n2)
print(f"Возводим число в степень и получаем {rez}")
