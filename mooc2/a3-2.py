import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N


ans = []
# 입력 받는 부분
N = Input_Data()

# 여기서부터 작성
l = [0] * 25001
l[0] = "0/1"
l[-1] = "1/1"

for i in range(2, N+1):
    for j in range(1, i):
        idx = int(j/i*25000)
        if l[idx] == 0:
            l[idx] = "{}/{}".format(j, i)
ans = [x for x in l if x != 0]
# 출력하는 부분
print(*ans, sep='\n')