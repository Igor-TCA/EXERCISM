import math

def score(x, y):
    if 0 <= math.sqrt(x**2 + y**2) <= 1:
        return 10
    if 1 < math.sqrt(x**2 + y**2) <= 5:
        return 5
    if 5 < math.sqrt(x**2 + y**2) <= 10:
        return 1
    return 0