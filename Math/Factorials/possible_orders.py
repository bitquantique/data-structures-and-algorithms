def num_possible_orders(num_posts: int) -> int:
    if num_posts == 0:
        return 1
    fact = num_posts * num_possible_orders(num_posts-1)
    return fact

print(num_possible_orders(10))