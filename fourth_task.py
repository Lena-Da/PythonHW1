#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

enter_number=int(input("Введи номер четверти координат: "))
if enter_number == 1:
    print("x=от 0 до 100, y=от 0 до 100")
elif enter_number == 2:
    print("x=от 0 до -100, y=от 0 до 100")
elif enter_number == 3:
    print("x=от 0 до -100, y=от 0 до -100")
elif enter_number == 4:
    print("x=от 0 до 100, y=от 0 до 100")
else:
    print("Введи корректный номер четверти координат")