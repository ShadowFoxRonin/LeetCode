from typing import List


def two_sum_two_for(arr: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == target:
                result.append(i)
                result.append(j)
                return result
    return result


print(two_sum_two_for([2, 7, 11, 15], 9))  # [0,1]


def two_sum(arr: List[int], target: int) -> List[int]:
    collection_of_numbers = {}
    for i in range(len(arr)):
        search_value = target - arr[i]
        if search_value in collection_of_numbers:
            return [collection_of_numbers[search_value], i]
        elif not arr[i] in collection_of_numbers:
            collection_of_numbers[arr[i]] = i

    return []


print(two_sum([2, 7, 11, 15], 9))  # [0,1]
