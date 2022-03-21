def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    x_min = -2**31
    x_max = 2**31
    ret = 0
    sign = True

    if x < 0:
        sign = False
        x = -x
    while x != 0:
        ret = ret * 10 + x % 10
        x //= 10
    
    if ret < x_min or ret > x_max:
        return 0
    if sign == False:
        return -ret
    return ret

x = [123, -123, 120, 1534236469]
for i in x:
    print(i, reverse(i))
