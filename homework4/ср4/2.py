n = int(input("Размерность массива a: "))
a = [0] * n
for i in range(n):
    print("a[", i, "]=", sep = "", end = "")
    a[i] = int(input())

n = int(input("Размерность массива b: "))
b = [0] * n
for i in range(n):
    print("b[", i, "]=", sep = "", end = "")
    b[i] = int(input())

print(set(a) & set (b))
