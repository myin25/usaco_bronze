# functions
def check(x):
    print(x)
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

# check values
check(B)
check(E)
check(S)
check(I)
check(G)
check(O)
check(M)

# main loop
for b in B:
    for e in E:
        for s in S:
            for i in I:
                myNum = b+e+s+s+i+e
                check("BESSIE " + str(myNum))

                if myNum %2 == 0:
                    myCounter += 1
                else:
                    for g in G:
                        for o in O:
                            myNum = g + o + e + s
                            check("GOES " + str(myNum))

                            if myNum%2 == 0:
                                myCounter += 1
                            else:
                                for m in M:
                                    myNum = m + o + o
                                    check("MOO " + str(myNum))

                                    if myNum%2 == 0:
                                        myCounter += 1
print(myCounter)
