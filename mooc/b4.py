import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_score = list(map(int, readl().split()))
    return N, list_score


sol = [-1, -1, -1]
#N, list_score = Input_Data()

N = 8
list_score = [70, 30, 70, 40, 60, 50, 90, 80]

A = list(zip(list_score, range(1, N+1)))
B = sorted(A, key=lambda x : (-x[0], x[1]))
sol = [i[1] for i in B][0:3]
#sol = list(zip(*B))[1][0:3]
print(*sol)