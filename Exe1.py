def delenie(n1, n2):
    try:
        rez = n1 / n2
    except ZeroDivisionError:
        rez = "На ноль не делим!"
    return rez


n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
f = delenie(n1, n2)
if type(f) == str:
    print(f)
else:
    print("%.3f" % f)
