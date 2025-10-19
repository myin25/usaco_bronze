# utility function
def check(x):
    print(x)
    return

# open file input
myfile = open("whereami.in.py","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")

check(content)

# defining variable
validOrNot = True

numBoxes = int(content[0][0])
myBoxes = list(content[1][0])

check(numBoxes)
check(myBoxes)

# define function
def findLen():
    for i in range(1, numBoxes):
        # define myTemp because there will be list editing
        myTemp = myBoxes.copy()

        for j in range(numBoxes +1 - i):
            # defining variables
            validOrNot = True
            temp = myTemp[j:i + j]
            check("temp " + str(temp))
            check(myTemp[i + j:])
            check("")

            cutoff = myTemp[i:]

            # loop through whole list
            for n in range(len(cutoff) - j + 1):
                myStr = myBoxes[n : j + n + 1]

                check("myStr " + str(myStr))
                if myStr == temp:
                    check("dude gimme a break")
                    validOrNot = False
                    break

            if validOrNot == True:
                break
            
        if validOrNot == True:
            # return the input as a file
            f= open("whereami.out","w+")
            f.write('%d' % i)
            f.close()
            check(i)
            
            break

findLen()
