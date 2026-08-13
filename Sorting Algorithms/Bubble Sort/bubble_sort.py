def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i-1] >= nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                swapping = True
        end -= 1
    return nums

print(bubble_sort([5, 7, 3, 6, 8]))