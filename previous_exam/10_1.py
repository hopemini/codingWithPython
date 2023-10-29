# 물류창고
# bfs 이용

import sys
from collections import deque


def input_data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	infos = [list(map(int, readl().split())) for _ in range(M)]
	return N, M, infos

sol = 987654321

# 입력받는 부분
N, M, infos = input_data()

INF = 987654321

dist_map = [[INF] * (N+1) for _ in range(N+1)]
for i in infos:
    dist_map[i[0]][i[1]] = i[2]
    dist_map[i[1]][i[0]] = i[2]

#print(dist_map)
def bfs(s):
    visit = [INF] * (N+1)
    q = deque()
    visit[s] = 0
    q.append((s, 0))

    while q:
        t, _ = q.popleft()
        for i in range(1, N+1):
            if t == i: continue
            if visit[i] <= visit[t] + dist_map[t][i]: continue
            visit[i] = visit[t] + dist_map[t][i]
            q.append((i, visit[t]))
    #print(visit)
    return max(visit[1:])

for i in range(1, N+1):
    ret = bfs(i)
    #print(ret)
    if sol > ret:
        sol = ret
print(sol)