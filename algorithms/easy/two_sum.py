from typing import List, Optional


def twoSumNoob(nums: List[int], target: int) -> Optional[List[int]]:
    pivot = 0
    while pivot < len(nums) - 1:
        k = pivot + 1
        while k < len(nums):
            if nums[pivot] + nums[k] == target:
                return [pivot, k]
            k += 1
        pivot += 1
    return


def twoSum1(nums: List[int], target: int) -> Optional[List[int]]:
    hashmap = {}  # index: value
    for i, n in enumerate(nums):
        if target - n in hashmap.values():
            return [i, list(hashmap.values()).index(target - n)]
        hashmap[i] = n
    return


def twoSum(nums: List[int], target: int) -> Optional[List[int]]:
    prevmap = {}  # value: index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevmap:
            return [i, prevmap[diff]]
        prevmap[n] = i
    return


if __name__ == "__main__":
    print(twoSum([4, 3, 5, 2], 7))
