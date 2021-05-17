def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
n1 = int(input('Введите число: '))
n2 = int(input('Введите число: '))
n3 = int(input('Введите число: '))
print(my_func(n1, n2, n3))
