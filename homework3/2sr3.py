AB = input("Длина первого катета: ")
AC = input("Длина второго катета: ")
AB = float(AB)
AC = float(AC)
BC = (AB  2 + AC  2)**0.5
S = (AB * AC) / 2
P = AB + AC + BC
print("Площадь треугольника: %.2f" % S)
print("Периметр треугольника: %.2f" % P)
