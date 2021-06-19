import sys

numbers = []
for number in sys.stdin:
    numbers.append(number)
for x in reversed(numbers):
    print(x)
