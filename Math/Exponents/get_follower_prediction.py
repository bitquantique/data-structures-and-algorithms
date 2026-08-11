# total = a1 × r^n
def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:
    match influencer_type:
        case "fitness":
            mul_const=4
        case "cosmetic":
            mul_const=3
        case _:
            mul_const=2
    return follower_count*(mul_const**num_months)

print(get_follower_prediction(10, "fitness", 1))