import sys
from collections import deque 
 
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_nor_pig = [[0] + list(readl()[:-1])+ [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
	return N, map_nor_pig


sol_nor_pig, sol_rg_pig = -1, -1
# 입력받는 부분
N, map_nor_pig = Input_Data()
 
# 여기서부터 작성
d = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(y, x):
    q = deque()
    chk[y][x] = 1
    color = map_nor_pig[y][x]
    q.append((y, x, color))

    while q:
        y, x, color = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if chk[ny][nx] == 1: continue
            ncolor = map_nor_pig[ny][nx]
            if color != ncolor: continue
            chk[ny][nx] = 1
            q.append((ny, nx, ncolor))
            

red, green, blue = 0, 0, 0
chk = [[0] * (N+2) for _ in range(N+2)]
for y in range(1, N+1):
    for x in range(1, N+1):
        if chk[y][x] == 0:
            if map_nor_pig[y][x] == 'R':
                bfs(y, x)
                red += 1
            elif map_nor_pig[y][x] == 'G':
                bfs(y, x)
                green += 1
            else:
                bfs(y, x)
                blue += 1

sol_nor_pig = red + green + blue

chk = [[0] * (N+2) for _ in range(N+2)]
for y in range(1, N+1):
    for x in range(1, N+1):
        if map_nor_pig[y][x] == 'G':
            map_nor_pig[y][x] = 'R'

red , blue = 0, 0
for y in range(1, N+1):
    for x in range(1, N+1):
        if chk[y][x] == 0:
            if map_nor_pig[y][x] == 'R':
                bfs(y, x)
                red += 1
            else:
                bfs(y, x)
                blue += 1

sol_rg_pig = red + blue

# 출력하는 부분
print(sol_nor_pig, sol_rg_pig)