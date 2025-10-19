# utility function
def check(x):
    #print(x)
    return

# taking input
numCows, numRows = input().split()
numCows = int(numCows)
numRows = int(numRows)

# define variables
myCows = {}
hold = [0]*numCows

# main loop
for i in range(numRows):
    # input
    cowID, startOrStop, timeHrs, timeMins = input().split()
    
    # define variables
    cowID = int(cowID) - 1
    timeHrs = int(timeHrs)*60
    timeMins = int(timeMins)
    mySum = 0
    
    # check to see if the item is start or stop
    if startOrStop == "START":
        hold[cowID] = timeHrs + timeMins
    else:
        mySum = abs(hold[cowID] - timeHrs - timeMins)

        check("mySum " + str(mySum))

        # check to see if the item is in the dictionary
        # note that this only happens if there is a stop AND start
        if cowID in myCows:
            myCows[cowID] += mySum
        else:
            myCows[cowID] = mySum

# printing output
for i in range(numCows):
    printHr = int(myCows[i]/60)
    printMin = myCows[i]%60

    print(printHr, printMin)
