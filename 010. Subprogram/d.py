def faktorisasiPrima(x, pembagi):
    count = 0
    while x % pembagi == 0:
        x /= pembagi
        count += 1
    return x, count


x = int(input())
for i in range(2, x + 1):
    x, c = faktorisasiPrima(x, i)
    if c == 0:
        pass
    else:
        if c == 1:
            print(i, end="")
        else:
            print(f"{i}^{c}", end="")
        if x == 1:
            print()
        else:
            print(" x ", end="")
