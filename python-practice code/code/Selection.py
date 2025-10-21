def sort(nums):
    for i in range(5):
        minpos = 1
        for j in range(i, 6):
            if nums[j] < nums[minpos]:
               minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)
nums = [5, 3, 8, 7, 2, 6]
sort(nums)
print(nums)