# utility function
def check(x):
    print(x)
    return

# take input
numDays = int(input())
breakoutLog = input().split()

for i in range(numDays):
    breakoutLog[i] = int(breakoutLog[i])

# variables
valid = True

# set up to find the minimum and maximum amounts of breakouts
# if the item is marked as "b", then it's definitely a breakout
# if the item is marked as -1, then it's a possibility
breakoutLog[0] = "b"
for i in range(numDays - 1, -1, -1):
    if breakoutLog[i] != str(breakoutLog[i]):
        check("integer")
        # if there are still more "peaceful" days left
        if breakoutLog[i] > 1:
            if breakoutLog[i] != breakoutLog[i - 1]:
                breakoutLog[i - 1] = breakoutLog[i] - 1
            else:
                valid = False
        elif breakoutLog[i] == 1: # if there was a breakout
            breakoutLog[i - 1] = "b"
        elif breakoutLog[i] == 0:
            breakoutLog[i] = "b"
    else:
        check("string")
check(breakoutLog)

if valid == True:
    # look for the least number of breakouts
    leastBreaks = 0
    for i in breakoutLog:
        if i == "b":
            leastBreaks += 1
    print(leastBreaks, end = " ")

    # look for the most number of breaks
    mostBreaks = leastBreaks
    for i in breakoutLog:
        if i == -1:
            mostBreaks += 1
    print(mostBreaks)
else:
    print(-1)
