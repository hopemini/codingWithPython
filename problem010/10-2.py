num1, num2 = input().split()
count, i, j = 0, len(num1)-1, len(num2)-1

#ret = ''
ret = []
while i>=0 or j>=0 or count>0:
    if i>=0:
        count += ord(num1[i]) - ord('0')
        i -= 1
    if j>=0:
        count += ord(num2[j]) - ord('0')
        j -= 1
    #ret = str(count % 10) + ret
    ret.append(str(count%10))
    count //= 10

#print(ret)
print(''.join(ret[::-1]))
