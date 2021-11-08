
def isPalindrome(x: int) -> bool:
    return list(str(x)) == list(str(x))[::-1]


if __name__ == '__main__':
    print(isPalindrome(123432))