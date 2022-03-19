def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 0
    nums.append(-100)
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[j] = nums[i]
            j += 1
    return j

nums = list(map(int, input().split()))

k = removeDuplicates(nums)
for i in range(k):
    print(nums[i], end=' ')