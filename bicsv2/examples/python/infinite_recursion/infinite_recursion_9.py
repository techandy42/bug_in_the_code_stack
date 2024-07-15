def generate_binary_numbers(n, arr, i):
    if i == n:
        print("".join(arr))
        generate_binary_numbers(n, arr, 0)
    arr[i] = '0'
    generate_binary_numbers(n, arr, i + 1)
    arr[i] = '1'
    generate_binary_numbers(n, arr, i + 1)
