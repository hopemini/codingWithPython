import sys
from collections import deque


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_uv = [[0] + list(map(int, readl().strip())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
	return N, map_uv


sol = -1
# 입력 받는 부분
N, map_uv = Input_Data()

# 여기서부터 작성
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs():
    q = deque()
    sum = [[9999] * (N+2) for _ in range(N+2)]
    sum[1][1] = map_uv[1][1]
    q.append((1, 1, map_uv[1][1]))
    while q:
        y, x, val = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not 1<= ny <= N: continue
            if not 1<= nx <= N: continue
            nval = val + map_uv[ny][nx]
            if nval >= sum[ny][nx]: continue
            q.append((ny, nx, nval))
            sum[ny][nx] = nval
    return sum[N][N]

sol = bfs()

# 출력하는 부분
print(sol)