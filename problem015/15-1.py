from re import T
import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    D = list(map(int, readl().split()))
    return N, D

N, D = input_data()

def Solve1():
    sol = -30001
    for i in range(N-2):
        t = sum(D[i:i+3])
        if t > sol:
            sol = t
    return sol

def Solve2():
    sol = -30001
    sum = 0
    for i in range(N):
        if sum > 0:
            sum += D[i]
        else:
            sum = D[i]
        if sum > sol:
            sol = sum
    return sol

sol1 = Solve1()
sol2 = Solve2()
print(sol1, sol2)
