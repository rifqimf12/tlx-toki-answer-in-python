def reverse(x):
    temp = x
    ret = 0

    while temp > 0:
        ret = (ret * 10) + (temp % 10)
        temp = int(temp / 10)

    return ret


a, b = [int(i) for i in input().split()]
print(reverse(reverse(a) + reverse(b)))
