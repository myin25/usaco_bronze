# utility function
def check(x):
    print(x)
    return

# open file input
myfile = open("triangles.in","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")

check(content)

# split the input
numPosts = int(content[0][0])

myCoords = []

for i in range(1, numPosts + 1):
    myCoords.append(int(content[i][0]), int(content[i][1]))

# bash out x
left = 1

for i in myCoords:
    myx, myy = i

    for j in myCoords[1:]:
        myx2, myy2 = j
        if myx == myx2:
            height = abs(myy - myy2)
        else:
            if myy == myy2:
                base = abs(my
