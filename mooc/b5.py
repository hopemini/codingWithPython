from struct import pack
import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    package = list(map(int,readl().split()))
    return N, package


sol = 0
#N, package = Input_Data()

N = 5
package = [2, 2, 5, 3]

#package.sort(reverse=True)
#while len(package) > 1:
#    sum = package.pop() + package.pop()
#    sol += sum
#    package.append(sum)
#    package.sort(reverse=True)
    
def Simple_Sort(s, e, n):
    for i in range(s, s+n):
        for j in range(i+1, e+1):
            if package[i] > package[j]:
                package[i], package[j] = package[j], package[i]

def Solve():
    sum = 0
    for i in range(N-1):
        #Simple_Sort(i, N-1, 2)
        package[i:N] = sorted(package[i:N])

        package[i+1] = package[i] + package[i+1]
        sum += package[i+1]
    return sum

def Solve2():
    package.sort(reverse=True)
    sol = 0
    while len(package) > 1:
        sum = package.pop() + package.pop()
        sol += sum
        package.append(sum)
        package.sort(reverse=True)
    return sol

sol = Solve2()
print(sol)