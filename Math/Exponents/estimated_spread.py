# estimated_spread = average_audience_followers * ( num_followers ** 1.2 )
def get_estimated_spread(audiences_followers: list[int]) -> float:
    if not audiences_followers:
        return 0
    avg = 0.0
    for follower in audiences_followers:
        avg += follower
    avg = avg/len(audiences_followers)
    return avg*(len(audiences_followers)**1.2)

print(get_estimated_spread([7, 4, 3, 100, 765, 2344, 1, 2, 32]))