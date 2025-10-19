# utility function
def check(x):
    #print(x)
    return

# define variables
myCows = []
bessieIndex = 0
sortedBessieIndex = 0
unsortedBessieIndex = 0
numMoves = 0

# take input
numCow = int(input())

for i in range(numCow):
    myCows.append(int(input()))

# have the sorted verson
mySortedCows = sorted(myCows)
check(mySortedCows)

# find the item that is out of place
for i in range(numCow - 1):
    if mySortedCows[i] > myCows[i + 1]:
        bessieIndex = i + 1
        break
check("bessieIndex " + str(bessieIndex))

# find the individual indices
sortedBessieIndex = mySortedCows.index(myCows[bessieIndex])
unsortedBessieIndex = myCows.index(myCows[bessieIndex])

check("unsortedBI " + str(unsortedBessieIndex))
check("sortedBI " + str(sortedBessieIndex))

# update numMoves
numMoves = abs(unsortedBessieIndex - sortedBessieIndex)
check("numMoves " + str(numMoves))

if unsortedBessieIndex > sortedBessieIndex:
    n = sortedBessieIndex
    sortedBessieIndex = unsortedBessieIndex
    unsortedBessieIndex = n

tempList = mySortedCows[unsortedBessieIndex + 1:sortedBessieIndex + 1:]

# check to find duplicates
for i in range(len(tempList) - 1):
    if tempList[i] == tempList[i + 1]:
        numMoves -= 1

print(numMoves)
