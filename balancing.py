# utility function
def check(x):
    print(x)
    return

# take input
numcow, mymax = input().split()
numcow = int(numcow)
mymax = int(mymax)

mymatrix = [[] for j in range(numcow)]

for i in range(numcow):
    myTemp = input().split()
    mymatrix[i].append(int(myTemp[0]))
    mymatrix[i].append(int(myTemp[1]))

mymatrix.sort()
check(mymatrix)

# find the vertical line's coordinates
def findx(numcow):
    # define variables
    myTemp = mymatrix.copy()

    # find the halfway cow
    if numcow%2 == 1:
        mycow = myTemp[numcow//2]
    else:
        mycow = myTemp[numcow//2-1]
    check(mycow)

    # find the halfway line
    check(mycow[0] - 1)
    return(mycow[0] - 1)

# flip the x and y in order to solve for findy
reverseMatrix = [[] for j in range(numcow)]
for i in range(numcow):
    myTemp = mymatrix[i]
    reverseMatrix[i].append(myTemp[1])
    reverseMatrix[i].append(myTemp[0])

reverseMatrix.sort()
check(reverseMatrix)

# find the horizontal line's coordinates
def findy(numcow):
    # define variables
    myTemp = reverseMatrix.copy()

    # find the halfway cow
    if numcow%2 == 1:
        mycow = myTemp[numcow//2]
    else:
        mycow = myTemp[numcow//2-1]

    # find the halfway line
    check(mycow[0] - 1)
    return(mycow[0] - 1)

# find the horizontal line's coordinates
findx(numcow)
findy(numcow)
