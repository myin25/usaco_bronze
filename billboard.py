# utility function
def check(x):
    print(x)
    return

# take input
board1 = input().split(" ")
board2 = input().split(" ")
truck = input().split(" ")

for i in range(len(board1)):
    board1[i] = int(board1[i])
    board2[i] = int(board2[i])
    truck[i] = int(truck[i])

check(board1)
check(board2)
check(truck)

# find the areas of the two billboards
board1area = (board1[3] - board1[1])*(board1[2] - board1[0])
board2area = (board2[3] - board2[1])*(board2[2] - board2[0])
check(board1area)
check(board2area)

# find the area of overlap for billboards
# on the condition that the UR corner of the truck is inside of or above board1
if (truck[3] in range(board1[1], board1[3])) or (truck[2] in range(board1[0], board1[2])):

    # maybe the truck only covers board 1
    if (truck[3] < board1[3]) and (truck[2] < board1[2]):
        temp1 = (truck[3] - board1[1]) *(board1[2] - truck[0])
        check(temp1)

        temp2 = 0

    elif (truck[0] < board1[0]) and (truck[2] > board2[2]): # if the truck is longer than the two boards
        # if the truck splits the boards into 2 pieces
        if (truck[1] > board1[1]) and (truck[3] < board2[3]):
            temp1 = (board1[2] - board1[0])*(truck[3]-truck[1])
            temp2 = (board2[2] - board2[0])*(truck[3] - truck[1])
        else:
            temp1 = (board1[2] - board1[0])*(truck[3] - board1[1])
            temp2 = (board2[2] - board2[0])*(truck[3] - board2[1])
        
    elif (truck[0] in range(board1[0], board1[2])) and (truck[3] in range(board1[1], board1[3])): # if there is still overlap on board1 even though LL and UR corners aren't inside.
        temp1 = (board1[2] - truck[0])*(truck[3] - board1[1])
        temp2 = (truck[3] - truck[1])*(truck[2] - board2[0])
        check(" ")
        check(temp1)
        check(temp2)
    else:
        # solve for the overlap in board 1 first
        temp1 = (truck[3] - board1[1]) *(board1[2] - truck[0])
        check(temp1)

        # check for the overlap in board 2 next
        if (truck[1] > board2[1]) and (truck[3] < board2[3]): # if the truck is completely inside
            temp2 = (truck[2] - board2[0])*(truck[3] - truck[1])
            check(temp2)
        else:
            temp2 = (truck[2] - board2[0])*(truck[3] - board2[1])

    n = board1area + board2area - temp1 - temp2

else:
    # if the truck covers both boards
    if (truck[0] < board1[0]) and (truck[1] < board1[1]) and (truck[2] > board2[2]) and (truck[3] > board2[3]) and (truck[3] > board1[3]):
        n = 0
    elif (truck[0] < board1[0]) and (truck[1] < board1[1]) and (truck[2] > board1[2]) and (truck[3] > board1[3]): # in the case that board1 is covered completely
        n = board2area
    elif (truck[0] < board2[0]) and (truck[1] < board2[1]) and (truck[2] > board2[2]) and (truck[3] > board2[3]): # in the case that board2 is covered completely
        n = board1area
    else: # if there is no overlap at all
        n = board1area + board2area

print(n)
