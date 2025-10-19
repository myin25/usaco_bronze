# utility function
def check(x):
    print(x)
    return

# take input
numCows, costumeLen = input().split()
numCows = int(numCows)
costumeLen = int(costumeLen)

myCows = []
for i in range(numCows):
    myCows.append(int(input()))
myCows.sort()

# remove duplicates from myCows, then update numCows
check(myCows)
'''myCows = list(set(myCows))
check(myCows)'''
check("")
numCows = len(myCows)
check("numCows " + str(numCows))

# define search method
def binarySearch(left, right, myItem):
    myTempList = myCows[left : right + 1]
    check("my target " + str(myItem))
    check("myTempList " + str(myTempList))
    check("myTempList len " + str(len(myTempList)))

    # check the length of the list to see if you need to return the value
    if (len(myTempList) == 1): # there is an exact middle
        if myTempList[0] <= myItem:
            check("entering here")
            return left
        else:
            check("returning zero")
            return left
    elif (len(myTempList) == 2):
        # see if the second is smaller/equal to the element in question
        if myTempList[1] <= myItem:
            check("right " + str(right))
            return right
        else:
            check("left " + str(left))
            return left
    else:
        # find the index of the middle item
        check("right " + str(right))
        check("left " + str(left))
        middle = right - left

        if middle%2 == 0: # if there is an exact middle
            middle = middle//2
        else: # if there isn't an exact middle
            middle = middle//2 + 1
        middle += left
        check("middle " + str(middle))

        # check to see if you are changing the left limit or right limit
        myMedian = myCows[middle]
        check("myMedian " + str(myMedian))
        if myItem > myMedian:
            return(binarySearch(middle + 1, right, myItem))
        else:
            check("return value " + str(right - left))
            return(right - left)


# main loop
left = 0
right = numCows - 1
counter = 0
for i in myCows:
    # update left border
    left += 1
    check("left border moved to " + str(left))
    
    # find the largest number that I can use
    myTemp = costumeLen - i
    check("base number " + str(i))
    counter += binarySearch(left, right, myTemp) - left + 1
    check("COUNTER " + str(counter))
    check("")

print(counter)
