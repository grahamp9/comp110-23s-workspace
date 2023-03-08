"""Example function for Unit Tests"""

def sum(xs: list[float]) -> float: 
    """return sum of all elements in xs"""
    sum_total: float = 0.0 
    for item in range(0, len(xs)):
        sum_total += xs[item]
    return sum_total 


print(sum([1.0, 2.0, 3.0]))