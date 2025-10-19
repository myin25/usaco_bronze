# utility function
def check(x):
    print(x)
    return

# take input
numCows = int(input())
myMatrix = []

for i in range(numCows):
    mytemp = [int(x) for x in input().split()]
    myMatrix.append(mytemp)

# sort myMatrix to make it chronological
myMatrix.sort()
check(myMatrix)

# define variable num, which keeps track of your answer
num = myMatrix[0][0]
xHistory = []

# define function to find how many buckets are available
def recycle(index, start, end, numbuckets):
    mycounter = 0

    for i in range(index):
        tempstart, tempend, tempbuckets = myMatrix[i]
        # see where you start
        if tempend < start:
            # the only way you can recycle is if your bracket is completely outside
            mycounter += tempbuckets

    return mycounter

# loop through the rest of the matrix
for row in range(1, numCows):
    # define temporary variables
    tempStart, tempEnd, tempBuckets = myMatrix[row]

    # call the function to determine how many buckets are available
    x = recycle(row, tempStart, tempEnd, tempBuckets)
    check(x)
    xHistory.append(x)

    # add to num, you don't need to if more than/equal to numbuckets
    if x != 0:
        if x < tempBuckets:
            num += tempBuckets - x
    else:
        num += tempBuckets
    check(num)
    check("")

print(num)
