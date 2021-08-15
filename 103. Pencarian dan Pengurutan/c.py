# dunno why these got an RTE, will review it later
n, tc = [int(q) for q in input().split()]
name = []
phone = []
for i in range(n):
    s = input().split()
    name.append(s[0])
    phone.append(s[1])


def f(x, firstIndex, lastIndex):
    midIndex = (firstIndex + lastIndex) // 2
    if midIndex < 0 or midIndex > n - 1:
        return "NIHIL"
    elif name[midIndex] == x:
        return phone[midIndex]
    elif firstIndex == lastIndex:
        return "NIHIL"
    elif x < name[midIndex]:
        return f(x, firstIndex, midIndex - 1)
    elif x > name[midIndex]:
        return f(x, midIndex + 1, lastIndex)


for _ in range(tc):
    print(f(input(), 0, n - 1))
