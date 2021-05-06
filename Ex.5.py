reiting = [7, 6, 4, 2, 1]
mark = int(input("Хотите оценить?(1 - да, 0 - выход): "))
while mark != 0:
    mark = int(input("Поставьте оценку от 1 до 9: "))
    if mark > 9:
        print("Упс, похоже вы нас перехвалили!:D Хватит и 9!")
        reiting.append(9)
        reiting.sort(reverse=True)
        print(f"Текущий список - {reiting}")
    elif mark < 1:
        print("Это слишком мало, поэтому остановимся на единичке. Надеемся, что в следующий раз вам понравиться! :С")
        reiting.append(1)
        reiting.sort(reverse=True)
        print(f"Текущий список - {reiting}")
    else:
        reiting.append(mark)
        reiting.sort(reverse=True)
        print(f"Текущий список - {reiting}")
        print("До свидания! :)")
    mark = int(input("Поставьте оценку от 1 до 9: "))
