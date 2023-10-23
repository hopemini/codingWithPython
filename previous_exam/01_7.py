## 소수 찾기
## https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    if n < 2: return 0
    s = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
            #for j in range(i*2, n+1, i):
            #    s[j] = 0
    #answer = len([i for i, v in enumerate(s) if v])
    answer = s.count(1)
    return answer

def solution2(n):
    if n < 2: return 0
    num=set(range(2,n+1))

    for i in range(2, int(n**.5) + 1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)

N = int(input())
print(solution(N))