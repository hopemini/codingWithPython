import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_lake = [[0] + list(map(int,list(readl().strip()))) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_lake


sol = 0
# 입력 받는 부분
N, map_lake = Input_Data()

def flood_fill_bfs(r, c):
    q = deque()
    d = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    map_lake[r][c] = 0
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if map_lake[nr][nc] == 0: continue
            map_lake[nr][nc] = 0
            q.append((nr, nc))

for r in range(1, N+1):
    for c in range(1, N+1):
        if map_lake[r][c] == 1:
            flood_fill_bfs(r, c)
            sol += 1


# 출력하는 부분
print(sol)