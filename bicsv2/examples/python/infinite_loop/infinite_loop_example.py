def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    i = 0
    while i < len(count):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
