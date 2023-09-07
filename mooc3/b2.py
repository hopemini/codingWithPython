import sys
 
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	A, B = map(int, readl().split())
	S = int(readl())
	seq = [int(readl()) for _ in range(S)]
	return N, A, B, S, seq
 
 
sol = -1
 
#입력받는 부분
N, A, B, S, seq = Input_Data()
 
# 여기서부터 작성

def dfs(s, left, right, sum_move):
    global sol
    if sol <= sum_move:
        return
    if s >= S:
        sol = sum_move
        return

    if seq[s] < right:
        dfs(s+1, seq[s], right, sum_move + abs(left-seq[s]))
    if left < seq[s]: 
        dfs(s+1, left, seq[s], sum_move + abs(right-seq[s]))


sol = 99999
dfs(0, min(A, B), max(A, B), 0)
 
# 출력하는 부분
print(sol)