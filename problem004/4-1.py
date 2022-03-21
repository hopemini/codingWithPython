n, k = map(int, input().split())

cnt = 0
while True:
    result = n % k
    if result == 0:
        n //= k
        cnt += 1
    else:
        n -= result
        cnt += result
    if n < k:
        break

cnt += (n - 1)

print(cnt)
