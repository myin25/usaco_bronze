# define variables
currentTime = 0

# utility function
def check(x):
    #print(x)
    return

# take input
numCows = int(input())
myMatrix = [[] for i in range(numCows)]

# creating matrix
for i in range(numCows):
    # taking input
    startTime, processingTime = input().split()
    startTime = int(startTime)
    processingTime = int(processingTime)

    # adding to matrix
    myMatrix[i].append(startTime)
    myMatrix[i].append(processingTime)


# sort matrix by arrival time
myMatrix.sort()

# loop through matrix
for i in range(numCows):
    # define temporary variables
    tempStartTime = myMatrix[i][0]
    tempProcessTime = myMatrix[i][1]
    
    # check if item is > or < of current time
    if currentTime < tempStartTime: # larger than current time
        currentTime = tempStartTime + tempProcessTime
    else: # smaller than current time
        currentTime += tempProcessTime
print(currentTime)
