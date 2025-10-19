# utility function
def check(x):
    #print(x)
    return

# open file input
myfile = open("race.in","r")

content = myfile.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    content[i] = content[i].split(" ")

check(content)

# structure the input
raceLen = int(content[0][0])
numSpeed = int(content[0][1])
endValue = []

for i in range(numSpeed):
    endValue.append(int(content[i + 1][0]))

check(endValue)

# define function, this is for if the endspeed is equal to one
def endIsOne():
    myTemp = raceLen
    counter = 0
    currentspeed = 1
    
    while myTemp >= 0:
        myTemp -= currentspeed*2
        counter += 2
        currentspeed += 1

    return(counter)

# define a function, this is for if the endspeed is larger than one
def moreThanOne(endspeed):
    myTemp = raceLen
    counter = 0
    currentspeed = 1

    while currentspeed < endspeed:
        myTemp -= currentspeed
        counter += 1
        currentspeed += 1
        check(currentspeed)

        if myTemp <= 0:
            return counter

    if myTemp < currentspeed:
        counter += 1
    elif myTemp == currentspeed:
        counter += 1
    else: # if there is still more of the race left
        while myTemp >= 0:
            if myTemp > (currentspeed + 1)*2:
                myTemp -= (currentspeed + 1)*2

                counter += 2
            elif myTemp > (currentspeed)*2:
                myTemp -= currentspeed*2

                counter += 2
            else:
                myTemp -= currentspeed

                counter += 1

            if currentspeed < endspeed:
                currentspeed += 1
                
            check(currentspeed)
    return counter

#check(moreThanOne(2))

f = open("race.out", "w+")


for i in endValue:
    #check(i)
    if i == 1:
        myTemp = endIsOne()
    else:
        myTemp = moreThanOne(i)

    check(myTemp)
    f.write(str(myTemp) + "\n")

f.close()
