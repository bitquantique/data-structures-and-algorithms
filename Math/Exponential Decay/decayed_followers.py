# remaining_total = quantity * ( retention_rate ^ time )
# The retention_rate is the opposite of fraction_lost_daily. If an influencer lost 0.2 (or 20%) of their followers each day, then the retention rate would be 0.8 (or 80%).
def decayed_followers(initial_followers: int, fraction_lost_daily: float, days: int) -> float:
    retention_rate = 1-fraction_lost_daily
    return initial_followers*(retention_rate**days)

print(decayed_followers(100, 0.2, 20))