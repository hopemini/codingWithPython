from dis import dis
from math import dist
from turtle import distance


INF = 987654321

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
X, K = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][K] + graph[K][X]

if distance >= INF:
    print('-1')
else:
    print(distance)