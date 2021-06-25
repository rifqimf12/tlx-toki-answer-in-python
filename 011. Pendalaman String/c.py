lastCharOrdinal = ord("z")
s = input()
k = int(input())
for c in s:
    ordVal = ord(c) + k
    if ordVal > lastCharOrdinal:
        ordVal -= 26
    print(chr(ordVal), end="")
