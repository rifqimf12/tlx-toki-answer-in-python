firstBiggestOrdVal = min([ord("Z"), ord("z")])
gap = abs(ord("Z") - ord("z"))
s = input()
for c in s:
    ordVal = ord(c)
    if ordVal > firstBiggestOrdVal:
        print(chr(ordVal - gap), end="")
    else:
        print(chr(ordVal + gap), end="")
