n, k = [int(q) for q in input().split()]
toBePrint = [0 for _ in range(n)]
isOnToBePrint = [False for _ in range(n)]


def printKombinasi(depth):
    global toBePrint
    if depth == k:
        for i in range(k):
            print(toBePrint[i], end=" ")
        print()
    else:
        for i in range(toBePrint[depth - 1], n):
            if not isOnToBePrint[i]:
                isOnToBePrint[i] = True
                toBePrint[depth] = i + 1
                printKombinasi(depth + 1)
                isOnToBePrint[i] = False


printKombinasi(0)
