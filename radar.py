# define variable
trueOrFalse = False
counter = 0

# utility function + palindrome function
def check(x):
    #print(x)
    return

def checkPalin(x):
    # variables
    x = list(str(x))
    #check(x)

    left = 0
    right = len(x) - 1

    for i in range(len(x)//2):
        if x[left] != x[right]:
            palinOrNot = False
            break
        else:
            palinOrNot = True
            left += 1
            right -= 1

    check("palinOrNot " + str(palinOrNot))
    
    return(palinOrNot)

# take input
originalNum = int(input())

# loop until palin == True
while trueOrFalse == False:
    # calling check and palin methods
    check(originalNum)
    trueOrFalse = checkPalin(originalNum)

    # update counter
    counter += 1

    # reverse originalnum
    reverseOriginalNum = int("".join(list(str(originalNum))[::-1]))
    originalNum += reverseOriginalNum

    if trueOrFalse == True:
        break

print(counter - 1, originalNum - reverseOriginalNum)
