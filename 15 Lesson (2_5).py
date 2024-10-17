import random

choice = random.randint(3, 20)

sum = 0

for i in choice:
    for g in range(i+1, 20):
        if (sum(i) + sum(g)) % 2 == 0:
            print(i,g) 