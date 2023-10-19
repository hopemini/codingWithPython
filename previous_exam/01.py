import sys

def input_data() :
	readl = sys.stdin.readline
	N = int(readl())#협찬 물품의 수
	D = list(map(int, readl().split()))#선호도 
	return N, D


def Solve():
    sol = -30001#첫번째 방법의 최대 선호도
    sum = 0
    # 1st option
    #for i in range(N-2):
    #    sum = D[i] + D[i+1] + D[i+2]
    #    if sum > sol:
    #        sol = sum
    #return sol
    for i in range(N):
        if sum > 0:
            sum += D[i]
        else:
            sum = D[i]
        if sum > sol:
            sol = sum
    return sol

# N^2
def Solve2():
    sol = -30001
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += D[j]
            if sol < sum:
                sol = sum
    return sol

#입력받는 부분
N, D = input_data()
sol = Solve()
print(sol)#출력하는 부분
