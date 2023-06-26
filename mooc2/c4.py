import sys


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	num = [0] + list(map(int, readl().split()))
	T = int(readl())
	query = list(map(int, readl().split()))
	return N, num, T, query


sol = []
# 입력받는 부분
N, num, T, query = Input_Data()

# 여기서부터 작성
def binary_search(s, e, q):
    while s <= e:
        m = (s + e) // 2
        if num[m] == q: return m
        elif num[m] < q: s = m + 1
        else: e = m - 1

# 출력하는 부분
print(*sol)