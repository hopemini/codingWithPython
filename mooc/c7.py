import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_uv = [[0] + list(map(int, readl().strip())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
    return N, map_uv


sol = -1
N, map_uv = Input_Data()

def bfs():
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    sum = [[9999] * (N+2) for _ in range(N+2)]
    q = deque()
    sum[1][1] = map_uv[1][1]
    q.append((1, 1, map_uv[1][1]))

    while q:
        h, w, s = q.popleft()
        if sum[h][w] < s: continue
        for dh, dw in d:
            nh, nw = h + dh, w + dw
            if not 1<= nh <= N: continue
            if not 1<= nw <= N: continue
            ns = s + map_uv[nh][nw]
            if ns >= sum[nh][nw]: continue
            q.append((nh, nw, ns))
            sum[nh][nw] = ns
    return sum[N][N]

sol = bfs()
print(sol)