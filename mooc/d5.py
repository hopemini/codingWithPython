import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_apt = [list(map(int,list(readl().strip()))) for r in range(N)]
    return N, map_apt

sys.setrecursionlimit(25*25)
def flood_fill_dfs(r, c):
    global size
    size += 1
    map_apt[r][c] = 0
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if not 0 <= nr < N: continue
        if not 0 <= nc < N: continue
        if map_apt[nr][nc] == 0: continue
        flood_fill_dfs(nr, nc)

def flood_fill_bfs(r, c):
    q = deque()
    map_apt[r][c] = 0
    q.append((r, c))
    size = 1
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if not 0 <= nr < N: continue
            if not 0 <= nc < N: continue
            if map_apt[nr][nc] == 0: continue
            map_apt[nr][nc] = 0
            q.append((nr, nc))
            size += 1
    return size

def Solve():
    global size
    list_size = []
    for r in range(N):
        for c in range(N):
            if map_apt[r][c]:
                #size = 0
                #flood_fill_dfs(r, c)
                size = flood_fill_bfs(r, c)
                list_size.append(size)
    list_size.sort()
    return len(list_size), list_size

cnt = -1
list_size = []

N, map_apt = Input_Data()

size = 0
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
q = 0
cnt, list_size = Solve()



print(cnt)
print(*list_size,sep='\n')