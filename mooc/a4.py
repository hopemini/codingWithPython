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
N, nums, op = Input_Data()

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

#sol = sum(s1)
for s in s1:
    sol += s
print(sol)
