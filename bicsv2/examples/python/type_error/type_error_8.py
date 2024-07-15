def number_to_bases():
    num = input("Enter an integer: ")
    try:
        num = float(num)
        binary = bin(num)[2:]
        octal = oct(num)[2:]
        hexadecimal = hex(num)[2:]
        return binary, octal, hexadecimal
    except ValueError:
        return "Invalid input. Please enter an integer."
    