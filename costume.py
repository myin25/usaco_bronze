# utility function
def check(x):
    #print(x)
    return

# take input
numCows, costumeLen = input().split()
numCows = int(numCows)
costumeLen = int(costumeLen)

myCows = []
for i in range(numCows):
    myCows.append(int(input()))
myCows.sort()

# main loop
left = 0
counter = 0
for i in myCows[:numCows - 1]:
    # increase left boundary to create list to check from
    left += 1
    check(i)
    # create checking list
    myTemp = myCows[left:]
    check(myTemp)

    for j in myTemp:
        if i + j < costumeLen:
            counter += 1
        else:
            break
print(counter)
