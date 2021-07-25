def fpb(a, b):
    if b == 0:
        return a
    else:
        return fpb(b, a % b)


kpk = 0
n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
    if i >= 1:
        kpk = kpk * d[i] // fpb(kpk, d[i])
    else:
        kpk = d[i]
print(kpk)
