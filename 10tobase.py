# take input
mynum, base = input().split()
mynum = int(mynum)
base = int(base)

# convert
final = ""
while mynum != 0:
    final += str(mynum%base)
    mynum //= base

print(final[::-1])
