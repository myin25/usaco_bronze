# utility function
def check(x):
    print(x)
    return

# taking input for dimensions
numCows, numMilk, milkLength, sickLength = input().split()

numCows = int(numCows)
numMilk = int(numMilk)
milkLength = int(milkLength)
sickLength = int(sickLength)

# define variables
milkTranscript = [[0] * 3 for i in range(milkLength)]
sickTranscript = [[0] * 2 for i in range(sickLength)]
sickCowIDs = []

mySickCows = []
possibleBadMilk = []

alreadyCheckedCows = []
myCounter = 0

# updating milkTranscript
for i in range(milkLength):
    cowID, milkType, time = input().split()
    cowID = int(cowID)
    milkType = int(milkType)
    time = int(time)

    milkTranscript[i] = [cowID, milkType, time]

# updating sickTranscript
for i in range(sickLength):
    cowID, sickTime = input().split()
    cowID = int(cowID)
    sickTime = int(sickTime)

    sickTranscript[i] = [cowID, sickTime]

check("milk transcript: original input, matrix")
check(milkTranscript)
check("")
check("sick transcript: original input, matrix")
check(sickTranscript)
check("")

# sort the matrices so you can go by cow
milkTranscript.sort()
sickTranscript.sort()

check("sorted transcripts...")
check(milkTranscript)
check(sickTranscript)
check("")

# find the sick cow ID's
for i in range(sickLength):
    sickCowIDs.append(sickTranscript[i][0])

check("sickcowIDs, list of all the sick cows")
check(sickCowIDs)
check("")

# pop anything after sick time in the potential badmilk list
for i in range(milkLength):
    cowID, milkID, timeMilkDrunk = milkTranscript[i]

    if cowID in sickCowIDs:
        n = sickCowIDs.index(cowID)
        check("n " + str(n))
        timeOfSickness = sickTranscript[n][1]
        check("cowNum, timeOfSickness " + str(cowID) + " " + str(timeOfSickness))

        if timeMilkDrunk < timeOfSickness:
            check("I am adding to new matrix because < timeofsick")
            mySickCows.append(milkTranscript[i])

            if milkID not in possibleBadMilk:
                possibleBadMilk.append(milkID)

check("")
check("mysickcows")
check(mySickCows)
check(possibleBadMilk)
check("")

sickCowConsumption = [[] for i in range(len(sickCowIDs))]
check("sickcowconsumption " + str(sickCowConsumption))

# getting each sick cow's consumption
if len(mySickCows) > 1:
    for i in range(len(mySickCows)):
        check("hi")
        check("mysickcows " + str(mySickCows[i][0] - 1))
        sickCowConsumption[sickCowIDs.index(mySickCows[i][0])].append(mySickCows[i][1])
        check("hihi")
else:
    sickCowConsumption[0].append(mySickCows[0][1])

check(sickCowConsumption)

# finding the intersection
n = sickCowConsumption[0]
myTemp = n

for i in range(len(sickCowConsumption) - 1):
    myTemp = set(n).intersection(sickCowConsumption[i + 1])

    n = sickCowConsumption[i + 1]

myTemp = list(myTemp)

# finding all cows who drank the potentially bad milk
for i in range(milkLength):
    cowID, milkID, timeDrunk = milkTranscript[i]

    if cowID not in alreadyCheckedCows:
        if milkID in myTemp:
            myCounter += 1
            alreadyCheckedCows.append(cowID)
print(myCounter)
