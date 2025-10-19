# utility function
def check(x):
    #print(x)
    return

# input + define variables
matrixSize = int(input())
originalMatrix = [[0] * matrixSize for i in range(matrixSize)]
endMatrix = [[0] * matrixSize for i in range(matrixSize)]
workingMatrix = [[0] * matrixSize for i in range(matrixSize)]

x = 0
y = 0
counter = 1

for row in range(matrixSize):
    originalMatrix[row] = list(input())

for row in range(matrixSize):
    endMatrix[row] = list(input())

# define function
def rotate90(beginningMatrix):
    workingMatrix = [[0] * matrixSize for i in range(matrixSize)]
    x = 0
    y = 0

    for row in range(matrixSize):
        for col in range(matrixSize -1, -1, -1):
            # update workingMatrix
            workingMatrix[x][y] = beginningMatrix[col][row]
            y += 1
        x += 1
        y = 0
    return(workingMatrix)

def rotate180(beginningMatrix):
    # round 1
    temp1 = rotate90(beginningMatrix)

    # round 2
    temp2 = rotate90(temp1)

    return(temp2)

def rotate270(beginningMatrix):
    # round 1
    temp1 = rotate90(beginningMatrix)

    # round 2
    temp2 = rotate90(temp1)

    # round 3
    temp3 = rotate90(temp2)

    return(temp3)

def reflect():
    x = 0
    y = 0

    for row in range(matrixSize):
        for col in range(matrixSize -1, -1, -1):
            # update workingMatrix
            workingMatrix[x][y] = originalMatrix[row][col]

            y += 1

        x += 1
        y = 0
    return(workingMatrix)

def combination(n): # loop through 1, 2, or 3
    myTemp = reflect()
    outcome = [[0] * matrixSize for i in range(matrixSize)]

    if n == 0:
        outcome = rotate90(myTemp)

    elif n == 1:
        outcome = rotate180(myTemp)

    elif n == 2:
        outcome = rotate270(myTemp)

    return(outcome)

# EXECUTION OF CODE
myMatrix = rotate90(originalMatrix)

# level 1
if myMatrix == endMatrix:
    print(counter)
else:
    # level 2
    counter += 1
    myMatrix = rotate180(originalMatrix)

    if myMatrix == endMatrix:
        print(counter)
    else:
        # level 3
        counter += 1
        myMatrix = rotate270(originalMatrix)

        if myMatrix == endMatrix:
            print(counter)
        else:
            # level 4
            counter += 1
            myMatrix = reflect()

            if myMatrix == endMatrix:
                print(counter)
            else:
                # level 5
                counter += 1

                for i in range(3):
                    myMatrix = combination(i)

                    if myMatrix == endMatrix:
                        print(counter)
                        break
                if myMatrix != endMatrix:
                    # level 7
                    counter += 2
                    print(counter)

