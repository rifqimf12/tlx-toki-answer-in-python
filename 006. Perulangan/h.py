n, x = [int(i) for i in input().split()]
for i in range(1, n + 1):
    if i % x == 0:
        print("*", end="")
    else:
        print(i, end="")
    if i < n:
        print(" ", end="")
