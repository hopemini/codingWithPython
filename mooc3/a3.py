import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	W, H = map(int, readl().split())
	sw, sh, ew, eh = map(int, readl().split())
	map_maze = [[0] + list(map(int, readl().strip())) + [0] if 1<=h<=H else [0] * (W+2) for h in range(H+2)]
	return W, H, sw, sh, ew, eh, map_maze


sol = -1
# 입력 받는 부분
W, H, sw, sh, ew, eh, map_maze = Input_Data()

# 여기서부터 작성
def bfs():
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque()
    q.append((sh, sw, 0))
    map_maze[sh][sw] = 1

    while q:
        h, w, c = q.popleft()
        for dh, dw in d:
            nh, nw, nc = h + dh, w + dw, c+1
            if not 1<= nh <= H: continue
            if not 1<= nw <= W: continue
            if map_maze[nh][nw] == 1: continue
            if nh == eh and nw == ew:
                return nc
            q.append((nh, nw, nc))
            map_maze[nh][nw] = 1
    return -1


sol = bfs()
# 출력하는 부분
print(sol)