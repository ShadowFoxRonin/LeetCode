from typing import List


def double_for(nums: List[int]) -> List[int]:
    r_nums: List[int] = []
    for ignore in range(2):
        for value in nums:
            r_nums.append(value)
    return r_nums


def make_a_copy(nums: List[int]) -> List[int]:
    r_nums: List[int] = nums.copy()
    for value in nums:
        r_nums.append(value)
    return r_nums


def concatenation_of_array(nums: List[int]) -> List[int]:
    new_size = len(nums) * 2
    r_nums: List[int] = [0] * new_size
    for i in range(len(nums)):
        r_nums[i] = nums[i]
        r_nums[i + len(nums)] = nums[i]
    return r_nums


def python_feature(nums: List[int]) -> List[int]:
    nums.extend(nums)
    return nums


print(make_a_copy([1, 2, 3]))
print(double_for([1, 2, 3]))
print(concatenation_of_array([1, 2, 3]))
print(python_feature([1, 2, 3]))
