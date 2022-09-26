#4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
import math
xA = int(input("A 1 ="))
yA = int(input("A 2 ="))
xB = int(input("B 1 ="))
yB = int(input("B 2 ="))
res = math.sqrt((xA - xB) * (xA - yB) + (yA - yB) * (yA - yB))
print(res)