import sys
   
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    W = list(map(int, readl().split()))
    V = list(map(int, readl().split()))
    A = int(readl())
    return N, W, V ,A
   
def DFS(n, remain, sum):
    global sol
    if remain == 0:                                 # N을 완성했다면?
        if sum > sol:                                # 기존 솔루션 후보보다 현재 경우의 수 평가가 더 좋다면
            sol = sum                               # 솔루션 후보 갱신
            for i in range(7): sol_cnt[i] = cnt[i]
        return
    if n == 7: return                               # n이 7이라면 더이상 사용할 2의 제곱수가 없으므로 돌아가기!
  
    # remain 일부 혹은 전부를 해결하기 위해 2**n 사용하기
    p = pow2[n]             # p = 2 ** n
    if remain % p: return   # p로 나눈 나머지가 존재 할 경우 p포함 이상의 2의 제곱수로 remain 완성 불가!
   
    for cnt_use in range(remain // p + 1):  # p의 사용개수에 대한 모든 경우의 수 시도
        cnt[n] = cnt_use
        DFS(n+1, remain-p*cnt_use, sum + cnt_use * (W[n] if cnt_use <= 4 else V[n]) + cnt_use * A)       
    cnt[n] = 0
   
sol, sol_cnt = -1, [0] * 7
# 입력받는 부분
N, W, V, A = Input_Data()
   
# 여기서부터 작성
cnt = [0] * 7                       # 각 동전별 사용개수 기록 하기 위한 list
pow2 = [1, 2, 4, 8, 16, 32, 64]     # N 완성 위한 2의 제곱수 목록 ( pow2[n] : 2**n )
   
DFS(0, N, 0)
   
# 출력하는 부분
print(sol)
print(*sol_cnt)