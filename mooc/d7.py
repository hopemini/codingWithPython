from distutils.command.config import config
import sys
from collections import deque 
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_nor_pig = [[0] + list(readl()[:-1])+ [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_nor_pig


def bfs(map_pig, r, c):
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque()
    colors = map_pig[r][c]
    map_pig[r][c] = 0
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if map_pig[nr][nc] != colors: continue
            map_pig[nr][nc] = 0
            q.append((nr, nc))

sol_nor_pig, sol_rg_pig = 0, 0
# 입력받는 부분
N, map_nor_pig = Input_Data()
 

map_rg_pig = [['R' if map_nor_pig[r][c]=='G' else map_nor_pig[r][c] for c in range(N+2)] for r in range(N+2)]
# 여기서부터 작성
for r in range(1, N+1):
    for c in range(1, N+1):
        if map_nor_pig[r][c] != 0:
            bfs(map_nor_pig, r, c)
            sol_nor_pig += 1
        if map_rg_pig[r][c] != 0:
            bfs(map_rg_pig, r, c)
            sol_rg_pig += 1


# 출력하는 부분
print(sol_nor_pig, sol_rg_pig)