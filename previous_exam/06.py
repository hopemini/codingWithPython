import sys

def InputData():
    readl = sys.stdin.readline
    B, S, D = readl().strip().split()
    return int(B), S, D
# 입력

# N : 테스트 케이스 수
# B : 진법
# S : 첫 번째 정수
# D : 두 번째 정수
d2c = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def c2d(s):
    if s<='9': return ord(s)-ord('0')
    else: return ord(s)-ord("A")+10

N = int(input())
for _ in range(N):
    B, S, D = InputData()
    ans = -1
    # 코드를 작성 하세요
    if S == '0' or D =='0':
        print('0')
        continue
    
    B = int(B)
    sign = 1
    if S[0] == '-': 
        sign *= -1
        S = S[1:]
    if D[0] == '-': 
        sign *= -1
        D = D[1:]

    A = [0 for _ in range(len(S)+len(D))]
    for i,v1 in enumerate(S):
        for j,v2 in enumerate(D):
            A[i+j+1] += c2d(v1)*c2d(v2)
    #A.reverse()
    #for i in range(len(A)-1):
    #    q,r = divmod(A[i],B)
    #    A[i] = r
    #    A[i+1] += q

    for i in range(len(A)-1, 0, -1):
        q = A[i] // B
        r = A[i] % B
        A[i] = r
        A[i-1] += q
    #A.reverse()
    if sign == -1:
        print("-", end="")
    if A[0] > 0:
        print(d2c[A[0]],end="")
    for i in range(1,len(A)):
        print(d2c[A[i]],end="")
    print()