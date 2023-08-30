import sys
from collections import deque


def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	R, C, S, K = map(int, readl().split())
	return N, M, R, C, S, K


sol = -1
# 입력 받는 부분
N, M, R, C, S, K = Input_Data()

# 여기서부터 작성
def bfs():
    d =((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
    q = deque()
    chk = [[0] * (M+2) for h in range(N+2)]
    q.append((R, C, 0))
    chk[R][C] = 1

    while q:
        x, y, c = q.popleft()
        for dx, dy in d:
            nx, ny, nc = x + dx, y + dy, c + 1
            if not 1 <= nx <= N: continue
            if not 1 <= ny <= M: continue
            if chk[nx][ny] == 1: continue
            if nx == S and ny == K:
                return nc
            q.append((nx, ny, nc))
            chk[nx][ny] = 1
    return -1

sol = bfs()

# 출력하는 부분
print(sol)