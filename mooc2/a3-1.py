import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N


ans = []
# 입력 받는 부분
N = Input_Data()

l = [(0, 0, 1)]
for i in range(2, N+1):
    for j in range(1, i):
        l.append((j/i, j, i))
l.append((1, 1, 1))
l.sort()

ans = ['0/1']
for i in range(1, len(l)):
    if l[i-1][0] != l[i][0]:
        ans.append("{}/{}".format(l[i][1], l[i][2]))

# 출력하는 부분
print(*ans, sep='\n')