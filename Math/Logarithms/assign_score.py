import math

def get_influencer_score(
    num_followers: int, average_engagement_percentage: float
) -> float:
    return average_engagement_percentage*(math.log(num_followers,2))

print(get_influencer_score(750000, 0.7))