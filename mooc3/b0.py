import sys

def Input_Data():
    N, K = map(int, readl().split())
    num = list(map(int, readl().split()))
    return N, K, num

sol = []

def dfs_bin(n, remain):
    if remain == 0:
        return True
    if remain < 0:
        return False
    if n >= N:
        return False
    if dfs_bin(n+1, remain-num[n]):
        return True
    if dfs_bin(n+1, remain):
        return True
    return False

def dfs(s, remain):
    if remain == 0:
        return True
    if remain < 0:
        return False

    for n in range(s, N):
        if dfs(n+1, remain-num[n]):
            return True  
    return False

# 입력 받는 부분
readl = sys.stdin.readline

T = int(readl())
for _ in range(T):
    N, K, num = Input_Data()
    # 여기서부터 입력
    ret = dfs_bin(0, K)
    if ret: sol.append("YES")
    else: sol.append("NO")

# 출력하는 부분
print(*sol, sep = '\n')