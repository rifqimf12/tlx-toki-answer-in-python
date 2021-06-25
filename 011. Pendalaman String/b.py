str, substr = input().split()
while str.find(substr) != -1:
    str = str.replace(substr, "")
print(str)
