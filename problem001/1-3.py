nums = [2, 7, 11, 15]
target = 9

N = {}
for i, n in enumerate(nums):
    t = target - n
    if t in N:
        print([N[t], i])
    else:
        N[n] = i
