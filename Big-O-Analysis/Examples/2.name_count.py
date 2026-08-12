def count_names(list_of_lists: list[list[str]], target_name: str) -> int:
    count = 0
    for lst in list_of_lists:
        for name in lst:
            if name == target_name:
                count += 1
    return count

print(count_names([["George", "Eva", "George"], ["Diane", "George", "Eva", "Frank"]], "George"))
# To, Future Me.
# If you're revisiting pls recall on why its O(mn) and not O(n^2).