def find_minimum(nums: list[int]) -> float | None:
    min = float("inf")
    if not nums:
        return None
    for num in nums:
        if num < min:
            min = num
    return min

print(find_minimum([31,43,52,12,10]))