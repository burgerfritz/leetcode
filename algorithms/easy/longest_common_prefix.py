from collections import defaultdict
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
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


def longestCommonPrefix(strs: List[str]) -> str:
    strs = sorted(strs)
    current = strs[0]
    for x in range(1, len(strs)):
        while strs[x].startswith(current) is not True:
            current = current[:-1]
            if len(current) == 0:
                break
    return current


if __name__ == '__main__':
    print(longestCommonPrefix(["ab", "a"]))
    print(longestCommonPrefix(["flower", "flour", "flight"]))
