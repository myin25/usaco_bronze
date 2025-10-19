#take input
numBales = int(input())

myList = []
for i in range(numBales):
    myList.append(int(input()))

# sort list
myList.sort()

# function 1
def leftExplodeIndex(myList, index):
    # define variables
    myRadius = 1
    lastExplosion = index
    # variable to help you move left
    direction = -1

    #see if the next item is in exploding distance
    myitem = myList[index]
    while (index + direction >= 0) and ((myList[index] - myList[index + direction]) <= myRadius):
        index += direction
        myRadius += 1
    return index

# function 2
def rightExplodeIndex(myList, index):
    # define variables
    myRadius = 1
    lastExplosion = index
    # variable to help move right
    direction = 1

    # see if item is in exploding distance
    myitem = myList[index]
    while (index + direction < len(myList)) and ((myList[index + direction] - myList[index]) <= myRadius):
        index += direction
        myRadius += 1
    return index
    
# start simulating explosions
for i in range(numBales):
    # find left half
    leftHalf = leftExplodeIndex(myList, i) - i

    # find right half
    rightHalf = rightExplodeIndex(myList, i) - i

    # check
    print(leftHalf, rightHalf)
