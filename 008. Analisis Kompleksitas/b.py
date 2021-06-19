n = int(input())
for i in range(0, n):
    x = int(input())
    if x == 2:
        print("YA")
        continue
    if x == 1 or x % 2 == 0:
        print("BUKAN")
        continue
    prime = True
    ii = 3
    while ii * ii <= x:
        if x % ii == 0:
            print("BUKAN")
            prime = False
            break
        ii += 1
    if prime:
        print("YA")
