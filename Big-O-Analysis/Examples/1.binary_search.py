# Example of O(log(n))
def binary_search(target: int, arr: list[int]) -> bool:
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if target == arr[mid]:
            return True
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return False

print(binary_search(4, [1,2,3,4,5,6,7,8,9]))