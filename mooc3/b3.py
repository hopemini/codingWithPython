import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0]*(N+1) for n in range(N+1)]
	return N, matrix


sol = -1
# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성
def dfs(s, c, sum):
    global sol
    if sol <= sum: return
    if s == N:
        if matrix[c][1] and sol > sum + matrix[c][1]:
            sol = sum + matrix[c][1]
        return


    for i in range(2, N+1):
        if chk[i]: continue
        if matrix[c][i] == 0: continue
        chk[i] = True
        dfs(s+1, i, sum + matrix[c][i])
        chk[i] = False

sol = 12*100
chk = [False] * (N+1)

dfs(1, 1, 0)

# 출력하는 부분
print(sol)