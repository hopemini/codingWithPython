import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [list(map(int, readl().split())) for _ in range(N)]
	return N, pos


sol = -1
# 입력받는 부분
N, pos = Input_Data()
# 여기서부터 작성

def Make_Map():
    min_r, min_c = 1000, 1000
    max_r, max_c = 0, 0
    map_field = [[0] * 102 for _ in range(102)]
    for c, r in pos:
        map_field[r][c] = 1
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
    min_r -= 1
    max_r += 1
    min_c -= 1
    max_c += 1
    return min_r, max_r, min_c, max_c, map_field
  
  
def Flood_Fill(sr, sc):
    q = deque()
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    edge = 0
  
    map_field[sr][sc] = 2
    q.append((sr, sc))
  
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if not min_r <= nr <= max_r: continue
            if not min_c <= nc <= max_c: continue
            if map_field[nr][nc] == 0:
                map_field[nr][nc] = 2
                q.append((nr, nc))
            elif map_field[nr][nc] == 1:
                edge += 1
    return edge

  
# 여기서부터 작성
min_r, max_r, min_c, max_c, map_field = Make_Map()
sol = Flood_Fill(min_r, min_c)

# 출력하는 부분
print(sol)