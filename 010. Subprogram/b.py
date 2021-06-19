def swap(a, b):
    return b, a


n = int(input())
baris = {}
baris["A"] = input().split()
baris["B"] = input().split()
t = int(input())
for i in range(t):
    x = input().split()
    baris[x[0]][int(x[1]) - 1], baris[x[2]][int(x[3]) - 1] = swap(
        baris[x[0]][int(x[1]) - 1], baris[x[2]][int(x[3]) - 1]
    )
for i in baris["A"]:
    print(i, end=" ")
print()
for i in baris["B"]:
    print(i, end=" ")
