# 불우이웃돕기
# https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8820/%EB%B6%88%EC%9A%B0%EC%9D%B4%EC%9B%83%EB%8F%95%EA%B8%B0

import sys


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	cnt_box = list(map(int, readl().split()))
	return N, cnt_box


sol = 0
sol_box_cnt = [0] * 10

# 입력받는 부분
N, cnt_box = input_data()

# 여기서부터 작성
box_type = [1, 5, 10, 50, 100, 500, 1000, 3000, 6000, 12000]
sol_box_cnt[0] = 0

for i in range(N):
	for j in range(box_type[i], ):
		
# 출력하는 부분
print(sol)
print(*sol_box_cnt)
