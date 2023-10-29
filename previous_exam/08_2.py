## 뱀
## https://www.acmicpc.net/problem/3190

from collections import deque

def direction_change(d, c):
    if c == 'L':
        d = (d-1) % 4
    else:
        d = (d+1) % 4
    return d

N = int(input())
K = int(input())
board = [[0] * (N + 2) for _ in range(N+2)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1
L = int(input())
time = {}
for i in range(L):
    X, C = input().split()
    time[int(X)] = C

d = ((-1, 0), (0, -1), (1, 0), (0, 1)) # 아래, 왼, 위, 오른

q = deque()
y, x = 1, 1
board[y][x] = 2
q.append((y, x))
direction = 3
t = 1
while True:
    y, x = y + d[direction][0], x + d[direction][1]
    if 1 <= x <= N and 1 <= y <= N and board[y][x] != 2:
        if not board[y][x] == 1:
            dy, dx = q.popleft()
            board[dy][dx] = 0
        board[y][x] = 2
        q.append((y, x))
        if t in time.keys():
            direction = direction_change(direction, time[t])
        t += 1
    else:
        break

print(t)