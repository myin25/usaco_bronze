# define billboard coordinates
badBillboard = [[],[]]
goodBillboard = [[],[]]
counter = 0

# utility function
def check(x):
    print(x)
    return

# take input
myTemp = input().split(" ")
badBillboard = [[int(myTemp[0]), int(myTemp[1])], [int(myTemp[2]), int(myTemp[3])]]

myTemp = input().split(" ")
goodBillboard = [[int(myTemp[0]), int(myTemp[1])], [int(myTemp[2]), int(myTemp[3])]]

check(badBillboard)
check(goodBillboard)

# make a list of all the points of badBillboard
badPoints = [[],[],[],[]]

# find the upper left badpoint
badPoints[0].append(badBillboard[0][0])
badPoints[0].append(badBillboard[1][1])
check("badpoints " + str(badPoints))

# find the lower left badpoint
badPoints[1].append(badBillboard[0][0])
badPoints[1].append(badBillboard[0][1])
check("badpoints " + str(badPoints))

# find the lower right badpoint
badPoints[2].append(badBillboard[1][0])
badPoints[2].append(badBillboard[0][1])
check("badpoints " + str(badPoints))

# find the lower right badpoint
badPoints[3].append(badBillboard[1][0])
badPoints[3].append(badBillboard[1][1])
check("badpoints " + str(badPoints))


# make a list of all the points of goodBillboard
goodPoints = [[],[],[],[]]

# find the upper left goodpoint
goodPoints[0].append(goodBillboard[0][0])
goodPoints[0].append(goodBillboard[1][1])
check("goodpoints " + str(goodPoints))

# find the lower left goodpoint
goodPoints[1].append(goodBillboard[0][0])
goodPoints[1].append(goodBillboard[0][1])
check("goodpoints " + str(goodPoints))

# find the lower right goodpoint
goodPoints[2].append(goodBillboard[1][0])
goodPoints[2].append(goodBillboard[0][1])
check("goodpoints " + str(goodPoints))

# find the upper right goodpoint
goodPoints[3].append(goodBillboard[1][0])
goodPoints[3].append(goodBillboard[1][1])
check("goodpoints " + str(goodPoints))

# take care of special cases
if (goodPoints[1][0] <= badPoints[1][0]) and (goodPoints[1][1] <= badPoints[1][1]):
    # if the goodboard completely covers badboard
    if (goodPoints[3][0] >= badPoints[3][0]) and (goodPoints[3][1] >= badPoints[3][1]):
        print(0)
    elif (goodPoints[3][0] <= badPoints[3][0]) and (goodPoints[3][1] >= badPoints[3][1]):
        counter = 2
    else: # when there's one corner inside of the badboard
        counter = 1
elif (goodPoints[1][0] <= badPoints[1][0]) and (goodPoints[1][1] >= badPoints[1][1]) and (goodPoints[1][1] <= badPoints[3][1]):
    if (goodPoints[3][0] >= badPoints[3][0]) and (goodPoints[3][1] >= badPoints[3][1]):
        counter = 3
        check("AwA")
    else:
        counter = 1
else:
    counter = 1

# handling the counter
if counter == 1:
    check("")
    print((badPoints[0][1] - badPoints[1][1])*(badPoints[2][0] - badPoints[0][0]))
elif counter == 2:
    check("length is " + str(badPoints[3][0] - goodPoints[3][0]))
    check("the height is " + str(badPoints[2][0] - badPoints[0][0]))
    print((badPoints[3][0] - goodPoints[3][0])*(badPoints[0][1] - badPoints[2][1]))
elif counter == 3:
    check("length is " + str(goodPoints[1][0] - badPoints[1][0]))
    check("height is " + str(badPoints[2][0] - badPoints[1][0]))
    print((goodPoints[1][1] - badPoints[1][1])*(badPoints[2][0] - badPoints[1][0]))
