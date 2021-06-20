def f(a, b, x):
    return abs(a * x + b)


a, b, k, x = [int(i) for i in input().split()]
for _ in range(k):
    x = f(a, b, x)
print(x)
