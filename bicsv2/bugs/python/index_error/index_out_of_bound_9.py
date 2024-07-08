def is_palindrome_backwards(s):
    left, right = 0, len(s) - 1
    while True:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
