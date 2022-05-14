from re import S
import sys
from bisect import bisect_left, bisect_right

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [0] + list(map(int, readl().split()))
    T = int(readl())
    query = list(map(int, readl().split()))
    return N, num, T, query


sol = []
# 입력받는 부분
#N, num, T, query = Input_Data()
N = 7
num = [0, 2, 4, 9, 9, 10, 14, 23, 32]
T = 3
query = [6, 23, 9]


def search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if num[mid] == target:
            return mid
        elif num[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

s=0
for i in query:
    l = bisect_left(num, i, lo=1)
    if l != len(num) and num[l] == i:
        sol.append(l)
    else:
        sol.append(0)
    #print(l, r)
    #if l == r:
    #    s = 0
    #elif r-l == 1:
    #    s = l
    #else:
    #    s= l + 1
    #sol.append(s)

# 출력하는 부분
print(*sol, sep = '\n')