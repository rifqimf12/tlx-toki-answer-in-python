n = int(input())
toBePrint = [0 for _ in range(n)]
isOnToBePrint = [False for _ in range(n)]


def isZigZag(depth):
    if depth < 2:
        return True
    if toBePrint[depth] < toBePrint[depth - 1]:
        if toBePrint[depth - 1] > toBePrint[depth - 2]:
            return True
    else:
        if toBePrint[depth - 1] < toBePrint[depth - 2]:
            return True
    return False


def printPermutasiZigZag(depth):
    global toBePrint
    if depth == n:
        for i in range(n):
            print(toBePrint[i], end="")
        print()
    else:
        for i in range(n):
            if not isOnToBePrint[i]:
                isOnToBePrint[i] = True
                toBePrint[depth] = i + 1
                if isZigZag(depth):
                    printPermutasiZigZag(depth + 1)
                isOnToBePrint[i] = False


printPermutasiZigZag(0)
