n, x = [int(q) for q in input().split()]
smallestDeficit = 400000
winner = 0
for coupon in [int(q) for q in input().split()]:
    deficit = abs(coupon - x)
    if deficit > smallestDeficit:
        pass
    elif deficit < smallestDeficit:
        smallestDeficit = deficit
        winner = coupon
    else:
        if coupon < winner:
            winner = coupon
print(winner)
