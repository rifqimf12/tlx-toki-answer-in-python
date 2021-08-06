totalRow, totalColumn, nilaiKemenarikan = [int(q) for q in input().split()]
k = [0 for _ in range(totalRow)]
for i in range(totalRow):
    k[i] = [int(q) for q in input().split()]


def calculate(i, ii):
    x = 1
    if i > 0:
        x *= k[i - 1][ii]
    if i < totalRow - 1:
        x *= k[i + 1][ii]
    if ii > 0:
        x *= k[i][ii - 1]
    if ii < totalColumn - 1:
        x *= k[i][ii + 1]
    return x


def find():
    for ii in range(totalColumn):
        for i in range(totalRow):
            if calculate(i, ii) == nilaiKemenarikan:
                return i + 1, ii + 1
    return 0, 0


x, y = find()
print(x, y)
