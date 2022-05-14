import sys
from bisect import bisect_left, bisect_right


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [int(readl()) for _ in range(N)]
	return N, pos


sol = -1
# 입력받는 부분
#N, pos = Input_Data()
N = 5
pos = [3, 1, 10, 7, 4]


# [1, 3, 4, 7, 10]
pos.sort()

# 1, 3 -> 2, find 3 + 2 <= 7 <= 3+2*2
# 1, 4 -> 3, find 4 + 3 <= 7, 10<= 4 + 3*2
# 1, 7 -> 6, find 7 + 5 <= X <= 7 + 5*2
# 3, 4 -> 1, find 3 + 1 <= X <= 3 + 1*2
# 4, 7 -> 3, find 7 + 3 <= 10  <= 7 + 3*2
# (1, 3, 7), (1, 4, 7), (4, 7, 10), (1, 4, 10)
sol = 0
for i in range(N-2):
    for j in range(i+1, N):
        diff = pos[j] - pos[i]
        end = pos[j] + diff*2 
        l = bisect_left(pos, pos[j]+diff, lo=j)
        if l == N or pos[l] > end: continue
        r = bisect_right(pos, end, lo=l)
        sol += r - l
print(sol)
