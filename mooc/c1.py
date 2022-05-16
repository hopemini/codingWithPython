import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = list(map(int, readl().split()))
    M = int(readl())
    return N, pos, M


sol = -1
# 입력받는 부분
N, pos, M = Input_Data()
#M = 450
#N = 4
#pos = [120, 110, 140, 150]
#M = 485

def search(l, h):
    while l <= h:
        mid = (l + h) // 2
        total = 0
        for i in pos:
            if i > mid:
                total += mid
            else:
                total += i
        #total = sum([mid for i in pos if i > mid else i])
        if total > M:
            h = mid - 1
        elif total < M:
            l = mid + 1
        else:
            return mid
    return h

pos.sort()
sol = search(pos[0], pos[-1])
print(sol)