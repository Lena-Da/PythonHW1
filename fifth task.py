# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
point_a1=float(input("Введи координату точки A1: "))
point_a2=float(input("Введи координату точки A2: "))
point_b1=float(input("Введи координату точки B1: "))
point_b2=float(input("Введи координату точки B2: "))
solution=((point_b1-point_a1)**2)+((point_b2-point_a2)**2)
result = (round(math.sqrt(solution),2))
print("Расстояние между точками: ", result)
