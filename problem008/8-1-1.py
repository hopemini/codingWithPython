def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
        ret = -int(str(-x)[::-1])
        if ret < -2**31:
            return 0
        else:
            return ret
    else:
        ret = int(str(x)[::-1])
        if ret > 2**31 - 1:
            return 0
        else:
            return ret


x = [123, -123, 120, 1534236469]
for i in x:
    print(i, reverse(i))
