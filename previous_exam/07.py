## 그림인식
## https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8815/%EA%B7%B8%EB%A6%BC%EC%9D%B8%EC%8B%9D

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	map_pic = [list(map(int, readl().strip())) for _ in range(N)]
	return N, map_pic


sol = -1
# 입력받는 부분
N, map_pic = input_data()

# 여기서부터 작성


# 출력하는 부분
print(sol)
