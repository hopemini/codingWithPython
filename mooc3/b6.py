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

# 여기서부터 작성
d = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def bfs(y, x):
    q = deque()
    map_lake[y][x] = 0
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if map_lake[ny][nx] == 0: continue
            map_lake[ny][nx] = 0
            q.append((ny, nx))

for y in range(1, N+1):
    for x in range(1, N+1):
        if map_lake[y][x] == 1:
            bfs(y, x)
            sol += 1
# 출력하는 부분
print(sol)