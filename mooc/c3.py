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

#W, H = 8, 7
#sw, sh, ew, eh = 1, 2, 7, 5
#map_maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# 여기서부터 작성
def bfs():
    d = ((-1, 0), (1, 0), (0, -1), (0, 1)) # (h, w)
    q = deque()
    chk = [[0] * (W + 2) for h in range(H + 2)] # chk[h][w]

    q.append((sh, sw, 0)) # (h, w, time)
    chk[sh][sw] = 1

    while q:
        h, w, t = q.popleft()
        for dh, dw in d:
            nh, nw, nt = h + dh, w + dw, t + 1
            if not 1 <= nh <= H: continue
            if not 1 <= nw <= W: continue 
            if map_maze[nh][nw] == 1: continue
            if chk[nh][nw] == 1: continue

            if nh == eh and nw == ew:
                return nt

            q.append((nh, nw, nt))
            chk[nh][nw] = 1
    return -1

def bfs_no_chk():
    d = ((-1, 0), (1, 0), (0, -1), (0, 1)) # (h, w)
    q = deque()

    q.append((sh, sw, 0)) # (h, w, time)
    map_maze[sh][sw] = 1

    while q:
        h, w, t = q.popleft()
        for dh, dw in d:
            nh, nw, nt = h + dh, w + dw, t + 1
            if not 1 <= nh <= H: continue
            if not 1 <= nw <= W: continue 
            if map_maze[nh][nw] == 1: continue

            if nh == eh and nw == ew:
                return nt

            q.append((nh, nw, nt))
            map_maze[nh][nw] = 1
    return -1

sol = bfs_no_chk()
# 출력하는 부분
print(sol)