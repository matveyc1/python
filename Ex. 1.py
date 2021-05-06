result_list = [12, 5.5, 'This will be text!']
i = 0
n = len(result_list)
while n > 0:
    tipe = type(result_list[i])
    if tipe == str:
        tipe = "строковый"
    elif tipe == int:
        tipe = "целочисленный"
    elif tipe == float:
        tipe = "вещественный"
    print(f"Элемент списка '{result_list[i]}' имеет тип {tipe}")
    n = n - 1
    i = i + 1

