def summed(nums: list[int]) -> int:
    if not nums:
        return 0
    sum = 0
    for num in nums:
        sum += num
    return sum

print(summed([31,43,52,12,10]))