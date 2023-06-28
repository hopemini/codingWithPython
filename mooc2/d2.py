import sys
    
def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int,readl().split())
    mat = [list(map(int,readl().split())) for n in range(N)]
    return N, M, mat
    
def Get_Min_Cost(i, need):
    limits = need // mat[i][4] + (1 if need % mat[i][4] else 0)
    min_cost = mat[i][5] * limits
    for cnt_big in range(limits):
        cost = mat[i][5] * cnt_big
        remain = need - (mat[i][4] * cnt_big)
        cnt_small = remain // mat[i][2] + (1 if remain % mat[i][2] else 0)
        cost += mat[i][3] * cnt_small
        if min_cost > cost: min_cost = cost
    return min_cost
    
def Check(cnt_food):
    sum_cost = 0
    for i in range(N):
        need = cnt_food * mat[i][0] - mat[i][1]
        if need>0:
            sum_cost += Get_Min_Cost(i, need)
            if sum_cost > M:
                return False
    return True
    
def Get_Solution():
    e = 1
    while Check(e):
        e *= 2
    s = e//2
    
    while s<=e:
        m = (s+e)//2
        if Check(m):
            sol = m
            s = m+1
        else:
            e = m-1
    return sol
    
 
ans = -1
# 입력 받는 부분
N, M, mat = Input_Data()
 
# 여기서 부터 작성
sol = Get_Solution()
 
# 출력 하는 부분
print(sol)