# utility function
def check(x):
    #print(x)
    return

# take input
numSpaces, numFlowerTypes = input().split()
numSpaces = int(numSpaces)
numFlowerTypes = int(numFlowerTypes)

plantInstructions = [[] for i in range(numFlowerTypes)]
for i in range(numFlowerTypes):
    myTemp = input().split()
    plantInstructions[i].append(int(myTemp[0]))
    plantInstructions[i].append(int(myTemp[1]))

check(plantInstructions)

# initialize the garden
myGarden = ["." for i in range(numSpaces)]

# define a "planting" function
def plant(beginning, howOften):
    beginning -= 1
    # create a list starting at the beginning spot
    myTempGarden = myGarden[beginning:]
    # loop through myGarden starting at the beginning index
    for i in range(len(myTempGarden)):
        # check to see if the position is valid
        if i % howOften == 0:
            myTempGarden[i] = "1"
    check("i " + str(i))
    plantedGarden = myGarden[:beginning] + myTempGarden
    check(plantedGarden)
    check("len planted " + str(len(plantedGarden)))
    return(plantedGarden)


# loop through all plant instructions using the "plant" function
for i in range(numFlowerTypes):
    start, frequency = plantInstructions[i]
    myGarden = plant(start, frequency)
    check(myGarden)
    check("len garden " + str(len(myGarden)))
    check("")

# find the number of leftover empty spots
emptyCounter = 0
for i in myGarden:
    if i == ".":
        emptyCounter += 1
print(emptyCounter)
