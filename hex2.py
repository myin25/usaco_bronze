# take input
mylist = input()

# take care of exceptions
if mylist == "0":
    print(0)
else:
    x = bin(int(mylist, 16))

    n = oct(int(x, 2))
    print(n[2:])
