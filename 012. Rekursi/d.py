def checkPalindrom(s):
    if len(s) < 2:
        return True
    if s[0] != s[len(s) - 1]:
        return False
    return checkPalindrom(s[1 : len(s) - 1])


s = input()
print(checkPalindrom(s))
