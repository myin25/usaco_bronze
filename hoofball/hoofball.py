# utility function
def check(x):
    print(x)
    return

# define variables
numCows = int(input())
myPositions = input().split()
distances = []
numBalls = 0
descending = True
ascending = True
i = 0

# convert to integers
for i in range(numCows):
    myPositions[i] = int(myPositions[i])

myPositions.sort()
check(myPositions)


# find distances
for i in range(1, numCows):
    n = myPositions[i] - myPositions[i - 1]
    distances.append(n)
check("  " + str(distances))

# remove repetitions if they're next to each other
i = 0

while i < len(distances) - 1:
    if distances[i] == distances[i + 1]:
        distances.pop(i)
    else:
        i += 1
check("here is the edited list")
check(distances)

# sum up total balls needed
check(len(distances))
check("")

i = 0

while i < len(distances) - 1:
    check(i)

    if distances[i] > distances[i + 1]:
        while descending == True and i < (len(distances) - 1):
            

            if distances[i] <= distances[i + 1]:
                descending = False
            else:
                check("descending continue")
            i += 1

        numBalls += 1
        check("increased number of balls " + str(numBalls))

        check("breaking from index, descending " + str(i))
        descending = True
        check("")
        
    elif distances[i] <= distances[i + 1]:
        while ascending == True and i < (numCows - 2):

            if distances[i] >= distances[i + 1]:
                ascending = False
            else:
                check("ascending continue")

            i += 1

        numBalls += 1
        check("increased number of balls " + str(numBalls))
        
        check("breaking from index, ascending " + str(i))
        ascending = True
        check("")

    if i < len(distances) - 3 and i > 0:
        if distances[i - 1] < distances[i] and distances[i] > distances[i + 1] and distances[i + 1] < distances[i + 2]:
            check("ENTER IF STATEMENT")
            i += 1

if (distances[len(distances) - 1] > distances[len(distances) - 2]) and distances[len(distances) - 2] < distances[len(distances) - 3]:
    numBalls += 1
check("heres i " + str(i))
check("numBalls:")
print(numBalls)
