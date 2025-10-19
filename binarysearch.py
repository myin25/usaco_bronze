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
        #check("myMedian " + str(myMedian))
        if myItem > myMedian:
            return(binarySearch(middle, right, myItem))
        elif myItem == myMedian:
            return(middle)
        else:
            return(binarySearch(left, middle, myItem))
        
    
    
# main loop
for i in myQueries:
    if i not in myList: # if the item is not in the list, return -1
        print(-1)
    else:
        if i == 0:
            print(myList[0])
        elif i == len(myList) - 1:
            print(myList[len(myList) - 1])
        else:
            n = binarySearch(0, numItems - 1, i)
            # see if there are more than 2 consecutive n's:
            if myList[n] == myList[n - 1]:
                #consecutiveEqual = True # this checks to see if the next is equal

                #while consecutiveEqual == True:
                for i in range(5):
                    if myList[n] == myList[n - 1]:
                        n -= 1
                    else:
                        break
                print(n)
            else:
                print(n)
