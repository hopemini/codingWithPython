## 건물옥상정원
## https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8813/%EA%B1%B4%EB%AC%BC%EC%98%A5%EC%83%81%EC%A0%95%EC%9B%90

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