# take input
inputBase2 = [int(x) for x in list(input())]

# find the largest power of two
x = 1
for i in range(len(inputBase2) - 1):
    x *= 2

# translate
inputBase10 = 0
for i in inputBase2:
    inputBase10 += i*x
    x = x//2

# multiply by 17
inputBase10 *= 17

# translate to binary form
final = ""
while inputBase10 > 0:
    if inputBase10%2 == 0:
        final += "0"
    else:
        final += "1"
    inputBase10 //= 2

print(final[::-1])
