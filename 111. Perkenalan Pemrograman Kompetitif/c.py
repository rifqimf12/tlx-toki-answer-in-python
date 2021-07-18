import re

pattern = "^" + input().replace("*", ".*") + "$"
n = int(input())
r = re.compile(pattern)
for _ in range(n):
    m = r.search(input())
    if m:
        print(m.group())
