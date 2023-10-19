## 약수의 합
## https://school.programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = 0
    #answer = sum([i for i in range(1, n+1) if n % i == 0])
    answer = n + sum([i for i in range(1, (n // 2) + 1) if n % i ==0])
    return answer

n = int(input())
print(solution(n))