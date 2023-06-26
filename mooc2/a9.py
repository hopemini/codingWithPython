import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	str_exp = readl().split()
	nums = list(map(int,str_exp[0::2]))
	op = str_exp[1::2]
	return N, nums, op


sol = 0
# 입력받는 부분
N, nums, op = Input_Data()

# 여기서부터 작성
s1 = deque()
s1.append(nums[0])
for o, n in zip(op, nums[1:]):
    if o == '+':
        s1.append(n)
    elif o == '-':
        s1.append(-n)
    elif o == '*':
        s1.append(s1.pop() * n)
    elif o == '/':
        s1.append(int(s1.pop() / n))

for s in s1:
    sol += s

# 출력하는 부분
print(sol)