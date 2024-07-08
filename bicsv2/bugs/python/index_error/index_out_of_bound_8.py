def reverse_array_in_place(arr):
    left, right = 0, len(arr) - 1
    while True:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
