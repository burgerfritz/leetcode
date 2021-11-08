def isValid(s: str) -> bool:
    if len(s) % 2 != 0 or not s:
        return False

    d = {"(": ")", "{": "}", "[": "]"}
    return isValidSub2(s, d)


def isValidSub1(s, d):
    for i in range(int(len(s) / 2)):
        index = list(d.values()).index(s[::-1][i])
        opposite = list(d.keys())[index]
        if s[i] != opposite:
            return False
    return True


def isValidSub2(s, d):
    while s:
        if d[s[0]] == s[1]:
            s = s[2:]
            continue
        return False
    return True


if __name__ == '__main__':
    print(isValid("()[}"))
