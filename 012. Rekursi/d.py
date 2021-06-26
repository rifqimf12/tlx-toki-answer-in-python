def checkPalindrom(s):
    if len(s) < 2:
        return "YA"
    if s[0] != s[len(s) - 1]:
        return "BUKAN"
    return checkPalindrom(s[1 : len(s) - 1])


s = input()
print(checkPalindrom(s))
