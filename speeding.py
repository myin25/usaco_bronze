# utility function
def check(x):
    print(x)
    return

# take input
speedSegments, bessieSegments = [int(x) for x in input().split()]
roadLimit = []
bessiePattern = []

# create roadLimit
for i in range(speedSegments):
    segmentlen, speedlimit = [int(x) for x in input().split()]
    roadLimit.extend([speedlimit for i in range(segmentlen)])

# create bessiePattern
for i in range(bessieSegments):
    segmentlen, speedlimit = [int(x) for x in input().split()]
    bessiePattern.extend([speedlimit for i in range(segmentlen)])

# compare
largestDiff = 0
for i in range(100):
    if bessiePattern[i] > roadLimit[i]:
        x = bessiePattern[i] - roadLimit[i]
        if x > largestDiff:
            largestDiff = x
print(largestDiff)
