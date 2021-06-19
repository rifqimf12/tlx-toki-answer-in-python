n = int(input())
numbers = [int(i) for i in input().split()]
appearance = [0 for i in range(1001)]

for i in numbers:
    appearance[i] += 1

appearance.reverse()
x = max(appearance)
print(1000 - appearance.index(x))
