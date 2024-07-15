def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    rotated_arr = arr[:-k] + arr[-k:]
    return rotated_arr
