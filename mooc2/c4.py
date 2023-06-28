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
def binary_search_lower(s, e, q):
	ret = -1
	while s <= e:
		m = (s + e) // 2
		if num[m] == q: 
			ret = m
			e = m - 1
		elif num[m] < q: s = m + 1
		else: e = m - 1
	return ret

def binary_search_upper(s, e, q):
	ret = -1
	while s <= e:
		m = (s + e) // 2
		if num[m] == q: 
			ret =  m
			s = m + 1
		elif num[m] < q: s = m + 1
		else: e = m - 1
	return ret


# 출력하는 부분
for q in query:
	lower = binary_search_lower(1, N, q)
	if lower == -1: 
		sol.append(0)
	else:
		upper = binary_search_upper(1, N, q)
		sol.append(upper - lower + 1)
print(*sol)