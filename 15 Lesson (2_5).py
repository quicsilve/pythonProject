import random

choice = random.randint(3, 20)

passw = ''

for i in range(1, choice // 2 + 1):
    for g in range(i + 1, choice + 1 - i):
        if choice % (i + g) == 0:
            passw += str(i) + str(g)
print(f"Пароль для числа {choice}: {passw}")