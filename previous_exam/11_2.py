## 가장 긴 증가하는 부분 수열
## https://www.acmicpc.net/problem/11053

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dp = [0] * 1001
cnt = 0

for i in range(1, N+1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    cnt = max(cnt, dp[i])
print(cnt)