import sys
from collections import deque
  
  
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    height = [int(readl()) for _ in range(N)]
    return N, height
  
  
def Solve_N2():
    cnt = 0
    for i in range(N):
        h = height[i]
        for h_right in height[i+1:N]:
            if h > h_right:
                cnt += 1
            else:
                break
  
    return cnt
  
  
def Solve_N():
    cnt = 0
    stack = deque()
    for h in height:
        while stack and stack[-1] <= h:
            stack.pop()
        cnt += len(stack)
        stack.append(h)
          
    return cnt
  
  
sol = -1
# 입력받는 부분
N, height = Input_Data()
  
# 여기서부터 작성
# sol = Solve_N2()
sol = Solve_N()
  
# 출력하는 부분
print(sol)