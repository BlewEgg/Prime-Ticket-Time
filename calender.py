
#Last updated : 11/30

def is_leap(yr):
    # CASE 1 ---- y is a mulitplie of 400
    # CASE 2 ---- y is a mulitple of 4 while not a mulit of 100 --- use and/or statement
    if yr % 400 == 0:
        return True
    elif yr % 4 == 0 and yr % 100 != 0:
        return True
    else:
        return False


# 2
def monthdays(yr, mon):
    Leap = is_leap(yr)
    if Leap == True:
        if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
            return 31
        elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
            return 30
        else:
            if mon == 2:
                return 29
    else:
        if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
            return 31
        elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
            return 30
        else:
            if mon == 2:
                return 28


# 3
def yeardays(yr):
    Leap = is_leap(yr)
    if Leap == True:
        return 366
    else:
        return 365


# 4


def wkday_on_first(yr, mon):  # returns day of week of first of month of the given year (1/1/2016)
    """
    This function takes the total amount of days using the yeardays(x) and monthdays() and then mod 7. Due to the fact
    that Jan 1754 began on a tuesday, Tuesday was chosen to be zero and so on.
    """
    TotalDays = 0
    for x in range(1754, yr):
        YearNum = yeardays(x)
        TotalDays += YearNum
    for x in range(1, mon):
        MonNum = monthdays(yr, x)
        TotalDays += MonNum
    WhatDayNum = TotalDays % 7
    WhatDay = ["Tues", "Wedn", "Thu", "Fri", "Sat", "Mon"]
    return WhatDay[WhatDayNum]


def print_calendar(yr, mon):
    if yr < 1754:
        return "The year inputted is less than 1754"
    else:
        WhatMon = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "Novemeber", "December"]
        WhatDay = ["Sun", "Mon", "Tues", "Wedn", "Thu", "Fri", "Sat"]
        start = wkday_on_first(yr, mon)
        start_index = WhatDay.index(start)
        MonNum = monthdays(yr, mon)

        test = ""
        #print(str(yr).center(20))
        test+=str(yr).center(20)+"\n"
        #print(str(WhatMon[mon - 1].center(20)))
        test +=str(WhatMon[mon - 1].center(20))+"\n"
        #print("Su Mo Tu We Th Fr Sa".center(20))
        dayStrings = "Su Mo Tu We Th Fr Sa".center(20)
        test += dayStrings+"\n"
        # This ForLoop will print out all the days into the calender with the consideration single/doubt digits
        for x in range(1, MonNum + 1):

            if (WhatDay.index(start) + x) % (7) == 0:  # Mod 7 will break up the rows
                if x == 1:  # Will add the necessary spaces so it will begin on the correct day
                    #print(start_index * "   ", end="")
                    test += start_index * "   "+ ""
                if x <= 9:
                    #print(" " + str(x), end='')
                    test += " " + str(x)+ ""
                    # Due to the fact single digits only use up one character, they have to be adjusted
                else:
                    #print(str(x) +   " ", end='')
                    test += str(x) +   " "+ ''

                #print(" ")  # Reset the row
                test += "\n"
            else:
                if x == 1:  # Will add the necessary spaces so it will begin on the correct day
                    #print(start_index * "   ", end="")
                    test += start_index * "   "+ ""
                if x <= 9:
                    #print(" " + str(x) + " ", end='')
                    test += " " + str(x) + " "+ ''

                else:
                    #print(str(x) + " ", end='')
                    test += str(x) + " "+''

        print("")
    return test