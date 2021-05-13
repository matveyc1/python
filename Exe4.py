my_l = input("Введите строку: ")
my_str = []
num = 1
i = 0
my_str = my_l.split()
long = len(my_str)
while long > 0:
    print(f"{num}. {my_str[i]}")
    i += 1
    num += 1
    long -= 1
