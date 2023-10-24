## 바이러스 검사
## https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8810/%EC%BD%94%EB%93%9C%EC%9D%B4%ED%95%B4-%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4-%EA%B2%80%EC%82%AC

import sys

def InputData():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	A = list(map(int, readl().split()))
	B = list(map(int, readl().split()))

	return N, M, A, B

def Find(start):
	P = A[start:start+M]
	P.sort()
	P = list(map(lambda x:x-P[0], P))
	return B == P

def Solve():
	sol = 0
	for i in range(N - M + 1) :
		sol += Find(i)
	return sol

sol = 0

# 입력
# N: 실행 코드의 데이터 개수
# M: 바이러스의 데이터 개수
# A: 실행 코드의 데이터
# B: 바이러스의 데이터
N, M, A, B = InputData()

B.sort()
B =list(map(lambda x:x-B[0], B))

# 코드를 작성하세요
sol = Solve()

# 출력
print(sol)
