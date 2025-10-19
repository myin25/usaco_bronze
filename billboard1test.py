# utility function
def check(x):
    #print(x)
    return

# define variables
n = 0 # n is the number that the user recieves at the end of the program
temp1 = 0 # the area of overlap between the truck and board1
temp2 = 0 # the area of overlap between the truck and board2
a1 = 0 # the area of the actual board1
a2 = 0 # the area of the actual board2
board1result = 0 # the result of board1 calculations
board2result = 0 # the result of board2 calculations

# take input
board1 = input().split(" ")
board2 = input().split(" ")
truck = input().split(" ")

# convert to integers
for i in range(len(board1)):
    board1[i] = int(board1[i])
    board2[i] = int(board2[i])
    truck[i] = int(truck[i])

# find the areas of the boards
a1 = (board1[2] - board1[0])*(board1[3] - board1[1])
a2 = (board2[2] - board2[0])*(board2[3] - board2[1])

# define a function to find overlap area
def myfunc(x):
    # find the upper right corner of the overlap area of board1 and truck
    URx = min(x[2], truck[2])
    URy = min(x[3], truck[3])

    #check(overlapURx)
    #check(overlapURy)

    # find the lower left corner of the overlap area of board1 and truck
    LLx = max(x[0], truck[0])
    LLy = max(x[1], truck[1])

    #check(overlapLLx)
    #check(overlapLLy)

    temp1 = (URx - LLx)*(URy - LLy)

    check(temp1)
    return temp1

# define a function to check whether the two rectangles overlap
def overlap(x):
    # define boolean called overlap
    overlap = False
    # check to see if it overlaps through x
    a = max(x[0], truck[0])
    b = min(x[2], truck[2])

    check(a)
    check(b)

    if b > a:
        overlap = True

        # check to see if it overlaps through y
        c = min(x[1], truck[0])
        d = max(x[3], truck[3])

        check(c)
        check(d)

        if d > c:
            return True
        else:
            return False
    else:
        return False

check(overlap(board1))

# taking care of truck and board1
# the truck does not cover any of board1
if (overlap(board1) == False):
    check("no overlap on x with board1")
    board1result = a1
else: # the truck intersects with board1
    board1result = a1 - myfunc(board1)

# taking care of truck and board2
# the truck does not cover any of board2
if (overlap(board2) == False):
    check("no overlap on x with board2")
    board2result = a2
else: # the truck intersects with board2
    board2result = a2 - myfunc(board2)

n = board1result + board2result
print(n)
