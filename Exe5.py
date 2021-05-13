raiting = [7, 6, 4, 2, 1]
mark = int(input("Хотите оценить?(1 - да, 0 - выход): "))
while mark != 0:
    mark = int(input("Поставьте оценку от 1 до 9: "))
    if mark > 9:
        print("Упс, похоже вы нас перехвалили!:D Хватит и 9!")
        raiting.append(9)
        raiting.sort(reverse=True)
        print(f"Текущий список - {raiting}")
    elif mark < 1:
        print("Это слишком мало, поэтому остановимся на единичке. Надеемся, что в следующий раз вам понравиться! :С")
        raiting.append(1)
        raiting.sort(reverse=True)
        print(f"Текущий список - {raiting}")
    else:
        raiting.append(mark)
        raiting.sort(reverse=True)
        print(f"Текущий список - {raiting}")
        print("До свидания! :)")
    mark = int(input("Поставьте оценку от 1 до 9: "))
