# take list
lst = input().split()
lst = [int(x) for x in lst]
myNumber = int(input())

# binary function
def binarysearch(myTarget):
    myIndex = -1
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right)//2

        # if statements
        if lst[middle] < myTarget:
            left = middle
        elif lst[middle] == myTarget:
            myIndex = middle
            break
        else:
            right = middle - 1

    return myIndex

print(binarysearch(myNumber))
