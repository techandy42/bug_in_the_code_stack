def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    i = 0
    while i < len(s):
        if s[i] in vowels:
            count += 1
    return count
