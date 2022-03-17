def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if nums[-1] < target:
        return len(nums)
    elif nums[0] > target:
        return 0
    l, r = 0, len(nums) - 1
    while l <= r:
        middle = (l + r) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            l = middle + 1
        else:
            r = middle - 1
    return l

nums = list(map(int, input().split()))
target = int(input()) 

print(searchInsert(nums, target))
