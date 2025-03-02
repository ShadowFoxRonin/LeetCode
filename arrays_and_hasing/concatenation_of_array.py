from typing import List


def double_for(nums: List[int]) -> List[int]:
    r_nums: List[int] = []
    for it in range(2):
        for i in range(len(nums)):
            r_nums.append(nums[i])
    return r_nums


def make_a_copy(nums: List[int]) -> List[int]:
    r_nums: List[int] = nums.copy()
    for i in range(len(nums)):
        r_nums.append(nums[i])
    return r_nums


def concatenation_of_array(nums: List[int]) -> List[int]:
    new_size = len(nums) * 2
    r_nums: List[int] = [0] * new_size
    for i in range(len(nums)):
        r_nums[i] = nums[i]
        r_nums[i + len(nums)] = nums[i]
    return r_nums


print(make_a_copy([1, 2, 3]))
print(double_for([1, 2, 3]))
print(concatenation_of_array([1, 2, 3]))
