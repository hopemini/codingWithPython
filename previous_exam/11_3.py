## 내리막 길
## https://www.acmicpc.net/problem/1520

M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
move = ((0, 1), (1, 0), (0, -1), (-1, 0))

def dp_move(y, x):
    if dp[y][x] != -1: return dp[y][x]
    if y == M-1 and x == N-1: return 1
    dp[y][x] = 0
    for i in range(4):
        dy = y + move[i][0]
        dx = x + move[i][1]
        if 0 <= dy < M and 0 <= dx < N and Map[dy][dx] < Map[y][x]:
            dp[y][x] += dp_move(dy, dx)
    return dp[y][x]

print(dp_move(0, 0))