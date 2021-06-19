n = int(input())
c = 0
for i in range(0, n):
    for ii in range(0, i + 1):
        if c == 10:
            c = 0
        print(c, end="")
        c += 1
    print()
