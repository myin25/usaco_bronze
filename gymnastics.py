# I used this website to learn how to handle a file in python: https://www.guru99.com/reading-and-writing-files-in-python.html

# define variable
temp = 0
tempList = []
consistent = True
counter = 0
leftmost = 2

# utility function
def check(x):
    #print(x)
    return


# open file input
myfile = open("gymnastics.in","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")

# create master list
fileinput = [int(content[0][0]), int(content[0][1])]
for row in range(int(content[0][0])):
    for col in range(int(content[0][1])):
        fileinput.append(int(content[row + 1][col]))


# defining numrow and numcol
numrow, numcol = fileinput[0], fileinput[1]
numrow = int(numrow)
numcol = int(numcol)

fileinput.pop(0)
fileinput.pop(0)

# initialize mymatrix as an empty matrix
myMatrix = [[] for i in range(numrow)]

# updating myMatrix with the input
for i in range(numrow):
    # define the main list, which is going to be the main reference point 
    userList = fileinput[leftmost : leftmost + numcol:]
    leftmost += numcol

    for j in range(numcol):
        myMatrix[i].append(int(fileinput[0]))
        fileinput.pop(0)

# main loop
originalLineup = myMatrix[0]

for i in range(len(originalLineup) - 1):
    # updating variables
    num1 = originalLineup[i]
    num2Options = originalLineup[i + 1::]

    # debug section

    for num2 in num2Options:
        # reset consistency
        consistent = True
        
        # checking to see if all cases are true
        for i in range(numrow):
            myTemp = myMatrix[i]

            if myTemp.index(num1) > myTemp.index(num2):
                consistent = False
        if consistent == True:
            counter += 1

# we have to return the input as a file form, so do it here
f= open("gymnastics.out","w+")
f.write('%d' % counter)
f.close()

check(counter)
