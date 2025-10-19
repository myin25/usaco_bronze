# utility function
def check(x):
    #print(x)
    return

# take input
numCows = int(input())

# initialize matrix
myCows = [[] for i in range(numCows)]
for i in range(numCows):
    myTemp = input().split()
    myCows[i].append(int(myTemp[0]))
    myCows[i].append(int(myTemp[1]))

# outlier function to return the index of the most alone cow to the right
def outlierPos():
    # find all of the x and y coords
    unsortedX = []
    unsortedY = []
    for i in range(numCows):
        unsortedX.append(myCows[i][0])
        unsortedY.append(myCows[i][1])
    xCoord = sorted(unsortedX)
    yCoord = sorted(unsortedY)

    # find the largest of each list
    xTemp = xCoord[len(xCoord) - 1]
    yTemp = yCoord[len(yCoord) - 1]

    # see which one is the furthest out
    xDiff = abs(xTemp - xCoord[len(xCoord) - 2])
    yDiff = abs(yTemp - yCoord[len(yCoord) - 2])

    # return the largest value
    if xDiff > yDiff:
        return(unsortedX.index(xTemp))
    else:
        return(unsortedY.index(yTemp))

# outlier function to reuturn the index of the most alone cow to the left
def outlierNeg():
    # find all of the x and y coords
    unsortedX = []
    unsortedY = []
    for i in range(numCows):
        unsortedX.append(myCows[i][0])
        unsortedY.append(myCows[i][1])
    xCoord = sorted(unsortedX)
    yCoord = sorted(unsortedY)

    # find the largest of each list
    xTemp = xCoord[0]
    yTemp = yCoord[0]

    # see which one is the furthest out
    xDiff = abs(xTemp - xCoord[0])
    yDiff = abs(yTemp - yCoord[0])

    # return the largest value
    if xDiff > yDiff:
        return(unsortedX.index(xTemp))
    else:
        return(unsortedY.index(yTemp))

# remove the outlier
removeCowPos = outlierPos()
removeCowNeg = outlierNeg()
if removeCowPos > removeCowNeg:
    myCows.pop(removeCowPos)
else:
    myCows.pop(removeCowNeg)

# find the area of the remaining cows
# first, find the possible x and ys
myXs = []
myYs = []
for i in range(len(myCows)):
    myXs.append(myCows[i][0])
    myYs.append(myCows[i][1])

# find the lower left corner and upper right corner coordinates
lowerLeftCorner = [min(myXs), min(myYs)]
upperRightCorner = [max(myXs), max(myYs)]

check(lowerLeftCorner)
check(upperRightCorner)

# find the base and height of the rectangle
rectangleBase = abs(lowerLeftCorner[0] - upperRightCorner[0])
rectangleHeight = abs(lowerLeftCorner[1] - upperRightCorner[1])
check(rectangleBase)
check(rectangleHeight)
print(rectangleBase*rectangleHeight)
