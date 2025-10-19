# check function
def check(x):
    print(x)
    return

# create numberdict
mydict = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

# take input
mylist = list(input())
for i in range(len(mylist)):
    if mylist[i] not in mydict:
        mylist[i] = int(mylist[i])
    else:
        mylist[i] = mydict[mylist[i]]

# convert to binary
powersOf2 = [8, 4, 2, 1]
base2 = ""

for myTemp in mylist:
    mystr = ""
    for i in range(len(powersOf2)):
        mystr += str(myTemp//powersOf2[i])
        myTemp -= int(mystr[i])*powersOf2[i]
    base2 += mystr

base2 = str(int(base2))

mymatrix = []
# initialize matrix
if len(base2)%3 != 0:
    mymatrix.append(base2[:int(len(base2)%3)])

addby = len(base2)%3

for i in range(len(base2)//3):
    i += 1
    i *= 3
    check(str(i + addby) + " " + str(i - 3 + addby))
    mytemp = base2[i - 3 + addby:i + addby]
    mymatrix.append(mytemp)

# convert to base 8
final = ""
powersOf2 = [1, 2, 4]
for templist in mymatrix:
    templist = [int(x) for x in list(templist)]
    x = 0
    for i in range(len(templist)):
        x += int(powersOf2[len(templist) - i - 1]) * int(templist[i])
    final += str(x)
print(int(final))
