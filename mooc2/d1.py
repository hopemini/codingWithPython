import sys

def Input_Data():
    readl = sys.stdin.readline
    str_org = readl().split()
    str_boom = readl().split()
    return str_org, str_boom

# 입력 받는 부분
str_org = input().strip() 
str_boom = input().strip() 

# 여기서부터 작성
stack = []

for c in str_org:
    stack.append(c)
    if c == str_boom[-1]:
        if ''.join(stack[-len(str_boom):]) == str_boom:
            del stack[-len(str_boom):]

ans = ''.join(stack)
if ans == '':
    print('FRULA')
else:
    print(ans)