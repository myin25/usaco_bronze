# utility function
def check(x):
    #print(x)
    return

# take input
numItems, numQuestions = input().split()
numItems = int(numItems)
numQuestions = int(numQuestions)

myList = input().split()
for i in range(numItems):
    myList[i] = int(myList[i])

myQueries = []
for i in range(numQuestions):
    myQueries.append(int(input()))

from bisect import bisect_left
for item in myQueries:
    left = 0
    right = numItems - 1
    pos = bisect_left(myList, item, left, right)
    if myList[pos] != item:
        print(-1)
    else:
        print(pos)
