# utility function
def check(x):
    #print(x)
    return

# take input
numMonths = int(input())*12

# define "calendars" and startnum, which is 2(for monday)
startnum = 2
monthIndex = 0
daysOfWeek = [0, 0, 0, 0, 0, 0, 0]

nonLeap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# define function
def find13th(firstdayofmonth):
    thirteenth = (5 + firstdayofmonth)%7
    return thirteenth

# find the first day of the next month
def findFirst(firstdayofmonth, monthIndex, year):
    # check to see if it's a leap year
    if (year%4 == 0) and (year%100 != 0): # is leap year
        # reference the leap year calendar
        nextfirstday = firstdayofmonth + leap[monthIndex]%7

    else:
        if (year%400 == 0): # leap year as well
            nextfirstday = firstdayofmonth + leap[monthIndex]%7
        else:
            nextfirstday = firstdayofmonth + nonLeap[monthIndex]%7
    return nextfirstday

# driver code
for month in range(numMonths):
    # update list with most recent 13th
    daysOfWeek[find13th(startnum)] += 1
    check(daysOfWeek)

    # update starting day
    startnum = findFirst(startnum, month%12, month//12 + 1900)

print(daysOfWeek)
