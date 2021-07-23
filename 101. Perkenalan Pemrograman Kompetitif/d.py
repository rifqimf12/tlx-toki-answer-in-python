# after looking for other's solution, my answer below seems bad
# for an easy-to-understand and efficient answer, check https://tlx.toki.id/courses/competitive/chapters/01/submissions/865910

a = input()
b = input()
i = 0
ii = 0
for _ in range(len(a)):
    if i - ii >= 2 or i >= len(a) - 1 or ii >= len(b):
        break
    if a[i] != b[ii]:
        i += 1
        continue
    i += 1
    ii += 1
if i - ii == 1 or (i == ii and len(a) - len(b) == 1):
    print("Tentu saja bisa!")
else:
    print("Wah, tidak bisa :(")
