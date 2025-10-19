# take input
mynum, base = input().split()
mynum = [int(x) for x in list(mynum[::-1])]
base = int(base)

# convert
final = 0
multiplyby = 1

for i in mynum:
    final += i*multiplyby
    multiplyby *= base

print(final)
