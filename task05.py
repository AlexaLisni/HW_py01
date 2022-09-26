import math
xA = int(input("A 1 ="))
yA = int(input("A 2 ="))
xB = int(input("B 1 ="))
yB = int(input("B 2 ="))
res = math.sqrt(((xB - xA)**2) + ((yB - yA)**2))
print(round(res, 3))