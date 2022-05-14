import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [int(readl()) for _ in range(N)]
    M = int(readl())
    return N, pos, M


sol = -1
# 입력받는 부분
#N, pos, M = Input_Data()

N = 4
pos = [120, 110, 140, 150]
M = 485


# 여기서부터 작성
pos.sort()
print(sum(pos)//4)
print(M//4)

# 출력하는 부분
print(sol)