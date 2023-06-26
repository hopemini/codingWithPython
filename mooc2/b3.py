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
q = deque()
for i in range(N, 0, -1):
    q.append(i)

print(q)

# 출력하는 부분
print(*sol)