import sys


def Input_Data():
    readl = sys.stdin.readline
    str_stick = readl().strip()
    return str_stick

ans = -1
# 입력 받는 부분
str_stick = Input_Data()

# 여기서부터 작성
stick = 0
seg = 0
for i in range(len(str_stick)):
    if str_stick[i] == '(':
        stick += 1
    else:
        stick -= 1
        seg += stick if str_stick[i-1] == '(' else 1

ans = seg

# 출력 하는 부분
print(ans)