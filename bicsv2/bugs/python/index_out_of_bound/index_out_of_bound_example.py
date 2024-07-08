def count_characters(s):
    char_count = {}
    for i in range(len(s)+1):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
