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