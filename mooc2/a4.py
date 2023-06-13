import sys

def Input_Data():
    readl = sys.stdin.readline
    R = int(readl())
    return R


ans = 0
# 입력 받은 부분
R = Input_Data()

# 여기서부터 작성
diag = 2**(1/2)
i = 1
while R > diag * i:
    i += 1
#i -= 1
print(i)
ans = i * i * 4

# 출력하는 부분
print(ans)