d = 1
a = float(input("Количество км в первый день: "))
print(a)
b = float(input("Необходимый результат: "))
print(b)
while b > a:
    a = a + a * 0.1
    d = d + 1
print(d)
