import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_num = [int(readl()) for _ in range(N)]
    return N, list_num


ans = []
# 입력 받는 부분
N, list_num = Input_Data()

print(list_num)
# 여기서부터 작성
def Reverse(num):
    return int(''.join(reversed(str(num))))

def Reverse1(num):
    rev = 0
    while num:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

for num in list_num:
    sum = num + Reverse(num)
    ans.append("YES" if sum == Reverse(sum) else "No")

# 출력받는 부분
print(*ans,sep='\n')