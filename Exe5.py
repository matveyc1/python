def sum():
    sum_res = 0
    n = False
    while n == False:
        number = input('Введите числа для работы или Q для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'Q':
                n = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма -  {sum_res}')
    return


print(sum())
