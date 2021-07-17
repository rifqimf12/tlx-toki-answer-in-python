def nearestKelipatanDua(x):
    i = 2
    while i < x:
        i *= 2
    return i


n = int(input())
oneHomogenLocations = []
for _ in range(n):
    oneHomogenLocations.append(input())
r, c = [int(q) for q in input().split()]

xl = nearestKelipatanDua(max([r, c]))  # panjang persegi
x = [[0 for _ in range(xl)] for _ in range(xl)]


def f(location, depth, ri, ci, length):
    halfLength = int(length / 2)
    if depth != len(location):
        if location[depth] == "0":
            f(location, depth + 1, ri, ci, halfLength)
        elif location[depth] == "1":
            f(location, depth + 1, ri, ci + halfLength, halfLength)
        elif location[depth] == "2":
            f(location, depth + 1, ri + halfLength, ci, halfLength)
        elif location[depth] == "3":
            f(location, depth + 1, ri + halfLength, ci + halfLength, halfLength)
    else:
        for i in range(ri, ri + length):
            for ii in range(ci, ci + length):
                x[i][ii] = 1


def printDecodeResult():
    for i in range(r):
        for ii in range(c):
            if ii != c - 1:
                print(x[i][ii], end=" ")
            else:
                print(x[i][ii])


for i in range(n):
    f(oneHomogenLocations[i][1:], 0, 0, 0, xl)
printDecodeResult()
