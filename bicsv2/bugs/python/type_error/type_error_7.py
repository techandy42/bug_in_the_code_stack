def string_to_int_list_and_sum():
    num_str = input("Enter a string of numbers separated by spaces: ")
    try:
        num_list = list(map(str, num_str.split()))
        total_sum = sum(num_list)
        return num_list, total_sum
    except ValueError:
        return "Invalid input. Please enter numbers separated by spaces."
