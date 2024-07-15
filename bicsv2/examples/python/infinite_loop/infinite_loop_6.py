def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while True:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
