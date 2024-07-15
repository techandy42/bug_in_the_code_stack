def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n / 2
    if n % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]
    return median
