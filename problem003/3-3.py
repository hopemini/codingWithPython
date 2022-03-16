def removeElement( nums, val):
    #j = 0
    #for i in range(len(nums)):
    #    if nums[i] != val:
    #        nums[j] = nums[i]
    #        j += 1
    #return j
    nums[:] = [num for num in nums if num != val]
    return len(nums)

nums = list(map(int, input().split()))
val = int(input())

print(removeElement(nums, val))
