def int_to_binary_and_count_ones(n):
    binary_str = bin(n)[2:]
    count_ones = 0
    for char in binary_str:
        if char == '0' + 1:
            count_ones += 1
    return binary_str, count_ones
