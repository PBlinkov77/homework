print("Введи имя")
name = input()
print("Введи фамилию")
surname = input()
print("Введи год рождения")
year = input()
print(name, "_", surname, "_", year)
x = name
name = surname
surname = x
year = int(year) + 60
print(name, "_", surname, "_", year)
