# 물류창고
# https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8819/%EB%AC%BC%EB%A5%98%EC%B0%BD%EA%B3%A0

import sys

def input_data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	infos = [list(map(int, readl().split())) for _ in range(M)]
	return N, M, infos

sol = -1

# 입력받는 부분
N, M, infos = input_data()

# 여기서부터 작성
INF = 987654321

# make map
dist_map = [[INF] * (N+1) for _ in range(N+1)]
for i in infos:
    dist_map[i[0]][i[1]] = i[2]
    dist_map[i[1]][i[0]] = i[2]

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j: continue
            dist_map[i][j] = min(dist_map[i][j], dist_map[i][k]+ dist_map[k][j])

#print(dist_map)
ans = []
for i in range(1, N+1):
    sol = -1
    for j in range(1, N+1):
        if dist_map[i][j] != INF:
            sol = max(sol, dist_map[i][j])
    ans.append(sol)
# 출력하는 부분
print(min(ans))
