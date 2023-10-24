## 카드2
## https://www.acmicpc.net/problem/2164

from collections import deque
import sys

N = int(sys.stdin.readline())

q = deque()
""" for i in range(N):
    q.append(i+1)
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q.pop())
 """
for i in range(N):
    q.append(N-i)
while len(q) > 1:
    q.pop()
    q.appendleft(q.pop())
print(q.pop())