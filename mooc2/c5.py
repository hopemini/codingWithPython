import sys


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [int(readl()) for _ in range(N)]
	return N, pos


sol = -1
# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
def Binary_Search_Lower(s, e, d):
    ret = -1
    while s<=e:
        m = (s+e)//2
        if pos[m]>=d:
            ret = m
            e = m-1
        else: s = m+1
    return ret
  
  
def Binary_Search_Upper(s, e, d):
    ret = -1
    while s<=e:
        m = (s+e)//2
        if pos[m]<=d:
            ret = m
            s = m+1
        else: e = m-1
    return ret

pos.sort()
cnt = 0
for s1 in range(N-2):
    for s2 in range(s1+1,N-1):
        jump = pos[s2] - pos[s1]
        rs = pos[s2] + jump
        re = pos[s2] + 2 * jump
        lower = Binary_Search_Lower(s2+1, N-1, rs)
        if lower == -1 or pos[lower] > re: continue
        upper = Binary_Search_Upper(lower, N-1, re)
        cnt += upper-lower+1
sol = cnt

# 출력하는 부분
print(sol)