import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	return N


sol = []
# 입력 받는 부분
N = Input_Data()

# 여기서부터 작성
q = deque(range(1, N+1))
while q:
	rot = q[-1] // 2
	for _ in range(rot):
		q.append(q.popleft())
	sol.append(q.popleft())


# 출력하는 부분
print(*sol)