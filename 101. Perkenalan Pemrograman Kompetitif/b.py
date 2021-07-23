r, c = [int(q) for q in input().split()]
x = [_ for _ in range(r)]
for i in range(r):
    x[i] = list(input())


def printResult():
    q = 0
    for i in x:
        print("".join(i))
        q += 1


# top most floor row index is 0
def couldExplodeHappen(atFloor):
    for i in range(c):
        if x[atFloor][i] == "0":
            return False
    return True


def explode():
    rx = -1  # floor at which explode occurred. -1 means there aren't
    for i in range(r - 1, -1, -1):
        if couldExplodeHappen(i):
            if rx == -1:
                rx = i
            x[i] = ["0" for _ in range(c)]
    return rx


def doBlockFalling(rx, cc):
    for i in range(rx, -1, -1):
        if x[i][cc] == "1":
            x[i][cc] = "0"
            for ii in range(i, r):
                if ii == i:
                    continue
                if ii + 1 == r or x[ii + 1][cc] == "1":
                    x[ii][cc] = "1"
                    break


def blockFallingAbove(rx):
    for i in range(c):
        doBlockFalling(rx, i)


def f():
    rx = explode()
    if rx == -1:
        return
    blockFallingAbove(rx)
    f()


f()
printResult()
