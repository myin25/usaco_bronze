# utility function
def check(x):
    #print(x)
    return

# take input
farmer, cow = input().split()
farmer = int(farmer)
cow = int(cow)

# define other variables
stepsCounter = 0
currentPosition = farmer
distanceToTravel = 1 # this basically tells me how much to travel, powers of 2
left = False # tells me what direction to travel

# main loop if the farmer is behind the cow
if farmer < cow:
    while currentPosition < cow:
        # debugging
        check("counter " + str(stepsCounter))
        check("position " + str(currentPosition))

        # if you are going to the right first
        if left == False: # if the farmer is going right
            currentPosition += distanceToTravel
            stepsCounter += distanceToTravel
            left = True
        else: # if you are going to the left
            currentPosition -= distanceToTravel
            stepsCounter += distanceToTravel
            left = False

        # checkpoint to see if I need to break
        if currentPosition >= cow:
            break
        else:
            # I need to reset the position of the farmer and update DTT
            stepsCounter += distanceToTravel
            currentPosition = farmer
            distanceToTravel *= 2

else: # main loop if the farmer is ahead of the cow
    while currentPosition > cow:
        # debugging
        check("counter " + str(stepsCounter))
        check("position " + str(currentPosition))
        check("distance to travel")

        # if you are going to the right first
        if left == False: # if the farmer is going right
            currentPosition += distanceToTravel
            stepsCounter += distanceToTravel
            left = True
        else: # if you are going to the left
            currentPosition -= distanceToTravel
            stepsCounter += distanceToTravel
            left = False

        # checkpoint to see if I need to break
        if currentPosition <= cow:
            break
        else:
            # I need to reset the position of the farmer and update DTT
            stepsCounter += distanceToTravel
            currentPosition = farmer
            distanceToTravel *= 2

stepsCounter -= abs(currentPosition - cow)
print(stepsCounter)
