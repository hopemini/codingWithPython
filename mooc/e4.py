import sys
from collections import deque 
 
def Input_Data():
    readl = sys.stdin.readline
    M = int(readl())
    N = int(readl())
    map_cell = [[0] + list(map(int, readl().split())) + [0] if 1 <= m <=M else [0] * (N+2) for m in range(M+2)]
    return M, N, map_cell


sol = -1
#입력 받는 부분
M, N, map_cell = Input_Data()

def bfs(r, c):
    q = deque()
    d = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),  (1, -1))
    map_cell[r][c] = 2
    q.append((r, c, 1))
    cnt = 1
    while q:
        r, c, dist = q.popleft()
        for dr, dc in d:
            nr, nc, ndist = r+dr, c+dc, dist+1
            if map_cell[nr][nc] != 1: continue
            map_cell[nr][nc] = 2
            q.append((nr, nc, ndist))
            cnt += 1
    return cnt

max_dist = -100
for r in range(1, M+1):
    for c in range(1, N+1):
        if map_cell[r][c] == 1:
            max_dist = max(max_dist, bfs(r, c))
sol = max_dist
print(sol)