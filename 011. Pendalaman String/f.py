upperCaseBiggestOrdVal = ord("Z")
gap = abs(ord("Z") - ord("z"))
s = input()
upperCasingNextChar = False
for c in s:
    ordVal = ord(c)
    if c == "_":
        upperCasingNextChar = True
    elif ordVal <= upperCaseBiggestOrdVal:
        print(f"_{chr(ord(c)+gap)}", end="")
    elif upperCasingNextChar:
        print(chr(ord(c) - gap), end="")
        upperCasingNextChar = False
    else:
        print(c, end="")
