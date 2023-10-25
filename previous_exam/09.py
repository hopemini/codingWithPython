## 무인열차
## https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8818/%EB%AC%B4%EC%9D%B8%EC%97%B4%EC%B0%A8


import sys
from collections import deque


def input_data():
	readl = sys.stdin.readline
	R, C = map(int, readl().split())
	map_line = [
		[0] + list(map(int, readl().split())) + [0] if 1 <= r <= R else [0] * (C + 2)
		for r in range(R + 2)
	]
	return R, C, map_line


sol = -1
# 입력받는 부분
R, C, map_line = input_data()

# 여기서부터 작성
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
def change_map(r, c):
    q = deque()
    q.append((r, c))
    map_line[r][c] = 2

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if not 1 <= nr <= R: continue
            if not 1 <= nc <= C: continue
            if map_line[nr][nc] == 2: continue
            if map_line[nr][nc] == 0: continue
            q.append((nr, nc))
            map_line[nr][nc] = 2

def change_map_dfs(r, c):
    map_line[r][c] = 2
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 1 <= nr <= R and 1 <= nc <= C and map_line[nr][nc]==1:
            change_map_dfs(nr, nc)


flag = False
for r in range(R+2):
    for c in range(C+2):
        if map_line[r][c] == 1:
            change_map_dfs(r, c)
            flag = True
            break
    if flag: break

def find_distance(r, c):
    dist = [[9999] * (C+2) for _ in range(R+2)]
    dist[r][c] = 0
    q = deque()
    q.append((r, c))

    while q:
        r, c = q.popleft()
        if map_line[r][c] == 1:
            return dist[r][c] - 1
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if not 1 <= nr <= R: continue
            if not 1 <= nc <= C: continue
            if map_line[nr][nc] == 2: continue
            if dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return 9999


dist = 987654321
for r in range(R+2):
    for c in range(C+2):
        if map_line[r][c] == 2:
            dist = min(dist, find_distance(r, c))

# 출력하는 부분
print(dist)
