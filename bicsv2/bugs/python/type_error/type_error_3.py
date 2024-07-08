def list_to_grouped_dict(lst):
    grouped_dict = set()
    for key, value in lst:
        if key in grouped_dict:
            grouped_dict[key].append(value)
        else:
            grouped_dict[key] = [value]
    return grouped_dict
