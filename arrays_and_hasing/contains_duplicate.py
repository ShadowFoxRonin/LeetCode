from typing import List


def contains_duplicate_dict(nums: List[int]) -> bool:
    if len(nums) == 1: return False
    nums_dict = {}
    for i in range(len(nums)):
        if nums_dict.__contains__(nums[i]):
            return True
        else:
            nums_dict[nums[i]] = 1
    return False


print(contains_duplicate_dict([1, 2, 3, 1]))  # True


def contains_duplicate_set(arr: List[int]) -> bool:
    arr_set = set(arr)
    return len(arr) != len(arr_set)


print(contains_duplicate_set([1, 2, 3, 1]))  # True
