# take input
numShips = int(input())
myLog = []
for i in range(numShips):
    myLog.append(int(input()))

# create intervals
divisible = False
myIntervals = []
element1 = myLog[0]

for j in range(1, numShips):
    x = myLog[j] - element1
    for k in myIntervals:
        if x%k == 0:
            divisible = True
            break
    if divisible == False:
        myIntervals.append(x)
    else: # reset variable
        divisible = False

print(len(myIntervals))
