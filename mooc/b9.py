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

N = 10
num = [0, 1, 1, 1, 6, 9, 11, 13, 17, 19, 20] 
T = 2
query = [1, 9] 

# 여기서부터 작성
for q in query:
    l = bisect_left(num, q, lo=1)
    r = bisect_right(num, q, lo=1)
    #print (l, r)
    sol.append(r - l)

# 출력하는 부분
print(*sol)