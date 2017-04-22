# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

def total_days(month,day,year):
    i = 0
    total = 0
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        daysOfMonths[1] = 29
    while i < month-1:
        total += daysOfMonths[i]
        i = i+1
    total += day
    return total
    
    
def total_year(year):
    i = 1900
    total = 0
    while i < year:
        if is_leap_year(i):
            total += 366 
        else: 
            total += 365
        i = i+1
    return total
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    return total_year(year2)-total_year(year1)+total_days(month2,day2,year2)-total_days(month1,day1,year1)


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
