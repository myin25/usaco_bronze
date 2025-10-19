# utility function
def check(x):
    #print(x)
    return

# take input
numNotes, numQuestions = input().split()
numNotes = int(numNotes)
numQuestions = int(numQuestions)

# format the song
mySong = []
for i in range(numNotes):
    numOfNote = int(input())
    for j in range(numOfNote):
        mySong.append(i + 1)
check("mySong "  + str(mySong))

# take the questions
myQuestions = []
for i in range(numQuestions):
    print(mySong(int(input()))
    myQuestions.append(int(input()))

# finding the positions of the questions
for i in myQuestions:
    print(mySong[i])

