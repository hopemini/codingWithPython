import sys
from collections import deque

#def Input_Data():
#    readl = sys.stdin.readline
#    N, M = map(int, readl().split())
#    matrix = [[0] + list(map(int, readl().split())) + [0] if 1<=r<=N else [0] * (M+2) for r in range(N+2)]
#    return N, M, matrix


#N, M, matrix = Input_Data()
#print(matrix)
N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input())))

#print(matrix)

def bfs():
    q = deque()
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q.append((0, 0, 1))
    matrix[0][0] = 0
    while q:
        y, x, t = q.popleft()
        for dy, dx in d:
            ny, nx, nt = y + dy, x + dx, t + 1
            if not 0 <= ny <= N-1: continue
            if not 0 <= nx <= M-1: continue
            if matrix[ny][nx] == 0: continue
            if ny == N - 1 and nx == M - 1:
                return nt
            q.append((ny, nx, nt))
            matrix[ny][nx] = 0

    return -1

print(bfs())