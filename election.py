# utility function
def check(x):
    #print(x)
    return

# define variables
round1 = []
round2 = []
myIndexes = []
tempList = []

# take input
numOrig, numFinal = input().split()
numOrig = int(numOrig)
numFinal = int(numFinal)

for i in range(numOrig):
    temp1, temp2 = input().split()
    temp1 = int(temp1)
    temp2 = int(temp2)

    round1.append(temp1)
    round2.append(temp2)

check(round1)
check(round2)

# finding sorted versions
sorted1 = sorted(round1)
sorted2 = sorted(round2)

check(sorted1)
check(sorted2)

# find the indices for round 1
n = sorted1[len(sorted1) - numFinal::]
check(n)

for i in range(numFinal):
    myIndexes.append(round1.index(n[i]))

check(myIndexes)

# create temporary list which holds the numbers from round 2
for i in range(len(myIndexes)):
    tempList.append(round2[myIndexes[i]])

tempList.sort()
check(tempList)

# find the index of the last item of the templist
myTemp = tempList[len(tempList) - 1]

print(round2.index(myTemp) + 1)
