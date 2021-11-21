def isValid1(s: str) -> bool:
    if len(s) % 2 != 0 or not s:
        return False

    d = {"(": ")", "{": "}", "[": "]"}
    if all(c in d.keys() for c in s):
        return False

    list_ = []
    for c in s:
        if c in d.keys():
            list_.append(c)
        else:
            if not list_:
                return False
            index = list(d.values()).index(c)
            opposite = list(d.keys())[index]
            if list_.pop() != opposite:
                return False

    if not list_:
        return True
    return False


def isValid(s: str) -> bool:
    stack = []
    close_to_open = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in close_to_open:
            if stack and stack.pop() == close_to_open[c]:
                continue
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


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


def rec(dd, s):
    for k, v in dd.items():
        if isinstance(v, dict):
            rec(v, s)
        else:
            s.add((k, v))
    return s


if __name__ == "__main__":
    # print(isValid("()[}"))
    print(isValid("(("))
    print(isValid("[[[]"))
    # print(isValid("{{}[][[[]]]}"))
    # print(rec({1: 2, 3: {4: 5}}, set()))
