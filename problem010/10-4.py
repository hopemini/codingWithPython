columnTitle = input()
ret = 0
for i in range(len(columnTitle)):
    ret = ret * 26 + (ord(columnTitle[i]) - ord('A') + 1)
print(ret)
