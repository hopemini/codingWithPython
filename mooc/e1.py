import sys
from collections import deque
 
 
def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int,readl().split())
    map_jewel = [[0] + list(readl().strip()) + [0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
    return R, C, map_jewel
 
 
def Get_Start():
    q_start = deque()
    [q_start.append((r,c)) for r in range(1, R+1) for c in range(1, C+1) if map_jewel[r][c] == 'L']
    return q_start
 
 
def BFS(sr,sc):
    q = deque()
    chk = [[0]*(C+2) for _ in range(R+2)]
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
 
    chk[sr][sc] = 1
    q.append((sr, sc, 0))
    while q:
        r, c, dist = q.popleft()
        for dr, dc in d:
            nr, nc, ndist = r + dr, c + dc, dist+1
            if map_jewel[nr][nc] != 'L' or chk[nr][nc]: continue
            chk[nr][nc] = 1
            q.append((nr, nc, ndist))

    return dist
 
 
def Solve(q_start):    
    return max([BFS(r, c) for r, c in q_start])
 
 
sol = -1
# 입력받는 부분
R, C, map_jewel = Input_Data()
 
# 여기서부터 작성
q_start = Get_Start()
sol = Solve(q_start)
 
# 출력하는 부분
print(sol)