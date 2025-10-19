# utility function
def check(x):
    #print(x)
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

# binary search function
def binarySearch(left, right, myItem):
    myTempList = myList[left:right + 1]
    #check("myTempList " + str(myTempList))

    # check the length of the list to see if you need to return the value
    if len(myTempList) == 1:
        return(myTempList[left])
    else:
        # find the index of the middle item
        #check("right " + str(right))
        #check("left " + str(left))
        middle = right - left

        if middle%2 == 0: # if there is no exact middle
            middle = middle//2
        else: # if there is an exact middle
            middle = middle//2 + 1
        middle += left
        #check("middle " + str(middle))

        # check to see if you are changing the left limit or right limit
        myMedian = myList[middle]
        
        #see what you need to return
        if myItem > myMedian:
            return(False, middle, right)
        elif myItem == myMedian:
            return(True, middle)
        else:
            return(False, left, middle)
        
    
    
# main loop
for i in myQueries:
    if i not in myList: # if the item is not in the list, return -1
        print(-1)
    else:
        # define variables
        left = 0
        right = len(myList) - 1
        n = list(binarySearch(left, right, i))

        # main loop
        while len(n) == 3:
            # if the length of n is two, then we know that we have the answer
            if len(n) == 2:
                break
            else: # in the case that we are not done yet
                left = n[1]
                right = n[2]
                n = list(binarySearch(left, right, i))

        # if the length of n is two, then we know that we have the answer
        if len(n) == 2:
            myTemp = n[1]
            if myList[myTemp] == myList[myTemp - 1]:
                consecutiveEqual = True # this checks to see if the next is equal

                while consecutiveEqual == True:
                    if myList[myTemp] == myList[myTemp - 1]:
                        myTemp -= 1
                    else:
                        consecutiveEqual = False
                print(myTemp)
            else:
                print(myTemp)
