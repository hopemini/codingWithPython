def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    index = len(digits) - 1
    carry = 1 if digits[index] == 9 else 0
    digits[index] = (digits[index] + 1) % 10
    while carry > 0 and index > 0:
        index -= 1
        digits[index] += carry
        carry = digits[index] // 10
        digits[index] = digits[index] % 10
    
    if carry > 0 and index == 0:
        digits.insert(0, carry)
    return digits

digits = list(map(int, input().split()))
print(plusOne(digits))