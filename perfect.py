# take input
squareSize = int(input())
myMatrix = []

for i in range(squareSize):
    myMatrix.append([int(x) for x in input().split()])

# function
middleSpot = squareSize//2
if squareSize%2 == 0:
    middleSpot -= 1

def median(lst):
    lst.sort()
    return(lst[middleSpot])

# main loop
finalList = []
for i in range(squareSize):
    finalList.append(median(myMatrix[i]))

print(median(finalList))
