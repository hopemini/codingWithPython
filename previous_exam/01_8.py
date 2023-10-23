## 제일 작은 수 제거하기
## https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0: return [-1]
    else: return arr

arr = list(map(int, input().split()))
print(solution(arr))