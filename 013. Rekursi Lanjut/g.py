r, c = [int(q) for q in input().split()]
ball = [[] for _ in range(r)]
ballTaken = [[False for _ in range(c)] for _ in range(r)]
for i in range(r):
    ball[i] = input().split()

x, y = [int(q) for q in input().split()]
count = 0
o = ball[x][y]  # ball that was looking for


def lookAtFourDirection(x, y):
    global count
    if o == ball[x][y] and not ballTaken[x][y]:
        ballTaken[x][y] = True
        count += 1
        if x - 1 >= 0 and not ballTaken[x - 1][y]:
            lookAtFourDirection(x - 1, y)
        if x + 1 < r and not ballTaken[x + 1][y]:
            lookAtFourDirection(x + 1, y)
        if y - 1 >= 0 and not ballTaken[x][y - 1]:
            lookAtFourDirection(x, y - 1)
        if y + 1 < c and not ballTaken[x][y + 1]:
            lookAtFourDirection(x, y + 1)


lookAtFourDirection(x, y)
print(count * (count - 1))
