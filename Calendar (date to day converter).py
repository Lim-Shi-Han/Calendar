import math 

a = float(input("Day: "))

b = float(input("Month: "))

c = float(input("Year: "))

d = 3

"""YEAR"""

if c >= 2020: 
    daysApart = c - 2020
    leapYearsAfter = math.floor((daysApart + 3)/ 4)
    if leapYearsAfter >= 1:
        daysApart += leapYearsAfter
    if c > 2100:
        numberOf100Years = math.floor((c - 2001)/100)
        daysApart -= numberOf100Years 
    if c > 2400:
        numberOf400Years = math.floor((c - 2001)/400)
        daysApart += numberOf400Years
    
        

if c < 2020: 
    daysApart = 2020 - c
    leapYearsAfter = math.floor(daysApart / 4)
    if leapYearsAfter >= 1:
        daysApart += leapYearsAfter
    if c < 2001:
        numberOf100Years = math.floor((2100 - c)/100)
        daysApart -= numberOf100Years
    if c < 2001:
        numberOf400Years = math.floor((2400 - c)/400)
        daysApart += numberOf400Years
    daysApart = -daysApart
    
   
    
"""MONTH"""

if c%4 == 0:
    if c%400 == 0:
        list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthsApart = 12 - (b - 1)
        while monthsApart > 0:
            list.pop()
            monthsApart -= 1
    elif c%100 == 0:
        list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthsApart = 12 - (b - 1)
        while monthsApart > 0:
            list.pop()
            monthsApart -= 1
    elif c%100 != 0:
        list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthsApart = 12 - (b - 1)
        while monthsApart > 0:
            list.pop()
            monthsApart -= 1
elif c%4 != 0:
        list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthsApart = 12 - (b - 1)
        while monthsApart > 0:
            list.pop()
            monthsApart -= 1
        
daysApart += sum(list)

"""DAY"""

daysApart += (a - 1)

"""END"""

changeInDay = daysApart%7
d += changeInDay
if d > 7:
    d -= 7
list1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
e = int(d - 1)
print(list1[e])
       




