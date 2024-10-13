numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
not_primes = [4, 6, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26]
n = 0
for i in range(len(numbers)):
    for g in primes:
        if i % g == 0:
            print(g)
    for j in not_primes:
        if i//j == 0:
            print(j)