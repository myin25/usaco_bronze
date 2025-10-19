# open file input
myfile = open("swap.in","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")

# define variables from input
numCows = int(content[0][0])
loopSize = int(content[0][1])
start1, stop1 = [int(x) for x in content[1]]
start2, stop2 = [int(x) for x in content[2]]

start1 -= 1
start2 -= 1

# create list
myList = [i for i in range(1, numCows + 1)]

# define 2 functions
def switch(templst):
    templst[start1:stop1] = templst[start1:stop1][::-1]
    templst[start2:stop2] = templst[start2:stop2][::-1]
    return templst

# main loop
x = myList

for i in range(loopSize):
    x = switch(x)

# input to file
f = open("swap.out","w+")

for i in x:
    f.write(str(i) + "\n")
f.close()
