x = [0 for _ in range(1000)]
y = [0 for _ in range(1000)]
n, d = [int(i) for i in input().split()]


def t(x1, x2, y1, y2):
    return abs(x1 - x2) ** d + abs(y1 - y2) ** d


min = 2 * (100 ** 3)
max = 0
for i in range(n):
    x[i], y[i] = [int(i) for i in input().split()]
    for ii in range(i):
        r = t(x[i], x[ii], y[i], y[ii])
        if r > max:
            max = r
        if r < min:
            min = r
print(min, max)
