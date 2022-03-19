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


print(123, reverse(123))
print(-123, reverse(-123))
print(120, reverse(120))
print(1534236469, reverse(1534236469))
