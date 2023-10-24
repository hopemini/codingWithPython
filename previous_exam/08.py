## 도로건설
## https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8816/%EB%8F%84%EB%A1%9C%EA%B1%B4%EC%84%A4

import sys

def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	map_cost = [
		[0] + list(map(int, readl()[:-1])) + [0] if 1 <= r <= N else [0] * (N + 2)
		for r in range(N + 2)
	]
	return N, map_cost


sol = -2

# 입력받는 부분
N, map_cost = input_data()

# 여기서부터 작성
## heapq 사용
from heapq import *
def bfs():
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    Q = [(1, 1, map_cost[1][1])]
    sum = [[9999] * (N+2) for _ in range(N+2)]
    sum[1][1] = map_cost[1][1]

    while Q:
        y, x, c = heappop(Q)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not 1 <= ny <= N: continue
            if not 1 <= nx <= N: continue
            nc = c + map_cost[ny][nx]
            if nc >= sum[ny][nx]: continue
            Q.append((ny, nx, nc))
            sum[ny][nx] = nc
    return sum[N][N]

## deque 사용
## TC #9, #10 Timeout
from collections import deque
def bfs2():
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque()
    q.append((1, 1, map_cost[1][1]))
    sum = [[9999] * (N+2) for _ in range(N+2)]
    sum[1][1] = map_cost[1][1]

    while q:
        y, x, c = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not 1 <= ny <= N: continue
            if not 1 <= nx <= N: continue
            nc = c + map_cost[ny][nx]
            if nc >= sum[ny][nx]: continue
            sum[ny][nx] = nc
            q.append((ny, nx, nc))
    return sum[N][N]

sol = bfs()

# 출력하는 부분
print(sol)
