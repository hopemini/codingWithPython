import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	list_score = list(map(int, readl().split()))
	return N, list_score


sol = [-1, -1, -1]
# 입력받는 부분
N, list_score = Input_Data()

# 여기서부터 받는
l_s = list(enumerate(list_score))
#l_s.sort(key=lambda x:x[1], reverse=True)
l_s.sort(key=lambda x:(-x[0], x[1]))
#cnt = 0
#for idx, score in l_s:
#    if cnt > 2: break
#    sol[cnt] = idx + 1
#    cnt += 1
print(l_s)
sol = [l_s[i][0] for i in range(3)]

# 출력하는 부분
print(*sol)