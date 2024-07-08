def float_to_string_and_extract_decimal_part(f):
    float_str = str(f)
    integer_part, decimal_part = float_str.split('.')
    print("Integer Part:", int(integer_part))
    print("Decimal Part:", '.' + int(decimal_part))
    return decimal_part
