import sys

def Input_Data():
    readl = sys.stdin.readline
    R = int(readl())
    return R


ans = 0
# 입력 받은 부분
R = Input_Data()

# 여기서부터 작성
R2 = R**2
#for h in range(1, R+1):
#    w = 0
#    while w**2 + h**2 <= R2:
#        w += 1
#    ans += w -1
for h in range(1, R+1):
    h2 = h**2
    ans += int((R2-h2) ** 0.5)
ans *= 4
# 출력하는 부분
print(ans)