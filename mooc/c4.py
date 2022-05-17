import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    R, C, S, K = map(int, readl().split())
    return N, M, R, C, S, K


sol = -1
N, M, R, C, S, K = Input_Data()

#N, M, R, C, S, K = 9, 9, 3, 5, 2, 8

def bfs():
    q = deque()
    d = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
    chk = [ [0] * (M+1) for _ in range(N+1)]
    q.append((R, C, 0))
    chk[R][C] = 1
    while q:
        h, w, t = q.popleft()
        for dh, dw in d:
            nh, nw, nt = h + dh, w + dw, t + 1
            if not 1 <= nh <= N: continue
            if not 1 <= nw <= M: continue
            if chk[nh][nw] == 1: continue

            if nh == S and nw == K:
                return nt
            q.append((nh, nw, nt))
            chk[nh][nw] = 1
    return -1

sol = bfs()
print(sol)