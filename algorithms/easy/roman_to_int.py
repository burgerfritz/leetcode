def romanToIntNoob(s: str) -> int:
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


def romanToInt1(s: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    s = s.replace("IV", "I" * 4).replace("IX", "I" * 9)
    s = s.replace("XL", "X" * 4).replace("XC", "X" * 9)
    s = s.replace("CD", "C" * 4).replace("CM", "C" * 9)

    res = 0
    for char in s:
        res += roman_dict[char]

    return res


def romanToInt(s: str) -> int:
    sum = 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(0, len(s) - 1):
        if roman_dict[s[i]] >= roman_dict[s[i + 1]]:
            sum += roman_dict[s[i]]
        else:
            sum -= roman_dict[s[i]]
    sum += roman_dict[s[len(s) - 1]]
    return sum


if __name__ == '__main__':
    print(romanToInt("MDCCCLXXXIV"))
