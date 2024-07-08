def is_palindrome(s):
    cleaned_str = ''
    for char in s:
        if char.isalnum():
            cleaned_str += char.lower()
    
    left = 0
    right = len(cleaned_str) - 1
    
    while left < right:
        if cleaned_str[left] == cleaned_str[right]:
            return False
        left += 1
        right -= 1
    
    return True
