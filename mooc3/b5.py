import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_apt = [list(map(int,list(readl().strip()))) for r in range(N)]
	return N, map_apt

cnt = -1
list_size = []

# 입력 받는 부분
N, map_apt = Input_Data()

d = ((-1, 0), (1, 0), (0, -1), (0, 1))

# 여기서부터 작성
def bfs(y, x):
    q = deque()
    map_apt[y][x]  = 0
    size = 1
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not 0 <= ny < N: continue
            if not 0 <= nx < N: continue
            if map_apt[ny][nx] == 0: continue
            map_apt[ny][nx] = 0
            size += 1
            q.append((ny, nx))
    return size


def Solve():
    global size
    list_size = []
    for y in range(N):
        for x in range(N):
            if map_apt[y][x]:
                size = bfs(y, x)
                list_size.append(size)
    list_size.sort()
    return len(list_size), list_size

cnt, list_size = Solve()
# 출력하는 부분
print(cnt)
print(*list_size,sep='\n')