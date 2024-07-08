def sum_digits_in_string(s):
    total = 0
    for char in s:
        total += int(char)
    return total
