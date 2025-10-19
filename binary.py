# utility function
def check(x):
    print(x)
    return

# take input
numItems, numQuestions = input().split()
numItems = int(numItems)
numQuestions = int(numQuestions)

myList = input().split()
for i in range(numItems):
    myList[i] = int(myList[i])

myQueries = []
for i in range(numQuestions):
    myQueries.append(int(input()))

# define function for binary search
def binarySearch(myList, target):
    # define left and right points
    minPoint = 0
    maxPoint = len(myList) - 1

    '''# define the middle point
    midPoint = (len(myList) - 1)//2'''

    # loop through
    while minPoint <= maxPoint:
        # define the middle point
        midPoint = minPoint + (maxPoint)//2

        # check values
        check("minPoint " + str(minPoint))
        check("maxPoint " + str(maxPoint))
        check("midPoint " + str(midPoint))

        # adjust the list
        if target > myList[midPoint]: # you have to take the right half of the list
            minPoint = midPoint + 1
        elif target == myList[midPoint]: # you hit the target exactly
            return midPoint
        else: # you have to take the left half of the list
            maxPoint = midPoint - 1

for i in myQueries:
    if i in myList:
        print(binarySearch(myList, i))
    else:
        print(-1)
