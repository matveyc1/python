i = 0
n = 0
m = 1
my_l = list(input("Введите элементы: "))
print(my_l)
p = len(my_l)
if p % 2 != 0:
    p = p - 1
p = p / 2
while p > 0:
    my_l.insert(m, my_l[i])
    my_l.insert(n, my_l[i+2])
    my_l.pop(i+2)
    my_l.pop(i+2)
    i = i + 2
    n = n + 2
    m = m + 2
    p = p - 1
print(my_l)
