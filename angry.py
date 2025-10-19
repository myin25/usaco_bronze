# utility function
def check(x):
    print(x)
    return

# take input
numCows = int(input())
myList = []

for i in range(numCows):
    myList.append(int(input()))

myList.sort()
check(myList)

# look through list and find the number of exploded hay bales on left
def simulateLeft(index):
    counter = 0
    largestStep = 1
    
    # check the left of the list
    left = myList[:index]
    if len(left) > 1:
        # define variables
        temp = index
        temp2 = index - 1

        # loop through 
        while temp2 >= 0:
            if myList[temp] - myList[temp2] <= largestStep:
                counter += 1
                largestStep += 1
            else:
                break
            temp -= 1
            temp2 -= 1
    elif len(left) == 1:
        if myList[index] - left[0] <= largestStep:
            counter += 1
    
    return counter

# look through list and find the number of exploded hay bales on the right
def simulateRight(index):
    counter = 0
    largestStep = 1

    # check the right of the list
    right = myList[index + 1:]
    if len(right) > 1:
        # define variables
        temp = index
        temp2 = index + 1

        # loop through
        while temp2 <= len(myList) - 1:
            if myList[temp2] - myList[temp] <= largestStep:
                counter += 1
                largestStep += 1
                check(str(myList[temp]) + " " + str(myList[temp2]))
                check("True, " + str(largestStep))
            else:
                check(str(myList[temp]) + " " + str(myList[temp2]))
                check("False, " + str(largestStep))
                break
            temp += 1
            temp2 += 1
    elif len(right) == 1:
        if myList[index + 1] - myList[index] <= largestStep:
            counter += 1

    return counter

# look through list and find the number of exploded hay bales on right
# driver code
end = 0
for i in range(len(myList)):
    x = simulateLeft(i)
    y = simulateRight(i)
    check("x " + str(x))
    check("y " + str(y))
    check(x + y)
    end = max(end, x + y)
    check("")

print(end)
