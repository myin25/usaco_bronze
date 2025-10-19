# utility function
def check(x):
    #print(x)
    return

# string creator function
def stringStitch(x):
    mystr = ""
    
    for i in range(len(x)*2 - 1):
        if i%2 == 0:
            mystr += x[i//2]
        else:
            mystr += " "
    return mystr
    
# open file input
myfile = open("word.in","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")

# define non input based variables
counter = 0
myTemp = []

# define variables from input
numWords = int(content[0][0])
lineLen = int(content[0][1])
essay = content[1]

check(numWords)
check(lineLen)
check(essay)

# main loop
f = open("word.out","w+")

for i in essay:
    counter += len(i)

    if counter > lineLen:
        myTemp = stringStitch(myTemp)

        f.write(myTemp + "\n")
        check(myTemp)
        
        myTemp = [i]
        counter = len(i)
    else:
        myTemp.append(i)

# check to see if end words are missed
f.write(stringStitch(myTemp))
check(stringStitch(myTemp))
f.close()
