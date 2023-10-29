## 포도주 시식
## https://www.acmicpc.net/problem/2156

glass = [0] * 10001
N = int(input())
for i in range(1, N+1):
    glass[i] = int(input())

## 연속 3잔 X
## 지금까지 마신 최대 포도주의 양 (n) : n-3, n-2, n-1, n
## 1. 지금껏 마신 포도주 (n-3) + 포도주 (n-1) + 포도주 (n)
## 2. 지금껏 마신 포도주 (n-2) + 포두주 (n)
## 3. 지금껏 마신 포도주 (n-1)
dp = [0] * 10001

dp[1] = glass[1]
dp[2] = glass[1] + glass[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-1], dp[i-2] + glass[i], dp[i-3] + glass[i-1] + glass[i])

print(dp[N])