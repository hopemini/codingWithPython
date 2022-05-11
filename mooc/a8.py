import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N

def Solve(N):
    q = deque([i for i in range(1, N+1)])
    while q: 
        r = q[-1] // 2
        #for _ in range(r):
        #    q.append(q.popleft())
        q.rotate(-r)
        sol.append(q.popleft())

sol = []
N = Input_Data()

Solve(N)

print(*sol)