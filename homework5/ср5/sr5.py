array = [0, 2, 3, 5, 1, 2, 3, 5, 6, 7]
delta = int(input("Введи значение delta: "))
result = array.count(min(array) + delta)
print(result)
