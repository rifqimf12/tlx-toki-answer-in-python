def f(x):
    if x % 2 == 0:
        return int(x / 2) * f(x - 1)
    elif x == 1:
        return 1
    else:
        return x * f(x - 1)


x = int(input())
print(f(x))
