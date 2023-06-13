import sys

def Input_Data():
    readl = sys.stdin.readline
    num = int(readl())
    return num


ans = 0
# 입력 받는 부분
num = Input_Data()

# 여기서부터 작성
while num != 6174:
#    num = [i for i in str(num)]
    num = str(num)
    num_max = sorted(num, reverse=True)
    num_min = sorted(num)
    num = int(''.join(num_max)) - int(''.join(num_min))
    ans += 1

# 출력하는 부분
print(ans)
