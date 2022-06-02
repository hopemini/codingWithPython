import sys

def Input_Data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N+1)]
    return N, W, H, info


N, W, H, info = Input_Data()
array = []
""" for i in range(N+1):
    position, value = info[i]
    if position == 1:
        array.append(H+value)
    elif position == 2:
        array.append(-value)
    elif position == 3:
        array.append(H-value)
    else:
        array.append(-W-H+value) """

# distance from (0, 0)
for i in range(N+1):
    position, value = info[i]
    if position == 1:
        array.append(value)
    elif position == 4:
        array.append(W + value)
    elif position == 2:
        array.append(W + H + W - value)
    else:
        array.append(W + H + W + H - value)
#print(array)
total = 2 * W + 2 * H
cnt = 0
for i in range(N):
    inner = abs(array[N] - array[i])
    outer = total - inner
    cnt += min(inner, outer)
print(cnt)
