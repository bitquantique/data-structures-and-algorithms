import math

def log_scale(data: list[float], base: float) -> list[float]:
    return list(map(lambda x: math.log(x, base), data))

print(log_scale([10,100,1000], 10))