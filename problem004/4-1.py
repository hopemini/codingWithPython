n, k = map(int, input().split())

result = n % k
while n != 1:
    n = n // k
    result += 1

print(result)