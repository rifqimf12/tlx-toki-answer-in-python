def nearestKelipatanDua(x):
    i = 2
    while i < x:
        i *= 2
    return i


oneHomogenLocations = []
r, c = [int(q) for q in input().split()]
xl = nearestKelipatanDua(max([r, c]))
x = [[False for _ in range(xl)] for _ in range(xl)]
for i in range(r):
    ii = 0
    for val in input().split():
        x[i][ii] = bool(int(val))
        ii += 1


def isHomogen(ri, ci, re, ce):
    benchmark = x[ri][ci]
    for i in range(ri, re):
        for ii in range(ci, ce):
            if x[i][ii] != benchmark:
                return False
    return True


def f(location, ri, ci, length):
    global oneHomogenLocations
    if isHomogen(ri, ci, ri + length, ci + length):
        if x[ri][ci]:
            oneHomogenLocations.append(location)
    else:
        f(location + "0", ri, ci, int(length / 2))
        f(location + "1", ri, ci + int(length / 2), int(length / 2))
        f(location + "2", ri + int(length / 2), ci, int(length / 2))
        f(location + "3", ri + int(length / 2), ci + int(length / 2), int(length / 2))


f("1", 0, 0, xl)
print(len(oneHomogenLocations))
for location in oneHomogenLocations:
    print(location)
