nums = [4, 1, 2, 1, 2]

ret = nums[0]
for i in range(1, len(nums)):
    ret ^= nums[i]
print(ret)
