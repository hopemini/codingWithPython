import sys
from collections import deque
  
def Input_Data():
    readl = sys.stdin.readline
    M, N = map(int,readl().split())
    K = int(readl())
    list_bus = [list(map(int,readl().split())) for _ in range(K)]
    sx, sy, dx, dy = map(int,readl().split())
    return M, N, K, list_bus, sx, sy, dx, dy

# 입력 받는 부분
M, N, K, list_bus, sx, sy, dx, dy = Input_Data()

# 여기서부터 작성
start = deque() # 현재 탈수 있는 버스
s = set()
# sx, sy에서 탈 수 있는 버스
for i, bus in enumerate(list_bus):
    n, x1, y1, x2, y2 = bus
    if min(x1,x2) <= sx and max(x1, x2) >= sx and min(y1,y2) <= sy and max(y1, y2) >= sy:
        start.append((i, 1))
        s.add(i)

# 목적지를 포함하는 버스 노선 확인하기
target = set()
for i, bus in enumerate(list_bus):
    n, x1, y1, x2, y2 = bus
    if min(x1,x2) <= dx and max(x1, x2) >= dx and min(y1,y2) <= dy and max(y1, y2) >= dy:
        target.add(i)

def isTransfered(bus1, bus2):
    bus1 = list_bus[bus1]
    bus2 = list_bus[bus2]
    if max(bus1[0], bus1[2]) < min(bus2[0], bus2[2]) or min(bus1[0], bus1[2]) > max(bus2[0], bus2[2]):
        return False
    if max(bus1[1], bus1[3]) < min(bus2[1], bus2[3]) or min(bus1[1], bus1[3]) > max(bus2[1], bus2[3]):
        return False
    return True


answer = 1
visited = set(start)
if len(s&target) == 0:
    while True:
        cur, cnt = start.popleft()
        # print(cur, cnt)
        for i in range(K):
            if i in visited:
                continue
            if isTransfered(i, cur):
                if i in target:
                    answer = cnt + 1
                    break
                start.append((i, cnt + 1))
                visited.add(i)

        if answer > 1:
            break
print(answer)
