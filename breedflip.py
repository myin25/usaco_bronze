# utility function
def check(x):
    #print(x)
    return

# open file input
myfile = open("breedflip.in","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")

check(content)

# define variables
numCows = int(content[0][0])
wantedCows = list(content[1][0])
actualCows = list(content[2][0])

check(wantedCows)
check(actualCows)

# toggle by looping through
i = 0
counter = 0
beforeEqual = True

while wantedCows != actualCows:
    check(i)
    if (wantedCows[i] != actualCows[i]):
        if beforeEqual == True:
            counter += 1
        actualCows[i] = wantedCows[i]
        beforeEqual = False
    else:
        beforeEqual = True
    i += 1

f= open("breedflip.out","w+")
f.write('%d' % counter)
f.close()
check(counter)
