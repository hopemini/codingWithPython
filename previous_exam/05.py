import sys

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	H = [ int(readl()) for i in range(N) ]
	return N, H


# 입력
# N: 건물 수
# H: 건물 높이
N, H = InputData()
ans = 0

# 코드를 작성 하세요
## timeout
# for i in range(N):
#     for j in range(i+1, N):
#         if H[i] > H[j]:
#             ans += 1
#         else:
#             break
A = []
for i in range(N):
    if not A:
        A.append(H[i])
    else:
        while A and A[-1]<=H[i]:
            A.pop()
        ans += len(A)
        A.append(H[i])
# 출력
print(ans)