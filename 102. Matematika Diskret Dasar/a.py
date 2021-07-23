def fpb(a, b):
    if b == 0:
        return a
    else:
        return fpb(b, a % b)


a, b = [int(q) for q in input().split()]
c, d = [int(q) for q in input().split()]

kpk = (b * d) // fpb(b, d)
e = a * (kpk // b) + c * (kpk // d)
f = kpk
x = fpb(e, f)
e = e // x
f = f // x
print(e, f)
