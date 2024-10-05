numbers1 = int(input("Введите число: "))
numbers2 = int(input("Введите число: "))
numbers3 = int(input("Введите число: "))
if numbers1 == numbers2 == numbers3:
    print(3)

if numbers1 == numbers2 or numbers1 == numbers3 or numbers2 == numbers3:
    print(2)
else:
    print(0)


