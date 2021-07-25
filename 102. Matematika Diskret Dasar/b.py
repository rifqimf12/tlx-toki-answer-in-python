# got two TLEs before tweaking this code
# i guess we should really use C++ in CP


# got maxInt value by try this script until primeCount=maxK, dunno if there's another way
maxInt = 10 ** 6
maxK = 77777
i = 2
isNotAPrime = [False for _ in range(maxInt)]
primeCount = 0
primeNumbers = []

while primeCount < maxK:
    if not isNotAPrime[i]:
        for ii in range(i * i, maxInt, i):
            isNotAPrime[ii] = True
        primeNumbers.append(i)
        primeCount += 1
    i += 1
t = int(input())
for _ in range(t):
    i = int(input()) - 1
    print(primeNumbers[i])
