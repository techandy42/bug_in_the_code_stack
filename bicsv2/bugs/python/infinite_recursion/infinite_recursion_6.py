def generate_subsets(arr, subset, index):
    if index == len(arr):
        print(subset)
        generate_subsets(arr, subset, index)
    else:
        generate_subsets(arr, subset, index + 1)
        generate_subsets(arr, subset + [arr[index]], index + 1)
