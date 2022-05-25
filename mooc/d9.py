import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    height = [int(readl()) for _ in range(N)]
    return N, height


sol = -1
# 입력받는 부분
N, height = Input_Data()

# 여기서부터 작성
cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if height[i] > height[j]:
            cnt += 1
        elif height[i] < height[j]:
            break

print(cnt)
# 출력하는 부분
print(sol)