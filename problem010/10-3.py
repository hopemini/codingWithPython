columnNumber = int(input())
#ret = []
ret = ''
while columnNumber > 0:
    #ret.append(chr((columnNumber - 1) % 26 + ord('A')))
    ret = chr((columnNumber - 1) % 26 + ord('A')) + ret
    columnNumber = (columnNumber - 1) // 26
print(ret)
#print(''.join(ret[::-1]))
