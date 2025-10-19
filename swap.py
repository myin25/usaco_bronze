# utility function
def check(x):
    #print(x)
    return

# open file input
myfile = open("swap.in","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")

check(content)

# define variables from input
numCows = int(content[0][0])
loopSize = int(content[0][1])
mystart1, stop1 = [int(x) for x in content[1]]
mystart2, stop2 = [int(x) for x in content[2]]

# create list
myList = [i for i in range(1, numCows + 1)]

# define 2 functions
def switch1(myList):
    start1 = mystart1 - 1
    templst = myList[:start1] + (myList[start1:stop1])[::-1] + myList[stop1:]
    check(templst)
    return templst

def switch2(myList):
    start2 = mystart2 - 1
    templst = myList[:start2] + (myList[start2:stop2])[::-1] + myList[stop2:]
    check(templst)
    return templstx

# main loop
x = myList

for i in range(loopSize):
    x = switch1(x)
    x = switch2(x)

# input to file
f = open("swap.out","w+")

for i in x:
    f.write(str(i) + "\n")
f.close()
