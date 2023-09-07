import sys
from collections import deque 
 
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_nor_pig = [[0] + list(readl()[:-1])+ [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
	return N, map_nor_pig


sol_nor_pig, sol_rg_pig = -1, -1
# 입력받는 부분
N, map_nor_pig = Input_Data()
 
# 여기서부터 작성
def Flood_Fill(map_art, y, x):
    #global q
    d = ((-1, 0), (1, 0), (0, 1), (0, -1))
    q = deque()
    q.append((y, x))
    color = map_art[y][x]
    map_art[y][x] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if map_art[ny][nx] != color: continue
            q.append((ny, nx))
            map_art[ny][nx] = 0

def Get_Answer(map_art):
    cnt_area = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            if map_art[r][c] != 0:
                Flood_Fill(map_art, r, c)
                cnt_area += 1
    return cnt_area
  
  
def Solve():
    return Get_Answer(map_nor_pig), Get_Answer(map_rg_pig)


map_rg_pig = [['R' if map_nor_pig[r][c]=='G' else map_nor_pig[r][c] for c in range(N+2)] for r in range(N+2)]
sol_nor_pig, sol_rg_pig = Solve()

# 출력하는 부분
print(sol_nor_pig, sol_rg_pig)