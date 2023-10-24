## Loop 실행기
## https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8812/loop-%EC%8B%A4%ED%96%89%EA%B8%B0

import sys

def input_data():
    readl = sys.stdin.readline
    loop = readl().strip()
    return loop

loop = input_data()

def analyze(str_loop, s):
    cnt = int(str_loop[s+1])
    while cnt > 0:
        cnt -= 1
        w = s + 2
        while str_loop[w] != '>':
            if str_loop[w] == '<':
                w = analyze(str_loop, w)
            else:
                print(str_loop[w], end='')
            w += 1
    return w

analyze(loop, 0)