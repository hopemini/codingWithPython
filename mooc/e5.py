import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int, readl().split())
    map_zergling = [[0]+list(map(int, readl()[:-1]))+[0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
    sc, sr = map(int, readl().split())
    return C, R, sc, sr, map_zergling


sol_time, sol_zergling = -1, 0

# 입력받는 부분
C, R, sc, sr, map_zergling = Input_Data()
 
# 여기서부터 작성
def bfs(r, c):
    q = deque()
    map_zergling[r][c] = 3
    q.append((r, c, 3))
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while q:
        r, c, n = q.popleft()
        for dr, dc in d:
            nr, nc, nn = r+dr, c+dc, n+1
            if map_zergling[nr][nc] != 1: continue
            map_zergling[nr][nc] = nn
            q.append((nr, nc, nn))
    return n

sol_time = bfs(sr, sc)
#for r in range(1, R+1):
#    for c in range(1, C+1):
#        if map_zergling[r][c] == 1:
#            sol_zergling += 1
sol_zergling = sum(ones.count(1) for ones in map_zergling)

print(sol_time, sol_zergling, sep='\n')