import sys

'''
첫 번째 줄에 임의의 수 N이 입력된다. (1<=N<=64)
두 번째 줄에는 2의 제곱수인 1,2,4,8,16,32,64 의 4개 이하 사용 시 가치 Wi가 공백으로 구분되어 입력된다. (1<=Wi<=2000)
세 번째 줄에는 2의 제곱수인 1,2,4,8,16,32,64 의 5개 이상 사용 시 가치 Vi가 공백으로 구분되어 입력된다. (1<=Vi<=2000)
네 번쩨 줄에는 항 하나당 추가 가치 A가 주어진다. (1<=A<=30)
'''
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	W = list(map(int, readl().split()))
	V = list(map(int, readl().split()))
	A = int(readl())
	return N, W, V ,A

sol, sol_cnt = -1, [0] * 7
# 입력받는 부분
N, W, V, A = Input_Data()


# 여기서부터 작성
chk = [0] * 7
two_double = [1, 2, 4, 8, 16, 32, 64]
def checkHang():
    ret = 0
    for i in range(7):
        ret += chk[i]
    return ret

def dfs(n, sum):
    global sol, sol_cnt
    if sum > N: return
    if sum == N:
        value = 0
        for k in range(7):
            if chk[k] >= 5:
                value += (chk[k] * V[k])
            else:
                value += (chk[k] * W[k])
        value += (A * checkHang())

        if value > sol:
            sol = value
            for l in range(7):
                sol_cnt[l] = chk[l]
        return
    for i in range(n, 7):
        chk[i] += 1
        dfs(i, sum + two_double[i])
        chk[i] -= 1

dfs(0, 0)
# 출력하는 부분
print(sol)
print(*sol_cnt)