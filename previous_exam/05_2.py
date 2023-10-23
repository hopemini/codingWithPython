## 크게 만들기
## https://www.acmicpc.net/problem/2812

n, k = map(int, input().split())
number = list(input())

answer = []
cnt = k
for num in number:
    while answer and cnt > 0 and answer[-1] < num:
        del answer[-1]
        cnt -= 1
    answer.append(num)

print(''.join(answer[:n-k]))