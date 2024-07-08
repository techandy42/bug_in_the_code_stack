def reverse_words(s):
    words = s.split()
    reversed_words = ''
    for i in range(0, len(words)):
        reversed_words += words[i] + ' '
    reversed_words = reversed_words[:-1]
    return reversed_words
