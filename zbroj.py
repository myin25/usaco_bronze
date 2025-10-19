# take input, but keep as string
a, b = input().split()

# find the largest a and smallest a
a = list(a)
maxa = ""
mina = ""

for i in a:
    if (i != "5") and (i != "6"):
        maxa += i
        mina += i
    else:
        maxa += "6"
        mina += "5"

# find the largest and smallest b
maxb = ""
minb = ""

for i in b:
    if (i != "5") and (i != "6"):
        maxb += i
        minb += i
    else:
        maxb += "6"
        minb += "5"

maxTotal = int(maxb) + int(maxa)
minTotal = int(minb) + int(mina)

print(minTotal, maxTotal)
