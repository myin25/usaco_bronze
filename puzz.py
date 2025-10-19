# take input
climbRate, sleepRate, poleHeight = [int(x) for x in input().split()]

# calculate time
endRate = climbRate - sleepRate
days = 0
altitude = 0

# see if you need to add one
if poleHeight%endRate == 0:
    days = poleHeight//endRate - 1
else:
    while altitude < poleHeight:
        altitude += climbRate
        days += 1

        if altitude >= poleHeight:
            break

        altitude -= sleepRate

print(days)
