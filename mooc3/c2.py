import sys
from collections import deque

input = sys.stdin.readline

def cross(i,j):
  x1,y1,x2,y2,x3,y3,x4,y4 = *line[i],*line[j]
  return max(x1,x2)>=min(x3,x4) and max(x3,x4)>=min(x1,x2) and max(y1,y2)>=min(y3,y4) and max(y3,y4)>=min(y1,y2)

M,N = map(int,input().split())
K = int(input())

line = [[*map(int,input().split())][1:] for i in range(K)]
sx,sy,dx,dy = map(int,input().split())
line += [[sx,sy,sx,sy],[dx,dy,dx,dy]]

visited = [0]*(K+2)
q = deque([(-2,0)])
while q:
  now,d = q.popleft()
  if visited[now]:
    continue
  visited[now] = 1
  if now == K+1:
    print(d-1)
    break
  for next in range(K+2):
    if not visited[next]:
      if cross(now,next):
        q.append((next,d+1))