# utility function
def check(x):
    #print(x)
    return

# take input
numNotes, numQuestions = input().split()
numNotes = int(numNotes)
numQuestions = int(numQuestions)

# format the song
startpoint = 0
mySong = []
for i in range(numNotes):
    numOfNote = int(input())
    mySong.append(startpoint)
    startpoint += numOfNote

check("mySong "  + str(mySong))

# binarysearch function
from bisect import bisect_right
def binarysearch(num):
    pos = bisect_right(mySong, num, 0, numNotes)
    return pos
    
# take the questions
for myQuery in range(numQuestions):
    # take input
    myQuery = int(input())
    print(binarysearch(myQuery))
