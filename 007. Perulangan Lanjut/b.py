n = int(input())
for i in range(0, n):
    for ii in range(0, n):
        if ii + i >= n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
