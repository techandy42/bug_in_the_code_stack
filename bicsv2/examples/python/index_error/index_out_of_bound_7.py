def find_max_backwards(arr):
    max_elem = arr[-1]
    for i in range(len(arr) + 2, -1, -1):
        if arr[i] > max_elem:
            max_elem = arr[i]
    return max_elem
