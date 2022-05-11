import imp
import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    job = list(map(int, readl().split()))
    return N, M, job

def Solve(N, M, job):
    q = deque()
    cnt_prio = [0] * 10

    for id, prio in enumerate(job):
        q.append((id, prio))
        cnt_prio[prio] += 1
    
    cnt = 0
    for i in range(9, 0, -1):
        for _ in range(cnt_prio[i]):
            while True:
                id, prio = q.popleft()
                if prio == i:
                    break
                q.append((id, prio))
            cnt += 1
            if id == M:
                return cnt
    return -1


T = int(sys.stdin.readline())
sol = []
for _ in range(T):
    # 입력받는 부분
    N, M, job = Input_Data()

    # 여기서부터 작성
    ret = Solve(N, M, job)
    sol.append(ret)

print(*sol, sep='\n')