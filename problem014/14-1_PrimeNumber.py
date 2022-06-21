## Prime Number
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = 100
array = [True for _ in range(n+1)]

def Eratosthenes(n):
    for i in range(2, int(math.sqrt(n))+1):
        if array[i]:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1

Eratosthenes(n)
for i in range(2, n+1):
    if array[i]:
        print(i, end= ' ')
print()
print(is_prime(7))
print(is_prime(503))