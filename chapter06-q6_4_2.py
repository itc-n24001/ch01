def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
       if n % i == 0 or n % (i + 2) == 0:
           return False
       i += 6
    return True

def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

gen = prime_generator()
for _ in range(10):
    print(next(gen))

