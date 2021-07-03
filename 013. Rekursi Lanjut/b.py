def gambarGunung(x):
    if x == 1:
        print("*")
    else:
        gambarGunung(x - 1)
        for _ in range(x):
            print("*", end="")
        print()
        gambarGunung(x - 1)


x = int(input())
gambarGunung(x)
