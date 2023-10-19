## 짝수와 홀수
## https://school.programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    answer = 'Even' if num % 2 == 0 else 'Odd'
    return answer

num = int(input())
print(solution(num))