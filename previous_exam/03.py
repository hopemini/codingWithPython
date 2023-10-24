## 노즐 교체
## https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8811/%EB%85%B8%EC%A6%90-%EA%B5%90%EC%B2%B4

import sys

def input_data():
	readl = sys.stdin.readline
	n = int(readl())
	a = [list(map(int, readl().split())) for y in range(n)]
	return n, a


# 입력
# N : 장비에 장착된 노즐의 가로, 세로 개수
# A : 각 노즐의 오염도 정보
sol = -1
N, A = input_data()

# 코드를 작성하세요
def Solve():
	
	h = 0
	for y in range(N):
		sum = [0] * 2
		for x in range(N):
			sum[x%2] += A[y][x]
		h += max(sum[0], sum[1])
	v = 0
	for x in range(N):
		sum = [0] * 2
		for y in range(N):
			sum[y%2] += A[y][x]
		v += max(sum[0], sum[1])
	return max(h, v)

	# even_sum = [sum(row[0::2]) for row in A]
	# odd_sum = [sum(row[1::2])for row in A]
	# sum1 = sum([max(i, j) for i, j in zip(odd_sum, even_sum)])

	# even_sum = [sum(col[0::2]) for col in zip(*A)]
	# odd_sum = [sum(col[1::2]) for col in zip(*A)]
	# sum2 = sum([max(i, j) for i, j in zip(odd_sum, even_sum)])
	# return max(sum1, sum2)

sol = Solve()
# 출력
print(sol)
