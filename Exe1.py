result_list = [12, 5.5, 'This will be text!']
i = 0
n = len(result_list)
while n > 0:
    point = type(result_list[i])
    if point == str:
        point = "строковый"
    elif point == int:
        point = "целочисленный"
    elif point == float:
        point = "вещественный"
    print(f"Элемент списка '{result_list[i]}' имеет тип {point}")
    n = n - 1
    i = i + 1
