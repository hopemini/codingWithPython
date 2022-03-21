def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    x_min = -2**31
    x_max = 2**31
    ret = 0
    if x < 0:
        ret = -int(str(-x)[::-1])
    else:
        ret = int(str(x)[::-1])
    if ret < x_min or ret > x_max:
        return 0
    return ret


x = [123, -123, 120, 1534236469]
for i in x:
    print(i, reverse(i))
