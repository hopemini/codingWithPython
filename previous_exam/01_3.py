## 평균 구하기
## https://school.programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    answer = sum(arr) / len(arr)
    return answer

arr = list(map(int, input().split()))
print(arr)
print(solution(arr))