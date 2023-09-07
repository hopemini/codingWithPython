import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0] * (N+1)  for n in range(N+1)]
	return N, matrix


sol = -1
# 입력 받는 부분
N, matrix = Input_Data()

chk = [False] * (N+1)
# 여기서부터 작성
def dfs(n, sum):
    global sol
    if sol <= sum:
        return
    if n > N:
        sol = sum
        return

    for i in range(1, N+1):
        if chk[i]: continue
        chk[i] = True
        dfs(n+1, sum + matrix[n][i])
        chk[i] = False

# 출력하는 부분
sol = 100 * N
dfs(1, 0)

print(sol)