n = int(input())
for i in range(0, n):
    x = int(input())
    if x <= 6:
        print("YA")
        continue
    ii = 2
    divider = 0
    while ii * ii <= x:
        if x % ii == 0:
            divider += 1
            if divider == 2:
                break
        ii += 1
    if divider > 1:
        print("BUKAN")
    else:
        print("YA")
