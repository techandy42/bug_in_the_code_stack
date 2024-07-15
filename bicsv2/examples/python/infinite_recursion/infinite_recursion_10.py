def majority_element(nums, candidate=None, count=0, index=0):
    if index == len(nums):
        return candidate
    if count == 0:
        return majority_element(nums, nums[index], 1, index)
    if nums[index] == candidate:
        return majority_element(nums, candidate, count + 1, index)
    return majority_element(nums, candidate, count - 1, index)
