import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    M, N = map(int, readl().split())
    map_box = [[0] + list(map(int, readl().split())) + [0] if 1<=r<=N else [0] * (M+2) for r in range(N+2)]
    return M, N, map_box


sol = -1
M, N, map_box = Input_Data()

def bfs():
    q = deque()
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if map_box[i][j] == 1:
                q.append((i, j, 0))
            elif map_box[i][j] == 0:
                cnt += 1
    if cnt == 0: return 0

    while q:
        h, w, t = q.popleft()
        for dh, dw in d:
            nh, nw, nt = h + dh, w + dw, t + 1
            if not 1 <= nh <= N: continue
            if not 1 <= nw <= M: continue
            if map_box[nh][nw] == 1 or map_box[nh][nw] == -1: continue
            q.append((nh, nw, nt))
            map_box[nh][nw] = 1
            cnt -= 1
            if cnt == 0: return nt
    #for i in range(1, N+1):
    #    for j in range(1, M+1):
    #        if map_box[i][j] == 0:
    #            return -1
    return -1

sol = bfs()
print(sol)