def majority_element(nums):
    candidate, count = None, 0
    i = 0
    while i < len(nums):
        if count == 0:
            candidate, count = nums[i], 1
        elif nums[i] == candidate:
            count += 1
        else:
            count -= 1
    i -= 1
    return candidate
