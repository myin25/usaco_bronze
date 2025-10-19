# take input
climbRate, sleepRate, poleHeight = [int(x) for x in input().split()]

# calculate time
endRate = climbRate - sleepRate
days = poleHeight/endRate

# see if you need to add one
days = round(days)
if poleHeight%endRate == 0:
    days -= 1

print(days)
