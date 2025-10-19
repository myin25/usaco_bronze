# utility function
def check(x):
    print(x)
    return

# define variables
n = 0 # n is the number that the user recieves at the end of the program
temp1 = 0 # the area of overlap between the truck and board1
temp2 = 0 # the area of overlap between the truck and board2

# take input
board1 = input().split(" ")
board2 = input().split(" ")
truck = input().split(" ")

# convert to integers
for i in range(len(board1)):
    board1[i] = int(board1[i])
    board2[i] = int(board2[i])
    truck[i] = int(truck[i])

# the truck does not cover anything
if (truck[0] not in range(board1[0], board2[2])) and (truck[2] not in range(board1[0], board2[2])):
    check("no overlap on x with board1")
    n = 0

elif (truck[1] not in range(board1[1], board2[3])) and (truck[3] not in range(board1[1], board2[3])):
    check("no overlap on y with board1")
    n = 0
    
else:
    # find the upper right corner of the overlap area of board1 and truck
    URx1 = min(board1[2], truck[2])
    URy1 = min(board1[3], truck[3])

    #check(overlapURx)
    #check(overlapURy)

    # find the lower left corner of the overlap area of board1 and truck
    LLx1 = max(board1[0], truck[0])
    LLy1 = max(board1[1], truck[1])

    #check(overlapLLx)
    #check(overlapLLy)

    temp1 = (URx1 - LLx1)*(URy1 - LLy1)

    check(temp1)
