import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	M, N = map(int, readl().split())
	map_box = [[0] + list(map(int, readl().split())) + [0] if 1<=r<=N else [0] * (M+2) for r in range(N+2)]
	return M, N, map_box


sol = -1
# 입력 받는 부분
M, N, map_box = Input_Data()

# 여기서부터 작성
def bfs():
    d = ((-1, 0), (1, 0), (0, 1), (0, -1))
    q = deque()
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if map_box[i][j] == 1:
                q.append((i, j, 0))
            elif map_box[i][j] == 0:
                cnt += 1
    if cnt == 0: return 0

    while q:
        y, x, c = q.popleft()
        for dy, dx in d:
            ny, nx, nc = y + dy, x + dx, c + 1
            if not 1 <= nx <= M: continue
            if not 1 <= ny <= N: continue
            if map_box[ny][nx] == -1 or map_box[ny][nx] == 1: continue
            q.append((ny, nx, nc))
            map_box[ny][nx] = 1
            cnt -= 1
            if cnt == 0: return nc

    return -1

sol = bfs()
# 출력하는 부분
print(sol)