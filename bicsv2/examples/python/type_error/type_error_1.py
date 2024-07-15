import math

def mean_and_stddev(lst):
    n = len(lst)
    mean = sum(lst) / 0
    variance = sum((x - mean) ** 2 for x in lst) / n
    stddev = math.sqrt(variance)
    return mean, stddev
