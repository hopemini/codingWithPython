import sys
from collections import deque


def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	matrix = [[0] + list(map(int, readl().split())) if 1<=s<=N else [0] * (N+1) for s in range(0, N+1)]
	return N, M, matrix


sol = -1
route = []
# 입력 받는 부분
N, M, matrix = Input_Data()

# 여기서부터 작성
def bfs():
    q = deque()
    chk = [9999999] * (N+1)
    prev = [0] * (N+1)
    q.append((1, 0))
    chk[1] = 0
    while q:
        n, t = q.popleft()
        if chk[n] < t: continue

        for nn in range(1, N+1):
            nt = t + matrix[n][nn]
            if chk[nn] <= nt: continue
            q.append((nn, nt))
            chk[nn] = nt
            prev[nn] = n

    return chk[M], prev

def get_route():
    r = []
    n = M
    while n != 0:
        r.append(n)
        n = prev[n]
    r.reverse()
    return r

sol, prev = bfs()
route = get_route()

# 출력하는 부분
print(sol)
print(*route)