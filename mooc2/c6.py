import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    needs = list(map(int, readl().split()))
    M = int(readl())
    return N, needs, M


sol = -1
# 입력받는 부분
N, needs, M = Input_Data()

# 여기서부터 작성
def Check(limit):
    s = 0
    for n in needs:
        s += n if n <limit else limit
    return s <= M

s, e = 0, max(needs)
while s <= e:
    m = (s + e) // 2
    if Check(m):
        sol = m
        s = m + 1
    else:
        e = m - 1

# 출력하는 부분
print(sol)