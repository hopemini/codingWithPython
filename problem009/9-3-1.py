nums = [4, 1, 2, 1, 2]

count = 0
d = {}
for i in nums:
    if i in d:
        d[i] += 1
        count -= i
    else:
        d[i] = 1
        count += i
print(count)
