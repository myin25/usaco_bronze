# functions
def check(x):
    #print(x)
    return

# define variables
myCounterBessie = 0
myCounterGoes = 0
myCounterMoo = 0

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

# create the counter addups
bessieAddup = len(B)*len(I)
goesAddup = len(G)*len(O)*len(E)*len(S)
mooAddup = len(M)

# find all possible even sums
for b in B:
    for i in I:
        myNum = b + i

        if myNum % 2 == 0:
            myCounterBessie += 1
check(bessieAddup)
check(myCounterBessie)
myCounterBessieNeg = bessieAddup - myCounterBessie
check(myCounterBessieNeg)
check("")

# find all possible even sums for goes
for g in G:
    for o in O:
        for e in E:
            for s in S:
                myNum = g + o + e + s

                if myNum % 2 == 0:
                    myCounterGoes += 1
check(goesAddup)
check(myCounterGoes)
myCounterGoesNeg = goesAddup - myCounterGoes
check(myCounterGoesNeg)
check("")

# find all possible even sums for moo
for m in M:
    myNum = m

    if myNum % 2 == 0:
        myCounterMoo += 1
check(mooAddup)
check(myCounterMoo)
myCounterMooNeg = mooAddup - myCounterMoo
check(myCounterMooNeg)
check("")

# total
check("")
total = mooAddup * goesAddup * bessieAddup
neg = myCounterBessieNeg*myCounterGoesNeg*myCounterMooNeg


print(total - neg)











