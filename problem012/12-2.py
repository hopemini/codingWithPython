import sys
from collections import deque

def Input_Data(): 
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    matrix = [[1]+list(map(int, readl()[:-1]))+[1] if 1<=r<=N else [1]*(M+2) for r in range(N+2)]
    
    return N, M, matrix

N, M, matrix = Input_Data()

def bfs(r, c):
    q = deque()
    d = ((-1,0), (1, 0), (0, -1), (0, 1))
    matrix[r][c] = 2
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if matrix[nr][nc] != 0: continue
            matrix[nr][nc] = 2
            q.append((nr, nc))

count = 0
for r in range(1, N+1):
    for c in range(1, M+1):
        if matrix[r][c] == 0:
            bfs(r, c)
            count += 1

print(count)