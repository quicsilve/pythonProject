numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i == 1:
        print(i, "Это ни то ни се")
        continue
    is_prime = True
    for g in range(2, i):
        if i % g == 0:
            is_prime = False
 

    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)
