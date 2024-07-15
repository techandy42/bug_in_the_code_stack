def harmonic_mean(lst):
    n = len(lst)
    reciprocal_sum = sum(1 / x for x in lst)
    h_mean = n / (reciprocal_sum - reciprocal_sum)
    return h_mean
