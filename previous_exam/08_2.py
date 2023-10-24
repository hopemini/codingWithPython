## 뱀
## https://www.acmicpc.net/problem/3190

from collections import deque

def direction_change(d, c):
    if c == 'L':
        d = ()
    else:
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

d = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 아래, 위, 왼, 오른

q = deque()
board[1][1] = 2
q.append((1, 1))
direction = (0, 1)
t = 1
while q:
    y, x = y + direction[0], x + direction[1]
    if not 1 <= x <= N: continue
    if not 1 <= y <= N: continue
    if board[y][x] == 2: continue
    if not board[y][x] == 1:
        dy, dx = q.popleft()
        board[dy][dx] = 0
    board[y][x] = 2
    q.append((y, x))
    if t in time.keys():
        direction = direction_change(direction, time[t])
    t += 1

print(t)