from collections import deque

X = int(input())

def bfs():
    q = deque
    chk = [0] * 1000
    d = (5, 3, 2, 1)
    q.append(X)
    
    while q:
        nX = q.popleft()
        for i in d:
            if i == 1:
                nX = nX - 1
            else:
                if nX % i == 0:
                    nX //= i
            q.append(nX)
            chk[nX]