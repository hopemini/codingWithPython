## 자릿수 더하기
## https://school.programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0

    while n > 0:
        answer += n % 10
        n = n // 10
    return answer

n = int(input())
print(solution(n))