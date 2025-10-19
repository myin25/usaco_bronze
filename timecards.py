# defining classes
class cow:
    def __init__(self, cowID):
        self.cowID = cowID
        self.start = 0
        self.stop = 0
        self.totalTime = 0
    
    def getTotal():
        return(self.totalTime)
    
    def startTime(self, start):
        self.start = start
    
    def stopTime(stop):
        self.stop = stop

        self.totalTime += self.stop - self.start

# utility function
def check(x):
    #print(x)
    return

# define variables
myCows = {}

# taking input
numCows, numRows = input().split()
numCows = int(numCows)
numRows = int(numRows)

# main loop
for i in range(numRows):
    cowID, startOrStop, timeHrs, timeMins = input().split()
    
    cowID = int(cowID)
    timeHrs = int(timeHrs)*60
    timeMins = int(timeMins)

    
    myCow = cow(cowID)
    check("cowID " + str(cowID))

    # check to see if the item is already in the list or not
    # if it is, then update that item
    # if it isn't then add the item
    if cowID not in myCows:
        check("cowID is not in myCows")
        myCows[cowID] = cow(cowID)

        if startOrStop == "START":
            myTime = timeHrs + timeMins
            #myCows[cowID].startTime= myTime
            myCows[cowID].startTime(myTime)
            check("added time 1 " + str(myCows[cowID].start))

        '''for i in (myCows):
            check(i)
            check(myCows[i].startTime)
            check("")'''
    
    else:
        myTime = timeHrs + timeMins
        if startOrStop == "START":
            check("added time 2 ")
            myCows[cowID].start = myTime
        else:
            check("stop time " + str(cowID))
            check(str(timeHrs) + " " + str(timeMins) + " " + str(myCows[cowID].startTime))
            timeDiff = myTime - myCows[cowID].startTime
            (myCows[cowID].totalTime) += timeDiff
            check("stop time " + str(myCows[cowID].totalTime))

for i in (myCows):
    check(i)
    check(myCows[i].totalTime)
    hour, minute = divmod(myCows[i].totalTime, 60)
    print(str(hour), str(minute))

