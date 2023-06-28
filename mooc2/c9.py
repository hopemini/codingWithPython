import sys
from bisect import bisect_left

def input_data():
    readl = sys.stdin.readline
    M, N, L = map(int, readl().split())
    shoots = list(map(int, readl().split()))
    animals = [list(map(int, readl().split())) for _ in range(N)]
    return M, N, L, shoots, animals


sol = -1

# 입력받는 부분
M, N, L, shoots, animals = input_data()

# 여기서부터 작성
def Solve():
    shoots.sort()
    cnt = 0
    for x, y in animals:
        if y > L: continue
        low = x - (L-y)
        up = x + (L-y)

        idx = bisect_left(shoots, low)
        if idx>=M or shoots[idx]>up:
            continue
        cnt+=1
    return cnt

sol = Solve()

# 출력받는 부분
print(sol)