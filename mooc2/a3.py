import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N


ans = []
# 입력 받는 부분
N = Input_Data()

res = 0
temp = [0, 1]
ans = ['0/1', '1/1']
# 여기서부터 작성
for i in range(2, N+1):
    for j in range(1, i):
        res = j / i
        if res in temp:
            continue
        temp.append(res)
        ans.append(str(j) + '/' + str(i))

ans = list(zip(temp, ans))
ans.sort()
_, ans = zip(*ans)
# 출력하는 부분
print(*ans, sep='\n')