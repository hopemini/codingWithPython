def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num =  int(''.join(map(str, digits)))
    num += 1
    return [int(x) for x in str(num)]

digits = list(map(int, input().split()))
print(plusOne(digits))