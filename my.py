# functions
def check(x):
    #print(x)
    return

# define variables
myCounter = 0

B = []
E = []
S = []
I = []
G = []
O = []
M = []
# take in input
numInput = int(input())

# adapt input to lists
for i in range(numInput):
    listAssignment, value = input().split()
    value = int(value)

    # if 
    if listAssignment == "B":
        B.append(value)
    elif listAssignment == "E":
        E.append(value)
    elif listAssignment == "S":
        S.append(value)
    elif listAssignment == "I":
        I.append(value)
    elif listAssignment == "G":
        G.append(value)
    elif listAssignment == "O":
        O.append(value)
    else:
        M.append(value)

# finding odd sums for "bessie"
bessieAddup = len(B)*len(I)
evenBessieCounter = 0
oddBessieCounter = 0

for b in B:
    for i in I:
        if (b + i)%2 == 0:    
            evenBessieCounter += 1
oddBessieCounter = bessieAddup - evenBessieCounter
check("oddBessieCounter " + str(oddBessieCounter))

# finding odd sums for "goes"
goesAddup = len(G)*len(O)*len(E)*len(S)
evenGoesCounter = 0
oddGoesCounter = 0

for g in G:
    for o in O:
        for e in E:
            for s in S:
                if (g+o+e+s)%2 == 0:    
                    evenGoesCounter += 1
oddGoesCounter = goesAddup - evenGoesCounter
check("oddGoesCounter " + str(oddGoesCounter))

# finding odd sums for "moo"
mooAddup = len(M)
evenMooCounter = 0
oddMooCounter = 0

for m in M:
    if m%2 == 0:
        evenMooCounter += 1
oddMooCounter = mooAddup - evenMooCounter
check("oddMooCounter " + str(oddMooCounter))

# printing values
negTotal = oddMooCounter*oddGoesCounter*oddBessieCounter
grandTotal = mooAddup*bessieAddup*goesAddup

endSum = grandTotal - negTotal
print(endSum)
