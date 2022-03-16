num = 1994

d = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
result = ''
for k in sorted(d)[::-1]:
    #print(k, v)
    r = num // k
    if r > 0:
        result += r * d[k]
        num -=  r * k

print(result)

