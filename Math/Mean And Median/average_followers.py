def average_followers(nums: list[int]) -> float | None:
    if not nums:
        return None
    sum = 0
    for num in nums:
        sum += num
    return sum/len(nums)

print(average_followers([1,2,411,121,141]))