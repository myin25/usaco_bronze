# utility function
def check(x):
    #print(x)
    return

# import permutation tool
from itertools import permutations

# open file input
myfile = open("lineup.in","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")

check(content)

# clean out all of the stuff that is not needed
for i in range(1, int(content[0][0]) + 1):
    # initialize temp, which is the variable we use to remove "must be milked.."
    temp = [(content[i])[0], (content[i])[5]]

    # checkpoint
    check(temp)

    # replacing content[i] with temp
    content[i] = temp

check(content)

# create a requirements list
myRequirements = content[1:]
check(myRequirements)

# function to check if a set of requirements are met
def checkRequirements(myList):
    validOrNot = True
    
    # loop through the list of requirements
    for i in range(len(myRequirements)):
        # define variables
        cow1 = myRequirements[i][0]
        cow2 = myRequirements[i][1]

        # checking indices to see if they are a difference of 1
        cow1Index = myList.index(cow1)
        cow2Index = myList.index(cow2)

        if abs(cow2Index - cow1Index) != 1:
            validOrNot = False
            break

    return validOrNot

myCows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
possiblePermutations = permutations(myCows)

for i in list(possiblePermutations):
    if checkRequirements(i) == True:
        check(i)
        break

# return the input as a file
f = open("lineup.out","w+")

for j in i:
    f.write(j)
    f.write("\n")

f.close()
check(i)
