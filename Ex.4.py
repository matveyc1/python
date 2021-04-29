a = 0
s = int(input("Введите число: "))
print(s)
while s > 0:
    b = s % 10
    if b > a:
        a = b
    s = s // 10
print("Наибольщая цифра числа: ", a)
