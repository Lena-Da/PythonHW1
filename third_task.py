# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

point_x=int(input("Введи координату точки Х: "))
point_y=int(input("Введи координату точки У: "))

if point_x > 0 and point_y > 0:
    print ("1 четверть")
elif point_x < 0 and point_y > 0:
    print ("2 четверть")
elif point_x < 0 and point_y < 0:
    print ("3 четверть")
elif point_x > 0 and point_y < 0:
    print ("4 четверть")

