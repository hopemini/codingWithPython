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
def find_number(start, end, q):
	
	while start <= end:
		mid = (start + end) // 2
		if q == num[mid]: return mid
		elif q < num[mid]:
			end = mid - 1
		else:
			start = mid + 1
	return -1

for q in query:
	ret = find_number(1, N, q)
	if ret == -1: sol.append(0)
	else: sol.append(ret)

# 출력하는 부분
print(*sol, sep = '\n')