from collections import defaultdict
from typing import List, Optional


class Solution:
    def twoSumNoob(self, nums: List[int], target: int) -> Optional[List[int]]:
        pivot = 0
        while pivot < len(nums) - 1:
            k = pivot + 1
            while k < len(nums):
                if nums[pivot] + nums[k] == target:
                    return [pivot, k]
                k += 1
            pivot += 1
        return

    def twoSum1(self, nums: List[int], target: int) -> Optional[List[int]]:
        hashmap = {}  # index: value
        for i, n in enumerate(nums):
            if target - n in hashmap.values():
                return [i, list(hashmap.values()).index(target - n)]
            hashmap[i] = n
        return

    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        prevmap = {}  # value: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [i, prevmap[diff]]
            prevmap[n] = i
        return

    def isPalindrome(self, x: int) -> bool:
        return list(str(x)) == list(str(x))[::-1]

    def romanToIntNoob(self, s: str) -> int:
        romanmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1_000}
        subtractions = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        spec = []
        sum = 0
        for c in s:
            if spec:
                spec.extend([c])
                specialsub = "".join(spec)
                if specialsub in subtractions:
                    sum += subtractions[specialsub] - romanmap[spec[0]]
                    spec = []
                    continue
                spec = []
            if c in ("I", "X", "C"):
                spec.append(c)
            sum += romanmap[c]
        return sum

    def romanToInt1(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        s = s.replace("IV", "I" * 4).replace("IX", "I" * 9)
        s = s.replace("XL", "X" * 4).replace("XC", "X" * 9)
        s = s.replace("CD", "C" * 4).replace("CM", "C" * 9)

        res = 0
        for char in s:
            res += roman_dict[char]

        return res

    def romanToInt(self, s: str) -> int:
        sum = 0
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(0, len(s) - 1):
            if roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                sum += roman_dict[s[i]]
            else:
                sum -= roman_dict[s[i]]
        sum += roman_dict[s[len(s) - 1]]
        return sum

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs.count(strs[0]) == len(strs):
            return strs[0]

        i = 0
        output = []
        while True:
            common = defaultdict(int)
            for s in strs:
                if not s:
                    return ""
                try:
                    s[i]
                except IndexError:
                    return "".join(output)

                common[s[i]] += 1

            for k, v in common.items():
                if v == len(strs):
                    output.append(k)
                else:
                    return "".join(output)

            i += 1

    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        current = strs[0]
        for x in range(1, len(strs)):
            while strs[x].startswith(current) is not True:
                current = current[:-1]
                if len(current) == 0:
                    break
        return current
