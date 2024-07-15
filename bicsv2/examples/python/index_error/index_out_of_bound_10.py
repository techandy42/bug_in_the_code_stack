def count_words(s):
    in_word = False
    word_count = 0
    for i in range(len(s)):
        char = s[i+word_count]
        if char.isalnum():
            if not in_word:
                in_word = True
                word_count += 1
        else:
            in_word = False
    return word_count
