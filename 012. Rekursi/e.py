# seems weird and not an efficient answer. will looking for other's answer and commit it later
def f(x, i):
    if x >= 2 ** (i + 1):
        x, tempBinaryValue = f(x, i + 1)
    else:
        tempBinaryValue = ""
    if x >= 2 ** i:
        x -= 2 ** i
        tempBinaryValue = tempBinaryValue + "1"
    else:
        tempBinaryValue = tempBinaryValue + "0"
    return x, tempBinaryValue


x = int(input())
_, binaryValue = f(x, 0)
print(binaryValue)
